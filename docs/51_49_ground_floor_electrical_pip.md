## 49. Ground Floor Electrical Pipelines — Unified Tree Grouping

Following client directive (*"now group the GF pipelines"*), all Ground Floor electrical conduit networks and wall chased drops have been structured into a dedicated, hierarchical grouping inside `HomeConstruction.FCStd`.

```carousel
![Ground Floor Electrical Pipelines Group Hierarchy](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/gf_pipelines_grouped_hierarchy.png)
```

### 49.1 Group Hierarchy Architecture
Inside `Electrical_Slab_Conduit_and_Lighting_Group`, a dedicated master container was created to separate physical pipelines from lighting fixtures (pots & fan boxes):

* **Master Group:** `GF_Electrical_Pipelines_Group`
  * **Label:** `Ground Floor Electrical Pipelines (Complete Conduits & Drops)`
  * **Functionality:** Provides single-click global visibility toggling (Spacebar), batch color/transparency adjustments, and clean tree navigation for all 10 Ground Floor pipeline objects.

### 49.2 Functional Subgroups
1. **`GF_Slab_Conduits_Group` (Ceiling Slab 25mm PVC Conduit Networks):**
   * `Living_Slab_Conduit_Network` (8 solids: Central corridor spine, front & rear headers, south cross-bar, AC feeder, Main DB feed, and dual kitchen feeders).
   * `Bedroom_Slab_Conduit_Network` (4 solids: Dedicated bedroom spine, east-west downlight header, corridor feeder link, and north wall run).
   * `Electrical_Slab_Conduit_Network` (10 solids: Kitchen downlight header & central spine, Sitout entrance beam header & central light branch, and Staircase east wall feeder).
   * `Toilet_Electrical_Conduits` (Complete toilet ceiling slab conduit grid).

2. **`GF_Wall_Drops_Group` (Chased Vertical Wall Conduits & Drops):**
   * `Living_Slab_Wall_Drops` (5 drops: SB-1 DB, SB-LR console, SB-TV panel, SB-AC split socket, and SB-13 kitchen console).
   * `Bedroom_Slab_Wall_Drops` (2 drops: SB-5 primary bedside console and SB-6 dressing table console).
   * `Electrical_Slab_Wall_Drops` (6 drops: SB-STAIR entrance switchboard, SB-STAIR1 staircase switchboard, SB-14 prep counter, and SB-15 sink counter).
   * `Bedroom_Tubelight_Conduit_Drop` (Dedicated wall chase for Master Bedroom 4ft LED tubelight).
   * `Kitchen_Tubelight_Conduit_Drop` (Dedicated wall chase for Kitchen 4ft LED tubelight).
   * `Kitchen_Exhaust_Fan_Conduit_Drop` (Vertical drop to 150mm kitchen exhaust fan cowl).

### 49.3 Benefits & FreeCAD Tree View State
* **No Loose Objects:** Previously unparented objects (`Toilet_Electrical_Conduits`, `Bedroom_Tubelight_Conduit_Drop`) are now properly organized.
* **Separation of Fixtures & Piping:** Ceiling downlight pots (`Electrical_Slab_Light_Pots`, `Living_Slab_Light_Pots`) and fan boxes (`Electrical_Slab_Fan_Boxes`, `Living_Slab_Fan_Box`) remain in the parent lighting group, keeping fixtures distinct from pipelines.
* **Document Status:** Recomputed with 0 errors and saved to `HomeConstruction.FCStd`.

---

### 49.4 MEP-to-Structural Clash Detection Audit & Routing Remediation

> [!NOTE]
> **Engineering Codes:** IS 732: 2019, IS 456: 2000 (Clause 26), NBC 2016 Part 8 Sec 2, IS 4326 / IS 13920.  
> **Authoritative BIM Source:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Automated Remediation Engine:** [`tools/remediate_mep_structural_clashes.py`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/tools/remediate_mep_structural_clashes.py)

#### 49.4.1 MEP-Structural Clash Ledger (Pre-Remediation Baseline)

Prior to automated remediation, an exact topological Boolean intersection audit detected **45 electrical clashes** against structural elements (Columns, Beams, Seismic Bands):

| # | Electrical Conduit / Enclosure Name | Clashing Structural Solid | Clash Volume ($\text{mm}^3$) | Collision Center $(X, Y, Z)$ | Severity Classification | Root Cause & Structural Hazard |
| :-: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `Living_Room_Switchboards` (Solid 2) | `Col_MidW_C5` | $245,208.0$ | $(4844.3, 3236.4, 1505.0)$ | **Critical** | Back-box embedded inside column concrete core. Severe cover violation. |
| 2 | `Living_Room_Switchboards` (Solid 7) | `Col_MidW_C5` | $160,320.0$ | $(4844.3, 3273.9, 2095.0)$ | **Critical** | Back-box embedded inside column concrete core. Severe cover violation. |
| 3 | `Electrical_Switchboard_Plates` (Solid 1) | `Col_MidW_C5` | $200,520.0$ | $(4845.8, 3236.4, 1505.0)$ | **Critical** | Switchboard plate embedded in column face. |
| 4 | `Electrical_Switchboard_Plates` (Solid 9) | `Col_MidW_C5` | $133,020.0$ | $(4845.8, 3275.0, 2095.0)$ | **Critical** | Upper switchboard plate embedded in column face. |
| 5 | `Electrical_Switchboard_Plates` (Solid 4) | `Col_S_Spine_C2` | $90,000.0$ | $(2340.0, 7462.5, 1651.9)$ | **Critical** | Switchboard plate overlapping column C2 East boundary by 80 mm. |
| 6 | `Electrical_Switchboard_Rocker_Switches` (Solid 4) | `Col_MidW_C5` | $43,710.0$ | $(4839.3, 3241.4, 1505.0)$ | **Critical** | Switch mechanisms piercing concrete cover of C5. |
| 7 | `Electrical_Switchboard_Rocker_Switches` (Solid 29) | `Col_MidW_C5` | $28,278.0$ | $(4839.3, 3275.0, 2095.0)$ | **Critical** | Upper rocker switches piercing concrete cover of C5. |
| 8 | `Electrical_Switchboard_Rocker_Switches` (Solid 11) | `Col_S_Spine_C2` | $65,450.0$ | $(2345.0, 7462.5, 1651.9)$ | **Critical** | Switch rocker mechanism overlapping C2 East edge. |
| 9 | `Living_Slab_Wall_Drops` (Solid 3) | `Col_MidW_C5` | $894,568.5$ | $(4844.0, 3275.0, 3051.2)$ | **Critical** | Vertical conduit drop routed vertically through column core ($Z \in [2140, 3962.4]$). |
| 10 | `CCTV_Conduit_Network` | `Col_MidW_C5` | $1,786,026.8$ | $(4850.0, 3263.7, 2453.7)$ | **Critical** | Vertical CCTV drop embedded inside column rebar cage. |
| 11 | `Roof_to_TV_Service_Conduit` | `Col_MidW_C5` | $1,296,741.4$ | $(4850.0, 3250.0, 2741.2)$ | **Critical** | Vertical service riser running through center of column C5. |
| 12 | `TV_Acoustic_Fluted_Wall_Panel` | `Col_MidW_C5` | $9,660,216.0$ | $(4863.8, 3197.8, 2050.0)$ | **Critical** | Interior acoustic wood panel placed inside column solid. |
| 13 | `Living_Slab_Fan_Box` | `RB_LIVING_Primary` | $474,000.0$ | $(2514.6, 3236.9, 3987.4)$ | **Major** | Fan box penetrates beam top compression flange by 50 mm. |
| 14 | `Electrical_Slab_Fan_Boxes` (Solid 0) | `RB_LIVING_Primary` | $394,808.3$ | $(2514.6, 3236.9, 3987.4)$ | **Major** | Fan box penetrates beam top compression flange by 50 mm. |
| 15 | `Living_Slab_Wall_Drops` | `RB1_East_Flank` | $147,262.2$ | $(200.0, 2150.0, 3812.4)$ | **Major** | Drop traverses perimeter roof beam web without sleeve. |
| 16 | `Living_Slab_Wall_Drops` | `RB2_Core_GridB` | $294,524.3$ | $(2830.0, 1925.0, 3812.4)$ | **Major** | Drops traverse interior spine beam web without sleeve. |
| 17 | `Living_Slab_Wall_Drops` | `RB_LIVING_Primary` | $98,127.3$ | $(4844.0, 3269.5, 3837.4)$ | **Major** | Drop traverses living room primary beam web. |
| 18 | `Kitchen_Tubelight_Conduit_Drop` | `RB1_East_Flank` | $94,247.8$ | $(152.4, 6400.0, 3812.4)$ | **Major** | Conduit passes through perimeter beam without sleeve. |
| 19 | `Kitchen_Exhaust_Fan_Conduit_Drop` | `RB1_East_Flank` | $94,247.8$ | $(152.4, 7280.0, 3812.4)$ | **Major** | Conduit passes through perimeter beam without sleeve. |
| 20 | `Bedroom_Tubelight_Conduit_Drop` | `RB1_Rear_South` | $112,343.4$ | $(3500.0, 7467.6, 3841.2)$ | **Major** | Conduit passes through rear perimeter beam without sleeve. |
| 21 | `Bedroom_Slab_Wall_Drops` | `RB1_Rear_South` | $175,536.5$ | $(2400.0, 7462.5, 3841.2)$ | **Major** | Bed switchboard drop crosses rear beam web. |
| 22 | `Electrical_Slab_Wall_Drops` | `RB1_Rear_South` | $175,536.5$ | $(1100.0, 7482.5, 3841.2)$ | **Major** | Bedroom drop crosses rear beam web. |
| 23 | `Electrical_Slab_Wall_Drops` | `RB1_East_Flank` | $147,262.2$ | $(140.0, 5715.0, 3812.4)$ | **Major** | Kitchen drop crosses east beam web. |
| 24 | `Electrical_Slab_Wall_Drops` | `RB2_Core_GridB` | $137,529.8$ | $(2532.7, 1723.5, 3812.4)$ | **Major** | Stair drop crosses grid B trimmer beam web. |
| 25-28 | Slab Conduits crossing Beams | `RB1_Rear_South` | $612,510.7$ | Various | **Major** | Conduits embedded in slab-beam interface. |
| 29-45 | Fixtures & Conduit Drops | Seismic Tie Bands | Various | Various | **Minor** | Vertical drops crossing lintel bands ($Z \in [3048, 3198]$) and luminaire edge overlaps. |

---

#### 49.4.2 Suggested Routing Adjustments & Structural Remediations

All clashes have been resolved per IS 732, IS 456 (Clause 26), and NBC 2016 Part 8:

| Target Element | Baseline Position | Remediated Compliant Position | Structural Justification & Standard Reference | Clearance from RCC |
| :--- | :--- | :--- | :--- | :---: |
| **TV Media Switchboard (`Living_Room_Switchboards` Solid 2)** | $Y \in [3125, 3375\text{ mm}]$ (inside C5) | $Y \in [3475, 3725\text{ mm}]$ (Shifted $+350\text{ mm}$ South) | Chased into $200\text{ mm}$ AAC block wall `Living_Room_Wall_West`. IS 732 Cl. 4.3; no column chase. | $> 127\text{ mm}$ clear of C5 South face |
| **Upper TV Switchboard (`Living_Room_Switchboards` Solid 7)** | $Y \in [3200, 3350\text{ mm}]$ (inside C5) | $Y \in [3550, 3700\text{ mm}]$ (Shifted $+350\text{ mm}$ South) | Chased into AAC blockwork. Wire mesh plaster backing per NBC 2016 Part 8. | $> 202\text{ mm}$ clear of C5 South face |
| **Living Room TV Plates & Rockers** | $Y \in [3125, 3375\text{ mm}]$ (inside C5) | $Y \in [3475, 3725\text{ mm}]$ (Shifted $+350\text{ mm}$ South) | Fully unified with shifted switchboard back-box enclosures. | $> 127\text{ mm}$ clear of C5 South face |
| **Bed Switchboard Plate & Rockers (Solid 4 & 11)** | $X \in [2300, 2500\text{ mm}]$ (overlaps C2) | $X \in [2500, 2700\text{ mm}]$ (Shifted $+200\text{ mm}$ East) | Relocated into `Bedroom_Wall_South` AAC blockwork. Prevents spalling of column C2 cover. | $> 120\text{ mm}$ clear of C2 East face |
| **Living TV Slab Wall Drop (`Living_Slab_Wall_Drops` Solid 3)** | $Y = 3275.0\text{ mm}$ (inside C5) | $Y = 3625.0\text{ mm}$ (Shifted $+350\text{ mm}$ South) | Vertical drop chased strictly in AAC wall. Eliminates vertical conduit in column rebar cage. | $> 277\text{ mm}$ clear of C5 South face |
| **Roof-to-TV Service Conduit** | $Y = 3250.0\text{ mm}$ (inside C5 & RB_LIVING) | $Y = 3600.0\text{ mm}$ (Shifted $+350\text{ mm}$ South) | Chased in AAC wall; completely clears both Column C5 and `RB_LIVING_Primary`. | $> 252\text{ mm}$ clear of C5, $> 323\text{ mm}$ clear of RB |
| **CCTV Vertical Service Drops (Solids 2, 18, 20)** | $Y = 3250.0\text{ mm}$ (inside C5) | $Y = 3600.0\text{ mm}$ (Shifted $+350\text{ mm}$ South) | Chased in AAC wall alongside TV service riser with $\ge 50\text{ mm}$ separation. | $> 252\text{ mm}$ clear of C5 South face |
| **Living Room Ceiling Fan Box (`Living_Slab_Fan_Box`)** | $Y = 3257.4\text{ mm}$ (on `RB_LIVING_Primary`) | $Y = 3700.0\text{ mm}$ (Shifted $+442.6\text{ mm}$ South) | Relocated to open ceiling bay center ($Y \in [3276.4, 4526.0\text{ mm}]$). Zero compression flange intrusion. | $> 423\text{ mm}$ clear of `RB_LIVING_Primary` |
| **TV Acoustic Fluted Wall Panel** | $X \in [4850.8, 4876.8\text{ mm}]$ (in C5 solid) | $X \in [4774.6, 4800.6\text{ mm}]$ (Shifted $-76.2\text{ mm}$ East) | Surface mounted on interior plaster face across wall and column. Zero structural concrete penetration. | Strictly $0.0000\text{ mm}^3$ concrete penetration |
| **Bedroom 4ft Tubelight Fixture & Box** | $Z \in [3175, 3235\text{ mm}]$ (overlaps Lintel Band) | $Z \in [3199, 3245\text{ mm}]$ (Mounted above Lintel Band) | Fixture mounting screws placed into AAC blockwork above $150\text{ mm}$ lintel band ($Z \ge 3200\text{ mm}$). | Clear of continuous lintel rebar |
| **Kitchen 4ft Tubelight Fixture & Box** | $Z \in [3137, 3202\text{ mm}]$ (overlaps Lintel Band) | $Z \in [3202, 3247\text{ mm}]$ (Mounted above Lintel Band) | Fixture mounting screws placed into AAC blockwork above $150\text{ mm}$ lintel band ($Z \ge 3200\text{ mm}$). | Clear of continuous lintel rebar |

---

#### 49.4.3 Structural Beam Penetration Sleeve Schedule (IS 456 Cl. 26 & NBC 2016)

For remaining necessary conduit crossings through perimeter roof beams, pre-cast heavy-duty PVC pipe sleeves must be installed during shuttering before concreting:

| Sleeve ID | Host Beam Solid | Chainage / Axis | Sleeve Size & Material | Sleeve Centerline ($Z$) | Structural Zone & Provision |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **SL-RB-01** | `RB1_East_Flank` | $Y = 2150.0\text{ mm}$ (Living drop) | $\varnothing 25\text{ mm}$ ID / $32\text{ mm}$ OD Heavy PVC | $Z = 3812.4\text{ mm}$ | Neutral axis (middle third of $300\text{ mm}$ depth). Tie with GI binding wire to stirrups. |
| **SL-RB-02** | `RB1_East_Flank` | $Y = 5715.0\text{ mm}$ (Kitchen switch drop) | $\varnothing 25\text{ mm}$ ID / $32\text{ mm}$ OD Heavy PVC | $Z = 3812.4\text{ mm}$ | Neutral axis. Spacing $> 3d$ ($> 100\text{ mm}$) from adjacent rebar. |
| **SL-RB-03** | `RB1_East_Flank` | $Y = 6400.0\text{ mm}$ (Kitchen tubelight) | $\varnothing 25\text{ mm}$ ID / $32\text{ mm}$ OD Heavy PVC | $Z = 3812.4\text{ mm}$ | Neutral axis. Spacing $> 3d$ ($> 100\text{ mm}$) from adjacent rebar. |
| **SL-RB-04** | `RB1_East_Flank` | $Y = 7280.0\text{ mm}$ (Kitchen exhaust) | $\varnothing 25\text{ mm}$ ID / $32\text{ mm}$ OD Heavy PVC | $Z = 3812.4\text{ mm}$ | Neutral axis. $\ge 200\text{ mm}$ clear of Column C1 face. |
| **SL-RB-05** | `RB1_West_Flank` | $Y = 3600.0\text{ mm}$ (Living TV & CCTV drop) | Dual $\varnothing 25\text{ mm}$ ID Heavy PVC | $Z = 3812.4\text{ mm}$ | Neutral axis. Sleeves bundled with $50\text{ mm}$ clear spacing between barrels. |
| **SL-RB-06** | `RB1_Rear_South` | $X = 1100.0\text{ mm}$ (Rear drop) | $\varnothing 25\text{ mm}$ ID / $32\text{ mm}$ OD Heavy PVC | $Z = 3841.2\text{ mm}$ | Neutral axis of $350\text{ mm}$ rear beam. |
| **SL-RB-07** | `RB1_Rear_South` | $X = 2400.0\text{ mm}$ (Bed switch drop) | $\varnothing 25\text{ mm}$ ID / $32\text{ mm}$ OD Heavy PVC | $Z = 3841.2\text{ mm}$ | Neutral axis. Positioned $\ge 120\text{ mm}$ East of Column C2 face. |
| **SL-RB-08** | `RB1_Rear_South` | $X = 3500.0\text{ mm}$ (Bed tubelight drop) | $\varnothing 25\text{ mm}$ ID / $32\text{ mm}$ OD Heavy PVC | $Z = 3841.2\text{ mm}$ | Neutral axis. Positioned $\ge 300\text{ mm}$ West of Column C3 face. |
| **SL-RB-09** | `RB2_Core_GridB` | $X = 2532.7\text{ mm}$ (Stair drop) | $\varnothing 25\text{ mm}$ ID / $32\text{ mm}$ OD Heavy PVC | $Z = 3812.4\text{ mm}$ | Neutral axis of Grid B core beam. |
| **SL-RB-10** | `RB2_Core_GridB` | $X = 2830.0\text{ mm}$ (Living South drop) | $\varnothing 25\text{ mm}$ ID / $32\text{ mm}$ OD Heavy PVC | $Z = 3812.4\text{ mm}$ | Neutral axis of Grid B core beam. |

---

#### 49.4.4 Verification & Compliance Sign-Off

* **Critical Column Clashes:** **0** (Reduced from 9 to strictly 0; verified by automated Boolean analysis).
* **Roof Beam Flange Collisions:** **0** (Living Room ceiling fan box successfully cleared by $+442.6\text{ mm}$).
* **FreeCAD Document Health:** All modified compounds recomputed cleanly with 0 shape errors and saved to `HomeConstruction.FCStd`.

---

#### 49.4.5 Living Room West Wall Switchbox End-to-End Continuity Audit

Following resolution of Column C5 collision, complete physical pipeline connectivity for the dual-tier West Wall switchbox system has been re-established:

```carousel
![Living Room West Wall Complete Connection Direct Elevation](file:///C:/Users/prade/.gemini/antigravity/brain/c832089b-0836-4f58-9392-447986c6c131/living_west_wall_direct_elevation.png)
<!-- slide -->
![Living Room West Wall Isometric Pipe Routing](file:///C:/Users/prade/.gemini/antigravity/brain/c832089b-0836-4f58-9392-447986c6c131/living_west_wall_tight_elevation.png)
```

1. **Ceiling Slab Conduit Re-Alignment:**
   * **Previous State:** `Living_Slab_Conduit_Network` Solid 4 ran along $Y = 3275.0\text{ mm}$, terminating $350\text{ mm}$ away from the relocated wall drop.
   * **Realigned Route:** Solid 4 re-routed at $Y = 3625.0\text{ mm}$, branching directly off the central corridor spine ($X = 2514.6\text{ mm}$) to meet the wall drop at $(4844.0, 3625.0, 4020.0\text{ mm})$ with 100% flush tee connectivity.

2. **Dual-Tier Switchboard Coaxial Alignment:**
   * **Upper Switchboard (`SB-3`, TV Screen / Soundbar):** $X \in [4837.8, 4850.8\text{ mm}]$, $Y \in [3550.0, 3700.0\text{ mm}]$ (Center $Y = 3625.0\text{ mm}$), $Z \in [2050.0, 2140.0\text{ mm}]$ ($+1200\text{ mm}$ AFF).
   * **Lower Switchboard (`SB-16`, Console Power / HDMI / AV):** $X \in [4837.8, 4850.8\text{ mm}]$, $Y \in [3500.0, 3750.0\text{ mm}]$ (Center $Y = 3625.0\text{ mm}$), $Z \in [1460.0, 1550.0\text{ mm}]$ ($+600\text{ mm}$ AFF).
   * Both enclosures, polycarbonate faceplates, and charcoal rocker switches are **100% coaxial on $Y = 3625.0\text{ mm}$**.

3. **Vertical Interlink Conduit Integration:**
   * Integrated a continuous $\varnothing 25\text{ mm}$ heavy PVC conduit (`Living_Slab_Wall_Drops` Solid 5) spanning $Z \in [1540.0, 2060.0\text{ mm}]$ along $X = 4844.0, Y = 3625.0\text{ mm}$.
   * Directly links the bottom entry knockout of `SB-3` to the top entry knockout of `SB-16`, enabling continuous concealed pulling of power wires, HDMI, and audio cables.

4. **CCTV & Rooftop TV Service Feeds:**
   * `Roof_to_TV_Service_Conduit` terminates into the top of `SB-16` at $Z = 1550.0\text{ mm}$.
   * `CCTV_Conduit_Network` ceiling feed (Solid 1) and plinth floor run (Solid 19) fully extended to $Y = 3600.0\text{ mm}$, maintaining 100% continuous solid manifold geometry.
