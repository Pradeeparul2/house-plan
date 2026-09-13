## 18. Rooftop Staircase Headroom (Mumty) Structural Frame Integration

Following client observation of missing roof columns during skeletal frame inspection, the structural column and roof beam frame for the rooftop rain protection enclosure was fully modeled:

### 18.1 Structural Audit & Findings
* **Identified Gap:** The First Floor staircase columns terminated at the roof slab level ($Z = 7135.4\text{ mm}$). While the Mumty masonry walls, lintel bands, and concrete roof slab ($Z = 9460.4\text{ mm}$) existed in the architectural model, the **4 vertical RCC structural column extensions** and **4 monolithic roof tie beams** were previously omitted from the structural frame, causing the Mumty lintel ring to appear suspended in mid-air.
* **Structural Solution Added & Updated (8-Column Frame Alignment):**
  1. **Primary North Facade Structural Column Extensions ($300 \times 228.6\text{ mm}$ M25, $H = 2.325\text{ m}$, $Z = 7135.4 - 9460.4\text{ mm}$):**
     - `Mumty_Col_C7`: Continuous vertical extension of Column C7 (`FF_Col_N_Stair_C7`) at $X = 1564.5 - 1864.5\text{ mm}$, $Y = 0.0 - 228.6\text{ mm}$.
     - `Mumty_Col_C8`: Continuous vertical extension of Column C8 (`FF_Col_NW_Mumty_C8`) at $X = 4800.6 - 5100.6\text{ mm}$, $Y = 0.0 - 228.6\text{ mm}$.
  2. **Staircase Bay Trimmer Posts ($228.6 \times 228.6\text{ mm}$ / $9" \times 9"$, $H = 2.325\text{ m}$, $Z = 7135.4 - 9460.4\text{ mm}$):**
     - `Headroom_Col_NE`: Staircase east trimmer post at $X = 1714.5, Y = 0.0\text{ mm}$.
     - `Headroom_Col_NW`: Staircase west trimmer post at $X = 3695.7, Y = 0.0\text{ mm}$.
     - `Headroom_Col_SE`: Staircase south-east landing post at $X = 1714.5, Y = 1714.5\text{ mm}$.
     - `Headroom_Col_SW`: Staircase south-west landing post at $X = 3695.7, Y = 1714.5\text{ mm}$.
  3. **4 RCC Roof Beams ($D = 200\text{ mm}$, $Z = 9260.4 - 9460.4\text{ mm}$):**
     - `Headroom_RB_Front_North`, `Headroom_RB_Rear_South`, `Headroom_RB_East_Flank`, `Headroom_RB_West_Flank` framing beneath the $125\text{ mm}$ Mumty roof slab.
  4. **2x Overhead Water Tank (OHT) RCC Saddle Beams ($230 \times 230\text{ mm}$ M25 / Fe500D, $Z = 9260.4 - 9490.4\text{ mm}$):**
     - `OHT_Saddle_Beam_North`: Spans $X = 1564.5 - 5100.6\text{ mm}$ ($L = 3536.1\text{ mm}$) at $Y = 570.0\text{ mm}$.
     - `OHT_Saddle_Beam_South`: Spans $X = 1564.5 - 5100.6\text{ mm}$ ($L = 3536.1\text{ mm}$) at $Y = 1100.0\text{ mm}$.
     - Direct vertical load path: The $1.1\text{ tonne}$ loaded weight of the $1,000\text{ L}$ OHT is transmitted directly via axial compression through columns C7 and C8 down to the substructure foundation.

```carousel
![Complete 3D Structural Skeleton with 4 Rooftop Mumty Columns and Roof Beams](C:\Users\prade\OneDrive\Desktop\home plan\renders\structural_frame_pure_with_mumty.png)
<!-- slide -->
![Refactored Secondary Structural Elements & OHT Saddle Beams](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/renders/secondary_structural_refactored_iso.png)
```

---

