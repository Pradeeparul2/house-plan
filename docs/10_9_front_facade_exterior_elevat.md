## 9. Front Facade & Exterior Elevation Design

The front elevation faithfully reproduces the high-contrast, modern architectural language of [`IMG_0379.JPG`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/references/IMG_0379.JPG):

```
       +-------------------------------------------------------------+
       |   TERRACE SAFETY RAILING (SS 304, H = 900 mm)               |
       |=============================================================| <--- White Drip Cornice
       |   ROOFLINE FASCIA BAND (Dark Charcoal Slate, H = 150 mm)    |
       +--------------------+-------------------+--------------------+
       |  WHITE BLOCK       |  OPEN STAIRWELL   |  TOILET VENTILATOR |
       |  ARCHITECTURAL     |  WITH SS RAILING  |  WINDOW            |
       |  SURROUND          |                   |                    |
       |  [Warm Peach Wall] |-------------------|                    |
       |  SINGLE 5-PANEL    |  STAIR NORTH WALL |                    |
       |  TEAK MAIN DOOR    |  [Louvered Niche] |                    |
       |--------------------+-------------------+--------------------+
       |  SITOUT SS & DARK  |  SOLID PLINTH     |  SOLID PLINTH      |
       |  CHARCOAL GATE     |  (Washer Enclosed)|                    |
       +====================+===================+====================+
       |  RED ENTRANCE STEPS|  SUMP TANK (Blue) |  SEPTIC TANK(Brown)|
+------+--------------------+-------------------+--------------------+------+
|                            ROAD LEVEL                              |
+--------------------------------------------------------------------+
```

### 9.1 Detailed Facade Features Schedule

| Feature                      | FreeCAD Object Name                                      | Dimensions                                                                            | Material / Color                                                         | Architectural Significance                                                                                                        |
| :--------------------------- | :------------------------------------------------------- | :------------------------------------------------------------------------------------ | :----------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| **Main Entrance Door**       | `Main_Door`, `GF_Main_Door_Frame`, `GF_Main_Door_Handle` | $1050 \times 100 \times 2100\text{ mm}$ (Leaf: $910 \times 40 \times 2025\text{ mm}$) | Burmese Teakwood (`#5A331C`) + Brushed Chrome (`#D9E0E5`)                | Single entrance door with 5 horizontal recessed panels and sleek horizontal lever handle matching reference photo `IMG_0379.JPG`. |
| **Main Door White Surround** | `GF_Main_Door_Architectural_Surround`                    | $1240 \times 25 \times 2270\text{ mm}$                                                | Crisp Architectural White (`#F8FAFC`)                                    | 17 rusticated quoin blocks with horizontal reveals framing the entrance door.                                                     |
| **Entrance Accent Wall**     | `Living_Room_Wall_Main_Door`                             | $1485.9 \times 228.6 \times 3048\text{ mm}$                                           | Warm Terracotta-Peach (`#E8B294`)                                        | Provides high-contrast backdrop for the white block surround.                                                                     |
| **Louvered Feature Niche**   | `GF_Stair_Wall_Niche_Frame`, `GF_Stair_Wall_Louvers`     | Frame: $880 \times 620\text{ mm}$; 5 Louvers: $780 \times 28\text{ mm}$               | Frame: White (`#F8FAFC`); Louvers: Dark Charcoal (`#2B2F38`)             | Architectural focal point on the staircase wall matching the elevation louvers.                                                   |
| **Roofline Fascia Band**     | `GF_Roofline_Fascia_Band`                                | $5069.2 \times 35 \times 150\text{ mm}$                                               | Dark Slate Charcoal (`#383C45`)                                          | Bold horizontal architectural beam defining the ground floor roofline.                                                            |
| **Roofline Drip Cornice**    | `GF_Roofline_Drip_Cornice`                               | $5089.2 \times 50 \times 30\text{ mm}$                                                | Crisp Architectural White (`#F8FAFC`)                                    | Cantilevered projection preventing rainwater staining on the facade.                                                              |
| **Sitout Safety Gate**       | `GF_Sitout_Gate_Group` (8 objects)                       | $1386 \times 50 \times 1000\text{ mm}$                                                | Satin SS 304 (`#D0D5DD`) + Dark Charcoal (`#282C34`) + Brass (`#D4AF37`) | Double-leaf swing gate with 6 tubes, charcoal mid-accent panel, aldrop, and pull handles.                                         |
| **Terrace Safety Railing**   | `GF_Terrace_Front_Railing`                               | $1900 \times 35 \times 900\text{ mm}$                                                 | Polished SS 304 (`#DCE1E7`)                                              | Front terrace balustrade with $\varnothing 50\text{ mm}$ top rail and 3 horizontal tubes.                                         |
| **Corner Architectural Fin** | `Col_NE_Corner`                                          | $228.6 \times 228.6 \times 3048\text{ mm}$                                            | Crisp Architectural White (`#F8FAFC`)                                    | Vertical white architectural fin anchoring the left facade edge.                                                                  |

### 9.2 Enhanced Contemporary Elevation & Feature Architecture

To match the refined contemporary architectural aesthetic of [`IMG_0379.JPG`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/references/IMG_0379.JPG), five major elevation features were integrated into the 3D model:

| Feature Area                                       | FreeCAD Objects & Containers                                                         | Dimensions & Engineering Specs                                                          | Finish & Materials                                                                          | Architectural & Functional Purpose                                                                                                                                 |
| :------------------------------------------------- | :----------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Canopy Warm Teak Soffits**                       | `GF_Entrance_Canopy_Wood_Soffit`, `FF_Balcony_Canopy_Wood_Soffit`                    | $1485.9 \times 600 \times 12\text{ mm}$ ($Z = 3036\text{ mm}$ & $Z = 7123.4\text{ mm}$) | Natural Golden Burmese Teak (`#8A5A36`, $\text{RGB}: 0.54, 0.35, 0.21$)                     | Warm wood ceiling panels under GF entrance and FF balcony canopies, introducing natural organic texture into the modern facade.                                    |
| **Flush Recessed Canopy Downlights**               | `GF_Canopy_Spotlight_1` to `_4`, `FF_Balcony_Spotlight_1` to `_4` (8 total)          | $\varnothing 75\text{ mm}$ trim, $50\text{ mm}$ depth, spaced $370\text{ mm}$ on center | Matt White Trim with $3000\text{K}$ Warm LED Core (`#FFE0A0`, 5W COB)                       | IP65 weather-sealed downlights casting a welcoming warm ambient wash over the entrance steps and balcony floor at dusk.                                            |
| **Equalized Canopy Overhang Band**                 | `GF_Stair_North_Canopy_Slab`, `GF_Roofline_Fascia_Band`, `GF_Roofline_Drip_Cornice`  | Projection: $600\text{ mm}$ ($Y \in [-600, 0]$), Fascia: $H = 150\text{ mm}$            | Dark Slate Charcoal (`#383C45`) with Crisp White Drip Cornice (`#F8FAFC`)                   | Equalized the Stair canopy overhang from $450\text{ mm}$ to $600\text{ mm}$, forming a continuous, unbroken, flush horizontal band across the entire front facade. |
| **Balcony Linear Planter Box**                     | `FF_Balcony_Planter_Group` (`Planter_Box`, `Drip_Rim`, `Soil`, `Cascading_Greenery`) | $1485.9 \times 250 \times 350\text{ mm}$ ($Z = 4087.4$ to $4437.4\text{ mm}$)           | Charcoal Planter (`#262930`), White Drip Rim (`#F8FAFC`), Lush Emerald Greenery (`#2D7A42`) | Linear parapet planter with internal waterproofing membrane and cascading creeping fig / English ivy softening the geometric masonry.                              |
| **Horizontal Groove Feature Wall Cladding**        | `FF_Front_Groove_Feature_Wall_Group` (`Groove_Slats`, `Reveal_Infill`)               | $1485.9 \times 40 \times 3048\text{ mm}$ ($X \in [3543.3, 5029.2]$, 28 Slats)           | Dark Charcoal Slats (`#2B2F38`) with Crisp White Reveals (`#F8FAFC`)                        | High-contrast horizontal cladding slats ($160\text{ mm}$ width, $25\text{ mm}$ reveal groove) wrapping the outer stair/toilet tower matching `IMG_0379.JPG`.       |
| **Rooftop Cantilevered Pergola Trellis**           | `Rooftop_Pergola_Trellis_Group` (4 Trellis Beams)                                    | 4 Beams: $75 \times 150 \times 1800\text{ mm}$, spaced $450\text{ mm}$ c/c              | Structural Architectural Charcoal Aluminum (`#2D3139`)                                      | Cantilevered $750\text{ mm}$ beyond the front terrace parapet with $45^\circ$ beveled tips, crowning the building with modern resort-style verticality.            |
| **Flamed Granite Plinth Steps with Floating LEDs** | `FF_Plinth_Floating_Steps_Group` (3 Steps + Reveals)                                 | Treads: $1485.9 \times 300 \times 30\text{ mm}$, Risers: $152.4\text{ mm}$              | Saddle Grey Flamed Granite (`#3A3D40`) + White Risers + Warm LED Cove (`#FFE0A0`)           | $30\text{ mm}$ bullnosed granite treads with $20\text{ mm}$ concealed cove reveals housing IP67 warm white LED linear ribbons for a weightless floating look.      |

---
