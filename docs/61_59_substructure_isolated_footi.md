## 59. Substructure Isolated Footings, Column Pedestals & Plinth Beam System (BOQ & Construction Detailing)

> [!NOTE]
> **System Title:** Foundation & Substructure Structural System (Ground Level to $-1.60\text{ m}$)  
> **Source Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Root Container:** `Substructure_Foundation_Group`  
> **Structural Compliance:** IS 456:2000 (Plain and Reinforced Concrete), IS 1904 (Design and Construction of Foundations in Soils)  
> **Datum Levels:** Natural Ground Level ($\text{NGL} = \pm 0.000\text{ m}$), Plinth Top ($\text{PT} = +0.914\text{ m} / +3'\text{-}0"$), Footing Base ($-1.500\text{ m}$), PCC Bed Base ($-1.600\text{ m}$).

### 59.1 Substructure Visual Portfolio

```carousel
![Substructure Structural Skeleton & Isolated Footings](c:\Users\prade\OneDrive\Desktop\home plan\renders\substructure_isolated_isometric.png)
<!-- slide -->
![Substructure Front Elevation Depth Profile](c:\Users\prade\OneDrive\Desktop\home plan\renders\substructure_front_elevation.png)
<!-- slide -->
![Full Building X-Ray with Foundation Anchor](c:\Users\prade\OneDrive\Desktop\home plan\renders\substructure_full_building_xray.png)
<!-- slide -->
![Substructure to Plinth Transition Closeup](c:\Users\prade\OneDrive\Desktop\home plan\renders\substructure_ground_transition_closeup.png)
```

---

### 59.2 Substructure Component Inventory (42 Objects)

All 14 column locations are reinforced with dedicated three-tier load transfer elements:

1. **PCC Blinding Beds (`PCC_Blinding_Layer_Group`):**
   * 14 Plain Cement Concrete (1:4:8, M7.5) pads ($100\text{ mm}$ thickness, $Z \in [-1600, -1500]\text{ mm}$).
   * Extends $75\text{ mm}$ beyond footing perimeter on all free faces.
2. **RCC Isolated Footings (`Isolated_Footings_Group`):**
   * 14 Reinforced Cement Concrete (M25) pads ($400\text{ mm}$ depth, $Z \in [-1500, -1100]\text{ mm}$).
   * Boundary and corner footings (C9, C10, C11, C12, C5, C8, C13, C4, C1, C_SP, C2) configured within the plot envelope (eccentric flush edges).
   * Core interior columns (C6, C7, C14) provided with concentric $1200 \times 1200\text{ mm}$ footings.
3. **RCC Column Pedestals (`Column_Pedestals_Group`):**
   * 14 RCC column stubs ($230 \times 230\text{ mm}$, $1714.4\text{ mm}$ vertical span, $Z \in [-1100, +614.4]\text{ mm}$).
   * Transmits vertical column forces directly from plinth beams to the footing pads.
4. **Plinth Beam Tie Network (`GF_Plinth_Beams`):**
   * 10 interconnected RCC tie beams ($230 \times 300\text{ mm}$, $Z \in [614.4, 914.4]\text{ mm}$).
   * Forms a monolithic closed-loop ring tying all 14 column tops at finished plinth level.

---

### 59.3 Contractor Bill of Quantities (BOQ) Schedule (Calculated from 3D Geometry)

| Item No. | Work Description | Mix / Grade | Geometric Volume ($\text{m}^3$) | Imperial Volume ($\text{cu.ft}$) | Standard Billing Unit |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.0** | **Earthwork Excavation** in foundation trenches and pits down to $-1.6\text{ m}$, including sump ($2.2\text{m}$) and septic pits ($1.6\text{m}$) | Soil / Moorum | $52.06\text{ m}^3$ | $1,838.5\text{ cu.ft}$ | $18.38\text{ Brass}$ |
| **2.0** | **PCC Blinding Bed** under 14 isolated footings ($100\text{ mm}$ thick) | PCC 1:4:8 (M7.5) | $1.885\text{ m}^3$ | $66.6\text{ cu.ft}$ | $1.89\text{ m}^3$ |
| **3.0** | **RCC Isolated Footing Pads** ($400\text{ mm}$ depth, 14 units) | RCC M25 | $6.168\text{ m}^3$ | $217.8\text{ cu.ft}$ | $6.17\text{ m}^3$ |
| **4.0** | **RCC Substructure Column Pedestals** ($230 \times 230\text{ mm}$, 14 stubs) | RCC M25 | $1.254\text{ m}^3$ | $44.3\text{ cu.ft}$ | $1.25\text{ m}^3$ |
| **5.0** | **RCC Plinth Tie Beams (PB1 & PB2)** ($230 \times 300\text{ mm}$, 10 beams) | RCC M25 | $2.845\text{ m}^3$ | $100.5\text{ cu.ft}$ | $2.85\text{ m}^3$ |
| **—** | **SUBTOTAL SUBSTRUCTURE RCC CONCRETE** (Items 3 + 4 + 5) | **RCC M25** | **$10.268\text{ m}^3$** | **$362.6\text{ cu.ft}$** | **$10.27\text{ m}^3$** |

---

### 59.4 Document Verification & Integrity

* **Master Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)
* **Total Objects in Document:** 537 objects (42 new substructure elements), 0 errors, 100% valid manifold solids.
* **Document Root Organization:** Consolidated under `Substructure_Foundation_Group`, `Ground_Floor_Group`, `First_Floor_Group`, `Master_Rooftop_Terrace_Group`, and `Page_Ground_Floor_Plan`.
* **Timestamped Backup:** Saved to [`backups/HomeConstruction_backup_before_footings.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/backups/HomeConstruction_backup_before_footings.FCStd).

---
