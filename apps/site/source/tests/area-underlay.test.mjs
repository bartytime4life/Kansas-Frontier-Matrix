import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';
import * as Three from 'three';
import clipping from 'polygon-clipping';
import {componentHarness,findNode,settle} from './component-harness.mjs';
const compile=source=>ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022,esModuleInterop:true}}).outputText;
async function module(name,imports={}){const exports={};vm.runInNewContext(compile(await readFile(`app/${name}.ts`,'utf8')),{exports,require:name=>{assert.ok(name in imports,name);return imports[name];}});return exports;}
const materials=await module('subsurface-materials'),model=await module('subsurface-model',{'./subsurface-materials':materials});
const cutaway=await module('cutaway-model',{'./subsurface-model':model}),camera=await module('cutaway-camera');
const studio=await module('scene-studio');
const volumeModel=await module('aquifer-volume',{'polygon-clipping':clipping});
const viewSession=await module('aquifer-view-session',{'./aquifer-volume':volumeModel});
const surfaceDetail=await module('cutaway-surface-detail',{'./basemap-cache':{basemapCacheRequest:url=>({url})},'./maplibre-seam':{},'./selected-surface':{}});
const style=new Proxy({},{get:(_,key)=>String(key)});
const text=node=>typeof node==='string'||typeof node==='number'?String(node):[node?.props?.children].flat(Infinity).filter(Boolean).map(text).join(' ');
const button=(tree,name)=>findNode(tree,n=>n.type==='button'&&text(n).replace(/\s+/g,' ').trim()===name);
const record={id:'a',sourceId:'kgs-wwc5',kind:'well',name:'A',coordinates:[-100.5,38.5],sourceTime:'1990-01-01',depthUnit:'m',depthReference:'land-surface',intervals:[{top:0,bottom:30,description:'sand'}]};
const later={...record,id:'b',name:'B',coordinates:[-100.45,38.55],sourceTime:'2000-01-01',intervals:[{top:0,bottom:100,description:'clay'}]};
const volume={bounds:[-100.7,38.3,-100.3,38.7],envelopes:[],heldClasses:0,truncated:false,period:'2022–2024'};
function locator({pitch=0,extent=volume.bounds,reduced=false}={}){
 const listeners=new Map();const map={extent:[...extent],pitch,bearing:0,zoom:9,moving:false,projection:'mercator',easeCalls:[],getPitch(){return this.pitch},getBearing(){return this.bearing},getProjection(){return{type:this.projection}},getBounds(){return{getWest:()=>this.extent[0],getSouth:()=>this.extent[1],getEast:()=>this.extent[2],getNorth:()=>this.extent[3]}},getCenter(){return{lng:(this.extent[0]+this.extent[2])/2,lat:(this.extent[1]+this.extent[3])/2}},getZoom(){return this.zoom},getCanvas(){return{width:700,height:430}},isMoving(){return this.moving},areTilesLoaded(){return true},isStyleLoaded(){return false},stop(){this.moving=false},on(name,fn){if(!listeners.has(name))listeners.set(name,new Set());listeners.get(name).add(fn)},off(name,fn){listeners.get(name)?.delete(fn)},emit(name){for(const fn of [...(listeners.get(name)??[])])fn()},triggerRepaint(){this.emit('render')},easeTo(value){this.easeCalls.push(value);this.moving=true;this.emit('movestart');this.finish=()=>{this.pitch=value.pitch??this.pitch;this.bearing=value.bearing??this.bearing;this.moving=false;this.emit('moveend')};if(reduced||value.duration===0)this.finish()},jumpTo(value){const c=value.center??[this.getCenter().lng,this.getCenter().lat],ratio=2**(this.zoom-(value.zoom??this.zoom)),w=(this.extent[2]-this.extent[0])*ratio,h=(this.extent[3]-this.extent[1])*ratio;this.extent=[c[0]-w/2,c[1]-h/2,c[0]+w/2,c[1]+h/2];this.zoom=value.zoom??this.zoom;this.pitch=value.pitch??this.pitch;this.bearing=value.bearing??this.bearing;this.emit('movestart');this.emit('resize');this.emit('moveend')}};return map;
}
// Execute the production page callback, including its unconditional 420 ms ease.
async function productionFlatMap(map,reduced=false){
 const page=await readFile('app/page.tsx','utf8'),start=page.indexOf('  const activateMapRepresentation ='),end=page.indexOf('\n  const startTerrainInvestigation',start),exports={};
 assert.ok(start>0&&end>start);
 const noop=()=>{},context={exports,compositionDefaults:studio.compositionDefaults,mapRef:{current:map},view:{pitch:map.pitch,bearing:0},projectionRef:{current:'mercator'},scenePresetRef:{current:'overview-2d'},verticalExaggerationRef:{current:1},atmospherePresetRef:{current:'night'},lightAzimuthRef:{current:210},fieldOfViewRef:{current:36},basemapRef:{current:'standard'},regionalViewRef:{current:{}},pendingViewRef:{current:null},motionDuration:n=>reduced?0:n};
 for(const name of ['stopSceneOrbit','stopFlyover','applyProjectionNavigationLimits','setProjection','setScenePreset','setVerticalExaggeration','setAtmospherePreset','setLightAzimuth','setFieldOfView','announce'])context[name]=noop;
 vm.runInNewContext(compile(page.slice(start,end)+'\nexports.activate=activateMapRepresentation;'),context);return()=>exports.activate('2d');
}
async function harness({reduced=true,map=locator(),actualSession=false,failWorker=false,fakeDetail=false,onFlatMap=()=>{},onArea=()=>{}}={}){
 const renders=[],renderers=[],controls=[],inspections=[],detailSessions=[],events=new Map(),tasks=new Map(),frames=new Map(),requests=[];let session,prepares=0,rayHits=[],timerId=0,frameId=0;const worker={terminate(){},postMessage:value=>requests.push(value)};
 const flushFrame=()=>{const pending=[...frames.values()];frames.clear();pending.forEach(callback=>callback(performance.now()));};
 const T={...Three,WebGLRenderer:class{
  constructor(){this.domElement={clientWidth:700,clientHeight:430,tabIndex:0,setAttribute(){},remove(){},addEventListener:(name,fn)=>events.set(name,fn),removeEventListener:name=>events.delete(name),getBoundingClientRect:()=>({left:0,top:0,width:700,height:430})};renderers.push(this);}
  setPixelRatio(){}setSize(w,h){this.domElement.clientWidth=w;this.domElement.clientHeight=h;}dispose(){this.disposed=true;}forceContextLoss(){this.contextReleased=true;}render(scene,camera){renders.push({scene,camera});}
 },Raycaster:class extends Three.Raycaster{intersectObjects(owners){return rayHits.filter(h=>owners.includes(h.object));}}};
 class OrbitControls{constructor(camera){this.camera=camera;this.target=new Three.Vector3();this.mouseButtons={};this.touches={};controls.push(this);}update(){this.camera.lookAt(this.target);}addEventListener(){}removeEventListener(){}listenToKeyEvents(){}dispose(){}}
 const h=await componentHarness('app/aquifer-volume-view.tsx',{
  './selected-surface-map':{default:()=>null},'./cutaway-surface-detail':fakeDetail?{...surfaceDetail,startCutawaySurfaceDetail:options=>{const session={...options,update(){},dispose(){this.disposed=true;}};detailSessions.push(session);return session;}}:surfaceDetail,'./subsurface-workers':{startAquiferVolumeWorker:()=>{if(failWorker)throw new Error('worker unavailable');return worker;}},'./aquifer-volume':volumeModel,'./subsurface-materials':materials,'./cutaway-model':cutaway,'./cutaway-camera':camera,'./aquifer-layers':{KGS_ATLAS_URL:'https://example.test/'},'./subsurface.module.css':{default:style},'./aquifer-volume-mesh':{aquiferGeometries:()=>[]},'./aquifer-view-session':{locatorBounds:viewSession.locatorBounds,startAquiferView:options=>{session=options;if(actualSession)return viewSession.startAquiferView({...options,timers:{set:(cb,delay)=>{const id=++timerId;tasks.set(id,{cb,delay});return id},clear:id=>tasks.delete(id)}});return Object.assign(()=>{},{prepare:()=>prepares++});}},three:T,'three/addons/controls/OrbitControls.js':{OrbitControls}
 },{devicePixelRatio:1,performance,queueMicrotask,matchMedia:()=>({matches:reduced,addEventListener(){},removeEventListener(){}}),document:{hidden:false,createElement:()=>({getContext:()=>({fillRect(){},fillText(){}})}),addEventListener(){},removeEventListener(){}},ResizeObserver:class{observe(){}disconnect(){}},requestAnimationFrame:callback=>{const id=++frameId;frames.set(id,callback);return id},cancelAnimationFrame:id=>frames.delete(id)});
 let props={map,records:[record,later],onFlatMap,onLocate(){},onInspect:(...args)=>inspections.push(args),locator:{anchor:record.coordinates,pinned:false},onLocatorSlot(){},sliceEntry:{type:'details',props:{children:'Inspect an individual log'}},onArea,recordsAvailable:2,onResetRecords(){},recordsLoading:false,recordStatus:'2 loaded records in selected area',partial:false,recordNavigation:{type:'nav',props:{'aria-label':'Record time navigation',children:'Record time'}}},tree;
 const host={clientWidth:700,clientHeight:430,append(){}};
 const render=async(patch={})=>{props={...props,...patch};tree=h.render(h.exports.default,props);const canvas=findNode(tree,n=>n.props?.className==='cutawayCanvas');if(canvas)canvas.props.ref.current=host;h.commit();await settle();flushFrame();return tree;};await render();await render();
 return{h,render,renders,renderers,controls,inspections,detailSessions,events,map,worker,requests,flushFrame,flush(delay){for(const [id,task] of [...tasks])if(task.delay===delay){tasks.delete(id);task.cb()}},get tree(){return tree;},get session(){return session;},get prepares(){return prepares;},setHits:h=>rayHits=h};
}
test('area selection starts without an empty canvas or disabled timeline, then reveals the model and disclosed tools',async()=>{
 const h=await harness();assert.equal(h.session.manual,true);assert.equal(h.prepares,0);assert.equal(h.renderers.length,0);
 button(h.tree,'Show this area ↗').props.onClick();assert.equal(h.prepares,1);
 assert.equal(findNode(h.tree,n=>n.props?.className==='cutawayCanvas'),undefined);assert.equal(findNode(h.tree,n=>n.props?.['aria-label']==='Record time navigation'),undefined);
 h.session.onSnapshot({volume,image:null});await h.render();assert.equal(h.renderers.length,1);assert.match(text(h.tree),/2 plotted columns/);assert.match(text(h.tree),/MAP IMAGE UNAVAILABLE/);
 assert.ok(findNode(h.tree,n=>n.props?.['aria-label']==='Record time navigation'));
 const tools=findNode(h.tree,n=>n.props?.className==='areaTools');for(const disclosure of tools.props.children){assert.equal(disclosure.type,'details');assert.ok(!disclosure.props.open);}
 h.session.onPreview(true);await h.render();assert.match(text(h.tree),/Map preview changed.*selected area/);assert.equal(h.renderers.length,1);h.h.dispose();
});
test('actual area controls retain renderer and camera, while record-time membership changes preserve pose and valid inspection',async()=>{
 const h=await harness();h.session.onSnapshot({volume,image:null});await h.render();const camera=h.renders.at(-1).camera;camera.position.set(7,3,12);h.controls.at(-1).target.set(.2,-.3,.4);const pose=camera.position.clone(),target=h.controls.at(-1).target.clone();
 button(h.tree,'Move').props.onClick();await h.render();assert.equal(h.controls[0].mouseButtons.LEFT,Three.MOUSE.PAN);assert.equal(h.controls[0].touches.ONE,Three.TOUCH.PAN);assert.equal(h.renderers.length,1);assert.deepEqual(camera.position,pose);
 findNode(h.tree,n=>n.props?.['aria-label']==='Basemap opacity').props.onChange({target:{value:'50'}});await h.render();assert.equal(h.renderers.length,1);assert.deepEqual(camera.position,pose);
 let column;h.renders.at(-1).scene.traverse(n=>{if(n.userData?.interval===record.intervals[0])column=n;});assert.ok(column);h.setHits([{object:column}]);h.events.get('pointerdown')({clientX:10,clientY:10,pointerId:1,isPrimary:true,button:0});h.events.get('pointerup')({clientX:10,clientY:10,pointerId:1,isPrimary:true,button:0});await h.render();assert.equal(h.inspections.at(-1)[0],record);assert.match(text(findNode(h.tree,n=>n.props?.className==='cutawayReadout')),/sand/);
 await h.render({records:[record]});assert.equal(h.renderers.length,2);assert.equal(h.renderers[0].disposed,true);assert.deepEqual(h.renders.at(-1).camera.position,pose);assert.deepEqual(h.controls.at(-1).target,target);assert.match(text(findNode(h.tree,n=>n.props?.className==='cutawayReadout')),/sand/);
 await h.render({records:[]});await h.render();assert.deepEqual(h.renders.at(-1).camera.position,pose);assert.deepEqual(h.controls.at(-1).target,target);assert.doesNotMatch(text(findNode(h.tree,n=>n.props?.className==='cutawayReadout')),/sand/);assert.match(text(h.tree),/No recorded intervals at this time/);
 h.h.dispose();assert.ok(h.renderers.every(r=>r.disposed&&r.contextReleased));assert.equal(h.events.size,0);
});

test('first settled records fit a geometry-first empty frame, unless the user has already moved its camera',async()=>{
 for(const manipulated of [false,true]){
  const h=await harness();await h.render({records:[],recordsLoading:true});
  const small={...volume,bounds:[-100.505,38.495,-100.495,38.505]};h.session.onSnapshot({volume:small,image:null});await h.render();
  if(manipulated)findNode(h.tree,n=>n.props?.['aria-label']==='Zoom in').props.onClick();
  const before=h.renders.at(-1).camera.position.clone(),deep={...record,intervals:[{top:0,bottom:500,description:'sand'}]};
  await h.render({records:[deep],recordsLoading:false});const {scene,camera}=h.renders.at(-1);
  if(manipulated)assert.deepEqual(camera.position,before,'first settlement must not override deliberate navigation');
  else{
   assert.notDeepEqual(camera.position,before,'the empty one-metre fit is replaced once records settle');let column;scene.traverse(n=>{if(n.userData?.interval===deep.intervals[0])column=n;});assert.ok(column);scene.updateMatrixWorld(true);camera.updateMatrixWorld(true);
   const box=new Three.Box3().setFromObject(column),center=box.getCenter(new Three.Vector3());for(const y of [box.min.y,box.max.y])assert.ok(Math.abs(new Three.Vector3(center.x,y,center.z).project(camera).y)<1,'deep recorded column fits the viewport');
   const fitted=camera.position.clone();await h.render({records:[]});await h.render({records:[deep]});assert.deepEqual(h.renders.at(-1).camera.position,fitted,'subsequent record-time scrubbing does not refit');
   await h.render({records:[],recordsLoading:true});await h.render({records:[deep],recordsLoading:false});assert.deepEqual(h.renders.at(-1).camera.position,fitted,'a later source/year query loading transition preserves pose');
  }h.h.dispose();
 }
});

test('Show uses the production 2D callback once through normal and reduced-motion transitions, without a second click',async()=>{
 for(const [pitch,reduced] of [[0,false],[45,false],[45,true]]){
  const map=locator({pitch,reduced}),areas=[],onFlatMap=await productionFlatMap(map,reduced),h=await harness({map,actualSession:true,onFlatMap,onArea:b=>areas.push(b)});
  button(h.tree,'Show this area ↗').props.onClick();
  if(pitch&&!reduced){assert.equal(h.requests.length,0);assert.equal(map.easeCalls[0].duration,420);map.emit('resize');map.finish();h.flush(80);}
  assert.equal(h.requests.length,1);assert.equal(areas.length,1);assert.equal(map.easeCalls.length,pitch?1:0);assert.deepEqual([...areas[0]],map.extent);
  await h.render();assert.equal(h.renderers.length,1,'independent log frame appears before aquifer result');
  map.emit('movestart');map.extent=[-99.8,38.2,-99.4,38.7];map.emit('resize');map.emit('moveend');
  h.worker.onmessage({data:{id:h.requests[0].id,volume:{...volume,bounds:h.requests[0].bounds}}});await h.render();
  assert.equal(h.requests.length,1);assert.match(text(h.tree),/Map preview changed/);assert.match(text(h.tree),/2 plotted columns/);h.h.dispose();
 }
});
test('worker construction and aquifer/capture failures retain independent source columns with visible recovery',async()=>{
 for(const failWorker of [true,false]){
  const areas=[],h=await harness({actualSession:true,failWorker,onArea:b=>areas.push(b)});button(h.tree,'Show this area ↗').props.onClick();
  if(!failWorker)h.worker.onerror();await h.render();
  assert.equal(areas.length,1);assert.equal(h.renderers.length,1);assert.match(text(h.tree),/2 plotted columns/);assert.match(text(h.tree),/Aquifer preparation.*(unavailable|failed)/);assert.match(text(h.tree),/Map image unavailable/);
  let logs=0;h.renders.at(-1).scene.traverse(n=>{if(n.userData?.interval)logs++});assert.equal(logs,2);h.h.dispose();
 }
});
test('wide initial selection offers a bounded reframe at the same center and applies once',async()=>{
 const map=locator({extent:[-102,37.1,-98,39.9]}),center=map.getCenter(),areas=[],h=await harness({map,actualSession:true,onArea:b=>areas.push(b)});
 assert.equal(h.renderers.length,0);assert.match(text(h.tree),/too broad/);button(h.tree,'Zoom in & explore ↗').props.onClick();await h.render();
 assert.equal(areas.length,1);assert.ok(volumeModel.validVolumeBounds(areas[0]));assert.deepEqual(map.getCenter(),center);assert.equal(h.requests.length,1);h.h.dispose();
});

test('independent deep logs fit before optional aquifer settles, then preserve a deliberate camera',async()=>{
 const h=await harness();await h.render({records:[],recordsLoading:true});
 const small={...volume,bounds:[-100.505,38.495,-100.495,38.505]};h.session.onSnapshot({volume:small,image:null,aquiferState:'loading'});await h.render();
 const deep={...record,intervals:[{top:0,bottom:500,description:'sand'}]};await h.render({records:[deep],recordsLoading:false});
 const {scene,camera}=h.renders.at(-1);scene.updateMatrixWorld(true);camera.updateMatrixWorld(true);let log;scene.traverse(n=>{if(n.userData?.interval===deep.intervals[0])log=n});const box=new Three.Box3().setFromObject(log),center=box.getCenter(new Three.Vector3());assert.ok(Math.abs(new Three.Vector3(center.x,box.min.y,center.z).project(camera).y)<1);
 findNode(h.tree,n=>n.props?.['aria-label']==='Zoom in').props.onClick();const pose=camera.position.clone();h.session.onSnapshot({volume:small,image:null,aquiferState:'ready'});await h.render();assert.deepEqual(h.renders.at(-1).camera.position,pose);h.h.dispose();
});
test('specialist navigation pauses resources and returns to the applied cutaway without another apply',async()=>{
 const h=await harness({actualSession:true});button(h.tree,'Show this area ↗').props.onClick();h.worker.onmessage({data:{id:h.requests[0].id,volume}});await h.render();const old=h.renders.at(-1).camera;old.position.set(7,3,12);const pose=old.position.clone();
 await h.render({active:false});assert.equal(h.renderers[0].disposed,true);assert.equal(h.worker.onmessage,null);
 h.map.extent=[-99.8,38.2,-99.4,38.7];await h.render({active:true});await h.render();assert.equal(h.requests.length,1,'returning does not apply the preview frame');assert.deepEqual(h.renders.at(-1).camera.position,pose);assert.match(text(h.tree),/Selected area retained/);assert.match(text(h.tree),/Map preview changed/);assert.match(text(h.tree),/2 plotted columns/);h.h.dispose();
});
test('a style-read exception preserves the apply intent and continues on map load without another click',async()=>{
 const map=locator(),h=await harness({map,actualSession:true});map.getPitch=()=>{throw new Error('style changing')};assert.doesNotThrow(()=>button(h.tree,'Show this area ↗').props.onClick());assert.equal(h.requests.length,0);await h.render();assert.match(text(h.tree),/Waiting for the map style/);
 map.getPitch=()=>0;map.emit('load');h.flush(80);await h.render();assert.equal(h.requests.length,1);assert.equal(h.renderers.length,1);h.h.dispose();
});
test('settled absence of both logs and aquifer uses compact recovery without empty camera or time chrome',async()=>{
 const h=await harness({actualSession:true});await h.render({records:[],recordsAvailable:0});button(h.tree,'Show this area ↗').props.onClick();h.worker.onerror();await h.render();
 assert.equal(findNode(h.tree,n=>n.props?.className==='cutawayCanvas'),undefined);assert.equal(findNode(h.tree,n=>n.props?.['aria-label']==='Area 3D navigation'),undefined);assert.equal(findNode(h.tree,n=>n.props?.['aria-label']==='Record time navigation'),undefined);assert.ok(button(h.tree,'Reset record filters'));assert.match(text(h.tree),/No recorded intervals at this time/);h.h.dispose();
});


test('surface inspection pauses the 3D renderer and returns to the same cutaway pose and bounds',async()=>{
 const h=await harness();h.session.onSnapshot({volume,image:null});await h.render();
 const camera=h.renders.at(-1).camera;camera.position.set(7,3,12);const pose=camera.position.clone();
 button(h.tree,'Surface map').props.onClick();await h.render();assert.equal(h.renderers[0].disposed,true);
 const surface=findNode(h.tree,n=>n.props?.source===h.map&&n.props?.bounds===volume.bounds);assert.ok(surface);assert.equal(surface.props.active,true);
 h.session.onPreview(true);await h.render();assert.equal(h.prepares,0);
 button(h.tree,'3D cutaway').props.onClick();await h.render();assert.deepEqual(h.renders.at(-1).camera.position,pose);assert.equal(h.prepares,0);h.h.dispose();
});

test('zoom reverses immediately at both limits without changing the slice or drifting the target',async()=>{
 const h=await harness({reduced:false});h.session.onSnapshot({volume,image:null});await h.render();
 const c=h.renders.at(-1).camera,controls=h.controls.at(-1),target=controls.target.clone();
 const zoom=direction=>findNode(h.tree,n=>n.props?.['aria-label']===`Zoom ${direction}`).props.onClick();
 for(let i=0;i<100;i++)zoom('out');
 assert.ok(Math.abs(c.position.distanceTo(target)-controls.maxDistance)<1e-8);
 const wide=c.position.distanceTo(target);zoom('in');assert.ok(c.position.distanceTo(target)<wide*.81);
 for(let i=0;i<100;i++)zoom('in');
 assert.ok(Math.abs(c.position.distanceTo(target)-controls.minDistance)<1e-8);
 zoom('out');assert.ok(c.position.distanceTo(target)>controls.minDistance*1.2);
 assert.deepEqual(controls.target,target);assert.equal(controls.zoomToCursor,false);assert.equal(h.prepares,0);
 // Wheel navigation can change distance without applyPose: every render refreshes clipping.
 c.position.set(400,300,200);
 button(h.tree,'Exact pixels').props.onClick();await h.render();assert.ok(c.far>c.position.length());
 h.h.dispose();assert.ok(h.renderers.every(r=>r.contextReleased));
});

test('cutaway exposes detailed basemaps and layer controls without reselecting geography or altering records',async()=>{
 const h=await harness(),changes=[];h.session.onSnapshot({volume,image:null});await h.render({basemap:'standard',onBasemap:key=>changes.push(key),onLayers:()=>changes.push('layers')});
 const select=findNode(h.tree,n=>n.props?.['aria-label']==='Cutaway basemap');assert.ok(select);
 select.props.onChange({target:{value:'kansas-aerial'}});button(h.tree,'Choose map layers').props.onClick();
 assert.deepEqual(changes,['kansas-aerial','layers']);assert.equal(h.prepares,0);
 const quality=findNode(h.tree,n=>n.props?.['aria-label']==='Cutaway surface resolution');assert.equal(quality.props.value,4096);
 quality.props.onChange({target:{value:'2048'}});await h.render();assert.equal(findNode(h.tree,n=>n.props?.['aria-label']==='Cutaway surface resolution').props.value,2048);
 assert.match(text(h.tree),/Display context, not KFM evidence/);assert.ok(button(h.tree,'Exact pixels'));h.h.dispose();
});

test('well and core surface anchors stay at recorded ground coordinates through exaggeration and close zoom',async()=>{
 const core={...later,kind:'core'},before=JSON.stringify([record,core]),h=await harness();
 h.session.onSnapshot({volume,image:{width:256,height:256}});await h.render({records:[record,core]});
 const {scene,camera}=h.renders.at(-1),anchors=[];scene.traverse(n=>{if(n.userData.surfaceAnchor)anchors.push(n)});assert.equal(anchors.length,2);
 const expected=volumeModel.projectVolumePosition(...core.coordinates,volume.bounds),input=label=>findNode(h.tree,n=>n.props?.['aria-label']===label);
 const checkAnchors=()=>{scene.updateMatrixWorld(true);for(const anchor of anchors){const p=volumeModel.projectVolumePosition(...anchor.userData.record.coordinates,volume.bounds),actual=anchor.getWorldPosition(new Three.Vector3());assert.ok(actual.distanceTo(new Three.Vector3(p.x,0,p.z))<1e-10,'marker center coincides with mapped coordinate and zero surface elevation');assert.equal(anchor.material.opacity,1)}};
 for(const exaggeration of [1,25,500]){input('Cutaway vertical scale').props.onChange({target:{value:String(exaggeration)}});await h.render();checkAnchors()}
 input('Sample location').props.onChange({target:{value:core.id}});await h.render();button(h.tree,'Zoom to sample').props.onClick();h.flushFrame();
 const target=h.controls.at(-1).target;assert.deepEqual(target.toArray(),[expected.x,0,expected.z]);
 const centered=new Three.Vector3(expected.x,0,expected.z).project(camera);assert.ok(Math.hypot(centered.x,centered.y)<1e-8,'selected recorded coordinate is centered');
 const anchor=anchors.find(n=>n.userData.record.id===core.id),pixelWidth=()=>{scene.updateMatrixWorld(true);const a=anchor.localToWorld(new Three.Vector3(-.5,0,0)).project(camera),b=anchor.localToWorld(new Three.Vector3(.5,0,0)).project(camera);return Math.abs(a.x-b.x)*350};
 assert.ok(Math.abs(pixelWidth()-18)<.01,'selection ring has a small screen footprint');
 for(let i=0;i<30;i++)input('Zoom in').props.onClick();h.flushFrame();assert.ok(Math.abs(pixelWidth()-18)<.01,'marker cannot grow into an oversized circle');
 assert.ok(camera.position.distanceTo(target)/volumeModel.volumeDepthScale(volume.bounds)<2.01,'close inspection is independent of slice width');checkAnchors();
 input('Basemap opacity').props.onChange({target:{value:'0'}});await h.render();checkAnchors();let mappedPlane;scene.traverse(n=>{if(n.material?.map&&n.geometry?.type==='PlaneGeometry')mappedPlane=n});assert.ok(mappedPlane);assert.equal(mappedPlane.material.opacity,0);
 input('Cutaway vertical scale').props.onChange({target:{value:'10'}});await h.render();assert.deepEqual(target.toArray(),[expected.x,0,expected.z]);checkAnchors();
 const child=findNode(h.tree,n=>n.props?.source===h.map&&n.props?.bounds===volume.bounds);assert.equal(child.props.opacity,0);
 assert.equal(h.prepares,0);assert.equal(JSON.stringify([record,core]),before);assert.match(text(h.tree),/Location accuracy is not supplied/);
 button(h.tree,'Show recorded columns').props.onClick();await h.render();assert.equal(anchor.parent.visible,false);
 h.h.dispose();
});


test('Top view targets the surface so close zoom never dives under a deep exaggerated log',async()=>{
 const h=await harness(),deep={...record,intervals:[{top:0,bottom:500,description:'sand'}]};h.session.onSnapshot({volume,image:null});await h.render({records:[deep]});
 button(h.tree,'Top view').props.onClick();const c=h.renders.at(-1).camera,target=h.controls.at(-1).target;assert.equal(target.y,0);
 for(let i=0;i<100;i++)findNode(h.tree,n=>n.props?.['aria-label']==='Zoom in').props.onClick();
 assert.ok(c.position.y>0,'camera stays above the geographic surface');assert.equal(target.y,0);assert.equal(h.prepares,0);h.h.dispose();
});


const mappedPlanes=h=>{
 const result=[];h.renders.at(-1).scene.traverse(node=>{if(node.geometry?.type==='PlaneGeometry'&&node.material?.map)result.push(node)});return result;
};
test('appearance controls reuse the captured surface without marking its unchanged pixels for upload',async()=>{
 const h=await harness(),image={width:4096,height:3437};h.session.onSnapshot({volume,image});await h.render();
 const [plane]=mappedPlanes(h),texture=plane.material.map,version=texture.version,camera=h.renders.at(-1).camera;
 const input=label=>findNode(h.tree,n=>n.props?.['aria-label']===label);
 for(let i=1;i<=20;i++){input('Basemap opacity').props.onChange({target:{value:String(i*5)}});await h.render();assert.equal(plane.material.opacity,i/20);}
 input('Aquifer opacity').props.onChange({target:{value:'40'}});await h.render();
 input('Cutaway vertical scale').props.onChange({target:{value:'50'}});await h.render();
 button(h.tree,'Move').props.onClick();await h.render();button(h.tree,'Show recorded columns').props.onClick();await h.render();
 assert.equal(texture.version,version,'24 appearance changes cause zero additional texture upload requests');
 assert.equal(texture.image,image);assert.equal(plane.material.map,texture);assert.equal(h.renders.at(-1).camera,camera);
 button(h.tree,'Exact pixels').props.onClick();await h.render();assert.equal(texture.version,version+1);assert.equal(texture.magFilter,Three.LinearFilter);assert.equal(texture.minFilter,Three.LinearFilter);
 button(h.tree,'Smooth image').props.onClick();await h.render();assert.equal(texture.version,version+2);assert.equal(texture.magFilter,Three.NearestFilter);
 let disposed=0;texture.addEventListener('dispose',()=>disposed++);h.h.dispose();assert.equal(disposed,1);
});
test('new and refreshed detail frames retain the chosen sampling and geography without opacity uploads',async()=>{
 const h=await harness({fakeDetail:true});h.session.onSnapshot({volume,image:null});await h.render();
 button(h.tree,'Exact pixels').props.onClick();await h.render();
 const surface=findNode(h.tree,n=>typeof n.props?.onCapture==='function');surface.props.onCapture({bounds:volume.bounds,style:{version:8,sources:{},layers:[]},images:[]});await h.render();
 assert.equal(h.detailSessions.length,1);const detail=h.detailSessions[0],image={width:4096,height:3437};
 detail.onFrame({image,bounds:volume.bounds,zoom:12});h.flushFrame();await h.render();
 assert.match(text(h.tree),/HIGH-DETAIL MAP/);
 assert.doesNotMatch(text(h.tree),/MAP IMAGE UNAVAILABLE/,'a real detail plane overrides the missing fallback image');
 let [plane]=mappedPlanes(h),texture=plane.material.map;
 assert.equal(texture.magFilter,Three.LinearFilter,'late frame honors Smooth image');assert.equal(texture.minFilter,Three.LinearFilter);assert.equal(texture.image,image);
 const before=texture.version,geometry=Array.from(plane.geometry.attributes.position.array),uv=Array.from(plane.geometry.attributes.uv.array),offset=texture.offset.toArray(),repeat=texture.repeat.toArray();
 for(let i=1;i<=20;i++){findNode(h.tree,n=>n.props?.['aria-label']==='Basemap opacity').props.onChange({target:{value:String(i*5)}});await h.render();assert.equal(plane.material.opacity,i/20);}
 assert.equal(texture.version,before);assert.deepEqual(Array.from(plane.geometry.attributes.position.array),geometry);assert.deepEqual(Array.from(plane.geometry.attributes.uv.array),uv);assert.deepEqual(texture.offset.toArray(),offset);assert.deepEqual(texture.repeat.toArray(),repeat);
 let disposed=0;texture.addEventListener('dispose',()=>disposed++);
 const refreshed={width:2048,height:1719};detail.onFrame({image:refreshed,bounds:volume.bounds,zoom:13});h.flushFrame();assert.equal(disposed,1);
 [plane]=mappedPlanes(h);texture=plane.material.map;assert.equal(texture.magFilter,Three.LinearFilter);assert.equal(texture.image,refreshed);assert.deepEqual(Array.from(plane.geometry.attributes.position.array),geometry);
 button(h.tree,'Smooth image').props.onClick();await h.render();assert.equal(texture.magFilter,Three.NearestFilter);assert.equal(texture.minFilter,Three.NearestFilter);
 detail.onFrame({image,bounds:volume.bounds,zoom:12});h.flushFrame();[plane]=mappedPlanes(h);assert.equal(plane.material.map.magFilter,Three.NearestFilter,'later frames also retain Exact pixels');
 const finalTexture=plane.material.map;let finalDisposed=0;finalTexture.addEventListener('dispose',()=>finalDisposed++);
 surface.props.onCapture(null);await h.render();await h.render();assert.equal(finalDisposed,1);assert.equal(mappedPlanes(h).length,0);
 assert.match(text(h.tree),/MAP IMAGE UNAVAILABLE/,'clearing the detail restores the truthful fallback caption');
 h.h.dispose();assert.equal(detail.disposed,true);assert.equal(h.prepares,0);
});
