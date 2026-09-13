## 64. Municipal Water Inflow Pipeline, Dual-Tap Kitchen Sink & Underground Sump Integration

> [!NOTE]
> **System Title:** Municipal Service Connection, Dual-Tap Kitchen Verification & Sump Automation Network  
> **Source Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Parent Group:** `Plumbing & Water Distribution Network` (`Master_Plumbing_Network_Group`)  
> **Subgroup:** `01 Municipal Water Supply to Sump Network` (`Municipal_To_Sump_Plumbing_Group`)  
> **Governing Standards:** NBC 2016 (Part 9 - Plumbing Services), IS 2065: Code of Practice for Water Supply in Buildings, IS 15778 CPVC Piping Standard.

### 64.1 Municipal to Sump Pipeline Visual Portfolio

```carousel
![GF Kitchen Sink Dual Taps - Municipal Potable Tap & OHT Faucet](c:\Users\prade\OneDrive\Desktop\home plan\renders\gf_kitchen_sink_dual_taps_and_valve.png)
<!-- slide -->
![Under-Sink Intermediate Shut-Off Valve & Pipe Routing X-Ray](c:\Users\prade\OneDrive\Desktop\home plan\renders\gf_kitchen_under_sink_valve_xray.png)
<!-- slide -->
![Underground Sump Inflow Pipe & Mechanical Brass Float Ball Valve](c:\Users\prade\OneDrive\Desktop\home plan\renders\sump_inflow_and_float_valve.png)
<!-- slide -->
![East Boundary Municipal Water Meter & Master Isolating Valve](c:\Users\prade\OneDrive\Desktop\home plan\renders\municipal_east_water_meter_and_valve.png)
```

---

### 64.2 Engineering Architecture & Operational Workflow

To fulfill the user requirement for **immediate verification of municipal water arrival** while preserving clean water storage in the underground sump, a specialized **Dual-Tap Direct Municipal Verification & Flow Routing System** has been engineered:

```
[East Street Municipal Main] 
              │
              ▼ (25mm Blue Lever Isolating Ball Valve & Brass Water Meter)
[Incoming Service Line through East External Wall Sleeve]
              │
              ├───► [GF Kitchen Sink Tap 1: Direct Municipal Potable Swan Neck Faucet]
              │      * Function: Instant visual check when municipal water starts flowing.
              │      * Function: Draw unchlorinated, direct drinking/cooking water.
              │
              ▼ [Under-Counter Intermediate Control Shut-Off Valve (Red Lever)]
              │      * Location: Easily accessible inside the under-sink cabinet.
              │      * Function: Keep CLOSED initially to check water clarity at Tap 1.
              │      * Function: Turn OPEN to direct clean municipal water into the Sump.
              │
              ▼ (25mm CPVC Pipeline along East Foundation Setback Trench)
[Underground Sump Inflow Port (Z = +750mm)]
              │
              ├───► [Sump Maintenance Isolation Ball Valve]
              │
              ▼
[Automatic Mechanical Brass Float Ball Valve (IS 1703 - Ø150mm Ball Cock)]
              * Shuts off inflow automatically when Sump reaches high-water level (+750mm).
```

---

### 64.3 3D MEP Component Schedule

| Object Name | FreeCAD Label | Location / Coordinates (mm) | Material / Specifications | Function & Engineering Purpose |
| :--- | :--- | :--- | :--- | :--- |
| `Municipal_Water_Meter` | Municipal Water Meter (25mm Brass Revenue Dial) | $X = -350, Y = 7120, Z = 1100$ | Cast Brass Body (`#D4AF37`) with glass register dial & unions | Records incoming municipal volumetric consumption; accessible from East boundary. |
| `Valve_Municipal_Main_Boundary` | Valve: Municipal Boundary Master Shut-Off | $X = -350, Y = 6980, Z = 1100$ | Forged Brass body, Blue quarter-turn lever handle (`#0573D9`) | Master property isolation during street mains repair or maintenance. |
| `Municipal_East_Service_Pipe` | Municipal East Service Inflow Pipe | $X \in [-800, 360], Y = 7215, Z = 1100$ | $25\text{ mm}$ ($\varnothing 32\text{ mm}$ OD) SDR 11 Heavy-gauge CPVC (`#2B78C5`) | Penetrates East wall sleeve ($X = 0\rightarrow 152\text{ mm}$) into kitchen under-sink zone. |
| `GF_Kitchen_Municipal_Riser_Pipe` | GF Kitchen Municipal Supply Riser Pipe | $X = 360\rightarrow 420, Y = 7215\rightarrow 7300, Z = 1100\rightarrow 1784$ | $20\text{ mm}$ ($\varnothing 25\text{ mm}$ OD) CPVC concealed riser | Ascends through granite countertop deck to feed Tap 1. |
| `GF_Kitchen_Sink_Municipal_Tap` | GF Kitchen Sink Tap 1: Direct Municipal Potable Tap | $X = 420, Y = 7300, Z = 1784\rightarrow 1948$ | Polished Chrome (`#E0E0E0`) swan-neck faucet with aerator | **Verification Faucet**: Direct municipal water for visual flow check and drinking water collection. |
| `Kitchen_Faucet` | GF Kitchen Sink Tap 2: OHT Domestic Water Faucet | $X = 495, Y = 7300, Z = 1784\rightarrow 2022$ | Polished Chrome high-arch swivel faucet | **Domestic Faucet**: Fed from rooftop Overhead Tank for daily dishwashing and cleaning. |
| `Valve_Municipal_Sink_To_Sump` | Valve: Sink-to-Sump Flow Control Shut-Off | $X = 360, Y = 7120, Z = 1100$ | Brass quarter-turn ball valve with vivid Red lever (`#EA2027`) | **Intermediate Diverter**: Controls filling of Sump after verifying clean water at Tap 1. |
| `Municipal_Pipe_Sink_To_Sump` | Municipal Pipeline: Sink to Sump Inflow | $X = -60, Y \in [1400, 7018], Z = 750$ | $25\text{ mm}$ CPVC encased along exterior East setback plinth | Transports water from kitchen under-sink valve along foundation to Sump inlet. |
| `Valve_Sump_Inlet_Maintenance` | Valve: Sump Inlet Maintenance Isolation | $X = 260, Y = 1400, Z = 750$ | Heavy-duty Brass ball valve (`#D4AF37`) with quarter-turn handle | Local isolation valve inside Sump collar for float valve servicing. |
| `Sump_Brass_Float_Valve` | Sump Automatic Mechanical Float Ball Valve | $X \in [290, 625], Y = 1400, Z \in [575, 766]$ | Cast Brass body, bronze lever arm, $\varnothing 150\text{ mm}$ brass float ball | Shuts off incoming municipal flow when Sump reaches full storage capacity ($5,600\text{ L}$). |

---

### 64.4 Verification & Document Status

* **Master Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)
* **Total Objects in Document:** 540 objects, 0 errors, 100% valid manifold solids.
* **Recompute Status:** Single transaction recompute completed with zero invalid shapes in `Municipal_To_Sump_Plumbing_Group`.
* **Visual Audit:** Dual taps verified on kitchen sink deck, under-counter valve positioned for ergonomic access, and Sump float valve verified below plinth top slab.

---
