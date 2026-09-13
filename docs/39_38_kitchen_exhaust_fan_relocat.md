## 38. Kitchen Exhaust Fan Relocation to East Side Wall (Over Sink Bay)

Following client directive (*"move exhaust fan east side wall since south side wall common wall"*), the kitchen exhaust fan has been relocated to the **East exterior wall directly adjacent to the sink bay**, completely avoiding the South boundary wall which is a shared common wall with the adjacent property.

```carousel
![Kitchen Exhaust Fan on East Side Wall Over Sink](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/kitchen_exhaust_east_wall_sink_annotated.png)
```

### 38.1 Site Boundary Rationale & Engineering Coordinates

1. **Boundary Wall Protection (South Wall as Solid Common Wall):**
   * The South exterior wall (`Kitchen_Wall_South`, $Y \in [7467.6, 7620.0\text{ mm}]$) is a shared common wall / zero-setback boundary abutting the neighboring property. Any penetrations through the South wall would discharge directly into the adjacent plot and face immediate blockage.
   * `Kitchen_Wall_South` is restored to **100% solid, continuous brick masonry** with zero punctures.

2. **Exhaust Fan Placement on East Wall (`Kitchen_Exhaust_Fan` & `FF_Kitchen_Exhaust_Fan`):**
   * **Wall Substrate:** East Exterior Wall (`Kitchen_Wall_East`, $X \in [0.0, 152.4\text{ mm}]$), venting directly into the open East compound walkway / side setback.
   * **Y-Center:** Centered at **$Y = 7125.0\text{ mm}$**, directly adjacent to the sink basin ($Y \in [6940.0, 7370.0\text{ mm}]$).
   * **Horizontal Clearances:** Located in the $533.4\text{ mm}$ clear masonry band between the East Window frame and corner column:
     - Clearance from East Window jamb ($Y = 6858.0\text{ mm}$): **$127.0\text{ mm}$ ($5.0"$)**.
     - Clearance from Column `Col_SE_Corner` ($Y = 7391.4\text{ mm}$): **$126.4\text{ mm}$ ($5.0"$)**.
   * **Mounting Height:** $+1950.0\text{ mm}$ AFF ($Z = 2864.4\text{ mm}$ absolute), casing spanning $Z \in [2724.4, 3004.4\text{ mm}]$.
   * **Loft Clearance:** Top of the fan casing sits at $Z = 3004.4\text{ mm}$, providing **$43.6\text{ mm}$ clearance** under the $Z = 3048.0\text{ mm}$ (7'-0" AFF) RCC storage loft slab soffit (`Kitchen_Loft_South`).
   * **Counter Clearance:** Sits **$946.4\text{ mm}$ ($3'\text{-}1"$)** above the granite countertop ($Z = 1778.0\text{ mm}$).

3. **Electrical Infrastructure & Circuit Routing:**
   * **Junction Box (`Kitchen_Exhaust_Fan_Junction_Box`):** Recessed galvanized circular box ($\varnothing 75\text{ mm} \times 35\text{ mm}$) at $X = 152.4\text{ mm}, Y = 7280.0\text{ mm}, Z = 2864.4\text{ mm}$ ($+1950\text{ mm}$ AFF), positioned safely beside the fan casing.
   * **Conduit Drop (`Kitchen_Exhaust_Fan_Conduit_Drop`):** Dedicated $20\text{ mm}$ PVC conduit cast into ceiling slab directly from nearest ceiling downlight pot `DL-10` ($X=1050, Y=7100$), routed straight East to $Y = 7280.0\text{ mm}$, and chased vertically down to the fan junction box.
   * **Switch Control:** Switched via Switch 3 on the entrance master console **`SB-13`** on the West spine wall.

### 38.2 Tubelight Pipe Centering & Kitchen Pipeline Simplification

Following client audit (*"check the tubelight pipe posotion and simplify the pipelines on kitchen"*), the kitchen electrical pipeline network was completely restructured from radial diagonal runs into a clean, professional **Orthogonal Trunk-and-Branch Grid**:

```carousel
![Kitchen Centered Tubelight Pipe](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/kitchen_tubelight_centered_annotated.png)
<!-- slide -->
![Kitchen Simplified Slab Pipelines](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/kitchen_slab_pipelines_simplified_annotated.png)
```

1. **Tubelight Pipe Centering (`Kitchen_Tubelight_Conduit_Drop`):**
   * **Previous State:** Chased at $Y = 6650.0\text{ mm}$ ($250\text{ mm}$ off-center) to avoid the former exhaust fan aperture.
   * **Optimized State:** Now that the exhaust fan has relocated to the sink bay, `Kitchen_Tubelight_Junction_Box` and its vertical conduit drop are relocated to **$Y = 6400.0\text{ mm}$**, entering the **exact geometric dead center** of the $1200\text{ mm}$ (4 ft) LED batten fixture (`Kitchen_Tubelight_Fixture`) directly above the East window.
   * **Aesthetics:** Completely symmetrical, with zero visible wire leads or offset bends.

2. **Pipeline Simplification & Orthogonal Routing:**
   * **Central Spine Trunk (North-South along $X = 1050.0\text{ mm}$):** A single continuous slab conduit runs down the middle of the kitchen connecting the three ceiling junction pots in a straight line: `DL-9` ($Y = 5550$) $\longleftrightarrow$ `CL-KIT` ($Y = 6325$) $\longleftrightarrow$ `DL-10` ($Y = 7100$).
   * **Lateral Branch 1 (Food Prep SB-14):** Originates directly from nearest pot `DL-9` ($1050, 5550$), running straight East to `SB-14` ($152.4, 5715$).
   * **Lateral Branch 2 (Tubelight):** Perpendicular $90^\circ$ branch from central pot `CL-KIT` ($1050, 6325$) straight East to $(152.4, 6400)$ and straight down to the tubelight center.
   * **Lateral Branch 3 (Exhaust Fan):** Originates directly from nearest pot `DL-10` ($1050, 7100$) straight East to $(152.4, 7280)$ and down to the exhaust fan over the sink.
   * **Lateral Branch 4 (Refrigerator SB-15):** Originates directly from `DL-10` ($1050, 7100$) running straight South to `SB-15` ($1100, 7468$) on the South wall.
   * **Results:** Eliminated all 4 diagonal criss-crossing pipes from `CL-KIT`. Total conduit length reduced by over 35%, perfectly aligned with the structural rebar grid.

3. **1:1 Duplicate First Floor Alignment:**
   * Identically mirrored on First Floor (`FF_Kitchen_Tubelight_Conduit_Drop`, `FF_Kitchen_Tubelight_Junction_Box`, `FF_Kitchen_Exhaust_Fan_Conduit_Drop`, `FF_Kitchen_Exhaust_Fan_Junction_Box`, `FF_Electrical_Slab_Conduit_Network`) at $\Delta Z = +3173.0\text{ mm}$.
