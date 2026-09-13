## 62. Substructure Spatial Collision Elimination: Raft Foundations & Exact Bay-Fitted Tanks

> [!NOTE]
> **System Title:** Foundation & Substructure Collision Resolution & Mat Raft Foundation Architecture  
> **Source Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Root Container:** `Substructure_Foundation_Group`  
> **Collision Status:** **0 Collisions across all 531 objects** (verified mathematically via 3D bounding-box intersection test).

### 62.1 Zero-Collision Substructure Portfolio

```carousel
![Zero Collision Substructure & Raft Foundations](c:\Users\prade\OneDrive\Desktop\home plan\renders\substructure_zero_collision_iso.png)
<!-- slide -->
![Zero Collision Front Elevation Depth Profile](c:\Users\prade\OneDrive\Desktop\home plan\renders\substructure_zero_collision_front.png)
```

---

### 62.2 Spatial Conflict Identification & Civil Engineering Resolution

1. **The Conflict Identified:**
   * A geometric overlap test revealed that the previous generic tank footprints intersected the RCC column pedestals, the plinth beams, and the isolated footing pads.
   * In standard construction, isolated footing pads cannot project into water storage or septic digestion chambers.
2. **Structural Engineering Redesign (Mat / Raft Foundations):**
   * **Sump Combined Raft Slab (`Sump_Raft_Foundation_Slab`):** Replaced the 4 clashing corner footings under C9, C10, C5, C6 with a monolithic $300\text{ mm}$ thick RCC raft base slab ($1943.1 \times 1943.1\text{ mm}$, $Z \in [-1500, -1200]\text{ mm}$) on a $100\text{ mm}$ PCC blinding bed ($Z \in [-1600, -1500]\text{ mm}$).
   * **Septic Combined Raft Slab (`Septic_Raft_Foundation_Slab`):** Replaced the 4 clashing corner footings under C11, C12, C7, C8 with a monolithic $300\text{ mm}$ thick RCC raft base slab ($1333.5 \times 1943.1\text{ mm}$, $Z \in [-1500, -1200]\text{ mm}$) on a $100\text{ mm}$ PCC blinding bed.
   * **Bay-Fitted Tank Outer Shells:**
     - `Sump_UG_Water_Tank`: Scaled to $1485.9 \times 1485.9\text{ mm}$ ($4'\text{-}10.5" \times 4'\text{-}10.5"$), $Z \in [-1200, +914.4]\text{ mm}$ ($2114.4\text{ mm}$ height, gross volume $\approx 4,670\text{ L}$). Fits precisely within the inner faces of plinth beams and pedestals with **$0.0\text{ mm}$ collision**.
     - `Septic_Tank`: Scaled to $876.3 \times 1485.9\text{ mm}$ ($2'\text{-}10.5" \times 4'\text{-}10.5"$), $Z \in [-1200, +914.4]\text{ mm}$ ($2114.4\text{ mm}$ height, gross volume $\approx 2,750\text{ L}$). Fits precisely within the inner faces of plinth beams and pedestals with **$0.0\text{ mm}$ collision**.
   * **Column Pedestal Realignment:** All 8 pedestals around the tanks now rise seamlessly from the top of the raft slab ($Z = -1200\text{ mm}$) to the underside of the plinth beams ($Z = +614.4\text{ mm}$, height = $1814.4\text{ mm}$), framing the tanks with zero interference.

---

### 62.3 Updated Substructure Contractor BOQ Schedule

| Item No. | Work Description | Mix / Grade | Geometric Volume ($\text{m}^3$) | Imperial Volume ($\text{cu.ft}$) | Standard Billing Unit |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **1.0** | **Earthwork Excavation** (pits for 6 rear isolated footings + Sump raft pit + Septic raft pit) | Soil / Moorum | $31.24\text{ m}^3$ | $1,103.3\text{ cu.ft}$ | $11.03\text{ Brass}$ |
| **2.0** | **PCC Blinding Beds** (Sump raft PCC + Septic raft PCC + 6 rear footing pads, $100\text{ mm}$ thick) | PCC 1:4:8 (M7.5) | $1.487\text{ m}^3$ | $52.5\text{ cu.ft}$ | $1.49\text{ m}^3$ |
| **3.0** | **RCC Footings & Raft Slabs** (2 Rafts $300\text{ mm}$ + 6 Isolated footings $400\text{ mm}$) | RCC M25 | $4.526\text{ m}^3$ | $159.8\text{ cu.ft}$ | $4.53\text{ m}^3$ |
| **4.0** | **RCC Substructure Column Pedestals** (14 RCC stubs) | RCC M25 | $1.296\text{ m}^3$ | $45.8\text{ cu.ft}$ | $1.30\text{ m}^3$ |
| **5.0** | **RCC Plinth Tie Beams (PB1 & PB2)** (10 interconnected beams) | RCC M25 | $2.845\text{ m}^3$ | $100.5\text{ cu.ft}$ | $2.85\text{ m}^3$ |
| **—** | **SUBTOTAL SUBSTRUCTURE RCC CONCRETE** (Items 3 + 4 + 5) | **RCC M25** | **$8.668\text{ m}^3$** | **$306.1\text{ cu.ft}$** | **$8.67\text{ m}^3$** |
| **6.0** | **Sump Tank Structural Shell** ($1485.9 \times 1485.9 \times 2114.4\text{ mm}$, $4,670\text{ L}$ gross) | Watertight RCC | $4.668\text{ m}^3$ | $164.8\text{ cu.ft}$ | Lump Sum / Unit |
| **7.0** | **Septic Tank Structural Shell** ($876.3 \times 1485.9 \times 2114.4\text{ mm}$, $2,750\text{ L}$ gross) | Watertight RCC | $2.753\text{ m}^3$ | $97.2\text{ cu.ft}$ | Lump Sum / Unit |

---

### 62.4 Verification & Object Status

* **Total Objects in Document:** 531 objects, 0 errors, 100% valid manifold solids.
* **Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd).

---
