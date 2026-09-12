---
name: construction-drawings
description: Produces and reviews dimensioned 2D construction drawings from the FreeCAD G+1 model, including plans, elevations, sections, dimensions, annotations, and schedules.
---

# Construction Drawings

## Workflow
1. Inspect the current 3D model.
2. Select the required view(s).
3. Generate/update the drawing from model geometry.
4. Add only necessary dimensions, levels, tags, notes, and annotations.
5. Recompute/update views.
6. Cross-check critical dimensions against the 3D model.
7. Report missing or conflicting information.

## Minimum checks
- overall building dimensions
- room dimensions
- wall thickness
- door/window openings
- staircase dimensions
- floor levels
- section cut correctness
- dimension consistency

Never invent a dimension. Mark it UNKNOWN when the model does not contain enough information.
