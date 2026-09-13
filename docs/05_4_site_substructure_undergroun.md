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

### 4.3 Substructure Foundation Coordination & Plinth Ring Flush Alignment

1. **Monolithic Stepped Raft Interface (Column C8 & Septic Tank)**:
   - **Footing C8 (`Footing_N8_C12`):** $X \in [3695.7, 5029.2\text{ mm}]$, $Y \in [0.0, 1200.0\text{ mm}]$, $Z \in [-1600.0, -1200.0\text{ mm}]$ ($400\text{ mm}$ thick RCC).
   - **Septic Tank Raft (`Septic_Raft_Foundation_Slab`):** $X \in [3695.7, 5029.2\text{ mm}]$, $Y \in [1200.0, 1943.1\text{ mm}]$, $Z \in [-1600.0, -1200.0\text{ mm}]$ ($400\text{ mm}$ thick RCC).
   - **Coordination Status:** Aligned along the exact same X-span ($1333.5\text{ mm}$ width) forming a continuous, monolithic stepped raft entity from $Y = 0.0$ to $Y = 1943.1\text{ mm}$ with $0.00\text{ mm}$ lateral mismatch.
   - **PCC Blinding Bed:** Aligned continuous bed $X \in [3645.7, 5029.2\text{ mm}]$, $Z \in [-1700.0, -1600.0\text{ mm}]$.

2. **Plinth Beam Network Flush Alignment (`PB1_Rear_South`)**:
   - Standardized to $300\text{ mm}$ depth ($Z \in [614.4, 914.4\text{ mm}]$).
   - Top face sits exactly flush with FFL datum $Z = +914.4\text{ mm}$ ($+3'\text{-}0"$), matching `PB1_Front_North`, `PB1_East_Flank`, and `PB1_West_Flank` with $0.00\text{ mm}$ floor ridge.

---
