import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';

// Runs the real map `error`, `sourcedata` and `idle` handlers from page.tsx in
// one context, so they share `degradedReason` as they share the page closure.
const pagePath=process.env.KFM_PAGE_SOURCE??'app/page.tsx';
const source=await readFile(pagePath,'utf8'),ast=ts.createSourceFile('page.tsx',source,ts.ScriptTarget.Latest,true,ts.ScriptKind.TSX);
const commonjs=async path=>{const exports={};vm.runInNewContext(ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText,{exports});return exports;};
const performanceModule=await commonjs('app/map-performance.ts');
const terrainModule=await commonjs('app/terrain-raster-status.ts');
const healthModule=await commonjs('app/basemap-raster-health.ts');
const handlers={};
// page.tsx registers several handlers per event; pick the main map effect's.
const markers={error:'basemapStyle',sourcedata:'TERRAIN_SOURCE_ID',idle:'Map readiness check'};
function visit(node){if(ts.isCallExpression(node)&&node.expression.getText(ast)==='map.on'){const name=node.arguments[0]?.getText(ast)?.replaceAll('"','');const body=node.arguments[1]?.getText(ast);if(markers[name]&&body?.includes(markers[name]))handlers[name]=body;}ts.forEachChild(node,visit)}visit(ast);
assert.ok(handlers.error&&handlers.sourcedata&&handlers.idle);
const code=ts.transpileModule(`exports.error=${handlers.error};exports.sourcedata=${handlers.sourcedata};exports.idle=${handlers.idle};`,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;

const sourceId='kansas-ng911-2024';
// Tile 7/28/48 is inside Kansas.
const kansasTile={z:7,x:28,y:48};
const kansas={west:-102,east:-94.6,south:37,north:40},colorado={west:-109,east:-102.1,south:37,north:41};
function harness(){
 const states=[],exports={};let view=kansas,zoom=7;
 const map={getBounds:()=>({getWest:()=>view.west,getEast:()=>view.east,getSouth:()=>view.south,getNorth:()=>view.north}),getZoom:()=>zoom,getTerrain:()=>null,getSource:()=>undefined,isSourceLoaded:()=>true};
 const BASEMAPS={'kansas-aerial':{style:{sources:{[sourceId]:{type:'raster',maxzoom:18}}}},standard:{style:'https://example.invalid/style.json'}};
 const context={...performanceModule,...terrainModule,...healthModule,exports,map,BASEMAPS,basemapRef:{current:'kansas-aerial'},basemapRasterHealthRef:{current:new healthModule.BasemapRasterHealth()},
  LAYER_REGISTRY:[],OFFICIAL_CONTEXT_BY_SOURCE_ID:{},officialContextForMapSource:()=>undefined,degradedReason:null,runtimeError:null,
  setRuntime:state=>states.push(typeof state==='function'?state(states.at(-1)):state),
  TERRAIN_SOURCE_ID:'terrain-dem',scenePresetRef:{current:'map'},mapMutationErrorRef:{current:null},
  runMapMutation:(_label,run)=>run(),syncTerrainRasterView:()=>{},sameValues:(a,b)=>JSON.stringify(a)===JSON.stringify(b),version:'test',
  refreshMaplibreProbe:()=>({styleLoaded:true,canvasReady:true,tilesLoaded:true,sourcesReady:0,interactionsReady:true,failedChecks:[]})};
 vm.runInNewContext(code,context);
 return {states,context,settle(next,nextZoom=zoom){view=next;zoom=nextZoom;exports.idle();return states.at(-1);},
  fail:tile=>exports.error({sourceId,error:new Error('private provider URL must never enter UI'),...(tile?{tile:{tileID:{canonical:tile}}}:{})}),
  load:tile=>exports.sourcedata({sourceId,isSourceLoaded:true,tile:{state:'loaded'},coord:{canonical:tile}})};
}

test('a selected aerial tile failure leaves cutaway controls usable with explicit missing coverage',()=>{
 const h=harness();h.fail(kansasTile);
 assert.equal(h.states[0].kind,'degraded');assert.match(h.states[0].message,/Gaps are unknown/);assert.match(h.states[0].message,/controls and records remain available/);assert.doesNotMatch(h.states[0].message,/private provider/);
});

test('a basemap gap still in the settled view keeps the warning',()=>{
 const h=harness();h.fail(kansasTile);
 const settled=h.settle(kansas,7);
 assert.equal(settled.kind,'degraded');assert.match(settled.message,/Gaps are unknown/);
});

test('a tile that failed during movement retires once the camera settles elsewhere, and warns again if still failing there',()=>{
 const h=harness();h.fail(kansasTile);
 assert.equal(h.settle(colorado,7).kind,'ready','MapLibre never re-requests the old tile, so it cannot be a gap in this view');
 h.fail(kansasTile);
 assert.equal(h.settle(kansas,7).kind,'degraded','returning re-requests the tile; a repeat failure warns again');
});

test('a reloaded tile clears its own failure',()=>{
 const h=harness();h.fail(kansasTile);h.load(kansasTile);
 assert.equal(h.settle(kansas,7).kind,'ready');
});

test('a source-level failure stays until the basemap changes',()=>{
 const h=harness();h.fail();
 assert.equal(h.settle(colorado,4).kind,'degraded','no tile identity, so no view can retire it');
 h.context.basemapRef.current='standard';h.context.basemapRasterHealthRef.current.reset();
 assert.equal(h.settle(colorado,4).kind,'ready','a basemap switch does not inherit the old basemap gap');
});
