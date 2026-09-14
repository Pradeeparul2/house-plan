import bpy

# Material Palette Definitions matching references/IMG_0379.JPG
PALETTE = {
    "Mat_Wall_Base": {"color": (0.88, 0.86, 0.82, 1.0), "roughness": 0.85, "metallic": 0.0},
    "Mat_Wall_Charcoal": {"color": (0.12, 0.13, 0.15, 1.0), "roughness": 0.70, "metallic": 0.0},
    "Mat_Teak_Wood": {"color": (0.35, 0.18, 0.08, 1.0), "roughness": 0.40, "metallic": 0.0},
    "Mat_SS_304": {"color": (0.80, 0.80, 0.82, 1.0), "roughness": 0.15, "metallic": 0.95},
    "Mat_Concrete_Structural": {"color": (0.45, 0.45, 0.45, 1.0), "roughness": 0.90, "metallic": 0.0},
    "Mat_Glass": {"color": (0.95, 0.95, 0.95, 1.0), "roughness": 0.05, "transmission": 1.0, "ior": 1.52},
}

def get_or_create_pbr_material(name, props):
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = props["color"]
        bsdf.inputs["Roughness"].default_value = props.get("roughness", 0.5)
        bsdf.inputs["Metallic"].default_value = props.get("metallic", 0.0)
        if "transmission" in props:
            # Blender 4.x / EEVEE Next compatibility
            socket = bsdf.inputs.get("Transmission Weight") or bsdf.inputs.get("Transmission")
            if socket:
                socket.default_value = props["transmission"]
            if "IOR" in bsdf.inputs:
                bsdf.inputs["IOR"].default_value = props.get("ior", 1.45)
    return mat

def apply_materials():
    materials = {k: get_or_create_pbr_material(k, v) for k, v in PALETTE.items()}
    
    # Keyword-to-material bindings matching FreeCAD object naming
    mapping_rules = [
        (["Railing", "Balustrade", "SS_304"], "Mat_SS_304"),
        (["Door_Main", "Teak", "Wood", "Joinery"], "Mat_Teak_Wood"),
        (["Charcoal", "Accent", "Parapet_Band", "Chajja"], "Mat_Wall_Charcoal"),
        (["Column", "Beam", "Footing", "Slab", "Plinth"], "Mat_Concrete_Structural"),
        (["Glass", "Window_Glazing"], "Mat_Glass"),
        (["Wall", "Partition", "Plaster"], "Mat_Wall_Base"),
    ]
    
    for obj in bpy.context.scene.objects:
        if obj.type != "MESH":
            continue
        assigned = False
        for keywords, mat_key in mapping_rules:
            if any(kw.lower() in obj.name.lower() for kw in keywords):
                obj.data.materials.clear()
                obj.data.materials.append(materials[mat_key])
                assigned = True
                break
        if not assigned:
            obj.data.materials.clear()
            obj.data.materials.append(materials["Mat_Wall_Base"])

if __name__ == "__main__":
    apply_materials()