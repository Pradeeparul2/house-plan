# 05. MEP Electrical Specification & Modular Switchbox Schedule

> [!NOTE]
> **Discipline:** MEP & Electrical Engineering  
> **Authoritative BIM Model:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Applicable Codes:** IS 732: 2019, IS 456: 2000 (Clause 26), NBC 2016 Part 8 Section 2  
> **Parametric Automation Engine:** [`tools/snap_switchboxes_to_walls.py`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/tools/snap_switchboxes_to_walls.py)

---

## 1. Executive Engineering Summary

Following the metric modular standardization of all exterior envelope walls to **200.0 mm (8″ nominal)** and interior partition walls to **100.0 mm (4″ nominal)**, all floating and buried modular switchboard assemblies (`SB-1` through `SB-16`, `DB_GF`, `DB_FF`) have been parametrically audited and re-anchored flush against their target host AAC masonry wall faces with **0.0 mm air gap** and **0.0 mm through-wall protrusion**.

---

## 2. Master Modular Switchbox Alignment Schedule

| Box ID | Room / Functional Space | Host Wall Solid | Wall Type & Face | Previous Gap (mm) | Final Coordinates $(X, Y, Z)$ [mm] | Mounting Status & Elevation Standard |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **`SB-1`** | Sitout Verandah Entrance | `Living_Room_Wall_Main_Door` | 100mm Partition (North face) | $0.0$ | $(370.0, 1714.5, 2114.4)$ | Flush on wall plaster; $+1200	ext{ mm}$ AFF |
| **`SB-2`** | Living Room Stair Entrance Foyer | `Wall_Stair_SE_SW` | 100mm Partition (South face) | $+128.6$ (Floating) | $(2050.0, 1814.5, 2114.4)$ | Flush on wall plaster; $+1200	ext{ mm}$ AFF |
| **`SB-3`** | Living Room Upper TV / Soundbar Console | `Living_Room_Wall_West` | 200mm Outer (Interior face) | $-21.6$ (Buried) | $(4829.2, 3625.0, 2050.0)$ | Flush on wall plaster; $+1135.6	ext{ mm}$ AFF; $>150	ext{ mm}$ clear of C5 |
| **`SB-4`** | Living Room Stair Wall South Console | `Wall_Stair_SE_SW` | 100mm Partition (South face) | $+128.6$ (Floating) | $(3560.0, 1814.5, 2114.4)$ | Flush on wall plaster; $+1200	ext{ mm}$ AFF |
| **`SB-STAIR1`**| Staircase Mid-Landing & Outdoor Master | `Wall_Stair_SE_SW` | 100mm Partition (North face) | $0.0$ | $(2017.5, 1714.5, 2525.9)$ | Flush under-stair landing control |
| **`SB-UTIL`** | Under-Stair Utility Station (Washer/Pump)| `Wall_Stair_SE_SW` | 100mm Partition (North face) | $+0.5$ (Flush) | $(3050.0, 1714.5, 1987.5)$ | Flush on wall plaster; $+1073.1	ext{ mm}$ AFF |
| **`SB-9`** | Master Bedroom Study / Entrance | `Bedroom_Wall_North` | 100mm Partition (South face) | $+47.5$ (Floating) | $(3325.0, 4626.0, 2114.4)$ | Flush on wall plaster; $+1200	ext{ mm}$ AFF |
| **`SB-10`** | Master Bedroom Bedside Console | `Bedroom_Wall_South` | 200mm Outer (Interior face) | $-50.0$ (Buried) | $(2600.0, 7420.0, 1614.4)$ | Flush on wall plaster; $+700	ext{ mm}$ AFF; $>220	ext{ mm}$ clear of C2 |
| **`SB-AC`** | Master Bedroom 20A AC Isolator | `Bedroom_Wall_East` | 100mm Spine (West face) | $+47.5$ (Floating) | $(2035.2, 7000.0, 3262.5)$ | Flush on wall plaster; $+2348.1	ext{ mm}$ AFF |
| **`SB-12`** | Ground Floor Toilet Geyser & Exhaust | `Toilet_Wall_West` | 200mm Outer (Interior face) | $-47.6$ (Buried) | $(4829.2, 1260.0, 2650.0)$ | Flush on wall plaster; $+1735.6	ext{ mm}$ AFF |
| **`SB-13`** | Kitchen Main Entrance Console | `Bedroom_Wall_East` | 100mm Spine (East face) | $+60.2$ (Floating) | $(1935.2, 4975.0, 2114.4)$ | Flush on kitchen aisle face; $+1200	ext{ mm}$ AFF |
| **`SB-14`** | Kitchen Food Prep Counter Appliances | `Kitchen_Wall_East` | 200mm Outer (Interior face) | $-47.6$ (Buried) | $(200.0, 5715.0, 2026.9)$ | Flush on wall plaster; $+162.5	ext{ mm}$ above granite counter |
| **`SB-15`** | Kitchen Refrigerator & RO Purifier | `Kitchen_Wall_South` | 200mm Outer (Interior face) | $-50.0$ (Buried) | $(1100.0, 7420.0, 1976.9)$ | Flush on wall plaster; $+1062.5	ext{ mm}$ AFF |
| **`SB-16`** | Living Room Lower TV Media Power & AV | `Living_Room_Wall_West` | 200mm Outer (Interior face) | $-21.6$ (Buried) | $(4829.2, 3625.0, 1460.0)$ | Flush inside console cabinet; $+545.6	ext{ mm}$ AFF |
| **`SB-16 (Loft)`**| Inverter & Tech Loft Hub (East Wall) | `Living_Room_Wall_East` | 200mm Outer (Interior face) | $-47.6$ (Buried) | $(200.0, 2325.0, 3260.0)$ | Flush on wall plaster; $+2345.6	ext{ mm}$ AFF |
| **`DB_GF`** | Ground Floor Main Distribution Board | `Living_Room_Wall_East` | 200mm Outer (Interior face) | $0.0$ | $(200.0, 2150.0, 2350.0)$ | Flush enclosure, acrylic door flush with plaster line |

---

## 3. First Floor Modular Switchbox Schedule

| Box ID | Room / Functional Space | Host Wall Solid | Final Coordinates $(X, Y, Z)$ [mm] | Mounting Status |
| :--- | :--- | :--- | :---: | :--- |
| **`FF_SB-1`** | FF Living Room Master Entrance | `FF_Living_Room_Wall_Main_Door` | $(1762.5, 2110.0, 5362.4)$ | Flush on wall plaster |
| **`FF_SB-2`** | FF Living Room Stair Wall Entry | `FF_Wall_Stair_SE_SW` | $(2050.0, 1814.5, 5573.9)$ | Flush on wall plaster; $\Delta Y = -128.6	ext{ mm}$ |
| **`FF_SB-3`** | FF Upper TV Display Console | `FF_Living_Room_Wall_West` | $(4829.2, 3625.0, 5268.0)$ | Flush on wall plaster; Clears FF C5 |
| **`FF_SB-4`** | FF Living Room Stair Wall South | `FF_Wall_Stair_SE_SW` | $(3560.0, 1814.5, 5573.9)$ | Flush on wall plaster; $\Delta Y = -128.6	ext{ mm}$ |
| **`FF_SB-9`** | FF Bedroom Study / Entrance | `FF_Bedroom_Wall_North` | $(3325.0, 4626.0, 5324.9)$ | Flush on wall plaster; $\Delta Y = -47.5	ext{ mm}$ |
| **`FF_SB-10`**| FF Bedroom Bedside Console | `FF_Bedroom_Wall_South` | $(2600.0, 7420.0, 4824.9)$ | Flush on wall plaster; Clears FF C2 |
| **`FF_SB-AC`**| FF Bedroom 20A AC Isolator | `FF_Bedroom_Wall_East` | $(2035.2, 7000.0, 6473.0)$ | Flush on wall plaster; $\Delta X = -47.5	ext{ mm}$ |
| **`FF_SB-12`**| FF Toilet Geyser & Exhaust | `FF_Toilet_Wall_West` | $(4829.2, 1260.0, 5865.5)$ | Flush on wall plaster; $\Delta X = -47.6	ext{ mm}$ |
| **`FF_SB-13`**| FF Kitchen Entrance Console | `FF_Bedroom_Wall_East` | $(1935.2, 4975.0, 5362.4)$ | Flush on wall plaster; $\Delta X = +60.2	ext{ mm}$ |
| **`FF_SB-14`**| FF Kitchen Food Prep Counter | `FF_Kitchen_Wall_East` | $(200.0, 5715.0, 5237.4)$ | Flush on wall plaster; $\Delta X = +47.6	ext{ mm}$ |
| **`FF_SB-15`**| FF Kitchen Refrigerator / South Wall | `FF_Kitchen_Wall_South` | $(1100.0, 7420.0, 5187.4)$ | Flush on wall plaster; $\Delta Y = -50.0	ext{ mm}$ |
| **`FF_SB-16`**| FF Lower TV Media Console | `FF_Living_Room_Wall_West` | $(4829.2, 3625.0, 4678.0)$ | Flush on wall plaster; Clears FF C5 |
| **`FF_SB-16L`**| FF Tech Loft Hub (East Wall) | `FF_Living_Room_Wall_East` | $(200.0, 2325.0, 6475.5)$ | Flush on wall plaster; $\Delta X = +47.6	ext{ mm}$ |

---

## 4. Execution Discipline & Quality Sign-Off

* **Air Gap Tolerance:** Strictly $0.0	ext{ mm}$ across all 16 modular assemblies.
* **Partition Wall Punch-Through:** $0.0	ext{ mm}$ (All $40	ext{ mm}$ backboxes maintain $\ge 60	ext{ mm}$ residual AAC masonry thickness in $100	ext{ mm}$ partition walls).
* **Structural Column Separation:** $\ge 150	ext{ mm}$ clear from concrete columns C1–C8.
* **BIM Verification:** Recomputed in `HomeConstruction.FCStd` with 0 non-manifold warnings, 0 recompute errors, and 0 invalid objects.
