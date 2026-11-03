import {Film,SCENES,TOTAL,Caption} from './Film';
import {Scene} from './Scenes';
export const WORKBENCH={name:'Ten Seconds · narrative film',fps:30,width:1920,height:1080,total:TOTAL,background:'#101b2b',revision:'1',
shots:SCENES.map(sc=>({id:`scene-${sc.id}`,label:sc.title,from:sc.from,duration:sc.duration,component:Scene,props:{id:sc.id,title:sc.title,label:sc.label,duration:sc.duration},durationProp:'duration',cardId:`scene-${sc.id}`,schema:[{type:'text',key:'title',label:'Title',default:sc.title}]})),
captions:SCENES.flatMap(sc=>sc.captions.map((c,i)=>({id:`caption-${sc.id}-${i}`,from:sc.from+c.from,duration:Math.min(c.duration,sc.duration-c.from),component:Caption,props:{text:c.text,duration:c.duration},durationProp:'duration',schema:[{type:'textarea',key:'text',label:'Subtitle',default:c.text}]}))),
sfx:[{from:0,duration:TOTAL,src:'audio/narration.flac',volume:1}],bgm:[{from:0,duration:TOTAL,src:'audio/score.flac',volume:1}],original:Film};
