import {bundle} from '@remotion/bundler';
import {openBrowser,selectComposition,renderStill,renderMedia} from '@remotion/renderer';
import fs from 'node:fs';import {resolve,dirname} from 'node:path';import {fileURLToPath} from 'node:url';import {createHash} from 'node:crypto';import {spawn} from 'node:child_process';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');const out=resolve(root,'out');fs.mkdirSync(resolve(out,'parts'),{recursive:true});fs.mkdirSync(resolve(out,'qa'),{recursive:true});
const scenes=JSON.parse(fs.readFileSync(resolve(root,'src/timeline.json'),'utf8'));const total=scenes.reduce((n,s)=>n+s.duration,0);
const hash=createHash('sha256');for(const name of fs.readdirSync(resolve(root,'src')).filter(n=>!n.startsWith('workbench.')).sort())hash.update(fs.readFileSync(resolve(root,'src',name)));const build=hash.digest('hex').slice(0,12);
const serveUrl=await bundle({entryPoint:resolve(root,'src/index.ts'),publicDir:resolve(root,'public')});
const browsers=[];const executable=process.env.CHROME_BIN||'/usr/bin/chromium';
const command=(cmd,args)=>new Promise((res,rej)=>{const p=spawn(cmd,args,{stdio:['ignore','pipe','pipe']});let text='';p.stdout.on('data',d=>text+=d);p.stderr.on('data',d=>text+=d);p.on('error',rej);p.on('close',code=>code===0?res(text):rej(new Error(text)))});
try{
 browsers.push(await openBrowser('chrome',{browserExecutable:executable}));
 const composition=await selectComposition({serveUrl,id:'Learn100xVI',puppeteerInstance:browsers[0]});
 const shots=JSON.parse(fs.readFileSync(resolve(root,'src/shots.json'),'utf8'));
 for(const shot of shots){await renderStill({serveUrl,composition,frame:shot.from+Math.round(shot.duration*.45),output:resolve(out,`qa/shot-${String(shot.id).padStart(3,'0')}.jpg`),puppeteerInstance:browsers[0],imageFormat:'jpeg',jpegQuality:90});if(shot.id%10===0)console.log(`KEYFRAMES ${shot.id}/${shots.length}`)}
 console.log('KEYFRAMES COMPLETE',shots.length);
 if(process.argv.includes('--stills-only'))process.exitCode=0;
 else{
  for(let i=1;i<4;i++)browsers.push(await openBrowser('chrome',{browserExecutable:executable}));
  let next=0,last=-1;const counts=scenes.map(()=>0);const paths=scenes.map(s=>resolve(out,`parts/${build}-scene-${s.id}.mp4`));
  const worker=async browser=>{while(next<scenes.length){const i=next++;const sc=scenes[i];
   if(fs.existsSync(paths[i])){try{const probe=JSON.parse(await command('ffprobe',['-v','error','-show_streams','-of','json',paths[i]]));if(Number(probe.streams.find(s=>s.codec_type==='video')?.nb_frames)===sc.duration){counts[i]=sc.duration;console.log(`REUSE ${i+1}/${scenes.length}`);continue;}}catch{console.log(`REBUILD incomplete part ${i+1}`)}}
   await renderMedia({serveUrl,composition,frameRange:[sc.from,sc.from+sc.duration-1],codec:'h264',outputLocation:paths[i],puppeteerInstance:browser,concurrency:1,crf:21,x264Preset:'veryfast',imageFormat:'jpeg',jpegQuality:88,muted:true,overwrite:true,ffmpegOverride:({args})=>[...args.slice(0,-1),'-threads','1',args.at(-1)],onProgress:p=>{counts[i]=p.renderedFrames;const f=counts.reduce((a,b)=>a+b,0),percent=Math.floor(f/total*20)*5;if(percent>last){last=percent;console.log(`RENDER ${percent}% frames=${f}/${total}`)}}});console.log(`CHAPTER RENDERED ${i+1}/${scenes.length}`);
  }};
  await Promise.all(browsers.map(worker));
  const list=resolve(out,'parts/concat.txt');fs.writeFileSync(list,paths.map(p=>`file '${p.replaceAll("'","'\\''")}'`).join('\n')+'\n');
  await command('ffmpeg',['-v','error','-y','-f','concat','-safe','0','-i',list,'-i',resolve(root,'public/audio/master.flac'),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','160k','-t',String(total/30),'-movflags','+faststart',resolve(out,'learn-100x-vi.mp4')]);
  await command('ffmpeg',['-v','error','-y','-i',resolve(out,'learn-100x-vi.mp4'),'-i',resolve(root,'public/audio/narration-sfx.flac'),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','160k','-t',String(total/30),'-movflags','+faststart',resolve(out,'learn-100x-vi-no-music.mp4')]);
  console.log('RENDER COMPLETE',total,total/30);
 }
}finally{await Promise.allSettled(browsers.map(b=>b.close({silent:true})))}
