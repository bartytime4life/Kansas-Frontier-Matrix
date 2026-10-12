import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { performance } from 'node:perf_hooks';
import os from 'node:os';
const baseline=process.argv[2];
if(!baseline) throw new Error('Usage: node scripts/measure-layer-lifecycle.mjs <baseline-directory containing page.tsx and map-runtime.ts>');
function compile(source,deps={}) { const code=ts.transpileModule(source,{compilerOptions:{target:ts.ScriptTarget.ES2022,module:ts.ModuleKind.CommonJS}}).outputText;const mod={exports:{}};new Function('require','module','exports',code)(id=>deps[id],mod,mod.exports);return mod.exports; }
const bounded=compile(await readFile('app/bounded-json.ts','utf8'));
const pageNew=await readFile('app/page.tsx','utf8'),pageOld=await readFile(`${baseline}/page.tsx`,'utf8');
async function dateReads(page,updated) {
  let requests=0;const states=[];const ref=current=>({current});
  const fetch=async()=>{requests++;await new Promise(resolve=>setTimeout(resolve,80));return Response.json({feed:'usgs-earthquakes',state:'empty',retrievedAt:'2024-06-03T00:00:00Z',featureCount:0,data:{type:'FeatureCollection',features:[]}});};
  const transport={browserJsonRequest:async url=>{const response=await fetch(url);return {response,body:await bounded.readBoundedJson(response,8388608)};}};
  const {LayerJsonReads}=compile(await readFile('app/layer-json-reads.ts','utf8'),{'./browser-json-request':transport});
  const ctx={useCallback:fn=>fn,announce:()=>{},currentUtcDay:()=>'2026-10-11',readFireDay:async()=>null,fetch,readBoundedJson:bounded.readBoundedJson,
    officialRequestsRef:ref(new Map()),officialArchiveDaysRef:ref({}),officialArchivePayloadsRef:ref({}),officialPayloadsRef:ref({}),setOfficialArchiveDays:()=>{},setOfficialPayloads:()=>{},setOfficialStates:fn=>states.push(fn({})),setOfficialErrors:()=>{},setOfficialReadPhases:()=>{},setEarthquakeArchiveFrameIndex:()=>{},setSmokeArchiveFrameIndex:()=>{},OFFICIAL_CONTEXT_BY_ID:{'usgs-earthquakes':{apiPath:'/api/live-context?feed=usgs-earthquakes',shortTitle:'Earthquakes'}},layerJsonReadsRef:ref(new LayerJsonReads()),validLayerPayload:()=>true,earthquakeEventTimes:()=>[],smokeValidityTimes:()=>[],smokeInitialFrameIndex:()=>-1,smokeValidAt:v=>v};
  const text=page.slice(page.indexOf('  const loadOfficialArchiveDay ='),page.indexOf('  const returnOfficialSourceToCurrent ='));
  const code=ts.transpileModule(text,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
  const load=new Function(...Object.keys(ctx),code+'\nreturn loadOfficialArchiveDay;')(...Object.values(ctx));
  const start=performance.now(),times=[];
  for(const day of ['2024-06-01','2024-06-02','2024-06-01','2024-06-02','2024-06-01','2024-06-02']){const mark=performance.now();await load('usgs-earthquakes',day);times.push(+(performance.now()-mark).toFixed(3));await new Promise(resolve=>setTimeout(resolve,0));}
  return {requests,totalMs:+(performance.now()-start).toFixed(3),coldMs:times.slice(0,2),repeatMs:times.slice(2),finalState:Object.values(states.at(-1))[0],updated};
}
const wanted=new Set(['temporalFilter','mergeFilters','evidenceFilterForRecord','registryFilters','registryZooms','registryOrders','setRegistryFilter','applyRegistryState','reorderRegistryLayers','applyTemporalRegistryFilters']);
function registryRuntime(source,registry){const ast=ts.createSourceFile('runtime.ts',source,ts.ScriptTarget.Latest,true);const subset=ast.statements.filter(s=>ts.isVariableStatement(s)&&s.declarationList.declarations.some(d=>ts.isIdentifier(d.name)&&wanted.has(d.name.text))).map(s=>s.getText(ast)).join('\n');
 const ctx={LAYER_REGISTRY:registry,addSystemLayers:()=>{},SYSTEM_LAYER_IDS:[],balanceMapFills:()=>{},requestFillOpacity:()=>{},composeMapLayers:()=>{}};
 const code=ts.transpileModule(subset,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
 const mod={exports:{}};new Function(...Object.keys(ctx),'exports',code)(...Object.values(ctx),mod.exports);return mod.exports;
}
function registryRun(source){
 const registry=Array.from({length:24},(_,i)=>({id:`layer-${i}`,sourceId:`source-${i}`,data:{type:'FeatureCollection',features:[]},temporal:{mode:'exact'},minZoom:0,maxZoom:16,defaultOpacity:.7,renderers:['circle','line'].map((type,j)=>({id:`renderer-${i}-${j}`,spec:{id:`renderer-${i}-${j}`,type},opacityProperties:[type==='circle'?'circle-opacity':'line-opacity']}))}));
 const runtime=registryRuntime(source,registry),layers=new Map(),sources=new Map();let counts={zoom:0,filter:0,layout:0,paint:0,order:0};
 const map={getLayer:id=>layers.get(id),getSource:id=>sources.get(id),addSource:(id,s)=>sources.set(id,s),addLayer:s=>layers.set(s.id,{...s,layout:{},paint:{}}),setLayerZoomRange:()=>counts.zoom++,setFilter:()=>counts.filter++,getLayoutProperty:(id,p)=>layers.get(id).layout[p],setLayoutProperty:(id,p,v)=>{counts.layout++;layers.get(id).layout[p]=v;},getPaintProperty:(id,p)=>layers.get(id).paint[p],setPaintProperty:(id,p,v)=>{counts.paint++;layers.get(id).paint[p]=v;},moveLayer:()=>counts.order++};
 const visibility=Object.fromEntries(registry.map(r=>[r.id,true])),opacity=Object.fromEntries(registry.map(r=>[r.id,.7])),order=registry.map(r=>r.id);
 runtime.applyRegistryState(map,visibility,opacity,2026,order);counts={zoom:0,filter:0,layout:0,paint:0,order:0};const start=performance.now();
 for(let i=0;i<100;i++)runtime.applyRegistryState(map,visibility,{...opacity,'layer-0':.4+i/1000},2026,order);
 const elapsed=performance.now()-start;return {iterations:100,layers:24,renderers:48,ms:+elapsed.toFixed(3),mutations:counts,totalMutations:Object.values(counts).reduce((a,b)=>a+b,0)};
}
const result={kind:'synthetic controlled layer lifecycle benchmark; no GPU, provider, INP, or device acceptance claim',recordedAt:new Date().toISOString(),environment:{node:process.version,platform:os.platform(),cpu:os.cpus()[0].model},scenario:{networkDelayMs:80,dates:['2024-06-01','2024-06-02'],iterations:6,cache:'page-owned exact URL; cold first two, warm remaining four',data:'empty earthquake fixture; 24-layer registry fixture; never production data'},before:{dateReads:await dateReads(pageOld,false),registry:registryRun(await readFile(`${baseline}/map-runtime.ts`,'utf8'))},after:{dateReads:await dateReads(pageNew,true),registry:registryRun(await readFile('app/map-runtime.ts','utf8'))}};
console.log(JSON.stringify(result,null,2));
