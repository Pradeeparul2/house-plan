---
name: freecad-mcp
description: Inspects and edits the current FreeCAD house model through MCP. Use for FreeCAD model queries, geometry changes, object creation, parameter edits, recompute, validation, and model-state checks.
---

# FreeCAD MCP

Use a conservative edit loop.

## Loop
1. Inspect document and relevant objects.
2. Identify target objects and current values.
3. Plan the minimum edit.
4. Execute through available FreeCAD MCP tools.
5. Recompute.
6. Verify only affected objects and dependencies.
7. Summarize changes and verification.

## MCP discipline
- Use only tools actually exposed by the connected MCP server.
- Never invent tool names, arguments, object IDs, or properties.
- Prefer object/property edits over destructive recreation.
- Preserve names, labels, constraints, links, placements, and dependencies.
- If a required MCP capability is unavailable, stop and state the missing capability.

## Output
Return:
- changed objects
- key before → after values
- recompute/validation result
- unresolved issues

Do not dump the complete document unless requested.
