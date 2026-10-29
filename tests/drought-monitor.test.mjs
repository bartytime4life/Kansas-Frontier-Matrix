import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const orientation=await compile('app/kansas-orientation.ts');
const dm=await compile('app/drought-monitor.ts',{'./kansas-orientation':orientation});
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const plain=v=>JSON.parse(JSON.stringify(v));

const box=(w,s,e,n)=>[[[w,s],[e,s],[e,n],[w,n],[w,s]]];
const feature=(DM,coordinates,type='Polygon')=>({type:'Feature',properties:{OBJECTID:1,DM,Shape_Leng:1,Shape_Area:1},geometry:{type,coordinates}});
// A national map in the USDM's shape: D0 over the whole region, D1 over western Kansas, D2 in its southwest corner, D3 in Texas only.
const national={type:'FeatureCollection',features:[
 feature(0,box(-110,30,-85,45)),feature(1,box(-103,36.5,-98.3,40.5)),feature(2,[box(-102.5,36.6,-100.5,38)],'MultiPolygon'),
 feature('3',box(-101,29,-99,33)),feature(7,box(-100,38,-99,39)),{type:'Feature',properties:{DM:1},geometry:null}]};

test('map weeks are Tuesdays from January 2000; the newest is the one released by Thursday 8:30 a.m. Eastern',()=>{
 assert.ok(dm.isUsdmDate('20261020'));
 assert.ok(!dm.isUsdmDate('20261021'),'a Wednesday');assert.ok(!dm.isUsdmDate('19991228'),'before the first map');assert.ok(!dm.isUsdmDate('20261320'));assert.ok(!dm.isUsdmDate('2026-10-20'));
 assert.equal(dm.latestUsdmDate(new Date('2026-10-22T13:00:00Z')),'20261013','Thursday before the release: the week before');
 assert.equal(dm.latestUsdmDate(new Date('2026-10-22T13:30:00Z')),'20261020');
 assert.equal(dm.latestUsdmDate(new Date('2026-10-26T02:00:00Z')),'20261020');
 assert.equal(dm.latestUsdmDate(new Date('2026-10-29T05:00:00Z')),'20261020','Thursday night UTC is still before the release');
 assert.equal(dm.previousUsdmDate('20260106'),'20251230');assert.equal(dm.nextUsdmDate('20251230'),'20260106');
 assert.equal(dm.usdmDateLabel('20261020'),'Oct 20, 2026');
 assert.equal(dm.usdmMapProviderUrl('20261020'),'https://droughtmonitor.unl.edu/data/json/usdm_20261020.json');
 const series=new URL(dm.usdmSeriesProviderUrl(new Date('2026-10-29T05:00:00Z')));
 assert.equal(series.origin+series.pathname,'https://usdmdataservices.unl.edu/api/StateStatistics/GetDroughtSeverityStatisticsByAreaPercent');
 assert.deepEqual(Object.fromEntries(series.searchParams),{aoi:'KS',startdate:'1/1/2000',enddate:'10/29/2026',statisticsType:'1'});
});

test('rings are cut to the region around Kansas; rings outside it are dropped',()=>{
 const whole=plain(dm.clipRing(box(-110,30,-85,45)[0]));
 assert.equal(whole.length,5);assert.deepEqual(whole[0],whole[4]);
 assert.deepEqual(whole.slice(0,4).map(String).sort(),['-103.2,36.2','-103.2,40.8','-93.6,36.2','-93.6,40.8'],'a ring around the region becomes the region');
 assert.equal(dm.clipRing(box(-101,29,-99,33)[0]),null);
 assert.deepEqual(plain(dm.clipRing(box(-99.123456,37,-98,38)[0])),[[-99.1235,37],[-98,37],[-98,38],[-99.1235,38],[-99.1235,37]],'inside: kept, to about 10 m');
 const triangle=dm.clipRing([[-104,38],[-98,42],[-98,38],[-104,38]]);
 assert.ok(triangle.every(([x,y])=>x>=-103.2&&x<=-93.6&&y>=36.2&&y<=40.8));
 assert.deepEqual(triangle[0],triangle.at(-1),'closed');
});

test('the national map becomes the Kansas region\'s categories, with Kansas\'s share in each measured on it',()=>{
 const map=dm.parseUsdmMap(national,'20261020','2026-10-29T05:00:00Z','src');
 assert.deepEqual(map.data.features.map(f=>f.properties.dm),[0,1,2],'unknown categories, Texas-only areas and missing geometry are left out');
 assert.equal(map.data.features[2].geometry.type,'Polygon','a one-part MultiPolygon stays a Polygon');
 for(const f of map.data.features)for(const ring of f.geometry.coordinates)for(const [x,y] of ring)assert.ok(x>=-103.2&&x<=-93.6&&y>=36.2&&y<=40.8);
 assert.equal(map.kansas[0],100);
 assert.ok(map.kansas[1]>45&&map.kansas[1]<56,`western Kansas west of 98.3°W is about half the state (${map.kansas[1]})`);
 assert.ok(map.kansas[2]>6&&map.kansas[2]<8.5,`the southwest corner, 1.55° by 1° of about 22.4 square degrees (${map.kansas[2]})`);
 assert.deepEqual([map.kansas[3],map.kansas[4]],[0,0]);
 // The same areas drawn as separate (not nested) polygons measure the same.
 const holes={type:'FeatureCollection',features:[feature(0,[...box(-110,30,-85,45),box(-103,36.5,-98.3,40.5)[0].slice().reverse()]),feature(1,[...box(-103,36.5,-98.3,40.5),box(-102.5,36.6,-100.5,38)[0].slice().reverse()]),feature(2,box(-102.5,36.6,-100.5,38))]};
 assert.deepEqual(plain(dm.parseUsdmMap(holes,'20261020','t','s').kansas),plain(map.kansas));
 assert.deepEqual(plain(dm.parseUsdmMap({type:'FeatureCollection',features:[]},'20261020','t','s').kansas),[0,0,0,0,0]);
 assert.throws(()=>dm.parseUsdmMap({type:'Topology'},'20261020','t','s'),/feature collection/);
 assert.ok(dm.validDroughtMap(plain(map)));
 assert.ok(!dm.validDroughtMap({...plain(map),date:'20261021'}));
 assert.ok(!dm.validDroughtMap({...plain(map),kansas:[1,2]}));
});

test('Kansas\'s weekly shares are read from JSON or CSV, cumulative or categorical, and sorted',()=>{
 const json=JSON.stringify([
  {MapDate:'20261020',StateAbbreviation:'KS',None:'23.40',D0:'76.60',D1:'50.12',D2:'20.30',D3:'3.20',D4:'0.00',ValidStart:'2026-10-20',ValidEnd:'2026-10-26',StatisticFormatID:1},
  {MapDate:'20261013',StateAbbreviation:'KS',None:22,D0:78,D1:52,D2:21,D3:4,D4:0},
  {MapDate:'20261014',None:0,D0:100,D1:0,D2:0,D3:0,D4:0},{MapDate:'20261006',None:'x',D0:1}]);
 const s=dm.parseUsdmSeries(json,'t','src');
 assert.deepEqual(plain(s.weeks),[{date:'20261013',shares:[78,52,21,4,0]},{date:'20261020',shares:[76.6,50.12,20.3,3.2,0]}],'non-Tuesday and incomplete rows are left out');
 const csv=['"MapDate","StateAbbreviation","None","D0","D1","D2","D3","D4","ValidStart","ValidEnd"','2012-07-31T00:00:00,KS,0.00,0.00,0.00,15.00,48.00,37.00,7/31/2012,8/6/2012',''].join('\r\n');
 assert.deepEqual(plain(dm.parseUsdmSeries(csv,'t','s').weeks),[{date:'20120731',shares:[100,100,100,85,37]}],'a categorical answer is accumulated');
 assert.deepEqual(plain(dm.parseUsdmSeries(JSON.stringify([{mapdate:'7/31/2012',d0:10,d1:20,d2:0,d3:0,d4:0}]),'t','s').weeks[0].shares),[30,20,0,0,0],'no None column: a rising share means categorical');
 assert.throws(()=>dm.parseUsdmSeries('[]','t','s'),/no Kansas weeks/);
 assert.ok(dm.validDroughtSeries(plain(s)));
 assert.ok(!dm.validDroughtSeries({...plain(s),weeks:[]}));
});

test('the reading prefers the USDM\'s own statistics and says when it measured the map instead',()=>{
 const map=dm.parseUsdmMap(national,'20261020','t','s');
 const series={weeks:[{date:'20261020',shares:[76.6,50.12,20.3,3.2,0]}],retrievedAt:'t',source:'s'};
 assert.equal(dm.droughtReading(map,series),'Valid Oct 20, 2026 · 50% of Kansas in drought (D1–D4) · D2+ 20% · D3+ 3.2% · D4 none');
 assert.match(dm.droughtReading(map,null),/^Valid Oct 20, 2026 · ≈ \d+% of Kansas in drought \(D1–D4\) · D2\+ ≈ [\d.]+% · D3\+ ≈ none · D4 ≈ none · shares measured on the map$/);
 const dry={...map,kansas:[12.5,0,0,0,0]};
 assert.equal(dm.droughtReading(dry,null),'Valid Oct 20, 2026 · no drought in Kansas; ≈ 13% abnormally dry · shares measured on the map');
 assert.equal(dm.droughtReading({...map,kansas:[0,0,0,0,0]},{weeks:[],retrievedAt:'t',source:'s'}),'Valid Oct 20, 2026 · no part of Kansas abnormally dry or in drought · shares measured on the map');
 const key=dm.droughtKey('20261020');
 assert.equal(key.title,'U.S. Drought Monitor · Oct 20, 2026');
 assert.deepEqual(plain(key.items.map(i=>[i.label,i.color,i.shape])),[['D0 Abnormally dry','#ffff00','area'],['D1 Moderate drought','#fcd37f','area'],['D2 Severe drought','#ffaa00','area'],['D3 Extreme drought','#e60000','area'],['D4 Exceptional drought','#730000','area']]);
 assert.match(key.note,/D0 is abnormally dry, not drought/);
});

test('the categories draw in the USDM colours, under the site overlays, and pass the style validator',async()=>{
 const {validateStyleMin}=await import('@maplibre/maplibre-gl-style-spec');
 const layers=[{id:'background'},{id:'kfm-roads'}];let source=null;const calls=[];
 const sources={};
 const map={getSource:id=>id===dm.DROUGHT_SOURCE_ID?source:sources[id],addSource:(id,spec)=>{if(id!==dm.DROUGHT_SOURCE_ID){sources[id]=spec;return;}source={spec,setData:d=>calls.push(['setData',d.features.length])};},
  getLayer:id=>layers.find(l=>l.id===id),addLayer:(spec,before)=>layers.splice(layers.findIndex(l=>l.id===before),0,{id:spec.id,spec}),
  getStyle:()=>({layers}),removeLayer:id=>layers.splice(layers.findIndex(l=>l.id===id),1),removeSource:id=>{if(id===dm.DROUGHT_SOURCE_ID)source=null;else delete sources[id];}};
 const drought=dm.parseUsdmMap(national,'20261020','t','s');
 dm.syncDroughtMonitor(map,drought);
 assert.deepEqual(layers.map(l=>l.id),['background',dm.DROUGHT_FILL_LAYER_ID,dm.DROUGHT_LINE_LAYER_ID,dm.DROUGHT_STATE_LAYER_ID,'kfm-roads'],'the state line over the categories');
 const outline=sources[dm.DROUGHT_STATE_SOURCE_ID].data.geometry.coordinates[0];
 assert.deepEqual(outline[0],outline.at(-1));assert.equal(outline.length,orientation.KANSAS_OUTLINE.length+1);
 assert.deepEqual(plain(layers[1].spec.paint['fill-color']),['match',['get','dm'],0,'#ffff00',1,'#fcd37f',2,'#ffaa00',3,'#e60000',4,'#730000','#9aa5ad']);
 dm.syncDroughtMonitor(map,drought);
 assert.deepEqual(calls,[],'the same map is not sent again');
 dm.syncDroughtMonitor(map,dm.parseUsdmMap({type:'FeatureCollection',features:[]},'20261013','t','s'));
 assert.deepEqual(calls,[['setData',0]]);
 const style={version:8,sources:{[dm.DROUGHT_SOURCE_ID]:{type:'geojson',data:{type:'FeatureCollection',features:[]}},[dm.DROUGHT_STATE_SOURCE_ID]:sources[dm.DROUGHT_STATE_SOURCE_ID]},layers:layers.slice(1,4).map(l=>l.spec)};
 assert.deepEqual(validateStyleMin(plain(style)).map(e=>e.message),[]);
 dm.syncDroughtMonitor(map,null);
 assert.deepEqual(layers.map(l=>l.id),['background','kfm-roads']);assert.equal(source,null);assert.deepEqual(sources,{});
});

test('the route answers a chosen week, falls back a week when the newest is late, and refuses other dates',async()=>{
 const asked=[];let failing=new Set();
 const upstream={boundedFetch:async url=>{asked.push(url);if([...failing].some(d=>url.includes(d)))throw new Error('HTTP 404');return {text:()=>JSON.stringify(national)};}};
 const route=await compile('app/api/drought-monitor/route.ts',{'../event-atlas/upstream':upstream,'../../drought-monitor':dm});
 const latest=dm.latestUsdmDate(new Date()),before=dm.previousUsdmDate(latest);
 failing=new Set([latest]);
 let response=await route.GET(new Request('http://x/api/drought-monitor'));
 assert.equal(response.status,200);
 assert.equal((await response.json()).date,before,'a late release answers the week before');
 assert.deepEqual(asked,[dm.usdmMapProviderUrl(latest),dm.usdmMapProviderUrl(before)]);
 asked.length=0;
 response=await route.GET(new Request(`http://x/api/drought-monitor?date=${before}`));
 assert.equal((await response.json()).date,before);
 assert.deepEqual(asked,[],'a past week is kept');
 assert.match(response.headers.get('cache-control'),/max-age=86400/);
 for(const bad of ['20261021','19991228','x',dm.nextUsdmDate(latest)]){
  response=await route.GET(new Request(`http://x/api/drought-monitor?date=${bad}`));
  assert.equal(response.status,400,bad);
 }
 failing=new Set(['usdm_']);
 response=await route.GET(new Request(`http://x/api/drought-monitor?date=20000104`));
 assert.equal(response.status,502);assert.equal(response.headers.get('cache-control'),'no-store');
 const series=await compile('app/api/drought-series/route.ts',{'../event-atlas/upstream':{boundedFetch:async()=>({text:()=>'[{"MapDate":"20261020","None":23.4,"D0":76.6,"D1":50.1,"D2":20.3,"D3":3.2,"D4":0}]'})},'../../drought-monitor':dm});
 const answer=await (await series.GET()).json();
 assert.deepEqual(answer.weeks,[{date:'20261020',shares:[76.6,50.1,20.3,3.2,0]}]);
 const upstreamSource=await readFile('app/api/event-atlas/upstream.ts','utf8');
 assert.match(upstreamSource,/"https:\/\/droughtmonitor\.unl\.edu", "https:\/\/usdmdataservices\.unl\.edu"/,'both origins are on the bounded fetch allowlist');
});

test('the Field view dock shows the Drought Monitor with its Kansas chart, a week slider and week steps',async()=>{
 const look=maps.CATEGORY_MAPS.agriculture;
 assert.ok(look.tools.includes('drought'));
 assert.match(look.lede,/weekly U\.S\. Drought Monitor/);
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  onDrought:v=>calls.push(['on',v]),onDroughtWeek:v=>calls.push(['week',v])};
 const weeks=['20261006','20261013','20261020'].map((date,i)=>({date,label:dm.usdmDateLabel(date),shares:[70+i,40+i,20,3,i===1?1:0]}));
 const drought={on:false,loading:false,failed:false,reading:null,url:dm.USDM_PAGE,date:null,label:null,previous:null,next:null,newest:true,categories:dm.USDM_CATEGORIES,weeks:null,seriesFailed:false};
 let tree=h.render(h.exports.CategoryMapDock,{...base,drought});
 findNode(tree,n=>n.type==='button'&&n.props.children==='Show the Drought Monitor').props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,drought:{...drought,on:true,loading:true}});
 assert.match(JSON.stringify(tree),/Reading the Drought Monitor…/);
 const shown={...drought,on:true,reading:'Valid Oct 13, 2026 · 41% of Kansas in drought (D1–D4)',date:'20261013',label:'Oct 13, 2026',previous:'20261006',next:'20261020',newest:false,weeks};
 tree=h.render(h.exports.CategoryMapDock,{...base,drought:shown});
 assert.match(JSON.stringify(tree),/41% of Kansas in drought/);
 const chart=findNode(tree,n=>n.type===h.exports.DroughtChart);
 assert.equal(chart.props.weeks,weeks);
 const figure=h.exports.DroughtChart(chart.props);
 assert.match(figure.props['aria-label'],/2026–2026; drought \(D1–D4\) peaked at 42% in the week of Oct 20, 2026/);
 const paths=findNode(figure,n=>n.type==='svg').props.children[0];
 assert.deepEqual(paths.map(p=>p.props.fill),['#ffff00','#fcd37f','#ffaa00','#e60000','#730000'],'milder categories first, worse over them');
 assert.equal(paths[1].props.d,'M0,50 L0,30.00 L1,29.50 L2,29.00 L2,50 Z');
 const svg=findNode(figure,n=>n.type==='svg');
 svg.props.onClick({clientX:10,currentTarget:{getBoundingClientRect:()=>({left:0,width:100})}});
 svg.props.onClick({clientX:99,currentTarget:{getBoundingClientRect:()=>({left:0,width:100})}});
 const slider=findNode(tree,n=>n.type==='input'&&n.props.type==='range');
 assert.equal(slider.props.value,1);assert.equal(slider.props['aria-valuetext'],'Oct 13, 2026');
 slider.props.onChange({target:{value:'0'}});slider.props.onChange({target:{value:'2'}});
 const step=label=>findNode(tree,n=>n.type==='button'&&(n.props['aria-label']===label||n.props.children===label));
 step('Week before').props.onClick();step('Week after').props.onClick();step('Newest').props.onClick();
 assert.equal(step('Newest').props['aria-pressed'],false);
 assert.deepEqual(calls,[['on',true],['week','20261006'],['week',null],['week','20261006'],['week',null],['week','20261006'],['week','20261020'],['week',null]]);
 tree=h.render(h.exports.CategoryMapDock,{...base,drought:{...shown,failed:true,weeks:null,seriesFailed:true,next:null}});
 const text=JSON.stringify(tree);
 assert.match(text,/did not answer for this week/);assert.match(text,/the shares are measured on the map/);
 assert.ok(!findNode(tree,n=>n.type==='input'&&n.props.type==='range'),'no slider without the series');
 assert.equal(findNode(tree,n=>n.type==='button'&&n.props['aria-label']==='Week after').props.disabled,true);
 assert.ok(!findNode(h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.weather,drought}),n=>n.type==='button'&&n.props.children==='Show the Drought Monitor'),'only maps that offer it');
 h.dispose?.();
});

test('the page reads the week shown, keeps the last map drawn while the next loads, and closes it with its map',()=>{
 assert.match(page,/fetch\(`\/api\/drought-monitor\$\{droughtWeek \? `\?date=\$\{droughtWeek\}` : ""\}`, \{ signal: controller\.signal \}\)/);
 assert.match(page,/\}, droughtWeek \? 350 : 0\);/,'a dragged slider settles before a week is read');
 assert.match(page,/fetch\("\/api\/drought-series", \{ signal: controller\.signal \}\)/);
 assert.match(page,/const shownDrought = droughtId \? droughtLoaded \?\? lastDroughtRef\.current : null;/);
 assert.match(page,/syncDroughtMonitor\(map, shownDrought\);/);
 assert.match(page,/\.\.\.\(shownDrought \? \[droughtKey\(shownDrought\.date\)\] : \[\]\)/);
 assert.match(page,/if \(on && map && map\.getZoom\(\) > 7\.5\) map\.easeTo\(\{ center: \[-98\.38, 38\.5\], zoom: 6\.2, duration: motionDuration\(1200\), essential: false \}\);/,'a field-scale view pulls out to the state');
 assert.match(page,/setQuakeRecordSelected\(null\);\s*setDroughtOn\(false\);\s*setDroughtWeek\(null\);\s*setOutlookDay\(null\);[\s\S]{0,200}\/\/ Each map opens on its own subject/);
 assert.match(page,/if \(droughtOn\) params\.set\("drought", droughtWeek \?\? "newest"\);/);
 assert.match(page,/setDroughtOn\(droughtOffered && \(restoredDrought === "newest" \|\| isUsdmDate\(restoredDrought\)\)\);/);
 assert.match(page,/const chooseDroughtWeek = \(date: string \| null\) => \{ setDroughtWeek\(date && date !== droughtNewest \? date : null\); setDroughtFailed\(null\); \};/,'the newest week is followed, not pinned');
});
