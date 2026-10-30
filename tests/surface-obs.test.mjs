import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const sfc=await compile('app/surface-obs.ts');
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const plain=v=>JSON.parse(JSON.stringify(v));

// METAR records as the site's route parses them (values illustrative).
const rec=(o={})=>({station:'KICT',name:'Wichita/Eisenhower Natl, KS, US',lon:-97.43,lat:37.65,elevationFt:1332,observedAt:'2026-10-29T21:53:00Z',raw:'KICT 292153Z 18012G22KT 10SM BKN025 22/14 A2992',
 tempC:22,dewpointC:14,windDirDeg:180,windVariable:false,windKt:12,gustKt:22,visibilitySm:10,visibilityAtLeast:true,altimeterInHg:29.92,weather:null,
 clouds:[{cover:'BKN',baseFtAgl:2500}],ceilingFtAgl:2500,ceilingCover:'BKN',flightCategory:'MVFR',providerCategory:'MVFR',densityAltitudeFt:null,...o});

test('humidity, heat index and wind chill follow the NWS formulas and tables',()=>{
 assert.equal(sfc.toF(22),71.6);
 assert.equal(Math.round(sfc.relativeHumidity(30,20)),55);assert.equal(sfc.relativeHumidity(20,20),100);
 assert.equal(Math.round(sfc.heatIndexF(96,65)),121,'NWS heat index table: 96 °F at 65% is 121 °F');
 assert.equal(Math.round(sfc.heatIndexF(84,40)),83,'the simple formula below 80 °F average');
 assert.equal(sfc.heatIndexF(79,90),null);
 assert.equal(Math.round(sfc.windChillF(0,15/1.150779)),-19,'NWS wind chill table: 0 °F with 15 mph is −19 °F');
 assert.equal(sfc.windChillF(51,20),null);assert.equal(sfc.windChillF(20,2),null,'3 mph or less is no wind chill');
});

test('a barb rounds to 5 kt and draws pennants, full and half barbs from the tip, feathers on the clockwise side',()=>{
 assert.deepEqual([2,3,12,13,65,148].map(sfc.barbKnots),[0,5,10,15,65,150]);
 const tipOf=s=>s.lines[0][3];
 const b65=sfc.barbShapes(65);
 assert.equal(b65.triangles.length,1);assert.equal(b65.lines.length,3,'staff, one full barb, one half barb');
 assert.ok(b65.lines.slice(1).every(([x1,,x2])=>x2>x1),'feathers to the right of a staff pointing north');
 const half=b65.lines[2];assert.ok(Math.abs(half[2]-half[0])<Math.abs(b65.lines[1][2]-b65.lines[1][0]),'the half barb is half as long');
 const b5=sfc.barbShapes(5);assert.equal(b5.lines.length,2);assert.ok(b5.lines[1][1]>tipOf(b5),'a lone half barb is set in from the tip');
 const b10=sfc.barbShapes(10);assert.equal(b10.lines[1][1],tipOf(b10),'a full barb starts at the tip');
 assert.equal(sfc.barbShapes(100).triangles.length,2);
 assert.equal(sfc.BARB_ICONS.length,30);assert.equal(sfc.BARB_ICONS[29],150);
 // Every barb, feathers and stroke included, stays inside the icon canvas: a clipped feather would misstate the speed.
 const pad=sfc.ICON_STROKE/2;
 for(const knots of sfc.BARB_ICONS){
  const {lines,triangles}=sfc.barbShapes(knots);
  const points=[...lines.flatMap(([a,b,c,d])=>[[a,b],[c,d]]),...triangles.flatMap(([a,b,c,d,e,f])=>[[a,b],[c,d],[e,f]])];
  for(const [x,y] of points)assert.ok(x>=pad&&y>=pad&&x<=sfc.ICON_SIZE-pad&&y<=sfc.ICON_SIZE-pad,`${knots} kt: (${x.toFixed(2)}, ${y.toFixed(2)}) is outside the ${sfc.ICON_SIZE} px canvas`);
 }
});

test('sky cover is the greatest layer reported, in the station circle\'s terms',()=>{
 const sky=(clouds,ceilingCover=null)=>sfc.skyCover({clouds:clouds.map(cover=>({cover,baseFtAgl:1000})),ceilingCover});
 assert.deepEqual([sky(['CLR']),sky(['FEW']),sky(['FEW','SCT']),sky(['SCT','BKN','FEW']),sky(['BKN','OVC']),sky([],'VV'),sky([])],['clear','few','scattered','broken','overcast','obscured','missing']);
 // The circle fills by quarters; an obscured sky is an X, a missing report an M.
 const calls=icon=>{const log=[];const ctx=new Proxy({},{get:(_,k)=>k in ctx_props?ctx_props[k]:(...a)=>log.push([k,...a.map(v=>typeof v==='number'?Math.round(v*100)/100:v)]),set:(_,k,v)=>{ctx_props[k]=v;return true;}});const ctx_props={};sfc.paintStationIcon(ctx,icon);return log;};
 const fills=icon=>calls(icon).filter(c=>c[0]==='fill').length;
 assert.equal(fills({kind:'sky',cover:'clear'}),0);assert.equal(fills({kind:'sky',cover:'scattered'}),1);
 const half=calls({kind:'sky',cover:'scattered'}).filter(c=>c[0]==='arc')[1];assert.equal(half[5]-half[4],3.14,'half the circle');
 assert.equal(calls({kind:'sky',cover:'obscured'}).filter(c=>c[0]==='lineTo').length,2);
 assert.equal(calls({kind:'barb',knots:55}).filter(c=>c[0]==='fill').length,1,'one pennant');
});

test('each station carries its plot: cover, barb and direction, °F temperature and dew point, weather; calm and variable winds draw no barb',()=>{
 const c=sfc.surfaceCollection([rec(),rec({station:'KGLD',windKt:0,windDirDeg:0,tempC:-3,dewpointC:-8,clouds:[]}),rec({station:'KHYS',windVariable:true,windDirDeg:null,windKt:4,weather:'-TSRA BR'})]);
 assert.deepEqual(plain(c.features.map(f=>f.properties)),[
  {station:'KICT',sky:'kfm-sfc-sky-broken',barb:'kfm-sfc-barb-10',dir:180,calm:false,variable:false,t:'72',td:'57',wx:''},
  {station:'KGLD',sky:'kfm-sfc-sky-missing',barb:'',dir:0,calm:true,variable:false,t:'27',td:'18',wx:''},
  {station:'KHYS',sky:'kfm-sfc-sky-broken',barb:'',dir:0,calm:false,variable:true,t:'72',td:'57',wx:'-TSRA'}]);
 assert.deepEqual(plain(c.features[0].geometry.coordinates),[-97.43,37.65]);
});

test('the statewide line, a station decoded, and the station list',()=>{
 const records=[rec(),rec({station:'KGLD',name:'Goodland Muni, KS, US',observedAt:'2026-10-29T21:35:00Z',tempC:8,dewpointC:-6,windDirDeg:320,windKt:25,gustKt:38,clouds:[{cover:'CLR',baseFtAgl:null}],ceilingFtAgl:null,ceilingCover:null})];
 assert.equal(sfc.surfaceReading(records),'2 stations, observed 4:35 PM CDT–4:53 PM CDT · warmest KICT Wichita/Eisenhower Natl 72°F, coolest KGLD Goodland Muni 46°F · strongest wind KGLD Goodland Muni, NW (320°) 25 kt, gusts 38');
 assert.equal(sfc.surfaceReading([records[0]]),'1 station, observed 4:53 PM CDT · KICT Wichita/Eisenhower Natl 72°F · strongest wind KICT Wichita/Eisenhower Natl, S (180°) 12 kt, gusts 22');
 assert.equal(sfc.surfaceReading([]),'No Kansas-area METARs under 90 minutes old; no conditions are inferred.');
 assert.equal(sfc.stationDetail(records[0]),'KICT Wichita/Eisenhower Natl · 4:53 PM CDT · 72°F (22°C), dew point 57°F, humidity 60% · S (180°) 12 kt, gusts 22 · visibility at least 10 mi · altimeter 29.92 inHg · ceiling BKN 2,500 ft');
 assert.match(sfc.stationDetail(records[1]),/46°F \(8°C\), dew point 21°F, humidity 37%, wind chill 37°F · NW \(320°\) 25 kt, gusts 38 · .* · sky clear$/);
 assert.match(sfc.stationDetail(rec({tempC:36,dewpointC:24})),/97°F \(36°C\), dew point 75°F, humidity 50%, heat index 110°F/);
 assert.match(sfc.stationDetail(rec({windKt:0})),/ · calm · /);
 assert.deepEqual(sfc.surfaceList(records).map(i=>i.id),['KGLD','KICT']);
 assert.equal(sfc.surfaceList(records)[1].label,'KICT Wichita/Eisenhower Natl · 72/57°F · S (180°) 12 kt, gusts 22');
 assert.equal(sfc.validSurfaceEnvelope({retrievedAt:'x',records}),true);assert.equal(sfc.validSurfaceEnvelope({records}),false);
 assert.equal(sfc.surfaceKey().items.length,4);assert.match(sfc.surfaceKey().note,/not interpolated/);
});

test('the plots sit on top with their icons painted once; the picked station is ringed; they close cleanly',()=>{
 const layers=[{id:'background'},{id:'kfm-roads'}],sources={},filters={},images=new Set();let painted=0;
 const map={getSource:id=>sources[id]&&{setData(){}},addSource:(id,s)=>{sources[id]=s;},removeSource:id=>{delete sources[id];},setFilter:(id,f)=>{filters[id]=f;},
  hasImage:id=>images.has(id),addImage:id=>{images.add(id);},
  getLayer:id=>layers.find(l=>l.id===id),removeLayer:id=>{layers.splice(layers.findIndex(l=>l.id===id),1);},addLayer:spec=>{layers.push({id:spec.id,spec});}};
 const painter=paint=>{painted++;paint(new Proxy({},{get:()=>()=>{},set:()=>true}));return {width:64,height:64,data:new Uint8Array(64*64*4)};};
 const c=sfc.surfaceCollection([rec()]);
 sfc.syncSurfaceObs(map,c,'KICT',painter);sfc.syncSurfaceObs(map,c,'KICT',painter);
 assert.equal(images.size,37);assert.equal(painted,37,'each icon painted once');
 assert.deepEqual(layers.map(l=>l.id),['background','kfm-roads',sfc.SURFACE_SKY_LAYER_ID,sfc.SURFACE_BARB_LAYER_ID,sfc.SURFACE_TEXT_LAYER_ID,sfc.SURFACE_SELECTED_LAYER_ID]);
 assert.deepEqual(plain(layers[3].spec.layout['icon-rotate']),['get','dir']);assert.equal(layers[3].spec.layout['icon-rotation-alignment'],'map','barbs turn with the map: wind is from true north');
 assert.deepEqual(plain(filters[sfc.SURFACE_SELECTED_LAYER_ID]),['==',['get','station'],'KICT']);
 sfc.syncSurfaceObs(map,null);assert.deepEqual(layers.map(l=>l.id),['background','kfm-roads']);assert.deepEqual(Object.keys(sources),[]);
});

test('the Storm desk offers surface observations: held away from the present, the station list and a decoded station; the page owns the plot click',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.weather,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  onSurface:v=>calls.push(['on',v]),onSurfacePick:v=>calls.push(['pick',v]),onSurfaceClear:()=>calls.push(['clear'])};
 const off={on:false,state:'loading',reading:null,list:[],picked:null,detail:null,raw:null};
 const tool=tree=>findNode(tree,n=>n.type==='button'&&/surface observations/i.test(String(n.props.children)));
 let tree=h.render(h.exports.CategoryMapDock,{...base,surface:off});
 assert.equal(tool(tree).props.children,'Show surface observations');tool(tree).props.onClick();
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,surface:{...off,on:true,state:'held'}})),/Observations are current only/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,surface:{...off,on:true}})),/Reading the latest METARs…/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,surface:{...off,on:true,state:'failed'}})),/no conditions are inferred/);
 const record=rec();
 tree=h.render(h.exports.CategoryMapDock,{...base,surface:{on:true,state:'ready',reading:sfc.surfaceReading([record]),list:sfc.surfaceList([record]),picked:'KICT',detail:sfc.stationDetail(record),raw:record.raw}});
 assert.equal(tool(tree).props.children,'Hide surface observations');
 const list=findNode(tree,n=>n.props?.label==='Kansas-area weather stations, by identifier');assert.equal(list.props.summary,'Stations (1)');list.props.onPick('KICT');
 const text=JSON.stringify(tree);assert.match(text,/humidity 60%/);assert.match(text,/"type":"code","props":\{"children":"KICT 292153Z/);
 findNode(tree,n=>n.type==='button'&&n.props['aria-label']==='Clear the selected station').props.onClick();
 assert.deepEqual(calls,[['on',true],['pick','KICT'],['clear']]);
 assert.equal(tool(h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.water,surface:off})),undefined,'only maps that offer it');
 // The page: current only, read again on a timer, a failed read clears the plots, the click, the key, and closing with the map.
 assert.match(page,/const surfaceLive = buildYearCurrent && temporalQuery\.frame === OFFICIAL_CONTEXT_PRESENT_FRAME;/);
 assert.match(page,/const timer = setInterval\(read, SURFACE_OBS_REFRESH_MS\);/);
 assert.match(page,/\.catch\(\(\) => \{ if \(!controller\.signal\.aborted\) \{ setSurfaceRecords\(null\); setSurfaceFailed\(true\); \} \}\);/);
 assert.match(page,/if \(renderedHits\[0\]\?\.source === SURFACE_OBS_SOURCE_ID\) \{\s*const station = renderedHits\[0\]\.properties\?\.station;/);
 assert.match(page,/\.\.\.\(surfaceData \? \[surfaceKey\(\)\] : \[\]\)/);
 assert.match(page,/\/\/ Surface observations and the daylight chart close with their map too\.\s*setSurfaceOn\(false\);\s*setSurfacePicked\(null\);/,'closes with its map');
});
