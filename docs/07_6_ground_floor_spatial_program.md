## 6. Ground Floor Spatial Program & Room Schedules

```
+-------------------------------------------------------------------------+
|                  KITCHEN                |          BEDROOM              |
|             6'-0" x 7'-0" (E)           |     10'-0" x 10'-0" (W)       |
|    Counters, Sink, Hob, Lofts, Exhaust  | Bed, 3-Door Wardrobe, Lofts   |
+-----------------------------------------+-------------------------------+
|                               LIVING ROOM                               |
|                             16'-0" x 9'-0"                              |
|           Dining Nook, 3-Split East Window, Teak Double Door            |
+-------------------+---------------------+-------------------------------+
|      SITOUT       |      STAIRCASE      |            TOILET             |
|   6'-0" x 6'-0"   | Dog-legged Flights  |         4'-0" x 6'-0"         |
|   SS Gate & Steps | Washer & Pump Area  | Indian Pan, Washbasin, Shower |
+-------------------+---------------------+-------------------------------+
```

### 6.1 Room Dimensional & Fitting Schedule

| Room                  | Carpet Dimensions                                                       | Clear Area                              | Key Architectural Features & Fittings                                                                                                                                                                                                                                                        |
| :-------------------- | :---------------------------------------------------------------------- | :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sitout (Verandah)** | $1828.8 \times 1828.8\text{ mm}$ ($6'\text{-}0" \times 6'\text{-}0"$)   | $3.34\text{ m}^2$ ($36\text{ sq.ft}$)   | Anti-skid ceramic tiles, East decorative wall ($930\text{ mm}$ high), custom SS 304 & charcoal double-leaf safety gate.                                                                                                                                                                      |
| **Living Room**       | $4876.8 \times 2743.2\text{ mm}$ ($16'\text{-}0" \times 9'\text{-}0"$)  | $13.38\text{ m}^2$ ($144\text{ sq.ft}$) | Teakwood double door ($1050 \times 2100\text{ mm}$), East 3-split UPVC sliding window ($1800 \times 1200\text{ mm}$) with tinted glass and safety grill, breakfast counter opening into kitchen.                                                                                             |
| **Master Bedroom**    | $3048.0 \times 3048.0\text{ mm}$ ($10'\text{-}0" \times 10'\text{-}0"$) | $9.29\text{ m}^2$ ($100\text{ sq.ft}$)  | Burmese Teak door D2 ($914.4 \times 2133.6\text{ mm}$ / $3'\text{-}0" \times 7'\text{-}0"$) in original north wall placeholder, King-size bed with side tables, full-height 3-door wardrobe ($1800 \times 600 \times 2100\text{ mm}$), North & East storage lofts at $Z = 2438.4\text{ mm}$. |
| **Kitchen**           | $1828.8 \times 2133.6\text{ mm}$ ($6'\text{-}0" \times 7'\text{-}0"$)   | $3.90\text{ m}^2$ ($42\text{ sq.ft}$)   | Black Galaxy granite L-counter ($600\text{ mm}$ depth, $850\text{ mm}$ FFL), breakfast counter bar, SS single bowl sink, 3-zone induction hob, overhead RCC lofts, exhaust fan ($300\text{ mm}$).                                                                                            |
| **Toilet**            | $1219.2 \times 1828.8\text{ mm}$ ($4'\text{-}0" \times 6'\text{-}0"$)   | $2.23\text{ m}^2$ ($24\text{ sq.ft}$)   | Dropped ceiling at $Z = 3048\text{ mm}$ for duct routing, Indian ceramic squatting pan with footrests, wall-mounted ceramic washbasin, chrome shower set, louvred ventilator window ($600 \times 600\text{ mm}$).                                                                            |

### 6.2 Bedroom North Door (D2) Integration in Existing Placeholder

The bedroom access door has been built directly inside the pre-existing architectural wall cutout in `Bedroom_Wall_North` ($Y \in [4572.0, 4673.5\text{ mm}]$):

- **Opening Geometry:** $X \in [3657.6, 4572.0\text{ mm}]$, $W = 914.4\text{ mm}$ ($3'\text{-}0"$), $H = 2133.6\text{ mm}$ ($7'\text{-}0"$), $Z \in [914.4, 3048.0\text{ mm}]$.
- **3D Components (`GF_Door_Bedroom_Group`):**
  - `Door_Bedroom_Frame`: Solid Burmese teakwood jambs and head ($60\text{ mm}$ profile, color `#5A3825`).
  - `Door_Bedroom_Leaf`: $38\text{ mm}$ teak flush panel swung open $20^\circ$ into the master bedroom.
  - `Door_Bedroom_Handle`: Polished SS 304 lever handle at $Z = 1864.4\text{ mm}$ ($+950\text{ mm}$ above finished plinth floor).
- **Structural Framing:** Directly below roof beam `RB2_Bedroom_Living` ($230 \times 350\text{ mm}$) and immediately adjacent to column `Col_Bed_West_Mid` (`Col_Notch` / C4).

```carousel
![3D View Bedroom Door D2](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\3d_bedroom_door_wall_view.png)
<!-- slide -->
![3D Model Axonometric Overview](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\3d_axonometric_model.png)
```

---
