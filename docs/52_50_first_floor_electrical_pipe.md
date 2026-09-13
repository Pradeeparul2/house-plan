## 50. First Floor Electrical Pipelines — Identical Grouping Parity

Following client directive (*"same like group the FF electrical pipelines it should same like GF"*), the exact same hierarchical group architecture has been replicated for the First Floor (FF) electrical pipelines in `HomeConstruction.FCStd`.

### 50.1 First Floor Group Hierarchy Architecture
Inside `FF_Electrical_Slab_Conduit_and_Lighting_Group`, physical pipelines are now cleanly separated from ceiling fixtures:

* **Master Group:** `FF_Electrical_Pipelines_Group`
  * **Label:** `First Floor Electrical Pipelines (Complete Conduits & Drops)`
  * **Functionality:** Provides single-click global visibility toggling (Spacebar), batch color/transparency adjustments, and unified tree navigation for all 10 First Floor pipeline objects.

### 50.2 Functional Subgroups (1:1 GF Parity)
1. **`FF_Slab_Conduits_Group` (FF Ceiling Slab 25mm PVC Conduit Networks — 4 Objects):**
   * `FF_Living_Slab_Conduit_Network` (First Floor Living Room slab conduits & dual kitchen feeder loop).
   * `FF_Bedroom_Slab_Conduit_Network` (First Floor Bedroom spine, downlight header & corridor feeder).
   * `FF_Electrical_Slab_Conduit_Network` (First Floor Kitchen, Sitout/Balcony header & Staircase feeder).
   * `FF_Toilet_Electrical_Conduits` (First Floor Toilet complete ceiling slab conduit grid).

2. **`FF_Wall_Drops_Group` (FF Chased Vertical Wall Conduits & Drops — 6 Objects):**
   * `FF_Living_Slab_Wall_Drops` (5 drops: Living Room console, TV panel, AC split socket, MDB & kitchen console).
   * `FF_Bedroom_Slab_Wall_Drops` (2 drops: Primary bedside console & dressing table console).
   * `FF_Electrical_Slab_Wall_Drops` (6 drops: Balcony switchboard, staircase switchboard, kitchen prep & sink drops).
   * `FF_Bedroom_Tubelight_Conduit_Drop` (Dedicated wall chase for First Floor Bedroom 4ft LED tubelight).
   * `FF_Kitchen_Tubelight_Conduit_Drop` (Dedicated wall chase for First Floor Kitchen 4ft LED tubelight).
   * `FF_Kitchen_Exhaust_Fan_Conduit_Drop` (Vertical drop to 150mm kitchen exhaust fan cowl).

### 50.3 Full Floor-to-Floor Parity Table

| Category | Ground Floor Group & Contents | First Floor Group & Contents |
| :--- | :--- | :--- |
| **Master Container** | `GF_Electrical_Pipelines_Group` | `FF_Electrical_Pipelines_Group` |
| **Slab Conduits Subgroup** | `GF_Slab_Conduits_Group` (4 items) | `FF_Slab_Conduits_Group` (4 items) |
| **Wall Drops Subgroup** | `GF_Wall_Drops_Group` (6 items) | `FF_Wall_Drops_Group` (6 items) |
| **Ceiling Fixtures (Parent)** | Downlight pots, fan boxes, wall lights | Downlight pots, fan boxes, wall lights |

* **Document Status:** 100% synchronized across floors; recomputed with 0 errors and saved to `HomeConstruction.FCStd`.

---
