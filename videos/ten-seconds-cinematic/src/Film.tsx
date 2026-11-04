import React from 'react';
import {AbsoluteFill,Audio,Sequence,staticFile,useCurrentFrame} from 'remotion';
import shots from './shots.json';
import captions from './captions.json';
import scenes from './timeline.json';
import {CinematicShot} from './Cinematic';
export const TOTAL=scenes.reduce((n,s)=>n+s.duration,0);export {shots,captions,scenes};
export const ShortCaption:React.FC<{caption:typeof captions[number]}>=({caption})=>{
 const f=useCurrentFrame();const textWords=caption.text.split(/\s+/);const keywords=/future|seconds|life|mom|ten|10|choice|courage|present|change|now|love|save|fixed/i;
 return <AbsoluteFill style={{justifyContent:'flex-end',alignItems:'center',paddingBottom:24,pointerEvents:'none'}}><div style={{maxWidth:1690,textAlign:'center',fontFamily:'Arial,sans-serif',fontWeight:800,fontSize:78,lineHeight:1.2,letterSpacing:-.7,color:'#fff9ec',WebkitTextStroke:'2px #0a1423',paintOrder:'stroke fill',textShadow:'0 3px 6px #000, 0 0 3px #000'}}>{textWords.map((w,i)=>{const a=caption.words[Math.min(i,caption.words.length-1)];const active=f>=a.from&&f<a.to;return <React.Fragment key={i}><span style={{color:keywords.test(w)?'#f5cd77':active?'#b8e9e0':'#fff9ec'}}>{w}</span>{i<textWords.length-1?' ':''}</React.Fragment>})}</div></AbsoluteFill>;
};
export const Film:React.FC<{bgm?:boolean;withAudio?:boolean}>=({bgm=true,withAudio=true})=><AbsoluteFill style={{background:'#080f1d'}}>{shots.map(s=><Sequence key={s.id} from={s.from} durationInFrames={s.duration}><CinematicShot shot={s}/></Sequence>)}{captions.map(c=><Sequence key={c.id} from={c.from} durationInFrames={c.duration}><ShortCaption caption={c}/></Sequence>)}{withAudio&&<Audio src={staticFile(bgm?'audio/master.flac':'audio/narration.flac')}/>}</AbsoluteFill>;
