## 27. De-scoping and Removal of Utility Switchboard (SB-UTIL) from First Floor

Per client instruction (*"SB-UTIL not needed on FF"*), the under-stair utility power board and its associated conduit feeds were completely removed from the **First Floor** while remaining fully operational on the **Ground Floor**:

```carousel
![Two-Storey Perspective Showing Ground Floor Utility Service Preserved and First Floor De-Cluttered](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\two_storey_sb_util_gf_only_iso.png)
<!-- slide -->
![First Floor Under-Stair Wall View Confirming Complete Removal of SB-UTIL and Vertical Drops](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\ff_under_stair_clean_no_sb_util.png)
```

### 27.1 Engineering Rationale
* **Equipment Zoning:** The under-stair wet-utility zone (Automatic Washing Machine and Submersible Sump Pump) is strictly localized to the **Ground Floor** substructure. The First Floor stairwell leads upward to the open rooftop terrace and does not house laundry appliances or sump drainage pumps.
* **Aesthetic & Structural Minimization:** Removing the redundant switchboard eliminates unnecessary wall chasing into `FF_Wall_Stair_SE_SW`, preserving the unbroken masonry finish of the upper residence corridor and eliminating dead electrical terminations.

### 27.2 Components Removed from First Floor
1. **Modular Switchboard Faceplate (`FF_Electrical_Switchboard_Plates`):**
   - Removed `FF_SB-UTIL` 4-Module plate from $(X = 3050.0\text{ mm}, Y = 1707.5\text{ mm}, Z = 5160.5\text{ mm})$.
   - Streamlined from 18 to **17 modular switchboards** (`FF_MDB` + 16 room switchboards).
2. **Rocker Switches & Sockets (`FF_Electrical_Switchboard_Rocker_Switches`):**
   - Removed $2 \times 16\text{A}$ modular switch/socket blocks.
   - Streamlined from 25 to **23 solid rocker elements**.
3. **Vertical Wall Conduit Drop (`FF_Electrical_Slab_Wall_Drops`):**
   - Removed the $25\text{ mm}$ rigid PVC vertical drop at $(3050.0, 1720.0\text{ mm})$ ($Z = 7193.0 \to 5198.0\text{ mm}$).
   - Streamlined from 20 to **19 solid conduit drops**.
4. **Ceiling Slab Conduit Distribution Run (`FF_Electrical_Slab_Conduit_Network`):**
   - Removed the overhead slab branch conduit running from $(3810.0, 1828.8\text{ mm})$ to $(3050.0, 1720.0\text{ mm})$.
   - Streamlined from 17 to **16 solid slab conduit runs**.

### 27.3 Ground Floor Service Retained
* **`SB-UTIL` Ground Floor Status:** 100% active and preserved at $(X = 3050.0\text{ mm}, Y = 1714.5\text{ mm}, Z = 1987.5\text{ mm})$ on `Wall_Stair_SE_SW`, complete with its $2 \times 16\text{A}$ dedicated sockets, vertical wall drop, and ceiling slab supply link powering the washing machine and sump motor.

### 27.4 Master Model Validation
* **Master Document:** `HomeConstruction.FCStd`
* **Object Count:** 422 objects (strictly 3 root groups, zero orphan features).
* **Errors:** 0 cyclic dependencies, 0 null shapes, 0 invalid objects.

---
