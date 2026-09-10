#!/usr/bin/env python3
"""Parse walkthrough.md into a structured KB JSON index.

This creates a normalized index of construction sections so the app can search and
retrieve specification sections without scanning the raw markdown in full.
"""

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


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[`*_~]", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"^-+|-+$", "", value)
    return value or "section"


def classify_section(title: str, content: str) -> list[str]:
    text = f"{title} {content}".lower()
    rules = {
        "structural": ["column", "beam", "slab", "lintel", "ring beam", "foundation", "seismic", "rcc", "concrete"],
        "plumbing": ["plumbing", "pipe", "drain", "septic", "sump", "toilet", "sanitary", "waterproofing", "waste"],
        "electrical": ["electrical", "conduit", "switchboard", "lighting", "cctv", "wiring", "eb", "ac", "ups"],
        "staircase": ["staircase", "stairs", "riser", "tread", "landing", "winder"],
        "architectural": ["facade", "elevation", "room", "door", "window", "layout", "architectural"],
        "site_work": ["site", "earthwork", "datum", "utility", "work", "verification", "file organization"],
    }
    matches: list[str] = []
    for key, keywords in rules.items():
        if any(k in text for k in keywords):
            matches.append(key)
    return matches or ["general"]


def parse_sections(markdown_text: str) -> list[dict[str, Any]]:
    lines = markdown_text.splitlines()
    pattern = re.compile(r"^(#{1,6})\s+(.*)$")

    sections: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None

    for idx, line in enumerate(lines, start=1):
        match = pattern.match(line)
        if match:
            if current is not None:
                current["content"] = "\n".join(current["content"]).strip()
                sections.append(current)

            level = len(match.group(1))
            title = match.group(2).strip()
            current = {
                "title": title,
                "level": level,
                "slug": slugify(title),
                "start_line": idx,
                "content": [],
                "categories": [],
            }
            continue

        if current is not None:
            current["content"].append(line)

    if current is not None:
        current["content"] = "\n".join(current["content"]).strip()
        sections.append(current)

    for section in sections:
        section["categories"] = classify_section(section["title"], section["content"])
        section["summary"] = (
            re.sub(r"\s+", " ", section["content"])[:220].strip()
            if section["content"]
            else "No section content extracted."
        )
        section["content_length"] = len(section["content"])
        section.pop("content", None)

    return sections


def main() -> int:
    source_path = project_root() / "walkthrough.md"
    output_path = kb_dir() / "specs_database.json"
    kb_dir().mkdir(parents=True, exist_ok=True)

    markdown_text = source_path.read_text(encoding="utf-8")
    sections = parse_sections(markdown_text)

    payload = {
        "project": "construction-copilot",
        "source_file": str(source_path.name),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_sections": len(sections),
        "sections": sections,
    }

    output_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "status": "ok",
        "source_file": str(source_path),
        "output_file": str(output_path),
        "total_sections": len(sections),
        "sample": sections[:3],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
