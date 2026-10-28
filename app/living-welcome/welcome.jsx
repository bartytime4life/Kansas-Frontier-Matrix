'use client';
import { useEffect, useLayoutEffect, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import { TOPIC_GROUPS, TOPIC_STRUCTURE } from '../layer-workspaces';
import { CATEGORY_MAPS, categorySceneLabel } from '../category-maps';
import { capabilityPreviews, capabilityNote, categoryGlimpse } from './capability-catalog.mjs';
import { CapabilityPreview } from './CapabilityPreview.jsx';
import { DomainStage } from './DomainStage.jsx';
import { welcomeView } from '../welcome-map-view';
import { isolateModalBackground, modalFocusableElements } from '../modal-background';

// Reuse the governed navigation taxonomy; a welcome tile does not admit data.
const TOPICS=TOPIC_STRUCTURE.map(t=>({...t,target:t.id,short:t.facets.join(' · '),note:t.limitation,look:CATEGORY_MAPS[t.id]}));
// Each card carries a three-colour sketch of the map it opens.
const swatch=look=>look?{'--m0':look.swatch[0],'--m1':look.swatch[1],'--m2':look.swatch[2]}:undefined;
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
export default function LivingWelcome({onClose,onAction,onMore,onSearch,onTopic,onMap,initialRemember=false,motionEnabled=true,onMotionChange}){
  const root=useRef(null),dialog=useRef(null),trigger=useRef(null),leave=useRef(null),wasFullscreen=useRef(false);
  const [remember,setRemember]=useState(initialRemember),[query,setQuery]=useState('');
  const [reduced,setReduced]=useState(()=>typeof window!=='undefined'&&window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  const [localMotion,setMotion]=useState(motionEnabled),[hidden,setHidden]=useState(()=>typeof document!=='undefined'&&document.hidden);
  const [active,setActive]=useState(null),[pinned,setPinned]=useState(null),[last,setLast]=useState('weather');
  const [touched,setTouched]=useState(false),[detail,setDetail]=useState(null),[panel,setPanel]=useState(null),[item,setItem]=useState(0),[fullscreen,setFullscreen]=useState(false);
  const [previewState,setPreviewState]=useState(null),[layersVisible,setLayersVisible]=useState(true);
  const motion=onMotionChange?motionEnabled:localMotion;
  const paused=!motion||reduced||hidden,engaged=pinned||active,control=engaged||last;
  const topic=TOPICS.find(t=>t.id===detail),modal=Boolean(detail||panel),glimpse=categoryGlimpse(control);
  const run=action=>{action?.();onClose(remember);};
  // Leaving the full-window preview clears the engaged card itself: hidden cards can
  // lose focus without a blur event, so release() alone may never run.
  function engage(id){clearTimeout(leave.current);setActive(id);setLast(id);setTouched(true);setLayersVisible(true);}
  function release(){clearTimeout(leave.current);leave.current=setTimeout(()=>{const keyboardFocus=root.current?.querySelector('.topic-callout:focus-visible');const pointerHover=window.matchMedia('(hover: hover) and (pointer: fine)').matches&&root.current?.querySelector('.topic-callout:hover');if(!keyboardFocus&&!pointerHover)setActive(null);},180);}
  function openTopic(id,keepPreview=false){trigger.current=document.activeElement;setItem(0);setDetail(id);setPanel(null);if(!keepPreview)setFullscreen(false);}
  function openPanel(name){trigger.current=document.activeElement;setDetail(null);setPanel(name);}
  function closePanel(){setDetail(null);setPanel(null);}
  function pin(id){setLayersVisible(true);setPinned(id);setActive(null);setLast(id);setTouched(true);closePanel();}
  useEffect(()=>{
    const media=window.matchMedia('(prefers-reduced-motion: reduce)'),change=()=>setReduced(media.matches),visibility=()=>setHidden(document.hidden);
    media.addEventListener('change',change);document.addEventListener('visibilitychange',visibility);
    return()=>{media.removeEventListener('change',change);document.removeEventListener('visibilitychange',visibility);clearTimeout(leave.current);};
  },[]);
  // Install focus and keyboard ownership before paint.
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
        if(modal)closePanel();else if(fullscreen){setFullscreen(false);setPinned(null);setActive(null);}else if(pinned){setPinned(null);setActive(null);}else onClose(remember);
      }
      if(event.key==='Tab'&&modal){
        const nodes=dialog.current?modalFocusableElements(dialog.current):[];
        if(event.shiftKey&&document.activeElement===nodes[0]){event.preventDefault();nodes.at(-1)?.focus();}
        else if(!event.shiftKey&&document.activeElement===nodes.at(-1)){event.preventDefault();nodes[0]?.focus();}
      }
    };document.addEventListener('keydown',keyboard,true);return()=>document.removeEventListener('keydown',keyboard,true);
  },[modal,pinned,fullscreen,remember,onClose]);
  useLayoutEffect(()=>{
    const returning=wasFullscreen.current&&!fullscreen;wasFullscreen.current=fullscreen;
    // Pause disappears on return. Restore the persistent control before the
    // next key, including when Escape was pressed from Pause/Resume itself.
    if(!modal&&(fullscreen||returning))root.current?.querySelector('.welcome-preview-expand')?.focus({preventScroll:true});
  },[fullscreen,modal]);
  const content = <><section className="explorer-guide living-welcome" ref={root} role="dialog" aria-modal="false" aria-labelledby="living-welcome-title" data-renderer="capability" data-active={engaged||null} data-fullscreen={fullscreen} data-motion={paused?'paused':'playing'} data-immersive={Boolean(engaged&&!modal)}>
    <div className="welcome-map-stage">
      <div className="welcome-wash" aria-hidden="true"/>
      <div className="welcome-capability-stage"><DomainStage topic={touched?control:null} layersVisible={layersVisible} paused={paused||modal||(!engaged&&!fullscreen)} reduced={reduced} onPreviewState={setPreviewState}/></div>
      <div className="welcome-heading-row"><div className="welcome-toolbar" role="group" aria-label="Welcome options"><button type="button" className="welcome-tool" aria-label={reduced?'Animations off: reduced motion preference':paused?'Play animation':'Pause animation'} disabled={reduced} onClick={()=>{const next=!motion;setMotion(next);onMotionChange?.(next);}}><span aria-hidden="true">{paused?'▶':'❚❚'}</span>{reduced?'Reduced motion':paused?'Play animation':'Pause animation'}</button><label className="welcome-tool"><input type="checkbox" checked={remember} onChange={e=>{setRemember(e.target.checked);}}/> Don’t show on start</label><button type="button" className="welcome-primary" onClick={()=>onClose(remember)}>Explore freely <span aria-hidden="true">→</span></button><button type="button" className="welcome-skip" aria-label="Close quick start" onClick={()=>onClose(remember)}>Skip welcome <span aria-hidden="true">×</span></button></div><div className="welcome-hero">
        <span className="welcome-kicker">KANSAS FRONTIER MATRIX</span>
        <h1 id="living-welcome-title">Kansas is full of <em>stories.</em></h1>
        <p>Explore the skies, the land, and the stories beneath.</p>
        <div className="welcome-hero-actions"><form onSubmit={e=>{e.preventDefault();run(()=>onSearch(query.trim()));}}><label><span aria-hidden="true">⌕</span><span className="sr-only">Find a county or place</span><input data-guide-autofocus="" value={query} onChange={e=>setQuery(e.target.value)} placeholder="Find a county or place" maxLength={180}/></label><button type="submit" className="welcome-primary">Explore <span aria-hidden="true">→</span></button></form><button type="button" className="welcome-ask" onClick={()=>run(()=>onAction('qwen'))}><span aria-hidden="true">✧</span><span><strong>Ask the atlas</strong><small>Start with a question</small></span><span aria-hidden="true">↗</span></button></div>
      </div>
      <aside className="welcome-preview-brief" aria-label="Category layer glimpse">
        <span className="welcome-kicker">{touched?'INSIDE THIS MAP':'A REAL MAP, READY TO EXPLORE'}</span>
        <h2>{touched?glimpse?.title:'Choose your first glimpse.'}</h2>
        <p>{touched?glimpse?.summary:'Point at a category or focus it to glimpse its map. Select it for a guided demonstration, source notes and an entry into the Explorer.'}</p>
        {touched&&<><p className="welcome-preview-try">{glimpse?.try}</p><div className="welcome-preview-feed-state">{previewState?.mapState==='unavailable'?<span>Map preview unavailable. Open the map to check its source controls.</span>:previewState?.topic!==control?<span>Preparing this category’s map…</span>:previewState.sources.map(source=><span key={source.id} data-state={source.state}><i aria-hidden="true"/>{source.label}: {source.state==='dated-frame'?`${source.product==='visible'?'visible band · ':source.product==='geocolor'?'GeoColor · ':''}${new Date(source.observedAt).toLocaleTimeString('en-US',{timeZone:'America/Chicago',hour:'numeric',minute:'2-digit',timeZoneName:'short'})}`:source.state==='records'?`${source.count} source records`:source.state==='empty'?'No records returned':source.state==='map-layer'?'Provider tile layer':source.state==='hidden'?'Hidden for comparison':source.state==='zoom-in'?'Closer zoom in the opened map':source.state==='unavailable'?'Unavailable':'Loading…'}</span>)}</div><button type="button" className="welcome-text-action" onClick={()=>openTopic(control)}>See this category’s demonstrations <span aria-hidden="true">↗</span></button></>}
      </aside>
      </div>
      <p className="discovery-hint"><strong>Choose a category to open its map, or start with a place.</strong> <span>{TOPICS.length} categories · each opens on a map built for its data.</span> <button type="button" onClick={()=>openPanel('credits')}>Map notes</button><span className="discovery-scene"><small>Map preview</small><b key={touched?control:'kansas'}>{welcomeView(touched?control:null).name}</b></span></p>
      <section className="discovery-field discovery-field--grouped" aria-label="Choose an exploration topic">{TOPIC_GROUPS.map(group=><div className="discovery-group" role="group" aria-label={group} key={group}><h2 className="discovery-group-title">{group}</h2>{TOPICS.map((t,i)=>[t,i]).filter(([t])=>t.group===group).map(([t,i])=><button type="button" className={`topic-callout topic-${t.id} ${engaged===t.id?'is-active':''}`} key={t.id} style={{'--i':i}} data-color={t.group==='Earth & environment'?'green':'sky'} aria-label={`${t.title}: ${t.short}`} onPointerEnter={e=>{if(e.pointerType!=='touch'){wake(e.currentTarget);engage(t.id);}}} onPointerMove={glow} onPointerLeave={release} onFocus={e=>{if(e?.currentTarget?.matches?.(':focus-visible')!==false){wake(e?.currentTarget);engage(t.id);}}} onBlur={release} onClick={()=>openTopic(t.id)}><span className="topic-light" aria-hidden="true"/><span className="topic-copy"><strong>{t.title}</strong><small>{t.short}</small><span className="topic-glimpse">{categoryGlimpse(t.id)?.title}</span><span className="topic-demo-label">{capabilityPreviews(t.id).length?'Map glimpse + recorded tours':'Map glimpse + guided starting point'}</span>{t.look&&<span className="topic-map" style={swatch(t.look)}><i aria-hidden="true"/>{t.look.name}</span>}</span><span className="topic-arrow" aria-hidden="true">→</span></button>)}</div>)}</section>
      {fullscreen&&touched&&<aside className="welcome-layer-demo" aria-label="Category demonstration"><span className="welcome-kicker">{CATEGORY_MAPS[control]?.name} · LAYER GLIMPSE</span><h2>{glimpse?.title}</h2><p>{glimpse?.try}</p><small>{glimpse?.limit}</small><div className="welcome-layer-demo-actions">{welcomeView(control).starters?.length>0&&<button type="button" aria-pressed={layersVisible} onClick={()=>setLayersVisible(!layersVisible)}>{layersVisible?'Hide starter layers':'Show starter layers'}</button>}<button type="button" onClick={()=>run(()=>(onMap||onTopic)(control))}>Open this category’s map →</button><button type="button" onClick={()=>openTopic(control,true)}>Source notes &amp; demonstrations</button></div><p className="welcome-layer-demo-state" role="status">{previewState?.mapState==='unavailable'?'Map preview unavailable. Open the map to inspect source status.':previewState?.topic!==control||previewState?.mapState==='loading'?'Preparing the category map…':!layersVisible?'Base context only. Starter overlays are hidden; the basemap and elevation remain.':'Provider context preview. Source clocks and availability remain separate.'}</p></aside>}<div className="welcome-scene-deck"><button type="button" className="welcome-preview-expand" aria-pressed={fullscreen} onClick={()=>{if(fullscreen){setPinned(null);setActive(null);}setFullscreen(!fullscreen);}}>{fullscreen?'Return to categories':'Expand animation'}</button>{fullscreen&&<button type="button" className="welcome-preview-pause" disabled={reduced} aria-pressed={!paused} onClick={()=>{const next=!motion;setMotion(next);onMotionChange?.(next);}}>{paused?'Play animation':'Pause animation'}</button>}</div>
      
    </div>
  </section>
    {modal&&<div className="living-welcome welcome-dialog-backdrop" onClick={e=>{if(e.target===e.currentTarget)closePanel();}}><section ref={dialog} className="welcome-dialog" role="dialog" aria-modal="true" aria-labelledby="welcome-detail-title"><div className="welcome-dialog-toolbar"><span className="welcome-kicker">EXPLORE KANSAS</span><button type="button" className="welcome-dialog-close" aria-label="Close exploration details" onClick={closePanel}>×</button></div><div className="welcome-dialog-body">
      {topic?<><h2 id="welcome-detail-title">{topic.title}</h2><p>{topic.description}</p><section className="welcome-category-glimpse" aria-label={`${topic.title} demonstration`}><span className="welcome-kicker">LAYER GLIMPSE</span><h3>{categoryGlimpse(topic.id)?.title}</h3><p>{categoryGlimpse(topic.id)?.summary}</p><p><strong>Look for:</strong> {categoryGlimpse(topic.id)?.try}</p><small>{categoryGlimpse(topic.id)?.limit}</small><button type="button" className="welcome-text-action" onClick={()=>{pin(topic.id);setFullscreen(true);}}>See this on the real map <span aria-hidden="true">↗</span></button></section><CapabilityPreview demo={capabilityPreviews(topic.id)[item]} paused={paused}/>{!capabilityPreviews(topic.id).length&&<p className="welcome-source-note">{capabilityNote(topic.id)}</p>}<h3>Explore in this workspace</h3><ul className="capability-facets">{topic.facets.map(facet=><li key={facet}>{facet}</li>)}</ul><div className="topic-options" role="group" aria-label={`${topic.title} starting points`}>{capabilityPreviews(topic.id).map((demo,i)=><button type="button" key={demo.id} aria-pressed={item===i} onClick={()=>setItem(i)}>{demo.title}<span aria-hidden="true">{item===i?'✓':'→'}</span></button>)}</div><p className="welcome-source-note">{topic.note}</p>{topic.look&&<div className="welcome-map-look" style={swatch(topic.look)}><span className="welcome-map-look-swatch" aria-hidden="true"/><div><strong>{topic.look.name}</strong><small>{categorySceneLabel(topic.look.scene)}</small><p>{topic.look.lede}</p></div></div>}{topic.look&&<button type="button" className="welcome-primary welcome-open-map" onClick={()=>run(()=>(onMap||onTopic)(topic.target))}>Open the {topic.look.name.toLowerCase()} <span aria-hidden="true">→</span></button>}<button type="button" className="welcome-text-action" onClick={()=>run(()=>onTopic(topic.target))}>Explore {topic.title.toLowerCase()} sources →</button><button type="button" className="welcome-text-action welcome-preview-action" onClick={()=>{pin(topic.id);setFullscreen(true);}}>Preview in the welcome window →</button>{topic.id==='groundwater'&&<button type="button" className="welcome-text-action" onClick={()=>run(()=>onAction('underground'))}>Open Underground Explorer →</button>}</>:panel==='credits'?<><h2 id="welcome-detail-title">The maps behind the categories.</h2><p>The map behind the topics is a preview of the real map each category opens with: the same basemap, view and camera. Until you point at a category it shows the Explorer’s default map of Kansas. A previewed category also shows its starter data, drawn as the Explorer draws it: radar as its newest scan while that scan is current, with its time in the caption. Satellite previews use one current, dated NOAA frame; a visible-band fallback is named separately. River gauges require the bounded River Pulse controls in the opened map. Empty and failed feeds are labeled, and source records loaded is not a claim that every record is visible. Providers that are off by default (imagery, aerials, topo maps and the 3D elevation model) load only for a category you preview. Credits for the map on screen are shown with its caption.</p><p>Every topic has a layer glimpse explaining what to look for and which tools need the opened map. Where a verified recorded Explorer tour exists, it loads only when you press Watch and stops after the short tour. Captures retain their original source clocks and limitations. Reused captures are labeled as context; they do not establish additional domain coverage.</p><div className="welcome-footage-credits">{TOPICS.map(t=><article key={t.id}><strong>{t.title}</strong>{capabilityPreviews(t.id).map(d=><div key={d.id}><strong>{d.title}</strong><small>{d.sourceTime}</small><p>{d.limitation}</p>{d.context&&<p>{d.context}</p>}</div>)}{!capabilityPreviews(t.id).length&&<p>{capabilityNote(t.id)}</p>}</article>)}</div></>:<><h2 id="welcome-detail-title">More stories are coming.</h2><p>Explore the available tools today. Additional records appear as their source coverage, dates and review are ready.</p><p className="welcome-source-note">A visual preview does not activate a dataset or establish that it is available. The Explorer’s source controls show current coverage and limitations.</p><button type="button" className="welcome-primary" onClick={()=>run(()=>onAction('layers'))}>Browse the source catalogue →</button><a className="welcome-text-action" href="/observatory/sources">Source observatory ↗</a><button type="button" className="welcome-text-action" onClick={()=>run(onMore)}>Map tools &amp; help →</button></>}
    </div></section></div>}
  </>;
  return createPortal(content,document.querySelector(".site-root")||document.body);
}
