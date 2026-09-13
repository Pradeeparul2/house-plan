## 56. Bedroom East Wall: Loft Removal & Split AC Electrical Provision Integration

Following client directive (*"remove betroom east side loft, and AC provistion on East side wall"*), structural and MEP modifications were executed across the Bedroom zones in `HomeConstruction.FCStd` on both Ground and First Floors.

```carousel
![Bedroom East Wall: Loft Removal and AC Provision Integration](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/bedroom_east_wall_ac_annotated.png)
```

### 56.1 Architectural & Structural Modifications
1. **Excised East Side Lofts:**
   * **Ground Floor (`Bedroom_Loft_East`):** Removed the 2-foot wide ($609.6\text{ mm}$) concrete slab spanning $X \in [2082.7, 2692.3\text{ mm}]$, $Y \in [4572.0, 7620.0\text{ mm}]$ at $Z \in [3048.0, 3123.0\text{ mm}]$.
   * **First Floor (`FF_Bedroom_Loft_East`):** Removed the matching First Floor slab at $Z \in [6221.0, 6296.0\text{ mm}]$.
   * **North Loft Retained:** `Bedroom_Loft_North` and `FF_Bedroom_Loft_North` remain $100\%$ intact above the wardrobe and bedroom entry door ($Y \in [4673.5, 5283.1\text{ mm}]$), providing ample storage without encroaching on bedroom wall spaces.
2. **Architectural Benefit:**
   * Eliminating the East loft clears over $2.18\text{ m}$ ($7'\text{-}2"$) of unobstructed wall height along `Bedroom_Wall_East`, opening sightlines and creating the ideal mounting substrate for split air conditioning.

---

### 56.2 Air Conditioning & Electrical Infrastructure

1. **1.5 Ton Inverter Split AC Indoor Units:**
   * **Ground Floor (`Bedroom_AC_Indoor_Unit`):** Modern high-wall indoor evaporator unit ($850 \times 220 \times 300\text{ mm}$) mounted flush against the East wall ($X \in [2082.7, 2302.7\text{ mm}]$), centered along $Y \in [5750.0, 6600.0\text{ mm}]$ ($Y_{\text{mid}} = 6175.0\text{ mm}$), positioned at $Z \in [3400.0, 3700.0\text{ mm}]$ ($+2455\text{ to }+2755\text{ mm}$ AFF, $262\text{ mm}$ below ceiling soffit).
   * **First Floor (`FF_Bedroom_AC_Indoor_Unit`):** 1:1 matching unit translated by $\Delta Z = +3173.0\text{ mm}$ ($Z \in [6573.0, 6873.0\text{ mm}]$).
2. **Dedicated Modular AC Power Switchboards (Relocated to South Side of AC):**
   * **Ground Floor (`Bedroom_AC_Switchboard`):** High-level 2-module plate ($120 \times 15 \times 75\text{ mm}$, Electric Cyan `#00D2FF`) mounted at $X = 2082.7\text{ mm}$, centered at $Y = 7000.0\text{ mm}$ (South of the indoor unit at $Y = 6175\text{ mm}$), $Z = 3300.0\text{ mm}$ ($+2355\text{ mm}$ AFF). Houses a heavy-duty **20A DP Switch with Neon Status Indicator + 16A/20A Shuttered Socket**.
   * **First Floor (`FF_Bedroom_AC_Switchboard`):** Symmetrical high-level board at $Z = 6473.0\text{ mm}$ ($Y = 7000.0\text{ mm}$).
3. **Concealed MEP Conduit Routing (0.0mm Gaps):**
   * **Ceiling Slab Runs (`Bedroom_Slab_Conduit_Network Solid 4` & FF Solid 4):** $25\text{ mm}$ rigid PVC pipe in Conduit Orange (`#FF7300`) runs from **Pot 4** ($X = 2600.0, Y = 5400.0\text{ mm}$) south to $Y = 7000.0\text{ mm}$, then west to the East wall drop at $(X = 2082.7, Y = 7000.0\text{ mm})$.
   * **Vertical Wall Chases (`Bedroom_Slab_Wall_Drops Solid 2` & FF Solid 2):** $25\text{ mm}$ rigid PVC pipe in Emerald Green (`#10AC84`) drops vertically from ceiling slab ($Z = 4020.0\text{ mm}$ GF / $Z = 7193.0\text{ mm}$ FF) straight into the top knockout of the AC switchboard at $Z = 3337.5\text{ mm}$ with **$0.000\text{ mm}$ gap**.

---

### 56.3 Verification Audit Summary

| Component | Coordinates / Elevation | Parent Container | Status |
| :--- | :--- | :--- | :---: |
| **`Bedroom_Loft_East`** | GF East Wall ($Z = 3048\text{ mm}$) | `Bedroom` | **REMOVED** |
| **`FF_Bedroom_Loft_East`** | FF East Wall ($Z = 6221\text{ mm}$) | `FF_Bedroom` | **REMOVED** |
| **`Bedroom_Loft_North`** | GF North Wall ($Y \in [4673, 5283]$) | `Bedroom` | **RETAINED** |
| **`FF_Bedroom_Loft_North`** | FF North Wall ($Y \in [4673, 5283]$) | `FF_Bedroom` | **RETAINED** |
| **`Bedroom_AC_Indoor_Unit`** | GF East Wall ($Y = 6175, Z = 3550$) | `Bedroom` | **ACTIVE** |
| **`FF_Bedroom_AC_Indoor_Unit`**| FF East Wall ($Y = 6175, Z = 6723$) | `FF_Bedroom` | **ACTIVE** |
| **`Bedroom_AC_Switchboard`** | GF East Wall ($Y = 7000, Z = 3300$) | `Electrical_Switchboards_Group` | **ACTIVE (South of AC, 0.0mm gap)** |
| **`FF_Bedroom_AC_Switchboard`**| FF East Wall ($Y = 7000, Z = 6473$) | `FF_Electrical_Switchboards_Group` | **ACTIVE (South of AC, 0.0mm gap)** |
| **Slab $\to$ Drop $\to$ Switchboard**| Pot 4 $\to$ Wall Drop $\to$ SB-AC | Bedroom Conduits & Drops | **100% Sealed (0.0mm gap)** |


---
