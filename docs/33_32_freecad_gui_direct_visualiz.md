## 32. FreeCAD GUI Direct Visualization & Tree Node Separation for Staircase Lighting and Switchbox (`SB_STAIR1`)

To address the client's notification (*"i dont see stairs light and switchbox on FreeCAD"*), targeted diagnostic and visual optimization steps were performed directly in the active FreeCAD document:

```carousel
![Annotated FreeCAD 3D Viewport Showing Staircase Wall Light Fixture, SB-STAIR1 Switchbox, and Connecting Conduit Drop](C:\Users\prade\.gemini\antigravity\brain\086e9390-dcd1-4cec-9724-3cc5bbdd6a28\staircase_electrical_located_annotated.png)
<!-- slide -->
![Close-Up View of the Lowered Luminaire on the East Wall of Toilet](C:\Users\prade\OneDrive\Desktop\home plan\renders\crop_light_fixture.png)
<!-- slide -->
![Close-Up View of the SB-STAIR1 Modular Switchboard on the South Partition Wall](C:\Users\prade\OneDrive\Desktop\home plan\renders\crop_entry_area.png)
```

### 32.1 Root Cause of Initial GUI Invisibility
1. **Camera Position & Viewport Scale:** The active FreeCAD 3D camera was left at an axonometric full-building scale ($>15\text{ m}$ away), making small $75\text{ mm}$ switchplates and $65\text{ mm}$ wall luminaires visually inconspicuous without zooming.
2. **Hidden Conduit Layer:** The vertical chased wall conduits (`Electrical_Slab_Wall_Drops`) had their visibility property set to `False`, hiding the emerald green connection pipe.
3. **Compound Aggregation in Model Tree:** `SB_STAIR1` was previously bundled as Solid 14 within the 19-solid compound `Electrical_Switchboard_Plates`, preventing the user from clicking a single node in the FreeCAD tree to highlight the staircase switchbox.
4. **Monochrome Shading:** `Staircase_Wall_Light_Fixture` was styled in neutral grey/white (`0.95, 0.95, 0.95`), causing it to blend into the concrete mid-landing and masonry background.

### 32.2 Enhancements Applied
1. **Dedicated Tree Objects Created:**
   - **Ground Floor:** Separated Solid 14 into an independent feature: `Staircase_Switchboard_SB_STAIR1` (Label: `Staircase Switchboard SB-STAIR1 (South Wall)`), located directly inside `Electrical_Switchboards_Group`.
   - **First Floor:** Separated Solid 13 into `FF_Staircase_Switchboard_SB_STAIR1` under `FF_Electrical_Switchboards_Group`.
2. **High-Contrast Luminaire Styling:**
   - Redesigned `Staircase_Wall_Light_Fixture` with a 3-part architectural sconce model (mounting bracket, outer housing, and glowing warm gold diffuser panel `#F1C40F`).
   - Styled `Staircase_Switchboard_SB_STAIR1` in vibrant Electric Cyan (`#00D2FF`) with a crisp architectural border.
3. **Viewport Camera Realignment:**
   - Set `Stair_Flight_1` and `Stair_Flight_2` transparency to $40\%$ so the internal utility bay and both devices are visible simultaneously through the flights.
   - Re-centered the active FreeCAD viewport camera directly on the staircase bay with both items selected and highlighted in green.

---
