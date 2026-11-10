import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';

async function load(file) {
  const code=ts.transpileModule(await readFile(file,'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
  return import('data:text/javascript;base64,'+Buffer.from(code).toString('base64'));
}
const {committedInspection}=await load('app/observatory/inspection.ts');
const performance=await load('app/map-performance.ts'), frameHelpers=await load('app/observatory/frame-data.ts');
const source=await readFile('app/observatory/workspace.tsx','utf8');
const ast=ts.createSourceFile('workspace.tsx',source,ts.ScriptTarget.Latest,true,ts.ScriptKind.TSX);
const declarations=new Map(), effects=[];let recordExpression,statusExpression,formatter;
function visit(node){
  if(ts.isVariableDeclaration(node)&&ts.isIdentifier(node.name)&&node.initializer)declarations.set(node.name.text,node.initializer.getText(ast));
  if(ts.isCallExpression(node)&&node.expression.getText(ast)==='useEffect')effects.push(node.arguments[0].getText(ast));
  if(ts.isFunctionDeclaration(node)&&node.name?.text==='weatherReadingText')formatter=node.getText(ast);
  if(ts.isJsxElement(node)){
    const attributes=node.openingElement.attributes.properties;
    if(attributes.some(a=>a.name?.getText(ast)==='className'&&a.initializer?.text==='event-feature-values'))recordExpression=node.parent.getText(ast);
    if(node.getText(ast).includes('Updating the selected record for the replay time')&&node.openingElement.tagName.getText(ast)==='p')statusExpression=node.parent.getText(ast);
  }
  ts.forEachChild(node,visit);
}visit(ast);
const effect=effects.find(e=>e.includes('const token = ++frameGeneration.current'));
assert.ok(effect);assert.ok(recordExpression);assert.ok(statusExpression);assert.ok(formatter);
const jsx=(type,props)=>({type,props});
function evaluate(expression,bindings){
  bindings={exports:{},...bindings};
  const code=ts.transpileModule('const result=('+expression+');',{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022,jsx:ts.JsxEmit.ReactJSX}}).outputText;
  return new Function(...Object.keys(bindings),code+'return result;')(...Object.values(bindings));
}
const textOf=node=>typeof node==='string'||typeof node==='number'?String(node):!node||typeof node!=='object'?'':[node.props?.children].flat(Infinity).map(textOf).join(' ').replace(/\s+/g,' ').trim();
const EMPTY={type:'FeatureCollection',features:[]};
const collection=(...properties)=>({type:'FeatureCollection',features:properties.map(p=>({type:'Feature',geometry:{type:'Point',coordinates:[-98.35,38.5]},properties:p}))});
const A='1900-05-19T23:00:00.000Z',B='1900-05-20T00:00:00.000Z';
const weather=(day,max=70)=>({station:'USC00143527',name:'SYNTHETIC REPLAY',day,maximumF:max,maximumFState:'reported',minimumF:44,minimumFState:'reported',precipitationInches:0,precipitationInchesState:'reported',snowfallInches:null,snowfallInchesState:'missing-presumed-zero',snowDepthInches:0,snowDepthInchesState:'reported'});
const initial={storms:false,radar:false,smoke:false,river:false,geology:false,flora:false,fauna:false,resources:false,counties:false,weather:true,earthquakes:false,shake:false};
const rawA=weather(A.slice(0,10)),rawB=weather(B.slice(0,10),99);
const frame=(time,data={})=>({time,data:{storms:EMPTY,river:EMPTY,counties:EMPTY,weather:EMPTY,earthquakes:EMPTY,shake:EMPTY,...data}});
const flush=async()=>{for(let i=0;i<16;i++)await Promise.resolve();};
function harness(){
  const state={requested:A,committed:A,loading:false,buffering:false,error:'',inspectionSelection:{track:'weather',properties:rawA},inspectionFrame:frame(A,{weather:collection(rawA)}),visible:{...initial}};
  const listeners=new Map(),sources=new Map(),timers=new Map(),held=new Set();let timerId=0,hidden=0;
  for(const id of ['ea-smoke','ea-river-data','ea-resource-data','ea-storms-data','ea-counties-data','ea-weather-data','ea-earthquakes-data','ea-shake-data'])sources.set(id,{ready:true,setData(data){this.data=data;this.ready=!held.has(id);}});
  const map={getSource:id=>sources.get(id),getLayer:()=>null,getStyle:()=>({layers:[]}),isSourceLoaded:id=>sources.get(id)?.ready===true,
    on(type,fn){if(!listeners.has(type))listeners.set(type,new Set());listeners.get(type).add(fn);},off(type,fn){listeners.get(type)?.delete(fn);},setFeatureState(){},moveLayer(){},setLayoutProperty(){}};
  const frameGeneration={current:0},frameRequest={current:null},sourceFailures={current:new Set()};
  const set=key=>value=>{state[key]=typeof value==='function'?value(state[key]):value;};
  const bindings=()=>({...state,...performance,...frameHelpers,committedInspection,EMPTY,LAYERS:evaluate(declarations.get('LAYERS'),{}),sourceFailures,mapRef:{current:map},mapReady:true,manifest:{start:A,end:'1900-05-20T05:00:00.000Z',radar:{scans:[]},smoke:{data:EMPTY},imagery:{dates:[]}},
    contextData:{weather:{date:state.requested.slice(0,10),data:collection(state.requested===A?rawA:rawB)}},countyEdition:'2020',river:null,loadedRiverResolution:'continuous',resourceData:null,order:Object.keys(initial),base:'reference',
    frameGeneration,frameRequest,radarSourceTime:{current:null},framesRef:{current:[]},urls:{current:new Map()},opacityRef:{current:{}},NEXRAD_EARLIEST_DAY:'2020-01-01',
    window:{setTimeout(fn,ms){assert.equal(ms,15000);const id=++timerId;timers.set(id,fn);return id;},clearTimeout:id=>timers.delete(id)},
    AbortController,URL,smokeAt:()=>EMPTY,stormRadarSites:()=>EMPTY,fetch(){assert.fail('Provider transport denied');},getRadarImage(){assert.fail('Radar transport denied');},getStorms(){assert.fail('Storm transport denied');},
    hideEventLayers(){hidden++;},setBuffering:set('buffering'),setError:set('error'),setCommitted:set('committed'),setInspectionFrame:set('inspectionFrame'),setBaseDay:set('baseDay'),setStormFrame:set('stormFrame'),setSourceErrors:set('sourceErrors'),setPlaying:set('playing')});
  const start=(requested,overrides={})=>{state.requested=requested;return evaluate(effect,{...bindings(),...overrides})();};
  const render=()=>{
    const b=bindings();const inspectedFeature=evaluate(declarations.get('inspectedFeature'),b);
    const props={...b,inspectedFeature,chosen:{id:state.inspectionSelection?.track??'weather'},weatherReadingText:evaluate(formatter,{}),require(name){assert.equal(name,'react/jsx-runtime');return{jsx,jsxs:jsx};}};
    return{inspectedFeature,record:textOf(evaluate(recordExpression,props)),status:textOf(evaluate(statusExpression,props))};
  };
  return{state,sources,held,timers,listeners,sourceFailures,start,render,emit(type){for(const fn of [...listeners.get(type)??[]])fn();},deadline(){for(const fn of [...timers.values()])fn();},get hidden(){return hidden;}};
}

test('actual frame effect and selected-record JSX follow the station across midnight and back without another click',async()=>{
  const h=harness();assert.match(h.render().record,/70/);h.state.error='The address bar now contains the replay link.';assert.match(h.render().record,/70/,'clipboard fallback must not invalidate a committed observation');const done=h.start(B);await flush();
  assert.equal(h.state.committed,B);assert.equal(h.render().inspectedFeature.properties.maximumF,99);assert.match(h.render().record,/99/);assert.match(h.render().record,/1900-05-20/);assert.doesNotMatch(h.render().record,/1900-05-19/);
  assert.match(h.render().record,/Withheld \(missing presumed zero\)/);assert.match(h.render().record,/Snow depth · in 0/);
  done();const back=h.start(A);await flush();assert.equal(h.render().inspectedFeature.properties.maximumF,70);assert.match(h.render().record,/1900-05-19/);back();
  assert.equal(h.timers.size,0);assert.equal([...h.listeners.values()].flatMap(s=>[...s]).length,0);
});

test('actual inspector withholds old values while a visible weather upload is pending and releases only after readiness',async()=>{
  const h=harness();h.held.add('ea-weather-data');const done=h.start(B);await flush();
  assert.equal(h.state.committed,A);assert.equal(h.state.buffering,true);assert.equal(h.render().record,'');assert.match(h.render().status,/Updating the selected record/);
  h.sources.get('ea-weather-data').ready=true;h.emit('sourcedata');await flush();assert.equal(h.state.committed,B);assert.equal(h.render().inspectedFeature.properties.maximumF,99);done();
});

test('a source failure or fixed readiness deadline cannot publish a stale selected record',async()=>{
  for(const failure of ['error','deadline']){
    const h=harness();h.held.add('ea-weather-data');const done=h.start(B);await flush();
    if(failure==='error'){h.sourceFailures.current.add('ea-weather-data');h.emit('error');}else h.deadline();await flush();
    assert.equal(h.state.committed,A);assert.equal(h.state.buffering,false);assert.ok(h.state.error);assert.equal(h.hidden,1);assert.equal(h.render().record,'');assert.match(h.render().status,/unavailable at this replay time/);assert.equal(h.timers.size,0);done();
  }
});

test('superseded pending frame cannot overwrite the current committed inspection after A-to-B-to-A',async()=>{
  const h=harness();h.held.add('ea-weather-data');const old=h.start(B);await flush();old();h.held.clear();const latest=h.start(A);await flush();h.sources.get('ea-weather-data').ready=true;h.emit('sourcedata');await flush();
  assert.equal(h.state.committed,A);assert.equal(h.state.inspectionFrame.time,A);assert.equal(h.render().inspectedFeature.properties.maximumF,70);latest();assert.equal(h.timers.size,0);
});

test('missing current record and hidden layer expose an explicit state without dropping the selection or resurrecting clicked bytes',async()=>{
  const h=harness();const done=h.start(B,{contextData:{}});await flush();assert.equal(h.state.committed,B);assert.equal(h.render().record,'');assert.match(h.render().status,/unavailable at this replay time/);assert.equal(h.state.inspectionSelection.properties,rawA);done();
  h.state.visible.weather=false;assert.match(h.render().status,/layer is hidden/);
  h.state.visible.weather=true;const restore=h.start(A);await flush();assert.equal(h.render().inspectedFeature.properties.maximumF,70);restore();
});

for(const track of ['counties','earthquakes','shake'])test(`active ${track} source must finish before the actual frame effect commits`,async()=>{
  const h=harness();h.state.visible={...initial,weather:false,[track]:true};const id=`ea-${track}-data`;h.held.add(id);const done=h.start(B);await flush();assert.equal(h.state.committed,A);assert.equal(h.state.buffering,true);h.sources.get(id).ready=true;h.emit('sourcedata');await flush();assert.equal(h.state.committed,B);done();
});

test('committed river inspection uses current sample provenance and true zero, withholds missing frames',()=>{
  const selection={track:'river',properties:{stationId:'USGS-06889000',value:100,unit:'ft3/s',observedAt:A}};
  const current={stationId:'USGS-06889000',value:0,unit:'m3/s',displayValue:'0 m3/s',observedAt:B,missing:false,approvalStatus:'approved'};
  const scope={requested:B,committed:B,ready:true,visible:true};
  const result=committedInspection(selection,frame(B,{river:collection(current)}),scope);assert.equal(result.properties,current);assert.equal(result.properties.value,0);assert.equal(result.properties.unit,'m3/s');assert.equal(result.properties.observedAt,B);
  assert.equal(committedInspection(selection,frame(B,{river:collection({...current,missing:true})}),scope),null);
});

test('earthquake, station epoch, Census and exact storm-scan identities resolve only unique current records',()=>{
  const scope={requested:B,committed:B,ready:true,visible:true};
  for(const [track,old,current] of [
    ['earthquakes',{featureId:'usgs-earthquake-a',magnitude:1},{featureId:'usgs-earthquake-a',magnitude:2}],
    ['shake',{featureId:'AM.A.epoch-1',name:'old'},{featureId:'AM.A.epoch-1',name:'new'}],
    ['counties',{geoid:'20001',population:1},{geoid:'20001',population:2}],
    ['storms',{kind:'cell',radar:'KICT',stormId:'A1',volumeTime:A,rotation:'weak'},{kind:'cell',radar:'KICT',stormId:'A1',volumeTime:A,rotation:'strong_low'}],
    ['storms',{kind:'radar',radar:'KICT'},{kind:'radar',radar:'KICT',radarName:'Wichita'}],
  ]){
    const selection={track,properties:old};assert.equal(committedInspection(selection,frame(B,{[track]:collection(current)}),scope)?.properties,current);
    assert.equal(committedInspection(selection,frame(B,{[track]:collection(current,{...current})}),scope),null,'ambiguous records cannot silently bind');
  }
  const storm={kind:'cell',radar:'KICT',stormId:'A1',volumeTime:A};assert.equal(committedInspection({track:'storms',properties:storm},frame(B,{storms:collection({...storm,volumeTime:B})}),scope),null,'a reused storm ID in another volume is a different observation');
  const selection={track:'weather',properties:rawA};for(const change of [{ready:false},{visible:false},{requested:A},{committed:A}])assert.equal(committedInspection(selection,frame(B,{weather:collection(rawB)}),{...scope,...change}),null);
  assert.equal(committedInspection({track:'__proto__',properties:{}},frame(B),scope),null);
  assert.equal(committedInspection({track:'weather',properties:{}},frame(B,{weather:collection(rawB)}),scope),null);
});
