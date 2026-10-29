import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';
async function compile(file, deps = {}) {
  const exports = {};
  new Function('exports', 'require', ts.transpileModule(await readFile(file, 'utf8'), { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText)(exports, name => {
    if (!(name in deps)) throw new Error(`Unexpected import ${name}`); return deps[name];
  }); return exports;
}
const civic = await compile('app/civic-districts.ts');
const history = await compile('app/civic-history.ts', { './civic-districts': civic });
const bounded = await compile('app/bounded-json.ts');
const reader = await compile('app/api/live-context/civic-history.ts', { '../../bounded-json': bounded, '../../civic-history': history, './civic-districts': {} });
const calendar = await compile('app/calendar-sweep.ts');
const maps = await compile('app/category-maps.ts');
const now = new Date('2026-10-29T00:00:00Z');
// Deliberately synthetic boxes, never used as deployed district geometry.
const rawFor = congress => {
  const plan = history.civicHistoryPlan(congress);
  return { type: 'FeatureCollection', features: plan.districts.map(district => ({ type: 'Feature', properties: {
    statename: 'Kansas', district: String(district), startcong: String(plan.first), endcong: String(plan.last),
    id: `020${String(plan.first).padStart(3,'0')}${String(plan.last).padStart(3,'0')}${String(district).padStart(3,'0')}`,
    member: 'UNTRUSTED_MEMBER', name: '<script>unsafe</script>',
  }, geometry: { type: 'Polygon', coordinates: [[[-99,38],[-98,38],[-98,39],[-99,39],[-99,38]]] } })) };
};
test('Congress dates respect statehood, March 4 terms, the 1935 transition and the future coverage cutoff', () => {
  for (const [day, expected] of [['1861-01-28',null],['1861-01-29',36],['1861-03-03',36],['1861-03-04',37],['1875-03-03',43],['1875-03-04',44],['1933-03-03',72],['1933-03-04',73],['1935-01-02',73],['1935-01-03',74],['2025-01-02',118],['2025-01-03',119],['2027-01-02',119],['2027-01-03',null],['1900-02-29',null],['abc',null]]) assert.equal(history.civicCongressForDay(day), expected, day);
  assert.throws(() => history.civicTermStart(35)); assert.throws(() => history.civicTermStart(120.5));
});
test('one pinned plan covers every Kansas state Congress without filling at-large gaps', () => {
  for (let n=36;n<=119;n++) assert.equal(history.CIVIC_HISTORY_PLANS.filter(p=>p.first<=n&&n<=p.last).length,1);
  for (const n of [36,43,48,53,59]) assert.ok(history.civicHistoryPlan(n).districts.includes(0));
  for (const n of [44,47,49,52,60,119]) assert.ok(!history.civicHistoryPlan(n).districts.includes(0));
  assert.equal(history.civicHistoryPlan(43).districts.length,1,'A statewide constituency is not a seat count');
  assert.equal(history.civicHistoryPlan(48).districts.length,4);
  assert.equal(history.civicHistoryPlan(60).districts.length,8);
  for (const plan of history.CIVIC_HISTORY_PLANS) { assert.match(plan.commit,/^[a-f0-9]{40}$/); assert.match(plan.sha256,/^[a-f0-9]{64}$/); assert.match(history.civicHistoryRawUrl(plan),/^https:\/\/raw\.githubusercontent\.com\/JeffreyBLewis\/congressional-district-boundaries\/[a-f0-9]{40}\/(GeoJson\/)?Kansas_\d+_to_\d+\.geojson$/); }
});
test('historical records retain exact plan identity and temporal provenance while dropping member and HTML fields', () => {
  for (let n=36;n<119;n++) {
    const day=history.civicTermStart(n), result=history.parseCivicHistory(rawFor(n),day,now);
    assert.equal(result.sourceDay,day); assert.equal(result.upstreamUpdatedAt,null);
    assert.ok(result.data.features.every(f=>f.properties.congressNumber===n&&f.properties.sourceSha256===history.civicHistoryPlan(n).sha256));
    assert.ok(!JSON.stringify(result).includes('UNTRUSTED_MEMBER')); assert.ok(!JSON.stringify(result).includes('<script>'));
    assert.match(result.license,/Copyright \(c\) 2013-2018 Jeffrey B. Lewis/);
  }
  assert.equal(history.parseCivicHistory(rawFor(43),'1873-03-04',now).data.features[0].properties.atLargeOnly,true);
  assert.equal(history.parseCivicHistory(rawFor(53),'1893-03-04',now).data.features[0].properties.atLargeOnly,false);
});
test('wrong state, plan, identity, datum, duplicated or missing districts and malformed geometry fail closed', () => {
  for(const mutate of [r=>r.features.pop(),r=>r.features.push(r.features[0]),r=>{r.features[1]=r.features[0]},r=>{r.features[0].properties.statename='Missouri'},r=>{r.features[0].properties.startcong='54'},r=>{r.features[0].properties.id='wrong'},r=>{r.crs={type:'name',properties:{name:'EPSG:3857'}}},r=>{r.features[0].geometry.coordinates[0][0]=[-120,38]}]) {
    const raw=rawFor(53);mutate(raw);assert.throws(()=>history.parseCivicHistory(raw,'1893-03-04',now));
  }
  assert.throws(()=>history.parseCivicHistory(rawFor(43),'1854-01-01',now));
});
test('fixed historical reader rejects redirects, oversize responses, hash changes and unsupported dates', async () => {
  for(const response of [new Response('',{status:302,headers:{location:'http://127.0.0.1'}}),new Response('',{status:500}),new Response(' '.repeat(2*1024*1024+1)),new Response('{}',{headers:{'content-length':String(2*1024*1024+1)}}),Response.json(rawFor(43))]) {
    let calls=0;const read=reader.createCivicHistoryReader(async (url,options)=>{calls++;assert.match(url,/a72f5836d0de4ad5aa94a18b6b725b46bf71b39e/);assert.equal(options.redirect,'manual');return response},()=>now.getTime());
    await assert.rejects(read('1873-03-04'),/unavailable/);await assert.rejects(read('1873-03-04'),/unavailable/);assert.equal(calls,1);
  }
  let calls=0;const read=reader.createCivicHistoryReader(async()=>{calls++;throw new Error('must not fetch')},()=>now.getTime(),async()=>({feed:civic.CIVIC_ID}));
  for(const day of ['1854-01-01','2027-01-03','2026-10-30','1900-02-29'])await assert.rejects(read(day),/supported historical date/);
  assert.equal(calls,0);assert.equal((await read('2025-01-03')).sourceDay,'2025-01-03');
});
test('exact checked dates gate annual and calendar rendering; stale plans cannot leak into other frames', () => {
  const visible=(frame,day,checked,build=true)=>history.civicFrameVisible(true,frame,2026,'2026-10-29',day,checked,build);
  assert.equal(visible(1900,null,'1900-01-01'),true);assert.equal(visible(1900,null,'1899-01-01'),false);
  assert.equal(visible(1861,null,'1861-01-29'),false);assert.equal(visible(1861,'1861-01-29','1861-01-29'),true);
  assert.equal(visible(1860,null,'1861-01-29'),false);assert.equal(visible(2026,null,undefined),true);
  assert.equal(visible(2026,null,'2025-01-03'),false);assert.equal(visible(2026,'2026-01-01',undefined),false);
  assert.equal(visible(1900,'1900-02-01','1900-01-01'),false);assert.equal(visible(1900,null,'1900-01-01',false),false);
  assert.equal(history.civicFrameVisible(true,2027,2027,'2027-01-03',null,undefined,true),false);
  assert.ok(calendar.calendarArchiveFeeds({[civic.CIVIC_ID]:true},'1861-01-29').includes(civic.CIVIC_ID));
});
const page = await readFile('app/page.tsx','utf8');
function pageFunction(start,end,deps,name) {
  const code=page.slice(page.indexOf(start),page.indexOf(end,page.indexOf(start)));
  const js=ts.transpileModule(code,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
  return new Function(...Object.keys(deps),js+`;return ${name}`)(...Object.values(deps));
}
test('actual archive loader rejects late responses after a newer Congress date replaces the request', async () => {
  const ref=current=>({current}), requests=new Map(), days=ref({}), payloads=ref({}), archives=ref({}), queued=[];
  let states={};const setState=fn=>{states=fn(states)};
  const load=pageFunction('  const loadOfficialArchiveDay =','  const returnOfficialSourceToCurrent',{
    useCallback:fn=>fn,CIVIC_ID:civic.CIVIC_ID,civicCongressForDay:history.civicCongressForDay,currentUtcDay:()=> '2026-10-29',calendarArchiveLoads:ref(new Map()),
    officialArchiveDaysRef:days,officialArchivePayloadsRef:archives,officialPayloadsRef:payloads,officialRequestsRef:ref(requests),
    setOfficialArchiveDays(){},setOfficialPayloads(){},setOfficialStates:setState,setOfficialErrors(){},setOfficialReadPhases(){},setEarthquakeArchiveFrameIndex(){},setSmokeArchiveFrameIndex(){},
    OFFICIAL_CONTEXT_BY_ID:{[civic.CIVIC_ID]:{apiPath:'/api/live-context?feed=census-congress-119',shortTitle:'Districts'}},
    layerJsonReadsRef:ref({read:(url,options)=>new Promise(resolve=>queued.push({url,options,resolve}))}),validLayerPayload:()=>true,cancelSmokePlayback(){},announce(){},
  },'loadOfficialArchiveDay');
  const first=load(civic.CIVIC_ID,'1873-03-04'),second=load(civic.CIVIC_ID,'1875-03-04');
  assert.equal(queued.length,2);assert.equal(queued[0].options.signal.aborted,true);assert.equal(payloads.current[civic.CIVIC_ID],undefined);
  queued[1].resolve({response:{ok:true},body:history.parseCivicHistory(rawFor(44),'1875-03-04',now)});await second;
  queued[0].resolve({response:{ok:true},body:history.parseCivicHistory(rawFor(43),'1873-03-04',now)});await first;
  assert.equal(days.current[civic.CIVIC_ID],'1875-03-04');assert.equal(payloads.current[civic.CIVIC_ID].sourceDay,'1875-03-04');assert.equal(states[civic.CIVIC_ID],'ready');
});
test('date route validates before acquisition and historical requests remain no-store',async()=>{
  const calls=[];const route=await compile('app/api/live-context/route.ts',{
    './civic-history':{readCivicHistory:async day=>{calls.push(day);return history.parseCivicHistory(rawFor(43),day,now)}},'../../civic-history':history,'./civic-districts':{},'./deflock':{},
    'cloudflare:workers':{env:{}},'next/server':{NextResponse:Response},'../../bounded-json':bounded,'../../event-atlas':{eventDay:day=>/^\d{4}-\d{2}-\d{2}$/.test(day)},'../event-atlas/upstream':{},'../../county-baseline':{},'../../fema-declarations':{},'@mapbox/vector-tile':{},pbf:{},
  });
  const req=query=>({nextUrl:new URL('https://kfm.invalid/api/live-context?feed=census-congress-119'+query),signal:new AbortController().signal});
  for(const q of ['&day=1854-01-01','&day=1900-02-29','&day=2027-01-03','&day=1873-03-04&day=1875-03-04','&day=1873-03-04&url=http://localhost'])assert.equal((await route.GET(req(q))).status,400);
  assert.equal(calls.length,0);const response=await route.GET(req('&day=1873-03-04'));assert.equal(response.status,200);assert.equal(response.headers.get('cache-control'),'no-store');assert.equal((await response.json()).sourceDay,'1873-03-04');
});
test('Congress picker, source download and variable constituency list work without inventing seat totals',async()=>{
  const h=await componentHarness('app/category-map-dock.tsx',{}),picked=[];
  const props={look:maps.categoryMap('government'),mode:'2d',depth:1,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},onReset(){},onLayers(){},onClose(){},
    civic:{visible:true,state:'ready',day:'1873-03-04',congress:43,options:[{value:43,label:'Congress 43'},{value:44,label:'Congress 44'}],items:[{id:'at-large',label:'Kansas statewide at-large constituency'}]},onCivicCongress:n=>picked.push(n),onCivicPick(){}};
  const tree=h.render(h.exports.CategoryMapDock,props),select=findNode(tree,n=>n.type==='select'&&n.props['aria-label']==='Choose Congress');
  select.props.onChange({target:{value:'44'}});select.props.onChange({target:{value:'120'}});assert.deepEqual(picked,[44]);
  assert.ok(findNode(tree,n=>n.type==='a'&&n.props.href==='/api/live-context?feed=census-congress-119&day=1873-03-04'));
  const text=JSON.stringify(tree);assert.match(text,/shapes do not count seats/);assert.match(text,/territorial delegate geometry is unverified/);
});
test('redistributed historical geometry retains the full MIT notice',async()=>{
  assert.equal(await readFile('public/civic-history-license.txt','utf8'),history.CIVIC_HISTORY_LICENSE);
});

test('synchronous provider failures release single-flight state after the cooldown',async()=>{
 let time=now.getTime(),calls=0;
 const read=reader.createCivicHistoryReader(()=>{calls++;throw new Error('sync failure')},()=>time);
 await assert.rejects(read('1873-03-04'),/unavailable/);assert.equal(calls,1);
 time+=60_000;await assert.rejects(read('1873-03-04'),/unavailable/);assert.equal(calls,2);
});

test('actual historical selection records preserve their year, author and immutable source link',()=>{
 const properties=history.parseCivicHistory(rawFor(43),'1873-03-04',now).data.features[0].properties;
 const str=(p,k)=>typeof p[k]==='string'?p[k]:null;
 const time=pageFunction('const officialContextTime =','const drawerTimestamp', {CIVIC_ID:civic.CIVIC_ID,stringContextProperty:str},'officialContextTime');
 const summary=pageFunction('const officialContextSummary =','const officialContextTime', {CIVIC_ID:civic.CIVIC_ID,CIVIC_LIMITATION:civic.CIVIC_LIMITATION,CIVIC_HISTORY_LIMITATION:history.CIVIC_HISTORY_LIMITATION,stringContextProperty:str},'officialContextSummary');
 const select=pageFunction('const buildBasemapContext =','const parseNumber =',{
  CIVIC_ID:civic.CIVIC_ID,CIVIC_SERVICE:civic.CIVIC_SERVICE,CIVIC_LIMITATION:civic.CIVIC_LIMITATION,CIVIC_HISTORY_CREDIT:history.CIVIC_HISTORY_CREDIT,CIVIC_HISTORY_LIMITATION:history.CIVIC_HISTORY_LIMITATION,
  civicSourceForRecord:history.civicSourceForRecord,OFFICIAL_CONTEXT_BY_SOURCE_ID:{[civic.CIVIC_SOURCE.sourceId]:civic.CIVIC_SOURCE},BASEMAP_CONTEXT_LAYER:{},officialContextTime:time,officialContextSummary:summary,stringContextProperty:str,drawerArtifactAttributes:()=>[],
 },'buildBasemapContext');
 const selected=select({...history.parseCivicHistory(rawFor(43),'1873-03-04',now).data.features[0],source:civic.CIVIC_SOURCE.sourceId},-99,38);
 assert.equal(selected.properties.year,1873);assert.equal(selected.properties.sourceOrganization,history.CIVIC_HISTORY_CREDIT);
 assert.match(selected.properties.temporalScope,/1873-03-04/);assert.match(history.civicSourceForRecord(properties).sourceUrl,/a72f5836d0de4ad5aa94a18b6b725b46bf71b39e/);
 assert.equal(history.civicSourceForRecord({congressNumber:119}).sourceUrl,civic.CIVIC_SERVICE);
 assert.equal(history.civicSourceForRecord({congressNumber:120}),civic.CIVIC_SOURCE);
 assert.match(selected.properties.summary,/Scholarly historical reconstruction/);
});
test('the no-date API request also refuses an unsupported Congress instead of serving an expired default',async()=>{
 let calls=0;
 const route=await compile('app/api/live-context/route.ts',{
  './civic-history':{},'../../civic-history':{civicCongressForDay:()=>null},'./civic-districts':{readCivicDistricts:async()=>{calls++;throw Error('expired default')}},'./deflock':{},
  'cloudflare:workers':{env:{}},'next/server':{NextResponse:Response},'../../bounded-json':bounded,'../../event-atlas':{},'../event-atlas/upstream':{},'../../county-baseline':{},'../../fema-declarations':{},'@mapbox/vector-tile':{},pbf:{},
 });
 const response=await route.GET({nextUrl:new URL('https://kfm.invalid/api/live-context?feed=census-congress-119')});
 assert.equal(response.status,400);assert.equal(calls,0);
});
