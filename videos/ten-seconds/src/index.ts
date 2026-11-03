import React from 'react';
import {Composition,registerRoot} from 'remotion';
import {Film,TOTAL} from './Film';
import {FastFilm,FAST_TOTAL} from './FastFilm';
registerRoot(()=>React.createElement(React.Fragment,null,
 React.createElement(Composition,{id:'TenSeconds',component:Film,durationInFrames:TOTAL,fps:30,width:1920,height:1080,defaultProps:{bgm:true,withAudio:true}}),
 React.createElement(Composition,{id:'TenSecondsFast',component:FastFilm,durationInFrames:FAST_TOTAL,fps:30,width:1920,height:1080,defaultProps:{bgm:true}})
));
