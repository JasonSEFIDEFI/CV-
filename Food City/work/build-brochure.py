from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor,white
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
import pypdfium2 as pdfium
ROOT=Path.cwd();OUT=ROOT/'outputs';ASSET=OUT/'community-connect/assets'
NAVY=HexColor('#123269');RED=HexColor('#C92032');GRAY=HexColor('#52617B')
c=canvas.Canvas(str(OUT/'Food-City-Community-Connect-Brochure.pdf'),pagesize=(612,792))
c.setTitle('Food City Community Connect | Independent proposal brochure')
c.setAuthor('Independent proposal')
def para(txt,x,y,w,size=13,color=NAVY,bold=False):
 style=ParagraphStyle('body',fontName='Helvetica-Bold' if bold else 'Helvetica',fontSize=size,leading=size*1.35,textColor=color)
 p=Paragraph(txt,style);_,h=p.wrap(w,700);p.drawOn(c,x,y-h);return y-h
def photo(name,x,y,w,h):
 im=ImageReader(str(ASSET/name));iw,ih=im.getSize();scale=max(w/iw,h/ih);dw,dh=iw*scale,ih*scale
 c.saveState();p=c.beginPath();p.rect(x,y,w,h);c.clipPath(p,stroke=0,fill=0);c.drawImage(im,x+(w-dw)/2,y+h-dh,dw,dh);c.restoreState()
def footer(page):
 c.setFillColor(RED);c.rect(0,0,612,12,fill=1,stroke=0)
 para(f'Independent, unofficial proposal. No Food City affiliation or system integration.  {page}',36,37,540,8,GRAY)
def header(label):
 c.setFillColor(NAVY);c.rect(0,744,612,48,fill=1,stroke=0);para(label,36,775,540,12,white,True)
header('A COMMUNITY DELIVERY CONCEPT')
para('Food City<br/>Community Connect',36,715,540,34,NAVY,True)
para('Groceries delivered.<br/>More neighbors connected.',36,606,540,21,RED,True)
photo('porch.png',0,228,612,302)
para('AI-generated illustrative scene. Fictional people, not actual Food City customers.',36,216,540,8,GRAY)
para('One proposed service. More ways to participate.',36,184,540,19,NAVY,True)
para('Customers order groceries. Employees choose paid delivery assignments. Approved households receive help with delivery fees through a funded community assistance program.',36,147,540,13)
footer(1);c.showPage()
header('HOW COMMUNITY CONNECT COULD WORK')
photo('family.png',0,510,612,234)
para('AI-generated illustrative scene. Fictional people. No endorsement implied.',36,497,540,8,GRAY)
y=465
for title,body in [
 ('For customers','Order a grocery basket of at least $15 and follow its progress. The proposed delivery fee is $4.95. Groceries remain customer funded.'),
 ('For neighbors who need assistance','Request a delivery fee waiver for a transportation barrier. The proposed benefit allows up to four deliveries during a 30-day approval, subject to manager review and available funding.'),
 ('For participating employees','The store manager decides who can be spared. Released employees choose whether to accept a paid assignment. Track delivery time and miles. Earn a proposed $2 supplementary fuel reward for each completed delivery, separate from wages and mileage reimbursement.'),
 ('For one store to test','Four readiness weeks, then eight service weeks. The five-mile radius applies unless an employee adds a rural or homeward corridor to the delivery map. Employees choose which route deliveries to accept.')]:
  y=para(title,36,y,540,17,RED,True)-8;y=para(body,36,y,540,12)-21
footer(2);c.showPage()
header('A PILOT WITH CLEAR RESPONSIBILITY')
para('A community benefit needs<br/>a funded operating plan',36,714,540,28,NAVY,True)
para('800',36,607,250,52,RED,True);para('proposed completed deliveries',36,541,260,13)
para('240',333,607,230,52,RED,True);para('proposed fee-assisted deliveries',333,541,243,13)
y=490
for title,body in [
 ('Short-route reference case, not a rural average','$18,413 in eight-week operating expense. $2,772 in customer delivery fees and an assumed $1,188 sponsor transfer leave a $14,453 operating gap. Sponsors have not committed funds.'),
 ('Reference gross pilot authorization: $38,425','At 18 miles and 45 delivery minutes per order, the rural scenario needs a $26,413 operating subsidy and $52,179 gross authorization. Validate actual routes before approving a budget.'),
 ('Readiness before live deliveries','HR and counsel review paid work and reward treatment. Insurers approve coverage. Operations approve safe handling and driver procedures. Security and finance approve data controls and funding.'),
 ('Longer-term delivery vision','A future network could use central drone hubs, with Abingdon as a feasibility example. This requires a separate operator, approvals and business case. Ground delivery remains the prototype and fallback.')]:
  y=para(title,36,y,540,17,RED,True)-8;y=para(body,36,y,540,12)-23
footer(3);c.showPage()
header('EXPLORE THE LOCAL DEMONSTRATION')
para('One prototype.<br/>Three connected consoles.',36,710,540,30,NAVY,True)
photo('porch.png',36,350,540,230)
para('AI-generated illustrative scene. Fictional people.',36,338,540,8,GRAY)
y=305
for title,body in [('Customer','Build a basket, place a paid or assisted order, request assistance and track progress.'),('Employee','Accept or release an assignment, record delivery outcomes and inspect fuel reward credits.'),('Management','Prepare and offer orders, review assistance, approve simulated rewards and inspect the demo scorecard.')]:
 y=para(title,36,y,540,15,RED,True)-4;y=para(body,36,y,540,11)-15
para('For demonstration only',36,98,540,13,NAVY,True)
para('Synthetic data throughout. No real payments, payroll connection, customer records or fuel vouchers. See the accompanying architecture and pilot plan for assumptions, risks and launch gates.',36,77,540,9,GRAY)
footer(4);c.save()
doc=pdfium.PdfDocument(str(OUT/'Food-City-Community-Connect-Brochure.pdf'));(ROOT/'work/brochure-preview').mkdir(exist_ok=True)
for i,p in enumerate(doc):p.render(scale=1.3).to_pil().save(ROOT/f'work/brochure-preview/page-{i+1}.png')
print('Created and rendered',len(doc),'brochure pages')

