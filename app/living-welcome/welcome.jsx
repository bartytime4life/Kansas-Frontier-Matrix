'use client';
import { useEffect, useLayoutEffect, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import { SCENES, HISTORY_ERAS, sceneArt } from './catalog.mjs';
import { MOTION_CLIPS, motionClip } from './motion-catalog.mjs';
import { MotionAtlas } from './MotionAtlas.jsx';
import { ScenePreview } from './ScenePreview.jsx';
import { WelcomeFeatureGuide } from './FeatureGuide.jsx';
import { isolateModalBackground } from '../modal-background';

const TOPICS=[
  {id:'weather',title:'Weather & skies',short:'Wind, storms & a changing atmosphere.',glyph:'☁',color:'sky',target:'weather',description:'Explore the atmosphere above Kansas, then inspect the source dates behind the map.',note:'Illustrative weather footage is separate from live warnings and forecasts. Follow the source controls for observation times and coverage.'},
  {id:'rivers',title:'Follow the rivers',short:'Currents, floods, farms & water supply.',glyph:'≋',color:'sky',target:'water',description:'Trace the waterways that connect the Kansas landscape.',note:'A river path is landscape context. A gauge describes one sampled station, not every point along the river.'},
  {id:'science',title:'Science & land',short:'Explore soil, ecology and land cover.',glyph:'♧',color:'green',target:'science',description:'Look closer at the science behind the places around you.',note:'Scientific demonstrations and example footage are separate from source observations. Compare compatible units, coverage and dates.'},
  {id:'underground',title:'Look underground',short:'Explore wells, drilling & groundwater.',glyph:'◇',color:'gold',target:'groundwater',description:'See a place through its recorded wells, cores and groundwater sources.',note:'Recorded columns describe sampled locations. The space between them remains unobserved; no continuous geological model is implied.'},
  {id:'history',title:'History & time',short:'Kansas stories, from the Civil War to civil rights.',glyph:'▤',color:'gold',target:'history',description:'Explore Bleeding Kansas, the Civil War, Nicodemus, the Dust Bowl and the fight for equal education in Topeka.',note:'Dated Kansas stories pair archival images with animated event maps. Maps use today’s Kansas outline and approximate place locators. Each chapter links to its archive and a historical source.'},
  {id:'transport',title:'Roads & Rail',short:'Follow the corridors that connect us.',glyph:'▥',color:'sky',target:'transport',description:'Find Kansas road, bridge and rail source layers.',note:'Footage locations are labeled. Example motion is separate from live traffic, train positions and reviewed route coverage.'},
  {id:'farming',title:'Farming',short:'Real fields, tractors & the work of harvest.',glyph:'♧',color:'green',target:'agriculture',description:'Explore a landscape shaped by growing seasons, fields and water.',note:'Real machinery keeps its filmed scale relative to the land. Footage locations are labeled; crop and soil sources retain their own units, dates and coverage.'},
  {id:'government',title:'Government',short:'Discover places of public life.',glyph:'⌂',color:'gold',target:'land',description:'Explore county boundaries, public-land context and the sources behind public places.',note:'Example footage shows public places and restoration work. A scene does not establish that a public record or jurisdiction dataset is connected.'},
];
export default function LivingWelcome({onClose,onAction,onMore,onSearch,onTopic,questions,initialRemember=false,onRememberChange,motionEnabled=true,onMotionChange}){
  const root=useRef(null),dialog=useRef(null),trigger=useRef(null),leave=useRef(null);
  const [localRemember,setRemember]=useState(initialRemember),[query,setQuery]=useState('');
  const remember=onRememberChange?initialRemember:localRemember;
  const [reduced,setReduced]=useState(()=>typeof window!=='undefined'&&window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  const [localMotion,setMotion]=useState(motionEnabled),[hidden,setHidden]=useState(()=>typeof document!=='undefined'&&document.hidden);
  const [active,setActive]=useState(null),[pinned,setPinned]=useState(null),[manual,setManual]=useState(null),[indices,setIndices]=useState({}),[last,setLast]=useState('weather');
  const [detail,setDetail]=useState(null),[panel,setPanel]=useState(null),[item,setItem]=useState(0),[enhanced,setEnhanced]=useState(false);
  const motion=onMotionChange?motionEnabled:localMotion;
  const visible=Object.fromEntries(TOPICS.map(t=>[t.id,true]));
  const paused=!motion||reduced||hidden,engaged=pinned||active,control=engaged||last,selection=manual?.id===control?manual.index:null;
  const topic=TOPICS.find(t=>t.id===detail),modal=Boolean(detail||panel);
  const run=action=>{action?.();onClose(remember);};
  const sceneIndex=id=>manual?.id===id&&engaged===id?manual.index:indices[id]??0;
  function engage(id){clearTimeout(leave.current);setActive(id);setLast(id);}
  function release(){clearTimeout(leave.current);leave.current=setTimeout(()=>{if(!root.current?.querySelector('.topic-callout:focus'))setActive(null);},180);}
  function openTopic(id){trigger.current=document.activeElement;setItem(sceneIndex(id));setDetail(id);setPanel(null);}
  function openPanel(name){trigger.current=document.activeElement;setDetail(null);setPanel(name);}
  function closePanel(){setDetail(null);setPanel(null);}
  function pin(id,index){setPinned(id);setActive(null);setLast(id);setManual({id,index});closePanel();}
  function step(delta){pin(control,(sceneIndex(control)+delta+SCENES[control].length)%SCENES[control].length);}
  function feature(destination){if(destination==='sources')openPanel('data');else run(()=>onTopic(destination));}
  useEffect(()=>{
    const media=window.matchMedia('(prefers-reduced-motion: reduce)'),change=()=>setReduced(media.matches),visibility=()=>setHidden(document.hidden);
    media.addEventListener('change',change);document.addEventListener('visibilitychange',visibility);
    return()=>{media.removeEventListener('change',change);document.removeEventListener('visibilitychange',visibility);clearTimeout(leave.current);};
  },[]);
  useEffect(()=>{
    if(!modal){const target=trigger.current;trigger.current=null;if(target?.isConnected)target.focus({preventScroll:true});return;}
    const node=dialog.current,restore=isolateModalBackground(node,document.body);
    node?.querySelector('button,a,input')?.focus({preventScroll:true});
    return restore;
  },[modal]);
  useLayoutEffect(()=>{
    const keyboard=event=>{
      if(!root.current?.contains(event.target))return;
      if(event.key==='Escape'){
        event.preventDefault();event.stopImmediatePropagation();
        if(modal)closePanel();else if(pinned){setPinned(null);setManual(null);setActive(null);}else onClose(remember);
      }
      if(event.key==='Tab'&&modal){
        const nodes=[...(dialog.current?.querySelectorAll('button,a[href],input')||[])].filter(n=>!n.disabled&&n.getClientRects().length&&!n.closest('[hidden],[inert]'));
        if(event.shiftKey&&document.activeElement===nodes[0]){event.preventDefault();nodes.at(-1)?.focus();}
        else if(!event.shiftKey&&document.activeElement===nodes.at(-1)){event.preventDefault();nodes[0]?.focus();}
      }
    };document.addEventListener('keydown',keyboard,true);return()=>document.removeEventListener('keydown',keyboard,true);
  },[modal,pinned,remember,onClose]);
  const content = <section className="explorer-guide living-welcome" ref={root} role="dialog" aria-modal="false" aria-labelledby="living-welcome-title" data-renderer={enhanced?'native':'fallback'} data-motion={paused?'paused':'playing'}>
    <div className="welcome-map-stage">
      <div className="welcome-wash" aria-hidden="true"/>
      <MotionAtlas paused={paused||modal} active={engaged} visible={visible} manual={selection} onReady={setEnhanced} onScenes={setIndices}/>
      <div className="welcome-hero">
        <span className="welcome-kicker">KANSAS FRONTIER MATRIX</span>
        <h1 id="living-welcome-title">Kansas is full of <em>stories.</em></h1>
        <p>Explore the skies, the land, and the stories beneath.</p>
        <div className="welcome-hero-actions"><form onSubmit={e=>{e.preventDefault();run(()=>onSearch(query.trim()));}}><label><span aria-hidden="true">⌕</span><span className="sr-only">Find a county or place</span><input data-guide-autofocus="" value={query} onChange={e=>setQuery(e.target.value)} placeholder="Find a county or place" maxLength={180}/></label><button type="submit" className="welcome-primary">Explore <span aria-hidden="true">→</span></button></form><button type="button" className="welcome-ask" onClick={()=>run(()=>onAction('qwen'))}><span aria-hidden="true">✧</span><span><strong>Ask the atlas</strong><small>Start with a question</small></span><span aria-hidden="true">↗</span></button></div>
        <div className="welcome-mobile-guide"><WelcomeFeatureGuide onNavigate={feature} paused={paused}/></div>
      </div>
      <button type="button" className="welcome-skip" aria-label="Close quick start" onClick={()=>onClose(remember)}>Skip welcome <span aria-hidden="true">×</span></button>
      <section className="discovery-field" aria-label="Choose an exploration topic">{TOPICS.map(t=><button type="button" className={`topic-callout topic-${t.id} ${engaged===t.id?'is-active':''}`} key={t.id} data-color={t.color} aria-label={`${t.title}: ${t.short}`} onPointerEnter={e=>{if(e.pointerType!=='touch')engage(t.id);}} onPointerLeave={release} onFocus={()=>engage(t.id)} onBlur={release} onClick={()=>openTopic(t.id)}><span className="topic-icon" aria-hidden="true">{t.glyph}</span><span className="topic-copy"><strong>{t.title}</strong><small>{t.short}</small><span className="topic-now">▸ {SCENES[t.id][sceneIndex(t.id)]}</span></span><span className="topic-arrow" aria-hidden="true">→</span><span className={`scene-anchor ${t.id}-scene`} aria-hidden="true"><img src={sceneArt(t.id,sceneIndex(t.id))} alt="" loading="lazy" decoding="async"/></span></button>)}</section>
      <div className="scene-caption" aria-label="Illustrative scene controls"><div><small>{engaged?'IMMERSIVE PREVIEW':'MOTION STORIES · ILLUSTRATIVE'}</small><strong>{TOPICS.find(t=>t.id===control)?.title}</strong><span>{SCENES[control][sceneIndex(control)]}</span><small>{motionClip(control,sceneIndex(control)).context}</small></div><div className="scene-nav"><button type="button" aria-label="Previous scene" onClick={()=>step(-1)}>‹</button><span>{sceneIndex(control)+1} / {SCENES[control].length}</span><button type="button" aria-label="Next scene" onClick={()=>step(1)}>›</button>{manual&&<button type="button" aria-label="Resume automatic scene cycling" onClick={()=>setManual(null)}>▶</button>}</div>{pinned&&<button type="button" onClick={()=>{setPinned(null);setManual(null);setActive(null);}}>End preview ×</button>}</div>
      {control==='history'&&<nav className="history-timeline" aria-label="Kansas history scenes">{HISTORY_ERAS.map((era,i)=><button type="button" key={era} aria-pressed={sceneIndex('history')===i} onClick={()=>pin('history',i)}>{era}</button>)}</nav>}
      <div className="welcome-credits"><span>Illustrative motion · source locations vary</span><button type="button" onClick={()=>openPanel('credits')}>Scene credits</button></div>
      <footer className="welcome-footer"><div><strong>Choose a topic or start with a place.</strong><small>Hover to immerse. Choose a scene, then follow the sources.</small></div><div className="welcome-footer-actions"><button type="button" onClick={()=>openPanel('questions')}>All questions &amp; tools</button><button type="button" aria-label={reduced?'Animations off: reduced motion preference':paused?'Play animation':'Pause animation'} disabled={reduced} aria-pressed={!paused} onClick={()=>{const next=!motion;setMotion(next);onMotionChange?.(next);}}>{reduced?'Reduced motion':paused?'▶ Play animation':'Ⅱ Pause animation'}</button><label><input type="checkbox" checked={remember} onChange={e=>{setRemember(e.target.checked);onRememberChange?.(e.target.checked);}}/> Don’t show on start</label><button type="button" className="welcome-primary" onClick={()=>onClose(remember)}>Explore freely →</button></div></footer>
    </div>
    {modal&&<div className="welcome-dialog-backdrop" onClick={e=>{if(e.target===e.currentTarget)closePanel();}}><section ref={dialog} className="welcome-dialog" role="dialog" aria-modal="true" aria-labelledby="welcome-detail-title"><button type="button" className="welcome-dialog-close" aria-label="Close exploration details" onClick={closePanel}>×</button>
      {topic?<><span className="welcome-kicker">EXPLORE KANSAS</span><h2 id="welcome-detail-title">{topic.title}</h2><p>{topic.description}</p><ScenePreview category={topic.id} index={item} paused={paused}/><div className="topic-options" role="group" aria-label={`${topic.title} starting points`}>{SCENES[topic.id].map((title,i)=><button type="button" key={title} aria-pressed={item===i} onClick={()=>setItem(i)}>{title}<span aria-hidden="true">{item===i?'✓':'→'}</span></button>)}</div><p className="welcome-source-note">{topic.note}</p><button type="button" className="welcome-primary" onClick={()=>pin(topic.id,item)}>Preview this scene on the map →</button><button type="button" className="welcome-text-action" onClick={()=>run(()=>onTopic(topic.target))}>Explore {topic.title.toLowerCase()} sources →</button>{topic.id==='underground'&&<button type="button" className="welcome-text-action" onClick={()=>run(()=>onAction('underground'))}>Open Underground Explorer →</button>}</>:panel==='credits'?<><h2 id="welcome-detail-title">The stories behind the scenes.</h2><p>Footage, scientific animations and Kansas archive maps have their own locations and sources. They are separate from observations on the map.</p><div className="welcome-footage-credits">{Object.values(MOTION_CLIPS).flat().map(clip=><article key={clip.id}><a href={clip.sourceUrl} target="_blank" rel="noreferrer">{clip.title}</a><span>{clip.artist}</span><small>{clip.context} · <a href={clip.licenseUrl} target="_blank" rel="noreferrer">{clip.license}</a></small><small>{clip.adaptation}</small>{clip.historicalSourceUrl&&<a href={clip.historicalSourceUrl} target="_blank" rel="noreferrer">Historical source ↗</a>}</article>)}</div></>:panel==='questions'?<><h2 id="welcome-detail-title">Follow your curiosity.</h2><div className="welcome-legacy-questions">{questions}</div></>:<><h2 id="welcome-detail-title">More stories are coming.</h2><p>Explore the available tools today. Additional records appear as their source coverage, dates and review are ready.</p><p className="welcome-source-note">A visual preview does not activate a dataset or establish that it is available. The Explorer’s source controls show current coverage and limitations.</p><button type="button" className="welcome-primary" onClick={()=>run(()=>onAction('layers'))}>Browse the source catalogue →</button><a className="welcome-text-action" href="/observatory/sources">Source observatory ↗</a><button type="button" className="welcome-text-action" onClick={()=>run(onMore)}>Map tools &amp; help →</button></>}
    </section></div>}
  </section>;
  return createPortal(content,document.querySelector(".site-root")||document.body);
}
