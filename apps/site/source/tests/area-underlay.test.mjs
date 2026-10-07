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
const volumeModel=await module('aquifer-volume',{'polygon-clipping':clipping});
const style=new Proxy({},{get:(_,key)=>String(key)});
const text=node=>typeof node==='string'||typeof node==='number'?String(node):[node?.props?.children].flat(Infinity).filter(Boolean).map(text).join(' ');
const button=(tree,name)=>findNode(tree,n=>n.type==='button'&&text(n).replace(/\s+/g,' ').trim()===name);
const record={id:'a',sourceId:'kgs-wwc5',kind:'well',name:'A',coordinates:[-100.5,38.5],sourceTime:'1990-01-01',depthUnit:'m',depthReference:'land-surface',intervals:[{top:0,bottom:30,description:'sand'}]};
const later={...record,id:'b',name:'B',coordinates:[-100.45,38.55],sourceTime:'2000-01-01',intervals:[{top:0,bottom:100,description:'clay'}]};
const volume={bounds:[-100.7,38.3,-100.3,38.7],envelopes:[],heldClasses:0,truncated:false,period:'2022–2024'};
async function harness(){
 const renders=[],renderers=[],controls=[],inspections=[],events=new Map();let session,prepares=0,rayHits=[];
 const T={...Three,WebGLRenderer:class{
  constructor(){this.domElement={clientWidth:700,clientHeight:430,tabIndex:0,setAttribute(){},remove(){},addEventListener:(name,fn)=>events.set(name,fn),removeEventListener:name=>events.delete(name),getBoundingClientRect:()=>({left:0,top:0,width:700,height:430})};renderers.push(this);}
  setPixelRatio(){}setSize(w,h){this.domElement.clientWidth=w;this.domElement.clientHeight=h;}dispose(){this.disposed=true;}render(scene,camera){renders.push({scene,camera});}
 },Raycaster:class{setFromCamera(){}intersectObjects(owners){return rayHits.filter(h=>owners.includes(h.object));}}};
 class OrbitControls{constructor(camera){this.camera=camera;this.target=new Three.Vector3();this.mouseButtons={};this.touches={};controls.push(this);}update(){this.camera.lookAt(this.target);}addEventListener(){}removeEventListener(){}listenToKeyEvents(){}dispose(){}}
 const h=await componentHarness('app/aquifer-volume-view.tsx',{
  './subsurface-workers':{startAquiferVolumeWorker:()=>({terminate(){}})},'./aquifer-volume':volumeModel,'./subsurface-materials':materials,'./cutaway-model':cutaway,'./cutaway-camera':camera,'./aquifer-layers':{KGS_ATLAS_URL:'https://example.test/'},'./subsurface.module.css':{default:style},'./aquifer-volume-mesh':{aquiferGeometries:()=>[]},'./aquifer-view-session':{startAquiferView:options=>{session=options;return Object.assign(()=>{},{prepare:()=>prepares++});}},three:T,'three/addons/controls/OrbitControls.js':{OrbitControls}
 },{devicePixelRatio:1,performance,queueMicrotask,matchMedia:()=>({matches:true,addEventListener(){},removeEventListener(){}}),document:{hidden:false,createElement:()=>({getContext:()=>({fillRect(){},fillText(){}})}),addEventListener(){},removeEventListener(){}},ResizeObserver:class{observe(){}disconnect(){}},requestAnimationFrame:()=>1,cancelAnimationFrame(){}});
 let props={map:{},records:[record,later],onFlatMap(){},onLocate(){},onInspect:(...args)=>inspections.push(args),locator:{anchor:record.coordinates,pinned:false},onLocatorSlot(){},sliceEntry:{type:'details',props:{children:'Inspect an individual log'}},onArea(){},recordsLoading:false,recordStatus:'2 loaded records in selected area',partial:false,recordNavigation:{type:'nav',props:{'aria-label':'Record time navigation',children:'Record time'}}},tree;
 const host={clientWidth:700,clientHeight:430,append(){}};
 const render=async(patch={})=>{props={...props,...patch};tree=h.render(h.exports.default,props);findNode(tree,n=>n.props?.className==='cutawayCanvas').props.ref.current=host;h.commit();await settle();return tree;};await render();
 return{h,render,renders,renderers,controls,inspections,events,get tree(){return tree;},get session(){return session;},get prepares(){return prepares;},setHits:h=>rayHits=h};
}
test('area underlay keeps the selector and explicit apply primary, with record time adjacent and tools disclosed',async()=>{
 const h=await harness();assert.equal(h.session.manual,true);assert.equal(h.prepares,0);assert.equal(h.renderers.length,0);
 button(h.tree,'Show this area ↗').props.onClick();assert.equal(h.prepares,1);
 const workspace=findNode(h.tree,n=>n.props?.className==='cutawayWorkspace'),children=workspace.props.children;
 assert.equal(children.length,2);assert.equal(children[0].type,'aside');assert.equal(children[1].props.className,'areaModel');
 assert.equal(children[1].props.children[1].props['aria-label'],'Record time navigation');
 const tools=findNode(h.tree,n=>n.props?.className==='areaTools');for(const disclosure of tools.props.children){assert.equal(disclosure.type,'details');assert.ok(!disclosure.props.open);}
 assert.equal(findNode(workspace,n=>n.type==='button'&&/Open.*log/.test(text(n))),undefined);
 h.session.onSnapshot({volume,image:null});await h.render();assert.equal(h.renderers.length,1);assert.match(text(h.tree),/2 plotted columns/);assert.match(text(h.tree),/SURFACE IMAGE UNAVAILABLE/);
 h.session.onPreview(true);await h.render();assert.match(text(h.tree),/Preview changed.*selected area/);assert.equal(h.renderers.length,1,'selector preview does not replace the selected geometry');h.h.dispose();
});
test('actual area controls retain renderer and camera, while record-time membership changes preserve pose and valid inspection',async()=>{
 const h=await harness();h.session.onSnapshot({volume,image:null});await h.render();const camera=h.renders.at(-1).camera;camera.position.set(7,3,12);h.controls.at(-1).target.set(.2,-.3,.4);const pose=camera.position.clone(),target=h.controls.at(-1).target.clone();
 button(h.tree,'Move').props.onClick();await h.render();assert.equal(h.controls[0].mouseButtons.LEFT,Three.MOUSE.PAN);assert.equal(h.controls[0].touches.ONE,Three.TOUCH.PAN);assert.equal(h.renderers.length,1);assert.deepEqual(camera.position,pose);
 findNode(h.tree,n=>n.props?.['aria-label']==='Surface map opacity').props.onChange({target:{value:'50'}});await h.render();assert.equal(h.renderers.length,1);assert.deepEqual(camera.position,pose);
 let column;h.renders.at(-1).scene.traverse(n=>{if(n.userData?.interval===record.intervals[0])column=n;});assert.ok(column);h.setHits([{object:column}]);h.events.get('pointerdown')({clientX:10,clientY:10});h.events.get('pointerup')({clientX:10,clientY:10});await h.render();assert.equal(h.inspections.at(-1)[0],record);assert.match(text(findNode(h.tree,n=>n.props?.className==='cutawayReadout')),/sand/);
 await h.render({records:[record]});assert.equal(h.renderers.length,2);assert.equal(h.renderers[0].disposed,true);assert.deepEqual(h.renders.at(-1).camera.position,pose);assert.deepEqual(h.controls.at(-1).target,target);assert.match(text(findNode(h.tree,n=>n.props?.className==='cutawayReadout')),/sand/);
 await h.render({records:[]});await h.render();assert.deepEqual(h.renders.at(-1).camera.position,pose);assert.deepEqual(h.controls.at(-1).target,target);assert.doesNotMatch(text(findNode(h.tree,n=>n.props?.className==='cutawayReadout')),/sand/);assert.match(text(h.tree),/No recorded intervals are plotted/);
 h.h.dispose();assert.ok(h.renderers.every(r=>r.disposed));assert.equal(h.events.size,0);
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
