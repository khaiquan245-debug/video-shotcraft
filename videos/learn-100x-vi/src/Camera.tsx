import React from 'react';
import {AbsoluteFill,useCurrentFrame} from 'remotion';
import {C,Room,Skyline} from './Art';
import {World,beatAt} from './World';
import {Stan,Label,Brain} from './Props';
import shots from './shots.json';
import scenes from './timeline.json';
import {viLabel} from './Vietnamese';
const TOTAL=scenes.reduce((n,s)=>n+s.duration,0);
export type Shot=typeof shots[number];
const ease=(n:number)=>{n=Math.max(0,Math.min(1,n));return n*n*(3-2*n)};
export const CameraShot:React.FC<{shot:Shot}>=({shot})=>{
 const f=useCurrentFrame(),t=shot.localFrom+f,beat=beatAt(shot.chapter,t),p=ease(f/Math.max(1,shot.duration-1));
 const emotional=shot.chapter>=8;const reveal=shot.tag==='brain'||shot.tag==='knowledge'||shot.tag==='everyone';const z=shot.zoom*(reveal?1.04-p*.04:1+p*(emotional?.018:.035));
 const x=Math.max(800/z,Math.min(1600-800/z,shot.x+(shot.mode==='medium'?(p-.5)*50:0)));const y=Math.max(380/z,Math.min(760-380/z,shot.mode==='medium'||shot.mode==='over'||(shot.mode==='portrait'&&shot.chapter===9)?340:shot.y));
 const topTitle=['requirements','diploma'].includes(beat.tag)?'YÊU CẦU CẤP BẰNG':beat.tag==='tests'?'BÀI KIỂM TRA KIẾN THỨC':beat.tag==='design'?'THIẾT KẾ. THỬ NGHIỆM.':beat.tag==='evidence'?'BẰNG CHỨNG TRƯỚC KẾT LUẬN':'GHI CHÉP NGHIÊN CỨU';
 const topItems=['requirements','diploma'].includes(beat.tag)?['Hoàn thành chương trình','Đạt yêu cầu kiểm tra','Tuân thủ thủ tục cấp bằng']:beat.tag==='tests'?['Toán học nâng cao','Phân tích và lập luận','Trình bày lời giải']:beat.tag==='design'?['Xác định nhu cầu','Phác thảo giải pháp','Thử nghiệm mẫu thiết kế']:['Xác định vấn đề','Đối chiếu bằng chứng','Thử ý tưởng tiếp theo'];
 const face=['zero','uncertainty','risk','fake'].includes(beat.tag)?'shock':['privacy','forget','exhausted','regret','journey','unhappy'].includes(beat.tag)?'sad':'calm';
 const opening=shot.chapter===0&&shot.localFrom===0?Math.min(1,f/12):1;
 const final=shot.chapter===9&&beat.tag==='final';const ending=final?Math.min(1,(TOTAL-(shot.from+f))/30):1;
 return <AbsoluteFill style={{background:'#080f1d',opacity:Math.min(opening,ending)}}><svg viewBox="0 0 1600 760" style={{position:'absolute',left:0,top:66,width:1920,height:912,overflow:'hidden'}}>
 <defs><radialGradient id="camera-shade"><stop offset=".3" stopColor="#030a18" stopOpacity="0"/><stop offset="1" stopColor="#030a18" stopOpacity=".42"/></radialGradient></defs>
 {shot.mode==='portrait'&&shot.chapter!==9?<><Room office={shot.chapter<8}/><rect width="1600" height="760" fill={emotional?'#633e32':'#11263a'} opacity={emotional?.18:.35}/><g transform={`translate(800 380) scale(${1+p*.025}) translate(-800 -380)`}><Stan x={800} y={1030} s={2.55} t={t} face={face}/></g></>:shot.mode==='top'?<><rect width="1600" height="760" fill="#7e6856"/>{[0,1,2,3,4,5,6].map(i=><path key={i} d={`M${i*270-200} 0l180 760`} stroke="#4e4541" strokeWidth="3" opacity=".4"/>)}<g transform={`translate(800 370) rotate(${-5+p*3})`}><rect x="-390" y="-240" width="780" height="480" rx="10" fill={C.cream}/><Label text={topTitle} width={690} x={0} y={-150} size={36} color={C.ink}/>{topItems.map((text,i)=><g key={i}><rect x="-310" y={-80+i*80} width="25" height="25" fill="none" stroke="#718a81" strokeWidth="4"/><text x="-260" y={-58+i*80} fontFamily="Arial" fontSize="38" fill={C.ink}>{viLabel(text)}</text></g>)}<path d={`M230 ${110+Math.sin(t*.1)*8}l100 -100`} stroke={C.gold} strokeWidth="14"/></g></>:<g transform={`translate(800 380) scale(${z}) translate(${-x} ${-y})`}><World id={shot.chapter} t={t}/></g>}
 {shot.mode==='over'&&<path d="M-30 760v-420q50 -90 100 -50q-70 -100 -10 -170l-15 -30 40 12 10 -38 30 28 35 -20 20 40q90 60 20 165q120 50 145 483Z" fill="#0b1422" opacity=".82"/>}
 {Array.from({length:8},(_,i)=><circle key={i} cx={(i*317+f*.12)%1600} cy={(i*137+f*.06)%760} r={1+i%3} fill={C.cream} opacity=".035"/>)}
 <rect width="1600" height="760" fill="url(#camera-shade)"/>
 {shot.chapter===8&&['memory','frustration','aha'].includes(beat.tag)&&<rect width="1600" height="760" fill="#e5c294" opacity={.07+.03*Math.sin(f/90)}/>}
 </svg></AbsoluteFill>;
};
