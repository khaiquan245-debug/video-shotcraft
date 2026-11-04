import React from 'react';
import {Film,TOTAL,shots,captions,ShortCaption} from './Film';
import {CameraShot,Shot} from './Camera';
import cues from './sfx-cues.json';
const ShotUnit:React.FC<{shot:Shot;duration?:number}>=({shot,duration=shot.duration})=>React.createElement(CameraShot,{shot:{...shot,duration}});
const CaptionUnit:React.FC<{caption:typeof captions[number];text?:string}>=({caption,text=caption.text})=>React.createElement(ShortCaption,{caption:{...caption,text}});
export const WORKBENCH={name:'Learn100× Faster · complete English film',fps:30,width:1920,height:1080,total:TOTAL,background:'#080f1d',revision:'learn100-1',
shots:shots.map(s=>({id:`shot-${s.id}`,label:`${s.chapter+1} · ${s.tag} · ${s.mode}`,from:s.from,duration:s.duration,component:ShotUnit,props:{shot:s,duration:s.duration},durationProp:'duration',cardId:`shot-${s.mode}`,schema:[]})),
captions:captions.map(c=>({id:`caption-${c.id}`,from:c.from,duration:c.duration,component:CaptionUnit,props:{caption:c,text:c.text},cardId:'spoken-caption',schema:[{type:'textarea',key:'text',label:'Subtitle',default:c.text}]})),
sfx:[{from:0,duration:TOTAL,src:'audio/voice.flac',volume:1},...cues.map((c,i)=>({from:Math.round(c.fromSeconds*30),duration:Math.ceil(c.duration*30),src:c.source,volume:c.gain}))],
bgm:[{from:0,duration:TOTAL,src:'audio/score.flac',volume:1}],original:Film};
