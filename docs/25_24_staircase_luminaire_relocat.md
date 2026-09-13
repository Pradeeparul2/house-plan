## 24. Staircase Luminaire Relocation to East Wall of Toilet

In response to the user's request, the staircase lighting system has been relocated and mounted directly onto the **East side wall of the toilet** (`Toilet_Wall_East`), serving both the Ground Floor and First Floor staircase flights.

```carousel
![Close-Up View of the Staircase Mid-Landing Showing the Relocated Luminaire on the Toilet East Wall](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\staircase_toilet_east_wall_light_closeup.png)
<!-- slide -->
![Front Elevation View Showing Continuous Vertical Conduit Drops for Both Ground and First Floor Staircase Lights](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\staircase_wall_lights_two_storey_front.png)
<!-- slide -->
![Two-Storey Isometric View Showing Complete Relocated Staircase Wall Lighting and Slab Conduit Network](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\staircase_wall_lights_two_storey_iso.png)
```

### 24.1 Architectural & Functional Rationale
1. **Uninterrupted Solid Masonry Host:**
   - The toilet East wall (`Toilet_Wall_East` spanning $X \in [3810, 3924.3\text{ mm}]$, $Y \in [0, 1828.8\text{ mm}]$) is a continuous, solid $114.3\text{ mm}$ (4.5") brick wall with **zero door or window openings** (the toilet ventilator is situated on the North wall at $Y = 0$, and the toilet entry door is on the South wall at $Y = 1714.5 - 1828.8\text{ mm}$).
   - This makes the East wall structurally and aesthetically the ideal host for wall-chased electrical conduit and surface-mounted luminaires.
2. **Optimal Bi-Directional Mid-Landing Illumination:**
   - The staircase mid-landing platform extends across $X \in [3060, 3810\text{ mm}]$, $Y \in [230, 1710\text{ mm}]$, with a finished platform elevation of $Z = 2438.4\text{ mm}$ ($+8'\text{-}0"$).
   - Centering the luminaire at $Y = 970.0\text{ mm}$ (exact centerline of the landing) and mounting at $Z = 3300.0\text{ mm}$ positions the fixture $+861.6\text{ mm}$ above the landing surface.
   - This wide-angle projection illuminates both the ascending Flight 1 and Flight 2 treads from the side, eliminating shadows cast by people climbing the stairs while keeping the light source completely sheltered from direct eye-glare.
3. **Safe & Effortless Maintenance:**
   - Positioned directly above the wide flat mid-landing rather than suspended high above raked steps, the luminaire can be safely reached for cleaning or bulb replacement from a standard two-step household stool without needing hazardous ladder balancing on inclined treads.

### 24.2 Fixture Specifications & Geometric Coordinates
* **Ground Floor Staircase Luminaire (`Staircase_Wall_Light_Fixture`):**
  - **Group:** `Ground_Floor_Group`
  - **Mounting Face:** Flush on outer plaster face of `Toilet_Wall_East` ($X = 3810.0\text{ mm}$)
  - **Center Coordinates:** $(X = 3810.0\text{ mm}, Y = 970.0\text{ mm}, Z = 3300.0\text{ mm})$
  - **Fixture Body:** $50\text{ mm} \times 120\text{ mm} \times 200\text{ mm}$ architectural die-cast bulkhead wall sconce with dual-diffuser warm LED lens (`#F5EE38` / `(0.95, 0.85, 0.40)`).
* **First Floor Matching Staircase Luminaire (`FF_Staircase_Wall_Light_Fixture`):**
  - **Group:** `First_Floor_Group`
  - **Center Coordinates:** $(X = 3810.0\text{ mm}, Y = 970.0\text{ mm}, Z = 6473.0\text{ mm})$ (Exact vertical duplicate with $\Delta Z = +3173.0\text{ mm}$).
  - Serves the upper staircase flight ascending towards the rooftop terrace head room.

### 24.3 Continuous Electrical Conduit Infrastructure
1. **Ceiling Slab Conduit Feeds (`Electrical_Slab_Conduit_Network` & `FF_Electrical_Slab_Conduit_Network`):**
   - Expanded to **19 solid pipe runs** on each floor.
   - Routes a $25\text{ mm}$ rigid PVC conduit from the toilet entry junction point at $(3810.0, 1828.8\text{ mm})$ along the top of the toilet wall directly to the vertical drop point at $(3800.0, 970.0\text{ mm})$.
2. **Vertical Chased Wall Drops (`Electrical_Slab_Wall_Drops` & `FF_Electrical_Slab_Wall_Drops`):**
   - Expanded to **20 solid vertical pipe runs** on each floor.
   - **Ground Floor Drop:** Continuous $25\text{ mm}$ rigid PVC drop from ceiling slab level $Z = 4020.0\text{ mm}$ down to fixture junction box knockout at $Z = 3400.0\text{ mm}$ (Length: $620\text{ mm}$).
   - **First Floor Drop:** Matching vertical drop from $Z = 7193.0\text{ mm}$ down to $Z = 6573.0\text{ mm}$ (Length: $620\text{ mm}$).
   - Finished in `#10AC84` (safety emerald green) for clear distinction from plumbing lines.

### 24.4 Quality & Structural Validation
* **Master Document:** `HomeConstruction.FCStd`
* **Total Object Count:** 422 objects.
* **Hierarchical Tree Integrity:** Strictly 3 master root groups (`Ground_Floor_Group`, `First_Floor_Group`, `Master_Rooftop_Terrace_Group`). Zero unparented objects.
* **Geometric Validation:** 0 cyclic dependencies, 0 null shapes, 0 recompute errors.


---
