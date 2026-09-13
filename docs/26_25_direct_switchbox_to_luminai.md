## 25. Direct Switchbox-to-Luminaire Staircase Wall Lighting & Slab Infrastructure De-Cluttering

Following client direction, the staircase electrical topology was optimized by routing the wall luminaire **directly from the staircase switchbox** and **completely clearing all slab conduits and ceiling downlight pots** from the staircase ceiling zone on both Ground and First Floors.

```carousel
![Close-Up View of the Staircase Switchbox SB_STAIR1 and Continuous Wall Conduit Rising to the Toilet East Wall Luminaire](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\staircase_wall_light_switchbox_connection.png)
<!-- slide -->
![Isometric Perspective of the Stairwell Showing Clean Ceiling Slab and Wall-Chased Conduit](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\staircase_switchbox_to_wall_light_iso.png)
<!-- slide -->
![Two-Storey Overview Revealing Completely De-Cluttered Staircase Ceiling Slabs on Both Floors](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\two_storey_electrical_staircase_updated_full_iso.png)
```

### 25.1 Removal of Ceiling Slab Conduits & Downlight Pot Boxes
1. **Slab Deep PVC Downlight & Pendant Pot Boxes (Blue) Removed:**
   * **Ground Floor (`Electrical_Slab_Light_Pots`):** Removed Solid 9 centered at $(X = 3435.0\text{ mm}, Y = 950.0\text{ mm}, Z = 3992.4\text{ mm})$. Solid count streamlined from 13 to **12 units** (4 Living, 4 Bedroom, 2 Kitchen, 1 Toilet, 1 Sitout).
   * **First Floor (`FF_Electrical_Slab_Light_Pots`):** Removed Solid 9 centered at $(X = 3435.0\text{ mm}, Y = 950.0\text{ mm}, Z = 7165.4\text{ mm})$. Solid count streamlined from 13 to **12 units**.
   * **Result:** Zero ceiling pots embedded in the staircase soffit slab, eliminating unwanted ceiling downlight holes directly above the stair flight.
2. **Slab 25mm Heavy-Duty PVC Conduit Piping Runs (Orange) Removed:**
   * **Ground Floor (`Electrical_Slab_Conduit_Network`):**
     - Omitted cylinder feed (Face 10 in `Solid 0`) running from $(1943.1, 228.6, 4020.0\text{ mm})$ to the old staircase pot at $(3435.0, 950.0\text{ mm})$.
     - Removed Solid 18 (the ceiling slab feed running along `Toilet_Wall_East` ceiling from $(3810.0, 1828.8\text{ mm})$ to $(3800.0, 970.0\text{ mm})$).
     - Removed Solid 3 (conduit crossing across the staircase flight void).
     - Solid count updated from 19 to **17 runs**.
   * **First Floor (`FF_Electrical_Slab_Conduit_Network`):**
     - Identical removal of the staircase slab conduits, updating from 19 to **17 runs**.
   * **Result:** Staircase ceiling slab and headroom are 100% free of orange conduit pipes.

### 25.2 Direct Wall-Chased Conduit from Staircase Switchbox
Instead of dropping down from the ceiling slab, the staircase wall light now receives its power and switching circuit directly from the dedicated **Staircase Ground Entry Switchboard (`SB_STAIR1` / Plate 14)**:

* **Conduit Specification:** $25\text{ mm}$ OD rigid heavy-duty PVC pipe in **Emerald Green (`#10AC84`)**, chased directly into the masonry wall plaster.
* **Ground Floor Routing Path:**
  1. Exits the top knockout of `SB_STAIR1` at $(X = 1987.5\text{ mm}, Y = 240.0\text{ mm}, Z = 2189.4\text{ mm})$.
  2. Rises vertically along `Wall_Stair_North` to the mid-landing floor level $Z = 2438.4\text{ mm}$ ($+8'\text{-}0"$).
  3. Runs horizontally along the North wall base at $Z = 2438.4\text{ mm}$ to the North-East corner at $(3800.0, 240.0\text{ mm})$.
  4. Turns 90° onto the outer face of `Toilet_Wall_East` and runs along the landing base to $(3800.0, 970.0\text{ mm})$, centered directly beneath the luminaire.
  5. Rises vertically up `Toilet_Wall_East` from $Z = 2438.4\text{ mm}$ to $Z = 3200.0\text{ mm}$, terminating directly into the bottom knockout of `Staircase_Wall_Light_Fixture` ($Z \in [3200.0, 3400.0\text{ mm}]$).
* **First Floor Matching Routing Path:**
  - Exact identical orthogonal geometry shifted by $\Delta Z = +3173.0\text{ mm}$:
  - Connects `FF_SB_STAIR1` at $(1987.5, 240.0, 5362.4\text{ mm})$ along the upper stair landing base and up `Toilet_Wall_East` into `FF_Staircase_Wall_Light_Fixture` at $Z = 6373.0\text{ mm}$.
* **Integrated Component Groups:**
  - Integrated cleanly inside `Electrical_Slab_Wall_Drops` (GF) and `FF_Electrical_Slab_Wall_Drops` (FF), maintaining **20 solid units** per floor after replacing the old ceiling drops.

### 25.3 Model Verification & Document Health
* **Master CAD File:** `HomeConstruction.FCStd`
* **Total Objects:** **422 objects** (unchanged, zero loose objects).
* **Root Hierarchy:** Strictly 3 master root groups (`Ground_Floor_Group`, `First_Floor_Group`, `Master_Rooftop_Terrace_Group`).
* **Validation:** 0 cyclic dependencies, 0 null shapes, 0 recompute errors.


---
