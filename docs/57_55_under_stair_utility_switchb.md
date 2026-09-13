## 55. Under-Stair Utility Switchboard (SB-UTIL) Pipeline Connectivity Resolution

Following client directive (*"SB-utls seems like disconnected"*), a forensic geometric inspection of the electrical pipeline feeding the Under-Stair Utility Switchboard (`SB-UTIL`) and its sump water pump circuit was conducted in `HomeConstruction.FCStd`.

```carousel
![SB-UTIL Electrical Pipeline Connectivity Resolution](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/sb_util_connected_resolution_annotated.png)
```

### 55.1 Diagnostic Findings: Root Causes of Disconnection
1. **Truncated Slab Distribution Conduit (Ground Floor):**
   * Solid 0 in `Electrical_Slab_Conduit_Network` previously spanned from $(3045.4, 1731.6, 4020.0)\text{ mm}$ to $(3290.7, 1828.8, 4020.0)\text{ mm}$ with an extruded length of only $263.8\text{ mm}$.
   * It terminated abruptly in the ceiling slab with a **$201.0\text{ mm}$ open void** before reaching the master stair/corridor distribution box (`PB-CROSS-3` / Pot 12 at $3580.0, 1930.0, 4020.0\text{ mm}$).
   * In 3D views from above or the stairwell, this appeared as a loose diagonal pipe floating into empty air.
2. **First Floor Symmetry Gap:**
   * `FF_Electrical_Slab_Conduit_Network Solid 0` suffered from the identical $201.0\text{ mm}$ truncated void at $Z = 7193.0\text{ mm}$.
   * `FF_Electrical_Slab_Wall_Drops Solid 0` dropped from $Z = 7193.0\text{ mm}$ down to $Z = 5198.0\text{ mm}$, but had no corresponding First Floor switchboard container in `FF_Electrical_Switchboards_Group`, leaving the drop unterminated.
3. **Wall Chase Depth Misalignment:**
   * The vertical wall drop (`Electrical_Slab_Wall_Drops Solid 0`) was centered at $Y = 1720.0\text{ mm}$ (inside the masonry wall chase), whereas the surface-mounted faceplate of `SB-UTIL` and the descending pump conduit (`Pump_Motor_Supply_Conduit`) were centered at $Y = 1707.5\text{ mm}$.
   * This $12.5\text{ mm}$ offset in $Y$ caused the top drop to appear recessed or disconnected behind the wall face.

---

### 55.2 Engineering Revisions & Physical Continuity

1. **Continuous Sealed Slab Conduit (`Electrical_Slab_Conduit_Network Solid 0`):**
   * Replaced with a continuous $25\text{ mm}$ rigid PVC pipe ($R = 12.5\text{ mm}$) spanning from $(3050.0, 1707.5, 4020.0)\text{ mm}$ straight into the casing of Pot 12 at $(3580.0, 1930.0, 4020.0)\text{ mm}$ (Length: $574.1\text{ mm}$).
   * Joint gap: **$0.000\text{ mm}$** (watertight sealed entry).
2. **Plumb Wall Drop Alignment (`Electrical_Slab_Wall_Drops Solid 0`):**
   * Re-centered at $(X = 3050.0\text{ mm}, Y = 1707.5\text{ mm})$ from $Z = 4020.0\text{ mm}$ down to $Z = 2020.0\text{ mm}$, plunging $5\text{ mm}$ directly into the top knockout of `Staircase_Switchboard_SB_UTIL`.
   * Perfectly plumb with `Pump_Motor_Supply_Conduit` ($Y = 1707.5\text{ mm}$) below the board.
3. **First Floor 1:1 Twin Consolidation:**
   * **Conduit:** `FF_Electrical_Slab_Conduit_Network Solid 0` extended continuously into FF Pot 12 ($0.000\text{ mm}$ gap).
   * **Drop:** `FF_Electrical_Slab_Wall_Drops Solid 0` aligned to $(X = 3050.0, Y = 1707.5\text{ mm})$ from $Z = 7193.0$ down to $Z = 5193.0\text{ mm}$.
   * **Switchboard Added:** Created `FF_Staircase_Switchboard_SB_UTIL` inside `FF_Electrical_Switchboards_Group` ($X \in [2975, 3125]\text{ mm}, Y \in [1699, 1716]\text{ mm}, Z \in [5123, 5198]\text{ mm}$, Electric Cyan `#00D2FF`) housing convenience and utility controls for the First Floor landing, cleanly terminating the drop.

---

### 55.3 Complete Chain Verification Audit

| Connection Interface | Starting Point $(X, Y, Z)$ | Ending Point $(X, Y, Z)$ | Physical Gap | Continuity Status |
| :--- | :--- | :--- | :---: | :---: |
| **Slab Pot 12 $\to$ Ceiling Conduit** | $(3580.0, 1930.0, 4020.0)$ | $(3050.0, 1707.5, 4020.0)$ | **$0.000\text{ mm}$** | Continuous Sealed Pipe |
| **Ceiling Conduit $\to$ Wall Drop** | $(3050.0, 1707.5, 4020.0)$ | Top of Wall Drop | **$0.000\text{ mm}$** | Direct Joint |
| **Wall Drop $\to$ SB-UTIL Top** | Top knockout ($Z = 2025.0$) | Plunges to $Z = 2020.0$ | **$0.000\text{ mm}$** | Plumb Sealed Entry |
| **SB-UTIL Bottom $\to$ Pump Conduit** | Bottom knockout ($Z = 1950.0$) | Floor drop ($Z = 950.0$) | **$0.000\text{ mm}$** | Plumb Continuous Conduit |
| **Pump Conduit $\to$ Motor Terminal** | Floor run to $(2460, 610)$ | Motor terminal box ($Z = 1255$) | **$0.000\text{ mm}$** | Sealed Terminal Connection |
| **FF Pot 12 $\to$ FF Conduit $\to$ FF SB-UTIL** | Matching 1:1 floor twin at $Z = 7193.0$ | FF SB-UTIL at $Z = 5198.0$ | **$0.000\text{ mm}$** | 100% Floor Symmetry |

* **Master Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)
* **Recompute Health:** 471 objects, 0 errors, 100% valid manifold solids.
* **Timestamped Backup:** Archived to `backups/HomeConstruction_backup_20260908-163536.FCStd` and `backups/walkthrough_backup_20260908-163536.md`.

---
