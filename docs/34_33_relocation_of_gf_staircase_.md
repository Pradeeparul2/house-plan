## 33. Relocation of GF Staircase Wall Luminaire to 2 Feet Below FF Stair Mid-Landing Slab

Per user instruction (*"can we move the GF staircase wall light to 2feet below the FF Stair Mid-Landing Slab"*), the Ground Floor staircase wall luminaire (`Staircase_Wall_Light_Fixture`) and its chased wall conduit feed were relocated to a high-level stairwell mounting elevation directly under the First Floor Stair Mid-Landing Slab:

```carousel
![Isometric Render of Multi-Storey Staircase Showing GF Wall Light Positioned 2 Feet Below FF Mid-Landing Slab](C:\Users\prade\.gemini\antigravity\brain\086e9390-dcd1-4cec-9724-3cc5bbdd6a28\staircase_light_2ft_below_ff_landing_annotated.png)
<!-- slide -->
![Detailed Close-Up Zoom of the 2-Foot Drop Dimension Below the FF Landing Slab](C:\Users\prade\.gemini\antigravity\brain\086e9390-dcd1-4cec-9724-3cc5bbdd6a28\crop_light_2ft_below_ff_landing.png)
```

### 33.1 Elevation & Ergonomic Rationale
1. **Vertical Circulation Geometry:**
   - **FF Stair Mid-Landing Slab (`FF_Stair_Mid_Landing`):**
     - Bottom Soffit Level: $Z = 5486.4\text{ mm}$ ($+1.399\text{ m}$ above FF floor datum $Z = 4087.4\text{ mm}$).
     - Top Slab Level: $Z = 5611.4\text{ mm}$ ($125\text{ mm}$ RCC monolithic slab).
   - **Exact 2-Foot Drop Calculation:**
     $$Z_{\text{target}} = 5486.4\text{ mm} - 609.6\text{ mm}\; (2'\text{-}0") = \mathbf{4876.8\text{ mm}}$$
   - **Luminaire Geometry ($H = 200\text{ mm}$):**
     - Sconce Housing: $Z \in [4776.8, 4976.8\text{ mm}]$, centered precisely at $Z = 4876.8\text{ mm}$.
     - Distance from top of luminaire to FF slab soffit: $5486.4 - 4976.8 = 509.6\text{ mm}$ ($1'\text{-}8"$).
2. **Clearance AFF from Ground Floor Mid-Landing:**
   - GF Mid-Landing floor level: $Z = 2438.4\text{ mm}$.
   - Clear Mounting Height above landing floor:
     $$4876.8\text{ mm} - 2438.4\text{ mm} = \mathbf{+2438.4\text{ mm}}\; (8'\text{-}0"\text{ AFF})$$
   - Standard architectural mounting height for double-height stairwell sconces, projecting light uniformly across both Flight 1 and Flight 2 while staying completely clear of foot/shoulder contact.

### 33.2 Concealed Masonry Wall Conduit Realignment
* **Host Component:** `Electrical_Slab_Wall_Drops` (Solid 19).
* **Conduit Specification:** $25\text{ mm}$ OD heavy-duty rigid PVC in **Safety Emerald Green (`#10AC84`)**.
* **Path Routing:**
  1. Ascends vertically from `Staircase_Switchboard_SB_STAIR1` ($Z = 2189.4\text{ mm}$) to ceiling level $Z = 4020.0\text{ mm}$.
  2. Runs horizontally along the South partition beam to corner $(X = 3800.0, Y = 1720.0, Z = 4020.0\text{ mm})$.
  3. Turns $90^\circ$ onto `Toilet_Wall_East` to $Y = 970.0\text{ mm}$.
  4. Rises vertically inside the chased brickwork from $Z = 4020.0\text{ mm}$ up to $Z = 4776.8\text{ mm}$ into the bottom knockout of `Staircase_Wall_Light_Fixture`.

### 33.3 Master CAD Model Status
* **CAD Master File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)
* **Object Count:** 424 objects (100% valid solids, 0 cyclic errors).

---
