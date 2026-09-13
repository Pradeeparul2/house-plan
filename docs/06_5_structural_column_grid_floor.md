## 5. Structural Column Grid & Floor Levels

> [!IMPORTANT]
> **Active Frame Optimization (Refer to Section 75):** The model's RCC structural frame has been updated from the initial 14 slender ($230 \times 230\text{ mm}$) columns to an optimized **8-column ($230 \times 300\text{ mm}$ / $9" \times 12"$) frame layout** with a continuous primary living cross-beam (`RB_LIVING_Primary`), making the entire Living Hall completely column-free. Detailed engineering schedules and centroid coordinates for the active 8-column system are documented in [Section 75](#75-rcc-structural-optimization-8-column-frame-layout-primary-living-hall-cross-beam--substructure-sync).

The building was originally structured on a **14-column Reinforced Concrete (RCC) frame** designed for seismic resistance and two-storey vertical load transmission.

```
       X = 0               X = 1714.5        X = 3695.7    X = 5029.2
Y=7620 [C1: Col_SE]----------------------------------------[C2: Col_SW]   (Rear Wall)
       |                                                   |
       |                   BEDROOM (10x10)                 |
Y=5181 [C3: Col_Mid_E]-------------------------------------[C4: Col_Mid_W]  (Bed/Living)
       |                                                   |
       |                   LIVING ROOM (16x9)              |
Y=1714 [C5: Col_East_Sitout]-[C6: Col_Stair_SE]--[C7: Col_Stair_SW]-[C8: Col_W_Toilet]
       |                      |                  |         |
       |      SITOUT (6x6)    |  STAIRCASE (6x7) |         |  TOILET (4x6)
Y=0    [C9: Col_NE]-----------[C10: Col_N_Stair]-[C11: Col_N_Toilet]-[C12: Col_NW] (Front)
```

### 5.1 Structural Column Schedule

| Col ID  | FreeCAD Object Name         | X Coordinate (mm)           | Y Coordinate (mm)           | Cross Section                                   | Vertical Span (Z)                    |
| :------ | :-------------------------- | :-------------------------- | :-------------------------- | :---------------------------------------------- | :----------------------------------- |
| **C1**  | `Col_SE_Corner`             | $0.0 \rightarrow 228.6$     | $7391.4 \rightarrow 7620.0$ | $228.6 \times 228.6\text{ mm}$ ($9" \times 9"$) | $914.4 \rightarrow 3962.4\text{ mm}$ |
| **C2**  | `Col_SW_Corner`             | $4800.6 \rightarrow 5029.2$ | $7391.4 \rightarrow 7620.0$ | $228.6 \times 228.6\text{ mm}$                  | $914.4 \rightarrow 3962.4\text{ mm}$ |
| **C3**  | `Col_Bed_East_Mid`          | $0.0 \rightarrow 228.6$     | $5181.6 \rightarrow 5410.2$ | $228.6 \times 228.6\text{ mm}$                  | $914.4 \rightarrow 3962.4\text{ mm}$ |
| **C4**  | `Col_Bed_West_Mid`          | $4800.6 \rightarrow 5029.2$ | $5181.6 \rightarrow 5410.2$ | $228.6 \times 228.6\text{ mm}$                  | $914.4 \rightarrow 3962.4\text{ mm}$ |
| **C5**  | `Col_East_Sitout`           | $0.0 \rightarrow 228.6$     | $1714.5 \rightarrow 1943.1$ | $228.6 \times 228.6\text{ mm}$                  | $914.4 \rightarrow 3962.4\text{ mm}$ |
| **C6**  | `Col_Stair_SE`              | $1714.5 \rightarrow 1943.1$ | $1714.5 \rightarrow 1943.1$ | $228.6 \times 228.6\text{ mm}$                  | $914.4 \rightarrow 3962.4\text{ mm}$ |
| **C7**  | `Col_Stair_SW`              | $3695.7 \rightarrow 3924.3$ | $1714.5 \rightarrow 1943.1$ | $228.6 \times 228.6\text{ mm}$                  | $914.4 \rightarrow 3962.4\text{ mm}$ |
| **C8**  | `Col_Toilet_West`           | $4800.6 \rightarrow 5029.2$ | $1714.5 \rightarrow 1943.1$ | $228.6 \times 228.6\text{ mm}$                  | $914.4 \rightarrow 3962.4\text{ mm}$ |
| **C9**  | `Col_NE_Corner` (White Fin) | $0.0 \rightarrow 228.6$     | $0.0 \rightarrow 228.6$     | $228.6 \times 228.6\text{ mm}$                  | $914.4 \rightarrow 3962.4\text{ mm}$ |
| **C10** | `Col_N_Stair_Sitout`        | $1714.5 \rightarrow 1943.1$ | $0.0 \rightarrow 228.6$     | $228.6 \times 228.6\text{ mm}$                  | $914.4 \rightarrow 3962.4\text{ mm}$ |
| **C11** | `Col_N_Toilet_Stair`        | $3695.7 \rightarrow 3924.3$ | $0.0 \rightarrow 228.6$     | $228.6 \times 228.6\text{ mm}$                  | $914.4 \rightarrow 3962.4\text{ mm}$ |
| **C12** | `Col_NW_Corner`             | $4800.6 \rightarrow 5029.2$ | $0.0 \rightarrow 228.6$     | $228.6 \times 228.6\text{ mm}$                  | $914.4 \rightarrow 3962.4\text{ mm}$ |
| **C13** | `Col_Kitchen_Mid_E`         | $0.0 \rightarrow 228.6$     | $3467.1 \rightarrow 3695.7$ | $228.6 \times 228.6\text{ mm}$                  | $914.4 \rightarrow 3962.4\text{ mm}$ |
| **C14** | `Col_Kitchen_Mid_W`         | $1943.1 \rightarrow 2171.7$ | $5181.6 \rightarrow 5410.2$ | $228.6 \times 228.6\text{ mm}$                  | $914.4 \rightarrow 3962.4\text{ mm}$ |

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
