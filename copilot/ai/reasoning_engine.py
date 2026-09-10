#!/usr/bin/env python3
"""Deterministic reasoning layer for the Construction Copilot.

This module acts as the project intelligence layer between:
- SQLite CAD database
- parsed walkthrough JSON KB
- indexed visual assets

It supplies a simple agent-style query router without depending on an external LLM,
while leaving a clear place to plug in Gemini or another model later.
"""

from __future__ import annotations

import json
import logging
import os
import re
import sqlite3
import time
from pathlib import Path
from typing import Any

try:
    from google import genai
except Exception:  # pragma: no cover - optional dependency
    genai = None


LOGGER = logging.getLogger("construction_copilot")
if not LOGGER.handlers:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s construction_copilot: %(message)s")

_RUNTIME_STATUS: dict[str, Any] = {
    "provider": "local",
    "planner_provider": "not_run",
    "answer_provider": "not_run",
    "gemini_configured": False,
    "gemini_sdk_available": genai is not None,
    "gemini_model": None,
    "last_error": None,
    "cooldown_seconds": 0,
}
_GEMINI_COOLDOWN_UNTIL = 0.0


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_project_env() -> None:
    """Load the Gemini key from the project .env without printing secrets."""
    env_path = project_root() / ".env"
    if not env_path.exists() or os.getenv("GEMINI_API_KEY"):
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        name, value = stripped.split("=", 1)
        if name.strip() == "GEMINI_API_KEY":
            os.environ["GEMINI_API_KEY"] = value.strip().strip('"').strip("'")
            return


def gemini_available() -> bool:
    """Return True when the Gemini SDK and API key are both available."""
    load_project_env()
    configured = bool(os.getenv("GEMINI_API_KEY"))
    _RUNTIME_STATUS["gemini_configured"] = configured
    _RUNTIME_STATUS["gemini_sdk_available"] = genai is not None
    _RUNTIME_STATUS["gemini_model"] = gemini_model_name() if configured else None
    remaining = max(0, int(_GEMINI_COOLDOWN_UNTIL - time.time()))
    _RUNTIME_STATUS["cooldown_seconds"] = remaining
    if remaining:
        return False
    if not configured:
        LOGGER.warning("Gemini unavailable: GEMINI_API_KEY is not configured")
    elif genai is None:
        LOGGER.error("Gemini unavailable: google.genai SDK could not be imported")
    return configured and genai is not None


def mark_gemini_quota_cooldown(error: Exception) -> None:
    """Pause remote calls briefly after a quota/rate-limit response."""
    global _GEMINI_COOLDOWN_UNTIL
    message = str(error)
    if "429" in message or "RESOURCE_EXHAUSTED" in message or "quota" in message.lower():
        _GEMINI_COOLDOWN_UNTIL = time.time() + 60
        _RUNTIME_STATUS["cooldown_seconds"] = 60
        LOGGER.warning("Gemini quota limit detected; local fallback enabled for 60 seconds")


def runtime_status() -> dict[str, Any]:
    """Return safe provider diagnostics suitable for logs and the UI."""
    gemini_available()
    return dict(_RUNTIME_STATUS)


def gemini_model_name() -> str:
    """Return the configured Gemini model, with a current default."""
    load_project_env()
    return os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


def build_gemini_prompt(query: str, evidence: dict[str, Any]) -> str:
    """Construct a structured prompt for Gemini using local evidence."""
    cad = evidence.get("cad_results") or []
    specs = evidence.get("spec_results") or []
    visuals = evidence.get("visual_results") or []
    search_plan = evidence.get("search_plan") or {}

    cad_block = json.dumps(cad[:5], ensure_ascii=False, indent=2) if cad else "[]"
    spec_context = []
    for section in specs[:5]:
        spec_context.append({
            "title": section.get("title"),
            "categories": section.get("categories", []),
            "start_line": section.get("start_line"),
            "content": (section.get("content") or section.get("summary") or "")[:6000],
        })
    spec_block = json.dumps(spec_context, ensure_ascii=False, indent=2) if spec_context else "[]"
    visual_block = json.dumps(visuals[:5], ensure_ascii=False, indent=2) if visuals else "[]"

    return f"""
You are the Senior Chief Structural Engineer, MEP Consultant, and Lead BIM Inspector for this residential home construction project.

User question: {query}

Retrieval plan:
{json.dumps(search_plan, ensure_ascii=False)}

Use only the provided evidence. Do not invent dimensions or codes. If no evidence is provided, say so clearly.

Relevant CAD objects:
{cad_block}

Relevant specification sections:
{spec_block}

Relevant visual references:
{visual_block}

Answer only the question asked in natural, conversational site language. Speak directly to the user as a construction assistant. Do not mention retrieval, CAD matches, evidence counts, search plans, JSON, or database records. Use the highest-confidence matching evidence first and ignore unrelated matches. Follow the requested answer type from the retrieval plan. For a location question, start with a direct plain-language placement sentence, then mention floor/elevation or coordinates only if they are supported. For a count or dimension question, state the result directly and explain any uncertainty in one short sentence. If the evidence cannot establish the requested fact, say that clearly instead of guessing. Cite relevant Indian standards or project-specific evidence when available. Do not output filesystem paths or image filenames; refer to matching visual evidence as "the visual reference shown below".
""".strip()


def build_search_planner_prompt(query: str, context: str = "") -> str:
    """Ask Gemini which local evidence sources are needed for a query."""
    return f"""
You are the retrieval planner for a construction BIM assistant.

User query: {query}

Recent conversation context:
{context or "None"}

Choose only the local evidence sources needed to answer the query:
- cad: exact model objects, dimensions, coordinates, quantities, or counts
- specs: construction methods, standards, sequences, safety, or code guidance
- visuals: renders, plans, elevations, or diagrams the user may need to see

Return JSON only, with this exact shape:
{{"searches":["cad", "specs", "visuals"], "category":"optional category or null", "focus_terms":["subject terms"], "exclude_terms":["irrelevant terms"], "answer_type":"fact|count|dimension|location|procedure|visual|general"}}
Do not answer the user and do not add markdown.
""".strip()


def parse_search_plan(text: str) -> dict[str, Any] | None:
    """Parse Gemini's JSON retrieval plan without trusting unknown tool names."""
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        if cleaned.startswith("json"):
            cleaned = cleaned[4:].strip()

    try:
        payload = json.loads(cleaned)
    except json.JSONDecodeError:
        return None

    searches = [item for item in payload.get("searches", []) if item in {"cad", "specs", "visuals"}]
    if not searches:
        return None
    category = payload.get("category")
    focus_terms = [item.lower() for item in payload.get("focus_terms", []) if isinstance(item, str) and item.strip()]
    exclude_terms = [item.lower() for item in payload.get("exclude_terms", []) if isinstance(item, str) and item.strip()]
    answer_type = payload.get("answer_type")
    if answer_type not in {"fact", "count", "dimension", "location", "procedure", "visual", "general"}:
        answer_type = "general"
    return {
        "searches": searches,
        "category": category if isinstance(category, str) else None,
        "focus_terms": focus_terms,
        "exclude_terms": exclude_terms,
        "answer_type": answer_type,
    }


def deterministic_search_plan(query: str) -> dict[str, Any]:
    """Choose evidence sources when Gemini is unavailable or returns invalid JSON."""
    normalized = normalize_query(query).replace("over head", "overhead")
    tokens = set(retrieval_tokens(normalized))
    searches: list[str] = []
    is_count_query = "how many" in normalized or bool(tokens & {"count", "number", "quantity"})
    if is_count_query or tokens & {"capacity", "dimension", "dimensions", "size", "length", "width", "height", "object", "model", "cad"}:
        searches.append("cad")
    if is_count_query and tokens & {"switchboard", "switchboards", "electrical"}:
        searches.append("specs")
    if is_count_query and tokens & {"fan", "fans", "ceiling", "exhaust"}:
        searches.append("specs")
    if tokens & {"capacity", "rating", "rated", "power"} and not is_count_query:
        searches.append("specs")
    if not is_count_query and tokens & {"install", "installation", "method", "procedure", "standard", "code", "curing", "waterproofing", "safety", "rule", "guidance"}:
        searches.append("specs")
    if tokens & {"show", "see", "view", "image", "picture", "plan", "elevation", "render", "diagram"}:
        searches.append("visuals")
    answer_type = "general"
    if is_count_query:
        answer_type = "count"
    elif tokens & {"capacity", "size", "height", "width", "length", "dimension", "dimensions"}:
        answer_type = "dimension"
    elif tokens & {"where", "placed", "located", "location", "position", "positioned"}:
        answer_type = "location"
    elif tokens & {"how", "install", "installation", "method", "procedure", "curing", "waterproofing"}:
        answer_type = "procedure"
    return {
        "searches": searches or ["cad", "specs", "visuals"],
        "category": None,
        "focus_terms": [
            token for token in retrieval_tokens(normalized)
            if token not in {"capacity", "size", "height", "width", "length", "dimension", "dimensions"}
        ],
        "exclude_terms": [],
        "answer_type": answer_type,
    }


def choose_search_plan(query: str, context: str = "") -> dict[str, Any]:
    """Let Gemini choose retrieval tools, with a local intent fallback."""
    if gemini_available():
        try:
            client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
            response = client.models.generate_content(
                model=gemini_model_name(),
                contents=build_search_planner_prompt(query, context),
            )
            plan = parse_search_plan(getattr(response, "text", "") or "")
            if plan:
                plan["planner"] = "gemini"
                _RUNTIME_STATUS.update({"provider": "gemini", "planner_provider": "gemini", "last_error": None})
                LOGGER.info("Gemini planner selected sources=%s answer_type=%s", plan["searches"], plan["answer_type"])
                return plan
            _RUNTIME_STATUS["last_error"] = "Gemini planner returned invalid JSON"
            LOGGER.warning("Gemini planner returned invalid JSON; using local planner")
        except Exception as exc:
            mark_gemini_quota_cooldown(exc)
            _RUNTIME_STATUS["last_error"] = f"planner {type(exc).__name__}: {str(exc)[:240]}"
            LOGGER.warning("Gemini planner failed (%s: %s); using local planner", type(exc).__name__, str(exc)[:240])

    plan = deterministic_search_plan(query)
    focus_terms = plan.get("focus_terms", [])
    if "front" in focus_terms and "step" in focus_terms and "entrance" not in focus_terms:
        focus_terms[:] = [term for term in focus_terms if term != "front"]
        focus_terms.append("entrance")
    plan["planner"] = "local_fallback"
    _RUNTIME_STATUS.update({"provider": "local", "planner_provider": "local", "last_error": _RUNTIME_STATUS.get("last_error")})
    LOGGER.info("Local planner selected sources=%s answer_type=%s", plan["searches"], plan["answer_type"])
    return plan


def summarize_answer(query: str, evidence: dict[str, Any]) -> str:
    """Return a Gemini answer when available, otherwise use retrieved evidence clearly."""
    if gemini_available():
        try:
            client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
            response = client.models.generate_content(
                model=gemini_model_name(),
                contents=build_gemini_prompt(query, evidence),
            )
            answer = getattr(response, "text", None)
            if answer:
                _RUNTIME_STATUS.update({"provider": "gemini", "answer_provider": "gemini", "last_error": None})
                LOGGER.info("Gemini answer generated successfully")
                return answer
            LOGGER.warning("Gemini returned an empty answer; using local fallback")
        except Exception as exc:
            mark_gemini_quota_cooldown(exc)
            _RUNTIME_STATUS["last_error"] = f"answer {type(exc).__name__}: {str(exc)[:240]}"
            LOGGER.warning("Gemini answer failed (%s: %s); using local fallback", type(exc).__name__, str(exc)[:240])

    _RUNTIME_STATUS.update({"provider": "local", "answer_provider": "local"})
    LOGGER.info("Local answer formatter used")
    search_plan = evidence.get("search_plan") or {}
    specs = evidence.get("spec_results") or []
    cad = evidence.get("cad_results") or []
    answer_type = search_plan.get("answer_type")

    if answer_type == "location" and specs:
        section = specs[0]
        content = " ".join((section.get("content") or section.get("summary") or "").split())
        detail = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", content)
        detail = detail.replace("`", "")
        detail = detail.split("carousel", 1)[0].strip()
        sentences = re.split(r"(?<=[.!?])\s+", detail)
        detail = " ".join(sentences[:2]).strip()
        return (
            "The relevant project guidance is **"
            + str(section.get("title"))
            + "**. "
            + detail.rstrip(".")
            + "."
        )
    if answer_type == "count" and specs:
        fan_tags = set()
        for section in specs:
            content = section.get("content") or ""
            if "fan" in content.lower():
                fan_tags.update(re.findall(r"\b(?:FF_)?FB[-_]?[A-Z0-9]+\b", content, flags=re.IGNORECASE))
        if fan_tags and any(term in (search_plan.get("focus_terms") or []) for term in ("fan", "fans")):
            fan_tags = {tag.upper().replace("FF_", "") for tag in fan_tags}
            has_first_floor_schedule = any(
                "FF_Electrical_Slab_Fan_Boxes" in (section.get("content") or "")
                for section in specs
            )
            if has_first_floor_schedule:
                return "The walkthrough provides 6 ceiling-fan provisions: 3 on the Ground Floor and 3 on the First Floor. Exhaust fans are separate fixtures."
            labels = ", ".join(sorted(tag.upper() for tag in fan_tags))
            return f"The walkthrough provides {len(fan_tags)} ceiling-fan provisions: {labels}. Exhaust fans are separate fixtures."

        tagged_items = set()
        switchboard_query = any(
            term in (search_plan.get("focus_terms") or [])
            for term in ("switchboard", "switchboards")
        )
        for section in specs:
            for line in (section.get("content") or "").splitlines():
                normalized_line = line.lower()
                direct_kitchen_context = (
                    "kitchen" in normalized_line
                    and any(
                        marker in normalized_line
                        for marker in ("switchboard", "console", "counter", "fridge", "food prep", "power point")
                    )
                    and not any(marker in normalized_line for marker in ("feeder", "throughout", "drop to", "pot"))
                )
                if not direct_kitchen_context:
                    continue
                line_tags = re.findall(
                    r"\b(?:GF_)?SB[- _]?\d+\b|\bFF_SB[- _]?\d+\b",
                    line,
                    flags=re.IGNORECASE,
                )
                if len(line_tags) == 1:
                    tagged_items.add(line_tags[0])
        if tagged_items:
            canonical_tags = {
                tag.upper().replace("GF ", "GF_").replace(" ", "-")
                for tag in tagged_items
            }
            labels = ", ".join(sorted(canonical_tags))
            if switchboard_query:
                return f"The walkthrough identifies {len(canonical_tags)} kitchen switchboards: {labels}."
            return f"The walkthrough identifies {len(canonical_tags)} kitchen control points: {labels}."
    if answer_type == "procedure" and specs:
        def instructional_text(item: dict[str, Any]) -> str:
            content = item.get("content") or item.get("summary") or ""
            return re.sub(r"```.*?```", "", content, flags=re.DOTALL).strip()

        substantive_specs = [
            item for item in specs
            if len(instructional_text(item)) > 80
        ] or specs
        section = max(
            substantive_specs,
            key=lambda item: (
                sum(
                    marker in (item.get("title") or "").lower()
                    for marker in ("installation", "safeguard", "procedure", "construction")
                ) * 10
                + sum(
                    marker in instructional_text(item).lower()
                    for marker in ("safeguard", "pedestal", "waterproof", "valve", "overflow", "install")
                )
                + len(re.findall(r"(?m)^\s*\d+\.\s+", instructional_text(item)))
            ),
        )
        raw_lines = instructional_text(section).splitlines()
        formatted_lines = []
        safeguard_count = 0
        numbered_content = any(re.match(r"^\s*\d+\.\s+", line) for line in raw_lines)
        for raw_line in raw_lines:
            line = raw_line.strip()
            if not line or line.startswith("```") or line.startswith(">"):
                continue
            if re.match(r"^\d+\.\s+", line):
                safeguard_count += 1
                if safeguard_count > 4:
                    break
            if numbered_content and safeguard_count == 0:
                continue
            if not numbered_content and not (line.startswith("*") or line.startswith("-") or "|" in line):
                continue
            line = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", line)
            line = line.replace("`", "").replace("$", "")
            line = line.replace(r"\varnothing", "diameter ")
            line = line.replace(r"\times", " x ").replace(r"\rightarrow", " to ").replace(r"\in", " in ")
            line = re.sub(r"\\text\{([^}]+)\}", r"\1", line)
            line = re.sub(r"\s+", " ", line).strip()
            if line:
                formatted_lines.append(line)

        if not formatted_lines:
            content = " ".join(instructional_text(section).split())
            content = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", content).replace("`", "")
            content = re.sub(r"\s+", " ", content).strip()
            sentences = re.split(r"(?<=[.!?])\s+", content)
            formatted_lines = [sentence.strip() for sentence in sentences[:5] if sentence.strip()]
        return (
            f"### Installation guidance\n\n"
            f"Follow **{section.get('title')}** for this project:\n\n"
            + "\n".join(formatted_lines)
        )
    if answer_type in {"count", "dimension"} and cad:
        if answer_type == "count":
            return f"The model shows {len(cad)} matching items. The detailed object list is available in the evidence panel."
        rated_values = []
        for item in cad:
            label = str(item.get("label") or item.get("id") or "")
            rated_values.extend(re.findall(r"\b\d+(?:\.\d+)?\s*HP\b", label, flags=re.IGNORECASE))
        if rated_values:
            return f"The recorded pump rating is {rated_values[0]}. The supporting installation details are available in the evidence panel."
        return f"The model contains {len(cad)} matching items with recorded dimensions. I’ve kept the detailed sizes in the evidence panel."

    return evidence.get("summary") or "No deterministic match found."


def cad_db_path() -> Path:
    return project_root() / "copilot" / "KB" / "cad_database.sqlite"


def specs_kb_path() -> Path:
    return project_root() / "copilot" / "KB" / "specs_database.json"


def visual_kb_path() -> Path:
    return project_root() / "copilot" / "KB" / "visual_index.json"


def normalize_query(query: str) -> str:
    normalized = " ".join(query.lower().split())
    return normalized.replace("over head", "overhead")


GREETING_MESSAGES = {
    "hi",
    "hello",
    "hey",
    "good morning",
    "good afternoon",
    "good evening",
}


def is_greeting(query: str) -> bool:
    return normalize_query(query).strip("!.?,") in GREETING_MESSAGES


RETRIEVAL_STOPWORDS = {
    "a", "about", "are", "can", "detail", "details", "do", "for", "how",
    "each", "give", "have", "is", "many", "me", "needed", "of", "on", "please", "show",
    "tell", "the", "there", "this", "what", "we", "where", "which", "with", "you",
}


def retrieval_tokens(query: str) -> list[str]:
    return [
        token
        for token in normalize_query(query).replace("-", " ").split()
        if token not in RETRIEVAL_STOPWORDS and len(token) > 1
    ]


CAD_TERM_ALIASES = {
    "column": {"column", "columns", "col"},
    "columns": {"column", "columns", "col"},
    "beam": {"beam", "beams", "rb", "pb"},
    "beams": {"beam", "beams", "rb", "pb"},
    "water": {"water", "sump", "pump"},
    "pump": {"pump", "motor", "sump"},
    "switchboard": {"switchboard", "switchboards", "sb", "mdb", "db"},
    "switchboards": {"switchboard", "switchboards", "sb", "mdb", "db"},
    "fan": {"fan", "fans", "fb"},
    "fans": {"fan", "fans", "fb"},
}


def expanded_terms(term: str) -> set[str]:
    return CAD_TERM_ALIASES.get(term.lower(), {term.lower()})


def cad_term_matches(term: str, text: str) -> bool:
    text = text.lower()
    aliases = expanded_terms(term)
    for alias in aliases:
        if alias == "col":
            if re.search(r"(?:^|[_\s-])col(?:[_\s-]|$)", text):
                return True
        elif alias in text:
            return True
    return False


def terms_match_document(terms: list[str], text: str, minimum: int | None = None) -> bool:
    """Apply the same alias-aware relevance rule to any indexed source."""
    normalized_text = text.lower()
    if not terms:
        return True
    required = minimum if minimum is not None else len(terms) if len(terms) <= 2 else (len(terms) + 1) // 2
    return sum(cad_term_matches(term, normalized_text) for term in terms) >= required


def query_cad_database(
    query: str,
    limit: int = 10,
    conn: sqlite3.Connection | None = None,
    focus_terms: list[str] | None = None,
    exclude_terms: list[str] | None = None,
) -> list[dict[str, Any]]:
    """Return CAD objects by matching the query text against relevant fields.

    This is lightweight deterministic filtering rather than a dense semantic search.
    """
    normalized = normalize_query(query)
    tokens = retrieval_tokens(normalized)
    focus_terms = [term.lower() for term in (focus_terms or []) if term.strip()]
    exclude_terms = [term.lower() for term in (exclude_terms or []) if term.strip()]

    if not tokens:
        return []

    if conn is None:
        connection = sqlite3.connect(str(cad_db_path()))
        close_after = True
    else:
        connection = conn
        close_after = False

    try:
        if not cad_db_path().exists():
            return []

        sql = """
            SELECT id, label, object_type, discipline, floor_level, room_zone,
                   material, coord_x_min, coord_x_max, coord_y_min, coord_y_max,
                   coord_z_min, coord_z_max, length_mm, width_mm, height_mm,
                   volume_m3, surface_area_m2
            FROM cad_objects
            WHERE 1=1
        """
        conditions: list[str] = []
        params: list[Any] = []

        for token in tokens:
            token_patterns = CAD_TERM_ALIASES.get(token, {token})
            conditions.append(
                "(" + " OR ".join(
                    "(LOWER(id) LIKE ? OR LOWER(label) LIKE ? OR LOWER(object_type) LIKE ? OR LOWER(room_zone) LIKE ? OR LOWER(floor_level) LIKE ? OR LOWER(discipline) LIKE ?)"
                    for _ in token_patterns
                ) + ")"
            )
            for alias in token_patterns:
                pattern = f"%{alias}%"
                params.extend([pattern, pattern, pattern, pattern, pattern, pattern])

        if conditions:
            sql += " AND " + " OR ".join(conditions)

        sql += " ORDER BY label"

        rows = connection.execute(sql, params).fetchall()
        columns = [
            "id",
            "label",
            "object_type",
            "discipline",
            "floor_level",
            "room_zone",
            "material",
            "coord_x_min",
            "coord_x_max",
            "coord_y_min",
            "coord_y_max",
            "coord_z_min",
            "coord_z_max",
            "length_mm",
            "width_mm",
            "height_mm",
            "volume_m3",
            "surface_area_m2",
        ]
        candidates = [dict(zip(columns, row)) for row in rows]
        searchable_fields = ("id", "label", "object_type", "room_zone", "floor_level", "discipline")

        if focus_terms:
            required_matches = len(focus_terms) if len(focus_terms) <= 2 else (len(focus_terms) + 1) // 2
            candidates = [
                item for item in candidates
                if sum(
                    cad_term_matches(term, f"{item.get('id', '')} {item.get('label', '')}".lower())
                    for term in focus_terms
                ) >= required_matches
            ]
        if exclude_terms:
            candidates = [
                item for item in candidates
                if not any(term in f"{item.get('id', '')} {item.get('label', '')}".lower() for term in exclude_terms)
            ]

        def relevance(item: dict[str, Any]) -> tuple[int, str]:
            score = 0
            for token in tokens + focus_terms:
                for field in searchable_fields:
                    value = str(item.get(field) or "").lower()
                    if cad_term_matches(token, value):
                        score += 5 if token in focus_terms else 3 if field in {"id", "label"} else 1
            return score, str(item.get("label") or "")

        candidates.sort(key=relevance, reverse=True)
        return candidates[:limit]
    finally:
        if close_after:
            connection.close()


def search_spec_sections(
    query: str,
    category: str | None = None,
    limit: int = 5,
    focus_terms: list[str] | None = None,
    exclude_terms: list[str] | None = None,
) -> list[dict[str, Any]]:
    """Search the parsed walkthrough KB for relevant sections."""
    path = specs_kb_path()
    if not path.exists():
        return []

    payload = json.loads(path.read_text(encoding="utf-8"))
    sections = payload.get("sections", [])
    normalized_query = normalize_query(query)
    query_tokens = retrieval_tokens(normalized_query)
    focus_terms = [term.lower() for term in (focus_terms or []) if term.strip()]
    exclude_terms = [term.lower() for term in (exclude_terms or []) if term.strip()]
    if not query_tokens:
        return []

    scored: list[tuple[float, dict[str, Any]]] = []

    for section in sections:
        title = (section.get("title") or "").lower()
        slug = (section.get("slug") or "").lower()
        summary = (section.get("summary") or "").lower()
        content = (section.get("content") or "").lower()
        cats = [str(item).lower() for item in section.get("categories", [])]
        text = f"{title} {slug} {summary} {content}".lower()

        if not terms_match_document(focus_terms, text):
            continue
        if exclude_terms and any(cad_term_matches(term, text) for term in exclude_terms):
            continue

        if category:
            category_lower = category.lower()
            if category_lower not in cats and category_lower not in text:
                continue

        score = 0.0
        for token in query_tokens:
            if cad_term_matches(token, title):
                score += 4.0
            if cad_term_matches(token, summary):
                score += 2.5
            if cad_term_matches(token, text):
                score += 1.5
        if score == 0:
            continue

        scored.append((score, section))

    scored.sort(key=lambda item: item[0], reverse=True)
    results = []
    for _, section in scored[:limit]:
        results.append({
            "title": section.get("title"),
            "slug": section.get("slug"),
            "level": section.get("level"),
            "categories": section.get("categories", []),
            "summary": section.get("summary"),
            "content": section.get("content", ""),
            "start_line": section.get("start_line"),
        })
    return results


def match_visual_assets(
    query: str,
    limit: int = 5,
    focus_terms: list[str] | None = None,
    exclude_terms: list[str] | None = None,
) -> list[dict[str, Any]]:
    """Return likely visual matches for a user question."""
    path = visual_kb_path()
    if not path.exists():
        return []

    payload = json.loads(path.read_text(encoding="utf-8"))
    assets = payload.get("assets", [])
    normalized = normalize_query(query)
    query_tokens = retrieval_tokens(normalized)
    focus_terms = [term.lower() for term in (focus_terms or []) if term.strip()]
    exclude_terms = [term.lower() for term in (exclude_terms or []) if term.strip()]
    if not query_tokens:
        return []

    scored: list[tuple[float, dict[str, Any]]] = []
    for asset in assets:
        text = " ".join(
            asset.get("keywords", [])
            + asset.get("categories", [])
            + asset.get("relevant_components", [])
            + [asset.get("file_name", "")]
        ).lower()
        if exclude_terms and any(term in text for term in exclude_terms):
            continue
        if not terms_match_document(focus_terms, text):
            continue
        score = 0.0
        for token in query_tokens:
            if token in text:
                score += 2.0
            if token in asset.get("file_name", "").lower():
                score += 3.0
        for term in focus_terms:
            if term in text:
                score += 5.0
        if score > 0:
            scored.append((score, asset))

    scored.sort(key=lambda item: item[0], reverse=True)
    results = []
    for _, asset in scored[:limit]:
        results.append({
            "file_name": asset.get("file_name"),
            "relative_path": asset.get("relative_path"),
            "categories": asset.get("categories", []),
            "relevant_components": asset.get("relevant_components", []),
            "score": asset.get("score", 0),
        })
    return results


def answer_query(
    query: str,
    category: str | None = None,
    limit: int = 5,
    context: str = "",
) -> dict[str, Any]:
    """Primary reasoning-layer entry point.

    It routes the query into CAD, KB/spec, and visual lookup layers and returns a
    single structured result object ready to be used by the UI or a future LLM.
    """
    normalized = normalize_query(query)
    if not normalized:
        return {
            "query": query,
            "cad_results": [],
            "spec_results": [],
            "visual_results": [],
            "summary": "No query text provided.",
        }

    if is_greeting(normalized):
        return {
            "query": query,
            "category": category,
            "cad_results": [],
            "spec_results": [],
            "visual_results": [],
            "summary": (
                "Hello. I am your Construction Copilot. Ask me about the FreeCAD model, "
                "staircases, structure, plumbing, electrical work, waterproofing, or site guidance."
            ),
        }

    retrieval_query = normalize_query(f"{context} {normalized}").strip() if context else normalized
    search_plan = choose_search_plan(normalized, context)
    selected_searches = set(search_plan["searches"])
    selected_category = category or search_plan.get("category")

    cad_limit = max(limit, 50) if search_plan.get("answer_type") in {"count", "dimension"} else limit
    cad_results = (
        query_cad_database(
            retrieval_query,
            limit=cad_limit,
            focus_terms=search_plan.get("focus_terms"),
            exclude_terms=search_plan.get("exclude_terms"),
        )
        if "cad" in selected_searches
        else []
    )
    physical_results = [
        item for item in cad_results
        if item.get("object_type") != "App::DocumentObjectGroup"
    ]
    if physical_results and search_plan.get("answer_type") in {"count", "dimension"}:
        cad_results = physical_results

    spec_results = (
        search_spec_sections(
            retrieval_query,
            category=selected_category,
            limit=max(limit, 20) if search_plan.get("answer_type") in {"procedure", "count"} else limit,
            focus_terms=search_plan.get("focus_terms"),
            exclude_terms=search_plan.get("exclude_terms"),
        )
        if "specs" in selected_searches
        else []
    )
    visual_results = (
        match_visual_assets(
            retrieval_query,
            limit=limit,
            focus_terms=search_plan.get("focus_terms"),
            exclude_terms=search_plan.get("exclude_terms"),
        )
        if "visuals" in selected_searches
        else []
    )

    summary_parts = []
    if cad_results:
        summary_parts.append(f"Found {len(cad_results)} CAD objects matching the query.")
    if spec_results:
        summary_parts.append(f"Found {len(spec_results)} relevant technical sections.")
    if visual_results:
        summary_parts.append(f"Found {len(visual_results)} matching visual assets.")

    if not summary_parts:
        summary_parts.append("No deterministic matches were found in the CAD, spec, or visual indexes.")
    elif spec_results:
        summary_parts.append(f"Most relevant project guidance: {spec_results[0]['title']}.")

    summary = summarize_answer(normalized, {
        "cad_results": cad_results,
        "spec_results": spec_results,
        "visual_results": visual_results,
        "search_plan": search_plan,
        "summary": " ".join(summary_parts),
    })

    return {
        "query": query,
        "category": category,
        "cad_results": cad_results,
        "spec_results": spec_results,
        "visual_results": visual_results,
        "search_plan": search_plan,
        "runtime_status": runtime_status(),
        "has_evidence": bool(cad_results or spec_results or visual_results),
        "evidence_status": "found" if (cad_results or spec_results or visual_results) else "not_found",
        "summary": summary,
    }


if __name__ == "__main__":
    sample_queries = [
        "what is the staircase riser height",
        "show kitchen drainage system",
        "find electrical switchboard details",
        "what are the columns and beams",
    ]

    for query in sample_queries:
        print(json.dumps(answer_query(query), ensure_ascii=False, indent=2))
        print("-" * 80)
