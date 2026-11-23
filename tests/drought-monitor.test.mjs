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
 assert.deepEqual(Object.fromEntries(series.searchParams),{aoi:'20',startdate:'1/1/2000',enddate:'10/29/2026',statisticsType:'1'},'Kansas by its state FIPS code');
 assert.deepEqual(plain(dm.USDM_SERIES_AREAS),['20','KS']);
 assert.equal(new URL(dm.usdmSeriesProviderUrl(new Date('2026-10-29T05:00:00Z'),'KS')).searchParams.get('aoi'),'KS');
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

test('the Kansas series asks by state code, falls back to the postal code on an empty answer, and keeps a series through a failed read',async()=>{
 // What the USDM data services sent on 2026-11-22: CSV for the state code, and an empty answer for the postal code.
 const csv='MapDate,StateAbbreviation,None,D0,D1,D2,D3,D4,ValidStart,ValidEnd,StatisticFormatID\n20261117,KS,62.90,37.10,11.92,1.66,0.00,0.00,2026-11-17,2026-11-23,1\n20261110,KS,64.50,35.50,11.49,1.75,0.00,0.00,2026-11-10,2026-11-16,1\n';
 const asked=[];let answer=url=>new URL(url).searchParams.get('aoi')==='20'?csv:'';
 const realNow=Date.now;let clock=realNow();Date.now=()=>clock;
 try{
  const load=()=>compile('app/api/drought-series/route.ts',{'../event-atlas/upstream':{boundedFetch:async url=>{asked.push(new URL(url).searchParams.get('aoi'));const text=answer(url);if(text===null)throw new Error('Source unavailable (HTTP 503).');return {text:()=>text};}},'../../drought-monitor':dm});
  let route=await load();
  let response=await route.GET();
  assert.equal(response.status,200);
  assert.deepEqual((await response.json()).weeks,[{date:'20261110',shares:[35.5,11.49,1.75,0,0]},{date:'20261117',shares:[37.1,11.92,1.66,0,0]}]);
  assert.deepEqual(asked,['20'],'the state code answers, so the postal code is not asked');
  // Within six hours the series in hand is served without asking.
  clock+=5*3600_000;await route.GET();assert.deepEqual(asked,['20']);
  // Past six hours the provider fails: the series in hand is served, briefly cacheable, and the provider is left alone for five minutes.
  clock+=2*3600_000;answer=()=>null;
  response=await route.GET();
  assert.equal(response.status,200);assert.equal((await response.json()).weeks.length,2);
  assert.equal(response.headers.get('cache-control'),'public, max-age=300');
  assert.deepEqual(asked,['20','20'],'a provider that does not answer is not asked under the other name');
  clock+=4*60_000;await route.GET();assert.deepEqual(asked,['20','20'],'not asked again inside five minutes');
  clock+=2*60_000;answer=url=>new URL(url).searchParams.get('aoi')==='KS'?csv:'[]';
  response=await route.GET();
  assert.deepEqual(asked,['20','20','20','KS'],'an empty answer for one name is asked again under the other');
  assert.match(response.headers.get('cache-control'),/s-maxage=21600/);
  assert.match((await response.json()).source,/aoi=KS/,'the source says which request was answered');
  // With nothing in hand a failure is a 503 whose message survives the host, and it is not kept.
  route=await load();asked.length=0;answer=()=>'[]';
  response=await route.GET();
  assert.equal(response.status,503);assert.equal(response.headers.get('cache-control'),'no-store');
  assert.match((await response.json()).message,/Drought Monitor statistics are unavailable/);
  assert.deepEqual(asked,['20','KS']);
  clock+=6*60_000;answer=url=>new URL(url).searchParams.get('aoi')==='20'?csv:'';
  assert.equal((await route.GET()).status,200,'a later read recovers');
  // Requests that arrive together share one read.
  route=await load();asked.length=0;
  const both=await Promise.all([route.GET(),route.GET()]);
  assert.deepEqual(both.map(r=>r.status),[200,200]);assert.deepEqual(asked,['20']);
 }finally{Date.now=realNow;}
});

test('a week is read once for everyone who asks, two weeks at a time, with a short line behind them',async()=>{
 const started=[];const release=new Map();let inFlight=0,most=0;
 const upstream={boundedFetch:url=>{const date=/usdm_(\d{8})/.exec(url)[1];started.push(date);inFlight++;most=Math.max(most,inFlight);
  return new Promise(resolve=>release.set(date,()=>{inFlight--;resolve({text:()=>JSON.stringify(national)});}));}};
 const route=await compile('app/api/drought-monitor/route.ts',{'../event-atlas/upstream':upstream,'../../drought-monitor':dm});
 const weeks=[];for(let date='20260106';weeks.length<16;date=dm.previousUsdmDate(date))weeks.push(date);
 const ask=date=>route.GET(new Request(`http://x/api/drought-monitor?date=${date}`));
 const settle=async()=>{for(let i=0;i<20;i++)await Promise.resolve();};
 // Three visitors ask for the same week: one read.
 const same=[ask(weeks[0]),ask(weeks[0]),ask(weeks[0])];
 await settle();assert.deepEqual(started,[weeks[0]]);
 // Fourteen more weeks: one more is read now, twelve wait, and the one after that is told to try again.
 const others=weeks.slice(1,14).map(ask);
 await settle();assert.deepEqual(started,[weeks[0],weeks[1]],'two weeks are read at once');
 const refused=await ask(weeks[14]);
 assert.equal(refused.status,503);assert.equal(refused.headers.get('retry-after'),'3');assert.equal(refused.headers.get('cache-control'),'no-store');
 assert.match((await refused.json()).message,/reading other weeks/);
 assert.equal(started.length,2,'a refused week is not read');
 // As each read finishes the next in line starts; the count never passes two.
 for(let i=0;i<14;i++){release.get(weeks[i])();await settle();}
 const answers=await Promise.all([...same,...others]);
 assert.deepEqual(answers.map(r=>r.status),Array(16).fill(200));
 assert.deepEqual(started,weeks.slice(0,14),'the line is served in order');
 assert.equal(most,2);
 assert.equal((await answers[0].json()).date,weeks[0]);
 // A read that fails gives its place up, and the week can be asked for again.
 const failing=await compile('app/api/drought-monitor/route.ts',{'../event-atlas/upstream':{boundedFetch:async()=>{throw new Error('HTTP 503');}},'../../drought-monitor':dm});
 for(let i=0;i<5;i++)assert.equal((await failing.GET(new Request(`http://x/api/drought-monitor?date=${weeks[i]}`))).status,502);
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

test('history loading is separate from the weekly map and its source remains available through success and failure',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const base={look:maps.CATEGORY_MAPS.agriculture,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,
  onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},onDrought(){},onDroughtWeek(){}};
 const weeks=['20261006','20261013','20261020'].map(date=>({date,label:dm.usdmDateLabel(date),shares:[70,40,20,3,0]}));
 const drought={on:true,loading:false,failed:false,reading:'Valid Oct 20, 2026 · 40% of Kansas in drought (D1–D4)',url:dm.USDM_PAGE,
  date:'20261020',label:'Oct 20, 2026',previous:'20261013',next:null,newest:true,categories:dm.USDM_CATEGORIES,weeks:null,seriesFailed:false};
 try{
  for(const [name,patch,historyPending,chartVisible] of [
   ['both requests pending',{loading:true},true,false],
   ['weekly map ready while history waits',{},true,false],
   ['history ready while weekly map waits',{weeks,loading:true},false,true],
   ['both requests ready',{weeks},false,true],
   ['history retry pending',{},true,false],
   ['history failed with a usable weekly map',{seriesFailed:true},false,false],
   ['weekly map failed with usable history',{weeks,failed:true},false,true],
   ['both requests failed',{seriesFailed:true,failed:true},false,false],
  ]){
   const state={...drought,...patch};
   const tree=h.render(h.exports.CategoryMapDock,{...base,drought:state});
   const panel=findNode(tree,n=>n.props?.className==='category-map-dock-drought');
   const status=findNode(panel,n=>n.props?.role==='status');
   assert.equal(Boolean(status),historyPending,name);
   if(status)assert.equal(status.props.children,'Loading Kansas drought history…',name);
   assert.equal(Boolean(findNode(panel,n=>n.type===h.exports.DroughtChart)),chartVisible,name);
   assert.equal(Boolean(findNode(panel,n=>n.type===h.exports.DroughtWeekComparison)),chartVisible,name);
   const reading=findNode(panel,n=>n.type==='p'&&n.props.className==='category-map-dock-reading');
   assert.equal(reading.props.children,state.failed?'The Drought Monitor did not answer for this week.':state.loading?'Reading the Drought Monitor for Oct 20, 2026…':drought.reading,name);
   const links=[];
   findNode(panel,n=>{if(n.type==='a'&&n.props.href===dm.USDM_PAGE)links.push(n);return false;});
   assert.equal(links.length,1,`${name}: one source link, including failures`);
   assert.equal(links[0].props.children,'U.S. Drought Monitor source ↗',name);
   assert.equal(links[0].props.target,'_blank',name);
   assert.equal(links[0].props.rel,'noreferrer',name);
   assert.equal(JSON.stringify(panel).includes('The USDM statistics did not answer'),state.seriesFailed,name);
  }
  const closed=h.render(h.exports.CategoryMapDock,{...base,drought:{...drought,on:false}});
  assert.ok(!findNode(closed,n=>n.props?.className==='category-map-dock-drought'),'a hidden tool announces no history load');
 }finally{h.dispose();}
});

test('statewide comparison uses exact recorded weeks and cumulative severity shares', async () => {
 const h = await componentHarness('app/category-map-dock.tsx', {});
 const weeks = [
  { date: '20000104', label: 'Jan 4, 2000', shares: [55.99, 7.84, 0, 0, 0] },
  { date: '20120807', label: 'Aug 7, 2012', shares: [100, 100, 100, 89.74, 38.58] },
  { date: '20120821', label: 'Aug 21, 2012', shares: [100, 100, 100, 90, 65] },
  { date: '20261117', label: 'Nov 17, 2026', shares: [37.10, 11.92, 1.66, 0, 0] },
 ];
 const render = (records = weeks) => h.render(h.exports.DroughtWeekComparison, { weeks: records });
 let tree = render();
 const result = () => findNode(tree, node => Object.hasOwn(node.props, 'data-comparison-result'))?.props.children;
 const row = slot => findNode(tree, node => node.props['data-comparison-week'] === slot);
 const input = slot => findNode(row(slot), node => node.type === 'input').props;
 const step = label => findNode(tree, node => node.props['aria-label'] === label).props;
 const change = (slot, value) => input(slot).onChange({ target: { value } });
 assert.equal(result(), undefined, 'the comparison is collapsed initially');
 tree.props.onToggle({ currentTarget: { open: true } });
 tree = render();
 assert.equal(input('a').value, '2012-08-07');
 assert.equal(input('b').value, '2026-11-17');
 assert.equal(step('Next recorded week for B')['aria-disabled'], true);
 step('Next recorded week for B').onClick();
 tree = render();
 assert.equal(input('b').value, '2026-11-17', 'a boundary button leaves the week and keyboard focus in place');
 assert.equal(result(), 'Week B is 98.34 percentage points lower than week A.');

 change('a', '2012-08-14'); // A Tuesday absent from this archive fixture.
 tree = render();
 assert.equal(input('a')['aria-invalid'], true);
 assert.match(JSON.stringify(row('a')), /Showing Aug 7, 2012/);
 assert.equal(result(), 'Week B is 98.34 percentage points lower than week A.');
 step('Next recorded week for A').onClick();
 tree = render();
 assert.equal(input('a').value, '2012-08-21', 'stepping follows records across gaps');
 assert.equal(input('a')['aria-invalid'], undefined);
 findNode(tree, node => node.type === 'select').props.onChange({ target: { value: '4' } });
 tree = render();
 assert.equal(result(), 'Week B is 65.00 percentage points lower than week A.');
 assert.equal(findNode(row('b'), node => node.type === 'b').props.children.join(''), '0.00%', 'a measured zero is presented');
 change('a', '2026-11-17');
 tree = render();
 assert.equal(result(), 'Both weeks cover the same share of Kansas.');
 change('b', '2012-08-07');
 tree = render();
 assert.equal(result(), 'Week B is 38.58 percentage points higher than week A.');

 tree = render(weeks.filter(week => week.date !== '20120807'));
 assert.equal(input('b').value, '2012-08-07', 'a removed choice is not silently replaced');
 assert.equal(input('b')['aria-invalid'], true);
 assert.equal(result(), 'Choose two recorded weeks to calculate the difference.');
 h.dispose();
});

test('comparison defaults use dates actually available in a short archive', async () => {
 const h = await componentHarness('app/category-map-dock.tsx', {});
 const weeks = [
  { date: '20261006', label: 'Oct 6, 2026', shares: [70, 41, 20, 3, 0] },
  { date: '20261013', label: 'Oct 13, 2026', shares: [72, 40, 19, 3, 0] },
  { date: '20261020', label: 'Oct 20, 2026', shares: [73, 39, 18, 3, 0] },
 ];
 const render = records => h.render(h.exports.DroughtWeekComparison, { weeks: records });
 assert.equal(render([weeks[0]]), null);
 render(weeks.slice(0, 2)).props.onToggle({ currentTarget: { open: true } });
 let tree = render(weeks.slice(0, 2));
 const input = id => findNode(findNode(tree, node => node.props['data-comparison-week'] === id), node => node.type === 'input').props;
 assert.equal(input('a').value, '2026-10-06');
 assert.equal(input('b').value, '2026-10-13');
 tree = render(weeks);
 assert.equal(input('b').value, '2026-10-20', 'the untouched latest choice follows a new record');
 h.dispose();
});

test('the page reads the week shown, keeps the last map drawn while the next loads, and closes it with its map',()=>{
 assert.match(page,/fetch\(`\/api\/drought-monitor\$\{droughtWeek \? `\?date=\$\{droughtWeek\}` : ""\}`, \{ signal: controller\.signal \}\)/);
 assert.match(page,/\}, droughtWeek \? 350 : 0\);/,'a dragged slider settles before a week is read');
 assert.match(page,/fetch\("\/api\/drought-series", \{ signal: controller\.signal \}\)/);
 assert.match(page,/const shownDrought = droughtId \? droughtLoaded \?\? lastDroughtRef\.current : null;/);
 assert.match(page,/syncDroughtMonitor\(map, shownDrought, droughtCounties, droughtCounty, shownDroughtChange\?\.data \?\? null\);/);
 assert.match(page,/\.\.\.\(shownDrought \? \[shownDroughtChange \? droughtChangeKey\(shownDroughtChange\.weeks, shownDroughtChange\.from, shownDroughtChange\.to\) : droughtKey\(shownDrought\.date\)\] : \[\]\)/);
 assert.match(page,/if \(freshDroughtChange\) lastDroughtChangeRef\.current = freshDroughtChange;\s*else if \(!droughtOn \|\| droughtChange !== lastDroughtChangeRef\.current\?\.weeks \|\| droughtChangeTooEarly \|\| \(droughtId !== null && droughtFailed === droughtId\)\s*\|\| \(droughtSinceDate !== null && droughtSinceFailed === droughtSinceDate\)\) lastDroughtChangeRef\.current = null;/,'the change last drawn holds while the next loads, and goes with a failure or another view');
 assert.match(page,/if \(on && map && map\.getZoom\(\) > 7\.5\) map\.easeTo\(\{ center: \[-98\.38, 38\.5\], zoom: 6\.2, duration: motionDuration\(1200\), essential: false \}\);/,'a field-scale view pulls out to the state');
 assert.match(page,/setQuakeRecordSelected\(null\);\s*setDroughtOn\(false\);\s*setDroughtWeek\(null\);\s*setDroughtCounty\(null\);\s*setOutlookDay\(null\);[\s\S]{0,200}\/\/ Each map opens on its own subject/);
 assert.match(page,/if \(droughtOn\) params\.set\("drought", droughtWeek \?\? "newest"\);/);
 assert.match(page,/setDroughtOn\(droughtOffered && \(restoredDrought === "newest" \|\| isUsdmDate\(restoredDrought\)\)\);/);
 assert.match(page,/const chooseDroughtWeek = \(date: string \| null\) => \{ setDroughtPlaying\(false\); setDroughtWeek\(date && date !== droughtNewest \? date : null\); setDroughtFailed\(null\); \};/,'the newest week is followed, not pinned');
});

test('the page keeps the newest and the dozen weeks read most recently, the week just read always among them',()=>{
 const week=date=>({date,data:{type:'FeatureCollection',features:[]},kansas:[0,0,0,0,0],retrievedAt:'t',source:'s'});
 // Twelve recent weeks read first, then an older one: as object keys, "YYYYMMDD" would list numerically and evict it at once.
 let maps=new Map([['newest',week('20261020')]]);
 let date='20261013';
 for(let i=0;i<12;i++){maps=dm.rememberDroughtMap(maps,date,week(date));date=dm.previousUsdmDate(date);}
 assert.equal(maps.size,13);
 const older='20240102';
 maps=dm.rememberDroughtMap(maps,older,week(older));
 assert.ok(maps.has(older),'the week just read is kept');
 assert.ok(maps.has('newest'));
 assert.ok(!maps.has('20261013'),'the week read longest ago goes');
 assert.equal([...maps.keys()].filter(k=>k!=='newest').length,12);
 const reread=dm.rememberDroughtMap(maps,'20261006',week('20261006'));
 assert.equal([...reread.keys()].at(-1),'20261006','a week read again moves to the end');
 const plain={};for(const k of ['20261013','20261006','20240102'])plain[k]=1;
 assert.deepEqual(Object.keys(plain),['20240102','20261006','20261013'],'why a Map: object keys of this shape are ordered numerically');
 assert.equal(dm.rememberDroughtMap(new Map(),'newest',week('20261020')).size,1);
});

test('while shown, the newest map and the Kansas series are read again as they age; past weeks are not',()=>{
 assert.equal(dm.DROUGHT_NEWEST_REFRESH_MS,3600000);assert.equal(dm.DROUGHT_SERIES_REFRESH_MS,21600000);
 assert.match(page,/if \(current\) \{\s*\/\/[^\n]*\n\s*if \(droughtId !== "newest"\) return;\s*const age = Date\.now\(\) - \(droughtReadAtRef\.current\.get\(droughtId\) \?\? 0\);\s*if \(age < DROUGHT_NEWEST_REFRESH_MS\) \{\s*const timer = setTimeout\(\(\) => setDroughtTick\(tick => tick \+ 1\), DROUGHT_NEWEST_REFRESH_MS - age\);/);
 assert.match(page,/const age = droughtSeries \? Date\.now\(\) - droughtSeriesReadAtRef\.current : Infinity;\s*if \(age < DROUGHT_SERIES_REFRESH_MS\)/);
 assert.match(page,/setDroughtMaps\(maps => rememberDroughtMap\(maps, droughtId, value\)\);/);
 assert.match(page,/if \(current\) \{ droughtReadAtRef\.current\.set\(droughtId, Date\.now\(\)\); setDroughtTick\(tick => tick \+ 1\); \}\s*else setDroughtFailed\(droughtId\);/,'a failed re-read keeps the newest map shown');
 assert.match(page,/setDroughtFailed\(null\);\s*setDroughtSeriesFailed\(false\);/,'showing it again retries the series');
});

const county=(geoid,name,w,s,e,n)=>({type:'Feature',id:geoid,properties:{geoid,name},geometry:{type:'Polygon',coordinates:box(w,s,e,n)}});
const countiesFc={type:'FeatureCollection',features:[county('20055','Finney',-101.1,37.7,-100.2,38.3),county('20187','Stanton',-102.05,37.4,-101.55,37.75),county('20209','Wyandotte',-94.95,39.0,-94.6,39.2),
 {type:'Feature',properties:{name:'No id'},geometry:{type:'Polygon',coordinates:box(-99,38,-98.5,38.5)}}]};

test('each county\'s share in each category is measured on the map, and the counties list most severe first',()=>{
 const map=dm.parseUsdmMap(national,'20261020','t','s');
 const counties=dm.countyDroughtShares(map.data,countiesFc);
 assert.deepEqual(counties.map(c=>c.geoid),['20055','20187','20209'],'a county without a GEOID is left out');
 const [finney,stanton,wyandotte]=counties;
 assert.deepEqual(plain(stanton.shares),[100,100,100,0,0]);assert.equal(stanton.worst,2,'inside the D2 corner');
 assert.equal(finney.shares[1],100);assert.ok(finney.shares[2]>31&&finney.shares[2]<36,`the D2 corner covers two-thirds of Finney's width and half its height, a third of it (${finney.shares[2]})`);assert.equal(finney.worst,2);
 assert.deepEqual(plain(wyandotte.shares),[100,0,0,0,0]);assert.equal(wyandotte.worst,0);
 assert.deepEqual(plain(dm.countyDroughtList(counties)),[
  {id:'20187',label:'Stanton · D2 on all · drought on all'},{id:'20055',label:`Finney · D2 on ${Math.round(finney.shares[2])}% · drought on all`},{id:'20209',label:'Wyandotte · D0 on all'}]);
 assert.equal(dm.countyDroughtSummary(counties),'Counties reached: D1–D4 2 · D2+ 2 · D3+ 0 · D4 0 of 3 · measured on the map');
 assert.equal(dm.countyDroughtReading(stanton,'20261020'),'Stanton County · valid Oct 20, 2026 · D0+ all · D1+ all · D2+ all · D3+ none · D4 none · measured on the map');
 const none=dm.countyDroughtShares({type:'FeatureCollection',features:[]},countiesFc);
 assert.deepEqual(none.map(c=>c.worst),[-1,-1,-1]);
 assert.equal(dm.countyDroughtList(none)[0].label,'Finney · none','with nothing reaching them, counties list by name');
 assert.deepEqual(dm.countyDroughtShares(map.data,{type:'FeatureCollection',features:[]}),[]);
});

test('the county lines draw over the categories and under the state line, with the picked county outlined',async()=>{
 const {validateStyleMin}=await import('@maplibre/maplibre-gl-style-spec');
 const layers=[{id:'background'},{id:'kfm-roads'}];const sources={};const filters={};const setData=[];
 const map={getSource:id=>sources[id],addSource:(id,spec)=>{sources[id]={...spec,setData:d=>setData.push([id,d])};},getLayer:id=>layers.find(l=>l.id===id),
  addLayer:(spec,before)=>layers.splice(layers.findIndex(l=>l.id===before),0,{id:spec.id,spec}),getStyle:()=>({layers}),setFilter:(id,f)=>{filters[id]=f;},
  removeLayer:id=>layers.splice(layers.findIndex(l=>l.id===id),1),removeSource:id=>{delete sources[id];}};
 const drought=dm.parseUsdmMap(national,'20261020','t','s');
 dm.syncDroughtMonitor(map,drought);
 assert.ok(!sources[dm.DROUGHT_COUNTY_SOURCE_ID],'no county lines until the counties are in hand');
 dm.syncDroughtMonitor(map,drought,countiesFc,'20187');
 assert.deepEqual(layers.map(l=>l.id),['background',dm.DROUGHT_FILL_LAYER_ID,dm.DROUGHT_LINE_LAYER_ID,dm.DROUGHT_COUNTY_HIT_LAYER_ID,dm.DROUGHT_COUNTY_LAYER_ID,dm.DROUGHT_COUNTY_SELECTED_LAYER_ID,dm.DROUGHT_STATE_LAYER_ID,'kfm-roads']);
 assert.deepEqual(plain(layers[3].spec.paint),{'fill-color':'#000000','fill-opacity':0},'the hit area is never painted');
 assert.deepEqual(filters[dm.DROUGHT_COUNTY_SELECTED_LAYER_ID],['==',['get','geoid'],'20187']);
 dm.syncDroughtMonitor(map,drought,countiesFc,null);
 assert.deepEqual(filters[dm.DROUGHT_COUNTY_SELECTED_LAYER_ID],['==',['get','geoid'],'']);
 assert.equal(setData.length,0,'the same counties are not sent again');
 const style={version:8,sources:Object.fromEntries(Object.entries(sources).map(([id,s])=>[id,{type:'geojson',data:s.data}])),layers:layers.slice(1,7).map(l=>({...l.spec,...(l.id===dm.DROUGHT_COUNTY_SELECTED_LAYER_ID?{filter:filters[l.id]}:{})}))};
 assert.deepEqual(validateStyleMin(plain(style)).map(e=>e.message),[]);
 dm.syncDroughtMonitor(map,null);
 assert.deepEqual(layers.map(l=>l.id),['background','kfm-roads']);assert.deepEqual(Object.keys(sources),[]);
});

test('the dock lists the counties, outlines the one picked, and the page reads the Census counties with the Drought Monitor',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.agriculture,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  onDrought(){},onDroughtWeek(){},onDroughtCounty:id=>calls.push(['county',id]),onDroughtCountyClear:()=>calls.push(['clear'])};
 const list=[{id:'20187',label:'Stanton · D2 on all · drought on all'},{id:'20209',label:'Wyandotte · D0 on all'}];
 const drought={on:true,loading:false,failed:false,reading:'Valid Oct 20, 2026',url:dm.USDM_PAGE,date:'20261020',label:'Oct 20, 2026',previous:'20261013',next:null,newest:true,categories:dm.USDM_CATEGORIES,weeks:null,seriesFailed:false,
  counties:{summary:'Counties reached: D1–D4 1 · D2+ 1 · D3+ 0 · D4 0 of 2 · measured on the map',list,picked:'20187',reading:'Stanton County · valid Oct 20, 2026 · D0+ all'}};
 const tree=h.render(h.exports.CategoryMapDock,{...base,drought});
 const text=JSON.stringify(tree);
 assert.match(text,/Counties reached: D1–D4 1/);assert.match(text,/Stanton County · valid Oct 20, 2026/);
 const pick=findNode(tree,n=>n.props?.label==='Kansas counties by drought, most severe first');
 assert.equal(pick.props.summary,'Counties, most severe first (2)');
 const buttons=findNode(pick.type(pick.props),n=>n.props?.['aria-label']==='Kansas counties by drought, most severe first').props.children.map(li=>li.props.children);
 assert.deepEqual(buttons.map(b=>b.props['aria-pressed']),[true,false]);
 buttons[1].props.onClick();
 findNode(tree,n=>n.props?.['aria-label']==='Clear the selected county').props.onClick();
 assert.deepEqual(calls,[['county','20209'],['clear']]);
 assert.ok(!findNode(h.render(h.exports.CategoryMapDock,{...base,drought:{...drought,loading:true}}),n=>n.props?.label==='Kansas counties by drought, most severe first'),'not while a week loads');
 h.dispose?.();
 assert.match(page,/if \(!droughtOn \|\| officialPayloads\["census-counties"\] \|\| droughtCountiesAskedRef\.current\) return;\s*droughtCountiesAskedRef\.current = true;\s*void refreshOfficialContext\("census-counties"\);/,'asked once a showing, so a failed read does not repeat');
 assert.match(page,/setDroughtCounty\(null\);\s*setDroughtChange\(0\);\s*setDroughtSinceFailed\(null\);\s*droughtCountiesAskedRef\.current = false;/);
 assert.match(page,/const countyDrought = useMemo\(\(\) => droughtLoaded && droughtCounties \? countyDroughtShares\(droughtLoaded\.data, droughtCounties\) : null, \[droughtLoaded, droughtCounties\]\);/);
 assert.match(page,/syncDroughtMonitor\(map, shownDrought, droughtCounties, droughtCounty, shownDroughtChange\?\.data \?\? null\);/);
 assert.match(page,/setDroughtCounty\(geoid\);\s*mapRef\.current\?\.fitBounds\(geometry\.bounds, \{ padding: 70, maxZoom: 9, duration: motionDuration\(650\) \}\);/);
 assert.match(page,/setDroughtSeriesFailed\(false\);\s*setDroughtCounty\(null\);/);
 assert.match(page,/const clickedCounty = droughtCountyAtClick\(renderedHits, id => availableLayers\.includes\(id\) \|\| OFFICIAL_CONTEXT_INTERACTIVE_LAYER_IDS\.includes\(id\)\);\s*if \(clickedCounty\) \{\s*setDroughtCounty\(clickedCounty\);\s*setCategoryDockHidden\(false\);\s*return;/,'a click on a county picks it, and a closed dock comes back to show it');
 const hit=(source,layer,properties={})=>({source,layer:{id:layer},properties});
 const interactive=id=>id==='kfm-overlay-points';
 assert.equal(dm.droughtCountyAtClick([hit('kfm-roads','kfm-roads'),hit(dm.DROUGHT_COUNTY_SOURCE_ID,dm.DROUGHT_COUNTY_HIT_LAYER_ID,{geoid:'20055'}),hit(dm.DROUGHT_SOURCE_ID,dm.DROUGHT_FILL_LAYER_ID)],interactive),'20055','labels and roads above a county do not stop the pick');
 assert.equal(dm.droughtCountyAtClick([hit('overlay','kfm-overlay-points'),hit(dm.DROUGHT_COUNTY_SOURCE_ID,dm.DROUGHT_COUNTY_HIT_LAYER_ID,{geoid:'20055'})],interactive),null,'an interactive feature above the county keeps its own selection');
 assert.equal(dm.droughtCountyAtClick([hit(dm.DROUGHT_COUNTY_SOURCE_ID,dm.DROUGHT_COUNTY_HIT_LAYER_ID,{geoid:'20055'}),hit('overlay','kfm-overlay-points')],interactive),'20055','one beneath it does not');
 assert.equal(dm.droughtCountyAtClick([hit(dm.DROUGHT_SOURCE_ID,dm.DROUGHT_FILL_LAYER_ID)],interactive),null,'outside the counties nothing is picked');
});

test('Play steps the weeks forward to the newest, from a year back when the newest is shown, and only with motion allowed',async()=>{
 assert.equal(dm.usdmWeeksBefore('20261020',52),'20251021');
 assert.equal(dm.usdmWeeksBefore('20000111',5),'20000104','never before the first map');
 assert.equal(dm.DROUGHT_PLAY_STEP_MS,1200);assert.equal(dm.DROUGHT_PLAY_WEEKS,52);
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.agriculture,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  onDrought(){},onDroughtWeek(){},onDroughtPlay:v=>calls.push(v)};
 const drought={on:true,loading:false,failed:false,reading:'Valid Oct 20, 2026',url:dm.USDM_PAGE,date:'20261020',label:'Oct 20, 2026',previous:'20261013',next:null,newest:true,categories:dm.USDM_CATEGORIES,weeks:null,seriesFailed:false,playing:false,motionAllowed:true};
 const play=tree=>findNode(tree,n=>n.type==='button'&&(n.props.children==='Play'||n.props.children==='Pause'));
 let tree=h.render(h.exports.CategoryMapDock,{...base,drought});
 assert.equal(play(tree).props.title,'Play the past year, a week at a time');
 play(tree).props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,drought:{...drought,newest:false,playing:true}});
 assert.equal(play(tree).props.children,'Pause');assert.equal(play(tree).props['aria-pressed'],true);
 assert.equal(findNode(tree,n=>n.type==='p'&&n.props.className==='category-map-dock-reading').props['aria-live'],'off','the reading is not announced every week while playing');
 const withCounty=h.render(h.exports.CategoryMapDock,{...base,drought:{...drought,newest:false,playing:true,counties:{summary:'s',list:[{id:'20187',label:'Stanton'}],picked:'20187',reading:'Stanton County · valid Oct 20, 2026'}}});
 assert.equal(findNode(withCounty,n=>n.type==='div'&&n.props.className==='category-map-dock-quake-event').props['aria-live'],'off','nor the picked county\'s reading');
 const paused=h.render(h.exports.CategoryMapDock,{...base,drought:{...drought,counties:{summary:'s',list:[{id:'20187',label:'Stanton'}],picked:'20187',reading:'Stanton County'}}});
 assert.equal(findNode(paused,n=>n.type==='div'&&n.props.className==='category-map-dock-quake-event').props['aria-live'],'polite');
 play(tree).props.onClick();
 assert.deepEqual(calls,[true,false]);
 tree=h.render(h.exports.CategoryMapDock,{...base,drought:{...drought,motionAllowed:false,playing:true}});
 assert.equal(play(tree).props.disabled,true);assert.equal(play(tree).props.children,'Play');assert.match(play(tree).props.title,/Reduced motion is on/);
 h.dispose?.();
 assert.match(page,/const droughtPlayStops = droughtPlaying && \(!droughtOn \|\| guideOpen !== false \|\| primaryWorkspace !== "map"\s*\|\| reducedMotion \|\| droughtWeek === null \|\| \(droughtId !== null && droughtFailed === droughtId\)\);\s*if \(droughtPlayStops\) setDroughtPlaying\(false\);/,'stops at the newest, on a failed week, without motion, when the map closes, or when quick start or another workspace covers it');
 assert.match(page,/const droughtSinceWaiting = droughtSinceDate !== null && !droughtSince && droughtSinceFailed !== droughtSinceDate;/,'in a change view a step waits for its earlier week, or that week\'s failure');
 assert.match(page,/if \(!droughtPlaying \|\| droughtPlayStops \|\| !droughtWeek \|\| !droughtLoaded \|\| droughtSinceWaiting\) return;\s*const timer = setTimeout\(\(\) => \{\s*const next = nextUsdmDate\(droughtWeek\);\s*setDroughtWeek\(droughtNewest && next >= droughtNewest \? null : next\);\s*\}, DROUGHT_PLAY_STEP_MS\);/,'each week is held once it is drawn');
 assert.match(page,/if \(on && droughtWeek === null\) \{\s*const from = droughtNewest \?\? droughtDate;\s*if \(!from\) return;\s*setDroughtWeek\(usdmWeeksBefore\(from, DROUGHT_PLAY_WEEKS\)\);/);
 assert.match(page,/const chooseDroughtWeek = \(date: string \| null\) => \{ setDroughtPlaying\(false\);/,'a week chosen by hand pauses Play');
 assert.match(page,/onDroughtPlay=\{playDrought\}/);assert.match(page,/playing: droughtPlaying, motionAllowed: !reducedMotion,/);
});

test('a change view shades each county by its change in the Drought Severity and Coverage Index over 4 or 12 weeks',async()=>{
 assert.equal(dm.droughtChangeStart(4),'20000201');assert.equal(dm.droughtChangeStart(12),'20000328');
 assert.ok(dm.isUsdmDate(dm.droughtChangeStart(12)),'a Drought Monitor week');
 assert.equal(dm.dsci([100,100,100,0,0]),300);assert.equal(dm.dsci([0,0,0,0,0]),0);assert.equal(dm.dsci([100,100,100,100,100]),500);assert.equal(dm.dsci([76.6,50.12,20.3,3.2,0]),150);
 const now=[{geoid:'20055',name:'Finney',shares:[100,100,33.4,0,0],worst:2},{geoid:'20187',name:'Stanton',shares:[100,100,100,0,0],worst:2},{geoid:'20209',name:'Wyandotte',shares:[100,0,0,0,0],worst:0},{geoid:'20999',name:'New',shares:[0,0,0,0,0],worst:-1}];
 const then=[{geoid:'20055',name:'Finney',shares:[100,60,0,0,0],worst:1},{geoid:'20187',name:'Stanton',shares:[100,100,100,40,0],worst:3},{geoid:'20209',name:'Wyandotte',shares:[95,0,0,0,0],worst:0}];
 const changes=dm.countyDroughtChange(now,then);
 assert.deepEqual(plain(changes),[{geoid:'20055',name:'Finney',then:160,now:233,delta:73},{geoid:'20187',name:'Stanton',then:340,now:300,delta:-40},{geoid:'20209',name:'Wyandotte',then:95,now:100,delta:5}],'a county missing from either week is left out');
 assert.deepEqual([-150,-100,-60,-50,-11,-10,0,9.9,10,49,50,99,100,300].map(dm.dsciChangeColor),['#1b7837','#5aae61','#5aae61','#a6dba0','#a6dba0','#e8e4d8','#e8e4d8','#e8e4d8','#fdb863','#fdb863','#e66101','#e66101','#8c2d04','#8c2d04']);
 assert.deepEqual(plain(dm.countyChangeList(changes)),[{id:'20055',label:'Finney · +73 (160 → 233)'},{id:'20209',label:'Wyandotte · +5 (95 → 100)'},{id:'20187',label:'Stanton · -40 (340 → 300)'}],'the most worsened first');
 assert.equal(dm.countyChangeReading(changes[0],4),'DSCI 160 → 233 over 4 weeks (+73, worse)');
 assert.equal(dm.countyChangeReading(changes[2],12),'DSCI 95 → 100 over 12 weeks (+5, little change)');
 assert.equal(dm.droughtChangeReading([76.6,50.12,20.3,3.2,0],[90,70,30,5,0],4,'20260922',true),'Kansas DSCI 150 (0–500), -45 from 195 on Sep 22, 2026, 4 weeks before: better');
 assert.match(dm.droughtChangeReading([90,70,30,5,0],[76.6,50.12,20.3,3.2,0],12,'20260728',false),/\+45 from 150 on Jul 28, 2026, 12 weeks before: worse · measured on the map$/);
 const key=dm.droughtChangeKey(4,'20260922','20261020');
 assert.equal(key.title,'Drought change · Sep 22, 2026 to Oct 20, 2026');
 assert.deepEqual(plain(key.items.map(i=>i.label)),['100+ better','50–100 better','10–50 better','Within 10','10–50 worse','50–100 worse','100+ worse']);
 assert.match(key.note,/over 4 weeks/);assert.match(key.note,/not a measurement of rain or soil moisture/);
 const collection=dm.changeCollection(countiesFc,changes);
 assert.deepEqual(plain(collection.features.map(f=>f.properties)),[{geoid:'20055',delta:73},{geoid:'20187',delta:-40},{geoid:'20209',delta:5}]);
 // Layers: the change fill sits over the categories and under the county lines; it leaves with the change view.
 const {validateStyleMin}=await import('@maplibre/maplibre-gl-style-spec');
 const layers=[{id:'background'},{id:'kfm-roads'}];const sources={};
 const map={getSource:id=>sources[id],addSource:(id,spec)=>{sources[id]={...spec,setData(){}};},getLayer:id=>layers.find(l=>l.id===id),
  addLayer:(spec,before)=>layers.splice(layers.findIndex(l=>l.id===before),0,{id:spec.id,spec}),getStyle:()=>({layers}),setFilter(){},
  removeLayer:id=>layers.splice(layers.findIndex(l=>l.id===id),1),removeSource:id=>{delete sources[id];}};
 const drought=dm.parseUsdmMap(national,'20261020','t','s');
 dm.syncDroughtMonitor(map,drought,countiesFc,null,collection);
 assert.deepEqual(layers.map(l=>l.id),['background',dm.DROUGHT_FILL_LAYER_ID,dm.DROUGHT_LINE_LAYER_ID,dm.DROUGHT_CHANGE_LAYER_ID,dm.DROUGHT_COUNTY_HIT_LAYER_ID,dm.DROUGHT_COUNTY_LAYER_ID,dm.DROUGHT_COUNTY_SELECTED_LAYER_ID,dm.DROUGHT_STATE_LAYER_ID,'kfm-roads']);
 assert.deepEqual(plain(layers[3].spec.paint['fill-color']),['step',['get','delta'],'#1b7837',-100,'#5aae61',-50,'#a6dba0',-10,'#e8e4d8',10,'#fdb863',50,'#e66101',100,'#8c2d04']);
 const style={version:8,sources:Object.fromEntries(Object.entries(sources).map(([id,s])=>[id,{type:'geojson',data:s.data}])),layers:layers.slice(1,8).map(l=>l.spec)};
 assert.deepEqual(validateStyleMin(plain(style)).map(e=>e.message),[]);
 dm.syncDroughtMonitor(map,drought,countiesFc,null,null);
 assert.ok(!layers.some(l=>l.id===dm.DROUGHT_CHANGE_LAYER_ID)&&!sources[dm.DROUGHT_CHANGE_SOURCE_ID],'back to the categories');
 dm.syncDroughtMonitor(map,drought,countiesFc,null,collection);dm.syncDroughtMonitor(map,null);
 assert.deepEqual(Object.keys(sources),[]);
 // The dock offers the three views and says what the change view reads.
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.agriculture,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  onDrought(){},onDroughtWeek(){},onDroughtChange:w=>calls.push(w)};
 const drought2={on:true,loading:false,failed:false,reading:'Valid Oct 20, 2026',url:dm.USDM_PAGE,date:'20261020',label:'Oct 20, 2026',previous:'20261013',next:null,newest:true,categories:dm.USDM_CATEGORIES,weeks:null,seriesFailed:false,
  change:{weeks:4,reading:'Kansas DSCI 150 (0–500), -45 from 195 on Sep 22, 2026, 4 weeks before: better',loading:false,failed:false}};
 let tree=h.render(h.exports.CategoryMapDock,{...base,drought:drought2});
 const group=findNode(tree,n=>n.props?.['aria-label']==='Drought map view');
 const buttons=group.props.children;
 assert.deepEqual(JSON.parse(JSON.stringify(buttons.map(b=>[b.props.children,b.props['aria-pressed']]))),[['Categories',false],['4-week change',true],['12-week change',false]]);
 buttons[2].props.onClick();buttons[0].props.onClick();
 assert.deepEqual(calls,[12,0]);
 assert.match(JSON.stringify(tree),/Kansas DSCI 150 \(0–500\), -45 from 195/);
 const withCounties=h.render(h.exports.CategoryMapDock,{...base,onDroughtCounty(){},drought:{...drought2,counties:{summary:'s',list:[{id:'20055',label:'Finney · +73 (160 → 233)'}],picked:null,reading:null}}});
 const changeList=findNode(withCounties,n=>n.props?.label==='Kansas counties by drought change over 4 weeks, most worsened first');
 assert.equal(changeList.props.summary,'Counties, most worsened first (1)','the list says how it is ordered in a change view');
 tree=h.render(h.exports.CategoryMapDock,{...base,drought:{...drought2,change:{weeks:12,reading:null,loading:true,failed:false}}});
 assert.match(JSON.stringify(tree),/Reading the week 12 weeks before…/);
 tree=h.render(h.exports.CategoryMapDock,{...base,drought:{...drought2,change:{weeks:4,reading:null,loading:false,failed:true}}});
 assert.match(JSON.stringify(tree),/The earlier week did not answer; the categories stay on the map/);
 tree=h.render(h.exports.CategoryMapDock,{...base,drought:{...drought2,date:'20000111',change:{weeks:12,reading:null,start:'Mar 28, 2000',loading:false,failed:false}}});
 assert.match(JSON.stringify(tree),/The Drought Monitor begins Jan 4, 2000, so a 12-week change starts with the week of Mar 28, 2000; the categories stay on the map/,'a week too near the first map says why it has no change');
 tree=h.render(h.exports.CategoryMapDock,{...base,drought:{...drought2,change:{weeks:0,reading:null,loading:false,failed:false}}});
 assert.doesNotMatch(JSON.stringify(tree),/Reading the week|DSCI/,'the categories view says nothing about change');
 h.dispose?.();
 // The page reads the earlier week like any other, and the change view closes with the tool.
 assert.match(page,/const droughtChangeTooEarly = Boolean\(droughtChangeFrom && droughtLoaded && droughtLoaded\.date < droughtChangeFrom\);\s*const droughtSinceDate = droughtChange && droughtLoaded && !droughtChangeTooEarly \? usdmWeeksBefore\(droughtLoaded\.date, droughtChange\) : null;/,'no change is drawn without a whole interval behind the week');
 assert.match(page,/start: droughtChangeTooEarly && droughtChangeFrom \? usdmDateLabel\(droughtChangeFrom\) : null/);
 assert.match(page,/fetch\(`\/api\/drought-monitor\?date=\$\{droughtSinceDate\}`, \{ signal: controller\.signal \}\)/);
 assert.match(page,/setDroughtMaps\(maps => rememberDroughtMap\(maps, droughtSinceDate, value\)\);/);
 assert.match(page,/setDroughtCounty\(null\);\s*setDroughtChange\(0\);\s*setDroughtSinceFailed\(null\);/);
 assert.match(page,/list: countyChange \? countyChangeList\(countyChange\) : countyDroughtItems/);
});
