#!/usr/bin/env python3
"""
Automated Parametric AAC Block Wall Refactoring Script for FreeCAD.
Standardizes all wall solids in HomeConstruction.FCStd to AAC block masonry:
- 8" (200.0 mm) for outer perimeter envelope walls (flush with 8-column boundary faces)
- 4" (100.0 mm) for interior partition walls (preserving all clear room boundaries)
- Recomputes full-depth aperture cutouts for doors/windows
- Re-aligns RCC continuous sill and lintel tie bands
"""
from pathlib import Path
import FreeCAD as App
import Part

def refactor_aac_walls():
    doc = App.ActiveDocument
    if not doc:
        raise RuntimeError("No active FreeCAD document.")

    # 1. Define Wall Specifications
    # Format: (name, (dx, dy, dz, x, y, z), [(cdx, cdy, cdz, cx, cy, cz)])
    wall_specs = [
        # --- Ground Floor Outer Envelope (200 mm) ---
        ("Bedroom_Wall_South", (3048.0, 200.0, 2748.0, 1981.2, 7420.0, 914.4), []),
        ("Kitchen_Wall_South", (1981.2, 200.0, 2748.0, 0.0, 7420.0, 914.4), []),
        ("Bedroom_Wall_West", (200.0, 3048.0, 2748.0, 4829.2, 4572.0, 914.4), []),
        ("Living_Room_Wall_West", (200.0, 2857.5, 2748.0, 4829.2, 1714.5, 914.4), []),
        ("Toilet_Wall_West", (200.0, 1714.5, 2748.0, 4829.2, 0.0, 914.4), []),
        ("Kitchen_Wall_East", (200.0, 2438.4, 2748.0, 0.0, 5181.6, 914.4), [
            (220.0, 914.4, 1219.2, -10.0, 5943.6, 1828.8), # W2 window
            (220.0, 250.0, 250.0, -10.0, 7000.0, 2739.4),   # Exhaust fan
        ]),
        ("Living_Room_Wall_East", (200.0, 3467.1, 2748.0, 0.0, 1714.5, 914.4), [
            (220.0, 1200.0, 1200.0, -10.0, 3510.0, 1848.0), # W1 window (Option 1 - South Bay clear of Col C4)
        ]),
        ("Toilet_Wall_Front", (1219.2, 200.0, 2748.0, 3810.0, 0.0, 914.4), [
            (600.0, 220.0, 600.0, 4050.0, -10.0, 2448.0),   # V1 ventilator
        ]),
        ("Wall_Stair_North", (2095.5, 100.0, 1370.4, 1714.5, 0.0, 914.4), []),
        ("Sitout_Compound_Wall_East", (200.0, 1485.9, 930.0, 0.0, 228.6, 914.4), []),

        # --- Ground Floor Inner Partitions (100 mm) ---
        ("Bedroom_Wall_North", (3048.0, 100.0, 2748.0, 1981.2, 4526.0, 914.4), [
            (914.4, 120.0, 2133.6, 3657.6, 4516.0, 914.4), # D2 bedroom door
        ]),
        ("Bedroom_Wall_East", (100.0, 3048.0, 2748.0, 1935.2, 4526.0, 914.4), []),
        ("Living_Room_Wall_Main_Door", (1514.5, 200.0, 2748.0, 200.0, 1714.5, 914.4), [
            (1050.0, 220.0, 2100.0, 446.55, 1704.5, 914.4), # D1 main entrance door (200mm wall cutout)
        ]),
        ("Wall_Stair_SE_SW", (2057.2, 200.0, 2748.0, 1714.5, 1714.5, 914.4), []),
        ("Toilet_Wall_North", (1057.5, 100.0, 2133.6, 3771.7, 1714.5, 914.4), [
            (750.0, 120.0, 2100.0, 3900.0, 1704.5, 914.4), # D4 toilet door
        ]),
        ("Toilet_Wall_East", (100.0, 1814.5, 2133.6, 3771.7, 0.0, 914.4), []),
        ("Toilet_Wall_East_Top", (100.0, 1814.5, 614.4, 3771.7, 0.0, 3048.0), []),

        # --- First Floor Outer Envelope (200 mm) ---
        ("FF_Bedroom_Wall_South", (3048.0, 200.0, 2748.0, 1981.2, 7420.0, 4087.4), []),
        ("FF_Kitchen_Wall_South", (1981.2, 200.0, 2748.0, 0.0, 7420.0, 4087.4), []),
        ("FF_Bedroom_Wall_West", (200.0, 3048.0, 2748.0, 4829.2, 4572.0, 4087.4), []),
        ("FF_Living_Room_Wall_West", (200.0, 2857.5, 2748.0, 4829.2, 1714.5, 4087.4), []),
        ("FF_Toilet_Wall_West", (200.0, 1714.5, 2748.0, 4829.2, 0.0, 4087.4), []),
        ("FF_Kitchen_Wall_East", (200.0, 2438.4, 2748.0, 0.0, 5181.6, 4087.4), [
            (220.0, 914.4, 1219.2, -10.0, 5943.6, 5001.8), # W2 window
            (220.0, 250.0, 250.0, -10.0, 7000.0, 5912.4),   # Exhaust fan
        ]),
        ("FF_Living_Room_Wall_East", (200.0, 3467.1, 2748.0, 0.0, 1714.5, 4087.4), [
            (220.0, 1200.0, 1200.0, -10.0, 3510.0, 5001.8), # W1 window (Option 1 - South Bay clear of Col C4)
        ]),
        ("FF_Toilet_Wall_Front", (1219.2, 200.0, 2748.0, 3810.0, 0.0, 4087.4), []),

        # --- First Floor Inner Partitions (100 mm) ---
        ("FF_Bedroom_Wall_North", (3048.0, 100.0, 2748.0, 1981.2, 4526.0, 4087.4), [
            (914.4, 120.0, 2133.6, 3657.6, 4516.0, 4087.4), # D2 bedroom door
        ]),
        ("FF_Bedroom_Wall_East", (100.0, 3048.0, 2748.0, 1935.2, 4526.0, 4087.4), []),
        ("FF_Living_Room_Wall_Main_Door", (1514.5, 100.0, 2748.0, 200.0, 1714.5, 4087.4), [
            (1000.0, 120.0, 2100.0, 500.0, 1704.5, 4087.4), # FF Main Door
        ]),
        ("FF_Wall_Stair_SE_SW", (2057.2, 100.0, 2748.0, 1714.5, 1714.5, 4087.4), []),
        ("FF_Toilet_Wall_North", (1057.5, 100.0, 2133.6, 3771.7, 1714.5, 4087.4), [
            (750.0, 120.0, 2100.0, 3900.0, 1704.5, 4087.4), # D4 toilet door
        ]),
        ("FF_Toilet_Wall_East", (100.0, 1814.5, 2133.6, 3771.7, 0.0, 4087.4), []),
        ("FF_Toilet_Wall_East_Top", (100.0, 1814.5, 614.4, 3771.7, 0.0, 6221.0), []),
    ]

    # Prune redundant double walls if still present
    for prune_name in ["Kitchen_Wall_West", "FF_Kitchen_Wall_West"]:
        pobj = doc.getObject(prune_name)
        if pobj:
            doc.removeObject(prune_name)

    modified_names = []

    for name, (dx, dy, dz, x, y, z), cutouts in wall_specs:
        obj = doc.getObject(name)
        if not obj:
            continue
        base_box = Part.makeBox(dx, dy, dz, App.Vector(x, y, z))
        wall_shape = base_box
        for (cdx, cdy, cdz, cx, cy, cz) in cutouts:
            cbox = Part.makeBox(cdx, cdy, cdz, App.Vector(cx, cy, cz))
            wall_shape = wall_shape.cut(cbox)
        obj.Shape = wall_shape
        modified_names.append(name)

    # 2. Update Continuous RCC Lintel & Sill Tie Bands
    band_updates = [
        # GF Bands
        ("GF_Continuous_Lintel_East_Wall", {"Length": 200.0}),
        ("GF_Continuous_Sill_East_Wall", {"Length": 200.0}),
        ("GF_Continuous_Lintel_South_Wall", {"Width": 200.0, "Base": App.Vector(0.0, 7420.0, 3048.0)}),
        ("GF_Continuous_Lintel_West_Wall", {"Length": 200.0, "Base": App.Vector(4829.2, 0.0, 3048.0)}),
        ("GF_Continuous_Lintel_Toilet_Front", {"Width": 200.0, "Base": App.Vector(3810.0, 0.0, 3048.0)}),
        ("GF_Continuous_Sill_Toilet_Front", {"Width": 200.0, "Base": App.Vector(3810.0, 0.0, 2373.0)}),
        ("GF_Continuous_Lintel_Toilet_Door", {"Length": 1057.5, "Width": 100.0, "Base": App.Vector(3771.7, 1714.5, 2964.4)}),
        ("GF_Continuous_Lintel_Bedroom_Wall", {"Width": 100.0, "Base": App.Vector(1981.2, 4526.0, 3048.0)}),
        ("GF_Lintel_Main_Door", {"Length": 1514.5, "Width": 200.0, "Base": App.Vector(200.0, 1614.5, 3014.4)}),
        ("GF_Continuous_Lintel_Stair_South_Wall", {"Length": 2057.2, "Width": 200.0, "Base": App.Vector(1714.5, 1714.5, 3048.0)}),
        ("GF_Continuous_Lintel_Toilet_West_Wall", {"Length": 100.0, "Width": 1814.5, "Base": App.Vector(3771.7, 0.0, 3048.0)}),
        ("GF_Continuous_Lintel_Bedroom_Kitchen_Wall", {"Length": 100.0, "Width": 3048.0, "Base": App.Vector(1935.2, 4526.0, 3048.0)}),
        
        # FF Bands
        ("FF_Continuous_Lintel_East_Wall", {"Length": 200.0}),
        ("FF_Continuous_Sill_East_Wall", {"Length": 200.0}),
        ("FF_Continuous_Lintel_South_Wall", {"Width": 200.0, "Base": App.Vector(0.0, 7420.0, 6201.8)}),
        ("FF_Continuous_Lintel_West_Wall", {"Length": 200.0, "Base": App.Vector(4829.2, 0.0, 6201.8)}),
        ("FF_Continuous_Lintel_Toilet_Front", {"Width": 200.0, "Base": App.Vector(3810.0, 0.0, 6221.0)}),
        ("FF_Continuous_Sill_Toilet_Front", {"Width": 200.0, "Base": App.Vector(3810.0, 0.0, 5546.0)}),
        ("FF_Continuous_Lintel_Toilet_Door", {"Length": 1057.5, "Width": 100.0, "Base": App.Vector(3771.7, 1714.5, 6137.4)}),
        ("FF_Continuous_Lintel_Bedroom_Wall", {"Width": 100.0, "Base": App.Vector(1981.2, 4526.0, 6221.0)}),
        ("FF_Continuous_Lintel_Balcony_Wall", {"Length": 2057.2, "Width": 100.0, "Base": App.Vector(1714.5, 1714.5, 6221.0)}),
        ("FF_Continuous_Lintel_Toilet_West_Wall", {"Length": 100.0, "Width": 1814.5, "Base": App.Vector(3771.7, 0.0, 6221.0)}),
        ("FF_Continuous_Lintel_Bedroom_Kitchen_Wall", {"Length": 100.0, "Width": 3048.0, "Base": App.Vector(1935.2, 4526.0, 6221.0)}),
        ("FF_Lintel_Main_Door", {"Length": 1514.5, "Width": 100.0, "Base": App.Vector(200.0, 1714.5, 6187.4)}),
    ]

    for bname, props in band_updates:
        bobj = doc.getObject(bname)
        if bobj:
            if "Length" in props and hasattr(bobj, "Length"):
                bobj.Length = props["Length"]
            if "Width" in props and hasattr(bobj, "Width"):
                bobj.Width = props["Width"]
            if "Base" in props and hasattr(bobj, "Placement"):
                bobj.Placement.Base = props["Base"]
            modified_names.append(bname)

    doc.recompute()

    # Geometry Validation
    invalid = [m for m in modified_names if doc.getObject(m).Shape.isNull() or not doc.getObject(m).Shape.isValid()]
    if invalid:
        raise RuntimeError(f"Invalid shapes generated: {invalid}")

    # Synchronize Model Cache
    root = Path(doc.FileName).resolve().parent
    cache_ns = {}
    exec((root / "tools" / "freecad_cache.py").read_text(encoding="utf-8"), cache_ns)
    cache_ns["refresh_objects"](modified_names)

    return {"status": "ok", "modified_count": len(modified_names), "invalid_count": len(invalid)}

if __name__ == "__main__":
    res = refactor_aac_walls()
    print(res)
