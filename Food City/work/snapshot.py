import pathlib,zipfile,hashlib,json
root=pathlib.Path.cwd(); dest=root/'outputs'/'Food-City-Complete-Workspace.zip'
files=[p for p in root.rglob('*') if p.is_file() and p!=dest and '.git' not in p.parts and not p.is_relative_to(root/'work'/'cv-save')]
manifest=[]
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED) as z:
 for p in files:
  data=p.read_bytes();rel=p.relative_to(root).as_posix();z.writestr(rel,data);manifest.append({'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
 z.writestr('BACKUP-MANIFEST.json',json.dumps(manifest,indent=2))
with zipfile.ZipFile(dest) as z: assert z.testzip() is None
print(f'Complete snapshot: {len(files)} files, {dest.stat().st_size} bytes')
