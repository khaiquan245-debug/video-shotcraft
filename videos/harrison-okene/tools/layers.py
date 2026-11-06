from pathlib import Path
from PIL import Image,ImageDraw,ImageFilter
r=Path(__file__).resolve().parents[1];d=r/'public/layers';d.mkdir(exist_ok=True)
# Original user-supplied illustration pieces, kept at original proportions.
im=Image.open(r/'assets/illustrations/01_hook_hand.png').convert('RGBA')
regions={'hand':[(300,326),(327,308),(346,288),(378,274),(411,273),(445,285),(471,304),(470,343),(447,365),(420,375),(402,368),(374,374),(350,375),(334,365),(310,364),(303,350)],'glove':[(179,496),(197,459),(226,428),(253,392),(278,385),(292,394),(291,411),(316,400),(342,408),(353,426),(340,447),(370,435),(402,447),(410,462),(392,487),(413,491),(425,511),(416,534),(391,555),(371,587),(336,618),(314,649),(197,649)]}
base=im.copy()
for name,poly in regions.items():
 mask=Image.new('L',im.size);ImageDraw.Draw(mask).polygon(poly,fill=255);mask=mask.filter(ImageFilter.GaussianBlur(.65));part=im.copy();part.putalpha(mask);part.save(d/f'{name}.png')
 texture=im.crop((495,390,590,645)).resize(im.size).filter(ImageFilter.GaussianBlur(4));erase=mask.filter(ImageFilter.MaxFilter(25)).filter(ImageFilter.GaussianBlur(12));base.paste(texture,(0,0),erase)
base.save(d/'hook-background.png')
print('LAYER ASSETS READY')
