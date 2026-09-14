# Blender MCP Tour Director Skill

## Mission

Automate the generation of a dimension-accurate 3D architectural walkthrough video inside Blender using exported CAD geometry (.glb) from HomeConstruction.FCStd[cite: 2, 5, 9]. Maintain strict token optimization, zero scene streaming, and seamless documentation synchronization[cite: 2, 8, 9].

---

## 1. Token Discipline & MCP Execution Rules

- **Zero Raw Mesh Streaming:** NEVER inspect, query, or pass raw vertices, mesh arrays, polygons, or transformation matrices into the LLM chat context[cite: 8, 9].
- **Template Invocation Over Code Generation:** Never stream multi-line, arbitrary `bpy` scripts into chat[cite: 9]. Use pre-built parameter scripts inside `blender_scripts/` and invoke them via compact Python loader calls[cite: 9]:
  `import sys; sys.path.append('blender_scripts'); import generate_tour_path; generate_tour_path.create_walkthrough()`
- **Structured Group Inspection:** Query scene hierarchy exclusively at the collection or container level (`Walls`, `Columns`, `Openings`, `Cameras`)[cite: 5, 9].
- **Advisory Cache Coordination:** Respect the FreeCAD state cache conventions (`tools/freecad_cache.py`)[cite: 5, 8]. Do not dump entire object trees; refer directly to module files under `docs/` (e.g., `docs/02_ground_floor.md`, `docs/03_first_floor.md`) to read clearances and room coordinates[cite: 2, 9].

---

## 2. Model Baseline & Spatial Rules

- **Footprint Envelope:** Strict adherence to the 16' 6" x 25' 0" (5029.2 x 7619.8 mm) building boundary[cite: 3, 4, 9].
- **Scale Integrity:** Enforce 1:1 scale conversion on import (1.000 unit scaling) with `+Z Up, -Y Forward` coordinate orientation to align with FreeCAD CAD coordinates[cite: 9].
- **Camera Clip Range:** Set `clip_start = 0.05` to `0.1` m and `clip_end = 100.0` m. The narrow near-clipping threshold prevents geometry slicing in tight interior spaces (e.g., 750 mm toilet doors, 1486 mm sitout)[cite: 9, 11, 12].
- **Eye-Level Datums:**
  - Plinth Finished Floor Level (FFL): +0.9144 m (+3' 0")[cite: 1, 9, 12]
  - Ground Floor Eye-Level: Z ~ +2.464 m (FFL + 1.55 m)[cite: 9]
  - First Floor FFL: +3.9624 m to +4.0874 m[cite: 9, 12]
  - First Floor Eye-Level: Z ~ +5.637 m[cite: 9]
  - Mumty / Terrace Floor: +7.1354 m (Eye-Level: Z ~ +8.685 m)[cite: 3, 9, 12]

---

## 3. Standard Automation Pipeline

### Step 1: CAD Geometry Ingestion

- Export active geometry from FreeCAD (`HomeConstruction.FCStd`) as `.glb` (ensuring non-structural clutter and temporary boolean cut tools are omitted)[cite: 5, 9, 17].
- Import geometry into Blender, normalize world origin (0, 0, 0) to the building boundary datum, and lock scale[cite: 9].

### Step 2: Batch PBR Material Assignment

- Execute `blender_scripts/assign_materials.py` to bind realistic shaders based on the project elevation palette[cite: 9]:
  - **Mat_Wall_Base:** Matte off-white architectural plaster[cite: 9].
  - **Mat_Wall_Charcoal:** Dark charcoal/slate accent bands and parapet trim[cite: 9].
  - **Mat_Teak_Wood:** Main entrance door, joinery, and frames[cite: 9].
  - **Mat_SS_304:** Staircase and balcony safety railings[cite: 9, 10].
  - **Mat_Concrete_Structural:** Exposed structural columns and floor slabs[cite: 9].
  - **Mat_Glass:** Translucent window and balcony glazing[cite: 9].

### Step 3: Camera Path Generation

- Run `blender_scripts/generate_tour_path.py` to instantiate a 3D Bezier curve path with linear time evaluation and a dedicated empty look-at tracking target[cite: 9].
- Follow the defined 8-shot architectural walkthrough sequence[cite: 9]:
  1. Front approach road to Sitout Porch[cite: 9, 17].
  2. Clear-span Living Room walkthrough (4724 x 3230 mm)[cite: 12].
  3. Breakfast counter glance into modular Kitchen[cite: 12].
  4. Turnaround at Staircase Core (Column C7)[cite: 3, 9].
  5. Smooth continuous ascent along the 4-winder staircase[cite: 5, 9, 17].
  6. First-floor living hall circulation[cite: 9, 17].
  7. Cantilevered front balcony view looking outward[cite: 1, 9, 17].
  8. Mumty core transit to open rooftop terrace[cite: 9, 17].

### Step 4: Rendering & Video Export

- Execute `blender_scripts/render_tour.py` with the appropriate profile[cite: 9]:
  - **Draft Preview:** EEVEE Next engine, 50% resolution (720p), GTAO enabled, fast preview turnaround[cite: 9].
  - **Master Production:** Cycles engine (GPU/OptiX/HIP enabled), 128 samples with denoising, 1080p/4K @ 30 fps, exported directly to MP4 (H.264)[cite: 9].

---

## 4. Documentation & Synchronization Discipline

Whenever camera waypoints, lighting angles, or scene presets are updated:

1. Locate the corresponding markdown section via `docs/index.md` (e.g., `docs/02_ground_floor.md`, `docs/03_first_floor.md`, or `walkthrough.md`)[cite: 2, 5, 13].
2. Update the documented camera sequence, waypoint table, or material schedules[cite: 2, 9].
3. Never mark an animation or staging task complete without committing the matching parameter changes in `blender_scripts/`[cite: 2, 9, 13].
