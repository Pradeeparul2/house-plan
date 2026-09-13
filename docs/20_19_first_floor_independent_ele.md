## 19. First Floor Independent Electricity Board (EB) Service & Electrical Infrastructure (IS 732 & NBC 2016 Compliance)

In accordance with municipal building standards and Indian Electricity Rules (IS 732: Code of Practice for Electrical Wiring Installations), the **First Floor is configured with a 100% independent Electricity Board (EB) service connection**, completely decoupled from the Ground Floor meter for autonomous billing, dedicated protection, and rental versatility:

### 19.1 Independent EB Service Architecture
* **Dual Energy Meter Board at Ground Plinth:** The ground floor electrical panel accommodates two separate tariff meters: **Meter 1 (Ground Floor)** and **Meter 2 (First Floor)**.
* **Dedicated 32mm Armored Mains Riser (`FF_EB_Service_Mains_Riser`):** A heavy-duty $32\text{ mm}$ rigid conduit runs vertically up the staircase service shaft from the ground plinth ($Z = 914.4\text{ mm}$) to the First Floor MDB ($Z = 5587.4\text{ mm}$, AFF $+1.5\text{ m}$). It houses a $4\text{-core } 10\text{ sq.mm}$ copper armored cable supplying independent single-phase / 3-phase power.
* **First Floor Main Distribution Board (`FF_MDB`):**
  - **Location:** Living Room North entrance wall ($X = 1480.0\text{ mm}, Y = 1900.0\text{ mm}, Z = 5427.4 - 5747.4\text{ mm}$).
  - **Enclosure:** 8-way SPN powder-coated metal enclosure with acrylic door.
  - **Protection:** 63A 2-Pole Main Isolator + 30mA RCCB / ELCB shock prevention breaker.
  - **6 Dedicated Sub-Circuits:**
    - Circuit 1 (10A Type C MCB): Living Room & Balcony Ceiling Fans & Downlights
    - Circuit 2 (10A Type C MCB): Bedroom Lighting & Bedside Sockets
    - Circuit 3 (16A Type C MCB): Kitchen Microwave, Mixer & Utility Outlets
    - Circuit 4 (25A Type C MCB): Bedroom 1.5-Ton Inverter Air Conditioner
    - Circuit 5 (20A Type C MCB): Attached Toilet 25-Litre Storage Geyser
    - Circuit 6 (10A Type C MCB): Stairwell & Terrace Access Exterior Lighting

### 19.2 First Floor Ceiling Slab Conduit & Lighting Layout
* **Ceiling Fan Hook Boxes (`FF_Electrical_Slab_Fan_Boxes`):** 3 heavy-duty octagonal boxes with integrated MS anchor hooks ($Z = 7135.4 - 7200.4\text{ mm}$) at Living Room center ($X = 2514.6, Y = 3257.4$), Bedroom center ($X = 3480.0, Y = 6070.0$), and Kitchen center ($X = 1050.0, Y = 6325.0$).
* **Recessed Downlight Pots (`FF_Electrical_Slab_Light_Pots`):** 12 deep PVC pot boxes ($R = 42.5\text{ mm}, H = 60\text{ mm}$) cast flush into the roof slab for ambient $3000\text{K}$ LED spot lighting (4 in Living Room, 4 in Bedroom, 2 in Kitchen, 1 in Toilet, 1 in Balcony).
* **Slab Conduit Network (`FF_Electrical_Slab_Conduit_Network`):** Heavy-gauge $25\text{ mm}$ rigid PVC pipe runs ($Z = 7193.0\text{ mm}$) forming direct star routes between `FF_MDB`, fan boxes, light pots, and perimeter wall drops.
* **Vertical Wall Drops (`FF_Electrical_Slab_Wall_Drops`):** 6 pre-formed vertical pipe drops ($Z = 6893.0 - 7193.0\text{ mm}$) cast through the beam soffits directly into wall chases.
* **10 Modular Switchboards (`FF_SB-1` to `FF_SB-10`):** Ergonomically placed throughout the living room, bedroom, kitchen, and bathroom.
* **Privacy Assurance (Zero CCTV on First Floor):** Strictly per client specifications, the CCTV surveillance network is **not extended** into the First Floor, ensuring total personal privacy for the upper residence.

```carousel
![Two-Storey 3D Perspective Showing Ground & First Floor Electrical Pipeline Networks](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\two_storey_electrical_pipelines.png)
<!-- slide -->
![Close-Up View of First Floor Slab Conduit Layout, Fan Boxes, Downlight Pots, and Wall Drops](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\first_floor_electrical_closeup.png)
<!-- slide -->
![Front Elevation Revealing Multi-Storey Vertical Electrical Drops and Dedicated EB Riser](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\two_storey_electrical_front.png)
```

### 19.3 Perfect Vertical Stacking & Alignment of GF & FF Distribution Boards
Following client instruction, the **Ground Floor Main Distribution Board (`GF_MDB`) was repositioned** from its previous location ($X \in [400, 700\text{ mm}]$) to align in **100% plumb vertical symmetry with the First Floor MDB**:

| Property | Ground Floor MDB (`GF_MDB`) | First Floor MDB (`FF_MDB`) | Vertical Alignment |
| :--- | :---: | :---: | :---: |
| **Plan Position ($X$)** | $1480.0 - 1720.0\text{ mm}$ | $1480.0 - 1720.0\text{ mm}$ | **Identical (100% Plumb)** |
| **Plan Position ($Y$)** | $1900.0 - 1960.0\text{ mm}$ | $1900.0 - 1960.0\text{ mm}$ | **Identical (100% Plumb)** |
| **Elevation ($Z$)** | $2254.4 - 2574.4\text{ mm}$ | $5427.4 - 5747.4\text{ mm}$ | $+3173.0\text{ mm}$ (Exact Story Height) |
| **Height AFF** | $+1500.0\text{ mm}$ ($5'\text{-}0"$) | $+1500.0\text{ mm}$ ($5'\text{-}0"$) | Ergonomic Eye-Level Access |
| **Enclosure Size** | $240 \times 60 \times 320\text{ mm}$ (8-Way SPN) | $240 \times 60 \times 320\text{ mm}$ (8-Way SPN) | Matching Standard Specs |

**On-Site Construction Benefits:**
1. **Single Straight Vertical Wall Chase:** The heavy-duty armored EB supply cables from the dual outdoor meter board enter the building at Column C2 and travel up a single, straight vertical chase, branching directly into `GF_MDB` and continuing straight up to `FF_MDB` with zero bends or friction.
2. **Direct Slab Drop Alignment:** Ground Floor vertical drop `Drop 0` ($X = 1600.0, Y = 1943.1\text{ mm}$) drops directly into the top of `GF_MDB`, eliminating horizontal conduit jogs across the room.
3. **Consistent Architectural Ergonomics:** Whether entering the ground residence or upper floor, the main isolator and circuit breakers are located in the identical intuitive spot next to the entrance door.

```carousel
![Isometric View Showing Both GF and FF MDBs Vertically Aligned on the Entrance Wall](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\mdb_vertical_stack_gf_ff.png)
<!-- slide -->
![Front Elevation Demonstrating Plumb Vertical Stacking of Ground and First Floor Electrical Networks](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\two_storey_electrical_with_aligned_mdb.png)
```

---
