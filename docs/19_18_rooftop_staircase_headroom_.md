## 18. Rooftop Staircase Headroom (Mumty) Structural Frame Integration

Following client observation of missing roof columns during skeletal frame inspection, the structural column and roof beam frame for the rooftop rain protection enclosure was fully modeled:

### 18.1 Structural Audit & Findings
* **Identified Gap:** The First Floor staircase columns terminated at the roof slab level ($Z = 7135.4\text{ mm}$). While the Mumty masonry walls, lintel bands, and concrete roof slab ($Z = 9460.4\text{ mm}$) existed in the architectural model, the **4 vertical RCC structural column extensions** and **4 monolithic roof tie beams** were previously omitted from the structural frame, causing the Mumty lintel ring to appear suspended in mid-air.
* **Structural Solution Added & Updated (8-Column Frame Alignment & Cantilever Rectification):**
  1. **Primary Structural Column Termination Datum & Extension:**
     - `Mumty_Col_C7`: Continuous vertical extension of Column C7 (`FF_Col_N_Stair_C7`, $230 \times 230\text{ mm}$ M25, $H = 2.325\text{ m}$, $Z = 7135.4 - 9460.4\text{ mm}$) aligned flush with the Mumty East frame post at $X = 1714.5\text{ mm}, Y = 0.0\text{ mm}$.
     - `FF_Col_NW_Mumty_C8`: Column C8 terminates flush at the terrace slab soffit ($Z = +7135.4\text{ mm}$), identical to columns C1–C6. The unbraced freestanding extension above the parapet was eliminated per IS 456 / IS 13920.
  2. **Staircase Bay Trimmer Posts ($228.6 \times 228.6\text{ mm}$ / $9" \times 9"$, $H = 2.325\text{ m}$, $Z = 7135.4 - 9460.4\text{ mm}$):**
     - `Headroom_Col_NE`: Staircase east trimmer post at $X = 1714.5, Y = 0.0\text{ mm}$.
     - `Headroom_Col_NW`: Staircase west trimmer post at $X = 3695.7, Y = 0.0\text{ mm}$.
     - `Headroom_Col_SE`: Staircase south-east landing post at $X = 1714.5, Y = 1714.5\text{ mm}$.
     - `Headroom_Col_SW`: Staircase south-west landing post at $X = 3695.7, Y = 1714.5\text{ mm}$.
  3. **4 RCC Roof Beams ($D = 200\text{ mm}$, $Z = 9260.4 - 9460.4\text{ mm}$):**
     - `Headroom_RB_Front_North`, `Headroom_RB_Rear_South`, `Headroom_RB_East_Flank`, `Headroom_RB_West_Flank` framing beneath the $125\text{ mm}$ Mumty roof slab ($X \in [1714.5, 3924.3\text{ mm}]$).
  4. **2x Overhead Water Tank (OHT) RCC Saddle Beams ($230 \times 230\text{ mm}$ M25 / Fe500D, $Z = 9260.4 - 9490.4\text{ mm}$):**
     - `OHT_Saddle_Beam_North`: Spans $X = 1714.5 - 3924.3\text{ mm}$ ($L = 2209.8\text{ mm}$) at $Y = 570.0\text{ mm}$.
     - `OHT_Saddle_Beam_South`: Spans $X = 1714.5 - 3924.3\text{ mm}$ ($L = 2209.8\text{ mm}$) at $Y = 1100.0\text{ mm}$.
     - Direct vertical load path: The $1.1\text{ tonne}$ loaded weight of the $1,000\text{ L}$ OHT is transmitted directly via the Mumty corner posts `Headroom_Col_NE` and `Headroom_Col_NW` to the main foundation, completely eliminating cantilever overhang past the Mumty west wall.

```carousel
![Complete 3D Structural Skeleton with 4 Rooftop Mumty Columns and Roof Beams](C:\Users\prade\OneDrive\Desktop\home plan\renders\structural_frame_pure_with_mumty.png)
<!-- slide -->
![Refactored Secondary Structural Elements & OHT Saddle Beams](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/renders/secondary_structural_refactored_iso.png)
```

---

