import { useEffect, useState } from 'react';
import { motionClip } from './motion-catalog.mjs';
import { MotionClip } from './MotionClip.jsx';
export function ScenePreview({category,index,paused}){
  const clip=motionClip(category,index),[held,setHeld]=useState(false),[hidden,setHidden]=useState(()=>typeof document!=='undefined'&&document.hidden);
  useEffect(()=>setHeld(false),[clip.id]);
  useEffect(()=>{const change=()=>setHidden(document.hidden);document.addEventListener('visibilitychange',change);return()=>document.removeEventListener('visibilitychange',change);},[]);
  return <div className="scene-preview" data-scene={clip.id}>
    <div className="scene-preview-visual" style={{'--scene-aspect':clip.width/clip.height}}><MotionClip clip={clip} paused={paused||held||hidden} showStatus/></div>
    <div className="scene-preview-caption"><div><strong>{clip.action}</strong><small>{clip.context}</small><a href={clip.sourceUrl} target="_blank" rel="noreferrer">Source &amp; credits · {clip.license}</a>{clip.historicalSourceUrl&&<a href={clip.historicalSourceUrl} target="_blank" rel="noreferrer">Read this Kansas story ↗</a>}</div><button type="button" disabled={paused} aria-label={held?'Play scene preview':'Pause scene preview'} aria-pressed={held} onClick={()=>setHeld(v=>!v)}><span aria-hidden="true">{held?'▶':'Ⅱ'}</span></button></div>
  </div>;
}
