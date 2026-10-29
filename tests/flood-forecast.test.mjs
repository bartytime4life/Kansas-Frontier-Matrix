import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const mapKeys=await compile('app/map-keys.ts');
const ff=await compile('app/flood-forecast.ts',{'./map-keys':mapKeys});
const hydrology=await compile('app/noaa-hydrology.ts',{'./flood-forecast':ff});
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const liveContext=await readFile('app/live-context.ts','utf8');
const plain=v=>JSON.parse(JSON.stringify(v));

const routeSource=await readFile('app/api/hydrology/noaa/route.ts','utf8');
const shim='data:text/javascript,export const NextResponse={json:(body,init)=>Response.json(body,init)}';
const {GET:noaaGet}=await import(`data:text/javascript;base64,${Buffer.from(ts.transpileModule(routeSource.replace('from "next/server"',`from "${shim}"`),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`);

const HOUR=3_600_000, NOW=Date.parse('2026-10-29T18:00:00Z');
const iso=t=>new Date(t).toISOString().replace('.000Z','Z');
// NWPS-shaped answers for one Kansas gauge (synthetic values): rising toward a minor-flood crest on Nov 1.
const observedData=Array.from({length:217},(_,i)=>{const t=NOW-HOUR-(216-i)*HOUR;return {validTime:iso(t),generatedTime:iso(t+600_000),primary:8+4*i/216,secondary:2+i/100};});
const forecastData=Array.from({length:21},(_,i)=>{const t=NOW+i*6*HOUR;const v=i<=11?12+7.2*i/11:19.2-(i-11)*0.8;return {validTime:iso(t),generatedTime:'2026-10-29T14:00:00Z',primary:Math.round(v*100)/100,secondary:-999};});
const nwps={
 metadata:{lid:'WCHK1',usgsId:'07144100',reachId:'21001234',name:'Arkansas River at Wichita',description:'',county:'Sedgwick',timeZone:'CST6CDT',latitude:37.65,longitude:-97.35,
  rfc:{abbreviation:'ABRFC',name:'Arkansas-Red Basin'},wfo:{abbreviation:'ICT',name:'Wichita'},state:{abbreviation:'KS',name:'Kansas'},pedts:{observed:'HGIRG',forecast:'HGIFF'},
  status:{observed:{primary:12,primaryUnit:'ft',secondary:4.2,secondaryUnit:'kcfs',floodCategory:'no_flooding',validTime:'2026-10-29T17:00:00Z'},
   forecast:{primary:19.2,primaryUnit:'ft',secondary:-999,secondaryUnit:'kcfs',floodCategory:'minor',validTime:'2026-11-01T12:00:00Z'}},
  flood:{stageUnits:'ft',flowUnits:'kcfs',categories:{action:{stage:16,flow:9},minor:{stage:18,flow:12},moderate:{stage:23,flow:20},major:{stage:28,flow:31}},
   crests:{historic:[{occurredTime:'1993-07-24T12:00:00Z',stage:27.1,flow:30.1,preliminary:'',olddatum:false},{occurredTime:'1951-07-13T12:00:00Z',stage:32.4,flow:-999,preliminary:'',olddatum:true}],recent:[]},
   lowWaters:{historic:[]},impacts:[{stage:18,statement:'Low-lying parks flood.'}]},datums:{vertical:{value:[]}}},
 observed:{pedts:'HGIRG',issuedTime:null,wfo:'ICT',timeZone:'CST6CDT',primaryName:'Stage',primaryUnits:'ft',secondaryName:'Flow',secondaryUnits:'kcfs',data:observedData},
 forecast:{pedts:'HGIFF',issuedTime:'2026-10-29T14:00:00Z',wfo:'ICT',timeZone:'CST6CDT',primaryName:'Stage',primaryUnits:'ft',secondaryName:'Flow',secondaryUnits:'kcfs',data:forecastData},
};
const adapterAnswer=async(answers=nwps,lid='WCHK1')=>{
 const original=globalThis.fetch;
 globalThis.fetch=async input=>{const url=String(input);return Response.json(url.endsWith('/stageflow/observed')?answers.observed:url.endsWith('/stageflow/forecast')?answers.forecast:answers.metadata);};
 try{const response=await noaaGet({nextUrl:new URL(`http://localhost/api/hydrology/noaa?mode=gauge&lid=${lid}`)});assert.equal(response.status,200);return await response.json();}
 finally{globalThis.fetch=original;}
};

test('NWPS flood categories read as one set, ranked, in the NWS colours',()=>{
 assert.deepEqual(['no_flooding','Minor','MAJOR','action','obs_not_current','fcst_not_current','out_of_service','low_threshold','not_defined','',null,'banana'].map(ff.floodStatus),
  ['none','minor','major','action','not_current','not_current','out_of_service','low_water','not_defined','unknown','unknown','unknown']);
 assert.deepEqual(['major','moderate','minor','action','none','not_defined','unknown'].map(ff.floodRank),[4,3,2,1,0,-1,-1]);
 assert.deepEqual(ff.FLOOD_CATEGORIES.map(c=>[c.id,c.color]),[['action','#ffff00'],['minor','#ff9900'],['moderate','#ff0000'],['major','#cc33ff']]);
 assert.equal(ff.FLOOD_STATUS.none.color,'#00ff00');
 assert.equal(ff.floodGaugePage('WCHK1'),'https://water.noaa.gov/gauges/WCHK1');
 assert.equal(ff.floodGaugeApiPath('WCHK1'),'/api/hydrology/noaa?mode=gauge&lid=WCHK1');
 const key=ff.floodKey();
 assert.equal(key.items.length,8);assert.equal(key.items.at(-1).shape,'ring');assert.match(key.note,/Not a flood warning/);
});

test('the network lists gauges most severe first, observed or forecast, and sums them up',()=>{
 const f=(lid,name,o,fc)=>({properties:{lid,name,observedCategory:o,forecastCategory:fc}});
 const gauges=ff.floodGaugeSummaries([f('AAA1','Alpha','no_flooding','no_flooding'),f('BBB1','Bravo','minor','moderate'),f('CCC1','Charlie','no_flooding','major'),f('DDD1','Delta','action','action'),f('EEE1','Echo',null,null),{properties:{}}]);
 assert.equal(gauges.length,5,'a feature without a gauge id is left out');
 assert.deepEqual(plain(ff.floodGaugeList(gauges)),[
  {id:'CCC1',label:'Charlie (CCC1) · no flooding · forecast major flooding'},
  {id:'BBB1',label:'Bravo (BBB1) · minor flooding · forecast moderate flooding'},
  {id:'DDD1',label:'Delta (DDD1) · near flood stage (action)'},
  {id:'AAA1',label:'Alpha (AAA1) · no flooding'},
  {id:'EEE1',label:'Echo (EEE1) · no category given'}]);
 assert.equal(ff.floodNetworkSummary(gauges),'1 in flood · 1 near flood stage · 1 forecast to flood · 5 NWS gauges in Kansas');
 assert.equal(ff.floodNetworkSummary(gauges.slice(0,1)),'No Kansas gauge is above action stage or forecast to flood · 1 NWS gauge in Kansas');
 // The network layer carries both categories and the one the map colours by.
 const network=hydrology.parseNoaaGaugeNetwork({mode:'network',state:'ready',retrievedAt:'2026-10-29T18:00:00Z',partial:false,truncated:false,limitation:'x',
  sourceLinks:[{rel:'upstream',href:'https://api.water.noaa.gov/nwps/v1/gauges?bbox'}],records:[
   {kind:'gauge',sourceRole:'OFFICIAL_NWS_GAUGE_STATUS',lid:'WCHK1',name:'Arkansas River at Wichita',location:{latitude:37.65,longitude:-97.35},rfc:{abbreviation:'ABRFC'},wfo:{abbreviation:'ICT'},
    observed:{sourceRole:'OFFICIAL_NWS_OBSERVATION',validTime:'2026-10-29T17:00:00Z',primary:{value:12,unit:'ft'},secondary:{value:null,unit:null},floodCategory:'no_flooding'},
    forecast:{sourceRole:'OFFICIAL_NWS_FORECAST',validTime:'2026-11-01T12:00:00Z',primary:{value:19.2,unit:'ft'},secondary:{value:null,unit:null},floodCategory:'minor'}},
   {kind:'gauge',sourceRole:'OFFICIAL_NWS_GAUGE_STATUS',lid:'XXXK1',name:null,location:{latitude:38,longitude:-98},rfc:{abbreviation:null},wfo:{abbreviation:null},
    observed:{sourceRole:'OFFICIAL_NWS_OBSERVATION',validTime:null,primary:{value:null,unit:null},secondary:{value:null,unit:null},floodCategory:null},
    forecast:{sourceRole:'OFFICIAL_NWS_FORECAST',validTime:null,primary:{value:null,unit:null},secondary:{value:null,unit:null},floodCategory:'action'}}]});
 const props=hydrology.noaaGaugeNetworkGeoJson(network).features.map(x=>x.properties);
 assert.deepEqual(props.map(p=>[p.observedCategory,p.forecastCategory,p.floodStatus]),[['no_flooding','minor','none'],[null,'action','action']]);
 assert.match(liveContext,/"circle-color": \["match", \["get", "floodStatus"\], \.\.\.\(\["major", "moderate", "minor", "action", "none", "not_defined", "low_water", "not_current", "out_of_service"\] as const\)\.flatMap\(status => \[status, FLOOD_STATUS\[status\]\.color\]\), nwps\.color\]/,'the gauges are drawn in the key\'s colours');
});

test('a gauge reads end to end through the hydrology adapter: stages, series, forecast and crests in the plotted units',async()=>{
 const gauge=ff.parseFloodGauge(await adapterAnswer(),'WCHK1');
 assert.equal(gauge.name,'Arkansas River at Wichita');assert.equal(gauge.usgsId,'07144100');assert.equal(gauge.wfo,'ICT');
 assert.equal(gauge.quantity,'stage');assert.equal(gauge.label,'Stage');assert.equal(gauge.units,'ft');
 assert.deepEqual(plain(gauge.thresholds),{action:16,minor:18,moderate:23,major:28});
 assert.equal(gauge.observed.length,217);assert.equal(gauge.forecast.length,21);
 assert.ok(gauge.observed.every((p,i,a)=>!i||a[i-1].time<p.time),'in time order');
 assert.equal(gauge.issuedTime,'2026-10-29T14:00:00Z');
 assert.equal(gauge.observedStatus,'none');assert.equal(gauge.forecastStatus,'minor');
 assert.deepEqual(plain(gauge.crests.map(c=>[c.value,c.oldDatum])),[[32.4,true],[27.1,false]],'highest first, the old datum flagged');
 await assert.rejects(async()=>ff.parseFloodGauge(await adapterAnswer(),'OTHER1'),/incomplete/,'an answer for another gauge is refused');
 assert.throws(()=>ff.parseFloodGauge({mode:'network',records:[]},'WCHK1'),/not a gauge/);
 // A flow series takes the flow stages; units that match neither take none.
 const flow=ff.parseFloodGauge(await adapterAnswer({...nwps,observed:{...nwps.observed,primaryName:'Flow',primaryUnits:'kcfs'},forecast:{...nwps.forecast,primaryName:'Flow',primaryUnits:'kcfs'}}),'WCHK1');
 assert.equal(flow.quantity,'flow');assert.deepEqual(plain(flow.thresholds),{action:9,minor:12,moderate:20,major:31});
 assert.deepEqual(plain(flow.crests.map(c=>c.value)),[30.1],'a crest without a flow is left out');
 const odd=ff.parseFloodGauge(await adapterAnswer({...nwps,observed:{...nwps.observed,primaryUnits:'m'},forecast:{...nwps.forecast,primaryUnits:'m'}}),'WCHK1');
 assert.equal(odd.quantity,null);assert.deepEqual(plain(odd.thresholds),{action:null,minor:null,moderate:null,major:null});
 assert.equal(ff.floodCategoryAt(30,odd.thresholds),'not_defined');
});

test('the hydrograph frames a week of observations and the forecast, open to the flood stage, with NWS bands',async()=>{
 const gauge=ff.parseFloodGauge(await adapterAnswer(),'WCHK1');
 assert.deepEqual([15.99,16,17.9,18,22.99,23,28,40].map(v=>ff.floodCategoryAt(v,gauge.thresholds)),['none','action','action','minor','minor','moderate','major','major']);
 const plot=ff.floodHydrograph(gauge,NOW);
 assert.ok(plot.start>=NOW-7*24*HOUR&&plot.observed[0].time===plot.start,'the past week of observations');
 assert.equal(plot.observed.length,168);assert.equal(plot.forecast.length,21);
 assert.equal(plot.end,Date.parse('2026-11-03T18:00:00Z'));
 assert.deepEqual(plain(plot.crest),{time:Date.parse('2026-11-01T12:00:00Z'),value:19.2});
 assert.ok(plot.high>23&&plot.high<24,'opened to the next stage above the crest (moderate, 23 ft)');
 assert.ok(plot.low<9&&plot.low>8);
 assert.deepEqual(plain(plot.bands.map(b=>[b.id,b.from,Math.round(b.to*100)/100])),[['action',16,18],['minor',18,23],['moderate',23,Math.round(plot.high*100)/100]]);
 assert.deepEqual(plain(plot.ticks),[10,15,20]);
 assert.equal(plot.days[0].label,'Oct 23');assert.equal(plot.days[0].time,Date.parse('2026-10-23T05:00:00Z'),'Central daylight midnight');
 assert.ok(plot.days.some(d=>d.label==='Nov 2'&&d.time===Date.parse('2026-11-02T06:00:00Z')),'Central standard midnight after the change');
 // A gauge far below its flood stage still shows the flood stage.
 const low=ff.floodHydrograph({...gauge,forecast:[]},NOW);
 assert.ok(low.high>18&&low.high<19.5);assert.deepEqual(low.bands.map(b=>b.id),['action','minor']);
 assert.equal(ff.floodHydrograph({...gauge,observed:[],forecast:[]},NOW),null,'nothing to draw');
 // A river above its lower stages: their bands are clipped, but each stage keeps its own value.
 const high=ff.floodHydrograph({...gauge,observed:gauge.observed.map((p,i)=>({time:p.time,value:20+i/217})),forecast:[]},NOW);
 assert.ok(high.low>19&&high.low<20);
 assert.deepEqual(plain(high.bands.map(b=>[b.id,b.value,b.from===high.low])),[['minor',18,true],['moderate',23,false]],'no action band above the plot\'s floor; the flood stage keeps 18');
 assert.ok(high.bands.every(b=>b.to>b.from));
 // The crest marked is still ahead; an expired forecast marks none.
 assert.equal(ff.floodHydrograph({...gauge,forecast:gauge.forecast.map(p=>({time:p.time-9*24*HOUR,value:p.value}))},NOW).crest,null);
 assert.deepEqual(plain(ff.floodValueTicks(0.2,1.1)),[0.2,0.4,0.6,0.8,1]);assert.deepEqual(plain(ff.floodValueTicks(1,25)),[5,10,15,20,25]);
});

test('the reading gives the latest observation, the forecast crest or trend, the flood stage and the record crest',async()=>{
 const gauge=ff.parseFloodGauge(await adapterAnswer(),'WCHK1');
 assert.equal(ff.floodReading(gauge,NOW),'Observed 12.0 ft at Oct 29, 12:00 PM CDT · no flooding · NWS forecast crest 19.2 ft at Nov 1, 6:00 AM CST · minor flooding (issued Oct 29, 9:00 AM CDT) · flood stage 18.0 ft · record crest 32.4 ft on Jul 13, 1951 (old datum)');
 const falling={...gauge,forecast:gauge.forecast.map(p=>({time:p.time,value:12-p.time%7/1e9-(p.time-NOW)/HOUR/40}))};
 assert.match(ff.floodReading(falling,NOW),/NWS forecast: falling to 9\.\d ft by Nov 3, 12:00 PM CST \(issued/);
 assert.match(ff.floodReading({...gauge,forecast:[],crests:[]},NOW),/^Observed 12\.0 ft at .* · no flooding · no NWS forecast is issued for this gauge · flood stage 18\.0 ft$/);
 assert.match(ff.floodReading({...gauge,observed:[]},NOW),/^No recent observation · NWS forecast crest 19\.2 ft/);
 // A forecast whose points have all passed is expired, not ahead, even when the observations stopped earlier still.
 const stale={...gauge,observed:gauge.observed.filter(p=>p.time<NOW-3*24*HOUR),forecast:[{time:NOW-2.5*24*HOUR,value:15},{time:NOW-24*HOUR,value:17}]};
 assert.match(ff.floodReading(stale,NOW),/ · the NWS forecast has expired \(last valid Oct 28, 1:00 PM CDT\) · /);
 assert.doesNotMatch(ff.floodReading(stale,NOW),/forecast crest/);
});

test('the dock shows flood forecasts with the gauge list, the hydrograph and its reading',async()=>{
 const gauge=ff.parseFloodGauge(await adapterAnswer(),'WCHK1');
 const plot=ff.floodHydrograph(gauge,NOW);
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.water,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  onFlood:v=>calls.push(['on',v]),onFloodPick:v=>calls.push(['pick',v]),onFloodClear:()=>calls.push(['clear'])};
 const flood={on:false,state:'ready',summary:null,list:[],picked:null,gauge:null,plot:null,reading:null,gaugeLoading:false,gaugeFailed:false,url:null};
 const tool=tree=>findNode(tree,n=>n.type==='button'&&/flood forecasts$/.test(String(n.props.children)));
 let tree=h.render(h.exports.CategoryMapDock,{...base,flood});
 assert.equal(tool(tree).props.children,'Show flood forecasts');tool(tree).props.onClick();
 const on={...flood,on:true,summary:'1 forecast to flood · 1 NWS gauge in Kansas',list:[{id:'WCHK1',label:'Arkansas River at Wichita (WCHK1) · no flooding · forecast minor flooding'}]};
 tree=h.render(h.exports.CategoryMapDock,{...base,flood:on});
 assert.equal(tool(tree).props['aria-pressed'],true);
 assert.match(JSON.stringify(tree),/1 forecast to flood · 1 NWS gauge in Kansas/);
 const list=findNode(tree,n=>n.props?.label==='Kansas NWS river gauges, most severe flood category first');
 assert.equal(list.props.summary,'Gauges, most severe first (1)');list.props.onPick('WCHK1');
 for(const [state,text] of [['loading','Reading the NWS river gauges…'],['failed','did not answer; no flood state is inferred'],['held','NWS gauges show only at the present map time.']])
  assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,flood:{...on,state}})),new RegExp(text.replace(/[.?]/g,'\\$&')));
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,flood:{...on,picked:'WCHK1',gaugeLoading:true}})),/Reading the NWS hydrograph…/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,flood:{...on,picked:'WCHK1',gaugeFailed:true}})),/The NWS did not answer for this gauge/);
 const reading=ff.floodReading(gauge,NOW);
 assert.match(reading,/at Nov 1, 6:00 AM CST/,'the crest falls after Central time leaves daylight saving');
 tree=h.render(h.exports.CategoryMapDock,{...base,flood:{...on,picked:'WCHK1',gauge,plot,reading,url:ff.floodGaugePage('WCHK1')}});
 const chart=findNode(tree,n=>n.type===h.exports.FloodHydrographChart);
 assert.ok(chart,'the hydrograph is drawn');
 const figure=chart.type(chart.props);
 assert.match(figure.props['aria-label'],/^Stage hydrograph for Arkansas River at Wichita: Observed 12\.0 ft/);
 const svg=JSON.stringify(figure);
 assert.equal((svg.match(/"fill":"#ff9900","fillOpacity":0.16/g)||[]).length,1,'one minor-flood band');
 assert.match(svg,/"children":"Flood 18\.0"/);assert.match(svg,/"children":"Moderate 23\.0"/);assert.match(svg,/"strokeDasharray":"4 2"/,'the forecast dashed');
 assert.match(svg,/Stage, ft · Central time/);
 const above=ff.floodHydrograph({...gauge,observed:gauge.observed.map((p,i)=>({time:p.time,value:20+i/217})),forecast:[]},NOW);
 const aboveSvg=JSON.stringify(h.exports.FloodHydrographChart({gauge,plot:above,reading:null}));
 assert.ok(!aboveSvg.includes('"children":"Flood 18.0"')&&!aboveSvg.includes('Action'),'a stage below the plot draws no line or label');
 assert.match(aboveSvg,/"children":"Moderate 23\.0"/);
 assert.deepEqual(['Oct 23','Oct 25','Oct 27','Oct 29','Oct 31','Nov 2'].map(d=>svg.includes(`"children":"${d}"`)),[true,true,true,true,true,true]);
 assert.ok(!svg.includes('"children":"Oct 24"'),'every other day labelled over 12 days');
 assert.match(JSON.stringify(tree),/https:\/\/water\.noaa\.gov\/gauges\/WCHK1/);
 findNode(tree,n=>n.type==='button'&&n.props['aria-label']==='Clear the selected gauge').props.onClick();
 assert.deepEqual(calls,[['on',true],['pick','WCHK1'],['clear']]);
 const other=h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.geology,flood});
 assert.equal(tool(other),undefined,'only maps that offer it');
 h.dispose?.();
 assert.deepEqual(plain(maps.CATEGORY_MAPS.water.tools),['flow','flood','reviewed']);
});

test('the page reads the picked gauge, refreshes it, rings it, owns its click, and closes it with its map',()=>{
 assert.match(page,/void fetch\(floodGaugeApiPath\(floodLid\), \{ signal: controller\.signal \}\)/);
 assert.match(page,/const floodLive = buildYearCurrent && temporalQuery\.frame === OFFICIAL_CONTEXT_PRESENT_FRAME;\s*useEffect\(\(\) => \{\s*if \(!floodOn \|\| !floodLid \|\| !floodLive\) return;/,'away from the present map time nothing is read');
 assert.match(page,/const floodGaugeFeatures = floodOn && floodLive \?/,'nor listed or ringed');
 assert.match(page,/const shownFloodGauge = floodLive && floodGauge/);
 assert.match(page,/state: !floodLive \? "held" :/);assert.match(page,/picked: floodLive \? floodLid : null/);
 assert.match(page,/setFloodGauge\(parseFloodGauge\(value, floodLid\)\);/);
 assert.match(page,/const timer = setInterval\(read, FLOOD_GAUGE_REFRESH_MS\);\s*return \(\) => \{ clearInterval\(timer\); controller\.abort\(\); \};\s*\}, \[floodOn, floodLid, floodLive\]\);/);
 assert.equal(ff.FLOOD_GAUGE_REFRESH_MS,600000);
 assert.match(page,/if \(!floodGaugesWereOnRef\.current\) setOfficialContextVisible\("noaa-nwps-gauges", true\);/,'the tool shows the NWS gauges');
 assert.match(page,/\} else if \(!floodGaugesWereOnRef\.current\) setOfficialContextVisible\("noaa-nwps-gauges", false\);/,'and hides them only if it showed them');
 assert.match(page,/if \(floodOnRef\.current && renderedHits\[0\]\?\.source === OFFICIAL_CONTEXT_BY_ID\["noaa-nwps-gauges"\]\.sourceId\) \{\s*const lid = renderedHits\[0\]\.properties\?\.lid;\s*if \(typeof lid === "string"\) \{ setFloodLid\(lid\); setFloodFailed\(null\); setCategoryDockHidden\(false\); \}\s*return;/);
 assert.match(page,/syncFloodSelection\(map, point\)/);
 assert.match(page,/setOfficialContextVisible\(source\.id, on\);\s*\}\s*\/\/ Flood forecasts close with their map[^\n]*\n\s*floodGaugesWereOnRef\.current = false;\s*setFloodOn\(false\);\s*setFloodLid\(null\);/,'closes with its map, after the starters are set');
 assert.match(page,/\.\.\.\(floodOn && officialVisibility\["noaa-nwps-gauges"\] \? \[floodKey\(\)\] : \[\]\)/);
 assert.match(page,/flood=\{activeCategoryMap\.tools\?\.includes\("flood"\) \?/);
});
