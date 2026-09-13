## 29. Sitout Area Electrical Pipelines Completion & Full Electrical Network Visualization (Walls Hidden)

Per user directive (*"wait first complete the electical wrining pipe lines one by one rooms first start with sitout area, hide other walls show the all electical pipe lines"*), the electrical conduit infrastructure for the **Sitout / Entrance Verandah** has been fully completed and integrated. All 69 opaque masonry walls and opaque slabs across the entire building have been hidden (`Visibility = False`), while columns and beams have been placed in an elegant semi-transparent structural ghost mode (`Transparency = 75`), revealing the complete, unobstructed 3D electrical pipeline network across all rooms.

```carousel
![Focused View of the Sitout Area Showing SB-1 Switchboard, Vertical Chased Wall Drop, and Plinth-to-Ceiling Conduits](C:\Users\prade\.gemini\antigravity\brain\086e9390-dcd1-4cec-9724-3cc5bbdd6a28\sitout_electrical_pipelines_closeup_focused.png)
<!-- slide -->
![Full Building 3D Isometric View (All Walls Hidden) Showing the Complete Multi-Storey Electrical Conduit Network](C:\Users\prade\.gemini\antigravity\brain\086e9390-dcd1-4cec-9724-3cc5bbdd6a28\electrical_pipelines_structural_ghost_iso.png)
<!-- slide -->
![Front Elevation View of Building Showing Plumb Vertical Wall Drops and Aligned Switchboards](C:\Users\prade\.gemini\antigravity\brain\086e9390-dcd1-4cec-9724-3cc5bbdd6a28\electrical_pipelines_front_elevation_ghost.png)
<!-- slide -->
![Direct Top Plan View Showing Room-by-Room Slab Conduit Distribution](C:\Users\prade\.gemini\antigravity\brain\086e9390-dcd1-4cec-9724-3cc5bbdd6a28\electrical_pipelines_top_plan_ghost.png)
```

### 29.1 Sitout Area Electrical Components Added

1. **Sitout Entrance Switchboard (`SB-1`):**
   - **Host Substrate:** Solid brick masonry pier on `Living_Room_Wall_Main_Door` (outer face facing Sitout verandah at $Y = 1714.5\text{ mm}$), positioned right of the main entrance door between structural column `Col_East_Sitout` ($X = 228.6\text{ mm}$) and the teak main door frame ($X = 515.55\text{ mm}$).
   - **Plan Coordinates:** Centered at $X = 370.0\text{ mm}$, $Y = 1707.0\text{ mm}$ ($Y \in [1699.5, 1714.5\text{ mm}]$).
   - **Mounting Elevation:** Centered at $Z = 2151.9\text{ mm}$ ($+1207.0\text{ mm}$ AFF from finished sitout floor at $Z = 944.9\text{ mm}$), matching ergonomic switchboard standards across the building.
   - **Faceplate & Rockers:** 4-Module pearl white modular plate ($150 \times 15 \times 75\text{ mm}$) housing 4 modular charcoal switch/socket blocks:
     - Switch 1: Sitout Central Ceiling Downlight Pot ($857.0, 857.0\text{ mm}$).
     - Switch 2: Front Entrance Canopy Recessed Spotlight ($850.0, -300.0\text{ mm}$).
     - Switch 3: East Side Portico Canopy Recessed Spotlight ($-225.0, 970.0\text{ mm}$).
     - Switch 4 & Socket: Weatherproof outdoor convenience power socket (IP44, 6A/16A).

2. **Vertical Chased Wall Conduit Drop to `SB-1` (`Electrical_Slab_Wall_Drops`):**
   - $25\text{ mm}$ OD heavy-duty rigid PVC pipe finished in **Emerald Green (`#10AC84`)**.
   - Chased vertically inside the brick pier at $(X = 370.0\text{ mm}, Y = 1720.0\text{ mm})$ from ceiling slab level $Z = 4020.0\text{ mm}$ down to the top knockout of `SB-1` at $Z = 2189.4\text{ mm}$ (Length: $1830.6\text{ mm}$).

3. **Ceiling Slab Conduit Runs for Sitout (`Electrical_Slab_Conduit_Network`):**
   - $25\text{ mm}$ OD heavy-duty rigid PVC pipe finished in **Safety Orange (`#FF7675` / `(1.0, 0.451, 0.0)`)**:
     - **Run S1 (Power Feed to SB-1 Drop):** Direct slab branch from Sitout Ceiling Light Pot $(857.0, 857.0, 4020.0\text{ mm})$ to `SB-1` vertical drop $(370.0, 1720.0, 4020.0\text{ mm})$ (Length: $991.6\text{ mm}$).
     - **Run S2 (Front Canopy Spotlight Feed):** Extends north from Sitout Ceiling Light Pot $(857.0, 857.0, 4020.0\text{ mm})$ through the front beam core into the Sitout Front Canopy Slab to the Front Recessed Spotlight at $(850.0, -300.0, 4020.0\text{ mm})$ (Length: $1157.0\text{ mm}$).
     - **Run S3 (East Portico Canopy Spotlight Feed):** Extends east from Sitout Ceiling Light Pot $(857.0, 857.0, 4020.0\text{ mm})$ through the east lintel beam into the East Portico Canopy Slab to the East Recessed Spotlight at $(-225.0, 970.0, 4020.0\text{ mm})$ (Length: $1087.9\text{ mm}$).
     - **Run S4 (Outdoor Plinth & Gate Light Feed):** Drops vertically from `SB-1` bottom knockout down to plinth level $Z = 945.0\text{ mm}$, then routes horizontally along the Sitout compound wall base to $(X = 100.0\text{ mm}, Y = 100.0\text{ mm}, Z = 945.0\text{ mm})$ to provide power for the gate pillar lights and floating granite step LEDs.

4. **1:1 Twin Synchronization on First Floor Balcony:**
   - Exact matching components added to `FF_Electrical_Switchboard_Plates`, `FF_Electrical_Switchboard_Rocker_Switches`, `FF_Electrical_Slab_Wall_Drops`, and `FF_Electrical_Slab_Conduit_Network` shifted by $\Delta Z = +3173.0\text{ mm}$:
     - `FF_SB-1` plate & 4 rockers at $(370.0, 1707.0, 5324.9\text{ mm})$.
     - Vertical drop from $Z = 7193.0\text{ mm}$ down to $Z = 5362.4\text{ mm}$.
     - 3 slab conduit feeds connecting the Balcony Ceiling Pot to `FF_SB-1`, Front Balcony Canopy Spotlight, and East Canopy Spotlight.

### 29.2 Complete Building Electrical Network Visibility Status

* **Walls Hidden:** 69 opaque brick masonry and partition walls across Ground Floor, First Floor, and Mumty Tower hidden (`Visibility = False`).
* **Slabs Optimized:** Monolithic intermediate and rooftop slabs hidden from view; Mumty roof slab hidden.
* **Electrical System Fully Active & Visible:** All 41 electrical components set to 100% visible:
  - Ground Floor: 22 slab conduit runs, 21 vertical wall drops, 19 switchboard plates, 29 rocker switches/sockets, 12 downlight pots, 3 fan boxes, 1 staircase wall light, CCTV conduit runs, and canopy spotlight bezels.
  - First Floor: 19 slab conduit runs, 20 vertical wall drops, 18 switchboard plates, 27 rocker switches/sockets, 12 downlight pots, 3 fan boxes, 1 staircase wall light, EB mains riser, and UPS feeder conduit.
* **Master CAD Model:** `HomeConstruction.FCStd` saved and recomputed (0 cyclic errors, 0 invalid shapes).

---
