import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';

// The welcome map's view module and its local dependencies as CommonJS in one context.
const files={'./welcome-map-view':'app/welcome-map-view.ts','./category-maps':'app/category-maps.ts','./category-basemaps':'app/category-basemaps.ts','./external-context-sources':'app/external-context-sources.ts','./kansas-orientation':'app/kansas-orientation.ts','./category-basemap-keys':'app/category-basemap-keys.ts'};
const compiled=Object.fromEntries(await Promise.all(Object.entries(files).map(async([id,path])=>[id,ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText])));
const cache=new Map();
function load(id){
 if(cache.has(id))return cache.get(id);
 const mod={exports:{}};cache.set(id,mod.exports);
 vm.runInNewContext(compiled[id],{module:mod,exports:mod.exports,require:dep=>{if(!(dep in compiled))throw new Error(`unexpected import ${dep}`);return load(dep);},URL,Object});
 cache.set(id,mod.exports);return mod.exports;
}
const view=load('./welcome-map-view'),maps=load('./category-maps'),basemaps=load('./category-basemaps');
const plain=value=>JSON.parse(JSON.stringify(value));

test('each topic previews the map it opens with, and the idle view is the default map of Kansas',()=>{
 for(const [topic,look] of Object.entries(maps.CATEGORY_MAPS)){
  const v=view.welcomeView(topic);
  assert.equal(v.topic,topic);assert.equal(v.basemap,look.basemap,`${topic}: the base map choice decides the preview`);
  assert.equal(v.scene,look.scene);assert.deepEqual(plain(v.camera),plain(look.camera));assert.equal(v.name,look.name);
 }
 for(const topic of [null,'unknown','__proto__'])assert.equal(view.welcomeView(topic),view.WELCOME_IDLE_VIEW);
 assert.equal(view.WELCOME_IDLE_VIEW.basemap,'standard','before a topic is chosen only the default-network vector map is requested');
 assert.equal(view.WELCOME_IDLE_VIEW.scene,'2d');
});

test('terrain looks get their own Terrarium DEM, globe looks the globe projection, flat maps neither',()=>{
 const relief=basemaps.CATEGORY_BASEMAPS.relief.style(),network=basemaps.CATEGORY_BASEMAPS.network.style();
 const terrain=view.welcomeStyle(relief,view.welcomeView('terrain'));
 assert.equal(terrain.projection.type,'mercator');
 assert.deepEqual(plain(terrain.terrain),{source:view.WELCOME_DEM_SOURCE_ID,exaggeration:view.WELCOME_TERRAIN_EXAGGERATION});
 assert.equal(terrain.sources[view.WELCOME_DEM_SOURCE_ID].type,'raster-dem');
 assert.notEqual(terrain.sources[view.WELCOME_DEM_SOURCE_ID],relief.sources[basemaps.BASEMAP_RELIEF_DEM_SOURCE_ID],'a separate source object, so hillshade and terrain do not share one');
 assert.equal(relief.terrain,undefined,'the shared basemap style is not modified');
 const engineering=view.welcomeStyle(network,view.welcomeView('engineering'));
 assert.equal(engineering.sources[view.WELCOME_DEM_SOURCE_ID].encoding,'terrarium','a style without a DEM gets the registered Terrarium source');
 const globe=view.welcomeStyle({version:8,sources:{},layers:[],terrain:{source:'x'}},view.welcomeView('sky'));
 assert.equal(globe.projection.type,'globe');assert.equal(globe.terrain,undefined);
 const flat=view.welcomeStyle(network,view.welcomeView('transport'));
 assert.equal(flat.projection.type,'mercator');assert.equal(flat.terrain,undefined);assert.equal(flat.sources[view.WELCOME_DEM_SOURCE_ID],undefined);
});

test('the drift turns tilted and globe views and eases flat maps, one slow leg at a time',()=>{
 const tilted=view.welcomeView('terrain'),flat=view.welcomeView('transport');
 const [a,b]=[0,1].map(leg=>view.welcomeDriftLeg(tilted,leg));
 assert.equal(a.bearing,tilted.camera.bearing+24);assert.equal(b.bearing,tilted.camera.bearing);assert.equal(a.zoom,tilted.camera.zoom);
 assert.ok(a.duration>=20000,'slow enough to read the map');
 const [c,d]=[0,1].map(leg=>view.welcomeDriftLeg(flat,leg));
 assert.equal(c.zoom,flat.camera.zoom+0.35);assert.equal(d.zoom,flat.camera.zoom);assert.equal(c.bearing,flat.camera.bearing);
});

test('the engine resolves styles itself, so one failed style never stalls later previews',async()=>{
 const source=await readFile('app/living-welcome/map-engine.mjs','utf8');
 assert.doesNotMatch(source,/transformStyle:/,'setStyle transformStyle waits for the previous style, which never loads after a failure');
 assert.match(source,/void resolveStyle\(BASEMAPS\[next\.basemap\]\.style\)\.then\(style => \{\s*if \(disposed \|\| styleKey !== key\) return;\s*map\.setStyle\(welcomeStyle\(style, view\), \{ diff: false \}\);/,'a superseded style is dropped; a pending one serves the topic selected when it arrives (behaviour in welcome-map-engine.test)');
 assert.match(source,/interactive: false/,'the welcome map is a backdrop, not a second map to operate');
 assert.match(source,/attributionControl: \{ compact: true \}/,'provider credits stay on the map');
 const stage=await readFile('app/living-welcome/DomainStage.jsx','utf8');
 assert.match(stage,/import\('\.\/map-engine\.mjs'\)/,'the map engine loads lazily after the welcome paints');
 const welcome=await readFile('app/living-welcome/welcome.jsx','utf8');
 assert.match(welcome,/<DomainStage topic=\{touched\?control:null\}/,'nothing but the default map until a visitor points at a category');
});
