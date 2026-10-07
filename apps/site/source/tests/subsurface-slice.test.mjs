import assert from 'node:assert/strict';
import test from 'node:test';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';
import * as Three from 'three';
import {componentHarness,findNode,settle} from './component-harness.mjs';
const compile=source=>ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
async function module(name,imports={}){const exports={};vm.runInNewContext(compile(await readFile(`app/${name}.ts`,'utf8')),{exports,URL,require:name=>{assert.ok(name in imports,name);return imports[name];}});return exports;}
const materials=await module('subsurface-materials');
const model=await module('subsurface-model',{'./subsurface-materials':materials});
const slices=await module('subsurface-slice',{'./subsurface-model':model});
const record={id:'well-a',sourceId:'kgs-wwc5',kind:'well',name:'WWC5 A',coordinates:[-100.5,38.5],coordinateReference:'WGS84',locationMethod:'approximate',sourceUrl:'https://example.test/a',sourceTime:'1990-01-01',depthUnit:'m',depthReference:'land-surface',totalDepth:30,intervals:[{top:0,bottom:10,description:'sand'},{top:20,bottom:30,description:'clay'}]};
const other={...record,id:'well-b',name:'WWC5 B',intervals:[{top:100,bottom:180,description:'shale'}]};
const empty={...record,id:'empty',name:'Empty log',intervals:[]};
const style=new Proxy({},{get:(_,key)=>String(key)});
const text=node=>typeof node==='string'||typeof node==='number'?String(node):[node?.props?.children].flat(Infinity).filter(Boolean).map(text).join(' ');
const button=(tree,name)=>findNode(tree,node=>node.type==='button'&&text(node).includes(name));
const same=(actual,expected)=>assert.deepEqual(JSON.parse(JSON.stringify(actual)),expected);

test('deliberate entry fits actual recorded metres and opens inside a real interval',()=>{
  same(slices.fitRecordedSlice(record,0),{range:[0,30],depth:5,intervalIndex:0});
  assert.equal(slices.fitRecordedSlice(record,7).depth,7,'useful user depth is retained');
  const thinSoil={...record,intervals:[{top:0,bottom:.1,description:'topsoil'},{top:.1,bottom:100,description:'sand'}]};
  assert.equal(slices.fitRecordedSlice(thinSoil,0).depth,50.05,'default slice should visibly cut the log, not skim a thin surface');
  const largeGap={...record,intervals:[{top:0,bottom:1,description:'sand'},{top:99,bottom:100,description:'clay'}]};
  const gapDepth=slices.fitRecordedSlice(largeGap,0).depth;assert.ok(gapDepth<1||gapDepth>99,'large gaps stay empty');
  assert.equal(slices.fitRecordedSlice(record,15).depth,5,'gaps are not invented material');
  same(slices.fitRecordedSlice(record,7,1),{range:[0,30],depth:25,intervalIndex:1});
  const feet={...record,depthUnit:'ft',intervals:[{top:100,bottom:200,description:'sand'}]};
  const fit=slices.fitRecordedSlice(feet,0);assert.ok(Math.abs(fit.depth-45.72)<1e-10);assert.ok(Math.abs(fit.range[1]-60.96)<1e-10);
});
test('invalid, degenerate, empty and out-of-window rows cannot create a slice or mutate original input',()=>{
  const invalid={...record,intervals:[{top:NaN,bottom:2},{top:5,bottom:5},{top:10,bottom:0},{top:-1,bottom:2},{top:13000,bottom:14000}]};
  assert.equal(slices.fitRecordedSlice(invalid,0),null);assert.equal(slices.fitRecordedSlice(empty,0),null);
  const original=JSON.stringify(record),rows=slices.sliceIntervals(record,[22,28]);
  assert.equal(rows.length,1);assert.equal(rows[0].interval,record.intervals[1]);assert.equal(rows[0].index,1);same([rows[0].top,rows[0].bottom],[22,28]);assert.equal(JSON.stringify(record),original);
  for(const window of [[8,8],[-1,10],[0,Infinity],[0,13000]])assert.equal(slices.sliceIntervals(record,window).length,0);
});
test('core inventory remains an envelope and original interval identity survives fitting',()=>{
  const core={...other,kind:'core'};const fit=slices.fitRecordedSlice(core,1);
  assert.equal(fit.depth,140);assert.equal(slices.sliceIntervals(core)[fit.intervalIndex].interval,core.intervals[0]);
  assert.equal(materials.materialFor(core.intervals[0],core.kind),'inventory');
});

async function panelHarness(initialContext=null,{failWorker=false}={}){
  const messages=[],inspections=[],contexts=[],timers=new Map(),focusCalls=[];let timerSerial=0;const worker={postMessage:message=>messages.push(message),terminate(){}};
  const h=await componentHarness('app/underground-panel.tsx',{'./subsurface-model':model,'./subsurface-materials':materials,'./subsurface-slice':slices,'./subsurface.module.css':{default:style},'./subsurface-workers':{startSubsurfaceWorker:()=>{if(failWorker)throw new Error("unavailable");return worker;}},'./cutaway-locator':{cutawayLocatorPlacement(){}}},{
    matchMedia:()=>({matches:true,addEventListener(){},removeEventListener(){}}),document:{hidden:false,addEventListener(){},removeEventListener(){}},queueMicrotask,performance,
    fetch:async()=>({ok:true,json:async()=>({version:1,surveys:[]})}),setTimeout:callback=>{const id=++timerSerial;timers.set(id,callback);return id;},clearTimeout:id=>timers.delete(id),
  });
  const props={map:null,initialContext,year:2026,redacted:false,onFlatMap(){},onTerrain(){},readElevation(){return null;},isDrawing(){return false;},onDraw(){},readTransect(){return[];},onContext:context=>contexts.push(context),onInspect:value=>inspections.push(value),onClose(){},onSave(){},onReport(){}};
  let tree;const render=()=>{tree=h.render(h.exports.default,props);const destination=findNode(tree,node=>node.props?.['aria-label']==='Slice a recorded column');if(destination)destination.props.ref.current={focus:options=>focusCalls.push(options)};h.commit();return tree;};render();const flushTimers=()=>{for(const [id,fn] of [...timers]){timers.delete(id);fn();}};flushTimers();
  if (!initialContext || initialContext.display === 'aquifer') { findNode(tree,node=>node.props?.onArea).props.onArea([-100.7,38.3,-100.3,38.7]);render();flushTimers(); }
  const load=(records=[record,other,empty])=>{worker.onmessage({data:{id:messages.at(-1).id,bounds:messages.at(-1).bounds,manifest:{sources:[],totals:{},counties:[]},columns:records.map(record=>({record,distanceMeters:0,alongMeters:0,offsetMeters:0})),coverage:'loaded'}});return render();};if(!failWorker)load();
  const aquifer=()=>findNode(tree,node=>node.props?.sliceEntry);
  const viewer=()=>findNode(tree,node=>node.props?.onSlice);
  return{h,render,load,aquifer,viewer,inspections,contexts,focusCalls,messages,worker,flushTimers,props,get tree(){return tree;}};
}
test('cutaway offers a named loaded record and preserves a picked interval when opening the slice',async()=>{
  const p=await panelHarness();let entry=p.aquifer().props.sliceEntry;
  assert.equal(findNode(entry,n=>n.type==='select').props.value,record.id);
  assert.match(text(entry),/WWC5 A/);
  p.aquifer().props.onInspect(record,record.intervals[1]);p.render();entry=p.aquifer().props.sliceEntry;
  button(entry,'Open selected log').props.onClick();p.render();const view=p.viewer();
  assert.equal(view.props.record,record);assert.equal(view.props.selectedIndex,1);assert.equal(view.props.slice,true);assert.equal(view.props.depth,25);same(view.props.depthRange,[0,30]);
  assert.equal(p.inspections.at(-1).interval,record.intervals[1]);
  const body=findNode(p.tree,n=>n.props?.['data-underground-scroll']!==undefined),children=body.props.children.flat(Infinity).filter(Boolean);
  assert.equal(children[0].type,'nav');assert.equal(children[1].props['aria-label'],'Slice a recorded column');
  assert.match(text(children[0]),/Individual log/);assert.doesNotMatch(text(p.tree),/Depth cursor/);
  const range=view.props.depthRange;view.props.onDepth(27);p.render();assert.equal(p.viewer().props.depthRange,range);assert.equal(p.viewer().props.depth,27);
  p.viewer().props.onInspect(record.intervals[0]);p.render();assert.equal(p.viewer().props.depth,27,'source inspection does not move cut plane');assert.equal(p.viewer().props.selectedIndex,0);
  p.viewer().props.onSlice(false);p.render();p.viewer().props.onSlice(true);p.render();assert.equal(p.viewer().props.depth,27,'inspection must not override a useful slice cursor when re-enabled');
  p.h.dispose();
});
test('slice remains enabled across record selection and refits instead of showing an empty model',async()=>{
  const p=await panelHarness();button(p.aquifer().props.sliceEntry,'Open selected log').props.onClick();p.render();
  findNode(p.tree,n=>n.props?.['aria-label']==='Slice source record').props.onChange({target:{value:other.id}});p.render();
  assert.equal(p.viewer().props.record,other);assert.equal(p.viewer().props.slice,true);assert.equal(p.viewer().props.depth,140);same(p.viewer().props.depthRange,[100,180]);
  p.viewer().props.onSlice(false);p.render();assert.equal(p.viewer().props.slice,false);
  const range=p.viewer().props.depthRange;p.viewer().props.onSlice(true);p.render();assert.equal(p.viewer().props.slice,true);assert.equal(p.viewer().props.depthRange,range,'equal fit retains geometry dependency identity');
  p.h.dispose();
});
test('empty entry is disabled and a legacy saved 3d context restores without forced clipping',async()=>{
  const p=await panelHarness();p.load([]);assert.equal(button(p.aquifer().props.sliceEntry,'Open selected log').props.disabled,true);assert.match(text(p.aquifer().props.sliceEntry),/Show an area/);p.h.dispose();
  const context={version:1,capturedAt:'2026-10-07T00:00:00Z',anchor:record.coordinates,pinned:true,transect:[],depthRange:[0,100],display:'3d',exaggeration:1,selectedSources:['kgs-wwc5'],sourceVersions:[],recordIds:[record.id],records:[record],coverage:[],cursorDepth:8,selectedRecordId:record.id};
  const restored=await panelHarness(context);assert.equal(restored.viewer().props.slice,false);assert.equal(restored.viewer().props.depth,8);assert.equal(restored.contexts.at(-1).display,'3d');assert.equal('slice' in restored.contexts.at(-1),false);restored.h.dispose();
});

async function threeHarness(initialProps={}){
  const renders=[],renderers=[],inspected=[],listeners={};let rayHits=[];
  const T={...Three,WebGLRenderer:class{
    constructor(){this.domElement={tabIndex:0,setAttribute(){},remove(){},addEventListener:(key,fn)=>listeners[key]=fn,removeEventListener:(key)=>delete listeners[key],getBoundingClientRect:()=>({left:0,top:0,width:800,height:440})};renderers.push(this);}
    setPixelRatio(){}setSize(){}dispose(){this.disposed=true;}render(scene,camera){renders.push({scene,camera});}
  },Raycaster:class{setFromCamera(){}intersectObjects(objects){return rayHits.filter(hit=>objects.includes(hit.object));}}};
  class OrbitControls{constructor(camera){this.camera=camera;this.target=new Three.Vector3();}update(){}addEventListener(){}removeEventListener(){}dispose(){}}
  const h=await componentHarness('app/subsurface-three.tsx',{'./subsurface-model':model,'./subsurface-materials':materials,'./subsurface-slice':slices,'./subsurface.module.css':{default:style},three:T,'three/addons/controls/OrbitControls.js':{OrbitControls}},
    {window:{devicePixelRatio:1},document:{hidden:false,addEventListener(){},removeEventListener(){}},ResizeObserver:class{observe(){}disconnect(){}}});
  let props={record,descriptionFilter:'',depthRange:[0,30],exaggeration:1,depth:5,slice:true,selectedIndex:null,onInspect:i=>inspected.push(i),onDepth:value=>props={...props,depth:value},onSlice:value=>props={...props,slice:value},...initialProps};
  let tree;const render=async(patch={})=>{props={...props,...patch};tree=h.render(h.exports.default,props);const host=findNode(tree,n=>n.props?.ref);host.props.ref.current={clientWidth:800,append(){}};h.commit();await settle();return tree;};await render();
  return{h,render,renders,renderers,inspected,listeners,setHits:hits=>rayHits=hits,get tree(){return tree;},get props(){return props;}};
}
test('actual slice slider, appearance and whole-column toggle retain renderer and camera',async()=>{
  const h=await threeHarness();assert.equal(h.renderers.length,1);
  const {scene,camera}=h.renders.at(-1);camera.position.set(7,-2,11);const position=camera.position.clone();
  const slider=findNode(h.tree,n=>n.props?.id==='recorded-slice-depth');slider.props.onChange({target:{value:'25'}});await h.render();
  assert.equal(h.props.depth,25);assert.equal(h.renderers.length,1);assert.equal(h.renders.at(-1).scene,scene);assert.deepEqual(camera.position,position);
  const meshes=[];scene.traverse(node=>{if(node.isMesh)meshes.push(node);});assert.equal(meshes.length,2);assert.equal(meshes[0].material.clippingPlanes[0].constant,-2.5);
  assert.match(text(h.tree),/25.00/);button(h.tree,'Show whole column').props.onClick();await h.render();assert.equal(meshes[0].material.clippingPlanes.length,0);assert.equal(h.renderers.length,1);
  const opacity=findNode(h.tree,n=>n.type==='input'&&n.props.max==='100');opacity.props.onChange({target:{value:'50'}});await h.render();assert.equal(meshes[0].material.opacity,.5);assert.deepEqual(camera.position,position);
  button(h.tree,'Separate layers').props.onClick();await h.render();button(h.tree,'Start 3D slice').props.onClick();await h.render();assert.deepEqual(camera.position,position,'slice toggle must not reset a separated camera');assert.equal(h.renderers.length,1);
  h.h.dispose();assert.equal(h.renderers[0].disposed,true);assert.equal(Object.keys(h.listeners).length,0);
});
test('clipped ray hits are skipped; original interval identity is inspected and cut guide is never pickable',async()=>{
  const h=await threeHarness();await h.render({depth:25});const {scene}=h.renders.at(-1),meshes=[],guides=[];scene.traverse(node=>{if(node.isMesh)meshes.push(node);if(node.isLineLoop)guides.push(node);});assert.equal(guides.length,1);assert.equal(guides[0].position.y,-2.5);assert.equal(guides[0].visible,true);
  h.setHits([{object:meshes[0],point:{y:-.8}},{object:guides[0],point:{y:-2.5}},{object:meshes[1],point:{y:-2.8}}]);h.listeners.pointerdown({clientX:10,clientY:10});h.listeners.pointerup({clientX:10,clientY:10});assert.equal(h.inspected.at(-1),record.intervals[1]);
  await h.render({selectedIndex:1});assert.match(text(findNode(h.tree,n=>n.props?.className==='selectedLayer')),/20.*30.*clay/);
  const original=record.intervals[1];button(h.tree,'20').props.onClick();assert.equal(h.inspected.at(-1),original);h.h.dispose();
});

const savedSliceContext=(depthRange=[22,28],descriptionFilter='clay')=>({version:1,capturedAt:'2026-10-07T00:00:00Z',anchor:record.coordinates,pinned:true,transect:[],depthRange,display:'3d',exaggeration:1,selectedSources:['kgs-wwc5'],sourceVersions:[],recordIds:[record.id],records:[record],coverage:[],cursorDepth:25,selectedRecordId:record.id,descriptionFilter});
test('actual parent partial-window toggle retains filter, range object, renderer and camera',async()=>{
  const p=await panelHarness(savedSliceContext());const initial=p.viewer().props,range=initial.depthRange;
  const scene=await threeHarness(initial);const camera=scene.renders.at(-1).camera;camera.position.set(7,-2,11);const pose=camera.position.clone();
  button(scene.tree,'Start 3D slice').props.onClick();p.render();await settle();p.render();await scene.render(p.viewer().props);
  assert.equal(p.viewer().props.slice,true);assert.equal(p.viewer().props.depthRange,range);same(range,[22,28]);assert.equal(p.viewer().props.descriptionFilter,'clay');assert.equal(p.viewer().props.depth,25);assert.equal(scene.renderers.length,1);assert.deepEqual(camera.position,pose);
  button(scene.tree,'Show whole column').props.onClick();p.render();await scene.render(p.viewer().props);button(scene.tree,'Start 3D slice').props.onClick();p.render();await scene.render(p.viewer().props);
  assert.equal(p.viewer().props.depthRange,range);assert.equal(scene.renderers.length,1);assert.deepEqual(camera.position,pose);assert.equal(p.focusCalls.length,0);
  scene.h.dispose();p.h.dispose();
});
test('empty filtered/window slice is disabled and parent callback cannot silently refit it',async()=>{
  for(const context of [savedSliceContext([11,19],''),savedSliceContext([22,28],'sand')]){
    const p=await panelHarness(context),before=p.viewer().props,scene=await threeHarness(before);
    assert.equal(button(scene.tree,'Start 3D slice').props.disabled,true);assert.match(text(scene.tree),/Use Fit recorded depths/);
    before.onSlice(true);p.render();await settle();p.render();assert.equal(p.viewer().props.slice,false);assert.equal(p.viewer().props.depthRange,before.depthRange);assert.equal(p.viewer().props.descriptionFilter,before.descriptionFilter);
    scene.h.dispose();p.h.dispose();
  }
});
test('deliberate entry focuses its new region once, while restore, tab entry and record changes do not steal focus',async()=>{
  const p=await panelHarness();assert.equal(p.focusCalls.length,0);button(p.aquifer().props.sliceEntry,'Open selected log').props.onClick();p.render();assert.equal(p.focusCalls.length,1);same(p.focusCalls[0],{preventScroll:true});assert.equal(findNode(p.tree,n=>n.props?.['aria-label']==='Slice a recorded column').props.tabIndex,-1);
  p.viewer().props.onDepth(23);p.render();findNode(p.tree,n=>n.props?.['aria-label']==='Slice source record').props.onChange({target:{value:other.id}});p.render();assert.equal(p.focusCalls.length,1);
  button(p.tree,'Back to cutaway').props.onClick();p.render();findNode(p.tree,n=>n.props?.['aria-label']==='Underground tool').props.onChange({target:{value:'3d'}});p.render();assert.equal(p.focusCalls.length,1);p.h.dispose();
  const restored=await panelHarness(savedSliceContext());restored.render();assert.equal(restored.focusCalls.length,0);restored.h.dispose();
});

test('area application sends exact bounds and rejects old or mismatched source results',async()=>{
 const p=await panelHarness(),first=p.messages.at(-1);assert.equal(first.kind,'area');same(first.bounds,[-100.7,38.3,-100.3,38.7]);same(first.route,[]);
 const bounds=[-99.8,38.2,-99.4,38.7];p.aquifer().props.onArea(bounds);p.render();p.flushTimers();const next=p.messages.at(-1);assert.equal(next.kind,'area');assert.equal(next.bounds,bounds);assert.notEqual(next.id,first.id);
 p.worker.onmessage({data:{id:first.id,bounds:first.bounds,columns:[{record}],coverage:'stale'}});p.render();assert.equal(p.aquifer().props.records.length,0);
 p.worker.onmessage({data:{id:next.id,bounds:first.bounds,columns:[{record}],coverage:'mismatch'}});p.render();assert.equal(p.aquifer().props.records.length,0);assert.match(p.aquifer().props.recordStatus,/did not match/);
 p.aquifer().props.onArea(bounds);p.render();p.flushTimers();p.load([other]);assert.equal(p.aquifer().props.records[0],other);assert.equal(p.contexts.at(-1).display,'aquifer');assert.match(p.contexts.at(-1).coverage[0],/-99.8, 38.2/);p.h.dispose();
});
test('compact record time restores undated rows at its explicit All endpoint without a new area query',async()=>{
 const p=await panelHarness();const dated={...other,sourceTime:'2000-01-01'},undated={...empty,id:'undated',intervals:record.intervals,sourceTime:'Unknown'};p.load([record,dated,undated]);const requests=p.messages.length;
 const nav=()=>p.aquifer().props.recordNavigation,slider=()=>findNode(nav(),n=>n.props?.['aria-label']==='Underground record year');
 assert.equal(slider().props.max,2);assert.equal(slider().props.value,2);assert.match(text(nav()),/All loaded records/);
 slider().props.onChange({target:{value:'1'}});p.render();assert.equal(p.aquifer().props.records.length,2);assert.equal(p.contexts.at(-1).recordCutoff,2000);
 slider().props.onChange({target:{value:'2'}});p.render();assert.equal(p.aquifer().props.records.length,3);assert.equal(p.contexts.at(-1).recordCutoff,null);assert.equal(p.messages.length,requests);
 assert.match(text(nav()),/Atlas year\s+2026\s+applies first/);assert.match(text(nav()),/Aquifer ranges stay fixed to 2022–2024/);
 p.aquifer().props.onArea([-99.8,38.2,-99.4,38.7]);p.render();assert.equal(button(p.aquifer().props.recordNavigation,'Play').props['aria-pressed'],false);p.h.dispose();
});

test('source and atlas-year transitions withhold stale rows and captures before the debounce runs',async()=>{
 for(const change of ['source','year']){
  const p=await panelHarness(),last=p.messages.at(-1);assert.equal(p.aquifer().props.records.length,3);
  if(change==='source')button(p.aquifer().props.recordNavigation,'Well logs').props.onClick();else p.props.year=1900;
  p.render();assert.equal(p.messages.at(-1),last,'the source request remains debounced');assert.equal(p.aquifer().props.records.length,0);assert.equal(p.aquifer().props.recordsLoading,true);
  assert.equal(p.contexts.at(-1).records.length,0,'the first new context cannot pair changed eligibility with old rows');assert.match(p.contexts.at(-1).coverage.join(' '),/Source loading/);
  if(change==='source')same(p.contexts.at(-1).selectedSources,['kgs-core']);
  p.worker.onmessage({data:{id:last.id,bounds:last.bounds,columns:[{record}],coverage:'stale'}});p.render();assert.equal(p.aquifer().props.records.length,0);
  p.flushTimers();assert.notEqual(p.messages.at(-1).id,last.id);p.load([]);assert.equal(p.aquifer().props.recordsLoading,false);assert.equal(p.aquifer().props.records.length,0);p.h.dispose();
 }
});

test('specialist picker pauses the mounted cutaway and omits unrelated time/depth controls for surveys and soil',async()=>{
 const p=await panelHarness(),visibleText=n=>n?.props?.hidden?'':typeof n==='string'?n:[n?.props?.children].flat(Infinity).filter(Boolean).map(visibleText).join(' '),original=p.aquifer().type;
 for(const display of ['surveys','soil']){
  findNode(p.tree,n=>n.props?.['aria-label']==='Underground tool').props.onChange({target:{value:display}});p.render();assert.equal(p.aquifer().type,original);assert.equal(p.aquifer().props.active,false);assert.doesNotMatch(visibleText(p.tree),/Depth cursor|Vertical scale|Through record year/);
  button(p.tree,'Back to cutaway').props.onClick();p.render();assert.equal(p.aquifer().props.active,true);p.flushTimers();assert.deepEqual([...p.messages.at(-1).bounds],[-100.7,38.3,-100.3,38.7]);
 }p.h.dispose();
});
test('record-worker startup or terminal failure remains recoverable after applying or changing eligibility',async()=>{
 for(const failWorker of [true,false]){
  const p=await panelHarness(null,{failWorker});await settle();if(!failWorker)p.worker.onerror();p.render();
  const before=p.messages.length;p.aquifer().props.onArea([-100.7,38.3,-100.3,38.7]);p.render();p.flushTimers();p.render();assert.equal(p.aquifer().props.recordsLoading,false);assert.match(p.aquifer().props.recordStatus,/Close and reopen Underground/);assert.equal(p.aquifer().props.records.length,0);
  p.props.year=1900;p.render();p.flushTimers();p.render();assert.equal(p.aquifer().props.recordsLoading,false);assert.equal(p.messages.length,before);p.h.dispose();
 }
});
