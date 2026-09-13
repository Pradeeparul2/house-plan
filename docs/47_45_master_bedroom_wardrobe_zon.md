## 45. Master Bedroom Wardrobe Zone — De-Cluttering & Redundant MEP Excision

Following client directive (*"on the 3d model i see wardrope siwtch box and behaind the wardrop horizonal slap switch box both need to be remove on 3d model"*), the Master Bedroom wardrobe zone ($X \in [2082.7, 2997.1\text{ mm}], Y \in [4673.5, 5283.1\text{ mm}]$) has been thoroughly audited and cleared of all conflicting electrical conduits and wall drops in both Ground Floor and First Floor models.

```carousel
![Master Bedroom Wardrobe Zone Cleared 3D](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/wardrobe_switchbox_removal_3d_annotated.png)
<!-- slide -->
![Ground Floor Electrical Plan Wardrobe Cleaned](C:/Users/prade/.gemini/antigravity/brain/086e9390-dcd1-4cec-9724-3cc5bbdd6a28/gf_electrical_plan_wardrobe_cleaned_annotated.png)
```

### 45.1 Excised Conflicting MEP Elements

1. **Excised Wardrobe Switchbox (`GF SB 11` / Drop 7):**
   * **Location:** $X = 2937.5\text{ mm}, Y = 4692.5\text{ mm}$.
   * **Issue:** Positioned directly against the outer side panel of the wooden wardrobe unit, creating clutter between the wardrobe and the entrance door.
   * **Action:** Excised vertical drop solid and its horizontal branch conduit stub (`Net 5` in `Living_Slab_Conduit_Network`).
2. **Excised Behind-Wardrobe Switchbox Drop (`GF SB 8` / Drop 5):**
   * **Location:** $X = 2107.5\text{ mm}, Y = 4925.0\text{ mm}$.
   * **Issue:** Trapped directly on the West brickwork wall behind the full-height wardrobe backing board ($H = 2100\text{ mm}$), creating an inaccessible fire/code hazard.
   * **Action:** Excised vertical drop solid completely from `Living_Slab_Wall_Drops`.
3. **Excised Behind-Wardrobe Horizontal Slab Conduit (`Net 6`):**
   * **Location:** $Y = 4925.0\text{ mm}$, spanning $X = 1867.5 \to 2514.6\text{ mm}$.
   * **Issue:** Redundant slab pipe running across the wardrobe ceiling zone purely to feed the trapped drop.
   * **Action:** Excised horizontal slab cylinder solid from `Living_Slab_Conduit_Network`. Truncated central spine `Net 0` back to $Y = 4673.5\text{ mm}$, removing dead-end stub.
4. **Excised Wardrobe Ceiling Pot & Feed (`Pot 11` & `Solid 2`):**
   * **Location:** `Pot 11` at $(2572.9, 4720.2\text{ mm})$ and slab feed at $X = 2600.0\text{ mm}, Y \in [4720.0, 5400.0\text{ mm}]$.
   * **Action:** Excised ceiling pot from `Electrical_Slab_Light_Pots` and excised feed cylinder from `Bedroom_Slab_Conduit_Network`.

---

### 45.2 Streamlined Continuous Feeder Architecture

* **Continuous Direct Header ($Y = 4673.5\text{ mm}$):**
  $$\text{Corridor Spine } (X=2514.6) \xrightarrow{\text{Direct Wall Header}} \text{Door Console SB-9 } (X=3325.0) \xrightarrow{\text{Central Header}} \text{Central Spine } (X=3500.0)$$
* **Clearance Achieved:**
  - Full-height wardrobe zone is **100% free of all conduits, drops, and junction boxes**.
  - All bedroom controls consolidated strictly into **`SB-9`** (Entrance door jamb at $+1200\text{ mm}$ AFF) and **`SB-10`** (Bedside console at $+750\text{ mm}$ AFF).
* **First Floor (G+1) Synchronized:**
  - Mirrored updates to `FF_Living_Slab_Conduit_Network`, `FF_Living_Slab_Wall_Drops`, `FF_Bedroom_Slab_Conduit_Network`, and `FF_Electrical_Slab_Light_Pots` at $\Delta Z = +3173.0\text{ mm}$.
  - Verified 0 invalid shapes; saved in `HomeConstruction.FCStd`.

---
