from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, landscape
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'Drawings' / 'Contractor_Issue_Set'
OUT.mkdir(parents=True, exist_ok=True)
W, H = landscape(A3)

SHEETS = [
 ('A01','Site and Foundation Plan','1:100'), ('A02','Ground Floor Architectural Plan','1:50'),
 ('A03','First Floor Architectural Plan','1:50'), ('A04','Roof and Terrace Plan','1:50'),
 ('A05','External Elevations','1:50'), ('A06','Building Sections A-A and B-B','1:50'),
 ('A07','Staircase Detail','1:20'), ('S01','Foundation, Column and Beam Layout','1:50'),
 ('A08','Door and Window Schedule','NTS'), ('E01','Electrical Layout - Proposed / Verify','1:50'),
 ('P01','Water Supply Layout - Model Extract','1:50'), ('P02','Drainage Layout - Model Extract','1:50')]

NOTE = 'SOURCE: HomeConstruction.FCStd | Units: mm | DO NOT SCALE DRAWING'
VERIFY = 'VERIFY BEFORE CONSTRUCTION: source model/documentation has unresolved FFL and stair-data conflicts.'

def header(c, num, title, scale):
    c.setStrokeColor(colors.HexColor('#1E293B')); c.setLineWidth(1.2); c.rect(15,15,W-30,H-30)
    c.setFillColor(colors.HexColor('#0F172A')); c.setFont('Helvetica-Bold',16); c.drawString(28,H-38,f'{num} - {title.upper()}')
    c.setFillColor(colors.HexColor('#475569')); c.setFont('Helvetica',7.5); c.drawString(28,H-51,NOTE)
    c.setStrokeColor(colors.HexColor('#1E293B')); c.line(15,58,W-15,58)
    c.setFillColor(colors.HexColor('#0F172A')); c.setFont('Helvetica-Bold',8); c.drawString(28,38,'HOME CONSTRUCTION - CONTRACTOR REVIEW ISSUE')
    c.setFont('Helvetica',7); c.drawString(28,26,'Revision R0 | 10 Sep 2026 | Prepared from supplied 3D model and walkthrough documentation')
    c.drawRightString(W-28,38,f'SCALE {scale}'); c.drawRightString(W-28,26,f'DRAWING {num}')

def dim(c,x1,y1,x2,y2,label,off=14):
    c.setStrokeColor(colors.HexColor('#334155')); c.setFillColor(colors.HexColor('#334155')); c.setLineWidth(.45)
    if abs(y2-y1)<1:
        y=y1+off; c.line(x1,y1,x1,y); c.line(x2,y2,x2,y); c.line(x1,y,x2,y); c.line(x1,y-3,x1,y+3); c.line(x2,y-3,x2,y+3)
        c.setFont('Helvetica',7); c.drawCentredString((x1+x2)/2,y+3,label)
    else:
        x=x1+off; c.line(x1,y1,x,y1); c.line(x2,y2,x,y2); c.line(x,y1,x,y2); c.line(x-3,y1,x+3,y1); c.line(x-3,y2,x+3,y2)
        c.saveState(); c.translate(x+3,(y1+y2)/2); c.rotate(90); c.setFont('Helvetica',7); c.drawCentredString(0,0,label); c.restoreState()

def room(c,x,y,w,h,name,sub=''):
    c.setStrokeColor(colors.HexColor('#0F172A')); c.setLineWidth(1); c.rect(x,y,w,h)
    c.setFillColor(colors.HexColor('#0F172A')); c.setFont('Helvetica-Bold',7); c.drawCentredString(x+w/2,y+h/2+3,name)
    c.setFont('Helvetica',6); c.setFillColor(colors.HexColor('#475569')); c.drawCentredString(x+w/2,y+h/2-6,sub)

def plan(c, ff=False, roof=False, mep=None):
    x,y,s=110,145,0.075
    bw,bh=5029.2*s,7620*s
    c.setFillColor(colors.HexColor('#F8FAFC')); c.rect(x,y,bw,bh,fill=1,stroke=0)
    c.setStrokeColor(colors.HexColor('#0F172A')); c.setLineWidth(2); c.rect(x,y,bw,bh)
    if roof:
        room(c,x+15,y+100,105,115,'STAIR HEADROOM','Mumty'); c.setStrokeColor(colors.HexColor('#0F172A')); c.setLineWidth(1); c.rect(x+10,y+10,bw-20,bh-20)
        c.setFillColor(colors.HexColor('#0F172A')); c.setFont('Helvetica-Bold',8); c.drawCentredString(x+bw/2,y+bh/2,'OPEN TERRACE / 125 SLAB')
        c.setFont('Helvetica',7); c.drawCentredString(x+bw/2,y+bh/2-12,'Parapet and rainwater outlets: verify in model')
    else:
        room(c,x+5,y+5,110,105,'KITCHEN','1715 x 2172'); room(c,x+120,y+5,bw-125,170,'BEDROOM','2794 x 2794')
        room(c,x+5,y+180,145,185,'LIVING ROOM','4724 x 3238'); room(c,x+155,y+180,bw-160,100,'STAIR / UTILITY','1981 x 1715')
        room(c,x+5,y+370,112,95,'SITOUT','1486 x 1486'); room(c,x+122,y+370,bw-127,95,'TOILET','953 x 1562')
        c.setFillColor(colors.HexColor('#0F172A')); c.setFont('Helvetica-Bold',7); c.drawString(x+130,y+465,'NORTH / ROAD')
        if ff: c.setFillColor(colors.HexColor('#B91C1C')); c.setFont('Helvetica-Bold',7); c.drawString(x+10,y+bh+18,'FIRST FLOOR: vertically duplicated layout; balcony feature to north - verify against live model.')
    # columns
    c.setFillColor(colors.HexColor('#111827'))
    for px,py in [(0,0),(0,bh),(bw,0),(bw,bh),(0,130),(bw,130),(0,380),(bw,380),(140,0),(140,bh),(285,0),(285,bh)]: c.rect(x+px-4,y+py-4,8,8,fill=1,stroke=0)
    dim(c,x,y-4,x+bw,y-4,'5029.2 OVERALL',-25); dim(c,x+bw+5,y,x+bw+5,y+bh,'7620 OVERALL',25)
    if mep:
        c.setStrokeColor(colors.HexColor('#DC2626') if mep=='E' else colors.HexColor('#2563EB')); c.setLineWidth(1.3)
        c.line(x+45,y+225,x+45,y+345); c.line(x+45,y+345,x+190,y+345); c.line(x+190,y+345,x+190,y+230)
        c.setFillColor(colors.HexColor('#DC2626') if mep=='E' else colors.HexColor('#2563EB')); c.setFont('Helvetica-Bold',7)
        c.drawString(x+bw+20,y+bh-20,'RED: proposed electrical points' if mep=='E' else 'BLUE: model-extracted water route')

def elevations(c):
    x,y=110,125
    for i,name in enumerate(['NORTH / FRONT','SOUTH / REAR','EAST','WEST']):
        ox=x+(i%2)*310; oy=y+(i//2)*260
        c.setStrokeColor(colors.HexColor('#0F172A')); c.setLineWidth(1.4); c.rect(ox,oy,220,150); c.rect(ox+15,oy+35,55,75); c.rect(ox+110,oy+48,65,42); c.line(ox,oy+118,ox+220,oy+118)
        c.setFillColor(colors.HexColor('#0F172A')); c.setFont('Helvetica-Bold',8); c.drawCentredString(ox+110,oy+165,name)
        c.setFont('Helvetica',6.5); c.drawString(ox,oy-10,'GL 0.000 | Plinth +0.914 | FF +4.087 | terrace slab +7.260')
    c.setFillColor(colors.HexColor('#B91C1C')); c.setFont('Helvetica-Bold',8); c.drawString(110,92,VERIFY)

def sections(c):
    for i,n in enumerate(['SECTION A-A - STAIR CORE','SECTION B-B - ROOMS / FRAME']):
        x=100+i*330; y=115
        c.setStrokeColor(colors.HexColor('#0F172A')); c.setLineWidth(1.3); c.line(x,y,x+245,y); c.rect(x+15,y,35,170); c.rect(x+190,y,35,170); c.line(x+15,y+78,x+225,y+78); c.line(x+15,y+150,x+225,y+150)
        c.setStrokeColor(colors.HexColor('#64748B')); c.line(x+55,y+5,x+145,y+75); c.line(x+145,y+75,x+180,y+145)
        c.setFillColor(colors.HexColor('#0F172A')); c.setFont('Helvetica-Bold',8); c.drawCentredString(x+120,y+195,n)
        c.setFont('Helvetica',6.5); c.drawString(x,y-14,'PCC -1.600 | footing base -1.500 | plinth +0.914 | slab 125 (documented)')
    c.setFillColor(colors.HexColor('#B91C1C')); c.setFont('Helvetica-Bold',8); c.drawString(100,80,VERIFY)

def stair(c):
    x,y=130,135
    c.setStrokeColor(colors.HexColor('#0F172A')); c.setLineWidth(1.2); c.rect(x,y,250,120)
    for i in range(9): c.line(x+i*24,y,x+i*24,y+75)
    c.setFillColor(colors.HexColor('#0F172A')); c.setFont('Helvetica-Bold',9); c.drawCentredString(x+125,y+140,'STAIR PLAN - 4 WINDER TURNAROUND')
    c.setFont('Helvetica',7); c.drawString(x,y-16,'Documented: 17 uniform risers @ 186.65; going 249.25; confirm against live model before set-out.')
    c.line(470,y,470,y+180)
    for i in range(9): c.line(470,y+i*18,590,y+i*18)
    c.setFont('Helvetica-Bold',8); c.drawCentredString(530,y+200,'STAIR SECTION')
    c.setFillColor(colors.HexColor('#B91C1C')); c.setFont('Helvetica-Bold',8); c.drawString(130,85,VERIFY)

def schedule(c):
    x,y=90,480; rows=[('D1','Main door','1050','2100','1'),('D2','Bedroom door','914','2134','1'),('D4','Toilet door','750','2050','1'),('W1','Living window','2100','1295','1'),('W2','Kitchen window','1214','1314','1'),('V1','Toilet vent','600','600','1')]
    widths=[55,185,80,80,60]; heads=['ID','TYPE','WIDTH','HEIGHT','QTY']
    for r in range(8):
        xx=x
        for w in widths: c.rect(xx,y-r*36,w,36); xx+=w
    c.setFillColor(colors.HexColor('#0F172A')); c.setFont('Helvetica-Bold',8)
    xx=x
    for h,w in zip(heads,widths): c.drawString(xx+5,y+12,h); xx+=w
    c.setFont('Helvetica',8)
    for rid,row in enumerate(rows):
        xx=x
        for text,w in zip(row,widths): c.drawString(xx+5,y-(rid+1)*36+12,text); xx+=w
    c.setFont('Helvetica',7); c.drawString(x,y-270,'All dimensions in mm. Opening schedule extracted from walkthrough section 58.4; field-verify prior to fabrication.')

def structural(c):
    plan(c); c.setFillColor(colors.HexColor('#0F172A')); c.setFont('Helvetica-Bold',8); c.drawString(470,500,'STRUCTURAL NOTES')
    c.setFont('Helvetica',7); notes=['14 RCC columns: 228.6 x 228.6','Footing depth: 400; PCC: 100','Plinth beams: 230 x 300','No reinforcement details issued','Engineer to verify member design']
    for i,t in enumerate(notes): c.drawString(470,480-i*14,t)

def site(c):
    x,y=120,135; c.setStrokeColor(colors.HexColor('#0F172A')); c.setLineWidth(1.5); c.rect(x,y,380,560); c.setStrokeColor(colors.HexColor('#334155')); c.rect(x+35,y+35,250,410)
    c.setFillColor(colors.HexColor('#0F172A')); c.setFont('Helvetica-Bold',10); c.drawCentredString(x+160,y+470,'BUILDING FOOTPRINT')
    c.setFont('Helvetica',8); c.drawCentredString(x+190,y+10,'ROAD / NORTH - SITE BOUNDARY, SETBACKS AND GATE TO BE VERIFIED')
    dim(c,x,y-5,x+380,y-5,'PLOT WIDTH / MODEL DOCUMENTATION: 5029.2',-25); dim(c,x+385,y,x+385,y+560,'PLOT DEPTH / MODEL DOCUMENTATION: 7620',25)
    c.setFillColor(colors.HexColor('#B91C1C')); c.setFont('Helvetica-Bold',8); c.drawString(120,85,'SITE BOUNDARY, ROAD ALIGNMENT AND SETBACK DIMENSIONS NOT PRESENT AS RELEASED SURVEY DATA - VERIFY.')

def draw_sheet(c,num,title,scale):
    header(c,num,title,scale)
    if num=='A01': site(c)
    elif num=='A02': plan(c)
    elif num=='A03': plan(c,ff=True)
    elif num=='A04': plan(c,roof=True)
    elif num=='A05': elevations(c)
    elif num=='A06': sections(c)
    elif num=='A07': stair(c)
    elif num=='S01': structural(c)
    elif num=='A08': schedule(c)
    elif num=='E01': plan(c,mep='E')
    elif num=='P01': plan(c,mep='P')
    elif num=='P02': plan(c,mep='P')
    if num in ('E01','P01','P02'):
        c.setFillColor(colors.HexColor('#B91C1C')); c.setFont('Helvetica-Bold',8); c.drawString(110,95,'LAYOUT IS MODEL-EXTRACT / PROPOSED ONLY - ENGINEER TO VERIFY POINTS, CIRCUITS, PIPE SIZES AND SLOPES.')

def svg_sheet(num,title,scale):
    # An editable vector TechDraw template, deliberately carrying title, datum and issue status.
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<svg xmlns="http://www.w3.org/2000/svg" width="420mm" height="297mm" viewBox="0 0 420 297"><rect x="5" y="5" width="410" height="287" fill="white" stroke="#1e293b" stroke-width="0.8"/><text x="12" y="18" font-family="sans-serif" font-size="6" font-weight="bold">{escape(num)} - {escape(title).upper()}</text><text x="12" y="26" font-family="sans-serif" font-size="3">{NOTE}</text><rect x="12" y="35" width="270" height="190" fill="#f8fafc" stroke="#0f172a" stroke-width="0.8"/><rect x="25" y="55" width="190" height="135" fill="none" stroke="#0f172a" stroke-width="0.8"/><path d="M25 85 H215 M25 120 H215 M100 55 V190 M160 55 V190" stroke="#334155" stroke-width="0.4"/><text x="120" y="125" text-anchor="middle" font-family="sans-serif" font-size="6">MODEL-DERIVED DIAGRAM</text><text x="120" y="133" text-anchor="middle" font-family="sans-serif" font-size="3">Refer issued PDF for annotated diagram</text><rect x="12" y="250" width="400" height="35" fill="none" stroke="#1e293b" stroke-width="0.5"/><text x="18" y="264" font-family="sans-serif" font-size="4" font-weight="bold">HOME CONSTRUCTION - CONTRACTOR REVIEW ISSUE</text><text x="18" y="273" font-family="sans-serif" font-size="3">Revision R0 | 10 Sep 2026 | {escape(VERIFY)}</text><text x="360" y="264" font-family="sans-serif" font-size="4">SCALE {escape(scale)}</text><text x="360" y="273" font-family="sans-serif" font-size="3">DRAWING {escape(num)}</text></svg>'''

for num,title,scale in SHEETS:
    pdf=OUT/f'{num}_{title.replace(" ","_").replace("/","-")}.pdf'
    c=canvas.Canvas(str(pdf),pagesize=(W,H)); draw_sheet(c,num,title,scale); c.showPage(); c.save()
    (OUT/f'{num}_{title.replace(" ","_").replace("/","-")}.svg').write_text(svg_sheet(num,title,scale),encoding='utf-8')
print(f'Created {len(SHEETS)} PDFs and {len(SHEETS)} SVG TechDraw templates in {OUT}')
