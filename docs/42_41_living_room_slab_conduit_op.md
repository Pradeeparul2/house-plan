## 41. Living Room Slab Conduit Optimization

### Summary
Optimized the **Living Room** roof-slab conduit network (`Living_Slab_Conduit_Network`) from a radial "spider-web" pattern into a clean **orthogonal spine-and-header grid**.

### Problem: Radial Star Pattern
The original conduits had all 20 solid segments radiating diagonally from the central ceiling fan box — a classic "star topology" anti-pattern:
- Multiple diagonal runs crossing the full room width
- Redundant overlapping segments near the south partition (SB-LR, SB-TV area)
- Criss-cross tangles in the north zone (dining switchboard area)
- Long diagonal run for the AC socket on the west wall
- Total conduit volume: 10,239,165 mm³ (slab runs) + 8,305,395 mm³ (wall drops) = **18.5M mm³**

### Solution: Orthogonal Grid Architecture
Replaced all diagonal runs with a 9-segment orthogonal grid:

| Segment | Route | Purpose |
|---------|-------|---------|
| N-S Spine | X=2514.6mm, Y: 1925→4925 | Central backbone through room |
| E-W Header FRONT | Y=2500mm, X: 1200→3800 | Connects DL-1 ↔ DL-2 (front downlights) |
| E-W Header REAR | Y=4000mm, X: 1200→3800 | Connects DL-3 ↔ DL-4 (rear downlights) |
| South Cross-bar | Y=1925mm, X: 2100→3560 | SB-LR ↔ SB-TV at south partition |
| DIN-1 Branch | Y=4697.5mm, X: 1925→2514 | Dining socket 1 |
| DECO Branch | Y=4692.5mm, X: 2514→2937 | Decorative strip socket |
| DIN-2/BED Branch | Y=4925mm, X: 1867→2514 | Dining 2 + bedroom switch |
| AC Run | Y=3275mm, X: 2514→4844 | AC split socket (west wall) |
| MCB Feed | Y=2150mm, X: 200→2514 | Main distribution panel feed |

### Results
| Metric | Before | After | Reduction |
|--------|--------|-------|-----------|
| Slab conduit segments | 20 solids | 9 clean pipes | 55% fewer |
| Slab conduit volume | 10,239,165 mm³ | 7,836,114 mm³ | **23.5% less** |
| Wall drops volume | 8,305,395 mm³ | 7,035,989 mm³ | **15.3% less** |
| Combined reduction | 18,544,560 mm³ | 14,872,103 mm³ | **~19.8% total** |

### Fixtures Preserved
- **Living_Slab_Fan_Box** — Ceiling fan junction box at (2514.6, 3257.4) — unchanged
- **Living_Slab_Light_Pots** — 4× downlights at corners: (1200,2500), (3800,2500), (1200,4000), (3800,4000)
- **8 switchboard wall drops** — SB1/MCB, SB-LR, SB-TV, SB-AC, SB-DIN1, SB-DIN2, SB-BED, SB-DECO

### First Floor Sync
All changes mirrored to `FF_Electrical_Slab_Conduit_Network`, `FF_Electrical_Slab_Wall_Drops`, and `FF_Electrical_Slab_Light_Pots` at ΔZ=+3173mm (First Floor offset).

### Files Modified
- `HomeConstruction.FCStd` — `Living_Slab_Conduit_Network`, `Living_Slab_Wall_Drops`, `Living_Slab_Light_Pots`, `Living_Slab_Fan_Box` updated and saved.


---
