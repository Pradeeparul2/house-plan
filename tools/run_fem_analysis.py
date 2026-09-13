import FreeCAD as App
import Part
import ObjectsFem
import femtools.ccxtools as ccxtools
from femmesh.gmshtools import GmshTools
import feminout.importCcxFrdResults as importCcxFrdResults
from pathlib import Path
import shutil
import math
import csv
import time

def run_analysis():
    t0 = time.time()
    doc = App.ActiveDocument
    if doc is None or not doc.FileName:
        raise RuntimeError("Active document HomeConstruction.FCStd not found or not saved.")
    
    root_dir = Path(doc.FileName).resolve().parent
    out_dir = root_dir / "docs" / "fem_results"
    out_dir.mkdir(parents=True, exist_ok=True)

    fc_bin = Path(App.getHomePath()) / "bin"
    ccx_exe = str((fc_bin / "ccx.exe").resolve()).replace("\\", "/")
    gmsh_exe = str((fc_bin / "gmsh.exe").resolve()).replace("\\", "/")
    App.ParamGet("User parameter:BaseApp/Preferences/Mod/Fem/Ccx").SetString("ccxBinaryPath", ccx_exe)
    App.ParamGet("User parameter:BaseApp/Preferences/Mod/Fem/Gmsh").SetString("gmshBinaryPath", gmsh_exe)

    # 1. Primary RCC Load-Bearing Members (65 items)
    member_names = [
        # Substructure Pedestals (8)
        "Pedestal_C1", "Pedestal_C_SP", "Pedestal_C2", "Pedestal_C13",
        "Pedestal_C4", "Pedestal_C9", "Pedestal_C10", "Pedestal_C12",
        # Plinth Beams (9)
        "PB1_Front_North", "PB1_Rear_South", "PB1_East_Flank", "PB1_West_Flank",
        "PB2_Core_GridB", "PB2_Stair_East", "PB2_Stair_West", "PB2_Bedroom_Living", "PB_LIVING_Primary",
        # GF Columns (8)
        "Col_SE_Rear_C1", "Col_S_Spine_C2", "Col_SW_Rear_C3", "Col_MidE_C4",
        "Col_MidW_C5", "Col_NE_Front_C6", "Col_N_Stair_C7", "Col_NW_Mumty_C8",
        # GF Roof Beams (9)
        "RB1_Front_North", "RB1_Rear_South", "RB1_East_Flank", "RB1_West_Flank",
        "RB2_Core_GridB", "RB2_Stair_East_Trimmer", "RB2_Stair_West_Trimmer", "RB2_Bedroom_Living", "RB_LIVING_Primary",
        # GF Roof / FF Floor Slab (1)
        "Roof_Slab",
        # FF Columns (8)
        "FF_Col_SE_Rear_C1", "FF_Col_S_Spine_C2", "FF_Col_SW_Rear_C3", "FF_Col_MidE_C4",
        "FF_Col_MidW_C5", "FF_Col_NE_Front_C6", "FF_Col_N_Stair_C7", "FF_Col_NW_Mumty_C8",
        # FF Roof Beams (9)
        "FF_RB1_Front_North", "FF_RB1_Rear_South", "FF_RB1_East_Flank", "FF_RB1_West_Flank",
        "FF_RB2_Core_GridB", "FF_RB2_Stair_East_Trimmer", "FF_RB2_Stair_West_Trimmer", "FF_RB2_Bedroom_Living", "FF_RB_LIVING_Primary",
        # Terrace Slab (1)
        "Terrace_Roof_Slab",
        # Rooftop Mumty & OHT Frame (12)
        "Mumty_Col_C7", "Mumty_Col_C8",
        "Headroom_Col_NE", "Headroom_Col_NW", "Headroom_Col_SE", "Headroom_Col_SW",
        "Headroom_RB_Front_North", "Headroom_RB_Rear_South", "Headroom_RB_East_Flank", "Headroom_RB_West_Flank",
        "OHT_Saddle_Beam_North", "OHT_Saddle_Beam_South"
    ]

    shapes = []
    for name in member_names:
        obj = doc.getObject(name)
        if not obj or not hasattr(obj, "Shape") or obj.Shape.isNull():
            raise RuntimeError(f"Required structural member '{name}' not found in document.")
        shapes.append(obj.Shape)

    # Clean up previous analysis objects if existing
    old_fem_objs = [
        "FemAnalysis", "CalculiX_Solver", "MechanicalMaterial",
        "ConstraintFixed_Pedestals", "ConstraintSelfWeight",
        "ConstraintPressure_FF_Slab", "ConstraintPressure_GF_Plinth",
        "ConstraintPressure_Terrace_Slab", "ConstraintForce_OHT",
        "FEMMeshGmsh", "CalculiX_static_results", "CCX_Results",
        "RCC_Structural_Frame_Fused"
    ]
    for n in old_fem_objs:
        if doc.getObject(n):
            doc.removeObject(n)
    doc.recompute()

    # Fuse into single continuous manifold solid
    print("Fusing primary RCC members...")
    fused_shape = shapes[0]
    for s in shapes[1:]:
        fused_shape = fused_shape.fuse(s)

    if not fused_shape.isValid():
        raise RuntimeError("Fused RCC shape is geometrically invalid.")

    fused_obj = doc.addObject("Part::Feature", "RCC_Structural_Frame_Fused")
    fused_obj.Label = "RCC Structural Frame (Fused Solid)"
    fused_obj.Shape = fused_shape
    doc.recompute()

    # Identify boundary and load faces
    fixed_faces = []
    ff_slab_faces = []
    gf_plinth_faces = []
    terrace_faces = []
    oht_faces = []

    for i, f in enumerate(fused_shape.Faces):
        fn = f"Face{i+1}"
        bb = f.BoundBox
        if abs(bb.ZMax - bb.ZMin) < 1e-2:
            z = bb.ZMax
            if abs(z - (-1200.0)) < 1e-1:
                fixed_faces.append(fn)
            elif abs(z - 4087.4) < 1e-1:
                ff_slab_faces.append(fn)
            elif 900.0 <= z <= 1000.0:
                gf_plinth_faces.append(fn)
            elif abs(z - 7260.4) < 1e-1:
                terrace_faces.append(fn)
            elif abs(z - 9490.4) < 1e-1:
                oht_faces.append(fn)

    print(f"Detected: {len(fixed_faces)} pedestal bases, {len(ff_slab_faces)} FF slab face, {len(gf_plinth_faces)} GF plinth faces, {len(terrace_faces)} terrace face, {len(oht_faces)} OHT faces.")
    if len(fixed_faces) != 8:
        raise RuntimeError(f"Expected 8 fixed pedestal base faces at Z=-1200mm, found {len(fixed_faces)}")

    # 2. FEM Analysis Container
    analysis = ObjectsFem.makeAnalysis(doc, "FemAnalysis")
    analysis.Label = "FemAnalysis"

    # 3. CalculiX Solver
    solver = ObjectsFem.makeSolverCalculiXCcxTools(doc, "CalculiX_Solver")
    solver.Label = "CalculiX_Solver"
    analysis.addObject(solver)

    # 4. Material M25 Concrete
    material = ObjectsFem.makeMaterialSolid(doc, "MechanicalMaterial")
    material.Label = "M25_Concrete_IS456"
    mat = material.Material
    mat['Name'] = "Concrete-M25"
    mat['YoungsModulus'] = "25000 MPa"
    mat['PoissonRatio'] = "0.18"
    mat['Density'] = "2500 kg/m^3"
    material.Material = mat
    analysis.addObject(material)

    # 5. Fixed Boundary Conditions at 8 Pedestals
    fixed = ObjectsFem.makeConstraintFixed(doc, "ConstraintFixed_Pedestals")
    fixed.Label = "Fixed_Base_C1_C8_Pedestals"
    fixed.References = [(fused_obj, fixed_faces)]
    analysis.addObject(fixed)

    # 6. Self-weight Load
    gravity = ObjectsFem.makeConstraintSelfWeight(doc, "ConstraintSelfWeight")
    gravity.Label = "IS875_Self_Weight_Gravity"
    gravity.GravityAcceleration = "9.81 m/s^2"
    gravity.GravityDirection = App.Vector(0, 0, -1)
    analysis.addObject(gravity)

    # 7. Live Loads (IS 875 Part 2)
    # First Floor Slab Live Load (2.0 kN/m2)
    press_ff = ObjectsFem.makeConstraintPressure(doc, "ConstraintPressure_FF_Slab")
    press_ff.Label = "Live_Load_FF_Slab_2.0kN_m2"
    press_ff.References = [(fused_obj, ff_slab_faces)]
    press_ff.Pressure = "2.0 kPa"
    analysis.addObject(press_ff)

    # Ground Floor Plinth Tie Live Load (2.0 kN/m2)
    press_gf = ObjectsFem.makeConstraintPressure(doc, "ConstraintPressure_GF_Plinth")
    press_gf.Label = "Live_Load_GF_Plinth_2.0kN_m2"
    press_gf.References = [(fused_obj, gf_plinth_faces)]
    press_gf.Pressure = "2.0 kPa"
    analysis.addObject(press_gf)

    # Terrace Slab Live Load (1.5 kN/m2)
    press_terrace = ObjectsFem.makeConstraintPressure(doc, "ConstraintPressure_Terrace_Slab")
    press_terrace.Label = "Live_Load_Terrace_Slab_1.5kN_m2"
    press_terrace.References = [(fused_obj, terrace_faces)]
    press_terrace.Pressure = "1.5 kPa"
    analysis.addObject(press_terrace)

    # Overhead Water Tank (OHT) Load (11.0 kN downward force)
    force_oht = ObjectsFem.makeConstraintForce(doc, "ConstraintForce_OHT")
    force_oht.Label = "OHT_Gravity_Force_11kN"
    force_oht.References = [(fused_obj, oht_faces)]
    force_oht.Force = "11.0 kN"
    force_oht.DirectionVector = App.Vector(0, 0, -1)
    force_oht.Reversed = True
    analysis.addObject(force_oht)

    # 8. Meshing with Gmsh (3D 10-node quadratic tetrahedrals, element size 150-200mm)
    print("Generating 3D Gmsh tetrahedral mesh...")
    gm = ObjectsFem.makeMeshGmsh(doc, "FEMMeshGmsh")
    gm.Label = "FEMMeshGmsh_C3D10"
    gm.Shape = fused_obj
    gm.CharacteristicLengthMax = 200
    gm.CharacteristicLengthMin = 150
    gm.ElementDimension = "3D"
    gm.ElementOrder = "2nd"
    analysis.addObject(gm)
    doc.recompute()

    gt = GmshTools(gm)
    mesh_err = gt.create_mesh()
    if mesh_err:
        raise RuntimeError(f"Gmsh meshing error: {mesh_err}")

    node_count = gm.FemMesh.NodeCount
    elem_count = gm.FemMesh.VolumeCount
    print(f"Mesh generated: {node_count} nodes, {elem_count} C3D10 solid elements.")

    # 9. Solver Setup & Run
    print("Writing CalculiX input deck and running ccx solver...")
    fea = ccxtools.FemToolsCcx(analysis=analysis, solver=solver)
    fea.update_objects()
    fea.check_prerequisites()
    fea.write_inp_file()

    inp_src = Path(fea.inp_file_name)
    inp_dst = out_dir / "full_structure_g1.inp"
    shutil.copyfile(inp_src, inp_dst)

    import subprocess
    print("Executing CalculiX solver ccx...")
    p = subprocess.run([ccx_exe, "full_structure_g1"], cwd=str(out_dir), capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"CalculiX ccx failed: {p.stderr}")

    frd_dst = out_dir / "full_structure_g1.frd"
    dat_dst = out_dir / "full_structure_g1.dat"
    base_src = inp_src.with_suffix("")
    if frd_dst.exists():
        shutil.copyfile(frd_dst, base_src.with_suffix(".frd"))
    if dat_dst.exists():
        shutil.copyfile(dat_dst, base_src.with_suffix(".dat"))

    fea.load_results()

    # Ensure results object is retained and properly labeled
    res_obj = doc.getObject("CCX_Results")
    if res_obj:
        res_obj.Label = "CalculiX_static_results"

    # 10. Extract Detailed Results from FRD
    frd_data = importCcxFrdResults.read_frd_result(str(frd_dst))
    nodes = frd_data["Nodes"]
    disp_dict = frd_data["Results"][0].get("disp", {})
    stress_dict = frd_data["Results"][0].get("stress", {})
    t10_elems = frd_data["Tetra10Elem"]

    # Calculate von Mises stress for each element
    elem_von_mises = {}
    elem_centroids = {}
    for eid, s in stress_dict.items():
        sxx, syy, szz, sxy, sxz, syz = s
        vm = math.sqrt(0.5 * ((sxx - syy)**2 + (syy - szz)**2 + (szz - sxx)**2 + 6.0 * (sxy**2 + syz**2 + sxz**2)))
        elem_von_mises[eid] = vm
        
        conn = t10_elems.get(eid, [])
        if conn:
            pts = [nodes[nid] for nid in conn if nid in nodes]
            if pts:
                cx = sum(p.x for p in pts) / len(pts)
                cy = sum(p.y for p in pts) / len(pts)
                cz = sum(p.z for p in pts) / len(pts)
                elem_centroids[eid] = (cx, cy, cz)

    # Classify nodes and elements by floor elevation Z
    levels = {
        "Substructure (Foundation Pedestals)": {"z_min": -1200.0, "z_max": 614.4, "disps": [], "stresses": []},
        "Ground Floor (Plinth Beams, Columns C1-C8, Beams)": {"z_min": 614.4, "z_max": 4087.4, "disps": [], "stresses": []},
        "First Floor (FF Slab, FF Columns C1-C8, Roof Beams)": {"z_min": 3962.4, "z_max": 7260.4, "disps": [], "stresses": []},
        "Terrace & Rooftop (Terrace Slab, Mumty, OHT Saddle Beams)": {"z_min": 7135.4, "z_max": 9490.4, "disps": [], "stresses": []}
    }

    for nid, dvec in disp_dict.items():
        if nid in nodes:
            nz = nodes[nid].z
            for lvl_name, lvl in levels.items():
                if lvl["z_min"] <= nz <= lvl["z_max"]:
                    lvl["disps"].append(dvec)

    for eid, vm in elem_von_mises.items():
        if eid in elem_centroids:
            ez = elem_centroids[eid][2]
            for lvl_name, lvl in levels.items():
                if lvl["z_min"] <= ez <= lvl["z_max"]:
                    lvl["stresses"].append(vm)

    # Build CSV Summary
    csv_path = out_dir / "structural_stress_summary.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Floor Level",
            "Z Elevation Range (mm)",
            "Node Count",
            "Element Count",
            "Max Downward Deflection Uz (mm)",
            "Max Resultant Displacement |U| (mm)",
            "Max von Mises Stress (MPa)",
            "Avg von Mises Stress (MPa)",
            "Permissible Stress Limit M25 (MPa)",
            "Structural Integrity Check"
        ])
        for lvl_name, lvl in levels.items():
            uz_vals = [v.z for v in lvl["disps"]]
            u_mags = [math.sqrt(v.x**2 + v.y**2 + v.z**2) for v in lvl["disps"]]
            min_uz = min(uz_vals) if uz_vals else 0.0
            max_u = max(u_mags) if u_mags else 0.0
            stresses = lvl["stresses"]
            max_vm = max(stresses) if stresses else 0.0
            avg_vm = sum(stresses) / len(stresses) if stresses else 0.0
            status = "PASS (Within IS 456 Limits)" if max_vm < 25.0 else "REVIEW"
            writer.writerow([
                lvl_name,
                f"[{lvl['z_min']:.1f}, {lvl['z_max']:.1f}]",
                len(lvl["disps"]),
                len(lvl["stresses"]),
                f"{min_uz:.4f}",
                f"{max_u:.4f}",
                f"{max_vm:.3f}",
                f"{avg_vm:.3f}",
                "25.0 (fck) / 8.5 (sigma_cbc)",
                status
            ])

    all_uz = [v.z for v in disp_dict.values()]
    all_u = [math.sqrt(v.x**2 + v.y**2 + v.z**2) for v in disp_dict.values()]
    all_vm = list(elem_von_mises.values())

    global_min_uz = min(all_uz) if all_uz else 0.0
    global_max_u = max(all_u) if all_u else 0.0
    global_max_vm = max(all_vm) if all_vm else 0.0

    # Group FEM objects cleanly in CAD file tree
    master_grp = doc.getObject("Master_FEM_Analysis_Group")
    if not master_grp:
        master_grp = doc.addObject("App::DocumentObjectGroup", "Master_FEM_Analysis_Group")
        master_grp.Label = "FEM Structural Analysis & Simulation (CalculiX)"

    sub1 = doc.getObject("FEM_Full_Structure_Group")
    if not sub1:
        sub1 = doc.addObject("App::DocumentObjectGroup", "FEM_Full_Structure_Group")
        sub1.Label = "1. Full Structure G+1 FEM Analysis"
    for m in ["FemAnalysis", "RCC_Structural_Frame_Fused"]:
        obj = doc.getObject(m)
        if obj and obj not in sub1.Group:
            sub1.addObject(obj)

    if sub1 not in master_grp.Group:
        master_grp.addObject(sub1)

    doc.recompute()
    doc.save()
    t1 = time.time()

    return {
        "status": "SUCCESS",
        "elapsed_seconds": round(t1 - t0, 2),
        "node_count": node_count,
        "element_count": elem_count,
        "fused_solid_volume_m3": round(fused_shape.Volume / 1e9, 3),
        "global_max_downward_uz_mm": round(global_min_uz, 4),
        "global_max_displacement_mm": round(global_max_u, 4),
        "global_max_von_mises_mpa": round(global_max_vm, 3),
        "inp_path": str(inp_dst),
        "dat_path": str(dat_dst),
        "frd_path": str(frd_dst),
        "csv_path": str(csv_path)
    }

if __name__ == "__main__":
    res = run_analysis()
    print(res)
