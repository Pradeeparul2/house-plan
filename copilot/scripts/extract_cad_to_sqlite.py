#!/usr/bin/env python3
"""Extract the FreeCAD model into a lightweight SQLite CAD database.

This script is designed for the construction project workflow described in
CONSTRUCTION_COPILOT_SPEC.md. The FreeCAD model remains the source of truth,
while the SQLite database acts as the generated runtime index used by the app.

Behavior:
- If FreeCAD is installed and the model is available, it will open the CAD
  document and extract metadata for each object into the SQLite table.
- If FreeCAD is unavailable, it creates the schema and an empty database so the
  project still has a valid cad_database.sqlite artifact in place.

Usage:
    python copilot/scripts/extract_cad_to_sqlite.py
    python copilot/scripts/extract_cad_to_sqlite.py --model <path-to-model>
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def db_path() -> Path:
    return project_root() / "copilot" / "KB" / "cad_database.sqlite"


def ensure_db_schema(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS cad_objects (
            id TEXT PRIMARY KEY,
            label TEXT,
            object_type TEXT,
            discipline TEXT,
            floor_level TEXT,
            room_zone TEXT,
            material TEXT,
            coord_x_min REAL,
            coord_x_max REAL,
            coord_y_min REAL,
            coord_y_max REAL,
            coord_z_min REAL,
            coord_z_max REAL,
            length_mm REAL,
            width_mm REAL,
            height_mm REAL,
            volume_m3 REAL,
            surface_area_m2 REAL,
            connected_objects TEXT,
            source_model TEXT,
            extracted_at TEXT,
            metadata_json TEXT
        )
        """
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_cad_objects_floor ON cad_objects(floor_level)"
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_cad_objects_zone ON cad_objects(room_zone)"
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_cad_objects_type ON cad_objects(object_type)"
    )
    conn.commit()


def safe_float(value: Any) -> float | None:
    try:
        if value is None:
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def freecad_object_to_row(obj: Any, source_model: str) -> dict[str, Any]:
    """Translate a FreeCAD object to a normalized DB row."""
    label = getattr(obj, "Label", "") or getattr(obj, "Name", "") or "unnamed"
    obj_type = getattr(obj, "TypeId", "") or type(obj).__name__

    bbox = getattr(getattr(obj, "Shape", None), "BoundBox", None)
    if bbox is not None:
        x_min, y_min, z_min = bbox.XMin, bbox.YMin, bbox.ZMin
        x_max, y_max, z_max = bbox.XMax, bbox.YMax, bbox.ZMax
        length_mm = max(0.0, safe_float(x_max - x_min) or 0.0)
        width_mm = max(0.0, safe_float(y_max - y_min) or 0.0)
        height_mm = max(0.0, safe_float(z_max - z_min) or 0.0)
    else:
        x_min = x_max = y_min = y_max = z_min = z_max = None
        length_mm = width_mm = height_mm = None

    volume_m3 = safe_float(getattr(getattr(obj, "Shape", None), "Volume", None))
    volume_m3 = None if volume_m3 is None else volume_m3 / 1000000.0 if volume_m3 > 0 else 0.0

    surface_area_m2 = None
    try:
        if hasattr(obj, "Shape") and obj.Shape is not None:
            surface_area_m2 = obj.Shape.Area / 1000000.0
    except Exception:
        surface_area_m2 = None

    metadata = {
        "name": getattr(obj, "Name", None),
        "label": label,
        "type_id": getattr(obj, "TypeId", None),
        "placement": getattr(obj, "Placement", None),
    }

    row = {
        "id": getattr(obj, "Name", label) or label,
        "label": label,
        "object_type": obj_type,
        "discipline": "unclassified",
        "floor_level": "unknown",
        "room_zone": "unknown",
        "material": "unknown",
        "coord_x_min": safe_float(x_min),
        "coord_x_max": safe_float(x_max),
        "coord_y_min": safe_float(y_min),
        "coord_y_max": safe_float(y_max),
        "coord_z_min": safe_float(z_min),
        "coord_z_max": safe_float(z_max),
        "length_mm": safe_float(length_mm),
        "width_mm": safe_float(width_mm),
        "height_mm": safe_float(height_mm),
        "volume_m3": volume_m3,
        "surface_area_m2": safe_float(surface_area_m2),
        "connected_objects": json.dumps([], ensure_ascii=False),
        "source_model": source_model,
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "metadata_json": json.dumps(metadata, ensure_ascii=False, default=str),
    }
    return row


def extract_from_freecad(model_path: Path, conn: sqlite3.Connection) -> int:
    try:
        import FreeCAD as App  # type: ignore
    except ImportError as exc:  # pragma: no cover - only for environments without FreeCAD
        raise RuntimeError("FreeCAD is not installed in this environment") from exc

    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")

    doc = App.openDocument(str(model_path))
    rows: list[dict[str, Any]] = []
    try:
        for obj in doc.Objects:
            if not hasattr(obj, "Shape"):
                continue
            row = freecad_object_to_row(obj, str(model_path.name))
            rows.append(row)

        conn.execute("DELETE FROM cad_objects")
        conn.executemany(
            """
            INSERT INTO cad_objects (
                id, label, object_type, discipline, floor_level, room_zone,
                material, coord_x_min, coord_x_max, coord_y_min, coord_y_max,
                coord_z_min, coord_z_max, length_mm, width_mm, height_mm,
                volume_m3, surface_area_m2, connected_objects, source_model,
                extracted_at, metadata_json
            ) VALUES (
                :id, :label, :object_type, :discipline, :floor_level, :room_zone,
                :material, :coord_x_min, :coord_x_max, :coord_y_min, :coord_y_max,
                :coord_z_min, :coord_z_max, :length_mm, :width_mm, :height_mm,
                :volume_m3, :surface_area_m2, :connected_objects, :source_model,
                :extracted_at, :metadata_json
            )
            """,
            rows,
        )
        conn.commit()
        return len(rows)
    finally:
        App.closeDocument(doc.Name)


def main() -> int:
    parser = argparse.ArgumentParser(description="Export FreeCAD objects to a SQLite CAD database.")
    parser.add_argument(
        "--model",
        type=str,
        default=str(project_root() / "HomeConstruction.FCStd"),
        help="Path to the FreeCAD document (.FCStd). Defaults to the project model.",
    )
    args = parser.parse_args()

    db_file = db_path()
    db_file.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(str(db_file))
    ensure_db_schema(conn)

    model_path = Path(args.model).resolve()
    rows_inserted = 0
    mode = "schema_only"

    try:
        if model_path.exists():
            try:
                rows_inserted = extract_from_freecad(model_path, conn)
                mode = "freecad_export"
            except RuntimeError as exc:
                # FreeCAD is not available in this environment. Keep a valid schema-only database.
                mode = "schema_only"
                print(json.dumps({"status": "warning", "error": str(exc)}, ensure_ascii=False))
            except Exception as exc:
                mode = "schema_only"
                print(json.dumps({"status": "error", "error": str(exc)}, ensure_ascii=False))
        else:
            conn.execute("DELETE FROM cad_objects")
            conn.commit()
    finally:
        conn.close()

    summary = {
        "status": "ok",
        "db_path": str(db_file),
        "mode": mode,
        "rows_inserted": rows_inserted,
        "project_root": str(project_root()),
    }
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
