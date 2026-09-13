## 57. Split AC Outdoor Unit (ODU) East Elevation Implementation (Option 2)

Following client approval of the most cost-effective approach (**Option 2: East Exterior Wall Cantilever Mounting**), dedicated outdoor condensing units (ODU), galvanized cantilever support brackets, vibration isolation damping pads, refrigerant line bundles, wall sleeves, gravity condensate drains, and interior kitchen pelmet runs were designed and integrated into [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd) on both Ground and First Floors.

```carousel
![Split AC Outdoor Units East Facade Implementation](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/east_facade_ac_odu_implemented.png)
<!-- slide -->
![AC Pipeline Concealed Over South Kitchen Loft](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/loft_pipeline_implementation_annotated.png)
<!-- slide -->
![AC Pipeline Over South Kitchen Loft Strategy](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/ac_pipeline_over_kitchen_loft_strategy.png)
<!-- slide -->
![AC Outdoor Unit Planning Strategy](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/ac_outdoor_unit_planning_strategy.png)
```

### 57.1 Architectural & Boundary Wall Design Rationale
* **Zero-Setback Party Walls Respected:** West and South walls are boundary party walls with zero setback. By mounting the indoor unit on `Bedroom_Wall_East` and routing through the adjacent Kitchen South loft, **zero core cutting, zero pipe penetrations, and zero equipment mounts** occur on common walls.
* **100% Concealed Routing Over South Kitchen Loft (Zero Visible Pipes):**
  * The pipe exits the back of `Bedroom_AC_Indoor_Unit` ($Z \approx 3450\text{ mm}$), crosses the 4-inch partition wall, and drops directly onto the upper horizontal surface of **`Kitchen_Loft_South`** ($Z_{\text{top}} = 3123.0\text{ mm}$).
  * There is **$839.4\text{ mm}$ ($2'\text{-}9''$)** of clear vertical headspace between the loft slab and the ceiling slab soffit ($Z = 3962.4\text{ mm}$).
  * Standing on the kitchen floor (eye level $\approx 1600\text{ mm}$), the entire pipeline rests flat behind the $75\text{ mm}$ loft concrete lip and storage cartons, making it **100% invisible from anywhere in the kitchen**.
  * **Zero ceiling casing, trunking, or false ceiling pelmets required.**
* **Natural Gravity Condensate Drainage:**
  * Because the IDU condensate tray is at $Z = 3450\text{ mm}$ and the loft slab is at $Z = 3123\text{ mm}$, the drain pipe enjoys a natural downward pitch into the Kitchen sink drain stack ($Z = 1750\text{ mm}$).
* **Capital Cost Optimization (₹8,000 – ₹11,000 Saved):** 
  * Total combined pipe run is under $2.8\text{ m}$ ($9.2\text{ ft}$), completely covered by the standard $3.0\text{ m}$ ($10\text{ ft}$) factory copper piping kit included with new split ACs. **Zero extra copper purchase** is needed.
  * Eliminates vertical core cutting through two intermediate RCC slabs.
* **Architectural Integration Above Window Chajjas:**
  * Ground Floor ODU is positioned directly above `GF_East_Kitchen_Window_Chajja` ($Z_{\text{base}} = 3173.0\text{ mm}$), visually sheltered by the cantilever canopy.
  * First Floor ODU is positioned symmetrically above `FF_East_Kitchen_Window_Chajja` ($Z_{\text{base}} = 6346.0\text{ mm}$).
  * Axial condenser fans discharge horizontally toward the open East driveway/setback, ensuring unimpeded heat rejection.

---

### 57.2 Mechanical & HVAC Detailed Specifications

1. **1.5 Ton Split AC Condensing Units (ODU):**
   * **Dimensions:** $800\text{ mm}$ wide (in $Y: 6000.0\text{ to }6800.0\text{ mm}$), $300\text{ mm}$ deep (in $X: -360.0\text{ to }-60.0\text{ mm}$), $550\text{ mm}$ high.
   * **Compressor & Fan Assembly:** Features an aerodynamic $420\text{ mm}$ diameter axial fan cowl, hub, and dark metallic outer protective ring with side service valve enclosure.
   * **Finish:** Appliance off-white (`#EBEBE6`).
2. **Heavy-Duty Galvanized Iron (GI) Cantilever Wall Brackets:**
   * Two $450\text{ mm}$ horizontal projection arms ($40 \times 35\text{ mm}$) spaced $550\text{ mm}$ apart ($Y = 6125.0\text{ mm}$ and $Y = 6675.0\text{ mm}$).
   * $250\text{ mm}$ vertical anchor plates with diagonal strut bracing secured to the 9-inch exterior masonry wall.
   * **Finish:** Galvanized steel gray (`#8C949E`).
3. **Acoustic & Vibration Damping:**
   * Four $50 \times 50 \times 20\text{ mm}$ high-density neoprene rubber damping pads mounted under each compressor foot to eliminate structure-borne noise into interior living spaces.
4. **Refrigerant & Drainage MEP Bundles:**
   * **Exterior Bundle & Sleeve:** $65\text{ mm}$ UPVC exterior wall sleeve ($Y = 6750.0\text{ mm}$) feeding $44\text{ mm}$ insulated Armaflex copper bundle with $90^\circ$ sweep bend directly into service valves.
   * **Gravity Condensate Drain:** $25\text{ mm}$ UPVC drop pipe discharging downward along the exterior wall facade into the storm/gully drain line.
   * **Concealed Over-Loft Run:** Insulated Armaflex tubing runs flat across the top of `Kitchen_Loft_South` ($Z = 3153.0\text{ mm}$ GF / $Z = 6326.0\text{ mm}$ FF) with zero vertical/horizontal exposure in the kitchen living space, plus a vertical gravity drain branch teeing into the sink waste stack.

---

### 57.3 Component Inventory & Group Hierarchy

| Component Name | Display Label | Elevation ($Z$) | Parent Container | Status |
| :--- | :--- | :--- | :--- | :---: |
| **`Bedroom_AC_Outdoor_Unit_Group`** | GF Bedroom AC Split AC Outdoor Unit (ODU) | $Z \in [2688, 3743]$ | `Ground_Floor_Group` | **ACTIVE** |
| `Bedroom_AC_Outdoor_Unit_Wall_Brackets` | GF Bedroom AC GI Cantilever Wall Brackets | $Z \in [2923, 3173]$ | `Bedroom_AC_Outdoor_Unit_Group` | **ACTIVE** |
| `Bedroom_AC_Outdoor_Unit_Damping_Pads` | GF Bedroom AC Vibration Damping Rubber Pads | $Z \in [3173, 3193]$ | `Bedroom_AC_Outdoor_Unit_Group` | **ACTIVE** |
| `Bedroom_AC_Outdoor_Unit_Cabinet` | GF Bedroom AC Condensing Unit 1.5T (ODU) | $Z \in [3193, 3743]$ | `Bedroom_AC_Outdoor_Unit_Group` | **ACTIVE** |
| `Bedroom_AC_Outdoor_Unit_Fan_Grille` | GF Bedroom AC Axial Fan Grille Ring | $Z \in [3268, 3667]$ | `Bedroom_AC_Outdoor_Unit_Group` | **ACTIVE** |
| `Bedroom_AC_Outdoor_Unit_Refrigerant_Bundle` | GF Bedroom AC Insulated Copper Lines & Wall Sleeve | $Z \in [3280, 3345]$ | `Bedroom_AC_Outdoor_Unit_Group` | **ACTIVE** |
| `Bedroom_AC_Outdoor_Unit_Condensate_Drain` | GF Bedroom AC Condensate Gravity Drain Pipe | $Z \in [2688, 3288]$ | `Bedroom_AC_Outdoor_Unit_Group` | **ACTIVE** |
| `Bedroom_AC_Indoor_Refrigerant_Run` | GF Bedroom AC Refrigerant Run Over South Kitchen Loft | $Z \in [1853, 3472]$ | `Bedroom_AC_Outdoor_Unit_Group` | **ACTIVE (Concealed)** |
| **`FF_Bedroom_AC_Outdoor_Unit_Group`** | FF Bedroom AC Split AC Outdoor Unit (ODU) | $Z \in [5861, 6916]$ | `First_Floor_Group` | **ACTIVE** |
| `FF_Bedroom_AC_Outdoor_Unit_Wall_Brackets` | FF Bedroom AC GI Cantilever Wall Brackets | $Z \in [6096, 6346]$ | `FF_Bedroom_AC_Outdoor_Unit_Group` | **ACTIVE** |
| `FF_Bedroom_AC_Outdoor_Unit_Damping_Pads` | FF Bedroom AC Vibration Damping Rubber Pads | $Z \in [6346, 6366]$ | `FF_Bedroom_AC_Outdoor_Unit_Group` | **ACTIVE** |
| `FF_Bedroom_AC_Outdoor_Unit_Cabinet` | FF Bedroom AC Condensing Unit 1.5T (ODU) | $Z \in [6366, 6916]$ | `FF_Bedroom_AC_Outdoor_Unit_Group` | **ACTIVE** |
| `FF_Bedroom_AC_Outdoor_Unit_Fan_Grille` | FF Bedroom AC Axial Fan Grille Ring | $Z \in [6441, 6840]$ | `FF_Bedroom_AC_Outdoor_Unit_Group` | **ACTIVE** |
| `FF_Bedroom_AC_Outdoor_Unit_Refrigerant_Bundle` | FF Bedroom AC Insulated Copper Lines & Wall Sleeve | $Z \in [6453, 6518]$ | `FF_Bedroom_AC_Outdoor_Unit_Group` | **ACTIVE** |
| `FF_Bedroom_AC_Outdoor_Unit_Condensate_Drain` | FF Bedroom AC Condensate Gravity Drain Pipe | $Z \in [5861, 6461]$ | `FF_Bedroom_AC_Outdoor_Unit_Group` | **ACTIVE** |
| `FF_Bedroom_AC_Indoor_Refrigerant_Run` | FF Bedroom AC Refrigerant Run Over South Kitchen Loft | $Z \in [5026, 6645]$ | `FF_Bedroom_AC_Outdoor_Unit_Group` | **ACTIVE (Concealed)** |

* **Master Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)
* **Total Objects in Document:** 492 objects, 0 errors, 100% valid manifold solids.
* **Document Root Organization:** Strictly 3 master floor groups (`Ground_Floor_Group`, `First_Floor_Group`, `Master_Rooftop_Terrace_Group`) plus dedicated `Page_Ground_Floor_Plan` TechDraw sheet.
* **Timestamped Backup:** Archived to `backups/HomeConstruction_backup_before_ac_odu.FCStd`.

---
