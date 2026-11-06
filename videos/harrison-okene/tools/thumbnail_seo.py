from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
r=Path(__file__).resolve().parents[1];src=Image.open(r/'assets/illustrations/04_rescue_reveal.png').convert('RGB');font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def txt(im,xy,text,size,color):
 d=ImageDraw.Draw(im);d.text(xy,text,font=ImageFont.truetype(font,size),fill=color,stroke_width=2,stroke_fill='#03151b')
im=Image.new('RGB',(1280,720),'#061e29');art=src.resize((800,877),Image.Resampling.LANCZOS);im.paste(art,(480,-85))
shade=Image.new('RGBA',im.size);pixels=shade.load()
for x in range(1280):
 alpha=250 if x<430 else round(max(0,250*(1-(x-430)/470)))
 for y in range(720):pixels[x,y]=(3,20,29,alpha)
im=Image.alpha_composite(im.convert('RGBA'),shade).convert('RGB')
txt(im,(48,158),'62 HOURS',103,'#ffe278');txt(im,(50,282),'UNDERWATER',64,'#ffffff')
d=ImageDraw.Draw(im);d.rounded_rectangle((50,402,598,493),radius=12,fill='#ffe278');d.text((71,421),'HE WAS ALIVE.',font=ImageFont.truetype(font,49),fill='#07212b')
txt(im,(50,641),'ILLUSTRATED RECONSTRUCTION',18,'#91b4bd');im.save(r/'output/harrison_okene_thumbnail_1280x720.png')
v=Image.new('RGB',(1080,1920),'#061e29');art=src.resize((1080,1184),Image.Resampling.LANCZOS);v.paste(art,(0,350));d=ImageDraw.Draw(v);txt(v,(75,100),'62 HOURS',145,'#ffe278');txt(v,(79,270),'UNDERWATER',105,'#fff');d.rounded_rectangle((88,1515,992,1680),radius=18,fill='#ffe278');d.text((128,1551),'HE WAS ALIVE.',font=ImageFont.truetype(font,95),fill='#07212b');txt(v,(250,1790),'ILLUSTRATED RECONSTRUCTION',26,'#91b4bd');v.save(r/'output/harrison_okene_thumbnail_1080x1920.png')
