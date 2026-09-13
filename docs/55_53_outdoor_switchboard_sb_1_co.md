## 53. Outdoor Switchboard (SB-1) Consolidation into Staircase Switchboard (SB_STAIR1)

Following client directive (*"SB-1 can we merge into the stairs wall light switch box - yes proceed"*), the outdoor front entrance switchboard (`SB-1`) and its associated vertical drop conduit have been removed from the front entrance wall and consolidated into the **Master Outdoor & Staircase Switchboard (`SB_STAIR1`)** at the foot of the stairs in `HomeConstruction.FCStd`.

```carousel
![SB-1 Consolidated into Master Staircase Switchboard SB_STAIR1](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/sb1_merged_into_staircase_switchboard_annotated.png)
```

### 53.1 Architectural & Engineering Rationale

1. **Pristine Front Entrance Portico:**
   * Removing `SB-1` and its chased wall conduit drop from the South entrance wall ($X = 370.0\text{ mm}$) leaves the Main Entrance Door and its teak architectural surround completely free of electrical clutter.
2. **Immediate Proximity to Steps:**
   * The staircase switchboard `SB_STAIR1` ($X = 2017.5\text{ mm}, Y = 1714.5\text{ mm}$) is just **$590\text{ mm}$ ($1.9\text{ ft}$)** past the right jamb of the Main Door, right at the Sitout-to-Staircase threshold. It is effortlessly accessible to someone entering from the gate or sitout.
3. **Unified 6-Module Master Control Hub:**
   * Consolidates all exterior, gate, and circulation lighting onto a single, high-capacity modular switchplate, eliminating dual redundant small boxes.

---

### 53.2 Re-Engineered Component Architecture

#### 1. Ground Floor Modifications
* **Excised Components at $X = 370.0\text{ mm}$:**
  * `Electrical_Switchboard_Plates`: Removed Solid 10 (4-module switchplate at $X = 370.0, Y = 1707.0\text{ mm}$).
  * `Electrical_Switchboard_Rocker_Switches`: Removed Solids 30 through 33 (4 rocker switches).
  * `Electrical_Slab_Wall_Drops`: Removed Solid 5 ($25\text{ mm}$ wall conduit drop at $X = 370.0, Y = 1720.0\text{ mm}$).
  * `Electrical_Slab_Conduit_Network`: Removed Solid 4 (plinth drop) and Solid 5 (plinth pipe).
* **Consolidated Master Switchboard (`Staircase_Switchboard_SB_STAIR1`):**
  * **Dimensions:** $200.0\text{ mm}\text{ (W)} \times 75.0\text{ mm}\text{ (H)} \times 15.0\text{ mm}\text{ (D)}$ (Centered at $X = 2017.5\text{ mm}, Y = 1707.0\text{ mm}, Z = 2151.9\text{ mm}$).
  * **Module Capacity:** 6 Modules comprising 4 modular rocker switches + 1 modular switched convenience socket:
    1. **Module 1:** Staircase Wall Light (2-Way master toggle)
    2. **Module 2:** Sitout Ceiling Recessed Downlight (`DL-10` / `Pot 10`)
    3. **Module 3:** Front Entrance & Portico Cantilever Canopy Spotlights
    4. **Module 4:** Main Entrance Gate Pillar Lights & Boundary Compound Lights
    5. **Modules 5 & 6:** 6A Weatherproof Switched Convenience Socket
* **Ceiling Conduit Grid Optimization (`Electrical_Slab_Conduit_Network`):**
  * **Entrance Header (Solid 6):** Truncated from $X \in [370.0, 2017.5]\text{ mm}$ to $X \in [857.0, 2017.5]\text{ mm}$, eliminating $487\text{ mm}$ of redundant pipe while seamlessly connecting the Sitout downlight pot to the staircase switchboard.
  * **Ceiling Cross-Wall Link (Solid 8):** Re-routed to $X = 2017.5\text{ mm}$ ($Y \in [1720.0, 1925.0]\text{ mm}$) directly entering the Living Room corridor slab trunk.
  * **Underground Gate Feed:** Chased down inside the staircase wall to the plinth ($Z = 945.0\text{ mm}$) and running along the foundation to the gate post.

#### 2. First Floor Modifications (1:1 Symmetry)
* **Excised Components at $X = 370.0\text{ mm}$:**
  * `FF_Electrical_Switchboard_Plates`: Removed Solid 14.
  * `FF_Electrical_Switchboard_Rocker_Switches`: Removed Solids 30 through 33.
  * `FF_Electrical_Slab_Wall_Drops`: Removed Solid 5.
  * `FF_Electrical_Slab_Conduit_Network`: Removed Solids 4 and 5.
* **Consolidated First Floor Switchboard (`FF_Staircase_Switchboard_SB_STAIR1`):**
  * Replaced with the exact 6-module consolidated geometry shifted by $\Delta Z = +3173.0\text{ mm}$ ($Z \in [5287.4, 5362.4]\text{ mm}$).
  * Controls First Floor Staircase Wall Light, Balcony Ceiling Downlights, Roof Canopy Spots, and 6A Balcony Socket.
* **Ceiling Grid Header:** Truncated to span $X \in [857.0, 2017.5]\text{ mm}$ at $Z = 7193.0\text{ mm}$.

---

### 53.3 Verification & Document Integrity

| Metric | Before Consolidation | After Consolidation | Net Change |
| :--- | :---: | :---: | :--- |
| **Front Porch Switchboards** | 2 (`SB-1` GF & FF) | **0** | Clean front door wall |
| **Porch Wall Chased Drops** | 2 drops at $X = 370$ | **0** | $0.0\text{ mm}$ wall penetrations |
| **Master Stair Switchboard** | 2 Modules ($75\text{ mm}$) | **6 Modules ($200\text{ mm}$)** | Unified master outdoor/stair hub |
| **Redundant Header Conduit** | $974\text{ mm}$ total | **$0\text{ mm}$** | $487\text{ mm}$ excised per floor |
| **Model Recompute Health** | 470 objects, 0 errors | **470 objects, 0 errors** | 100% Manifold Solids |

* **Master Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)
* **Saved & Verified:** Complete FreeCAD XML-RPC sync, valid geometry, and zero recompute warnings.

---
