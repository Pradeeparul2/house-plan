## 31. Relocation of Ground Floor Staircase Wall Luminaire to Low-Level Landing Elevation

Following client direction (*"can we move the gf stairs wall light to below 2feet from second flight"*), the Ground Floor staircase wall luminaire (`Staircase_Wall_Light_Fixture`) and its chased wall conduit feed were modified to lower the fixture by exactly **2 feet ($609.6\text{ mm}$)** on `Toilet_Wall_East`:

```carousel
![Isometric 3D Perspective of Staircase Tower Showing Lowered Wall Luminaire Position](C:\Users\prade\.gemini\antigravity\brain\086e9390-dcd1-4cec-9724-3cc5bbdd6a28\staircase_lowered_light_clean_iso.png)
<!-- slide -->
![Front View of the Two Flights Showing the Low-Level Luminaire Illuminating the Second Flight Base](C:\Users\prade\.gemini\antigravity\brain\086e9390-dcd1-4cec-9724-3cc5bbdd6a28\staircase_lowered_light_clean_front.png)
```

### 31.1 Geometric Translation & Architectural Details

* **Previous Position:** Mounted at $Z \in [3200.0, 3400.0\text{ mm}]$ (center $Z = 3300.0\text{ mm}$, $+861.6\text{ mm}$ above mid-landing).
* **New Lowered Position:** Lowered by exactly $610.0\text{ mm}$ ($2'\text{-}0"$) down to $Z \in [2590.0, 2790.0\text{ mm}]$ (center $Z = 2690.0\text{ mm}$).
* **Elevation AFF from Mid-Landing Floor ($Z = 2438.4\text{ mm}$):**
  $$2690.0\text{ mm} - 2438.4\text{ mm} = \mathbf{+251.6\text{ mm}}\; (10")$$
* **Lighting Ergonomics & Foot of Flight 2 Illumination:**
  - The luminaire is now positioned at low-level tread height directly adjacent to the first 2 steps of Second Flight ($Z_{\text{step 1}} = 2590.8\text{ mm}$, $Z_{\text{step 2}} = 2743.2\text{ mm}$).
  - Projects downward and outward across the $180^\circ$ mid-landing turnaround, casting crisp, low-glare foot-level light directly onto the riser transitions where missteps are most likely to occur.
  - Eliminates harsh eye-level glare for people ascending Flight 1 or descending Flight 2.

### 31.2 Continuous Masonry Wall Conduit Adaptation

* **Host Solid:** `Electrical_Slab_Wall_Drops` (Solid 19).
* **Conduit Specification:** $25\text{ mm}$ OD rigid PVC in **Emerald Green (`#10AC84`)**.
* **Routing Path:**
  1. Starts at `SB_STAIR1` top knockout at $(X = 2017.5\text{ mm}, Y = 1714.5\text{ mm}, Z = 2189.4\text{ mm})$.
  2. Rises vertically along `Wall_Stair_SE_SW` to the mid-landing floor datum $Z = 2438.4\text{ mm}$.
  3. Runs horizontally along the landing base to corner $(3800.0, 1714.5\text{ mm})$.
  4. Turns $90^\circ$ onto `Toilet_Wall_East` and runs along the landing base to $(3800.0, 970.0\text{ mm})$.
  5. Rises vertically from $Z = 2438.4\text{ mm}$ directly into the bottom knockout of the lowered fixture at $Z = 2590.0\text{ mm}$ (rise length: $151.6\text{ mm}$).

### 31.3 Document Health & Verification

* **Master Model:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd) saved.
* **Geometric Validation:** 0 cyclic dependencies, 0 null shapes, 0 recompute errors.

---
