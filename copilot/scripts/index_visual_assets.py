#!/usr/bin/env python3
"""Index renders/ assets and map them to relevant construction components."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def kb_dir() -> Path:
    return project_root() / "copilot" / "KB"


def normalize_token(token: str) -> str:
    token = token.strip().lower()
    token = token.replace("-", " ")
    token = token.replace("_", " ")
    token = re.sub(r"[^a-z0-9 ]+", "", token)
    token = re.sub(r"\s+", " ", token).strip()
    return token


def extract_keywords(filename: str) -> list[str]:
    stem = Path(filename).stem
    cleaned = stem.replace(".", " ")
    parts = re.split(r"[_\-\s]+", cleaned)
    tokens = []
    for part in parts:
        token = normalize_token(part)
        if token and token not in {"png", "jpg", "jpeg", "svg", "pdf", "gif", "webp"}:
            tokens.append(token)
    return tokens


def infer_categories(filename: str, tokens: list[str]) -> list[str]:
    text = " ".join(tokens)
    categories: list[str] = []

    mapping = {
        "structural": ["beam", "column", "lintel", "ring", "seismic", "footing", "frame", "skeleton", "slab", "structural"],
        "plumbing": ["plumbing", "pipe", "drain", "drainage", "sump", "septic", "toilet", "sink", "valve", "outfall", "water", "pump"],
        "electrical": ["electrical", "conduit", "switchbox", "light", "cctv", "mdb", "ac", "ups", "wiring", "power"],
        "staircase": ["stair", "stairs", "staircase", "landing", "winder", "step", "rail", "balustrade"],
        "architectural": ["elevation", "facade", "front", "rear", "door", "window", "wall", "room", "bedroom", "living", "kitchen", "sitout"],
        "floor_plan": ["plan", "layout", "techdraw", "floor"],
        "cctv": ["cctv", "camera", "surveillance"],
        "waterproofing": ["wet", "waterproof", "membrane", "shower", "sunken"],
    }

    for category, keywords in mapping.items():
        if any(keyword in text for keyword in keywords):
            categories.append(category)

    if not categories:
        categories = ["general"]
    return categories


def infer_component_matches(filename: str, tokens: list[str]) -> list[str]:
    text = " ".join(tokens)
    matches: set[str] = set()

    if any(token in text for token in ["stair", "stairs", "winder", "landing", "rail", "balustrade"]):
        matches.add("stairs_and_balustrades")
    if any(token in text for token in ["column", "beam", "frame", "skeleton", "lintel", "ring"]):
        matches.add("structural_frame")
    if any(token in text for token in ["toilet", "sink", "septic", "sump", "drain", "pump", "valve", "wet", "shower"]):
        matches.add("sanitary_and_plumbing")
    if any(token in text for token in ["electrical", "conduit", "switchbox", "light", "cctv", "mdb", "ac", "ups", "power", "wiring"]):
        matches.add("electrical_mep")
    if any(token in text for token in ["door", "window", "facade", "elevation", "front", "rear"]):
        matches.add("architectural_envelope")
    if any(token in text for token in ["plan", "layout", "techdraw", "floor"]):
        matches.add("floor_plan")
    if any(token in text for token in ["bedroom", "kitchen", "living", "sitout", "utility", "laundry"]):
        matches.add("room_zone")

    if not matches:
        matches.add("general_project_view")
    return sorted(matches)


def build_visual_index() -> list[dict[str, Any]]:
    renders_dir = project_root() / "renders"
    records: list[dict[str, Any]] = []

    for path in sorted(renders_dir.iterdir()):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".svg", ".pdf", ".gif", ".webp"}:
            continue

        tokens = extract_keywords(path.name)
        categories = infer_categories(path.name, tokens)
        components = infer_component_matches(path.name, tokens)

        records.append({
            "file_name": path.name,
            "relative_path": str(path.relative_to(project_root())),
            "extension": path.suffix.lower().lstrip("."),
            "keywords": tokens,
            "categories": categories,
            "relevant_components": components,
            "asset_type": "render" if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"} else "drawing",
        })

    return records


def main() -> int:
    kb = kb_dir()
    kb.mkdir(parents=True, exist_ok=True)

    records = build_visual_index()
    payload = {
        "project": "construction-copilot",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "asset_count": len(records),
        "assets": records,
    }

    output_path = kb / "visual_index.json"
    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps({
        "status": "ok",
        "asset_count": len(records),
        "output_file": str(output_path),
        "sample": records[:3],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
