import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';
import {validateStyleMin} from '@maplibre/maplibre-gl-style-spec';

// Load the style module and its two local dependencies as CommonJS in one context.
const files={'./external-context-sources':'app/external-context-sources.ts','./kansas-orientation':'app/kansas-orientation.ts','./category-basemaps':'app/category-basemaps.ts','./category-basemap-keys':'app/category-basemap-keys.ts'};
const compiled=Object.fromEntries(await Promise.all(Object.entries(files).map(async([id,path])=>[id,ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText])));
const cache=new Map();
function load(id){
 if(cache.has(id))return cache.get(id);
 const mod={exports:{}};cache.set(id,mod.exports);
 vm.runInNewContext(compiled[id],{module:mod,exports:mod.exports,require:dep=>{if(!(dep in compiled))throw new Error(`unexpected import ${dep}`);return load(dep);},URL,Object});
 cache.set(id,mod.exports);return mod.exports;
}
const basemaps=load('./category-basemaps');
const sources=load('./external-context-sources');
const keys=load('./category-basemap-keys');
const styles=Object.fromEntries(Object.entries(basemaps.CATEGORY_BASEMAPS).map(([key,entry])=>[key,entry.style()]));
styles.aviation=styles['aviation-chart'];

test('category basemaps are valid MapLibre styles',()=>{
 for(const [name,style] of Object.entries(styles)){
  const errors=validateStyleMin(JSON.parse(JSON.stringify(style)));
  assert.deepEqual(errors.map(e=>e.message),[],`${name} style validates`);
 }
});

test('category basemaps only request registered carriers: OpenFreeMap tiles and fonts, the Terrarium DEM and a bundled outline',()=>{
 const ofm=new URL(sources.externalContextSource('openfreemap-liberty').requestUrl).origin;
 const dem=sources.externalContextSource('aws-mapzen-terrarium').requestUrl;
 for(const style of Object.values(styles)){
  assert.ok(style.glyphs.startsWith(`${ofm}/fonts/`));
  assert.equal(style.sprite,undefined,'no sprite: airport symbols are drawn, not fetched');
  assert.equal(style.sources.openmaptiles.url,`${ofm}/planet`);
  assert.deepEqual(JSON.parse(JSON.stringify(style.sources['basemap-relief-dem'].tiles)),[dem]);
  assert.equal(style.sources['orientation-kansas'].type,'geojson');
  assert.deepEqual(Object.keys(style.sources).sort(),['basemap-relief-dem','openmaptiles','orientation-kansas']);
 }
 for(const id of ['openfreemap-liberty','aws-mapzen-terrarium'])
  for(const key of keys.CATEGORY_BASEMAP_KEYS) assert.ok(sources.externalContextSource(id).activatesWhen.includes(key),`${id} discloses ${key}`);
 assert.deepEqual(Object.keys(basemaps.CATEGORY_BASEMAPS).sort(),[...keys.CATEGORY_BASEMAP_KEYS].sort(),'one registry entry per key');
 for(const [key,entry] of Object.entries(basemaps.CATEGORY_BASEMAPS))assert.ok(entry.title&&entry.note.includes('display context')&&/display (context|geography|DEM)/.test(entry.legend),`${key} discloses its role`);
});

test('basemap layer ids stay below overlays and share the relief id the 2D relief effect defers to',async()=>{
 for(const style of Object.values(styles)){
  for(const layer of style.layers) assert.ok(layer.id==='kfm-background'||!/^(kfm-|external-)/.test(layer.id),layer.id);
  assert.equal(style.layers[0].id,'kfm-background');
  assert.ok(style.layers.some(layer=>layer.id===basemaps.BASEMAP_HILLSHADE_LAYER_ID&&layer.type==='hillshade'));
 }
 const overlays=await readFile('app/scene-overlays.ts','utf8');
 assert.match(overlays,new RegExp(`CATEGORY_BASEMAP_HILLSHADE_LAYER_ID = "${basemaps.BASEMAP_HILLSHADE_LAYER_ID}"`));
 assert.match(overlays,/&& !map\.getLayer\(CATEGORY_BASEMAP_HILLSHADE_LAYER_ID\)/);
});

test('the aviation chart reads like a sectional: banded 1,000 ft tints, runways and identified, classed airports',()=>{
 const layers=Object.fromEntries(styles.aviation.layers.map(layer=>[layer.id,layer]));
 const tint=layers['chart-elevation-tint'];
 assert.equal(tint.type,'color-relief');
 const ramp=JSON.parse(JSON.stringify(tint.paint['color-relief-color']));
 assert.equal(ramp[0],'interpolate','MapLibre builds color-relief ramps from interpolate stops');
 const stops=ramp.slice(3);
 for(let i=2;i+1<stops.length;i+=4)assert.equal(stops[i+1],stops[i-1],'each band holds one colour to its edge');
 for(let i=4;i<stops.length;i+=4)assert.equal(stops[i]-stops[i-2],1,'band edges are one metre wide: hard chart bands');
 const bands=basemaps.AVIATION_TINT_BANDS.map(([metres])=>Math.round(metres*3.28084/100)*100);
 assert.deepEqual(JSON.parse(JSON.stringify(bands)),[0,1000,2000,3000,4000,5000]);
 assert.equal(layers['chart-runway']['source-layer'],'aeroway');
 assert.equal(layers['chart-airport-ring'].type,'circle');
 assert.match(JSON.stringify(layers['chart-airport-labels'].layout['text-field']),/"icao".*"iata"/);
 assert.match(JSON.stringify(layers['chart-airport-ring'].paint['circle-stroke-color']),/military.*private/);
 assert.equal(layers['chart-urban'].paint['fill-color'],'#f5d96a','built-up areas are chart yellow');
});

test('the civic map makes state, county and municipal boundaries the subject and stars state capitals',()=>{
 const layers=Object.fromEntries(styles.civic.layers.map(layer=>[layer.id,layer]));
 for(const [id,level] of [['civic-state-boundary',4],['civic-county-boundary',6],['civic-municipal-boundary',8]])
  assert.match(JSON.stringify(layers[id].filter),new RegExp(`"admin_level"\\],${level}`),id);
 const order=styles.civic.layers.map(layer=>layer.id);
 assert.ok(order.indexOf('civic-county-boundary')>order.indexOf('civic-roads-major'),'boundaries draw above roads');
 assert.match(JSON.stringify(layers['civic-place-labels'].layout['text-field']),/★/);
});

test('the four science basemaps each make their subject the lead layer',()=>{
 const ids=key=>styles[key].layers.map(layer=>layer.id),layer=(key,id)=>styles[key].layers.find(l=>l.id===id);
 assert.match(JSON.stringify(layer('hydro','hydro-waterway').paint['line-width']),/"match",\["get","class"\],"river",1/,'rivers are scaled by class');
 assert.ok(ids('hydro').indexOf('hydro-waterway-glow')<ids('hydro').indexOf('hydro-waterway'),'the glow sits under the course');
 assert.equal(layer('hydro','hydro-waterway-labels').layout['symbol-placement'],'line','river names follow their courses');
 const ramp=JSON.parse(JSON.stringify(layer('relief','relief-tint').paint['color-relief-color']));
 assert.equal(ramp[0],'interpolate');const elevations=ramp.slice(3).filter((_,i)=>i%2===0);
 assert.deepEqual(elevations,[...elevations].sort((a,b)=>a-b),'relief stops ascend');
 assert.ok(layer('relief',basemaps.BASEMAP_HILLSHADE_LAYER_ID).paint['hillshade-exaggeration']>=0.8,'relief hillshade is the strongest');
 assert.equal(layer('storm','kfm-background').paint['background-color'],'#12171d');
 const chroma=hex=>{const channels=[1,3,5].map(i=>parseInt(hex.slice(i,i+2),16)/255);return Math.max(...channels)-Math.min(...channels);};
 for(const color of JSON.stringify(styles.storm.layers).match(/#[0-9a-f]{6}/gi))assert.ok(chroma(color)<0.2,`storm ground ${color} stays neutral so radar and alert colours read true`);
 assert.ok(ids('storm').includes('storm-place-labels')&&ids('storm').includes('storm-state-boundary'),'where weather is hitting: towns and the state line');
 assert.match(JSON.stringify(layer('network','network-roads').paint['line-color']),/motorway.*trunk.*primary/);
 assert.equal(layer('network','network-route-numbers')['source-layer'],'transportation_name');
 assert.match(JSON.stringify(layer('network','network-road-casing').paint['line-color']),/"brunnel"\],"bridge"/,'bridges are cased');
 assert.ok(ids('network').indexOf('network-rail-ties')>ids('network').indexOf('network-rail'),'ties draw over the rail line');
});

test('the historic atlas makes railroads the subject on a parchment ground and lets modern roads recede',()=>{
 const ids=styles.historic.layers.map(layer=>layer.id),layer=id=>styles.historic.layers.find(l=>l.id===id);
 assert.equal(layer('kfm-background').paint['background-color'],'#efe4c8');
 assert.equal(layer('historic-graticule').source,'orientation-kansas','the atlas graticule comes from the bundled orientation source');
 assert.ok(ids.indexOf('historic-rail-ties')>ids.indexOf('historic-rail')&&ids.indexOf('historic-rail')>ids.indexOf('historic-roads'),'ties cross the rail, both over the receding roads');
 assert.match(JSON.stringify(layer('historic-place-labels').layout['text-field']),/"upcase"/,'city names are capitals');
 assert.equal(layer('historic-roads').minzoom,6);
 assert.match(basemaps.CATEGORY_BASEMAPS.historic.legend,/present-day/,'the base is today\'s geography in an atlas style, not a historical map');
});

test('county lines and river lines appear only on the maps whose subject they are',()=>{
 const sourceLayers=key=>new Set(styles[key].layers.filter(l=>l['source-layer']==='waterway').map(l=>l.id));
 const counties=key=>styles[key].layers.filter(l=>l['source-layer']==='boundary'&&JSON.stringify(l.filter).includes('"admin_level"],6')).map(l=>l.id);
 for(const key of Object.keys(styles)){
  assert.equal(counties(key).join(),key==='civic'?'civic-county-boundary':'',`${key}: county lines only where jurisdictions are the subject`);
  assert.equal(sourceLayers(key).size>0,key==='hydro'||key==='aviation'||key==='aviation-chart',`${key}: river lines only on the river network and the aviation chart`);
 }
});

test('every surface that whitelists basemaps accepts the category basemaps',async()=>{
 const [runtime,page,saved,wind,report]=await Promise.all(['app/map-runtime.ts','app/page.tsx','app/saved-workspaces.ts','app/wind-arrow-canvas.ts','app/report-story-workspaces.tsx'].map(path=>readFile(path,'utf8')));
 assert.match(runtime,/export type BasemapKey = "standard" \| CategoryBasemapKey \|/);
 assert.match(runtime,/\.\.\.Object\.fromEntries\(CATEGORY_BASEMAP_KEYS\.map\(key => \[key, \{ title: CATEGORY_BASEMAPS\[key\]\.title/);
 assert.match(runtime,/VECTOR_BASEMAPS: ReadonlySet<BasemapKey> = new Set<BasemapKey>\(\["standard", \.\.\.CATEGORY_BASEMAP_KEYS\]\)/);
 assert.match(page,/isCategoryBasemapKey\(basemap\) \? CATEGORY_BASEMAPS\[basemap\]\.legend/);
 assert.deepEqual([...keys.LIGHT_CATEGORY_BASEMAPS].sort(),['aviation-chart','civic','historic','network','relief'],'dark grounds (hydro, storm) get light wind strokes');
 assert.equal((page.match(/isBasemapKey\((restoredBasemap|snapshot\.basemap)\)/g)||[]).length,2,'URL and snapshot restore accept every BASEMAPS key');
 assert.match(page,/VECTOR_BASEMAPS\.has\(basemapRef\.current\) && !styleFallbackAttempted && shouldFallbackStandardBasemap/);
 assert.match(page,/mode === "globe" && !VECTOR_BASEMAPS\.has\(basemapRef\.current\)/);
 assert.match(saved,/"standard", \.\.\.CATEGORY_BASEMAP_KEYS, "imagery"/);
 assert.match(wind,/"standard", \.\.\.LIGHT_CATEGORY_BASEMAPS, "prairie"/);
 assert.match(report,/draft\.snapshot\.basemap === "standard" \|\| isCategoryBasemapKey\(draft\.snapshot\.basemap\)/);
});

test('a category basemap tile failure after the one local fallback degrades the map instead of stopping it',async()=>{
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/basemapStyle\.sources\[sourceId\]\?\.type === "raster" \|\| VECTOR_BASEMAPS\.has\(basemapRef\.current\) && Object\.hasOwn\(basemapStyle\.sources, sourceId\)/);
 const fallback=page.indexOf('VECTOR_BASEMAPS.has(basemapRef.current) && !styleFallbackAttempted'),degrade=page.indexOf('VECTOR_BASEMAPS.has(basemapRef.current) && Object.hasOwn(basemapStyle.sources, sourceId)');
 assert.ok(fallback>0&&degrade>fallback,'the local-style fallback is tried first');
});
