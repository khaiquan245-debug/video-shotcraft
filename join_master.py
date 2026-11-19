from pathlib import Path
import hashlib,json,zipfile
root=Path(__file__).resolve().parent
m=json.loads((root/'manifest.json').read_text())
def digest(path):
 h=hashlib.sha256()
 with path.open('rb')as f:
  while b:=f.read(1048576):h.update(b)
 return h.hexdigest()
z=root/m['zip_name']
if not z.exists():
 tmp=z.with_suffix('.zip.tmp')
 with tmp.open('wb')as out:
  for p in m['parts']:
   src=root/p['name']
   assert src.stat().st_size==p['bytes']and digest(src)==p['sha256'],'Part mismatch: '+p['name']
   with src.open('rb')as f:
    while b:=f.read(1048576):out.write(b)
 assert digest(tmp)==m['zip_sha256'],'ZIP checksum mismatch'
 tmp.rename(z)
assert digest(z)==m['zip_sha256'],'Existing ZIP checksum mismatch'
dest=root/'Video_Master'
if dest.exists():
 video=dest/m['master_name']
 if video.exists()and digest(video)==m['master_sha256']:
  print('Existing master verified:',video)
  raise SystemExit(0)
 import time
 dest=root/('Video_Master_'+str(time.time_ns()))
with zipfile.ZipFile(z)as f:
 for n in f.namelist():(dest/n).resolve().relative_to(dest.resolve())
 f.extractall(dest)
video=dest/m['master_name']
assert video.stat().st_size==m['master_bytes']and digest(video)==m['master_sha256'],'Master mismatch'
print('Verified original master:',video)
