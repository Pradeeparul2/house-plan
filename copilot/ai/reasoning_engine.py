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
import os
import sqlite3
from pathlib import Path
from typing import Any

try:
    from google import genai
except Exception:  # pragma: no cover - optional dependency
    genai = None


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
    return bool(os.getenv("GEMINI_API_KEY")) and genai is not None


def gemini_model_name() -> str:
    """Return the configured Gemini model, with a current default."""
    load_project_env()
    return os.getenv("GEMINI_MODEL", "gemini-3.6-flash")


def build_gemini_prompt(query: str, evidence: dict[str, Any]) -> str:
    """Construct a structured prompt for Gemini using local evidence."""
    cad = evidence.get("cad_results") or []
    specs = evidence.get("spec_results") or []
    visuals = evidence.get("visual_results") or []

    cad_block = json.dumps(cad[:5], ensure_ascii=False, indent=2) if cad else "[]"
    spec_block = json.dumps(specs[:5], ensure_ascii=False, indent=2) if specs else "[]"
    visual_block = json.dumps(visuals[:5], ensure_ascii=False, indent=2) if visuals else "[]"

    return f"""
You are the Senior Chief Structural Engineer, MEP Consultant, and Lead BIM Inspector for this residential home construction project.

User question: {query}

Use only the provided evidence. Do not invent dimensions or codes. If no evidence is provided, say so clearly.

Relevant CAD objects:
{cad_block}

Relevant specification sections:
{spec_block}

Relevant visual references:
{visual_block}

Answer in concise, practical site language. Cite relevant Indian standards or project-specific evidence when available. Do not output filesystem paths or image filenames; refer to matching visual evidence as "the visual reference shown below".
""".strip()


def build_search_planner_prompt(query: str) -> str:
    """Ask Gemini which local evidence sources are needed for a query."""
    return f"""
You are the retrieval planner for a construction BIM assistant.

User query: {query}

Choose only the local evidence sources needed to answer the query:
- cad: exact model objects, dimensions, coordinates, quantities, or counts
- specs: construction methods, standards, sequences, safety, or code guidance
- visuals: renders, plans, elevations, or diagrams the user may need to see

Return JSON only, with this exact shape:
{{"searches":["cad", "specs", "visuals"], "category":"optional category or null"}}
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
    return {"searches": searches, "category": category if isinstance(category, str) else None}


def deterministic_search_plan(query: str) -> dict[str, Any]:
    """Choose evidence sources when Gemini is unavailable or returns invalid JSON."""
    tokens = set(retrieval_tokens(query))
    searches: list[str] = []
    if tokens & {"dimension", "dimensions", "size", "length", "width", "height", "count", "object", "model", "cad"}:
        searches.append("cad")
    if tokens & {"how", "install", "installation", "method", "procedure", "standard", "code", "curing", "waterproofing", "safety", "rule", "guidance"}:
        searches.append("specs")
    if tokens & {"show", "see", "view", "image", "picture", "plan", "elevation", "render", "diagram"}:
        searches.append("visuals")
    return {"searches": searches or ["cad", "specs", "visuals"], "category": None}


def choose_search_plan(query: str) -> dict[str, Any]:
    """Let Gemini choose retrieval tools, with a local intent fallback."""
    if gemini_available():
        try:
            client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
            response = client.models.generate_content(
                model=gemini_model_name(),
                contents=build_search_planner_prompt(query),
            )
            plan = parse_search_plan(getattr(response, "text", "") or "")
            if plan:
                plan["planner"] = "gemini"
                return plan
        except Exception:
            pass

    plan = deterministic_search_plan(query)
    plan["planner"] = "local_fallback"
    return plan


def summarize_answer(query: str, evidence: dict[str, Any]) -> str:
    """Return a Gemini answer when available, otherwise fallback to local summary."""
    if gemini_available():
        try:
            client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
            response = client.models.generate_content(
                model=gemini_model_name(),
                contents=build_gemini_prompt(query, evidence),
            )
            return getattr(response, "text", None) or evidence.get("summary") or "No answer generated."
        except Exception:
            pass

    return evidence.get("summary") or "No deterministic match found."


def cad_db_path() -> Path:
    return project_root() / "copilot" / "KB" / "cad_database.sqlite"


def specs_kb_path() -> Path:
    return project_root() / "copilot" / "KB" / "specs_database.json"


def visual_kb_path() -> Path:
    return project_root() / "copilot" / "KB" / "visual_index.json"


def normalize_query(query: str) -> str:
    return " ".join(query.lower().split())


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
    "have", "is", "many", "me", "of", "on", "please", "show", "tell", "the",
    "there", "this", "what", "we", "where", "which", "with", "you",
}


def is_front_entrance_steps_query(query: str) -> bool:
    tokens = set(retrieval_tokens(query))
    return bool(tokens & {"step", "steps", "riser"}) and bool(
        tokens & {"front", "entrance", "entry", "building", "exterior", "outside", "sitout", "porch"}
    )


def retrieval_tokens(query: str) -> list[str]:
    return [
        token
        for token in normalize_query(query).replace("-", " ").split()
        if token not in RETRIEVAL_STOPWORDS and len(token) > 1
    ]


def query_cad_database(
    query: str,
    limit: int = 10,
    conn: sqlite3.Connection | None = None,
) -> list[dict[str, Any]]:
    """Return CAD objects by matching the query text against relevant fields.

    This is lightweight deterministic filtering rather than a dense semantic search.
    """
    normalized = normalize_query(query)
    tokens = retrieval_tokens(normalized)

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
            conditions.append(
                "(LOWER(id) LIKE ? OR LOWER(label) LIKE ? OR LOWER(object_type) LIKE ? OR LOWER(room_zone) LIKE ? OR LOWER(floor_level) LIKE ? OR LOWER(discipline) LIKE ?)"
            )
            pattern = f"%{token}%"
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

        if is_front_entrance_steps_query(normalized):
            entrance_terms = ("entrance", "entry", "front step", "front_step", "sitout", "porch", "gate")
            candidates = [
                item for item in candidates
                if any(term in f"{item.get('id', '')} {item.get('label', '')}".lower() for term in entrance_terms)
                and any(term in f"{item.get('id', '')} {item.get('label', '')}".lower() for term in ("step", "riser", "tread"))
            ]

        def relevance(item: dict[str, Any]) -> tuple[int, str]:
            score = 0
            for token in tokens:
                for field in searchable_fields:
                    value = str(item.get(field) or "").lower()
                    if token in value:
                        score += 3 if field in {"id", "label"} else 1
            return score, str(item.get("label") or "")

        candidates.sort(key=relevance, reverse=True)
        return candidates[:limit]
    finally:
        if close_after:
            connection.close()


def search_spec_sections(query: str, category: str | None = None, limit: int = 5) -> list[dict[str, Any]]:
    """Search the parsed walkthrough KB for relevant sections."""
    path = specs_kb_path()
    if not path.exists():
        return []

    payload = json.loads(path.read_text(encoding="utf-8"))
    sections = payload.get("sections", [])
    normalized_query = normalize_query(query)
    query_tokens = retrieval_tokens(normalized_query)
    if not query_tokens:
        return []

    scored: list[tuple[float, dict[str, Any]]] = []

    for section in sections:
        title = (section.get("title") or "").lower()
        slug = (section.get("slug") or "").lower()
        summary = (section.get("summary") or "").lower()
        cats = [str(item).lower() for item in section.get("categories", [])]
        text = f"{title} {slug} {summary}".lower()

        if category:
            category_lower = category.lower()
            if category_lower not in cats and category_lower not in text:
                continue

        score = 0.0
        for token in query_tokens:
            if token in title:
                score += 4.0
            if token in summary:
                score += 2.5
            if token in text:
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
            "start_line": section.get("start_line"),
        })
    return results


def match_visual_assets(query: str, limit: int = 5) -> list[dict[str, Any]]:
    """Return likely visual matches for a user question."""
    path = visual_kb_path()
    if not path.exists():
        return []

    payload = json.loads(path.read_text(encoding="utf-8"))
    assets = payload.get("assets", [])
    normalized = normalize_query(query)
    query_tokens = retrieval_tokens(normalized)
    if not query_tokens:
        return []

    scored: list[tuple[float, dict[str, Any]]] = []
    for asset in assets:
        text = " ".join(asset.get("keywords", []) + asset.get("categories", []) + asset.get("relevant_components", []))
        score = 0.0
        for token in query_tokens:
            if token in text:
                score += 2.0
            if token in asset.get("file_name", "").lower():
                score += 3.0
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


def answer_query(query: str, category: str | None = None, limit: int = 5) -> dict[str, Any]:
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

    search_plan = choose_search_plan(normalized)
    if is_front_entrance_steps_query(normalized):
        search_plan = {"searches": ["cad"], "category": None, "planner": search_plan.get("planner", "local_fallback")}
    selected_searches = set(search_plan["searches"])
    selected_category = category or search_plan.get("category")

    cad_results = query_cad_database(normalized, limit=limit) if "cad" in selected_searches else []
    spec_results = (
        search_spec_sections(normalized, category=selected_category, limit=limit)
        if "specs" in selected_searches
        else []
    )
    visual_results = match_visual_assets(normalized, limit=limit) if "visuals" in selected_searches else []

    if is_front_entrance_steps_query(normalized) and not cad_results:
        summary = "No exact front entrance step count is available in the current CAD model."
        return {
            "query": query,
            "category": category,
            "cad_results": [],
            "spec_results": [],
            "visual_results": [],
            "search_plan": search_plan,
            "summary": summary,
        }

    if is_front_entrance_steps_query(normalized):
        physical_objects = [
            item for item in cad_results
            if item.get("object_type") != "App::DocumentObjectGroup"
        ]
        summary = (
            f"The current CAD model contains {len(physical_objects)} modeled front entrance step features "
            f"plus {len(cad_results) - len(physical_objects)} organizing group record(s). "
            "The database does not identify the exact number of individual treads."
        )
        return {
            "query": query,
            "category": category,
            "cad_results": cad_results,
            "spec_results": [],
            "visual_results": [],
            "search_plan": search_plan,
            "summary": summarize_answer(normalized, {
                "cad_results": cad_results,
                "spec_results": [],
                "visual_results": [],
                "summary": summary,
            }),
        }

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

    return {
        "query": query,
        "category": category,
        "cad_results": cad_results,
        "spec_results": spec_results,
        "visual_results": visual_results,
        "search_plan": search_plan,
        "summary": summarize_answer(normalized, {
            "cad_results": cad_results,
            "spec_results": spec_results,
            "visual_results": visual_results,
            "summary": " ".join(summary_parts),
        }),
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
