'use client';
import { Suspense, lazy, useEffect, useLayoutEffect, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import { TOPIC_GROUPS, TOPIC_STRUCTURE } from '../layer-workspaces';
import { CATEGORY_MAPS, categorySceneLabel, combineCategoryMaps, normalizeCategoryTopics } from '../category-maps';
import { capabilityPreviews, capabilityNote, categoryGlimpse } from './capability-catalog.mjs';
import { CapabilityPreview } from './CapabilityPreview.jsx';
import { DomainStage } from './DomainStage.jsx';
import { centeredCard, centeredScrollLeft } from './card-carousel.mjs';
import { welcomeView } from '../welcome-map-view';
import { RECORD_COUNTS, recordLinksFor, newspaperSearchUrl, librarySearchUrl } from './record-links.mjs';
import { isolateModalBackground, modalFocusableElements } from '../modal-background';

// "The Kansas record" is a separate section with its own lazy chunks, not a map topic.
const StorySection=lazy(()=>import('./stories/StorySection.jsx'));
// Reuse the governed navigation taxonomy; a welcome tile does not admit data.
const TOPICS=TOPIC_STRUCTURE.map(t=>({...t,target:t.id,short:t.facets.join(' · '),note:t.limitation,look:CATEGORY_MAPS[t.id]}));
// Each card carries a three-colour sketch of the map it opens.
const swatch=look=>look?{'--m0':look.swatch[0],'--m1':look.swatch[1],'--m2':look.swatch[2]}:undefined;
// Siblings recede in a wave that starts at the chosen card. All rects are read
// before any write so one pointer entry costs a single layout for the grid.
function wake(card){
  const cards=card?.closest?.('.discovery-group')?.querySelectorAll('.topic-callout');if(!cards?.length||!card.getBoundingClientRect)return;
  const rects=[...cards].map(node=>node.getBoundingClientRect()),a=card.getBoundingClientRect(),ax=a.left+a.width/2,ay=a.top+a.height/2;
  rects.forEach((r,i)=>cards[i].style.setProperty('--wake',`${Math.min(180,Math.round(Math.hypot(r.left+r.width/2-ax,r.top+r.height/2-ay)*.14))}ms`));
}
// The overview hints at the zones using the same pinned snapshot as Aviation.
// Weather, aircraft, temporary restrictions and UAS grids stay in the opened map.
export function AviationGlimpse({mode,onMode,state,layersVisible}){
 const data=state?.aviation;
 return <div className="welcome-aviation-glimpse">
  <div className="welcome-aviation-modes" role="group" aria-label="Airspace preview view">{[['3d','3D zones'],['2d','2D chart'],['slice','4,000 ft MSL']].map(([id,label])=><button key={id} type="button" aria-pressed={mode===id} onClick={()=>onMode(id)}>{label}</button>)}</div>
  <p className="welcome-aviation-legend"><span>Blue · B / D</span><span>Magenta · C / surface E</span><span>Ochre / red · special use</span></p>
  <p className="welcome-aviation-status" role="status">{!layersVisible?'Zone overlays hidden for comparison.':data?.state==='unavailable'?'Aviation reference unavailable; the basemap alone does not show these zones.':data?.state!=='ready'?'Loading the verified FAA reference…':`${data.edition.state} edition · NASR ${data.cycle}.`}</p>
  <small>Display only; not for navigation or authorization.</small>
  <details className="welcome-aviation-notes"><summary>Source edition &amp; display limits</summary>{data?.edition&&<p>{data.edition.text} Source inventory: {data.volumes} airspace volumes; not all are visible in this view. Only zones are previewed here; airports, airways and other tools are in the opened map.</p>}<small>{mode==='slice'?'Only mapped volumes intersecting 4,000 ft MSL. ':mode==='3d'?'1× display heights above reference airport ground; not a terrain-clearance model. ':''}Not for navigation or authorization. Unshaded areas are not an all-clear; temporary restrictions and drone grids are separate.</small></details>
 </div>;
}
export default function LivingWelcome({onClose,onAction,onMore,onSearch,onTopic,onMap,initialRemember=false,initialTopics=/** @type {readonly string[]} */ ([]),onMaps=/** @type {((topics: readonly import('../layer-workspaces').TopicId[]) => void) | undefined} */ (undefined),motionEnabled=true,onMotionChange,onSources=/** @type {(() => void) | undefined} */ (undefined)}){
  const root=useRef(null),dialog=useRef(null),trigger=useRef(null),leave=useRef(null),wasFullscreen=useRef(false);
  const glowFrame=useRef(0),rail=useRef(null),returnCard=useRef(null),returnScroll=useRef(0),returnCardScroll=useRef(0),returnCardLeft=useRef(0);
  const carouselList=useRef(null),carouselTimer=useRef(null),carouselPointer=useRef(null),carouselDragged=useRef(false);
  const [carousel,setCarousel]=useState(false),[centered,setCentered]=useState(()=>normalizeCategoryTopics(initialTopics)[0]||TOPICS[0].id);
  // Wide, tall screens get the atlas layout: the live map is the page, topics are a rail, one panel describes the chosen map.
  const [desktop,setDesktop]=useState(()=>typeof window!=='undefined'&&window.matchMedia('(min-width:1101px) and (min-height:761px)').matches);
  const departed=useRef(false),modalRestore=useRef(null);
  const [selectedTopics,setSelectedTopics]=useState(()=>normalizeCategoryTopics(initialTopics));
  const [topicQuery,setTopicQuery]=useState(''),[topicGroup,setTopicGroup]=useState('All');
  const selection=combineCategoryMaps(selectedTopics);
  const filteredTopics=TOPICS.filter(t=>(topicGroup==='All'||t.group===topicGroup)&&`${t.title} ${t.short} ${t.description}`.toLowerCase().includes(topicQuery.trim().toLowerCase()));
  const [remember,setRemember]=useState(initialRemember),[query,setQuery]=useState('');
  const [recordQuery,setRecordQuery]=useState(''),[recordScope,setRecordScope]=useState('newspapers');
  // One search box for the whole record: a place opens the map; newspapers, texts and collections open the data library.
  function searchRecord(event){
    event.preventDefault();const q=recordQuery.trim();if(!q)return;
    if(recordScope==='place'){run(()=>onSearch(q));return;}
    const url=recordScope==='collections'?librarySearchUrl(q):newspaperSearchUrl(q,recordScope);
    run(()=>{if(typeof window!=='undefined'&&window.location)window.location.assign(url);});
  }
  const [reduced,setReduced]=useState(()=>typeof window!=='undefined'&&window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  const [localMotion,setMotion]=useState(motionEnabled),[hidden,setHidden]=useState(()=>typeof document!=='undefined'&&document.hidden);
  const [active,setActive]=useState(null),[pinned,setPinned]=useState(null),[last,setLast]=useState('weather');
  const [touched,setTouched]=useState(false),[detail,setDetail]=useState(null),[panel,setPanel]=useState(null),[item,setItem]=useState(0),[fullscreen,setFullscreen]=useState(false);
  const [storyOpen,setStoryOpen]=useState(false);
  const [previewState,setPreviewState]=useState(null),[layersVisible,setLayersVisible]=useState(true),[aviationMode,setAviationMode]=useState('3d');
  const motion=onMotionChange?motionEnabled:localMotion;
  const paused=!motion||reduced||hidden,engaged=pinned||(carousel&&!fullscreen?centered:active),control=engaged||last;
  const atlas=desktop&&!carousel&&!fullscreen,atlasTopic=TOPICS.find(t=>t.id===control),atlasIndex=TOPICS.findIndex(t=>t.id===control),record=atlas?recordLinksFor(control):null;
  // One owned frame; held/reduced-motion views do not keep repainting card
  // highlights, and a dismissed welcome cannot write to a detached card.
  function glow(event){
    if(paused||event.pointerType==='touch')return;
    const card=event.currentTarget,x=event.clientX,y=event.clientY;
    if(glowFrame.current)cancelAnimationFrame(glowFrame.current);
    glowFrame.current=requestAnimationFrame(()=>{glowFrame.current=0;const r=card.getBoundingClientRect();card.style.setProperty('--mx',`${x-r.left}px`);card.style.setProperty('--my',`${y-r.top}px`);});
  }
  useEffect(()=>()=>{if(glowFrame.current){cancelAnimationFrame(glowFrame.current);glowFrame.current=0;}},[paused]);
  const topic=TOPICS.find(t=>t.id===detail),modal=Boolean(detail||panel),glimpse=categoryGlimpse(control);
  // One departure owns the handoff, even if repeated activations are batched
  // before React unmounts the chooser and its retained event handlers.
  const run=action=>{if(departed.current)return;departed.current=true;modalRestore.current?.();modalRestore.current=null;action?.();onClose(remember);};
  // Leaving the full-window preview clears the engaged card itself: hidden cards can
  // lose focus without a blur event, so release() alone may never run.
  function engage(id){clearTimeout(leave.current);setActive(id);setLast(id);setTouched(true);setLayersVisible(true);}
  function release(){clearTimeout(leave.current);leave.current=setTimeout(()=>{const keyboardFocus=root.current?.querySelector('.topic-callout:focus-visible');const pointerHover=window.matchMedia('(hover: hover) and (pointer: fine)').matches&&root.current?.querySelector('.topic-callout:hover');if(!keyboardFocus&&!pointerHover)setActive(null);},180);}
  function openTopic(id,keepPreview=fullscreen){trigger.current=document.activeElement;setItem(0);setDetail(id);setPanel(null);if(!keepPreview)setFullscreen(false);}
  function openPanel(name){trigger.current=document.activeElement;setDetail(null);setPanel(name);}
  function closePanel(){setDetail(null);setPanel(null);}
  function pin(id){clearTimeout(leave.current);setLayersVisible(true);setPinned(id);setActive(null);setLast(id);setTouched(true);closePanel();}
  // Only an explicit Preview action enters the demonstration stage. Hover and
  // keyboard focus update the backdrop without moving the working-map targets.
  function showStage(id){
    // An explicit preview action leaves notes for Return, even on the same stage.
    if(modal)trigger.current=root.current?.querySelector('.welcome-preview-expand');
    if(fullscreen&&id===control){closePanel();return;}
    if(!fullscreen){returnCard.current=id;returnScroll.current=root.current?.scrollTop||0;returnCardScroll.current=root.current?.querySelector('.discovery-field--grouped')?.scrollTop||0;returnCardLeft.current=carouselList.current?.scrollLeft||0;}
    pin(id);setFullscreen(true);
  }
  function hoverStage(id,event){
    if(carousel||event.pointerType==='touch')return;
    wake(event.currentTarget);engage(id);
  }
  function returnToCategories(){
    clearTimeout(leave.current);
    setFullscreen(false);setPinned(null);setActive(null);
  }
  function railKey(event,index){
    const next=event.key==='ArrowRight'?(index+1)%TOPICS.length:event.key==='ArrowLeft'?(index+TOPICS.length-1)%TOPICS.length:event.key==='Home'?0:event.key==='End'?TOPICS.length-1:null;
    if(next===null)return;
    event.preventDefault();showStage(TOPICS[next].id);
    rail.current?.querySelector(`[data-topic="${TOPICS[next].id}"]`)?.focus({preventScroll:true});
  }
  function scrollRail(direction){rail.current?.scrollBy({left:direction*(rail.current.clientWidth*.75),behavior:paused?'instant':'smooth'});}
  // Keep source captions and long panels above the rail even when labels wrap
  // or browser text sizing changes its height.
  useLayoutEffect(()=>{
    if(!fullscreen)return;
    const node=rail.current?.closest?.('.welcome-category-rail'),host=root.current;
    if(!node||!host)return;
    const measure=()=>{
      host.style.setProperty('--welcome-rail-height',`${node.getBoundingClientRect().height}px`);
      rail.current?.querySelector('[aria-pressed="true"]')?.scrollIntoView?.({block:'nearest',inline:'nearest',behavior:'instant'});
    };
    measure();
    if(typeof ResizeObserver==='undefined')return;
    const observer=new ResizeObserver(measure);observer.observe(node);
    return()=>observer.disconnect();
  },[fullscreen]);

  function centerTopic(id, behavior='smooth'){
    const list=carouselList.current,card=list?.querySelector(`[data-carousel-topic="${id}"]`);
    if(!card)return;
    clearTimeout(carouselTimer.current);setCentered(id);setTouched(true);setLayersVisible(true);
    list.scrollTo({left:centeredScrollLeft(card.getBoundingClientRect(),list.getBoundingClientRect(),list.scrollLeft,list.scrollWidth-list.clientWidth),behavior:paused?'instant':behavior});
  }
  function settleCarousel(){
    if(!carousel||fullscreen)return;
    clearTimeout(carouselTimer.current);
    carouselTimer.current=setTimeout(()=>{
      const list=carouselList.current;if(!list)return;
      const id=centeredCard(Array.from(list.querySelectorAll('[data-carousel-topic]'),card=>{const {left,width}=card.getBoundingClientRect();return {left,width,id:card.dataset.carouselTopic};}),list.getBoundingClientRect());
      if(id){setCentered(id);setTouched(true);setLayersVisible(true);}
    },120);
  }
  function moveCarousel(direction){
    const index=filteredTopics.findIndex(t=>t.id===centered);
    const next=filteredTopics[Math.max(0,Math.min(filteredTopics.length-1,index+direction))];
    if(next)centerTopic(next.id);
  }
  function carouselKey(event,id){
    if(!carousel||!['ArrowLeft','ArrowRight','Home','End'].includes(event.key))return;
    const index=filteredTopics.findIndex(t=>t.id===id);
    const next=event.key==='Home'?0:event.key==='End'?filteredTopics.length-1:Math.max(0,Math.min(filteredTopics.length-1,index+(event.key==='ArrowRight'?1:-1)));
    const topic=filteredTopics[next];if(!topic)return;
    event.preventDefault();centerTopic(topic.id,'instant');
    carouselList.current?.querySelector(`.topic-${topic.id}`)?.focus({preventScroll:true});
  }
  useEffect(()=>{
    const media=window.matchMedia('(max-width:700px), (max-height:500px) and (max-width:1100px)');
    const update=()=>setCarousel(media.matches);update();media.addEventListener('change',update);
    const wide=window.matchMedia('(min-width:1101px) and (min-height:761px)');
    const updateWide=()=>setDesktop(wide.matches);wide.addEventListener('change',updateWide);
    return()=>{media.removeEventListener('change',update);wide.removeEventListener('change',updateWide);clearTimeout(carouselTimer.current);};
  },[]);
  useLayoutEffect(()=>{
    if(!carousel||fullscreen)return;
    const id=filteredTopics.some(t=>t.id===centered)?centered:filteredTopics[0]?.id;
    if(id)centerTopic(id,'instant');
  },[carousel,topicQuery,topicGroup,fullscreen]);

  useEffect(()=>{
    const media=window.matchMedia('(prefers-reduced-motion: reduce)'),change=()=>setReduced(media.matches),visibility=()=>{setHidden(document.hidden);};
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
    modalRestore.current=restore;
    node?.querySelector('button,a,input')?.focus({preventScroll:true});
    // Navigation releases isolation before the parent commits its own inert
    // state. A later unmount must not restore the covered map's stale state.
    return()=>{if(modalRestore.current===restore){modalRestore.current=null;restore();}};
  },[modal]);
  useLayoutEffect(()=>{
    const keyboard=event=>{
      if(!root.current?.contains(event.target)&&!dialog.current?.contains(event.target))return;
      if(event.key==='Escape'){
        event.preventDefault();event.stopImmediatePropagation();
        if(modal)closePanel();else if(fullscreen){returnToCategories();}else if(pinned){setPinned(null);setActive(null);}else onClose(remember);
      }
      if(event.key==='Tab'&&modal){
        const nodes=dialog.current?modalFocusableElements(dialog.current):[];
        if(event.shiftKey&&document.activeElement===nodes[0]){event.preventDefault();nodes.at(-1)?.focus();}
        else if(!event.shiftKey&&document.activeElement===nodes.at(-1)){event.preventDefault();nodes[0]?.focus();}
      }
    };document.addEventListener('keydown',keyboard,true);return()=>document.removeEventListener('keydown',keyboard,true);
  },[modal,pinned,fullscreen,remember,onClose]);
  useLayoutEffect(()=>{
    const entering=!wasFullscreen.current&&fullscreen,returning=wasFullscreen.current&&!fullscreen;wasFullscreen.current=fullscreen;
    // Pause disappears on return. Restore the persistent control before the
    // next key, including when Escape was pressed from Pause/Resume itself.
    if(modal)return;
    // Closing notes restores their trigger above; only stage entry owns Return.
    if(entering){if(root.current)root.current.scrollTop=0;root.current?.querySelector('.welcome-preview-expand')?.focus({preventScroll:true});}
    else if(returning){
      const card=returnCard.current&&root.current?.querySelector(`.topic-preview-${returnCard.current}`);
      (card||root.current?.querySelector('.welcome-preview-expand'))?.focus({preventScroll:true});
      // Focus previews a card; returning itself must not restart the stage.
      setActive(null);
      if(root.current)root.current.scrollTop=returnScroll.current;
      const cards=root.current?.querySelector('.discovery-field--grouped');
      if(cards){cards.scrollTop=returnCardScroll.current;cards.scrollLeft=returnCardLeft.current;}
    }
  },[fullscreen,modal]);
  useLayoutEffect(()=>{
    if(fullscreen)rail.current?.querySelector(`[data-topic="${control}"]`)?.scrollIntoView?.({block:'nearest',inline:'nearest',behavior:'instant'});
  },[fullscreen,control]);
  function toggleTopic(id){
    setSelectedTopics(current=>current.includes(id)?current.filter(value=>value!==id):[...current,id]);
    setLast(id);
  }
  function openSelection(){if(selection)run(()=>onMaps?onMaps(selection.topics):(onMap||onTopic)(selection.topics[0]));}
  const selectedIndex=TOPICS.findIndex(t=>t.id===control);
  const content = <><section className="explorer-guide living-welcome" ref={root} role="dialog" aria-modal="false" aria-label={fullscreen?`${TOPICS[selectedIndex]?.title||'Kansas'} map preview`:undefined} aria-labelledby={fullscreen?undefined:'living-welcome-title'} data-renderer="capability" data-builder="true" data-carousel={carousel} data-layout={atlas?"atlas":undefined} data-centered-topic={carousel?centered:undefined} data-selected-count={selectedTopics.length} data-active={engaged||null} data-fullscreen={fullscreen} data-cinematic={fullscreen} data-motion={paused?'paused':'playing'} data-immersive={Boolean(engaged&&!modal)}>
    <div className="welcome-map-stage">
      <div className="welcome-wash" aria-hidden="true"/>
      <div className="welcome-capability-stage"><DomainStage topic={carousel||touched||atlas?control:null} expanded={fullscreen||carousel} aviationMode={aviationMode} layersVisible={layersVisible} paused={paused||modal||storyOpen||(!engaged&&!fullscreen&&!atlas)} reduced={reduced} onPreviewState={setPreviewState}/></div>
      <div className="welcome-heading-row">
        <div className="welcome-toolbar" role="group" aria-label="Welcome options">
          {/* There is no selection tray: cards and the focus panel tick topics, and this opens the ticked set. The phone toolbar has room for one primary, so there it stands in for Explore freely while topics are ticked. */}
          {selection&&<button type="button" className="welcome-primary selection-open" aria-label={`Open my map with ${selectedTopics.length} selected ${selectedTopics.length===1?'topic':'topics'}`} onClick={openSelection}>Open my map <span className="selection-count" aria-hidden="true">{selectedTopics.length}</span><span aria-hidden="true">→</span></button>}
          {!(carousel&&selection)&&<button type="button" className="welcome-primary" onClick={()=>onClose(remember)}>Explore freely <span aria-hidden="true">→</span></button>}
          <details className="welcome-preferences"><summary>Options</summary><div>
            <button type="button" className="welcome-tool" aria-label={reduced?'Animations off: reduced motion preference':paused?'Play animation':'Pause animation'} disabled={reduced} onClick={()=>{const next=!motion;setMotion(next);onMotionChange?.(next);}}>{reduced?'Reduced motion':paused?'Play animation':'Pause animation'}</button>
            <label className="welcome-tool"><input type="checkbox" checked={remember} onChange={e=>setRemember(e.target.checked)}/> Don’t show on start</label>
            <button type="button" className="welcome-map-notes" onClick={()=>{onSources?.();openPanel('credits');}}>Map notes</button>
            <button type="button" onClick={()=>run(()=>onAction('qwen'))}>Ask the atlas</button>
          </div></details>
          <button type="button" className="welcome-skip" aria-label="Close quick start" onClick={()=>onClose(remember)}>×</button>
        </div>
        <div className="welcome-hero"><span className="welcome-kicker">KANSAS FRONTIER MATRIX</span>
          <h1 id="living-welcome-title" tabIndex={-1} data-guide-autofocus="">Kansas is full of <em>stories.</em></h1>
          <p>Choose a map. See what connects.</p>
          {atlas&&<form className="welcome-record-search" onSubmit={searchRecord} aria-label="Search the record">
            <label><span className="sr-only">Search words</span><input type="search" value={recordQuery} onChange={e=>setRecordQuery(e.target.value)} placeholder={recordScope==='place'?'Find a county or place':recordScope==='collections'?'Wells, bridges, census, schools…':'tornado · "dust storm" · grasshopper*'} maxLength={200}/></label>
            <label><span className="sr-only">Where to search</span><select value={recordScope} onChange={e=>setRecordScope(e.target.value)}><option value="newspapers">Newspapers 1864–1960</option><option value="texts">Archive texts</option><option value="collections">{RECORD_COUNTS.collections} collections</option><option value="place">A place on the map</option></select></label>
            <button type="submit" className="welcome-primary" disabled={!recordQuery.trim()}>Search</button>
          </form>}
          <details className="welcome-place-search"><summary>Looking for a place?</summary><form onSubmit={e=>{e.preventDefault();if(query.trim())run(()=>onSearch(query.trim()));}}><label><span className="sr-only">Find a county or place</span><input value={query} onChange={e=>setQuery(e.target.value)} placeholder="Find a county or place" maxLength={180}/></label><button type="submit" className="welcome-primary" disabled={!query.trim()}>Find place</button></form></details>
        </div>
      </div>
      <div className="welcome-discovery-layout"><div className="welcome-discovery-content">
        <details className="topic-filters"><summary>Find a topic</summary><div className="topic-finder"><label><span className="sr-only">Filter topics</span><input type="search" value={topicQuery} onChange={e=>setTopicQuery(e.target.value)} placeholder="Find topics: water, roads, history…"/></label><label><span className="sr-only">Topic group</span><select value={topicGroup} onChange={e=>setTopicGroup(e.target.value)}><option value="All">All topics</option>{TOPIC_GROUPS.map(group=><option key={group}>{group}</option>)}</select></label></div></details>
        <p className="discovery-hint"><strong>Choose your map</strong><span>Tap a card to open · + to combine</span></p>
        {carousel&&<nav className="welcome-carousel-nav" aria-label="Browse map previews"><button type="button" aria-label="Previous map preview" disabled={filteredTopics.findIndex(t=>t.id===centered)<=0} onClick={()=>moveCarousel(-1)}>←</button><span aria-live="polite">{filteredTopics.length?filteredTopics.findIndex(t=>t.id===centered)+1:0} / {filteredTopics.length}</span><button type="button" aria-label="Next map preview" disabled={!filteredTopics.length||filteredTopics.findIndex(t=>t.id===centered)>=filteredTopics.length-1} onClick={()=>moveCarousel(1)}>→</button></nav>}
        <section className="discovery-field discovery-field--grouped" ref={carouselList} aria-label={carousel?'Swipe to preview maps; tap a card to open':'Choose exploration topics'} aria-roledescription={carousel?'carousel':undefined} onScroll={settleCarousel} onPointerDown={event=>{carouselPointer.current={x:event.clientX,y:event.clientY};carouselDragged.current=false;}} onPointerMove={event=>{const start=carouselPointer.current;if(start&&Math.hypot(event.clientX-start.x,event.clientY-start.y)>8)carouselDragged.current=true;}} onPointerUp={()=>{carouselPointer.current=null;}} onPointerCancel={()=>{carouselPointer.current=null;}} onClickCapture={event=>{if(carousel&&carouselDragged.current&&event.detail!==0){event.preventDefault();event.stopPropagation();}}}>{TOPIC_GROUPS.filter(group=>filteredTopics.some(t=>t.group===group)).map(group=><div className="discovery-group" role="group" aria-label={group} key={group}><h2 className="discovery-group-title">{group}</h2>{filteredTopics.filter(t=>t.group===group).map(t=><div className="topic-choice" data-carousel-topic={t.id} data-centered={carousel&&centered===t.id} data-selected={selectedTopics.includes(t.id)} key={t.id} style={swatch(t.look)}>
          <button type="button" className={`topic-callout topic-${t.id} ${engaged===t.id?'is-active':''}`} aria-label={`Open ${t.title} map: ${t.short}`} onPointerEnter={e=>hoverStage(t.id,e)} onPointerMove={glow} onPointerLeave={release} onFocus={e=>{if(e?.currentTarget?.matches?.(':focus-visible')!==false){if(carousel)centerTopic(t.id,'instant');else engage(t.id);}}} onKeyDown={e=>carouselKey(e,t.id)} onBlur={release} onClick={()=>run(()=>onMaps?onMaps(normalizeCategoryTopics([t.id,...selectedTopics])):(onMap||onTopic)(t.id))}>
            <span className="topic-light" aria-hidden="true"/><span className="topic-copy"><strong>{t.title}</strong><small>{t.facets.slice(0,2).join(' · ')}</small><span className="topic-map" style={swatch(t.look)}><i aria-hidden="true"/>{t.look?.name}</span><span className="topic-demo-label">Open map →</span></span>
          </button><div className="topic-card-actions"><button type="button" className={`topic-preview topic-preview-${t.id}`} aria-label={`Preview ${t.title}`} onClick={()=>showStage(t.id)}>Preview <span aria-hidden="true">↗</span></button><button type="button" className="topic-add" data-topic={t.id} aria-label={`${selectedTopics.includes(t.id)?'Remove':'Add'} ${t.title} ${selectedTopics.includes(t.id)?'from':'to'} combined map`} aria-pressed={selectedTopics.includes(t.id)} onClick={()=>toggleTopic(t.id)}><span aria-hidden="true">{selectedTopics.includes(t.id)?'✓':'+'}</span></button></div>
        </div>)}</div>)}</section>
        {atlas&&<nav className="welcome-record-rail" aria-label="The public record">
          <p className="discovery-group-title">The record</p>
          <a href="/data-library"><strong>Public data library</strong><small>{RECORD_COUNTS.collections} collections · {RECORD_COUNTS.mapped} with map geometry · every field, every source</small></a>
          <a href={newspaperSearchUrl('tornado')}><strong>Newspaper &amp; text archive</strong><small>Search the digitised Kansas pages, 1864–1960, and public-domain texts</small></a>
        </nav>}
        {!fullscreen&&<Suspense fallback={null}><StorySection paused={paused} reduced={reduced} modal={modal} compact={carousel} onOpenChange={setStoryOpen}/></Suspense>}
        {!filteredTopics.length&&<div className="topic-empty" role="status"><strong>No matching topics</strong><p>Try a broader term, or see every topic.</p><button type="button" onClick={()=>{setTopicQuery('');setTopicGroup('All');}}>Show all topics</button></div>}
      </div></div>
      {atlas&&atlasTopic&&<aside className="welcome-focus" aria-label="Chosen map" data-topic={control} key={control}>
        <span className="welcome-kicker">{atlasTopic.group} · {String(atlasIndex+1).padStart(2,'0')} / {TOPICS.length}</span>
        <h2>{atlasTopic.title}</h2>
        {atlasTopic.look&&<p className="welcome-focus-map" style={swatch(atlasTopic.look)}><i aria-hidden="true"/><strong>{atlasTopic.look.name}</strong><span>{categorySceneLabel(atlasTopic.look.scene)}</span></p>}
        <p className="welcome-focus-lede">{atlasTopic.look?.lede||atlasTopic.description}</p>
        <div className="welcome-focus-actions">
          <button type="button" className="welcome-primary" onClick={()=>run(()=>onMaps?onMaps(normalizeCategoryTopics([control,...selectedTopics])):(onMap||onTopic)(control))}>Open this map <span aria-hidden="true">→</span></button>
          <button type="button" aria-label="Full-screen preview" onClick={()=>showStage(control)}>Preview <span aria-hidden="true">↗</span></button>
          <button type="button" aria-pressed={selectedTopics.includes(control)} onClick={()=>toggleTopic(control)}>{selectedTopics.includes(control)?'✓ In my map':'+ Add to my map'}</button>
        </div>
        {/* The map keeps the screen: facets, the glimpse and the record fold away under one disclosure, their hooks unchanged. */}
        <details className="welcome-focus-more"><summary>About this map &amp; its records</summary>
        <ul className="welcome-focus-facets" aria-label="What this map covers">{atlasTopic.facets.map(facet=><li key={facet}>{facet}</li>)}</ul>
        {glimpse&&<p className="welcome-focus-try"><strong>{glimpse.title}.</strong> {glimpse.try}</p>}
        {record&&<section className="welcome-focus-record" aria-label="In the public record">
          <span className="welcome-kicker">IN THE RECORD · {record.total} {record.total===1?'collection':'collections'}{record.mapped?` · ${record.mapped} on the map`:''}</span>
          <ul>{record.collections.map(c=><li key={c.id}><a href={c.url}>{c.title}</a>{c.mapUrl&&<a href={c.mapUrl} className="welcome-focus-record-map" aria-label={`${c.title} on the map`}>map</a>}</li>)}</ul>
          <p>Newspapers: {record.terms.map((t,i)=><span key={t.term}>{i>0&&' · '}<a href={t.url}>“{t.term}”</a></span>)}<span> · </span><a href={record.libraryUrl}>all collections →</a></p>
        </section>}
        </details>
        <small>{atlasTopic.note}</small>
      </aside>}
      {fullscreen&&touched&&<aside className="welcome-layer-demo" aria-label="Category demonstration">
        <span className="welcome-kicker">{TOPICS[selectedIndex]?.title}</span>
        <h2>{glimpse?.title}</h2>
        <div className="welcome-layer-demo-actions">
          <button type="button" className="welcome-open-category" aria-label={carousel?`Open map: ${TOPICS[selectedIndex]?.title}`:'Open this category’s map →'} onClick={()=>run(()=>onMaps?onMaps(normalizeCategoryTopics([...selectedTopics,control])):(onMap||onTopic)(control))}>{carousel?'Open map →':'Open this category’s map →'}</button>
          {(control==='aviation'||welcomeView(control).starters?.length>0||welcomeView(control).scientificLayers?.length>0)&&<button type="button" aria-label={carousel?(layersVisible?'Hide layers in preview':'Show layers in preview'):(layersVisible?'Hide starter layers':'Show starter layers')} aria-pressed={layersVisible} onClick={()=>setLayersVisible(!layersVisible)}>{carousel?(layersVisible?'Hide layers':'Show layers'):(layersVisible?'Hide starter layers':'Show starter layers')}</button>}
          <button type="button" aria-label={carousel?'Details: source notes & demonstrations':'Source notes & demonstrations'} onClick={()=>openTopic(control,true)}>{carousel?'Details':'Source notes & demonstrations'}</button>
        </div>
        <p>{glimpse?.try}</p><small>{glimpse?.limit}</small>
        {control==='geology'&&<button type="button" className="welcome-text-action" onClick={()=>run(()=>onAction('underground'))}>Open Underground Explorer →</button>}
        {control==='aviation'&&<details className="welcome-aviation-disclosure" open={!carousel}><summary>Airspace view &amp; source</summary><AviationGlimpse mode={aviationMode} onMode={setAviationMode} state={previewState?.topic===control?previewState:null} layersVisible={layersVisible}/></details>}
        <p className="welcome-layer-demo-state" role="status" data-attention={previewState?.mapState==='unavailable'||previewState?.topic!==control||previewState?.mapState==='loading'||!layersVisible}>{previewState?.mapState==='unavailable'?'Map preview unavailable. Open the map to inspect source status.':previewState?.topic!==control||previewState?.mapState==='loading'?'Preparing the category map…':!layersVisible?'Base context only. Starter overlays are hidden; the basemap and elevation remain.':'Provider context preview. Source clocks and availability remain separate.'}</p>
      </aside>}<div className="welcome-scene-deck">{fullscreen&&<button type="button" className="welcome-preview-expand" aria-pressed={true} onClick={returnToCategories}>Return to categories</button>}{fullscreen&&<><span className="welcome-stage-title">KANSAS FRONTIER MATRIX <span> / {welcomeView(control).name}</span></span><button type="button" className="welcome-preview-pause" disabled={reduced} aria-pressed={!paused} onClick={()=>{const next=!motion;setMotion(next);onMotionChange?.(next);}}>{paused?'Play animation':'Pause animation'}</button><button type="button" className="welcome-stage-close" aria-label="Close quick start" onClick={()=>onClose(remember)}>×</button></>}</div>
      {fullscreen&&<nav className="welcome-category-rail" aria-label="Explore other categories">
        <div className="welcome-rail-heading"><span>CHOOSE YOUR NEXT STORY</span><span id="welcome-rail-keys" className="sr-only">Use Left and Right arrow keys to choose a category; Home and End choose the first and last.</span><span>{String(selectedIndex+1).padStart(2,'0')} / {TOPICS.length}</span></div>
        <div className="welcome-rail-track"><button type="button" className="welcome-rail-scroll" aria-label="Scroll categories left" onClick={()=>scrollRail(-1)}>←</button>
          <div className="welcome-rail-items" ref={rail} role="toolbar" aria-label="Category maps" aria-describedby="welcome-rail-keys">{TOPICS.map((t,index)=><button type="button" key={t.id} data-topic={t.id} tabIndex={control===t.id?0:-1} aria-pressed={control===t.id} className="welcome-rail-card" style={swatch(t.look)} onClick={()=>showStage(t.id)} onKeyDown={event=>railKey(event,index)}><span className="welcome-rail-swatch" aria-hidden="true"/><span><strong>{t.title}</strong><small>{t.look?.name}</small></span></button>)}</div>
          <button type="button" className="welcome-rail-scroll" aria-label="Scroll categories right" onClick={()=>scrollRail(1)}>→</button>
        </div>
      </nav>}
      
    </div>
  </section>
    {modal&&<div className="living-welcome welcome-dialog-backdrop" onClick={e=>{if(e.target===e.currentTarget)closePanel();}}><section ref={dialog} className="welcome-dialog" role="dialog" aria-modal="true" aria-labelledby="welcome-detail-title"><div className="welcome-dialog-toolbar"><span className="welcome-kicker">EXPLORE KANSAS</span><button type="button" className="welcome-dialog-close" aria-label="Close exploration details" onClick={closePanel}>×</button></div><div className="welcome-dialog-body">
      {topic?<><h2 id="welcome-detail-title">{topic.title}</h2><p>{topic.description}</p><section className="welcome-category-glimpse" aria-label={`${topic.title} demonstration`}><span className="welcome-kicker">LAYER GLIMPSE</span><h3>{categoryGlimpse(topic.id)?.title}</h3><p>{categoryGlimpse(topic.id)?.summary}</p><p><strong>Look for:</strong> {categoryGlimpse(topic.id)?.try}</p><small>{categoryGlimpse(topic.id)?.limit}</small><button type="button" className="welcome-text-action" onClick={()=>{showStage(topic.id);}}>See this on the real map <span aria-hidden="true">↗</span></button></section>{topic.id==='aviation'&&<section className="welcome-aviation-tools" aria-label="Aviation tools"><h3>Try the airspace tools</h3><p>Compare mapped zones in 3D, a flat chart, or a 4,000 ft MSL slice here. Open the aviation map to inspect a point’s vertical column, draw an A→B side view, or check separately dated weather, aircraft, drone grids and TFRs when available.</p><div className="welcome-aviation-modes">{[['3d','Preview 3D zones'],['2d','Preview 2D chart'],['slice','Preview altitude slice']].map(([id,label])=><button type="button" key={id} onClick={()=>{setAviationMode(id);showStage('aviation');}}>{label}</button>)}</div></section>}<CapabilityPreview demo={capabilityPreviews(topic.id)[item]} paused={paused}/>{!capabilityPreviews(topic.id).length&&<p className="welcome-source-note">{capabilityNote(topic.id)}</p>}<h3>Explore in this workspace</h3><ul className="capability-facets">{topic.facets.map(facet=><li key={facet}>{facet}</li>)}</ul><div className="topic-options" role="group" aria-label={`${topic.title} starting points`}>{capabilityPreviews(topic.id).map((demo,i)=><button type="button" key={demo.id} aria-pressed={item===i} onClick={()=>setItem(i)}>{demo.title}<span aria-hidden="true">{item===i?'✓':'→'}</span></button>)}</div><p className="welcome-source-note">{topic.note}</p>{topic.look&&<div className="welcome-map-look" style={swatch(topic.look)}><span className="welcome-map-look-swatch" aria-hidden="true"/><div><strong>{topic.look.name}</strong><small>{categorySceneLabel(topic.look.scene)}</small><p>{topic.look.lede}</p></div></div>}{topic.look&&<button type="button" className="welcome-primary welcome-open-map" onClick={()=>run(()=>onMaps?onMaps(normalizeCategoryTopics([...selectedTopics,topic.target])):(onMap||onTopic)(topic.target))}>Open the {topic.look.name.toLowerCase()} <span aria-hidden="true">→</span></button>}<button type="button" className="welcome-text-action" onClick={()=>run(()=>onTopic(topic.target))}>Explore {topic.title.toLowerCase()} sources →</button><button type="button" className="welcome-text-action welcome-preview-action" onClick={()=>{showStage(topic.id);}}>Preview in the welcome window →</button>{['groundwater','geology'].includes(topic.id)&&<button type="button" className="welcome-text-action" onClick={()=>run(()=>onAction('underground'))}>Open Underground Explorer →</button>}</>:panel==='credits'?<><h2 id="welcome-detail-title">The maps behind the categories.</h2><p>The map behind the topics is a preview of the real map each category opens with: the same basemap, view and camera. Until you point at a category it shows the Explorer’s default map of Kansas. A previewed category also shows its starter data, drawn as the Explorer draws it: radar as its newest scan while that scan is current, with its time in the caption. Satellite previews use one current, dated NOAA frame; a visible-band fallback is named separately. River gauges require the bounded River Pulse controls in the opened map. Empty and failed feeds are labeled, and source records loaded is not a claim that every record is visible. Providers that are off by default (imagery, aerials, topo maps and the 3D elevation model) load only for a category you preview. Credits for the map on screen are shown with its caption.</p><p>Every topic has a layer glimpse explaining what to look for and which tools need the opened map. Where a verified recorded Explorer tour exists, it loads only when you press Watch and stops after the short tour. Captures retain their original source clocks and limitations. Reused captures are labeled as context; they do not establish additional domain coverage.</p><div className="welcome-footage-credits">{TOPICS.map(t=><article key={t.id}><strong>{t.title}</strong>{capabilityPreviews(t.id).map(d=><div key={d.id}><strong>{d.title}</strong><small>{d.sourceTime}</small><p>{d.limitation}</p>{d.context&&<p>{d.context}</p>}</div>)}{!capabilityPreviews(t.id).length&&<p>{capabilityNote(t.id)}</p>}</article>)}</div></>:<><h2 id="welcome-detail-title">More stories are coming.</h2><p>Explore the available tools today. Additional records appear as their source coverage, dates and review are ready.</p><p className="welcome-source-note">A visual preview does not activate a dataset or establish that it is available. The Explorer’s source controls show current coverage and limitations.</p><button type="button" className="welcome-primary" onClick={()=>run(()=>onAction('layers'))}>Browse the source catalogue →</button><a className="welcome-text-action" href="/observatory/sources">Source observatory ↗</a><a className="welcome-text-action" href="/pipelines">Card pipelines &amp; source coverage ↗</a><button type="button" className="welcome-text-action" onClick={()=>run(onMore)}>Map tools &amp; help →</button></>}
    </div></section></div>}
  </>;
  return createPortal(content,document.querySelector(".site-root")||document.body);
}
