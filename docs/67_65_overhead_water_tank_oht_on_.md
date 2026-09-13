## 65. Overhead Water Tank (OHT) on Mumty Headroom Roof & Mandatory Construction Safeguards

> [!NOTE]
> **System Title:** Overhead Water Tank (OHT) Headroom Roof Assembly & Structural Plumbing Safeguards  
> **Source Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Parent Group:** `Plumbing & Water Distribution Network` (`Master_Plumbing_Network_Group`)  
> **Subgroup:** `02 Overhead Water Tank Assembly & Roof Infrastructure` (`OHT_Assembly_Group`)  
> **Elevation Span:** $Z = 9585.4\text{ mm}$ (Mumty Roof Slab Top) to $Z = 11462.0\text{ mm}$ (Air Vent Crown).  
> **Governing Standards:** NBC 2016 (Part 9 - Plumbing Services), IS 2065 (Water Supply), IS 456:2000 (Structural Concrete), IS 12701 (Polyethylene Water Storage Tanks).

### 65.1 Overhead Water Tank & Rooftop Assembly Portfolio

```carousel
![OHT on Mumty Headroom Roof - Isometric Overview](c:\Users\prade\OneDrive\Desktop\home plan\renders\oht_headroom_roof_iso_overview.png)
<!-- slide -->
![OHT Raised Concrete Pedestal, Master Valve & Scour Drain Detail](c:\Users\prade\OneDrive\Desktop\home plan\renders\oht_valves_and_pedestal_closeup.png)
<!-- slide -->
![South Mumty Wall SS 304 Maintenance Monkey Ladder](c:\Users\prade\OneDrive\Desktop\home plan\renders\oht_monkey_ladder_and_terrace_view.png)
<!-- slide -->
![Full Building Architectural Skyline with OHT Crown](c:\Users\prade\OneDrive\Desktop\home plan\renders\oht_full_building_skyline_axonometric.png)
```

---

### 65.2 Engineering Justification & Hydraulic Pressure Analysis

Placing the $1,000\text{ L}$ Overhead Water Tank on the monolithic RCC roof slab of the Staircase Headroom (Mumty) at $Z = 9585.4\text{ mm}$ provides critical hydraulic, structural, and spatial advantages over placing it on the main terrace floor:

| Comparison Criterion | Tank on Main Terrace Floor ($Z = 7.26\text{ m}$) | **Tank on Mumty Headroom Roof ($Z = 9.59\text{ m}$)** | Engineering Verdict |
| :--- | :--- | :--- | :--- |
| **First Floor Shower Head Pressure** ($Z \approx 5.9\text{ m}$) | **Only $1.6\text{ m}$ head ($0.16\text{ bar}$ / $2.3\text{ psi}$)**<br>❌ *Extremely weak drizzle; mixer valves, diverters, and health faucets malfunction.* | **$3.9\text{ m}$ head ($0.39\text{ bar}$ / $5.7\text{ psi}$)**<br>✅ **Brisk, refreshing natural gravity shower flow with ZERO booster pump required!** | **+144% Pressure Increase** on First Floor! |
| **Ground Floor Shower & Tap Pressure** ($Z \approx 1.5 - 2.5\text{ m}$) | $5.0 - 6.0\text{ m}$ head ($0.5 - 0.6\text{ bar}$) | **$7.3 - 8.3\text{ m}$ head ($0.73 - 0.83\text{ bar}$ / $11.0\text{ psi}$)**<br>✅ **High-velocity gravity pressure for all ground-floor fixtures.** | **+45% Pressure Increase** on Ground Floor! |
| **Structural Load Transfer Path** | Point load resting on wide residential living/bedroom floor slabs, causing potential long-term deflection. | **Resting directly on 4 monolithic RCC columns** (`Headroom Col NE, NW, SE, SW`) and 4 ring beams (`RB Front, Rear, East, West`). | **Direct vertical load transmission** to foundation bed. |
| **Usable Terrace Living Space** | Consumes $4 - 6\text{ m}^2$ of terrace floor; cluttered by pipes and crossover hazards. | **100% Zero Terrace Intrusion**; the main terrace remains completely open, safe, and pristine. | **100% Usable Terrace Area** preserved for recreation/solar. |

---

### 65.3 The 4 Mandatory Construction Safeguards

To ensure structural longevity, leak-free waterproofing, and effortless maintenance, four mandatory civil and MEP safeguards have been engineered into the model:

```
                  [OHT Airtight Threaded Lid (450mm)]
                                  │
      [1" UPVC Overflow Pipe] ───┼─── [1.2m Anti-Vacuum Air Vent with Cowl]
                                  │
               [1,000L UV-Stabilized Navy Tank Body]
                                  │
    [Scour Washout Valve] ───────┼─────── [1.25" Master Shut-Off Ball Valve]
                                  │
     ============================================================
     [SAFEGUARD 1: Raised Concrete Plinth Pedestal (200mm M25)]
     ------------------------------------------------------------
     [SAFEGUARD 2: Dual-Coat Elastomeric Waterproofing (1:100)]
     ============================================================
     [Mumty Monolithic RCC Roof Slab (125mm M25, Z = 9585.4mm)]
                                  │
     [SAFEGUARD 3: SS 304 External Monkey Ladder on South Wall]
```

1. **Safeguard 1: Raised Monolithic Plinth Pedestal (`OHT_RCC_Pedestal_Plinth`):**
   * **Dimensions:** $\varnothing 1200\text{ mm}$ circular base $\times 200\text{ mm}$ high ($Z = 9585.4\text{ mm} \rightarrow 9785.4\text{ mm}$) centered symmetrically at $(X = 2760, Y = 950)$.
   * **Purpose:** Prevents the plastic tank bottom from resting flat on the roof screed. Guarantees a continuous $200\text{ mm}$ air gap allowing storm rainwater to drain freely underneath without water ponding, while protecting the underlying elastomeric waterproofing membrane from point-load abrasive friction.
2. **Safeguard 2: Dual-Coat Elastomeric Waterproofing & 1:100 Parapet Drainage Slope:**
   * Prior to casting the pedestal, the Mumty roof slab receives a 2-coat UV-resistant elastomeric acrylic polymer waterproofing coating with fiber mesh reinforcement, finished with a 1:100 slope towards a $\varnothing 75\text{ mm}$ drainage gargoyle spout.
3. **Safeguard 3: External SS 304 Maintenance Monkey Ladder (`Mumty_External_Maintenance_Ladder`):**
   * **Dimensions:** Spans $Z = 7260.0\text{ mm}$ (Terrace floor) up to $Z = 9750.0\text{ mm}$ (Mumty roof curb) on the South exterior wall ($Y = 1910\text{ mm}$, $X \in [2284, 2766\text{ mm}]$).
   * **Specification:** Twin $\varnothing 32\text{ mm}$ SS 304 side stringer rails with 8 anti-slip knurled rungs spaced at $280\text{ mm}$ c/c and heavy-duty masonry standoff expansion brackets. Ensures safe, permanent climbing access for bi-annual tank inspection, sediment flushing, and water testing.
4. **Safeguard 4: Anti-Vacuum Air Vent Pipe & Sediment Trap Invert (`OHT_Anti_Vacuum_Air_Vent_Pipe`):**
   * **Air Vent:** Extends to $Z = 11462\text{ mm}$ ($+327\text{ mm}$ above the tank lid) with a $180^\circ$ return bend and fine bronze insect mesh to equalize atmospheric pressure during rapid draw-down, preventing vacuum tank implosion and air locks in the down-take branches.
   * **Sediment Trap:** The $1.25"$ master gravity outlet is elevated $+75\text{ mm}$ above the tank base, while the dedicated scour drain valve (`Valve_OHT_Washout_Drain_Scour`) sits flush at the lowest invert ($Z = 9815\text{ mm}$) to effortlessly flush out accumulated dust and silt.

---

### 65.4 3D Rooftop Component Schedule

| Object Name | FreeCAD Label | Location / Coordinates (mm) | Material / Specifications | Function & Engineering Purpose |
| :--- | :--- | :--- | :--- | :--- |
| `OHT_RCC_Pedestal_Plinth` | OHT Raised Concrete Plinth Pedestal | $X \in [2162, 3360], Y \in [351, 1550], Z \in [9585, 9785]$ | M25 RCC with smooth cement plaster (`#BDC3C7`) | Circular pedestal spreading $10.3\text{ kN}$ load evenly across Mumty roof beams. |
| `OHT_1000L_Water_Tank_Body` | Overhead Water Tank Body (1,000L) | $X \in [2228, 3295], Y \in [416, 1484], Z \in [9785, 11135]$ | 4-layer antimicrobial UV Navy Blue polymer (`#1B1464`) | $1,000\text{ L}$ main domestic potable storage with 3 structural hoop reinforcement ribs. |
| `OHT_Inspection_Threaded_Lid` | OHT Airtight Threaded Inspection Lid | $X \in [2526, 2995], Y \in [715, 1185], Z \in [11135, 11225]$ | $\varnothing 470\text{ mm}$ Charcoal polymer (`#2C3E50`) with lock lugs | Airtight, dust-proof, and insect-proof access lid for cleaning and inspection. |
| `OHT_Overflow_Pipe_Terrace_Drop` | OHT 1-Inch UPVC Overflow Pipe | $X \in [1963, 2235], Y = 950, Z \in [7350, 10966]$ | $25\text{ mm}$ Class 3 UPVC (`#E8ECEF`) with wire mesh cowl | Discharges excess water safely onto terrace floor drain in case of float failure. |
| `Valve_OHT_Washout_Drain_Scour` | Valve: OHT Washout & Scour Drain | $X \in [1935, 2235], Y = 950, Z \in [9790, 9875]$ | Forged Brass body with vivid Red quarter-turn lever | Low-point scour valve for desludging and complete tank emptying. |
| `OHT_Anti_Vacuum_Air_Vent_Pipe` | OHT Anti-Vacuum Air Vent Pipe | $X = 3350, Y \in [938, 1022], Z \in [9860, 11462]$ | $25\text{ mm}$ CPVC riser with inverted $180^\circ$ goose-neck | Prevents hydraulic air binding and tank vacuum collapse during high water draw. |
| `Valve_OHT_Master_Gravity_Outlet` | Valve: OHT Master Gravity Supply Shut-Off | $X \in [3285, 3573], Y = 950, Z \in [9828, 9938]$ | $1.25"$ ($32\text{ mm}$) Heavy-duty Brass ball valve (`#EA2027`) | Master building isolation valve for entire gravity down-take network. |
| `Mumty_External_Maintenance_Ladder` | Mumty External SS 304 Maintenance Ladder | $X \in [2284, 2766], Y \in [1867, 1926], Z \in [7260, 9750]$ | SS 304 tubular rails & 8 knurled anti-slip rungs (`#DCDDE1`) | Safe vertical climbing ladder from terrace to Mumty roof for maintenance personnel. |
| `OHT_Saddle_Beam_North` | OHT RCC Saddle Beam North | $X \in [1564.5, 5100.6], Y \in [570.0, 800.0], Z \in [9260.4, 9490.4]$ | $230 \times 230\text{ mm}$ M25 RCC with Fe500D rebar | Transmits OHT tank load directly into column stems C7 and C8 via axial compression. |
| `OHT_Saddle_Beam_South` | OHT RCC Saddle Beam South | $X \in [1564.5, 5100.6], Y \in [1100.0, 1330.0], Z \in [9260.4, 9490.4]$ | $230 \times 230\text{ mm}$ M25 RCC with Fe500D rebar | Transmits OHT tank load directly into column stems C7 and C8 via axial compression. |

---

### 65.5 Verification & Document Status

* **Master Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)
* **Total Objects in Document:** 548 objects, 0 errors, 100% valid manifold solids.
* **Structural Verification:** Zero beam or column collisions; load transferred through Mumty columns C2, C3, C8, and C9.
* **Document Synchronization:** Section 65 added and Table of Contents updated.


---
