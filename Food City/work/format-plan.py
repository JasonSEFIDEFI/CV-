from pathlib import Path
import html,re
src=Path('outputs/Architecture-and-Pilot.md').read_text(encoding='utf-8-sig')
parts=[];table=False
for line in src.splitlines():
 if line.startswith('|'):
  if not table:parts.append('<table>');table=True
  if re.match(r'^\|[\s:|\-]+$',line):continue
  cells=line.strip('|').split('|');parts.append('<tr>'+''.join('<td>'+html.escape(c.strip())+'</td>' for c in cells)+'</tr>');continue
 if table:parts.append('</table>');table=False
 if not line:continue
 if line.startswith('#'):
  n=len(line)-len(line.lstrip('#'));parts.append(f'<h{n}>'+html.escape(line[n:].strip())+f'</h{n}>')
 else:parts.append('<p>'+html.escape(line)+'</p>')
body='\n'.join(parts)
body=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',body)
body=re.sub(r'(https://[^\s<]+)',r'<a href="\1">\1</a>',body)
Path('outputs/Architecture-and-Pilot.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>Community Connect architecture and pilot</title><style>body{font:17px/1.6 system-ui;color:#123269;max-width:1100px;margin:45px auto;padding:0 25px}h1{border-top:12px solid #c92032;padding-top:25px;font-size:40px}h2{color:#c92032;margin-top:42px}table{border-collapse:collapse;width:100%;font-size:15px}td{padding:10px;border-bottom:1px solid #cbd3e2}tr:first-child{background:#123269;color:white;font-weight:bold}a{color:#c92032;overflow-wrap:anywhere}@media print{body{font-size:11pt}h2{break-after:avoid}tr{break-inside:avoid}}</style>'+body+'</html>',encoding='utf-8')
