## 51. First Floor Stairs Wall Light Pipeline — Seamless Jointing (Gap Elimination)

Following client observation (*"First floor stairs wall light not jointed with the pipeline i see some gap"*), the vertical chased wall drop conduit feeding the First Floor stairs mid-landing wall light was inspected, lengthened, and seamlessly jointed into the fixture base in `HomeConstruction.FCStd`.

```carousel
![First Floor Stairs Wall Light Before vs After](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/ff_stair_light_before_after.png)
<!-- slide -->
![First Floor Stairs Wall Light 3D Verification](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/ff_stair_light_connected_annotated.png)
```

### 51.1 Root Cause of the 801mm Gap
* **Fixture Location:** The First Floor stairs wall light fixture (`FF_Staircase_Wall_Light_Fixture`) is mounted on the east wall of the Headroom (Mumty) tower at $Z = [8750.8, 8950.8]\text{ mm}$ ($+3139.4\text{ mm}$ above the FF mid-landing floor level $Z = 5611.4\text{ mm}$).
* **Legacy Drop Height:** When the conduit was initially mirrored from Ground Floor, it was translated by a flat $+3173\text{ mm}$ offset ($4776.8 + 3173 = 7949.8\text{ mm}$), causing the conduit to terminate at $Z = 7949.8\text{ mm}$.
* **The Resulting Gap:** A vertical void of $801.0\text{ mm}$ ($8750.8 - 7949.8\text{ mm}$) was left between the conduit cutoff and the light fixture base.

### 51.2 Re-Engineered Conduit Geometry
Solid 4 in `FF_Electrical_Slab_Wall_Drops` (located inside `FF_Wall_Drops_Group`) was regenerated with full-height vertical extrusion:

* **Conduit Specification:** $25\text{ mm}$ rigid heavy-duty PVC ($R = 12.5\text{ mm}$).
* **Plan Centerline:** $X = 3800.0\text{ mm}, Y = 970.0\text{ mm}$ (embedded inside the Headroom east brick wall).
* **Elevation Span:** $Z = 7193.0\text{ mm}$ (First Floor ceiling slab soffit) to $Z = 8750.8\text{ mm}$ (exact bottom entry face of `FF_Staircase_Wall_Light_Fixture`).
* **Total Height:** $1557.8\text{ mm}$ (continuous single vertical pipe run).
* **Joint Status:** **$0.0\text{ mm}$ gap**; completely sealed into the fixture junction knock-out.

### 51.3 Quality Verification
* **Shape Integrity:** Validated `s.isValid() = True` on all solids of `FF_Electrical_Slab_Wall_Drops`.
* **Visual Verification:** Rendered from the same perspective and confirmed continuous physical jointing.
* **Document Status:** Recomputed with 0 errors and saved to `HomeConstruction.FCStd`.

---
