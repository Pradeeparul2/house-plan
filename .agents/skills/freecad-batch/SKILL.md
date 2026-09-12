---
name: freecad-batch
description: Performs efficient batch FreeCAD MCP operations using Python, targeted inspection, deterministic naming, minimal recompute, and post-edit validation.
---

# Batch FreeCAD Operations

## Primary strategy

For multi-step geometry:

INSPECT → BATCH → RECOMPUTE → VERIFY

Prefer one execute_python operation over many micro-tool calls.

## Batch rules

- Create or modify related objects in one Python execution.
- Avoid create_box → placement → property → recompute sequences.
- Build the complete operation in memory where practical.
- Add objects to the document.
- Recompute after the batch.

## Output

Python execution should return only compact machine-readable results.

Preferred:

{"status":"ok","created":12,"modified":3}

Avoid:

- print loops
- object dumps
- vertex arrays
- mesh data
- complete property dumps

## Targeted validation

Track affected objects:

affected = [obj1, obj2, obj3]

Validate only:

- affected objects
- direct dependents
- explicitly requested objects

Check:

- Shape.isNull()
- Shape.isValid()
- BoundBox
- placement
- key dimensions

## Error handling

Use try/except.

On failure:

1. Stop.
2. Report the failing operation.
3. Preserve the existing model where possible.
4. Do not silently continue with partially invalid geometry.

## MCP

Use only MCP tools actually exposed by the server.

Never invent:

- tool names
- arguments
- object IDs
- properties

If execute_python is available, prefer it for multi-step deterministic operations.
