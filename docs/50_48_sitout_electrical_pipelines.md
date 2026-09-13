## 48. Sitout Electrical Pipelines Checked & Optimized — 100% Orthogonal Grid

Following client instruction (*"now check and optimize the sitout pipelines"*), a thorough diagnostic and re-engineering of the Ground Floor Sitout (Front Porch / Verandah) electrical conduit layout was performed in `HomeConstruction.FCStd`.

```carousel
![Sitout Electrical Pipelines Before vs After](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/sitout_pipelines_before_after.png)
<!-- slide -->
![Sitout Electrical Pipelines 3D Verification](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/sitout_pipelines_optimized_3d_annotated.png)
<!-- slide -->
![Sitout Electrical Pipelines Plan Layout](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/sitout_pipelines_optimized_plan_annotated.png)
```

### 48.1 Diagnostics of Legacy Sitout Layout
Inspection of `Electrical_Slab_Conduit_Network` (Solids 0, 1, and 2) identified severe legacy defects originating from the original front-wall MDB design:
1. **Dangling South Pipe ($1157\text{ mm}$):** Protruded past the roof slab boundary to $Y = -300.1\text{ mm}$, hanging in open mid-air over the granite entrance steps.
2. **Dangling West Pipe ($1083\text{ mm}$):** Protruded to $X = -226.3\text{ mm}$, hanging in open air beyond the east compound wall.
3. **Diagonal Supply Run ($1312\text{ mm}$ at $55.6^\circ$):** Traversed diagonally from the deleted phantom MDB node $(1600.0, 1943.1\text{ mm})$ across the ceiling slab into `Pot 10`.
4. **Diagonal Switchboard Link ($992\text{ mm}$ at $60.5^\circ$):** Traversed diagonally across the Sitout ceiling from `Pot 10` to `Pot 13`.
5. **Slanted Staircase Run ($1495\text{ mm}$ at $78.7^\circ$):** Traversed diagonally across the open staircase airspace from $(1600.0, 1943.1\text{ mm})$ to $(1943.1, 228.6\text{ mm})$.

### 48.2 Re-Engineered Orthogonal Conduit Network ($25\text{ mm}$ PVC, $R = 12.5\text{ mm}, Z = 4020.0\text{ mm}$)
All diagonal and dangling conduits were excised and replaced by a four-branch orthogonal tee-grid embedded within the structural lintel beam and ceiling slab:

1. **Run A — Entrance Beam Header ($Y = 1720.0\text{ mm}$):**
   * **Span:** $X = 370.0\text{ mm} \to 2017.5\text{ mm}$ (Length: $1647.5\text{ mm}$).
   * **Role:** Continuous horizontal trunk line cast inside the Main Entrance Door lintel beam, interconnecting the Sitout Switchboard drop (`Pot 13`), the Sitout Central Downlight branch, and the Staircase switchboard drop.
2. **Run B — Sitout Central Downlight Branch ($X = 857.0\text{ mm}$):**
   * **Span:** $Y = 1720.0\text{ mm} \to 857.0\text{ mm}$ (Length: $863.0\text{ mm}$).
   * **Role:** Clean, perpendicular North-South feeder dropping directly into Sitout Central Downlight `Pot 10` at $(857.0, 857.0\text{ mm})$ (dead center of the verandah).
3. **Run C — Main DB Supply Feeder ($X = 370.0\text{ mm}$):**
   * **Span:** $Y = 1720.0\text{ mm} \to 1925.0\text{ mm}$ (Length: $205.0\text{ mm}$).
   * **Role:** Straight cross-wall link penetrating through the main entrance wall into the Living Room South cross-bar (`LR Net Solid 3`), providing continuous energized supply from the Main Distribution Board.
4. **Run D — Staircase Under-Stair Utility Line ($X = 1943.1\text{ mm}$):**
   * **Span:** $Y = 228.6\text{ mm} \to 1720.0\text{ mm}$ (Length: $1491.4\text{ mm}$).
   * **Role:** Strictly orthogonal North-South run embedded inside the Staircase east partition wall, powering the under-stair sump pump motor and utility points.

### 48.3 Verification & Quality Metrics
* **Boundary Confinement:** All conduits strictly bounded within $X \in [150.1, 3810.0]\text{ mm}$ and $Y \in [228.6, 7469.3]\text{ mm}$; zero mid-air overhangs ($0.0\text{ mm}$ beyond perimeter).
* **Strict Orthogonality:** 100% of conduits are aligned at $90^\circ$ with Cartesian $X$ and $Y$ axes.
* **First Floor Synchronization:** Mirrored updates to `FF_Electrical_Slab_Conduit_Network` at $\Delta Z = +3173.0\text{ mm}$ (validating 0 invalid shapes).
* **Document Status:** Recomputed with 0 errors and saved to `HomeConstruction.FCStd`.

---
