## 75. RCC Structural Optimization: 8-Column Frame Layout, Primary Living Hall Cross-Beam & Substructure Sync

> [!NOTE]
> **Engineering Discipline:** RCC Structural Frame & Substructure BIM Optimization  
> **Source Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Governing Codes:** IS 456:2000 (Plain and Reinforced Concrete), IS 13920:2016 (Ductile Design and Detailing of RCC Structures), IS 1904:2021 (Design and Construction of Foundations in Soils), NBC 2016 (Part 6 - Structural Design).  
> **Active Target Groups Synchronized:**
>
> 1. `Substructure_Foundation_Group` (`Column_Pedestals_Group`, `Isolated_Footings_Group`, `PCC_Blinding_Layer_Group`)
> 2. `Ground_Floor_Group` (`Columns`, `GF_Plinth_Beams`, `GF_Roof_Beams`)
> 3. `First_Floor_Group` (`FF_Columns`, `FF_Roof_Beams`)  
>    **Structural Concrete / Rebar Grade:** M25 Concrete ($f_{ck} = 25\text{ N/mm}^2$), Fe500D High-Yield Strength Deformed Steel ($f_y = 500\text{ N/mm}^2$).

---

### 75.1 Structural Engineering Rationale & Architectural Safeguards

To maximize usable carpet area, eliminate internal structural obstructions, and optimize construction economy without compromising load paths, the structural column layout was reorganized from **14 slender ($230 \times 230\text{ mm}$ / $9" \times 9"$) columns down to an optimized 8-column RCC frame ($230 \times 300\text{ mm}$ / $9" \times 12"$)**:

1. **Zero Architectural Compromise:**
   - **Room Dimensions Intact:** Sitout ($1486 \times 1486\text{ mm}$), Living Room ($4724 \times 3230\text{ mm}$), Kitchen ($1715 \times 2172\text{ mm}$), Master Bedroom ($2794 \times 2794\text{ mm}$), and Toilet ($957.5 \times 1680\text{ mm}$) remain 100% unchanged.
   - **Wall Flush Embedding:** All column sections embed flush into the $200\text{ mm}$ ($8"$) exterior envelope or partition wall alignments, eliminating internal pilaster protrusions into usable living and bedroom floor spaces.
   - **Living Room Column-Free Hall:** The entire Living Room ($15'\text{-}6" \times 10'\text{-}7.5"$) is 100% open and column-free.

2. **Load Redistribution & Primary Cross-Beam (`RB-LIVING`):**
   - Eliminating interior columns (`Col_Notch`, `Col_West_Bedroom`, `Col_Stair_SW`, `Col_Stair_SE`, etc.) transfers upper-floor masonry and intermediate slab loads onto a newly engineered **Primary Living Hall Cross-Beam (`RB_LIVING_Primary`)** spanning $5029.2\text{ mm}$ ($16'\text{-}6"$) E-W across the Living/Bed-Kitchen dividing wall line at $230 \times 350\text{ mm}$ ($9" \times 14"$) in M25 concrete.
   - Perimeter south rear beam depth was upsized from $300\text{ mm}$ to $375\text{ mm}$ (`RB1_Rear_South` and `PB1_Rear_South`) to safely handle the clear span between C1 and C3.

---

### 75.2 Coordinate Datum Mapping

- **Plot Origin:** South-East rear boundary corner ($X = 0.0\text{ mm}, Y = 0.0\text{ mm}$).
- **Width Axis ($X$):** East ($0.0\text{ mm}$) $\to$ West ($5029.2\text{ mm}$) [$16'\text{-}6"$].
- **Depth Axis ($Y$):** South/Rear ($0.0\text{ mm}$) $\to$ North/Front Road ($7620.0\text{ mm}$) [$25'\text{-}0"$].
- **Model Coordinate Datum Conversion:** $\text{Model } Y = 7619.8\text{ mm} - \text{User } Y$.
- **Elevation Datums:** Road Level = $0.0\text{ mm}$; Plinth Beam Level = $+614.4\text{ mm}$; Finished Plinth / Column Base = $+914.4\text{ mm}$; First Floor Column Base = $+3962.4\text{ mm}$.

---

### 75.3 Exact 8-Column Schedule & Orientation Table

| Column ID | FreeCAD Object Name (GF) | FreeCAD Object Name (FF) | Functional Anchor & Grid Line                  | User CL $(X, Y)$ (mm) | Model Centroid $(X, Y)$ (mm) | Section $(L \times W)$ (mm) | Orientation & Structural Duty                                                         |
| :-------- | :----------------------- | :----------------------- | :--------------------------------------------- | :-------------------- | :--------------------------- | :-------------------------- | :------------------------------------------------------------------------------------ |
| **C1**    | `Col_SE_Rear_C1`         | `FF_Col_SE_Rear_C1`      | SE Corner (Rear: Kitchen outer corner)         | $(150.0, 114.3)$      | $(150.0, 7505.7)$            | $300 \times 228.6$          | $300\text{ mm}$ along South wall ($X$); Primary frame corner anchor.                  |
| **C2**    | `Col_S_Spine_C2`         | `FF_Col_S_Spine_C2`      | S Center (Rear: Bed / Kitchen dividing wall)   | $(2230.0, 114.5)$     | $(2230.0, 7505.5)$           | $300 \times 228.6$          | $300\text{ mm}$ along South wall ($X$); Ties rear masonry & partition spine.          |
| **C3**    | `Col_SW_Rear_C3`         | `FF_Col_SW_Rear_C3`      | SW Corner (Rear: Master Bed outer corner)      | $(4914.9, 78.6)$      | $(4914.9, 7541.4)$           | $228.6 \times 300$          | $300\text{ mm}$ along West wall ($Y$); Primary frame corner anchor.                   |
| **C4**    | `Col_MidE_C4`            | `FF_Col_MidE_C4`         | Mid-East (Living / Kitchen dividing line)      | $(114.3, 4422.2)$     | $(114.3, 3197.8)$            | $228.6 \times 300$          | $300\text{ mm}$ along East wall ($Y$); East anchor for `RB-LIVING` primary beam.      |
| **C5**    | `Col_MidW_C5`            | `FF_Col_MidW_C5`         | Mid-West (Living / Bedroom outer wall)         | $(4914.9, 4422.2)$    | $(4914.9, 3197.8)$           | $228.6 \times 300$          | $300\text{ mm}$ along West wall ($Y$); West anchor for `RB-LIVING` primary beam.      |
| **C6**    | `Col_NE_Front_C6`        | `FF_Col_NE_Front_C6`     | NE Corner (Front: Sitout / Porch outer edge)   | $(150.0, 7505.7)$     | $(150.0, 114.3)$             | $300 \times 228.6$          | $300\text{ mm}$ along North facade ($X$); Front road frame / Porch anchor.            |
| **C7**    | `Col_N_Stair_C7`         | `FF_Col_N_Stair_C7`      | N Center (Front: Sitout / Stair spine divider) | $(1714.5, 7505.7)$    | $(1714.5, 114.3)$            | $300 \times 228.6$          | $300\text{ mm}$ along North facade ($X$); Dog-leg staircase & trimmer anchor.         |
| **C8**    | `Col_NW_Mumty_C8`        | `FF_Col_NW_Mumty_C8`     | NW Corner (Front: Toilet outer / Mumty anchor) | $(4950.6, 7505.7)$    | $(4950.6, 114.3)$            | $300 \times 228.6$          | $300\text{ mm}$ along North facade ($X$); Stair turnaround & Rooftop 1,000L OHT base. |

---

### 75.4 Obsolete Structural Elements Removed

The following 6 redundant columns and their corresponding substructure pedestals, isolated footings, and partial stub beams were excised cleanly across all document layers:

| Obsolete Element (GF / FF)                     | Former Centroid Location $(X, Y)$ | Level / Group               | Rationale for Removal                                                             |
| :--------------------------------------------- | :-------------------------------- | :-------------------------- | :-------------------------------------------------------------------------------- |
| `Col_N_Toilet_Stair` / `FF_Col_N_Toilet_Stair` | $(3695.7, 0.0)$                   | GF & FF Columns             | Intermediate North wall post; load consolidated to C8 via `RB2_Core_GridB`.       |
| `Col_Stair_SW` / `FF_Col_Stair_SW`             | $(3695.7, 1714.5)$                | GF & FF Columns             | Stair cell interior post; loads carried by landing trimmer beams.                 |
| `Col_Stair_SE` / `FF_Col_Stair_SE`             | $(1714.5, 1714.5)$                | GF & FF Columns             | Stair cell interior post; loads carried by landing trimmer beams.                 |
| `Col_West_Toilet` / `FF_Col_West_Toilet`       | $(4800.6, 1714.5)$                | GF & FF Columns             | Redundant post on West boundary; anchored by C5 and C8.                           |
| `Col_East_Sitout` / `FF_Col_East_Sitout`       | $(0.0, 1714.5)$                   | GF & FF Columns             | Redundant post on East boundary; anchored by C4 and C6.                           |
| `Col_Notch` / `FF_Col_Notch`                   | $(1866.9, 5067.3)$                | GF & FF Columns             | Deep interior post; load fully bridged by new continuous `RB-LIVING`.             |
| `Pedestal_C6`, `C7`, `C11`, `C5`, `C8`, `C14`  | Various Substructure              | `Column_Pedestals_Group`    | Substructure pedestal stubs corresponding to the 6 deleted columns.               |
| `Footing_C13`, `C14`, `C4`, `C_SP`             | Substructure $(Z = -1500)$        | `Isolated_Footings_Group`   | Superseded by the new standardized 8-footing layout.                              |
| `PCC_Bed_C13`, `C14`, `C4`, `C_SP`             | Substructure $(Z = -1600)$        | `PCC_Blinding_Layer_Group`  | Superseded by the new standardized 8-bed PCC layout.                              |
| `RB2_Kitchen_Living` / `PB2_Kitchen_Living`    | $Y = 5067.3\text{ mm}$            | GF / FF Roof & Plinth Beams | Partial stub beam terminating at deleted `Col_Notch`; replaced by `RB-LIVING`.    |
| `RB2_Bed_Kit_Spine` / `PB2_Bed_Kit_Spine`      | $X = 1866.9\text{ mm}$            | GF / FF Roof & Plinth Beams | Partial stub beam terminating at deleted interior posts; replaced by `RB-LIVING`. |

---

### 75.5 Beam & Substructure Schedule Updates

#### A. New & Modified Framing Beams

| Beam Identifier        | Group             | Placement Coordinates $(X, Y, Z)$ (mm) | Dimensions $(L \times W \times D)$ (mm)     | Specification & Engineering Function                                                                              |
| :--------------------- | :---------------- | :------------------------------------- | :------------------------------------------ | :---------------------------------------------------------------------------------------------------------------- |
| `RB_LIVING_Primary`    | `GF_Roof_Beams`   | $(0.0, 3047.8, 3662.4)$                | $5029.2 \times 228.6 \times 350.0$          | **Primary Living Cross-Beam:** Spans C4 $\to$ C5 ($9" \times 14"$ in M25/Fe500D). Carries upper AAC wall load.    |
| `PB_LIVING_Primary`    | `GF_Plinth_Beams` | $(0.0, 3047.8, 614.4)$                 | $5029.2 \times 228.6 \times 300.0$          | **Primary Plinth Tie Beam:** Spans C4 $\to$ C5 at plinth level (+3' 0") capping foundation stem wall.             |
| `FF_RB_LIVING_Primary` | `FF_Roof_Beams`   | $(0.0, 3047.8, 6835.4)$                | $5029.2 \times 228.6 \times 350.0$          | **First Floor Primary Cross-Beam:** 1:1 duplicate framing for upper storey roof.                                  |
| `RB1_Rear_South`       | `GF_Roof_Beams`   | $(0.0, 7391.4, 3662.4)$                | $5029.2 \times 228.6 \times \mathbf{375.0}$ | **Depth Upgraded ($300 \to 375\text{ mm}$):** Spans C1 $\to$ C3 clear span safely without middle post deflection. |
| `PB1_Rear_South`       | `GF_Plinth_Beams` | $(0.0, 7391.4, 614.4)$                 | $5029.2 \times 228.6 \times \mathbf{375.0}$ | **Depth Upgraded ($300 \to 375\text{ mm}$):** Continuous plinth tie spanning C1 $\to$ C3.                         |

#### B. Substructure Isolated Footings & Pedestals (8-Column Configuration)

- **Pedestals ($230 \times 300\text{ mm}$ M25, $Z \in [-1200.0, +614.4\text{ mm}]$, Height $= 1814.4\text{ mm}$):**  
  `Pedestal_C1`, `Pedestal_C_SP` (C2), `Pedestal_C2` (C3), `Pedestal_C13` (C4), `Pedestal_C4` (C5), `Pedestal_C9` (C6), `Pedestal_C10` (C7), `Pedestal_C12` (C8).
- **Isolated Footings ($400\text{ mm}$ M25 RCC, $Z \in [-1500.0, -1100.0\text{ mm}]$):**  
  `Footing_N8_C1` ($1500 \times 1428\text{ mm}$), `Footing_N8_C_SP` ($1500 \times 1428\text{ mm}$), `Footing_N8_C2` ($1428 \times 1500\text{ mm}$), `Footing_N8_C13` ($1428 \times 1500\text{ mm}$), `Footing_N8_C4` ($1428 \times 1500\text{ mm}$), `Footing_N8_C9` ($1500 \times 1428\text{ mm}$), `Footing_N8_C10` ($1500 \times 1428\text{ mm}$), `Footing_N8_C12` ($1500 \times 1428\text{ mm}$).
- **PCC Blinding Beds ($100\text{ mm}$ M10 Blinding, $Z \in [-1600.0, -1500.0\text{ mm}]$):**  
  8 matching PCC pads projected $50\text{ mm}$ beyond each footing perimeter (`PCC_N8_C1` through `PCC_N8_C12`).

---

### 75.6 Underground Sump & Septic Tank Substructure Clearances

1. **Underground Sump ($3,888\text{ L}$, $X \in [228.6, 1714.5\text{ mm}]$, $Y \in [228.6, 1714.5\text{ mm}]$, $Z \in [-1200, 914.4\text{ mm}]$):**
   - Sump is isolated on its own base raft `Sump_Raft_Foundation_Slab`.
   - **C7 (N Stair Spine)** at $X = 1714.5\text{ mm}$ directly bounds the East wall of the staircase; C6 at $X = 150.0\text{ mm}$ bounds the Porch.
   - **Substructure Coordination Note:** For the North front boundary, a combined continuous strip raft is recommended for columns C6 and C7 to seamlessly integrate with the Sump tank pit walls, avoiding individual pad overlap in deep excavation.
2. **Septic Tank ($2,592\text{ L}$, $X \in [3924.3, 4800.6\text{ mm}]$, $Y \in [228.6, 1714.5\text{ mm}]$, $Z \in [-1200, 914.4\text{ mm}]$):**
   - Maintained safely adjacent to `Septic_Raft_Foundation_Slab`.
   - C8 ($X = 4950.6\text{ mm}$) anchors the NW corner outside the tank perimeter, keeping the septic inspection zone accessible and unencumbered.

---

### 75.7 Verification & Quality Certification

- **Master Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)
- **Idempotent Automation Script:** [`col_8_optimize.py`](file:///c:/Users/prade/.gemini/antigravity/brain/00c48360-4b9f-4264-850c-1415ae2701a3/col_8_optimize.py)
- **Automated Test Results:** **STATUS: PASS (11 / 11 Checks Green)**
  - `GF Columns` count = 8 (all manifold solids, valid shapes)
  - `FF Columns` count = 8 (all manifold solids, valid shapes)
  - All 8 column cross-sections verified: $230 \times 300\text{ mm}$ ($9" \times 12"$)
  - `RB_LIVING_Primary` verified: $5029.2 \times 228.6 \times 350.0\text{ mm}$ (M25)
  - Zero deleted column entities remaining in document
  - Living Room column-free zone confirmed (Model $Y \in [228.6, 3047.8\text{ mm}]$ completely open)

---

### 75.8 Secondary Structural Elements Refactoring & Rooftop Mumty Frame

To achieve 100% monolithic frame alignment with columns `C1` through `C8`, all secondary structural members, seismic ring bands, and rooftop supports were audited and refactored:

1. **Partition & Divider Beams Re-anchored:**
   - `PB2_Bedroom_Living`, `RB2_Bedroom_Living`, `FF_RB2_Bedroom_Living`: Start position shifted from $X = 1866.9\text{ mm}$ to $X = 1981.2\text{ mm}$ (flush with bedroom east wall) and length adjusted to $2819.4\text{ mm}$, terminating flush into Column C5 inner face at $X = 4800.6\text{ mm}$.
   - `PB2_Stair_East`, `RB2_Stair_East_Trimmer`, `FF_RB2_Stair_East_Trimmer`: Position shifted to $X = 1564.5\text{ mm}$ with length $300.0\text{ mm}$, perfectly matching Column C7 width.
2. **Seismic Ring Bands Aligned:**
   - `GF_Continuous_Lintel_Toilet_Front`, `GF_Continuous_Sill_Toilet_Front`, `FF_Continuous_Lintel_Toilet_Front`, `FF_Continuous_Sill_Toilet_Front`: Length trimmed from $1066.8\text{ mm}$ to $990.6\text{ mm}$, ensuring clean flush termination at Column C8 ($X = 4800.6\text{ mm}$) without any external overhang.
3. **Rooftop Mumty Pillars & OHT Saddle Beams Rectification:**
   - **Pruning Overextended Column C8:** Column C8 terminates flush at the First Floor terrace slab soffit ($Z = +7135.4\text{ mm}$), identical to perimeter columns C1–C6. The rogue freestanding cantilever post (`Mumty_Col_C8`) above the parapet was eliminated per IS 456 / IS 13920.
   - **Reconciling Mumty Column C7:** Column C7 vertical extension (`Mumty_Col_C7`, $230 \times 230\text{ mm}$) is aligned flush with the Mumty East frame post (`Headroom_Col_NE`) at $X = 1714.5\text{ mm}, Y = 0.0\text{ mm}, Z \in [7135.4, 9460.4\text{ mm}]$.
   - **Trimmed OHT Saddle Beams:** Dual $230 \times 230\text{ mm}$ RCC saddle beams (`OHT_Saddle_Beam_North` and `OHT_Saddle_Beam_South`) in M25 concrete trimmed to length $2209.8\text{ mm}$ spanning $X \in [1714.5, 3924.3\text{ mm}]$. The beams bear squarely atop Mumty corner posts `Headroom_Col_NE` and `Headroom_Col_NW` directly below the 1,000 L OHT pedestal plinth with zero external overhang past the Mumty west wall.

---

### 75.9 Full-Structure FEM Linear Static Analysis & CalculiX Load Test (IS 456 & IS 875 Compliance)

A full-structure finite element simulation was re-executed directly on the refactored monolithic primary RCC frame ($V = 27.431\text{ m}^3$, 72 load-bearing solids including 8 boundary-contained footings) in [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd) using FreeCAD FEM & CalculiX (`ccx` static analysis) incorporating the newly optimized, boundary-contained foundation and superstructure geometry.

#### A. Finite Element Mesh & Parameters

- **Structural Scope (72 Monolithic Solids):** 8 Footings/Rafts, 8 Pedestals, 9 Plinth Beams, 8 GF Columns, 9 GF Roof Beams, 1 GF Roof/FF Floor Slab (`Roof_Slab`), 8 FF Columns, 9 FF Roof Beams, 1 Terrace Slab (`Terrace_Roof_Slab`), and 11 Rooftop Mumty & OHT saddle frame members.
- **Material Properties (M25 Concrete):** Young's modulus $E = 25,000\text{ MPa}$, Poisson's ratio $\nu = 0.18$, Density $\rho = 2,500\text{ kg/m}^3$.
- **Mesher:** Gmsh 3D quadratic 10-node tetrahedrals (`C3D10`), characteristic element length $h \in [150, 200]\text{ mm}$.
- **Boundary Conditions:** Fixed base supports ($U_x = U_y = U_z = 0$) applied to the 8 foundation footing bottom bearing faces at base excavation level ($Z = -1600.0\text{ mm}$, footprint area strictly inside $X \in [0, 5029.2], Y \in [0, 7619.8]$).
- **Applied Gravity & Live Loads (IS 875 Part 2):**
  - Self-weight: $g = -9.81\text{ m/s}^2$ ($Z$-axis), total concrete self-weight = $672.75\text{ kN}$.
  - Ground Floor Plinth Live Load: $2.0\text{ kN/m}^2$ uniform pressure across plinth beam top faces ($17.16\text{ kN}$).
  - First Floor Slab Live Load: $2.0\text{ kN/m}^2$ uniform pressure across $34.24\text{ m}^2$ floor area ($68.48\text{ kN}$).
  - Terrace Slab Live Load: $1.5\text{ kN/m}^2$ uniform pressure across $34.51\text{ m}^2$ area ($51.77\text{ kN}$).
  - Overhead Water Tank (OHT): $11.0\text{ kN}$ downward load applied directly across the trimmed $2209.8\text{ mm}$ saddle beams above Mumty posts.
  - **Total Applied Vertical Gravity Load:** $821.16\text{ kN}$.
  - **Total Substructure Vertical Reaction ($F_z$):** $810.41\text{ kN}$ (CalculiX static equilibrium agreement: **$98.69\%$**).

#### B. Floor-by-Floor Stress & Deflection Summary Table

| Floor Level | Elevation Range $Z$ (mm) | Node Count | Element Count | Max Downward Deflection $U_z$ (mm) | Max Resultant Disp $\|U\|$ (mm) | Max von Mises Stress (MPa) | Avg von Mises Stress (MPa) | Permissible Stress Limit (IS 456) | Safety Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Substructure (Footings & Pedestals)** | $[-1600.0, +614.4]$ | 16,378 | 6,994 | $-5.519\text{ mm}$ | $5.524\text{ mm}$ | $3.564\text{ MPa}$ | $0.549\text{ MPa}$ | $\sigma_{cbc} = 8.5\text{ MPa}$ / $f_{ck} = 25\text{ MPa}$ | **PASS** |
| **Ground Floor (PB, C1–C8, RB)** | $[+614.4, +4087.4]$ | 40,302 | 19,380 | $-5.519\text{ mm}$ | $5.529\text{ mm}$ | $3.381\text{ MPa}$ | $0.506\text{ MPa}$ | $\sigma_{cbc} = 8.5\text{ MPa}$ / $f_{ck} = 25\text{ MPa}$ | **PASS** |
| **First Floor (Slab, C1–C8, RB)** | $[+3962.4, +7260.4]$ | 47,602 | 23,313 | $-1.817\text{ mm}$ | $1.820\text{ mm}$ | $3.077\text{ MPa}$ | $0.476\text{ MPa}$ | $\sigma_{cbc} = 8.5\text{ MPa}$ / $f_{ck} = 25\text{ MPa}$ | **PASS** |
| **Terrace & Rooftop (Slab, Mumty, OHT)** | $[+7135.4, +9490.4]$ | 21,641 | 10,406 | $-1.809\text{ mm}$ | $1.810\text{ mm}$ | $3.391\text{ MPa}$ | $0.468\text{ MPa}$ | $\sigma_{cbc} = 8.5\text{ MPa}$ / $f_{ck} = 25\text{ MPa}$ | **PASS** |

#### C. Engineering Compliance Verdict

1. **Deflection Limits (IS 456 Cl. 23.2):** Max permissible deflection across the critical $5.029\text{ m}$ living room span is $\text{Span}/250 = 20.12\text{ mm}$. The observed maximum downward deflection is $5.519\text{ mm}$, well within the permissible threshold ($27.4\%$ of allowance).
2. **Stress Concentrations (IS 456 Cl. 34.4):** Peak von Mises stress in the critical superstructure zones is $3.381\text{ MPa}$ (and $3.564\text{ MPa}$ at footing necks), safely below the permissible direct compressive bending stress ($\sigma_{cbc} = 8.5\text{ MPa}$) and characteristic compressive strength ($f_{ck} = 25.0\text{ MPa}$).
3. **Equilibrium & Support Stability:** Total vertical reaction of $810.41\text{ kN}$ matches applied gravity loads within $1.31\%$, with horizontal reactions resolving to zero ($\Sigma F_x \approx 0, \Sigma F_y \approx 0$).
4. **Artifact Persistence:**
   - Solver Input Deck: [`docs/fem_results/full_structure_g1.inp`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/docs/fem_results/full_structure_g1.inp)
   - Raw Results Deck: [`docs/fem_results/full_structure_g1.frd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/docs/fem_results/full_structure_g1.frd)
   - Reaction Forces Deck: [`docs/fem_results/full_structure_g1.dat`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/docs/fem_results/full_structure_g1.dat)
   - CSV Stress & Deflection Summary: [`docs/fem_results/structural_stress_summary.csv`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/docs/fem_results/structural_stress_summary.csv)
