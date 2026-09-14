import math
import bpy

# ==========================================
# 1. ARCHITECTURAL WAYPOINTS (Z in METERS)
# Plinth FFL = +0.9144m, GF Ceiling = +3.6624m[cite: 3, 11]
# Eye level = FFL + 1.55m
# ==========================================
WAYPOINTS = [
    # Shot 1: Approach from Road to Sitout
    {"pos": (0.8, -1.5, 1.55), "target": (0.8, 1.0, 1.55)},
    # Shot 2: Sitout Porch (X=1.486m, Y=1.486m)[cite: 1, 11]
    {"pos": (0.8, 0.8, 2.46), "target": (2.5, 3.2, 2.46)},
    # Shot 3: Clear-Span Living Hall (Facing South toward Bed/Kitchen)[cite: 1, 11, 13]
    {"pos": (2.5, 2.2, 2.46), "target": (2.5, 5.5, 2.46)},
    {"pos": (2.5, 4.2, 2.46), "target": (3.5, 6.0, 2.46)},
    # Shot 4: Turnaround toward Staircase Core (Near Col C7)[cite: 1, 13]
    {"pos": (1.8, 3.2, 2.46), "target": (1.7, 1.0, 2.46)},
    # Shot 5: Climbing 4-Winder Staircase (Flight 1 to Mid-Landing)[cite: 1, 3]
    {"pos": (1.6, 1.2, 2.80), "target": (2.5, 0.5, 3.20)},
    {"pos": (2.2, 0.5, 3.50), "target": (3.2, 0.8, 4.00)},  # 4-winder turn[cite: 1, 11]
    # Shot 6: Arriving at First Floor Hall (FF FFL = +4.087m -> Eye = 5.637m)[cite: 13, 17]
    {"pos": (2.5, 2.5, 5.64), "target": (2.5, 5.0, 5.64)},
    # Shot 7: First Floor Balcony (Palkani) Looking Out[cite: 1, 19]
    {"pos": (1.0, 0.8, 5.64), "target": (0.8, -2.0, 5.64)},
    # Shot 8: Upper Mumty Core to Terrace Level (Terrace Slab Z = +7.135m)[cite: 13, 17]
    {"pos": (2.0, 0.8, 8.68), "target": (2.5, 4.0, 8.68)},
]

TOTAL_FRAMES = 900  # 30 seconds @ 30 fps


def create_walkthrough():
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = TOTAL_FRAMES
    scene.render.fps = 30

    # 1. Build Bézier Curve Path
    curve_data = bpy.data.curves.new("Tour_Path_Curve", type="CURVE")
    curve_data.dimensions = "3D"
    polyline = curve_data.splines.new("BEZIER")
    polyline.bezier_points.add(len(WAYPOINTS) - 1)

    for i, wp in enumerate(WAYPOINTS):
        bp = polyline.bezier_points[i]
        bp.co = wp["pos"]
        bp.handle_left_type = "AUTO"
        bp.handle_right_type = "AUTO"

    path_obj = bpy.data.objects.new("Tour_Path", curve_data)
    bpy.context.collection.objects.link(path_obj)

    # 2. Camera Setup
    cam_data = bpy.data.cameras.new("Tour_Camera")
    cam_data.lens = 24  # Wide architectural focal length
    cam_data.clip_start = 0.1
    cam_data.clip_end = 100.0

    cam_obj = bpy.data.objects.new("Tour_Camera", cam_data)
    bpy.context.collection.objects.link(cam_obj)
    scene.camera = cam_obj

    # 3. Path Follow Constraint
    follow_constraint = cam_obj.constraints.new(type="FOLLOW_PATH")
    follow_constraint.target = path_obj
    follow_constraint.use_curve_follow = False  # Controlled via aim target

    # Animate curve evaluation along the path
    curve_data.use_path = True
    curve_data.path_duration = TOTAL_FRAMES
    path_obj.data.eval_time = 0.0
    path_obj.data.keyframe_insert(data_path="eval_time", frame=1)
    path_obj.data.eval_time = TOTAL_FRAMES
    path_obj.data.keyframe_insert(data_path="eval_time", frame=TOTAL_FRAMES)

    # Linear easing to maintain constant walk velocity
    if path_obj.data.animation_data and path_obj.data.animation_data.action:
        for fcurve in path_obj.data.animation_data.action.fcurves:
            for kf in fcurve.keyframe_points:
                kf.interpolation = "LINEAR"

    # 4. Animated Look-At Target (Aim Empty)
    aim_empty = bpy.data.objects.new("Camera_Aim_Target", None)
    aim_empty.empty_display_type = "SPHERE"
    aim_empty.empty_display_size = 0.2
    bpy.context.collection.objects.link(aim_empty)

    track_constraint = cam_obj.constraints.new(type="TRACK_TO")
    track_constraint.target = aim_empty
    track_constraint.track_axis = "TRACK_NEGATIVE_Z"
    track_constraint.up_axis = "UP_Y"

    # Keyframe the aim empty along waypoint targets
    step = TOTAL_FRAMES / (len(WAYPOINTS) - 1)
    for i, wp in enumerate(WAYPOINTS):
        frame = int(1 + i * step)
        aim_empty.location = wp["target"]
        aim_empty.keyframe_insert(data_path="location", frame=frame)


if __name__ == "__main__":
    create_walkthrough()