import FreeCAD as App
import TechDraw
from pathlib import Path

ROOT=Path(r'C:\Users\prade\OneDrive\Desktop\home plan')
model=ROOT/'HomeConstruction.FCStd'
out=ROOT/'Drawings'/'Contractor_Issue_Set'
backup=ROOT/'HomeConstruction_before_contractor_issue.FCStd'
if not backup.exists(): backup.write_bytes(model.read_bytes())
doc=App.openDocument(str(model))
for page in [o for o in doc.Objects if o.Name.startswith('Issue_')]: doc.removeObject(page.Name)
for svg in sorted(out.glob('*.svg')):
    num=svg.name.split('_',1)[0]
    page=doc.addObject('TechDraw::DrawPage',f'Issue_{num}')
    page.Label=f'ISSUE {num} - {svg.stem.split("_",1)[1].replace("_"," ")}'
    template=doc.addObject('TechDraw::DrawSVGTemplate',f'Issue_{num}_Template')
    template.Template=str(svg)
    page.Template=template
doc.recompute()
doc.save()
App.closeDocument(doc.Name)
print('Saved native TechDraw issue pages:',len(list(out.glob('*.svg'))))
