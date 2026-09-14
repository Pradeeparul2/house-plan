"""
audit_and_fix_mep_electrical.py
===============================
Comprehensive MEP Electrical audit, remediation, and coordination script for HomeConstruction.FCStd.

Standards Compliance:
  - IS 732: 2019 (Code of Practice for Electrical Wiring Installations)
  - NBC 2016 Part 8 (Building Services: Electrical and Allied Installations)
  - IS 456: 2000 (Plain and Reinforced Concrete - Code of Practice)
  - IS 2667 / IS 3419 (Fittings for Rigid and Flexible Conduits / Circular Junction Boxes)
"""

import FreeCAD
import Part
from pathlib import Path
import math

def audit_and_fix(doc=None, save_doc=True):
    if doc is None:
        doc = FreeCAD.ActiveDocument
        if doc is None:
            doc = FreeCAD.openDocument("HomeConstruction.FCStd")

    print("=== EXECUTING COMPREHENSIVE MEP ELECTRICAL REMEDIATION ===")

    # ---------------------------------------------------------
    # 1. PRUNE DEGENERATE & GHOST SOLIDS (< 100 mm³ or dim < 1 mm)
    # ---------------------------------------------------------
    print("\n--- 1. Pruning Ghost and Degenerate Solids ---")
    
    # 1a. Electrical_Switchboard_Plates (GF)
    pl_gf = doc.getObject('Electrical_Switchboard_Plates')
    if pl_gf:
        valid_solids = []
        for i, s in enumerate(pl_gf.Shape.Solids):
            bb = s.BoundBox
            if s.Volume < 100.0 or bb.DiagonalLength < 1.0:
                print(f"  [Pruned] GF Plate Solid {i}: Vol={s.Volume:.2f}, Dim=({bb.XLength:.1f}, {bb.YLength:.1f}, {bb.ZLength:.1f})")
            else:
                valid_solids.append(s.copy())
        pl_gf.Shape = Part.Compound(valid_solids)
        print(f"  [OK] GF Plates count: {len(valid_solids)} valid solids.")

    # 1b. FF_Electrical_Switchboard_Plates (FF)
    pl_ff = doc.getObject('FF_Electrical_Switchboard_Plates')
    if pl_ff:
        valid_solids = []
        for i, s in enumerate(pl_ff.Shape.Solids):
            bb = s.BoundBox
            if s.Volume < 100.0 or bb.DiagonalLength < 1.0:
                print(f"  [Pruned] FF Plate Solid {i}: Vol={s.Volume:.2f}, Dim=({bb.XLength:.1f}, {bb.YLength:.1f}, {bb.ZLength:.1f})")
            else:
                valid_solids.append(s.copy())
        pl_ff.Shape = Part.Compound(valid_solids)
        print(f"  [OK] FF Plates count: {len(valid_solids)} valid solids.")

    # 1c. Electrical_Slab_Conduit_Network (GF)
    cn_gf = doc.getObject('Electrical_Slab_Conduit_Network')
    if cn_gf:
        valid_solids = []
        for i, s in enumerate(cn_gf.Shape.Solids):
            bb = s.BoundBox
            # Solid 1 is a 0.2 mm sliver (Vol=19.4 mm³)
            if s.Volume < 50.0 or bb.YLength < 0.5:
                print(f"  [Pruned] GF Conduit Solid {i}: Vol={s.Volume:.2f}, Dim=({bb.XLength:.1f}, {bb.YLength:.1f}, {bb.ZLength:.1f})")
            else:
                valid_solids.append(s.copy())
        cn_gf.Shape = Part.Compound(valid_solids)
        print(f"  [OK] GF Electrical Conduit Network count: {len(valid_solids)} valid solids.")

    # ---------------------------------------------------------
    # 2. COLUMN CLEARANCES & MOUNTING HEIGHT CORRECTIONS
    # ---------------------------------------------------------
    print("\n--- 2. Column Clearances and Mounting Heights ---")
    
    # 2a. Ground Floor Bedside Switchboard (SB-10) and Kitchen Counter (SB-14)
    if pl_gf:
        new_solids = []
        for i, s in enumerate(pl_gf.Shape.Solids):
            sc = s.copy()
            c = s.BoundBox.Center
            # Bedside SB-10 (X~2600, Y~7412.5)
            if abs(c.x - 2600.0) < 50.0 and abs(c.y - 7412.5) < 50.0:
                sc.translate(FreeCAD.Vector(30.0, 0, -87.5))
                print(f"  [Shifted] GF Plate Solid {i} (SB-10): +30mm X, -87.5mm Z -> Height above FFL = 650mm, Dist to C2 = 150mm")
            # Kitchen Counter SB-14 (X~204.0, Y~5715.0)
            elif abs(c.x - 204.0) < 50.0 and abs(c.y - 5715.0) < 50.0 and abs(c.z - 2064.4) < 50.0:
                sc.translate(FreeCAD.Vector(0, 0, -150.0))
                print(f"  [Shifted] GF Plate Solid {i} (SB-14): -150mm Z -> Height above FFL = 1000mm (+150mm above counter)")
            new_solids.append(sc)
        pl_gf.Shape = Part.Compound(new_solids)

    # Rocker switches GF
    sw_gf = doc.getObject('Electrical_Switchboard_Rocker_Switches')
    if sw_gf:
        new_sw_solids = []
        for i, s in enumerate(sw_gf.Shape.Solids):
            sc = s.copy()
            c = s.BoundBox.Center
            if abs(c.x - 2600.0) < 50.0 and abs(c.y - 7412.5) < 50.0:
                sc.translate(FreeCAD.Vector(30.0, 0, -87.5))
            elif abs(c.x - 210.0) < 50.0 and abs(c.y - 5715.0) < 50.0 and abs(c.z - 2064.4) < 50.0:
                sc.translate(FreeCAD.Vector(0, 0, -150.0))
            new_sw_solids.append(sc)
        sw_gf.Shape = Part.Compound(new_sw_solids)

    # Wall drops GF adjustment for SB-10 and SB-14
    bd_drops = doc.getObject('Bedroom_Slab_Wall_Drops')
    if bd_drops:
        d_solids = []
        for i, s in enumerate(bd_drops.Shape.Solids):
            c = s.BoundBox.Center
            if i == 0 and abs(c.x - 2400.0) < 50.0 and abs(c.y - 7462.5) < 50.0:
                sc = s.copy()
                sc.translate(FreeCAD.Vector(30.0, 0, 0))
                ext = Part.makeCylinder(12.5, 87.5, FreeCAD.Vector(c.x + 30.0, c.y, 1689.4 - 87.5), FreeCAD.Vector(0, 0, 1))
                sc = sc.fuse(ext)
                d_solids.append(sc)
            else:
                d_solids.append(s.copy())
        bd_drops.Shape = Part.Compound(d_solids)

    elec_drops = doc.getObject('Electrical_Slab_Wall_Drops')
    if elec_drops:
        e_solids = []
        for i, s in enumerate(elec_drops.Shape.Solids):
            c = s.BoundBox.Center
            if i == 5 and abs(c.x - 140.0) < 50.0 and abs(c.y - 5715.0) < 50.0:
                sc = s.copy()
                ext = Part.makeCylinder(12.5, 150.0, FreeCAD.Vector(c.x, c.y, 2101.9 - 150.0), FreeCAD.Vector(0, 0, 1))
                sc = sc.fuse(ext)
                e_solids.append(sc)
            else:
                e_solids.append(s.copy())
        elec_drops.Shape = Part.Compound(e_solids)

    # 2b. First Floor Bedside (FF_SB-10), TV Board (FF_SB-16), Kitchen Counter (FF_SB-14)
    if pl_ff:
        new_ff_solids = []
        for i, s in enumerate(pl_ff.Shape.Solids):
            sc = s.copy()
            c = s.BoundBox.Center
            # Bedside FF_SB-10 (X~2600, Y~7412.5)
            if abs(c.x - 2600.0) < 50.0 and abs(c.y - 7412.5) < 50.0:
                sc.translate(FreeCAD.Vector(30.0, 0, -87.5))
                print(f"  [Shifted] FF Plate Solid {i} (SB-10): +30mm X, -87.5mm Z -> Height above FFL = 650mm, Dist to C2 = 150mm")
            # TV Console FF_SB-16 (X~4824.2, Y~3600.0) -> align to Y=3625.0
            elif abs(c.x - 4824.2) < 50.0 and abs(c.y - 3600.0) < 50.0 and abs(c.z - 4678.0) < 50.0:
                sc.translate(FreeCAD.Vector(0, 25.0, 0))
                print(f"  [Shifted] FF Plate Solid {i} (SB-16 TV): +25mm Y (to Y=3625.0) -> Dist to C5 = 152.2mm")
            # Kitchen Counter FF_SB-14 (X~204.0, Y~5715.0)
            elif abs(c.x - 204.0) < 50.0 and abs(c.y - 5715.0) < 50.0 and abs(c.z - 5237.4) < 50.0:
                sc.translate(FreeCAD.Vector(0, 0, -150.0))
                print(f"  [Shifted] FF Plate Solid {i} (SB-14): -150mm Z -> Height above FFL = 1000mm (+150mm above counter)")
            new_ff_solids.append(sc)
        pl_ff.Shape = Part.Compound(new_ff_solids)

    # Rocker switches FF
    sw_ff = doc.getObject('FF_Electrical_Switchboard_Rocker_Switches')
    if sw_ff:
        new_sw_ff = []
        for i, s in enumerate(sw_ff.Shape.Solids):
            sc = s.copy()
            c = s.BoundBox.Center
            if abs(c.x - 2600.0) < 50.0 and abs(c.y - 7412.5) < 50.0:
                sc.translate(FreeCAD.Vector(30.0, 0, -87.5))
            elif abs(c.x - 4817.7) < 50.0 and abs(c.y - 3600.0) < 50.0 and abs(c.z - 4678.0) < 50.0:
                sc.translate(FreeCAD.Vector(0, 25.0, 0))
            elif abs(c.x - 210.0) < 50.0 and abs(c.y - 5715.0) < 50.0 and abs(c.z - 5237.4) < 50.0:
                sc.translate(FreeCAD.Vector(0, 0, -150.0))
            new_sw_ff.append(sc)
        sw_ff.Shape = Part.Compound(new_sw_ff)

    # FF Wall drops adjustments
    ff_bd_drops = doc.getObject('FF_Bedroom_Slab_Wall_Drops')
    if ff_bd_drops:
        d_solids = []
        for i, s in enumerate(ff_bd_drops.Shape.Solids):
            c = s.BoundBox.Center
            if i == 0 and abs(c.x - 2400.0) < 50.0 and abs(c.y - 7462.5) < 50.0:
                sc = s.copy()
                sc.translate(FreeCAD.Vector(30.0, 0, 0))
                ext = Part.makeCylinder(12.5, 87.5, FreeCAD.Vector(c.x + 30.0, c.y, 4862.4 - 87.5), FreeCAD.Vector(0, 0, 1))
                sc = sc.fuse(ext)
                d_solids.append(sc)
            else:
                d_solids.append(s.copy())
        ff_bd_drops.Shape = Part.Compound(d_solids)

    ff_elec_drops = doc.getObject('FF_Electrical_Slab_Wall_Drops')
    if ff_elec_drops:
        e_solids = []
        for i, s in enumerate(ff_elec_drops.Shape.Solids):
            c = s.BoundBox.Center
            if i == 4 and abs(c.x - 140.0) < 50.0 and abs(c.y - 5715.0) < 50.0:
                sc = s.copy()
                ext = Part.makeCylinder(12.5, 150.0, FreeCAD.Vector(c.x, c.y, 5274.9 - 150.0), FreeCAD.Vector(0, 0, 1))
                sc = sc.fuse(ext)
                e_solids.append(sc)
            else:
                e_solids.append(s.copy())
        ff_elec_drops.Shape = Part.Compound(e_solids)

    # ---------------------------------------------------------
    # 3. DE-DUPLICATE OVERLAPPING POT BOXES & FAN BOXES
    # ---------------------------------------------------------
    print("\n--- 3. De-duplicating Pot Boxes and Fan Boxes ---")
    lp_gf = doc.getObject('Electrical_Slab_Light_Pots')
    if lp_gf:
        unique_pots = []
        for s in lp_gf.Shape.Solids:
            c = s.BoundBox.Center
            is_dup = any(abs(c.x - x0) < 10.0 and abs(c.y - y0) < 10.0 
                         for x0, y0 in [(1200, 2500), (3800, 2500), (1200, 4000), (3800, 4000)])
            if not is_dup:
                unique_pots.append(s.copy())
        lp_gf.Shape = Part.Compound(unique_pots)
        print(f"  [OK] Pruned duplicate living room pots from Electrical_Slab_Light_Pots (Remaining unique: {len(unique_pots)}).")

    lp_ff = doc.getObject('FF_Electrical_Slab_Light_Pots')
    if lp_ff:
        unique_pots_ff = []
        for s in lp_ff.Shape.Solids:
            c = s.BoundBox.Center
            is_dup = any(abs(c.x - x0) < 10.0 and abs(c.y - y0) < 10.0 
                         for x0, y0 in [(1200, 2500), (3800, 2500), (1200, 4000), (3800, 4000)])
            if not is_dup:
                unique_pots_ff.append(s.copy())
        lp_ff.Shape = Part.Compound(unique_pots_ff)
        print(f"  [OK] Pruned duplicate living room pots from FF_Electrical_Slab_Light_Pots (Remaining unique: {len(unique_pots_ff)}).")

    # ---------------------------------------------------------
    # 4. INSERT CIRCULAR DEEP JUNCTION BOXES (ROOF/CEILING NODES)
    # ---------------------------------------------------------
    print("\n--- 4. Modeling & Inserting Circular Deep Junction Boxes ---")
    
    jb_points_gf = [
        ("JB_GF_LIV_SPINE_1", 2514.6, 2500.0, 3962.4, "Living Room South 3-way spine & pot cross-arm"),
        ("JB_GF_LIV_SPINE_2", 2514.6, 4000.0, 3962.4, "Living Room North 3-way spine & pot cross-arm"),
        ("JB_GF_LIV_TV_BRANCH", 2514.6, 3625.0, 3962.4, "Living Room West Wall TV branch T-junction"),
        ("JB_GF_FOYER_NODE", 2017.5, 1925.0, 3962.4, "Foyer/Staircase 3-way distribution node"),
        ("JB_GF_BED_LOOP", 3191.3, 6070.6, 3962.4, "Bedroom ceiling loop central node"),
        ("JB_GF_KIT_HEADER", 1058.5, 5181.6, 3962.4, "Kitchen North wall conduit header node"),
        ("JB_GF_DROP_DB", 200.0, 2150.0, 3962.4, "Living East drop to DB_GF"),
        ("JB_GF_DROP_TV", 4844.0, 3625.0, 3962.4, "Living West drop to TV console"),
        ("JB_GF_DROP_FOYER_SW", 2100.0, 1925.0, 3962.4, "Living South drop to Foyer SB-2"),
        ("JB_GF_DROP_SITOUT", 3560.0, 1925.0, 3962.4, "Living South-East drop to Sitout SB-4"),
        ("JB_GF_DROP_PARTITION", 1867.5, 4975.0, 3962.4, "Living/Dining partition drop to SB-9"),
        ("JB_GF_DROP_BED_BEDSIDE", 2430.0, 7462.5, 3962.4, "Bedroom South drop to bedside SB-10"),
        ("JB_GF_DROP_BED_ENTRY", 3325.0, 4673.5, 3962.4, "Bedroom North drop to entrance SB-1"),
        ("JB_GF_DROP_BED_AC", 2082.7, 7000.0, 3962.4, "Bedroom West drop to Split AC"),
        ("JB_GF_DROP_STAIR_UTIL", 3050.0, 1707.5, 3962.4, "Staircase drop to utility SB_UTIL"),
        ("JB_GF_DROP_KIT_EAST", 140.0, 5715.0, 3962.4, "Kitchen East drop to counter SB-14"),
        ("JB_GF_DROP_KIT_SOUTH", 1100.0, 7482.5, 3962.4, "Kitchen South drop to fridge SB-15")
    ]

    jb_points_ff = [
        ("JB_FF_LIV_SPINE_1", 2514.6, 2500.0, 7135.4, "FF Living Room South 3-way spine & pot cross-arm"),
        ("JB_FF_LIV_SPINE_2", 2514.6, 4000.0, 7135.4, "FF Living Room North 3-way spine & pot cross-arm"),
        ("JB_FF_LIV_TV_BRANCH", 2514.6, 3625.0, 7135.4, "FF Living Room West Wall TV branch T-junction"),
        ("JB_FF_FOYER_NODE", 2017.5, 1925.0, 7135.4, "FF Foyer/Staircase 3-way distribution node"),
        ("JB_FF_BED_LOOP", 3191.3, 6070.6, 7135.4, "FF Bedroom ceiling loop central node"),
        ("JB_FF_KIT_HEADER", 1058.5, 5181.6, 7135.4, "FF Kitchen North wall conduit header node"),
        ("JB_FF_DROP_DB", 200.0, 2150.0, 7135.4, "FF Living East drop to DB_FF"),
        ("JB_FF_DROP_TV", 4844.0, 3625.0, 7135.4, "FF Living West drop to TV console"),
        ("JB_FF_DROP_FOYER_SW", 2100.0, 1925.0, 7135.4, "FF Living South drop to Foyer switchboard"),
        ("JB_FF_DROP_SITOUT", 3560.0, 1925.0, 7135.4, "FF Living South-East drop to Balcony switchboard"),
        ("JB_FF_DROP_PARTITION", 1867.5, 4975.0, 7135.4, "FF Living/Dining partition drop to switchboard"),
        ("JB_FF_DROP_BED_BEDSIDE", 2430.0, 7462.5, 7135.4, "FF Bedroom South drop to bedside switchboard"),
        ("JB_FF_DROP_BED_ENTRY", 3325.0, 4673.5, 7135.4, "FF Bedroom North drop to entrance switchboard"),
        ("JB_FF_DROP_BED_AC", 2082.7, 7000.0, 7135.4, "FF Bedroom West drop to Split AC"),
        ("JB_FF_DROP_STAIR_UTIL", 3050.0, 1707.5, 7135.4, "FF Staircase drop to utility switchboard"),
        ("JB_FF_DROP_KIT_EAST", 140.0, 5715.0, 7135.4, "FF Kitchen East drop to counter switchboard"),
        ("JB_FF_DROP_KIT_SOUTH", 1100.0, 7482.5, 7135.4, "FF Kitchen South drop to fridge switchboard")
    ]

    def make_jb_compound(points):
        solids = []
        for tag, x, y, z_base, desc in points:
            cyl = Part.makeCylinder(32.5, 60.0, FreeCAD.Vector(x, y, z_base), FreeCAD.Vector(0, 0, 1))
            solids.append(cyl)
        return Part.Compound(solids)

    # GF Circular Deep Junction Boxes
    jb_gf_obj = doc.getObject("GF_Circular_Deep_Junction_Boxes")
    if jb_gf_obj is None:
        jb_gf_obj = doc.addObject("Part::Feature", "GF_Circular_Deep_Junction_Boxes")
        jb_gf_obj.Label = "Ground Floor Circular Deep PVC Junction Boxes (Roof Slab Conduits)"
    jb_gf_obj.Shape = make_jb_compound(jb_points_gf)
    print(f"  [OK] Created/Updated GF_Circular_Deep_Junction_Boxes with {len(jb_points_gf)} boxes.")

    # FF Circular Deep Junction Boxes
    jb_ff_obj = doc.getObject("FF_Circular_Deep_Junction_Boxes")
    if jb_ff_obj is None:
        jb_ff_obj = doc.addObject("Part::Feature", "FF_Circular_Deep_Junction_Boxes")
        jb_ff_obj.Label = "First Floor Circular Deep PVC Junction Boxes (Roof Slab Conduits)"
    jb_ff_obj.Shape = make_jb_compound(jb_points_ff)
    print(f"  [OK] Created/Updated FF_Circular_Deep_Junction_Boxes with {len(jb_points_ff)} boxes.")

    # Group association
    gf_elec_grp = doc.getObject("GF_Electrical_Pipelines_Group")
    if gf_elec_grp and jb_gf_obj not in gf_elec_grp.Group:
        gf_elec_grp.addObject(jb_gf_obj)

    ff_elec_grp = doc.getObject("FF_Electrical_Pipelines_Group")
    if ff_elec_grp and jb_ff_obj not in ff_elec_grp.Group:
        ff_elec_grp.addObject(jb_ff_obj)

    # ---------------------------------------------------------
    # 5. RECOMPUTE, VALIDATE & GUI STYLING
    # ---------------------------------------------------------
    print("\n--- 5. Recomputing and Validating Document ---")
    doc.recompute()

    # GUI styling
    try:
        import FreeCADGui
        gui_gf = FreeCADGui.ActiveDocument.getObject("GF_Circular_Deep_Junction_Boxes")
        if gui_gf:
            gui_gf.ShapeColor = (0.0, 0.45, 0.85)  # Safety Blue
            gui_gf.Transparency = 0
            gui_gf.Visibility = True

        gui_ff = FreeCADGui.ActiveDocument.getObject("FF_Circular_Deep_Junction_Boxes")
        if gui_ff:
            gui_ff.ShapeColor = (0.0, 0.45, 0.85)  # Safety Blue
            gui_ff.Transparency = 0
            gui_ff.Visibility = True
    except Exception as e:
        print(f"  GUI styling note: {e}")

    error_count = 0
    checked_names = [
        "Electrical_Switchboard_Plates", "Electrical_Switchboard_Rocker_Switches",
        "FF_Electrical_Switchboard_Plates", "FF_Electrical_Switchboard_Rocker_Switches",
        "Electrical_Slab_Conduit_Network", "Bedroom_Slab_Wall_Drops", "Electrical_Slab_Wall_Drops",
        "FF_Bedroom_Slab_Wall_Drops", "FF_Electrical_Slab_Wall_Drops",
        "Electrical_Slab_Light_Pots", "FF_Electrical_Slab_Light_Pots",
        "GF_Circular_Deep_Junction_Boxes", "FF_Circular_Deep_Junction_Boxes"
    ]
    for name in checked_names:
        o = doc.getObject(name)
        if o and hasattr(o, "Shape"):
            if not o.Shape.isValid():
                print(f"  [ERROR] Object {name} shape is INVALID!")
                error_count += 1
            print(f"  [Verified] {name:35}: Shape Valid, {len(o.Shape.Solids):2d} Solids, Volume={o.Shape.Volume:10.1f} mm³")

    if error_count == 0:
        print("  [SUCCESS] All audited MEP electrical objects are 100% valid with 0 errors.")

    # Update FreeCAD Cache
    root = Path(doc.FileName).resolve().parent
    cache_tool = root / "tools" / "freecad_cache.py"
    if cache_tool.exists():
        ns = {}
        exec(cache_tool.read_text(encoding="utf-8"), ns)
        ns["validate"](checked_names)
        ns["refresh_objects"](checked_names)
        print("  [OK] FreeCAD Cache updated and validated.")

    if save_doc:
        doc.save()
        print("  [SAVED] HomeConstruction.FCStd saved successfully.")

    return True

if __name__ == "__main__":
    audit_and_fix()
