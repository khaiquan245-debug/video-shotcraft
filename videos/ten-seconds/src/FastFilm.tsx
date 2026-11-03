import React from 'react';
import {AbsoluteFill,Audio,Freeze,staticFile,useCurrentFrame} from 'remotion';
import {Film,TOTAL} from './Film';
export const SPEED=1.1;
export const FAST_TOTAL=Math.round(TOTAL/SPEED);
export const FastFilm:React.FC<{bgm?:boolean}>=({bgm=true})=>{
 const frame=useCurrentFrame();
 return <AbsoluteFill><Freeze frame={Math.min(TOTAL-1,Math.floor(frame*SPEED))}><Film withAudio={false}/></Freeze><Audio src={staticFile(bgm?'audio/master-fast.flac':'audio/narration-fast.flac')}/></AbsoluteFill>;
};
