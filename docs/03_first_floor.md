# First Floor AAC Block Masonry Specification & Wall Schedule

> [!NOTE]
> **Discipline:** Architectural & Structural Masonry Engineering (First Floor Expansion)  
> **Authoritative BIM Source:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Material Standard:** Autoclaved Aerated Concrete (AAC) Blocks per IS 2185 (Part 3): 1984  
> **Joint Adhesive:** Thin-Bed High-Strength Polymer-Modified AAC Block Adhesive (ASTM C1660 / IS 15477)  
> **Execution Baseline:** First Floor Finished Level $Z = +4087.4\text{ mm}$ to Roof Slab Soffit $Z = +7135.4\text{ mm}$ ($H = 3048.0\text{ mm}$ / $10'\text{-}0"$).

---

## 1. First Floor Modular Expansion Overview

The First Floor masonry layout maintains strict 1:1 vertical structural alignment with the Ground Floor load-bearing grid:
1. **Vertical Load Path Continuity:** All outer envelope walls ($200.0\text{ mm}$) and inner partition walls ($100.0\text{ mm}$) align directly over the corresponding Ground Floor walls and RCC beams, ensuring zero eccentric shear load on intermediate floor slabs.
2. **Structural Dead Load Reduction:** Standardizing on AAC block masonry (dry density $\approx 550 - 650\text{ kg/m}^3$) versus traditional red clay brickwork (density $\approx 1800 - 1920\text{ kg/m}^3$) achieves an exceptional **65% dead load reduction** on the First Floor slab and primary cross-beam `RB_LIVING_Primary`.
3. **Thermal Insulation & Energy Efficiency:** Thermal conductivity $k \approx 0.12 - 0.16\text{ W/m}\cdot\text{K}$ drastically attenuates tropical heat penetration through exterior facades.

---

## 2. First Floor Wall Geometry & Schedule Ledger

| Wall Identifier | Level | Functional Classification | Thickness ($T$) | Length ($L$) | Height ($H$) | Net Volume ($V$) | Alignment Baseline & Boundary Face |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `FF_Bedroom_Wall_South` | FF | Outer Envelope (Rear South) | $200.0\text{ mm}$ | $3048.0\text{ mm}$ | $3048.0\text{ mm}$ | $1.858\text{ m}^3$ | Flush with South plot boundary ($Y = 7620.0\text{ mm}$) |
| `FF_Kitchen_Wall_South` | FF | Outer Envelope (Rear South) | $200.0\text{ mm}$ | $1981.2\text{ mm}$ | $3048.0\text{ mm}$ | $1.208\text{ m}^3$ | Flush with South plot boundary ($Y = 7620.0\text{ mm}$) |
| `FF_Bedroom_Wall_West` | FF | Outer Envelope (West Boundary) | $200.0\text{ mm}$ | $3048.0\text{ mm}$ | $3048.0\text{ mm}$ | $1.858\text{ m}^3$ | Flush with West plot boundary ($X = 5029.2\text{ mm}$) |
| `FF_Living_Room_Wall_West` | FF | Outer Envelope (West Boundary) | $200.0\text{ mm}$ | $2857.5\text{ mm}$ | $3048.0\text{ mm}$ | $1.742\text{ m}^3$ | Flush with West plot boundary ($X = 5029.2\text{ mm}$) |
| `FF_Toilet_Wall_West` | FF | Outer Envelope (West Boundary) | $200.0\text{ mm}$ | $1714.5\text{ mm}$ | $3048.0\text{ mm}$ | $1.045\text{ m}^3$ | Flush with West plot boundary ($X = 5029.2\text{ mm}$) |
| `FF_Kitchen_Wall_East` | FF | Outer Envelope (East Boundary) | $200.0\text{ mm}$ | $2438.4\text{ mm}$ | $3048.0\text{ mm}$ | $1.251\text{ m}^3$ | Flush with East plot boundary ($X = 0.0\text{ mm}$); cutouts for W2 & Exhaust |
| `FF_Living_Room_Wall_East` | FF | Outer Envelope (East Boundary) | $200.0\text{ mm}$ | $3467.1\text{ mm}$ | $3048.0\text{ mm}$ | $1.682\text{ m}^3$ | Flush with East plot boundary ($X = 0.0\text{ mm}$); cutout for 3-Split W1 |
| `FF_Toilet_Wall_Front` | FF | Outer Envelope (North Facade) | $200.0\text{ mm}$ | $1219.2\text{ mm}$ | $3048.0\text{ mm}$ | $0.743\text{ m}^3$ | Flush with North front facade ($Y = 0.0\text{ mm}$) |
| `FF_Bedroom_Wall_North` | FF | Inner Partition (Living / Bed) | $100.0\text{ mm}$ | $3048.0\text{ mm}$ | $3048.0\text{ mm}$ | $0.734\text{ m}^3$ | Aligned at $Y \in [4526.0, 4626.0]$; cutout for D2 ($914 \times 2134\text{ mm}$) |
| `FF_Bedroom_Wall_East` | FF | Inner Partition (Bed / Kit Spine) | $100.0\text{ mm}$ | $3048.0\text{ mm}$ | $3048.0\text{ mm}$ | $0.929\text{ m}^3$ | Aligned at $X \in [1935.2, 2035.2]$; preserves $2794\text{ mm}$ Bed width |
| `FF_Kitchen_Wall_East` | FF | Outer Envelope (East Boundary) | $200.0\text{ mm}$ | $2438.4\text{ mm}$ | $3048.0\text{ mm}$ | $1.251\text{ m}^3$ | Flush with East plot boundary ($X = 0.0\text{ mm}$); cutouts for W2 & Exhaust |
| `FF_Living_Room_Wall_East` | FF | Outer Envelope (East Boundary) | $200.0\text{ mm}$ | $3467.1\text{ mm}$ | $3048.0\text{ mm}$ | $1.682\text{ m}^3$ | Flush with East plot boundary ($X = 0.0\text{ mm}$); cutout for 3-Split W1 |
| `FF_Toilet_Wall_Front` | FF | Outer Envelope (North Facade) | $200.0\text{ mm}$ | $1219.2\text{ mm}$ | $3048.0\text{ mm}$ | $0.743\text{ m}^3$ | Flush with North front facade ($Y = 0.0\text{ mm}$) |
| `FF_Bedroom_Wall_North` | FF | Inner Partition (Living / Bed) | $100.0\text{ mm}$ | $3048.0\text{ mm}$ | $3048.0\text{ mm}$ | $0.734\text{ m}^3$ | Aligned at $Y \in [4526.0, 4626.0]$; cutout for D2 ($914 \times 2134\text{ mm}$) |
| `FF_Bedroom_Wall_East` | FF | Inner Partition (Bed / Kit Spine) | $100.0\text{ mm}$ | $3048.0\text{ mm}$ | $3048.0\text{ mm}$ | $0.929\text{ m}^3$ | Aligned at $X \in [1935.2, 2035.2]$; single structural divider for Bedroom & open Kitchen |
| `FF_Living_Room_Wall_Main_Door` | FF | Inner Partition (Balcony / Living) | $100.0\text{ mm}$ | $1514.5\text{ mm}$ | $3048.0\text{ mm}$ | $0.252\text{ m}^3$ | Aligned at $Y \in [1714.5, 1814.5]$; ties flush to East wall ($X = 200$) & Stair wall ($X = 1714.5$); Balcony door |
| `FF_Wall_Stair_SE_SW` | FF | Inner Partition (Stair / Living) | $100.0\text{ mm}$ | $2057.2\text{ mm}$ | $3048.0\text{ mm}$ | $0.627\text{ m}^3$ | Aligned with Main Door wall line ($Y \in [1714.5, 1814.5]$); spans $X \in [1714.5, 3771.7]$ |
| `FF_Toilet_Wall_North` | FF | Inner Partition (Toilet North Door) | $100.0\text{ mm}$ | $1057.5\text{ mm}$ | $2133.6\text{ mm}$ | $0.068\text{ m}^3$ | Aligned to exact same $Y$-datum ($Y \in [1714.5, 1814.5]$); cutout for D4 ($750 \times 2100\text{ mm}$) |
| `FF_Toilet_Wall_East` | FF | Inner Partition (Toilet / Stair Lower) | $100.0\text{ mm}$ | $1814.5\text{ mm}$ | $2133.6\text{ mm}$ | $0.387\text{ m}^3$ | Aligned at $X \in [3771.7, 3871.7]$, $Y \in [0.0, 1814.5]$; clean $90^\circ$ flush corner |
| `FF_Toilet_Wall_East_Top` | FF | Inner Partition (Toilet / Stair Upper) | $100.0\text{ mm}$ | $1814.5\text{ mm}$ | $914.4\text{ mm}$ | $0.166\text{ m}^3$ | Parapet tier above door lintel capping toilet enclosure ($Y \in [0.0, 1814.5]$) |

---

## 3. First Floor Material Takeoff (BOQ)

### 3.1 AAC Masonry Volume & Block Counts

- **Total First Floor AAC Masonry Volume:** **$14.550\text{ m}^3$**
- **Outer Envelope ($200\text{ mm}$ Thick):**
  - Net Masonry Volume: $11.387\text{ m}^3$
  - Standard Block Section: $600 \times 200 \times 200\text{ mm}$ ($0.024\text{ m}^3$/unit)
  - Net Block Count: $475\text{ blocks}$
  - Gross Block Requirement (+5% cutting/wastage): **$499\text{ blocks}$**
- **Inner Partitions ($100\text{ mm}$ Thick):**
  - Net Masonry Volume: $3.163\text{ m}^3$
  - Standard Block Section: $600 \times 200 \times 100\text{ mm}$ ($0.012\text{ m}^3$/unit)
  - Net Block Count: $264\text{ blocks}$
  - Gross Block Requirement (+5% cutting/wastage): **$277\text{ blocks}$**

### 3.2 Mortar & Consumables
- **Joint Type:** Thin-Bed Polymer AAC Block Jointing Adhesive ($3\text{ to }4\text{ mm}$ joint thickness).
- **Consumption Rate:** $65\text{ kg per m}^3$ of AAC masonry.
- **Adhesive Mortar Requirement:** $14.550 \times 65 = 946\text{ kg}$ (**24 bags of 40 kg each**).
- **RCC Seismic Bands (FF):** Continuous lintel and sill tie bands ($200\text{ mm}$ and $100\text{ mm}$ wide) integrated at $Z = 5001.8\text{ mm}$ (Sill) and $Z = 6201.8\text{ mm}$ (Lintel).

---

## 4. Total G+1 Building Masonry Takeoff Summary

| Category | Ground Floor | First Floor | Combined Building Total |
| :--- | :--- | :--- | :--- |
| **$200\text{ mm}$ Outer Envelope Volume** | $12.038\text{ m}^3$ | $11.387\text{ m}^3$ | **$23.425\text{ m}^3$** |
| **$200\text{ mm}$ AAC Blocks ($600 \times 200 \times 200\text{ mm}$)** | $527\text{ units}$ | $499\text{ units}$ | **$1026\text{ units}$** |
| **$100\text{ mm}$ Inner Partition Volume** | $3.152\text{ m}^3$ | $3.163\text{ m}^3$ | **$6.315\text{ m}^3$** |
| **$100\text{ mm}$ AAC Blocks ($600 \times 200 \times 100\text{ mm}$)** | $276\text{ units}$ | $277\text{ units}$ | **$553\text{ units}$** |
| **Total AAC Masonry Volume** | $15.190\text{ m}^3$ | $14.550\text{ m}^3$ | **$29.740\text{ m}^3$** |
| **Thin-Bed Adhesive Mortar (40 kg Bags)** | $25\text{ bags}$ | $24\text{ bags}$ | **$49\text{ bags}$ ($1933\text{ kg}$)** |
| **AAC Total Dead Weight ($\approx 650\text{ kg/m}^3$)** | $9.87\text{ tonnes}$ | $9.46\text{ tonnes}$ | **$19.33\text{ tonnes}$** |
| **Equivalent Red Clay Brick Weight ($\approx 1900\text{ kg/m}^3$)** | $28.86\text{ tonnes}$ | $27.65\text{ tonnes}$ | **$56.51\text{ tonnes}$** |
| **Total Dead Load Reduction Achieved** | **$18.99\text{ tonnes}$ (65.8%)** | **$18.19\text{ tonnes}$ (65.8%)** | **$37.18\text{ tonnes}$ (65.8%)** |
