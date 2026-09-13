## 40. Ground Floor Toilet (4'-0" x 6'-0") Architectural, MEP & Plumbing Pipeline System

Following client directive (*"show toilet and pipelines"*), the complete architectural, MEP electrical conduit network, and sanitary plumbing infrastructure of the Ground Floor Toilet ($4'-0" \times 6'-0"$) has been fully visualized, coordinated, and rendered in 3D:

````carousel
![Ground Floor Toilet MEP Overview](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/toilet_mep_overview_annotated.png)
<!-- slide -->
![Toilet West Wall Plumbing & Electrical Riser](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/toilet_west_wall_pipelines_annotated.png)
````

### 40.1 Spatial Envelope & Dropped Ceiling Loft

1. **Clear Internal Dimensions:**
   * Width (East-West): $4'-0"\ (1219.2\text{ mm})$ between inside wall faces ($X = 3810.0\text{ mm}$ to $4876.8\text{ mm}$, excluding West column offset).
   * Length (North-South): $6'-0"\ (1828.8\text{ mm})$ from front door wall to North external wall ($Y = 0.0\text{ mm}$ to $1828.8\text{ mm}$).
   * Floor Plinth Level: Finished Floor Level (FFL) at $Z = 914.4\text{ mm}$ (+3'-0" above natural ground).
2. **Dropped Ceiling Slab (Loft) at 7'-0" Height:**
   * A structural $100\text{ mm}$ RCC dropped slab (`Toilet_Ceiling_Slab`) is cast at $Z = 3048.0\text{ to }3148.0\text{ mm}$ (clear room height of $2133.6\text{ mm} = 7'-0"$).
   * **Overhead Storage Loft:** The space between $Z = 3148.0\text{ mm}$ and main floor ceiling soffit $Z = 3962.4\text{ mm}$ forms an enclosed overhead utility loft ($814.4\text{ mm}$ vertical clearance) accessible from the lobby/stairwell.
3. **Zero Structural Column Chasing:**
   * Both adjacent RCC structural columns (`Col_N_Toilet_Stair` at $X \in [4876.8, 5105.4], Y \in [152.4, 381.0]$ and `Col_West_Toilet` at $X \in [4876.8, 5105.4], Y \in [1714.5, 1943.1]$) remain 100% untouched.
   * All plumbing and electrical conduits are strictly chased into 9-inch non-structural brick infill walls.

---

### 40.2 Electrical Network & Safety Segregation (IS 732 Compliance)

Water splash and moisture are rigorously segregated from electrical switches in accordance with IS 732 / IEC 60364 bathroom zoning:

1. **Entrance Control Console (`SB-7` on Outside Lobby Wall):**
   * **Mounting:** Outer lobby wall adjacent to the toilet door latch at $X = 3560.0\text{ mm}, Y = 1943.1\text{ mm}, Z = 2114.4\text{ mm}$ (+1200 mm AFF).
   * **Console Capacity:** 6-module flush plate containing:
     1. Switch 1: `DL-TOILET` (Central Ceiling Downlight)
     2. Switch 2: `EF-TOILET` (North Ventilator Exhaust Fan)
     3. Switch 3: Mirror Light (Over-counter washbasin point in lobby)
     4. Switch 4: 6A Utility Socket (Grooming / Shaver in lobby)
     5. Switch 5 & 6 (Double-Pole): **25A Heavy-Duty Geyser DP Isolator Switch** with red neon indicator lamp.
   * *Safety Advantage:* High-voltage geyser isolation and daily light/exhaust switching are handled entirely in the dry zone outside the bathroom before entering.
2. **Internal High-Level Geyser Socket (`SB-8`):**
   * **Mounting:** West wall at $X = 4876.8\text{ mm}, Y = 1260.0\text{ mm}, Z = 2650.0\text{ mm}$ (+1735 mm AFF / 5'-8" AFF).
   * **Specification:** 25A 3-pin moisture-sealed socket box with spring-loaded IP55 protective flap.
   * **Supply Line:** Fed directly via dedicated $4.0\text{ mm}^2$ FRLS phase, neutral, and earth wires from the `SB-7` DP switch above through the dropped ceiling conduit.
3. **Moisture-Sealed Ceiling Downlight Pot (`DL-TOILET`):**
   * Cast centrally into the dropped slab at $X = 4350.0\text{ mm}, Y = 1000.0\text{ mm}, Z = 3048.0\text{ mm}$.
   * Pre-fitted for an IP65 moisture-sealed 7W warm/neutral white LED round downlight.
4. **Ventilator Exhaust Fan (`EF-TOILET`):**
   * Installed inside the North wall concrete ventilator frame ($600 \times 600\text{ mm}$) at $Z = 2750.0\text{ mm}$ (+1835 mm AFF).
   * Fed via a dedicated $20\text{ mm}$ rigid PVC conduit branching North from `DL-TOILET`.

---

### 40.3 Plumbing & Sanitary Pipeline Infrastructure

1. **Underground Soil Drainage to Septic Tank:**
   * **Fixture:** Vitreous china Indian WC pan (`Toilet_Indian_WC`) with slip-resistant integrated footrests, positioned at $X \in [4170, 4876], Y \in [152, 940], Z = 914.4\text{ mm}$.
   * **Drop Pipe:** Heavy-duty $\varnothing 110\text{ mm}$ (4-inch) PVC soil pipe connecting the pan's integrated deep-seal S-trap directly down into the underground `Septic_Tank` ($Z \in [-1524.0, 0.0\text{ mm}]$).
   * **Direct Gravity Flow:** Because the septic tank sits directly underneath the toilet plinth, the soil line drops vertically without any horizontal bends, eliminating clogs and sewer gas resistance.
2. **Dual-Flush Cistern & Flush Pipe:**
   * Low-level wall-hung dual-flush cistern mounted on the North wall at $Z = 2200\text{ mm}$ (+1285 mm AFF).
   * Rigid $\varnothing 32\text{ mm}$ flush bend dropping into the rear spud of the Indian WC pan.
3. **CPVC Potable Cold Water Supply Network:**
   * **Main Riser:** $\varnothing 25\text{ mm}$ (1-inch) SDR 11 CPVC vertical riser running along the West wall brickwork chased channel.
   * **Geyser Feed Stub:** $90^\circ$ branch at $Z = 2400.0\text{ mm}$ (+1485 mm AFF) providing cold water inlet to the 25L geyser.
   * **Diverter Mixer Supply:** Continuous feed down to the shower diverter mixer at $Z = 1964.0\text{ mm}$ (+1050 mm AFF).
   * **Low-Level Sanitary Distribution:** Low branch at $Z = 1200.0\text{ mm}$ (+285 mm AFF) traversing to:
     - Cistern angle cock valve (+300 mm AFF)
     - Health faucet 2-way bib tap with wall bracket (+350 mm AFF adjacent to WC pan)
4. **Hot Water Supply & Shower Infrastructure:**
   * **Hot Delivery Line:** $\varnothing 20\text{ mm}$ (3/4-inch) CPVC hot water line originating from the geyser outlet at $Z = 2300.0\text{ mm}$ and dropping into the hot inlet port of the concealed shower diverter.
   * **Concealed Single-Lever Diverter:** Centrally located on West wall at $Z = 1964.0\text{ mm}$ (+1050 mm AFF) with lower spout for bucket filling.
   * **Overhead Shower Arm & Rose:** $\varnothing 15\text{ mm}$ concealed riser running upwards from diverter to $Z = 2760.0\text{ mm}$ (+1845 mm AFF) with a $300\text{ mm}$ projecting brass shower arm and rain shower rose head.

---

### 40.4 Quantitative Technical Schedule

| Component | Tag / Name | Location / Wall | Elevation (AFF) | Absolute Z | Specification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Entrance Console** | `SB-7` | South / Lobby Wall | $+1200\text{ mm}$ | $2114.4\text{ mm}$ | 6-Module Plate (Light, EF, Mirror, 6A Skt, 25A DP) |
| **Internal Geyser Skt** | `SB-8` | West Wall | $+1735\text{ mm}$ | $2650.0\text{ mm}$ | 25A IP55 Spring-Flap Sealed Power Socket |
| **Ceiling Light Pot** | `DL-TOILET` | Dropped Slab Center | $+2133.6\text{ mm}$ | $3048.0\text{ mm}$ | IP65 Round Downlight Pot (7W LED) |
| **Exhaust Fan Box** | `EF-TOILET` | North Ventilator Frame | $+1835\text{ mm}$ | $2750.0\text{ mm}$ | Heavy-Duty Exhaust Fan with External Louvers |
| **Indian WC Pan** | `Toilet_Indian_WC` | Plinth Floor | $\pm 0\text{ mm}$ FFL | $914.4\text{ mm}$ | Vitreous China Pan with S-Trap & Footrests |
| **Soil Waste Pipe** | PVC Soil Drop | Under WC Pan | Drops below plinth | $-1524\text{ to }914\text{ mm}$ | $\varnothing 110\text{ mm}$ Rigid PVC Soil Line to Septic Tank |
| **Dual-Flush Cistern** | Flush Cistern | North Wall | $+1285\text{ mm}$ | $2200.0\text{ mm}$ | 10L Dual-Flush Tank with $\varnothing 32\text{ mm}$ Drop Bend |
| **Shower Diverter Tap** | Diverter Mixer | West Wall | $+1050\text{ mm}$ | $1964.0\text{ mm}$ | Concealed Single-Lever Brass Diverter & Spout |
| **Overhead Shower** | Shower Head | West Wall | $+1845\text{ mm}$ | $2760.0\text{ mm}$ | $\varnothing 150\text{ mm}$ Rain Shower Rose with $300\text{ mm}$ Arm |
| **Cold Water Supply** | CPVC Cold Riser | West Wall Chase | Full Height | $914\text{ to }2760\text{ mm}$ | $\varnothing 25\text{ mm}$ (1") SDR 11 CPVC Potable Pipe |
| **Hot Water Delivery** | CPVC Hot Line | West Wall Chase | Mid-Level | $1964\text{ to }2300\text{ mm}$ | $\varnothing 20\text{ mm}$ (3/4") CPVC Hot Water Pipe |

---

### 40.5 First Floor (G+1) Lockstep Synchronization
* The identical configuration has been established for the First Floor Toilet (`FF_Toilet_Group`) at vertical translation $\Delta Z = +3173.0\text{ mm}$, ensuring absolute vertical alignment of the sanitary shaft, CPVC risers, and drainage drops.


---
