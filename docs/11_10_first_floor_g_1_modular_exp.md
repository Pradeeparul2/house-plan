## 10. First Floor (G+1) Modular Expansion Design

The complete First Floor model is fully constructed and stored inside [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd) under [`First Floor (Complete)`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd).

### 10.1 Vertical Datum Translation

- **Ground Floor FFL:** $Z = 914.4\text{ mm}$
- **Intermediate Slab Underside:** $Z = 3962.4\text{ mm}$ ($10'\text{-}0"$ ceiling clearance)
- **First Floor FFL:** $Z = 4087.4\text{ mm}$ ($125\text{ mm}$ slab)
- **Vertical Translation Offset ($\Delta Z$):** $\mathbf{+3173.0\text{ mm}}$ ($10'\text{-}5"$)
- **First Floor Ceiling:** $Z = 7135.4\text{ mm}$
- **Terrace Roof Slab:** $Z \in [7135.4, 7260.4\text{ mm}]$

### 10.2 First Floor Component Hierarchy

- `FF_Columns`: 14 RCC columns ($228.6 \times 228.6\text{ mm}$, $Z \in [4087.4, 7135.4\text{ mm}]$).
- `FF_Bedroom`: $10'\text{-}0" \times 10'\text{-}0"$ with 3-door wardrobe and RCC lofts.
- `FF_Kitchen`: $6'\text{-}0" \times 7'\text{-}0"$ with granite L-counter, breakfast bar, sink, and lofts.
- `FF_Toilet`: $4'\text{-}0" \times 6'\text{-}0"$ with dropped ceiling, wall-hung WC, and washbasin.
- `FF_Living_Room`: $16'\text{-}0" \times 9'\text{-}0"$ with entrance door and stair partition.
- `FF_Door_Main_Group`: Teak double door with signature white block architectural surround.
- `FF_Living_Room_Window_East_Group`: $1800 \times 1200\text{ mm}$ 3-split sliding UPVC window vertically aligned over the Ground Floor window.
- `FF_Balcony_Group`: Modern SS 304 balustrade, dark charcoal fascia beam with $45^\circ$ angled return, vertical white architectural fin, and canopy fascia.
- `FF_Staircase_Group`: Upper dog-legged staircase flight ($Z = 4087.4 \rightarrow 7135.4\text{ mm}$) to the rooftop.
- `FF_Roof_Terrace_Group`: $125\text{ mm}$ monolithic RCC slab with staircase headroom cutout.

> [!TIP]
> **To unhide the First Floor anytime:** Select [`First Floor (Complete)`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd) in the FreeCAD tree and press **Spacebar**, or prompt me to activate full G+1 mode.

---
