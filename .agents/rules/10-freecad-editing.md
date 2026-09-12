# FreeCAD Editing Rule

Use this rule for FreeCAD model changes.

1. Inspect the document before editing.
2. Identify the smallest set of affected objects.
3. Read only the properties/geometry needed for the requested change.
4. Make the smallest deterministic edit.
5. Recompute.
6. Re-read affected objects and verify dimensions, placement, dependencies, and validity.
7. If verification fails, fix the cause before continuing.
8. Do not duplicate objects when an existing object can be edited.
9. Do not delete or rename objects unless explicitly required.
10. Report changed object names and verified values; do not dump the entire model state.
