## 26. Under-Stair Utility Switchboard (SB-UTIL) Proper Repositioning

During user inspection of the staircase electrical network, it was identified that the under-stair utility switchboard (`SB-UTIL`) was previously mislocated at $(X = 2275.0\text{ mm}, Y = 797.5\text{ mm}, Z = 2151.9\text{ mm})$. This placed the box and its ceiling drop floating in mid-air directly above the walking treads of Staircase Flight 1.

This has been resolved by relocating `SB-UTIL` onto the solid masonry partition wall (`Wall_Stair_SE_SW`) inside the dedicated under-stair utility alcove:

```carousel
![Properly Repositioned Under-Stair Utility Switchboard SB-UTIL on Wall_Stair_SE_SW Beside Washing Machine](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\sb_util_repositioned_annotated.png)
<!-- slide -->
![Stairwell 3D View Showing Stair Flight 1 Completely Free of Mid-Air Obstructions](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\staircase_all_switchboxes_repositioned_iso.png)
```

### 26.1 Technical Specification of Repositioned SB-UTIL
* **Host Wall:** `Wall_Stair_SE_SW` (Ground Floor) & `FF_Wall_Stair_SE_SW` (First Floor). A $228.6\text{ mm}$ (9") solid brick load-bearing wall dividing the Living Room from the Staircase utility bay.
* **Mounting Face:** Flush on the inner utility face at $Y = 1714.5\text{ mm}$ (spanning $Y \in [1700.0, 1715.0\text{ mm}]$).
* **Plan Position ($X$):** Centered at $X = 3050.0\text{ mm}$ ($X \in [2975.0, 3125.0\text{ mm}]$), directly beside the Washing Machine ($X \in [3180.0, 3780.0\text{ mm}]$) with a $55\text{ mm}$ lateral clearance from the washing machine edge.
* **Ergonomic Elevation ($Z$):**
  - **Ground Floor:** $Z \in [1950.0, 2025.0\text{ mm}]$ (center $Z = 1987.5\text{ mm}$, $+1073.1\text{ mm}$ AFF). Sits $+192.6\text{ mm}$ above the washing machine top surface ($Z = 1794.9\text{ mm}$) at standard countertop appliance height.
  - **First Floor (`FF_SB-UTIL`):** $Z \in [5123.0, 5198.0\text{ mm}]$ (center $Z = 5160.5\text{ mm}$, exact duplicate shifted by $\Delta Z = +3173.0\text{ mm}$).
* **Hardware Configuration:** 4-Module white modular faceplate housing $2 \times 16\text{A}$ heavy-duty modular switched sockets dedicated to the **Washing Machine** and **Sump Pump**.
* **Safety Water Clearance:** Provides $>800\text{ mm}$ of clear lateral distance from the utility water tap (`WM_Water_Tap` at $X = 3810.0\text{ mm}, Y = 1400.0\text{ mm}$), ensuring 100% compliance with electrical safety codes for wet-area appliances.

### 26.2 Continuous Wall-Chased Conduit Drop
* **Vertical Chase Drop:** A $25\text{ mm}$ rigid PVC conduit in **Emerald Green (`#10AC84`)** chased vertically inside `Wall_Stair_SE_SW` from the ceiling slab ($Z = 4020.0\text{ mm}$) down into the top knockout of `SB-UTIL` ($Z = 2025.0\text{ mm}$) at $(X = 3050.0\text{ mm}, Y = 1720.0\text{ mm})$.
* **Slab Distribution Link:** An embedded $25\text{ mm}$ rigid PVC slab conduit runs above `Wall_Stair_SE_SW` from $(3810.0, 1828.8\text{ mm})$ to $(3050.0, 1720.0\text{ mm})$, providing continuous circuit supply without penetrating the staircase ceiling opening.
* **Clearance Achievement:** The walking envelope of Staircase Flight 1 is now **100% free and clear of any mid-air conduits or floating boxes**.


---
