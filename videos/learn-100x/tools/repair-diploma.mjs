import {bundle} from '@remotion/bundler';
import {openBrowser,selectComposition,renderMedia,renderStill} from '@remotion/renderer';
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {spawn} from 'node:child_process';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..'),out=path.join(root,'out');
const scenes=JSON.parse(fs.readFileSync(path.join(root,'src/timeline.json'),'utf8')),sc=scenes[2];
const run=(cmd,args)=>new Promise((res,rej)=>{const p=spawn(cmd,args,{stdio:['ignore','pipe','pipe']});let s='';p.stdout.on('data',d=>s+=d);p.stderr.on('data',d=>s+=d);p.on('close',c=>c===0?res(s):rej(Error(s)))});
const url=await bundle({entryPoint:path.join(root,'src/index.ts'),publicDir:path.join(root,'public')});const browser=await openBrowser('chrome',{browserExecutable:'/usr/bin/chromium'});
const part=path.join(out,'parts/classroom-legibility-final.mp4');
try{const composition=await selectComposition({serveUrl:url,id:'TenSeconds',puppeteerInstance:browser});
await renderMedia({serveUrl:url,composition,frameRange:[sc.from,sc.from+sc.duration-1],codec:'h264',outputLocation:part,puppeteerInstance:browser,concurrency:1,crf:20,x264Preset:'veryfast',imageFormat:'jpeg',jpegQuality:88,muted:true,overwrite:true,ffmpegOverride:({args})=>[...args.slice(0,-1),'-threads','1',args.at(-1)]});
for(const b of sc.beats.filter(b=>['diploma','requirements'].includes(b.tag)))await renderStill({serveUrl:url,composition,frame:sc.from+b.from+20,output:path.join(out,`qa/final-classroom-${b.tag}.jpg`),imageFormat:'jpeg',puppeteerInstance:browser});
}finally{await browser.close({silent:true})}
console.log('CLASSROOM REPAIR RENDERED');
while(!fs.readFileSync(path.join(out,'render.log'),'utf8').includes('RENDER COMPLETE'))await new Promise(r=>setTimeout(r,3000));
const lines=fs.readFileSync(path.join(out,'parts/concat.txt'),'utf8').trim().split('\n');lines[2]=`file '${part}'`;const list=path.join(out,'parts/concat-final.txt');fs.writeFileSync(list,lines.join('\n')+'\n');
await run('ffmpeg',['-v','error','-y','-f','concat','-safe','0','-i',list,'-i',path.join(root,'public/audio/master.flac'),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','160k','-t',String(scenes.reduce((n,s)=>n+s.duration,0)/30),'-movflags','+faststart',path.join(out,'learn-100x-final.mp4')]);
fs.copyFileSync(path.join(out,'learn-100x-final.mp4'),path.join(out,'learn-100x.mp4'));console.log('FINAL PICTURE AND MIX READY');
