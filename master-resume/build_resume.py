"""Render the current Markdown master résumé to PDF (requires ReportLab)."""
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parent
source=ROOT/'Jason_Duran_Dutton_Master_Resume.md'
output=ROOT/'Jason_Duran_Dutton_Master_Resume.pdf'
regular=Path('C:/Windows/Fonts/calibri.ttf')
bold=Path('C:/Windows/Fonts/calibrib.ttf')
if regular.exists() and bold.exists():
    pdfmetrics.registerFont(TTFont('Resume',str(regular)))
    pdfmetrics.registerFont(TTFont('Resume-Bold',str(bold)))
    pdfmetrics.registerFontFamily('Resume',normal='Resume',bold='Resume-Bold')
    normal,boldname='Resume','Resume-Bold'
else:
    normal,boldname='Helvetica','Helvetica-Bold'

ink=HexColor('#222d38');accent=HexColor('#183c53');muted=HexColor('#536171')
body=ParagraphStyle('body',fontName=normal,fontSize=9.8,leading=12.5,textColor=ink,spaceAfter=5)
styles={
    1:ParagraphStyle('name',parent=body,fontName=boldname,fontSize=23,leading=28,spaceAfter=7,keepWithNext=True),
    2:ParagraphStyle('section',parent=body,fontName=boldname,fontSize=11.6,leading=14.2,textColor=accent,spaceBefore=9,spaceAfter=5,keepWithNext=True),
    3:ParagraphStyle('role',parent=body,fontName=boldname,fontSize=10.4,leading=13.2,spaceBefore=5,spaceAfter=3,keepWithNext=True)}
bullet=ParagraphStyle('bullet',parent=body,leftIndent=12,firstLineIndent=0,bulletIndent=1,spaceAfter=3)

def clean(s):
    for a,b in [('—','-'),('–','-'),('‑','-'),('’',"'"),('‘',"'"),('“','"'),('”','"')]:s=s.replace(a,b)
    return s

def inline(s):
    s=escape(clean(s))
    s=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<link href="\2" color="#183c53">\1</link>',s)
    return s

story=[];pending=[]
def flush():
    if pending:
        story.append(Paragraph(inline(' '.join(pending)),body))
        pending.clear()

for raw in source.read_text(encoding='utf-8').splitlines():
    line=raw.strip()
    if line.startswith('<!-- Page'):
        flush();story.append(PageBreak())
    elif not line:
        flush()
    elif line.startswith('#'):
        flush();m=re.match(r'^(#{1,3})\s+(.*)$',line)
        if m:story.append(Paragraph(inline(m[2]),styles[len(m[1])]))
    elif line.startswith('- '):
        flush();story.append(Paragraph(inline(line[2:]),bullet,bulletText='•'))
    else:pending.append(line)
flush()

def decorate(c,doc):
    c.saveState()
    if doc.page>1:
        c.setFont(boldname,9);c.setFillColor(accent)
        c.drawString(48,766,'JASON DURAN DUTTON')
        c.setFont(normal,8);c.setFillColor(muted)
        c.drawRightString(564,766,'MASTER RESUME')
    c.setStrokeColor(HexColor('#d9e0e6'));c.setLineWidth(.4);c.line(48,35,564,35)
    c.setFont(normal,8);c.setFillColor(muted)
    c.drawString(48,23,'Education updated October 26, 2026')
    c.drawRightString(564,23,str(doc.page))
    c.restoreState()

doc=SimpleDocTemplate(str(output),pagesize=(612,792),leftMargin=48,rightMargin=48,topMargin=45,bottomMargin=46,
    title='Jason Duran Dutton - Master Resume',author='Jason Duran Dutton',
    subject='Current education, professional experience and independent research')
doc.build(story,onFirstPage=decorate,onLaterPages=decorate)
print(output)
