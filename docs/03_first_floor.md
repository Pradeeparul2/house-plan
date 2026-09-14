# First Floor AAC Block Masonry Specification & Wall Schedule

> [!NOTE]
> **Discipline:** Architectural & Structural Masonry Engineering (First Floor Expansion)  
> **Authoritative BIM Source:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Material Standard:** Autoclaved Aerated Concrete (AAC) Blocks per IS 2185 (Part 3): 1984  
> **Joint Adhesive:** Thin-Bed High-Strength Polymer-Modified AAC Block Adhesive (ASTM C1660 / IS 15477)  
> **Execution Baseline:** First Floor Finished Level $Z = +4087.4\text{ mm}$ to Roof Beam Soffit $Z = +6835.4\text{ mm}$ ($H = 2748.0\text{ mm}$ / $9'\text{-}0.2"$ clear height, eliminating 300 mm vertical clash penetrations with FF roof beams).

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
| `FF_Bedroom_Wall_South` | FF | Outer Envelope (Rear South) | $200.0\text{ mm}$ | $3048.0\text{ mm}$ | $2748.0\text{ mm}$ | $1.675\text{ m}^3$ | Flush with South plot boundary ($Y = 7620.0\text{ mm}$); terminates at beam soffit ($Z = 6835.4\text{ mm}$) |
| `FF_Kitchen_Wall_South` | FF | Outer Envelope (Rear South) | $200.0\text{ mm}$ | $1981.2\text{ mm}$ | $2748.0\text{ mm}$ | $1.089\text{ m}^3$ | Flush with South plot boundary ($Y = 7620.0\text{ mm}$); terminates at beam soffit ($Z = 6835.4\text{ mm}$) |
| `FF_Bedroom_Wall_West` | FF | Outer Envelope (West Boundary) | $200.0\text{ mm}$ | $3048.0\text{ mm}$ | $2748.0\text{ mm}$ | $1.675\text{ m}^3$ | Flush with West plot boundary ($X = 5029.2\text{ mm}$); terminates at beam soffit ($Z = 6835.4\text{ mm}$) |
| `FF_Living_Room_Wall_West` | FF | Outer Envelope (West Boundary) | $200.0\text{ mm}$ | $2857.5\text{ mm}$ | $2748.0\text{ mm}$ | $1.570\text{ m}^3$ | Flush with West plot boundary ($X = 5029.2\text{ mm}$); terminates at beam soffit ($Z = 6835.4\text{ mm}$) |
| `FF_Toilet_Wall_West` | FF | Outer Envelope (West Boundary) | $200.0\text{ mm}$ | $1714.5\text{ mm}$ | $2748.0\text{ mm}$ | $0.942\text{ m}^3$ | Flush with West plot boundary ($X = 5029.2\text{ mm}$); terminates at beam soffit ($Z = 6835.4\text{ mm}$) |
| `FF_Kitchen_Wall_East` | FF | Outer Envelope (East Boundary) | $200.0\text{ mm}$ | $2438.4\text{ mm}$ | $2748.0\text{ mm}$ | $1.105\text{ m}^3$ | Flush with East plot boundary ($X = 0.0\text{ mm}$); cutouts for W2 & Exhaust; beam soffit flush |
| `FF_Living_Room_Wall_East` | FF | Outer Envelope (East Boundary) | $200.0\text{ mm}$ | $3467.1\text{ mm}$ | $2748.0\text{ mm}$ | $1.618\text{ m}^3$ | Flush with East plot boundary ($X = 0.0\text{ mm}$); cutout for 3-Split W1; beam soffit flush |
| `FF_Toilet_Wall_Front` | FF | Outer Envelope (North Facade) | $200.0\text{ mm}$ | $1219.2\text{ mm}$ | $2748.0\text{ mm}$ | $0.670\text{ m}^3$ | Flush with North front facade ($Y = 0.0\text{ mm}$); cutout for V1; beam soffit flush |
| `FF_Living_Room_Wall_Main_Door` | FF | Outer Envelope (Balcony / Living) | **$200.0\text{ mm}$** (8″) | $1514.5\text{ mm}$ | $2748.0\text{ mm}$ | **$0.391\text{ m}^3$** | Aligned at $Y \in [1614.5, 1814.5]$; absorbs into Balcony interface preserving $3230\text{ mm}$ clear living depth; 220mm full-depth D1 cutout; beam soffit flush |
| `FF_Wall_Stair_SE_SW` | FF | Outer Envelope (Stair / Living) | **$200.0\text{ mm}$** (8″) | $2057.2\text{ mm}$ | $2748.0\text{ mm}$ | **$1.131\text{ m}^3$** | Aligned at $Y \in [1714.5, 1914.5]$; North face collinear with `FF_Toilet_Wall_North` along $Y = 1714.5\text{ mm}$; spans $X \in [1714.5, 3771.7]$; beam soffit flush |
| `FF_Bedroom_Wall_North` | FF | Inner Partition (Living / Bed) | $100.0\text{ mm}$ | $3048.0\text{ mm}$ | $2748.0\text{ mm}$ | $0.642\text{ m}^3$ | Aligned at $Y \in [4526.0, 4626.0]$; cutout for D2 ($914 \times 2134\text{ mm}$); beam soffit flush |
| `FF_Bedroom_Wall_East` | FF | Inner Partition (Bed / Kit Spine) | $100.0\text{ mm}$ | $3048.0\text{ mm}$ | $2748.0\text{ mm}$ | $0.838\text{ m}^3$ | Aligned at $X \in [1935.2, 2035.2]$; single structural divider for Bedroom & open Kitchen; beam soffit flush |
| `FF_Toilet_Wall_North` | FF | Inner Partition (Toilet North Door) | $100.0\text{ mm}$ | $1057.5\text{ mm}$ | $2133.6\text{ mm}$ | $0.068\text{ m}^3$ | Aligned to exact same $Y$-datum ($Y \in [1714.5, 1814.5]$); cutout for D4 ($750 \times 2100\text{ mm}$) |
| `FF_Toilet_Wall_East` | FF | Inner Partition (Toilet / Stair Lower) | $100.0\text{ mm}$ | $1814.5\text{ mm}$ | $2133.6\text{ mm}$ | $0.387\text{ m}^3$ | Aligned at $X \in [3771.7, 3871.7]$, $Y \in [0.0, 1814.5]$; clean $90^\circ$ flush corner |
| `FF_Toilet_Wall_East_Top` | FF | Inner Partition (Toilet / Stair Upper) | $100.0\text{ mm}$ | $1814.5\text{ mm}$ | **$614.4\text{ mm}$** | **$0.111\text{ m}^3$** | Parapet tier above door lintel capping toilet enclosure ($Z \in [6221.0, 6835.4\text{ mm}]$, 0 beam clash) |
| `FF_Kitchen_Wall_North_Drop` | FF | Lintel Spandrel / Drop Wall (Breakfast Counter) | **$100.0\text{ mm}$** (4″) | $1782.8\text{ mm}$ | **$464.4\text{ mm}$** | **$0.083\text{ m}^3$** | Aligned above `FF_Kitchen_Breakfast_Counter` centered at $Y = 5181.6\text{ mm}$; top datum $Z = 6835.4\text{ mm}$ (flush to beam soffit) |

---

## 3. First Floor Material Takeoff (BOQ)

### 3.1 AAC Masonry Volume & Block Counts

- **Total First Floor AAC Masonry Volume:** **$14.283\text{ m}^3$**
- **Outer Envelope ($200\text{ mm}$ Thick):**
  - Net Masonry Volume: $11.866\text{ m}^3$
  - Standard Block Section: $600 \times 200 \times 200\text{ mm}$ ($0.024\text{ m}^3$/unit)
  - Net Block Count: $495\text{ blocks}$
  - Gross Block Requirement (+5% cutting/wastage): **$520\text{ blocks}$**
- **Inner Partitions ($100\text{ mm}$ Thick):**
  - Net Masonry Volume: $2.417\text{ m}^3$
  - Standard Block Section: $600 \times 200 \times 100\text{ mm}$ ($0.012\text{ m}^3$/unit)
  - Net Block Count: $202\text{ blocks}$
  - Gross Block Requirement (+5% cutting/wastage): **$212\text{ blocks}$**

### 3.2 Mortar & Consumables
- **Joint Type:** Thin-Bed Polymer AAC Block Jointing Adhesive ($3\text{ to }4\text{ mm}$ joint thickness).
- **Consumption Rate:** $65\text{ kg per m}^3$ of AAC masonry.
- **Adhesive Mortar Requirement:** $14.283 \times 65 = 928.4\text{ kg}$ (**24 bags of 40 kg each**).
- **RCC Seismic Bands (FF):** Continuous lintel and sill tie bands ($200\text{ mm}$ and $100\text{ mm}$ wide) integrated at $Z = 5001.8\text{ mm}$ (Sill) and $Z = 6221.0\text{ mm}$ (Lintel).

---

## 4. Total G+1 Building Masonry Takeoff Summary

| Category | Ground Floor | First Floor | Combined Building Total |
| :--- | :--- | :--- | :--- |
| **$200\text{ mm}$ Outer Envelope Volume** | $12.038\text{ m}^3$ | $11.866\text{ m}^3$ | **$23.904\text{ m}^3$** |
| **$200\text{ mm}$ AAC Blocks ($600 \times 200 \times 200\text{ mm}$)** | $527\text{ units}$ | $520\text{ units}$ | **$1047\text{ units}$** |
| **$100\text{ mm}$ Inner Partition Volume** | $3.152\text{ m}^3$ | $2.417\text{ m}^3$ | **$5.569\text{ m}^3$** |
| **$100\text{ mm}$ AAC Blocks ($600 \times 200 \times 100\text{ mm}$)** | $276\text{ units}$ | $212\text{ units}$ | **$488\text{ units}$** |
| **Total AAC Masonry Volume** | $15.190\text{ m}^3$ | $14.283\text{ m}^3$ | **$29.473\text{ m}^3$** |
| **Thin-Bed Adhesive Mortar (40 kg Bags)** | $25\text{ bags}$ | $24\text{ bags}$ | **$49\text{ bags}$ ($1916\text{ kg}$)** |
| **AAC Total Dead Weight ($\approx 650\text{ kg/m}^3$)** | $9.87\text{ tonnes}$ | $9.28\text{ tonnes}$ | **$19.15\text{ tonnes}$** |
| **Equivalent Red Clay Brick Weight ($\approx 1900\text{ kg/m}^3$)** | $28.86\text{ tonnes}$ | $27.14\text{ tonnes}$ | **$56.00\text{ tonnes}$** |
| **Total Dead Load Reduction Achieved** | **$18.99\text{ tonnes}$ (65.8%)** | **$17.86\text{ tonnes}$ (65.8%)** | **$36.85\text{ tonnes}$ (65.8%)** |
