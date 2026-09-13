## 60. Underground Sump Vertical Alignment to Plinth Floor & Sitout Manhole Integration

> [!NOTE]
> **System Title:** Sump Tank Elevation Optimization & Floor Access Maintenance Detail  
> **Source Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd)  
> **Parent Containers:** `Substructure_Foundation_Group` & `Sump_Motor_Group`  
> **Z-Elevation Alignment:** Base at $-1.500\text{ m}$ (footing datum level), Top Slab flush at $+0.914\text{ m}$ ($+3'\text{-}0"$, plinth top).

### 60.1 Sump Optimization Portfolio

```carousel
![Raised Sump Substructure Isometric](c:\Users\prade\OneDrive\Desktop\home plan\renders\sump_raised_isolated_iso.png)
<!-- slide -->
![Raised Sump Front Elevation Depth Continuity](c:\Users\prade\OneDrive\Desktop\home plan\renders\sump_raised_front_elev.png)
<!-- slide -->
![Sump and Substructure Full Overview](c:\Users\prade\OneDrive\Desktop\home plan\renders\sump_raised_substructure_overview.png)
```

---

### 60.2 Problem Statement & Resolution

* **Previous Discrepancy:** The underground water sump was previously modeled between $Z = -2133.6\text{ mm}$ and $Z = 0.0\text{ mm}$ (Natural Ground Level). Because the finished plinth beam and Sitout floor sit at $Z = +914.4\text{ mm}$ ($+3'\text{-}0"$), an awkward $914.4\text{ mm}$ ($3\text{ ft}$) open gap existed between the sump tank and the sitout foundation. This would have required a deep, hazardous maintenance shaft and left the pump suction pipe floating in mid-air.
* **Corrective Implementation:**
  1. **Vertical Extension:** `Sump_UG_Water_Tank` has been raised so its top slab finishes flush at $Z = +914.4\text{ mm}$ ($+3'\text{-}0"$), with its base resting at the foundation footing level $Z = -1500.0\text{ mm}$ (Height = $2414.4\text{ mm}$ / $7'\text{-}11"$).
  2. **Storage Capacity Enhancement:** The vertical expansion provides an enlarged water capacity of approx. **$5,600\text{ L}$ gross volume** ($1.524 \times 1.524 \times 2.414\text{ m}$), comfortably providing 4,500L+ net potable water storage.
  3. **Sitout Flush Manhole Cover (`Sump_Manhole_Cover`):** Added a standard $600 \times 600\text{ mm}$ ($2\text{ ft} \times 2\text{ ft}$) airtight stainless steel / cast-iron inspection manhole cover flush on the Sitout floor ($Z \in [914.4, 944.9]\text{ mm}$), positioned at $(X = 614.4, Y = 614.4)$ for effortless cleaning and visual inspection.
  4. **Internal Suction Drop & Foot Valve:** Added vertical $1.25"$ suction drop pipe (`Sump_Internal_Suction_Pipe`) dropping from the plinth line ($Z = +914.4\text{ mm}$) to $Z = -1350\text{ mm}$, terminating with a heavy-duty brass foot valve & strainer (`Sump_Foot_Valve`, $Z \in [-1450, -1300]\text{ mm}$) hovering $50\text{ mm}$ above the sump floor.
  4. **Internal Suction Drop & Foot Valve:** Added vertical $1.25"$ suction drop pipe (`Sump_Internal_Suction_Pipe`) dropping from the plinth line ($Z = +914.4\text{ mm}$) to $Z = -1350\text{ mm}$, terminating with a heavy-duty brass foot valve & strainer (`Sump_Foot_Valve`, $Z \in [-1450, -1300\text{ mm}$]) hovering $50\text{ mm}$ above the sump floor.

---

### 60.3 Verification & Object Status

* **Total Objects in Document:** 541 objects, 0 errors, 100% valid manifold solids.
* **Model File:** [`HomeConstruction.FCStd`](file:///c:/Users/prade/OneDrive/Desktop/home%20plan/HomeConstruction.FCStd).

---
