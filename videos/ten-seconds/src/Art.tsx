import React from 'react';
export const C={ink:'#101b2b',navy:'#223449',teal:'#78d6cf',cream:'#f5eddb',coral:'#ef7868',gold:'#e9b68a',dim:'#8295a3'};
export const Person:React.FC<{x:number;y:number;s?:number;pose?:string;face?:string;color?:string;flip?:boolean;phase?:number;elder?:boolean}>=({x,y,s=1,pose='stand',face='calm',color=C.teal,flip=false,phase=0,elder=false})=>{
 const walk=pose==='walk'||pose==='run';const a=walk?Math.sin(phase)*24:0;const bend=pose==='fall'?65:pose==='save'?-20:0;const outfit=color===C.teal?'#29455f':color;const edge='#172333';
 const arm=pose==='save'||pose==='rescue'?'M-29 -193 L-69 -159 L-112 -176 M29 -193 L73 -174 L115 -183':pose==='phone'?'M-30 -191 L-45 -153 L-63 -212 M30 -191 L50 -146 L70 -155':pose==='point'?'M-29 -193L-43 -137 M29 -193L73 -203L118 -203':`M-29 -193L${-46-a} -147L${-49-a} -116 M29 -193L${46+a} -147L${49+a} -116`;
 const hands=pose==='save'||pose==='rescue'?[[-112,-176],[115,-183]]:pose==='phone'?[[-63,-212],[70,-155]]:pose==='point'?[[-43,-137],[118,-203]]:[[-49-a,-116],[49+a,-116]];
 return <g transform={`translate(${x} ${y}) scale(${flip?-s:s} ${s}) rotate(${bend})`} strokeLinecap="round" strokeLinejoin="round">
 <ellipse cx="0" cy="8" rx="57" ry="12" fill="#172333" opacity=".16"/>
 <path d={`M-17 -100 L${-20+a} -47 L${-30-a} 0 M17 -100 L${20-a} -48 L${30+a} 0`} fill="none" stroke={edge} strokeWidth="23"/>
 <path d={`M${-35-a} 0h33 M${15+a} 0h33`} stroke={edge} strokeWidth="17"/>
 <path d={`M${-35-a} -1h33 M${15+a} -1h33`} stroke="#e5e8e4" strokeWidth="11"/>
 <path d={`M${-31-a} -6l5 5m4 -5l5 5 M${19+a} -6l5 5m4 -5l5 5`} stroke="#78919b" strokeWidth="2"/>
 <path d={arm} fill="none" stroke={edge} strokeWidth="24"/><path d={arm} fill="none" stroke={outfit} strokeWidth="17"/>
 {hands.map(([hx,hy],i)=><ellipse key={i} cx={hx} cy={hy} rx="11" ry="8" fill="#fffef5" stroke={edge} strokeWidth="2.5"/>)}
 <path d="M-29 -205Q-44 -225 -18 -231H18Q44 -225 29 -205" fill={outfit} stroke={edge} strokeWidth="3"/>
 <path d="M-29 -205 Q0 -215 29 -205 L38 -106 Q0 -96 -38 -106Z" fill={outfit} stroke={edge} strokeWidth="3.5"/>
 <path d="M-11 -207L-9 -176 M11 -207L9 -176" stroke="#c8d7d7" strokeWidth="2.5"/>
 <path d="M-20 -143h40l8 23h-56Z" fill="none" stroke={edge} strokeWidth="3"/>
 <path d="M-34 -114q34 8 68 0" fill="none" stroke="#587287" strokeWidth="3"/>
 <path d="M-10 -220v-15h23v15" fill="#fffef5" stroke={edge} strokeWidth="3"/>
 <ellipse cy="-261" rx="44" ry="49" fill="#fffef5" stroke={edge} strokeWidth="3.5"/>
 <path d={elder?'M-44 -268Q-50 -312 -7 -317Q42 -324 47 -278L36 -276L29 -297L8 -301L-20 -293L-35 -273Z':'M-45 -278L-55 -291L-37 -290L-47 -309L-24 -303L-21 -325L-5 -313L8 -332L15 -310L37 -322L35 -302L57 -300L39 -285L47 -275L28 -281L20 -292L9 -283L0 -291L-12 -280L-27 -285L-38 -269Z'} fill={elder?'#a8b0b5':edge} stroke={edge} strokeWidth="2"/>
 <path d="M-26 -275l16 -2M10 -277l16 2" stroke={edge} strokeWidth="3"/>
 {face==='blink'?<path d="M-21 -260h10 M11 -260h10" stroke={edge} strokeWidth="3"/>:<><ellipse cx="-15" cy="-261" rx="3.5" ry="8" fill={edge}/><ellipse cx="16" cy="-261" rx="3.5" ry="8" fill={edge}/></>}
 <path d={face==='sad'?'M-10 -237q10 -9 20 0':face==='shock'?'M-5 -244q10 -7 10 4q-6 9 -10 -4':'M-10 -244q10 12 20 0'} fill="none" stroke={edge} strokeWidth="2.8"/>
 {pose==='phone'&&<rect x="-77" y="-231" width="19" height="38" rx="4" fill={edge} stroke="#fffef5" strokeWidth="2"/>}
 </g>;
};
export const Skyline:React.FC<{night?:boolean;warm?:boolean}>=({night=false,warm=false})=><g>
 <rect width="1600" height="760" fill={warm?'#d99d80':night?'#18263e':'#bac9c5'}/>
 <circle cx={warm?1210:1230} cy={warm?260:115} r={warm?125:65} fill={warm?'#f7d39c':C.cream} opacity=".85"/>
 {[0,1,2,3,4,5,6,7,8,9,10,11].map(i=><g key={i}><rect x={i*150-40} y={230+(i*71)%130} width={110+(i%3)*16} height="460" fill={night?'#263951':'#859e9e'}/>{[0,1,2].map(j=><g key={j}><rect x={i*150-15} y={280+(i*71)%130+j*65} width="17" height="25" fill={night?C.gold:'#dce4d9'} opacity=".7"/><rect x={i*150+25} y={280+(i*71)%130+j*65} width="17" height="25" fill={night?C.gold:'#dce4d9'} opacity=".7"/></g>)}</g>)}
 <rect y="575" width="1600" height="185" fill={night?'#172234':'#dbd6c7'}/><path d="M0 655h1600" stroke={night?'#526278':'#b4b7ad'} strokeWidth="3"/>
 </g>;
export const Cup:React.FC<{x:number;y:number;angle?:number}>=({x,y,angle=0})=><g transform={`translate(${x} ${y}) rotate(${angle})`}><path d="M-21 -35h42L15 22h-30Z" fill={C.cream}/><rect x="-26" y="-42" width="52" height="10" rx="4" fill={C.ink}/><path d="M-19 -15h38v19h-38Z" fill={C.coral}/></g>;
export const Phone:React.FC<{x:number;y:number;s?:number;angle?:number;calling?:boolean}>=({x,y,s=1,angle=0,calling=false})=><g transform={`translate(${x} ${y}) scale(${s}) rotate(${angle})`}><rect x="-75" y="-132" width="150" height="264" rx="22" fill={C.ink} stroke={C.dim} strokeWidth="4"/><rect x="-66" y="-115" width="132" height="230" rx="13" fill={calling?'#31495a':'#76bdb8'}/><rect x="-24" y="-122" width="48" height="8" rx="4" fill={C.ink}/>{calling?<><circle cy="-50" r="30" fill={C.gold}/><text y="10" textAnchor="middle" fill={C.cream} fontSize="20" fontFamily="sans-serif">MOM</text><text y="35" textAnchor="middle" fill={C.cream} fontSize="12" fontFamily="sans-serif">calling…</text><circle cx="-32" cy="79" r="18" fill={C.coral}/><circle cx="32" cy="79" r="18" fill={C.teal}/><path d="M-40 79h16M26 83l12 -9" stroke={C.cream} strokeWidth="4"/></>:<><circle cy="-20" r="29" fill={C.cream} opacity=".65"/><path d="M-40 45h80M-40 63h55" stroke={C.cream} strokeWidth="6"/></>}</g>;
export const Car:React.FC<{x:number;y:number;truck?:boolean;sy?:number;flip?:boolean}>=({x,y,truck=false,sy=1,flip=false})=><g transform={`translate(${x} ${y}) scale(${flip?-1:1} ${sy})`}><path d={truck?'M-160 -142h210v112h-210Z M50 -103h72l55 60v55H50Z':'M-160 -63l45 -62H20l74 59 56 13v66h-310Z'} fill={C.coral}/><path d={truck?'M62 -90h50l36 43H62Z':'M-101 -111H9l49 44h-186Z'} fill="#263d51"/><circle cx="-100" cy="12" r="31" fill={C.ink}/><circle cx="100" cy="12" r="31" fill={C.ink}/><circle cx="-100" cy="12" r="13" fill={C.dim}/><circle cx="100" cy="12" r="13" fill={C.dim}/><path d="M142 -32h16" stroke={C.cream} strokeWidth="12"/></g>;
export const Room:React.FC<{office?:boolean}>=({office=false})=><g><rect width="1600" height="760" fill="#b9c6be"/><rect x="70" y="55" width="520" height="360" rx="6" fill="#e2e7d9"/><path d="M330 55v360M70 235h520" stroke="#8da6a3" strokeWidth="14"/><rect x="1040" y="70" width="410" height="265" rx="4" fill={C.navy}/>{office?<><path d="M1090 260l65 -70 65 25 100 -90 75 25" stroke={C.teal} strokeWidth="10" fill="none"/><path d="M1080 300h300" stroke={C.dim} strokeWidth="3"/></>:<><circle cx="1245" cy="190" r="80" fill={C.gold}/><path d="M1140 290l120 -130 140 130" fill={C.teal}/></>}<rect y="560" width="1600" height="200" fill="#d8c9b2"/><path d="M0 560h1600" stroke="#9ca89d" strokeWidth="3"/><path d="M1470 565V375M1470 470q-115 -95 -95 -140q100 0 95 140M1470 500q100 -90 95 -140q-95 0 -95 140" fill="#567d73" stroke="#567d73" strokeWidth="9"/><path d="M1424 550h90l-18 100h-55Z" fill={C.coral}/></g>;
export const Balloon:React.FC<{x:number;y:number;text:string;w?:number}>=({x,y,text,w=400})=><g transform={`translate(${x} ${y})`}><rect width={w} height="92" rx="18" fill={C.cream}/><path d="M38 92l-12 28 55 -28" fill={C.cream}/><text x={w/2} y="56" fontFamily="sans-serif" fontSize="25" textAnchor="middle" fill={C.ink}>{text}</text></g>;
