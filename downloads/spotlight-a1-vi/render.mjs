import{createRequire}from'node:module';import{spawn}from'node:child_process';import{once}from'node:events';
const req=createRequire('/workspace/video-shotcraft/.agents/skills/directing-stickman-videos/package.json');const{createCanvas}=req('@napi-rs/canvas');let c=createCanvas(1080,1920),g=c.getContext('2d');const duration=66.8,fps=24;
const clamp=x=>Math.max(0,Math.min(1,x)),ease=x=>{x=clamp(x);return x*x*(3-2*x)},mix=(a,b,t)=>a+(b-a)*t;
function line(p,col='#171717',w=7){g.beginPath();p.forEach(([x,y],i)=>i?g.lineTo(x,y):g.moveTo(x,y));g.lineWidth=w;g.strokeStyle=col;g.lineCap='round';g.lineJoin='round';g.stroke()}
function circle(x,y,r,col='#171717',w=7){g.beginPath();g.arc(x,y,r,0,Math.PI*2);g.strokeStyle=col;g.lineWidth=w;g.stroke()}
function figure(x,y,s,t,pose='idle',alpha=1){g.save();g.globalAlpha=alpha;g.translate(x,y);g.scale(s,s);let bob=Math.sin(t*2)*2;g.translate(0,bob);circle(0,0,46);line([[0,46],[0,190]]);let a=Math.sin(t*3)*15;
let left=pose==='hair'?[[-2,85],[-80,58],[-25,-35]]:pose==='open'?[[-2,85],[-77,112],[-127,75]]:[[-2,85],[-61,140],[-73+a,195]];
let right=pose==='chest'?[[2,85],[76,122],[15,135]]:pose==='open'?[[2,85],[77,112],[127,75]]:[[2,85],[61,140],[73-a,195]];line(left);line(right);let stride=pose==='walk'?Math.sin(t*5)*33:0;line([[0,190],[-38-stride,260],[-50-stride,330]]);line([[0,190],[38+stride,260],[50+stride,330]]);
if(pose==='hair'||pose==='chest'){line([[-15,12],[-7,8]],'#171717',4);line([[9,8],[17,12]],'#171717',4);g.beginPath();g.arc(0,31,9,Math.PI,2*Math.PI);g.stroke()}else{line([[-14,11],[-12,11]],'#171717',4);line([[12,11],[14,11]],'#171717',4);g.beginPath();g.arc(0,22,10,0,Math.PI);g.stroke()}g.restore()}
function thought(x,y,r,kind,t){g.save();g.globalAlpha=.8;circle(x,y,r,'#3785bd',4);circle(x-25,y+r+18,7,'#3785bd',3);circle(x-39,y+r+36,4,'#3785bd',3);if(kind==='hair'){line([[x-32,y+5],[x-26,y-20],[x-10,y-28],[x+8,y-20],[x+22,y-30],[x+35,y+5]],'#3785bd',5);circle(x,y+9,29,'#3785bd',4)}else{line([[x-25,y-24],[x+25,y+24]],'#3785bd',6);line([[x+25,y-24],[x-25,y+24]],'#3785bd',6)}g.restore()}
function draw(t){g.fillStyle='white';g.fillRect(0,0,1080,1920);let reveal=ease((t-23)/8);let fade=t>65?1-ease((t-65)/1.8):1;g.save();g.globalAlpha=fade;
// Consistent hollow-head figures on a flat white canvas. Connected single-pose limbs.
let sx=t<7?mix(170,490,ease(t/7)):t>59?mix(490,580,ease((t-59)/7)):490;let sy=1020;
if(t<33){g.save();g.globalAlpha=.3;line([[100,800],[100,1430],[980,1430],[980,800]],'#171717',4);line([[100,800],[100,550],[320,550],[320,1300]],'#171717',4);g.restore();}
let crowd=t>54?1-ease((t-54)/7):1;for(let i=0;i<5;i++){let x=[170,380,710,910,830][i],y=[850,650,650,850,1140][i];figure(x,y,.62,t+i,(t>32&&i===0)?'hair':(t>40&&i===3)?'chest':'idle',(.28+.4*reveal)*crowd)}
if(t>5&&t<28){let a=ease((t-5)/2)*(1-ease((t-23)/5));g.save();g.globalAlpha=a*.14;g.fillStyle='#e8b430';g.beginPath();g.moveTo(490,260);g.lineTo(190,1430);g.lineTo(800,1430);g.closePath();g.fill();g.restore();for(let i=0;i<4;i++){g.save();g.globalAlpha=a*.65;let x=[170,380,710,910][i],y=[850,650,650,850][i];line([[x,y+40],[mix(x,490,.70),mix(y+40,1050,.70)]],'#e8b430',3);g.restore()}}
let pose=t<7?'walk':t<13?'hair':t<24?'chest':t<32?'idle':t<54?'open':t<60?'chest':'walk';figure(sx,sy,1.05,t,pose);
if(t>8&&t<19){g.save();g.globalAlpha=Math.sin(Math.PI*clamp((t-8)/11));thought(620,790,76,'hair',t);g.restore()}
if(t>32&&t<54){let a=ease((t-32)/2)*(1-ease((t-51)/3));g.save();g.globalAlpha=a;thought(180,660,66,'hair',t);thought(890,650,66,'cross',t);g.restore()}
if(t>54){g.save();g.globalAlpha=ease((t-54)/4);circle(sx,sy+110,250,'#3785bd',4);g.restore()}
g.restore();return c}
let enc=spawn('ffmpeg',['-v','error','-y','-f','rawvideo','-pix_fmt','rgba','-s','1080x1920','-r','24','-i','pipe:0','-i','/workspace/outputs/spotlight-voice/spotlight-vi-continuous.mp3','-map','0:v','-map','1:a','-c:v','libx264','-crf','20','-preset','fast','-threads','4','-c:a','aac','-b:a','192k','-t',String(duration),'-pix_fmt','yuv420p','-movflags','+faststart','/workspace/outputs/spotlight-a1/spotlight-a1-vi.mp4'],{stdio:['pipe','inherit','inherit']});
for(let i=0;i<Math.ceil(duration*fps);i++){if(!enc.stdin.write(draw(i/fps).data()))await once(enc.stdin,'drain');if(i%240===0)console.log(i/fps)}enc.stdin.end();let[code]=await once(enc,'close');if(code)throw Error('encoder '+code);
