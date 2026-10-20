import { useEffect, useRef, useState } from 'react';
import { WELCOME_FEATURES } from './features';
const DWELL=7000, SLIDE=1150;
export function WelcomeFeatureGuide({onNavigate, paused=false}) {
  const [index,setIndex]=useState(0),[sliding,setSliding]=useState(false),[held,setHeld]=useState(false);
  const elapsed=useRef(0),phase=useRef(false);
  useEffect(()=>{
    if(paused||held){elapsed.current=0;phase.current=false;setSliding(false);return;}
    let last=performance.now();
    const timer=setInterval(()=>{
      const now=performance.now(),dt=now-last;last=now;if(document.hidden)return;
      elapsed.current+=Math.min(dt,150);
      if(elapsed.current>=(phase.current?SLIDE:DWELL)){
        elapsed.current=0;
        if(phase.current){setIndex(i=>(i+1)%WELCOME_FEATURES.length);setSliding(false);phase.current=false;}
        else{setSliding(true);phase.current=true;}
      }
    },50);return()=>clearInterval(timer);
  },[paused,held]);
  function move(delta){elapsed.current=0;phase.current=false;setSliding(false);setIndex(i=>(i+delta+WELCOME_FEATURES.length)%WELCOME_FEATURES.length);}
  const current=WELCOME_FEATURES[index],next=WELCOME_FEATURES[(index+1)%WELCOME_FEATURES.length];
  return <section className="welcome-feature-guide" aria-label="Things to explore and what’s coming" data-sliding={sliding} onPointerEnter={()=>setHeld(true)} onPointerLeave={()=>setHeld(false)} onFocusCapture={()=>setHeld(true)} onBlurCapture={e=>{if(!e.currentTarget.contains(e.relatedTarget))setHeld(false);}}>
    <div className="welcome-feature-window"><div className={`welcome-feature-strip ${sliding?'is-sliding':''}`}>
      {[current,next].map((feature,i)=><button type="button" key={`${feature.id}-${i}`} tabIndex={i===0?0:-1} aria-hidden={i===1?true:undefined} className="welcome-feature-item" onClick={()=>onNavigate(feature.destination)}><span className="welcome-feature-status">{feature.status}</span><span>{feature.description}</span><span aria-hidden="true">↗</span></button>)}
    </div></div><div className="welcome-feature-steppers"><button type="button" aria-label="Previous feature" onClick={()=>move(-1)}>⌃</button><button type="button" aria-label="Next feature" onClick={()=>move(1)}>⌄</button></div>
  </section>;
}
