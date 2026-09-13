# Terrace Roof & Staircase Headroom (Mumty) Structural Specifications

**Target Document:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
**Structural Baseline:** 8-Column Parametric RCC Frame with Rectified Mumty Enclosure & OHT Saddle Beams  
**Design Standards:** IS 456:2000, IS 875 (Part 2), IS 13920:2016, NBC 2016

---

## 1. Column Termination Datums (Superstructure to Terrace)

| Column ID | Location Description | Cross Section | Termination Datum (Z) | Extension Status Above Terrace |
| :--- | :--- | :--- | :--- | :--- |
| **C1** | SE Rear Corner (Kitchen Outer) | 300 x 230 mm | +7135.4 mm (Terrace slab soffit) | **Terminated** (No extension) |
| **C2** | S Center (Bed/Kitchen Spine) | 300 x 230 mm | +7135.4 mm (Terrace slab soffit) | **Terminated** (No extension) |
| **C3** | SW Rear Corner (Master Bed Outer) | 230 x 300 mm | +7135.4 mm (Terrace slab soffit) | **Terminated** (No extension) |
| **C4** | Mid-East Flank (Living/Kitchen) | 230 x 300 mm | +7135.4 mm (Terrace slab soffit) | **Terminated** (No extension) |
| **C5** | Mid-West Flank (Living/Bed) | 230 x 300 mm | +7135.4 mm (Terrace slab soffit) | **Terminated** (No extension) |
| **C6** | NE Front Corner (Sitout Gate) | 300 x 230 mm | +7135.4 mm (Terrace slab soffit) | **Terminated** (No extension) |
| **C7** | N Front Spine (Staircase Bay East) | 300 x 230 mm | +7135.4 mm (Terrace) -> +9460.4 mm | **Extended** (`Mumty_Col_C7`, 230 x 230 mm) flush with NE Post |
| **C8** | NW Front Corner (Boundary Parapet) | 300 x 230 mm | +7135.4 mm (Terrace slab soffit) | **Terminated** per IS 456 / IS 13920 |

> [!IMPORTANT]
> **Column C8 Termination Datum:** Column C8 terminates flush at the First Floor terrace slab soffit ($Z = +7135.4\text{ mm}$), identical to columns C1–C6. The unbraced freestanding cantilever post above the parapet has been removed, eliminating seismic drift risk, weathering exposure, and aesthetic disruption.

---

## 2. Staircase Headroom (Mumty) Tower Framing

* **Footprint:** $X \in [1714.5, 3810.0\text{ mm}]$, $Y \in [0.0, 1866.9\text{ mm}]$.
* **Clear Height:** $Z = 7135.4\text{ mm}$ to $Z = 9460.4\text{ mm}$ ($H = 2325.0\text{ mm}$, compliant with NBC 2016 minimum of $2100.0\text{ mm}$).
* **Vertical Corner Posts (228.6 x 228.6 mm / 9" x 9" M25 RCC):**
  1. `Mumty_Col_C7` / `Headroom_Col_NE`: $X = 1714.5\text{ mm}, Y = 0.0\text{ mm}, Z \in [7135.4, 9460.4\text{ mm}]$
  2. `Headroom_Col_NW`: $X = 3695.7\text{ mm}, Y = 0.0\text{ mm}, Z \in [7135.4, 9460.4\text{ mm}]$
  3. `Headroom_Col_SE`: $X = 1714.5\text{ mm}, Y = 1714.5\text{ mm}, Z \in [7135.4, 9460.4\text{ mm}]$
  4. `Headroom_Col_SW`: $X = 3695.7\text{ mm}, Y = 1714.5\text{ mm}, Z \in [7135.4, 9460.4\text{ mm}]$
* **Perimeter Ring Beams (D = 200 mm, Z in [9260.4, 9460.4 mm]):**
  - `Headroom_RB_Front_North` & `Headroom_RB_Rear_South` (Span = 2209.8 mm)
  - `Headroom_RB_East_Flank` & `Headroom_RB_West_Flank` (Span = 1485.9 mm)

---

## 3. Overhead Water Tank (OHT) Saddle Beam Rectification

* **Ballast Load:** 1,000 L domestic water tank + RCC plinth (~11 kN total load).
* **Saddle Beams:** Dual 230 x 230 mm M25 RCC beams (`OHT_Saddle_Beam_North` and `OHT_Saddle_Beam_South`).
* **Revised Span & Placement:**
  - Length: **2209.8 mm** ($X \in [1714.5, 3924.3\text{ mm}]$).
  - Elevation: $Z \in [9260.4, 9490.4\text{ mm}]$, embedded directly under the 200 mm OHT PCC pedestal plinth.
  - Bearing Seats: Beams bear squarely atop Mumty corner posts `Headroom_Col_NE` and `Headroom_Col_NW`.
* **Cantilever Overhang Elimination:** 0 mm external projection past the Mumty west wall ($X = 3890.0\text{ mm}$). All load transmission remains 100% internal to the Mumty structural cage.
