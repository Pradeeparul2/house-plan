## 21. Continuous Vertical Wall Conduit Network into Modular Switch Boxes & Distribution Boards

In residential electrical engineering and construction practice, electrical conduits are installed across two distinct phases:
1. **Ceiling Slab Conduit Pour Phase (Pre-Casting):** Heavy-duty rigid PVC conduits ($25\text{ mm}$ OD) are laid horizontally over the shuttering before RCC slab casting, terminating with curved PVC drop bends at column/wall boundaries.
2. **Masonry Chase & Switch Box Chasing Phase (Post-Deshuttering):** Vertical wall chases ($30 - 40\text{ mm}$ wide, $25\text{ mm}$ deep) are grooved into the brick masonry using wall chasers. Continuous rigid PVC conduit pipes are joined to the ceiling slab drops using PVC couplers and run vertically down into the top knock-outs of the flush modular metal concealed switch boxes and distribution boards.

To ensure 100% physical continuity between the ceiling slab conduit networks and every concealed modular switch box, the stub ceiling drops have been extended into continuous, full-height vertical wall conduit pipe runs across both the **Ground Floor** and **First Floor**.

```carousel
![Front Elevation of Two-Storey Electrical System Showing Continuous Vertical Conduit Drops Entering Switchboxes](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\electrical_front_view_all_conduits.png)
<!-- slide -->
![Isometric 3D View of Complete Two-Storey Electrical Infrastructure with Fully Connected Conduits](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\electrical_isometric_view_all_conduits.png)
<!-- slide -->
![Close-Up Elevation of First Floor and Ground Floor Vertically Stacked MDBs and Switchboards with Direct Pipe Feeds](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\mdb_stack_conduit_connections.png)
<!-- slide -->
![Perspective View of First Floor Rear Bedroom, Bedside, AC, and Kitchen Switchboards with Vertical Conduits](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\ff_rear_bedroom_kitchen_conduits.png)
```

### 21.1 First Floor Vertical Wall Conduit Schedule (`FF_Electrical_Slab_Wall_Drops`)
All 12 switchboxes and distribution boards on the First Floor are connected via continuous heavy-gauge $25\text{ mm}$ rigid PVC conduits in **Emerald Green (`#10AC84`)**:

| Switch Box / Board ID | Description & Functional Zone | Coordinates $(X, Y)$ | Elevation Run ($Z_{top} \to Z_{slab}$) | Conduit Length | Knockout Entry Point |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **`FF_MDB`** | 8-Way SPN Main Distribution Board | $(1600.0, 1930.0\text{ mm})$ | $5747.4 \to 7193.0\text{ mm}$ | $1445.6\text{ mm}$ | Top Knockout |
| **`FF_SB-1`** | Living Room Main Modular Switchboard | $(1700.0, 1932.5\text{ mm})$ | $5387.4 \to 7193.0\text{ mm}$ | $1805.6\text{ mm}$ | Top Knockout + MDB Interconnect |
| **`FF_SB-2`** | Living Room West TV Modular Switchboard | $(4852.5, 3310.0\text{ mm})$ | $5187.4 \to 7193.0\text{ mm}$ | $2005.6\text{ mm}$ | Top Knockout |
| **`FF_SB-3`** | Bedroom Entry Modular Switchboard | $(2125.0, 4782.5\text{ mm})$ | $5387.4 \to 7193.0\text{ mm}$ | $1805.6\text{ mm}$ | Top Knockout |
| **`FF_SB-4`** | Bedroom Bedside Modular Switchboard | $(4852.5, 6075.0\text{ mm})$ | $4937.4 \to 7193.0\text{ mm}$ | $2255.6\text{ mm}$ | Top Knockout |
| **`FF_SB-5`** | Bedroom AC High-Level Power Point | $(4852.5, 6750.0\text{ mm})$ | $6287.4 \to 7193.0\text{ mm}$ | $905.6\text{ mm}$ | Top Knockout |
| **`FF_SB-6`** | Kitchen Working Counter Switchboard | $(252.5, 6500.0\text{ mm})$ | $5237.4 \to 7193.0\text{ mm}$ | $1955.6\text{ mm}$ | Top Knockout |
| **`FF_SB-7`** | Kitchen Refrigerator / Power Point | $(252.5, 7150.0\text{ mm})$ | $4687.4 \to 7193.0\text{ mm}$ | $2505.6\text{ mm}$ | Top Knockout |
| **`FF_SB-8`** | Toilet Entry Modular Switchboard | $(3850.0, 1752.5\text{ mm})$ | $5387.4 \to 7193.0\text{ mm}$ | $1805.6\text{ mm}$ | Top Knockout |
| **`FF_SB-9`** | Toilet Geyser High-Level Power Point | $(4852.5, 907.0\text{ mm})$ | $6287.4 \to 7193.0\text{ mm}$ | $905.6\text{ mm}$ | Top Knockout |
| **`FF_SB-10`** | Balcony Corridor Switchboard | $(1660.0, 1672.5\text{ mm})$ | $5387.4 \to 7193.0\text{ mm}$ | $1805.6\text{ mm}$ | Top Knockout |
| **`FF_SB_UPS`** | Dedicated UPS Charging & Output Box | $(158.4, 2320.0\text{ mm})$ | $6530.0 \to 6580.0\text{ mm}$ | $50.0\text{ mm}$ | Top Knockout (via `FF_UPS_Conduit_Pipeline`) |

### 21.2 Ground Floor Vertical Wall Conduit Schedule (`Electrical_Slab_Wall_Drops`)
All 18 switchboxes and distribution boards on the Ground Floor are connected via continuous heavy-gauge $25\text{ mm}$ rigid PVC conduits in **Emerald Green (`#10AC84`)**:

| Switch Box / Board ID | Description & Functional Zone | Coordinates $(X, Y)$ | Elevation Run ($Z_{top} \to Z_{slab}$) | Conduit Length | Knockout Entry Point |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **`GF_MDB`** | 8-Way SPN Main Distribution Board | $(1600.0, 1930.0\text{ mm})$ | $2574.4 \to 4020.0\text{ mm}$ | $1445.6\text{ mm}$ | Top Knockout |
| **`GF SB 0`** | Living Room Main Switchboard | $(1700.0, 1937.5\text{ mm})$ | $2189.4 \to 4020.0\text{ mm}$ | $1830.6\text{ mm}$ | Top Knockout + MDB Interconnect |
| **`GF SB 1`** | Foyer / Entrance Switchboard | $(2275.0, 797.5\text{ mm})$ | $2189.4 \to 4020.0\text{ mm}$ | $1830.6\text{ mm}$ | Top Knockout |
| **`GF SB 2`** | Living Room South Wall Switchboard | $(1762.5, 2117.5\text{ mm})$ | $2264.4 \to 4020.0\text{ mm}$ | $1755.6\text{ mm}$ | Top Knockout |
| **`GF SB 17`** | Living Room TV Upper Display Point | $(4845.8, 3275.0\text{ mm})$ | $2140.0 \to 4020.0\text{ mm}$ | $1880.0\text{ mm}$ | Top Knockout |
| **`GF SB 3`** | Living Room TV Lower Modular Console | $(4845.8, 3262.5\text{ mm})$ | $1550.0 \to 2050.0\text{ mm}$ | $500.0\text{ mm}$ | Interconnecting Chase Pipe |
| **`GF SB 4`** | Dining Room Entry Switchboard | $(1925.0, 4697.5\text{ mm})$ | $2189.4 \to 4020.0\text{ mm}$ | $1830.6\text{ mm}$ | Top Knockout |
| **`GF SB 5`** | Dining Room South Wall Switchboard | $(1867.5, 4975.0\text{ mm})$ | $2264.4 \to 4020.0\text{ mm}$ | $1755.6\text{ mm}$ | Top Knockout |
| **`GF SB 6`** | Kitchen Working Counter Switchboard | $(222.5, 6300.0\text{ mm})$ | $2089.4 \to 4020.0\text{ mm}$ | $1930.6\text{ mm}$ | Top Knockout |
| **`GF SB 7`** | Kitchen Utility / Under-Counter Point | $(1837.5, 7357.5\text{ mm})$ | $1439.4 \to 4020.0\text{ mm}$ | $2580.6\text{ mm}$ | Top Knockout |
| **`GF SB 8`** | Bedroom Entry Switchboard | $(2107.5, 4925.0\text{ mm})$ | $2264.4 \to 4020.0\text{ mm}$ | $1755.6\text{ mm}$ | Top Knockout |
| **`GF SB 9`** | Bedroom Bedside Left Switchboard | $(2400.0, 7462.5\text{ mm})$ | $1689.4 \to 4020.0\text{ mm}$ | $2330.6\text{ mm}$ | Top Knockout |
| **`GF SB 10`** | Bedroom Bedside Right Switchboard | $(4575.0, 7462.5\text{ mm})$ | $1689.4 \to 4020.0\text{ mm}$ | $2330.6\text{ mm}$ | Top Knockout |
| **`GF SB 11`** | Bedroom Wardrobe / Study Point | $(2937.5, 4692.5\text{ mm})$ | $2039.4 \to 4020.0\text{ mm}$ | $1980.6\text{ mm}$ | Top Knockout |
| **`GF SB 12`** | Toilet Entry Switchboard | $(3807.5, 1850.0\text{ mm})$ | $2189.4 \to 4020.0\text{ mm}$ | $1830.6\text{ mm}$ | Top Knockout |
| **`GF SB 13`** | Toilet Geyser Point | $(4757.5, 1260.0\text{ mm})$ | $2339.4 \to 4020.0\text{ mm}$ | $1680.6\text{ mm}$ | Top Knockout |
| **`GF SB 14`** | Car Porch / Verandah Switchboard | $(1987.5, 247.5\text{ mm})$ | $2189.4 \to 4020.0\text{ mm}$ | $1830.6\text{ mm}$ | Top Knockout |
| **`GF SB 16`** | Dedicated Ground Floor UPS Point | $(157.4, 2325.0\text{ mm})$ | $3345.0 \to 4020.0\text{ mm}$ | $675.0\text{ mm}$ | Top Knockout |

### 21.3 Ceiling Slab Network Continuity & Interconnections
To complete unbroken circuit paths from the rooftop solar/EB mains, downlight pots, and ceiling fan boxes into each vertical drop:
* **First Floor Slab Network (`FF_Electrical_Slab_Conduit_Network`):** 8 connecting branch conduits were added ($20 \to 28$ solid elements), creating direct physical links at $Z = 7193.0\text{ mm}$ to every wall drop position.
* **Ground Floor Slab Network (`Electrical_Slab_Conduit_Network`):** 14 connecting branch conduits were added ($1 \to 15$ solid elements), connecting all ceiling fan boxes and downlight circuits at $Z = 4020.0\text{ mm}$ directly into each vertical wall conduit.

### 21.4 Visual Coding Standards
The 3D model maintains clear, high-contrast visual differentiation across all electrical layers:
* **Horizontal Slab Conduits:** Safety Orange (`#FF7675` / `(1.0, 0.45, 0.0)`) embedded inside the RCC slab core.
* **Vertical Wall Chased Conduits:** Emerald Green (`#10AC84` / `(0.06, 0.67, 0.52)`) running down brick chases directly into switchbox tops.
* **Dedicated UPS Inverter Conduits:** Deep Electric Cyan (`(0.04, 0.52, 0.89)`).
* **RF / Cable TV Antenna Conduit:** Sky Blue (`#00CECB`).
* **CCTV Security Network:** Royal Purple (`#9B59B6`).
* **Concealed Modular Switch Boxes & MDBs:** Clean Pearl White and Galvanized Metal Gray (`#FFFFFF` / `#BDC3C7`).

---
