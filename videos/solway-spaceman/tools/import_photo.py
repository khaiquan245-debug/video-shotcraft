from pathlib import Path
import sys,zipfile,io,json,hashlib
from PIL import Image
r=Path(__file__).resolve().parents[1];p=Path(sys.argv[1]);data=None;source=p.name
if zipfile.is_zipfile(p):
 with zipfile.ZipFile(p) as z:
  files=[i for i in z.infolist() if not i.is_dir() and Path(i.filename).suffix.lower() in ['.jpg','.jpeg','.png','.webp'] and i.file_size<=16*1024*1024]
  if not files:raise SystemExit('No image file found in ZIP')
  files.sort(key=lambda i:i.file_size,reverse=True);data=z.read(files[0]);source=files[0].filename
else:data=p.read_bytes()
im=Image.open(io.BytesIO(data));im.verify();im=Image.open(io.BytesIO(data));ext={"JPEG":'.jpg',"PNG":'.png',"WEBP":'.webp'}.get(im.format)
if not ext:raise SystemExit('Unsupported image format')
name='solway_original'+ext
for d in [r/'assets/archival',r/'public/archival']:d.mkdir(exist_ok=True,parents=True);(d/name).write_bytes(data)
meta={'photoAvailable':True,'photoFile':'archival/'+name,'userPermissionConfirmed':True};(r/'src/media.json').write_text(json.dumps(meta,indent=2))
manifest={'file':str(r/'assets/archival'/name),'sha256':hashlib.sha256(data).hexdigest(),'sourceFile':source,'width':im.width,'height':im.height,'attribution':'Jim Templeton, May1964','permission':'User explicitly confirmed reuse rights in this chat; no independent public-domain/CC claim','modifications':'No retouching/recoloring; original aspect ratio preserved. Separate annotation/crop layers used in the edit.'};(r/'output/archival_manifest.json').write_text(json.dumps(manifest,indent=2));print(json.dumps(manifest,indent=2))
