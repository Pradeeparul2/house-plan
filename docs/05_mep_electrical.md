# 05. MEP Electrical Specification & Modular Switchbox Schedule

> [!NOTE]
> **Discipline:** MEP & Electrical Engineering  
> **Authoritative BIM Model:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Applicable Codes:** IS 732: 2019, IS 456: 2000 (Clause 26), NBC 2016 Part 8 Section 2, IS 2667 / IS 3419  
> **Parametric Automation Engine:** [`tools/audit_and_fix_mep_electrical.py`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/tools/audit_and_fix_mep_electrical.py)

---

## 1. Executive Engineering Summary

Following the metric modular standardization of all exterior envelope walls to **200.0 mm (8″ nominal)** and interior partition walls to **100.0 mm (4″ nominal)**, a comprehensive MEP Electrical audit was performed on `HomeConstruction.FCStd`.
All modular switchboard assemblies (`SB-1` through `SB-16`, `DB_GF`, `DB_FF`) were audited, verified flush against AAC masonry walls with **0.0 mm air gap**, calibrated for ergonomic mounting heights per NBC 2016 Part 8, and checked for **$\ge 150.0\text{ mm}$ clear horizontal distance** from concrete column cores (`C1` through `C8`).
All degenerate ghost solids were purged, overlapping pot boxes de-duplicated, and **34 circular deep PVC ceiling junction boxes** ($65\text{ mm dia} \times 60\text{ mm depth}$) were placed at slab conduit intersection nodes and wall chase transition points.

---

## 2. Master Modular Switchbox Alignment Schedule

| Box ID | Room / Functional Space | Host Wall Solid | Wall Type & Face | Final Coordinates $(X, Y, Z)$ [mm] | Mounting Status & Elevation Standard | Column Clearance |
| :--- | :--- | :--- | :--- | :---: | :--- | :---: |
| **`SB-1`** | Sitout Verandah Entrance | `Living_Room_Wall_Main_Door` | 100mm Partition (North face) | $(370.0, 1714.5, 2114.4)$ | Flush on wall plaster; $+1200\text{ mm}$ AFF | $>1200\text{ mm}$ |
| **`SB-2`** | Living Room Stair Entrance Foyer | `Wall_Stair_SE_SW` | 100mm Partition (South face) | $(2050.0, 1814.5, 2114.4)$ | Flush on wall plaster; $+1200\text{ mm}$ AFF | $>1500\text{ mm}$ from C7 |
| **`SB-3`** | Living Room Upper TV / Soundbar Console | `Living_Room_Wall_West` | 200mm Outer (Interior face) | $(4829.2, 3625.0, 2050.0)$ | Flush on wall plaster; $+1135.6\text{ mm}$ AFF | $202.2\text{ mm}$ from C5 ($\ge 150\text{ mm}$) |
| **`SB-4`** | Living Room Stair Wall South Console | `Wall_Stair_SE_SW` | 100mm Partition (South face) | $(3560.0, 1814.5, 2114.4)$ | Flush on wall plaster; $+1200\text{ mm}$ AFF | $>1600\text{ mm}$ from C5 |
| **`SB-STAIR1`**| Staircase Mid-Landing & Outdoor Master | `Wall_Stair_SE_SW` | 100mm Partition (North face) | $(2017.5, 1714.5, 2525.9)$ | Flush under-stair landing control | $>1500\text{ mm}$ |
| **`SB-UTIL`** | Under-Stair Utility Station (Washer/Pump)| `Wall_Stair_SE_SW` | 100mm Partition (North face) | $(3050.0, 1714.5, 1987.5)$ | Flush on wall plaster; $+1073.1\text{ mm}$ AFF | $>800\text{ mm}$ |
| **`SB-9`** | Master Bedroom Study / Entrance | `Bedroom_Wall_North` | 100mm Partition (South face) | $(3325.0, 4626.0, 2114.4)$ | Flush on wall plaster; $+1200\text{ mm}$ AFF | $>1800\text{ mm}$ from C5 |
| **`SB-10`** | Master Bedroom Bedside Console | `Bedroom_Wall_South` | 200mm Outer (Interior face) | $(2630.0, 7420.0, 1564.4)$ | Flush on wall plaster; $+650.0\text{ mm}$ AFF | **$150.0\text{ mm}$ clear of C2** |
| **`SB-AC`** | Master Bedroom 20A AC Isolator | `Bedroom_Wall_East` | 100mm Spine (West face) | $(2035.2, 7000.0, 3262.5)$ | Flush on wall plaster; $+2348.1\text{ mm}$ AFF | $>1400\text{ mm}$ from C2 |
| **`SB-12`** | Ground Floor Toilet Geyser & Exhaust | `Toilet_Wall_West` | 200mm Outer (Interior face) | $(4829.2, 1260.0, 2650.0)$ | Flush on wall plaster; $+1735.6\text{ mm}$ AFF | $900.0\text{ mm}$ from C8 |
| **`SB-13`** | Kitchen Main Entrance Console | `Bedroom_Wall_East` | 100mm Spine (East face) | $(1935.2, 4975.0, 2114.4)$ | Flush on kitchen aisle face; $+1200\text{ mm}$ AFF | $>1800\text{ mm}$ |
| **`SB-14`** | Kitchen Food Prep Counter Appliances | `Kitchen_Wall_East` | 200mm Outer (Interior face) | $(200.0, 5715.0, 1914.4)$ | Flush on wall; $+1000\text{ mm}$ AFF ($+150\text{ mm}$ above counter) | $>1500\text{ mm}$ from C1 |
| **`SB-15`** | Kitchen Refrigerator & RO Purifier | `Kitchen_Wall_South` | 200mm Outer (Interior face) | $(1100.0, 7420.0, 1976.9)$ | Flush on wall plaster; $+1062.5\text{ mm}$ AFF | $725.0\text{ mm}$ from C1 |
| **`SB-16`** | Living Room Lower TV Media Power & AV | `Living_Room_Wall_West` | 200mm Outer (Interior face) | $(4829.2, 3625.0, 1460.0)$ | Flush inside console cabinet; $+545.6\text{ mm}$ AFF | $152.2\text{ mm}$ from C5 ($\ge 150\text{ mm}$) |
| **`SB-16 (Loft)`**| Inverter & Tech Loft Hub (East Wall) | `Living_Room_Wall_East` | 200mm Outer (Interior face) | $(200.0, 2325.0, 3260.0)$ | Flush on wall plaster; $+2345.6\text{ mm}$ AFF | $647.8\text{ mm}$ from C4 |
| **`DB_GF`** | Ground Floor Main Distribution Board | `Living_Room_Wall_East` | 200mm Outer (Interior face) | $(200.0, 2150.0, 2350.0)$ | Flush enclosure, center $+1435.6\text{ mm}$ AFF | $747.8\text{ mm}$ from C4 |

---

## 3. First Floor Modular Switchbox Schedule

| Box ID | Room / Functional Space | Host Wall Solid | Final Coordinates $(X, Y, Z)$ [mm] | Mounting Status & Elevation Standard | Column Clearance |
| :--- | :--- | :--- | :---: | :--- | :---: |
| **`FF_SB-1`** | FF Living Room Master Entrance | `FF_Living_Room_Wall_Main_Door` | $(1762.5, 2110.0, 5362.4)$ | Flush on wall plaster; $+1275\text{ mm}$ AFF | $>1600\text{ mm}$ |
| **`FF_SB-2`** | FF Living Room Stair Wall Entry | `FF_Wall_Stair_SE_SW` | $(2050.0, 1814.5, 5573.9)$ | Flush on wall plaster; $+1486.5\text{ mm}$ AFF | $>1500\text{ mm}$ |
| **`FF_SB-3`** | FF Upper TV Display Console | `FF_Living_Room_Wall_West` | $(4829.2, 3625.0, 5268.0)$ | Flush on wall plaster; $+1180.6\text{ mm}$ AFF | $202.2\text{ mm}$ from C5 |
| **`FF_SB-4`** | FF Living Room Stair Wall South | `FF_Wall_Stair_SE_SW` | $(3560.0, 1814.5, 5573.9)$ | Flush on wall plaster; $+1486.5\text{ mm}$ AFF | $>1600\text{ mm}$ |
| **`FF_SB-9`** | FF Bedroom Study / Entrance | `FF_Bedroom_Wall_North` | $(3325.0, 4626.0, 5324.9)$ | Flush on wall plaster; $+1237.5\text{ mm}$ AFF | $>1800\text{ mm}$ |
| **`FF_SB-10`**| FF Bedroom Bedside Console | `FF_Bedroom_Wall_South` | $(2630.0, 7420.0, 4737.4)$ | Flush on wall plaster; $+650.0\text{ mm}$ AFF | **$150.0\text{ mm}$ clear of C2** |
| **`FF_SB-AC`**| FF Bedroom 20A AC Isolator | `FF_Bedroom_Wall_East` | $(2035.2, 7000.0, 6473.0)$ | Flush on wall plaster; $+2385.6\text{ mm}$ AFF | $>1400\text{ mm}$ |
| **`FF_SB-12`**| FF Toilet Geyser & Exhaust | `FF_Toilet_Wall_West` | $(4829.2, 1260.0, 5865.5)$ | Flush on wall plaster; $+1778.1\text{ mm}$ AFF | $900.0\text{ mm}$ from C8 |
| **`FF_SB-13`**| FF Kitchen Entrance Console | `FF_Bedroom_Wall_East` | $(1935.2, 4975.0, 5362.4)$ | Flush on wall plaster; $+1275\text{ mm}$ AFF | $>1800\text{ mm}$ |
| **`FF_SB-14`**| FF Kitchen Food Prep Counter | `FF_Kitchen_Wall_East` | $(200.0, 5715.0, 5087.4)$ | Flush on wall; $+1000\text{ mm}$ AFF ($+150\text{ mm}$ above counter) | $>1500\text{ mm}$ from C1 |
| **`FF_SB-15`**| FF Kitchen Refrigerator / South Wall | `FF_Kitchen_Wall_South` | $(1100.0, 7420.0, 5187.4)$ | Flush on wall plaster; $+1100\text{ mm}$ AFF | $725.0\text{ mm}$ from C1 |
| **`FF_SB-16`**| FF Lower TV Media Console | `FF_Living_Room_Wall_West` | $(4829.2, 3625.0, 4678.0)$ | Flush on wall; $+590.6\text{ mm}$ AFF | **$152.2\text{ mm}$ clear of C5** |
| **`FF_SB-16L`**| FF Tech Loft Hub (East Wall) | `FF_Living_Room_Wall_East` | $(200.0, 2325.0, 6475.5)$ | Flush on wall plaster; $+2388.1\text{ mm}$ AFF | $647.8\text{ mm}$ from C4 |

---

## 4. Ghost & Disconnection Ledger

| Defect ID | Affected Component | Defect Type | Root Cause / Diagnostic | Corrective Action Taken | Resulting Geometry |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **GD-01** | `Electrical_Switchboard_Plates` (Solid 5) | Degenerate Solid | Micro-artifact ($0.2 \times 0.2 \times 0.2\text{ mm}$, Vol $0.00\text{ mm}^3$) left behind from boolean slice. | Pruned via parametric volume filter ($<100\text{ mm}^3$). | Clean compound with 12 valid solids. |
| **GD-02** | `FF_Electrical_Switchboard_Plates` (Solid 7) | Degenerate Solid | Micro-artifact ($0.2 \times 0.2 \times 0.2\text{ mm}$, Vol $0.00\text{ mm}^3$) on First Floor plate compound. | Pruned via parametric volume filter ($<100\text{ mm}^3$). | Clean compound with 15 valid solids. |
| **GD-03** | `Electrical_Slab_Conduit_Network` (Solid 1) | Zero-Length Pipe Sliver | Micro-sliver conduit extrusion ($12.5 \times 0.2 \times 25.0\text{ mm}$, Vol $19.4\text{ mm}^3$) at $X = 3803.7\text{ mm}$. | Pruned via dimension filter ($dY < 0.5\text{ mm}$). | Clean network with 9 valid solids. |
| **GD-04** | `Electrical_Slab_Light_Pots` (Solids 0–3) | Overlapping Duplication | Duplicated 4 living room light pots already defined in `Living_Slab_Light_Pots`. | De-duplicated: removed identical coordinates from composite group. | 11 unique peripheral light pots. |
| **GD-05** | `FF_Electrical_Slab_Light_Pots` (Solids 0–3) | Overlapping Duplication | Duplicated 4 living room light pots already defined in `FF_Living_Slab_Light_Pots`. | De-duplicated: removed identical coordinates from composite group. | 11 unique peripheral light pots. |
| **GD-06** | `FF_SB-16` / `FF_SB-3` TV Console | Alignment Offset | FF TV console was located at $Y = 3600.0\text{ mm}$ ($127.2\text{ mm}$ from `C5`, breaching $150\text{ mm}$ rule). | Shifted $+25.0\text{ mm}$ along $+Y$ to $Y = 3625.0\text{ mm}$. | Coaxial vertical stack with GF TV; $152.2\text{ mm}$ clear of `C5`. |

---

## 5. Circular Deep PVC Junction Box Schedule (IS 2667 / IS 3419)

Standard deep PVC ceiling junction boxes ($65\text{ mm}\text{ OD} \times 60\text{ mm}\text{ depth}$) embedded inside the $125\text{ mm}$ reinforced ceiling slab:
- **Ground Floor:** Embedded at $Z \in [3962.4, 4022.4\text{ mm}]$, underside flush with soffit ($Z = 3962.4\text{ mm}$), top concrete cover $= 65.0\text{ mm}$.
- **First Floor:** Embedded at $Z \in [7135.4, 7195.4\text{ mm}]$, underside flush with soffit ($Z = 7135.4\text{ mm}$), top concrete cover $= 65.0\text{ mm}$.

| Junction Box ID | Floor | Node Coordinates $(X, Y, Z)$ [mm] | Node Type & Connection Description | Structural Clearance |
| :--- | :---: | :---: | :--- | :--- |
| **`JB_GF_LIV_SPINE_1`** | GF | $(2514.6, 2500.0, 3962.4)$ | Living Room South 3-way spine & pot cross-arm | $547.8\text{ mm}$ South of `RB_LIVING_Primary` |
| **`JB_GF_LIV_SPINE_2`** | GF | $(2514.6, 4000.0, 3962.4)$ | Living Room North 3-way spine & pot cross-arm | $723.6\text{ mm}$ North of `RB_LIVING_Primary` |
| **`JB_GF_LIV_TV_BRANCH`**| GF | $(2514.6, 3625.0, 3962.4)$ | Living Room West Wall TV branch T-junction | $348.6\text{ mm}$ North of `RB_LIVING_Primary` |
| **`JB_GF_FOYER_NODE`** | GF | $(2017.5, 1925.0, 3962.4)$ | Foyer / Staircase 3-way distribution node | Clear of columns C7 & C6 |
| **`JB_GF_BED_LOOP`** | GF | $(3191.3, 6070.6, 3962.4)$ | Bedroom ceiling loop central distribution node | Centered in 2-way slab panel |
| **`JB_GF_KIT_HEADER`** | GF | $(1058.5, 5181.6, 3962.4)$ | Kitchen North wall conduit header node | Clear of door/window lintels |
| **`JB_GF_DROP_DB`** | GF | $(200.0, 2150.0, 3962.4)$ | Living East Wall drop above Main DB (`DB_GF`) | Embedded above AAC chase |
| **`JB_GF_DROP_TV`** | GF | $(4844.0, 3625.0, 3962.4)$ | Living West Wall drop above TV Console (`SB-3`/`SB-16`) | Embedded above AAC chase |
| **`JB_GF_DROP_FOYER_SW`**| GF | $(2100.0, 1925.0, 3962.4)$ | Living South Wall drop above Foyer `SB-2` | Embedded above AAC chase |
| **`JB_GF_DROP_SITOUT`** | GF | $(3560.0, 1925.0, 3962.4)$ | Living South-East drop above Sitout `SB-4` | Embedded above AAC chase |
| **`JB_GF_DROP_PARTITION`**| GF | $(1867.5, 4975.0, 3962.4)$ | Living / Dining partition drop to `SB-9` | Embedded above 100mm partition chase |
| **`JB_GF_DROP_BED_BEDSIDE`**| GF | $(2430.0, 7462.5, 3962.4)$ | Bedroom South Wall drop above bedside `SB-10` | $150.0\text{ mm}$ clear of Column C2 |
| **`JB_GF_DROP_BED_ENTRY`**| GF | $(3325.0, 4673.5, 3962.4)$ | Bedroom North Wall drop above entrance `SB-1` | Embedded above 100mm partition chase |
| **`JB_GF_DROP_BED_AC`** | GF | $(2082.7, 7000.0, 3962.4)$ | Bedroom West Wall drop above Split AC point | Embedded above AAC chase |
| **`JB_GF_DROP_STAIR_UTIL`**| GF | $(3050.0, 1707.5, 3962.4)$ | Staircase drop above utility `SB_UTIL` | Embedded above AAC chase |
| **`JB_GF_DROP_KIT_EAST`** | GF | $(140.0, 5715.0, 3962.4)$ | Kitchen East Wall drop above counter `SB-14` | Embedded above AAC chase |
| **`JB_GF_DROP_KIT_SOUTH`**| GF | $(1100.0, 7482.5, 3962.4)$ | Kitchen South Wall drop above fridge `SB-15` | Embedded above AAC chase |
| **`JB_FF_*` (17 Boxes)**| FF | Same $(X, Y)$ at $Z = 7135.4\text{ mm}$ | First Floor ceiling conduit nodes & wall drops | Identical slab core embedding |

---

## 6. Execution Discipline & Quality Sign-Off

* **Air Gap Tolerance:** Strictly $0.0\text{ mm}$ across all 16 modular assemblies.
* **Partition Wall Punch-Through:** $0.0\text{ mm}$ (All $40\text{ mm}$ backboxes maintain $\ge 60\text{ mm}$ residual AAC masonry thickness in $100\text{ mm}$ partition walls).
* **Structural Column Separation:** $\ge 150.0\text{ mm}$ clear from concrete columns C1–C8.
* **Slab Core Cover:** $\ge 60.0\text{ mm}$ concrete cover over the top of all pot boxes and circular junction boxes.
* **BIM Verification:** Recomputed in `HomeConstruction.FCStd` with 0 non-manifold warnings, 0 recompute errors, and 0 invalid shapes.
