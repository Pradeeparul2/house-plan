---
name: structural-coordination
description: Coordinates architectural FreeCAD geometry with RCC G+1 structural elements and checks model consistency, load-path assumptions, openings, stairs, beams, columns, and slabs. Use for coordination, not final structural certification.
---

# Structural Coordination

## Workflow
1. Inspect architectural geometry and existing structural objects.
2. Identify affected columns, beams, slabs, stairs, walls, and openings.
3. Check geometric continuity and obvious coordination conflicts.
4. Make only explicitly requested model changes.
5. Recompute and verify affected objects.

## Safety boundary
- Do not certify structural adequacy.
- Do not invent reinforcement or member sizes.
- Do not assume soil capacity or foundation adequacy.
- Label engineering values as ASSUMED, CALCULATED, or VERIFIED.
- Escalate unknown structural inputs to a qualified engineer.

## Checks
- column/beam alignment
- openings versus structural members
- stair/slab interfaces
- vertical continuity between floors
- wall/column conflicts
- service openings that may affect structural members
