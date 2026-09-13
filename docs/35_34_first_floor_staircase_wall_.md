## 34. First Floor Staircase Wall Luminaire Relocation: 2 Feet Below Rain Protection Canopy Slab

Following client directive (*"same like change the FF wall light adjustment it will move to rain protection area"*), the First Floor staircase wall luminaire (`FF_Staircase_Wall_Light_Fixture`) and its chased wall conduit connection were re-engineered to mirror the Ground Floor standard, positioning the luminaire exactly **2 feet ($609.6\text{ mm}$)** below the soffit of the Rooftop Rain Protection Canopy Slab (`FF_Stair_North_Canopy_Slab` / Terrace Roof):

```carousel
![Two-Storey FreeCAD Viewport Showing Symmetrical 2-Foot Drops for Both GF and FF Staircase Luminaires](C:\Users\prade\.gemini\antigravity\brain\086e9390-dcd1-4cec-9724-3cc5bbdd6a28\ff_stair_light_rain_protection_annotated.png)
<!-- slide -->
![Close-Up View of First Floor Luminaire Positioned Below the Rain Protection Canopy Slab](C:\Users\prade\.gemini\antigravity\brain\086e9390-dcd1-4cec-9724-3cc5bbdd6a28\crop_ff_light_rain_protection.png)
```

### 34.1 Mathematical Elevation Alignment
1. **Overhead Rain Protection Ceiling Level:**
   - **Canopy / Terrace Roof Slab Soffit:** $Z_{\text{soffit}} = 7135.4\text{ mm}$ (`FF_Stair_North_Canopy_Slab` & `Terrace_Roof_Slab`).
2. **Exact 2-Foot ($609.6\text{ mm}$) Drop:**
   $$Z_{\text{center}} = 7135.4\text{ mm} - 609.6\text{ mm} = \mathbf{6525.8\text{ mm}}$$
3. **Luminaire Geometry ($H = 200\text{ mm}$):**
   - Sconce Housing: $Z \in [6425.8, 6625.8\text{ mm}]$.
   - Top of Fixture to Canopy Soffit: $7135.4 - 6625.8 = 509.6\text{ mm}$ ($1'\text{-}8"$).
   - Center of Fixture to Canopy Soffit: $7135.4 - 6525.8 = \mathbf{609.6\text{ mm}}\; (2'\text{-}0")$.
4. **Elevation AFF from First Floor Mid-Landing:**
   - FF Mid-Landing floor level: $Z = 5611.4\text{ mm}$.
   - Clearance AFF: $6525.8\text{ mm} - 5611.4\text{ mm} = \mathbf{+914.4\text{ mm}}\; (3'\text{-}0"\text{ AFF above landing steps})$.

### 34.2 Concealed Masonry Conduit Run (`FF_Electrical_Slab_Wall_Drops`)
* **Host Solid:** Solid 18 of `FF_Electrical_Slab_Wall_Drops`.
* **Conduit Specification:** $25\text{ mm}$ OD heavy-duty rigid PVC in **Safety Emerald Green (`#10AC84`)**.
* **Routing:**
  1. Branches from the roof slab corridor drop at $(X = 3800.0, Y = 1720.0, Z = 7193.0\text{ mm})$.
  2. Runs horizontally along the East wall chase to $Y = 970.0\text{ mm}$.
  3. Drops vertically through `FF_Toilet_Wall_East` from $Z = 7193.0\text{ mm}$ down to $Z = 6625.8\text{ mm}$ into the top knockout of `FF_Staircase_Wall_Light_Fixture`.

### 34.3 Symmetrical Multi-Storey Staircase Lighting Standard
With both modifications applied, the two-storey building achieves 100% structural and electrical symmetry:
* **Ground Floor:** Luminaire centered at $Z = 4876.8\text{ mm}$ (exactly $2'\text{-}0"$ below FF Stair Mid-Landing Slab soffit $5486.4\text{ mm}$).
* **First Floor:** Luminaire centered at $Z = 6525.8\text{ mm}$ (exactly $2'\text{-}0"$ below Rain Protection Canopy Slab soffit $7135.4\text{ mm}$).
* **CAD Master File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd) (424 objects, 0 errors).
---
