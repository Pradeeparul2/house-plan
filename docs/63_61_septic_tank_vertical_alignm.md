## 61. Septic Tank Vertical Alignment to Plinth Floor & Airtight Inspection Manhole Integration

> [!NOTE]
> **System Title:** Septic Tank Elevation Alignment & Airtight Sewer Maintenance Detail  
> **Source Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Parent Container:** `Substructure_Foundation_Group`  
> **Z-Elevation Alignment:** Base resting at $-1.500\text{ m}$ (footing stratum level), Top Slab flush at $+0.914\text{ m}$ ($+3'\text{-}0"$, plinth top).

### 61.1 Symmetrical Substructure Portfolio (Both Tanks Raised)

```carousel
![Both Underground Tanks Raised to Plinth Level Isometric](c:\Users\prade\OneDrive\Desktop\home plan\renders\substructure_both_tanks_raised_iso.png)
<!-- slide -->
![Both Tanks Front Elevation Symmetrical Alignment](c:\Users\prade\OneDrive\Desktop\home plan\renders\substructure_both_tanks_front_elev.png)
```

---

### 61.2 Engineering Implementation & Features

1. **Zero-Gap Vertical Continuity:**
   * `Septic_Tank` raised from its previous $Z = 0.0\text{ mm}$ cap up to $Z = +914.4\text{ mm}$ ($+3'\text{-}0"$), with its base resting at the foundation footing datum $Z = -1500.0\text{ mm}$ (Height = $2414.4\text{ mm}$ / $7'\text{-}11"$).
   * Symmetrically matches the `Sump_UG_Water_Tank` on the opposite quadrant, creating clean load distribution along the front perimeter plinth beams.
2. **Enlarged Digestion & Retention Capacity:**
   * Total gross volume expands to approx. **$3.93\text{ m}^3$ (3,930 Liters)** ($1.067 \times 1.524 \times 2.414\text{ m}$), providing ample settling retention time complying with IS 2470 Code of Practice for Small Domestic Sewage Treatment.
3. **Airtight Inspection Manhole Cover (`Septic_Manhole_Cover`):**
   * $500 \times 500\text{ mm}$ airtight heavy-duty FRP / cast-iron manhole cover ($30.5\text{ mm}$ thick) mounted flush at $Z \in [914.4, 944.9]\text{ mm}$, centered at $(X = 4169.6, Y = 664.4)$.
   * Fitted with perimeter rubber gasket to guarantee zero sewer odor infiltration into living or utility areas.
4. **110mm UPVC Soil Inlet Dip Pipe (`Septic_Inlet_Tee_Pipe`):**
   * Standard $110\text{ mm}$ OD SWR drainage dip tee ($600\text{ mm}$ vertical dip, $Z \in [314.4, 914.4]\text{ mm}$) centered at $(X = 4600.0, Y = 600.0)$, discharging waste smoothly beneath the scum floating layer.

---

### 61.3 Verification & Object Status

* **Total Objects in Document:** 543 objects, 0 errors, 100% valid manifold solids.
* **Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd).

---
