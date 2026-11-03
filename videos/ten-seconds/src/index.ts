import React from 'react';
import {Composition,registerRoot} from 'remotion';
import {Film,TOTAL} from './Film';
registerRoot(()=>React.createElement(Composition,{id:'TenSeconds',component:Film,durationInFrames:TOTAL,fps:30,width:1920,height:1080,defaultProps:{bgm:true}}));
