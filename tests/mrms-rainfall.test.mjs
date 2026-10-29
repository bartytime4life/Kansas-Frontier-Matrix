import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const rain=await compile('app/mrms-rainfall.ts');
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const plain=v=>JSON.parse(JSON.stringify(v));
const esm=async(path,replace=s=>s)=>`data:text/javascript;base64,${Buffer.from(ts.transpileModule(replace(await readFile(path,'utf8')),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`;
const upstreamUrl=await esm('app/api/event-atlas/upstream.ts');
const rainUrl=await esm('app/mrms-rainfall.ts');
const route=async tag=>import(await esm('app/api/mrms-rainfall/legend/route.ts',s=>s.replace('from "../../event-atlas/upstream"',`from "${upstreamUrl}"`).replace('from "../../../mrms-rainfall"',`from "${rainUrl}"`)+`\n// ${tag}`));

const PNG='iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==';
// An ArcGIS ImageServer legend answer in the service's shape (synthetic classes).
const legendAnswer={layers:[{layerId:0,layerName:'mrms_qpe',legend:[{label:'0.01 - 0.10',imageData:PNG,contentType:'image/png',height:20,width:20},{label:'0.10 - 0.25',imageData:PNG,contentType:'image/png'},
 {label:'bad data',imageData:'not base64!',contentType:'image/png'},{label:'wrong type',imageData:PNG,contentType:'text/html'},{label:'',imageData:PNG,contentType:'image/png'}]}]};

test('the NWS MRMS service draws each window with its own raster function, a 512-pixel tile at a time',()=>{
 assert.deepEqual(plain(rain.RAINFALL_WINDOWS),[1,3,6,12,24,48,72]);
 assert.ok(rain.isRainfallHours(24));assert.ok(!rain.isRainfallHours(2));assert.ok(!rain.isRainfallHours('24'));
 assert.equal(rain.rainfallRenderingRule(72),'{"rasterFunction":"rft_72hr"}');
 const url=rain.rainfallTileUrl(24,'1234');
 assert.ok(url.startsWith('https://mapservices.weather.noaa.gov/raster/rest/services/obs/mrms_qpe/ImageServer/exportImage?bbox={bbox-epsg-3857}&'),'the bbox template is left for MapLibre');
 const q=new URL(url.replace('{bbox-epsg-3857}','0,0,1,1')).searchParams;
 assert.deepEqual([q.get('bboxSR'),q.get('imageSR'),q.get('size'),q.get('format'),q.get('transparent'),q.get('f'),q.get('_')],['3857','3857','512,512','png32','true','image','1234']);
 assert.deepEqual(JSON.parse(q.get('renderingRule')),{rasterFunction:'rft_24hr'});
 assert.equal(rain.rainfallStamp(0),'0');assert.equal(rain.rainfallStamp(rain.RAINFALL_REFRESH_MS*3+5),'3','a new stamp each quarter hour');
 assert.equal(rain.RAINFALL_REFRESH_MS,900000);
 assert.equal(rain.rainfallLegendApiPath({kind:'observed',hours:6}),'/api/mrms-rainfall/legend?kind=observed&hours=6');assert.equal(rain.rainfallLegendApiPath({kind:'forecast',hours:72}),'/api/mrms-rainfall/legend?kind=forecast&hours=72');
 assert.match(rain.rainfallLegendProviderUrl(6),/\/ImageServer\/legend\?renderingRule=%7B%22rasterFunction%22%3A%22rft_6hr%22%7D&f=json$/);
 assert.match(rain.rainfallReading({kind:'observed',hours:1}),/^Rain in the past 1 hour, in inches, from the NWS MRMS radar estimate on a 1 km grid · .* radar-only, not corrected to rain gauges$/);
});

test('the WPC forecast draws each window from its own layer of the service, with its own symbols',()=>{
 assert.deepEqual(plain(rain.QPF_WINDOWS),[6,24,48,72,120,168]);
 assert.deepEqual(plain(rain.QPF_LAYERS),{6:7,24:1,48:8,72:9,120:10,168:11});
 assert.ok(rain.isQpfHours(168));assert.ok(!rain.isQpfHours(12));
 const url=rain.qpfTileUrl(72,'9');
 assert.ok(url.startsWith('https://mapservices.weather.noaa.gov/vector/rest/services/precip/wpc_qpf/MapServer/export?bbox={bbox-epsg-3857}&'));
 const q=new URL(url.replace('{bbox-epsg-3857}','0,0,1,1')).searchParams;
 assert.deepEqual([q.get('layers'),q.get('size'),q.get('format'),q.get('transparent'),q.get('f'),q.get('_')],['show:9','512,512','png32','true','image','9']);
 assert.equal(rain.rainfallViewTileUrl({kind:'forecast',hours:6},'1'),rain.qpfTileUrl(6,'1'));assert.equal(rain.rainfallViewTileUrl({kind:'observed',hours:6},'1'),rain.rainfallTileUrl(6,'1'));
 assert.equal(rain.QPF_LEGEND_PROVIDER_URL,'https://mapservices.weather.noaa.gov/vector/rest/services/precip/wpc_qpf/MapServer/legend?f=json');
 assert.deepEqual([6,24,48,168].map(rain.qpfWindowLabel),['the next 6 hours','Day 1 (24 hours)','2 days from Day 1','7 days from Day 1']);
 assert.deepEqual([6,24,120].map(rain.qpfWindowButton),['6 h','Day 1','5 d']);
 assert.equal(rain.rainfallReading({kind:'forecast',hours:120}),'Forecast precipitation for 5 days from Day 1, in inches of liquid, from the NWS Weather Prediction Center · issued twice a day · a forecast, not a measurement');
 // The WPC legend lists every layer; the window's own is taken.
 const wpc={layers:[{layerId:1,legend:[{label:'0.01 - 0.10',imageData:PNG,contentType:'image/png'}]},{layerId:9,legend:[{label:'0.10 - 0.25',imageData:PNG,contentType:'image/png'},{label:'0.25 - 0.50',imageData:PNG,contentType:'image/png'}]}]};
 assert.deepEqual(plain(rain.parseRainfallLegend(wpc,{kind:'forecast',hours:72},'x').items.map(i=>i.label)),['0.10 - 0.25','0.25 - 0.50']);
 assert.deepEqual(plain(rain.parseRainfallLegend(wpc,{kind:'forecast',hours:24},'x').items.map(i=>i.label)),['0.01 - 0.10']);
 assert.throws(()=>rain.parseRainfallLegend(wpc,{kind:'forecast',hours:168},'x'),/no classes/,'a window the legend does not list has no key');
});

test('the legend keeps the service\'s own swatches and labels; malformed classes are dropped',()=>{
 const legend=rain.parseRainfallLegend(legendAnswer,{kind:'observed',hours:24},'2026-10-29T19:00:00Z');
 assert.deepEqual(plain(legend.items.map(i=>i.label)),['0.01 - 0.10','0.10 - 0.25']);
 assert.equal(legend.items[0].image,`data:image/png;base64,${PNG}`);
 assert.ok(rain.validRainfallLegend(plain(legend),{kind:'observed',hours:24}));assert.ok(!rain.validRainfallLegend(plain(legend),{kind:'observed',hours:6}),'another window\'s legend is refused');assert.ok(!rain.validRainfallLegend(plain(legend),{kind:'forecast',hours:24}),'or the forecast\'s');
 assert.ok(!rain.validRainfallLegend({kind:'observed',hours:24,items:[{label:'x',image:'javascript:alert(1)'}]},{kind:'observed',hours:24}));
 assert.throws(()=>rain.parseRainfallLegend({layers:[]},{kind:'observed',hours:24},'x'),/no classes/);
});

test('the legend route checks the window, reads the service once a day, and fails closed',async()=>{
 const original=globalThis.fetch;const asked=[];
 const {GET}=await route('a');
 try{
  globalThis.fetch=async input=>{asked.push(String(input));return Response.json(legendAnswer);};
  for(const q of ['hours=2','kind=forecast&hours=12','kind=other&hours=24'])assert.equal((await GET(new Request(`http://x/api/mrms-rainfall/legend?${q}`))).status,400,q);
  assert.equal(asked.length,0);
  const ok=await GET(new Request('http://x/api/mrms-rainfall/legend?hours=24'));
  assert.equal(ok.status,200);assert.equal((await ok.json()).items.length,2);
  assert.equal(asked[0],rain.rainfallLegendProviderUrl(24));
  await GET(new Request('http://x/api/mrms-rainfall/legend?hours=24'));assert.equal(asked.length,1,'kept');
  globalThis.fetch=async input=>{asked.push(String(input));return Response.json({layers:[{layerId:9,legend:[{label:'1.00 - 1.50',imageData:PNG,contentType:'image/png'}]}]});};
  const forecast=await GET(new Request('http://x/api/mrms-rainfall/legend?kind=forecast&hours=72'));
  assert.equal(forecast.status,200);assert.deepEqual((await forecast.json()).items.map(i=>i.label),['1.00 - 1.50']);
  assert.equal(asked.at(-1),rain.QPF_LEGEND_PROVIDER_URL);
 }finally{globalThis.fetch=original;}
 const fresh=await route('b');
 try{
  globalThis.fetch=async()=>new Response('down',{status:503});
  const failed=await fresh.GET(new Request('http://x/api/mrms-rainfall/legend?hours=24'));
  assert.equal(failed.status,502);assert.match((await failed.json()).message,/rainfall legend is unavailable/);
 }finally{globalThis.fetch=original;}
 assert.match(await readFile('app/api/event-atlas/upstream.ts','utf8'),/"https:\/\/mapservices\.weather\.noaa\.gov"/);
});

test('the raster sits under the site\'s overlays, is replaced when the window or stamp changes, and is removed',()=>{
 const layers=[{id:'background',type:'background'},{id:'external-usgs-3dep-hillshade',type:'raster'},{id:'external-usgs-streamflow-points',type:'circle'},{id:'kfm-roads',type:'line'}],sources={};
 const map={getSource:id=>sources[id],addSource:(id,s)=>{sources[id]=s;},removeSource:id=>{delete sources[id];},
  getLayer:id=>layers.find(l=>l.id===id),removeLayer:id=>{layers.splice(layers.findIndex(l=>l.id===id),1);},
  addLayer:(spec,before)=>{const i=before?layers.findIndex(l=>l.id===before):-1;layers.splice(i<0?layers.length:i,0,{id:spec.id,type:spec.type,spec});},
  getStyle:()=>({layers})};
 rain.syncRainfall(map,{kind:'observed',hours:24},'1');
 assert.deepEqual(layers.map(l=>l.id),['background','external-usgs-3dep-hillshade',rain.RAINFALL_LAYER_ID,'external-usgs-streamflow-points','kfm-roads'],'over the hillshade, under the gauges');
 rain.syncRainfall(map,{kind:'observed',hours:24},'2');
 assert.equal(layers.findIndex(l=>l.id===rain.RAINFALL_LAYER_ID),2,'a quarter-hour refresh keeps it under the gauges');
 assert.equal(sources[rain.RAINFALL_SOURCE_ID].type,'raster');assert.equal(sources[rain.RAINFALL_SOURCE_ID].tileSize,512);
 assert.deepEqual(plain(sources[rain.RAINFALL_SOURCE_ID].tiles),[rain.rainfallTileUrl(24,'2')],'the refresh asks for the new stamp');
 assert.equal(layers.find(l=>l.id===rain.RAINFALL_LAYER_ID).spec.paint['raster-resampling'],'nearest','the 1 km cells stay sharp');
 rain.syncRainfall(map,{kind:'observed',hours:24},'2');assert.equal(layers.filter(l=>l.id===rain.RAINFALL_LAYER_ID).length,1,'idempotent');
 rain.syncRainfall(map,{kind:'observed',hours:72},'2');assert.deepEqual(plain(sources[rain.RAINFALL_SOURCE_ID].tiles),[rain.rainfallTileUrl(72,'2')]);
 rain.syncRainfall(map,{kind:'forecast',hours:72},'2');assert.deepEqual(plain(sources[rain.RAINFALL_SOURCE_ID].tiles),[rain.qpfTileUrl(72,'2')],'the forecast replaces the observed rain');
 assert.equal(layers.find(l=>l.id===rain.RAINFALL_LAYER_ID).spec.paint['raster-resampling'],'linear','the forecast areas are smooth');assert.match(sources[rain.RAINFALL_SOURCE_ID].attribution,/WPC QPF/);
 rain.syncRainfall(map,null,'2');
 assert.deepEqual(layers.map(l=>l.id),['background','external-usgs-3dep-hillshade','external-usgs-streamflow-points','kfm-roads']);assert.deepEqual(Object.keys(sources),[]);
});

test('the dock offers rainfall on the River network, Field view and Storm desk: observed or forecast, windows, reading and the NWS key',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.water,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  onRainfall:v=>calls.push(['on',v]),onRainfallKind:v=>calls.push(['kind',v]),onRainfallHours:v=>calls.push(['hours',v])};
 const observedWindows=rain.RAINFALL_WINDOWS.map(hours=>({hours,label:`${hours} h`,title:`Rain in the past ${rain.rainfallWindowLabel(hours)}`}));
 const off={on:false,held:false,kind:'observed',hours:24,windows:observedWindows,reading:rain.rainfallReading({kind:'observed',hours:24}),legend:null,legendFailed:false};
 const tool=tree=>findNode(tree,n=>n.type==='button'&&/rainfall/i.test(String(n.props.children)));
 let tree=h.render(h.exports.CategoryMapDock,{...base,rainfall:off});
 assert.equal(tool(tree).props.children,'Show rainfall');tool(tree).props.onClick();
 const legend=rain.parseRainfallLegend(legendAnswer,{kind:'observed',hours:24},'x');
 tree=h.render(h.exports.CategoryMapDock,{...base,rainfall:{...off,on:true,legend:legend.items}});
 assert.equal(tool(tree).props.children,'Hide rainfall');
 const kinds=findNode(tree,n=>n.props?.['aria-label']==='Rainfall observed or forecast');
 assert.deepEqual(plain(kinds.props.children.map(b=>[b.props.children,b.props['aria-pressed']])),[['Observed (MRMS)',true],['Forecast (WPC)',false]]);
 kinds.props.children[1].props.onClick();
 const group=findNode(tree,n=>n.props?.['aria-label']==='Rainfall window');
 assert.deepEqual(plain(group.props.children.map(b=>[b.props.children,b.props['aria-pressed']])),[['1 h',false],['3 h',false],['6 h',false],['12 h',false],['24 h',true],['48 h',false],['72 h',false]]);
 assert.equal(group.props.style.gridTemplateColumns,'repeat(7,minmax(0,1fr))');
 group.props.children[6].props.onClick();
 const key=findNode(tree,n=>n.type==='ul'&&n.props.className==='category-map-dock-rain-key');
 assert.equal(key.props['aria-label'],'Rain in the past 24 hours, inches');
 assert.match(JSON.stringify(key),/"backgroundImage":"url\(\\"data:image\/png;base64,/);assert.match(JSON.stringify(key),/0\.10 - 0\.25/);
 assert.match(JSON.stringify(tree),/radar-only, not corrected to rain gauges/);
 // The forecast view: its own windows, reading and key.
 const forecastWindows=rain.QPF_WINDOWS.map(hours=>({hours,label:rain.qpfWindowButton(hours),title:`Forecast for ${rain.qpfWindowLabel(hours)}`}));
 const forecast=h.render(h.exports.CategoryMapDock,{...base,rainfall:{...off,on:true,kind:'forecast',hours:72,windows:forecastWindows,reading:rain.rainfallReading({kind:'forecast',hours:72}),legend:legend.items}});
 const fgroup=findNode(forecast,n=>n.props?.['aria-label']==='Rainfall window');
 assert.deepEqual(plain(fgroup.props.children.map(b=>[b.props.children,b.props['aria-pressed']])),[['6 h',false],['Day 1',false],['2 d',false],['3 d',true],['5 d',false],['7 d',false]]);
 assert.equal(fgroup.props.style.gridTemplateColumns,'repeat(6,minmax(0,1fr))');
 assert.equal(findNode(forecast,n=>n.type==='ul'&&n.props.className==='category-map-dock-rain-key').props['aria-label'],'Forecast precipitation, inches');
 assert.match(JSON.stringify(forecast),/Weather Prediction Center · issued twice a day · a forecast, not a measurement/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,rainfall:{...off,on:true}})),/Reading the NWS legend…/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,rainfall:{...off,on:true,legendFailed:true}})),/the colours on the map are the NWS's own/);
 const held=JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,rainfall:{...off,on:true,held:true}}));
 assert.match(held,/Rainfall shows only at the present map time/);assert.doesNotMatch(held,/Rainfall window/);
 assert.equal(tool(h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.geology,rainfall:off})),undefined,'only maps that offer it');
 assert.deepEqual(calls,[['on',true],['kind','forecast'],['hours',72]]);
 h.dispose?.();
 for(const id of ['water','agriculture','weather'])assert.ok(maps.CATEGORY_MAPS[id].tools.includes('rainfall'),id);
});

test('the page keeps a window for each view, holds rainfall away from the present, refreshes it, reads the key, and closes it with its map',()=>{
 assert.match(page,/const rainfallView = useMemo<RainfallView>\(\(\) => rainfallKind === "forecast" \? \{ kind: "forecast", hours: qpfHours \} : \{ kind: "observed", hours: rainfallHours \}/);
 assert.match(page,/const rainfallLive = buildYearCurrent && temporalQuery\.frame === OFFICIAL_CONTEXT_PRESENT_FRAME;/);
 assert.match(page,/const rainfallShown = rainfallOn && rainfallLive \? rainfallView : null;/);
 assert.match(page,/const timer = setInterval\(\(\) => setRainfallClock\(Date\.now\(\)\), RAINFALL_REFRESH_MS\);/);
 assert.match(page,/syncRainfall\(map, rainfallShown, rainfallTileStamp\)/);
 assert.match(page,/void fetch\(rainfallLegendApiPath\(view\), \{ signal: controller\.signal \}\)/);
 assert.match(page,/if \(!validRainfallLegend\(value, view\)\) throw new Error\("Invalid rainfall legend\."\);/);
 assert.match(page,/onRainfallHours=\{hours => \{ if \(rainfallKind === "forecast"\) \{ if \(isQpfHours\(hours\)\) setQpfHours\(hours\); \} else if \(isRainfallHours\(hours\)\) setRainfallHours\(hours\); \}\}/);
 assert.match(page,/setFemaCounty\(null\);\s*setRainfallOn\(false\);/,'closes with its map');
});
