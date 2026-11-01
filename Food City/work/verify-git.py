from pathlib import Path
import subprocess,hashlib
root=Path.cwd();repo=root/'work/cv-save'
for name in ['Food-City-Community-Connect-Final.pptx','Food-City-Community-Connect-Brochure.pdf','Community-Connect-Prototype.zip','Food-City-Complete-Workspace.zip']:
 path='Food City/'+('' if name=='Food-City-Complete-Workspace.zip' else 'outputs/')+name
 data=subprocess.check_output(['git','-C',str(repo),'show','HEAD:'+path])
 local=(root/'outputs'/name).read_bytes()
 print(name, 'identical' if hashlib.sha256(data).digest()==hashlib.sha256(local).digest() else 'DIFFERS')
