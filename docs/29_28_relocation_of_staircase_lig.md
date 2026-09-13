## 28. Relocation of Staircase Light Switchbox to South Staircase Wall

In accordance with user requirements (*"can we keep staiscase light switchbox on south staircase wall"*), the primary staircase lighting switchbox (`SB_STAIR1`) and its First Floor twin (`FF_SB_STAIR1`) have been relocated from the North staircase wall (`Wall_Stair_North`) to the **South staircase partition wall** (`Wall_Stair_SE_SW`):

```carousel
![Annotated Isometric View Showing SB_STAIR1 on South Wall and Continuous Chased Conduit to Toilet East Luminaire](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\staircase_switchbox_south_wall_annotated.png)
<!-- slide -->
![Close-Up View of SB_STAIR1 on Wall_Stair_SE_SW at Staircase Entrance Beside MDB](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\staircase_switchbox_south_wall_closeup.png)
<!-- slide -->
![Two-Storey Overview Showing Identical Vertical Alignment on Both Ground and First Floor](C:\Users\prade\.gemini\antigravity\brain\102a4231-65f5-4ac9-bae0-88dae5a0acab\two_storey_staircase_south_wall_iso.png)
```

### 28.1 Architectural & Ergonomic Rationale
1. **Direct Entrance Ergonomics:**
   - Previously, placing the switchbox on `Wall_Stair_North` ($Y = 228.6\text{ mm}$) required a person entering the staircase from the living room to walk past the first 3 steps into the flight before reaching the switch.
   - On the South wall (`Wall_Stair_SE_SW` at $Y = 1714.5\text{ mm}$), the switchboard is positioned right at the entry threshold ($X = 2017.5\text{ mm}$), allowing anyone approaching from the Living Room or Foyer to switch on the staircase light before taking the first step.
2. **Structural Integration & Clearance:**
   - Positioned $74.4\text{ mm}$ east of structural column `Col_Stair_SE` ($X = 1943.1\text{ mm}$), ensuring the box is embedded entirely within the solid $228.6\text{ mm}$ (9") brickwork without requiring structural concrete chipping.
3. **Continuous Masonry Conduit Path:**
   - `Wall_Stair_SE_SW` meets `Toilet_Wall_East` at the South-East corner ($X = 3800.0\text{ mm}, Y = 1714.5\text{ mm}$).
   - This allows a direct, continuous wall-chased conduit run along the South wall that turns a single clean $90^\circ$ bend into `Toilet_Wall_East` and rises straight into the bottom knockout of `Staircase_Wall_Light_Fixture` ($Z = 3200.0\text{ mm}$).
   - Completely eliminates exposed conduits, ceiling crossings, or routing around open stairwell voids.

### 28.2 Technical Coordinates & Component Schedule
* **Ground Floor Switchboard (`SB_STAIR1`):**
  - **Host Wall:** `Wall_Stair_SE_SW` (Inner face at $Y = 1714.5\text{ mm}$)
  - **Coordinates:** Centered at $(X = 2017.5\text{ mm}, Y = 1707.5\text{ mm}, Z = 2151.9\text{ mm})$
  - **Mounting Height:** $+1200.0\text{ mm}$ AFF from finished ground floor ($Z = 914.4 + 37.5 = 951.9\text{ mm}$)
  - **Faceplate:** 2-Module pearl white modular plate with rocker switch controlling the two-way staircase circuit.
* **First Floor Duplicate Switchboard (`FF_SB_STAIR1`):**
  - **Host Wall:** `FF_Wall_Stair_SE_SW`
  - **Coordinates:** Centered at $(X = 2017.5\text{ mm}, Y = 1707.5\text{ mm}, Z = 5324.9\text{ mm})$
  - **Mounting Height:** $+1200.0\text{ mm}$ AFF from finished first floor ($Z = 4087.4 + 37.5 = 4124.9\text{ mm}$, $\Delta Z = +3173.0\text{ mm}$).
* **Continuous Wall-Chased PVC Conduit Run:**
  - $25\text{ mm}$ OD heavy-duty rigid PVC pipe in safety **Emerald Green (`#10AC84`)**.
  - **Ground Floor:** Runs from `SB_STAIR1` at $(2017.5, 1714.5, 2151.9\text{ mm})$ along `Wall_Stair_SE_SW` to corner $(3800.0, 1714.5\text{ mm})$, turns onto `Toilet_Wall_East` and rises vertically to $(3800.0, 970.0, 3200.0\text{ mm})$ into the bottom knockout of `Staircase_Wall_Light_Fixture`.
  - **First Floor:** Identical run connecting `FF_SB_STAIR1` along `FF_Wall_Stair_SE_SW` to `FF_Staircase_Wall_Light_Fixture` at $Z = 6373.0\text{ mm}$.
  - Supply power is fed via a dedicated vertical chase drop from the MDB entrance beam at $(1943.1, 1943.1, 4020.0\text{ mm})$.

### 28.3 Master Model Verification
* **CAD Master File:** `HomeConstruction.FCStd`
* **Object Count:** **422 objects** (100% stable).
* **Hierarchical Tree:** Strictly 3 master root groups (`Ground_Floor_Group`, `First_Floor_Group`, `Master_Rooftop_Terrace_Group`).
* **Document Health:** 0 cyclic dependencies, 0 null shapes, 0 recompute errors.

---
