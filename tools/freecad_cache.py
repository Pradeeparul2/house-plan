"""
Project-side FreeCAD model-state cache.

Run from Robust MCP execute_python:
    exec(open(r"<PROJECT_ROOT>/tools/freecad_cache.py", encoding="utf-8").read())

The module writes .freecad-cache/state.json, object-index.json and
relationships.json beside the current FCStd file.

FreeCAD remains authoritative. Cache is advisory only.
"""
from __future__ import annotations

import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import FreeCAD as App


def _doc():
    doc = App.ActiveDocument
    if doc is None:
        raise RuntimeError("No active FreeCAD document.")
    return doc


def _project_root(doc) -> Path:
    filename = getattr(doc, "FileName", "") or ""
    if not filename:
        raise RuntimeError(
            "Active document is unsaved. Save the FCStd file before using the cache."
        )
    return Path(filename).resolve().parent


def _cache_dir(doc) -> Path:
    path = _project_root(doc) / ".freecad-cache"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _num(v: Any) -> float:
    try:
        return round(float(v), 4)
    except Exception:
        return 0.0


def _bbox(shape) -> list[float] | None:
    try:
        if shape is None or shape.isNull():
            return None
        b = shape.BoundBox
        return [
            _num(b.XMin), _num(b.YMin), _num(b.ZMin),
            _num(b.XMax), _num(b.YMax), _num(b.ZMax),
        ]
    except Exception:
        return None


def _placement(obj) -> list[float] | None:
    try:
        p = obj.Placement
        q = p.Rotation.Q
        return [
            _num(p.Base.x), _num(p.Base.y), _num(p.Base.z),
            _num(q[0]), _num(q[1]), _num(q[2]), _num(q[3]),
        ]
    except Exception:
        return None


def _shape_signature(obj) -> str | None:
    try:
        shape = obj.Shape
        if shape.isNull():
            return None
        # hashCode is used only as a lightweight in-session/change fingerprint.
        return str(shape.hashCode())
    except Exception:
        return None


def _safe_property(obj, name: str) -> Any:
    try:
        value = getattr(obj, name)
        if isinstance(value, (str, int, float, bool)):
            return value
        return str(value)
    except Exception:
        return None


def _object_record(obj) -> dict[str, Any]:
    return {
        "label": obj.Label,
        "type": obj.TypeId,
        "placement": _placement(obj),
        "bbox": _bbox(getattr(obj, "Shape", None)),
        "shape_hash": _shape_signature(obj),
    }


def _fingerprint(records: list[dict[str, Any]]) -> str:
    payload = json.dumps(records, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(
        prefix=path.name + ".",
        suffix=".tmp",
        dir=str(path.parent),
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
        os.replace(tmp_name, path)
    finally:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass


def _current_records(doc, names: list[str] | None = None):
    wanted = set(names) if names else None
    result = []
    for obj in doc.Objects:
        if wanted is not None and obj.Name not in wanted:
            continue
        result.append({
            "name": obj.Name,
            **_object_record(obj),
        })
    result.sort(key=lambda x: x["name"])
    return result


def model_state() -> dict[str, Any]:
    """Return compact state and current fingerprint; does not write cache."""
    doc = _doc()
    records = _current_records(doc)
    shapes = [o for o in doc.Objects if hasattr(o, "Shape")]
    invalid = []
    for o in shapes:
        try:
            if not o.Shape.isNull() and not o.Shape.isValid():
                invalid.append(o.Name)
        except Exception:
            pass

    bbox = None
    boxes = []
    for o in shapes:
        b = _bbox(getattr(o, "Shape", None))
        if b:
            boxes.append(b)
    if boxes:
        bbox = [
            _num(min(b[0] for b in boxes)),
            _num(min(b[1] for b in boxes)),
            _num(min(b[2] for b in boxes)),
            _num(max(b[3] for b in boxes)),
            _num(max(b[4] for b in boxes)),
            _num(max(b[5] for b in boxes)),
        ]

    return {
        "document": doc.Name,
        "file": str(Path(doc.FileName).resolve()),
        "object_count": len(doc.Objects),
        "bbox_mm": bbox,
        "invalid_objects": invalid,
        "fingerprint": _fingerprint(records),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    }


def refresh_all() -> dict[str, Any]:
    """Refresh compact cache for the current document."""
    doc = _doc()
    cache = _cache_dir(doc)
    records = _current_records(doc)
    state = model_state()

    # Lightweight container/parent relationship data where available.
    relationships = []
    for obj in doc.Objects:
        try:
            group = getattr(obj, "Group", None)
            if group:
                relationships.append({
                    "parent": obj.Name,
                    "children": [x.Name for x in group],
                })
        except Exception:
            pass

    _write_json(cache / "state.json", state)
    _write_json(cache / "object-index.json", records)
    _write_json(cache / "relationships.json", relationships)

    return {
        "status": "ok",
        "cache": str(cache),
        "object_count": len(records),
        "fingerprint": state["fingerprint"],
        "invalid": len(state["invalid_objects"]),
    }


def inspect(names: list[str]) -> dict[str, Any]:
    """Return only requested object summaries and refresh those entries."""
    doc = _doc()
    records = _current_records(doc, names)
    return {
        "status": "ok",
        "document": doc.Name,
        "objects": records,
    }


def validate(names: list[str] | None = None) -> dict[str, Any]:
    """Targeted geometry validation."""
    doc = _doc()
    wanted = set(names) if names else None
    checked = []
    invalid = []
    for obj in doc.Objects:
        if wanted is not None and obj.Name not in wanted:
            continue
        if not hasattr(obj, "Shape"):
            continue
        checked.append(obj.Name)
        try:
            if not obj.Shape.isNull() and not obj.Shape.isValid():
                invalid.append(obj.Name)
        except Exception:
            invalid.append(obj.Name)
    return {
        "status": "ok" if not invalid else "invalid",
        "checked": checked,
        "invalid": invalid,
    }


def find(query: str, limit: int = 10) -> dict[str, Any]:
    """Search the cached object index by case-insensitive substring match.

    Searches object name and label only.  Reads object-index.json locally
    inside FreeCAD execute_python — the index is never returned to LLM context.

    Sort order (deterministic):
      1. Exact name match
      2. Exact label match
      3. Name alphabetically

    Returns compact {name, label, type} records up to *limit*.
    """
    doc = _doc()
    cache = _cache_dir(doc)
    index_path = cache / "object-index.json"

    if not index_path.exists():
        return {"query": query, "count": 0, "matches": [], "note": "index_not_found"}

    try:
        records = json.loads(index_path.read_text(encoding="utf-8"))
        if not isinstance(records, list):
            records = []
    except Exception as exc:
        return {"query": query, "count": 0, "matches": [], "note": f"read_error:{exc}"}

    q = query.lower()

    def _sort_key(r):
        name  = (r.get("name")  or "").lower()
        label = (r.get("label") or "").lower()
        return (
            0 if name  == q else 1,   # exact name match first
            0 if label == q else 1,   # exact label match second
            name,                      # alphabetical fallback
        )

    matched = []
    for r in records:
        name  = (r.get("name")  or "").lower()
        label = (r.get("label") or "").lower()
        if q in name or q in label:
            matched.append(r)

    matched.sort(key=_sort_key)
    matched = matched[:limit]

    return {
        "query": query,
        "count": len(matched),
        "matches": [
            {"name": r.get("name"), "label": r.get("label"), "type": r.get("type")}
            for r in matched
        ],
    }


def cache_status() -> dict[str, Any]:
    """Compare current model fingerprint with cached state."""
    doc = _doc()
    cache = _cache_dir(doc)
    state_path = cache / "state.json"
    if not state_path.exists():
        return {"status": "miss", "reason": "no_cache"}

    try:
        cached = json.loads(state_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"status": "miss", "reason": f"cache_read_error:{exc}"}

    current = model_state()
    hit = cached.get("fingerprint") == current.get("fingerprint")
    return {
        "status": "hit" if hit else "stale",
        "cached_fingerprint": cached.get("fingerprint"),
        "current_fingerprint": current.get("fingerprint"),
        "object_count": current["object_count"],
        "invalid": len(current["invalid_objects"]),
    }


def refresh_objects(names: list[str]) -> dict[str, Any]:
    """Update selected object records in object-index.json."""
    doc = _doc()
    cache = _cache_dir(doc)
    index_path = cache / "object-index.json"

    try:
        existing = json.loads(index_path.read_text(encoding="utf-8"))
        if not isinstance(existing, list):
            existing = []
    except Exception:
        existing = []

    by_name = {x.get("name"): x for x in existing if isinstance(x, dict)}
    for record in _current_records(doc, names):
        by_name[record["name"]] = record

    for name in names:
        if doc.getObject(name) is None:
            by_name.pop(name, None)

    updated = sorted(by_name.values(), key=lambda x: x.get("name", ""))
    _write_json(index_path, updated)

    return {
        "status": "ok",
        "updated": names,
        "cached_objects": len(updated),
    }
