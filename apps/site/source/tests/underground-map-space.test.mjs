import assert from 'node:assert/strict';
import test from 'node:test';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';
import clipping from 'polygon-clipping';
import * as Three from 'three';
import {componentHarness,findNode,settle} from './component-harness.mjs';

async function module(name,imports={}){
 const exports={};
 vm.runInNewContext(ts.transpileModule(await readFile(`app/${name}.ts`,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText,{exports,require(name){assert.ok(name in imports,name);return imports[name];}});
 return exports;
}
const materials=await module('subsurface-materials');
const model=await module('subsurface-model',{'./subsurface-materials':materials});
const volumeModel=await module('aquifer-volume',{'polygon-clipping':{default:clipping}});
const cutaway=await module('cutaway-model',{'./subsurface-model':model});
const mesh=await module('aquifer-volume-mesh',{'./aquifer-volume':volumeModel});
const camera=await module('cutaway-camera');
const styles=new Proxy({},{get:(_,key)=>String(key)});
const text=node=>typeof node==='string'||typeof node==='number'?String(node):[node?.props?.children].flat(Infinity).filter(Boolean).map(text).join(' ').replace(/\s+/g,' ').trim();
const button=(tree,label)=>findNode(tree,n=>n.type==='button'&&(n.props['aria-label']===label||text(n)===label));
const byClass=(tree,name)=>findNode(tree,n=>n.props?.className===name);
const same=(actual,expected)=>assert.deepEqual(JSON.parse(JSON.stringify(actual)),expected);
const bounds=[-100.7,38.3,-100.3,38.7];
const record={id:'well-a',sourceId:'kgs-wwc5',kind:'well',name:'WWC5 A',coordinates:[-100.5,38.5],coordinateReference:'WGS84',locationMethod:'approximate',sourceUrl:'https://example.test/a',sourceTime:'1990-01-01',depthUnit:'m',depthReference:'land-surface',totalDepth:30,intervals:[{top:0,bottom:30,description:'sand'}]};

// Actual hooks, handlers, camera and geometry; only browser/WebGL transport is
// stubbed. These tests do not claim responsive browser or provider acceptance.
async function harness({narrow=false,acceptsArea=true}={}){
 const renderers=[],controls=[],observers=[],frames=new Map(),focusCalls=[],areas=[],inspections=[];
 let frameId=0,prepares=0,options,sessionStarts=0,tree,awaitingArea=false;
 const doc={hidden:false,activeElement:null,createElement:()=>({getContext:()=>null}),addEventListener(){},removeEventListener(){}};
 class Renderer{
  constructor(){this.domElement=Object.assign(new EventTarget(),{clientWidth:800,clientHeight:600,setAttribute(){},remove(){}});renderers.push(this);}
  setPixelRatio(){}setSize(w,h){this.domElement.clientWidth=w;this.domElement.clientHeight=h;}dispose(){this.disposed=true;}forceContextLoss(){}
  render(scene,camera){this.scene=scene;this.camera=camera;}
 }
 class Controls extends Three.EventDispatcher{
  constructor(camera){super();this.camera=camera;this.target=new Three.Vector3();this.mouseButtons={};this.touches={};controls.push(this);}
  update(){this.camera.lookAt(this.target);}listenToKeyEvents(){}dispose(){}
 }
 const host={clientWidth:800,clientHeight:600,append(){}};
 const map={extent:bounds,getBounds(){return{getWest:()=>this.extent[0],getSouth:()=>this.extent[1],getEast:()=>this.extent[2],getNorth:()=>this.extent[3]}},getPitch:()=>0,getBearing:()=>0,getProjection:()=>({type:'mercator'}),on(){},off(){}};
 const snapshot={volume:{bounds,envelopes:[],heldClasses:0,truncated:false,period:'2022–2024'},image:null,aquiferState:'ready'};
 const h=await componentHarness('app/aquifer-volume-view.tsx',{
  './subsurface-workers':{startAquiferVolumeWorker:()=>({terminate(){}})},'./aquifer-volume':volumeModel,'./subsurface-materials':materials,'./cutaway-model':cutaway,'./cutaway-camera':camera,'./aquifer-layers':{KGS_ATLAS_URL:'https://example.test/source'},'./subsurface.module.css':{default:styles},'./aquifer-volume-mesh':mesh,
  './aquifer-view-session':{locatorBounds:()=>map.extent,startAquiferView(value){sessionStarts++;options=value;return Object.assign(()=>{},{prepare(){prepares++;if(awaitingArea)return;if(!acceptsArea){value.onArea(null);value.onStatus('Choose a valid local area');return;}value.onArea(bounds);value.onStatus('Accepted selected area');value.onSnapshot(snapshot);}});}},
  './selected-surface-map':{default:function SelectedSurfaceMap(){}},'./cutaway-surface-detail':{detailBoundsFromSurface:()=>null,startCutawaySurfaceDetail(){throw Error('No provider capture is requested by layout changes');}},
  three:{...Three,WebGLRenderer:Renderer},'three/addons/controls/OrbitControls.js':{OrbitControls:Controls},
 },{
  matchMedia:query=>({matches:query.includes('max-width')?narrow:true,addEventListener(){},removeEventListener(){}}),document:doc,devicePixelRatio:1,performance,queueMicrotask,
  requestAnimationFrame:fn=>{const id=++frameId;frames.set(id,fn);return id;},cancelAnimationFrame:id=>frames.delete(id),
  ResizeObserver:class{constructor(callback){this.callback=callback;observers.push(this);}observe(target){this.target=target;}disconnect(){}},
 });
 const props={map,active:true,records:[record],onArea:value=>areas.push(value),onFlatMap(){throw Error('Layout cannot change the map representation');},onInspect:value=>inspections.push(value),onLocatorSlot(){},recordsLoading:false,recordStatus:'Eligible source records',partial:false,recordsAvailable:1,recordNavigation:{type:'section',props:{'aria-label':'Underground record timeline'}},onResetRecords(){},locator:{anchor:record.coordinates,pinned:true}};
 const flush=()=>{for(const [id,fn] of [...frames]){frames.delete(id);fn();}};
 const render=async()=>{
  tree=h.render(h.exports.default,props);
  const canvas=byClass(tree,'cutawayCanvas');if(canvas)canvas.props.ref.current=host;
  byClass(tree,'areaModel').props.ref.current={focus(value){focusCalls.push(value);doc.activeElement='selected-area';}};
  h.commit();await settle();flush();return tree;
 };
 await render();await render();
 const apply=async()=>{button(tree,'Show this area ↗').props.onClick();await render();await render();};
 return{h,render,apply,renderers,controls,host,observers,doc,focusCalls,areas,inspections,flush,props,waitForNextArea(){awaitingArea=true;},get options(){return options;},get prepares(){return prepares;},get sessionStarts(){return sessionStarts;},get tree(){return tree;}};
}

test('entry keeps the geographic selector visible until an area is explicitly applied',async()=>{
 const h=await harness({narrow:true});
 assert.equal(byClass(h.tree,'cutawayLocator').props.hidden,false);
 assert.equal(h.tree.props['data-ready'],false);assert.equal(h.tree.props['data-area-map'],'open');
 assert.equal(button(h.tree,'Show area map'),undefined);assert.equal(h.prepares,0);assert.equal(h.areas.length,0);assert.equal(h.focusCalls.length,0);
 h.h.dispose();
});

test('hiding and restoring the area map keeps the actual renderer, camera, accepted frame and selected record',async()=>{
 const h=await harness();await h.apply();assert.equal(h.renderers.length,1);assert.equal(h.renderers[0].disposed,undefined);
 const selection=findNode(h.tree,n=>n.props?.['aria-label']==='Sample location');selection.props.onChange({target:{value:record.id}});await h.render();
 const renderer=h.renderers[0],camera=renderer.camera,control=h.controls[0];assert.ok(camera,'actual Three camera was rendered');
 camera.position.set(7,8,9);control.target.set(1,2,3);
 const sourceView=findNode(h.tree,n=>n.props?.onCapture),frame=sourceView.props.bounds;
 const focusCount=h.focusCalls.length;
 for(const label of ['Hide area map','Show area map']){
  const toggle=button(h.tree,label);h.doc.activeElement=toggle;toggle.props.onClick();await h.render();
  assert.equal(h.doc.activeElement,toggle,'a layout control retains focus');
  assert.equal(h.renderers.length,1);assert.equal(renderer.disposed,undefined);assert.equal(renderer.camera,camera);
  same(camera.position.toArray(),[7,8,9]);same(control.target.toArray(),[1,2,3]);
  assert.equal(findNode(h.tree,n=>n.props?.onCapture).props.bounds,frame);
  assert.equal(findNode(h.tree,n=>n.props?.['aria-label']==='Sample location').props.value,record.id);
  assert.equal(h.prepares,1);assert.equal(h.sessionStarts,1);assert.equal(h.areas.length,1);assert.equal(h.focusCalls.length,focusCount);
 }
 assert.equal(h.inspections.length,1);assert.equal(h.inspections[0],record);h.h.dispose();
});

test('real canvas resize after hiding the selector preserves the inspection camera and target',async()=>{
 const h=await harness();await h.apply();const renderer=h.renderers[0],camera=renderer.camera,control=h.controls[0];
 camera.position.set(6,4,9);control.target.set(.5,-2,1);
 button(h.tree,'Hide area map').props.onClick();await h.render();
 h.host.clientWidth=1100;h.host.clientHeight=700;
 h.observers.find(observer=>observer.target===h.host).callback();h.flush();
 same(camera.position.toArray(),[6,4,9]);same(control.target.toArray(),[.5,-2,1]);assert.equal(camera.aspect,1100/700);
 assert.equal(h.renderers.length,1);assert.equal(h.prepares,1);assert.equal(h.areas.length,1);h.h.dispose();
});

test('narrow screens collapse after explicit apply, focus the selected workspace once and permit reopening',async()=>{
 const h=await harness({narrow:true});await h.apply();
 const toggle=button(h.tree,'Show area map'),locator=byClass(h.tree,'cutawayLocator');
 assert.equal(toggle.props['aria-expanded'],false);assert.equal(toggle.props['aria-controls'],locator.props.id);assert.equal(locator.props.hidden,true);
 assert.equal(h.doc.activeElement,'selected-area');same(h.focusCalls,[{preventScroll:false}]);
 h.doc.activeElement=toggle;toggle.props.onClick();await h.render();assert.equal(byClass(h.tree,'cutawayLocator').props.hidden,false);assert.equal(h.doc.activeElement,toggle);
 // Late source geometry is the same accepted slice, not another user navigation.
 h.options.onSnapshot({volume:{bounds,envelopes:[],heldClasses:0,truncated:false,period:'2022–2024'},image:null,aquiferState:'ready'});
 await h.render();assert.equal(byClass(h.tree,'cutawayLocator').props.hidden,false);assert.equal(h.focusCalls.length,1);assert.equal(h.prepares,1);h.h.dispose();
});

test('secondary settings and source details use closed native disclosures while time and view controls stay available',async()=>{
 const h=await harness();await h.apply();
 for(const name of ['surfaceDetailTools','sampleLocationTools','areaCameraTools']){
  const details=byClass(h.tree,name);assert.equal(details.type,'details');assert.equal(details.props.open,undefined);assert.ok(findNode(details,n=>n.type==='summary'));
 }
 assert.match(text(byClass(h.tree,'surfaceDetailTools')),/Imagery dates and resolution vary by location/);
 assert.match(text(byClass(h.tree,'surfaceDetailTools')),/Display context, not KFM evidence/);
 assert.ok(findNode(h.tree,n=>n.props?.['aria-label']==='Underground record timeline'));
 assert.equal(button(h.tree,'3D cutaway').props['aria-pressed'],true);
 assert.equal(button(h.tree,'Surface map').props['aria-pressed'],false);h.h.dispose();
});

test('an unsuccessful area apply never hides the selector or transfers focus',async()=>{
 const h=await harness({narrow:true,acceptsArea:false});await h.apply();
 assert.equal(byClass(h.tree,'cutawayLocator').props.hidden,false);assert.equal(h.tree.props['data-ready'],false);
 assert.equal(h.focusCalls.length,0);assert.equal(h.renderers.length,0);assert.equal(h.prepares,1);same(h.areas,[null]);
 h.options.onSnapshot(null);await h.render();assert.equal(byClass(h.tree,'cutawayLocator').props.hidden,false);assert.equal(h.focusCalls.length,0);h.h.dispose();
});

test('late snapshots of the prior frame cannot collapse or focus while a new apply awaits acceptance',async()=>{
 const h=await harness({narrow:true});await h.apply();
 button(h.tree,'Show area map').props.onClick();await h.render();const focusCount=h.focusCalls.length;
 h.waitForNextArea();await h.apply();assert.equal(h.prepares,2);assert.equal(h.areas.length,1);
 const prior={volume:{bounds,envelopes:[],heldClasses:0,truncated:false,period:'2022–2024'},image:null,aquiferState:'ready'};
 h.options.onSnapshot(prior);await h.render();assert.equal(byClass(h.tree,'cutawayLocator').props.hidden,false);assert.equal(h.focusCalls.length,focusCount);
 // The accepted-area callback, rather than any snapshot, owns layout navigation.
 const next=[-100.6,38.2,-100.2,38.6];h.options.onArea(next);h.options.onSnapshot({...prior,volume:{...prior.volume,bounds:next}});await h.render();
 assert.equal(byClass(h.tree,'cutawayLocator').props.hidden,true);assert.equal(h.focusCalls.length,focusCount+1);h.h.dispose();
});
