# Plumbing & Water Distribution Network Engineering Plan (Updated)

Implement a complete, closed-loop residential water supply and distribution infrastructure in [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd), complying with **National Building Code (NBC) 2016 (Part 9 - Plumbing Services)** and incorporating the **Dual-Tap Kitchen Sink Direct Municipal Verification System**.

---

## 1. System Architecture & Flow Overview

```
[East Municipality Main (X <= 0, East Street)]
              │
              ▼ (Municipal Isolation Valve & Water Meter at East Boundary)
     [25mm Inflow Pipeline along East Foundation]
              │
              ├───► [GF Kitchen Sink Tap 1: Direct Municipal Potable Tap]
              │      (Allows immediate visual verification of municipal flow & pure drinking water)
              │
              ▼ [Intermediate Control Shut-Off Valve (Between Sink & Sump)]
              │  (Controls filling of sump; enables flushing initial dirty water before sump intake)
              │
              ▼ (Float Valve / Ball Cock)
[Underground Sump (5,600L, Z = -1500 to +914mm)]
              │
              ▼ (Foot Valve & 1.25" Suction Drop Pipe)
[1.0 HP Sump Pump Motor (Under Stair Flight 1)]
              │
              ▼ (NRV Check Valve + Delivery Control Valve)
[1" Rising Main Riser (Z = 1000mm -> Z = 9700mm)]
              │
              ▼ (Inlet Goose-neck)
[Overhead Water Tank (1000L Sintex/Supreme on Mumty Roof, Z = 9585mm)]
              │
              ▼ (Master OHT Shut-Off Valve + Air Vent + Drain/Washout)
    [Distribution Manifold]
        ├─── Line A: Toilet Down-take Riser (1" CPVC)
        │       │     (Routed in False Duct; branches into East Wall; 0 South wall pipes)
        │       ├─── [FF Toilet Shut-Off Valve (East Wall)] ──► FF East Wall Shower & Mixer Tap
        │       └─── [GF Toilet Shut-Off Valve (East Wall)] ──► GF East Wall Shower & Mixer Tap
        │
        ├─── Line B: Kitchen Down-take Riser (1" CPVC)
        │       │     (Routed via Front Weather Head & Outer Edge of East Parapet at X = -60mm; 100% clean terrace)
        │       ├─── [FF Kitchen Shut-Off Valve] ──► FF Kitchen Sink Faucet
        │       └─── [GF Kitchen Shut-Off Valve] ──► [GF Kitchen Sink Tap 2: OHT Domestic Water Tap]
        │
        ├─── Line C: Multi-Purpose Utility Feeder (3/4" CPVC in False Duct)
        │       └─── [Utility Station Shut-Off Valve] ──► Dual-Spout 2-Way Brass Bibcock (Washer & Garden)
        │
        └─── Line D: Rooftop Terrace Utility Feeder (3/4" CPVC)
                └─── [Terrace Tap Shut-Off Valve] ──────► Rooftop Terrace Utility Bibcock
```

---

## 2. Updated Engineering Components

### A. East Municipality Supply & Dual-Tap GF Kitchen Integration
- **Source Point:** East street boundary at $X = -500\text{ mm}, Y = 1000\text{ mm}, Z = 400\text{ mm}$.
- **Service Connection:** 
  - Water meter assembly ($25\text{ mm}$ brass dial casing with bronze unions).
  - Main Municipal Isolating Ball Valve at boundary.
  - $25\text{ mm}$ incoming municipal pipeline running along the East wall.
- **GF Kitchen Sink Dual-Tap Setup ($X \approx 450-550\text{ mm}, Y \approx 7250-7350\text{ mm}, Z \approx 1784-1950\text{ mm}$):**
  - **Tap 1 (Direct Municipal Tap):** Swan-neck / bibcock faucet connected directly to the incoming city supply line. 
    * *Purpose:* Visually verify municipal supply arrival without checking the sump, and collect fresh potable cooking/drinking water.
  - **Tap 2 (Overhead Tank Domestic Tap):** High-arch swivel faucet connected to the gravity down-take from the rooftop OHT.
    * *Purpose:* General utensil washing, cleaning, and day-to-day kitchen sink usage.
- **Intermediate Shut-Off Valve (`Valve_Municipal_Sink_To_Sump`):**
  - Positioned along the municipal line immediately between the Kitchen sink branch and the Sump inlet.
  - *Operational Benefit:* Allows opening the kitchen tap to flush out any stagnant/turbid initial municipal line water before turning the valve to divert clean water into the underground sump. Also allows closing sump filling if the sump is full while still drawing water at the kitchen sink.
- **Sump Automatic Cut-off:**
  - Sump inlet maintenance ball valve.
  - High-capacity mechanical brass float ball valve ($\varnothing 150\text{ mm}$) inside `Sump_UG_Water_Tank`.

### B. Motor Pumping Line (Rising Main Extension)
- **Pump Station:** Existing 1.0 HP monobloc pump assembly under Staircase Flight 1 ($X \approx 2270\text{ mm}, Y \approx 650\text{ mm}$).
- **Suction Line:** $1.25"$ suction drop pipe with foot valve & strainer ($Z = -1450\text{ mm}$ to $+914\text{ mm}$).
- **Rising Main (1" UPVC / GI):**
  - Continuous vertical riser from `Delivery Control Valve` ($Z = 1500\text{ mm}$) up through Ground Floor, First Floor, and Staircase Headroom to $Z = 9700\text{ mm}$.
  - Terminating with a $90^\circ$ goose-neck discharging into the top of the Overhead Tank with an anti-siphon air gap.

### C. Rooftop Overhead Water Tank (OHT) Assembly
- **Location:** On the monolithic RCC roof slab of the Staircase Headroom (Mumty) at $Z = 9585\text{ mm}$, positioned at $X = 2400\text{ mm}, Y = 1000\text{ mm}$.
- **Structural Ring Pedestal:** $1200\text{ mm}$ diameter $\times 200\text{ mm}$ high reinforced concrete ring base (`#BDC3C7`).
- **Tank Geometry:** $1,000\text{ L}$ commercial 4-layer UV-stabilized storage tank (cylindrical $\varnothing 1050\text{ mm} \times H = 1350\text{ mm}$, dark navy blue `#1B1464` with gold rib rings).
- **Fittings:**
  1. Top inlet goose-neck from pump rising main.
  2. 1" UPVC overflow pipe dropping to terrace floor with mesh cowl.
  3. 1" UPVC bottom washout/scour drain with dedicated Scour Ball Valve (`Valve_OHT_Drain`).
  4. 1.2m anti-vacuum air vent pipe with inverted U-bend.
  5. 1.25" main bottom gravity outlet with Master Shut-Off Ball Valve (`Valve_OHT_Master_Outlet`).

### D. Down-take Gravity Distribution Manifold & Vertical Risers
- **Line A (Toilets Riser - 1" CPVC):** Down-take chase feeding FF Toilet and GF Toilet.
- **Line B (Kitchens Riser - 1" CPVC):** Down-take chase feeding FF Kitchen sink and GF Kitchen Sink Tap 2 (OHT Domestic Tap).
- **Line C (Utility & Sitout - 3/4" CPVC):** Down-take feeding under-stair washing machine and sitout outdoor tap.

### E. Zonal Shut-Off Valves (Individual Leak Isolation Protection)
1. **GF Kitchen Municipal-to-Sump Valve (`Valve_Municipal_Sink_To_Sump`)**: Quarter-turn valve between sink tap and sump.
2. **GF Toilet Shut-Off Valve (`Valve_GF_Toilet_Isolate`)**: Wall stop cock / ball valve. Shuts off only GF toilet fixtures during leak.
3. **FF Toilet Shut-Off Valve (`Valve_FF_Toilet_Isolate`)**: Shuts off only FF toilet fixtures.
4. **GF Kitchen OHT Domestic Shut-Off Valve (`Valve_GF_Kitchen_Isolate`)**: Under-counter valve for OHT supply.
5. **FF Kitchen Shut-Off Valve (`Valve_FF_Kitchen_Isolate`)**: Under-counter valve for FF kitchen sink.
6. **Utility Station Shut-Off Valve (`Valve_GF_Utility_Isolate`)**: Above washing machine inlet.
7. **Sitout Garden Tap Shut-Off Valve (`Valve_GF_Sitout_Tap_Isolate`)**: At sitout hose bibcock.
8. **OHT Master Gravity Shut-Off Valve (`Valve_OHT_Master_Outlet`)**: At OHT outlet.
9. **OHT Scour Drain Valve (`Valve_OHT_Drain`)**: For tank cleaning.
10. **Municipal Boundary Main Valve (`Valve_Municipal_Main`)**: At east property entry.
11. **Sump Maintenance Valve (`Valve_Sump_Inlet`)**: Inside sump hatch before float valve.

---

## 3. FreeCAD Document Organization

```
Plumbing & Water Distribution Network (Master_Plumbing_Network_Group)
  ├── 01_Municipal_Water_Supply_Group
  │     ├── Municipal_Water_Meter
  │     ├── Valve_Municipal_Main_Shutoff
  │     ├── Municipal_Inflow_Pipe_East_Boundary (25mm CPVC)
  │     ├── GF_Kitchen_Municipal_Direct_Supply_Pipe
  │     ├── GF_Kitchen_Sink_Municipal_Tap (Direct Potable Water Tap)
  │     ├── Valve_Municipal_Sink_To_Sump (Intermediate Shut-Off Valve)
  │     ├── Municipal_Pipe_To_Sump_Inlet
  │     ├── Valve_Sump_Inlet_Maintenance
  │     └── Sump_Brass_Float_Valve
  │
  ├── 02_Sump_Pump_Rising_Main_Group
  │     ├── Sump_Rising_Main_GF_Vertical_Rise (1" UPVC)
  │     ├── Sump_Rising_Main_FF_Vertical_Rise (1" UPVC)
  │     ├── Sump_Rising_Main_Headroom_Rise (1" UPVC)
  │     └── Sump_Rising_Main_OHT_Inlet_Gooseneck
  │
  ├── 03_Overhead_Water_Tank_Assembly_Group
  │     ├── OHT_RCC_Pedestal_Plinth (1200mm dia x 200mm)
  │     ├── OHT_1000L_Water_Tank_Body (Cylindrical with ribbed bands)
  │     ├── OHT_Inspection_Threaded_Lid (450mm dia)
  │     ├── OHT_Overflow_Pipe_Terrace_Drop (1" UPVC)
  │     ├── Valve_OHT_Washout_Drain_Scour
  │     ├── OHT_Anti_Vacuum_Air_Vent_Pipe (1.2m with U-bend)
  │     └── Valve_OHT_Master_Gravity_Outlet
  │
  ├── 04_Gravity_Downtake_Distribution_Network_Group
  │     ├── Rooftop_Gravity_Distribution_Manifold
  │     ├── Downtake_Toilet_Riser_Shaft (1" CPVC)
  │     ├── Downtake_Kitchen_Riser_Shaft (1" CPVC)
  │     ├── GF_Kitchen_Sink_OHT_Domestic_Tap (Overhead Tank Tap)
  │     └── Downtake_Utility_Sitout_Branch (3/4" CPVC)
  │
  └── 05_Zonal_Isolation_Shutoff_Valves_Group
        ├── Valve_GF_Toilet_Isolate (Brass quarter-turn with red lever)
        ├── Valve_FF_Toilet_Isolate (Brass quarter-turn with red lever)
        ├── Valve_GF_Kitchen_Isolate (Under-counter OHT stop cock)
        ├── Valve_FF_Kitchen_Isolate (Under-counter stop cock)
        ├── Valve_GF_Utility_Isolate (Brass bibcock/ball valve)
        └── Valve_GF_Sitout_Tap_Isolate (Brass outdoor shut-off valve)
```

---

## 4. Verification Plan

1. **Automated Geometric Manifold Verification**:
   - Zero invalid shapes in FreeCAD (`doc.Objects`).
2. **Elevation & Continuity Audit**:
   - Verify Municipal incoming line branches to GF Kitchen Sink (Tap 1) at $Z \approx 1784\text{ mm}$.
   - Verify intermediate valve between sink and Sump inlet ($Z \approx 750\text{ mm}$).
   - Verify Sump pump delivery pipe ascends continuously from $Z = 1500\text{ mm}$ to $Z = 9700\text{ mm}$.
   - Verify OHT sits securely on Mumty roof ($Z = 9585\text{ mm}$).
   - Verify GF Kitchen Sink features both Tap 1 (Municipal) and Tap 2 (OHT).
   - Verify independent shut-off valves in all wet zones.
3. **Visual Verification & Walkthrough Update**:
   - Generate renders showing:
     * GF Kitchen sink dual-tap arrangement and intermediate valve.
     * Full building water network (transparent walls).
     * Rooftop OHT assembly.
   - Update `walkthrough.md` with Section 64, 65, and 66.

---

## 5. Execution Status: 100% COMPLETE

* **Phase 1 (Municipal Water Supply to Sump Network):** COMPLETED (9 objects in `Municipal_To_Sump_Plumbing_Group`).
* **Phase 2 (Overhead Water Tank Assembly & Roof Infrastructure):** COMPLETED (8 objects in `OHT_Assembly_Group`).
* **Phase 3 (Sump Pump Rising Main & Internal False Duct - Method B):** COMPLETED (4 objects in `Sump_Pump_Rising_Main_Group`).
* **Phase 4 (Gravity Down-take Distribution Network):** COMPLETED (7 objects in `Gravity_Downtake_Distribution_Network_Group`).
* **Phase 5 (Zonal Isolation Shut-Off Valves):** COMPLETED (6 objects in `Zonal_Isolation_Shutoff_Valves_Group`).
* **Model Integrity:** 574 total objects in `HomeConstruction.FCStd`, 0 errors, 100% valid manifold shapes, saved to disk.
* **Documentation & Renders:** Sections 64, 65, and 66 documented in `walkthrough.md` with high-resolution visual renders embedded.

