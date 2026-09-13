## 35. First Floor Staircase Wall Luminaire Relocation: Headroom Weatherproof Wall (2 Feet Below Headroom Roof Slab)

Following client directive (*"same like change the FF wall light adjustment it will move to Headroom Weatherproof Wall"*), the First Floor staircase luminaire (`FF_Staircase_Wall_Light_Fixture`) and its chased wall conduit connection were re-engineered to mount on the East weatherproof enclosure wall of the Headroom (`Headroom_Walls`), positioned exactly **2 feet ($609.6\text{ mm}$)** below the soffit of the `Headroom_Roof_Slab`:

````carousel
![FreeCAD Viewport Showing FF Staircase Luminaire Relocated to Headroom Weatherproof Wall 2ft Below Roof Slab](C:\Users\prade\.gemini\antigravity\brain\086e9390-dcd1-4cec-9724-3cc5bbdd6a28\headroom_weatherproof_wall_light_annotated.png)
<!-- slide -->
![Close-Up FreeCAD View of Sconce on Headroom Weatherproof Wall and Chased Rigid Conduit](C:\Users\prade\.gemini\antigravity\brain\086e9390-dcd1-4cec-9724-3cc5bbdd6a28\crop_headroom_wall_light.png)
````

### 35.1 Mathematical Elevation & Coordinate Alignment
1. **Headroom Structure & Roof Level:**
   - **Headroom Wall Enclosure:** $X \in [1714.5, 3810.0]$, $Y \in [0, 1866.9]$, $Z \in [7260.4, 9460.4\text{ mm}]$ ($2.2\text{ m}$ height).
   - **Headroom Roof Slab Soffit:** $Z_{\text{soffit}} = \mathbf{9460.4\text{ mm}}$ ($125\text{ mm}$ RCC slab, top $Z = 9585.4\text{ mm}$).
   - **Continuous Lintel Band:** $Z \in [8960.4, 9110.4\text{ mm}]$ (depth $150\text{ mm}$).
2. **Exact 2-Foot ($609.6\text{ mm}$) Drop Calculation:**
   $$Z_{\text{center}} = 9460.4\text{ mm} - 609.6\text{ mm} = \mathbf{8850.8\text{ mm}}$$
3. **Luminaire Fixture Geometry ($H = 200\text{ mm}$):**
   - **Sconce Bounding Box:**
     - $X \in [3745.0, 3810.0\text{ mm}]$ (flush against East wall plaster face, projection $65\text{ mm}$).
     - $Y \in [910.0, 1030.0\text{ mm}]$ (width $120\text{ mm}$, centered at $Y = 970.0\text{ mm}$, plumb with GF light).
     - $Z \in [8750.8, 8950.8\text{ mm}]$ (height $200\text{ mm}$, centered at $Z = 8850.8\text{ mm}$).
   - **Clearance to Lintel Band:** Top of sconce ($8950.8\text{ mm}$) sits comfortably $10\text{ mm}$ below the lintel soffit ($8960.4\text{ mm}$), avoiding rebar conflicts.
   - **Drop from Roof Soffit:** $9460.4 - 8850.8 = \mathbf{609.6\text{ mm}}\; (2'\text{-}0")$.

### 35.2 Concealed Masonry Conduit Run (`FF_Electrical_Slab_Wall_Drops`)
* **Host Solid:** Solid 18 of `FF_Electrical_Slab_Wall_Drops`.
* **Conduit Specification:** $25\text{ mm}$ OD heavy-duty rigid PVC in **Safety Emerald Green (`#10AC84`)**.
* **Path Routing:**
  1. Branches from the Terrace level at $(X = 3800.0, Y = 1720.0, Z = 7193.0\text{ mm})$.
  2. Runs horizontally along the East wall chase to $Y = 970.0\text{ mm}$.
  3. Rises vertically inside the chased masonry of `Headroom_Walls` (East wall) from $Z = 7193.0\text{ mm}$ up to $Z = 8750.8\text{ mm}$ entering directly into the bottom knockout of `FF_Staircase_Wall_Light_Fixture`.

### 35.3 Multi-Storey Electrical Architecture Summary
* **Ground Floor Staircase Luminaire:** Centered at $Z = 4876.8\text{ mm}$ ($2'\text{-}0"$ below `FF_Stair_Mid_Landing` soffit).
* **Headroom Staircase Luminaire:** Centered at $Z = 8850.8\text{ mm}$ ($2'\text{-}0"$ below `Headroom_Roof_Slab` soffit).
* **Master CAD Model:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd) (424 objects, 100% valid solids, 0 errors).
---
