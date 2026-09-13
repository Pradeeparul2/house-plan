## 49. Ground Floor Electrical Pipelines — Unified Tree Grouping

Following client directive (*"now group the GF pipelines"*), all Ground Floor electrical conduit networks and wall chased drops have been structured into a dedicated, hierarchical grouping inside `HomeConstruction.FCStd`.

```carousel
![Ground Floor Electrical Pipelines Group Hierarchy](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/gf_pipelines_grouped_hierarchy.png)
```

### 49.1 Group Hierarchy Architecture
Inside `Electrical_Slab_Conduit_and_Lighting_Group`, a dedicated master container was created to separate physical pipelines from lighting fixtures (pots & fan boxes):

* **Master Group:** `GF_Electrical_Pipelines_Group`
  * **Label:** `Ground Floor Electrical Pipelines (Complete Conduits & Drops)`
  * **Functionality:** Provides single-click global visibility toggling (Spacebar), batch color/transparency adjustments, and clean tree navigation for all 10 Ground Floor pipeline objects.

### 49.2 Functional Subgroups
1. **`GF_Slab_Conduits_Group` (Ceiling Slab 25mm PVC Conduit Networks):**
   * `Living_Slab_Conduit_Network` (8 solids: Central corridor spine, front & rear headers, south cross-bar, AC feeder, Main DB feed, and dual kitchen feeders).
   * `Bedroom_Slab_Conduit_Network` (4 solids: Dedicated bedroom spine, east-west downlight header, corridor feeder link, and north wall run).
   * `Electrical_Slab_Conduit_Network` (10 solids: Kitchen downlight header & central spine, Sitout entrance beam header & central light branch, and Staircase east wall feeder).
   * `Toilet_Electrical_Conduits` (Complete toilet ceiling slab conduit grid).

2. **`GF_Wall_Drops_Group` (Chased Vertical Wall Conduits & Drops):**
   * `Living_Slab_Wall_Drops` (5 drops: SB-1 DB, SB-LR console, SB-TV panel, SB-AC split socket, and SB-13 kitchen console).
   * `Bedroom_Slab_Wall_Drops` (2 drops: SB-5 primary bedside console and SB-6 dressing table console).
   * `Electrical_Slab_Wall_Drops` (6 drops: SB-STAIR entrance switchboard, SB-STAIR1 staircase switchboard, SB-14 prep counter, and SB-15 sink counter).
   * `Bedroom_Tubelight_Conduit_Drop` (Dedicated wall chase for Master Bedroom 4ft LED tubelight).
   * `Kitchen_Tubelight_Conduit_Drop` (Dedicated wall chase for Kitchen 4ft LED tubelight).
   * `Kitchen_Exhaust_Fan_Conduit_Drop` (Vertical drop to 150mm kitchen exhaust fan cowl).

### 49.3 Benefits & FreeCAD Tree View State
* **No Loose Objects:** Previously unparented objects (`Toilet_Electrical_Conduits`, `Bedroom_Tubelight_Conduit_Drop`) are now properly organized.
* **Separation of Fixtures & Piping:** Ceiling downlight pots (`Electrical_Slab_Light_Pots`, `Living_Slab_Light_Pots`) and fan boxes (`Electrical_Slab_Fan_Boxes`, `Living_Slab_Fan_Box`) remain in the parent lighting group, keeping fixtures distinct from pipelines.
* **Document Status:** Recomputed with 0 errors and saved to `HomeConstruction.FCStd`.

---
