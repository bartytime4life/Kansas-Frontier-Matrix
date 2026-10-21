import { useEffect, useState } from 'react';
import { WELCOME_FEATURES } from './features';
const DWELL=7000, SLIDE=1150;
export function WelcomeFeatureGuide({onNavigate, paused=false}) {
  const [index,setIndex]=useState(0),[sliding,setSliding]=useState(false);
  const [pointerHeld,setPointerHeld]=useState(false),[focusHeld,setFocusHeld]=useState(false);
  const held=pointerHeld||focusHeld;
  const [cycle,setCycle]=useState(0);
  const stopped=paused||held;
  const [wasStopped,setWasStopped]=useState(stopped);
  if(wasStopped!==stopped){setWasStopped(stopped);setSliding(false);}
  useEffect(()=>{
    let timer,disposed=false;
    const cancel=()=>{clearTimeout(timer);timer=undefined;};
    // CSS animates the slide. JavaScript only wakes at its two deadlines;
    // hidden tabs have no timer and resume with a complete reading interval.
    const restart=()=>{
      cancel();setSliding(false);
      if(disposed||paused||held||document.hidden)return;
      timer=setTimeout(()=>{
        if(disposed||document.hidden)return;
        setSliding(true);
        timer=setTimeout(()=>{
          if(disposed||document.hidden)return;
          setIndex(i=>(i+1)%WELCOME_FEATURES.length);restart();
        },SLIDE);
      },DWELL);
    };
    document.addEventListener('visibilitychange',restart);restart();
    return()=>{disposed=true;cancel();document.removeEventListener('visibilitychange',restart);};
  },[paused,held,cycle]);
  function move(delta){setCycle(value=>value+1);setSliding(false);setIndex(i=>(i+delta+WELCOME_FEATURES.length)%WELCOME_FEATURES.length);}
  const current=WELCOME_FEATURES[index],next=WELCOME_FEATURES[(index+1)%WELCOME_FEATURES.length];
  return <section className="welcome-feature-guide" aria-label="Things to explore and what’s coming" data-sliding={sliding} onPointerEnter={()=>setPointerHeld(true)} onPointerLeave={()=>setPointerHeld(false)} onPointerCancel={()=>setPointerHeld(false)} onFocusCapture={()=>setFocusHeld(true)} onBlurCapture={e=>{if(!e.currentTarget.contains(e.relatedTarget))setFocusHeld(false);}}>
    <div className="welcome-feature-window"><div className={`welcome-feature-strip ${sliding?'is-sliding':''}`}>
      {[current,next].map((feature,i)=><button type="button" key={`${feature.id}-${i}`} tabIndex={i===0?0:-1} aria-hidden={i===1?true:undefined} className="welcome-feature-item" onClick={()=>onNavigate(feature.destination)}><span className="welcome-feature-status">{feature.status}</span><span>{feature.description}</span><span aria-hidden="true">↗</span></button>)}
    </div></div><div className="welcome-feature-steppers"><button type="button" aria-label="Previous feature" onClick={()=>move(-1)}>⌃</button><button type="button" aria-label="Next feature" onClick={()=>move(1)}>⌄</button></div>
  </section>;
}
