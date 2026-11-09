import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
import ts from 'typescript';

const compile = source => ts.transpileModule(source, {compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
function moduleFrom(path, require = () => {throw new Error('Unexpected runtime import');}) {
  const exports = {}; vm.runInNewContext(compile(readFileSync(path,'utf8')), {exports,require}); return exports;
}
const health = moduleFrom('app/basemap-health.ts'), perf = moduleFrom('app/map-performance.ts');
const page = readFileSync(process.env.KFM_BASEMAP_BASELINE ?? 'app/page.tsx','utf8');
const ast = ts.createSourceFile('page.tsx',page,ts.ScriptTarget.Latest,true,ts.ScriptKind.TSX);
const callbacks = {};
function visit(node) {
  if (ts.isCallExpression(node) && node.expression.getText(ast)==='map.on') {
    const name = node.arguments[0]?.text;
    const body=node.arguments[1]?.getText(ast) ?? '';
    if (name==='error' && body.includes('controlOwnsMapSourceErrors')
      || name==='sourcedata' && body.includes('OFFICIAL_CONTEXT_BY_SOURCE_ID')
      || name==='idle' && body.includes('Map readiness check')) callbacks[name] = body;
  }
  if (ts.isVariableDeclaration(node) && node.name.getText(ast)==='syncStyle') callbacks.style = node.initializer.getText(ast);
  if (ts.isCallExpression(node) && node.expression.getText(ast)==='useEffect' && node.arguments[0]?.getText(ast).includes('"Basemap style update"')) callbacks.replace = node.arguments[0].getText(ast);
  ts.forEachChild(node,visit);
}
visit(ast);
for (const name of ['error','sourcedata','idle','style','replace']) assert.ok(callbacks[name],name);
const callbackCode = compile(Object.entries(callbacks).map(([name,body])=>`exports.${name}=${body};`).join('\n'));
const dem = {type:'raster-dem',tiles:['https://example.invalid/current/{z}/{x}/{y}.png'],encoding:'terrarium',tileSize:256};
const coord = {canonical:{z:6,x:14,y:24}};
const event = (sourceId='basemap-relief-dem',state='errored',source=dem) => ({sourceId,source,tile:{state,tileID:coord},coord,error:Object.assign(new Error('https://private.invalid/?token=secret'),{status:503})});

function harness(basemap='aviation-chart') {
  const states = [], exports = {}, basemapHealth = health.createBasemapHealth(); basemapHealth.beginStyle();
  const specs = {'basemap-relief-dem':dem,openmaptiles:{type:'vector',url:'https://example.invalid/planet'},'orientation-kansas':{type:'geojson',data:{type:'FeatureCollection',features:[]}}};
  const sources = Object.fromEntries(Object.entries(specs).map(([id,spec])=>[id,{serialize:()=>spec}]));
  const ctx = {...perf,...health,exports,states,basemapHealth,basemapHealthRef:{current:basemapHealth},
    basemapRef:{current:basemap},basemap,
    BASEMAPS:{'aviation-chart':{title:'Aviation chart',style:{sources:specs}},midnight:{title:'Midnight navy',style:{sources:{'basemap-relief-dem':dem,'orientation-kansas':specs['orientation-kansas']}}}},
    VECTOR_BASEMAPS:new Set(['standard','aviation-chart']),LAYER_REGISTRY:[],OFFICIAL_CONTEXT_BY_SOURCE_ID:{},OFFICIAL_CONTEXT_SOURCES:[],
    officialContextForMapSource:()=>undefined,
    shouldFallbackStandardBasemap:(id,local,official,loaded=true)=>!local&&!official&&(id==='openmaptiles'||id==='ne2_shaded'||(!id&&!loaded)),
    runtimeError:null,degradedReason:null,styleFallbackAttempted:false,
    styleDocumentLoadedRef:{current:true},styleGenerationReadyRef:{current:true},mapMutationErrorRef:{current:null},
    hoverDrawerTimerRef:{current:null},hoverCandidateIdRef:{current:null},scenePresetRef:{current:'flat'},
    noaaRadarPendingFrameTimeRef:{current:null},noaaRadarFrameLoadCleanupRef:{current:null},noaaRadarFrameFailureRef:{current:null},
    attachedTerrainProviderRef:{current:null},officialRasterFailuresRef:{current:new Set()},terrainRasterViewRef:{current:{resetAll(){}}},
    cancelHoverSample(){},setHoverSummary(){},setHoverActive(){},syncTerrainRasterView(){},setTerrainState(){},
    setNoaaRadarFrameLoadState(){},setTerrainElevationReading(){},setTerrainElevationUnavailable(){},setPlaying(){},setStyleReady(){},
    setOfficialStates(){},setMaplibreProbe(){},setSourceStates(){},setSourceActivity(){},
    failedSourceIds:new Set(),TERRAIN_SOURCE_ID:'terrain-test',TERRAIN_HILLSHADE_SOURCE_ID:'hill-test',TERRAIN_COLOR_SOURCE_ID:'color-test',
    window:{clearTimeout(){}},version:'6.9.0',
    setRuntime(value){states.push(typeof value==='function'?value(states.at(-1)):value);},
    sameValues:(a,b)=>JSON.stringify(a)===JSON.stringify(b),
    setBasemap(value){ctx.basemapRef.current=value;ctx.basemap=value;},
    refreshMaplibreProbe:()=>({styleLoaded:true,canvasReady:true,tilesLoaded:true,sourcesReady:0,interactionsReady:true,failedChecks:[]}),
    // Abstract successful renderer/overlay synchronization while executing the
    // unchanged page's real warning-state transitions and style replacement.
    runMapMutation(label,fn){if(label!=='Map style synchronization')fn();return true;},
    hiDpiBasemapStyle:style=>style,
    map:{getSource:id=>sources[id],getPixelRatio:()=>1,setStyle(){exports.style();}},
  };
  ctx.mapRef={current:ctx.map};
  vm.runInNewContext(callbackCode,ctx);
  return {ctx,sources,states,error:e=>exports.error(e),data:e=>exports.sourcedata(e),idle:()=>exports.idle(),style:()=>exports.style(),
    replace(name='midnight',duringSetStyle){ctx.basemapRef.current=name;ctx.basemap=name;ctx.map.setStyle=()=>{for(const [id,spec] of Object.entries(specs))sources[id]={serialize:()=>spec};duringSetStyle?.();exports.style();};exports.replace();}};
}

test('a current failed tile remains warned after idle and source settlement',()=>{
  const h=harness();h.error(event());h.data({...event(),isSourceLoaded:true});h.idle();
  assert.equal(h.states.at(-1).message,health.BASEMAP_TILE_WARNING);
  assert.doesNotMatch(JSON.stringify(h.states),/private|secret/);
});
test('successful reload of the actual failed tile clears its warning',()=>{
  const h=harness();h.error(event());h.data(event('basemap-relief-dem','loaded'));h.idle();
  assert.equal(h.states.at(-1).kind,'ready');
});
test('a different loaded tile cannot clear the failed tile',()=>{
  const h=harness();h.error(event());const e=event('basemap-relief-dem','loaded');e.tile.tileID=e.coord={canonical:{z:6,x:15,y:24}};h.data(e);h.idle();
  assert.equal(h.states.at(-1).message,health.BASEMAP_TILE_WARNING);
});
test('successful replacement-style sync and tile loading retire the old style warning',()=>{
  const h=harness();h.error(event());h.replace();h.data(event('basemap-relief-dem','loaded'));h.idle();
  assert.equal(h.states.at(-1).kind,'ready');
});
test('replacement scope begins before setStyle can report a new current failure',()=>{
  const h=harness();h.error(event());h.replace('midnight',()=>h.error(event()));h.idle();
  assert.equal(h.states.at(-1).message,health.BASEMAP_TILE_WARNING);
});
test('style.load alone does not clear a current failed tile',()=>{
  const h=harness();h.error(event());h.style();h.idle();assert.equal(h.states.at(-1).message,health.BASEMAP_TILE_WARNING);
});
test('local GeoJSON errors remain visible without being classified as tile outages',()=>{
  const h=harness();h.error({sourceId:'orientation-kansas',source:{type:'geojson'},error:new Error('parse failed')});
  assert.ok(['degraded','error'].includes(h.states.at(-1).kind));assert.doesNotMatch(h.states.at(-1).message,/basemap tiles are unavailable/);
  assert.match(h.states.at(-1).message,/MAP_SOURCE_FAILED/);
});
test('tileless provider metadata/source failure remains meaningful and is not a tile claim',()=>{
  const h=harness('midnight');h.error({sourceId:'basemap-relief-dem',source:dem,error:new Error('metadata unavailable')});h.idle();
  assert.equal(h.states.at(-1).message,health.BASEMAP_SOURCE_WARNING);
  h.data(event('basemap-relief-dem','loaded'));h.idle();assert.equal(h.states.at(-1).message,health.BASEMAP_SOURCE_WARNING);
});
test('positively different source provenance cannot warn the current style',()=>{
  const h=harness('midnight');h.error(event('basemap-relief-dem','errored',{...dem,tiles:['https://example.invalid/obsolete/{z}/{x}/{y}.png']}));h.idle();
  assert.equal(h.states.at(-1).kind,'ready');
});
test('stale vector provenance is checked before automatic fallback',()=>{
  const h=harness();h.error(event('openmaptiles','errored',{type:'vector',url:'https://example.invalid/obsolete'}));
  assert.equal(h.ctx.basemapRef.current,'aviation-chart');
});
test('missing event provenance remains unknown, not silently dismissed as stale',()=>{
  const h=harness('midnight');const e=event();delete e.source;h.error(e);h.idle();assert.equal(h.states.at(-1).message,health.BASEMAP_TILE_WARNING);
});
test('explicit abort is not an outage and never clears an earlier real failure',()=>{
  const h=harness('midnight');const abort=event();abort.error.name='AbortError';h.error(abort);h.idle();assert.equal(h.states.at(-1).kind,'ready');
  h.error(event());h.error(abort);h.idle();assert.equal(h.states.at(-1).message,health.BASEMAP_TILE_WARNING);
});
test('vector fallback recovers without latching its temporary transition message',()=>{
  const h=harness();h.error(event('openmaptiles','errored',{type:'vector',url:'https://example.invalid/planet'}));
  assert.equal(h.ctx.basemapRef.current,'midnight');h.replace();h.idle();assert.equal(h.states.at(-1).kind,'ready');
});
test('a category vector tile failure after the existing fallback stays degraded rather than stopping navigation',()=>{
  const h=harness();h.ctx.styleFallbackAttempted=true;
  h.error(event('openmaptiles','errored',{type:'vector',url:'https://example.invalid/planet'}));
  assert.equal(h.ctx.basemapRef.current,'aviation-chart');assert.equal(h.states.at(-1).kind,'degraded');
  assert.equal(h.states.at(-1).message,health.BASEMAP_TILE_WARNING);
});
test('an independent renderer failure is still visible after basemap recovery',()=>{
  const h=harness();h.error(event());h.error({error:new Error('renderer failed')});h.data(event('basemap-relief-dem','loaded'));h.idle();
  assert.equal(h.states.at(-1).kind,'degraded');assert.match(h.states.at(-1).message,/MAP_RENDER_FAILED/);
});
test('matching coordinates from a replaced source object cannot clear an active failure',()=>{
  const h=health.createBasemapHealth(),one={},two={};h.beginStyle();h.error({sourceId:'relief',sourceInstance:one,sourceSpec:dem,event:event()});
  h.loaded({sourceId:'relief',sourceInstance:two,sourceSpec:dem,event:event('relief','loaded')});assert.equal(h.warning(),health.BASEMAP_TILE_WARNING);
});
test('tracking overflow stays explicitly unknown after all retained tiles recover',()=>{
  const h=health.createBasemapHealth(1),sourceInstance={};h.beginStyle();
  const input={sourceId:'relief',sourceInstance,sourceSpec:dem,event:event()};h.error(input);
  h.error({...input,event:{...event(),tile:{state:'errored',tileID:{canonical:{z:6,x:15,y:24}}}}});
  h.loaded({...input,event:event('relief','loaded')});assert.match(h.warning(),/exceeded the health tracking bound/);
  h.beginStyle();assert.equal(h.warning(),null);
});
