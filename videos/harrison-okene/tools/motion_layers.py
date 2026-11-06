from pathlib import Path
from PIL import Image,ImageDraw,ImageFilter
r=Path(__file__).resolve().parents[1];d=r/'public/layers';im=Image.open(r/'assets/illustrations/03_air_pocket.png').convert('RGBA')
poly=[(0,321),(46,286),(74,242),(66,171),(82,119),(131,86),(195,68),(239,87),(265,121),(285,159),(302,207),(292,247),(318,239),(369,242),(411,268),(445,326),(471,347),(489,391),(518,430),(518,484),(491,520),(420,538),(278,548),(139,552),(0,541)]
mask=Image.new('L',im.size);ImageDraw.Draw(mask).polygon(poly,fill=255);mask=mask.filter(ImageFilter.GaussianBlur(.7))
for name,box in [('survivor-head',(0,0,594,279)),('survivor-body',(0,260,594,650))]:
 m=Image.new('L',im.size);ImageDraw.Draw(m).rectangle(box,fill=255)
 import PIL.ImageChops
 a=PIL.ImageChops.multiply(mask,m);out=im.copy();out.putalpha(a);out.save(d/f'{name}.png')
