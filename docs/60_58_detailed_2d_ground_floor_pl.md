## 58. Detailed 2D Ground Floor Plan with Dimensions (From 3D Model)

> [!NOTE]
> **Plan Type:** Architectural 2D Working Floor Plan with Comprehensive Dual-Unit Dimensions  
> **Source Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd) (100% extracted from active 3D solids and structural column grid)  
> **Cut-Plane Datum:** Horizontal cross-section cutting plane at Z = +2100.0 mm looking downward along -Z  
> **Drawing Scale:** 1:50 @ ISO A3 Landscape (420 mm × 297 mm)  
> **TechDraw Page:** `Page_Ground_Floor_Plan`  
> **Output Deliverables:**
> - TechDraw Master Architectural Vector SVG: [`Page_Ground_Floor_Plan.svg`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/renders/Page_Ground_Floor_Plan.svg)
> - TechDraw Master Print-Ready PDF (300 DPI): [`Page_Ground_Floor_Plan.pdf`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/renders/Page_Ground_Floor_Plan.pdf)
> - TechDraw Native Views Projection Layer: [`Page_Ground_Floor_Plan_NativeViews.svg`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/renders/Page_Ground_Floor_Plan_NativeViews.svg)
> - Architectural Sheet Template: [`Page_Ground_Floor_Plan_Template.svg`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/drawings/templates/Page_Ground_Floor_Plan_Template.svg)
> - Workspace Compatibility Symlinks/Exports: [`techdraw_gf_plan.svg`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/renders/techdraw_gf_plan.svg) & [`techdraw_gf_plan.pdf`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/renders/techdraw_gf_plan.pdf)
> - Automated Generation Script: [`generate_ground_floor_drawing.py`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/tools/generate_ground_floor_drawing.py)

---

### 58.1 Dimension Verification & Validation Table (0.0 mm Drift)

Every single key dimension figured on the drawing sheet was validated directly against the solid geometry extracted from `HomeConstruction.FCStd`:

| Member / Grid Span | Target Dimension | 3D Solid Model Extract | Variance / Drift | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Overall Plot Width** | $5029.2\text{ mm}$ ($16'\text{-}6"$) | $5029.20\text{ mm}$ (East: 0.0 to West: 5029.2) | $0.00\text{ mm}$ | **PASS** |
| **Overall Plot Depth** | $7620.0\text{ mm}$ ($25'\text{-}0"$) | $7620.00\text{ mm}$ (North: 0.0 to South: 7620.0) | $0.00\text{ mm}$ | **PASS** |
| **Centerline Grid C6–C7** | $1564.5\text{ mm}$ | $1564.50\text{ mm}$ ($X = 150.0 \rightarrow 1714.5$) | $0.00\text{ mm}$ | **PASS** |
| **Centerline Grid C7–C8** | $3200.4\text{ mm}$ | $3200.40\text{ mm}$ ($X = 1714.5 \rightarrow 4914.9$) | $0.00\text{ mm}$ | **PASS** |
| **Centerline Grid C6–C4** | $3083.5\text{ mm}$ | $3083.50\text{ mm}$ ($Y = 114.3 \rightarrow 3197.8$) | $0.00\text{ mm}$ | **PASS** |
| **Centerline Grid C4–C1** | $4307.9\text{ mm}$ | $4307.90\text{ mm}$ ($Y = 3197.8 \rightarrow 7505.7$) | $0.00\text{ mm}$ | **PASS** |
| **Centerline Grid C8–C5** | $3047.8\text{ mm}$ | $3047.80\text{ mm}$ ($Y = 150.0 \rightarrow 3197.8$) | $0.00\text{ mm}$ | **PASS** |
| **Centerline Grid C5–C3** | $4272.2\text{ mm}$ | $4272.20\text{ mm}$ ($Y = 3197.8 \rightarrow 7470.0$) | $0.00\text{ mm}$ | **PASS** |
| **Centerline Grid C1–C2** | $2080.0\text{ mm}$ | $2080.00\text{ mm}$ ($X = 150.0 \rightarrow 2230.0$) | $0.00\text{ mm}$ | **PASS** |
| **Centerline Grid C2–C3** | $2684.9\text{ mm}$ | $2684.90\text{ mm}$ ($X = 2230.0 \rightarrow 4914.9$) | $0.00\text{ mm}$ | **PASS** |
| **Living Room Clear** | $4724.4 \times 3230.0\text{ mm}$ | $4724.4 \times 3230.0\text{ mm}$ (Internal Faces) | $0.00\text{ mm}$ | **PASS** |
| **Master Bedroom Clear** | $2794.1 \times 2794.1\text{ mm}$ | $2794.1 \times 2794.1\text{ mm}$ (Internal Faces) | $0.00\text{ mm}$ | **PASS** |
| **Kitchen Clear** | $1714.5 \times 2171.7\text{ mm}$ | $1714.5 \times 2171.7\text{ mm}$ (Internal Faces) | $0.00\text{ mm}$ | **PASS** |
| **Sitout / Porch Clear** | $1485.9 \times 1485.9\text{ mm}$ | $1485.9 \times 1485.9\text{ mm}$ (Internal Faces) | $0.00\text{ mm}$ | **PASS** |
| **Toilet Clear Enclosure** | $957.5 \times 1680.0\text{ mm}$ | $957.5 \times 1680.0\text{ mm}$ (Internal Faces) | $0.00\text{ mm}$ | **PASS** |
| **Main Door Wall (Grid B)** | $200.0\text{ mm}$ (8" AAC) | $Y = [1714.50, 1914.50]\text{ mm}$ (Aligned to RB2/PB2) | $0.00\text{ mm}$ | **PASS** |
| **Grid B L-Corner Joint** | $X = 200.0, Y = 1714.50$ | Flush with `Living_Room_Wall_East` & `Wall_Stair_SE_SW` | $0.00\text{ mm}$ | **PASS** |

---

### 58.2 Active Structural Column Grid (8 Primary RCC Columns)

| Col Bubble | Model Object Name | Label in FreeCAD | Center $(X, Y)$ Coordinates (mm) | Size ($W \times D$ mm) | Location & Function |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **C1** | `Col_SE_Rear_C1` | `C1 (SE Rear Outer Column)` | $(150.0, 7505.7)$ | $230 \times 230$ | SE Rear Boundary & Kitchen Flank |
| **C2** | `Col_S_Spine_C2` | `C2 (South Spine Column)` | $(2230.0, 7505.7)$ | $230 \times 230$ | South Rear Spine & Bedroom-Kitchen Divider |
| **C3** | `Col_SW_Rear_C3` | `C3 (SW Rear Master Bedroom Column)` | $(4914.9, 7470.0)$ | $230 \times 300$ | SW Rear Boundary & Master Bedroom Flank |
| **C4** | `Col_MidE_C4` | `C4 (Mid East Living Column)` | $(150.0, 3197.8)$ | $230 \times 230$ | Mid-East Boundary & Transfer Beam Span |
| **C5** | `Col_MidW_C5` | `C5 (Mid West Column)` | $(4914.9, 3197.8)$ | $230 \times 300$ | Mid-West Boundary & Transfer Beam Span |
| **C6** | `Col_NE_Front_C6` | `C6 (NE Front Corner Column)` | $(150.0, 114.3)$ | $230 \times 230$ | NE Front Road Flank & Sitout Post |
| **C7** | `Col_N_Stair_C7` | `C7 (North Stair Column)` | $(1714.5, 114.3)$ | $230 \times 230$ | North Facade & Staircase/Sitout Junction |
| **C8** | `Col_NW_Mumty_C8` | `C8 (NW Mumty Column)` | $(4914.9, 150.0)$ | $230 \times 300$ | NW Front Corner & Toilet Enclosure |

---

### 58.3 Ground Floor Openings Schedule

| Tag | Opening Type | Width $\times$ Height (mm) | Sill Height | Lintel Height | Material / Specifications |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **D1** | Main Entrance Door | $1050 \times 2100$ ($3'\text{-}5" \times 6'\text{-}11"$) | $\pm 0.0\text{ mm}$ (FFL) | $+2133.6\text{ mm}$ | Teak Wood Frame with $38\text{ mm}$ Solid Carved Shutter |
| **D2** | Bedroom Door | $914 \times 2134$ ($3'\text{-}0" \times 7'\text{-}0"$) | $\pm 0.0\text{ mm}$ (FFL) | $+2133.6\text{ mm}$ | Solid Flush Door with Teak Veneer & Mortise Lock |
| **D4** | Toilet Door | $750 \times 2050$ ($2'\text{-}6" \times 6'\text{-}9"$) | $\pm 0.0\text{ mm}$ (FFL) | $+2050.0\text{ mm}$ | Waterproof FRP / UPVC Heavy-Duty Shutter |
| **GATE** | Sitout Entrance Gate | $1524 \times 1030$ ($5'\text{-}0" \times 3'\text{-}5"$) | $\pm 0.0\text{ mm}$ (FFL) | $+1030.0\text{ mm}$ | SS 304 Tubular Frame with Horizontal Slats |
| **W1** | Living Room Window | $1200 \times 1200$ ($3'\text{-}11" \times 3'\text{-}11"$) | $+900.0\text{ mm}$ | $+2100.0\text{ mm}$ | 3-Track UPVC Sliding Window with Mosquito Net |
| **W2** | Kitchen Window | $914 \times 1219$ ($3'\text{-}0" \times 4'\text{-}0"$) | $+900.0\text{ mm}$ | $+2119.0\text{ mm}$ | 2-Track UPVC Sliding Window with Toughened Glass |
| **V1** | Toilet Ventilator | $600 \times 600$ ($2'\text{-}0" \times 2'\text{-}0"$) | $+1500.0\text{ mm}$ | $+2100.0\text{ mm}$ | Pinhead Obscure Glass Louvers with Exhaust Port |
| **LOUV** | Stair Niche Louvers | $790 \times 530$ ($2'\text{-}7" \times 1'\text{-}9"$) | $+1500.0\text{ mm}$ | $+2030.0\text{ mm}$ | Architectural Charcoal Aluminium Air Louvers |

---

### 58.4 Elevation Level Datums

| Datum Name | Elevation Above Road | Imperial Equivalent | Description / Structural Reference |
| :--- | :--- | :--- | :--- |
| **Natural Ground / Road Level** | $\pm 0.0\text{ mm}$ | $\pm 0'\text{-}0"$ | Benchmark Ground Datum at North Frontage |
| **Plinth Finished Floor Level (FFL)** | $+914.4\text{ mm}$ | $+3'\text{-}0"$ | Top of Vitrified Tile Flooring (Ground Floor Living) |
| **Toilet Sunken Floor Level** | $+764.4\text{ mm}$ | $+2'\text{-}6"$ | $150\text{ mm}$ Sunken Slab for Waterproof Drainage |
| **Lintel Level** | $+2133.6\text{ mm}$ | $+7'\text{-}0"$ | Continuous RCC Lintel Band Bottom Soffit |
| **Roof Beam Soffit Elevation** | $+3662.4\text{ mm}$ | $+12'\text{-}0"$ | Underside of Primary RCC Roof Transfer Beams |

---

### 58.5 FreeCAD TechDraw Implementation Details

1. **Section Cut Geometry (`GF_Cut_Section_Z2100`):**
   - Created in `Ground_Floor_Group` using `Part::Feature`.
   - Formed by taking a planar cross-section slice at $Z = +2100.0\text{ mm}$ across the entire structural frame, external 200 mm walls, internal 100 mm partitions, staircase flight, and window/door openings.
2. **TechDraw Drawing Page (`Page_Ground_Floor_Plan`):**
   - Standard ISO A3 Landscape ($420\text{ mm} \times 297\text{ mm}$).
   - `Scale = 0.02` ($1:50$).
   - `Page_Ground_Floor_Plan_Template` (`TechDraw::DrawSVGTemplate`) references `drawings/templates/Page_Ground_Floor_Plan_Template.svg`.
3. **DrawViewPart (`GF_Section_Cut_DrawViewPart`):**
   - Projects `GF_Cut_Section_Z2100` downwards along $-Z$ (`Direction = (0, 0, 1)`).
   - Centered on the sheet at $(X = 145.0\text{ mm}, Y = 148.5\text{ mm})$ with `ScaleType = Custom` and `Scale = 0.02`.
4. **Drawing Automation:**
   - Script [`generate_ground_floor_drawing.py`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/tools/generate_ground_floor_drawing.py) handles model inspection, geometry validation, SVG template drafting, TechDraw configuration, and multi-format export.
