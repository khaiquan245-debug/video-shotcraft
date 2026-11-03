import {bundle} from '@remotion/bundler';
import {openBrowser,selectComposition,renderStill,renderMedia} from '@remotion/renderer';
import fs from 'node:fs';import {dirname,resolve} from 'node:path';import {fileURLToPath} from 'node:url';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const serveUrl=await bundle({entryPoint:`${root}/src/index.ts`,publicDir:`${root}/public`});
const browser=await openBrowser('chrome',{browserExecutable:'/usr/bin/chromium'});
try{const composition=await selectComposition({serveUrl,id:'TenSeconds',puppeteerInstance:browser});const scenes=JSON.parse(fs.readFileSync(`${root}/src/timeline.json`,'utf8'));
for(const sc of scenes){for(const p of [.18,.62]){const frame=sc.from+Math.round(sc.duration*p);await renderStill({serveUrl,composition,frame,output:`${root}/out/qa/scene-${String(sc.id+1).padStart(2,'0')}-${Math.round(p*100)}.png`,puppeteerInstance:browser,imageFormat:'png'});}console.log(`KEYFRAMES ${sc.id+1}/12`)}
const sc=scenes[9];const rescueFrame=sc.from+(sc.events?.truck??966)+30;await renderStill({serveUrl,composition,frame:rescueFrame,output:`${root}/out/qa/rescue.png`,puppeteerInstance:browser,imageFormat:'png'});
let last=-1;await renderMedia({serveUrl,composition,codec:'h264',outputLocation:`${root}/out/ten-seconds-reference.mp4`,puppeteerInstance:browser,concurrency:4,crf:20,x264Preset:'veryfast',imageFormat:'jpeg',jpegQuality:88,inputProps:{bgm:true},onProgress:p=>{const n=Math.floor(p.progress*20)*5;if(n!==last){last=n;console.log(`RENDER ${n}% frames=${p.renderedFrames} encoded=${p.encodedFrames}`)}}});console.log('RENDER COMPLETE');}finally{await browser.close({silent:true})}
