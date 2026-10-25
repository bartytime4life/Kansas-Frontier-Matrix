import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';
import {validateStyleMin} from '@maplibre/maplibre-gl-style-spec';

// Load the style module and its two local dependencies as CommonJS in one context.
const files={'./external-context-sources':'app/external-context-sources.ts','./kansas-orientation':'app/kansas-orientation.ts','./category-basemaps':'app/category-basemaps.ts'};
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
const styles={aviation:basemaps.aviationChartStyle(),civic:basemaps.civicStyle()};

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
  for(const key of ['aviation-chart','civic']) assert.ok(sources.externalContextSource(id).activatesWhen.includes(key),`${id} discloses ${key}`);
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

test('every surface that whitelists basemaps accepts the category basemaps',async()=>{
 const [runtime,page,saved,wind,report]=await Promise.all(['app/map-runtime.ts','app/page.tsx','app/saved-workspaces.ts','app/wind-arrow-canvas.ts','app/report-story-workspaces.tsx'].map(path=>readFile(path,'utf8')));
 assert.match(runtime,/export type BasemapKey = "standard" \| "aviation-chart" \| "civic"/);
 assert.match(runtime,/VECTOR_BASEMAPS: ReadonlySet<BasemapKey> = new Set<BasemapKey>\(\["standard", "aviation-chart", "civic"\]\)/);
 assert.equal((page.match(/isBasemapKey\((restoredBasemap|snapshot\.basemap)\)/g)||[]).length,2,'URL and snapshot restore accept every BASEMAPS key');
 assert.match(page,/VECTOR_BASEMAPS\.has\(basemapRef\.current\) && !styleFallbackAttempted && shouldFallbackStandardBasemap/);
 assert.match(page,/mode === "globe" && !VECTOR_BASEMAPS\.has\(basemapRef\.current\)/);
 assert.match(saved,/"standard", "aviation-chart", "civic", "imagery"/);
 assert.match(wind,/"standard", "aviation-chart", "civic", "prairie"/);
 assert.match(report,/basemap === "aviation-chart" \|\| draft\.snapshot\.basemap === "civic"/);
});

test('a category basemap tile failure after the one local fallback degrades the map instead of stopping it',async()=>{
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/basemapStyle\.sources\[sourceId\]\?\.type === "raster" \|\| VECTOR_BASEMAPS\.has\(basemapRef\.current\) && Object\.hasOwn\(basemapStyle\.sources, sourceId\)/);
 const fallback=page.indexOf('VECTOR_BASEMAPS.has(basemapRef.current) && !styleFallbackAttempted'),degrade=page.indexOf('VECTOR_BASEMAPS.has(basemapRef.current) && Object.hasOwn(basemapStyle.sources, sourceId)');
 assert.ok(fallback>0&&degrade>fallback,'the local-style fallback is tried first');
});
