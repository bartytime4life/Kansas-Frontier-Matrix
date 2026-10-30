import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
import { componentHarness, findNode, settle } from './component-harness.mjs';
import { SCENES, CATEGORY_IDS, HISTORY_ERAS, sceneArt } from '../app/living-welcome/catalog.mjs';
import { MOTION_CLIPS, motionClip } from '../app/living-welcome/motion-catalog.mjs';

import { capabilityPreviews, capabilityNote, categoryGlimpse } from '../app/living-welcome/capability-catalog.mjs';
const topicModule={};
new Function('exports',ts.transpileModule(await readFile('app/layer-workspaces.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(topicModule);
const {TOPIC_STRUCTURE,TOPIC_GROUPS}=topicModule;
const categoryModule={};
new Function('exports',ts.transpileModule(await readFile('app/category-maps.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(categoryModule);
const rootOf=tree=>findNode(tree,node=>node.props?.className==='explorer-guide living-welcome');
const features=[{id:'roads',status:'Explore',description:'Roads',destination:'transport'},{id:'farms',status:'Explore',description:'Farms',destination:'agriculture'}];
function environment(reduced=false){
 const listeners=new Map(),media={matches:reduced,addEventListener(){},removeEventListener(){}};
 return {window:{matchMedia:()=>media},document:{hidden:false,body:{},querySelector:()=>null,activeElement:null,addEventListener:(id,fn)=>listeners.set(id,fn),removeEventListener:id=>listeners.delete(id)},listeners};
}
async function welcome(reduced=false,globals={}){
 const env={...environment(reduced),...globals},calls=[];
 const harness=await componentHarness('app/living-welcome/welcome.jsx',{
  'react-dom':{createPortal:content=>content},'../layer-workspaces':{TOPIC_STRUCTURE,TOPIC_GROUPS},'../category-maps':categoryModule,'./capability-catalog.mjs':{capabilityPreviews,capabilityNote,categoryGlimpse},'./CapabilityPreview.jsx':{CapabilityPreview:'capability-preview'},'./DomainStage.jsx':{DomainStage:'domain-stage'},'../welcome-map-view':{welcomeView:topic=>({topic,name:topic?categoryModule.CATEGORY_MAPS[topic]?.name??topic:'Kansas',starters:categoryModule.CATEGORY_MAPS[topic]?.starters??[]})},'./catalog.mjs':{SCENES,HISTORY_ERAS,sceneArt},'./motion-catalog.mjs':{MOTION_CLIPS,motionClip},
  './MotionAtlas.jsx':{MotionAtlas:'motion-atlas'},'./ScenePreview.jsx':{ScenePreview:'scene-preview'},'./MapDemoPanel.jsx':{MapDemoPanel:'map-demo-panel'},
  './FeatureGuide.jsx':{WelcomeFeatureGuide:'feature-guide'},'../modal-background':{isolateModalBackground:()=>{env.isolated=true;return()=>{env.isolated=false;};},modalFocusableElements:panel=>env.focusCandidates?.(panel)||[]},
 },env);
 const props={onClose:value=>calls.push(['close',value]),onAction:value=>calls.push(['action',value]),onMore:()=>calls.push(['help']),onSearch:value=>calls.push(['search',value]),onTopic:value=>calls.push(['topic',value]),onMap:value=>calls.push(['map',value])};
 const render=()=>{const tree=harness.render(harness.exports.default,props);harness.commit();return tree;};
 return {harness,props,calls,render,env};
}
const byText=(tree,text)=>findNode(tree,node=>node.type==='button'&&node.props.children===text);

function openDetails(h,tree){byText(tree,'Source notes & demonstrations').props.onClick();return h.render();}
const expandedStatus=tree=>findNode(tree,node=>node.props?.className==='welcome-layer-demo-state');
function expandCategory(h,id){
 let tree=h.render();
 findNode(tree,node=>node.type==='button'&&node.props.className?.includes(`topic-${id} `)).props.onClick();tree=h.render();tree=openDetails(h,tree);
 byText(tree,'Preview in the welcome window →').props.onClick();return h.render();
}
function reportPreview(h,tree,value){
 findNode(tree,node=>node.type==='domain-stage').props.onPreviewState(value);return h.render();
}

test('expanded map failure beats missing or stale category identity and hidden-layer copy, with working map entry',async()=>{
 for(const fallback of [false,true]){
  const h=await welcome();if(fallback)delete h.props.onMap;
  try{
   let tree=expandCategory(h,'history');
   for(const value of [{mapState:'unavailable'},{topic:'weather',mapState:'unavailable'},{topic:'history',mapState:'unavailable'}]){
    tree=reportPreview(h,tree,value);
    assert.equal(expandedStatus(tree).props.role,'status');
    assert.equal(expandedStatus(tree).props.children,'Map preview unavailable. Open the map to inspect source status.');
   }
   byText(tree,'Hide starter layers').props.onClick();tree=h.render();
   assert.match(expandedStatus(tree).props.children,/Map preview unavailable/,'comparison cannot mask a failed map');
   byText(tree,'Show starter layers').props.onClick();tree=h.render();
   byText(tree,'Source notes & demonstrations').props.onClick();tree=h.render();
   byText(tree,'Preview in the welcome window →').props.onClick();tree=h.render();
   assert.match(expandedStatus(tree).props.children,/Map preview unavailable/,'reopening details preserves failure guidance');
   byText(tree,'Open this category’s map →').props.onClick();
   assert.deepEqual(h.calls,[[fallback?'topic':'map','history'],['close',false]]);
  }finally{h.harness.dispose();}
 }
});

test('expanded status preserves loading, provider failures, category switching and recovery',async()=>{
 const h=await welcome();
 try{
  let tree=expandCategory(h,'history');
  assert.equal(expandedStatus(tree).props.children,'Preparing the category map…');
  byText(tree,'Hide starter layers').props.onClick();tree=h.render();
  assert.equal(expandedStatus(tree).props.children,'Preparing the category map…','comparison cannot mask initial loading');
  for(const value of [{topic:'history',mapState:'loading',sources:[]},{topic:'weather',mapState:'ready',sources:[]}]){
   tree=reportPreview(h,tree,value);assert.equal(expandedStatus(tree).props.children,'Preparing the category map…');
  }
  byText(tree,'Show starter layers').props.onClick();tree=h.render();
  tree=reportPreview(h,tree,{topic:'history',mapState:'ready',sources:[{id:'nps',label:'Park service',state:'unavailable'}]});
  assert.match(expandedStatus(tree).props.children,/Provider context preview/,'a provider failure is separate from map availability');
  assert.ok(findNode(tree,node=>node.type==='span'&&node.props['data-state']==='unavailable'));
  byText(tree,'Hide starter layers').props.onClick();tree=h.render();
  assert.match(expandedStatus(tree).props.children,/Base context only/);
  tree=reportPreview(h,tree,{mapState:'unavailable'});
  assert.match(expandedStatus(tree).props.children,/Map preview unavailable/);
  byText(tree,'Return to categories').props.onClick();tree=h.render();
  tree=expandCategory(h,'groundwater');
  assert.match(expandedStatus(tree).props.children,/Map preview unavailable/,'global failure survives a category switch');
  tree=reportPreview(h,tree,{topic:'history',mapState:'ready',sources:[]});
  assert.equal(expandedStatus(tree).props.children,'Preparing the category map…','late previous-category success is not current readiness');
  tree=reportPreview(h,tree,{topic:'groundwater',mapState:'loading',sources:[]});
  assert.equal(expandedStatus(tree).props.children,'Preparing the category map…');
  tree=reportPreview(h,tree,{topic:'groundwater',mapState:'ready',sources:[]});
  assert.match(expandedStatus(tree).props.children,/Provider context preview/,'current-category readiness replaces failure');
  assert.equal(findNode(tree,node=>node.type==='domain-stage').props.layersVisible,true);
 }finally{h.harness.dispose();}
});

test('DomainStage reports callback and rejected initialization failures to its welcome owner',async()=>{
 for(const failure of ['callback','reject']){
  let boot;const reports=[];
  const h=await componentHarness('app/living-welcome/DomainStage.jsx',{
   '../map-runtime':{BASEMAPS:{standard:{note:'Provider credit'}}},'../live-context':{OFFICIAL_CONTEXT_BY_ID:{}},
   '../welcome-map-view':{welcomeView:topic=>({topic,name:'Map',basemap:'standard',detail:'Context'})},
   './map-engine.mjs':{createWelcomeMap:async(_host,{onError})=>{if(failure==='reject')throw new Error('Initialization failed');onError();return null;}},
  },{window:{requestIdleCallback:fn=>{boot=fn;return 1;},cancelIdleCallback(){}}});
  const props={topic:'history',onPreviewState:value=>reports.push(value)};
  try{
   let tree=h.render(h.exports.DomainStage,props);findNode(tree,node=>node.props?.className==='domain-stage-map').props.ref.current={};h.commit();
   boot();await settle();tree=h.render(h.exports.DomainStage,props);h.commit();
   assert.equal(tree.props['data-state'],'unavailable');
   assert.deepEqual(JSON.parse(JSON.stringify(reports)),[{mapState:'unavailable'}],failure);
  }finally{h.dispose();}
 }
});

test('a hidden welcome defers its renderer, cancels queued boot and starts only once when visible',async()=>{
 const listeners=new Map(),queued=new Map();let id=0,starts=0,disposals=0;
 const document={hidden:true,addEventListener:(event,fn)=>listeners.set(event,fn),removeEventListener:event=>listeners.delete(event)};
 const h=await componentHarness('app/living-welcome/DomainStage.jsx',{
  '../map-runtime':{BASEMAPS:{standard:{note:'Credit'}}},'../live-context':{OFFICIAL_CONTEXT_BY_ID:{}},
  '../welcome-map-view':{welcomeView:()=>({topic:null,name:'Kansas',basemap:'standard',detail:'Context'})},
  './map-engine.mjs':{createWelcomeMap:async()=>{starts++;return {setAviationMode(){},setReduced(){},setPaused(){},setLayersVisible(){},show(){},dispose(){disposals++;}};}},
 },{document,window:{requestIdleCallback:fn=>{queued.set(++id,fn);return id;},cancelIdleCallback:key=>queued.delete(key)}});
 try{
  const tree=h.render(h.exports.DomainStage,{});findNode(tree,n=>n.props?.className==='domain-stage-map').props.ref.current={};h.commit();
  assert.equal(queued.size,0,'background tabs do not schedule a second WebGL renderer');
  assert.equal(starts,0);
  document.hidden=false;listeners.get('visibilitychange')();assert.equal(queued.size,1);
  document.hidden=true;listeners.get('visibilitychange')();assert.equal(queued.size,0,'hiding before idle cancels startup');
  document.hidden=false;listeners.get('visibilitychange')();
  const boot=[...queued.values()][0];queued.clear();boot();await settle();
  assert.equal(starts,1);
  document.hidden=true;listeners.get('visibilitychange')();document.hidden=false;listeners.get('visibilitychange')();
  assert.equal(queued.size,0);assert.equal(starts,1,'ordinary visibility changes reuse the existing map');
 }finally{h.dispose();}
 assert.equal(disposals,1);assert.equal(listeners.size,0);assert.equal(queued.size,0);
});

test('pointer highlights coalesce and stop on pause, reduced motion and dismissal',async()=>{
 const frames=new Map();let id=0,rects=0,writes=0;
 const globals={requestAnimationFrame:fn=>{frames.set(++id,fn);return id;},cancelAnimationFrame:key=>frames.delete(key)};
 const card={getBoundingClientRect:()=>{rects++;return {left:10,top:20};},style:{setProperty(){writes++;}}};
 const event={pointerType:'mouse',currentTarget:card,clientX:30,clientY:40};
 const h=await welcome(false,globals);
 const move=tree=>findNode(tree,n=>n.props?.className?.includes('topic-weather ')).props.onPointerMove(event);
 try{
  let tree=h.render();move(tree);move(tree);
  assert.equal(frames.size,1);assert.equal(rects,0,'pointer bursts do not force immediate layout');
  const paint=[...frames.values()][0];frames.clear();paint();assert.equal(rects,1);assert.equal(writes,2);
  move(tree);findNode(tree,n=>n.props?.['aria-label']==='Pause animation').props.onClick();tree=h.render();
  assert.equal(frames.size,0,'pausing cancels an already queued highlight');move(tree);assert.equal(frames.size,0);
  findNode(tree,n=>n.props?.['aria-label']==='Play animation').props.onClick();tree=h.render();move(tree);assert.equal(frames.size,1);
 }finally{h.harness.dispose();}
 assert.equal(frames.size,0,'dismissal cancels writes to detached cards');
 const quiet=await welcome(true,globals);
 try{move(quiet.render());assert.equal(frames.size,0,'reduced motion performs no highlight layout or paint');}finally{quiet.harness.dispose();}
});

test('comparison controls retain category identity, work with motion off, and reset for the next glimpse',async()=>{
 const h=await welcome(true);let tree=h.render();
 try{
  const open=id=>findNode(tree,n=>n.type==='button'&&n.props.className?.includes('topic-callout')&&n.props.className?.includes('topic-'+id)).props.onClick();
  open('history');tree=h.render();tree=openDetails(h,tree);
  findNode(tree,n=>n.props?.className==='welcome-text-action welcome-preview-action').props.onClick();tree=h.render();
  const toggle=byText(tree,'Hide starter layers');assert.ok(toggle);assert.equal(toggle.props.disabled,undefined);
  toggle.props.onClick();tree=h.render();
  assert.equal(findNode(tree,n=>n.type==='domain-stage').props.layersVisible,false);
  assert.equal(findNode(tree,n=>n.type==='domain-stage').props.topic,'history');
  assert.equal(findNode(tree,n=>n.type==='domain-stage').props.paused,true);
  byText(tree,'Show starter layers').props.onClick();tree=h.render();
  assert.equal(findNode(tree,n=>n.type==='domain-stage').props.layersVisible,true);
  byText(tree,'Hide starter layers').props.onClick();tree=h.render();
  findNode(tree,n=>n.props?.className==='welcome-preview-expand').props.onClick();tree=h.render();
  open('groundwater');tree=h.render();tree=openDetails(h,tree);
  findNode(tree,n=>n.props?.className==='welcome-text-action welcome-preview-action').props.onClick();tree=h.render();
  assert.equal(findNode(tree,n=>n.type==='domain-stage').props.layersVisible,true);
  assert.equal(findNode(tree,n=>n.type==='domain-stage').props.topic,'groundwater');
 }finally{h.harness.dispose();}
});

test('every category advertises its own glimpse and the expanded guide opens that category',async()=>{
 for(const topic of TOPIC_STRUCTURE){
  const h=await welcome();let tree=h.render();
  try{
   const card=findNode(tree,n=>n.type==='button'&&n.props.className?.includes('topic-callout')&&n.props.className?.includes('topic-'+topic.id));
   assert.equal(findNode(card,n=>n.props?.className==='topic-glimpse').props.children,categoryGlimpse(topic.id).title);
   card.props.onClick();tree=h.render();tree=openDetails(h,tree);
   findNode(tree,n=>n.type==='button'&&n.props.className==='welcome-text-action welcome-preview-action').props.onClick();tree=h.render();
   const guide=findNode(tree,n=>n.props?.['aria-label']==='Category demonstration');
   assert.ok(guide,topic.id);
   assert.equal(findNode(guide,n=>n.type==='h2').props.children,categoryGlimpse(topic.id).title);
   assert.equal(findNode(tree,n=>n.type==='domain-stage').props.topic,topic.id);
   if(topic.id==='weather'){
    const sourceNotes=findNode(guide,n=>n.type==='button'&&n.props.children==='Source notes & demonstrations');
    sourceNotes.props.onClick();tree=h.render();
    assert.equal(rootOf(tree).props['data-fullscreen'],true,'the notes trigger remains mounted for focus return');
    findNode(tree,n=>n.props?.['aria-label']==='Close exploration details').props.onClick();tree=h.render();
    assert.equal(rootOf(tree).props['data-fullscreen'],true);
   }
   findNode(guide,n=>n.type==='button'&&n.props.children==='Open this category’s map →').props.onClick();
   assert.deepEqual(h.calls,[['map',topic.id],['close',false]]);
  }finally{h.harness.dispose();}
 }
});

test('visual welcome owns focus and Escape before passive effects run',async()=>{
 const h=await welcome(),input={};
 const tree=h.harness.render(h.harness.exports.default,h.props);
 findNode(tree,node=>node.props?.className==='explorer-guide living-welcome').props.ref.current={
  contains:node=>node===input,
  querySelector:()=>({focus(){h.env.document.activeElement=input;}}),
 };
 try{
  // React commits layout effects before the browser can paint or dispatch
  // another key. Scene loading does not postpone keyboard ownership.
  h.harness.commitLayout();
  assert.equal(h.env.document.activeElement,input);
  const keyboard=h.env.listeners.get('keydown');
  assert.equal(typeof keyboard,'function');
  keyboard({target:{},key:'Escape'});
  assert.deepEqual(h.calls,[],'keys outside the non-modal welcome remain available');
  let prevented=false,stopped=false;
  keyboard({target:input,key:'Escape',preventDefault(){prevented=true;},stopImmediatePropagation(){stopped=true;}});
  assert.equal(prevented,true);assert.equal(stopped,true);
  assert.deepEqual(h.calls,[['close',false]]);
 }finally{h.harness.dispose();}
 assert.equal(h.env.listeners.has('keydown'),false);
});

test('Escape from expanded Pause restores a persistent control before the next key',async()=>{
 const h=await welcome();let tree=h.render();
 const expand={focus(){h.env.document.activeElement=this;}},pause={};
 rootOf(tree).props.ref.current={contains:node=>node===expand||node===pause,querySelector:selector=>selector==='.welcome-preview-expand'?expand:null};
 try{
  findNode(tree,node=>node.props?.className==='welcome-preview-expand').props.onClick();
  tree=h.harness.render(h.harness.exports.default,h.props);h.harness.commitLayout();
  assert.equal(h.env.document.activeElement,expand);
  h.env.document.activeElement=pause;
  const escape=()=>h.env.listeners.get('keydown')({target:h.env.document.activeElement,key:'Escape',preventDefault(){},stopImmediatePropagation(){}});
  escape();tree=h.harness.render(h.harness.exports.default,h.props);
  assert.equal(rootOf(tree).props['data-fullscreen'],false);
  assert.equal(findNode(tree,node=>node.props?.className==='welcome-preview-pause'),undefined);
  h.env.document.activeElement=h.env.document.body;h.harness.commitLayout();
  assert.equal(h.env.document.activeElement,expand,'the removed Pause button cannot strand focus on body');
  assert.deepEqual(h.calls,[]);escape();assert.deepEqual(h.calls,[['close',false]]);
 }finally{h.harness.dispose();}
});

test('nested welcome dialogs own and return keyboard focus in the layout commit',async()=>{
 const h=await welcome();let tree=h.render();
 const trigger={isConnected:true,focus(){h.env.document.activeElement=this;}};
 const close={focus(){h.env.document.activeElement=this;}};
 const root=findNode(tree,node=>node.props?.className==='explorer-guide living-welcome');
 root.props.ref.current={contains:node=>node===trigger,querySelector:()=>null};
 h.env.document.activeElement=trigger;
 byText(tree,'Map notes').props.onClick();
 tree=h.harness.render(h.harness.exports.default,h.props);
 findNode(tree,node=>node.props?.className==='welcome-dialog').props.ref.current={
  contains:node=>node===close,querySelector:()=>close,
 };
 try{
  h.harness.commitLayout();
  assert.equal(h.env.document.activeElement,close,'modal receives focus before passive effects');
  assert.equal(h.env.isolated,true,'background isolation is committed with modal focus');
  const escape=()=>h.env.listeners.get('keydown')({target:h.env.document.activeElement,key:'Escape',preventDefault(){},stopImmediatePropagation(){}});
  escape();
  tree=h.harness.render(h.harness.exports.default,h.props);
  assert.equal(findNode(tree,node=>node.props?.className==='welcome-dialog'),undefined);
  // Removing the focused dialog sends browser focus to the document body.
  h.env.document.activeElement=h.env.document.body;
  h.harness.commitLayout();
  assert.equal(h.env.document.activeElement,trigger,'closing returns focus before another key can arrive');
  assert.equal(h.env.isolated,false,'background isolation is restored before returning focus');
  assert.deepEqual(h.calls,[],'first Escape dismisses only the nested dialog');
  escape();
  assert.deepEqual(h.calls,[['close',false]],'a second immediate Escape reaches the welcome owner');
 }finally{h.harness.dispose();}
});

test('nested modal Tab wraps through eligible controls and a notes-only modal keeps its sole close',async()=>{
 for(const bodyControls of [0,2]){
  const h=await welcome();let tree=h.render();
  const trigger={isConnected:true,focus(){h.env.document.activeElement=this;}};
  const controls=Array.from({length:bodyControls+1},()=>({focus(){h.env.document.activeElement=this;}}));
  const root=rootOf(tree),panel={contains:node=>controls.includes(node),querySelector:()=>controls[0]};
  root.props.ref.current={contains:node=>node===trigger,querySelector:()=>null};
  h.env.document.activeElement=trigger;
  byText(tree,'Map notes').props.onClick();
  tree=h.harness.render(h.harness.exports.default,h.props);
  findNode(tree,node=>node.props?.className==='welcome-dialog').props.ref.current=panel;
  h.env.focusCandidates=actual=>{assert.equal(actual,panel);return controls;};
  try{
   h.harness.commitLayout();assert.equal(h.env.document.activeElement,controls[0]);
   const tab=shiftKey=>{let prevented=false;h.env.listeners.get('keydown')({target:h.env.document.activeElement,key:'Tab',shiftKey,preventDefault(){prevented=true;}});return prevented;};
   assert.equal(tab(true),true);assert.equal(h.env.document.activeElement,controls.at(-1),'reverse wrap uses the eligible last control');
   assert.equal(tab(false),true);assert.equal(h.env.document.activeElement,controls[0],'forward wrap returns to persistent close');
   if(bodyControls){h.env.document.activeElement=controls[1];assert.equal(tab(false),false,'native Tab handles interior controls');}
   assert.deepEqual(h.calls,[],'Tab does not close the welcome or invoke a workspace');
  }finally{h.harness.dispose();}
 }
});

test('welcome uses real search and draft actions without requests or implicit dismissal preferences',async()=>{
 const h=await welcome();let tree=h.render();assert.deepEqual(h.calls,[]);
 const input=findNode(tree,node=>node.type==='input'&&node.props.placeholder==='Find a county or place');
 input.props.onChange({target:{value:'Douglas County'}});tree=h.render();
 findNode(tree,node=>node.type==='form').props.onSubmit({preventDefault(){}});
 assert.deepEqual(h.calls.splice(0),[['search','Douglas County'],['close',false]]);
 tree=h.render();findNode(tree,node=>node.type==='input'&&node.props.type==='checkbox').props.onChange({target:{checked:true}});tree=h.render();
 const ask=findNode(tree,node=>node.type==='button'&&node.props.className==='welcome-ask');ask.props.onClick();
 assert.deepEqual(h.calls.splice(0),[['action','qwen'],['close',true]]);
 h.harness.dispose();
});

test('each topic links to its actual source workspace and preview selection does not activate layers',async()=>{
 for(const [id,target] of TOPIC_STRUCTURE.filter(t=>capabilityPreviews(t.id).length).map(t=>[t.id,t.id])){
  const h=await welcome();let tree=h.render();
  findNode(tree,node=>node.type==='button'&&node.props.className?.includes(`topic-${id} `)).props.onClick();tree=h.render();tree=openDetails(h,tree);
  const options=findNode(tree,node=>node.props?.className==='topic-options');
  options.props.children[1].props.onClick();tree=h.render();
  assert.equal(findNode(tree,node=>node.type==='capability-preview'&&node.props.demo?.id===capabilityPreviews(id)[1].id).props.demo.id,capabilityPreviews(id)[1].id);
  assert.deepEqual(h.calls,[],'scene selection is presentation only');
  byText(tree,'Preview in the welcome window →').props.onClick();tree=h.render();
  assert.equal(rootOf(tree).props['data-active'],id);assert.equal(findNode(tree,node=>node.type==='domain-stage').props.topic,id,'the pinned domain scene plays behind the cards');
  findNode(tree,node=>node.type==='button'&&node.props.className?.includes('topic-weather ')).props.onFocus();tree=h.render();
  assert.equal(rootOf(tree).props['data-active'],id,'explicit pin beats passive focus');
  findNode(tree,node=>node.type==='button'&&node.props.className?.includes(`topic-${id} `)).props.onClick();tree=h.render();tree=openDetails(h,tree);
  findNode(tree,node=>node.type==='button'&&[node.props.children].flat(Infinity).filter(x=>typeof x==='string').join('')===`Explore ${TOPIC_STRUCTURE.find(t=>t.id===id).title.toLowerCase()} sources →`).props.onClick();
  assert.deepEqual(h.calls,[['topic',target],['close',false]]);
  h.harness.dispose();
 }
});

test('pause and reduced motion stop media while detailed sources preserve the user’s current layers',async()=>{
 const h=await welcome();let tree=h.render();
 findNode(tree,node=>node.props?.['aria-label']==='Pause animation').props.onClick();tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='domain-stage').props.paused,true);
 assert.deepEqual(h.calls,[]);h.harness.dispose();
 const quiet=await welcome(true);tree=quiet.render();
 const still=findNode(tree,node=>node.type==='domain-stage');
 assert.equal(still.props.paused,true);assert.equal(still.props.reduced,true,'reduced motion renders a still frame');
 assert.equal(findNode(tree,node=>node.props?.['aria-label']==='Animations off: reduced motion preference').props.disabled,true);
 quiet.harness.dispose();
});

function featureClock() {
 let now=0,nextId=0,wakes=0;const timers=new Map(),listeners=new Map();
 const document={hidden:false,addEventListener:(type,fn)=>listeners.set(type,fn),removeEventListener:(type,fn)=>{if(listeners.get(type)===fn)listeners.delete(type);}};
 return {document,listeners,timers,get wakes(){return wakes;},
  globals:{document,setTimeout:(fn,ms)=>{const id=++nextId;timers.set(id,{fn,at:now+ms});return id;},clearTimeout:id=>timers.delete(id)},
  advance(ms){const until=now+ms;while(true){const due=[...timers].filter(([,v])=>v.at<=until).sort((a,b)=>a[1].at-b[1].at)[0];if(!due)break;now=due[1].at;timers.delete(due[0]);wakes++;due[1].fn();}now=until;},
  hidden(value){document.hidden=value;listeners.get('visibilitychange')?.();},
 };
}

test('tips can stay paused through pointer, focus and tab visibility changes; manual navigation still works',async()=>{
 const clock=featureClock(),calls=[];
 const h=await componentHarness('app/living-welcome/FeatureGuide.jsx',{'./features':{WELCOME_FEATURES:features}},clock.globals);
 const render=()=>{const tree=h.render(h.exports.WelcomeFeatureGuide,{onNavigate:value=>calls.push(value)});h.commit();return tree;};
 try{
  let tree=render();
  findNode(tree,node=>node.props?.['aria-label']==='Pause tips').props.onClick();tree=render();tree=render();
  assert.equal(clock.timers.size,0);
  assert.equal(findNode(tree,node=>node.props?.['aria-label']==='Resume tips').props['aria-pressed'],true);
  tree.props.onPointerEnter();tree=render();tree.props.onPointerLeave();tree=render();
  tree.props.onFocusCapture();tree=render();tree.props.onBlurCapture({currentTarget:{contains:()=>false},relatedTarget:null});tree=render();
  clock.hidden(true);clock.hidden(false);clock.advance(60000);tree=render();
  assert.equal(clock.timers.size,0,'explicit pause survives hover, focus and hidden-tab resume');
  findNode(tree,node=>node.props?.['aria-label']==='Next feature').props.onClick();tree=render();
  findNode(tree,node=>node.props?.tabIndex===0).props.onClick();assert.deepEqual(calls,[features[1].destination]);
  assert.equal(findNode(tree,node=>node.props?.tabIndex===-1).props.inert,true,'the offscreen clone cannot receive pointer or focus input');
  findNode(tree,node=>node.props?.['aria-label']==='Resume tips').props.onClick();tree=render();tree=render();
  clock.advance(6999);tree=render();assert.equal(tree.props['data-sliding'],false);
  clock.advance(1);tree=render();assert.equal(tree.props['data-sliding'],true,'resuming gives a complete reading interval');
 }finally{h.dispose();}
});

test('header feature scroll uses two deadlines, pauses on interest, and navigates only on a click',async()=>{
 const clock=featureClock(),calls=[];
 const h=await componentHarness('app/living-welcome/FeatureGuide.jsx',{'./features':{WELCOME_FEATURES:features}},clock.globals);
 const props={onNavigate:value=>calls.push(value)};
 const render=()=>{const tree=h.render(h.exports.WelcomeFeatureGuide,props);h.commit();return tree;};
 let tree=render();clock.advance(6999);tree=render();assert.equal(tree.props['data-sliding'],false);assert.equal(clock.wakes,0);
 clock.advance(1);tree=render();assert.equal(tree.props['data-sliding'],true);
 clock.advance(1150);tree=render();assert.equal(tree.props['data-sliding'],false);assert.equal(clock.wakes,2);
 tree.props.onPointerEnter();tree=render();tree=render();assert.equal(clock.timers.size,0);
 clock.advance(60000);assert.equal(clock.wakes,2);assert.deepEqual(calls,[]);
 const current=findNode(tree,node=>node.type==='button'&&node.props.tabIndex===0);current.props.onClick();assert.deepEqual(calls,[features[1].destination]);
 const next=findNode(tree,node=>node.type==='button'&&node.props.tabIndex===-1);assert.equal(next.props['aria-hidden'],true);
 h.dispose();assert.equal(clock.timers.size,0);assert.equal(clock.listeners.size,0);
});

test('an open category map holds the strip on its own hint: no rotation, no steppers, nothing to follow away',async()=>{
 const clock=featureClock(),calls=[];
 const h=await componentHarness('app/living-welcome/FeatureGuide.jsx',{'./features':{WELCOME_FEATURES:features}},clock.globals);
 let hint={title:'Hazard watch',text:'Select a fire detection to compare it with nearby fire reports.'};
 const render=()=>{const tree=h.render(h.exports.WelcomeFeatureGuide,{onNavigate:value=>calls.push(value),hint});h.commit();return tree;};
 let tree=render();tree=render();
 assert.equal(tree.props['data-hint'],'true');assert.equal(tree.props['aria-label'],'Hazard watch: what to try');
 assert.match(JSON.stringify(tree),/Hazard watch.*Select a fire detection/);
 assert.equal(findNode(tree,node=>node.type==='button'),undefined,'no steppers and no link away from the open map');
 assert.equal(clock.timers.size,0,'the hint does not rotate');clock.advance(60000);assert.equal(clock.wakes,0);assert.deepEqual(calls,[]);
 hint=null;tree=render();tree=render();
 assert.ok(findNode(tree,node=>node.props?.['aria-label']==='Next feature'),'leaving the map brings the tips back');
 assert.equal(clock.timers.size,1,'and their rotation');
 h.dispose();
});

test('feature rotation suspends while hidden, resumes a full dwell and resets after manual or paused input',async()=>{
 const clock=featureClock();
 const h=await componentHarness('app/living-welcome/FeatureGuide.jsx',{'./features':{WELCOME_FEATURES:features}},clock.globals);
 let paused=false;const render=()=>{const tree=h.render(h.exports.WelcomeFeatureGuide,{onNavigate(){},paused});h.commit();return tree;};
 let tree=render();clock.advance(7000);tree=render();assert.equal(tree.props['data-sliding'],true);
 clock.hidden(true);tree=render();assert.equal(tree.props['data-sliding'],false);assert.equal(clock.timers.size,0);
 clock.advance(60000);assert.equal(clock.wakes,1);clock.hidden(false);clock.advance(6999);tree=render();assert.equal(tree.props['data-sliding'],false);
 clock.advance(1);tree=render();assert.equal(tree.props['data-sliding'],true);
 findNode(tree,node=>node.props?.['aria-label']==='Next feature').props.onClick();tree=render();assert.equal(tree.props['data-sliding'],false);
 clock.advance(1150);tree=render();assert.equal(tree.props['data-sliding'],false);assert.equal(clock.wakes,2);
 paused=true;tree=render();tree=render();assert.equal(clock.timers.size,0);clock.advance(60000);assert.equal(clock.wakes,2);
 paused=false;render();assert.equal(clock.timers.size,1);h.dispose();assert.equal(clock.timers.size,0);assert.equal(clock.listeners.size,0);
});

test('feature rotation waits until both pointer and keyboard focus leave',async()=>{
 for(const lastToLeave of ['focus','pointer','cancel']){
  const clock=featureClock();
  const h=await componentHarness('app/living-welcome/FeatureGuide.jsx',{'./features':{WELCOME_FEATURES:features}},clock.globals);
  const render=()=>{let tree=h.render(h.exports.WelcomeFeatureGuide,{onNavigate(){}});h.commit();tree=h.render(h.exports.WelcomeFeatureGuide,{onNavigate(){}});h.commit();return tree;};
  try{
   let tree=render();tree.props.onPointerEnter();tree=render();tree.props.onFocusCapture();tree=render();
   tree.props.onBlurCapture({currentTarget:{contains:()=>true},relatedTarget:{}});tree=render();
   assert.equal(clock.timers.size,0,'focus within the guide remains held');
   const blur=()=>tree.props.onBlurCapture({currentTarget:{contains:()=>false},relatedTarget:null});
   if(lastToLeave==='focus')tree.props.onPointerLeave();else blur();
   tree=render();assert.equal(clock.timers.size,0,`${lastToLeave} still holds rotation`);
   clock.advance(60000);tree=render();assert.equal(clock.wakes,0);
   assert.equal(findNode(tree,node=>node.type==='button'&&node.props.tabIndex===0).props.children[1].props.children,'Roads');
   if(lastToLeave==='focus')blur();else if(lastToLeave==='cancel')tree.props.onPointerCancel();else tree.props.onPointerLeave();
   render();assert.equal(clock.timers.size,1);
   clock.advance(6999);tree=render();assert.equal(tree.props['data-sliding'],false);
   clock.advance(1);tree=render();assert.equal(tree.props['data-sliding'],true);
  }finally{h.dispose();}
  assert.equal(clock.timers.size,0);assert.equal(clock.listeners.size,0);
 }
});

test('production welcome handlers filter existing source UI and preserve URL/dismissal lifecycle',async()=>{
 const ast=ts.createSourceFile('app/page.tsx',await readFile('app/page.tsx','utf8'),ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX),callbacks=new Map();
 const visit=node=>{if(ts.isVariableDeclaration(node)&&node.initializer&&ts.isArrowFunction(node.initializer))callbacks.set(node.name.getText(ast),node.initializer.getText(ast));ts.forEachChild(node,visit);};visit(ast);
 const evaluate=(name,scope)=>new Function(...Object.keys(scope),ts.transpileModule(`return ${callbacks.get(name)};`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText)(...Object.values(scope));
 let calls=[];
 evaluate('runWelcomeTopic',{runExplorerGuideAction:x=>calls.push(['action',x]),setStarterPanelOpen:x=>calls.push(['starters',x]),setLayerCatalogView:x=>calls.push(['view',x]),setOfficialWorkspace:x=>calls.push(['topic',x])})('history');
 assert.deepEqual(calls,[['action','layers'],['starters',false],['view','official'],['topic','history']]);calls=[];
 evaluate('runWelcomeSearch',{setGlobalQuery:x=>calls.push(['query',x]),openAtlasComposer:(...x)=>calls.push(x)})('Riley County');
 assert.deepEqual(calls,[['query','Riley County'],['find','Riley County']]);calls=[];
 evaluate('runWelcomeFeature',{setGuideOpen:x=>calls.push(['open',x]),openSourceStatus:()=>calls.push(['status']),runWelcomeTopic:x=>calls.push(['topic',x])})('sources');
 assert.deepEqual(calls,[['open',false],['status']]);
});

test('every accepted motion asset is packaged with its provenance and Kansas history remains complete',async()=>{
 assert.equal(CATEGORY_IDS.length,8);let count=0;
 for(const category of CATEGORY_IDS){
  assert.equal(MOTION_CLIPS[category].length,SCENES[category].length);
  for(const clip of MOTION_CLIPS[category]){
   for(const key of ['src','preview','poster']){assert.match(clip[key],/^\/welcome\/motion\/[a-z0-9-]+\.(?:webm|jpg)$/);assert.ok((await readFile('public'+clip[key])).length>0);}
   assert.ok(clip.artist&&clip.sourceUrl&&clip.license);count++;
  }
 }
 assert.equal(count,30);
 const manifest=JSON.parse(await readFile('scripts/welcome-history/runtime-assets.json','utf8'));
 assert.equal(manifest.files.length,90);
 for(const file of manifest.files){const bytes=await readFile('public'+file.path);assert.equal(bytes.length,file.bytes);assert.equal(createHash('sha256').update(bytes).digest('hex'),file.sha256);}
 assert.equal(manifest.files.reduce((total,file)=>total+file.bytes,0),manifest.usedBytes);
 assert.equal(MOTION_CLIPS.history.length,6);
 assert.ok(MOTION_CLIPS.history.every(clip=>clip.historicalSourceUrl&&clip.mediaKind==='historical-map'));
 for(const clip of [MOTION_CLIPS.transport[1],MOTION_CLIPS.underground[1]]){assert.equal(clip.width,1920);assert.equal(clip.height,1080);assert.equal(clip.fps,30);}
});

test('hover focus isolates one topic and restores the scene after pointer focus leaves', async()=>{
 const h=await welcome(); let tree=h.render();
 const root=findNode(tree,node=>node.props?.className==='explorer-guide living-welcome');
 root.props.ref.current={querySelector:()=>null};
 const topic=findNode(tree,node=>node.type==='button'&&node.props.className?.includes('topic-weather '));
 topic.props.onPointerEnter({pointerType:'mouse'});tree=h.render();
 assert.equal(findNode(tree,node=>node.props?.className==='explorer-guide living-welcome').props['data-immersive'],true);
 assert.equal(rootOf(tree).props['data-active'],'weather');
 topic.props.onPointerLeave();await new Promise(resolve=>setTimeout(resolve,200));tree=h.render();
 assert.equal(findNode(tree,node=>node.props?.className==='explorer-guide living-welcome').props['data-immersive'],false);
 // A touch-generated focus must not leave an invisible hover state behind it.
 topic.props.onFocus({currentTarget:{matches:()=>false}});tree=h.render();
 assert.equal(rootOf(tree).props['data-active'],null);
 topic.props.onFocus({currentTarget:{matches:()=>true}});tree=h.render();
 assert.equal(rootOf(tree).props['data-active'],'weather');
 h.harness.dispose();
});

test('all shared domains expose their facets and actual destination without mounting a video',async()=>{
 const h=await welcome();let tree=h.render();
 for(const topic of TOPIC_STRUCTURE){
  findNode(tree,node=>node.type==='button'&&node.props.className?.includes(`topic-${topic.id} `)).props.onClick();tree=h.render();tree=openDetails(h,tree);
  const facets=findNode(tree,node=>node.props?.className==='capability-facets');
  assert.equal(facets.props.children.length,topic.facets.length);
  assert.equal(findNode(tree,node=>node.type==='video'),undefined);
  findNode(tree,node=>node.type==='button'&&[node.props.children].flat(Infinity).filter(x=>typeof x==='string').join('')===`Explore ${topic.title.toLowerCase()} sources →`).props.onClick();
  assert.deepEqual(h.calls.splice(0),[['topic',topic.id],['close',false]]);
 }
 h.harness.dispose();
});

test('Return from the full-window preview clears an engaged card even when no blur arrives',async()=>{
 const h=await welcome();let tree=h.render();
 const card=()=>findNode(tree,node=>node.type==='button'&&node.props.className?.includes('topic-history '));
 card().props.onFocus({currentTarget:{matches:()=>true}});tree=h.render();
 assert.equal(rootOf(tree).props['data-active'],'history');
 // Expanding hides the cards; Chrome can drop their focus without firing blur, so onBlur/release never runs.
 byText(tree,'Expand animation').props.onClick();tree=h.render();
 byText(tree,'Return to categories').props.onClick();tree=h.render();
 assert.equal(rootOf(tree).props['data-fullscreen'],false);
 assert.equal(rootOf(tree).props['data-active'],null,'Return leaves no card engaged');
 h.harness.dispose();
});

test('full-window preview returns to the same categories and uncaptured domains still get their own scene',async()=>{
 const h=await welcome();let tree=h.render();
 byText(tree,'Expand animation').props.onClick();tree=h.render();assert.equal(rootOf(tree).props['data-fullscreen'],true);
 byText(tree,'Return to categories').props.onClick();tree=h.render();assert.equal(rootOf(tree).props['data-fullscreen'],false);
 for(const id of ['sky','evidence']){
  findNode(tree,node=>node.type==='button'&&node.props.className?.includes(`topic-${id} `)).props.onPointerEnter({pointerType:'mouse'});tree=h.render();
  assert.equal(findNode(tree,node=>node.type==='domain-stage').props.topic,id);
  assert.match(capabilityNote(id),/No verified/,'no recorded capture is claimed for this domain');
 }
 h.harness.dispose();
});

test('a late blur cannot cancel a fine-pointer hover, while leaving restores all topics without a mouse-focus pin',async()=>{
 const h=await welcome();let tree=h.render(),hovered=true,finePointer=true;
 h.env.window.matchMedia=query=>({matches:query==='(hover: hover) and (pointer: fine)'?finePointer:false});
 findNode(tree,node=>node.props?.className==='explorer-guide living-welcome').props.ref.current={querySelector:selector=>selector==='.topic-callout:hover'&&hovered?{}:null};
 const weather=findNode(tree,node=>node.type==='button'&&node.props.className?.includes('topic-weather '));
 weather.props.onPointerEnter({pointerType:'mouse'});weather.props.onBlur();
 await new Promise(resolve=>setTimeout(resolve,200));tree=h.render();
 assert.equal(rootOf(tree).props['data-active'],'weather','late focus departure preserves the actual hover');
 hovered=false;weather.props.onPointerLeave();await new Promise(resolve=>setTimeout(resolve,200));tree=h.render();
 assert.equal(rootOf(tree).props['data-active'],null,'ordinary mouse focus does not pin an exited card');
 // Touch browsers may retain CSS :hover after a tap. That stale selector must
 // never keep every other topic hidden once touch focus has left.
 finePointer=false;hovered=true;weather.props.onPointerEnter({pointerType:'mouse'});weather.props.onBlur();
 await new Promise(resolve=>setTimeout(resolve,200));tree=h.render();
 assert.equal(rootOf(tree).props['data-active'],null,'coarse pointers ignore sticky CSS hover');
 h.harness.dispose();
});


test('keyboard focus and direct mouse topic changes coexist until focus and hover both leave',async()=>{
 const h=await welcome();let tree=h.render(),keyboardFocused=true,hovered=false;
 h.env.window.matchMedia=query=>({matches:query==='(hover: hover) and (pointer: fine)'});
 const keyboardTarget={};
 findNode(tree,node=>node.props?.className==='explorer-guide living-welcome').props.ref.current={querySelector:selector=>selector==='.topic-callout:focus-visible'&&keyboardFocused?keyboardTarget:selector==='.topic-callout:hover'&&hovered?{}:null};
 const card=id=>findNode(tree,node=>node.type==='button'&&node.props.className?.includes(`topic-${id} `));
 card('weather').props.onFocus({currentTarget:{matches:()=>true}});tree=h.render();
 assert.equal(rootOf(tree).props['data-active'],'weather');
 hovered=true;card('water').props.onPointerEnter({pointerType:'mouse'});tree=h.render();
 assert.equal(rootOf(tree).props['data-active'],'water','actual mouse entry selects the new topic while previous keyboard focus remains');
 card('water').props.onPointerLeave();card('science').props.onPointerEnter({pointerType:'mouse'});tree=h.render();
 assert.equal(rootOf(tree).props['data-active'],'science','latest direct mouse target wins');
 hovered=false;card('science').props.onPointerLeave();await new Promise(resolve=>setTimeout(resolve,200));tree=h.render();
 assert.equal(rootOf(tree).props['data-active'],'science','legitimate keyboard focus keeps the preview until it actually leaves');
 keyboardFocused=false;card('weather').props.onBlur();await new Promise(resolve=>setTimeout(resolve,200));tree=h.render();
 assert.equal(rootOf(tree).props['data-active'],null,'no stale focus or invisible hit region pins the preview');
 h.harness.dispose();
});

test('leaving a pinned full-window preview ends the preview and restores hover and the hero',async()=>{
 const h=await welcome();let tree=h.render();
 findNode(tree,node=>node.type==='button'&&node.props.className?.includes('topic-water ')).props.onClick();tree=h.render();tree=openDetails(h,tree);
 byText(tree,'Preview in the welcome window →').props.onClick();tree=h.render();
 assert.equal(rootOf(tree).props['data-fullscreen'],true);assert.equal(rootOf(tree).props['data-active'],'water');
 byText(tree,'Return to categories').props.onClick();tree=h.render();
 assert.equal(rootOf(tree).props['data-fullscreen'],false);
 assert.equal(rootOf(tree).props['data-active'],null,'no pin survives, so other cards can take over again');
 assert.equal(rootOf(tree).props['data-immersive'],false,'the hero and the other cards return');
 findNode(tree,node=>node.type==='button'&&node.props.className?.includes('topic-sky ')).props.onPointerEnter({pointerType:'mouse'});tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='domain-stage').props.topic,'sky');
 h.harness.dispose();
});

test('the live map shows the default map until a visitor points at a category, then that category\'s map',async()=>{
 const h=await welcome();let tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='domain-stage').props.topic,null,'no topic preview, and no opt-in provider, before a choice');
 assert.match(JSON.stringify(findNode(tree,node=>node.props?.className==='discovery-scene')),/Kansas/);
 findNode(tree,node=>node.type==='button'&&node.props.className?.includes('topic-aviation ')).props.onPointerEnter({pointerType:'mouse',currentTarget:{}});tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='domain-stage').props.topic,'aviation');
 assert.match(JSON.stringify(findNode(tree,node=>node.props?.className==='discovery-scene')),/Aviation chart/);
 assert.deepEqual(h.calls,[],'previewing a map changes nothing in the Explorer');
 h.harness.dispose();
});

test('aviation glimpse offers three views and truthful unavailable, hidden and edition states',async()=>{
 const h=await welcome();try{
  const render=props=>h.harness.exports.AviationGlimpse(props);
  const calls=[],props={mode:'3d',onMode:value=>calls.push(value),layersVisible:true};
  let tree=render(props);
  const group=findNode(tree,n=>n.props?.['aria-label']==='Airspace preview view');
  assert.deepEqual(Array.from(group.props.children,n=>n.props.children),['3D zones','2D chart','4,000 ft MSL']);
  group.props.children[2].props.onClick();assert.deepEqual(calls,['slice']);
  assert.match(findNode(tree,n=>n.props?.role==='status').props.children,/Loading the verified/);
  tree=render({...props,state:{aviation:{state:'unavailable'}}});assert.match(findNode(tree,n=>n.props?.role==='status').props.children,/unavailable/);
  tree=render({...props,layersVisible:false});assert.match(findNode(tree,n=>n.props?.role==='status').props.children,/hidden/);
  tree=render({...props,state:{aviation:{state:'ready',edition:{state:'PREVIEW',text:'Preview edition effective tomorrow.'},cycle:'2026-10-29',volumes:201}}});
  assert.match(findNode(tree,n=>n.props?.role==='status').props.children,/PREVIEW edition.*NASR 2026-10-29/);
  assert.match(JSON.stringify(findNode(tree,n=>n.props?.className==='welcome-aviation-notes')),/201.*airspace volumes.*Only zones are previewed here/);
 }finally{h.harness.dispose();}
});

test('Geology offers a compact source specimen without changing the workspace, and Underground opens only explicitly',async()=>{
 for(const entry of ['details','expanded']){
  const h=await welcome();try{
   let tree=h.render();const geology=findNode(tree,node=>node.type==='button'&&node.props.className?.includes('topic-geology '));
   geology.props.onFocus({currentTarget:{matches:()=>true}});tree=h.render();
   assert.deepEqual(h.calls,[],'a keyboard glimpse never selects workspace layers');
   findNode(tree,node=>node.type==='domain-stage').props.onGeologyModule({Component:'geology-glimpse'});tree=h.render();
   const hint=findNode(tree,node=>node.type==='geology-glimpse');assert.ok(hint);assert.equal(hint.props.expanded,undefined,'startup stays compact');
   findNode(tree,node=>node.type==='button'&&node.props.className?.includes('topic-geology ')).props.onClick();tree=h.render();tree=openDetails(h,tree);
   if(entry==='expanded'){
    byText(tree,'Preview in the welcome window →').props.onClick();tree=h.render();
    assert.equal(findNode(tree,node=>node.type==='geology-glimpse'),undefined,'compact owner unmounts when expanded owner takes over');
    assert.equal(findNode(tree,node=>node.type==='domain-stage').props.expanded,true);
   }
   byText(tree,'Open Underground Explorer →').props.onClick();
   assert.deepEqual(h.calls,[['action','underground'],['close',false]]);
  }finally{h.harness.dispose();}
 }
});

function intentClock(){
 let next=0;const jobs=new Map();
 return {jobs,setTimeout(fn,delay){const id=++next;jobs.set(id,{fn,delay});return id;},clearTimeout(id){jobs.delete(id);},fire(delay){for(const [id,job] of [...jobs])if(job.delay===delay){jobs.delete(id);job.fn();}}};
}
const gridCard=(tree,id)=>findNode(tree,n=>n.type==='button'&&n.props.className?.includes(`topic-${id} `));
const railCard=(tree,id)=>findNode(tree,n=>n.props?.className==='welcome-rail-card'&&n.props['data-topic']===id);

test('settled hover opens a stable stage, brief crossings cancel, and rail keeps every category',async()=>{
 const clock=intentClock(),h=await welcome(false,clock);
 try{
  let tree=h.render();gridCard(tree,'water').props.onPointerEnter({pointerType:'mouse'});tree=h.render();
  assert.equal(rootOf(tree).props['data-cinematic'],false,'hover immediately previews without moving the hit target');
  gridCard(tree,'water').props.onPointerLeave();clock.fire(650);tree=h.render();
  assert.equal(rootOf(tree).props['data-cinematic'],false,'crossing a card does not open the stage');
  gridCard(tree,'weather').props.onPointerEnter({pointerType:'mouse'});clock.fire(650);tree=h.render();
  assert.equal(rootOf(tree).props['data-cinematic'],true);
  gridCard(tree,'weather').props.onPointerLeave();clock.fire(180);tree=h.render();
  assert.equal(rootOf(tree).props['data-active'],'weather','grid disappearing cannot close or clear the chosen stage');
  const rail=findNode(tree,n=>n.props?.className==='welcome-rail-items');
  assert.equal(rail.props.children.length,TOPIC_STRUCTURE.length);
  for(const topic of TOPIC_STRUCTURE){
   railCard(tree,topic.id).props.onClick();tree=h.render();
   assert.equal(findNode(tree,n=>n.type==='domain-stage').props.topic,topic.id);
   assert.equal(railCard(tree,topic.id).props['aria-pressed'],true);
  }
  assert.deepEqual(h.calls,[],'choosing a preview does not enter a workspace or change published layers');
 }finally{h.harness.dispose();assert.equal(clock.jobs.size,0);}
});

test('touch click opens immediately, keyboard focus does not collapse the grid, and reduced motion stays paused',async()=>{
 const clock=intentClock(),h=await welcome(true,clock);
 try{
  let tree=h.render();gridCard(tree,'aviation').props.onPointerEnter({pointerType:'touch'});tree=h.render();
  assert.equal(clock.jobs.size,0);assert.equal(rootOf(tree).props['data-cinematic'],false);
  gridCard(tree,'aviation').props.onFocus({currentTarget:{matches:()=>true}});tree=h.render();
  assert.equal(rootOf(tree).props['data-cinematic'],false,'Tab keeps the navigation layout stable');
  gridCard(tree,'aviation').props.onClick();tree=h.render();
  assert.equal(rootOf(tree).props['data-cinematic'],true);assert.equal(rootOf(tree).props['data-active'],'aviation');
  assert.equal(findNode(tree,n=>n.type==='domain-stage').props.paused,true);
  assert.equal(findNode(tree,n=>n.props?.className==='welcome-preview-pause').props.disabled,true);
 }finally{h.harness.dispose();}
});

test('pending hover is cancelled by notes, hidden tab, and component disposal',async()=>{
 for(const reason of ['notes','hidden','dispose']){
  const clock=intentClock(),h=await welcome(false,clock);let disposed=false;
  try{
   let tree=h.render();gridCard(tree,'weather').props.onPointerEnter({pointerType:'mouse'});tree=h.render();
   assert.equal([...clock.jobs.values()].filter(j=>j.delay===650).length,1);
   if(reason==='notes')byText(tree,'Map notes').props.onClick();
   if(reason==='hidden'){h.env.document.hidden=true;h.env.listeners.get('visibilitychange')();}
   if(reason==='dispose'){h.harness.dispose();disposed=true;}
   assert.equal([...clock.jobs.values()].filter(j=>j.delay===650).length,0,reason);
   clock.fire(650);
   if(!disposed){tree=h.render();assert.equal(rootOf(tree).props['data-cinematic'],false);}
  }finally{if(!disposed)h.harness.dispose();}
 }
});

test('rail keyboard wraps and scroll controls honour paused motion',async()=>{
 const h=await welcome(true),focused=[],scrolled=[];
 try{
  let tree=h.render();gridCard(tree,'water').props.onClick();tree=h.render();
  const rail=findNode(tree,n=>n.props?.className==='welcome-rail-items');
  rail.props.ref.current={clientWidth:400,scrollBy:o=>scrolled.push(o),querySelector:selector=>({focus:()=>focused.push(selector),scrollIntoView(){}})};
  let prevented=0;
  const key=(id,key)=>{railCard(tree,id).props.onKeyDown({key,preventDefault(){prevented++;}});tree=h.render();};
  key('water','Home');assert.equal(rootOf(tree).props['data-active'],TOPIC_STRUCTURE[0].id);
  key(TOPIC_STRUCTURE[0].id,'ArrowLeft');assert.equal(rootOf(tree).props['data-active'],TOPIC_STRUCTURE.at(-1).id);
  key(TOPIC_STRUCTURE.at(-1).id,'ArrowRight');assert.equal(rootOf(tree).props['data-active'],TOPIC_STRUCTURE[0].id);
  key(TOPIC_STRUCTURE[0].id,'End');assert.equal(rootOf(tree).props['data-active'],TOPIC_STRUCTURE.at(-1).id);
  assert.equal(prevented,4);assert.equal(focused.length,4);
  findNode(tree,n=>n.props?.['aria-label']==='Scroll categories right').props.onClick();
  findNode(tree,n=>n.props?.['aria-label']==='Scroll categories left').props.onClick();
  assert.deepEqual(scrolled.map(o=>[o.left,o.behavior]),[[300,'instant'],[-300,'instant']]);
 }finally{h.harness.dispose();}
});

test('Return restores the original card and grid scroll before another Escape dismisses welcome',async()=>{
 const h=await welcome(),focus=[];let tree=h.render();
 const card={focus(){focus.push('card');h.env.document.activeElement=card;}},back={focus(){focus.push('return');h.env.document.activeElement=back;}};
 const root={scrollTop:680,contains:()=>true,querySelector:selector=>selector==='.topic-water'?card:selector==='.welcome-preview-expand'?back:null};
 rootOf(tree).props.ref.current=root;
 try{
  gridCard(tree,'water').props.onClick();tree=h.render();assert.equal(root.scrollTop,0);assert.equal(focus.at(-1),'return');
  railCard(tree,'sky').props.onClick();tree=h.render();
  byText(tree,'Return to categories').props.onClick();tree=h.render();
  assert.equal(focus.at(-1),'card');assert.equal(root.scrollTop,680);assert.equal(rootOf(tree).props['data-active'],null);
  h.env.listeners.get('keydown')({target:card,key:'Escape',preventDefault(){},stopImmediatePropagation(){}});
  assert.deepEqual(h.calls,[['close',false]]);
 }finally{h.harness.dispose();}
});

test('keyboard interest cancels a pending pointer takeover and selecting the current rail item preserves comparison',async()=>{
 const clock=intentClock(),h=await welcome(false,clock);
 try{
  let tree=h.render();gridCard(tree,'weather').props.onPointerEnter({pointerType:'mouse'});
  gridCard(tree,'history').props.onFocus({currentTarget:{matches:()=>true}});clock.fire(650);tree=h.render();
  assert.equal(rootOf(tree).props['data-cinematic'],false);assert.equal(rootOf(tree).props['data-active'],'history');
  gridCard(tree,'history').props.onClick();tree=h.render();byText(tree,'Hide starter layers').props.onClick();tree=h.render();
  railCard(tree,'history').props.onClick();tree=h.render();assert.equal(findNode(tree,n=>n.type==='domain-stage').props.layersVisible,false);
  railCard(tree,'water').props.onClick();tree=h.render();assert.equal(findNode(tree,n=>n.type==='domain-stage').props.layersVisible,true);
 }finally{h.harness.dispose();}
});
