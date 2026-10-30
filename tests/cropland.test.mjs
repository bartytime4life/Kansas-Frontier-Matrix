import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const cdl=await compile('app/cropland.ts');
const dm=await compile('app/drought-monitor.ts',{'./kansas-orientation':await compile('app/kansas-orientation.ts')});
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const plain=v=>JSON.parse(JSON.stringify(v));
const esm=async(path,replace=s=>s)=>`data:text/javascript;base64,${Buffer.from(ts.transpileModule(replace(await readFile(path,'utf8')),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`;
const upstreamUrl=await esm('app/api/event-atlas/upstream.ts');
const cdlUrl=await esm('app/cropland.ts');
const route=async path=>import(await esm(path,s=>s.replace('from "../../event-atlas/upstream"',`from "${upstreamUrl}"`).replace('from "../../../cropland"',`from "${cdlUrl}"`)));
const tile=await route('app/api/cropland/tile/route.ts');
const point=await route('app/api/cropland/point/route.ts');
const near=(a,b,tol,msg)=>assert.ok(Math.abs(a-b)<=tol,`${msg}: ${a} vs ${b}`);

test('years run from 2008 to the newest released, newest first; the main Kansas crops keep CropScape colours',()=>{
 assert.equal(cdl.CDL_YEARS[0],cdl.CDL_LATEST_YEAR);assert.equal(cdl.CDL_YEARS.at(-1),2008);assert.equal(cdl.CDL_YEARS.length,cdl.CDL_LATEST_YEAR-2007);
 assert.ok(cdl.isCdlYear(2008));assert.ok(!cdl.isCdlYear(2007));assert.ok(!cdl.isCdlYear(cdl.CDL_LATEST_YEAR+1));assert.ok(!cdl.isCdlYear('2020'));
 assert.deepEqual(plain(cdl.CDL_MAIN_CLASSES.filter(c=>[1,5,24].includes(c.value)).map(c=>[c.name,c.color])),[['Corn','#ffd300'],['Soybeans','#267000'],['Winter wheat','#a87000']]);
 const key=cdl.cdlKey(2024);
 assert.equal(key.title,'USDA Cropland Data Layer 2024 · 30 m');assert.equal(key.items.length,9);assert.match(key.note,/over a hundred/);
});

test('a Web Mercator tile is asked for by its corners in longitude and latitude, from zoom 8',()=>{
 const b=cdl.tileBounds(8,56,98);
 near(b.west,-101.25,1e-9,'west');near(b.east,-99.84375,1e-9,'east');
 near(b.north,38.8225909761771,1e-9,'north');near(b.south,37.7185903255,1e-6,'south');
 assert.ok(cdl.tileInRegion(b));assert.ok(!cdl.tileInRegion(cdl.tileBounds(8,10,98)),'far west of Kansas');
 const url=new URL(cdl.cdlTileProviderUrl(2024,8,56,98));
 assert.equal(url.origin+url.pathname,'https://nassgeodata.gmu.edu/CropScapeService/wms_cdlall.cgi');
 assert.deepEqual(['REQUEST','LAYERS','SRS','WIDTH','HEIGHT','FORMAT','TRANSPARENT'].map(k=>url.searchParams.get(k)),['GetMap','cdl_2024','EPSG:4326','512','512','image/png','true']);
 assert.equal(url.searchParams.get('BBOX'),'-101.2500000,37.7185903,-99.8437500,38.8225910');
 assert.equal(cdl.cdlTileTemplate(2020),'/api/cropland/tile?year=2020&z={z}&x={x}&y={y}');
 // Over one zoom-8 tile at Kansas's latitude, the linear-latitude image and the Mercator tile differ by under a pixel.
 const toY=lat=>Math.log(Math.tan(Math.PI/4+lat*Math.PI/360));
 const mid=(b.north+b.south)/2, frac=(toY(b.north)-toY(mid))/(toY(b.north)-toY(b.south));
 assert.ok(Math.abs(frac-0.5)*512<1,`mid-tile offset ${(Math.abs(frac-0.5)*512).toFixed(2)} px`);
});

test('points go to CropScape in NAD83 Conus Albers (EPSG:5070), matching PROJ to the centimetre',()=>{
 // Reference values from pyproj (PROJ) for EPSG:4326 → EPSG:5070.
 for(const [lon,lat,x,y] of [[-96,23,0,0],[-100.87,37.98,-423528.4272608746,1671437.3972748942],[-94.6,39.1,119953.17325223352,1787001.8218529415],[-102.05,40,-511621.167906482,1903268.4710547875]]){
  const [px,py]=cdl.toConusAlbers(lon,lat);near(px,x,0.01,`x at ${lon},${lat}`);near(py,y,0.01,`y at ${lon},${lat}`);
 }
 assert.equal(cdl.cdlValueProviderUrl(2024,-100.87,37.98),'https://nassgeodata.gmu.edu/axis2/services/CDLService/GetCDLValue?year=2024&x=-423528.427&y=1671437.397');
 assert.equal(cdl.cdlPointApiPath(2024,-100.871234,37.98),'/api/cropland/point?year=2024&lon=-100.87123&lat=37.98000');
 const xml='<?xml version="1.0"?><ns1:GetCDLValueResponse xmlns:ns1="http://cdlservice"><Result>{x: -423528.427, y: 1671437.397, value: "24", category: "Winter Wheat", color: "#A87000"}</Result></ns1:GetCDLValueResponse>';
 assert.deepEqual(plain(cdl.parseCdlValue(xml)),{value:24,category:'Winter Wheat',color:'#a87000'});
 assert.deepEqual(plain(cdl.parseCdlValue('{value: 1, category: "Corn"}')),{value:1,category:'Corn',color:null});
 assert.equal(cdl.parseCdlValue('{value: "0", category: "Background"}'),null,'0 is no data');
 assert.equal(cdl.parseCdlValue('<html>error</html>'),null);
});

test('the readings name the year, the zoom it draws at, and the crop at the point clicked',()=>{
 assert.equal(cdl.cdlReading(2024,null,10),'USDA Cropland Data Layer 2024: what was planted in each 30 m cell · click a field for its crop');
 assert.match(cdl.cdlReading(2024,null,6),/zoom in to field scale to draw it$/);
 const p={lon:-100.87,lat:37.98,year:2023};
 assert.equal(cdl.cdlReading(2024,{...p,state:'ready',crop:{value:24,category:'Winter Wheat',color:'#a87000'}},10),'At 37.980°N, 100.870°W, 2023: Winter Wheat (24)');
 assert.equal(cdl.cdlReading(2024,{...p,state:'loading',crop:null},10),'At 37.980°N, 100.870°W, 2023: reading CropScape…');
 assert.match(cdl.cdlReading(2024,{...p,state:'failed',crop:null},10),/CropScape did not answer/);
 assert.match(cdl.cdlReading(2024,{...p,state:'none',crop:null},10),/no CDL class here/);
});

test('the tile route proxies CropScape PNGs for Kansas tiles only; the point route reads GetCDLValue',async()=>{
 const original=globalThis.fetch;const asked=[];
 try{
  globalThis.fetch=async input=>{asked.push(String(input));return new Response(new Uint8Array([137,80,78,71]),{headers:{'content-type':'image/png'}});};
  for(const q of ['year=2007&z=8&x=56&y=98','year=2024&z=7&x=28&y=49','year=2024&z=8&x=999&y=98','year=2024&z=8&x=56'])
   assert.equal((await tile.GET(new Request(`http://x/api/cropland/tile?${q}`))).status,400,q);
  const outside=await tile.GET(new Request('http://x/api/cropland/tile?year=2024&z=8&x=10&y=98'));
  assert.equal(outside.status,204);assert.equal(asked.length,0,'nothing outside Kansas is asked');
  const ok=await tile.GET(new Request('http://x/api/cropland/tile?year=2024&z=8&x=56&y=98'));
  assert.equal(ok.status,200);assert.equal(ok.headers.get('content-type'),'image/png');assert.deepEqual([...new Uint8Array(await ok.arrayBuffer())],[137,80,78,71]);
  assert.equal(asked[0],cdl.cdlTileProviderUrl(2024,8,56,98));
  globalThis.fetch=async()=>new Response('<ServiceException/>',{headers:{'content-type':'application/vnd.ogc.se_xml'}});
  assert.equal((await tile.GET(new Request('http://x/api/cropland/tile?year=2024&z=8&x=56&y=98'))).status,502,'an error document is not drawn');
  globalThis.fetch=async input=>{asked.push(String(input));return new Response('<Result>{x: 1, y: 2, value: "4", category: "Sorghum", color: "#FF9E0B"}</Result>');};
  for(const q of ['year=2024&lon=-90&lat=38','year=2000&lon=-100&lat=38','year=2024&lat=38'])assert.equal((await point.GET(new Request(`http://x/api/cropland/point?${q}`))).status,400,q);
  const answer=await point.GET(new Request('http://x/api/cropland/point?year=2023&lon=-100.87&lat=37.98'));
  assert.equal(answer.status,200);assert.deepEqual(await answer.json(),{year:2023,lon:-100.87,lat:37.98,crop:{value:4,category:'Sorghum',color:'#ff9e0b'}});
  assert.equal(asked.at(-1),cdl.cdlValueProviderUrl(2023,-100.87,37.98));
  globalThis.fetch=async()=>new Response('down',{status:503});
  assert.equal((await point.GET(new Request('http://x/api/cropland/point?year=2023&lon=-100.87&lat=37.98'))).status,502);
 }finally{globalThis.fetch=original;}
 assert.match(await readFile('app/api/event-atlas/upstream.ts','utf8'),/"https:\/\/nassgeodata\.gmu\.edu"/);
 assert.match(await readFile('app/map-performance.ts','utf8'),/"tool-usda-cdl",/,'a failed CDL tile does not fail the map');
});

test('the crop raster is drawn from zoom 8 in Kansas, under the Drought Monitor, replaced with the year, and removed',()=>{
 const layers=[{id:'background',type:'background'},{id:'kfm-roads',type:'line'}],sources={};
 const map={getSource:id=>sources[id]&&{setData(){}},addSource:(id,s)=>{sources[id]=s;},removeSource:id=>{delete sources[id];},setFilter(){},
  getLayer:id=>layers.find(l=>l.id===id),removeLayer:id=>{layers.splice(layers.findIndex(l=>l.id===id),1);},
  addLayer:(spec,before)=>{const i=before?layers.findIndex(l=>l.id===before):-1;layers.splice(i<0?layers.length:i,0,{id:spec.id,type:spec.type,spec});},getStyle:()=>({layers})};
 cdl.syncCropland(map,2024);
 const source=sources[cdl.CDL_SOURCE_ID];
 assert.deepEqual(plain(source.tiles),['/api/cropland/tile?year=2024&z={z}&x={x}&y={y}']);
 assert.equal(source.minzoom,8);assert.deepEqual(plain(source.bounds),[-103.5,36.5,-93.5,40.5]);
 assert.equal(layers.find(l=>l.id===cdl.CDL_LAYER_ID).spec.paint['raster-resampling'],'nearest');
 dm.syncDroughtMonitor(map,{date:'20261020',data:{type:'FeatureCollection',features:[]}});
 const at=id=>layers.findIndex(l=>l.id===id);
 assert.ok(at(cdl.CDL_LAYER_ID)<at(dm.DROUGHT_FILL_LAYER_ID),'the drought colours stay over the crops');
 cdl.syncCropland(map,2012);assert.deepEqual(plain(sources[cdl.CDL_SOURCE_ID].tiles),['/api/cropland/tile?year=2012&z={z}&x={x}&y={y}']);
 cdl.syncCropland(map,null);assert.ok(!layers.some(l=>l.id===cdl.CDL_LAYER_ID)&&!sources[cdl.CDL_SOURCE_ID]);
 assert.ok(!cdl.CDL_LAYER_ID.startsWith('kfm-'));
});

test('the dock offers crops on the Field view with a year and the crop clicked; the page reads it on each click and closes it with its map',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.agriculture,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  onCrops:v=>calls.push(['on',v]),onCropsYear:v=>calls.push(['year',v])};
 const crops={on:false,year:2024,years:cdl.CDL_YEARS,reading:cdl.cdlReading(2024,null,10),swatch:null};
 const tool=tree=>findNode(tree,n=>n.type==='button'&&/crops/i.test(String(n.props.children)));
 let tree=h.render(h.exports.CategoryMapDock,{...base,crops});
 assert.equal(tool(tree).props.children,'Show crops (USDA CDL)');tool(tree).props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,crops:{...crops,on:true,reading:'At 37.980°N, 100.870°W, 2024: Winter Wheat (24)',swatch:'#a87000'}});
 assert.equal(tool(tree).props.children,'Hide crops');
 const select=findNode(tree,n=>n.type==='select');assert.equal(select.props.value,2024);select.props.onChange({target:{value:'2012'}});
 assert.match(JSON.stringify(tree),/"background":"#a87000"/);assert.match(JSON.stringify(tree),/Winter Wheat \(24\)/);
 assert.equal(tool(h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.water,crops})),undefined,'only maps that offer it');
 assert.deepEqual(calls,[['on',true],['year',2012]]);
 h.dispose?.();
 assert.ok(maps.CATEGORY_MAPS.agriculture.tools.includes('crops'));
 assert.match(page,/if \(cropsRef\.current !== null\) \{\s*readCropAtRef\.current\(cropsRef\.current, event\.lngLat\.lng, event\.lngLat\.lat\);\s*readCropHistoryRef\.current\(event\.lngLat\.lng, event\.lngLat\.lat\);\s*readSurveySoilRef\.current\(event\.lngLat\.lng, event\.lngLat\.lat\);\s*readDegreeDaysRef\.current\(event\.lngLat\.lng, event\.lngLat\.lat, cropsRef\.current\);\s*readFrostRef\.current\(event\.lngLat\.lng, event\.lngLat\.lat, cropsRef\.current\);\s*\}/);
 assert.match(page,/void fetch\(cdlPointApiPath\(year, lon, lat\), \{ signal: controller\.signal \}\)/);
 assert.match(page,/setCropsYear\(year\);\s*if \(cropPoint\) readCropAt\(year, cropPoint\.lon, cropPoint\.lat\);/,'a new year reads the last point again');
 assert.match(page,/syncCropland\(map, year\)/);
 assert.match(page,/setFloraOpacity\(0.75\);\s*setCropsOn\(false\);\s*setCropPoint\(null\);/,'closes with its map');
 assert.match(page,/\.\.\.\(cropsOn \? \[cdlKey\(cropsYear\)\] : \[\]\)/);
});
