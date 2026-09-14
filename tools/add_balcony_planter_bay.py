"""
Parametric creation and integration of the Balcony Plant Decoration Bay
in front of Balcony Modern Fascia Band (FF_Balcony_Fascia_Band) in HomeConstruction.FCStd.
"""

import sys
from pathlib import Path
import math

try:
    import FreeCAD as App
    import FreeCADGui as Gui
    import Part
    from FreeCAD import Vector
except ImportError:
    pass


def build_balcony_planter_bay(doc=None, save_on_complete=True):
    if doc is None:
        doc = App.ActiveDocument
    if doc is None:
        raise RuntimeError("No active FreeCAD document.")

    print("================================================================================")
    print("BUILDING FIRST FLOOR BALCONY PLANT DECORATION BAY")
    print("================================================================================")

    balcony_grp = doc.getObject("FF_Balcony_Group")
    if not balcony_grp:
        balcony_grp = doc.addObject("App::DocumentObjectGroup", "FF_Balcony_Group")
        balcony_grp.Label = "FF Balcony & Elevation Features"

    # Clean existing planter objects if present
    planter_objs = [
        "FF_Balcony_Planter_Trough",
        "FF_Balcony_Planter_Rim",
        "FF_Balcony_Planter_Soil",
        "FF_Balcony_Planter_Foliage"
    ]
    for name in planter_objs:
        old_obj = doc.getObject(name)
        if old_obj:
            if balcony_grp and old_obj in balcony_grp.Group:
                balcony_grp.removeObject(old_obj)
            doc.removeObject(name)
            print(f"  [CLEAN] Removed existing {name}.")

    # 1. PLANTER TROUGH WITH ARCHITECTURAL REVEAL GROOVES (MYSTIC DREAM)
    outer_box = Part.makeBox(1485.9, 200.0, 320.0, Vector(228.6, -200.0, 4087.4))
    inner_cavity = Part.makeBox(1435.9, 165.0, 295.0, Vector(253.6, -175.0, 4112.4))
    trough_solid = outer_box.cut(inner_cavity)

    # 2 Contemporary horizontal flute reveals on front face (Y = -200 mm)
    reveal_1 = Part.makeBox(1487.9, 8.0, 14.0, Vector(227.6, -201.0, 4180.0))
    reveal_2 = Part.makeBox(1487.9, 8.0, 14.0, Vector(227.6, -201.0, 4280.0))
    trough_solid = trough_solid.cut(reveal_1).cut(reveal_2)

    obj_trough = doc.addObject("Part::Feature", "FF_Balcony_Planter_Trough")
    obj_trough.Label = "Balcony Modern Planter Bay Trough (Mystic Dream)"
    obj_trough.Shape = trough_solid
    balcony_grp.addObject(obj_trough)
    print("  [OK] FF_Balcony_Planter_Trough created (1485.9 x 200.0 x 320.0 mm).")

    # 2. ARCHITECTURAL COPING DRIP RIM (WHITE)
    rim_outer = Part.makeBox(1505.9, 215.0, 25.0, Vector(218.6, -215.0, 4392.4))
    rim_cutout = Part.makeBox(1435.9, 165.0, 30.0, Vector(253.6, -175.0, 4390.0))
    rim_solid = rim_outer.cut(rim_cutout)

    obj_rim = doc.addObject("Part::Feature", "FF_Balcony_Planter_Rim")
    obj_rim.Label = "Balcony Planter Bay Coping Rim (White)"
    obj_rim.Shape = rim_solid
    balcony_grp.addObject(obj_rim)
    print("  [OK] FF_Balcony_Planter_Rim created (1505.9 x 215.0 x 25.0 mm).")

    # 3. SOIL SUBSTRATE BED
    soil_solid = Part.makeBox(1435.9, 165.0, 265.0, Vector(253.6, -175.0, 4112.4))
    obj_soil = doc.addObject("Part::Feature", "FF_Balcony_Planter_Soil")
    obj_soil.Label = "Balcony Planter Soil Substrate"
    obj_soil.Shape = soil_solid
    balcony_grp.addObject(obj_soil)
    print("  [OK] FF_Balcony_Planter_Soil created.")

    # 4. LUSH DECORATIVE PLANT FOLIAGE & CASCADING IVY GREENERY
    foliage_parts = []
    foliage_parts.append(Part.makeBox(1415.9, 155.0, 75.0, Vector(263.6, -170.0, 4377.4)))

    shrub_centers = [
        (305.0, -95.0, 4445.0, 48.0),
        (390.0, -100.0, 4460.0, 54.0),
        (480.0, -92.0, 4450.0, 50.0),
        (575.0, -98.0, 4465.0, 56.0),
        (670.0, -94.0, 4452.0, 52.0),
        (765.0, -100.0, 4470.0, 58.0),
        (860.0, -92.0, 4455.0, 50.0),
        (955.0, -98.0, 4468.0, 56.0),
        (1050.0, -94.0, 4450.0, 52.0),
        (1145.0, -100.0, 4465.0, 55.0),
        (1240.0, -93.0, 4452.0, 50.0),
        (1335.0, -98.0, 4465.0, 56.0),
        (1430.0, -94.0, 4450.0, 52.0),
        (1520.0, -99.0, 4460.0, 54.0),
        (1610.0, -95.0, 4445.0, 48.0),
    ]
    for (cx, cy, cz, cr) in shrub_centers:
        foliage_parts.append(Part.makeSphere(cr, Vector(cx, cy, cz)))
        foliage_parts.append(Part.makeCylinder(cr * 0.72, 40.0, Vector(cx, cy, cz - 15.0)))

    ivy_tendril_specs = [
        (280.0, 32.0, 105.0, 12.0),
        (370.0, 42.0, 180.0, 12.0),
        (460.0, 36.0, 130.0, 12.0),
        (560.0, 46.0, 230.0, 12.0),
        (660.0, 38.0, 150.0, 12.0),
        (760.0, 50.0, 260.0, 12.0),
        (860.0, 40.0, 170.0, 12.0),
        (970.0, 48.0, 240.0, 12.0),
        (1080.0, 36.0, 140.0, 12.0),
        (1190.0, 46.0, 220.0, 12.0),
        (1300.0, 38.0, 135.0, 12.0),
        (1410.0, 44.0, 195.0, 12.0),
        (1510.0, 35.0, 115.0, 12.0),
        (1600.0, 40.0, 165.0, 12.0),
    ]
    for (tx, tw, th, td) in ivy_tendril_specs:
        tendril_box = Part.makeBox(tw, td, th, Vector(tx - tw / 2.0, -215.0 - td, 4392.4 - th))
        foliage_parts.append(tendril_box)
        foliage_parts.append(Part.makeSphere(tw * 0.45, Vector(tx, -215.0 - td / 2.0, 4392.4 - th)))
        if th > 160.0:
            foliage_parts.append(Part.makeSphere(tw * 0.38, Vector(tx + 4.0, -215.0 - td / 2.0, 4392.4 - th * 0.52)))

    plant_compound = Part.makeCompound(foliage_parts)
    obj_foliage = doc.addObject("Part::Feature", "FF_Balcony_Planter_Foliage")
    obj_foliage.Label = "Balcony Decorative Plant Foliage & Cascading Ivy"
    obj_foliage.Shape = plant_compound
    balcony_grp.addObject(obj_foliage)
    print("  [OK] FF_Balcony_Planter_Foliage created with lush canopy and cascading ivy.")

    # 5. ASSIGN PALETTE COLORS
    COLOR_MYSTIC_DREAM = (51 / 255.0, 73 / 255.0, 91 / 255.0, 1.0)
    COLOR_WHITE = (232 / 255.0, 229 / 255.0, 230 / 255.0, 1.0)
    COLOR_SOIL = (60 / 255.0, 45 / 255.0, 30 / 255.0, 1.0)
    COLOR_EMERALD_GREEN = (45 / 255.0, 122 / 255.0, 66 / 255.0, 1.0)

    if hasattr(obj_trough, "ViewObject") and obj_trough.ViewObject:
        obj_trough.ViewObject.ShapeColor = COLOR_MYSTIC_DREAM
    if hasattr(obj_rim, "ViewObject") and obj_rim.ViewObject:
        obj_rim.ViewObject.ShapeColor = COLOR_WHITE
    if hasattr(obj_soil, "ViewObject") and obj_soil.ViewObject:
        obj_soil.ViewObject.ShapeColor = COLOR_SOIL
    if hasattr(obj_foliage, "ViewObject") and obj_foliage.ViewObject:
        obj_foliage.ViewObject.ShapeColor = COLOR_EMERALD_GREEN

    doc.recompute()
    print("  [PASS] doc.recompute() executed successfully.")

    if save_on_complete:
        doc.save()
        print("  [PASS] HomeConstruction.FCStd saved cleanly to disk.")

    print("\n================================================================================")
    print("BALCONY PLANT DECORATION BAY COMPLETED SUCCESSFULLY")
    print("================================================================================")
    return {
        "trough": obj_trough.Name,
        "rim": obj_rim.Name,
        "soil": obj_soil.Name,
        "foliage": obj_foliage.Name
    }


if __name__ == "__main__":
    build_balcony_planter_bay()
