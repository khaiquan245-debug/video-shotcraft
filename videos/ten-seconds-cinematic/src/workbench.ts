import React from 'react';
import {Film,TOTAL,shots,captions,ShortCaption} from './Film';
import {CinematicShot,Shot} from './Cinematic';
const ShotUnit:React.FC<{shot:Shot;duration?:number;text?:string}>=({shot,duration=shot.duration,text=shot.text})=>React.createElement(CinematicShot,{shot:{...shot,duration,text}});
const CaptionUnit:React.FC<{caption:typeof captions[number];text?:string}>=({caption,text=caption.text})=>React.createElement(ShortCaption,{caption:{...caption,text}});
export const WORKBENCH={name:'Ten Seconds · cinematic reference edition',fps:30,width:1920,height:1080,total:TOTAL,background:'#080f1d',revision:'cinematic-1',
 shots:shots.map(s=>({id:`shot-${s.id}`,label:`${String(s.id+1).padStart(2,'0')} · ${s.mode} · ${s.phrase||'Opening'}`,from:s.from,duration:s.duration,component:ShotUnit,props:{shot:s,duration:s.duration,text:s.text},durationProp:'duration',cardId:`camera-${s.mode}`,schema:s.mode==='concept'?[{type:'textarea',key:'text',label:'Card text',default:s.text}]:[]})),
 captions:captions.map(c=>({id:`caption-${c.id}`,from:c.from,duration:c.duration,component:CaptionUnit,props:{caption:c,text:c.text},cardId:'spoken-caption',schema:[{type:'textarea',key:'text',label:'Subtitle',default:c.text}]})),
 sfx:[{from:0,duration:TOTAL,src:'audio/master.flac',volume:1}],bgm:[],original:Film};
