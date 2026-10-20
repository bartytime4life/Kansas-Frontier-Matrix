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
  './MotionAtlas.jsx':{MotionAtlas:'motion-atlas'},'./ScenePreview.jsx':{ScenePreview:'scene-preview'},
  './FeatureGuide.jsx':{WelcomeFeatureGuide:'feature-guide'},'../modal-background':{isolateModalBackground:()=>()=>{}},
 },env);
 const props={onClose:value=>calls.push(['close',value]),onAction:value=>calls.push(['action',value]),onMore:()=>calls.push(['help']),onSearch:value=>calls.push(['search',value]),onTopic:value=>calls.push(['topic',value]),questions:'preserved questions'};
 const render=()=>{const tree=harness.render(harness.exports.default,props);harness.commit();return tree;};
 return {harness,props,calls,render,env};
}
const byText=(tree,text)=>findNode(tree,node=>node.type==='button'&&node.props.children===text);

test('visual welcome owns focus and Escape before passive effects run after the fallback handoff',async()=>{
 const h=await welcome(),input={};
 const tree=h.harness.render(h.harness.exports.default,h.props);
 tree.props.ref.current={
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

test('header feature scroll dwells, pauses on interest, and only navigates on an explicit click',async()=>{
 let now=0,tick;const calls=[];
 const h=await componentHarness('app/living-welcome/FeatureGuide.jsx',{'./features':{WELCOME_FEATURES:features}},{performance:{now:()=>now},setInterval:fn=>{tick=fn;return 1;},clearInterval(){},document:{hidden:false}});
 const props={onNavigate:value=>calls.push(value)};
 const render=()=>{const tree=h.render(h.exports.WelcomeFeatureGuide,props);h.commit();return tree;};
 let tree=render();for(let i=0;i<46;i++){now+=150;tick();}tree=render();assert.equal(tree.props['data-sliding'],false);
 now+=150;tick();tree=render();assert.equal(tree.props['data-sliding'],true);
 tree.props.onPointerEnter();tree=render();tree=render();assert.equal(tree.props['data-sliding'],false);
 assert.deepEqual(calls,[]);
 const current=findNode(tree,node=>node.type==='button'&&node.props.tabIndex===0);current.props.onClick();assert.deepEqual(calls,['transport']);
 const next=findNode(tree,node=>node.type==='button'&&node.props.tabIndex===-1);assert.equal(next.props['aria-hidden'],true);
 h.dispose();
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
 assert.equal(manifest.files.reduce((total,file)=>total+file.bytes,0),82380456);
 assert.equal(MOTION_CLIPS.history.length,6);
 assert.ok(MOTION_CLIPS.history.every(clip=>clip.historicalSourceUrl&&clip.mediaKind==='historical-map'));
 for(const clip of [MOTION_CLIPS.transport[1],MOTION_CLIPS.underground[1]]){assert.equal(clip.width,1920);assert.equal(clip.height,1080);assert.equal(clip.fps,30);}
});
