'use client';
import { useEffect, useLayoutEffect, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import { TOPIC_STRUCTURE } from '../layer-workspaces';
import { capabilityPreviews, capabilityNote } from './capability-catalog.mjs';
import { CapabilityPreview } from './CapabilityPreview.jsx';
import { WelcomeFeatureGuide } from './FeatureGuide.jsx';
import { DomainStage } from './DomainStage.jsx';
import { SCENE_CATALOG, SCENE_LABEL } from './scenes/catalog.mjs';
import { isolateModalBackground } from '../modal-background';

// Reuse the governed navigation taxonomy; a welcome tile does not admit data.
const TOPICS=TOPIC_STRUCTURE.map(t=>({...t,target:t.id,short:t.facets.join(' · '),note:t.limitation}));
// Siblings recede in a wave that starts at the chosen card. All rects are read
// before any write so one pointer entry costs a single layout, not seventeen.
function wake(card){
  const cards=card?.parentElement?.children;if(!cards?.length||!card.getBoundingClientRect)return;
  const rects=[...cards].map(node=>node.getBoundingClientRect()),a=card.getBoundingClientRect(),ax=a.left+a.width/2,ay=a.top+a.height/2;
  rects.forEach((r,i)=>cards[i].style.setProperty('--wake',`${Math.min(180,Math.round(Math.hypot(r.left+r.width/2-ax,r.top+r.height/2-ay)*.14))}ms`));
}
// The card light follows the pointer through CSS variables, at most once per
// frame and without a React render.
let glowFrame=0;
function glow(event){
  if(event.pointerType==='touch')return;
  const card=event.currentTarget,x=event.clientX,y=event.clientY;
  cancelAnimationFrame(glowFrame);
  glowFrame=requestAnimationFrame(()=>{const r=card.getBoundingClientRect();card.style.setProperty('--mx',`${x-r.left}px`);card.style.setProperty('--my',`${y-r.top}px`);});
}
export default function LivingWelcome({onClose,onAction,onMore,onSearch,onTopic,questions,initialRemember=false,onRememberChange,motionEnabled=true,onMotionChange}){
  const root=useRef(null),dialog=useRef(null),trigger=useRef(null),leave=useRef(null);
  const [localRemember,setRemember]=useState(initialRemember),[query,setQuery]=useState('');
  const remember=onRememberChange?initialRemember:localRemember;
  const [reduced,setReduced]=useState(()=>typeof window!=='undefined'&&window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  const [localMotion,setMotion]=useState(motionEnabled),[hidden,setHidden]=useState(()=>typeof document!=='undefined'&&document.hidden);
  const [active,setActive]=useState(null),[pinned,setPinned]=useState(null),[last,setLast]=useState('weather');
  const [beat,setBeat]=useState({id:null,index:0}),[detail,setDetail]=useState(null),[panel,setPanel]=useState(null),[item,setItem]=useState(0),[fullscreen,setFullscreen]=useState(false);
  const motion=onMotionChange?motionEnabled:localMotion;
  const paused=!motion||reduced||hidden,engaged=pinned||active,control=engaged||last;
  const topic=TOPICS.find(t=>t.id===detail),modal=Boolean(detail||panel);
  const run=action=>{action?.();onClose(remember);};
  function engage(id){clearTimeout(leave.current);setActive(id);setLast(id);}
  function release(){clearTimeout(leave.current);leave.current=setTimeout(()=>{const keyboardFocus=root.current?.querySelector('.topic-callout:focus-visible');const pointerHover=window.matchMedia('(hover: hover) and (pointer: fine)').matches&&root.current?.querySelector('.topic-callout:hover');if(!keyboardFocus&&!pointerHover)setActive(null);},180);}
  function openTopic(id){trigger.current=document.activeElement;setItem(0);setDetail(id);setPanel(null);setFullscreen(false);}
  function openPanel(name){trigger.current=document.activeElement;setDetail(null);setPanel(name);}
  function closePanel(){setDetail(null);setPanel(null);}
  function pin(id){setPinned(id);setActive(null);setLast(id);closePanel();}
  function feature(destination){if(destination==='sources')openPanel('data');else run(()=>onTopic(destination));}
  useEffect(()=>{
    const media=window.matchMedia('(prefers-reduced-motion: reduce)'),change=()=>setReduced(media.matches),visibility=()=>setHidden(document.hidden);
    media.addEventListener('change',change);document.addEventListener('visibilitychange',visibility);
    return()=>{media.removeEventListener('change',change);document.removeEventListener('visibilitychange',visibility);clearTimeout(leave.current);};
  },[]);
  // The lazy visual replaces a focused fallback. Restore focus and install its
  // keyboard owner before paint, so a fast Tab/Escape cannot fall between them.
  useLayoutEffect(()=>{root.current?.querySelector('[data-guide-autofocus]')?.focus({preventScroll:true});},[]);
  // Nested dialogs need the same before-paint handoff when opening and closing;
  // otherwise a quick second Escape can arrive while focus is on the body.
  useLayoutEffect(()=>{
    if(!modal){const target=trigger.current;trigger.current=null;if(target?.isConnected)target.focus({preventScroll:true});return;}
    const node=dialog.current,restore=isolateModalBackground(node,document.body);
    node?.querySelector('button,a,input')?.focus({preventScroll:true});
    return restore;
  },[modal]);
  useLayoutEffect(()=>{
    const keyboard=event=>{
      if(!root.current?.contains(event.target)&&!dialog.current?.contains(event.target))return;
      if(event.key==='Escape'){
        event.preventDefault();event.stopImmediatePropagation();
        if(modal)closePanel();else if(fullscreen){setFullscreen(false);}else if(pinned){setPinned(null);setActive(null);}else onClose(remember);
      }
      if(event.key==='Tab'&&modal){
        const nodes=[...(dialog.current?.querySelectorAll('button,a[href],input')||[])].filter(n=>!n.disabled&&n.getClientRects().length&&!n.closest('[hidden],[inert]'));
        if(event.shiftKey&&document.activeElement===nodes[0]){event.preventDefault();nodes.at(-1)?.focus();}
        else if(!event.shiftKey&&document.activeElement===nodes.at(-1)){event.preventDefault();nodes[0]?.focus();}
      }
    };document.addEventListener('keydown',keyboard,true);return()=>document.removeEventListener('keydown',keyboard,true);
  },[modal,pinned,fullscreen,remember,onClose]);
  useLayoutEffect(()=>{if(fullscreen&&!modal)root.current?.querySelector('.welcome-preview-expand')?.focus({preventScroll:true});},[fullscreen,modal]);
  const content = <><section className="explorer-guide living-welcome" ref={root} role="dialog" aria-modal="false" aria-labelledby="living-welcome-title" data-renderer="capability" data-active={engaged||null} data-fullscreen={fullscreen} data-motion={paused?'paused':'playing'} data-immersive={Boolean(engaged&&!modal)}>
    <div className="welcome-map-stage">
      <div className="welcome-wash" aria-hidden="true"/>
      <div className="welcome-capability-stage"><DomainStage topic={control} paused={paused||modal} reduced={reduced} onBeat={(id,index)=>setBeat({id,index})}/></div>
      <div className="welcome-heading-row"><div className="welcome-hero">
        <span className="welcome-kicker">KANSAS FRONTIER MATRIX</span>
        <h1 id="living-welcome-title">Kansas is full of <em>stories.</em></h1>
        <p>Explore the skies, the land, and the stories beneath.</p>
        <div className="welcome-hero-actions"><form onSubmit={e=>{e.preventDefault();run(()=>onSearch(query.trim()));}}><label><span aria-hidden="true">⌕</span><span className="sr-only">Find a county or place</span><input data-guide-autofocus="" value={query} onChange={e=>setQuery(e.target.value)} placeholder="Find a county or place" maxLength={180}/></label><button type="submit" className="welcome-primary">Explore <span aria-hidden="true">→</span></button></form><button type="button" className="welcome-ask" onClick={()=>run(()=>onAction('qwen'))}><span aria-hidden="true">✧</span><span><strong>Ask the atlas</strong><small>Start with a question</small></span><span aria-hidden="true">↗</span></button></div>
        <div className="welcome-mobile-guide"><WelcomeFeatureGuide onNavigate={feature} paused={paused}/></div>
      </div>
      <div className="welcome-toolbar" role="group" aria-label="Welcome options"><button type="button" className="welcome-tool" onClick={()=>openPanel('questions')}>All questions &amp; tools</button><button type="button" className="welcome-tool" aria-label={reduced?'Animations off: reduced motion preference':paused?'Play animation':'Pause animation'} disabled={reduced} aria-pressed={!paused} onClick={()=>{const next=!motion;setMotion(next);onMotionChange?.(next);}}><span aria-hidden="true">{paused?'▶':'❚❚'}</span>{reduced?'Reduced motion':paused?'Play animation':'Pause animation'}</button><label className="welcome-tool"><input type="checkbox" checked={remember} onChange={e=>{setRemember(e.target.checked);onRememberChange?.(e.target.checked);}}/> Don’t show on start</label><button type="button" className="welcome-primary" onClick={()=>onClose(remember)}>Explore freely <span aria-hidden="true">→</span></button><button type="button" className="welcome-skip" aria-label="Close quick start" onClick={()=>onClose(remember)}>Skip welcome <span aria-hidden="true">×</span></button></div></div>
      <p className="discovery-hint"><strong>Choose a topic or start with a place.</strong> <span>17 domains · hover to preview, choose one for options and source limits.</span> <button type="button" onClick={()=>openPanel('credits')}>Scene notes</button><span className="discovery-scene" aria-live="polite"><small>{SCENE_LABEL}</small><b key={`${control}-${beat.id===control?beat.index:0}`}>{SCENE_CATALOG[control]?.beats[beat.id===control?beat.index:0]?.[1]}</b></span></p>
      <section className="discovery-field" aria-label="Choose an exploration topic">{TOPICS.map((t,i)=><button type="button" className={`topic-callout topic-${t.id} ${engaged===t.id?'is-active':''}`} key={t.id} style={{'--i':i}} data-color={t.group==='Earth & environment'?'green':'sky'} aria-label={`${t.title}: ${t.short}`} onPointerEnter={e=>{if(e.pointerType!=='touch'){wake(e.currentTarget);engage(t.id);}}} onPointerMove={glow} onPointerLeave={release} onFocus={e=>{if(e?.currentTarget?.matches?.(':focus-visible')!==false){wake(e?.currentTarget);engage(t.id);}}} onBlur={release} onClick={()=>openTopic(t.id)}><span className="topic-light" aria-hidden="true"/><span className="topic-copy"><strong>{t.title}</strong><small>{t.short}</small></span><span className="topic-arrow" aria-hidden="true">→</span></button>)}</section>
      <div className="welcome-scene-deck"><button type="button" className="welcome-preview-expand" aria-pressed={fullscreen} onClick={()=>setFullscreen(v=>!v)}>{fullscreen?'Return to categories':'Expand animation'}</button>{fullscreen&&<button type="button" className="welcome-preview-pause" disabled={reduced} aria-pressed={!paused} onClick={()=>{const next=!motion;setMotion(next);onMotionChange?.(next);}}>{paused?'Play animation':'Pause animation'}</button>}</div>
      
    </div>
  </section>
    {modal&&<div className="living-welcome welcome-dialog-backdrop" onClick={e=>{if(e.target===e.currentTarget)closePanel();}}><section ref={dialog} className="welcome-dialog" role="dialog" aria-modal="true" aria-labelledby="welcome-detail-title"><div className="welcome-dialog-toolbar"><span className="welcome-kicker">EXPLORE KANSAS</span><button type="button" className="welcome-dialog-close" aria-label="Close exploration details" onClick={closePanel}>×</button></div><div className="welcome-dialog-body">
      {topic?<><h2 id="welcome-detail-title">{topic.title}</h2><p>{topic.description}</p><CapabilityPreview demo={capabilityPreviews(topic.id)[item]} paused={paused}/>{!capabilityPreviews(topic.id).length&&<p className="welcome-source-note">{capabilityNote(topic.id)}</p>}<h3>Explore in this workspace</h3><ul className="capability-facets">{topic.facets.map(facet=><li key={facet}>{facet}</li>)}</ul><div className="topic-options" role="group" aria-label={`${topic.title} starting points`}>{capabilityPreviews(topic.id).map((demo,i)=><button type="button" key={demo.id} aria-pressed={item===i} onClick={()=>setItem(i)}>{demo.title}<span aria-hidden="true">{item===i?'✓':'→'}</span></button>)}</div><p className="welcome-source-note">{topic.note}</p><button type="button" className="welcome-primary" onClick={()=>{pin(topic.id);setFullscreen(true);}}>Preview in the welcome window →</button><button type="button" className="welcome-text-action" onClick={()=>run(()=>onTopic(topic.target))}>Explore {topic.title.toLowerCase()} sources →</button>{topic.id==='groundwater'&&<button type="button" className="welcome-text-action" onClick={()=>run(()=>onAction('underground'))}>Open Underground Explorer →</button>}</>:panel==='credits'?<><h2 id="welcome-detail-title">The stories behind the scenes.</h2><p>The scene behind the topics is illustrative: real-time graphics on synthetic terrain that show how each workspace’s tools behave. It is not a map of Kansas, and its gauges, readings, fields and events are not observations.</p><p>Each topic’s details show recorded captures of the actual Explorer, with their original source clocks and limitations. Reused captures are labeled as context; they do not establish additional domain coverage.</p><div className="welcome-footage-credits">{TOPICS.map(t=><article key={t.id}><strong>{t.title}</strong>{capabilityPreviews(t.id).map(d=><div key={d.id}><strong>{d.title}</strong><small>{d.sourceTime}</small><p>{d.limitation}</p>{d.context&&<p>{d.context}</p>}</div>)}{!capabilityPreviews(t.id).length&&<p>{capabilityNote(t.id)}</p>}</article>)}</div></>:panel==='questions'?<><h2 id="welcome-detail-title">Follow your curiosity.</h2><div className="welcome-legacy-questions">{questions}</div></>:<><h2 id="welcome-detail-title">More stories are coming.</h2><p>Explore the available tools today. Additional records appear as their source coverage, dates and review are ready.</p><p className="welcome-source-note">A visual preview does not activate a dataset or establish that it is available. The Explorer’s source controls show current coverage and limitations.</p><button type="button" className="welcome-primary" onClick={()=>run(()=>onAction('layers'))}>Browse the source catalogue →</button><a className="welcome-text-action" href="/observatory/sources">Source observatory ↗</a><button type="button" className="welcome-text-action" onClick={()=>run(onMore)}>Map tools &amp; help →</button></>}
    </div></section></div>}
  </>;
  return createPortal(content,document.querySelector(".site-root")||document.body);
}
