"""
isolate_water_pipeline_network.py

Isolates and renders the clean water supply pipeline network alongside primary
host RCC columns and AAC masonry walls in HomeConstruction.FCStd.
Hides all slabs, beams, foundations, electrical, drainage, fixtures, and furniture.
Sets wall transparency to 65% for clear inspection of pipe routing and wall penetrations.
"""

import os
import FreeCAD as App
import FreeCADGui as Gui

def isolate_water_network(doc=None, view=None, artifact_dir=None):
    if doc is None:
        doc = App.ActiveDocument
    if view is None and Gui.ActiveDocument:
        view = Gui.ActiveDocument.ActiveView

    if not doc:
        print("Error: No active FreeCAD document found.")
        return False

    print(f"Executing Water Pipeline Network Isolation on '{doc.Name}'...")

    # 1. Primary Structural Columns to Show (16 Superstructure Pillars)
    column_names = {
        # Ground Floor Columns
        'Col_SE_Rear_C1', 'Col_S_Spine_C2', 'Col_SW_Rear_C3', 'Col_MidE_C4',
        'Col_MidW_C5', 'Col_NE_Front_C6', 'Col_N_Stair_C7', 'Col_NW_Mumty_C8',
        # First Floor Columns
        'FF_Col_SE_Rear_C1', 'FF_Col_S_Spine_C2', 'FF_Col_SW_Rear_C3', 'FF_Col_MidE_C4',
        'FF_Col_MidW_C5', 'FF_Col_NE_Front_C6', 'FF_Col_N_Stair_C7', 'FF_Col_NW_Mumty_C8',
    }

    # 2. Masonry Envelope & Partition Walls to Show (34 Wall Solids, 65% Transparency)
    wall_names = {
        # Ground Floor Walls
        'Living_Room_Wall_East', 'Living_Room_Wall_West', 'Living_Room_Wall_Main_Door',
        'Bedroom_Wall_East', 'Bedroom_Wall_North', 'Bedroom_Wall_South', 'Bedroom_Wall_West',
        'Kitchen_Wall_East', 'Kitchen_Wall_South', 'Kitchen_Wall_North_Drop',
        'Toilet_Wall_West', 'Toilet_Wall_Front', 'Toilet_Wall_East', 'Toilet_Wall_East_Top', 'Toilet_Wall_North',
        'Wall_Stair_SE_SW', 'Wall_Stair_North', 'Sitout_Compound_Wall_East',
        # First Floor Walls
        'FF_Living_Room_Wall_East', 'FF_Living_Room_Wall_West', 'FF_Living_Room_Wall_Main_Door',
        'FF_Bedroom_Wall_East', 'FF_Bedroom_Wall_North', 'FF_Bedroom_Wall_South', 'FF_Bedroom_Wall_West',
        'FF_Kitchen_Wall_East', 'FF_Kitchen_Wall_South', 'FF_Kitchen_Wall_North_Drop',
        'FF_Toilet_Wall_West', 'FF_Toilet_Wall_Front', 'FF_Toilet_Wall_East', 'FF_Toilet_Wall_East_Top', 'FF_Toilet_Wall_North',
        'FF_Wall_Stair_SE_SW',
    }

    # 3. Clean Water Supply & Plumbing Pipeline Assemblies to Show (34 Components)
    water_pipe_names = {
        # 01 Municipal Water Supply to Sump Network
        'Municipal_Water_Meter',
        'Valve_Municipal_Main_Boundary',
        'Municipal_East_Service_Pipe',
        'GF_Kitchen_Municipal_Riser_Pipe',
        'GF_Kitchen_Sink_Municipal_Tap',
        'Valve_Municipal_Sink_To_Sump',
        'Municipal_Pipe_Sink_To_Sump',
        'Valve_Sump_Inlet_Maintenance',
        'Sump_Brass_Float_Valve',
        # 02 Overhead Water Tank Assembly
        'OHT_RCC_Pedestal_Plinth',
        'OHT_1000L_Water_Tank_Body',
        'OHT_Inspection_Threaded_Lid',
        'OHT_Overflow_Pipe_Terrace_Drop',
        'Valve_OHT_Washout_Drain_Scour',
        'OHT_Anti_Vacuum_Air_Vent_Pipe',
        'Valve_OHT_Master_Gravity_Outlet',
        # 03 Sump Pump Rising Main & Internal False Duct
        'Rising_Main_Understair_Run',
        'Staircase_Vertical_Rising_Main_Pipe',
        'Staircase_Internal_Corner_False_Duct',
        'OHT_Rising_Main_Inlet_Gooseneck',
        # 04 Gravity Down-take Distribution Network
        'Rooftop_Gravity_Distribution_Manifold',
        'Downtake_Toilet_Riser_Shaft',
        'Downtake_Kitchen_Riser_Shaft',
        'Downtake_Utility_Sitout_Branch',
        'FF_Kitchen_Sink_OHT_Domestic_Tap',
        'GF_Utility_Washing_Machine_Bibcock',
        'Terrace_Utility_Bibcock',
        'Terrace_Tap_Supply_Feed',
        # 05 Zonal Isolation Shut-Off Valves
        'Valve_FF_Toilet_Isolate',
        'Valve_GF_Toilet_Isolate',
        'Valve_FF_Kitchen_Isolate',
        'Valve_GF_Kitchen_Isolate',
        'Valve_GF_Utility_Isolate',
        'Valve_Terrace_Tap_Isolate'
    }

    # Pass 1: Hide ALL objects (including groups) to guarantee zero residual geometry
    for obj in doc.Objects:
        vo = obj.ViewObject
        if vo and hasattr(vo, 'Visibility'):
            vo.Visibility = False

    # Pass 2: Show and style Columns (16 Nos)
    shown_cols = 0
    for cname in column_names:
        obj = doc.getObject(cname)
        if obj and obj.ViewObject:
            obj.ViewObject.Visibility = True
            if hasattr(obj.ViewObject, 'ShapeColor') and hasattr(obj, 'Shape') and not obj.Shape.isNull():
                obj.ViewObject.ShapeColor = (0.72, 0.72, 0.76, 1.0)
                obj.ViewObject.Transparency = 10
                shown_cols += 1

    # Pass 3: Show and style Walls (34 Nos, 65% Transparency)
    shown_walls = 0
    for wname in wall_names:
        obj = doc.getObject(wname)
        if obj and obj.ViewObject:
            obj.ViewObject.Visibility = True
            if hasattr(obj.ViewObject, 'ShapeColor') and hasattr(obj, 'Shape') and not obj.Shape.isNull():
                obj.ViewObject.ShapeColor = (0.86, 0.86, 0.88, 1.0)
                obj.ViewObject.Transparency = 65
                if hasattr(obj.ViewObject, 'DisplayMode'):
                    obj.ViewObject.DisplayMode = "Shaded"
                shown_walls += 1

    # Pass 4: Show and style Water Pipelines and Assemblies (34 Nos)
    shown_pipes = 0
    for pname in water_pipe_names:
        obj = doc.getObject(pname)
        if obj and obj.ViewObject:
            obj.ViewObject.Visibility = True
            shown_pipes += 1
            if pname == 'Staircase_Internal_Corner_False_Duct':
                obj.ViewObject.Transparency = 70
                obj.ViewObject.ShapeColor = (0.80, 0.80, 0.85, 1.0)
            elif 'Valve' in pname:
                obj.ViewObject.Transparency = 0
            elif 'OHT' in pname and 'Body' in pname:
                obj.ViewObject.Transparency = 15

    # Clear GUI selection
    Gui.Selection.clearSelection()

    # Reset 3D viewport camera to Isometric and fit all
    if view:
        view.viewIsometric()
        view.fitAll()

    print(f"Isolation complete: {shown_cols} Columns, {shown_walls} Walls (65% trans), {shown_pipes} Water Pipeline Components.")

    if artifact_dir and view:
        os.makedirs(artifact_dir, exist_ok=True)
        view.viewIsometric()
        view.fitAll()
        view.zoomIn()
        img1 = os.path.join(artifact_dir, "water_pipeline_network_isometric.png")
        view.saveImage(img1, 1920, 1080, "Current")

        view.viewAxonometric()
        view.fitAll()
        view.zoomIn()
        img2 = os.path.join(artifact_dir, "water_pipeline_network_se_perspective.png")
        view.saveImage(img2, 1920, 1080, "Current")

        view.viewTop()
        view.fitAll()
        img3 = os.path.join(artifact_dir, "water_pipeline_network_top_plan.png")
        view.saveImage(img3, 1920, 1080, "Current")

        view.viewFront()
        view.fitAll()
        view.zoomIn()
        img4 = os.path.join(artifact_dir, "water_pipeline_network_front_elevation.png")
        view.saveImage(img4, 1920, 1080, "Current")

        view.viewIsometric()
        view.fitAll()
        for _ in range(3):
            view.zoomIn()
        img5 = os.path.join(artifact_dir, "water_pipeline_oht_manifold_closeup.png")
        view.saveImage(img5, 1920, 1080, "Current")

        view.viewIsometric()
        view.fitAll()

    return True

if __name__ == '__main__':
    artifact_path = r"C:\Users\prade\.gemini\antigravity\brain\c832089b-0836-4f58-9392-447986c6c131"
    isolate_water_network(artifact_dir=artifact_path)
