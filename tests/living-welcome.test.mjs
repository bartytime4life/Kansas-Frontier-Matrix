import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';
import { SCENES, CATEGORY_IDS, HISTORY_ERAS, sceneArt } from '../app/living-welcome/catalog.mjs';
import { MOTION_CLIPS, motionClip } from '../app/living-welcome/motion-catalog.mjs';

const features=[{id:'roads',status:'Explore',description:'Roads',destination:'transport'},{id:'farms',status:'Explore',description:'Farms',destination:'agriculture'}];
function environment(reduced=false){
 const listeners=new Map(),media={matches:reduced,addEventListener(){},removeEventListener(){}};
 return {window:{matchMedia:()=>media},document:{hidden:false,body:{},querySelector:()=>null,activeElement:null,addEventListener:(id,fn)=>listeners.set(id,fn),removeEventListener:id=>listeners.delete(id)},listeners};
}
async function welcome(reduced=false){
 const env=environment(reduced),calls=[];
 const harness=await componentHarness('app/living-welcome/welcome.jsx',{
  'react-dom':{createPortal:content=>content},'./catalog.mjs':{SCENES,HISTORY_ERAS,sceneArt},'./motion-catalog.mjs':{MOTION_CLIPS,motionClip},
  './MotionAtlas.jsx':{MotionAtlas:'motion-atlas'},'./ScenePreview.jsx':{ScenePreview:'scene-preview'},'./MapDemoPanel.jsx':{MapDemoPanel:'map-demo-panel'},
  './FeatureGuide.jsx':{WelcomeFeatureGuide:'feature-guide'},'../modal-background':{isolateModalBackground:()=>{env.isolated=true;return()=>{env.isolated=false;};}},
 },env);
 const props={onClose:value=>calls.push(['close',value]),onAction:value=>calls.push(['action',value]),onMore:()=>calls.push(['help']),onSearch:value=>calls.push(['search',value]),onTopic:value=>calls.push(['topic',value]),questions:'preserved questions'};
 const render=()=>{const tree=harness.render(harness.exports.default,props);harness.commit();return tree;};
 return {harness,props,calls,render,env};
}
const byText=(tree,text)=>findNode(tree,node=>node.type==='button'&&node.props.children===text);

test('visual welcome owns focus and Escape before passive effects run after the fallback handoff',async()=>{
 const h=await welcome(),input={};
 const tree=h.harness.render(h.harness.exports.default,h.props);
 findNode(tree,node=>node.props?.className==='explorer-guide living-welcome').props.ref.current={
  contains:node=>node===input,
  querySelector:()=>({focus(){h.env.document.activeElement=input;}}),
 };
 try{
  // React commits layout effects before the browser can paint or dispatch
  // another key. Passive effects may run later, after the fallback is gone.
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
 byText(tree,'Scene credits').props.onClick();
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
 for(const [id,target] of [['weather','weather'],['rivers','water'],['science','science'],['underground','groundwater'],['history','history'],['transport','transport'],['farming','agriculture'],['government','land']]){
  const h=await welcome();let tree=h.render();
  findNode(tree,node=>node.type==='button'&&node.props.className?.includes(`topic-${id} `)).props.onClick();tree=h.render();
  const options=findNode(tree,node=>node.props?.className==='topic-options');
  options.props.children[1].props.onClick();tree=h.render();
  assert.equal(findNode(tree,node=>node.type==='scene-preview').props.index,1);
  assert.deepEqual(h.calls,[],'scene selection is presentation only');
  byText(tree,'Preview this scene on the map →').props.onClick();tree=h.render();
  let atlas=findNode(tree,node=>node.type==='motion-atlas');assert.equal(atlas.props.active,id);assert.equal(atlas.props.manual,1);
  findNode(tree,node=>node.type==='button'&&node.props.className?.includes('topic-weather ')).props.onFocus();tree=h.render();
  atlas=findNode(tree,node=>node.type==='motion-atlas');assert.equal(atlas.props.active,id,'explicit pin beats passive focus');
  findNode(tree,node=>node.type==='button'&&node.props.className?.includes(`topic-${id} `)).props.onClick();tree=h.render();
  findNode(tree,node=>node.type==='button'&&node.props.className==='welcome-text-action').props.onClick();
  assert.deepEqual(h.calls,[['topic',target],['close',false]]);
  h.harness.dispose();
 }
});

test('pause and reduced motion stop media while detailed sources preserve the user’s current layers',async()=>{
 const h=await welcome();let tree=h.render();
 findNode(tree,node=>node.props?.['aria-label']==='Pause animation').props.onClick();tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='motion-atlas').props.paused,true);
 assert.deepEqual(h.calls,[]);h.harness.dispose();
 const quiet=await welcome(true);tree=quiet.render();
 assert.equal(findNode(tree,node=>node.type==='motion-atlas').props.paused,true);
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
 assert.equal(findNode(tree,node=>node.type==='motion-atlas').props.active,'weather');
 topic.props.onPointerLeave();await new Promise(resolve=>setTimeout(resolve,200));tree=h.render();
 assert.equal(findNode(tree,node=>node.props?.className==='explorer-guide living-welcome').props['data-immersive'],false);
 // A touch-generated focus must not leave an invisible hover state behind it.
 topic.props.onFocus({currentTarget:{matches:()=>false}});tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='motion-atlas').props.active,null);
 topic.props.onFocus({currentTarget:{matches:()=>true}});tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='motion-atlas').props.active,'weather');
 h.harness.dispose();
});

test('each topic exposes recorded demos and hands its selected tool to the existing destination',async()=>{
 const h=await welcome();let tree=h.render();
 findNode(tree,node=>node.type==='button'&&node.props.className?.includes('topic-weather ')).props.onClick();tree=h.render();
 const demos=findNode(tree,node=>node.type==='map-demo-panel');assert.equal(demos.props.category,'weather');
 demos.props.onPlaybackChange(true);tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='scene-preview').props.paused,true,'decorative footage yields to the actual map demonstration');
 demos.props.onTry({destination:{kind:'topic',value:'weather'}});
 assert.deepEqual(h.calls,[['topic','weather'],['close',false]]);h.harness.dispose();
});


test('a late blur cannot cancel a fine-pointer hover, while leaving restores all topics without a mouse-focus pin',async()=>{
 const h=await welcome();let tree=h.render(),hovered=true,finePointer=true;
 h.env.window.matchMedia=query=>({matches:query==='(hover: hover) and (pointer: fine)'?finePointer:false});
 findNode(tree,node=>node.props?.className==='explorer-guide living-welcome').props.ref.current={querySelector:selector=>selector==='.topic-callout:hover'&&hovered?{}:null};
 const weather=findNode(tree,node=>node.type==='button'&&node.props.className?.includes('topic-weather '));
 weather.props.onPointerEnter({pointerType:'mouse'});weather.props.onBlur();
 await new Promise(resolve=>setTimeout(resolve,200));tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='motion-atlas').props.active,'weather','late focus departure preserves the actual hover');
 hovered=false;weather.props.onPointerLeave();await new Promise(resolve=>setTimeout(resolve,200));tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='motion-atlas').props.active,null,'ordinary mouse focus does not pin an exited card');
 // Touch browsers may retain CSS :hover after a tap. That stale selector must
 // never keep every other topic hidden once touch focus has left.
 finePointer=false;hovered=true;weather.props.onPointerEnter({pointerType:'mouse'});weather.props.onBlur();
 await new Promise(resolve=>setTimeout(resolve,200));tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='motion-atlas').props.active,null,'coarse pointers ignore sticky CSS hover');
 h.harness.dispose();
});


test('keyboard focus and direct mouse topic changes coexist until focus and hover both leave',async()=>{
 const h=await welcome();let tree=h.render(),keyboardFocused=true,hovered=false;
 h.env.window.matchMedia=query=>({matches:query==='(hover: hover) and (pointer: fine)'});
 const keyboardTarget={};
 findNode(tree,node=>node.props?.className==='explorer-guide living-welcome').props.ref.current={querySelector:selector=>selector==='.topic-callout:focus-visible'&&keyboardFocused?keyboardTarget:selector==='.topic-callout:hover'&&hovered?{}:null};
 const card=id=>findNode(tree,node=>node.type==='button'&&node.props.className?.includes(`topic-${id} `));
 card('weather').props.onFocus({currentTarget:{matches:()=>true}});tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='motion-atlas').props.active,'weather');
 hovered=true;card('rivers').props.onPointerEnter({pointerType:'mouse'});tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='motion-atlas').props.active,'rivers','actual mouse entry selects the new topic while previous keyboard focus remains');
 card('rivers').props.onPointerLeave();card('science').props.onPointerEnter({pointerType:'mouse'});tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='motion-atlas').props.active,'science','latest direct mouse target wins');
 hovered=false;card('science').props.onPointerLeave();await new Promise(resolve=>setTimeout(resolve,200));tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='motion-atlas').props.active,'science','legitimate keyboard focus keeps the preview until it actually leaves');
 keyboardFocused=false;card('weather').props.onBlur();await new Promise(resolve=>setTimeout(resolve,200));tree=h.render();
 assert.equal(findNode(tree,node=>node.type==='motion-atlas').props.active,null,'no stale focus or invisible hit region pins the preview');
 h.harness.dispose();
});
