import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
import { componentHarness, findNode, settle } from './component-harness.mjs';
import { matchRedirect, requestContextFromRequest } from '../node_modules/vinext/dist/config/config-matchers.js';

// Analytic fixture only: the pinned provider identity exercises validation; these
// invented heights/corners are not field observations or GPU acceptance evidence.
function fixture() {
  const tile = 'NEON_D06_KONZ_DP3_706000_4336000', crs = 'PROJCRS["Analytic test UTM"]';
  return { format: 'kfm-neon-relay-pilot-v1', generatedAt: '2026-11-23T12:00:00Z', cache: { state: 'fresh', at: '2026-11-23T13:00:00Z' },
    review: { status: 'pending', scientific_accuracy_verified: false, source_admitted: false, canopy_native_max_m: 83.41000366210938, canopy_native_cells_above_50m: 5, surface_minus_ground_native_max_m: 32.5, notes: ['Invented analytic test values only.'] },
    preview: { schema_version: 'kfm-neon-lidar-preview-v1', data_kind: 'provider-files', generated_at: '2026-11-23T11:00:00Z', lifecycle: 'local-preview-only', source_admitted: false, released: false,
      source: { site: 'KONZ', month: '2024-09', acquisition_run: '2024_KONZ_10', release: 'RELEASE-2026', tile, attribution: 'Analytic fixture only', horizontal_crs: crs, vertical_reference: 'Test reference', vertical_reference_basis: 'Analytic test', canopy_floor_m: null, canopy_floor_basis: 'Unknown',
        files: ['dtm','dsm','chm'].map((kind,i) => ({ kind, name: `${tile}_${kind.toUpperCase()}.tif`, product: kind === 'chm' ? 'DP3.30015.001' : 'DP3.30024.001', bytes: 1000, sha256: 'abc'[i].repeat(64) })) },
      grid: { width: 8, height: 8, bounds: [706000,4336000,707000,4337000], source_resolution_m: 1, preview_resolution_m: 125, sampling: 'nearest-neighbor', dtm: Array.from({length:64},(_,i)=>300+i), dsm: Array.from({length:64},(_,i)=>312+i), chm: Array(64).fill(8) },
      georeferencing: { method: 'rasterio-warp-transform', target_crs: 'EPSG:4326', source_crs: crs, coordinate_epoch: null, height_values_transformed: false, horizontal_accuracy_m: null, corner_width: 9, corners: Array.from({length:81},(_,i)=>[-96.7+(i%9)*.0014,39.16-Math.floor(i/9)*.00112]) } } };
}
const url = source => `data:text/javascript;base64,${Buffer.from(ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`;
const source = name => readFile(`app/${name}.ts`,'utf8');
const previewUrl = url(await source('neon-lidar-preview')), preview = await import(previewUrl);
const boundedUrl = url(await source('bounded-json'));
const pilotUrl = url((await source('neon-lidar-pilot-client')).replace('"./bounded-json"',JSON.stringify(boundedUrl)).replace('"./neon-lidar-preview"',JSON.stringify(previewUrl)));
const science = await import(url((await source('neon-lidar-science')).replace('"./neon-lidar-pilot-client"',JSON.stringify(pilotUrl)).replace('"./neon-lidar-preview"',JSON.stringify(previewUrl))));
const mapModel = await import(url((await source('neon-lidar-map')).replace('"./neon-lidar-preview"',JSON.stringify(previewUrl)).replace('"./map-layer-composition"','"data:text/javascript,export const composeMapLayers=()=>{}"')));
const story = await import(url((await source('neon-lidar-story')).replace('"./neon-lidar-preview"',JSON.stringify(previewUrl))));
const {NEON_LOCAL_SOURCE:SOURCE,NEON_LOCAL_FILL:FILL,NEON_LOCAL_GROUND:GROUND}=mapModel;
const deferred = () => {let resolve,reject;const promise=new Promise((a,b)=>{resolve=a;reject=b;});return{promise,resolve,reject};};

async function harness(options={}) {
  const timers=new Map(); let timerId=0, env;
  const controllerHarness=await componentHarness('app/terrain/terrain-controller.ts',{
    '../maplibre-seam':{loadMapLibre:()=>{env.loads++;return Promise.resolve(env.lib);}},'../map-performance':{browserRenderBudget:()=>({pixelRatio:1.5,tileCache:24})},'../webgl-support':{webgl2Available:()=>options.webgl!==false},'../neon-lidar-pilot-client':{readNeonLidarPilot:signal=>{env.reads++;env.signal=signal;return Promise.resolve(options.receipt??fixture());}},'../neon-lidar-science':science,'../neon-lidar-preview':preview,'../neon-lidar-map':mapModel,'../neon-lidar-story':story,
  },{queueMicrotask:options.nativeQueue??queueMicrotask,ResizeObserver:class{constructor(fn){this.fn=fn;}observe(){env.resize=this.fn;}disconnect(){env.unobserved++;}},...options.globals,setTimeout:(fn,ms)=>{const id=++timerId;timers.set(id,{fn,ms});return id;},clearTimeout:id=>timers.delete(id)});
  env={maps:[],loads:0,reads:0,unobserved:0,states:[],timers,host:{getBoundingClientRect:()=>({width:1000,height:550})},...options};
  class FakeMap {
    constructor(config){this.config=config;this.events=new Map();this.sources=new Map();this.layers=new Map();this.canvas=new EventTarget();this.canvas.setAttribute=()=>{};this.fits=[];this.moves=[];this.zoom=14;this.bearing=-25;this.resizeCount=0;this.removed=0;this.hits=[];this.sourceReady=false;this.projection=config.style.projection;env.maps.push(this);}
    on(name,fn){if(!this.events.has(name))this.events.set(name,new Set());this.events.get(name).add(fn);return this;}
    off(name,fn){this.events.get(name)?.delete(fn);return this;}
    emit(name,event={}){for(const fn of [...(this.events.get(name)||[])])fn(event);}
    getCanvas(){return this.canvas;} remove(){this.removed++;} resize(){this.resizeCount++;return this;}
    getProjection(){return this.projection;} setProjection(value){this.projection=value;} getTerrain(){return null;}
    getSource(id){return this.sources.get(id);} getLayer(id){return this.layers.get(id);}
    addSource(id,spec){this.sources.set(id,{...spec,setData:data=>{this.sources.get(id).data=data;if(env.failOnData)this.emit('error');}});}
    addLayer(spec){this.layers.set(spec.id,structuredClone(spec));if(env.failOnLayer)this.emit('error');}
    removeLayer(id){this.layers.delete(id);} removeSource(id){this.sources.delete(id);}
    setFilter(id,value){this.layers.get(id).filter=value;} setPaintProperty(id,key,value){this.layers.get(id).paint[key]=value;}
    fitBounds(bounds,config){this.fits.push({bounds,config});this.pitch=config.pitch;this.bearing=config.bearing;this.zoom=14;}
    easeTo(config){this.moves.push(config);if(config.bearing!==undefined)this.bearing=config.bearing;}
    getZoom(){return this.zoom;} getBearing(){return this.bearing;}
    isSourceLoaded(){return this.sourceReady;} queryRenderedFeatures(...args){this.lastQuery=args;return this.hits;}
    triggerRepaint(){this.repaint=true;}
  }
  const lib={Map:FakeMap,setWorkerUrl:value=>env.worker=value};
  const runtime={loadMap:()=>{env.loads++;return options.mapPending?.promise??Promise.resolve(lib);},readPilot:signal=>{env.reads++;env.signal=signal;return options.pilotPending?.promise??Promise.resolve(options.receipt??fixture());},webgl:()=>options.webgl!==false,budget:()=>({pixelRatio:1.5,tileCache:24}),observe:(_host,fn)=>{env.resize=fn;return()=>env.unobserved++;},defer:options.defer??queueMicrotask};
  env.lib=lib;
  env.controller=options.productionDefault
    ? controllerHarness.exports.createTerrainController(env.host,state=>env.states.push(state),options.reduced??false)
    : controllerHarness.exports.createTerrainController(env.host,state=>env.states.push(state),options.reduced??false,runtime);
  env.current=()=>env.controller.getState();env.stop=()=>env.controller.dispose();
  await settle();return env;
}
const ready=env=>{const map=env.maps[0];map.emit('style.load');map.sourceReady=true;map.hits=[{source:SOURCE,properties:{row:0,column:0}}];map.emit('render');return map;};

test('production default startup preserves the browser global receiver for native microtask scheduling',async()=>{
  // WebIDL operation semantics: undefined/null uses the relevant global;
  // a non-null ordinary receiver cannot implement Window/WorkerGlobalScope.
  // Node's queueMicrotask does not make this receiver check, so ordinary Node
  // injection hid the original client-effect Illegal invocation failure.
  const brand=Symbol('browser-global'),pending=[],receivers=[];
  function nativeQueue(callback){
    if(this!=null&&this.__terrainWindowBrand!==brand)throw new TypeError('Illegal invocation');
    receivers.push(this);pending.push(callback);
  }
  assert.throws(()=>({defer:nativeQueue}).defer(()=>{}),/Illegal invocation/);
  const env=await harness({productionDefault:true,nativeQueue,globals:{__terrainWindowBrand:brand}});
  try{
    assert.equal(pending.length,1);assert.equal(env.reads,0);assert.equal(env.loads,0,'default session is deferred until the native microtask runs');
    assert.equal(receivers[0].__terrainWindowBrand,brand,'production default calls the actual global, not its runtime container');
    pending.shift()();await settle();assert.equal(env.reads,1);assert.equal(env.loads,1);
    const map=ready(env);assert.equal(env.current().phase,'ready');assert.equal(map.fits[0].config.pitch,60);
    env.stop();assert.equal(env.signal.aborted,true);assert.equal(map.removed,1);assert.equal(env.unobserved,1);assert.equal(env.timers.size,0);
  }finally{env.stop();}
});

test('direct session automatically loads once, frames pitched 3× columns and waits for actual owned viewport features',async()=>{
  const env=await harness();try{
    assert.equal(env.reads,1);assert.equal(env.loads,1);assert.equal(env.worker,'/maplibre/maplibre-gl-worker.mjs');
    const map=env.maps[0];assert.deepEqual({...map.config.style.sources},{});assert.equal(map.config.style.projection.type,'mercator');assert.equal(map.layers.size,0);
    map.emit('style.load');assert.equal(env.current().phase,'rendering');assert.equal(map.getLayer(FILL).type,'fill-extrusion');
    assert.equal(map.fits.length,1);assert.equal(map.fits[0].config.pitch,60);assert.equal(map.fits[0].config.bearing,-25);assert.equal(map.fits[0].config.duration,0);
    assert.equal(map.getSource(SOURCE).data.features[1].properties.display_top_m,3);
    map.emit('render');assert.equal(env.current().phase,'rendering');map.sourceReady=true;map.emit('render');assert.equal(env.current().phase,'rendering','loaded source with blank viewport is not success');
    map.hits=[{source:'foreign'}];map.emit('render');assert.equal(env.current().phase,'rendering');map.hits=[{source:SOURCE}];map.emit('render');assert.equal(env.current().phase,'ready');assert.equal(env.timers.size,0);
    const fits=map.fits.length;env.resize();assert.equal(map.fits.length,fits,'resize does not repeatedly reframe the user camera');
  }finally{env.stop();}
});

test('mode, scale, overhead and story actions change real renderer geometry while preserving native measurements',async()=>{
  const receipt=fixture();receipt.preview.grid.chm[2]=28.65;const env=await harness({receipt});try{
    const map=ready(env),controller=env.controller;assert.equal(env.current().probe.dtm,363,'initial actual high ground is automatically inspected');
    controller.setMode('chm');controller.setScale(5);assert.ok(map.getLayer(GROUND));assert.equal(map.getSource(SOURCE).data.features[2].properties.display_top_m,(2+28.65)*5);
    controller.focus('high-canopy');assert.equal(env.current().column,'3');assert.equal(env.current().probe.chm,28.65);assert.equal(env.current().probe.surfaceAboveGround,12);assert.equal(map.moves.at(-1).zoom,14,'focus cannot zoom into high columns beyond fitted view');
    controller.show2D();assert.equal(map.getLayer(FILL).type,'fill');assert.equal(map.fits.at(-1).config.pitch,0);controller.show3D();assert.equal(map.getLayer(FILL).type,'fill-extrusion');assert.equal(map.fits.at(-1).config.pitch,60);assert.equal(env.current().scale,5);
    controller.setReducedMotion(true);controller.turn(30);controller.focus('low-ground');assert.equal(map.moves.at(-1).duration,0);
    assert.deepEqual(receipt.preview.grid.chm,fixture().preview.grid.chm.map((v,i)=>i===2?28.65:v),'source values are not exaggerated');
  }finally{env.stop();}
});

test('clicked pedestal/columns and editable bounded coordinates select the exact same original cell, including zero/null',async()=>{
  const receipt=fixture();receipt.preview.grid.chm[0]=0;receipt.preview.grid.dtm[1]=null;const env=await harness({receipt});try{
    const map=ready(env),c=env.controller;c.setMode('chm');map.emit('render');map.hits=[{source:SOURCE,properties:{row:0,column:0}}];map.emit('click',{point:{x:1,y:2}});
    assert.equal(env.current().probe.chm,0);assert.deepEqual(Array.from(map.lastQuery[1].layers),[FILL,GROUND]);
    c.setCoordinate('row','001');c.setCoordinate('column','002');assert.equal(env.current().probe.dtm,null);assert.equal(env.current().probe.differenceIssue,'missing');assert.equal(env.current().probe.easting,706187.5);
    c.setCoordinate('column','');assert.equal(env.current().column,'');assert.equal(env.current().probe,null);c.setCoordinate('column','999');assert.equal(env.current().probe,null);c.setCoordinate('column','1e0');assert.equal(env.current().probe,null);c.setCoordinate('column','1');assert.equal(env.current().probe.chm,0);
  }finally{env.stop();}
});

test('synchronous MapLibre addLayer and setData errors remain terminal and cannot publish rendering over failure',async()=>{
  for(const point of ['layer','data']){
    const env=await harness({failOnLayer:point==='layer'});try{
      const map=env.maps[0];map.emit('style.load');if(point==='data'){map.sourceReady=true;map.hits=[{source:SOURCE}];map.emit('render');env.failOnData=true;env.controller.setScale(4);}
      assert.equal(env.current().phase,'error');assert.equal(map.removed,1);assert.equal(env.signal.aborted,true);assert.equal(env.timers.size,0);assert.equal(env.states.at(-1).phase,'error');map.emit('render');assert.equal(env.current().phase,'error');
    }finally{env.stop();}
  }
});

test('stalled map import times out before construction and late imports/receipt completions are ignored',async()=>{
  const mapPending=deferred(),pilotPending=deferred(),env=await harness({mapPending,pilotPending});try{
    assert.equal(env.timers.size,1);const deadline=[...env.timers.values()][0];assert.equal(deadline.ms,20000);deadline.fn();assert.equal(env.current().phase,'error');assert.equal(env.signal.aborted,true);
    mapPending.resolve(env.lib);pilotPending.resolve(fixture());await settle();assert.equal(env.maps.length,0);assert.equal(env.current().dataset,null);assert.equal(env.current().phase,'error');
  }finally{env.stop();}
});

test('render deadline and context loss dispose GPU resources; a fresh retry session starts both resources again',async()=>{
  const env=await harness();const map=ready(env);map.canvas.dispatchEvent(new Event('webglcontextlost',{cancelable:true}));assert.equal(env.current().phase,'error');assert.match(env.current().message,/context was lost/);assert.equal(map.removed,1);assert.equal(env.unobserved,1);env.stop();assert.equal(map.removed,1);
  const retry=await harness();try{const replacement=retry.maps[0];replacement.emit('style.load');const timeout=[...retry.timers.values()][0];timeout.fn();assert.equal(retry.current().phase,'error');assert.equal(replacement.removed,1);assert.equal(retry.reads,1);assert.equal(retry.loads,1);}finally{retry.stop();}
});

test('retired Strict Mode attempts acquire nothing; disposal aborts in-flight work and blocks stale state',async()=>{
  const deferredStarts=[],env=await harness({defer:fn=>deferredStarts.push(fn)});env.stop();deferredStarts[0]();await settle();assert.equal(env.reads,0);assert.equal(env.loads,0);
  const mapPending=deferred(),pilotPending=deferred(),late=await harness({mapPending,pilotPending});late.stop();const count=late.states.length;assert.equal(late.signal.aborted,true);assert.equal(late.timers.size,0);mapPending.resolve(late.lib);pilotPending.resolve(fixture());await settle();assert.equal(late.maps.length,0);assert.equal(late.states.length,count);
});

test('WebGL and receipt/georeferencing failures explain unavailable state rather than reporting blank success',async()=>{
  const unsupported=await harness({webgl:false});assert.equal(unsupported.current().phase,'unsupported');assert.equal(unsupported.reads,0);assert.equal(unsupported.loads,0);unsupported.stop();
  for(const mutate of [r=>r.review.source_admitted=true,r=>delete r.preview.georeferencing]){const receipt=fixture();mutate(receipt);const env=await harness({receipt});assert.equal(env.current().phase,'error');assert.equal(env.current().dataset,null);env.stop();}
  const env=await harness({host:{getBoundingClientRect:()=>({width:80,height:100})}});env.maps[0].emit('style.load');assert.equal(env.current().phase,'error','zero/tiny hosts cannot be declared framed');env.stop();
});

test('direct page binds visible mode/scale/story and retry controls, cleans the retired session and respects motion changes',async()=>{
  const sessions=[],media={matches:true,addEventListener:(_name,fn)=>media.change=fn,removeEventListener:()=>media.removed=true};
  const initial=()=>({phase:'loading',message:'Loading',dataset:null,mode:'dtm',scale:3,representation:'columns',metadata:null,row:'',column:'',probe:null,stops:[],activeStop:null});
  const h=await componentHarness('app/terrain/TerrainView.tsx',{'next/link':{default:'a'},'./terrain-controller':{initialTerrainState:initial,createTerrainController:(host,update,reduced)=>{const calls=[];const session={host,update,reduced,calls,dispose:()=>calls.push(['dispose']),setReducedMotion:v=>calls.push(['motion',v]),setMode:v=>calls.push(['mode',v]),setScale:v=>calls.push(['scale',v]),show3D:()=>calls.push(['3d']),show2D:()=>calls.push(['2d']),turn:v=>calls.push(['turn',v]),focus:v=>calls.push(['focus',v]),setCoordinate:(...args)=>calls.push(['coordinate',...args])};sessions.push(session);return session;}},'../neon-lidar-science':science,'../neon-lidar-preview':preview,'../maplibre-seam.css':{},'./terrain.module.css':{default:new Proxy({},{get:(_t,key)=>key})}}, {window:{matchMedia:()=>media}});
  let tree=h.render(h.exports.default);const host=findNode(tree,n=>n.props?.['data-terrain-map']==='');host.props.ref.current={};h.commit();assert.equal(sessions.length,1);assert.equal(sessions[0].reduced,true);
  const dataset=science.createNeonScienceDataset(fixture());sessions[0].update({...initial(),phase:'ready',dataset,stops:story.buildNeonStoryStops(dataset.receipt.preview),probe:preview.neonLidarProbe(dataset.receipt.preview,0,0),row:'1',column:'1'});tree=h.render(h.exports.default);h.commit();
  const canopy=findNode(tree,n=>n.type==='button'&&n.props.children?.[0]?.props?.children==='Canopy');canopy.props.onClick();findNode(tree,n=>n.props?.id==='terrain-scale').props.onChange({target:{value:'4.5'}});findNode(tree,n=>n.type==='button'&&n.props.children==='Fit & tilt 3D').props.onClick();assert.deepEqual(sessions[0].calls,[['mode','chm'],['scale',4.5],['3d']]);
  assert.ok(findNode(tree,n=>n.props?.['aria-label']==='Ground color scale in original metres'));assert.ok(findNode(tree,n=>n.props?.href==='/labs/terrain'));
  media.matches=false;media.change();assert.deepEqual(sessions[0].calls.at(-1),['motion',false]);
  sessions[0].update({...initial(),phase:'error'});tree=h.render(h.exports.default);findNode(tree,n=>n.type==='button'&&n.props.children==='Retry 3D').props.onClick();tree=h.render(h.exports.default);h.commit();assert.equal(sessions.length,2);assert.ok(sessions[0].calls.some(c=>c[0]==='dispose'));h.dispose();assert.ok(sessions[1].calls.some(c=>c[0]==='dispose'));
});

test('native QA warnings use the validated receipt and show no unvalidated statistics during loading',async()=>{
  const alt=fixture();alt.review.canopy_native_max_m=90.25;alt.review.canopy_native_cells_above_50m=7;
  const dataset=science.createNeonScienceDataset(alt);assert.ok(dataset);
  const visibleText=node=>node==null||typeof node==='boolean'?'':typeof node!=='object'?String(node):[node.props?.children].flat(Infinity).map(visibleText).join(' ');
  for(const loaded of [false,true]){
    const state={phase:loaded?'ready':'loading',message:'Loading',dataset:loaded?dataset:null,mode:'dtm',scale:3,representation:'columns',metadata:null,row:'',column:'',probe:null,stops:[],activeStop:null};
    const h=await componentHarness('app/terrain/TerrainView.tsx',{'next/link':{default:'a'},'./terrain-controller':{initialTerrainState:()=>state,createTerrainController:()=>{throw new Error('Effects not mounted for presentation check');}},'../neon-lidar-science':science,'../neon-lidar-preview':preview,'../maplibre-seam.css':{},'./terrain.module.css':{default:new Proxy({},{get:(_t,key)=>key})}});
    const tree=h.render(h.exports.default),warning=findNode(tree,n=>n.props?.className==='reviewStrip'),text=visibleText(warning).replace(/\s+/g,' ');
    assert.doesNotMatch(text,/83\.41|5 cells/);
    if(loaded){assert.match(text,/90\.25 m maximum and 7 cells above 50 m/);assert.doesNotMatch(text,/Source-specific statistics appear/);}
    else{assert.match(text,/after the receipt is validated/);assert.doesNotMatch(text,/maximum|cells above/);}
    h.dispose();
  }
});

test('legacy review alias matches the exact query only, preserving normal root and all existing routes',async()=>{
  const config=await import(url((await readFile('next.config.ts','utf8')).replace('import { browserHeaders } from "./server/browser-headers.mjs";','const browserHeaders={};')));
  const redirects=await config.default.redirects();const match=value=>{const request=new Request(`https://example.test${value}`);return matchRedirect(new URL(request.url).pathname,redirects,requestContextFromRequest(request));};
  assert.deepEqual(match('/?neon-review=3'),{destination:'/terrain',permanent:false});for(const path of ['/','/?neon-review=30','/?neon-review=','/?other=3','/labs/terrain?neon-review=3','/terrain?neon-review=3'])assert.equal(match(path),null);
  for(const path of ['app/terrain/page.tsx','app/terrain/TerrainView.tsx','app/terrain/terrain-controller.ts']){const compiled=ts.transpileModule(await readFile(path,'utf8'),{fileName:path,reportDiagnostics:true,compilerOptions:{jsx:ts.JsxEmit.ReactJSX,target:ts.ScriptTarget.ES2022}});assert.deepEqual(compiled.diagnostics.filter(d=>d.category===ts.DiagnosticCategory.Error),[],`valid route syntax: ${path}`);}
  const route=await readFile('app/terrain/page.tsx','utf8');assert.match(route,/<TerrainView\/>/);assert.match(route,/canonical: 'https:\/\/kansasfrontiermatrix.com\/terrain'/);
  const welcome=await readFile('app/living-welcome/welcome.jsx','utf8');assert.ok(welcome.indexOf('href="/terrain">3D Terrain')<welcome.indexOf('<details className="welcome-preferences">'),'direct entry is outside closed Options');
});
