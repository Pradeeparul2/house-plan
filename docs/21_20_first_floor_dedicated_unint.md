## 20. First Floor Dedicated Uninterruptible Power Supply (UPS) System & Utility Loft

To guarantee 100% independent emergency backup power during grid power failures without sharing or cross-feeding from the Ground Floor EB connection, a **dedicated First Floor UPS Inverter and Battery system** has been fully integrated:

### 20.1 Structural & Architectural Accommodation
* **Monolithic RCC East Utility Loft (`FF_Living_Room_Loft_East`):**
  - **Location:** Spans the East wall of the First Floor Living Room ($X \in [152.4, 752.4\text{ mm}]$, $Y \in [1943.1, 5067.3\text{ mm}]$).
  - **Dimensions:** Width = $600\text{ mm}$ ($2'\text{-}0"$), Length = $3124.2\text{ mm}$ ($10'\text{-}3"$), Slab Thickness = $75\text{ mm}$ ($3"$), Elevation $Z = 6221.0 - 6296.0\text{ mm}$.
  - **Structural Integration:** Cast monolithically with the continuous RCC lintel band `FF_Continuous_Lintel_East_Wall` at $+2.13\text{ m}$ AFF, perfectly mirroring the Ground Floor East utility loft.
  - **Benefits:** Keeps the heavy battery and inverter completely off the floor (saving usable living space), naturally ventilated near the ceiling, and safe from children and water.

### 20.2 UPS Equipment & Electrical Integration
* **1.1kVA Pure Sine Wave Inverter (`FF_UPS_Power_Backup_Model`):**
  - High-efficiency inverter chassis ($286 \times 300 \times 130\text{ mm}$) finished in Metallic Blue (`#1B4F72`), delivering clean pure sine wave AC power safe for sensitive electronics (laptops, smart TVs, Wi-Fi routers).
* **150Ah Tall Tubular Deep-Cycle Battery:**
  - Heavy-duty deep-cycle battery cabinet ($190 \times 505 \times 410\text{ mm}$) finished in Appliance White (`#F4F6F7`) with 6 hydro float electrolyte level indicators in safety red (`#C0392B`). Provides $4 - 6\text{ hours}$ of backup under standard residential load.
* **Dedicated 20mm PVC Feed & Backup Pipeline (`FF_UPS_Conduit_Pipeline`):**
  - Heavy-gauge $20\text{ mm}$ rigid PVC conduit running directly between `FF_MDB` ($X = 1480.0, Y = 1900.0, Z = 5587.4\text{ mm}$) and the East utility loft.
  - Houses:
    - 1 $\times$ 16A Inverter AC charging input line (from Circuit 1 of `FF_MDB`)
    - 1 $\times$ Inverter AC emergency backup output line (feeding the isolated UPS sub-bus in `FF_MDB`)
    - 1 $\times$ $2.5\text{ sq.mm}$ green earth continuity conductor
* **Automatic Changeover & Manual Bypass Switch:**
  - Integrated into `FF_MDB`, ensuring zero-gap transfer upon power outage ($< 15\text{ ms}$ switchover) and an ergonomic manual bypass knob for easy maintenance without interrupting mains grid power.

### 20.3 Connected First Floor Emergency Backup Load Schedule
| Room | Connected Backup Loads | Watts (Avg) |
| :--- | :--- | :---: |
| **Living Room** | 1 $\times$ BLDC Ceiling Fan + 2 $\times$ 9W LED Downlights | $48\text{ W}$ |
| **Living Room TV / Tech** | Wi-Fi 6 Router + Fiber ONT + 1 Phone Charger | $25\text{ W}$ |
| **Bedroom** | 1 $\times$ BLDC Ceiling Fan + 1 $\times$ Bedside Reading Lamp + Phone Charger | $45\text{ W}$ |
| **Kitchen** | 1 $\times$ 9W LED Ceiling Downlight | $9\text{ W}$ |
| **Staircase / Balcony** | 1 $\times$ Staircase Entry Security Light | $9\text{ W}$ |
| **Total Continuous Load** | | **$136\text{ W}$** |
| **Estimated Backup Duration** | **$150\text{Ah} \times 12\text{V} \times 0.8 / 136\text{W} \approx 10.5\text{ Hours}$** | **$8 - 11\text{ Hours}$** |

```carousel
![Close-Up View of First Floor East Utility Loft Showing 1.1kVA Inverter and 150Ah Battery](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\first_floor_ups_closeup.png)
<!-- slide -->
![Two-Storey Overview Showing Symmetrical Ground and First Floor UPS Installations](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\dual_ups_two_storey_overview.png)
```

### 20.4 Dedicated First Floor UPS Modular Switch Box (`FF_SB_UPS`)
To complete the electrical power connection for the inverter, a **dedicated modular UPS switch box (`FF_SB_UPS`)** was modeled directly on the East wall adjacent to the inverter unit:

* **Location & Elevation:**
  - **Wall:** Living Room East wall plaster face ($X \in [152.4, 164.4\text{ mm}]$, $Y \in [2220.0, 2420.0\text{ mm}]$).
  - **Elevation:** $Z = 6430.0 - 6530.0\text{ mm}$ ($+134\text{ mm}$ above the loft slab top $Z = 6296.0\text{ mm}$, or $+2.39\text{ m}$ AFF).
  - **Plate Specifications:** $200 \times 100 \times 12\text{ mm}$ modular flush faceplate in Crisp White (`#FFFFFF`).
* **Electrical Outlets & Controls Integrated:**
  1. **16A Inverter AC Input Charging Socket:** 3-pin heavy-duty socket accepting the inverter's power cord plug.
  2. **16A Master Power Control Switch:** Heavy-duty rocker switch with an illuminated red neon indicator.
  3. **16A Inverter Output Backup Socket:** Dedicated return outlet feeding the inverter's emergency AC output back through the conduit into the `FF_MDB` UPS sub-bus.
* **Direct Conduit Drop:** The $20\text{ mm}$ rigid PVC conduit pipeline `FF_UPS_Conduit_Pipeline` drops vertically from the ceiling corner ($Z = 6580.0\text{ mm}$) straight into the top knock-out of this switch box at $Z = 6530.0\text{ mm}$, ensuring zero exposed wiring.

```carousel
![Close-Up View Showing the Dedicated First Floor UPS Switch Box on the East Wall](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\ff_ups_switchbox_closeup.png)
<!-- slide -->
![Angled Perspective Showing the Inverter, Battery, Dedicated Switch Box, and Conduit Pipeline](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\ff_ups_switchbox_perspective.png)
```

---
