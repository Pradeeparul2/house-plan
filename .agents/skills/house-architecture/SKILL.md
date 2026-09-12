---
name: house-architecture
description: Designs and reviews the residential G+1 architectural layout in FreeCAD, including rooms, walls, openings, circulation, staircase, kitchen, toilets, ventilation, and spatial coordination.
---

# House Architecture

Use the existing FreeCAD model as the source of truth.

## Workflow
1. Inspect current plan and levels.
2. Identify affected spaces and adjacent constraints.
3. Check circulation, access, openings, furniture clearance, and room relationships.
4. Propose the smallest layout change that satisfies the request.
5. Apply through FreeCAD MCP only after the design intent is clear.
6. Recompute and verify affected dimensions.

## Rules
- Do not silently resize unrelated rooms.
- Do not move structural elements merely to solve an architectural issue.
- Keep stair geometry coordinated with floor height and openings.
- Flag conflicts between architectural and structural requirements.
- Record assumptions rather than hiding them.

## Design basis
Current project basis includes a G+1 residential concept, RCC framed construction, and AAC infill walls. Treat exact dimensions as model data, not as permanent assumptions.
