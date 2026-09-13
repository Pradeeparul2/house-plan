## 59. Substructure Isolated Footings, Column Pedestals & Plinth Beam System (BOQ & Construction Detailing)

> [!NOTE]
> **System Title:** Foundation & Substructure Structural System (Ground Level to $-1.70\text{ m}$)  
> **Source Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Root Container:** `Substructure_Foundation_Group`  
> **Structural Compliance:** IS 456:2000 (Plain and Reinforced Concrete), IS 1904 (Design and Construction of Foundations in Soils)  
> **Datum Levels:** Natural Ground Level ($\text{NGL} = \pm 0.000\text{ m}$), Plinth Top ($\text{PT} = +0.914\text{ m} / +3'\text{-}0"$), Pedestal Bottom Datum ($-1.200\text{ m}$), Footing Base ($-1.600\text{ m}$), PCC Bed Base ($-1.700\text{ m}$).
> **Plot Envelope Bounds:** Strict boundary $X \in [0.0, 5029.2\text{ mm}]$ ($16'\text{ }6''$) and $Y \in [0.0, 7619.8\text{ mm}]$ ($25'\text{ }0''$) with **zero boundary encroachments**.

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

### 59.2 Substructure Component Inventory (Zero-Encroachment Eccentric & Raft Foundation System)

All 8 active column locations (C1–C8) are reinforced with dedicated three-tier load transfer elements flush with site boundaries:

1. **PCC Blinding Beds (`PCC_Blinding_Layer_Group`):**
   * 8 Plain Cement Concrete (1:4:8, M7.5) blinding beds ($100\text{ mm}$ thickness, $Z \in [-1700, -1600]\text{ mm}$).
   * Set flush along exterior property boundaries with zero boundary overshoot ($X \ge 0.0, X \le 5029.2, Y \ge 0.0, Y \le 7619.8$).
   * Total PCC Blinding Volume: $1.54\text{ m}^3$ ($54.3\text{ cu.ft}$).
2. **RCC Foundation Pads & Combined Rafts (`Isolated_Footings_Group`):**
   * 8 Reinforced Cement Concrete (M25) pads/rafts ($400\text{ mm}$ thickness, $Z \in [-1600, -1200]\text{ mm}$).
   * **SE Corner (C1):** `Footing_N8_C1` ($1200 \times 1200 \times 400\text{ mm}$, eccentric, flush with East $X=0$ & South $Y=7619.8$).
   * **South Spine (C2):** `Footing_N8_C_SP` ($1400 \times 1200 \times 400\text{ mm}$, eccentric, flush with South $Y=7619.8$).
   * **SW Corner (C3):** `Footing_N8_C2` ($1200 \times 1200 \times 400\text{ mm}$, eccentric, flush with West $X=5029.2$ & South $Y=7619.8$).
   * **Mid-East (C4):** `Footing_N8_C13` ($1200 \times 1400 \times 400\text{ mm}$, eccentric, flush with East $X=0$).
   * **Mid-West (C5):** `Footing_N8_C4` ($1200 \times 1400 \times 400\text{ mm}$, eccentric, flush with West $X=5029.2$).
   * **NW Corner (C8):** `Footing_N8_C12` ($1200 \times 1200 \times 400\text{ mm}$, eccentric, flush with West $X=5029.2$ & North Road $Y=0$).
   * **Front Bay Raft (C6 & C7 + Sump Pit):** `Sump_Raft_Foundation_Slab` (`Footing_Combined_Front_C6_C7`, $1943.1 \times 1943.1 \times 400\text{ mm}$, monolithic combined raft unifying C6, C7, and the 3,888 L sump tank foundation with zero pit clash).
   * **Septic Bay Raft Extension:** `Septic_Raft_Foundation_Slab` ($1333.5 \times 743.1 \times 400\text{ mm}$, providing non-overlapping monolithic support under the Septic Tank).
   * Total RCC Footings/Raft Volume: $5.65\text{ m}^3$ ($199.5\text{ cu.ft}$).
3. **RCC Column Pedestals (`Column_Pedestals_Group`):**
   * 8 RCC column pedestals ($230 \times 300\text{ mm}$ cross-section, $1814.4\text{ mm}$ vertical height, $Z \in [-1200, +614.4]\text{ mm}$).
   * Pedestals `Pedestal_C1`, `Pedestal_C_SP`, `Pedestal_C2`, `Pedestal_C13`, `Pedestal_C4`, `Pedestal_C9`, `Pedestal_C10`, `Pedestal_C12`.
   * Reconciled corner pedestals (`Pedestal_C2` and `Pedestal_C12`) flush within site boundaries ($X \le 5029.2\text{ mm}, Y \le 7619.8\text{ mm}$).
   * Total Pedestals Volume: $1.00\text{ m}^3$ ($35.3\text{ cu.ft}$).
4. **Plinth Beam Tie Network (`GF_Plinth_Beams`):**
   * 9 interconnected RCC tie beams ($230 \times 300\text{ mm}$ / $230 \times 375\text{ mm}$, $Z \in [614.4, 914.4]\text{ mm}$).
   * Features `PB_LIVING_Primary` ($230 \times 300\text{ mm}$, $L = 5029.2\text{ mm}$) and upsized `PB1_Rear_South` ($230 \times 375\text{ mm}$).
   * Total Plinth Beams Volume: $2.98\text{ m}^3$ ($105.2\text{ cu.ft}$).

---

### 59.3 Contractor Bill of Quantities (BOQ) Schedule (8-Column Active Frame)

| Item No. | Work Description | Mix / Grade | Geometric Volume ($\text{m}^3$) | Imperial Volume ($\text{cu.ft}$) | Standard Billing Unit |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.0** | **Earthwork Excavation** in 8 footing/raft pits ($-1.7\text{ m}$ depth), Sump ($2.1\text{ m}$), Septic pit ($2.1\text{ m}$) & trenches | Soil / Moorum | $51.20\text{ m}^3$ | $1,808.1\text{ cu.ft}$ | $18.08\text{ Brass}$ |
| **2.0** | **PCC Blinding Bed** under 6 eccentric footings + Front combined raft + Septic raft ($100\text{ mm}$ M7.5) | PCC 1:4:8 (M7.5) | $1.54\text{ m}^3$ | $54.3\text{ cu.ft}$ | $1.54\text{ m}^3$ |
| **3.0** | **RCC Footing Pads & Combined Rafts** ($400\text{ mm}$ M25 concrete, 8 structural units) | RCC M25 | $5.65\text{ m}^3$ | $199.5\text{ cu.ft}$ | $5.65\text{ m}^3$ |
| **4.0** | **RCC Substructure Column Pedestals** ($230 \times 300\text{ mm} \times 1814.4\text{ mm}$, 8 stubs) | RCC M25 | $1.00\text{ m}^3$ | $35.3\text{ cu.ft}$ | $1.00\text{ m}^3$ |
| **5.0** | **RCC Plinth Tie Beams** (PB1 + `PB_LIVING_Primary` + PB2, 9 beams) | RCC M25 | $2.98\text{ m}^3$ | $105.2\text{ cu.ft}$ | $2.98\text{ m}^3$ |
| **—** | **SUBTOTAL SUBSTRUCTURE RCC CONCRETE** (Items 3 + 4 + 5) | **RCC M25** | **$9.63\text{ m}^3$** | **$340.0\text{ cu.ft}$** | **$9.63\text{ m}^3$** |

---

### 59.4 Document Verification & Integrity

* **Master Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)
* **Total Substructure Objects:** 8 Footing/Raft solids, 8 PCC blinding layers, 8 Column pedestals, 9 Plinth tie beams.
* **Boundary Verification:** 100% compliant with strict $16'\text{ }6'' \times 25'\text{ }0''$ plot box ($X \in [0.0, 5029.2\text{ mm}], Y \in [0.0, 7619.8\text{ mm}]$). Zero boundary encroachments, 0 manifold errors, zero solid collisions.
* **Document Root Organization:** Consolidated under `Substructure_Foundation_Group` -> `Isolated_Footings_Group`, `PCC_Blinding_Layer_Group`, `Column_Pedestals_Group`, and `GF_Plinth_Beams`.

---
