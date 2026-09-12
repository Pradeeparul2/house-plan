---
name: mep-coordination
description: Coordinates electrical and plumbing layouts with the FreeCAD G+1 house model, including fixtures, routes, shafts, drainage, water supply, electrical points, DB/circuits, and service clearances.
---

# MEP Coordination

## Workflow
1. Inspect architecture and existing MEP objects.
2. Identify the requested service and affected spaces.
3. Prefer shared shafts/routes and short maintainable paths.
4. Avoid structural conflicts and inaccessible maintenance routes.
5. Model only the requested scope.
6. Recompute and verify endpoints, routes, levels, and clashes.

## Electrical
Track DB, circuits, switches, sockets, lighting, dedicated loads, earthing, and AC points.

## Plumbing
Track water supply, hot/cold lines where applicable, drainage, vents, traps, inspection/maintenance access, sump/OHT/septic interfaces.

## Rules
- Do not invent pipe/cable sizing as a final engineering decision.
- Do not route services through structural members without explicit engineering coordination.
- Flag inaccessible valves, cleanouts, junctions, and maintenance points.
