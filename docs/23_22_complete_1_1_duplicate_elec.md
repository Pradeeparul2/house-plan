## 22. Complete 1:1 Duplicate Electrical System Alignment (Ground Floor to First Floor)

Following the comprehensive deviation audit, the First Floor electrical infrastructure was updated to be an **exact 1:1 vertical duplicate** of the Ground Floor design, elevated by exactly the structural floor-to-floor height ($\Delta Z = +3173.0\text{ mm}$):

```carousel
![Front Elevation of Two-Storey Structure Showing 100% Plumb Vertical Symmetrical Electrical Infrastructure](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\two_storey_electrical_1to1_duplicate_front.png)
<!-- slide -->
![Isometric 3D Perspective of Fully Synchronized Two-Storey Electrical and Conduit Network](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\two_storey_electrical_1to1_duplicate_iso.png)
<!-- slide -->
![Ground Floor Top-View Electrical Layout Plan](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\gf_electrical_plan_final_duplicate.png)
<!-- slide -->
![First Floor Top-View Electrical Layout Plan (Identical 1:1 Geometry to Ground Floor)](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\ff_electrical_plan_final_duplicate.png)
```

### 22.1 Synchronized Electrical Component Schedules

#### A. Ceiling Fan Boxes (`FF_Electrical_Slab_Fan_Boxes` - 3 Units)
Identical $(X, Y)$ coordinates to Ground Floor, elevated to Roof Slab Soffit ($Z = 7167.9\text{ mm}$):
1. **Living Room Fan:** $(2514.6, 3257.4\text{ mm})$
2. **Master Bedroom Fan:** $(3480.0, 6070.0\text{ mm})$
3. **Kitchen Fan:** $(1050.0, 6325.0\text{ mm})$

#### B. Ceiling Slab Downlights (`FF_Electrical_Slab_Light_Pots` - 12 Units)
Identical $(X, Y)$ coordinates to Ground Floor, elevated to Roof Slab Soffit ($Z = 7165.4\text{ mm}$):
* **Living Room (4 Downlights):** $(1200, 2500)$, $(3800, 2500)$, $(1200, 4000)$, $(3800, 4000\text{ mm})$
* **Master Bedroom (2 Downlights):** $(2600, 5400)$, $(4300, 5400\text{ mm})$
* **Kitchen (2 Downlights):** $(1050, 5550)$, $(1050, 7100\text{ mm})$
* **Toilet (2 Downlights):** $(4350, 950)$, $(3435, 950\text{ mm})$
* **Dining / Stair Corridor (2 Downlights):** $(750, 4750)$, $(1350, 4750\text{ mm})$

#### C. Modular Concealed Switchboards (`FF_Electrical_Switchboard_Plates` - 18 Units)
All 18 Ground Floor switchboard plates duplicated at $\Delta Z = +3173.0\text{ mm}$:
1. **`FF_MDB`** (8-Way SPN Main DB): $(1600.0, 1930.0\text{ mm})$, $Z = 5427.4 - 5747.4\text{ mm}$
2. **`FF_SB-0`** (Living Room Main Switchboard): $(1700.0, 1937.5\text{ mm})$, $Z = 5324.9\text{ mm}$
3. **`FF_SB-1`** (North Balcony Wall Switchboard): $(2275.0, 797.5\text{ mm})$, $Z = 5324.9\text{ mm}$
4. **`FF_SB-2`** (Living Room South Wall): $(1762.5, 2117.5\text{ mm})$, $Z = 5362.4\text{ mm}$
5. **`FF_SB-3`** (Living TV Media Console - Lower): $(4845.8, 3250.0\text{ mm})$, $Z = 4678.0\text{ mm}$
6. **`FF_SB-17`** (Living TV Display - Upper): $(4845.8, 3275.0\text{ mm})$, $Z = 5268.0\text{ mm}$
7. **`FF_SB-4`** (Dining Area Entry): $(1925.0, 4697.5\text{ mm})$, $Z = 5324.9\text{ mm}$
8. **`FF_SB-5`** (Dining Area South Wall): $(1867.5, 4975.0\text{ mm})$, $Z = 5362.4\text{ mm}$
9. **`FF_SB-6`** (Kitchen Working Countertop): $(222.5, 6300.0\text{ mm})$, $Z = 5224.9\text{ mm}$
10. **`FF_SB-7`** (Kitchen Utility / Fridge - South Wall): $(1837.5, 7357.5\text{ mm})$, $Z = 4574.9\text{ mm}$
11. **`FF_SB-8`** (Bedroom Entry - West Jamb): $(2107.5, 4925.0\text{ mm})$, $Z = 5362.4\text{ mm}$
12. **`FF_SB-9`** (Bedroom Bedside Left - South Wall): $(2400.0, 7462.5\text{ mm})$, $Z = 4824.9\text{ mm}$
13. **`FF_SB-10`** (Bedroom Bedside Right - South Wall): $(4575.0, 7462.5\text{ mm})$, $Z = 4824.9\text{ mm}$
14. **`FF_SB-11`** (Bedroom Wardrobe / Study Desk): $(2937.5, 4692.5\text{ mm})$, $Z = 5174.9\text{ mm}$
15. **`FF_SB-12`** (Toilet Entry): $(3807.5, 1850.0\text{ mm})$, $Z = 5324.9\text{ mm}$
16. **`FF_SB-13`** (Toilet Geyser Point): $(4757.5, 1260.0\text{ mm})$, $Z = 5474.9\text{ mm}$
17. **`FF_SB-14`** (Balcony Entrance): $(1987.5, 247.5\text{ mm})$, $Z = 5324.9\text{ mm}$
18. **`FF_SB_UPS`** (Dedicated UPS Backup Socket - East Loft): $(157.4, 2325.0\text{ mm})$, $Z = 6475.5\text{ mm}$

#### D. Vertical Wall Conduits (`FF_Electrical_Slab_Wall_Drops` - 19 Runs)
All 19 continuous vertical rigid PVC wall conduit pipe runs dropping from the ceiling slab ($Z = 7193.0\text{ mm}$) into each switchbox knockout on the First Floor, exactly matching the Ground Floor vertical drops ($Z = 4020.0\text{ mm}$).

#### E. Ceiling Slab Conduit Network (`FF_Electrical_Slab_Conduit_Network` - 15 Runs)
The 15 ceiling slab conduit runs on the First Floor roof slab are an exact $Z$-shifted duplicate ($\Delta Z = +3173.0\text{ mm}$) of the Ground Floor slab network.

#### F. Independent First Floor Services Preserved
* **Dedicated EB Service Mains Riser (`FF_EB_Service_Mains_Riser`):** Preserved in Safety Magenta, supplying the First Floor MDB directly from the outdoor meter board via Column C2.
* **Dedicated First Floor UPS System (`FF_UPS_Power_Backup_Model` & `FF_UPS_Conduit_Pipeline`):** Preserved on the East utility loft, connected directly to `FF_MDB` and `FF_SB_UPS`.
* **Zero CCTV on First Floor:** CCTV surveillance remains strictly confined to the Ground Floor perimeter.

---
