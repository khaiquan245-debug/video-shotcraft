from pathlib import Path
import hashlib
EXPECTED = 'c697da2b2a678f97762f0d6e21851c8d463d9d80928247a3d60816572692b9ff'
PARTS = {'ChiLon_ReviewV3_MASTER_10Mbps.zip.part001': '84e9157d6a4a16eb8e91d7d07a63874a4d2b84ec572310dc3c257f047e1443be', 'ChiLon_ReviewV3_MASTER_10Mbps.zip.part002': 'cbde4a80c0fa22eeb09e3164719b26c698ae3ae316d190f515ddd7f27700c5a1'}
root=Path(__file__).resolve().parent
out=root/'ChiLon_ReviewV3_MASTER_10Mbps.zip'
if out.exists():
 assert hashlib.file_digest(out.open('rb'),'sha256').hexdigest()==EXPECTED,'Existing ZIP checksum mismatch; keep it and use a different folder.'
 print('ZIP already complete:',out)
else:
 for name,expected in PARTS.items():
  p=root/name
  assert p.exists(),'Missing part: '+name
  with p.open('rb')as f:assert hashlib.file_digest(f,'sha256').hexdigest()==expected,'Corrupt part: '+name
 tmp=out.with_suffix('.zip.partial')
 with tmp.open('wb')as f:
  for name in PARTS:
   with (root/name).open('rb')as src:
    while block:=src.read(1024*1024):f.write(block)
 with tmp.open('rb')as f:assert hashlib.file_digest(f,'sha256').hexdigest()==EXPECTED,'Joined ZIP checksum mismatch'
 tmp.rename(out)
 print('Verified ZIP ready; extract to get the original 10 Mbps MP4:',out)
