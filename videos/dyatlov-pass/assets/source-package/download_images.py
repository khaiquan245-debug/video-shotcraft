#!/usr/bin/env python3
"""Download 3 archival photographs for the Dyatlov Pass VideoShotCraft project.
Run with Internet access: python download_images.py
The photos' reuse rights are NOT automatically granted by a successful download.
"""
from pathlib import Path
from urllib.request import Request, urlopen
from io import BytesIO
from PIL import Image
import time

OUT = Path(__file__).resolve().parent / 'anh_that'
OUT.mkdir(exist_ok=True)
SOURCES = {
 '01_nhom_nguoi_leo_nui_1959.jpg': [
  'https://dyatlovpass.com/resources/340/gallery/Yuri-Doroshenko-13.jpg',
 ],
 '03_leu_duoc_tim_thay_1959.jpg': [
  'https://dyatlovpass.com/resources/340/Dyatlov-pass-tent-01.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/7/71/Dyatlov_Pass_incident_02.jpg',
 ],
}
FIGURE='https://geomechanics.ethz.ch/project-list/Dyatlov_pass/_jcr_content/par/image/image.imageformat.1286.965835515.jpg'

def get(url):
 req=Request(url,headers={'User-Agent':'Mozilla/5.0 (educational archival research)'})
 with urlopen(req, timeout=30) as resp:
  return resp.read()

for filename, urls in SOURCES.items():
 path = OUT / filename
 if path.exists():
  print('Already exists:', path.name)
  continue
 for url in urls:
  try:
   data=get(url)
   img=Image.open(BytesIO(data)).convert('RGB')
   img.save(path, quality=93)
   print('Downloaded:', path.name, img.size, 'from', url)
   break
  except Exception as e:
   print('Failed:', url, str(e)[:200])
 else:
  print('NOT DOWNLOADED:', path.name)

# ETH Zurich Figure 1 is a composite (a,b,c). Crop only panel (a): the last campsite photograph.
path=OUT/'02_anh_cuoi_chuan_bi_dung_leu_1959.jpg'
if not path.exists():
 try:
  img=Image.open(BytesIO(get(FIGURE))).convert('RGB')
  w,h=img.size
  # Panel (a) occupies the top-left rectangle of Figure 1, above the horizontal divider.
  # Geometry determined from the verified 923x1000 figure preview; proportional scaling.
  crop=(0,0,round(w*439/923),round(h*295/1000))
  cropped=img.crop(crop)
  cropped.save(path, quality=95)
  print('Saved cropped original historical photo:', path.name, cropped.size)
 except Exception as e:
  print('NOT DOWNLOADED (ETH Figure 1a):', str(e)[:240])

print('Available photographs:', [x.name for x in OUT.glob('*.jpg')])
if len(list(OUT.glob('*.jpg')))!=3:
 print('Some websites blocked direct downloads. Download the pictures manually from the verified links in README.md.')
