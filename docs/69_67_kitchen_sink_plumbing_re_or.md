## 67. Kitchen Sink Plumbing Re-Orientation: East-Side Tap Relocation & Direct Chase Feed

> [!NOTE]
> **System Modification:** Kitchen Sink Tap Relocation from South Side to East Side  
> **Source Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Parent Group:** `Plumbing & Water Distribution Network` (`Master_Plumbing_Network_Group`)  
> **Updated Components:**  
>   * `Kitchen_Faucet` (GF OHT Domestic High-Arch Swivel Faucet)
>   * `GF_Kitchen_Sink_Municipal_Tap` (GF Direct Municipal Verification Tap)
>   * `FF_Kitchen_Sink_OHT_Domestic_Tap` (FF OHT Domestic High-Arch Swivel Faucet)
>   * `Downtake_Kitchen_Riser_Shaft` (Line B Kitchen Gravity Down-take)
>   * `Valve_GF_Kitchen_Isolate` & `Valve_FF_Kitchen_Isolate` (Under-Counter Domestic Isolation Valves)
>   * `GF_Kitchen_Municipal_Riser_Pipe` & `Valve_Municipal_Sink_To_Sump` (Direct Potable Line & Diverter Valve)
>   * `Municipal_Pipe_Sink_To_Sump` (Inflow & Sump Divert Pipeline)
> **Compliance & Standards:** IS 2065 (Water Supply in Buildings), IS 15778 (CPVC Plumbing), NBC 2016 Part 9 Section 1.

---

### 67.1 Visual Portfolio: East-Side Kitchen Tap Layout

```carousel
![Close-Up 3D View: Kitchen Sink Dual Taps Mounted on East Counter Deck](c:\Users\prade\OneDrive\Desktop\home plan\renders\kitchen_sink_east_taps_closeup.png)
<!-- slide -->
![Top-Down Plan View: Taps on East Side Facing West with South Side 100% Clear](c:\Users\prade\OneDrive\Desktop\home plan\renders\kitchen_sink_east_taps_top_plan.png)
<!-- slide -->
![Building Isometric X-Ray View: 50% Opacity Translucent Walls & East Plumbing](c:\Users\prade\OneDrive\Desktop\home plan\renders\building_isometric_east_kitchen_taps.png)
```

---

### 67.2 Engineering Rationale & Architectural Benefits

1. **Natural Ergonomic Alignment for the User**:
   - The kitchen sink is recessed into the granite countertop along the East wall ($X \in [270, 720]\text{ mm}$, $Y \in [6940, 7370]\text{ mm}$).
   - The user stands on the West side of the counter facing East towards the wall/window.
   - Relocating the faucets to the **East deck** ($X = 215\text{ mm}$) places them directly facing the user, with both spouts arching in the $+X$ direction (westward) directly over the center of the sink basin.
2. **100% Clearance on the South Side**:
   - Previously, faucets and supply pipes were routed along the South side of the sink ($Y \approx 7270 - 7300\text{ mm}$) towards the South partition wall.
   - By moving all faucets and risers to the East side, the South rim and South counter space are **100% free of all plumbing lines, pipes, and valves**, preventing clutter in the corner.
3. **Ultra-Short Direct Pipe Route**:
   - The main kitchen gravity down-take (`Line B`) runs in the external East setback chase at $X = -60\text{ mm}, Y = 7180\text{ mm}$.
   - Mounting the faucets on the East deck ($X = 215\text{ mm}$) enables an ultra-short, straight through-wall penetration ($275\text{ mm}$ length), completely eliminating long horizontal pipe detours under the counter.
4. **Structural Safeguards (0 Column & Beam Clashes)**:
   - The East wall penetration occurs at $Z = 1710\text{ mm}$ (clear below the window sill band at $Z = 1773.0\text{ mm}$).
   - The subgrade municipal divert line runs through brickwork above the plinth beam at $Z = 1050\text{ mm}$, drops vertically in the exterior setback chase at $X = -60\text{ mm}$, and travels subgrade at $Z = 480\text{ mm}$ below the plinth beam ($Z = 614.4\text{ mm}$).
   - **Automated Collision Result**: Exactly **0 clashes** across all 37 structural columns and 9 concrete beams.

---

### 67.3 Updated Kitchen Plumbing Geometric Coordinates

| Component Name | Description | Placement Coordinates (mm) | Spout / Flow Direction | Function |
| :--- | :--- | :--- | :--- | :--- |
| `Kitchen_Faucet` | GF OHT Domestic Faucet | Base: $(215, 7190, 1784)$, Top: $Z = 2004$ | Reaches $+X$ (West) by $180\text{ mm}$ to $X = 406$ | Daily domestic washing from OHT. |
| `GF_Kitchen_Sink_Municipal_Tap` | GF Potable Verification Tap | Base: $(215, 7070, 1784)$, Top: $Z = 1940$ | Reaches $+X$ (West) by $140\text{ mm}$ to $X = 365$ | Direct municipal drinking water verification. |
| `FF_Kitchen_Sink_OHT_Domestic_Tap` | FF OHT Domestic Faucet | Base: $(215, 7180, 4950)$, Top: $Z = 5170$ | Reaches $+X$ (West) by $180\text{ mm}$ to $X = 406$ | First Floor domestic kitchen faucet. |
| `Valve_GF_Kitchen_Isolate` | GF Domestic Isolation Valve | $(215, 7150, 1710)$, Red Lever in Y | Shut-off on East deck riser | Independent domestic shut-off under GF sink. |
| `Valve_FF_Kitchen_Isolate` | FF Domestic Isolation Valve | $(140, 7180, 4800)$, Red Lever in X | Shut-off on FF East branch | Independent domestic shut-off under FF sink. |
| `Valve_Municipal_Sink_To_Sump` | Municipal Diverter Valve | $(215, 7030, 1050)$, Red Lever in Y | Shut-off / Divert to Sump | Controls flushing/divert to underground sump. |
| `Downtake_Kitchen_Riser_Shaft` | Line B Kitchen Down-take | $X \in [-60, 3550], Y \in [-120, 7202]$ | Direct East wall penetration at $Y = 7180$ | 100% zero South wall pipes; zero column clashes. |
| `GF_Kitchen_Municipal_Riser_Pipe` | Municipal Potable Riser | $X = 215, Y = 7070, Z = 1050 \rightarrow 1784$ | Vertical riser along East wall | Supplies potable water to East municipal tap. |
| `Municipal_Pipe_Sink_To_Sump` | Municipal Inflow & Sump Divert | $X \in [-60, 396], Y \in [1400, 7070]$ | Subgrade at $Z = 480$, Penetrates at $Z = 1050$ | Inflow from East road main + subgrade divert. |

---

### 67.4 Verification & Document Status

* **Document File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)
* **Total Objects in Document:** 574 objects, 0 errors, 100% valid manifold solids.
* **Structural Clash Status:** 0 clashes detected across all structural columns, plinth beams, and lintel/sill bands.
* **Architectural Visibility:** All 84 walls active at 50% opacity, providing continuous visual access to internal pipes and columns.


---
