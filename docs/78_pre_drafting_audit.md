# 78. Pre-Drafting Model Health & Specification Readiness Audit

> [!NOTE]
> **Engineering Discipline:** Pre-Drafting BIM Health & 2D TechDraw Readiness Certification  
> **Source Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Automated MCP Fix Script:** [`tools/pre_drafting_audit_and_fix.py`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/tools/pre_drafting_audit_and_fix.py)  
> **Governing Standards:** IS 456:2000, IS 13920:2016, IS 732:2019, NBC 2016 (Parts 3, 6, 8, 9).

---

## 78.1 Comprehensive Audit Overview

An exhaustive pre-drafting diagnostic audit was executed across all 629 entities in `HomeConstruction.FCStd` to verify geometric integrity, structural sanity, architectural envelope hygiene, MEP service containment, and 2D drawing sheet readiness.

### Key Audit Findings & Remediation Summary:
1. **Vertical Wall Soffit Clearances (FF Walls):** Trimming all 12 First Floor full-height masonry walls from $dz = 3048.0\text{ mm}$ to clear height $dz = 2748.0\text{ mm}$ eliminated all $300\text{ mm}$ penetrations into `FF_Roof_Beams`, yielding **0.00 mm³ collision volume**.
2. **Structural Frame Parity (`RB2_Bedroom_Living`):** Modeled and restored `RB2_Bedroom_Living` ($2819.4 \times 228.6 \times 300\text{ mm}$ M25) in `GF_Roof_Beams` at $(1981.2, 4457.7, 3662.4\text{ mm})$, creating 1:1 parity with Plinth (`PB2_Bedroom_Living`), FF Roof (`FF_RB2_Bedroom_Living`), and BBS (Items 68–71).
3. **8-Column Axial Alignment:** 0.00 mm drift verified across Foundation Pedestals, GF, and FF for all columns C1–C8 ($230 \times 300\text{ mm}$).
4. **Substructure Coordination:** Monolithic stepped raft abutment ($0.0\text{ mm}$ gap/overlap) between `Footing_N8_C12` and `Septic_Raft_Foundation_Slab` verified, and C6–C7 unified strip raft `Sump_Raft_Foundation_Slab` confirmed.
5. **MEP Flush Snapping:** All 16 modular switchboards snap flush with $0.0\text{ mm}$ air gap and maintain $\ge 150.0\text{ mm}$ clear distance from RCC column faces. Deep PVC junction boxes sit within the $125\text{ mm}$ slab core. Zero ghost conduits.
6. **2D TechDraw Readiness:** All 12 production drawing sheets certified **READY (PASS)**.

---

## 78.2 Pre-Drawing Discrepancy Matrix

| Component ID | Discipline | Issue Description | Clash / Gap Value | Status & Action Taken |
| :--- | :--- | :--- | :---: | :--- |
| `FF_Bedroom_Wall_South`<br>`FF_Kitchen_Wall_South`<br>`FF_Bedroom_Wall_West`<br>`FF_Living_Room_Wall_West`<br>`FF_Toilet_Wall_West`<br>`FF_Kitchen_Wall_East`<br>`FF_Living_Room_Wall_East`<br>`FF_Toilet_Wall_Front`<br>`FF_Bedroom_Wall_North`<br>`FF_Bedroom_Wall_East`<br>`FF_Living_Room_Wall_Main_Door`<br>`FF_Wall_Stair_SE_SW` | Architectural / Structural | FF walls extended into terrace slab soffit ($Z = 7135.4\text{ mm}$) instead of beam soffit ($Z = 6835.4\text{ mm}$), penetrating into FF roof beams. | **300.0 mm** vertical penetration ($>1.2\text{ m}^3$ overlap) | **RESOLVED**: Parametrically trimmed all 12 walls to clear height $dz = 2748.0\text{ mm}$ ($Z \in [4087.4, 6835.4\text{ mm}]$). Remaining clash volume: **0.00 mm³**. |
| `RB2_Bedroom_Living` | RCC Structural Frame | Beam omitted from `GF_Roof_Beams` in 3D model despite being scheduled in BBS (Items 68–71) and modeled at plinth and FF levels. | **Missing solid entity** | **RESOLVED**: Restored `RB2_Bedroom_Living` ($2819.4 \times 228.6 \times 300\text{ mm}$ M25) in `GF_Roof_Beams` at $(1981.2, 4457.7, 3662.4\text{ mm})$ flush to Column C5 inner face. |
| `Col_SE_Rear_C1` to `Col_NW_Mumty_C8` | RCC Structural Frame | Setting-out grid axial alignment across Foundation Pedestals, GF columns, and FF columns. | **0.00 mm** drift | **PASS**: Centroids verified identical across all storeys: C1 $(150.0, 7505.7)$, C2 $(2230.0, 7505.5)$, C3 $(4914.9, 7470.0)$, C4 $(114.3, 3197.8)$, C5 $(4914.9, 3197.8)$, C6 $(150.0, 114.3)$, C7 $(1714.5, 114.3)$, C8 $(4914.9, 150.0)$. |
| `PB_LIVING_Primary`<br>`RB_LIVING_Primary` | RCC Structural Frame | Boundary and transfer span across C4 to C5 inner/outer faces. | **0.00 mm** gap / overhang | **PASS**: Spans full $5029.2\text{ mm}$ width from $X = 0.0$ to $5029.2\text{ mm}$ at $Y = 3047.8\text{ mm}$ without pilaster protrusions. |
| `Footing_N8_C12` vs `Septic_Raft_Foundation_Slab` | Substructure Foundation | Abutment interface between C8 eccentric footing and Septic tank base raft. | **0.00 mm** gap / overlap | **PASS**: Unified stepped raft pad ($X \in [3695.7, 5029.2\text{ mm}]$, $Z \in [-1600, -1200\text{ mm}]$) meeting cleanly along $Y = 1200.0\text{ mm}$. |
| `Sump_Raft_Foundation_Slab` | Substructure Foundation | Front North foundation coordination for Columns C6 and C7 adjacent to 3,888 L Sump. | **0.00 mm** gap / overlap | **PASS**: Unified continuous strip raft pad ($1943.1 \times 1943.1 \times 400\text{ mm}$) seating C6, C7, and sump pit. |
| `Mumty_Col_C8` | Rooftop Structural Frame | Potential rogue column extension above rooftop terrace. | **0.00 mm** | **PASS**: Confirmed removed. Column C8 terminates at $Z = 7010.4\text{ mm}$ below terrace slab. |
| `OHT_Saddle_Beam_North`<br>`OHT_Saddle_Beam_South` | Rooftop Structural Frame | Overhead tank saddle beam span and terrace boundary projection. | **0.00 mm** projection | **PASS**: Length $2209.8\text{ mm}$ spanning $X \in [1714.5, 3924.3\text{ mm}]$ squarely over `Headroom_Col_NE` and `Headroom_Col_NW` without open terrace overhang. |
| `Living_Room_Wall_Main_Door`<br>`Wall_Stair_SE_SW` | Architectural Envelope | Masonry wall thickness upgrade from 100 mm to 200 mm (8"). | **0.00 mm** variance | **PASS**: Both walls measured at exactly $200.0\text{ mm}$ thickness. |
| `Living_Room_Wall_Main_Door` vs `Wall_Stair_SE_SW` | Architectural Envelope | Daylight gap at jamb return at $X = 1714.5\text{ mm}$. | **0.00 mm** daylight gap | **PASS**: Both walls meet at $X = 1714.5\text{ mm}$ and overlap along $Y \in [1714.5, 1814.5\text{ mm}]$. |
| `Toilet_Wall_North` vs `Wall_Stair_SE_SW` | Architectural Envelope | Collinear corridor alignment across D4 door opening. | **0.00 mm** collinear delta | **PASS**: Both walls share identical South datum plane $Y = 1714.5000\text{ mm}$. |
| All Doors & Windows | Joinery & Openings | Solid aperture web check through wall thickness. | **0.00 mm** uncut web | **PASS**: Cutouts project $10\text{ mm}$ beyond each face. 100% manifold solids. |
| Modular Switchboards (`SB_1` to `SB_16`, DBs) | MEP Electrical | Wall flush snap and RCC column clearance. | Gap: **0.0 mm**<br>Col clearance: **$\ge 150.0\text{ mm}$** | **PASS**: Flush snapped against wall faces. Minimum column clearance: $150.0\text{ mm}$ (SB-10 to C2), $152.2\text{ mm}$ (SB-16 to C5). |
| Slab Deep PVC Boxes | MEP Electrical | Containment within $125\text{ mm}$ slab core. | **0.00 mm** cage clash | **PASS**: Box depth $60.0\text{ mm}$ sitting within $Z \in [3962.4, 4022.4\text{ mm}]$ (GF) and $Z \in [7135.4, 7195.4\text{ mm}]$ (Terrace). |
| Electrical / Plumbing Conduits | MEP Services | Floating / degenerate / zero-length pipeline segments. | **0 ghost elements** | **PASS**: 0 zero-length conduits found. |
| Toilet Sunken Wet Area Floor | Architectural / Plumbing | Sunken slab depression for drainage traps. | **150.0 mm** drop | **PASS**: GF Wet Floor $Z = 764.4\text{ mm}$ vs Dry $Z = 914.4\text{ mm}$; FF Wet Floor $Z = 3937.4\text{ mm}$ vs Dry $Z = 4087.4\text{ mm}$. |
| Staircase Vertical Travel | Vertical Circulation | Uniformity of 17 risers, 4 winders, and headroom. | $\Delta R = \mathbf{0.00\text{ mm}}$<br>Headroom: **$>2150\text{ mm}$** | **PASS**: 17 risers @ $186.65\text{ mm}$, straight tread $249.25\text{ mm}$, 4 winders ($180^\circ$ turnaround), min headroom $2150\text{ mm} \ge 2100\text{ mm}$ NBC. |

---

## 78.3 2D TechDraw Drawing Sheet Readiness Scorecard

| Drawing Sheet Discipline & Title | Readiness Status | Target Projection / View Details | Governing Standards & Verification |
| :--- | :---: | :--- | :--- |
| **1. Setting-Out & Centerline Grid Sheet** | **READY (PASS)** | Centerline grid across 8 columns (`C1`–`C8`) with structural offsets, diagonal checks ($9.128\text{ m}$ living bay diagonal), and boundary offset datums ($X \in [0, 5029.2]$, $Y \in [0, 7620.0]$). | IS 1498, IS 1904. Column centroids 100% verified with 0.00 mm drift. Setting-out ready for site excavation. |
| **2. Substructure Foundation & Raft Plan** | **READY (PASS)** | Plan layout showing 6 isolated eccentric footings (`F1`, `F2`, `F3`, `F4`, `F5`, `F8`), unified Sump strip raft (`F6-F7`), Septic stepped raft pad, and $100\text{ mm}$ PCC blinding beds. | IS 1080, IS 1904. Zero encroachment past plot boundary enforced. Step interfaces and pit wall clearances fully coordinated. |
| **3. Ground Floor Architectural Plan** | **READY (PASS)** | Dimensioned floor plan showing Sitout ($1486 \times 1486$), Living Hall ($4724 \times 3230$), Kitchen ($1715 \times 2172$), Master Bedroom ($2794 \times 2794$), and Toilet ($957.5 \times 1680$) with door/window schedules. | NBC 2016 Part 3. $200\text{ mm}$ outer envelope and $100\text{ mm}$ interior partitions verified. Zero daylight gaps; apertures cut cleanly. |
| **4. First Floor Architectural Plan** | **READY (PASS)** | 1:1 duplicate floor plan featuring dust-protected Balcony/Sitout enclosure, identical room carpet areas, and access to upper stair flight. | NBC 2016 Part 3. Masonry wall clear height verified at $2748.0\text{ mm}$ terminating flush at beam soffit. Zero beam-wall clash. |
| **5. Terrace & Rooftop Headroom Plan** | **READY (PASS)** | Open terrace layout ($34.5\text{ m}^2$), $1000\text{ mm}$ parapet with precast coping, Mumty headroom tower, 1,000 L OHT on dual saddle beams, and solar water heater zone. | NBC 2016 Part 3. C8 cantilever trimmed; OHT saddle beams span strictly $2209.8\text{ mm}$ over headroom posts. |
| **6. Plinth Framing & Tie Beam Layout** | **READY (PASS)** | Structural framing plan at $Z = +614.4\text{ mm}$ showing `PB1` boundary beams ($230 \times 300\text{ mm}$), `PB_LIVING_Primary`, `PB2_Bedroom_Living`, and stair tie beams. | IS 456, IS 13920. All plinth beams terminate flush at finished plinth level $Z = +914.4\text{ mm}$ with zero step-up. |
| **7. Ground Floor Roof Framing Plan** | **READY (PASS)** | Structural slab beam layout at $Z = +3662.4\text{ mm}$ showing heavy transfer cross-beam `RB_LIVING_Primary` ($230 \times 350\text{ mm}$), `RB1_Rear_South` ($230 \times 375\text{ mm}$), and restored `RB2_Bedroom_Living`. | IS 456, IS 13920. 100% 9-beam framing system complete. Load path across Living Room unobstructed. |
| **8. First Floor Roof Framing Plan** | **READY (PASS)** | 1:1 duplicate structural roof beam layout at $Z = +6835.4\text{ mm}$ supporting intermediate terrace slab. | IS 456, IS 13920. Complete 9-beam framing system verified with 0 clash to trimmed masonry walls. |
| **9. Longitudinal Building Section (A-A)** | **READY (PASS)** | South-to-North longitudinal cross-section cutting through Master Bedroom, column-free Living Room, Entrance Sitout, and Porch. | NBC 2016 Part 3. Floor-to-floor heights ($3173.0\text{ mm}$) and clear headroom ($2748.0\text{ mm}$) verified uniform across storeys. |
| **10. Transverse Staircase Section (B-B)** | **READY (PASS)** | East-to-West cross-section cutting through Dog-leg 4-Winder Staircase core, Under-stair Laundry station, Sump pump pedestal, and Mumty tower. | NBC 2016 Part 3 Clause 4.4.2. Exactly 17 risers @ $186.65\text{ mm}$, $249.25\text{ mm}$ tread purchase, and min $2150\text{ mm}$ vertical headroom. |
| **11. Electrical Conduit & Switchboard Plan (GF & FF)** | **READY (PASS)** | Reflected ceiling plan and wall elevation showing slab conduits, fan boxes, deep junction pot boxes, modular switchboards (`SB_1` to `SB_16`), and MDBs. | IS 732:2019. Switchboards flush-snapped ($0\text{ mm}$ air gap), $\ge 150\text{ mm}$ clear of columns, deep boxes sit inside $125\text{ mm}$ slab core. |
| **12. Plumbing, Water Supply & Drainage Plan** | **READY (PASS)** | Integrated plumbing schematic showing municipal inflow, 3,888 L sump, rising main, OHT gravity down-takes, dual-stream drainage, and $150\text{ mm}$ sunken toilet drop. | IS 1742, IS 2470. Sunken slab drop ($150\text{ mm}$) verified on GF and FF. Sleeve runs through false duct coordinated. |
