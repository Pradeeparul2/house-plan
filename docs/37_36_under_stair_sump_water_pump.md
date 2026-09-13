## 36. Under-Stair Sump Water Pump Motor Switch Integrated into Utility Switchboard (SB-UTIL)

Following client directive (*"can we have motor switch on Stair util box instead of seperate pipeline"*), the electrical design was streamlined by eliminating the redundant external pipeline and standalone starter enclosure. The **1.0 HP Sump Water Pump** motor starter switch is now integrated directly into the modular **Under-Stair Utility Switchboard (`SB-UTIL`)** on `Wall_Stair_SE_SW`.

```carousel
![FreeCAD 3D View Showing Motor Switch Integrated on SB-UTIL with Direct Floor Conduit to Pump Motor](C:\Users\prade\.gemini\antigravity\brain\086e9390-dcd1-4cec-9724-3cc5bbdd6a28\sb_util_integrated_pump_switch_annotated.png)
<!-- slide -->
![Staircase Flight 1 Entrance 100% Clear and Unobstructed for Ascending Pedestrians](C:\Users\prade\.gemini\antigravity\brain\086e9390-dcd1-4cec-9724-3cc5bbdd6a28\stairs_entrance_clear_annotated.png)
```

### 36.1 Streamlined Electrical Architecture
1. **Consolidated Utility Control Point:**
   - **Switchboard ID:** `Staircase_Switchboard_SB_UTIL` (dedicated tree object in `Electrical_Switchboards_Group`, Electric Cyan `#00D2FF`).
   - **Host Wall:** Solid masonry partition wall `Wall_Stair_SE_SW` inside the walk-in utility alcove at $Y = 1714.5\text{ mm}$, centered at $X = 3050.0\text{ mm}$, $Z = 1987.5\text{ mm}$ ($+1073.1\text{ mm}$ AFF, directly above washing machine counter height).
   - **Integrated Modules:**
     - **Module 1 & 2:** $16\text{A}$ Heavy-Duty Switched Socket for **Washing Machine**.
     - **Module 3 & 4:** $16\text{A}$ Heavy-Duty Modular Motor Starter Switch with Neon Status Indicator for **1.0 HP Sump Water Pump**.
2. **Elimination of Redundant Infrastructure:**
   - The separate ceiling-to-starter pipeline (`Pump_Power_Supply_Conduit`) was completely removed.
   - The detached industrial starter box (`Pump_Starter_Panel`) was eliminated, replacing it with the sleek modular switch directly on `SB-UTIL`.
   - Stair Flight 1 entrance ($X = 1714.5\text{ mm}, Y \in [230.0, 950.0\text{ mm}]$) remains **100% wide open and unobstructed**.

### 36.2 Direct Feed Conduit Run (`Pump_Motor_Supply_Conduit`)
* **Host Component:** Added as dedicated parametric object `Pump_Motor_Supply_Conduit` in `Sump_Motor_Group`.
* **Conduit Specification:** $20\text{ mm}$ OD heavy-duty rigid PVC in **Safety Emerald Green (`#10AC84`)**.
* **Routing Path:**
  1. **Source:** Bottom knockout of `SB-UTIL` directly under the motor switch at $(X = 3087.5, Y = 1707.5, Z = 1950.0\text{ mm})$.
  2. **Wall Chase Drop:** Drops vertically inside `Wall_Stair_SE_SW` to floor skirting level $Z = 960.0\text{ mm}$ ($L = 990\text{ mm}$).
  3. **Skirting Run:** Runs along the floor skirting to $X = 2460.0\text{ mm}$ ($L = 627.5\text{ mm}$).
  4. **Floor Transverse Crossing:** Crosses neatly under the staircase floor slab from $Y = 1707.5\text{ mm}$ to $Y = 610.0\text{ mm}$ ($L = 1097.5\text{ mm}$).
  5. **Terminal Box Entry:** Rises vertically from $Z = 960.0\text{ mm}$ up into the bottom entry of `Pump_Terminal_Box` at $(X = 2460.0, Y = 610.0, Z = 1255.0\text{ mm})$ ($L = 295\text{ mm}$).

### 36.3 Master CAD Model Status
* **CAD Master File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)
* **Integrity:** 425 objects, 0 cyclic errors, 100% valid manifold solids.
---
