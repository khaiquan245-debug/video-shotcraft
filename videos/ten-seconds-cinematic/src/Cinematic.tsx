import React from 'react';
import {AbsoluteFill,interpolate,useCurrentFrame} from 'remotion';
import {StoryArt} from './Story';
import {C,Person,Room,Skyline,Phone,Cup,Car} from './Art';
import scenes from './timeline.json';
import shots from './shots.json';
export type Shot=typeof shots[number];
const clamp={extrapolateLeft:'clamp',extrapolateRight:'clamp'} as const;
const ease=(x:number)=>{x=Math.max(0,Math.min(1,x));return x*x*(3-2*x)};
export const futureAt=(id:number,t:number)=>{const e=scenes[id].events as unknown as Record<string,number>;return (id===1&&t>=e.future&&t<e.present)||(id===2&&t<e.present)||(id===4&&t>=e.fall&&t<e.present)||(id===5&&t>=e.blink&&t<e.present)||(id===6&&t>=e.right&&t<e.present)||(id===7&&t>=e.future&&t<e.followup+75)||(id===8&&t>=e.visionSorry-30&&t<e.visionSorry+90)||(id===9&&t>=e.future&&t<e.present)};
const Backdrop:React.FC<{chapter:number}>=({chapter})=>[1,3,4,7].includes(chapter)?<Room office={chapter===3||chapter===7}/>:<Skyline warm={chapter===8||chapter===11} night={chapter===9||chapter===10}/>;
const Insert:React.FC<{shot:Shot;t:number;progress:number}>=({shot,t,progress})=>{
 const id=shot.chapter;const future=futureAt(id,t);const reaction=(/Apparently|And that|Okay|breathing/.test(shot.phrase)||(id===3&&shot.phrase.startsWith('You have')))?'shock':/words|choice|ignored/.test(shot.phrase)?'sad':'calm';
 if(shot.mode==='face')return <><Backdrop chapter={id}/><rect width="1600" height="760" fill={id===9?'#091322':'#13263b'} opacity=".5"/><circle cx="800" cy="360" r="350" fill={id===9?'#e9b68a':'#78d6cf'} opacity=".055"/><g transform={`translate(800 390) scale(${1+progress*.035}) translate(-800 -390)`}><Person x={800} y={1010} s={2.55} face={shot.phrase.includes('blink')&&progress>.15&&progress<.4?'blink':reaction} pose={id===9&&t>(scenes[9].events.answer??1179)?'phone':'stand'}/>{future&&<g fill={C.teal} opacity=".72"><ellipse cx="762" cy="344" rx="21" ry="31"/><ellipse cx="841" cy="344" rx="21" ry="31"/></g>}</g></>;
 if(shot.mode==='phone'||shot.mode==='desk'||shot.mode==='cup')return <><defs><linearGradient id="desk-wood" x2="1" y2="1"><stop stopColor="#a78a71"/><stop offset="1" stopColor="#3c3434"/></linearGradient></defs><rect width="1600" height="760" fill="url(#desk-wood)"/>{[0,1,2,3,4,5,6,7].map(i=><path key={i} d={`M${i*240-300} 0l250 760`} stroke="#241f27" strokeWidth="3" opacity=".22"/>)}{shot.mode==='cup'?<><ellipse cx="800" cy="500" rx="180" ry="48" fill="#142135" opacity=".22"/><g transform={`translate(800 380) rotate(${-12+progress*25}) scale(4)`}><Cup x={0} y={0}/></g><path d="M970 190l70 -70m-45 100l90 -20" stroke={C.cream} strokeWidth="8" opacity=".5"/></>:shot.mode==='desk'?<><g transform="translate(800 375) rotate(-6)"><rect x="-330" y="-235" width="660" height="470" rx="10" fill={C.cream}/><text x="-270" y="-150" fontFamily="Arial" fontSize="38" fill={C.ink} fontWeight="bold">THE PLAN</text>{[0,1,2,3].map(i=><path key={i} d={`M-270 ${-80+i*60}h${i===1?390:500}`} stroke={i===1?C.teal:'#a0aaa2'} strokeWidth={i===1?28:9}/>)}<path d="M-270 -20h390" stroke={C.ink} strokeWidth="7"/></g></>:<><path d="M450 760q20 -300 220 -260l220 50 210 210Z" fill="#fff5df" stroke="#172333" strokeWidth="10"/><g transform={`translate(800 380) rotate(${-7+progress*4}) translate(-800 -380)`}><Phone x={800} y={365} s={1.9} calling={id===9}/></g></>}<rect width="1600" height="760" fill="#102033" opacity=".1"/></>;
 if(shot.mode==='danger')return <><Skyline night/><path d="M0 540h1600v220H0Z" fill="#253347"/><path d="M0 700h380m180 0h400m180 0h460" stroke={C.gold} strokeWidth="7"/><g transform={`translate(${1000-progress*450} 0)`}><Car x={800} y={640} truck={id===9} sy={1.2} flip/></g><path d="M1500 530h-390m390 40h-290m290 40h-180" stroke={C.cream} opacity=".25" strokeWidth="5"/></>;
 return null;
};
export const CinematicShot:React.FC<{shot:Shot}>=({shot})=>{
 const f=useCurrentFrame();const t=shot.localFrom+f;const p=ease(f/Math.max(1,shot.duration-1));const future=futureAt(shot.chapter,t);
 const z=shot.zoom*(1+p*(shot.mode==='over'?.02:.035));const x=Math.max(800/z,Math.min(1600-800/z,shot.x));const y=Math.max(380/z,Math.min(760-380/z,shot.y));
 const world=shot.mode==='world'||shot.mode==='over';const sc=scenes[shot.chapter];const e=sc.events as unknown as Record<string,number>;
 const switchFrames=[e.future??e.blink??e.fall??e.right,e.present].filter(n=>typeof n==='number');const blink=Math.max(0,...switchFrames.map(n=>1-Math.abs(t-n)/5));
 return <AbsoluteFill style={{background:'#080f1d'}}>
 <svg viewBox="0 0 1600 760" style={{position:'absolute',left:0,top:66,width:1920,height:912,overflow:'hidden'}}>
 <defs><radialGradient id="shot-vignette"><stop offset=".35" stopColor="#020716" stopOpacity="0"/><stop offset="1" stopColor="#020716" stopOpacity=".48"/></radialGradient><linearGradient id="window-light"><stop stopColor="#ffe1a7" stopOpacity=".12"/><stop offset="1" stopColor="#ffe1a7" stopOpacity="0"/></linearGradient></defs>
 {world?<g transform={`translate(800 380) scale(${z}) translate(${-x} ${-y})`}><StoryArt id={shot.chapter} t={t} duration={sc.duration}/></g>:shot.mode==='concept'?<><Skyline warm={shot.chapter!==6} night={shot.chapter===6}/><rect width="1600" height="760" fill="#091322" opacity=".82"/>{shot.chapter===0&&<text x="800" y="260" textAnchor="middle" fill={C.teal} fontFamily="Arial" fontSize="30" letterSpacing="9">WHAT IF YOU COULD SEE</text>}{shot.text.split('\n').map((line,i,ls)=><text key={line} x="800" y={ls.length===1?420:340+i*110} textAnchor="middle" fill={i===1?C.cream:C.gold} fontFamily="Arial,sans-serif" fontWeight="800" fontSize={line.length>30?62:80} letterSpacing="-2">{line}</text>)}<path d="M700 500h200" stroke={C.teal} strokeWidth="4"/>{shot.chapter===0&&<text x="800" y="580" textAnchor="middle" fill={C.cream} fontFamily="Arial" fontSize="28">One glimpse. A different choice.</text>}</>:<Insert shot={shot} t={t} progress={p}/>}
 {shot.mode==='over'&&<g transform="translate(-70 140)"><path d="M-40 620q-30 -250 85 -290q-70 -120 -10 -210l-20 -35 55 8 5 -36 35 28 35 -40 20 48 45 -10 0 45q85 100 0 205q150 50 170 287Z" fill="#08111d" opacity=".9"/></g>}
 {world&&shot.chapter===8&&<g transform={`translate(${-p*45} 0)`} fill="#152d31" opacity=".55"><path d="M0 0q150 130 115 265Q20 240 0 0M1600 0q-180 120 -130 270q130 -20 130 -270Z"/></g>}
 {[0,1,2,3,4,5,6,7,8,9,10,11].map(i=><circle key={i} cx={(i*317+f*.13)%1600} cy={(i*137+f*.07)%760} r={1+i%3} fill={C.cream} opacity={.035+i%3*.015}/>)}
 {!future&&<path d="M0 80l720 680h-350L0 380Z" fill="url(#window-light)"/>}
 {future&&<><rect width="1600" height="760" fill={C.teal} opacity=".08"/><rect x="1240" y="34" width="310" height="61" rx="8" fill="#081b2c" opacity=".94"/><circle cx="1270" cy="65" r="6" fill={C.teal}/><text x="1396" y="76" textAnchor="middle" fill={C.teal} fontFamily="Arial" fontSize="27" letterSpacing="2">+10 SECONDS</text></>}
 <rect width="1600" height="760" fill="url(#shot-vignette)"/>
 {blink>0&&<><rect width="1600" height={380*blink} fill="#091322"/><rect y={760-380*blink} width="1600" height={380*blink} fill="#091322"/></>}
 </svg>

 </AbsoluteFill>;
};
