"""
apply_mystic_dream_white_oracle_paint.py
========================================
Applies the three-tone architectural paint palette (Mystic Dream, White, Oracle)
plus natural teak wood and marine SS 304 to all architectural elements of HomeConstruction.FCStd.

Palette:
- White:        RGB(232, 229, 230) -> (0.910, 0.898, 0.902, 1.0)
- Oracle:       RGB(164, 173, 186) -> (0.643, 0.678, 0.729, 1.0)
- Mystic Dream: RGB(51, 73, 91)    -> (0.200, 0.286, 0.357, 1.0)
- Natural Teak: RGB(158, 107, 56)  -> (0.620, 0.420, 0.220, 1.0)
- Marine Steel: RGB(209, 214, 219) -> (0.820, 0.840, 0.860, 1.0)
- Dark Charcoal:RGB(46, 46, 51)    -> (0.180, 0.180, 0.200, 1.0)
"""
from __future__ import annotations

import FreeCAD as App

COLOR_WHITE        = (0.910, 0.898, 0.902, 1.0) # White (#e8e5e6)
COLOR_ORACLE       = (0.643, 0.678, 0.729, 1.0) # Oracle Dove Grey (#a4adba)
COLOR_MYSTIC_DREAM = (0.200, 0.286, 0.357, 1.0) # Mystic Dream Slate Navy (#33495b)
COLOR_TEAK         = (0.620, 0.420, 0.220, 1.0) # Natural Teak Wood
COLOR_STEEL        = (0.820, 0.840, 0.860, 1.0) # Marine Brushed SS 304
COLOR_CHARCOAL     = (0.180, 0.180, 0.200, 1.0) # Dark Charcoal Joinery

def apply_paint_palette() -> dict:
    doc = App.ActiveDocument
    if doc is None or not getattr(doc, "FileName", None):
        doc = App.openDocument("HomeConstruction.FCStd")

    stats = {"white": 0, "oracle": 0, "mystic_dream": 0, "teak": 0, "steel": 0, "charcoal": 0, "skipped": 0}

    def set_color(obj_name: str, color_tuple: tuple, transparency: int = 0) -> bool:
        obj = doc.getObject(obj_name)
        if obj and hasattr(obj, "ViewObject") and obj.ViewObject is not None:
            vo = obj.ViewObject
            if hasattr(vo, "ShapeColor"):
                vo.ShapeColor = color_tuple
            if hasattr(vo, "Transparency") and transparency is not None:
                vo.Transparency = transparency
            return True
        return False

    # -------------------------------------------------------------
    # 1. WHITE (#e8e5e6) - Primary Facade Plaster, Columns, Parapets
    # -------------------------------------------------------------
    white_objects = [
        # Ground Floor Facade & Interior Walls
        "Living_Room_Wall_Main_Door", "Living_Room_Wall_East", "Living_Room_Wall_West",
        "Bedroom_Wall_South", "Bedroom_Wall_West", "Bedroom_Wall_North", "Bedroom_Wall_East",
        "Kitchen_Wall_South", "Kitchen_Wall_East", "Kitchen_Wall_North_Drop",
        "Toilet_Wall_West", "Toilet_Wall_Front", "Toilet_Wall_East", "Toilet_Wall_North", "Toilet_Wall_East_Top",
        "Sitout_Compound_Wall_East",
        # First Floor Facade & Interior Walls
        "FF_Living_Room_Wall_Main_Door", "FF_Living_Room_Wall_East", "FF_Living_Room_Wall_West",
        "FF_Bedroom_Wall_South", "FF_Bedroom_Wall_West", "FF_Bedroom_Wall_North", "FF_Bedroom_Wall_East",
        "FF_Kitchen_Wall_South", "FF_Kitchen_Wall_East", "FF_Kitchen_Wall_North_Drop",
        "FF_Toilet_Wall_West", "FF_Toilet_Wall_Front", "FF_Toilet_Wall_East", "FF_Toilet_Wall_North", "FF_Toilet_Wall_East_Top",
        # Columns (Ground & First Floor)
        "Col_SE_Rear_C1", "Col_S_Spine_C2", "Col_SW_Rear_C3", "Col_MidE_C4", "Col_MidW_C5", "Col_NE_Front_C6", "Col_N_Stair_C7", "Col_NW_Mumty_C8",
        "FF_Col_SE_Rear_C1", "FF_Col_S_Spine_C2", "FF_Col_SW_Rear_C3", "FF_Col_MidE_C4", "FF_Col_MidW_C5", "FF_Col_NE_Front_C6", "FF_Col_N_Stair_C7", "FF_Col_NW_Mumty_C8",
        # Window Sills & Chajjas
        "GF_East_Living_Window_Chajja", "GF_East_Kitchen_Window_Chajja", "GF_Toilet_Ventilator_Chajja",
        "GF_Continuous_Sill_East_Wall", "FF_Continuous_Sill_East_Wall",
        # Copings & Planter Rims
        "Terrace_Parapet_Coping", "Headroom_Roof_Coping", "FF_Balcony_Planter_Rim",
        # Plinth & Entrance Steps
        "Sitout", "Steps_Road_To_Sitout"
    ]
    for name in white_objects:
        if set_color(name, COLOR_WHITE, 0):
            stats["white"] += 1

    # -------------------------------------------------------------
    # 2. ORACLE (#a4adba) - Circulation Core, Staircase & Mumty Tower
    # -------------------------------------------------------------
    oracle_objects = [
        # Staircase Enclosure Walls
        "Wall_Stair_North",
        "Wall_Stair_SE_SW", "FF_Wall_Stair_SE_SW",
        # Headroom / Mumty Tower
        "Headroom_Walls", "Headroom_Roof_Slab",
        "Terrace_Parapet_Wall",
        # Mumty Columns
        "Headroom_Col_NE", "Headroom_Col_NW", "Headroom_Col_SE", "Headroom_Col_SW", "Mumty_Col_C7",
        # Canopy Slabs (Top Surface)
        "GF_Entrance_Canopy_Slab", "FF_Balcony_Canopy_Slab",
        "GF_Stair_North_Canopy_Slab", "FF_Stair_North_Canopy_Slab",
        # Stair Steps & Landings
        "Stair_Flight_1", "Stair_Mid_Landing", "Stair_Flight_2"
    ]
    for name in oracle_objects:
        if set_color(name, COLOR_ORACLE, 0):
            stats["oracle"] += 1

    # -------------------------------------------------------------
    # 3. MYSTIC DREAM (#33495b) - Framing Borders, Fascia Bands, Trellis
    # -------------------------------------------------------------
    mystic_dream_objects = [
        # Architectural Surrounds & Accent Fins
        "GF_Main_Door_Architectural_Surround", "FF_Main_Door_Architectural_Surround",
        "Headroom_Accent_Fins", "FF_Balcony_Vertical_Fin",
        # Tower Grooves & Reveals
        "GF_Tower_Groove_Slats", "GF_Tower_Groove_Reveals",
        "FF_Tower_Groove_Slats", "FF_Tower_Groove_Reveals",
        # Canopy Fascia Bands & Drips
        "GF_Entrance_Canopy_Fascia", "GF_Entrance_Canopy_Drip",
        "FF_Balcony_Canopy_Fascia", "FF_Balcony_Canopy_Drip", "FF_Balcony_Canopy_Curb", "FF_Balcony_Fascia_Band", "FF_Balcony_Planter_Trough",
        "GF_Stair_North_Canopy_Fascia", "GF_Stair_North_Canopy_Drip",
        "FF_Stair_North_Canopy_Fascia", "FF_Stair_North_Canopy_Drip", "FF_Stair_North_Canopy_Curb",
        # Roofline Fascia Bands & Cornices
        "GF_Roofline_Fascia_Band", "GF_Roofline_Drip_Cornice",
        "FF_Roofline_Fascia_Band", "FF_Roofline_Drip_Cornice",
        # Ventilation Louvers
        "GF_Stair_Wall_Louvers",
        # Terrace Pergola Trellis Beams
        "Terrace_Pergola_Trellis_Beams",
        # Overhead Water Tank Support Saddle Beams
        "OHT_Saddle_Beam_North", "OHT_Saddle_Beam_South", "OHT_RCC_Pedestal_Plinth",
        # Continuous Lintel Bands (Exterior Accent Reveal)
        "GF_Lintel_Main_Door", "FF_Lintel_Main_Door"
    ]
    for name in mystic_dream_objects:
        if set_color(name, COLOR_MYSTIC_DREAM, 0):
            stats["mystic_dream"] += 1

    # -------------------------------------------------------------
    # 4. NATURAL TEAK WOOD - Doors & Warm Soffits
    # -------------------------------------------------------------
    teak_objects = [
        "Main_Door", "GF_Main_Door_Frame",
        "FF_Main_Door_Leaves", "FF_Main_Door_Frame",
        "Door_Bedroom_Leaf", "Door_Bedroom_Frame",
        "FF_Door_Bedroom_Leaf", "FF_Door_Bedroom_Frame",
        "Headroom_Door_Leaf", "Headroom_Door_Frame",
        "GF_Canopy_Teak_Soffit", "FF_Balcony_Teak_Soffit"
    ]
    for name in teak_objects:
        if set_color(name, COLOR_TEAK, 0):
            stats["teak"] += 1

    # -------------------------------------------------------------
    # 5. MARINE SS 304 STEEL & GLASS - Balcony & Stair Railings
    # -------------------------------------------------------------
    steel_objects = [
        "FF_Balcony_Railing", "GF_Terrace_Front_Railing",
        "Stair_Railing_Flight_1", "Stair_Railing_Landing", "Stair_Railing_Flight_2",
        "FF_Stair_Railing_Flight_1", "FF_Stair_Railing_Landing", "FF_Stair_Railing_Flight_2",
        "Sitout_Gate_Accent_SS_Slats", "Mumty_External_Maintenance_Ladder"
    ]
    for name in steel_objects:
        if set_color(name, COLOR_STEEL, 0):
            stats["steel"] += 1

    # -------------------------------------------------------------
    # 6. DARK CHARCOAL - Window Frames, Water Tank & Handles
    # -------------------------------------------------------------
    charcoal_objects = [
        "GF_Main_Door_Handle", "FF_Main_Door_Handles", "Door_Bedroom_Handle", "Door_Toilet_Handle",
        "FF_Door_Bedroom_Handle", "FF_Door_Toilet_Handle",
        "Headroom_Window_Frame", "OHT_1000L_Water_Tank_Body", "OHT_Inspection_Threaded_Lid"
    ]
    for name in charcoal_objects:
        if set_color(name, COLOR_CHARCOAL, 0):
            stats["charcoal"] += 1

    # -------------------------------------------------------------
    # 7. BALCONY PLANTER ACCENTS - Organic Foliage & Soil
    # -------------------------------------------------------------
    set_color("FF_Balcony_Planter_Foliage", (45 / 255.0, 122 / 255.0, 66 / 255.0, 1.0), 0)
    set_color("FF_Balcony_Planter_Soil", (60 / 255.0, 45 / 255.0, 30 / 255.0, 1.0), 0)

    print(f"Paint palette application complete:")
    for k, v in stats.items():
        print(f"  - {k.replace('_', ' ').title()}: {v} objects colored")

    doc.recompute()
    doc.save()
    print("  [OK] Saved HomeConstruction.FCStd cleanly.")

    return stats

if __name__ == "__main__":
    apply_paint_palette()
