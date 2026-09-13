---
name: model-state-cache
description: Uses a compact project-side FreeCAD state cache through execute_python to avoid repeated full-model inspection. Use before broad inspection and after successful edits.
---

# Model State Cache

## Purpose

Reduce repeated FreeCAD inspection context. The FCStd model is always authoritative; cache is advisory only.

## Cache location

`.freecad-cache/` beside the active `.FCStd` file:

- `state.json` — compact document state and fingerprint
- `object-index.json` — compact object summaries
- `relationships.json` — lightweight container relationships

Cache is disposable; add `.freecad-cache/` to `.gitignore`.

## Workflow

### Before a broad inspection

1. Save the FCStd document.
2. Run `cache_status()`.
3. On `hit` → use cached index to locate targets.
4. On `stale`/`miss` → run `refresh_all()` only when no usable index exists.

### Targeted task

1. `cache_status()` — check freshness.
2. Known target → `inspect(names)`.
3. Unknown target → `find(query, limit)`.
4. Inspect only selected objects and direct dependencies.
5. Make the smallest deterministic edit; recompute once.
6. `validate(affected_names)` — verify geometry.
7. `refresh_objects(affected_names)` — update cache entries.

### After an edit

- `refresh_objects(names)` only. **Do not** call `refresh_all()`.

## Bootstrap

```python
import FreeCAD as App
from pathlib import Path

doc = App.ActiveDocument
if doc is None or not doc.FileName:
    raise RuntimeError("Save the active FCStd document before using the cache.")

root = Path(doc.FileName).resolve().parent
ns = {}
exec((root / "tools" / "freecad_cache.py").read_text(encoding="utf-8"), ns)

ns["cache_status"]()             # freshness
ns["find"]("wall", 5)           # locate by name/label substring
ns["inspect"](["Object_Name"])  # single-object summary
ns["validate"](["Object_Name"]) # geometry check
ns["refresh_objects"](names)    # update after edit
```

## Critical rules

**Do:**

- Access cache only through `tools/freecad_cache.py` via `execute_python`.
- Return only `status`, `fingerprint`, `object_count`, `invalid`, and requested summaries.

**Do NOT:**

- Read `.freecad-cache/*.json` into LLM context.
- Dump the object index into context.
- Use filesystem/file-reading tools on the cache.
- Return meshes, vertices, faces, or full property dumps.
- Skip final validation because the cache reports an object valid.

## Cache safety

- Cached geometry is not proof of current geometry — always validate after edits.
- `shape_hash` is a lightweight change indicator, not a geometric proof.
- If cache and FreeCAD disagree, FreeCAD wins.
- Stale fingerprint = model changed since last `refresh_all()` — this is correct behaviour, not a bug.

### Documentation Access Discipline

- NEVER read `walkthrough.md` or all files in `docs/` simultaneously.
- When specifications, coordinates, or BOQ values are needed, inspect `docs/index.md` first.
- Read ONLY the single matching sub-file (e.g., `docs/06_mep_plumbing.md`).

### 3D Model & Documentation Synchronization Rule

Whenever any geometry, member dimension, or coordinate placement changes within `HomeConstruction.FCStd`:

1. Identify the affected functional group (e.g., Substructure, Ground Floor, First Floor, Rooftop/Terrace, or MEP Network).
2. Locate the corresponding target file via `docs/index.md` (e.g., `docs/01_substructure.md`, `docs/06_mep_plumbing.md`).
3. Immediately update the relevant specification, coordinate log, or schedule inside that specific markdown file only.
4. Never mark a 3D modeling task complete without committing the matching documentation diff.
