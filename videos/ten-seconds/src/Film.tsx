import React from 'react';
import {AbsoluteFill,Audio,Sequence,staticFile,useCurrentFrame,interpolate} from 'remotion';
import scenes from './timeline.json';
import {Scene} from './Scenes';
import {C} from './Art';
export const SCENES=scenes;
export const TOTAL=14400;
export const Caption:React.FC<{text?:string;duration?:number}>=({text='',duration=90})=>{const f=useCurrentFrame();return <AbsoluteFill style={{justifyContent:'flex-end',alignItems:'center',paddingBottom:54,opacity:interpolate(f,[0,3,duration-2,duration],[0,1,1,0],{extrapolateLeft:'clamp',extrapolateRight:'clamp'}),pointerEvents:'none'}}><div style={{maxWidth:1650,background:'#101b2bf2',padding:'10px 26px',borderRadius:9,fontFamily:'Arial,sans-serif',fontSize:64,lineHeight:1.18,textAlign:'center',color:C.cream,boxShadow:'0 2px 12px #0002'}}>{text}</div></AbsoluteFill>};
export const Film:React.FC<{bgm?:boolean}>=({bgm=true})=><AbsoluteFill style={{background:C.ink}}>
{scenes.map(sc=><Sequence key={sc.id} from={sc.from} durationInFrames={sc.duration}><Scene {...sc}/></Sequence>)}
{scenes.flatMap(sc=>sc.captions.map((c,i)=><Sequence key={`${sc.id}-${i}`} from={sc.from+c.from} durationInFrames={Math.min(c.duration,sc.duration-c.from)}><Caption text={c.text} duration={c.duration}/></Sequence>))}
<Audio src={staticFile(bgm?'audio/master.flac':'audio/narration.flac')}/>
</AbsoluteFill>;
