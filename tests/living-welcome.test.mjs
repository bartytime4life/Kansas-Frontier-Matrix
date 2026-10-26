import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';
import { SCENES, CATEGORY_IDS, HISTORY_ERAS, sceneArt } from '../app/living-welcome/catalog.mjs';
import { MOTION_CLIPS, motionClip } from '../app/living-welcome/motion-catalog.mjs';

import { capabilityPreviews, capabilityNote } from '../app/living-welcome/capability-catalog.mjs';
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
async function welcome(reduced=false){
 const env=environment(reduced),calls=[];
 const harness=await componentHarness('app/living-welcome/welcome.jsx',{
  'react-dom':{createPortal:content=>content},'../layer-workspaces':{TOPIC_STRUCTURE,TOPIC_GROUPS},'../category-maps':categoryModule,'./capability-catalog.mjs':{capabilityPreviews,capabilityNote},'./CapabilityPreview.jsx':{CapabilityPreview:'capability-preview'},'./DomainStage.jsx':{DomainStage:'domain-stage'},'../welcome-map-view':{welcomeView:topic=>({topic,name:topic?categoryModule.CATEGORY_MAPS[topic]?.name??topic:'Kansas'})},'./catalog.mjs':{SCENES,HISTORY_ERAS,sceneArt},'./motion-catalog.mjs':{MOTION_CLIPS,motionClip},
  './MotionAtlas.jsx':{MotionAtlas:'motion-atlas'},'./ScenePreview.jsx':{ScenePreview:'scene-preview'},'./MapDemoPanel.jsx':{MapDemoPanel:'map-demo-panel'},
  './FeatureGuide.jsx':{WelcomeFeatureGuide:'feature-guide'},'../modal-background':{isolateModalBackground:()=>{env.isolated=true;return()=>{env.isolated=false;};},modalFocusableElements:panel=>env.focusCandidates?.(panel)||[]},
 },env);
 const props={onClose:value=>calls.push(['close',value]),onAction:value=>calls.push(['action',value]),onMore:()=>calls.push(['help']),onSearch:value=>calls.push(['search',value]),onTopic:value=>calls.push(['topic',value]),onMap:value=>calls.push(['map',value])};
 const render=()=>{const tree=harness.render(harness.exports.default,props);harness.commit();return tree;};
 return {harness,props,calls,render,env};
}
const byText=(tree,text)=>findNode(tree,node=>node.type==='button'&&node.props.children===text);

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
  findNode(tree,node=>node.type==='button'&&node.props.className?.includes(`topic-${id} `)).props.onClick();tree=h.render();
  const options=findNode(tree,node=>node.props?.className==='topic-options');
  options.props.children[1].props.onClick();tree=h.render();
  assert.equal(findNode(tree,node=>node.type==='capability-preview'&&node.props.demo?.id===capabilityPreviews(id)[1].id).props.demo.id,capabilityPreviews(id)[1].id);
  assert.deepEqual(h.calls,[],'scene selection is presentation only');
  byText(tree,'Preview in the welcome window →').props.onClick();tree=h.render();
  assert.equal(rootOf(tree).props['data-active'],id);assert.equal(findNode(tree,node=>node.type==='domain-stage').props.topic,id,'the pinned domain scene plays behind the cards');
  findNode(tree,node=>node.type==='button'&&node.props.className?.includes('topic-weather ')).props.onFocus();tree=h.render();
  assert.equal(rootOf(tree).props['data-active'],id,'explicit pin beats passive focus');
  findNode(tree,node=>node.type==='button'&&node.props.className?.includes(`topic-${id} `)).props.onClick();tree=h.render();
  findNode(tree,node=>node.type==='button'&&node.props.className==='welcome-text-action').props.onClick();
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
  findNode(tree,node=>node.type==='button'&&node.props.className?.includes(`topic-${topic.id} `)).props.onClick();tree=h.render();
  const facets=findNode(tree,node=>node.props?.className==='capability-facets');
  assert.equal(facets.props.children.length,topic.facets.length);
  assert.equal(findNode(tree,node=>node.type==='video'),undefined);
  findNode(tree,node=>node.type==='button'&&node.props.className==='welcome-text-action').props.onClick();
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
 findNode(tree,node=>node.type==='button'&&node.props.className?.includes('topic-water ')).props.onClick();tree=h.render();
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
