from pathlib import Path
import zipfile,json,hashlib,shutil,datetime
root=Path.cwd();archive=root/'outputs/Food-City-Complete-Workspace.zip'
repo=root/'work/cv-save/Food City'
backup=Path('V:/Food City')/('Community-Connect-Final-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
backup.mkdir(parents=True,exist_ok=False)
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    for name in z.namelist():
        assert not Path(name).is_absolute() and '..' not in Path(name).parts
    manifest=json.loads(z.read('BACKUP-MANIFEST.json'))
    z.extractall(backup)
    z.extractall(repo)
for folder in (backup,repo):
    shutil.copy2(archive,folder/archive.name)
    for row in manifest:
        file=folder/row['path']
        assert hashlib.sha256(file.read_bytes()).hexdigest()==row['sha256'],str(file)
    assert hashlib.sha256((folder/archive.name).read_bytes()).digest()==hashlib.sha256(archive.read_bytes()).digest()
record={'backup':str(backup),'repository_project_folder':'Food City','verified_file_count':len(manifest),'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'status':'verified'}
(root/'outputs/SAVE-VERIFICATION.json').write_text(json.dumps(record,indent=2))
print(json.dumps(record,indent=2))
