"""
show_full_3d_model.py

Restores full visibility of the complete 3D residential building model in HomeConstruction.FCStd.
Restores all architectural elements (walls, slabs, columns, beams, doors, windows,
chajjas, railings, sitout canopy, mumty tower, pergola trellis, OHT) to 100% opacity,
while cleanly hiding FEM analysis meshes, load constraint vectors, and subterranean footing pads.
"""

import FreeCAD as App
import FreeCADGui as Gui

def show_full_model(doc=None, view=None):
    if doc is None:
        doc = App.ActiveDocument
    if view is None and Gui.ActiveDocument:
        view = Gui.ActiveDocument.ActiveView

    if not doc:
        print("Error: No active FreeCAD document found.")
        return False

    print(f"Restoring Full 3D Model Visibility on '{doc.Name}'...")

    # 1. Hide FEM, constraints, simulation, and section cut planes
    for obj in doc.Objects:
        n = obj.Name
        vo = obj.ViewObject
        if not vo or not hasattr(vo, 'Visibility'):
            continue
        
        if (any(k in n.lower() for k in ['constraint', 'fem', 'ccx', 'mesh', 'analysis', 'material', 'dat_file']) or 
            n == 'Section'):
            vo.Visibility = False

        if (any(k in n.lower() for k in ['blinding', 'isolated_footing', 'footing_', 'pedestal', 'septic_tank', 'sump_ug', 'substructure']) or
            n in ['Substructure_Foundation_Group', 'Foundation', 'Septic_Tank', 'Sump_UG_Water_Tank', 'RCC_Structural_Frame_Fused',
                  'Sump_Raft_Foundation_Slab', 'Septic_Raft_Foundation_Slab'] or n.startswith('PCC_')):
            vo.Visibility = False

    # 2. Make all architectural building elements visible & reset opacity
    for obj in doc.Objects:
        n = obj.Name
        vo = obj.ViewObject
        if not vo or not hasattr(vo, 'Visibility'):
            continue
        
        # Skip hidden categories
        if (any(k in n.lower() for k in ['constraint', 'fem', 'ccx', 'mesh', 'analysis', 'material', 'dat_file', 'blinding', 'footing', 'pedestal']) or
            n in ['Section', 'Substructure_Foundation_Group', 'Foundation', 'Septic_Tank', 'Sump_UG_Water_Tank',
                  'RCC_Structural_Frame_Fused', 'Sump_Raft_Foundation_Slab', 'Septic_Raft_Foundation_Slab'] or n.startswith('PCC_')):
            continue
        
        vo.Visibility = True
        
        if hasattr(vo, 'Transparency'):
            if 'glass' in n.lower() or 'glazing' in n.lower():
                vo.Transparency = 55
            elif 'water' in n.lower() and 'tank' not in n.lower():
                vo.Transparency = 40
            else:
                vo.Transparency = 0

    Gui.Selection.clearSelection()

    if view:
        view.viewIsometric()
        view.fitAll()
        view.zoomIn()

    print("Full 3D Model display restored successfully.")
    return True

if __name__ == '__main__':
    show_full_model()
