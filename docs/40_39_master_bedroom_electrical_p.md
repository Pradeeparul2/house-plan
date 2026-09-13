## 39. Master Bedroom Electrical Pipeline Optimization

Following client directive (*"optimize the bedroom pipeliens"*), the Master Bedroom electrical conduit network has been completely restructured from legacy diagonal runs into a streamlined, high-efficiency **Orthogonal Spine-and-Header Grid**:

```carousel
![Bedroom Optimized Slab Pipelines](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/bedroom_slab_pipelines_optimized_annotated.png)
<!-- slide -->
![Bedroom South Wall Controls & Lighting](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/bedroom_south_wall_optimized_annotated.png)
```

### 39.1 Legacy Issues Resolved

1. **Elimination of Diagonal Criss-Crosses:**
   * Previously, four diagonal conduits radiated outward from the central ceiling fan box `FB-2` ($(X=3480, Y=6070)$) like an "X" across the bedroom floor/slab:
     - Diagonal NW to `DL-5` $(2600, 5400)$
     - Diagonal NE to `DL-6` $(4300, 5400)$
     - Long diagonal SW to $(2200, 7468)$ across the bed area
   * These diagonals created weak diagonal planes across the RCC slab and made rebar tying difficult during casting.
2. **Decommissioning of Orphaned Pot 15 & SB-11 Dogleg:**
   * When `SB-11` was deleted, an orphaned ceiling light pot (`Pot 15` at $X = 2200.0, Y = 7467.6$) and a $200	ext{ mm}$ dogleg jog to `SB-10` ($X = 2400$) remained in the slab.
   * `Pot 15` and the dogleg have been **completely excised from the slab**.
3. **Consolidation of Redundant South Wall Runs:**
   * Previously, two parallel lines ran from `FB-2` to the South wall (one for `SB-10` and one for the Tubelight). These have been consolidated into a single central feed and horizontal header.

---

### 39.2 Optimized Orthogonal Pipeline Grid

1. **Central Spine Trunk Line (North-South along $X = 3500.0	ext{ mm}$):**
   * A single, continuous straight conduit runs down the center of the bedroom:
     $$	ext{Entrance SB-9 Drop } (Y=4650) \longleftrightarrow 	ext{Downlight Crossing } (Y=5400) \longleftrightarrow 	ext{Fan Box FB-2 } (Y=6070) \longleftrightarrow 	ext{South Wall Tubelight } (Y=7468)$$
   * Feeds the entrance console `SB-9`, the ceiling fan `FB-2`, and hits the South wall dead-center above the 4ft LED Tubelight.
2. **East-West Downlight Header (along $Y = 5400.0	ext{ mm}$):**
   * A clean $90^\circ$ perpendicular cross-conduit connects:
     $$	ext{Front-East Downlight DL-5 } (X=2600) \longleftrightarrow 	ext{Central Crossing } (X=3500) \longleftrightarrow 	ext{Front-West Downlight DL-6 } (X=4300)$$
   * Receives incoming main feed from the Living Room at $(X=2566, Y=4550)$ through `DL-5`.
   * Branch to Wardrobe pot `Pot 12` ($(X=2573, Y=4720)$) runs straight North-South off `DL-5`.
3. **South Wall Distribution Header (along $Y = 7467.6	ext{ mm}$ at Ceiling Soffit $Z = 4020.0	ext{ mm}$):**
   * From the central spine termination at the South wall ($X = 3500.0	ext{ mm}$), the conduit splits:
     - Drops vertically straight down into **`Bedroom_Tubelight_Junction_Box`** at $+2300	ext{ mm}$ AFF.
     - Runs horizontally West along the South wall ceiling soffit for $1100	ext{ mm}$ straight to $X = 2400.0	ext{ mm}$.
     - Drops vertically straight down into **`SB-10`** (Bedside console at $+700	ext{ mm}$ AFF).
   * **Direct 2-Way Switching:** Provides the shortest possible path ($1.1	ext{ m}$) for the 2-way traveler wires between `SB-10` and the South Wall Tubelight, eliminating wire routing back through the fan box.

---

### 39.3 Quantitative Optimization Summary

| Metric | Legacy Radial Layout | Optimized Orthogonal Grid | Improvement |
| :--- | :--- | :--- | :--- |
| **Grid Geometry** | Multiple diagonal angles ($45^\circ, 60^\circ$) | **Strictly $90^\circ$ Orthogonal (E-W & N-S)** | **Aligned with structural rebar grid** |
| **Total Bedroom Conduit Volume** | $3,188,712	ext{ mm}^3$ | **$2,066,560	ext{ mm}^3$** | **35.2% Reduction in conduit material** |
| **Orphaned Ceiling Pots** | 1 (`Pot 15` at $X=2200$) | **0 (Excised cleanly)** | **No dead junction boxes in ceiling** |
| **2-Way Switching Loop (SB-10 to Tubelight)** | $pprox 3.8	ext{ meters}$ (via fan box) | **$1.1	ext{ meters}$ (direct wall header)** | **71% Shorter wire run** |
| **South Wall Chases** | Off-center jog ($X=2200 
ightarrow 2400$) | **Straight vertical drop at $X=2400$** | **Clean, flush finish** |

---

### 39.4 First Floor (G+1) Synchronization
* All bedroom optimizations (`FF_Electrical_Slab_Conduit_Network`, `FF_Bedroom_Tubelight_Conduit_Drop`, `FF_Electrical_Slab_Light_Pots`) have been mirrored in 1:1 lockstep at $\Delta Z = +3173.0	ext{ mm}$.


---
