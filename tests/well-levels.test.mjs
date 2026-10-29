import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const wl=await compile('app/well-levels.ts');
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const plain=v=>JSON.parse(JSON.stringify(v));
const esm=async(path,replace=s=>s)=>`data:text/javascript;base64,${Buffer.from(ts.transpileModule(replace(await readFile(path,'utf8')),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`;
const upstreamUrl=await esm('app/api/event-atlas/upstream.ts');
const wlUrl=await esm('app/well-levels.ts');
const route=async tag=>import(await esm('app/api/well-levels/route.ts',s=>s.replace('from "../event-atlas/upstream"',`from "${upstreamUrl}"`).replace('from "../../well-levels"',`from "${wlUrl}"`)+`\n// ${tag}`));

const SITE='370012101070901';
// USGS field-measurements-shaped features (values illustrative): one January measurement a year, 1966–2025,
// the water level falling a foot a year; the last provisional.
const feature=(time,value,extra={})=>({type:'Feature',id:`m-${time}`,geometry:null,properties:{monitoring_location_id:`USGS-${SITE}`,parameter_code:'72019',unit_of_measure:'ft',time,value,approval_status:'Approved',...extra}});
const yearly=Array.from({length:60},(_,i)=>feature(`${1966+i}-01-10T17:00:00+00:00`,String(80+i),i===59?{approval_status:'Provisional'}:{}));

test('the USGS query asks for one well\'s depth to water, and only same-collection next pages are followed',()=>{
 const url=new URL(wl.wellLevelsProviderUrl(SITE));
 assert.equal(url.origin+url.pathname,'https://api.waterdata.usgs.gov/ogcapi/v1/collections/field-measurements/items');
 assert.deepEqual(Object.fromEntries(url.searchParams),{f:'json',monitoring_location_id:`USGS-${SITE}`,parameter_code:'72019',limit:'1000',skipGeometry:'true'});
 assert.equal(wl.nextPageUrl({links:[{rel:'self',href:'x'},{rel:'next',href:'https://api.waterdata.usgs.gov/ogcapi/v1/collections/field-measurements/items?offset=1000'}]}),'https://api.waterdata.usgs.gov/ogcapi/v1/collections/field-measurements/items?offset=1000');
 assert.equal(wl.nextPageUrl({links:[{rel:'next',href:'https://example.com/ogcapi/v1/collections/field-measurements/items'}]}),null,'another host');
 assert.equal(wl.nextPageUrl({links:[{rel:'next',href:'https://api.waterdata.usgs.gov/ogcapi/v1/collections/daily/items'}]}),null,'another collection');
 assert.equal(wl.nextPageUrl({links:[]}),null);
 assert.equal(wl.isWellSite(SITE),true);assert.equal(wl.isWellSite('07144100'),false,'a stream gauge number is not a well');assert.equal(wl.isWellSite('37001210107090x'),false);
 assert.equal(wl.wellLevelsApiPath(SITE),`/api/well-levels?site=${SITE}`);
 assert.equal(wl.wellKgsPage(SITE),`https://geohydro.kgs.ku.edu/geohydro/wizard/wizardwelldetail.cfm?usgs_id=${SITE}`);
});

test('measurements are read as feet below land surface, oldest first; a missing value is left out, not read as zero',()=>{
 const levels=wl.parseWellLevels([...yearly].reverse().concat([
  feature('2010-01-12T00:00:00Z',null,{qualifier:'Dry'}),
  feature('2011-01-12T00:00:00Z',33,{parameter_code:'62610'}),
  feature('2012-01-12T00:00:00Z',33,{unit_of_measure:'m'}),
  feature('1966-01-10T17:00:00+00:00','80'),
  {type:'Feature',properties:null},
 ]),SITE,'2026-10-29T22:00:00Z','x');
 assert.equal(levels.measurements.length,60,'no dry, other-parameter, other-unit or repeated reading');
 assert.deepEqual(plain(levels.measurements[0]),{date:'1966-01-10',precision:'day',time:Date.parse('1966-01-10T17:00:00Z'),span:null,depth:80,provisional:false});
 assert.equal(levels.measurements[59].provisional,true);assert.equal(levels.measurements[59].depth,139);
 assert.equal(wl.validWellLevels(levels,SITE),true);assert.equal(wl.validWellLevels(levels,'370012101070902'),false);
 assert.throws(()=>wl.pageFeatures({type:'nope'}),/Not a USGS field-measurements answer/);
});

test('a date USGS knows only to the month or year stays that vague: labelled honestly, placed mid-period, its whole period kept',()=>{
 const levels=wl.parseWellLevels([
  feature('1958-01-01T00:00:00+00:00',41,{month:null,day:null}),
  feature('1962-03-01T00:00:00+00:00',47,{month:3,day:null}),
  ...yearly.slice(0,10),
 ],SITE,'x','x');
 const [y,m]=levels.measurements;
 assert.deepEqual(plain([y.precision,y.span,y.time]),['year',[Date.UTC(1958,0,1),Date.UTC(1959,0,1)],(Date.UTC(1958,0,1)+Date.UTC(1959,0,1))/2]);
 assert.deepEqual(plain([m.precision,m.span]),['month',[Date.UTC(1962,2,1),Date.UTC(1962,3,1)]]);
 assert.deepEqual([y,m,levels.measurements[2]].map(wl.measurementDate),['1958','Mar 1962','Jan 10, 1966']);
 assert.match(wl.wellReading(levels),/ · 2 dated only to the month or year, placed mid-period in the trend$/);
 assert.doesNotMatch(wl.wellReading(levels),/Jan 1, 1958/,'no placeholder day is shown as a date');
 const plot=wl.wellPlot(levels);assert.equal(plot.firstLabel,'1958');assert.equal(plot.lastLabel,'Jan 10, 1975');
 // The latest measurement, if vague, says "in", not "on".
 assert.match(wl.wellReading(wl.parseWellLevels([feature('1958-01-01T00:00:00Z',41,{month:null,day:null})],SITE,'x','x')),/^Depth to water 41\.0 ft in 1958 · /);
});

test('the reading gives the latest depth, the change since the first measurement, and the trend over the record and the last ten years',()=>{
 const levels=wl.parseWellLevels(yearly,SITE,'x','x');
 assert.equal(wl.depthTrend(levels.measurements).toFixed(2),'1.00');
 assert.equal(wl.wellReading(levels),'Depth to water 139.0 ft on Jan 10, 2025 (provisional) · 60 measurements, 1966–2025 · water level down 59.0 ft since 1966 · trend falling 1.00 ft/yr over the record, falling 1.00 ft/yr over 2015–2025');
 // A recovering well, a single measurement, none, and a record cut short.
 const rising=wl.parseWellLevels(yearly.slice(0,10).map((f,i)=>feature(f.properties.time,100-2*i)),SITE,'x','x');
 assert.match(wl.wellReading(rising),/water level up 18\.0 ft since 1966 · trend rising 2\.00 ft\/yr over the record$/);
 assert.equal(wl.wellReading(wl.parseWellLevels(yearly.slice(0,1),SITE,'x','x')),'Depth to water 80.0 ft on Jan 10, 1966 · the only measurement on record');
 assert.match(wl.wellReading(wl.parseWellLevels([],SITE,'x','x')),/^USGS holds no depth-to-water measurements for this well/);
 assert.match(wl.wellReading(wl.parseWellLevels(yearly,SITE,'x','x',true)),/the USGS answer was cut short$/);
 assert.equal(wl.depthTrend(wl.parseWellLevels(yearly.slice(0,2),SITE,'x','x').measurements),null,'two measurements are no trend');
});

test('the hydrograph runs depth downward on round ticks, with year ticks and the trend line',()=>{
 const plot=wl.wellPlot(wl.parseWellLevels(yearly,SITE,'x','x'));
 assert.deepEqual(plain(plot.ticks),[80,100,120,140]);assert.equal(plot.low,80);assert.equal(plot.high,140);
 assert.deepEqual(plot.years.map(y=>y.label),['1970','1980','1990','2000','2010','2020']);
 assert.equal(plot.start,Date.UTC(1966,0,1));assert.equal(plot.end,Date.UTC(2026,0,1));
 assert.ok(Math.abs(plot.trend.from.depth-80)<0.2&&Math.abs(plot.trend.to.depth-139)<0.2,'the fitted line meets a straight record');
 assert.equal(wl.wellPlot(wl.parseWellLevels(yearly.slice(0,1),SITE,'x','x')),null);
});

test('the wells of the snapshot, nearest the map centre first',async()=>{
 const snapshot=JSON.parse(await readFile('public/data/groundwater/kgs-monitoring-wells.geojson','utf8'));
 const wells=wl.wellSites(snapshot);
 assert.ok(wells.length>1000,'the 2026 network');
 assert.deepEqual(plain(wells[0]),{site:SITE,name:'35S 35W 15BCC 01',lon:-101.11925,lat:37.00336});
 const near=wl.wellsNear(wells,{lon:-101.11925,lat:37.00336},5);
 assert.equal(near.length,5);assert.deepEqual(near[0],{id:SITE,label:'35S 35W 15BCC 01 · 0.0 mi'});
 assert.equal(wl.wellSites({features:[{properties:{USGS_ID:'123'},geometry:{coordinates:[0,0]}}]}).length,0,'no usable site number');
});

test('the route follows the pages, keeps a well six hours, and fails closed',async()=>{
 const original=globalThis.fetch;
 try{
  const asked=[];
  globalThis.fetch=async input=>{const url=String(input);asked.push(url);
   return /offset=2/.test(url)?Response.json({type:'FeatureCollection',features:yearly.slice(2),links:[]})
    :Response.json({type:'FeatureCollection',features:yearly.slice(0,2),links:[{rel:'next',href:'https://api.waterdata.usgs.gov/ogcapi/v1/collections/field-measurements/items?offset=2'}]});};
  const {GET}=await route('pages');
  const ok=await GET(new Request(`https://kfm.test/api/well-levels?site=${SITE}`));assert.equal(ok.status,200);
  const body=await ok.json();assert.equal(body.measurements.length,60);assert.equal(body.truncated,false);assert.equal(asked.length,2);
  await GET(new Request(`https://kfm.test/api/well-levels?site=${SITE}`));assert.equal(asked.length,2,'kept');
  assert.equal((await GET(new Request('https://kfm.test/api/well-levels?site=07144100'))).status,400);
  assert.equal((await GET(new Request(`https://kfm.test/api/well-levels?site=${SITE}&x=1`))).status,400);
  globalThis.fetch=async()=>new Response('down',{status:503});
  const failed=await (await route('fail')).GET(new Request(`https://kfm.test/api/well-levels?site=${SITE}`));
  assert.equal(failed.status,502);assert.match((await failed.json()).message,/USGS Water Data did not answer/);
 }finally{globalThis.fetch=original;}
});

test('a ring marks the picked well and goes with it',()=>{
 const layers=[{id:'background'}],sources={};
 const map={getSource:id=>sources[id]&&{setData(d){sources[id].data=d;}},addSource:(id,s)=>{sources[id]=s;},removeSource:id=>{delete sources[id];},
  getLayer:id=>layers.find(l=>l.id===id),removeLayer:id=>{layers.splice(layers.findIndex(l=>l.id===id),1);},addLayer:spec=>{layers.push({id:spec.id,spec});}};
 wl.syncWellPick(map,{site:SITE,name:'x',lon:-101.1,lat:37});
 assert.deepEqual(layers.map(l=>l.id),['background',wl.WELL_PICK_LAYER_ID]);assert.deepEqual(plain(sources[wl.WELL_PICK_SOURCE_ID].data.features[0].geometry.coordinates),[-101.1,37]);
 wl.syncWellPick(map,{site:SITE,name:'x',lon:-100,lat:38});assert.deepEqual(plain(sources[wl.WELL_PICK_SOURCE_ID].data.features[0].geometry.coordinates),[-100,38]);
 wl.syncWellPick(map,null);assert.deepEqual(layers.map(l=>l.id),['background']);assert.deepEqual(Object.keys(sources),[]);
 const key=wl.wellLevelsKey();assert.deepEqual(key.items.map(i=>i.shape),['dot','ring']);assert.match(key.note,/pumps off/);
});

test('the Aquifer dock offers water levels at wells: the nearest wells, the picked well\'s line, hydrograph and links; the page owns the well click',async()=>{
 const levels=wl.parseWellLevels(yearly,SITE,'x','x');
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.groundwater,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  onWells:v=>calls.push(['on',v]),onWellPick:v=>calls.push(['pick',v]),onWellClear:()=>calls.push(['clear'])};
 const off={on:false,list:[],picked:null,name:null,loading:false,failed:false,reading:null,plot:null,usgsUrl:null,kgsUrl:null};
 const tool=tree=>findNode(tree,n=>n.type==='button'&&/water levels/i.test(String(n.props.children)));
 let tree=h.render(h.exports.CategoryMapDock,{...base,wells:off});
 assert.equal(tool(tree).props.children,'Water levels at wells');tool(tree).props.onClick();
 const list=[{id:SITE,label:'35S 35W 15BCC 01 · 0.4 mi'}];
 tree=h.render(h.exports.CategoryMapDock,{...base,wells:{...off,on:true,list}});
 assert.match(JSON.stringify(tree),/Pick a monitoring well on the map, or from the list/);
 const picker=findNode(tree,n=>n.props?.label==='KGS monitoring wells nearest the map centre');assert.equal(picker.props.summary,'Wells nearest the map centre (1)');picker.props.onPick(SITE);
 const picked={...off,on:true,list,picked:SITE,name:'35S 35W 15BCC 01',usgsUrl:wl.wellUsgsPage(SITE),kgsUrl:wl.wellKgsPage(SITE)};
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,wells:{...picked,loading:true}})),/Reading the USGS measurements…/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,wells:{...picked,failed:true}})),/did not answer for this well; no level is inferred/);
 tree=h.render(h.exports.CategoryMapDock,{...base,wells:{...picked,reading:wl.wellReading(levels),plot:wl.wellPlot(levels)}});
 assert.equal(tool(tree).props.children,'Hide well water levels');
 const text=JSON.stringify(tree);
 assert.match(text,/water level down 59\.0 ft since 1966/);assert.match(text,/"href":"https:\/\/waterdata\.usgs\.gov\/monitoring-location\/USGS-370012101070901\/"/);assert.match(text,/KGS WIZARD/);
 const chart=findNode(tree,n=>n.type===h.exports.WellHydrographChart);
 const figure=chart.type(chart.props);
 assert.equal(figure.props['aria-label'],'Depth to water at 35S 35W 15BCC 01, 60 measurements from Jan 10, 1966 to Jan 10, 2025, 80.0 to 139.0 feet below land surface');
 const svg=JSON.stringify(figure);assert.match(svg,/"strokeDasharray":"4 2"/);assert.match(svg,/"fill":"none","stroke":"#5cc8ff"/,'the provisional measurement is hollow');
 assert.doesNotMatch(svg,/data-span/,'exact dates have no period bar');
 const vague=wl.parseWellLevels([feature('1958-01-01T00:00:00Z',41,{month:null,day:null}),...yearly],SITE,'x','x');
 const vagueFigure=h.exports.WellHydrographChart({plot:wl.wellPlot(vague),name:'x'});
 assert.match(JSON.stringify(vagueFigure),/"data-span":"year"/);assert.match(JSON.stringify(vagueFigure),/bar: month or year only/);assert.match(vagueFigure.props['aria-label'],/from 1958 to/);
 findNode(tree,n=>n.type==='button'&&n.props['aria-label']==='Clear the selected well').props.onClick();
 assert.deepEqual(calls,[['on',true],['pick',SITE],['clear']]);
 assert.equal(tool(h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.water,wells:off})),undefined,'only maps that offer it');
 // The page: the wells shown while on (and put back only if it showed them), the well click, the key, and closing with the map.
 assert.match(page,/wellsWereOnRef\.current = Boolean\(officialVisibilityRef\.current\["kgs-monitoring-wells"\]\);\s*if \(!wellsWereOnRef\.current\) setOfficialContextVisible\("kgs-monitoring-wells", true\);/);
 assert.match(page,/\} else if \(!wellsWereOnRef\.current\) setOfficialContextVisible\("kgs-monitoring-wells", false\);/);
 assert.match(page,/if \(wellsOnRef\.current && renderedHits\[0\]\?\.source === OFFICIAL_CONTEXT_BY_ID\["kgs-monitoring-wells"\]\.sourceId\) \{\s*const site = renderedHits\[0\]\.properties\?\.USGS_ID;/);
 assert.match(page,/void fetch\(wellLevelsApiPath\(site\), \{ signal: controller\.signal \}\)/);
 assert.match(page,/\|\| \(wellsOnRef\.current && renderedHits\[0\]\?\.source === OFFICIAL_CONTEXT_BY_ID\["kgs-monitoring-wells"\]\.sourceId\)\) \{\s*map\.getCanvas\(\)\.style\.cursor = "pointer";/,'no hover preview over a well the dock picks');
 assert.match(page,/\.\.\.\(wellsOn \? \[wellLevelsKey\(\)\] : \[\]\)/);
 assert.match(page,/wellsWereOnRef\.current = false;\s*setWellsOn\(false\);\s*setWellPicked\(null\);/,'closes with its map');
});
