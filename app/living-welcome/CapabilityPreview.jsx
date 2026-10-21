import { useEffect, useState } from 'react';
/** Animated, source-bound captures of the actual Explorer. Never a live feed. */
export function CapabilityPreview({ demo, paused = false, className = '' }) {
 const [hidden,setHidden]=useState(()=>typeof document!=='undefined'&&document.hidden);
 const [failed,setFailed]=useState(null);
 useEffect(()=>{const sync=()=>setHidden(document.hidden);document.addEventListener('visibilitychange',sync);return()=>document.removeEventListener('visibilitychange',sync);},[]);
 if(!demo)return null;
 const moving=!paused&&!hidden&&failed!==demo.id;
 return <figure className={`capability-preview ${className}`} data-demo={demo.id} data-moving={moving}>
  {/* eslint-disable-next-line @next/next/no-img-element -- Keep animation bytes and still fallback unmodified; load only the selected capture. */}
  <img key={`${demo.id}-${moving}`} src={moving?demo.animation:demo.poster} alt={demo.title} decoding="async" onError={()=>setFailed(demo.id)} />
  <figcaption><span className="capability-preview-label">{demo.context?'CONTEXT PREVIEW':'EXPLORER CAPTURE'} · {moving?'ANIMATION':'STILL'}</span><strong>{demo.title}</strong><span>{demo.sourceTime}</span>{demo.context&&<span>{demo.context}</span>}<small>{demo.limitation}</small>{failed===demo.id&&<span role="status">Animation unavailable; showing the captured still.</span>}</figcaption>
 </figure>;
}
