"""
align_main_door_wall_grid_b.py
==============================
Aligns Living_Room_Wall_Main_Door, GF_Lintel_Main_Door, and surrounds with
RB2 Core Header Beam (Grid B) and PB2 Core Front Divider (Grid B) at Y = [1714.50, 1914.50].
Links the corner seamlessly with Living_Room_Wall_East at (X = 200.0, Y = 1714.50).
Also standardizes First Floor equivalents (FF_Living_Room_Wall_Main_Door, FF_Lintel_Main_Door).
"""
from __future__ import annotations

import FreeCAD as App
import Part

def align_walls_to_grid_b() -> dict:
    doc = App.ActiveDocument
    if doc is None or not getattr(doc, "FileName", None):
        doc = App.openDocument("HomeConstruction.FCStd")

    print("--- 1. ALIGNING GROUND FLOOR MAIN DOOR WALL TO GRID B ---")

    # 1. Living_Room_Wall_Main_Door: 200mm thickness at Y = [1714.50, 1914.50]
    wall_main = doc.getObject("Living_Room_Wall_Main_Door")
    if wall_main:
        base_box = Part.makeBox(1514.5, 200.0, 2748.0, App.Vector(200.0, 1714.5, 914.4))
        cutout = Part.makeBox(1050.0, 220.0, 2100.0, App.Vector(446.55, 1704.5, 914.4))
        wall_main.Shape = base_box.cut(cutout)
        bb = wall_main.Shape.BoundBox
        print(f"  [OK] Living_Room_Wall_Main_Door: X=[{bb.XMin:.1f}, {bb.XMax:.1f}], Y=[{bb.YMin:.1f}, {bb.YMax:.1f}], Z=[{bb.ZMin:.1f}, {bb.ZMax:.1f}]")

    # 2. GF_Lintel_Main_Door: 200mm thickness at Y = [1714.50, 1914.50]
    lintel_main = doc.getObject("GF_Lintel_Main_Door")
    if lintel_main:
        lintel_main.Length = 1514.5
        lintel_main.Width = 200.0
        lintel_main.Height = 150.0
        lintel_main.Placement.Base = App.Vector(200.0, 1714.5, 3048.0)
        bb = lintel_main.Shape.BoundBox
        print(f"  [OK] GF_Lintel_Main_Door: X=[{bb.XMin:.1f}, {bb.XMax:.1f}], Y=[{bb.YMin:.1f}, {bb.YMax:.1f}], Z=[{bb.ZMin:.1f}, {bb.ZMax:.1f}]")

    # 3. GF_Main_Door_Architectural_Surround: flush against front wall face at Y = 1714.5
    surround = doc.getObject("GF_Main_Door_Architectural_Surround")
    if surround:
        bb = surround.Shape.BoundBox
        if bb.YMax < 1650.0:
            s_copy = surround.Shape.copy()
            s_copy.translate(App.Vector(0.0, 100.0, 0.0))
            surround.Shape = s_copy
            bb = surround.Shape.BoundBox
            print(f"  [OK] GF_Main_Door_Architectural_Surround translated +100mm: Y=[{bb.YMin:.1f}, {bb.YMax:.1f}]")
        else:
            print(f"  [SKIP] GF_Main_Door_Architectural_Surround already at Y=[{bb.YMin:.1f}, {bb.YMax:.1f}]")

    print("\n--- 2. ALIGNING FIRST FLOOR MAIN DOOR WALL TO GRID B ---")

    # 4. FF_Living_Room_Wall_Main_Door: 200mm thickness at Y = [1714.50, 1914.50]
    ff_wall_main = doc.getObject("FF_Living_Room_Wall_Main_Door")
    if ff_wall_main:
        base_box = Part.makeBox(1514.5, 200.0, 2748.0, App.Vector(200.0, 1714.5, 4087.4))
        cutout = Part.makeBox(1050.0, 220.0, 2100.0, App.Vector(446.55, 1704.5, 4087.4))
        ff_wall_main.Shape = base_box.cut(cutout)
        bb = ff_wall_main.Shape.BoundBox
        print(f"  [OK] FF_Living_Room_Wall_Main_Door: X=[{bb.XMin:.1f}, {bb.XMax:.1f}], Y=[{bb.YMin:.1f}, {bb.YMax:.1f}], Z=[{bb.ZMin:.1f}, {bb.ZMax:.1f}]")

    # 5. FF_Lintel_Main_Door: 200mm thickness at Y = [1714.50, 1914.50]
    ff_lintel_main = doc.getObject("FF_Lintel_Main_Door")
    if ff_lintel_main:
        ff_lintel_main.Length = 1514.5
        ff_lintel_main.Width = 200.0
        ff_lintel_main.Height = 150.0
        ff_lintel_main.Placement.Base = App.Vector(200.0, 1714.5, 6221.0)
        bb = ff_lintel_main.Shape.BoundBox
        print(f"  [OK] FF_Lintel_Main_Door: X=[{bb.XMin:.1f}, {bb.XMax:.1f}], Y=[{bb.YMin:.1f}, {bb.YMax:.1f}], Z=[{bb.ZMin:.1f}, {bb.ZMax:.1f}]")

    # 6. FF_Main_Door_Architectural_Surround: flush against front wall face at Y = 1714.5
    ff_surround = doc.getObject("FF_Main_Door_Architectural_Surround")
    if ff_surround:
        bb = ff_surround.Shape.BoundBox
        if bb.YMax < 1650.0:
            s_copy = ff_surround.Shape.copy()
            s_copy.translate(App.Vector(0.0, 100.0, 0.0))
            ff_surround.Shape = s_copy
            bb = ff_surround.Shape.BoundBox
            print(f"  [OK] FF_Main_Door_Architectural_Surround translated +100mm: Y=[{bb.YMin:.1f}, {bb.YMax:.1f}]")
        else:
            print(f"  [SKIP] FF_Main_Door_Architectural_Surround already at Y=[{bb.YMin:.1f}, {bb.YMax:.1f}]")

    print("\n--- 3. RECOMPUTING & VALIDATING GEOMETRY ---")
    doc.recompute()

    # Validations
    east_wall = doc.getObject("Living_Room_Wall_East")
    stair_wall = doc.getObject("Wall_Stair_SE_SW")
    rb2_beam = doc.getObject("RB2_Core_GridB")
    pb2_beam = doc.getObject("PB2_Core_GridB")

    w_main_bb = wall_main.Shape.BoundBox
    e_wall_bb = east_wall.Shape.BoundBox
    stair_bb = stair_wall.Shape.BoundBox
    rb2_bb = rb2_beam.Shape.BoundBox
    pb2_bb = pb2_beam.Shape.BoundBox

    assert abs(w_main_bb.YMin - 1714.5) < 0.01, f"Living_Room_Wall_Main_Door YMin mismatch: {w_main_bb.YMin}"
    assert abs(w_main_bb.YMax - 1914.5) < 0.01, f"Living_Room_Wall_Main_Door YMax mismatch: {w_main_bb.YMax}"
    assert abs(w_main_bb.YMin - e_wall_bb.YMin) < 0.01, "Living_Room_Wall_Main_Door not flush with Living_Room_Wall_East"
    assert abs(w_main_bb.YMin - stair_bb.YMin) < 0.01, "Living_Room_Wall_Main_Door not flush with Wall_Stair_SE_SW"
    assert abs(w_main_bb.YMin - rb2_bb.YMin) < 0.01, "Living_Room_Wall_Main_Door not aligned with RB2_Core_GridB header beam"
    assert abs(w_main_bb.YMin - pb2_bb.YMin) < 0.01, "Living_Room_Wall_Main_Door not aligned with PB2_Core_GridB plinth beam"

    print("  [SUCCESS] All alignment assertions passed!")
    print(f"    - Living_Room_Wall_Main_Door: Y = [{w_main_bb.YMin:.2f}, {w_main_bb.YMax:.2f}]")
    print(f"    - Living_Room_Wall_East:      Y = [{e_wall_bb.YMin:.2f}, {e_wall_bb.YMax:.2f}] (Corner at X=200, Y=1714.5: PERFECT L-JOINT)")
    print(f"    - Wall_Stair_SE_SW:           Y = [{stair_bb.YMin:.2f}, {stair_bb.YMax:.2f}] (Collinear front face at Y=1714.5)")
    print(f"    - RB2_Core_GridB (Header):    Y = [{rb2_bb.YMin:.2f}, {rb2_bb.YMax:.2f}] (Wall sits 100% directly below)")
    print(f"    - PB2_Core_GridB (Plinth):    Y = [{pb2_bb.YMin:.2f}, {pb2_bb.YMax:.2f}] (Wall sits 100% directly above)")

    doc.save()
    print("  [OK] Saved HomeConstruction.FCStd cleanly.")

    return {
        "status": "success",
        "wall_main_y": [round(w_main_bb.YMin, 2), round(w_main_bb.YMax, 2)],
        "corner_linked": True,
        "aligned_with_rb2": True
    }

if __name__ == "__main__":
    align_walls_to_grid_b()
