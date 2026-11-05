import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';

// Exercise the actual renderer's projected-hit lifecycle with a mock GL seam;
// actual shader/GPU rendering remains the separate built-app browser test.
const source=await readFile('app/kansas-sky-layer.ts','utf8');
const code=ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
const exports={};
new Function('exports','require','document',code)(exports,name=>{
  if(name==='./aviation-traffic')return {TRAFFIC_ALTITUDE_COLORS:[[0,'#7d8a96']]};
  if(name==='./kansas-sky')return {bankHeightOffset:(right,roll)=>-right*Math.sin((roll??0)*Math.PI/180)};
  throw Error(`Unexpected renderer dependency ${name}`);
},{hidden:false});
const {attachKansasSky,pickKansasSkyAircraft}=exports;
function fixture(loaded=true){
  const layers=new Map(),events=[],listeners=new Map();
  let styleLoaded=loaded;
  const gl=new Proxy({getShaderParameter:()=>true,getProgramParameter:()=>true,getAttribLocation:()=>0,getUniformLocation:()=>null},
    {get:(target,key)=>key in target?target[key]:()=>({})});
  const map={isStyleLoaded:()=>styleLoaded,getLayer:id=>layers.get(id),getZoom:()=>0,getProjection:()=>({type:'mercator'}),getCanvas:()=>({clientWidth:100,clientHeight:100}),
    on(name,fn){events.push(['on',name]);if(!listeners.has(name))listeners.set(name,new Set());listeners.get(name).add(fn);},
    off(name,fn){events.push(['off',name]);listeners.get(name)?.delete(fn);},triggerRepaint(){},queryTerrainElevation:()=>0,
    addLayer(layer){layers.set(layer.id,layer);layer.onAdd(map,gl);},removeLayer(id){layers.get(id)?.onRemove();layers.delete(id);}};
  const matrix=[1/512,0,0,0,0,1/512,0,0,0,0,0,0,-.25,-.5,0,1];
  return {map,events,setStyleLoaded:value=>{styleLoaded=value;},emit:name=>{for(const fn of [...(listeners.get(name)??[])])fn();},listenerCount:name=>listeners.get(name)?.size??0,draw:()=>layers.get('kfm-kansas-sky').render(gl,{modelViewProjectionMatrix:matrix})};
}
const aircraft={hex:'abc123',lon:-90,lat:0,onGround:false,altGeomFt:5000,altBaroFt:4800,trackDeg:90,rollDeg:null,emergency:null};
for(const readyEvent of ['render','error'])for(const phase of ['initial attachment','replacement style'])test(`aircraft renderer recovers after pending ${phase} on ${readyEvent} and cancels disposed work`,()=>{
  const f=fixture(phase!=='initial attachment'),selected=[];
  const renderer=attachKansasSky(f.map,hex=>selected.push(hex),message=>assert.fail(message));
  renderer.update([aircraft],[],null);
  if(phase==='replacement style'){
    f.draw();
    f.map.removeLayer('kfm-kansas-sky');
    f.setStyleLoaded(false);
    f.emit('style.load');
  }
  assert.equal(f.map.getLayer('kfm-kansas-sky'),undefined,'pending source work cannot install the layer');
  f.setStyleLoaded(true);
  f.emit(readyEvent);
  assert.ok(f.map.getLayer('kfm-kansas-sky'),'a ready frame installs the retained renderer without another style.load');
  f.draw();
  assert.equal(pickKansasSkyAircraft(f.map,{x:50,y:50}),true,'observations received while waiting become pickable');
  assert.deepEqual(selected,['abc123']);
  assert.equal(f.listenerCount('render'),0,'the completed install releases its frame listener');
  assert.equal(f.listenerCount('error'),0,'the completed install releases its settlement listener');
  f.map.removeLayer('kfm-kansas-sky');f.setStyleLoaded(false);f.emit('style.load');
  renderer.dispose();f.setStyleLoaded(true);f.emit('render');f.emit('error');f.emit('style.load');
  assert.equal(f.map.getLayer('kfm-kansas-sky'),undefined,'disposal cannot resurrect a pending renderer');
  assert.equal(f.listenerCount('render'),0,'disposal removes pending frame work');
  assert.equal(f.listenerCount('error'),0,'disposal removes pending settlement work');
  assert.equal(pickKansasSkyAircraft(f.map,{x:50,y:50}),false);
});
test('aircraft click ownership uses projected hits, preserves misses, and unregisters on disposal',()=>{
  const f=fixture(),selected=[];
  assert.equal(pickKansasSkyAircraft(f.map,{x:50,y:50}),false,'unmounted layer owns no clicks');
  const renderer=attachKansasSky(f.map,hex=>selected.push(hex),message=>assert.fail(message));
  assert.equal(f.events.some(([,name])=>name==='click'),false,'page remains the sole aircraft click dispatcher');
  renderer.update([aircraft],[],null);f.draw();
  assert.equal(pickKansasSkyAircraft(f.map,{x:0,y:0}),false);
  assert.deepEqual(selected,[]);
  assert.equal(pickKansasSkyAircraft(f.map,{x:50,y:50}),true);
  assert.deepEqual(selected,['abc123']);
  renderer.update([],[],null);f.draw();
  assert.equal(pickKansasSkyAircraft(f.map,{x:50,y:50}),false,'cleared observations leave no clickable stale aircraft');
  renderer.update([aircraft],[],null);f.draw();renderer.dispose();
  assert.equal(pickKansasSkyAircraft(f.map,{x:50,y:50}),false,'disposed layer owns no clicks');
  assert.deepEqual(selected,['abc123']);
});
test('page dispatch respects dedicated pick modes, aircraft hits and ordinary-context misses',async()=>{
  const page=await readFile('app/page.tsx','utf8');
  const ast=ts.createSourceFile('page.tsx',page,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
  let callback;
  function visit(node){
    if(ts.isCallExpression(node)&&node.expression.getText(ast)==='map.on'&&node.arguments[0]?.getText(ast)==='"click"'&&node.arguments[1]?.getText(ast).includes('pickKansasSkyAircraft'))callback=node.arguments[1].getText(ast);
    ts.forEachChild(node,visit);
  }
  visit(ast);assert.ok(callback,'actual map dispatcher includes aircraft ownership');
  for(const mode of ['aviation','underground','measure','aircraft','miss']){
    let picks=0;
    const scope={aviationPickingRef:{current:mode==='aviation'},undergroundOpenRef:{current:mode==='underground'},measureModeRef:{current:mode==='measure'?'point':null},
      measureCoordinatesRef:{set current(_value){throw Error('measurement owns click');}},
      pickKansasSkyAircraft:()=>{picks++;return mode==='aircraft';},map:{queryRenderedFeatures(){throw Error('ordinary context owns click');}}};
    const output=ts.transpileModule(`return ${callback};`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
    const click=new Function(...Object.keys(scope),output)(...Object.values(scope));
    if(mode==='measure')assert.throws(()=>click({point:{x:50,y:50},lngLat:{lng:-90,lat:0}}),/measurement owns click/);
    else if(mode==='miss')assert.throws(()=>click({point:{x:0,y:0}}),/ordinary context owns click/);
    else click({point:{x:50,y:50}});
    assert.equal(picks,mode==='aircraft'||mode==='miss'?1:0,'higher-priority tools prevent aircraft inspection');
  }
});
