import fs from 'node:fs';
import path from 'node:path';
import {spawn} from 'node:child_process';
import {once} from 'node:events';
import {createRequire} from 'node:module';
const req=createRequire('/workspace/video-shotcraft/.agents/skills/directing-stickman-videos/package.json');
const {createCanvas}=req('@napi-rs/canvas');
const BASE=path.dirname(new URL(import.meta.url).pathname),OUT=BASE+'/output';
const W=1080,H=1920,FPS=24,TAU=Math.PI*2,INK='#252626';
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));const ease=x=>{x=clamp(x);return x*x*(3-2*x)};const mix=(a,b,t)=>a+(b-a)*t;const P=(a,b,t)=>[mix(a[0],b[0],t),mix(a[1],b[1],t)];
const rnd=(()=>{let s=1683;return()=>{s=(s*1664525+1013904223)>>>0;return s/4294967296}})();
function line(c,ps,col,w=3){c.beginPath();ps.forEach((p,i)=>i?c.lineTo(...p):c.moveTo(...p));c.strokeStyle=col;c.lineWidth=w;c.lineCap='round';c.lineJoin='round';c.stroke()}
function poly(c,ps,col,stroke=null,w=2){c.beginPath();ps.forEach((p,i)=>i?c.lineTo(...p):c.moveTo(...p));c.closePath();c.fillStyle=col;c.fill();if(stroke){c.strokeStyle=stroke;c.lineWidth=w;c.stroke()}}
function el(c,x,y,rx,ry,col,stroke=null,w=2){c.beginPath();c.ellipse(x,y,rx,ry,0,0,TAU);if(col){c.fillStyle=col;c.fill()}if(stroke){c.strokeStyle=stroke;c.lineWidth=w;c.stroke()}}
function box(c,x,y,w,h,r,col,stroke=null,lw=2){c.beginPath();c.roundRect(x,y,w,h,r);c.fillStyle=col;c.fill();if(stroke){c.strokeStyle=stroke;c.lineWidth=lw;c.stroke()}}
function grad(c,x,y,xx,yy,stops){const g=c.createLinearGradient(x,y,xx,yy);for(const [p,col]of stops)g.addColorStop(p,col);return g}
function glow(c,x,y,rx,ry,col,a=1){c.save();c.translate(x,y);c.scale(1,ry/rx);const gr=c.createRadialGradient(0,0,0,0,0,rx);gr.addColorStop(0,col);gr.addColorStop(1,'rgba(0,0,0,0)');c.globalAlpha=a;c.fillStyle=gr;c.fillRect(-rx,-rx,rx*2,rx*2);c.restore()}
const far=createCanvas(1600,2200),f=far.getContext('2d');f.fillStyle=grad(f,0,0,0,1700,[[0,'#78b3cc'],[.42,'#c9d9c5'],[.65,'#efd6a4'],[1,'#be9b72']]);f.fillRect(0,0,1600,2200);
// Layered painted Mediterranean landscape, cypress trees and sunlit architecture.
for(let k=0;k<7;k++){const x=k*280-120;el(f,x,600+(k%3)*30,230,135,['#9faf87','#a3b78e','#b8bc91'][k%3]);}
for(const x of [120,310,1400]){poly(f,[[x,850],[x+40,500],[x+65,570],[x+88,850]],'#56755c');line(f,[[x+45,620],[x+45,880]],'#6b7552',5)}
for(let i=0;i<5;i++){let x=i*350-130,y=690+(i%2)*65;poly(f,[[x,y],[x+280,y],[x+282,1130],[x,1130]],'#ceb68c');poly(f,[[x-30,y],[x+145,y-102],[x+310,y]],'#ac6b50');for(let j=0;j<4;j++){box(f,x+30+j*61,y+60,35,78,16,'#9e9a79');line(f,[[x+30+j*61,y+100],[x+64+j*61,y+100]],'#bdac86',2)}}
const mid=createCanvas(1600,2200),m=mid.getContext('2d');
// Arcade columns recede toward the busy market court, with no visible signage.
poly(m,[[700,450],[1600,360],[1600,1320],[700,1320]],'#dcc9a4');poly(m,[[650,450],[1600,330],[1600,425],[650,535]],'#eddfbf','#b59b79',3);
for(let i=0;i<5;i++){const x=760+i*175,top=530-i*20;box(m,x,top,100,720,8,'#eadabd','#b6a07e',2);box(m,x-14,top-18,128,41,5,'#e7d4ad','#b59c77',2);box(m,x-16,1220,132,46,6,'#d7c09a','#ae9473',2);for(let j=0;j<4;j++)line(m,[[x+18+j*20,top+25],[x+18+j*20,1216]],'#d0bc98',3);if(i<4){box(m,x+103,top+95,69,550,31,'#847b64');glow(m,x+136,top+150,50,190,'rgba(225,194,137,.28)')}}
// Paving and perspective seams.
poly(m,[[0,1250],[1600,1220],[1600,2200],[0,2200]],'#d7bd90');for(let k=0;k<10;k++)line(m,[[k*190-150,1250],[k*300-390,2200]],'#bfa77f',2);for(let j=0;j<8;j++){const y=1280+j*j*18;line(m,[[0,y],[1600,y-13]],'#c1aa82',2)}
// A striped cloth canopy, warm reflected light and a side amphora define the stall.
line(m,[[650,680],[635,1395]],'#775b3f',12);line(m,[[1450,610],[1470,1360]],'#775b3f',12);poly(m,[[610,620],[1470,545],[1560,770],[550,866]],'#e0b784','#8e6950',3);
for(let i=0;i<8;i++)poly(m,[[610+i*108,620-i*9],[663+i*108,615-i*9],[619+i*126,859-i*11],[550+i*126,866-i*11]],i%2?'#e8d8af':'#a95745');line(m,[[550,866],[1560,770]],'#8e6950',3);
// Foliage and a terracotta vessel add depth without changing the historical drawing style.
poly(m,[[116,1200],[182,1200],[211,1375],[79,1375]],'#b47b54','#765d43',3);el(m,145,1195,38,13,'#7f6549');for(let k=0;k<12;k++){const a=k*.8;line(m,[[145,1200],[145+Math.sin(a)*70,1020+k*7]],'#697450',4);el(m,145+Math.sin(a)*70,1020+k*7,25,9,'#7f9863',null)}
// Distant cloth bundles and amphorae give material variety.
for(const [x,y,s]of [[1290,1300,1],[1420,1300,.8]]){m.save();m.translate(x,y);m.scale(s,s);el(m,0,-73,46,77,'#b88358','#8c6748',2);box(m,-22,-174,44,55,6,'#c59466','#8c6748',2);el(m,0,-174,27,8,'#755a40');line(m,[[-22,-142],[-56,-130],[-54,-79]],'#8c6748',9);m.restore()}
const table=createCanvas(900,650),t=table.getContext('2d');poly(t,[[50,150],[860,130],[860,220],[40,250]],grad(t,40,150,860,220,[[0,'#c5945f'],[1,'#9b7047']]),'#76573f',3);line(t,[[40,250],[860,220]],'#dec293',3);for(const x of [110,730]){poly(t,[[x,220],[x+35,220],[x+50,610],[x+12,610]],'#856343','#614c38',3)}
// A single shallow woven basket; the two fruit props remain distinct and conserved.
poly(t,[[150,120],[730,103],[690,170],[190,190]],'#ba8d58','#866641',3);for(let i=0;i<14;i++)line(t,[[170+i*38,125],[197+i*35,183]],'#8f6e47',2);for(let i=0;i<4;i++)line(t,[[168,133+i*13],[720,117+i*13]],'#d9b87e',2);
const c=createCanvas(process.argv.includes('--rig-check')?1:W,process.argv.includes('--rig-check')?1:H),g=c.getContext('2d');
const stats={frame_times:720,joint_samples:0,unreachable:0,max_length_error:0,white_neck_connection:'Single continuous filled head-neck path; no horizontal jaw line across neck.'};let now=0;
function ik(a,b,L=85,side=1){const dx=b[0]-a[0],dy=b[1]-a[1],d=Math.hypot(dx,dy);if(d>2*L+.001){stats.unreachable++;throw Error('Unreachable target at '+now+' '+JSON.stringify({a,b,d,L}))}const theta=Math.atan2(dy,dx),bend=Math.acos(clamp(d/(2*L),-1,1));return[a[0]+Math.cos(theta+side*bend)*L,a[1]+Math.sin(theta+side*bend)*L]}
function bone(c,a,b,end,L,w=5.5){stats.joint_samples++;const e=Math.max(Math.abs(Math.hypot(b[0]-a[0],b[1]-a[1])-L),Math.abs(Math.hypot(end[0]-b[0],end[1]-b[1])-L));stats.max_length_error=Math.max(stats.max_length_error,e);if(e>.01)throw Error('Bone drift '+e);line(c,[a,b,end],INK,w)}
// The black mitten silhouette has a single small thumb lobe, not fingers or a wrist-tip dot.
function palm(c,x,y,angle=0){c.save();c.translate(x,y);c.rotate(angle);c.beginPath();c.ellipse(0,0,4.4,9.3,0,0,TAU);c.ellipse(3.3,-1.6,2.6,4.2,-.25,0,TAU);c.fillStyle=INK;c.fill();c.restore()}
function actor(c,{x=400,y=820,s=1.45,face='calm',right=null,left=null,phase=0,merchant=false,lean=0}={}){
 c.save();c.translate(x,y+375*s);c.rotate(lean);c.scale(s,s);c.translate(0,-375);
 const local=pt=>{const dx=(pt[0]-x)/s,dy=(pt[1]-y-375*s)/s;return[dx*Math.cos(lean)+dy*Math.sin(lean),-dx*Math.sin(lean)+dy*Math.cos(lean)+375]};
 const hip=[0,205],feet=[[-38,375],[42,375]];
 for(const [j,foot]of feet.entries()){const knee=ik(hip,foot,90,j? -1:1);bone(c,hip,knee,foot,90,6.2);box(c,foot[0]-18,foot[1]-7,39,14,6,'#92704d',INK,2);line(c,[[foot[0]-12,foot[1]-7],[foot[0]+7,foot[1]-4]],'#d4b48b',2)}
 const cloth=merchant?grad(c,-70,70,80,225,[[0,'#ca8b65'],[.5,'#aa5b48'],[1,'#7d4f40']]):grad(c,-70,70,80,225,[[0,'#8caab5'],[.5,'#527c91'],[1,'#3b6278']]);
 poly(c,[[-70,70],[69,70],[82,126],[54,149],[55,212],[-57,212],[-57,146],[-84,127]],cloth,INK,2.8);line(c,[[-49,93],[-40,194]],merchant?'#dfa477':'#a2bbc0',3);line(c,[[37,87],[34,195]],merchant?'#844c3d':'#36596f',3);
 box(c,-58,168,116,13,3,'#806247',INK,1.8);box(c,-2,169,16,12,2,'#c7a259',INK,1.3);
 if(merchant){poly(c,[[-35,122],[36,122],[44,213],[-44,213]],'#e8d4b4','#b59979',1.8);line(c,[[-30,120],[-22,92]],'#c6ad87',3);line(c,[[30,120],[22,92]],'#c6ad87',3)}else{box(c,-57,180,26,37,5,'#9c794f',INK,2);box(c,-57,181,26,12,4,'#b08b61',INK,1.5)}
 // Exposed limbs are slender black strokes, with fixed shoulder/elbow/wrist chains.
 const rh=right?local(right):[75,236],lh=left?local(left):[-75,236];
 for(const [a,b,side]of [[[-62,86],lh,1],[[62,86],rh,-1]]){const elbow=ik(a,b,85,side);bone(c,a,elbow,b,85,5.5);palm(c,b[0],b[1],side*.12)}
 // A5 head and short white neck are one continuous silhouette, entering the tunic collar.
 c.beginPath();c.moveTo(-12,68);c.lineTo(-12,50.6);c.ellipse(0,0,52,52,0,Math.acos(-12/52),TAU+Math.acos(12/52));c.lineTo(12,68);c.closePath();c.fillStyle=grad(c,-45,0,50,20,[[0,'#ece7da'],[.48,'#fffaf0'],[1,'#f8e4bd']]);c.fill();c.strokeStyle=INK;c.lineWidth=2.8;c.stroke();
 // Collared edge leaves the short white jaw/neck connection fully visible.
 line(c,[[-20,70],[-13,74],[13,74],[22,70]],merchant?'#a45d49':'#4a6f82',3);
 if(merchant){
  for(const [xx,yy,r]of [[-43,-30,18],[-31,-43,18],[-8,-49,19],[17,-47,18],[39,-33,18]])el(c,xx,yy,r,r*.85,'#a7a599',INK,1.7);
  poly(c,[[-40,20],[-26,48],[0,57],[28,44],[40,21],[26,31],[0,38],[-25,31]],'#a3a397',INK,1.5);line(c,[[-18,29],[0,32],[17,27]],'#d0cabe',2);
 }else{
  poly(c,[[-50,-15],[-46,-44],[-25,-59],[-2,-63],[21,-57],[44,-40],[51,-10],[32,-28],[15,-23],[-2,-35],[-22,-25]],grad(c,-40,-50,50,-10,[[0,'#795844'],[1,'#4a382e']]),INK,2);line(c,[[-29,-46],[-4,-51],[19,-42]],'#a1805c',2.8)
 }
 const blink=Math.sin(phase*2.1)>.992;for(const xx of [-17,16])el(c,xx,-2,4.7,blink?1.1:8.3,INK);
 line(c,[[2,5],[5,10],[1,12]],INK,1.5);
 if(face==='smile'){c.beginPath();c.moveTo(-12,23);c.quadraticCurveTo(1,34,18,20);c.strokeStyle=INK;c.lineWidth=2.2;c.stroke()}
 else if(face==='defensive'){line(c,[[-28,-23],[-12,-18]],INK,2.2);line(c,[[11,-18],[28,-24]],INK,2.2);line(c,[[-10,25],[13,22]],INK,2.2)}
 else if(face==='thoughtful'){line(c,[[-28,-23],[-12,-26]],INK,2);line(c,[[11,-27],[28,-23]],INK,2);c.beginPath();c.moveTo(-10,24);c.quadraticCurveTo(1,20,13,24);c.strokeStyle=INK;c.lineWidth=2;c.stroke()}
 else line(c,[[-10,24],[13,24]],INK,2.1);
 // A restrained cheek tint adds cartoon warmth without changing the white head.
 el(c,-29,15,9,4,'rgba(190,119,91,.13)');el(c,29,15,9,4,'rgba(190,119,91,.13)');
 c.restore();
}
function apple(c,x,y,scale=1,bad=0,angle=0){c.save();c.translate(x,y);c.rotate(angle);c.scale(scale,scale);c.beginPath();c.moveTo(0,-27);c.bezierCurveTo(-40,-46,-49,-4,-31,23);c.bezierCurveTo(-17,41,-5,29,0,30);c.bezierCurveTo(12,40,32,30,38,8);c.bezierCurveTo(51,-25,23,-42,0,-27);c.fillStyle=grad(c,-32,-28,38,30,[[0,'#d78e69'],[.4,'#bd5c47'],[1,'#924738']]);c.fill();c.strokeStyle=INK;c.lineWidth=2;c.stroke();line(c,[[0,-28],[3,-44]],'#6e563c',4);c.beginPath();c.ellipse(14,-38,16,6,-.4,0,TAU);c.fillStyle='#7a8d58';c.fill();line(c,[[-20,-19],[-24,-5]],'#e9ad7a',5);if(bad){c.globalAlpha=bad;el(c,12,9,18,15,'#805a3c');el(c,17,12,9,8,'#604d37');line(c,[[-4,12],[3,18],[12,17]],'#b98e58',2);c.globalAlpha=1}c.restore()}
function camera(z,cx,cy){g.translate(W/2,H*.54);g.scale(z,z);g.translate(-cx,-cy)}
function cam(t){if(t<2.8)return {z:mix(2.25,1.18,ease(t/2.8)),x:mix(550,650,ease(t/2.8)),y:mix(1010,1030,ease(t/2.8))};if(t<9.7)return {z:mix(1.14,1.30,ease((t-2.8)/6.9)),x:650,y:1030};if(t<16)return {z:mix(1.46,1.7,ease((t-9.7)/6.3)),x:590,y:1050};if(t<21)return {z:mix(1.48,1.65,ease((t-16)/5)),x:470,y:980};return {z:mix(1.3,1.46,ease((t-21)/9)),x:540,y:1030}}
function draw(time){now=time;g.resetTransform();g.fillStyle='#e6d1a7';g.fillRect(0,0,W,H);const k=cam(time);g.save();camera(k.z,k.x,k.y);g.drawImage(far,-150,-110);g.drawImage(mid,-150,-110);
 // A small soft foreground plant frames the sunny market without covering actions.
 const rootX=400,rootY=820,S=1.45;
 let right=[560,1115],left=null,face='calm',good=[620,1090],bad=[480,1080],badAngle=.22;
 if(time<4){const u=ease(time/4);good=P([620,1090],[590,1050],u);right=[good[0],good[1]+31];face=u>.6?'smile':'calm'}
 else if(time<10){const u=ease((time-4)/6);good=P([590,1050],[575,1028],u);right=[good[0],good[1]+31];face='smile'}
 else if(time<17){const u=ease((time-10)/3);good=[575,1028];right=[good[0],good[1]+31];face='defensive';bad=P([480,1080],[500,1080],u);left=time<13?[bad[0],bad[1]+21]:null}
 else if(time<22){good=[575,1028];right=[good[0],good[1]+31];face='defensive';bad=[500,1080]}
 else if(time<26){const u=ease((time-22)/4);good=P([575,1028],[550,1090],u);right=[good[0],good[1]+31];bad=P([500,1080],[320,1090],u);left=[bad[0],bad[1]+21];face='thoughtful';badAngle=mix(.22,-.12,u)}
 else {const u=ease((time-26)/4);good=[550,1090];right=[good[0],good[1]+31];bad=[320,1090];left=[bad[0],bad[1]+21];face='thoughtful';badAngle=-.12+Math.sin(u*Math.PI)*.15}
 // Two recurring roles only. The seller stays behind the same table and never spawns an apple.
 el(g,400,1378,85,14,'rgba(99,74,48,.16)');el(g,940,1352,75,12,'rgba(99,74,48,.14)');
 actor(g,{x:940,y:845,s:1.32,merchant:true,face:time>22?'smile':'calm',left:time>13&&time<18?P([841,1156],[810,1090],Math.sin(Math.PI*(time-13)/5)):null,phase:time*.4});
 g.drawImage(table,405,910,790,570);
 actor(g,{x:rootX,y:rootY,s:S,face,right,left,phase:time*.6});
 apple(g,good[0],good[1],1.0,0,-.08+Math.sin(time*.7)*.025);apple(g,bad[0],bad[1],.95,1,badAngle);
 // Small glints emphasize selected evidence; the bruised fruit stays visible, never erased.
 if(time>3&&time<9){const a=Math.sin(Math.PI*clamp((time-3)/6));g.save();g.globalAlpha=a*.45;line(g,[[good[0]-45,good[1]-43],[good[0]-55,good[1]-55]],'#f5df9c',2);line(g,[[good[0]+42,good[1]-35],[good[0]+52,good[1]-42]],'#f5df9c',2);g.restore()}
 // Painterly light, softened ground shadows and slight dust give depth, not paper grain.
 g.save();g.globalCompositeOperation='screen';glow(g,250,600,620,780,'rgba(255,218,145,.10)');for(let j=0;j<12;j++){const q=(j*.173+time*.025)%1;el(g,520+Math.sin(j*2.3)*390,680+q*520,1.4,1.4,`rgba(255,236,177,${.06+.1*Math.sin(q*Math.PI)})`)}g.restore();
 g.restore();const vig=g.createRadialGradient(W*.5,H*.43,270,W*.5,H*.5,1200);vig.addColorStop(0,'rgba(0,0,0,0)');vig.addColorStop(1,'rgba(102,75,42,.18)');g.fillStyle=vig;g.fillRect(0,0,W,H);
 if(time>29.4){g.fillStyle=`rgba(238,218,181,${ease((time-29.4)/.6)*.75})`;g.fillRect(0,0,W,H)}return c;
}
fs.mkdirSync(OUT,{recursive:true});
if(process.argv.includes('--rig-check')){for(let i=0;i<FPS*30;i++)draw(i/FPS);fs.writeFileSync(BASE+'/joint-diagnostics.json',JSON.stringify(stats,null,2));console.log(JSON.stringify(stats));process.exit(0)}
if(process.argv.includes('--stills')){for(const time of [.4,3.8,8.2,10.5,12,17,22.8,25,28.2])fs.writeFileSync(OUT+'/frame-'+time+'.jpg',draw(time).toBuffer('image/jpeg',92));console.log('Stills rendered.');process.exit(0)}
const enc=spawn('ffmpeg',['-v','error','-y','-f','rawvideo','-pix_fmt','rgba','-s',W+'x'+H,'-r',String(FPS),'-i','pipe:0','-an','-c:v','libx264','-crf','18','-preset','fast','-threads','4','-pix_fmt','yuv420p','-movflags','+faststart',OUT+'/picture.mp4'],{stdio:['pipe','inherit','inherit']});
for(let i=0;i<FPS*30;i++){if(!enc.stdin.write(draw(i/FPS).data()))await once(enc.stdin,'drain');if(i%48===0)console.log(JSON.stringify({seconds:i/FPS,total:30}))}enc.stdin.end();const [code]=await once(enc,'close');if(code)throw Error('FFmpeg exit '+code);fs.writeFileSync(BASE+'/joint-diagnostics.json',JSON.stringify(stats,null,2));console.log('Picture complete.');
