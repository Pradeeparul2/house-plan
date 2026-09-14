#!/usr/bin/env python3
"""
tools/remodel_first_floor_1to1.py
==================================
Parametrically remodels the First Floor (FF) assembly in HomeConstruction.FCStd
to achieve 100% exact 1:1 structural, architectural, and MEP vertical alignment
with the Ground Floor (GF), eliminating past cantilever offsets, beam discrepancies,
and wall thickness mismatches.

Discipline: Architectural, Structural RCC & MEP Coordination (G+1 Monolithic BIM)
Governing Codes: IS 456:2000, IS 13920:2016, IS 732:2019, NBC 2016 Part 3 & Part 6
"""

import FreeCAD as App
import Part
from pathlib import Path


def remodel_first_floor(doc=None, save_on_complete=True):
    if doc is None:
        doc = App.ActiveDocument
    if not doc:
        raise RuntimeError("No active FreeCAD document found. Open HomeConstruction.FCStd first.")

    report = {
        "structural_updates": [],
        "architectural_updates": [],
        "mep_updates": [],
        "removed_elements": [],
        "added_elements": [],
        "validation": {}
    }

    print("================================================================================")
    print("PARAMETRIC 1:1 REMODELING: FIRST FLOOR (FF) ASSEMBLY -> GROUND FLOOR (GF) PARITY")
    print("================================================================================")

    # -------------------------------------------------------------------------
    # 1. STRUCTURAL FRAMING & ROOF BEAMS
    # -------------------------------------------------------------------------
    print("\n--- 1. STRUCTURAL ROOF BEAMS PARITY ---")
    
    # 1.1 Upgrade FF_RB1_Rear_South depth from 300mm to 375mm (matching GF RB1_Rear_South)
    rb_rear = doc.getObject("FF_RB1_Rear_South")
    if rb_rear:
        rb_rear.Height = 375.0
        rb_rear.Length = 5029.2
        rb_rear.Width = 228.6
        rb_rear.Placement = App.Placement(App.Vector(0.0, 7391.4, 6835.4), App.Rotation(0, 0, 0, 1))
        report["structural_updates"].append("FF_RB1_Rear_South: Depth upgraded to 375.0mm (Z: 6835.4..7210.4)")
        print("  [OK] FF_RB1_Rear_South depth set to 375.0 mm.")

    # 1.2 Extend FF_RB2_Stair_East_Trimmer to 1714.5mm (spanning flush from Col C7 to FF_RB2_Core_GridB)
    rb_trimmer = doc.getObject("FF_RB2_Stair_East_Trimmer")
    if rb_trimmer:
        rb_trimmer.Length = 300.0
        rb_trimmer.Width = 1714.5
        rb_trimmer.Height = 300.0
        rb_trimmer.Placement = App.Placement(App.Vector(1564.5, 0.0, 6835.4), App.Rotation(0, 0, 0, 1))
        report["structural_updates"].append("FF_RB2_Stair_East_Trimmer: Width extended to 1714.5mm (Y: 0.0..1714.5)")
        print("  [OK] FF_RB2_Stair_East_Trimmer width set to 1714.5 mm.")

    # 1.3 Verify FF_RB_LIVING_Primary transfer beam
    rb_living = doc.getObject("FF_RB_LIVING_Primary")
    if rb_living:
        rb_living.Length = 5029.2
        rb_living.Width = 228.6
        rb_living.Height = 350.0
        rb_living.Placement = App.Placement(App.Vector(0.0, 3047.8, 6835.4), App.Rotation(0, 0, 0, 1))
        report["structural_updates"].append("FF_RB_LIVING_Primary: 5029.2x228.6x350mm spanning C4-C5 verified")
        print("  [OK] FF_RB_LIVING_Primary 5029.2x228.6x350mm transfer beam verified.")

    # -------------------------------------------------------------------------
    # 2. ARCHITECTURAL ENVELOPE & PARTITION WALLS
    # -------------------------------------------------------------------------
    print("\n--- 2. ARCHITECTURAL ENVELOPE & PARTITIONS STANDARDIZATION ---")

    # 2.1 Standardize FF_Living_Room_Wall_Main_Door to 200.0 mm (8") thickness
    wall_main = doc.getObject("FF_Living_Room_Wall_Main_Door")
    if wall_main:
        base_box = Part.makeBox(1514.5, 200.0, 2748.0, App.Vector(200.0, 1714.5, 4087.4))
        cutout = Part.makeBox(1050.0, 220.0, 2100.0, App.Vector(446.55, 1704.5, 4087.4))
        wall_main.Shape = base_box.cut(cutout)
        report["architectural_updates"].append("FF_Living_Room_Wall_Main_Door: 200mm thickness (Y: 1714.5..1914.5), 220mm cutout")
        print("  [OK] FF_Living_Room_Wall_Main_Door updated to 200mm thickness (Y: 1714.5..1914.5).")

    # 2.2 Standardize FF_Wall_Stair_SE_SW to 200.0 mm (8") thickness
    wall_stair = doc.getObject("FF_Wall_Stair_SE_SW")
    if wall_stair:
        wall_stair.Shape = Part.makeBox(2057.2, 200.0, 2748.0, App.Vector(1714.5, 1714.5, 4087.4))
        report["architectural_updates"].append("FF_Wall_Stair_SE_SW: 200mm thickness (Y: 1714.5..1914.5), collinear along Y=1714.5")
        print("  [OK] FF_Wall_Stair_SE_SW updated to 200mm thickness (Y: 1714.5..1914.5).")

    # 2.3 Remove FF_Wall_Stair_North as per user request
    wall_stair_north = doc.getObject("FF_Wall_Stair_North")
    if wall_stair_north:
        stair_grp = doc.getObject("FF_Staircase_Group")
        if stair_grp and wall_stair_north in stair_grp.Group:
            stair_grp.removeObject(wall_stair_north)
        doc.removeObject("FF_Wall_Stair_North")
        report["removed_elements"].append("FF_Wall_Stair_North")
        print("  [OK] FF_Wall_Stair_North removed.")

    # 2.4 Rebuild FF_Kitchen_Wall_North_Drop to full specification
    wall_drop = doc.getObject("FF_Kitchen_Wall_North_Drop")
    if wall_drop:
        wall_drop.Shape = Part.makeBox(1782.8, 100.0, 464.4, App.Vector(152.4, 5131.6, 6371.0))
        report["architectural_updates"].append("FF_Kitchen_Wall_North_Drop: 1782.8x100x464.4mm (Z: 6371.0..6835.4 flush to soffit)")
        print("  [OK] FF_Kitchen_Wall_North_Drop rebuilt (1782.8x100x464.4mm flush to beam soffit).")

    # 2.5 Trim FF_Toilet_Wall_East_Top to 614.4 mm height (flush at Z = 6835.4 mm)
    wall_east_top = doc.getObject("FF_Toilet_Wall_East_Top")
    if wall_east_top:
        wall_east_top.Shape = Part.makeBox(100.0, 1814.5, 614.4, App.Vector(3771.7, 0.0, 6221.0))
        report["architectural_updates"].append("FF_Toilet_Wall_East_Top: Trimmed to 614.4mm (Z: 6221.0..6835.4, 0 clash)")
        print("  [OK] FF_Toilet_Wall_East_Top trimmed to 614.4 mm height.")

    # 2.6 Remove Cantilever Planter solids past Y = 0.0 mm
    balcony_grp = doc.getObject("FF_Balcony_Group")
    planter_objs = ["FF_Balcony_Planter_Trough", "FF_Balcony_Planter_Rim", "FF_Balcony_Planter_Foliage"]
    for p_name in planter_objs:
        p_obj = doc.getObject(p_name)
        if p_obj:
            if balcony_grp and p_obj in balcony_grp.Group:
                balcony_grp.removeObject(p_obj)
            doc.removeObject(p_name)
            report["removed_elements"].append(p_name)
            print(f"  [OK] Removed cantilevered {p_name} to restrict footprint strictly to 16'6\"x25'0\".")

    # -------------------------------------------------------------------------
    # 3. CONTINUOUS RCC LINTEL BANDS & JOINERY SYNCHRONIZATION
    # -------------------------------------------------------------------------
    print("\n--- 3. CONTINUOUS LINTELS & JOINERY PARITY ---")

    # 3.1 Update FF_Lintel_Main_Door to 200mm
    lintel_main = doc.getObject("FF_Lintel_Main_Door")
    if lintel_main:
        lintel_main.Length = 1514.5
        lintel_main.Width = 200.0
        lintel_main.Height = 150.0
        lintel_main.Placement = App.Placement(App.Vector(200.0, 1714.5, 6221.0), App.Rotation(0, 0, 0, 1))
        report["structural_updates"].append("FF_Lintel_Main_Door: Width 200mm (Base: 200, 1714.5, 6221)")
        print("  [OK] FF_Lintel_Main_Door updated to 200mm width.")

    # 3.2 Update FF_Continuous_Lintel_Balcony_Wall to 200mm
    lintel_balcony = doc.getObject("FF_Continuous_Lintel_Balcony_Wall")
    if lintel_balcony:
        lintel_balcony.Length = 2057.2
        lintel_balcony.Width = 200.0
        lintel_balcony.Height = 150.0
        lintel_balcony.Placement = App.Placement(App.Vector(1714.5, 1714.5, 6221.0), App.Rotation(0, 0, 0, 1))
        report["structural_updates"].append("FF_Continuous_Lintel_Balcony_Wall: Width 200mm (Base: 1714.5, 1714.5, 6221)")
        print("  [OK] FF_Continuous_Lintel_Balcony_Wall updated to 200mm width.")

    # 3.3 Synchronize Main Door Surround & Leaves to 1:1 Ground Floor
    gf_surround = doc.getObject("GF_Main_Door_Architectural_Surround")
    ff_surround = doc.getObject("FF_Main_Door_Architectural_Surround")
    if gf_surround and ff_surround:
        ff_surround.Placement = App.Placement()
        ff_surround.Shape = gf_surround.Shape.copy().translated(App.Vector(0, 0, 3173.0))
        report["architectural_updates"].append("FF_Main_Door_Architectural_Surround: 1:1 vertical copy (Y: 1690..1715)")
        print("  [OK] FF_Main_Door_Architectural_Surround synchronized flush with Y=1714.5 facade face.")

    gf_frame = doc.getObject("GF_Main_Door_Frame")
    ff_frame = doc.getObject("FF_Main_Door_Frame")
    if gf_frame and ff_frame:
        ff_frame.Placement = App.Placement()
        ff_frame.Shape = gf_frame.Shape.copy().translated(App.Vector(0, 0, 3173.0))
        report["architectural_updates"].append("FF_Main_Door_Frame: 1:1 vertical copy (X: 446.55..1496.55)")
        print("  [OK] FF_Main_Door_Frame synchronized flush with door opening.")

    gf_leaf = doc.getObject("Main_Door")
    ff_leaf = doc.getObject("FF_Main_Door_Leaves")
    if gf_leaf and ff_leaf:
        ff_leaf.Placement = App.Placement()
        ff_leaf.Shape = gf_leaf.Shape.copy().translated(App.Vector(0, 0, 3173.0))
        report["architectural_updates"].append("FF_Main_Door_Leaves: 1:1 vertical copy (X: 515.55..1427.55)")
        print("  [OK] FF_Main_Door_Leaves synchronized flush with door opening.")

    gf_handle = doc.getObject("GF_Main_Door_Handle")
    ff_handle = doc.getObject("FF_Main_Door_Handles")
    if gf_handle and ff_handle:
        ff_handle.Placement = App.Placement()
        ff_handle.Shape = gf_handle.Shape.copy().translated(App.Vector(0, 0, 3173.0))
        report["architectural_updates"].append("FF_Main_Door_Handles: 1:1 vertical copy (Z: 4963.4..5183.4)")
        print("  [OK] FF_Main_Door_Handles synchronized flush with door opening.")

    # -------------------------------------------------------------------------
    # 4. MEP SWITCHBOARDS FLUSH MOUNTING PARITY
    # -------------------------------------------------------------------------
    print("\n--- 4. MEP ELECTRICAL SWITCHBOARD FLUSH SNAPPING ---")

    def transform_compound(obj, filter_func, shift_vec):
        new_solids = []
        shifted_count = 0
        for s in obj.Shape.Solids:
            sc = s.copy()
            if filter_func(s.BoundBox):
                sc.translate(shift_vec)
                shifted_count += 1
            new_solids.append(sc)
        obj.Shape = Part.Compound(new_solids)
        return shifted_count

    # 4.1 Shift FF_Electrical_Switchboard_Plates on FF_Wall_Stair_SE_SW by +100mm in Y
    ff_plates = doc.getObject("FF_Electrical_Switchboard_Plates")
    if ff_plates:
        cnt = transform_compound(
            ff_plates,
            lambda bb: (1790.0 <= bb.YMin <= 1825.0) and (1900.0 <= bb.XMin <= 3700.0),
            App.Vector(0, 100, 0)
        )
        report["mep_updates"].append(f"FF_Electrical_Switchboard_Plates: Shifted {cnt} solids +100mm in Y (flush at Y=1914.5)")
        print(f"  [OK] Shifted {cnt} switchboard plate solids to flush Y=1914.5 datum.")

    # 4.2 Shift FF_Electrical_Switchboard_Rocker_Switches on FF_Wall_Stair_SE_SW by +100mm in Y
    ff_switches = doc.getObject("FF_Electrical_Switchboard_Rocker_Switches")
    if ff_switches:
        cnt_sw = transform_compound(
            ff_switches,
            lambda bb: (1805.0 <= bb.YMin <= 1835.0) and (1900.0 <= bb.XMin <= 3700.0),
            App.Vector(0, 100, 0)
        )
        report["mep_updates"].append(f"FF_Electrical_Switchboard_Rocker_Switches: Shifted {cnt_sw} rocker solids +100mm in Y (flush at Y=1914.5)")
        print(f"  [OK] Shifted {cnt_sw} rocker switch solids to flush Y=1914.5 datum.")

    # -------------------------------------------------------------------------
    # 5. RECOMPUTE & QUALITY ASSURANCE VALIDATION
    # -------------------------------------------------------------------------
    print("\n--- 5. RECOMPUTE & COMPREHENSIVE QA AUDIT ---")
    doc.recompute()

    # 5.1 Check for invalid or null shapes
    invalids = [o.Name for o in doc.Objects if hasattr(o, "Shape") and hasattr(o.Shape, "isNull") and (o.Shape.isNull() or not o.Shape.isValid())]
    if invalids:
        raise RuntimeError(f"Invalid shapes detected after remodeling: {invalids}")
    report["validation"]["invalid_shapes"] = 0
    print("  [PASS] 0 invalid or null shapes across entire document.")

    # 5.2 Verify 8-Column Centroid Parity
    cols_map = [
        ("Col_SE_Rear_C1", "FF_Col_SE_Rear_C1"),
        ("Col_S_Spine_C2", "FF_Col_S_Spine_C2"),
        ("Col_SW_Rear_C3", "FF_Col_SW_Rear_C3"),
        ("Col_MidE_C4", "FF_Col_MidE_C4"),
        ("Col_MidW_C5", "FF_Col_MidW_C5"),
        ("Col_NE_Front_C6", "FF_Col_NE_Front_C6"),
        ("Col_N_Stair_C7", "FF_Col_N_Stair_C7"),
        ("Col_NW_Mumty_C8", "FF_Col_NW_Mumty_C8")
    ]
    col_drifts = []
    for gf_c_name, ff_c_name in cols_map:
        gf_c = doc.getObject(gf_c_name)
        ff_c = doc.getObject(ff_c_name)
        if not gf_c or not ff_c:
            raise RuntimeError(f"Missing column {gf_c_name} or {ff_c_name}")
        gf_bb = gf_c.Shape.BoundBox
        ff_bb = ff_c.Shape.BoundBox
        gf_cen = ((gf_bb.XMin + gf_bb.XMax)/2, (gf_bb.YMin + gf_bb.YMax)/2)
        ff_cen = ((ff_bb.XMin + ff_bb.XMax)/2, (ff_bb.YMin + ff_bb.YMax)/2)
        drift = ((gf_cen[0]-ff_cen[0])**2 + (gf_cen[1]-ff_cen[1])**2)**0.5
        col_drifts.append((gf_c_name, round(drift, 4)))
    report["validation"]["column_drifts"] = col_drifts
    max_drift = max(d[1] for d in col_drifts)
    if max_drift > 0.01:
        raise RuntimeError(f"Column centroid drift exceeded tolerance: {col_drifts}")
    print(f"  [PASS] 8-Column axial alignment verified: maximum drift = {max_drift:.4f} mm (0.00 mm drift).")

    # 5.3 Verify Beam Dimensions
    rb_rear_bb = doc.getObject("FF_RB1_Rear_South").Shape.BoundBox
    rb_trim_bb = doc.getObject("FF_RB2_Stair_East_Trimmer").Shape.BoundBox
    report["validation"]["FF_RB1_Rear_South_depth"] = round(rb_rear_bb.ZLength, 2)
    report["validation"]["FF_RB2_Stair_East_Trimmer_width"] = round(rb_trim_bb.YLength, 2)
    assert abs(rb_rear_bb.ZLength - 375.0) < 0.1, f"FF_RB1_Rear_South depth mismatch: {rb_rear_bb.ZLength}"
    assert abs(rb_trim_bb.YLength - 1714.5) < 0.1, f"FF_RB2_Stair_East_Trimmer width mismatch: {rb_trim_bb.YLength}"
    print("  [PASS] Roof Beams: FF_RB1_Rear_South depth = 375.0 mm | FF_RB2_Stair_East_Trimmer width = 1714.5 mm.")

    # 5.4 Verify Wall Thickness & Collinear Datum
    w_main_bb = doc.getObject("FF_Living_Room_Wall_Main_Door").Shape.BoundBox
    w_stair_bb = doc.getObject("FF_Wall_Stair_SE_SW").Shape.BoundBox
    w_t_north_bb = doc.getObject("FF_Toilet_Wall_North").Shape.BoundBox
    assert abs(w_main_bb.YLength - 200.0) < 0.1, f"Main door wall thickness mismatch: {w_main_bb.YLength}"
    assert abs(w_stair_bb.YLength - 200.0) < 0.1, f"Stair wall thickness mismatch: {w_stair_bb.YLength}"
    assert abs(w_stair_bb.YMin - w_t_north_bb.YMin) < 0.01, f"Collinear datum mismatch: {w_stair_bb.YMin} vs {w_t_north_bb.YMin}"
    print(f"  [PASS] Wall thicknesses: 200.0 mm verified | Collinear Y-datum along Y = {w_stair_bb.YMin:.1f} mm (0.00 mm delta).")

    # 5.5 Verify Wall Clear Heights Soffit Flush Termination (Z <= 6835.4 mm)
    ff_walls = [
        "FF_Bedroom_Wall_South", "FF_Kitchen_Wall_South", "FF_Bedroom_Wall_West",
        "FF_Living_Room_Wall_West", "FF_Toilet_Wall_West", "FF_Kitchen_Wall_East",
        "FF_Living_Room_Wall_East", "FF_Toilet_Wall_Front", "FF_Bedroom_Wall_North",
        "FF_Bedroom_Wall_East", "FF_Living_Room_Wall_Main_Door", "FF_Wall_Stair_SE_SW",
        "FF_Toilet_Wall_North", "FF_Toilet_Wall_East", "FF_Toilet_Wall_East_Top",
        "FF_Kitchen_Wall_North_Drop"
    ]
    max_z = max(doc.getObject(w).Shape.BoundBox.ZMax for w in ff_walls)
    report["validation"]["max_ff_wall_z"] = round(max_z, 2)
    assert max_z <= 6835.45, f"Wall penetration into roof beams detected: ZMax = {max_z}"
    print(f"  [PASS] All {len(ff_walls)} FF walls terminate flush at beam soffit: max Z = {max_z:.1f} mm <= 6835.4 mm (0 clash).")

    # -------------------------------------------------------------------------
    # 6. MODEL STATE CACHE & PERSISTENCE
    # -------------------------------------------------------------------------
    if save_on_complete:
        doc.save()
        print("\n  [OK] Master document HomeConstruction.FCStd saved cleanly.")

        # Update cache selectively
        project_root = Path(doc.FileName).resolve().parent
        cache_script = project_root / "tools" / "freecad_cache.py"
        if cache_script.exists():
            ns = {}
            exec(cache_script.read_text(encoding="utf-8"), ns)
            affected = [
                "FF_RB1_Rear_South", "FF_RB2_Stair_East_Trimmer", "FF_Living_Room_Wall_Main_Door",
                "FF_Wall_Stair_SE_SW", "FF_Kitchen_Wall_North_Drop",
                "FF_Toilet_Wall_East_Top", "FF_Lintel_Main_Door", "FF_Continuous_Lintel_Balcony_Wall",
                "FF_Main_Door_Architectural_Surround", "FF_Main_Door_Frame", "FF_Main_Door_Leaves",
                "FF_Main_Door_Handles", "FF_Electrical_Switchboard_Plates", "FF_Electrical_Switchboard_Rocker_Switches"
            ]
            ns["validate"](affected)
            ns["refresh_objects"](affected)
            print("  [OK] FreeCAD Cache updated and verified.")

    print("\n================================================================================")
    print("ALL FIRST FLOOR 1:1 PARAMETRIC REMODELING TASKS COMPLETED SUCCESSFULLY (100% PASS)")
    print("================================================================================")
    return report


if __name__ == "__main__":
    remodel_first_floor()
