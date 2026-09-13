# 📋 Bill of Quantities (BOQ)
## Residential Home Construction — Ground Floor + G+1 Expansion Ready

> **Project:** Modern Residential Single-Family Home — South Indian Urban Design  
> **Site Footprint:** $5.03\text{ m} \times 7.62\text{ m}$ ($16'\text{-}6'' \times 25'\text{-}0''$)  
> **Total Built-Up Area:** $\approx 850\text{ sq.ft}$ (GF: $412.5\text{ sq.ft}$ + FF: $412.5\text{ sq.ft}$ + Staircase Mumty Tower)  
> **Source BIM Model:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd) — 612 Parametric Solid Objects, 0 Errors  
> **Technical Reference:** [`walkthrough.md`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/walkthrough.md) — 72 Chapters  
> **Standards Applied:** IS 456:2000, IS 1742, IS 4326, NBC 2016, IS 732, IS 2065  
> **Prepared Date:** September 2026  
> **Cost Benchmark:** South Indian Urban Rates 2025–2026

> [!NOTE]
> **Revision 2 — Structural Frame Optimization & Substructure Sync (Sep 2026):**
> - Structural frame optimized from legacy 14 columns (9″ × 9″) to **8 columns (C1–C8, 9″ × 12″ / 230 × 300 mm)** in M25 concrete with Fe500D rebar
> - Substructure standardized to **8 isolated RCC footings** (Footing_N8_C1 to C12: ~1500 × 1428 × 400 mm) on 100 mm M7.5 PCC blinding beds
> - Retained **8 pedestals** (230 × 300 mm, Z = -1200 to +614.4 mm, H = 1814.4 mm); 6 obsolete pedestals and pads excised
> - Primary Living Hall Cross-Beam added: **`RB_LIVING_Primary` & `PB_LIVING_Primary`** (230 × 350 mm / 230 × 300 mm, span 5029.2 mm) carrying upper partition loads across open living hall
> - Rear perimeter beams upsized to 375 mm depth (**`RB1_Rear_South`**, **`PB1_Rear_South`**)
> - Rooftop Mumty: Vertical extensions for C7 and C8 (**`Mumty_Col_C7`**, **`Mumty_Col_C8`**) and dual 230 × 230 mm RCC saddle beams (**`OHT_Saddle_Beam_North`/`South`**, span 3536.1 mm) supporting 1,000 L OHT
> - Masonry: Lightweight AAC blocks (200 mm exterior, 100 mm interior partitions); adjusted for 230 × 300 mm column embedment
> - Rebar procurement synchronized with comprehensive Bar Bending Schedule (BBS) and IS 13920:2016 ductile seismic detailing

---

## Section 1 — Substructure & Earthwork

### 1.1 Site Preparation & Excavation

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 1.1.1 | Site clearing and demarcation of $5.03 \times 7.62\text{ m}$ footprint | LS | 1 | 8,000 | 8,000 |
| 1.1.2 | Excavation for 8 isolated column footing pits (depth 1.6 m, pit size $\approx 1.8 \times 1.7\text{ m}$) | m³ | 38.10 | 400 | 15,240 |
| 1.1.3 | Excavation for Underground Sump pit — $1.8 \times 1.2 \times 2.1\text{ m}$ (incl. working space) | m³ | 9.07 | 400 | 3,628 |
| 1.1.4 | Excavation for Septic Tank pit — $1.2 \times 1.2 \times 2.1\text{ m}$ (incl. working space) | m³ | 4.54 | 400 | 1,816 |
| 1.1.5 | Excavation for subgrade municipal pipe trench — $\approx 8\text{ m}$ long, $0.6\text{ m}$ wide, $0.8\text{ m}$ deep | m³ | 3.84 | 400 | 1,536 |
| 1.1.6 | Earth filling and compaction in plinth area (M-sand + gravel 200 mm layers) | m³ | 24.5 | 350 | 8,575 |
| 1.1.7 | Anti-termite chemical treatment to soil (pre-construction, IS 6313 Part 2) | m² | 38.3 | 120 | 4,596 |
| 1.1.8 | Disposal of surplus excavated earth (lorry hire, 5 trips) | LS | 5 | 1,800 | 9,000 |
| | | | | **Sub-Total 1.1** | **₹52,391** |

### 1.2 Plain Cement Concrete (PCC) Bed — M7.5 / M10 Grade

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 1.2.1 | PCC M7.5 blinding bed (100 mm thick) under 8 column footings ($1.60 \times 1.528\text{ m}$ each) | m³ | 1.96 | 5,500 | 10,780 |
| 1.2.2 | PCC M10 bed (100 mm thick) under Underground Sump ($1.8 \times 1.2\text{ m}$) | m³ | 0.22 | 5,500 | 1,210 |
| 1.2.3 | PCC M10 bed (100 mm thick) under Septic Tank ($1.2 \times 1.2\text{ m}$) | m³ | 0.14 | 5,500 | 770 |
| | | | | **Sub-Total 1.2** | **₹12,760** |

### 1.3 Isolated Column Footings & Pedestals — M25 RCC (8 Nos.)

> **8 Standardized Footings:** $1500 \times 1428\text{ mm}$ plan, $400\text{ mm}$ deep pad (`Footing_N8_C1` to `Footing_N8_C12`).  
> **8 Column Pedestals:** $230 \times 300\text{ mm}$ stub from footing top ($Z = -1200\text{ mm}$) to plinth level ($Z = +614.4\text{ mm}$, $H = 1814.4\text{ mm}$).  
> **Fe500D rebar:** 12 mm & 10 mm @ 150 mm c/c bi-directional mats + 16/12 mm vertical starter dowels + 8 mm confinement ties.

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 1.3.1 | M25 RCC for 8 footing pads ($1.50 \times 1.428 \times 0.40\text{ m}$ each, $V = 6.857\text{ m}^3$) | m³ | 6.86 | 8,500 | 58,310 |
| 1.3.2 | M25 RCC for 8 column pedestals ($0.23 \times 0.30 \times 1.8144\text{ m}$ each, $V = 0.995\text{ m}^3$) | m³ | 1.00 | 8,500 | 8,500 |
| 1.3.3 | Fe500D TMT rebar in footings + pedestals (mats + starter dowels + ties per BBS) | kg | 566 | 72 | 40,752 |
| 1.3.4 | Shuttering and centering for footing pad vertical edges ($18.74\text{ m}^2$) and 8 pedestals ($15.35\text{ m}^2$) | m² | 34.1 | 380 | 12,958 |
| 1.3.5 | Waterproofing admixture in footing concrete (integral type, Dr. Fixit Pidiproof) | kg | 55 | 85 | 4,675 |
| | | | | **Sub-Total 1.3** | **₹1,25,195** |

### 1.4 Underground Sump Water Tank

> **Sump:** $1800\text{ mm (L)} \times 1200\text{ mm (W)} \times 1800\text{ mm (D)}$ — Capacity: $\approx 3,888\text{ L}$  
> Under Sitout plinth; 150 mm waterproofed reinforced concrete walls + base slab; airtight flush SS 304 inspection manhole.

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 1.4.1 | M25 RCC base slab of sump ($1.8 \times 1.2 \times 0.15\text{ m}$) | m³ | 0.32 | 8,500 | 2,720 |
| 1.4.2 | M25 RCC walls of sump — 150 mm thick, 4 sides | m³ | 1.22 | 8,500 | 10,370 |
| 1.4.3 | M25 RCC roof slab of sump with manhole opening ($1.8 \times 1.2 \times 0.125\text{ m}$) | m³ | 0.27 | 8,500 | 2,295 |
| 1.4.4 | Fe500 rebar for sump (mesh + vertical bars, $\approx 90\text{ kg/m}^3$ average) | kg | 164 | 72 | 11,808 |
| 1.4.5 | Two-coat integral crystalline waterproofing slurry (Xypex or Dr. Fixit) — all 6 surfaces | m² | 14.7 | 220 | 3,234 |
| 1.4.6 | SS 304 airtight flush inspection manhole cover ($450 \times 450\text{ mm}$) | No | 1 | 4,500 | 4,500 |
| 1.4.7 | Shuttering and centering for sump walls and roof | m² | 22.4 | 380 | 8,512 |
| 1.4.8 | 48-hour water ponding test and curing | LS | 1 | 500 | 500 |
| | | | | **Sub-Total 1.4** | **₹43,939** |

### 1.5 Septic Tank

> **Septic Tank:** $1200\text{ mm (L)} \times 1200\text{ mm (W)} \times 1800\text{ mm (D)}$ — Capacity: $\approx 2,592\text{ L}$  
> Under Toilet plinth; twin-chamber anaerobic baffle design; airtight inspection cover.

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 1.5.1 | M25 RCC base slab ($1.2 \times 1.2 \times 0.15\text{ m}$) | m³ | 0.22 | 8,500 | 1,870 |
| 1.5.2 | M25 RCC walls — 150 mm thick (4 sides + internal baffle) | m³ | 1.10 | 8,500 | 9,350 |
| 1.5.3 | M25 RCC roof slab with manhole opening ($1.2 \times 1.2 \times 0.125\text{ m}$) | m³ | 0.18 | 8,500 | 1,530 |
| 1.5.4 | Fe500 rebar for septic tank | kg | 135 | 72 | 9,720 |
| 1.5.5 | Integral waterproofing slurry — 2 coats on all 6 surfaces | m² | 10.4 | 220 | 2,288 |
| 1.5.6 | CI/SS airtight inspection cover + vent pipe (IS 1742 compliant) | No | 1 | 3,200 | 3,200 |
| 1.5.7 | Shuttering and centering | m² | 16.2 | 380 | 6,156 |
| | | | | **Sub-Total 1.5** | **₹34,114** |

### 1.6 Primary Entrance Steps (Road to Sitout)

> 6 uniform risers × $152.4\text{ mm}$ (6") each; tread $= 255\text{ mm}$ (10"); width $= 1350\text{ mm}$.

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 1.6.1 | M20 RCC steps structure ($1.35 \times 1.275\text{ m}$ × stepped volume $\approx 0.38\text{ m}^3$) | m³ | 0.38 | 7,500 | 2,850 |
| 1.6.2 | Fe500 rebar in steps | kg | 28 | 72 | 2,016 |
| 1.6.3 | Heavy-duty anti-skid terracotta-red flamed granite / clay paving tiles on steps | m² | 1.72 | 1,800 | 3,096 |
| | | | | **Sub-Total 1.6** | **₹7,962** |

> ### Section 1 Total: **₹2,76,361**

---

## Section 2 — Plinth Beams & RCC Structural Frame

### 2.1 Plinth Beams (Z = 614.4 to 914.4 mm | Depth = 300 mm / 375 mm)

> **PB1 Perimeter Ring Beams:** $230 \times 300\text{ mm}$ (Front, East, West) & $230 \times 375\text{ mm}$ (Rear South)  
> **PB_LIVING_Primary:** $230 \times 300\text{ mm}$ primary transverse plinth tie ($L = 5029.2\text{ mm}$) spanning C4 $\to$ C5  
> **PB2 Internal Tie Beams:** `PB2_Core_GridB` ($5.03\text{ m}$), `PB2_Bedroom_Living` ($2.82\text{ m}$), `PB2_Stair_East` & `West` ($1.71\text{ m}$)

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 2.1.1 | M25 RCC for perimeter plinth beams PB1 (Front, Rear upsized 375mm, East & West flanks) | m³ | 1.82 | 8,500 | 15,470 |
| 2.1.2 | M25 RCC for `PB_LIVING_Primary` cross plinth tie ($0.35\text{ m}^3$) and internal tie beams PB2 ($0.81\text{ m}^3$) | m³ | 1.16 | 8,500 | 9,860 |
| 2.1.3 | Fe500D TMT rebar in plinth beams ($3\#16\text{ mm}$ top/bot + $2\#12\text{ mm}$ curtailment + $8\text{ mm}$ stirrups @ 100/150 c/c per BBS) | kg | 583 | 72 | 41,976 |
| 2.1.4 | Shuttering and centering for plinth beam vertical sides | m² | 36.7 | 380 | 13,946 |
| 2.1.5 | Integral waterproofing admixture in plinth beam concrete | kg | 30 | 85 | 2,550 |
| | | | | **Sub-Total 2.1** | **₹83,802** |

### 2.2 Structural Columns (8 Nos. — Ground Floor)

> **All columns:** $230 \times 300\text{ mm}$ ($9'' \times 12''$) RCC — M25 concrete, Fe500D rebar  
> **Vertical span:** $Z = 914.4\text{ mm}$ to $Z = 3962.4\text{ mm}$ → Height $= 3048\text{ mm}$ ($10'\text{-}0''$)  
> **Reinforcement:** Corner columns C1, C2, C6, C7: $4\#16 + 2\#12\text{ mm}$; Interior/load columns C3, C4, C5, C8: $6\#16\text{ mm}$; Ties: $8\text{ mm}$ @ 100 mm ($L_o$) / 150 mm c/c

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 2.2.1 | M25 RCC for 8 GF columns ($0.23 \times 0.30 \times 3.048\text{ m}$ each, $V = 1.672\text{ m}^3$) | m³ | 1.67 | 8,500 | 14,195 |
| 2.2.2 | Fe500D TMT main bars ($16\text{ mm} + 12\text{ mm}$) + seismic ties ($8\text{ mm}$) in 8 GF columns per BBS | kg | 339 | 72 | 24,408 |
| 2.2.3 | Column shuttering and centering (4 faces × 8 columns × 3.048 m height = $25.78\text{ m}^2$) | m² | 25.8 | 400 | 10,320 |
| 2.2.4 | Needle vibration of concrete + curing compound (14-day protocol) | LS | 1 | 4,500 | 4,500 |
| | | | | **Sub-Total 2.2** | **₹53,423** |

### 2.3 Structural Columns — First Floor (8 Nos.)

> **All columns:** $230 \times 300\text{ mm}$ ($9'' \times 12''$) RCC — M25 concrete, Fe500D rebar  
> **Vertical span:** $Z = 3962.4\text{ mm}$ to $Z = 7010.4\text{ mm}$ → Height $= 3048\text{ mm}$ ($10'\text{-}0''$)

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 2.3.1 | M25 RCC for 8 FF columns ($0.23 \times 0.30 \times 3.048\text{ m}$ each) | m³ | 1.67 | 8,500 | 14,195 |
| 2.3.2 | Fe500D TMT rebar in 8 FF columns (lap splice + roof anchor hooks per BBS) | kg | 217 | 72 | 15,624 |
| 2.3.3 | Column shuttering and centering (FF level, 8 columns) | m² | 25.8 | 400 | 10,320 |
| 2.3.4 | Needle vibration and curing | LS | 1 | 4,500 | 4,500 |
| | | | | **Sub-Total 2.3** | **₹44,639** |

### 2.4 Roof Beams — Ground Floor Intermediate Slab Level

> **RB1 Perimeter Beams:** $230 \times 350\text{ mm}$ (Front, East, West) & $230 \times 375\text{ mm}$ (Rear South upsized)  
> **RB_LIVING_Primary:** $230 \times 350\text{ mm}$ ($9'' \times 14''$) primary cross-beam spanning C4 $\to$ C5 ($L = 5029.2\text{ mm}$)  
> **RB2 Internal Beams & Trimmers:** `RB2_Core_GridB` ($5.03\text{ m}$), `RB2_Bedroom_Living` ($2.82\text{ m}$), stair trimmers, `Kitchen_Beam_North`

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 2.4.1 | M25 RCC for GF perimeter roof beams RB1 (4 boundary beams incl. upsized rear) | m³ | 2.05 | 8,500 | 17,425 |
| 2.4.2 | M25 RCC for Primary Cross-Beam `RB_LIVING_Primary` ($0.40\text{ m}^3$) and internal roof beams RB2 ($0.86\text{ m}^3$) | m³ | 1.26 | 8,500 | 10,710 |
| 2.4.3 | M25 RCC for staircase mid-landing beam MLB ($230 \times 300\text{ mm}$, span 1.98 m) | m³ | 0.14 | 8,500 | 1,190 |
| 2.4.4 | Fe500D TMT rebar in all GF roof beams (incl. hanger stirrups, curtailments per BBS) | kg | 617 | 72 | 44,424 |
| 2.4.5 | Shuttering and centering for all GF roof beams (sides + soffits) | m² | 42.5 | 420 | 17,850 |
| | | | | **Sub-Total 2.4** | **₹91,599** |

### 2.5 Roof Beams — First Floor / Terrace Level

> **FF_RB1 Perimeter Beams:** $230 \times 300\text{ mm}$ / $230 \times 350\text{ mm}$  
> **FF_RB_LIVING_Primary:** $230 \times 350\text{ mm}$ ($9'' \times 14''$) upper primary cross-beam ($L = 5029.2\text{ mm}$)  
> **FF_RB2 Internal Beams:** `FF_RB2_Core_GridB`, `FF_RB2_Bedroom_Living`, stair trimmers

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 2.5.1 | M25 RCC for FF perimeter roof beams FF_RB1 (4 beams) | m³ | 1.91 | 8,500 | 16,235 |
| 2.5.2 | M25 RCC for Primary Cross-Beam `FF_RB_LIVING_Primary` ($0.40\text{ m}^3$) and internal roof beams FF_RB2 ($0.75\text{ m}^3$) | m³ | 1.15 | 8,500 | 9,775 |
| 2.5.3 | Fe500D TMT rebar in all FF roof beams per BBS | kg | 579 | 72 | 41,688 |
| 2.5.4 | Shuttering and centering for FF roof beams (sides + soffits) | m² | 39.8 | 420 | 16,716 |
| | | | | **Sub-Total 2.5** | **₹84,414** |

### 2.6 Intermediate Roof Slab — Ground Floor Ceiling ($125\text{ mm}$ thick)

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 2.6.1 | M25 RCC for 125 mm intermediate slab (GF ceiling) | m³ | 4.35 | 8,500 | 36,975 |
| 2.6.2 | Fe500 TMT rebar in slab (8 mm @ 150 mm c/c mesh, both ways) | kg | 400 | 72 | 28,800 |
| 2.6.3 | Shuttering/centering with steel plates and props for slab | m² | 34.83 | 500 | 17,415 |
| 2.6.4 | Slab concrete needle vibration + 14-day ponding curing | LS | 1 | 5,500 | 5,500 |
| 2.6.5 | Slab conduit casting — embedded conduits for electrical (30 mm heavy PVC, $\approx 85\text{ LM}$) | LM | 85 | 180 | 15,300 |
| | | | | **Sub-Total 2.6** | **₹1,03,990** |

### 2.7 Terrace Roof Slab — First Floor Ceiling ($125\text{ mm}$ thick)

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 2.7.1 | M25 RCC for 125 mm terrace roof slab (FF ceiling) | m³ | 4.35 | 8,500 | 36,975 |
| 2.7.2 | Fe500 rebar in terrace slab | kg | 400 | 72 | 28,800 |
| 2.7.3 | Shuttering and centering for FF terrace slab | m² | 34.83 | 500 | 17,415 |
| 2.7.4 | 14-day ponding curing on terrace slab | LS | 1 | 5,500 | 5,500 |
| 2.7.5 | Conduit casting in FF slab | LM | 85 | 180 | 15,300 |
| 2.7.6 | Two-coat elastomeric waterproofing on terrace (1:100 slope, fiber mesh) | m² | 38.33 | 320 | 12,266 |
| | | | | **Sub-Total 2.7** | **₹1,16,256** |

### 2.8 Staircase Headroom (Mumty) Structure & OHT Saddle Beams

> **Mumty Pillars:** Vertical extensions for C7 and C8 (`Mumty_Col_C7`, `Mumty_Col_C8`: $300 \times 228.6\text{ mm} \times 2325\text{ mm}$)  
> **OHT Saddle Beams:** 2 nos. $230 \times 230\text{ mm}$ M25 beams (`OHT_Saddle_Beam_North`/`South`, span $3536.1\text{ mm}$) directly transferring 1,000 L OHT gravity loads into columns C7 and C8  
> **Mumty Ring Beams & Roof Slab:** $230 \times 300\text{ mm}$ ring beams + $125\text{ mm}$ roof slab

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 2.8.1 | M25 RCC for 2 Mumty column extensions (`Mumty_Col_C7`, `Mumty_Col_C8`, $H = 2.325\text{ m}$) | m³ | 0.32 | 8,500 | 2,720 |
| 2.8.2 | M25 RCC for Mumty ring beams ($0.42\text{ m}^3$) + OHT Saddle Beams (2 nos., $0.37\text{ m}^3$) | m³ | 0.79 | 8,500 | 6,715 |
| 2.8.3 | M25 RCC for Mumty roof slab (125 mm) | m³ | 0.72 | 8,500 | 6,120 |
| 2.8.4 | Fe500D rebar for Mumty columns ($104\text{ kg}$) + Saddle Beams ($70\text{ kg}$) + Mumty ring/slab ($82\text{ kg}$) | kg | 256 | 72 | 18,432 |
| 2.8.5 | Shuttering and centering for Mumty (columns $4.92\text{ m}^2$ + saddles $5.09\text{ m}^2$ + ring/slab $16.5\text{ m}^2$) | m² | 26.5 | 450 | 11,925 |
| 2.8.6 | Waterproofing on Mumty roof slab + OHT pedestal M25 ($\varnothing 1200 \times 200\text{ mm}$) | LS | 1 | 6,500 | 6,500 |
| | | | | **Sub-Total 2.8** | **₹52,412** |

> ### Section 2 Total: **₹6,30,535**

---

## Section 3 — Masonry & Superstructure Walls *(AAC Block)*

> [!IMPORTANT]
> **Material Change: AAC (Autoclaved Aerated Concrete) blocks** replace burnt-clay brick throughout.  
> **Exterior walls: 8 inch (200 mm) AAC blocks** | **Interior partition walls: 4 inch (100 mm) AAC blocks**  
> AAC block mortar: thin-bed AAC jointing compound (3–5 mm joints) instead of conventional CM.  
> AAC blocks (Aerocon / Siporex / Magicrete): Grade A — density 550–650 kg/m³, compressive strength ≥ 3.5 N/mm².

> [!TIP]
> **Why AAC is better here:** 60% lighter than brick → reduces dead load on columns/beams, better thermal insulation (U-value $\approx 0.5\text{ W/m²K}$ vs $1.9$ for brick), faster laying speed (2–3× faster), no soaking required, minimal mortar wastage, GRIHA-rated eco-friendly.

### 3.1 Exterior Walls — 8" (200 mm) AAC Block Masonry

> Total GF + FF external wall area: $\approx 165\text{ m}^2$ combined (after deducting openings).

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 3.1.1 | 200 mm AAC blocks (Grade A, 625×200×200 mm) supply | m³ | 16.5 | 4,800 | 79,200 |
| 3.1.2 | AAC block jointing compound (thin-bed mortar, 25 kg bags) | Bag | 64 | 380 | 24,320 |
| 3.1.3 | AAC block laying labour — GF + FF external walls (165 m² × 0.20 m = 33 m³) | m³ | 33.0 | 600 | 19,800 |
| 3.1.4 | 6 mm chicken wire mesh at column-wall junction (anti-crack, both sides) | m² | 165 | 65 | 10,725 |
| 3.1.5 | AAC wall cement plaster bonding primer / polymer bonding agent (2 coats) | m² | 165 | 80 | 13,200 |
| 3.1.6 | Cement mortar capping on AAC parapet tops (CM 1:3) | LM | 28 | 120 | 3,360 |
| | | | | **Sub-Total 3.1** | **₹1,50,605** |

### 3.2 Interior Partition Walls — 4" (100 mm) AAC Block Masonry

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 3.2.1 | 100 mm AAC blocks (Grade A, 625×200×100 mm) supply | m³ | 6.8 | 4,800 | 32,640 |
| 3.2.2 | AAC block jointing compound (thin-bed mortar) | Bag | 26 | 380 | 9,880 |
| 3.2.3 | AAC block laying labour — GF + FF interior partitions (110 m² × 0.10 m = 11 m³) | m³ | 11.0 | 600 | 6,600 |
| 3.2.4 | Chicken wire mesh at all column/beam-to-AAC junctions | m² | 110 | 65 | 7,150 |
| 3.2.5 | AAC bonding primer for internal walls | m² | 110 | 80 | 8,800 |
| 3.2.6 | Staircase North wall — 200 mm AAC block ($W = 1752\text{ mm}$, $H = 1524\text{ mm}$) | m² | 2.67 | 820 | 2,189 |
| 3.2.7 | AAC parapet walls on terrace (100 mm, 900 mm high, 3 sides) | LM | 16.8 | 650 | 10,920 |
| | | | | **Sub-Total 3.2** | **₹78,179** |

### 3.3 Continuous RCC Lintel & Sill Seismic Bands (IS 4326 & NBC Compliance)

> Continuous full-width $360°$ closed-loop RCC lintel ($200 \times 150\text{ mm}$) and sill bands ($200 \times 75\text{ mm}$) cast monolithic with columns across all exterior envelope and interior masonry runs.

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 3.3.1 | M20 RCC continuous lintel and sill bands ($L = 52.1\text{ LM}$) — GF level | m³ | 1.16 | 7,500 | 8,700 |
| 3.3.2 | M20 RCC continuous lintel and sill bands ($L = 63.8\text{ LM}$) — FF level | m³ | 1.16 | 7,500 | 8,700 |
| 3.3.3 | Fe500D TMT rebar in lintel/sill bands (2 × 10 mm main + 6 mm stirrups @ 150 mm c/c) | kg | 175 | 72 | 12,600 |
| | | | | **Sub-Total 3.3** | **₹30,000** |

> ### Section 3 Total: **₹2,58,784** *(Saving of ₹21,613 vs original brick BOQ)*

---

## Section 4 — Staircases

### 4.1 RCC Dog-Legged Staircase — NBC 2016 Compliant (4-Winder Turnaround)

> **17 uniform risers** of $186.65\text{ mm}$ each ($\Delta R = 0.0\text{ mm}$)  
> **Tread going:** $249.25\text{ mm}$ (straight flights) + 4 winder steps at landing  
> **Flight width:** $720\text{ mm}$ | **Landing depth:** $750\text{ mm}$ | **Waist slab:** $125\text{ mm}$

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 4.1.1 | M25 RCC for stair waist slabs, landings, and winder steps — GF stair | m³ | 1.45 | 9,000 | 13,050 |
| 4.1.2 | M25 RCC for stair waist slabs, landings, and winder steps — FF stair | m³ | 1.45 | 9,000 | 13,050 |
| 4.1.3 | Fe500 TMT rebar in both stair flights and landings | kg | 240 | 72 | 17,280 |
| 4.1.4 | Shuttering and centering for stair soffits (inclined formwork) | m² | 22.4 | 550 | 12,320 |
| 4.1.5 | Black Galaxy granite treads ($720 \times 249.25\text{ mm}$, 20 mm thick, 17 Nos.) + bullnose nosing | No | 17 | 1,800 | 30,600 |
| 4.1.6 | Anti-skid granite step risers + step curbs for toilet sunken area | No | 17 | 900 | 15,300 |
| 4.1.7 | Landing granite tile finish (mid-landing + terrace landing) | m² | 2.8 | 1,800 | 5,040 |
| | | | | **Sub-Total 4.1** | **₹1,06,640** |

### 4.2 SS 304 Stainless Steel Safety Railings & Void Guardrails (NBC 2016 Compliant)

> **Total railing run:** $28.5\text{ Running Meters}$ — $\varnothing 50\text{ mm}$ top rail + 3 × $\varnothing 20\text{ mm}$ intermediate bars

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 4.2.1 | SS 304 $\varnothing 50\text{ mm}$ handrail top tube — GF + FF staircase flights | LM | 18.5 | 1,800 | 33,300 |
| 4.2.2 | SS 304 $\varnothing 20\text{ mm}$ horizontal intermediate bars (3 per panel × 5 panels) | LM | 55.5 | 750 | 41,625 |
| 4.2.3 | SS 304 railing uprights ($\varnothing 32\text{ mm}$, H = 900 mm, @ 1200 mm c/c) | No | 24 | 1,500 | 36,000 |
| 4.2.4 | SS 304 terrace perimeter safety railing (front + sides) | LM | 10.0 | 2,200 | 22,000 |
| 4.2.5 | Staircase void guardrail (open stairwell guard) — SS 304 | LM | 6.8 | 2,200 | 14,960 |
| 4.2.6 | Polishing, base plate welding, anchor bolting, sealant | LS | 1 | 12,000 | 12,000 |
| | | | | **Sub-Total 4.2** | **₹1,59,885** |

> ### Section 4 Total: **₹2,66,525**

---

## Section 5 — Plastering, Waterproofing & Finishes

> [!NOTE]
> AAC block walls require a **polymer bonding coat** before conventional cement plaster to prevent delamination and map cracking. Specified below.

### 5.1 Internal Wall Plastering (AAC Block — Single Coat 12 mm)

> AAC block walls need only 12 mm single-coat plaster (vs 15 mm for brick) due to flatter block surface.

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 5.1.1 | 12 mm cement plaster CM 1:5 over bonding coat — GF internal walls | m² | 185 | 200 | 37,000 |
| 5.1.2 | 12 mm cement plaster CM 1:5 over bonding coat — FF internal walls | m² | 185 | 200 | 37,000 |
| 5.1.3 | 2 mm skim coat / putty finish over plaster (GF + FF) | m² | 370 | 120 | 44,400 |
| | | | | **Sub-Total 5.1** | **₹1,18,400** |

### 5.2 External Wall Plastering & Facade Finishes

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 5.2.1 | 15 mm cement plaster CM 1:4 over bonding coat — GF external walls | m² | 110 | 240 | 26,400 |
| 5.2.2 | 15 mm cement plaster CM 1:4 over bonding coat — FF external walls | m² | 105 | 240 | 25,200 |
| 5.2.3 | Horizontal groove feature wall cladding slats (Charcoal, 28 slats — NW corner tower) | m² | 4.57 | 2,500 | 11,425 |
| 5.2.4 | Roofline fascia band (dark charcoal slate, $5069 \times 150\text{ mm}$) | LM | 5.07 | 1,200 | 6,084 |
| 5.2.5 | Roofline drip cornice (architectural white, $5089 \times 30\text{ mm}$) | LM | 5.09 | 750 | 3,818 |
| 5.2.6 | Main door white block architectural surround (17 rusticated quoin blocks) | LS | 1 | 9,500 | 9,500 |
| 5.2.7 | Warm terracotta-peach accent wall paint — Living room entrance wall | m² | 14.3 | 350 | 5,005 |
| | | | | **Sub-Total 5.2** | **₹87,432** |

### 5.3 Toilet Sunken Wet Area Waterproofing ($150\text{ mm}$ Drop)

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 5.3.1 | Sunken floor excavation (100 mm PCC below 150 mm drop) | m² | 2.23 | 450 | 1,004 |
| 5.3.2 | M10 PCC 100 mm base in sunken toilet | m² | 2.23 | 580 | 1,293 |
| 5.3.3 | Two-coat chemical elastomeric waterproofing slurry (Dr. Fixit Fastflex / Xypex) | m² | 8.5 | 350 | 2,975 |
| 5.3.4 | $150\text{ mm}$ perimeter cove angle fillet with fiber mesh reinforcement | LM | 11.6 | 280 | 3,248 |
| 5.3.5 | Black granite step riser curb at toilet entry | LS | 1 | 3,500 | 3,500 |
| 5.3.6 | 48-hour mandatory water ponding test before tiling | LS | 1 | 500 | 500 |
| 5.3.7 | Anti-skid vitrified tile for toilet floor (300 × 300 mm, R11 rating) | m² | 2.23 | 1,400 | 3,122 |
| 5.3.8 | Ceramic wall tile for toilet walls (300 × 450 mm, 2.4 m height) | m² | 13.5 | 850 | 11,475 |
| | | | | **Sub-Total 5.3** | **₹27,117** |

> ### Section 5 Total: **₹2,32,949** *(Saving of ₹11,700 vs original)*

---

## Section 6 — Flooring

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 6.1 | Anti-skid ceramic tiles — Sitout verandah ($3.35\text{ m}^2$) | m² | 3.35 | 1,200 | 4,020 |
| 6.2 | Large-format vitrified tiles ($600 \times 600\text{ mm}$) — Living Room ($13.38\text{ m}^2$) | m² | 13.38 | 1,600 | 21,408 |
| 6.3 | Vitrified tiles — Master Bedroom ($9.29\text{ m}^2$) | m² | 9.29 | 1,600 | 14,864 |
| 6.4 | Vitrified tiles — Kitchen ($3.90\text{ m}^2$) | m² | 3.90 | 1,600 | 6,240 |
| 6.5 | Screed bed (25 mm CM 1:4) for all floor tiles | m² | 30.0 | 180 | 5,400 |
| 6.6 | FF duplicate floor tiling (all rooms — same spec as GF) | m² | 30.0 | 1,600 | 48,000 |
| 6.7 | Rooftop terrace floor — anti-skid rustic vitrified tile / IPS finish | m² | 38.33 | 1,200 | 45,996 |
| | | | | **Sub-Total 6** | **₹1,45,928** |

> ### Section 6 Total: **₹1,45,928**

---

## Section 7 — Doors, Windows & Facade Joinery

### 7.1 Doors *(Revised)*

> [!NOTE]
> **Door revision summary:**
> - Main entrance → **Steel door** (security + cost saving vs teak)
> - Living Room → **Single steel door** (retained — security/weather barrier between open sitout and living space)
> - Bedroom → **Flush door** (factory-made flush, cost-effective)
> - Toilet → **UPVC/PVC waterproof door** (ideal for wet areas — warp-proof, rot-proof)
> - Geyser unit **removed**; 16A electrical provision retained

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 7.1.1 | GF Main entrance — **steel door** (ISI marked, 5-panel embossed, $1050 \times 2100\text{ mm}$) with frame + SS lever handle | No | 1 | 14,000 | 14,000 |
| 7.1.2 | GF Living Room — **single steel door** ($1050 \times 2100\text{ mm}$) with frame + hardware *(recommended: acts as primary security barrier between open sitout and living space)* | No | 1 | 12,000 | 12,000 |
| 7.1.3 | GF Bedroom — **flush door** (commercial ply, 35 mm thick, $914 \times 2133\text{ mm}$) with teak frame + lever handle | No | 1 | 6,500 | 6,500 |
| 7.1.4 | GF Toilet — **UPVC waterproof door** ($762 \times 2100\text{ mm}$) with frame + SS hinges + rubber seal | No | 1 | 5,500 | 5,500 |
| 7.1.5 | FF duplicate door set (Main steel + Living steel + Bedroom flush + Toilet UPVC) | Set | 1 | 38,000 | 38,000 |
| | | | | **Sub-Total 7.1** | **₹76,000** |
| | *(Saving vs original teak doors: **₹88,500**)* | | | | |

### 7.2 Windows & Ventilators

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 7.2.1 | GF Living Room — 3-split UPVC sliding window ($1800 \times 1200\text{ mm}$, tinted glass + safety grill) | No | 1 | 14,500 | 14,500 |
| 7.2.2 | Toilet louvred ventilator window ($600 \times 600\text{ mm}$) — GF | No | 1 | 3,200 | 3,200 |
| 7.2.3 | FF Living Room UPVC window — identical to GF | No | 1 | 14,500 | 14,500 |
| 7.2.4 | Staircase architectural louvered niche frame ($880 \times 620\text{ mm}$, 5 dark charcoal slats) | No | 1 | 8,500 | 8,500 |
| 7.2.5 | Bedroom East window ($1200 \times 900\text{ mm}$ UPVC) | No | 1 | 8,500 | 8,500 |
| 7.2.6 | FF toilet ventilator + bedroom window (duplicate of GF) | Set | 1 | 11,700 | 11,700 |
| 7.2.7 | Safety grills (MS powder-coated) for all windows | m² | 12.4 | 1,200 | 14,880 |
| | | | | **Sub-Total 7.2** | **₹75,780** |

### 7.3 Sitout Safety Gate & Facade Elements

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 7.3.1 | Custom SS 304 + dark charcoal double-leaf safety gate ($1386 \times 1000\text{ mm}$, 6 tubes + aldrop) | No | 1 | 28,000 | 28,000 |
| 7.3.2 | Canopy warm teak wood soffit panels — GF entrance + FF balcony (2 Nos.) | m² | 1.78 | 3,200 | 5,696 |
| 7.3.3 | FF balcony linear planter box ($1485.9 \times 250 \times 350\text{ mm}$, charcoal + drip rim + greenery) | LM | 1.49 | 6,500 | 9,685 |
| 7.3.4 | Rooftop cantilevered pergola trellis (4 beams, charcoal aluminum, $750\text{ mm}$ cantilever) | LS | 1 | 18,000 | 18,000 |
| 7.3.5 | Flamed granite plinth floating steps with LED cove ($1485.9 \times 300\text{ mm}$, 3 steps) | LS | 1 | 22,000 | 22,000 |
| | | | | **Sub-Total 7.3** | **₹83,381** |

> ### Section 7 Total: **₹2,35,161** *(Saving of ₹88,500 vs original)*

---

## Section 8 — Electrical, ELV & Surveillance

### 8.1 MCB Distribution Boards

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 8.1.1 | GF Main Distribution Board (MDB) — 12-way, 40A 30mA 4-pole RCCB + 8 SP MCBs | No | 1 | 9,500 | 9,500 |
| 8.1.2 | FF duplicate MDB — 12-way | No | 1 | 9,500 | 9,500 |
| | | | | **Sub-Total 8.1** | **₹19,000** |

### 8.2 Modular Switchboards & Consoles

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 8.2.1 | SB-1 Sitout 4-module board | No | 1 | 1,800 | 1,800 |
| 8.2.2 | SB-2 Living Room Main Entry 8-module | No | 1 | 2,800 | 2,800 |
| 8.2.3 | SB-3 Living Room TV Media 8+2 module (HDMI, RJ45, DTH, fiber) | No | 1 | 6,500 | 6,500 |
| 8.2.4 | SB-4 Living Room corner 2-module | No | 1 | 900 | 900 |
| 8.2.5 | SB-5 Staircase Entry 4-module | No | 1 | 1,800 | 1,800 |
| 8.2.6 | SB-6 Under-stair Utility 6-module (sump motor 16A + WM 16A) | No | 1 | 2,500 | 2,500 |
| 8.2.7 | SB-7 Toilet Entrance 6-module *(25A geyser DP isolator switch retained as provision — geyser unit not purchased now)* | No | 1 | 3,200 | 3,200 |
| 8.2.8 | SB-8 Toilet high-level 16A/25A socket provision *(conduit + socket installed; geyser unit deferred)* | No | 1 | 1,400 | 1,400 |
| 8.2.9 | SB-9 Bedroom Entry 8-module + BLDC regulator | No | 1 | 3,500 | 3,500 |
| 8.2.10 | SB-10 Bedside consolidated console (2-way switch) | No | 1 | 2,200 | 2,200 |
| 8.2.11 | SB-11 to SB-16 Kitchen + stair + AC + CCTV boards (6 boards) | No | 6 | 2,500 | 15,000 |
| 8.2.12 | FF duplicate switchboard set (16 boards, same as GF) | Set | 1 | 42,000 | 42,000 |
| | | | | **Sub-Total 8.2** | **₹83,600** |

### 8.3 Ceiling Fixtures & Luminaires

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 8.3.1 | Deep PVC spotlight junction pots ($\varnothing 75\text{ mm}$) cast in slab — GF (12 nos.) | No | 12 | 450 | 5,400 |
| 8.3.2 | Malleable iron fan hook boxes with safety clamp — GF (3 nos.) | No | 3 | 850 | 2,550 |
| 8.3.3 | 50W BLDC ceiling fans — Living, Bedroom, Kitchen (GF) | No | 3 | 3,800 | 11,400 |
| 8.3.4 | 7W–9W COB LED downlight spotlights (GF, 12 nos.) | No | 12 | 650 | 7,800 |
| 8.3.5 | GF canopy IP65 flush downlights ($\varnothing 75\text{ mm}$, 5W warm LED, 4 nos.) | No | 4 | 1,200 | 4,800 |
| 8.3.6 | FF duplicate ceiling fixtures + fans + spotlights | Set | 1 | 32,000 | 32,000 |
| 8.3.7 | Staircase wall luminaires (GF + FF + Mumty, 3 weatherproof fittings) | No | 3 | 2,200 | 6,600 |
| 8.3.8 | Rooftop terrace weatherproof wall luminaire + SB-TERRACE board | No | 1 | 3,500 | 3,500 |
| | | | | **Sub-Total 8.3** | **₹74,050** |

### 8.4 Wiring, Conduits & Cable Infrastructure

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 8.4.1 | Heavy-duty 25 mm PVC conduit (wall + slab chase) — GF | LM | 95 | 180 | 17,100 |
| 8.4.2 | Heavy-duty 25 mm PVC conduit — FF | LM | 90 | 180 | 16,200 |
| 8.4.3 | 2.5 sq.mm FR-LSH copper multi-strand wire (lighting + sockets) — GF + FF | LM | 850 | 65 | 55,250 |
| 8.4.4 | 4.0 sq.mm copper wire (AC, geyser provision, motor home-runs) | LM | 180 | 95 | 17,100 |
| 8.4.5 | 6.0 sq.mm copper wire (main incomer) | LM | 25 | 140 | 3,500 |
| 8.4.6 | CCTV coaxial + CAT6 LAN + DTH satellite cable (rooftop to boards) | LS | 1 | 15,000 | 15,000 |
| 8.4.7 | 6 CCTV deep PVC pot points ($\varnothing 85\text{ mm}$, slab-cast) | No | 6 | 600 | 3,600 |
| 8.4.8 | Earthing pit + GI tape loop + DB earth strips | LS | 1 | 8,500 | 8,500 |
| | | | | **Sub-Total 8.4** | **₹1,36,250** |

> ### Section 8 Total: **₹3,12,900** *(Geyser unit excluded; provision wiring retained)*

---

## Section 9 — Plumbing, Sanitary & Water Supply

### 9.1 Overhead Water Tank (OHT) — Mumty Rooftop

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 9.1.1 | 1,000 L 4-layer antimicrobial UV polymer tank (Sintex / Penguin) | No | 1 | 8,500 | 8,500 |
| 9.1.2 | SS 304 external maintenance monkey ladder (8 rungs, $Z = 7260$ to $9750\text{ mm}$) | No | 1 | 18,000 | 18,000 |
| 9.1.3 | OHT overflow pipe + anti-vacuum vent + sediment trap scour valve | LS | 1 | 3,500 | 3,500 |
| 9.1.4 | 1.25" master gravity shut-off brass ball valve + 4-way cross manifold | LS | 1 | 4,500 | 4,500 |
| | | | | **Sub-Total 9.1** | **₹34,500** |

### 9.2 Sump Motor & Pumping System

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 9.2.1 | 1.0 HP monobloc water pump motor (ISI marked) | No | 1 | 7,500 | 7,500 |
| 9.2.2 | Anti-vibration concrete pedestal ($480 \times 320 \times 100\text{ mm}$ M25 RCC) | LS | 1 | 1,800 | 1,800 |
| 9.2.3 | 32 mm UPVC suction line + foot valve + brass NRV check valve | LS | 1 | 3,200 | 3,200 |
| 9.2.4 | 25 mm UPVC delivery riser + gate valve + DOL starter panel | LS | 1 | 4,500 | 4,500 |
| | | | | **Sub-Total 9.2** | **₹17,000** |

### 9.3 Closed-Loop Water Distribution Network (CPVC)

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 9.3.1 | 25 mm CPVC SDR 11 toilet riser (Line A) — GF + FF toilet showers | LM | 14.5 | 280 | 4,060 |
| 9.3.2 | 25 mm CPVC SDR 11 kitchen riser (Line B) — front weather head to kitchen | LM | 18.5 | 280 | 5,180 |
| 9.3.3 | 20 mm CPVC utility bibcock feeder (Line C — washing machine) | LM | 9.0 | 220 | 1,980 |
| 9.3.4 | 20 mm CPVC terrace tap feeder (Line D — Mumty bibcock) | LM | 5.5 | 220 | 1,210 |
| 9.3.5 | 32 mm CPVC pumping rising main (staircase duct, sump to OHT) | LM | 26.0 | 380 | 9,880 |
| 9.3.6 | 6 forged-brass red-lever isolation shut-off valves (zonal) | No | 6 | 1,800 | 10,800 |
| 9.3.7 | Kitchen sink chrome high-arch faucets (GF + FF) + municipal tap (GF) | No | 3 | 2,200 | 6,600 |
| 9.3.8 | Dual-spout brass bibcock (under-stair washing machine utility) | No | 1 | 1,800 | 1,800 |
| 9.3.9 | Terrace utility heavy-duty brass bibcock on Mumty South wall | No | 1 | 1,500 | 1,500 |
| 9.3.10 | Municipal inflow water meter + master shut-off valve (East boundary) | LS | 1 | 6,500 | 6,500 |
| | | | | **Sub-Total 9.3** | **₹49,510** |

### 9.4 Sanitary Fixtures & Drain System *(Revised — Washbasin Removed)*

> [!NOTE]
> **GF toilet revision:** Wall-mounted ceramic washbasin and CP mixer set **removed**.  
> **Retained:** Indian squatting pan + chrome shower set only.  
> 10 L instant geyser **unit removed**; 16A socket + 4 sq.mm circuit + 25A MCB provision **retained**.

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 9.4.1 | Indian ceramic squatting pan with anti-skid footrests — GF toilet | No | 1 | 3,500 | 3,500 |
| ~~9.4.2~~ | ~~Wall-mounted ceramic washbasin + CP mixer set — GF toilet~~ | — | — | — | ~~₹4,500~~ **Removed** |
| 9.4.3 | Chrome shower set with diverter — GF toilet | No | 1 | 3,200 | 3,200 |
| ~~9.4.4~~ | ~~10 L instant geyser water heater — GF toilet~~ | — | — | — | ~~₹4,800~~ **Deferred — provision only** |
| 9.4.5 | FF toilet: wall-hung WC + washbasin + shower set (FF spec may differ — confirm later) | Set | 1 | 16,000 | 16,000 |
| 9.4.6 | 110 mm PVC soil pipe (WC → septic tank, 3.5 m run, 1:40 slope) | LM | 3.5 | 380 | 1,330 |
| 9.4.7 | 50 mm PVC waste pipe (floor drain → gully trap GT-1) | LM | 5.0 | 220 | 1,100 |
| 9.4.8 | 50 mm PVC waste pipe (kitchen sink → IC-1 → road outfall) | LM | 8.0 | 220 | 1,760 |
| 9.4.9 | P-trap, gully traps, inspection chamber (IC-1) with CI cover | LS | 1 | 7,500 | 7,500 |
| 9.4.10 | Washing machine floor drain trap + braided SS inlet hose | No | 1 | 1,800 | 1,800 |
| 9.4.11 | Kitchen SS single-bowl sink (built-in granite counter) | No | 1 | 4,500 | 4,500 |
| 9.4.12 | EB temporary water connection (municipal) | LS | 1 | 5,000 | 5,000 |
| | | | | **Sub-Total 9.4** | **₹45,690** |
| | *(Saving vs original: **₹9,300** — washbasin ₹4,500 + geyser unit ₹4,800 removed)* | | | | |

> ### Section 9 Total: **₹1,46,700** *(Saving ₹9,300)*

---

## Section 10 — Kitchen Fixtures & Built-In Fittings

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 10.1 | Black Galaxy granite L-counter (600 mm depth, 850 mm FFL, 20 mm thick) — GF kitchen | m² | 3.2 | 4,800 | 15,360 |
| 10.2 | Breakfast counter bar granite top ($600 \times 1000\text{ mm}$) — GF | No | 1 | 6,000 | 6,000 |
| 10.3 | 3-zone induction hob (built-in) — GF kitchen | No | 1 | 7,500 | 7,500 |
| 10.4 | Kitchen exhaust fan ($300\text{ mm}$, East side wall over sink) — GF | No | 1 | 2,800 | 2,800 |
| 10.5 | RCC overhead lofts in kitchen (2 lofts, shuttered and cast) | No | 2 | 3,500 | 7,000 |
| 10.6 | FF kitchen duplicate (granite L-counter + breakfast bar + hob + exhaust + lofts) | Set | 1 | 38,000 | 38,000 |
| | | | | **Sub-Total 10** | **₹76,660** |

> ### Section 10 Total: **₹76,660**

---

## Section 11 — Painting & Final Finishes

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 11.1 | Interior wall primer + 2-coat premium emulsion (GF) | m² | 210 | 180 | 37,800 |
| 11.2 | Interior wall primer + 2-coat premium emulsion (FF) | m² | 210 | 180 | 37,800 |
| 11.3 | Exterior weatherproof Apex / Snowcem paint (GF + FF facade, 3 coats) | m² | 215 | 220 | 47,300 |
| 11.4 | Architectural white paint for block surround + columns + cornice | m² | 35 | 220 | 7,700 |
| 11.5 | Dark charcoal slate paint for fascia band + gate accent panels | m² | 18 | 250 | 4,500 |
| 11.6 | Ceiling primer + OBD / oil-bound distemper (GF + FF, 2 coats) | m² | 76 | 140 | 10,640 |
| | | | | **Sub-Total 11** | **₹1,45,740** |

> ### Section 11 Total: **₹1,45,740**

---

## Section 12 — Plant, Equipment & Miscellaneous

| Item | Description | Unit | Qty | Rate (₹) | Amount (₹) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 12.1 | Concrete mixer (drum type, 200L) rental — 8 weeks | Week | 8 | 3,500 | 28,000 |
| 12.2 | Needle vibrator rental — casting days only | Week | 6 | 1,200 | 7,200 |
| 12.3 | Scaffolding props and steel plates rental | Week | 10 | 4,000 | 40,000 |
| 12.4 | EB temporary power connection (construction supply) | LS | 1 | 8,000 | 8,000 |
| 12.5 | Municipal plan approval + building permission fees | LS | 1 | 12,000 | 12,000 |
| 12.6 | Cube testing, soil testing, slump tests (quality assurance) | LS | 1 | 5,000 | 5,000 |
| 12.7 | Safety PPE, site barricading, first-aid equipment | LS | 1 | 4,500 | 4,500 |
| 12.8 | Water curing labor (hand misting + hessian burlap, 14-day cycles) | LS | 1 | 6,000 | 6,000 |
| 12.9 | General site cleanup, debris removal, final handover cleaning | LS | 1 | 8,000 | 8,000 |
| | | | | **Sub-Total 12** | **₹1,18,700** |

> ### Section 12 Total: **₹1,18,700**

---

## 📊 Bill of Quantities Summary — Revision 2 (8-Column RCC Frame Sync)

| Section | Description | Original (14-Col) (₹) | Revised (8-Col) (₹) | Change (₹) | Status & Structural Notes |
| :--- | :--- | ---: | ---: | ---: | :--- |
| **01** | Substructure, Earthwork, Underground Tanks & Steps | 2,15,782 | **2,76,361** | **+60,579** | 8 larger pads ($1.5 \times 1.43\text{ m}$) & 8 pedestals ($H = 1.81\text{ m}$) |
| **02** | Plinth Beams, Columns, Roof Beams & Slabs | 6,56,782 | **6,30,535** | **−26,247** | Net savings from 6 fewer columns & reduced shuttering |
| **03** | Masonry — AAC Blocks & Continuous Seismic Bands | 2,80,397 | **2,58,784** | **−21,613** | AAC blocks + IS 4326 continuous lintel & sill bands |
| **04** | Staircases — RCC + Granite + SS 304 Railings | 2,66,525 | **2,66,525** | — | 17 uniform risers + SS 304 safety railings |
| **05** | Plastering, Waterproofing & Facade | 2,44,649 | **2,32,949** | **−11,700** | Single-coat 12 mm plaster over AAC bonding coat |
| **06** | Flooring | 1,45,928 | **1,45,928** | — | Vitrified tiles + anti-skid terrace |
| **07** | Doors, Windows, Gates & Joinery | 3,23,661 | **2,35,161** | **−88,500** | Steel entrance + flush bedroom + UPVC toilet |
| **08** | Electrical, ELV & CCTV (geyser unit excluded) | 3,12,900 | **3,12,900** | — | 16 switchboards + conduits + CCTV provisions |
| **09** | Plumbing, Sanitary (washbasin + geyser removed) | 1,56,000 | **1,46,700** | **−9,300** | CPVC closed loop + 1000L OHT + dual stream |
| **10** | Kitchen Fixtures | 76,660 | **76,660** | — | Black Galaxy granite counter + breakfast bar |
| **11** | Painting & Finishes | 1,45,740 | **1,45,740** | — | Apex exterior + premium interior emulsion |
| **12** | Plant, Equipment & Miscellaneous | 1,18,700 | **1,18,700** | — | Mixer, vibrator, props rental & quality testing |
| | | | | | |
| | **GROSS TOTAL (A)** | **₹27,43,324** | **₹28,46,943** | **+₹1,03,619** | **+3.78% vs original / +5.47% vs Rev 1** |
| | Contingency Reserve @ 5% | ₹1,37,166 | **₹1,42,347** | +₹5,181 | Unforeseen site conditions & market fluctuations |
| | **ESTIMATED TOTAL (A + Contingency)** | **₹28,80,490** | **₹29,89,290** | **+₹1,08,800** | **Monolithic G+1 Frame Certified (CalculiX FEM PASS)** |

---

## 📌 Key Quantity Summary — 8-Column Monolithic Space Frame

| Resource | Quantity | Source / Engineering Specification |
| :--- | :---: | :--- |
| M25 Structural Concrete (RCC Frame) | **$\approx 22.5\text{ m}^3$** | Footings ($6.86$) + Pedestals ($1.00$) + PB ($2.98$) + Cols ($3.66$) + RB ($7.30$) + Saddles ($0.37$) + Slabs ($9.42\text{ m}^3$) |
| Fe500D TMT Rebar (Space Frame Net Fabricated) | **$3,076.2\text{ kg}$ ($3.08\text{ MT}$)** | IS 13920:2016 ductile detailed BBS ([`docs/bbs_8_column_frame.csv`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/docs/bbs_8_column_frame.csv)) |
| Fe500D Commercial Rebar Procurement (+4% Margin) | **$3,199.2\text{ kg}$ ($3.20\text{ MT}$)** | **305 commercial 12m bars / 62 bundles** (8mm: 15 bdl, 10mm: 3 bdl, 12mm: 9 bdl, 16mm: 35 bdl) |
| Total Structural Steel (incl. Slabs, Stairs, Tanks) | **$\approx 4.76\text{ Metric Tons}$** | Frame ($3.20\text{ MT}$) + Slabs ($0.80\text{ MT}$) + Stairs ($0.24\text{ MT}$) + Tanks ($0.30\text{ MT}$) + Bands ($0.18\text{ MT}$) + Steps ($0.04\text{ MT}$) |
| Formwork / Shuttering (Columns + Beams + Footings) | **$\approx 195.4\text{ m}^2$** | Footings ($18.7\text{ m}^2$) + Pedestals ($15.4\text{ m}^2$) + Columns ($56.5\text{ m}^2$) + Beams ($104.8\text{ m}^2$) |
| Total Built-Up Area | $\approx 850\text{ sq.ft}$ | Ground Floor $412.5\text{ sq.ft} +$ First Floor $412.5\text{ sq.ft} +$ Staircase Mumty Tower |
| AAC Block — 200 mm (Exterior Wall Envelope) | $\approx 16.5\text{ m}^3$ | Net masonry supply ($33.0\text{ m}^3$ gross wall) deducting $230 \times 300\text{ mm}$ columns & openings |
| AAC Block — 100 mm (Interior Partition Walls) | $\approx 6.8\text{ m}^3$ | Net partition block supply ($11.0\text{ m}^3$ gross wall) |
| Underground Sump Capacity | $3,888\text{ L}$ | $1.8 \times 1.2 \times 1.8\text{ m}$ M25 waterproofed RCC under Sitout plinth |
| Septic Tank Capacity | $2,592\text{ L}$ | $1.2 \times 1.2 \times 1.8\text{ m}$ twin-chamber anaerobic baffle tank under Toilet plinth |
| Overhead Water Tank Capacity | $1,000\text{ L}$ | Antimicrobial UV polymer tank on dual $230 \times 230\text{ mm}$ RCC saddle beams |
| SS 304 Staircase Railings & Void Guardrails | $28.5\text{ RM}$ | NBC 2016 compliant: $\varnothing 50\text{ mm}$ top rail + 3 intermediate $\varnothing 20\text{ mm}$ safety bars |
| Structural Columns | 8 (GF) + 8 (FF) + 2 (Mumty) = **18 total** | **$230 \times 300\text{ mm}$ ($9'' \times 12''$)** M25 RCC with Fe500D rebar |
| RCC Framing Beams (all levels) | 9 PB + 10 RB (GF) + 9 RB (FF) + 4 Mumty/OHT = **32 total** | Includes `RB_LIVING_Primary` ($230 \times 350\text{ mm}$) and upsized rear perimeter beams |
| Concealed PVC Conduits (electrical) | $\approx 185\text{ LM}$ | Slab-cast conduits + wall chases across GF and FF |
| Modular Switchboards | 16 (GF) + 16 (FF) = **32 total** | IS 732 compliant modular layout |

---

## 💰 Phase-Wise Payment Milestone Schedule — Revision 2

| Milestone | Work Description | Payment % | Approx. Amount (₹) |
| :--- | :--- | :---: | :---: |
| **Milestone 1 (15%)** | 8 Footing excavation, PCC blinding beds, 8 Footing pads, 8 Pedestals, Sump Tank & Septic Tank cast and cured | 15% | ₹4,48,394 |
| **Milestone 2 (15%)** | Plinth Beams (PB1 + `PB_LIVING_Primary` + PB2) cast, earth backfill compacted, anti-termite treatment done | 15% | ₹4,48,394 |
| **Milestone 3 (25%)** | All 16 Columns (GF+FF) cast to roof level; AAC block walls to lintel level + continuous seismic bands cast | 25% | ₹7,47,322 |
| **Milestone 4 (25%)** | Roof beams (`RB_LIVING_Primary`) & slabs shuttered, rebar bound per BBS, conduits cast & concrete poured | 25% | ₹7,47,322 |
| **Milestone 5 (15%)** | Internal/external plastering over bonding coat, plumbing hydro-tested at 5 bar, Mumty & OHT saddle beams cast | 15% | ₹4,48,394 |
| **Milestone 6 (5%)** | Tile flooring, paint finishes, electrical fittings, sanitary fixtures installed & final handover | 5% | ₹1,49,464 |
| | **TOTAL** | **100%** | **₹29,89,290** |

---

## 🔑 Notes & Engineering Safeguards

1. **8-Column Frame Optimization (IS 456 & IS 13920 Compliance):**
   - Structural refactoring replaced 14 slender ($9" \times 9"$) columns with 8 heavy-duty ($9" \times 12"$ / $230 \times 300\text{ mm}$) columns, eliminating interior columns in the living hall.
   - **`RB_LIVING_Primary` ($230 \times 350\text{ mm}$, clear span $5029.2\text{ mm}$):** Safely transmits upper partition and intermediate slab loads to columns C4 and C5 without exceeding allowable deflection ($\Delta = 5.56\text{ mm} \ll \text{Span}/250 = 20.12\text{ mm}$, CalculiX FEA validated).
   - **Mumty OHT Saddle Beams:** Dual $230 \times 230\text{ mm}$ M25 beams (`OHT_Saddle_Beam_North`/`South`) span directly across columns C7 and C8, directing the $11.0\text{ kN}$ OHT gravity load straight down the column grid into the foundation.

2. **BBS & Steel Optimization (IS 2502 & IS 13920):**
   - Rebar procurement is indexed to [`docs/bbs_8_column_frame.csv`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/docs/bbs_8_column_frame.csv) and [`docs/07_boq_schedules.md`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/docs/07_boq_schedules.md).
   - Column starter dowels ($4.00\text{ m}$) yield exactly 3 cuts per $12\text{ m}$ rod with **$0.0\%$ cutting loss**.
   - Beam rebar combinations ($8.006\text{ m}$ flank $+ 3.772\text{ m}$ curtailment $= 11.78\text{ m}$) achieve **$98.2\%$ commercial steel utilization** with $< 0.22\text{ m}$ scrap reused as chair supports.

3. **AAC Block Masonry & Jointing Compound:**
   - Lightweight AAC blocks (density 550–650 kg/m³) reduce dead loads on beams and footings by over 55% compared to burnt clay bricks.
   - Thin-bed adhesive polymer mortar (3–5 mm joints) prevents thermal bridging and eliminates thick cement mortar sand requirements.
   - Galvanized wire mesh must be installed at all column/beam-to-AAC junctions prior to applying the acrylic bonding agent.

4. **Rates & Certification:**
   - Benchmark rates reflect South Indian urban market costs for 2025–2026. GST (18% on service contracts) is excluded.
   - Derived directly from 3D parametric solids in [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd).

---

*BOQ prepared from model data in [`walkthrough.md`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/walkthrough.md), [`docs/77_75_rcc_structural_optimization.md`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/docs/77_75_rcc_structural_optimization.md), and [`docs/07_boq_schedules.md`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/docs/07_boq_schedules.md).*  
*Revision 2 — Updated: September 2026*
