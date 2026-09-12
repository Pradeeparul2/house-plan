---
name: model-audit
description: Audits the FreeCAD house model for geometry, naming, dimensions, levels, duplicates, broken references, and coordination problems before drawings or major edits.
---

# Model Audit

Run targeted audits instead of dumping the entire model.

## Checks
- document recompute/validity
- duplicate or unexpected objects
- missing dependencies
- inconsistent names/labels
- level/elevation consistency
- wall/opening alignment
- stair continuity
- structural coordination
- MEP clashes when requested

## Method
1. Inspect high-level document structure.
2. Narrow to suspicious or relevant objects.
3. Inspect only necessary properties.
4. Report findings by severity:
   - BLOCKER
   - WARNING
   - INFO
5. Suggest the smallest corrective action.

Do not modify the model during an audit unless explicitly requested.
