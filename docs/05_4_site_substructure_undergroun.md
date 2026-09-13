## 4. Site, Substructure & Underground Utilities

### 4.1 Substructure Datum Levels

- **Road Level (Ground Zero):** $Z \in [0.0, 30.48\text{ mm}]$ ($1"$). Wide asphalt road profile ($12000 \times 4572\text{ mm}$) at the front.
- **Plinth Beam Level:** $Z = 914.4\text{ mm}$ ($3'\text{-}0"$ above road level). Protects against monsoon flooding and surface runoff.
- **Finished Floor Level (FFL):** $Z = 944.88\text{ mm}$ ($914.4\text{ mm}$ RCC plinth $+ 30.48\text{ mm}$ screed & anti-skid ceramic tiles).

### 4.2 Underground Utility Infrastructure

> [!NOTE]
> **Construction Update (Refer to Sections 60, 61 & 62):** Both the Underground Sump and Septic Tank have been vertically aligned up to the finished plinth level ($Z = +914.4	ext{ mm}$) with airtight flush stainless steel inspection manholes, and horizontally fitted between isolated footing raft projections to achieve 100% collision-free substructure geometry.

```
+-------------------------------------------------------------------------+
|                  ROAD LEVEL (Z = 0 to 30.5 mm)                          |
+-------------------+---------------------------------+-------------------+
                    |    FOUNDATION STEPS (6 Risers)  |
                    |    Width: 1350 mm | Red Finish  |
                    +---------------------------------+
                    |    PLINTH BEAM (Z = 914.4 mm)   |
+-------------------+---------------------------------+-------------------+
|  SUMP WATER TANK  |      EARTH BACKFILL / PLINTH    |    SEPTIC TANK    |
|  Size: 1.8x1.2x1.8m|                                 |    1.2x1.2x1.8m   |
|  Capacity: 3888 L |                                 |    Capacity: 2592L|
|  Under Sitout     |                                 |    Under Toilet   |
+-------------------+---------------------------------+-------------------+
```

1. **Underground Sump Water Tank (`Sump_UG_Water_Tank`)**:
   - **Location:** Under the Sitout plinth ($X \in [0.0, 1800.0\text{ mm}]$, $Y \in [0.0, 1200.0\text{ mm}]$, $Z \in [-1800.0, 0.0\text{ mm}]$).
   - **Dimensions:** $1800\text{ mm}$ (L) $\times 1200\text{ mm}$ (W) $\times 1800\text{ mm}$ (D).
   - **Effective Volume:** $3.89\text{ m}^3$ ($\approx 3,888\text{ Liters}$ / $1,027\text{ Gallons}$).
   - **Construction:** $150\text{ mm}$ waterproofed reinforced concrete walls with access inspection manhole.
2. **Underground Septic Tank (`Septic_Tank`)**:
   - **Location:** Under the Toilet plinth ($X \in [3810.0, 5010.0\text{ mm}]$, $Y \in [0.0, 1200.0\text{ mm}]$, $Z \in [-1800.0, 0.0\text{ mm}]$).
   - **Dimensions:** $1200\text{ mm}$ (L) $\times 1200\text{ mm}$ (W) $\times 1800\text{ mm}$ (D).
   - **Effective Volume:** $2.59\text{ m}^3$ ($\approx 2,592\text{ Liters}$).
   - **Design:** Twin-chamber anaerobic baffle tank with top inspection cover.
3. **Primary Entrance Steps (`Steps_Road_To_Sitout`)**:
   - **Dimensions:** Width = $1350\text{ mm}$ ($X \in [300.0, 1650.0\text{ mm}]$), Projection = $1275\text{ mm}$ ($Y \in [-1275.0, 0.0\text{ mm}]$).
   - **Step Geometry:** 6 uniform risers of $152.4\text{ mm}$ ($6"$) each; treads of $255\text{ mm}$ ($10"$).
   - **Finish:** Heavy-duty anti-skid terracotta-red flamed granite / clay paving tiles.

---
