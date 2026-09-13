# 📋 Bar Bending Schedule (BBS) & Steel Procurement Ledger
## G+1 Residential RCC Framed Structure — 8-Column Optimized System

> **Source BIM Model:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Structural Optimization Reference:** [Section 75: 8-Column Optimization & Substructure Sync](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/docs/77_75_rcc_structural_optimization.md)  
> **Governing Standards:**  
> - **IS 2502:1963:** Code of Practice for Bending and Fixing of Bars for Concrete Reinforcement  
> - **IS 13920:2016:** Ductile Design and Detailing of Reinforced Concrete Structures Subjected to Seismic Forces  
> - **IS 456:2000:** Plain and Reinforced Concrete — Code of Practice (Fourth Revision)  
> - **SP 34 (S&T):1987:** Handbook on Concrete Reinforcement and Detailing  
> **Material Specifications:** Fe500D High-Yield Deformed Steel Rebar ($f_y = 500\text{ N/mm}^2$), M25 Concrete ($f_{ck} = 25\text{ N/mm}^2$)  
> **Commercial Stock Rebar:** $12.0\text{ m}$ standard commercial lengths with **$4.0\%$ site cutting wastage & rolling tolerance margin**  
> **Exported Machine-Readable Dataset:** [`docs/bbs_8_column_frame.csv`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/docs/bbs_8_column_frame.csv)  

---

## 1. Executive Structural Engineering Summary

The Bar Bending Schedule (BBS) detailed herein reflects the **as-modeled 8-column ($230 \times 300\text{ mm}$) monolithic RCC space frame** for the $16'\text{-}6" \times 25'\text{-}0"$ ($5.03 \times 7.62\text{ m}$) single-family residential building.

### 1.1 Structural Frame Parameters & Detailing Rules
1. **Clear Concrete Cover (IS 456 Cl. 26.4):**
   - **Isolated Footings:** $50\text{ mm}$ (aggressive subsoil moisture barrier)
   - **Columns & Pedestals:** $40\text{ mm}$ (confinement hoop protective envelope)
   - **Framing Beams (Plinth, Floor & Roof):** $25\text{ mm}$ (tensile crack & fire barrier)
2. **Bend Deductions (IS 2502 Table 2):**
   - $45^\circ$ Bend: $1d$
   - $90^\circ$ Standard Hook / Angle: $2d$
   - $135^\circ$ Seismic Hook: $3d$
3. **Seismic Confinement (IS 13920:2016 Cl. 7.4 & 8.2):**
   - Rectangular ties with **$135^\circ$ seismic hooks** having **$10d$ extension** ($10 \times 8 = 80\text{ mm}$).
   - Nodal confinement zone $L_o = \max(300\text{ mm}, 600\text{ mm}, H_{clr}/6) = 600\text{ mm}$ with stirrup pitch @ $100\text{ mm}$ c/c.
   - Column mid-height lap splice zones outside plastic hinge regions with staggered $L_d = 50\Phi$ ($800\text{ mm}$ for $\Phi16$, $600\text{ mm}$ for $\Phi12$).
4. **Primary Living Cross-Beam (`RB_LIVING_Primary`):**
   - Spanning $5029.2\text{ mm}$ clear across Columns C4 and C5 ($230 \times 350\text{ mm}$ M25).
   - Top: $3\#16\text{ mm}$ continuous; Bottom: $3\#16\text{ mm}$ continuous $+ 2\#12\text{ mm}$ curtailment in central $0.75L$ tension zone.
   - Includes **3 nos. $8\text{ mm}$ hanger stirrups @ $75\text{ mm}$ c/c** at the `RB2_Bedroom_Living` secondary beam intersection.
5. **Rooftop OHT Saddle Beams (`OHT_Saddle_Beam_North` & `South`):**
   - Spanning $3536.1\text{ mm}$ directly across rooftop Mumty columns C7 and C8 ($230 \times 230\text{ mm}$ M25).
   - Reinforced with $4\#16\text{ mm}$ ($2$ top, $2$ bottom) $+ 8\text{ mm}$ confinement links @ $100\text{ mm}$ c/c to transmit the $11.0\text{ kN}$ gravity tank load.

---

## 2. Dia-Wise Procurement Tonnage Ledger

> **Rebar Unit Weight Formula:** $W = \frac{D^2}{162.28}\text{ kg/m}$  
> - $\Phi 8\text{ mm}$: $0.395\text{ kg/m}$ | $\Phi 10\text{ mm}$: $0.617\text{ kg/m}$ | $\Phi 12\text{ mm}$: $0.888\text{ kg/m}$ | $\Phi 16\text{ mm}$: $1.578\text{ kg/m}$

| Bar Diameter ($\Phi$) | Unit Wt (kg/m) | Net Total Length (m) | Net Fabricated Wt (kg) | Procurement Length (+4%) (m) | Procurement Weight (kg) | Procurement Tonnage (MT) | Stock 12m Bars Req. | Commercial Packaging (Bars/Bundle) | Standard Commercial Bundles |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **8 mm** | `0.395` |  1650.08 m |   651.78 kg |  1716.08 m | **  677.85 kg** | ** 0.678 MT** | **144 pcs** | 10 pcs/bdl | **15 bundles** |
| **10 mm** | `0.617` |   166.14 m |   102.51 kg |   172.79 m | **  106.61 kg** | ** 0.107 MT** | **15 pcs** | 7 pcs/bdl | **3 bundles** |
| **12 mm** | `0.888` |   462.11 m |   410.36 kg |   480.60 m | **  426.77 kg** | ** 0.427 MT** | **41 pcs** | 5 pcs/bdl | **9 bundles** |
| **16 mm** | `1.578` |  1211.37 m |  1911.54 kg |  1259.82 m | ** 1988.00 kg** | ** 1.988 MT** | **105 pcs** | 3 pcs/bdl | **35 bundles** |
| **TOTALS** | — | ** 3489.71 m** | ** 3076.19 kg** | ** 3629.30 m** | ** 3199.24 kg** | ** 3.199 MT** | **305 pcs** | — | **62 bundles** |

---

## 3. Comprehensive Itemized Bar Bending Schedule (BBS)

| Member ID / Level | Bar Mark | Description & Engineering Role | Bending Shape & Code Geometry | Bar $\Phi$ (mm) | Bars Per Mem. | Total Bars | Cutting Length (m) | Total Length (m) | Unit Wt (kg/m) | Total Weight (kg) |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **SUBSTRUCTURE (Z = -1500 TO -1100 MM)** | | | | | | | | | | |
| `Footings (F1-F8, 8 Pads)` | **FTG-M12-01** | Bottom Mat Primary Main Bar | U-Shape Mat Bar (2x90° hooks) | **12** | 10 | **80** | 1.952 | 156.16 | 0.888 | **138.67** |
| `Footings (F1-F8, 8 Pads)` | **FTG-M10-02** | Bottom Mat Transverse Cross Bar | U-Shape Mat Bar (2x90° hooks) | **10** | 11 | **88** | 1.888 | 166.14 | 0.617 | **102.51** |
| **SUBSTRUCTURE PEDESTALS (Z = -1200 TO +614.4 MM)** | | | | | | | | | | |
| `Pedestals C1, C2, C6, C7` | **PED-V16-01** | Corner Starter Dowels (Footing Mat to GF Inflection) | L-Shape Dowel (300mm 90° Foot Bend) | **16** | 4 | **16** | 4.006 | 64.10 | 1.578 | **101.14** |
| `Pedestals C1, C2, C6, C7` | **PED-V12-02** | Flange/Web Starter Dowels (Footing Mat to GF Inflection) | L-Shape Dowel (300mm 90° Foot Bend) | **12** | 2 | **8** | 4.014 | 32.11 | 0.888 | **28.52** |
| `Pedestals C3, C4, C5, C8` | **PED-V16-03** | Longitudinal Starter Dowels (6#16mm per col) | L-Shape Dowel (300mm 90° Foot Bend) | **16** | 6 | **24** | 4.006 | 96.14 | 1.578 | **151.72** |
| `Pedestals C1 to C8 (8 Nos)` | **PED-T8-04** | Confinement Ties (100mm c/c Lo, 150mm mid) | Rectangular Tie + 135° Seismic Hooks (10d) | **8** | 17 | **136** | 0.804 | 109.34 | 0.395 | **43.19** |
| **GROUND FLOOR (Z = +614.4 TO +3962.4 MM)** | | | | | | | | | | |
| `GF Columns C1, C2, C6, C7` | **GFC-V16-01** | Corner Longitudinal Rebar (GF to FF Mid Splice) | Straight Splice Bar (incl. 50d lap) | **16** | 4 | **16** | 3.874 | 61.98 | 1.578 | **97.81** |
| `GF Columns C1, C2, C6, C7` | **GFC-V12-02** | Flange/Web Longitudinal Rebar (GF to FF Mid Splice) | Straight Splice Bar (incl. 50d lap) | **12** | 2 | **8** | 3.674 | 29.39 | 0.888 | **26.10** |
| `GF Columns C3, C4, C5, C8` | **GFC-V16-03** | Longitudinal Rebar (6#16mm, GF to FF Mid Splice) | Straight Splice Bar (incl. 50d lap) | **16** | 6 | **24** | 3.874 | 92.98 | 1.578 | **146.72** |
| `GF Columns C1 to C8 (8 Nos)` | **GFC-T8-04** | Confinement Ties (100mm c/c Lo & Joint, 150mm mid) | Rectangular Tie + 135° Seismic Hooks (10d) | **8** | 27 | **216** | 0.804 | 173.66 | 0.395 | **68.60** |
| **FIRST FLOOR (Z = +3962.4 TO +7135.4 MM)** | | | | | | | | | | |
| `FF Columns C1, C2, C6 (Terrace Term.)` | **FFC-V16-01** | Corner Rebar (FF Mid Splice to Terrace Roof Anchor) | L-Shape Bar (300mm 90° Roof Hook) | **16** | 4 | **12** | 2.841 | 34.09 | 1.578 | **53.80** |
| `FF Columns C1, C2, C6 (Terrace Term.)` | **FFC-V12-02** | Flange/Web Rebar (FF Mid Splice to Terrace Roof Anchor) | L-Shape Bar (300mm 90° Roof Hook) | **12** | 2 | **6** | 2.649 | 15.89 | 0.888 | **14.11** |
| `FF Columns C3, C4, C5 (Terrace Term.)` | **FFC-V16-03** | Longitudinal Rebar (6#16mm, Terrace Roof Anchor) | L-Shape Bar (300mm 90° Roof Hook) | **16** | 6 | **18** | 2.841 | 51.14 | 1.578 | **80.70** |
| `FF Columns C1 to C8 (8 Nos)` | **FFC-T8-04** | Confinement Ties (100mm c/c Lo & Joint, 150mm mid) | Rectangular Tie + 135° Seismic Hooks (10d) | **8** | 27 | **216** | 0.804 | 173.66 | 0.395 | **68.60** |
| **ROOFTOP MUMTY TOWER (Z = +7135.4 TO +9460.4 MM)** | | | | | | | | | | |
| `Mumty Column C7 (1 No)` | **MUM-V16-01** | Corner Rebar (Continuous from FF to Mumty Roof Hook) | L-Shape Bar (300mm 90° Mumty Roof Hook) | **16** | 4 | **4** | 5.166 | 20.66 | 1.578 | **32.61** |
| `Mumty Column C7 (1 No)` | **MUM-V12-02** | Flange/Web Rebar (Continuous from FF to Mumty Roof Hook) | L-Shape Bar (300mm 90° Mumty Roof Hook) | **12** | 2 | **2** | 4.974 | 9.95 | 0.888 | **8.83** |
| `Mumty Column C8 (1 No)` | **MUM-V16-03** | Longitudinal Rebar (6#16mm, Mumty Roof Hook) | L-Shape Bar (300mm 90° Mumty Roof Hook) | **16** | 6 | **6** | 5.166 | 31.00 | 1.578 | **48.91** |
| `Mumty Columns C7, C8 (2 Nos)` | **MUM-T8-04** | Confinement Ties (100mm c/c Lo, 150mm mid) | Rectangular Tie + 135° Seismic Hooks (10d) | **8** | 22 | **44** | 0.804 | 35.38 | 0.395 | **13.97** |
| **GF PLINTH LEVEL (Z = +614.4 MM)** | | | | | | | | | | |
| `PB_LIVING_Primary (230x300, L=5.03m)` | **PB-LIV-T16** | Top Continuous Rebar (3#16mm) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `PB_LIVING_Primary (230x300, L=5.03m)` | **PB-LIV-B16** | Bottom Continuous Rebar (3#16mm) | U-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `PB_LIVING_Primary (230x300, L=5.03m)` | **PB-LIV-C12** | Bottom Curtailment Rebar (2#12mm, Central 0.75L) | Straight Bar | **12** | 2 | **2** | 3.772 | 7.54 | 0.888 | **6.70** |
| `PB_LIVING_Primary (230x300, L=5.03m)` | **PB-LIV-S8** | 2-Legged Shear Stirrups (100mm c/c ends, 150mm mid) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 43 | **43** | 0.924 | 39.73 | 0.395 | **15.69** |
| `PB1_Rear_South (230x375, L=5.03m)` | **PB-RS-T16** | Top Continuous Perimeter Rebar (3#16mm) | C-Shape Beam Bar (2x90° End Anchorage 325mm) | **16** | 3 | **3** | 5.565 | 16.70 | 1.578 | **26.34** |
| `PB1_Rear_South (230x375, L=5.03m)` | **PB-RS-B16** | Bottom Continuous Perimeter Rebar (3#16mm) | U-Shape Beam Bar (2x90° End Anchorage 325mm) | **16** | 3 | **3** | 5.565 | 16.70 | 1.578 | **26.34** |
| `PB1_Rear_South (230x375, L=5.03m)` | **PB-RS-C12** | Bottom Curtailment Rebar (2#12mm, Central 0.75L) | Straight Bar | **12** | 2 | **2** | 3.772 | 7.54 | 0.888 | **6.70** |
| `PB1_Rear_South (230x375, L=5.03m)` | **PB-RS-S8** | 2-Legged Shear Stirrups (230x375mm, 100/150mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 43 | **43** | 1.074 | 46.18 | 0.395 | **18.24** |
| `PB1_Front_North (230x300, L=5.03m)` | **PB-FN-T16** | Top Continuous Perimeter Rebar (3#16mm) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `PB1_Front_North (230x300, L=5.03m)` | **PB-FN-B16** | Bottom Continuous Perimeter Rebar (3#16mm) | U-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `PB1_Front_North (230x300, L=5.03m)` | **PB-FN-C12** | Bottom Curtailment Rebar (2#12mm, Central 0.75L) | Straight Bar | **12** | 2 | **2** | 3.772 | 7.54 | 0.888 | **6.70** |
| `PB1_Front_North (230x300, L=5.03m)` | **PB-FN-S8** | 2-Legged Shear Stirrups (230x300mm, 100/150mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 43 | **43** | 0.924 | 39.73 | 0.395 | **15.69** |
| `PB1_East & West Flanks (230x300, L=7.62m, 2 Nos)` | **PB-FL-T16** | Top Continuous Boundary Rebar (3#16mm, C1-C4-C6 / C3-C5-C8) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **6** | 8.006 | 48.04 | 1.578 | **75.80** |
| `PB1_East & West Flanks (230x300, L=7.62m, 2 Nos)` | **PB-FL-B16** | Bottom Continuous Boundary Rebar (3#16mm, C1-C4-C6 / C3-C5-C8) | U-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **6** | 8.006 | 48.04 | 1.578 | **75.80** |
| `PB1_East & West Flanks (230x300, L=7.62m, 2 Nos)` | **PB-FL-C12** | Bottom Curtailment Rebar (4#12mm, 2 per span) | Straight Bar | **12** | 4 | **8** | 2.800 | 22.40 | 0.888 | **19.89** |
| `PB1_East & West Flanks (230x300, L=7.62m, 2 Nos)` | **PB-FL-S8** | 2-Legged Shear Stirrups (230x300mm across 2 spans) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 78 | **156** | 0.924 | 144.14 | 0.395 | **56.94** |
| `PB2_Core_GridB (230x300, L=5.03m)` | **PB-GB-T16** | Top Continuous Transverse Header Rebar (3#16mm) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `PB2_Core_GridB (230x300, L=5.03m)` | **PB-GB-B16** | Bottom Continuous Transverse Header Rebar (3#16mm) | U-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `PB2_Core_GridB (230x300, L=5.03m)` | **PB-GB-C12** | Bottom Curtailment Rebar (2#12mm, Central 0.75L) | Straight Bar | **12** | 2 | **2** | 3.772 | 7.54 | 0.888 | **6.70** |
| `PB2_Core_GridB (230x300, L=5.03m)` | **PB-GB-S8** | 2-Legged Shear Stirrups (230x300mm, 100/150mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 43 | **43** | 0.924 | 39.73 | 0.395 | **15.69** |
| `PB2_Bedroom_Living (230x300, L=2.82m)` | **PB-BL-T16** | Top Partition Divider Rebar (2#16mm) anchored into C5 | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 2 | **2** | 3.205 | 6.41 | 1.578 | **10.11** |
| `PB2_Bedroom_Living (230x300, L=2.82m)` | **PB-BL-B16** | Bottom Partition Divider Rebar (2#16mm) anchored into C5 | U-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 2 | **2** | 3.205 | 6.41 | 1.578 | **10.11** |
| `PB2_Bedroom_Living (230x300, L=2.82m)` | **PB-BL-C12** | Bottom Curtailment Rebar (1#12mm, Central 0.75L) | Straight Bar | **12** | 1 | **1** | 2.115 | 2.12 | 0.888 | **1.88** |
| `PB2_Bedroom_Living (230x300, L=2.82m)` | **PB-BL-S8** | 2-Legged Shear Stirrups (230x300mm, 100/150mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 23 | **23** | 0.924 | 21.25 | 0.395 | **8.39** |
| `PB2_Stair_East (300x300, L=1.71m)` | **PB-SE-V12** | Main Longitudinal Rebar (4#12mm: 2 top, 2 bot) into C7 | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **12** | 4 | **4** | 2.100 | 8.40 | 0.888 | **7.46** |
| `PB2_Stair_East (300x300, L=1.71m)` | **PB-SE-S8** | 2-Legged Shear Stirrups (300x300mm square tie @ 125mm c/c) | Square Stirrup + 135° Hooks (10d) | **8** | 14 | **14** | 1.064 | 14.90 | 0.395 | **5.88** |
| `PB2_Stair_West (230x300, L=1.71m)` | **PB-SW-V12** | Main Longitudinal Rebar (4#12mm: 2 top, 2 bot) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **12** | 4 | **4** | 2.100 | 8.40 | 0.888 | **7.46** |
| `PB2_Stair_West (230x300, L=1.71m)` | **PB-SW-S8** | 2-Legged Shear Stirrups (230x300mm tie @ 125mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 14 | **14** | 0.924 | 12.94 | 0.395 | **5.11** |
| **GF ROOF BEAM (Z = +3662.4 MM)** | | | | | | | | | | |
| `RB_LIVING_Primary (230x350, L=5.03m)` | **RB-LIV-T16** | Top Continuous Primary Cross-Beam Rebar (3#16mm) | C-Shape Beam Bar (2x90° End Anchorage 300mm) | **16** | 3 | **3** | 5.515 | 16.54 | 1.578 | **26.11** |
| `RB_LIVING_Primary (230x350, L=5.03m)` | **RB-LIV-B16** | Bottom Continuous Primary Cross-Beam Rebar (3#16mm) | U-Shape Beam Bar (2x90° End Anchorage 300mm) | **16** | 3 | **3** | 5.515 | 16.54 | 1.578 | **26.11** |
| `RB_LIVING_Primary (230x350, L=5.03m)` | **RB-LIV-C12** | Bottom Curtailment Rebar (2#12mm, Central 0.75L) | Straight Bar | **12** | 2 | **2** | 3.772 | 7.54 | 0.888 | **6.70** |
| `RB_LIVING_Primary (230x350, L=5.03m)` | **RB-LIV-S8** | 2-Legged Shear Stirrups (230x350mm, 100/150mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 43 | **43** | 1.024 | 44.03 | 0.395 | **17.39** |
| `RB_LIVING_Primary (230x350, L=5.03m)` | **RB-LIV-HG8** | Hanger Stirrups (8mm @ 75mm c/c at RB2 Secondary Junction) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 3 | **3** | 1.024 | 3.07 | 0.395 | **1.21** |
| `RB1_Rear_South (230x375, L=5.03m)` | **RB-RS-T16** | Top Continuous Perimeter Rebar (3#16mm) | C-Shape Beam Bar (2x90° End Anchorage 325mm) | **16** | 3 | **3** | 5.565 | 16.70 | 1.578 | **26.34** |
| `RB1_Rear_South (230x375, L=5.03m)` | **RB-RS-B16** | Bottom Continuous Perimeter Rebar (3#16mm) | U-Shape Beam Bar (2x90° End Anchorage 325mm) | **16** | 3 | **3** | 5.565 | 16.70 | 1.578 | **26.34** |
| `RB1_Rear_South (230x375, L=5.03m)` | **RB-RS-C12** | Bottom Curtailment Rebar (2#12mm, Central 0.75L) | Straight Bar | **12** | 2 | **2** | 3.772 | 7.54 | 0.888 | **6.70** |
| `RB1_Rear_South (230x375, L=5.03m)` | **RB-RS-S8** | 2-Legged Shear Stirrups (230x375mm, 100/150mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 43 | **43** | 1.074 | 46.18 | 0.395 | **18.24** |
| `RB1_Front_North (230x300, L=5.03m)` | **RB-FN-T16** | Top Continuous Perimeter Rebar (3#16mm) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `RB1_Front_North (230x300, L=5.03m)` | **RB-FN-B16** | Bottom Continuous Perimeter Rebar (3#16mm) | U-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `RB1_Front_North (230x300, L=5.03m)` | **RB-FN-C12** | Bottom Curtailment Rebar (2#12mm, Central 0.75L) | Straight Bar | **12** | 2 | **2** | 3.772 | 7.54 | 0.888 | **6.70** |
| `RB1_Front_North (230x300, L=5.03m)` | **RB-FN-S8** | 2-Legged Shear Stirrups (230x300mm, 100/150mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 43 | **43** | 0.924 | 39.73 | 0.395 | **15.69** |
| `RB1_East & West Flanks (230x300, L=7.62m, 2 Nos)` | **RB-FL-T16** | Top Continuous Boundary Rebar (3#16mm, C1-C4-C6 / C3-C5-C8) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **6** | 8.006 | 48.04 | 1.578 | **75.80** |
| `RB1_East & West Flanks (230x300, L=7.62m, 2 Nos)` | **RB-FL-B16** | Bottom Continuous Boundary Rebar (3#16mm, C1-C4-C6 / C3-C5-C8) | U-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **6** | 8.006 | 48.04 | 1.578 | **75.80** |
| `RB1_East & West Flanks (230x300, L=7.62m, 2 Nos)` | **RB-FL-C12** | Bottom Curtailment Rebar (4#12mm, 2 per span) | Straight Bar | **12** | 4 | **8** | 2.800 | 22.40 | 0.888 | **19.89** |
| `RB1_East & West Flanks (230x300, L=7.62m, 2 Nos)` | **RB-FL-S8** | 2-Legged Shear Stirrups (230x300mm across 2 spans) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 78 | **156** | 0.924 | 144.14 | 0.395 | **56.94** |
| `RB2_Core_GridB (230x300, L=5.03m)` | **RB-GB-T16** | Top Continuous Transverse Header Rebar (3#16mm) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `RB2_Core_GridB (230x300, L=5.03m)` | **RB-GB-B16** | Bottom Continuous Transverse Header Rebar (3#16mm) | U-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `RB2_Core_GridB (230x300, L=5.03m)` | **RB-GB-C12** | Bottom Curtailment Rebar (2#12mm, Central 0.75L) | Straight Bar | **12** | 2 | **2** | 3.772 | 7.54 | 0.888 | **6.70** |
| `RB2_Core_GridB (230x300, L=5.03m)` | **RB-GB-S8** | 2-Legged Shear Stirrups (230x300mm, 100/150mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 43 | **43** | 0.924 | 39.73 | 0.395 | **15.69** |
| `RB2_Bedroom_Living (230x300, L=2.82m)` | **RB-BL-T16** | Top Partition Divider Rebar (2#16mm) anchored into C5 | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 2 | **2** | 3.205 | 6.41 | 1.578 | **10.11** |
| `RB2_Bedroom_Living (230x300, L=2.82m)` | **RB-BL-B16** | Bottom Partition Divider Rebar (2#16mm) anchored into C5 | U-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 2 | **2** | 3.205 | 6.41 | 1.578 | **10.11** |
| `RB2_Bedroom_Living (230x300, L=2.82m)` | **RB-BL-C12** | Bottom Curtailment Rebar (1#12mm, Central 0.75L) | Straight Bar | **12** | 1 | **1** | 2.115 | 2.12 | 0.888 | **1.88** |
| `RB2_Bedroom_Living (230x300, L=2.82m)` | **RB-BL-S8** | 2-Legged Shear Stirrups (230x300mm, 100/150mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 23 | **23** | 0.924 | 21.25 | 0.395 | **8.39** |
| `RB2_Stair_East_Trimmer (300x300, L=0.99m)` | **RB-SET-V12** | Trimmer Longitudinal Rebar (4#12mm: 2 top, 2 bot) into C7 | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **12** | 4 | **4** | 1.376 | 5.50 | 0.888 | **4.89** |
| `RB2_Stair_East_Trimmer (300x300, L=0.99m)` | **RB-SET-S8** | 2-Legged Shear Stirrups (300x300mm tie @ 100mm c/c) | Square Stirrup + 135° Hooks (10d) | **8** | 9 | **9** | 1.064 | 9.58 | 0.395 | **3.78** |
| `RB2_Stair_West_Trimmer (230x300, L=1.71m)` | **RB-SWT-V12** | Trimmer Longitudinal Rebar (4#12mm: 2 top, 2 bot) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **12** | 4 | **4** | 2.100 | 8.40 | 0.888 | **7.46** |
| `RB2_Stair_West_Trimmer (230x300, L=1.71m)` | **RB-SWT-S8** | 2-Legged Shear Stirrups (230x300mm tie @ 125mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 14 | **14** | 0.924 | 12.94 | 0.395 | **5.11** |
| **GF ROOF BEAM (Z = +3048.0 MM)** | | | | | | | | | | |
| `Kitchen_Beam_North (230x228.6, L=2.10m)` | **KB-N-V12** | Monolithic Counter Beam Rebar (4#12mm: 2 top, 2 bot) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **12** | 4 | **4** | 2.482 | 9.93 | 0.888 | **8.82** |
| `Kitchen_Beam_North (230x228.6, L=2.10m)` | **KB-N-S8** | 2-Legged Shear Stirrups (230x230mm tie @ 125mm c/c) | Square Stirrup + 135° Hooks (10d) | **8** | 17 | **17** | 0.784 | 13.33 | 0.395 | **5.26** |
| **STAIRCASE MID-LANDING (Z = +2138.4 MM)** | | | | | | | | | | |
| `MLB_Staircase_Mid_Landing (230x300, L=1.98m)` | **MLB-ST-V16** | Waist Turnaround Support Rebar (4#16mm: 2 top, 2 bot) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 4 | **4** | 2.367 | 9.47 | 1.578 | **14.94** |
| `MLB_Staircase_Mid_Landing (230x300, L=1.98m)` | **MLB-ST-S8** | 2-Legged Shear Stirrups (230x300mm tie @ 125mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 16 | **16** | 0.924 | 14.78 | 0.395 | **5.84** |
| **FF ROOF BEAM (Z = +6835.4 MM)** | | | | | | | | | | |
| `FF_RB_LIVING_Primary (230x350, L=5.03m)` | **FF-LIV-T16** | Top Continuous Primary Cross-Beam Rebar (3#16mm) | C-Shape Beam Bar (2x90° End Anchorage 300mm) | **16** | 3 | **3** | 5.515 | 16.54 | 1.578 | **26.11** |
| `FF_RB_LIVING_Primary (230x350, L=5.03m)` | **FF-LIV-B16** | Bottom Continuous Primary Cross-Beam Rebar (3#16mm) | U-Shape Beam Bar (2x90° End Anchorage 300mm) | **16** | 3 | **3** | 5.515 | 16.54 | 1.578 | **26.11** |
| `FF_RB_LIVING_Primary (230x350, L=5.03m)` | **FF-LIV-C12** | Bottom Curtailment Rebar (2#12mm, Central 0.75L) | Straight Bar | **12** | 2 | **2** | 3.772 | 7.54 | 0.888 | **6.70** |
| `FF_RB_LIVING_Primary (230x350, L=5.03m)` | **FF-LIV-S8** | 2-Legged Shear Stirrups (230x350mm, 100/150mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 43 | **43** | 1.024 | 44.03 | 0.395 | **17.39** |
| `FF_RB_LIVING_Primary (230x350, L=5.03m)` | **FF-LIV-HG8** | Hanger Stirrups (8mm @ 75mm c/c at FF Secondary Junction) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 3 | **3** | 1.024 | 3.07 | 0.395 | **1.21** |
| `FF_RB1_Rear_South (230x300, L=5.03m)` | **FF-RS-T16** | Top Continuous Perimeter Rebar (3#16mm) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `FF_RB1_Rear_South (230x300, L=5.03m)` | **FF-RS-B16** | Bottom Continuous Perimeter Rebar (3#16mm) | U-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `FF_RB1_Rear_South (230x300, L=5.03m)` | **FF-RS-C12** | Bottom Curtailment Rebar (2#12mm, Central 0.75L) | Straight Bar | **12** | 2 | **2** | 3.772 | 7.54 | 0.888 | **6.70** |
| `FF_RB1_Rear_South (230x300, L=5.03m)` | **FF-RS-S8** | 2-Legged Shear Stirrups (230x300mm, 100/150mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 43 | **43** | 0.924 | 39.73 | 0.395 | **15.69** |
| `FF_RB1_Front_North (230x300, L=5.03m)` | **FF-FN-T16** | Top Continuous Perimeter Rebar (3#16mm) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `FF_RB1_Front_North (230x300, L=5.03m)` | **FF-FN-B16** | Bottom Continuous Perimeter Rebar (3#16mm) | U-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `FF_RB1_Front_North (230x300, L=5.03m)` | **FF-FN-C12** | Bottom Curtailment Rebar (2#12mm, Central 0.75L) | Straight Bar | **12** | 2 | **2** | 3.772 | 7.54 | 0.888 | **6.70** |
| `FF_RB1_Front_North (230x300, L=5.03m)` | **FF-FN-S8** | 2-Legged Shear Stirrups (230x300mm, 100/150mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 43 | **43** | 0.924 | 39.73 | 0.395 | **15.69** |
| `FF_RB1_East & West Flanks (230x300, L=7.62m, 2 Nos)` | **FF-FL-T16** | Top Continuous Boundary Rebar (3#16mm, C1-C4-C6 / C3-C5-C8) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **6** | 8.006 | 48.04 | 1.578 | **75.80** |
| `FF_RB1_East & West Flanks (230x300, L=7.62m, 2 Nos)` | **FF-FL-B16** | Bottom Continuous Boundary Rebar (3#16mm, C1-C4-C6 / C3-C5-C8) | U-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **6** | 8.006 | 48.04 | 1.578 | **75.80** |
| `FF_RB1_East & West Flanks (230x300, L=7.62m, 2 Nos)` | **FF-FL-C12** | Bottom Curtailment Rebar (4#12mm, 2 per span) | Straight Bar | **12** | 4 | **8** | 2.800 | 22.40 | 0.888 | **19.89** |
| `FF_RB1_East & West Flanks (230x300, L=7.62m, 2 Nos)` | **FF-FL-S8** | 2-Legged Shear Stirrups (230x300mm across 2 spans) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 78 | **156** | 0.924 | 144.14 | 0.395 | **56.94** |
| `FF_RB2_Core_GridB (230x300, L=5.03m)` | **FF-GB-T16** | Top Continuous Transverse Header Rebar (3#16mm) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `FF_RB2_Core_GridB (230x300, L=5.03m)` | **FF-GB-B16** | Bottom Continuous Transverse Header Rebar (3#16mm) | U-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 3 | **3** | 5.415 | 16.25 | 1.578 | **25.63** |
| `FF_RB2_Core_GridB (230x300, L=5.03m)` | **FF-GB-C12** | Bottom Curtailment Rebar (2#12mm, Central 0.75L) | Straight Bar | **12** | 2 | **2** | 3.772 | 7.54 | 0.888 | **6.70** |
| `FF_RB2_Core_GridB (230x300, L=5.03m)` | **FF-GB-S8** | 2-Legged Shear Stirrups (230x300mm, 100/150mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 43 | **43** | 0.924 | 39.73 | 0.395 | **15.69** |
| `FF_RB2_Bedroom_Living (230x300, L=2.82m)` | **FF-BL-T16** | Top Partition Divider Rebar (2#16mm) anchored into C5 | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 2 | **2** | 3.205 | 6.41 | 1.578 | **10.11** |
| `FF_RB2_Bedroom_Living (230x300, L=2.82m)` | **FF-BL-B16** | Bottom Partition Divider Rebar (2#16mm) anchored into C5 | U-Shape Beam Bar (2x90° End Anchorage 250mm) | **16** | 2 | **2** | 3.205 | 6.41 | 1.578 | **10.11** |
| `FF_RB2_Bedroom_Living (230x300, L=2.82m)` | **FF-BL-C12** | Bottom Curtailment Rebar (1#12mm, Central 0.75L) | Straight Bar | **12** | 1 | **1** | 2.115 | 2.12 | 0.888 | **1.88** |
| `FF_RB2_Bedroom_Living (230x300, L=2.82m)` | **FF-BL-S8** | 2-Legged Shear Stirrups (230x300mm, 100/150mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 23 | **23** | 0.924 | 21.25 | 0.395 | **8.39** |
| `FF_RB2_Stair_East_Trimmer (300x300, L=0.99m)` | **FF-SET-V12** | Trimmer Longitudinal Rebar (4#12mm: 2 top, 2 bot) into C7 | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **12** | 4 | **4** | 1.376 | 5.50 | 0.888 | **4.89** |
| `FF_RB2_Stair_East_Trimmer (300x300, L=0.99m)` | **FF-SET-S8** | 2-Legged Shear Stirrups (300x300mm tie @ 100mm c/c) | Square Stirrup + 135° Hooks (10d) | **8** | 9 | **9** | 1.064 | 9.58 | 0.395 | **3.78** |
| `FF_RB2_Stair_West_Trimmer (230x300, L=1.71m)` | **FF-SWT-V12** | Trimmer Longitudinal Rebar (4#12mm: 2 top, 2 bot) | C-Shape Beam Bar (2x90° End Anchorage 250mm) | **12** | 4 | **4** | 2.100 | 8.40 | 0.888 | **7.46** |
| `FF_RB2_Stair_West_Trimmer (230x300, L=1.71m)` | **FF-SWT-S8** | 2-Legged Shear Stirrups (230x300mm tie @ 125mm c/c) | Rectangular Stirrup + 135° Hooks (10d) | **8** | 14 | **14** | 0.924 | 12.94 | 0.395 | **5.11** |
| **TERRACE TANK SADDLE (Z = +9260.4 MM)** | | | | | | | | | | |
| `OHT_Saddle_Beams North & South (2 Nos)` | **OHT-SAD-T16** | Top Load Transfer Rebar (2#16mm) across C7-C8 | C-Shape Beam Bar (2x90° End Anchorage 180mm) | **16** | 2 | **4** | 3.782 | 15.13 | 1.578 | **23.87** |
| `OHT_Saddle_Beams North & South (2 Nos)` | **OHT-SAD-B16** | Bottom Load Transfer Rebar (2#16mm) across C7-C8 | U-Shape Beam Bar (2x90° End Anchorage 180mm) | **16** | 2 | **4** | 3.782 | 15.13 | 1.578 | **23.87** |
| `OHT_Saddle_Beams North & South (2 Nos)` | **OHT-SAD-S8** | 2-Legged Heavy Shear Stirrups (@ 100mm c/c continuous) | Square Stirrup + 135° Hooks (10d) | **8** | 36 | **72** | 0.784 | 56.45 | 0.395 | **22.30** |
| **TOTAL FRAME FABRICATED NET WEIGHT** | | | | | | | | | | **3076.19 kg** |

---

## 4. Rebar Bending Shape Diagrams & Standard Detailing

### 4.1 Footing Bi-Directional Mat Bars (`FTG-M12-01` & `FTG-M10-02`)
```
     300 mm (Leg)                     300 mm (Leg)
       |                                |
       |                                |
       +--------------------------------+
             1400 mm / 1328 mm
  IS 2502 Form: 2 x 90° bends. Bend deduction = 2 x 2d = 4d.
  FTG-M12-01: Lc = 1400 + 2*(300) - 4*(12) = 1952 mm = 1.952 m
  FTG-M10-02: Lc = 1328 + 2*(300) - 4*(10) = 1888 mm = 1.888 m
```

### 4.2 Column Starter Dowels (`PED-V16-01`, `PED-V12-02`, `PED-V16-03`)
```
  3738.4 mm (Vertical rise to GF Inflection Zone)
  |
  |
  |
  +-------- 300 mm (Foot anchor resting on bottom mat)
  Bend deduction: 1 x 90° bend = 2d.
  PED-V16: Lc = 3738.4 + 300 - 32 = 4006.4 mm ≈ 4.006 m (Optimized 12m stock cut = 4.000 m)
  PED-V12: Lc = 3738.4 + 300 - 24 = 4014.4 mm ≈ 4.014 m (Optimized 12m stock cut = 4.000 m)
```

### 4.3 Column Confinement Ties (`PED-T8-04`, `GFC-T8-04`, `FFC-T8-04`, `MUM-T8-04`)
```
        220 mm (Core)
     +---------------+
     |               | 150 mm (Core)
     |               |
     +-------\ /-----+
            / X \
       80 mm / \ 80 mm (10d 135° Seismic Hooks)
  IS 13920 & IS 2502 Form: 3 x 90° bends (6d) + 2 x 135° bends (6d) = 12d = 96 mm deduction.
  Lc = 2*(150 + 220) + 2*(80) - 96 = 740 + 160 - 96 = 804 mm = 0.804 m.
```

### 4.4 Continuous Beam Longitudinal Rebar with End Anchorages
```
  Top Rebar:
  250/300 mm
       |
       +---------------------------------------------+
                     4979.2 mm (Span)                | 250/300 mm
  Bottom Rebar:
  250/300 mm                                         250/300 mm
       |                                             |
       +---------------------------------------------+
  Curtailment (Tension Zone):
       +=============================================+
                     3772 mm (0.75 L)
```

---

## 5. Commercial Stock Optimization & Waste Mitigation Protocol

1. **Exact 12.0 m Stock Division:**
   - Column dowels ($4.00\text{ m}$): Yields **exactly 3 bars per $12\text{ m}$ stock rod with $0.0\%$ cutting loss**.
   - Plinth / Roof Beams ($8.006\text{ m}$ flank beam $+ 3.772\text{ m}$ curtailment bar $= 11.78\text{ m}$): Yields **$98.2\%$ utilization with $< 0.22\text{ m}$ scrap offcut**, which is reused for beam stirrup spacers and chair supports.
   - Column ties ($0.804\text{ m}$): Yields **14 complete ties per $12\text{ m}$ rod** ($14 \times 0.804 = 11.256\text{ m}$) with scrap offcuts utilized as cover block binding pins.
2. **Quality Assurance & Verification:**
   - Fe500D TMT bars must comply with IS 1786:2008 with minimum elongation $\ge 16.0\%$ and tensile/yield ratio $\ge 1.10$ for high seismic ductility.
   - Cold bending must use mandated mandrel diameters ($4d$ for $\Phi \le 16\text{ mm}$) to avoid microscopic micro-cracking at bend points.
