import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const lc=await compile('app/land-cover.ts');
const rain=await compile('app/mrms-rainfall.ts');
const dm=await compile('app/drought-monitor.ts',{'./kansas-orientation':await compile('app/kansas-orientation.ts')});
const perf=await readFile('app/map-performance.ts','utf8');
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const plain=v=>JSON.parse(JSON.stringify(v));
const esm=async(path,replace=s=>s)=>`data:text/javascript;base64,${Buffer.from(ts.transpileModule(replace(await readFile(path,'utf8')),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`;
const upstreamUrl=await esm('app/api/event-atlas/upstream.ts');
const lcUrl=await esm('app/land-cover.ts');
const {GET}=await import(await esm('app/api/land-cover/point/route.ts',s=>s.replace('from "../../event-atlas/upstream"',`from "${upstreamUrl}"`).replace('from "../../../land-cover"',`from "${lcUrl}"`)));

test('NLCD 2021 is drawn by MRLC in its own colours, and its classes keep their official codes, names and colours',()=>{
 assert.deepEqual(plain(lc.NLCD_CLASSES.map(c=>c.code)),[11,21,22,23,24,31,41,42,43,52,71,81,82,90,95]);
 assert.deepEqual(plain(['#466b9f','#ab6c28','#dcd939','#dfdfc2','#68ab5f']),plain([11,82,81,71,41].map(code=>lc.nlcdClass(code).color)));
 assert.equal(lc.nlcdClass(82).name,'Cultivated crops');assert.equal(lc.nlcdClass(12),null,'perennial ice/snow does not occur in Kansas');
 const url=new URL(lc.LAND_COVER_TILE_URL.replace('{bbox-epsg-3857}','0,0,1,1'));
 assert.equal(url.origin+url.pathname,'https://www.mrlc.gov/geoserver/wms');
 assert.deepEqual(['service','version','request','layers','format','transparent','srs','width','height'].map(k=>url.searchParams.get(k)),['WMS','1.1.1','GetMap','mrlc_display:NLCD_2021_Land_Cover_L48','image/png','true','EPSG:3857','512','512']);
 assert.ok(lc.LAND_COVER_TILE_URL.includes('&bbox={bbox-epsg-3857}&'),'the bbox template is left for MapLibre');
 const key=lc.landCoverKey();
 assert.equal(key.title,'NLCD 2021 land cover · 30 m');assert.equal(key.items.length,15);
 assert.deepEqual(plain(key.items[13]),{label:'90 Woody wetlands',color:'#b8d9eb',shape:'area'});
 assert.match(key.note,/not a field survey/);
});

test('a point reads the class of its 30 m cell from GetFeatureInfo, in or near Kansas only',async()=>{
 const url=new URL(lc.landCoverPointProviderUrl(-100.87,37.98));
 assert.deepEqual(['request','query_layers','srs','width','height','x','y','info_format'].map(k=>url.searchParams.get(k)),['GetFeatureInfo','mrlc_display:NLCD_2021_Land_Cover_L48','EPSG:4326','3','3','1','1','application/json']);
 assert.equal(url.searchParams.get('bbox'),'-100.870200,37.979800,-100.869800,37.980200');
 assert.equal(lc.landCoverPointApiPath(-100.871234,37.98),'/api/land-cover/point?lon=-100.87123&lat=37.98000');
 assert.equal(lc.parseLandCoverPoint({features:[{properties:{PALETTE_INDEX:82}}]}),82);
 assert.equal(lc.parseLandCoverPoint({features:[{properties:{GRAY_INDEX:'71'}}]}),71);
 assert.equal(lc.parseLandCoverPoint({features:[{properties:{PALETTE_INDEX:0}}]}),null,'no data is not a class');
 assert.equal(lc.parseLandCoverPoint({features:[]}),null);assert.equal(lc.parseLandCoverPoint('x'),null);
 assert.ok(lc.inLandCoverRegion(-98,38.5));assert.ok(!lc.inLandCoverRegion(-90,38.5));assert.ok(!lc.inLandCoverRegion(Number.NaN,38));
 const original=globalThis.fetch;const asked=[];
 try{
  globalThis.fetch=async input=>{asked.push(String(input));return Response.json({type:'FeatureCollection',features:[{properties:{PALETTE_INDEX:82}}]});};
  for(const q of ['lon=-90&lat=38','lat=38','lon=abc&lat=38'])assert.equal((await GET(new Request(`http://x/api/land-cover/point?${q}`))).status,400,q);
  assert.equal(asked.length,0,'nothing outside the region is asked');
  const ok=await GET(new Request('http://x/api/land-cover/point?lon=-100.87&lat=37.98'));
  assert.equal(ok.status,200);assert.deepEqual(await ok.json(),{lon:-100.87,lat:37.98,code:82});
  assert.match(ok.headers.get('cache-control'),/max-age=86400/);
  assert.equal(asked[0],lc.landCoverPointProviderUrl(-100.87,37.98));
  globalThis.fetch=async()=>new Response('down',{status:503});
  assert.equal((await GET(new Request('http://x/api/land-cover/point?lon=-100.87&lat=37.98'))).status,502);
 }finally{globalThis.fetch=original;}
 assert.match(await readFile('app/api/event-atlas/upstream.ts','utf8'),/"https:\/\/www\.mrlc\.gov"/);
});

test('the reading names the map, then the class at the point clicked',()=>{
 assert.match(lc.landCoverReading(null),/^USGS NLCD 2021: land cover classified from Landsat at 30 m · click the map/);
 assert.equal(lc.landCoverReading({lon:-100.87,lat:37.98,state:'ready',code:82}),'At 37.980°N, 100.870°W: Cultivated crops (82) · planted/cultivated');
 assert.equal(lc.landCoverReading({lon:-100.87,lat:37.98,state:'loading',code:null}),'At 37.980°N, 100.870°W: reading NLCD…');
 assert.match(lc.landCoverReading({lon:-100.87,lat:37.98,state:'failed',code:null}),/MRLC did not answer/);
 assert.match(lc.landCoverReading({lon:-90,lat:38,state:'none',code:null}),/no NLCD class/);
});

test('the raster sits over the base and other rasters, under the overlays, and is removed',()=>{
 const layers=[{id:'background',type:'background'},{id:'external-usgs-3dep-hillshade',type:'raster'},{id:'external-usgs-wbd-watersheds-line',type:'line'},{id:'kfm-roads',type:'line'}],sources={};
 const map={getSource:id=>sources[id],addSource:(id,s)=>{sources[id]=s;},removeSource:id=>{delete sources[id];},
  getLayer:id=>layers.find(l=>l.id===id),removeLayer:id=>{layers.splice(layers.findIndex(l=>l.id===id),1);},
  addLayer:(spec,before)=>{const i=before?layers.findIndex(l=>l.id===before):-1;layers.splice(i<0?layers.length:i,0,{id:spec.id,type:spec.type,spec});},getStyle:()=>({layers})};
 lc.syncLandCover(map,true);lc.syncLandCover(map,true);
 assert.deepEqual(layers.map(l=>l.id),['background','external-usgs-3dep-hillshade',lc.LAND_COVER_LAYER_ID,'external-usgs-wbd-watersheds-line','kfm-roads'],'watershed lines stay on top');
 assert.deepEqual(plain(sources[lc.LAND_COVER_SOURCE_ID].tiles),[lc.LAND_COVER_TILE_URL]);
 assert.equal(layers[2].spec.paint['raster-resampling'],'nearest','30 m cells stay sharp');
 lc.syncLandCover(map,false);
 assert.deepEqual(layers.map(l=>l.id),['background','external-usgs-3dep-hillshade','external-usgs-wbd-watersheds-line','kfm-roads']);assert.deepEqual(Object.keys(sources),[]);
});

test('the Drought Monitor and other kfm- overlays stay above land cover and rainfall, whichever is turned on first',()=>{
 assert.ok(!lc.LAND_COVER_LAYER_ID.startsWith('kfm-')&&!rain.RAINFALL_LAYER_ID.startsWith('kfm-'),'overlays anchor under the first kfm- layer; these rasters must not be it');
 const fakeMap=()=>{const layers=[{id:'background',type:'background'},{id:'external-usgs-wbd-watersheds-line',type:'line'},{id:'kfm-roads',type:'line'}],sources={};
  return {layers,getSource:id=>sources[id]&&{setData(){}},addSource:(id,s)=>{sources[id]=s;},removeSource:id=>{delete sources[id];},setFilter(){},
   getLayer:id=>layers.find(l=>l.id===id),removeLayer:id=>{layers.splice(layers.findIndex(l=>l.id===id),1);},
   addLayer:(spec,before)=>{const i=before?layers.findIndex(l=>l.id===before):-1;layers.splice(i<0?layers.length:i,0,{id:spec.id,type:spec.type,spec});},getStyle:()=>({layers})};};
 const drought={date:'20261020',data:{type:'FeatureCollection',features:[]}};
 const below=(map,a,b)=>map.layers.findIndex(l=>l.id===a)<map.layers.findIndex(l=>l.id===b);
 for(const order of ['land cover first','drought first']){
  const map=fakeMap();
  if(order==='land cover first'){lc.syncLandCover(map,true);rain.syncRainfall(map,{kind:'observed',hours:24},'1');dm.syncDroughtMonitor(map,drought);}
  else{dm.syncDroughtMonitor(map,drought);lc.syncLandCover(map,true);rain.syncRainfall(map,{kind:'observed',hours:24},'1');}
  assert.ok(below(map,lc.LAND_COVER_LAYER_ID,dm.DROUGHT_FILL_LAYER_ID),`${order}: land cover under the drought fill`);
  assert.ok(below(map,rain.RAINFALL_LAYER_ID,dm.DROUGHT_FILL_LAYER_ID),`${order}: rainfall under the drought fill`);
  assert.ok(below(map,dm.DROUGHT_STATE_LAYER_ID,'kfm-roads'));
 }
 assert.match(perf,/"tool-mrms-rainfall",\s*"tool-nlcd-land-cover",/,'a failed rainfall or land-cover tile does not fail the map');
});

test('the dock offers land cover on Landscape imagery and the Field view; the page reads the class on each click and closes it with its map',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.ecology,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},onLandCover:v=>calls.push(v)};
 const tool=tree=>findNode(tree,n=>n.type==='button'&&/land cover/i.test(String(n.props.children)));
 let tree=h.render(h.exports.CategoryMapDock,{...base,landCover:{on:false,reading:lc.landCoverReading(null)}});
 assert.equal(tool(tree).props.children,'Show land cover (NLCD 2021)');tool(tree).props.onClick();
 assert.doesNotMatch(JSON.stringify(tree),/USGS NLCD 2021: land cover/,'no reading while off');
 tree=h.render(h.exports.CategoryMapDock,{...base,landCover:{on:true,reading:lc.landCoverReading({lon:-100.87,lat:37.98,state:'ready',code:82})}});
 assert.equal(tool(tree).props.children,'Hide land cover');assert.match(JSON.stringify(tree),/Cultivated crops \(82\)/);
 assert.equal(tool(h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.water,landCover:{on:false,reading:''}})),undefined,'only maps that offer it');
 assert.deepEqual(calls,[true]);
 h.dispose?.();
 assert.deepEqual(plain(maps.CATEGORY_MAPS.ecology.tools),['landcover']);assert.ok(maps.CATEGORY_MAPS.agriculture.tools.includes('landcover'));
 assert.match(maps.CATEGORY_MAPS.ecology.lede,/NLCD 2021/);
 assert.match(page,/if \(landCoverOnRef\.current\) readLandCoverAtRef\.current\(event\.lngLat\.lng, event\.lngLat\.lat\);/,'every click reads the class; the click still selects');
 assert.match(page,/void fetch\(landCoverPointApiPath\(lon, lat\), \{ signal: controller\.signal \}\)/);
 assert.match(page,/landCoverRequestRef\.current\?\.abort\(\);\s*if \(!inLandCoverRegion\(lon, lat\)\)/,'a new click replaces the last');
 assert.match(page,/syncLandCover\(map, landCoverOn\)/);
 assert.match(page,/setRainfallOn\(false\);\s*setLandCoverOn\(false\);\s*setLandCoverPoint\(null\);/,'closes with its map');
 assert.match(page,/\.\.\.\(landCoverOn \? \[landCoverKey\(\)\] : \[\]\)/);
});
