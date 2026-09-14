#!/usr/bin/env python3
\"\"\"
Automated Parametric Remodeling Script for Kitchen/Living Interface & Slab Connections
Executed in FreeCAD via MCP.
\"\"\"
from __future__ import annotations

import sys
from pathlib import Path
import FreeCAD as App
import Part

def remodel_kitchen_living_interface():
    doc = App.ActiveDocument
    if not doc:
        raise RuntimeError("No active FreeCAD document.")

    # 1. Update CCTV_UPS_Power_Backup_Model placement (Shift north by 150 mm to stay within North MEP station)
    ups = doc.getObject("CCTV_UPS_Power_Backup_Model")
    if ups:
        pos = ups.Placement.Base
        bb = ups.Shape.BoundBox
        if bb.YMax > 3047.8:
            ups.Placement.Base = App.Vector(pos.x, pos.y - 150.0, pos.z)

    # 2. Add continuous RCC Lintel Beam below the spandrel drop wall (IS 4326)
    # Spans X in [152.4, 1935.2 mm], Y in [5131.6, 5231.6 mm], Z in [3048.0, 3198.0 mm] (H = 150 mm)
    lintel = doc.getObject("GF_Continuous_Lintel_Kitchen_Living")
    if not lintel:
        lintel = doc.addObject("Part::Box", "GF_Continuous_Lintel_Kitchen_Living")
    lintel.Label = "GF Continuous RCC Lintel Beam - Kitchen Living Interface (IS 4326)"
    lintel.Length = 1782.8
    lintel.Width = 100.0
    lintel.Height = 150.0
    lintel.Placement.Base = App.Vector(152.4, 5131.6, 3048.0)
    if hasattr(lintel, "ViewObject") and lintel.ViewObject:
        lintel.ViewObject.ShapeColor = (0.60, 0.65, 0.70)
        lintel.ViewObject.Visibility = True
    lintel_group = doc.getObject("GF_Lintel_and_Sill_Beams")
    if lintel_group and lintel not in lintel_group.Group:
        lintel_group.addObject(lintel)

    # 3. Position Kitchen_Wall_North_Drop (4" AAC Spandrel Wall) directly ABOVE the lintel beam
    # Spans X in [152.4, 1935.2 mm], Y in [5131.6, 5231.6 mm], Z in [3198.0, 3662.4 mm] (H = 464.4 mm)
    spandrel = doc.getObject("Kitchen_Wall_North_Drop")
    spandrel_box = Part.makeBox(1782.8, 100.0, 464.4, App.Vector(152.4, 5131.6, 3198.0))
    if spandrel:
        spandrel.Shape = spandrel_box
        spandrel.Label = "Kitchen_Living_Spandrel_Drop_Wall"
        if hasattr(spandrel, "ViewObject") and spandrel.ViewObject:
            spandrel.ViewObject.ShapeColor = (0.85, 0.85, 0.85)
            spandrel.ViewObject.Visibility = True
    else:
        spandrel = doc.addObject("Part::Feature", "Kitchen_Wall_North_Drop")
        spandrel.Shape = spandrel_box
        spandrel.Label = "Kitchen_Living_Spandrel_Drop_Wall"
        kg = doc.getObject("Kitchen") or doc.getObject("GF_Kitchen")
        if kg:
            kg.addObject(spandrel)

    # 3. Clean up any temporary passage bridge at Y = 3047.8
    bridge = doc.getObject("Kitchen_Passage_Loft_Bridge")
    if bridge:
        doc.removeObject("Kitchen_Passage_Loft_Bridge")

    # 4. Update Kitchen_Loft_West: attach flush to Kitchen_Living_Spandrel_Drop_Wall at Y = 5231.6 mm & Bedroom_Wall_East at X = 1935.2 mm
    loft_w = doc.getObject("Kitchen_Loft_West")
    if loft_w:
        loft_w.Length = 677.9
        loft_w.Width = 1626.4
        loft_w.Height = 75.0
        loft_w.Placement.Base = App.Vector(1257.3, 5231.6, 3048.0)

    # 5. Update Living_Room_Loft_East: attach flush to Kitchen_Living_Spandrel_Drop_Wall at Y = 5131.6 mm
    loft_lr = doc.getObject("Living_Room_Loft_East")
    if loft_lr:
        loft_lr.Shape = Part.makeBox(600.0, 3188.5, 75.0, App.Vector(152.4, 1943.1, 3048.0))
        if hasattr(loft_lr, "ViewObject") and loft_lr.ViewObject:
            loft_lr.ViewObject.ShapeColor = (0.75, 0.75, 0.75)

    # 6. Update Kitchen_Loft_South: embed flush into Bedroom_Wall_East at X = 1935.2 mm
    loft_s = doc.getObject("Kitchen_Loft_South")
    if loft_s:
        loft_s.Length = 1782.8
        loft_s.Width = 609.6
        loft_s.Height = 75.0
        loft_s.Placement.Base = App.Vector(152.4, 6858.0, 3048.0)

    # 7. Update First Floor counterparts for complete building consistency
    ff_loft_w = doc.getObject("FF_Kitchen_Loft_West")
    if ff_loft_w:
        ff_loft_w.Shape = Part.makeBox(677.9, 1626.4, 75.0, App.Vector(1257.3, 5231.6, 6221.0))

    ff_loft_lr = doc.getObject("FF_Living_Room_Loft_East")
    if ff_loft_lr:
        ff_loft_lr.Shape = Part.makeBox(600.0, 3188.5, 75.0, App.Vector(152.4, 1943.1, 6221.0))

    ff_loft_s = doc.getObject("FF_Kitchen_Loft_South")
    if ff_loft_s:
        ff_loft_s.Shape = Part.makeBox(1782.8, 609.6, 75.0, App.Vector(152.4, 6858.0, 6221.0))

    doc.recompute()
    doc.save()

    # 8. Update FreeCAD model state cache
    try:
        tools_dir = Path(__file__).resolve().parent
        if str(tools_dir) not in sys.path:
            sys.path.insert(0, str(tools_dir))
        import freecad_cache
        freecad_cache.refresh_objects([
            "GF_Continuous_Lintel_Kitchen_Living", "Kitchen_Wall_North_Drop",
            "Kitchen_Loft_West", "Kitchen_Loft_South",
            "Living_Room_Loft_East", "FF_Living_Room_Loft_East",
            "CCTV_UPS_Power_Backup_Model", "FF_Kitchen_Loft_West", "FF_Kitchen_Loft_South"
        ])
    except Exception as exc:
        print(f"Warning: Cache update error: {exc}")

    print("Remodeling of Kitchen/Living interface and slab connections completed successfully.")

if __name__ == "__main__":
    remodel_kitchen_living_interface()
