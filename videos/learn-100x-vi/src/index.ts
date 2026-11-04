import React from 'react';
import {Composition,registerRoot} from 'remotion';
import {Film,TOTAL} from './Film';
const Root=()=>React.createElement(Composition,{id:'Learn100xVI',component:Film,durationInFrames:TOTAL,fps:30,width:1920,height:1080,defaultProps:{bgm:true,withAudio:true}});
registerRoot(Root);
