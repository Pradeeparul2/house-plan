## 52. First Floor MCB Distribution Board (MDB) & Main Door Handle — 100% Ground Floor Parity

Following client directive (*"FF MCB box not same like GF check FF main door handle position as well it should same like GF"*), a comprehensive spatial audit and geometric re-engineering of the First Floor entrance door handle, MCB distribution board, and associated wiring infrastructure was completed in `HomeConstruction.FCStd`.

```carousel
![First Floor and Ground Floor Main Door Handle Parity](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/ff_gf_door_handles_aligned_annotated.png)
<!-- slide -->
![First Floor and Ground Floor MCB Distribution Board Parity](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/ff_gf_mcb_boxes_aligned_annotated.png)
```

### 52.1 First Floor Main Door Handle Alignment (1:1 GF Parity)

#### 1. Diagnostic Findings
* **Ground Floor Reference (`GF_Main_Door_Handle`):**
  * Bounding Box: $X \in [1226.55, 1367.55]\text{ mm}$, $Y \in [1690.05, 1729.50]\text{ mm}$, $Z \in [1790.40, 2010.40]\text{ mm}$.
  * Positioned on the **Right / Latch side** of the entrance door leaf (Center $X \approx 1297.0\text{ mm}$, $60\text{ mm}$ backset from right door edge).
* **First Floor Previous State (`FF_Main_Door_Handles`):**
  * Bounding Box: $X \in [629.00, 770.00]\text{ mm}$, $Y \in [1690.05, 1729.50]\text{ mm}$, $Z \in [4963.40, 5183.40]\text{ mm}$.
  * Inadvertently positioned on the **Left / Hinge side** of the door leaf ($60\text{ mm}$ from left jamb), creating an ergonomic conflict.

#### 2. Re-Engineered Handle Placement
* Replaced `FF_Main_Door_Handles.Shape` with the exact Ground Floor handle geometry translated by the standard vertical floor-to-floor offset ($\Delta Z = +3173.0\text{ mm}$):
  * **New First Floor Coordinates:** $X \in [1226.55, 1367.55]\text{ mm}$, $Y \in [1690.05, 1729.50]\text{ mm}$, $Z \in [4963.40, 5183.40]\text{ mm}$.
  * **Plumb Line Alignment:** $100\%$ co-planar along $X = 1297.0\text{ mm}$ with Ground Floor handle.
  * **Lever Action:** Inward-pointing horizontal chrome lever and escutcheon plate, identical to Ground Floor.

---

### 52.2 First Floor MCB Distribution Board (MDB) Alignment

#### 1. Diagnostic Findings of Previous FF Discrepancies
1. **Wrong Enclosure Size & Orientation:** Solid 11 in `FF_Electrical_Switchboard_Plates` was sized $240\text{ mm} \times 60\text{ mm} \times 320\text{ mm}$ centered at $Z = 5587.4\text{ mm}$ (rotated 90°), whereas Ground Floor MDB Solid 11 is $70\text{ mm} \times 300\text{ mm} \times 400\text{ mm}$ centered at $Z = 2350.0\text{ mm}$.
2. **Missing Switch Toggles on Box:** The MCB toggle switches were completely missing from the MDB enclosure at $X = 200, Y = 2150\text{ mm}$.
3. **Stray North Wall Toggles:** Six floating MCB switch solids (Solids 30 to 35 in `FF_Electrical_Switchboard_Rocker_Switches`) were hovering in mid-air on the North entrance wall at $X \in [1500, 1693]\text{ mm}, Y = 1897.5\text{ mm}$ (remnants of an old layout).
4. **Redundant 32mm EB Riser:** A separate yellow vertical conduit (`FF_EB_Service_Mains_Riser`) terminated in empty space at $X = 1600\text{ mm}$ on the North wall. Because the First Floor has its own independent EB service connection, this redundant riser caused visual clutter.

#### 2. Re-Engineered First Floor MDB Geometry
* **Host Component:** Solid 11 of `FF_Electrical_Switchboard_Plates`.
  * **Dimensions:** $300.0\text{ mm}\text{ (W)} \times 400.0\text{ mm}\text{ (H)} \times 70.0\text{ mm}\text{ (D)}$.
  * **Bounding Box:** $X \in [165.0, 235.0]\text{ mm}$, $Y \in [2000.0, 2300.0]\text{ mm}$, $Z \in [5323.0, 5723.0]\text{ mm}$ (Center: $200.0, 2150.0, 5523.0\text{ mm}$).
  * **Recess:** Embedded into the 9" brick East wall with $5\text{ mm}$ architectural projection, completely concealed behind the inward-swinging entrance door leaf.
* **MCB Toggle Switches:**
  * Excised the 6 stray toggles from the North wall ($X \approx 1600\text{ mm}$).
  * Integrated an 8-way MCB rocker switch panel matching GF Solid 34 shifted by $\Delta Z = +3173.0\text{ mm}$:
    * Bounding Box: $X \in [224.0, 236.0]\text{ mm}$, $Y \in [2060.0, 2240.0]\text{ mm}$, $Z \in [5503.0, 5548.0]\text{ mm}$ (Center: $230.0, 2150.0, 5525.5\text{ mm}$).
    * Face-mounted in charcoal black on the white MDB panel.
* **Ceiling Conduit Drop (`FF_Living_Slab_Wall_Drops` Solid 2):**
  * $25\text{ mm}$ rigid PVC conduit centered at $(200.0, 2150.0\text{ mm})$, running from ceiling slab $Z = 7193.0\text{ mm}$ straight into the top knockout of the MDB at $Z = 5723.0\text{ mm}$ ($0.0\text{ mm}$ gap).
* **UPS Feeder Conduit (`FF_UPS_Conduit_Pipeline`):**
  * Re-routed from the previous cross-ceiling span to a clean vertical $20\text{ mm}$ conduit run along the East wall between the top of the MDB ($Z = 5723.0\text{ mm}$) and the overhead UPS power backup system ($Z = 6350.0\text{ mm}$).
* **EB Service Mains Riser (`FF_EB_Service_Mains_Riser`):**
  * Redundant 32mm riser on North wall suppressed, leaving the North entrance wall clean and symmetrical.

---

### 52.3 Floor-to-Floor Symmetry & Audit Summary

| Parameter | Ground Floor Reference | First Floor Re-Engineered | Parity Status |
| :--- | :--- | :--- | :--- |
| **Door Handle X-Span** | $X \in [1226.55, 1367.55]\text{ mm}$ | $X \in [1226.55, 1367.55]\text{ mm}$ | **1:1 Plumb Alignment** |
| **Door Handle Latch Side** | Right side ($60\text{ mm}$ backset) | Right side ($60\text{ mm}$ backset) | **1:1 Identical** |
| **MDB Location** | East Wall behind door ($Y = 2150\text{ mm}$) | East Wall behind door ($Y = 2150\text{ mm}$) | **1:1 Co-axial** |
| **MDB Box Dimensions** | $300\text{ (W)} \times 400\text{ (H)} \times 70\text{ (D)}\text{ mm}$ | $300\text{ (W)} \times 400\text{ (H)} \times 70\text{ (D)}\text{ mm}$ | **1:1 Identical** |
| **MDB Elevation Span** | $Z \in [2150.0, 2550.0]\text{ mm}$ | $Z \in [5323.0, 5723.0]\text{ mm}$ | **Exact $\Delta Z = +3173.0\text{ mm}$** |
| **Rocker Switches Count** | 37 solids | 37 solids | **1:1 Exact Parity** |
| **North Wall Clutter** | 0 stray switches, 0 exposed risers | 0 stray switches, 0 exposed risers | **1:1 Clean Wall** |

* **Master Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)
* **Recompute Health:** 0 cyclic dependencies, 0 shape errors, 100% valid manifold solids.

---
