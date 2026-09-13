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

### 59.2 Substructure Component Inventory (8-Column Standardized System)

All 8 active column locations (C1–C8) are reinforced with dedicated three-tier load transfer elements (Refer to Section 75):

1. **PCC Blinding Beds (`PCC_Blinding_Layer_Group`):**
   * 8 Plain Cement Concrete (1:4:8, M7.5) pads ($100\text{ mm}$ thickness, $Z \in [-1600, -1500]\text{ mm}$).
   * Standardized pad size: $1600 \times 1528 \times 100\text{ mm}$ (`PCC_N8_N8_C1` through `PCC_N8_N8_C12`), projecting $50\text{ mm}$ beyond footing perimeters.
2. **RCC Isolated Footings (`Isolated_Footings_Group`):**
   * 8 Reinforced Cement Concrete (M25) pads ($400\text{ mm}$ depth, $Z \in [-1500, -1100]\text{ mm}$).
   * Standardized footing pad dimensions: $1500 \times 1428 \times 400\text{ mm}$ (`Footing_N8_C1` through `Footing_N8_C12`).
   * Engineered for $SBC = 200\text{ kN/m}^2$, safely transmitting two-storey axial and bending moment loads.
3. **RCC Column Pedestals (`Column_Pedestals_Group`):**
   * 8 RCC column pedestals ($230 \times 300\text{ mm}$ cross-section, $1814.4\text{ mm}$ vertical height, $Z \in [-1200, +614.4]\text{ mm}$).
   * Pedestals `Pedestal_C1`, `Pedestal_C_SP`, `Pedestal_C2`, `Pedestal_C13`, `Pedestal_C4`, `Pedestal_C9`, `Pedestal_C10`, `Pedestal_C12`.
4. **Plinth Beam Tie Network (`GF_Plinth_Beams`):**
   * 9 interconnected RCC tie beams ($230 \times 300\text{ mm}$ / $230 \times 375\text{ mm}$, $Z \in [614.4, 914.4]\text{ mm}$).
   * Features `PB_LIVING_Primary` ($230 \times 300\text{ mm}$, $L = 5029.2\text{ mm}$) and upsized `PB1_Rear_South` ($230 \times 375\text{ mm}$).

---

### 59.3 Contractor Bill of Quantities (BOQ) Schedule (8-Column Active Frame)

| Item No. | Work Description | Mix / Grade | Geometric Volume ($\text{m}^3$) | Imperial Volume ($\text{cu.ft}$) | Standard Billing Unit |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.0** | **Earthwork Excavation** in 8 footing pits ($-1.6\text{ m}$), Sump ($2.1\text{ m}$), Septic pit ($2.1\text{ m}$) & pipe trench | Soil / Moorum | $55.55\text{ m}^3$ | $1,961.7\text{ cu.ft}$ | $19.62\text{ Brass}$ |
| **2.0** | **PCC Blinding Bed** under 8 isolated footings ($1.96\text{ m}^3$) + Sump ($0.22\text{ m}^3$) + Septic ($0.14\text{ m}^3$) | PCC 1:4:8 (M7.5) | $2.32\text{ m}^3$ | $81.9\text{ cu.ft}$ | $2.32\text{ m}^3$ |
| **3.0** | **RCC Isolated Footing Pads** ($1500 \times 1428 \times 400\text{ mm}$, 8 units) | RCC M25 | $6.86\text{ m}^3$ | $242.3\text{ cu.ft}$ | $6.86\text{ m}^3$ |
| **4.0** | **RCC Substructure Column Pedestals** ($230 \times 300\text{ mm} \times 1814.4\text{ mm}$, 8 stubs) | RCC M25 | $1.00\text{ m}^3$ | $35.3\text{ cu.ft}$ | $1.00\text{ m}^3$ |
| **5.0** | **RCC Plinth Tie Beams** (PB1 + `PB_LIVING_Primary` + PB2, 9 beams) | RCC M25 | $2.98\text{ m}^3$ | $105.2\text{ cu.ft}$ | $2.98\text{ m}^3$ |
| **—** | **SUBTOTAL SUBSTRUCTURE RCC CONCRETE** (Items 3 + 4 + 5) | **RCC M25** | **$10.84\text{ m}^3$** | **$382.8\text{ cu.ft}$** | **$10.84\text{ m}^3$** |

---

### 59.4 Document Verification & Integrity

* **Master Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)
* **Total Objects in Document:** 537 objects (42 new substructure elements), 0 errors, 100% valid manifold solids.
* **Document Root Organization:** Consolidated under `Substructure_Foundation_Group`, `Ground_Floor_Group`, `First_Floor_Group`, `Master_Rooftop_Terrace_Group`, and `Page_Ground_Floor_Plan`.
* **Timestamped Backup:** Saved to [`backups/HomeConstruction_backup_before_footings.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/backups/HomeConstruction_backup_before_footings.FCStd).

---
