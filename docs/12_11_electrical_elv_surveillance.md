## 11. Electrical & ELV Surveillance Engineering Specifications

Per user instructions, all 2D TechDraw drawing sheets and 2D diagrams have been deleted from the FreeCAD model and workspace, focusing the project on the active 3D parametric BIM model. The comprehensive ceiling slab conduit routing and ergonomic modular switchboard schedules are documented below.

### 11.1 Ceiling Slab Conduit & Direct Light Point Layout (Direct Slab)

To preserve maximum vertical headroom and avoid the thermal and maintenance drawbacks of false ceilings, the electrical distribution is engineered for **Direct Concrete Slab Installation**. All conduit piping, fan hook boxes, and spotlight deep junction pots are cast directly into the $125\text{ mm}$ monolithic RCC slab during pouring.

#### A. Ceiling Fixture Coordinate Schedule (Datum: Grid 1-A / North-East Column Interior Corner)

| Fixture Tag | Fixture Description | Room / Zone | Center X (mm) | Center Y (mm) | Slab Z (mm) | Fixture Type & Wattage |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FB-1** | Heavy-Duty Ceiling Fan Hook Box | Living Room (Center) | $743.0$ | $2275.0$ | $+3962.4$ | Malleable iron fan hook box with safety clamp (50W BLDC Fan) |
| **FB-2** | Heavy-Duty Ceiling Fan Hook Box | Master Bedroom (Center) | $2271.6$ | $5650.0$ | $+3962.4$ | Malleable iron fan hook box with safety clamp (50W BLDC Fan) |
| **FB-3** | Heavy-Duty Ceiling Fan Hook Box | Kitchen & Dining (Center) | $4056.4$ | $5650.0$ | $+3962.4$ | Malleable iron fan hook box with safety clamp (50W BLDC Fan) |
| **DL-1** | Deep PVC Spotlight Junction Pot | Living Room (Entrance) | $350.0$ | $1200.0$ | $+3962.4$ | $\varnothing 75\text{ mm}$ deep pot, 7W COB Warm LED ($3000\text{K}$) |
| **DL-2** | Deep PVC Spotlight Junction Pot | Living Room (North Bay) | $350.0$ | $3200.0$ | $+3962.4$ | $\varnothing 75\text{ mm}$ deep pot, 7W COB Warm LED ($3000\text{K}$) |
| **DL-3** | Deep PVC Spotlight Junction Pot | Living Room (East Window) | $1136.0$ | $3200.0$ | $+3962.4$ | $\varnothing 75\text{ mm}$ deep pot, 7W COB Warm LED ($3000\text{K}$) |
| **DL-4** | Deep PVC Spotlight Junction Pot | Living Room (South-East) | $1136.0$ | $1200.0$ | $+3962.4$ | $\varnothing 75\text{ mm}$ deep pot, 7W COB Warm LED ($3000\text{K}$) |
| **DL-5** | Deep PVC Spotlight Junction Pot | Bedroom (Wardrobe Aisle) | $1800.0$ | $4600.0$ | $+3962.4$ | $\varnothing 75\text{ mm}$ deep pot, 9W COB Natural White ($4000\text{K}$) |
| **DL-6** | Deep PVC Spotlight Junction Pot | Bedroom (North Bedside) | $1800.0$ | $6700.0$ | $+3962.4$ | $\varnothing 75\text{ mm}$ deep pot, 7W COB Warm LED ($3000\text{K}$) |
| **DL-7** | Deep PVC Spotlight Junction Pot | Bedroom (East Bedside) | $2743.0$ | $6700.0$ | $+3962.4$ | $\varnothing 75\text{ mm}$ deep pot, 7W COB Warm LED ($3000\text{K}$) |
| **DL-8** | Deep PVC Spotlight Junction Pot | Bedroom (South-East Corner)| $2743.0$ | $4600.0$ | $+3962.4$ | $\varnothing 75\text{ mm}$ deep pot, 7W COB Warm LED ($3000\text{K}$) |
| **DL-9** | Deep PVC Spotlight Junction Pot | Kitchen (Breakfast Bar) | $3500.0$ | $4600.0$ | $+3962.4$ | $\varnothing 75\text{ mm}$ deep pot, 9W Focused Beam ($3000\text{K}$) |
| **DL-10**| Deep PVC Spotlight Junction Pot | Kitchen (Cooking Hob Counter)| $3500.0$ | $6700.0$ | $+3962.4$ | $\varnothing 75\text{ mm}$ deep pot, 9W High-CRI Cool Day ($6500\text{K}$) |
| **DL-11**| Deep PVC Spotlight Junction Pot | Kitchen (Sink & Prep Area) | $4600.0$ | $6700.0$ | $+3962.4$ | $\varnothing 75\text{ mm}$ deep pot, 9W High-CRI Cool Day ($6500\text{K}$) |
| **DL-12**| Deep PVC Spotlight Junction Pot | Kitchen (Refrigerator/Storage)| $4600.0$ | $4600.0$ | $+3962.4$ | $\varnothing 75\text{ mm}$ deep pot, 9W High-CRI Cool Day ($6500\text{K}$) |

#### B. Vertical Wall Drop Conduit Elbows (Slab to Masonry Switch Chases)

* **WD-1 (Living Main Entry):** Drop to SB-2 at $X = 228.6\text{ mm}$, $Y = 914.4\text{ mm}$.
* **WD-2 (Living TV / Entertainment Console):** Drop to SB-3 at $X = 1485.9\text{ mm}$, $Y = 2500.0\text{ mm}$.
* **WD-3 (Bedroom Entry & Dressing):** Drop to SB-9 at $X = 1485.9\text{ mm}$, $Y = 4600.0\text{ mm}$.
* **WD-4 (Bedside Two-Way Console):** Chased vertical drop inside `Bedroom_Wall_South` at $X = 2400.0\text{ mm}$, $Y = 7467.6\text{ mm}$ down to $+700\text{ mm}$ AFF ($Z = 1689.4\text{ mm}$) feeding single consolidated bedside console `SB-10`.
* **WD-4B (Bedroom South Wall Tubelight):** Chased vertical drop inside `Bedroom_Wall_South` at $X = 3500.0\text{ mm}$, $Y = 7500.0\text{ mm}$ feeding a $4\text{ ft}$ 22W T5 LED Batten Luminaire with concealed junction box mounted at $+2300\text{ mm}$ AFF ($Z = 3214.4\text{ mm}$).
* **WD-5 (Kitchen Unified Main Console):** Chased vertical drop inside `Kitchen_Wall_West` (Spine Wall) at $X = 1866.9\text{ mm}$, $Y = 4950.0\text{ mm}$ down to $+1200\text{ mm}$ AFF ($Z = 2114.4\text{ mm}$) feeding single consolidated entrance console `SB-13`.
* **WD-6 (Kitchen Food Prep Counter):** Chased vertical drop inside `Kitchen_Wall_East` at $X = 152.4\text{ mm}$, $Y = 5715.0\text{ mm}$ down to $+1150\text{ mm}$ AFF ($Z = 2064.4\text{ mm}$) feeding 6-module appliance console `SB-14` (Food Prep Counter).
* **WD-6B (Kitchen Exhaust Fan East Wall Drop):** Chased vertical drop inside `Kitchen_Wall_East` at $X = 152.4\text{ mm}$, $Y = 7320.0\text{ mm}$ down to $+1950\text{ mm}$ AFF ($Z = 2864.4\text{ mm}$) feeding recessed junction box `Kitchen_Exhaust_Fan_Junction_Box` adjacent to the exhaust fan over the sink.
* **WD-7 (Toilet Complete Slab & Wall Network):** Dedicated dropped slab conduit grid cast at $Z = 3048\text{ to }3148\text{ mm}$ (Toilet ceiling FFL). Directly fed from outside console `SB-7` via pillar bypass jog around `Col_Stair_SW`. Connects in an unbroken loop to:
  - `DL-TOILET`: Moisture-sealed ceiling downlight junction pot ($\varnothing 85\text{ mm} \times 60\text{ mm}$) at room center ($X = 4350, Y = 1000, Z = 3048\text{ mm}$).
  - `EF-TOILET`: North ventilator wall chase dropping to Exhaust Fan high-level box ($Z = 2750\text{ mm}$).
  - `SB-8`: West wall chase dropping to 16A/25A high-level Geyser power socket ($Z = 2650\text{ mm}$).

---

### 11.2 Ground Floor Ergonomic Switchboard & Distribution Board Schedule

Every switchboard is modeled in FreeCAD under `Electrical_Switchboards_Group` with precise ergonomically verified mounting heights in accordance with **IS 732: Code of Practice for Electrical Wiring Installations**:

| Board Tag | Location & Serving Zone | X Coord (mm) | Y Coord (mm) | Height AFF (mm) | Modular Gang Size | Connected Circuits & Controls |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **MDB** | Entrance Foyer North Wall | $1400.0$ | $950.0$ | $+1500\text{ mm}$ ($5'\text{-}0"$) | 12-Way Enclosure | 40A 30mA 4-Pole RCCB, 8 SP MCBs (Lighting, Power, Geyser, AC, Pump) |
| **SB-1** | Sitout Entrance Wall | $100.0$ | $850.0$ | $+1200\text{ mm}$ ($4'\text{-}0"$) | 4-Module | Sitout ceiling warm downlight, Gate pillar lights, 6A outdoor socket |
| **SB-2** | Living Room Main Entry | $250.0$ | $950.0$ | $+1200\text{ mm}$ ($4'\text{-}0"$) | 8-Module | Living Fan FB-1 speed regulator, DL-1 to DL-4 spotlights, Cove LED strip |
| **SB-3** | Living Room West Wall TV Media Unit | $4876.8$ | $3250.0$ | $+555\text{ mm}$ ($1'\text{-}10"$) [Console] & $+1150\text{ mm}$ [TV] | 8-Module + 2-Mod High | $3 \times 6/16\text{A}$ power sockets, $1 \times 6\text{A}$ UPS router socket, 4K HDMI port, dual RJ45 Gigabit LAN, FTTH fiber coupler, DTH Satellite TV Coaxial F-connector keystone port (linked to rooftop dish), 50mm cable manager sleeve |
| **SB-4** | Living Room South-East Corner | $750.0$ | $3500.0$ | $+300\text{ mm}$ ($1'\text{-}0"$) | 2-Module | 16A multipurpose utility socket for vacuum cleaner / floor lamp |
| **SB-5** | Staircase Entry Wall | $1550.0$ | $850.0$ | $+1200\text{ mm}$ ($4'\text{-}0"$) | 4-Module | Staircase Flight 1 2-way switch, Mid-landing step lights, Stair canopy LEDs |
| **SB-6** | Under-Stair Utility Station | $3450.0$ | $850.0$ | $+1200\text{ mm}$ ($4'\text{-}0"$) | 6-Module | 16A dedicated starter for 1.0 HP Sump Motor + 16A Washing Machine point |
| **SB-7** | Toilet Entrance Outer Wall (Lobby) | $3560.0$ | $1943.1$ | $+1200\text{ mm}$ ($4'\text{-}0"$) | 6-Module Console | Ceiling Downlight (6A), Exhaust Fan (6A), Vanity Mirror Light (6A), Handwash 6A Convenience Socket (2-Mod), Geyser 25A DP Isolator Switch with Red Neon Indicator |
| **SB-8** | Toilet Internal High-Level Geyser Point | $4750.0$ | $1260.0$ | $+1735\text{ mm}$ ($5'\text{-}8"$) [Z=2650mm] | 2-Module High | 16A/25A Heavy-Duty 3-Pin Socket with splash-resistant spring flap lid for Instant/Storage Water Heater (fed via 4.0 sq.mm circuit from SB-7 DP switch) |
| **SB-9** | Bedroom Entry Wall (Between Door & Wardrobe) | $3325.0$ | $4673.5$ | $+1200\text{ mm}$ ($4'\text{-}0"$) | 6/8-Module Console | BLDC Fan FB-2 speed regulator, DL-5 to DL-8 ceiling downlights, Cove/night light, 6A universal convenience socket, 2-way master bedside light switch |
| **SB-10**| Master Bedside Console (Retained) | $2400.0$ | $7467.6$ | $+700\text{ mm}$ ($2'\text{-}4"$) | 4-Module | 2-Way Fan toggle, 2-Way South Wall Tubelight toggle, Dual USB-A/C fast charger + 6A multi-pin socket |
| ~~**SB-11**~~| ~~Master Bedside Right~~ | — | — | — | Decommissioned | Removed per client request to avoid dual-bedside clutter; bedside control consolidated into SB-10 |
| ~~**SB-12**~~| ~~Bedroom Dressing & Wardrobe~~ | — | — | — | Decommissioned | Consolidated into SB-9 console between door and wardrobe |
| **SB-13**| Kitchen Main Entrance (Spine Wall) | $1866.9$ | $4950.0$ | $+1200\text{ mm}$ ($4'\text{-}0"$) | 6-Module Unified | Kitchen Primary Light, 3-Point Ceiling Downlight Array (DL-9, CL-KIT, DL-10), Breakfast Bar Pendant, Master Exhaust/Chimney switch |
| **SB-14**| Kitchen Food Prep Counter | $152.4$ | $5715.0$ | $+1150\text{ mm}$ ($3'\text{-}9"$) | 6-Module | $2 \times 16\text{A}$ modular switched sockets for Mixer-Grinder, Electric Kettle, Toaster, Blender |
| **SB-15**| Kitchen South Wall (Beside Fridge / Above L-Counter) | $1100.0$ | $7467.6$ | $+1100\text{ mm}$ ($3'\text{-}8"$) | 4-Module | 16A Dedicated refrigerator socket + 6A RO Water Purifier switch & socket |
| **SB-16**| Living Room East Wall Utility Loft | $152.4$ | $2250.0$ | $+2315.2\text{ mm}$ ($+3260.0\text{ mm}$ abs) | 4-Module | 16A Inverter Charging Socket + 6A UPS Output Socket (CCTV NVR & Wi-Fi Router) |

---

### 11.3 CCTV Surveillance System Provision & Wiring Layout (Site-Adapted)

The residential surveillance network has been custom engineered to accommodate the site's boundary conditions: **the West boundary ($X = 5029.2\text{ mm}$) and South/Rear boundary ($Y = 7620.0\text{ mm}$) are shared COMMON WALLS with adjacent properties (zero external setback).**

Accordingly, zero exterior conduits or cameras are placed on the outside of the West and South walls. All surveillance coverage is concentrated on the **North (Front Street / Canopies)**, the **East (Open Side Walkway & Windows)**, the **Rooftop Terrace**, and the **Internal Main Door Foyer**.

#### A. Camera Placement & Coverage Schedule

| Camera Tag | Camera Form Factor & Lens | Mounting Substrate & Orientation | Coordinates $(X, Y, Z)$ (mm) | Height AFF (mm) | Targeted Security Zone |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CAM-01** | 4MP IP Turret Dome ($2.8\text{ mm}, 108^\circ$) | GF Entrance Canopy Burmese Teak Soffit | $X = 600.0, Y = -400.0, Z = 3950.4$ | $+3036.0\text{ mm}$ | Main Entrance Teak Door, Sitout Safety Gate, Foundation Steps, Street Approach |
| **CAM-02** | 4MP IP Turret Dome ($2.8\text{ mm}, 108^\circ$) | GF Stair Canopy Burmese Teak Soffit | $X = 2600.0, Y = -400.0, Z = 3950.4$ | $+3036.0\text{ mm}$ | External Staircase Flight 1 Entry, Mid-Landing Ascent, Sump Motor & Washer Bay |
| **CAM-03** | 4MP IP Turret Dome ($2.8\text{ mm}, 108^\circ$) | East Portico Canopy Burmese Teak Soffit | $X = -200.0, Y = 1100.0, Z = 3950.4$ | $+3036.0\text{ mm}$ | East Boundary Setback Passage, Living Room 3-Split Window Bay & Side Portico |
| **CAM-04** | 4MP IP Bullet ($2.8\text{ mm}, 108^\circ$) | FF Balcony Canopy Burmese Teak Soffit | $X = 600.0, Y = -350.0, Z = 7123.4$ | $+3036.0\text{ mm}$ (FF) | Elevated Street Panorama, Vehicle Parking Bay, Balcony Planter & Railing Edge |
| **CAM-05** | 4MP IP Turret Dome (IP67) | Rooftop Mumty Tower South Exterior Wall | $X = 2200.0, Y = 1866.9, Z = 8600.0$ | $+1339.6\text{ mm}$ (Terrace) | Open Rooftop Terrace Slab, Pergola Trellis, Overhead Water Tank & Mumty Access Door |
| **CAM-06** | 4MP IP Turret Dome ($2.8\text{ mm}, 112^\circ$) | Indoor Living Room Ceiling Foyer | $X = 800.0, Y = 2200.0, Z = 3962.4$ | $+3048.0\text{ mm}$ | Indoor Main Door Entry Foyer, Living Room Lounge & TV Entertainment Console |

#### B. Wiring Architecture & Infrastructure Specifications

1. **Power over Ethernet (PoE - IEEE 802.3af/at):**
   * Every camera receives both gigabit IP digital video and 48V DC power over a single **Cat6 UTP solid bare copper cable**.
   * Completely eliminates 230V AC wiring or outdoor adapters at camera locations, enhancing electrical safety and weather resistance.
2. **Dedicated ELV Conduit Network:**
   * Heavy-gauge **$20\text{ mm}$ rigid PVC conduits** embedded in concrete slabs and recessed in brick wall chases, colored in high-visibility purple (`#6C5CE7`) for Extra Low Voltage (ELV) distinction.
   * Conduits route entirely along the North and East slabs and interior walls, strictly avoiding the West and South common boundary walls.
   * Maintained $>200\text{ mm}$ ($8"$) physical separation from high-voltage 230V AC conduits to prevent electromagnetic interference (EMI) and video signal degradation.
   * IP66 circular weatherproof junction boxes ($\varnothing 100\text{ mm} \times 40\text{ mm}$) at every camera point housing waterproof RJ45 modular couplers.
3. **Central NVR Hub & UPS Emergency Power Station (East Wall Full-Width Utility Loft):**
   * Configured across the **full clear room width of the East Living Room Wall** ($Y = 1943.1\text{ mm}$ to $5067.3\text{ mm}$, clear span = $3124.2\text{ mm}$ / $10'\text{-}3"$; projection = $600.0\text{ mm}$ / $2'\text{-}0"$, $X \in [152.4, 752.4\text{ mm}]$).
   * **Monolithic Lintel-Chajja Structural Integration:** Cast at standard door/window lintel level ($Z = 3048.0\text{ mm}$ to $3123.0\text{ mm}$ / $75\text{ mm}$ RCC slab). The indoor loft ($600\text{ mm}$ projection) counterbalances the outdoor window sunshade chajja ($450\text{ mm}$ projection) over the $152.4\text{ mm}$ East wall, tied monolithically into the continuous lintel band supported at `Col_East_Sitout` (North) and `Col_East_Kitchen` (South).
   * **Window Light & Headroom Preservation:** Positioned entirely above the 3-track sliding window ($Z \in [1848.0, 3048.0\text{ mm}]$), ensuring 100% unhindered natural sunlight and ventilation. Provides $+2103.1\text{ mm}$ ($+6'\text{-}11"$) clear headroom AFF below and $839.4\text{ mm}$ ($2'\text{-}9"$) vertical overhead clearance to the ceiling slab.
   * **Dual Functional Zoning ($20.2\text{ sq.ft}$ / $1.87\text{ m}^2$ Total Usable Deck):**
     - **North MEP Station ($Y \in [1943.1, 2600\text{ mm}]$):** Dedicated security and emergency power hub housing the NVR, UPS Inverter, 150Ah Tubular Battery, and `SB-16` switchboard.
     - **Central & South Storage Deck ($Y \in [2600, 5067.3\text{ mm}]$):** Over $2.46\text{ m}$ ($8'\text{-}1"$) of continuous heavy-duty overhead storage for luggage, seasonal items, and household goods, neatly recessed above eye level.
   * **8-Channel 4K Ultra-HD PoE NVR Hub (`CCTV_NVR_Hub_Model`):**
     - 4TB surveillance-grade Western Digital Purple / Seagate SkyHawk HDD supporting 30+ days continuous loop recording.
     - 8 gigabit PoE ports directly powering all 6 IP turret dome and bullet cameras.
     - Direct high-speed concealed HDMI feed across the ceiling slab down to the West TV Console (`SB-3`) for 4K quad/live monitoring on the living room smart TV.
   * **Integrated UPS Emergency Power Backup System (`CCTV_UPS_Power_Backup_Model`):**
     - **1.1kVA Pure Sine Wave Digital Inverter** ($X \in [220, 500\text{ mm}], Y \in [2300, 2600\text{ mm}], Z \in [3123, 3253\text{ mm}]$): Features smart micro-controller telemetry, high-efficiency copper transformer, and instantaneous $<10\text{ ms}$ grid-to-battery transfer switch ensuring zero camera reboot or data loss during power outages.
     - **150Ah Tall Tubular Deep-Cycle Battery** ($X \in [230, 420\text{ mm}], Y \in [2670, 3175\text{ mm}], Z \in [3123, 3558\text{ mm}]$): Equipped with 6 visible float hydrostatic electrolyte vent caps, heavy-duty lead terminal posts, and acid-resistant polypropylene casing.
     - **Backup Autonomy:** Delivers $>12\text{ hours}$ of continuous power to the NVR, all 6 PoE cameras, and the optical fiber broadband router.
   * **Dedicated Electrical Service (`SB-16`):**
     - Mounted directly on the East brick masonry wall at $X = 152.4\text{ mm}, Y = 2250.0\text{ mm}, Z = 3260.0\text{ mm}$ ($+137\text{ mm}$ above loft slab).
     - Equipped with a 16A heavy-duty switched socket for inverter input charging and a 6A filtered output socket for the NVR hub and router.

#### C. 100% Concealed Wiring & Zero Surface Exposure Construction Details

To preserve the pristine modern facade and prevent vandalism or weather deterioration, **zero conduits, wires, or surface casings are exposed on any exterior wall or ceiling**:

```
[ CONCRETE SLAB CORE (Z = 4025 mm) ]  <=== 20mm Rigid PVC Conduit cast inside RCC slab
              |
              | (Vertical drop inside wood soffit cavity)
              v
[ 12mm TEAK WOOD SOFFIT ]             <=== Flush recessed circular IP66 J-Box (Z = 3950 mm)
              |
              v
[ 4MP IP TURRET CAMERA ]              <=== Sleek camera body & mounting collar (ZERO wire exposed)
```

1. **Pre-Cast Slab Embedded Conduits:**
   * All horizontal conduit runs for `CAM-01`, `CAM-02`, `CAM-04`, and `CAM-06` are embedded directly inside the $125\text{ mm}$ monolithic RCC slab core ($Z = 4025\text{ mm}$ for Ground Floor, $Z = 7200\text{ mm}$ for First Floor).
   * Conduits are laid over the bottom rebar mat before casting concrete, fully encapsulated within the concrete mass.
2. **Canopy Wood Soffit Cavity Integration:**
   * Under the Ground Floor Entrance Canopy and First Floor Balcony, junction boxes are **recessed flush behind the $12\text{ mm}$ Burmese Teak Wood Soffit**.
   * The Cat6 PoE cable and RJ45 waterproof coupler remain 100% concealed inside the ceiling cavity above the wood panel.
   * Only the compact camera turret and flush collar ring extend below the teak wood ceiling.
3. **Concealed Masonry Chases (Internal Mumty & Wall Plastering):**
   * For the Rooftop Mumty camera (`CAM-05`), the junction box is recessed $50\text{ mm}$ flush into the exterior South brick wall ($Y = 1866.9\text{ mm}$), and the conduit drops vertically inside a $25\text{ mm} \times 25\text{ mm}$ chase cut into the brickwork masonry on the **interior Mumty staircase side** directly down into the Terrace RCC slab core ($Z = 7260.4\text{ mm}$).
   * Junction boxes are recessed flush with the plaster line (`CCTV IP66 Recessed Concealed Junction Boxes (White)`). The camera baseplate bolts directly over the recessed box with a silicone rubber gasket, completely concealing the wall cavity and cable pigtail.
4. **Internal Vertical Conduit Riser Pier & Transverse Slab Run to West TV Unit:**
   * Cabling from the Rooftop Mumty (`CAM-05`) and First Floor Balcony (`CAM-04`) descends through an internal vertical conduit sleeve cast inside the solid $228.6\text{ mm}$ ($9"$) interior masonry pier between the main door frame and column (`X = 1600.0\text{ mm}, Y = 1800.0\text{ mm}`).
   * Conduits route seamlessly inside the Ground Floor ceiling slab core ($Z = 4025.0\text{ mm}$) directly to the central hub point directly above the East wall utility loft ($X = 360.0\text{ mm}, Y = 2050.0\text{ mm}$).
   * All 6 Cat6 cables drop vertically from the ceiling slab core straight into the NVR chassis on the loft through an internal concealed chase.
   * **Transverse Ceiling Slab Conduit to West TV Unit (`SB-3`):** A dedicated $25\text{ mm}$ rigid PVC conduit routes across the monolithic Ground Floor ceiling slab core from the East loft hub ($X = 360.0\text{ mm}, Y = 2050.0\text{ mm}, Z = 4025.0\text{ mm}$) directly across the living room ceiling to the West wall intersection point ($X = 4850.0\text{ mm}, Y = 3250.0\text{ mm}, Z = 4025.0\text{ mm}$). It drops vertically down an internal masonry chase cut into the room plaster face of the West wall into `SB-3` at $Z = 1520.0\text{ mm}$, carrying high-speed 4K HDMI video and Gigabit Cat6 LAN data links.
   * **FTTH Broadband Fiber Optic Service Entry:** A dedicated $20\text{ mm}$ conduit enters from the road-side front sitout plinth ($X = 4850.0\text{ mm}, Y = 0.0\text{ mm}, Z = 944.9\text{ mm}$) and runs concealed in the floor screed along the West perimeter directly up into `SB-3`.

#### D. Rooftop DTH Dish TV Antenna, Weatherproof Service Cowl & Continuous Vertical Conduit Pipeline

To fulfill the user requirement for **uninterrupted Dish TV satellite television and high-speed FTTH optical fiber internet connectivity without visible cables or exterior wall penetration on the common boundary**, a dedicated multi-storey telecommunications riser pipeline has been modeled:

```
[ ROOFTOP DTH DISH ANTENNA (Z = 8310 - 8887 mm) ]  <=== Clamped on West Parapet Coping
                     | (Coaxial RG-6 Drop)
                     v
[ IP65 WEATHERPROOF TERMINAL COWL (Z = 8180 mm) ]   <=== Downward Drip Loop on Inner Parapet Face
                     |
                     | 25mm Heavy-Gauge Rigid PVC Conduit
                     | (Continuous straight vertical drop: 6.62 m / 21'-9")
                     | (Recessed 100% inside internal room plaster chase)
                     |
                     +--- Passes through First Floor West Wall Chase (Z = 4087 - 7135 mm)
                     |
                     +--- Passes through Intermediate RCC Slab Core (Z = 3962 - 4087 mm)
                     |
                     v
[ GROUND FLOOR WEST TV MEDIA CENTER (SB-3) ]        <=== Direct entry into media console (Z = 1520 mm)
                     ▲
                     | (FTTH Optical Fiber Inlet Conduit from Sitout Plinth Z = 945 mm)
```

1. **Rooftop DTH Satellite Dish TV Antenna (`Terrace_Dish_TV_Antenna`):**
   * **Reflector:** Standard $\varnothing 650\text{ mm}$ ($2'\text{-}2"$) offset parabolic dish reflector stamped from corrosion-resistant galvannealed steel and finished with UV-stabilized electrostatic polyester powder coat (`#DCE1E7`).
   * **Elevation & Azimuth Alignment:** Pre-tilted at $45^\circ$ elevation angle, oriented South-East towards Indian geostationary broadcast satellites (GSAT-15 @ $93.5^\circ\text{E}$ for Tata Play / DD FreeDish; SES-7 / MEASAT-3 @ $91.5^\circ\text{E}$ for Airtel Digital TV; ST-2 @ $88.0^\circ\text{E}$ for Videocon D2H).
   * **Mounting Mast & Parapet Clamp:** $\varnothing 38\text{ mm} \times 2.0\text{ mm}$ galvanized tubular steel mast anchored securely via a heavy-duty saddle clamp bracket directly over the reinforced concrete coping beam of the West parapet wall at $X \in [4451.8, 5063.96\text{ mm}]$, $Y \in [2985.9, 3554.8\text{ mm}]$, $Z \in [8310.4, 8887.3\text{ mm}]$. This elevation places the dish well above the rooftop parapet, providing a $100\%$ obstruction-free line of sight over all adjacent building rooftops.
   * **LNB Subsystem:** Ku-band Universal Twin-Output Low Noise Block (LNB) ($10.70 - 12.75\text{ GHz}$, Local Oscillator $9.75 / 10.60\text{ GHz}$, Noise Figure $\le 0.3\text{ dB}$) mounted on an aluminum support boom arm with integrated drip-seal boot. Twin outputs allow independent dual-tuner recording or multi-room feeds.

2. **Terrace Weatherproof Telecom Terminal Cowl (`Terrace_Telecom_Service_Cowl`):**
   * **Enclosure:** High-impact UV-stabilized polycarbonate terminal box ($120\text{ mm} \times 70\text{ mm} \times 200\text{ mm}$, `#F8FAFC`, IP65 rated) mounted flush on the **inner room plaster face** of the West parapet wall at $X = 4840.0\text{ mm}, Y = 3250.0\text{ mm}, Z = 8180.0\text{ mm}$ (immediately beneath the parapet coping).
   * **Downward Gooseneck Drip Cowl:** The entry aperture is fitted with a downward-facing gooseneck cowl and silicone elastomer compression grommet. Incoming RG-6 coaxial cables form a physical drip loop before entering the cowl, making it impossible for wind-driven monsoon rainwater to enter the conduit riser.

3. **Continuous Multi-Storey Vertical Riser Conduit Pipeline (`Roof_to_TV_Service_Conduit`):**
   * **Specifications:** Heavy-gauge **$25\text{ mm}$ outer-diameter rigid PVC conduit** (Medium/Heavy Mechanical Stress Grade as per IS 9537 Part 3), colored in vivid telecom blue (`#0A84E3`).
   * **Unbroken Vertical Path:** Runs a continuous straight drop of **$6.62\text{ m}$ ($21'\text{-}9"$)** from the rooftop cowl ($Z = 8140.0\text{ mm}$) down through the First Floor living/staircase wall chase ($Z = 4087.4$ to $7135.4\text{ mm}$), penetrates the intermediate Ground Floor ceiling RCC slab core ($Z = 3962.4$ to $4087.4\text{ mm}$), and descends down the Ground Floor internal West wall chase directly into `SB-3` behind the TV media console ($Z = 1520.0\text{ mm}$).
   * **Zero Bends / Effortless Cable Pulling:** Because the West wall on the Ground Floor, First Floor, and Terrace parapet are in **100% plumb vertical alignment** ($X = 4876.8\text{ mm}, Y = 3250.0\text{ mm}$), the conduit has **zero horizontal offsets and zero 90-degree elbows**. Cable pulling via nylon fish tape is effortless with zero friction, allowing effortless future cable replacement without opening any plaster or tiles.
   * **Dual Service Segregation & Fill Ratio:**
     - 1 $\times$ RG-6 Quad-Shielded 75-Ohm coaxial satellite cable ($\varnothing 7.0\text{ mm}$, copper-clad steel center conductor, 3.0 GHz rated).
     - 1 $\times$ FTTH 2-core outdoor armored fiber optic drop cable ($\varnothing 3.0\text{ mm} \times 5.0\text{ mm}$ flat figure-8 or $\varnothing 4.0\text{ mm}$ round).
     - Pre-installed 18-gauge galvanized steel fish draw wire for future cable pulls.
     - Total cable cross-sectional area: $\approx 55\text{ mm}^2$ inside a $25\text{ mm}$ conduit ($314\text{ mm}^2$ internal area) $\rightarrow$ **$17.5\%$ conduit fill ratio**, well below the National Building Code (NBC) maximum limit of $40\%$, guaranteeing optimal thermal dissipation and low pulling tension.

4. **Common Boundary Wall Absolute Zero-Exposure Compliance:**
   * The West property line ($X = 5029.2\text{ mm}$) is a shared party wall.
   * Both the vertical conduit chase and switchbox recesses are cut exclusively into the internal room plaster face ($X = 4876.8\text{ mm}$), leaving the structural brick core ($152.4\text{ mm}$ / $6"$) and common wall boundary completely intact, soundproof, and unpenetrated.
   * Zero exterior pipes, zero exterior brackets, zero exterior wires visible from the outside.
   * **Result:** 100% invisible wiring from all angles inside and outside, with zero exposed cables anywhere in the living room or exterior facades, and strictly zero conduits on the common wall exterior.

---
