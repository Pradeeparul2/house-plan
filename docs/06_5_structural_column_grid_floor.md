## 5. Structural Column Grid & Floor Levels

> [!IMPORTANT]
> **Active Frame Optimization (Refer to Section 75):** The model's RCC structural frame has been updated from the initial 14 slender ($230 \times 230\text{ mm}$) columns to an optimized **8-column ($230 \times 300\text{ mm}$ / $9" \times 12"$) frame layout** with a continuous primary living cross-beam (`RB_LIVING_Primary`), making the entire Living Hall completely column-free. Detailed engineering schedules and centroid coordinates for the active 8-column system are documented in [Section 75](#75-rcc-structural-optimization-8-column-frame-layout-primary-living-hall-cross-beam--substructure-sync).

The building structure is an optimized **8-column Reinforced Concrete (RCC) monolithic space frame ($230 \times 300\text{ mm}$ / $9" \times 12"$)** in M25 concrete with Fe500D rebar, designed for seismic resistance, complete column-free living space, and two-storey vertical load transmission (IS 456 & IS 13920 compliant).

```
       X = 0 mm                           X = 2230 mm                        X = 4915 mm
Y=7506 [C1: Col_SE_Rear_C1]--------------[C2: Col_S_Spine_C2]----------------[C3: Col_SW_Rear_C3]  (Rear Wall)
       |                                                                     |
       |                              BEDROOM & KITCHEN                      |
Y=3198 [C4: Col_MidE_C4]=====================================================[C5: Col_MidW_C5]     (RB_LIVING_Primary)
       |                                                                     |
       |                         COLUMN-FREE LIVING HALL (16x10)             |
       |                                                                     |
       |            SITOUT                STAIRCASE BAY                      |  TOILET
Y=114  [C6: Col_NE_Front_C6]-------------[C7: Col_N_Stair_C7]----------------[C8: Col_NW_Mumty_C8] (Front Road)
```

### 5.1 Active 8-Column Structural Schedule ($230 \times 300\text{ mm}$)

| Column ID | FreeCAD Object Name (GF) | FreeCAD Object Name (FF) | Grid / Functional Anchor | Model Centroid $(X, Y)$ (mm) | Section $(L \times W)$ (mm) | Vertical Span $Z$ (mm) |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: |
| **C1** | `Col_SE_Rear_C1` | `FF_Col_SE_Rear_C1` | SE Corner (Kitchen rear outer) | $(150.0, 7505.7)$ | $300 \times 228.6$ | $+914.4 \to +3962.4$ |
| **C2** | `Col_S_Spine_C2` | `FF_Col_S_Spine_C2` | S Center (Bed/Kitchen wall spine) | $(2230.0, 7505.5)$ | $300 \times 228.6$ | $+914.4 \to +3962.4$ |
| **C3** | `Col_SW_Rear_C3` | `FF_Col_SW_Rear_C3` | SW Corner (Master Bed outer) | $(4914.9, 7541.4)$ | $228.6 \times 300$ | $+914.4 \to +3962.4$ |
| **C4** | `Col_MidE_C4` | `FF_Col_MidE_C4` | Mid-East (Living/Kit divider) | $(114.3, 3197.8)$ | $228.6 \times 300$ | $+914.4 \to +3962.4$ |
| **C5** | `Col_MidW_C5` | `FF_Col_MidW_C5` | Mid-West (Living/Bed divider) | $(4914.9, 3197.8)$ | $228.6 \times 300$ | $+914.4 \to +3962.4$ |
| **C6** | `Col_NE_Front_C6` | `FF_Col_NE_Front_C6` | NE Corner (Sitout front porch) | $(150.0, 114.3)$ | $300 \times 228.6$ | $+914.4 \to +3962.4$ |
| **C7** | `Col_N_Stair_C7` | `FF_Col_N_Stair_C7` | N Center (Stair spine divider) | $(1714.5, 114.3)$ | $300 \times 228.6$ | $+914.4 \to +3962.4$ |
| **C8** | `Col_NW_Mumty_C8` | `FF_Col_NW_Mumty_C8` | NW Corner (Toilet outer / Mumty) | $(4950.6, 114.3)$ | $300 \times 228.6$ | $+914.4 \to +3962.4$ |

*Note: Columns C7 and C8 extend upward through the rooftop terrace to $Z = +9460.4\text{ mm}$ (`Mumty_Col_C7`, `Mumty_Col_C8`) carrying dual $230 \times 230\text{ mm}$ OHT saddle beams supporting the 1,000 L overhead water tank. Full optimization details documented in [Section 75](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/docs/77_75_rcc_structural_optimization.md).*

### 5.2 Structural Beams Network (21 Beams Modeled in 3D)

A complete framed beam system conforming to **IS 456:2000** has been modeled directly into [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd) under `GF_Plinth_Beams` and `GF_Roof_Beams`:

#### A. Plinth Beams (Z = 614.4 to 914.4 mm | Depth = 300 mm | Finished Plinth +0.914m)

- **Perimeter Ring Beams (PB1 — 230 x 300 mm):**
  - `PB1_Front_North`: Front road facade spanning C1 to C4 ($L = 5029.2\text{ mm}$). Supports entrance steps, sitout safety gate, and front toilet wall.
  - `PB1_Rear_South`: Rear boundary spanning C12 to C14 ($L = 5029.2\text{ mm}$). Supports 9" rear exterior wall.
  - `PB1_East_Flank`: East property line spanning C1 to C12 ($L = 7620.0\text{ mm}$). Supports East exterior masonry.
  - `PB1_West_Flank`: West property line spanning C4 to C14 ($L = 7620.0\text{ mm}$). Supports continuous West exterior wall.
- **Internal Partition Tie Beams (PB2 & PB_LIVING):**
  - `PB_LIVING_Primary` (230 x 300 mm M25): Primary plinth tie beam spanning C4 to C5 across full width ($X = 0.0 - 5029.2\text{ mm}$ at $Y = 3047.8\text{ mm}$).
  - `PB2_Core_GridB` (230 x 300 mm): Transverse beam at $Y = 1714.5\text{ mm}$ spanning $X = 0.0 - 5029.2\text{ mm}$.
  - `PB2_Stair_East` (300 x 300 mm): Longitudinal beam at $X = 1564.5 - 1864.5\text{ mm}$ ($L = 300\text{ mm}$ in $X$, $1714.5\text{ mm}$ in $Y$) anchored into Column C7.
  - `PB2_Stair_West` (230 x 300 mm): Longitudinal beam at $X = 3695.7\text{ mm}$ ($L = 1714.5\text{ mm}$ in $Y$).
  - `PB2_Bedroom_Living` (230 x 300 mm): Transverse partition beam spanning $X = 1981.2 - 4800.6\text{ mm}$ ($L = 2819.4\text{ mm}$) flush between bedroom east wall and Column C5.

#### B. Roof Slab Downstand Beams (Z = 3662.4 to 4012.4 mm)

- **Perimeter Roof Frame Beams (RB1 — 230 x 350 mm / 375 mm):**
  - `RB1_Front_North`, `RB1_East_Flank`, `RB1_West_Flank` (230 x 350 mm): Boundary ring framing intermediate slab.
  - `RB1_Rear_South` (230 x 375 mm): Depth upgraded to 375 mm for extended clear span C1 to C3.
- **Internal Roof Framing Beams (RB2 & RB_LIVING):**
  - `RB_LIVING_Primary` (230 x 350 mm M25): Heavy primary cross-beam spanning C4 to C5 across full width ($X = 0.0 - 5029.2\text{ mm}$ at $Y = 3047.8\text{ mm}$).
  - `RB2_Core_GridB` (230 x 300 mm): Spans across Grid B at $Y = 1714.5\text{ mm}$.
  - `RB2_Stair_East_Trimmer` (300 x 300 mm): Anchored into Column C7 ($X = 1564.5 - 1864.5\text{ mm}$, $Y = 0.0 - 990.0\text{ mm}$).
  - `RB2_Stair_West_Trimmer` (230 x 300 mm): Spans $X = 3695.7\text{ mm}$, $Y = 0.0 - 1714.5\text{ mm}$.
  - `RB2_Bedroom_Living` (230 x 300 mm): Spans $X = 1981.2 - 4800.6\text{ mm}$ ($L = 2819.4\text{ mm}$) flush to Column C5.
  - `Kitchen_Beam_North` (230 x 228.6 mm): Monolithic drop beam over kitchen breakfast counter.

#### C. Staircase Mid-Landing Beam (Z = 2138.4 to 2438.4 mm | Depth = 300 mm)

- **`MLB_Staircase_Mid_Landing` (230 x 300 mm):**
  - Spans between Column C6 and Column C7 at $Z = 2438.4\text{ mm}$ ($+1.524\text{ m}$ above plinth).
  - Crucial structural role: Directly carries the waist slab turnaround for the external dog-leg staircase.

---
