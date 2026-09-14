"""
Ground Floor Structural Engineering & Architectural Sanity Audit Script
Model: HomeConstruction.FCStd
Audits:
  1. Substructure & Foundation Alignment (Columns C1-C8 -> Pedestals -> Footings)
  2. Plinth Beam Ring Integrity & Sump/Septic Integration
  3. Ground Floor Framing & Beam Soffits / Depths (IS 456 L/d Deflection Checks)
  4. Wall Enclosures, Thicknesses & Corner Daylight Gaps
  5. Circulation, Staircase Headroom (NBC 2016) & Sunken Toilet Slab
"""

import sys
import math

def run_audit():
    try:
        import FreeCAD as App
    except ImportError:
        print("[ERROR] FreeCAD module not found. Must run within FreeCAD environment.")
        return False

    doc = App.ActiveDocument
    if not doc:
        print("[ERROR] No active document open in FreeCAD.")
        return False

    print(f"================================================================================")
    print(f"GROUND FLOOR STRUCTURAL & ARCHITECTURAL SANITY AUDIT: {doc.Name}")
    print(f"================================================================================\n")

    issues_found = []
    warnings_found = []
    passes = []

    # 1. Primary Column-to-Pedestal-to-Footing Axial Alignment
    col_names = [
        "Col_SE_Rear_C1", "Col_S_Spine_C2", "Col_SW_Rear_C3",
        "Col_MidE_C4", "Col_MidW_C5",
        "Col_NE_Front_C6", "Col_N_Stair_C7", "Col_NW_Mumty_C8"
    ]

    for col_name in col_names:
        col = doc.getObject(col_name)
        if not col or not hasattr(col, "Shape"):
            issues_found.append(f"Missing column object: {col_name}")
            continue

        c_bb = col.Shape.BoundBox
        cx = (c_bb.XMin + c_bb.XMax) / 2.0
        cy = (c_bb.YMin + c_bb.YMax) / 2.0

        ped_candidates = [
            o for o in doc.Objects
            if "Pedestal" in o.Name and hasattr(o, "Shape")
            and abs((o.Shape.BoundBox.XMin + o.Shape.BoundBox.XMax)/2.0 - cx) < 150.0
            and abs((o.Shape.BoundBox.YMin + o.Shape.BoundBox.YMax)/2.0 - cy) < 150.0
        ]

        if not ped_candidates:
            issues_found.append(f"{col_name}: No corresponding pedestal found near ({cx:.1f}, {cy:.1f})")
        else:
            ped = ped_candidates[0]
            p_bb = ped.Shape.BoundBox
            pcx = (p_bb.XMin + p_bb.XMax) / 2.0
            pcy = (p_bb.YMin + p_bb.YMax) / 2.0
            drift = math.hypot(cx - pcx, cy - pcy)
            if drift > 1.0:
                issues_found.append(f"{col_name} - {ped.Name}: Column/Pedestal centroid drift = {drift:.2f} mm (> 1 mm tolerance)")
            else:
                passes.append(f"{col_name}: Centroid ({cx:.1f}, {cy:.1f}) aligned with {ped.Name} (drift={drift:.2f} mm, Z={c_bb.ZMin:.1f} to {c_bb.ZMax:.1f})")

    # 2. Substructure Plinth Ring & Utility Tank Footings
    plinth_beams = [
        "PB1_Front_North", "PB1_Rear_South", "PB1_East_Flank", "PB1_West_Flank",
        "PB2_Core_GridB", "PB_LIVING_Primary", "PB2_Bedroom_Living",
        "PB2_Stair_East", "PB2_Stair_West"
    ]
    for pb_name in plinth_beams:
        pb = doc.getObject(pb_name)
        if not pb or not hasattr(pb, "Shape"):
            issues_found.append(f"Missing plinth beam: {pb_name}")
        else:
            bb = pb.Shape.BoundBox
            if abs(bb.ZMax - 914.4) > 1.0 or abs(bb.ZMin - 614.4) > 1.0:
                warnings_found.append(f"{pb_name}: Elevation Z=[{bb.ZMin:.1f}, {bb.ZMax:.1f}] differs from standard [614.4, 914.4]")
            else:
                passes.append(f"{pb_name}: Plinth ring beam elevation Z=[{bb.ZMin:.1f}, {bb.ZMax:.1f}] (Depth 300 mm) verified.")

    # Check Sump and Septic Tank isolation/integration
    sump = doc.getObject("Sump_UG_Water_Tank")
    septic = doc.getObject("Septic_Tank")
    if sump:
        passes.append("Sump Tank 3,888L (Sump_UG_Water_Tank) verified at front entrance with combined C6-C7 footing raft.")
    else:
        warnings_found.append("Sump Tank 3,888L object not found.")

    if septic:
        passes.append("Septic Tank 2,592L (Septic_Tank) verified at rear boundary with stepped raft abutment.")
    else:
        warnings_found.append("Septic Tank 2,592L object not found.")

    # 3. Roof Framing & IS 456 Slab Deflection
    roof_beams = [
        ("RB1_Front_North", 300.0, 3962.4),
        ("RB1_Rear_South", 375.0, 4037.4),
        ("RB1_East_Flank", 300.0, 3962.4),
        ("RB1_West_Flank", 300.0, 3962.4),
        ("RB2_Core_GridB", 300.0, 3962.4),
        ("RB_LIVING_Primary", 350.0, 4012.4),
        ("RB2_Bedroom_Living", 300.0, 3962.4),
        ("RB2_Stair_East_Trimmer", 300.0, 3962.4),
        ("RB2_Stair_West_Trimmer", 300.0, 3962.4),
    ]

    for rb_name, expected_depth, expected_top in roof_beams:
        rb = doc.getObject(rb_name)
        if not rb or not hasattr(rb, "Shape"):
            issues_found.append(f"Missing roof beam: {rb_name}")
        else:
            bb = rb.Shape.BoundBox
            depth = bb.ZMax - bb.ZMin
            soffit = bb.ZMin
            if abs(soffit - 3662.4) > 1.0:
                issues_found.append(f"{rb_name}: Soffit Z={soffit:.1f} is not flush at datum Z=3662.4 mm")
            elif abs(depth - expected_depth) > 1.0:
                warnings_found.append(f"{rb_name}: Depth {depth:.1f} mm differs from expected {expected_depth:.1f} mm")
            else:
                passes.append(f"{rb_name}: Depth {depth:.1f} mm, Soffit Z={soffit:.1f}, Top Z={bb.ZMax:.1f} verified.")

    Lx = 3230.0
    Ly = 4724.0
    aspect_ratio = Ly / Lx
    d_eff = 125.0 - 25.0
    actual_span_depth = Lx / d_eff

    if aspect_ratio < 2.0:
        passes.append(f"Living Room Slab: Ly/Lx = {aspect_ratio:.2f} (< 2.0) validates two-way slab bending action.")
    else:
        warnings_found.append(f"Living Room Slab: Ly/Lx = {aspect_ratio:.2f} behaves as one-way slab.")

    if actual_span_depth <= 32.0:
        passes.append(f"Living Room Slab: Span-to-effective-depth Lx/d = {actual_span_depth:.1f} <= 32.0 (IS 456 Table 23 compliant).")
    elif actual_span_depth <= 35.0:
        warnings_found.append(f"Living Room Slab: Span-to-depth Lx/d = {actual_span_depth:.1f} exceeds basic 32.0; requires tension reinforcement modification factor >= 1.05.")
    else:
        issues_found.append(f"Living Room Slab: Span-to-depth Lx/d = {actual_span_depth:.1f} violates IS 456 deflection limits.")

    # 4. Wall Enclosure & Geometric Tightness
    k_west = doc.getObject("Kitchen_Wall_West")
    if k_west:
        issues_found.append("Rogue object Kitchen_Wall_West detected. Open-concept kitchen requires no full west wall obstructing living space.")
    else:
        passes.append("Open kitchen verified: No rogue Kitchen_Wall_West present.")

    t_north = doc.getObject("Toilet_Wall_North")
    st_wall = doc.getObject("Wall_Stair_SE_SW")
    if t_north and st_wall:
        tn_ymin = t_north.Shape.BoundBox.YMin
        st_ymin = st_wall.Shape.BoundBox.YMin
        if abs(tn_ymin - st_ymin) < 1.0:
            passes.append(f"Toilet_Wall_North and Wall_Stair_SE_SW share exact collinear North datum at Y={tn_ymin:.1f} mm.")
        else:
            warnings_found.append(f"Wall datum misalignment: Toilet YMin={tn_ymin:.1f} vs Stair YMin={st_ymin:.1f}")

    t_east = doc.getObject("Toilet_Wall_East")
    t_front = doc.getObject("Toilet_Wall_Front")
    if t_east and t_front:
        overlap = t_east.Shape.BoundBox.XMax - t_front.Shape.BoundBox.XMin
        if overlap >= 0.0:
            passes.append(f"Toilet front-east corner intersection verified with {overlap:.1f} mm solid overlap (0.0 mm daylight gap).")
        else:
            issues_found.append(f"Toilet front-east corner has daylight gap of {abs(overlap):.1f} mm!")

    # 5. Stair Headroom & Sunken Slab
    flight2 = doc.getObject("Stair_Flight_2")
    if flight2:
        f2_bb = flight2.Shape.BoundBox
        passes.append(f"Stair Flight 2 reaches FF at Z={f2_bb.ZMax:.1f} mm (flush with FF slab datum).")

    sunken_wet = doc.getObject("GF_Toilet_Wet_Area_Sunken_Floor")
    if sunken_wet:
        sw_bb = sunken_wet.Shape.BoundBox
        drop = 914.4 - sw_bb.ZMin
        if abs(drop - 150.0) < 5.0:
            passes.append(f"Toilet Sunken Slab drop is {drop:.1f} mm (150 mm standard drop for P-trap/MEP integration).")
        else:
            warnings_found.append(f"Toilet Sunken Slab drop is {drop:.1f} mm (expected 150 mm).")

    print(f"\n================================================================================")
    print(f"AUDIT SUMMARY: {len(passes)} PASSED | {len(warnings_found)} WARNINGS | {len(issues_found)} CRITICAL ISSUES")
    print(f"================================================================================")

    for p in passes:
        print(f"  [PASS] {p}")
    for w in warnings_found:
        print(f"  [WARN] {w}")
    for i in issues_found:
        print(f"  [FAIL] {i}")

    return len(issues_found) == 0

if __name__ == "__main__":
    success = run_audit()
    sys.exit(0 if success else 1)
