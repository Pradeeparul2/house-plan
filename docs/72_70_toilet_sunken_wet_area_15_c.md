## 70. Toilet Sunken Wet Area (15 cm Drop Below Surface) Architectural & Sanitary Detailing

### 70.1 Architectural Zoning & Sunken Slab Philosophy

In direct response to client requirements (*"on toilet keep wet area 15cm blow the surface"*), both Ground Floor and First Floor toilets have been precision-engineered with a **15 cm (150 mm) sunken bathing wet zone**:

1. **Functional Separation (Wet vs. Dry Zoning)**:
   - **Dry Area (Indian WC Platform)**:
     - Spans $Y \in [152.4, 950.0\text{ mm}]$, $X \in [3924.3, 4800.6\text{ mm}]$ (Width $876.3\text{ mm}$, Length $797.6\text{ mm}$).
     - Maintained at the main floor surface level: **$\text{FFL} = +914.4\text{ mm}$ (Ground Floor)** and **$\text{FFL} = +4087.4\text{ mm}$ (First Floor)**.
     - Finished in light-grey anti-skid porcelain ceramic tiles (`GF_Toilet_Dry_Area_Floor` and `FF_Toilet_Dry_Area_Floor`).
     - Houses the Indian WC squatting pan (`Toilet_Indian_WC` / `FF_Toilet_Indian_WC`), footrests, flush water inlet, and health faucet.
   - **Wet Area (Sunken Bathing & Shower Tray)**:
     - Spans $Y \in [980.0, 1680.0\text{ mm}]$, $X \in [3924.3, 4800.6\text{ mm}]$ (Width $876.3\text{ mm}$, Length $700.0\text{ mm}$).
     - **Depressed by exactly $15\text{ cm}$ ($150\text{ mm}$) below the finished floor surface**:
       - Ground Floor Wet FFL: **$Z = 764.4\text{ mm}$** ($914.4 - 150\text{ mm}$).
       - First Floor Wet FFL: **$Z = 3937.4\text{ mm}$** ($4087.4 - 150\text{ mm}$).
     - Finished in high-grip slate blue-grey mosaic tiles (`GF_Toilet_Wet_Area_Sunken_Floor` and `FF_Toilet_Wet_Area_Sunken_Floor`).
     - Contains the shower diverter mixer, overhead shower rose, and the stainless steel floor drain trap.
   - **Step Riser (15 cm Granite Drop)**:
     - A $150\text{ mm}$ vertical black granite riser (`GF_Toilet_Wet_Dry_Step_Riser` and `FF_Toilet_Wet_Dry_Step_Riser`) at $Y \in [950, 980\text{ mm}]$ creates a clean architectural threshold separating the dry WC platform from the sunken shower tray.
   - **Entrance Door Threshold Curb (15 cm Splash Barrier)**:
     - A $150\text{ mm}$ granite door curb (`GF_Toilet_Door_Threshold_Curb` and `FF_Toilet_Door_Threshold_Curb`) at $Y \in [1680, 1714.5\text{ mm}]$ ensures that water splashing during showers is 100% contained within the sunken tray and cannot spill out through the door into the stair lobby.

2. **Drainage & Trap Elevation Lockstep**:
   - **Recessed Floor Traps**: The top stainless steel grates of `GF_Toilet_Bath_Floor_Trap` ($Z = 794.88\text{ mm}$) and `FF_Toilet_Bath_Floor_Trap` ($Z = 3967.88\text{ mm}$) sit flush with the sunken wet floor surface.
   - **Optimized Gravity Invert**:
     - Ground Floor: Sullage pipe drops to subgrade $Z = 430\text{ mm}$, running cleanly beneath `PB2_Stair_West` and passing under the septic tank effluent tee into Gully Trap GT-2.
     - First Floor: Sullage pipe drops to $Z = 3580\text{ mm}$, passing safely under roof beam `RB2_Stair_West_Trimmer` to vertical stack `Toilet_Bath_Waste_Vertical_Stack`.

---

### 70.2 Visual Documentation

````carousel
![Ground Floor Toilet Cross-Section Showing 15cm Sunken Wet Floor, Riser Step & Dry WC Platform](c:\Users\prade\OneDrive\Desktop\home plan\renders\toilet_gf_sunken_wet_area_closeup.png)
<!-- slide -->
![3D Isometric X-Ray View Showing 30% Opacity Toilet Walls with Sunken Wet Area](c:\Users\prade\OneDrive\Desktop\home plan\renders\toilet_sunken_wet_area_isometric.png)
<!-- slide -->
![Top Plan View of Building Showing Toilet Sunken Shower Zone](c:\Users\prade\OneDrive\Desktop\home plan\renders\toilet_sunken_wet_area_plan_view.png)
````

---

### 70.3 Quantitative Component Schedule

| Object Identifier | FreeCAD Label | Elevation $Z$ (mm) | Thickness / Dimensions | Material / Specification |
| :--- | :--- | :--- | :--- | :--- |
| `GF_Toilet_Dry_Area_Floor` | GF Toilet Dry Area Floor Platform | $Z = 914.4 \to 944.88$ | $30.48\text{ mm}$ ($1.2\"$) | Light Grey Anti-Skid Ceramic Tiles (FFL $+914.4\text{ mm}$) |
| `GF_Toilet_Wet_Area_Sunken_Floor` | GF Toilet Sunken Wet Area Floor | $Z = 764.4 \to 794.88$ | $30.48\text{ mm}$ | Slate Blue Non-Slip Mosaic Tiles (**$-15\text{ cm}$ Sunken**) |
| `GF_Toilet_Wet_Dry_Step_Riser` | GF Toilet Wet-Dry Step Riser | $Z = 764.4 \to 944.88$ | $150\text{ mm}$ Rise, $30\text{ mm}$ Run | Polished Black Granite Riser with Bullnose Edge |
| `GF_Toilet_Door_Threshold_Curb`| GF Toilet Door Granite Threshold Curb | $Z = 764.4 \to 944.88$ | $150\text{ mm}$ Rise, $34.5\text{ mm}$ Run | Polished Black Granite Splash Barrier at Door Sill |
| `GF_Toilet_Bath_Floor_Trap` | GF Toilet Bath Floor Trap | Top $Z = 794.88$ | $\varnothing 100\text{ mm}$ Grate, $120\text{ mm}$ Depth | Flush Stainless Steel Grate with $50\text{ mm}$ Water Seal |
| `FF_Toilet_Dry_Area_Floor` | FF Toilet Dry Area Floor Platform | $Z = 4087.4 \to 4117.88$ | $30.48\text{ mm}$ | Light Grey Anti-Skid Ceramic Tiles (FFL $+4087.4\text{ mm}$) |
| `FF_Toilet_Wet_Area_Sunken_Floor` | FF Toilet Sunken Wet Area Floor | $Z = 3937.4 \to 3967.88$ | $30.48\text{ mm}$ | Slate Blue Non-Slip Mosaic Tiles (**$-15\text{ cm}$ Sunken**) |
| `FF_Toilet_Wet_Dry_Step_Riser` | FF Toilet Wet-Dry Step Riser | $Z = 3937.4 \to 4117.88$ | $150\text{ mm}$ Rise, $30\text{ mm}$ Run | Polished Black Granite Riser with Bullnose Edge |
| `FF_Toilet_Door_Threshold_Curb`| FF Toilet Door Granite Threshold Curb | $Z = 3937.4 \to 4117.88$ | $150\text{ mm}$ Rise, $34.5\text{ mm}$ Run | Polished Black Granite Splash Barrier at Door Sill |
| `FF_Toilet_Bath_Floor_Trap` | FF Toilet Bath Floor Trap | Top $Z = 3967.88$ | $\varnothing 100\text{ mm}$ Grate, $120\text{ mm}$ Depth | Flush Stainless Steel Grate with $50\text{ mm}$ Water Seal |

---

### 70.4 Quality Certification & Structural Safety
* **Zero Structural Clashes:** $100\%$ verified across all RCC beams, columns, pedestals, and footings.
* **Zero Fixture Clashes:** Clean separation between dry WC pan, step riser, conduits, and piping.
* **Master CAD Model:** Updated in [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd).


---
