import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';
import {installWelcomeAttributionFixture} from './welcome-attribution-browser-fixtures.mjs';

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

test('each topic previews real map renderers and starters, and the idle view is the default map of Kansas',()=>{
 for(const [topic,look] of Object.entries(maps.CATEGORY_MAPS)){
  const v=view.welcomeView(topic);
  assert.equal(v.topic,topic);
  if(!['flora','fauna','ecology','land','history','evidence','public-safety'].includes(topic)){
   assert.equal(v.basemap,look.basemap);assert.equal(v.scene,look.scene);assert.deepEqual(plain(v.camera),plain(look.camera));assert.equal(v.name,look.name);
  }else assert.ok(v.key,'the geographic preview retains its short source key');
  for(const id of look.starters.filter(id=>!view.WELCOME_PREVIEW_SKIPPED_STARTERS.has(id)))assert.ok(v.starters.includes(id),`${topic}: the preview retains its own starters`);
  assert.ok(v.starters.length||v.scientificLayers.length||v.scene==='terrain',`${topic}: a scientific layer or real terrain, beyond a plain basemap`);
 }
 for(const topic of [null,'unknown','__proto__'])assert.equal(view.welcomeView(topic),view.WELCOME_IDLE_VIEW);
 assert.equal(view.WELCOME_IDLE_VIEW.basemap,'standard','before a topic is chosen only the default-network vector map is requested');
 assert.equal(view.WELCOME_IDLE_VIEW.scene,'2d');
 assert.deepEqual(plain(view.WELCOME_IDLE_VIEW.starters),[],'the default map carries no data');
 assert.deepEqual(plain(view.WELCOME_IDLE_VIEW.scientificLayers),[],'tools stay off before a choice');
 assert.deepEqual(plain(view.welcomeView('weather').starters),['nws-alerts','nws-radar'],'the storm preview shows alerts and its newest current radar scan');
 assert.deepEqual(plain(view.welcomeView('geology').starters),['usgs-earthquakes']);
 assert.deepEqual([...view.WELCOME_PREVIEW_SKIPPED_STARTERS].sort(),['usgs-streamflow']);
});

test('basemap-only cards gain appropriate existing science without changing working-map defaults',()=>{
 for(const topic of ['ecology','flora'])assert.deepEqual(plain(view.welcomeView(topic).scientificLayers),['land-cover']);
 assert.deepEqual(plain(view.welcomeView('agriculture').scientificLayers),['cropland']);
 assert.deepEqual(plain(view.welcomeView('sky').scientificLayers),['daylight']);
 assert.deepEqual(plain(view.welcomeView('water').starters),['usgs-wbd-watersheds'],'no managed gauge network on hover');
 assert.deepEqual(plain(view.welcomeView('fauna').scientificLayers),['animal-records']);
 assert.deepEqual(plain(view.welcomeView('public-safety').starters),['deflock-alpr']);
 for(const topic of ['evidence']){
  assert.deepEqual(plain(view.welcomeView(topic).starters),['census-counties']);
  assert.deepEqual(plain(maps.CATEGORY_MAPS[topic].starters),[],'a preview never enables the opened map\'s layers');
 }
 assert.match(view.welcomeView('fauna').detail,/2025.*coarse hexagons/);
 assert.match(view.welcomeView('fauna').detail,/not abundance/);
 assert.deepEqual(plain(view.welcomeView('land').starters),['blm-plss-townships','blm-plss-sections']);
 assert.ok(view.welcomeView('land').camera.zoom>=11);
 assert.equal(maps.CATEGORY_MAPS.land.camera.zoom,8.4,'the closer preview leaves working-map defaults intact');
 assert.equal(view.welcomeView('flora').scene,'terrain');
 assert.ok(view.welcomeView('flora').camera.zoom>=10);
 assert.match(view.welcomeView('public-safety').detail,/no crime, court or live emergency/);
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
 assert.match(source,/const requestedStyle = BASEMAPS\[next\.basemap\]\.style;/,'the selected registered style is bound explicitly for resolution and rejected-document eviction');
 assert.match(source,/void resolveStyle\(requestedStyle\)\.then/,'style documents resolve outside MapLibre, so a failed previous style cannot block the request');
 // Supersession, pending-style reuse, A→B→A and retry execute the real engine
 // in welcome-map-engine.test; do not couple them to one guard's spelling.
 assert.match(source,/interactive: false/,'the welcome map is a backdrop, not a second map to operate');
 assert.match(source,/attributionControl: \{ compact: true \}/,'provider credits stay on the map');
 const stage=await readFile('app/living-welcome/DomainStage.jsx','utf8');
 assert.match(stage,/import\('\.\/map-engine\.mjs'\)/,'the map engine loads lazily after the welcome paints');
 // Idle desktop and centered mobile previews execute in living-welcome.test
 // and the native carousel browser journeys; avoid a stale source-pattern rule.
});

test('subject camera passes return home, reverse without accumulating drift, and stay local to their zoom',()=>{
 const signatures=new Set();
 for(const topic of Object.keys(maps.CATEGORY_MAPS)){
  const v=view.welcomeView(topic),camera=plain(v.camera),span=360/2**camera.zoom;
  for(const leg of [0,1,2,3,100,101,102,103]){
   const pose=plain(view.welcomeDriftLeg(v,leg));
   assert.ok(pose.center.every(Number.isFinite)&&Number.isFinite(pose.zoom)&&Number.isFinite(pose.bearing));
   assert.ok(Math.abs(pose.center[0]-camera.center[0])<=span*.08,topic+' stays near its source view');
   assert.ok(Math.abs(pose.center[1]-camera.center[1])<=span*.05);
   assert.ok(pose.pitch>=0&&pose.pitch<=68);
   assert.ok(Math.abs(pose.zoom-camera.zoom)<=.36);
   assert.ok(pose.duration>=24000&&pose.duration<=36000);
   if(leg%2)assert.deepEqual({center:pose.center,pitch:pose.pitch,zoom:pose.zoom,bearing:pose.bearing},camera,topic+' returns home');
   assert.deepEqual(pose,plain(view.welcomeDriftLeg(v,leg%4)),topic+' does not accumulate drift');
  }
  const pose=view.welcomeDriftLeg(v,0);
  signatures.add(JSON.stringify([pose.center[0]-camera.center[0],pose.center[1]-camera.center[1],pose.bearing-camera.bearing,pose.zoom-camera.zoom,pose.duration]));
 }
 assert.ok(signatures.size>=18,'topics have distinct camera choreography');
});

// Execute the production attribution placement effect: main and preview maps
// must never exchange their native controls, including on a return to welcome.
test('Explorer attribution never borrows welcome credits and retains fullscreen placement',async()=>{
 const source=await readFile('app/page.tsx','utf8'),ast=ts.createSourceFile('page.tsx',source,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
 let effect;const visit=node=>{if(ts.isCallExpression(node)&&node.expression.getText(ast)==='useEffect'&&node.arguments[0]?.getText(ast).includes('mapInformationHostRef.current'))effect=node.arguments[0].getText(ast);ts.forEachChild(node,visit);};visit(ast);assert.ok(effect);
 const classes=new Set(),listeners=new Map();let disconnected=false;
 const owner={fullscreenElement:null,addEventListener:(name,fn)=>listeners.set(name,fn),removeEventListener:name=>listeners.delete(name)};
 const native={open:true,classList:{toggle(){},remove(){}}},preview={open:true,classList:{toggle(){},remove(){}}};
 const host={child:native,querySelector(){return this.child;},appendChild(node){if(node.parent)node.parent.child=null;this.child=node;node.parent=this;}};native.parent=host;
 const welcomeHost={...host,child:preview};preview.parent=welcomeHost;
 const corner={...host,child:null};
 const container={ownerDocument:owner,classList:{contains:name=>classes.has(name)},querySelector:selector=>selector==='.maplibregl-ctrl-top-right'?corner:corner.child};
 const scope={mapContainerRef:{current:container},mapInformationHostRef:{current:host},welcomeAttributionHostRef:{current:welcomeHost},welcomeShowing:true,styleReady:true,MutationObserver:class{observe(){}disconnect(){disconnected=true;}}};
 const execute=()=>new Function(...Object.keys(scope),ts.transpileModule(`return (${effect})();`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText)(...Object.values(scope));
 const cleanup=execute();
 assert.equal(host.child,native,'returning to welcome leaves the main map control in its own information host');assert.equal(welcomeHost.child,preview,'the preview remains the only owner of the welcome source strip');
 owner.fullscreenElement=container;listeners.get('fullscreenchange')();assert.equal(corner.child,native);assert.equal(welcomeHost.child,preview);
 owner.fullscreenElement=null;listeners.get('fullscreenchange')();assert.equal(host.child,native);assert.equal(welcomeHost.child,preview);
 cleanup();assert.equal(listeners.size,0);assert.equal(disconnected,true);
});

test('composition attribution fixture covers inline style changes without copying controls or modifying the main map',()=>{
 const previous=globalThis.window;globalThis.window={};
 class MapFixture{
  constructor(welcome){this.welcome=welcome;this.styles=[];}
  getContainer(){return {classList:{contains:name=>this.welcome&&name==='domain-stage-map'}};}
  setStyle(style,options){this.styles.push({style,options});return this;}
  addControl(control){control._map=this;return this;}
 }
 const source={type:'geojson',data:{type:'FeatureCollection',features:[]},attribution:'Fixture source'},layer={id:'test-attribution-layer',type:'circle',source:'test-attribution'};
 try{
  installWelcomeAttributionFixture(MapFixture,{version:8,sources:{'test-attribution':source},layers:[layer]});
  const preview=new MapFixture(true),main=new MapFixture(false);
  const inline={version:8,projection:{type:'globe'},terrain:{source:'dem'},sources:{dem:{type:'raster-dem',tiles:['https://provider.invalid/tile']}},layers:[{id:'native-background',type:'background'}]};
  preview.setStyle(inline,{diff:false});main.setStyle(inline);
  assert.equal(preview.styles[0].style.sources['test-attribution'].attribution,'Fixture source');assert.equal(main.styles[0].style,inline,'the main-map style is untouched');assert.equal(inline.sources['test-attribution'],undefined,'registered source styles are never mutated');
  assert.deepEqual(preview.styles[0].style.terrain,inline.terrain);assert.deepEqual(preview.styles[0].style.projection,inline.projection);assert.deepEqual(preview.styles[0].style.sources.dem,inline.sources.dem,'terrain and original source bindings remain available');
  const control={_container:{classList:{contains:name=>name==='maplibregl-ctrl-attrib'}}};preview.addControl(control);
  assert.equal(window.__welcomeCreditFixture.control,control);assert.equal(window.__welcomeCreditFixture.node,control._container);assert.equal(control._map,preview,'identity is measured from the native control');
  preview.setStyle({version:8,sources:{},layers:[]});assert.equal(preview.styles[1].style.sources['test-attribution'].attribution,'Fixture source');assert.equal(window.__welcomeCreditFixture.node,control._container);
  preview.setStyle(null);assert.equal(preview.styles.at(-1).style,null,'disposal does not install another style');
 }finally{if(previous===undefined)delete globalThis.window;else globalThis.window=previous;}
});

test('composition credit readiness tolerates deferred creation and requires source, owner and both links',async()=>{
 const source=await readFile('tests/explorer-startup.browser.mjs','utf8'),ast=ts.createSourceFile('browser.mjs',source,ts.ScriptTarget.ES2022,true,ts.ScriptKind.JS);
 let expression;const find=node=>{if(ts.isVariableDeclaration(node)&&node.name.getText(ast)==='creditsReady')expression=node.initializer.text;ts.forEachChild(node,find);};find(ast);assert.ok(expression);
 let sourceReady=true,styleReady=true,count=2;
 const strip={isConnected:true,getBoundingClientRect:()=>({width:80,height:30}),querySelectorAll:()=>Array.from({length:count},()=>({textContent:'Fixture credit'}))};
 const document={querySelector:selector=>selector==='.domain-stage'?{dataset:{state:'ready'}}:strip};
 const map={getContainer:()=>({matches:()=>true}),isStyleLoaded:()=>styleReady,getSource:()=>sourceReady?{}:null},control={_map:map};
 const ready=window=>new Function('window','document',`return Boolean(${expression});`)(window,document);
 assert.equal(ready({}),false,'waiting before map creation must not throw');
 const window={__welcomeCreditFixture:{map,control,node:strip}};assert.equal(ready(window),true);
 styleReady=false;assert.equal(ready(window),false);styleReady=true;sourceReady=false;assert.equal(ready(window),false);sourceReady=true;
 count=0;assert.equal(ready(window),false,'an empty native box is not credit readiness');count=1;assert.equal(ready(window),false);count=2;
 control._map={};assert.equal(ready(window),false,'another map cannot satisfy preview ownership');
});
