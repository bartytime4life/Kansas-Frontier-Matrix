import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {resolve,dirname} from 'node:path';
import {createHash} from 'node:crypto';
import ts from 'typescript';

const fixture = name => readFileSync(`tests/fixtures/iem/${name}`,'utf8');
function load(path, overrides={}, cache=new Map()) {
  path=resolve(path);
  if(cache.has(path)) return cache.get(path);
  const exports={};cache.set(path,exports);
  const code=ts.transpileModule(readFileSync(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
  new Function('exports','require',code)(exports,name=>name in overrides?overrides[name]:load(resolve(dirname(path),name+'.ts'),overrides,cache));
  return exports;
}
const gdd=load('app/growing-degree-days.ts');
const stationModule=load('app/kansas-stations.ts');
const catalog=JSON.parse(fixture('ks-asos.geojson'));
const stations=stationModule.parseKansasStations(catalog);
const expected={SLN:{file:'sln-2024.csv',gdd:4426,precip:15.81,traces:28,tz:'America/Chicago'},GLD:{file:'gld-2024.csv',gdd:3749,precip:8.28,traces:17,tz:'America/Denver'}};
const csv=(rows,header='station,day,max_temp_f,min_temp_f,precip_in,network')=>header+'\n'+rows+'\n';
const contract={station:'SLN',start:'2024-04-01',end:'2024-10-31'};

test('captured real-source fixture bytes match retrieval receipts',()=>{
 for(const receipt of JSON.parse(fixture('provenance.json'))) assert.equal(createHash('sha256').update(fixture(receipt.file)).digest('hex'),receipt.sha256);
});
for(const [id,e] of Object.entries(expected)) test(`${id}: real 214-day sample agrees with independent decimal totals and timezone`,()=>{
 const days=gdd.parseDailyCsv(fixture(e.file),{...contract,station:id});
 assert.equal(days.length,214);
 assert.deepEqual(gdd.seasonDegreeDays(days,2024),{degreeDays:e.gdd,daysRead:214,daysMissing:0});
 assert.deepEqual(gdd.seasonRainfall(days,2024),{inches:e.precip,daysRead:214,daysMissing:0,traceDays:e.traces});
 const s=stations.find(s=>s.id===id);
 assert.equal(s.tzname,e.tz);assert.equal(gdd.nearestStation(stations,s.lon,s.lat).id,id);
});
test('trace is not a measured depth, zero rain or a missing observation',()=>{
 const days=gdd.seasonDates(2024).map(day=>({day,maxF:70,minF:50,precipIn:0.0001}));
 assert.deepEqual(gdd.seasonRainfall(days,2024),{inches:0,daysRead:214,daysMissing:0,traceDays:214});
 assert.match(gdd.rainLine({state:'ready',year:2024,rainInches:0,rainDaysMissing:0,rainTraceDays:214}),/trace on 214 days/);
});
test('published corn-method examples retain Fahrenheit arithmetic and reject inconsistent or nonfinite temperatures',()=>{
 assert.equal(gdd.dailyDegreeDays(80,55),17.5);assert.equal(gdd.dailyDegreeDays(90,72),29);assert.equal(gdd.dailyDegreeDays(68,41),9);
 assert.equal(gdd.dailyDegreeDays(30,40),null);assert.equal(gdd.dailyDegreeDays(NaN,40),null);assert.equal(gdd.dailyDegreeDays(Infinity,40),null);
});
test('missing sentinels, negative precipitation and impossible pairs cannot turn into valid totals',()=>{
 const rows=gdd.parseDailyCsv(csv('SLN,2024-04-01,None,M,M,KS_ASOS\nSLN,2024-04-02,,,0.0,KS_ASOS\nSLN,2024-04-03,30,40,-1,KS_ASOS'),contract);
 assert.equal(gdd.seasonDegreeDays(rows,2024).daysRead,0);
 assert.deepEqual(gdd.seasonRainfall(rows,2024),{inches:0,daysRead:1,daysMissing:213,traceDays:0});
 const closed=gdd.parseDailyCsv(fixture('closed-1k1-2024.csv'),{station:'1K1',start:'2024-04-01',end:'2024-04-03'});
 assert.equal(gdd.seasonDegreeDays(closed,2024).daysRead,0);
});
test('wrong station, network, date, duplicate dates and malformed rows fail closed',()=>{
 for(const row of ['GLD,2024-04-01,80,60,0,KS_ASOS','SLN,2024-04-01,80,60,0,IA_ASOS','SLN,2024-03-31,80,60,0,KS_ASOS','SLN,2024-04-31,80,60,0,KS_ASOS','SLN,2024-04-01,80,60,0,KS_ASOS,extra','SLN,2024-04-01,80,60,0,KS_ASOS\nSLN,2024-04-01,80,60,0,KS_ASOS']) assert.throws(()=>gdd.parseDailyCsv(csv(row),contract));
 assert.throws(()=>gdd.parseDailyCsv('station,day,max_temp_f,min_temp_f\nSLN,2024-04-01,80,60',contract));
});
test('station archive dates exclude retired/newer sites only for nonoverlapping years; malformed catalogs fail closed',async()=>{
 const module=load('app/kansas-stations.ts',{'./api/event-atlas/upstream':{boundedFetch:async()=>({text:()=>JSON.stringify(catalog)})}});
 const active=await module.kansasStations('2024-04-01','2024-10-31');
 assert.ok(!active.some(s=>s.id==='1K1'));
 assert.ok((await module.kansasStations('2020-04-01','2020-10-31')).some(s=>s.id==='1K1'));
 const benton=stations.find(s=>s.id==='1K1');
 assert.notEqual(gdd.nearestStation(active,benton.lon,benton.lat).id,'1K1');
 assert.ok(!(await module.kansasStations('2000-04-01','2000-10-31')).some(s=>s.id==='13K'));
 for(const props of [{network:'IA_ASOS'},{tzname:'UTC'},{archive_begin:'2024-02-30'}]) assert.throws(()=>stationModule.parseKansasStations({...catalog,features:[{...catalog.features[0],properties:{...catalog.features[0].properties,...props}}]}));
});
test('station-local cutoff conservatively excludes incomplete days across Central, Mountain and DST transitions',()=>{
 assert.equal(gdd.lastCompleteStationDate(new Date('2024-07-01T06:30:00Z'),'America/Chicago'),'2024-06-29');
 assert.equal(gdd.lastCompleteStationDate(new Date('2024-07-01T07:30:00Z'),'America/Chicago'),'2024-06-30');
 assert.equal(gdd.lastCompleteStationDate(new Date('2024-07-01T07:30:00Z'),'America/Denver'),'2024-06-29');
 assert.equal(gdd.lastCompleteStationDate(new Date('2024-03-10T08:30:00Z'),'America/Chicago'),'2024-03-09');
 assert.equal(gdd.lastCompleteStationDate(new Date('2024-11-03T07:30:00Z'),'America/Chicago'),'2024-11-01');
 assert.equal(gdd.lastCompleteStationDate(new Date('2024-11-03T08:30:00Z'),'America/Chicago'),'2024-11-02');
 assert.deepEqual(gdd.seasonDegreeDays([],2024,'2024-03-31'),{degreeDays:0,daysRead:0,daysMissing:0});
 assert.equal(gdd.seasonDegreeDays([],2024,'2024-04-02').daysMissing,2);
});
function routeWith(daily, stationPayload=catalog) {
 const calls=[];
 const route=load('app/api/farming/degree-days/route.ts',{
  './api/event-atlas/upstream':{boundedFetch:async()=>({text:()=>JSON.stringify(stationPayload)})},
  '../../../iem-daily-source':{fetchDailySummary:async url=>{calls.push(url);if(daily instanceof Error)throw daily;return daily;}}
 });
 return {route,calls};
}
const request=(q='lon=-97.6522&lat=38.791&year=2024&v=2')=>new Request('https://kfm.test/api/farming/degree-days?'+q);
test('route replays real fixtures, binds source request identity and caches only complete historical results',async()=>{
 const {route,calls}=routeWith(fixture('sln-2024.csv'));
 const response=await route.GET(request()), body=await response.json();
 assert.equal(response.status,200);assert.equal(body.degreeDays,4426);assert.equal(body.rainInches,15.81);assert.equal(body.rainTraceDays,28);
 assert.equal(body.station.id,'SLN');assert.equal(body.daysPending,0);assert.equal(body.completedThrough,'2024-10-31');
 assert.equal(gdd.validDegreeDays(body,-97.6522,38.791,2024),true);
 const url=new URL(calls[0]);assert.equal(url.searchParams.get('stations'),'SLN');assert.equal(url.searchParams.get('var'),'max_temp_f,min_temp_f,precip_in');assert.equal(url.searchParams.get('na'),'M');
 assert.equal(response.headers.get('cache-control'),'public, max-age=86400, s-maxage=86400');
 assert.match(gdd.GDD_API_PATH(-97.6522,38.791,2024),/&v=2$/);
});
test('rain-only data is shown; absent dates and provider failures never manufacture complete readings',async()=>{
 const {route}=routeWith(csv('SLN,2024-04-01,M,M,0.1,KS_ASOS'));
 const response=await route.GET(request()), body=await response.json();
 assert.equal(body.state,'ready');assert.equal(body.degreeDays,null);assert.equal(body.rainInches,0.1);assert.equal(body.daysMissing,214);
 assert.equal(gdd.validDegreeDays(body,-97.6522,38.791,2024),true);assert.match(gdd.degreeDaysLine(body),/No valid temperature/);
 assert.match(gdd.rainLine(body),/^Partial:/);assert.equal(response.headers.get('cache-control'),'no-store');
 for(const payload of [new Error('HTTP 503'),'<html>outage</html>',csv('GLD,2024-04-01,80,60,0,KS_ASOS')]){const r=await routeWith(payload).route.GET(request());assert.equal(r.status,502);assert.equal(r.headers.get('cache-control'),'no-store');}
 const missing=await routeWith('station,day,max_temp_f,min_temp_f,precip_in,network\n').route.GET(request());
 const none=await missing.json();assert.equal(none.state,'none');assert.equal(none.degreeDays,null);assert.equal(none.rainInches,null);assert.equal(missing.headers.get('cache-control'),'no-store');
});
test('legacy responses remain readable without pretending to contain precipitation; inconsistent caches are rejected',()=>{
 const old={lon:-97.6522,lat:38.791,year:2024,retrievedAt:'2026-10-30T17:43:01.727Z',state:'ready',station:{id:'SLN',name:'SALINA',km:0},degreeDays:4426,daysRead:214,daysMissing:0};
 assert.ok(gdd.validDegreeDays(old,old.lon,old.lat,old.year));assert.match(gdd.rainLine(old),/unavailable/);
 for(const patch of [{degreeDays:NaN},{degreeDays:Infinity},{daysMissing:-1},{daysRead:2},{rainInches:1},{station:null},{retrievedAt:'x'},{rainInches:Infinity,rainDaysMissing:0}]) assert.equal(gdd.validDegreeDays({...old,...patch},old.lon,old.lat,old.year),false);
});
test('daily request queue is sequential, deduplicated, bounded and recovers after failures',async()=>{
 const {createDailyReader}=load('app/iem-daily-source.ts');let time=0;const starts=[],delays=[];
 const read=createDailyReader(async url=>{starts.push({url,time});if(url==='bad')throw new Error('outage');return url;},()=>time,async ms=>{delays.push(ms);time+=ms;});
 const a=read('a'),b=read('b');assert.equal(read('a'),a);assert.deepEqual(await Promise.all([a,b]),['a','b']);assert.deepEqual(starts,[{url:'a',time:0},{url:'b',time:2100}]);
 await assert.rejects(read('bad'));assert.equal(await read('b'),'b');assert.ok(delays.every(d=>d>=2100));
 let release;const gate=new Promise(r=>{release=r;});
 const blocked=createDailyReader(async url=>{await gate;return url;},()=>time,async ms=>{time+=ms;});
 const pending=['1','2','3','4'].map(x=>blocked(x));await assert.rejects(blocked('5'),/queue is full/);
 release();assert.deepEqual(await Promise.all(pending),['1','2','3','4']);
});

test('in-progress seasons count due gaps separately from pending dates and never cache',async t=>{
 t.mock.timers.enable({apis:['Date'],now:Date.parse('2024-04-03T12:00:00Z')});
 try {
  const {route,calls}=routeWith(csv('SLN,2024-04-01,80,60,0.1,KS_ASOS'));
  const r=await route.GET(request()),body=await r.json();
  assert.equal(body.completedThrough,'2024-04-02');assert.equal(body.daysRead,1);assert.equal(body.daysMissing,1);assert.equal(body.daysPending,212);
  assert.equal(r.headers.get('cache-control'),'no-store');assert.equal(new URL(calls[0]).searchParams.get('day2'),'2');
  assert.match(gdd.degreeDaysLine(body),/^Partial:/);assert.match(gdd.degreeDaysLine(body),/212 days not yet due/);
  assert.ok(gdd.validDegreeDays(body,body.lon,body.lat,body.year));
  assert.equal(gdd.validDegreeDays({...body,completedThrough:'2024-10-31'},body.lon,body.lat,body.year),false);
 } finally { t.mock.timers.reset(); }
});
test('preseason makes no daily request; no eligible station and wholly missing observations remain distinct from zero',async t=>{
 t.mock.timers.enable({apis:['Date'],now:Date.parse('2024-03-20T12:00:00Z')});
 try {
  const {route,calls}=routeWith(new Error('must not fetch'));
  const r=await route.GET(request()),body=await r.json();assert.equal(calls.length,0);assert.equal(body.state,'none');assert.equal(body.degreeDays,null);assert.equal(body.daysPending,214);assert.equal(body.daysMissing,0);
  assert.ok(gdd.validDegreeDays(body,body.lon,body.lat,body.year));assert.equal(r.headers.get('cache-control'),'no-store');
 } finally { t.mock.timers.reset(); }
 const onlySalina={...catalog,features:catalog.features.filter(f=>f.id==='SLN')};
 const {route,calls}=routeWith(new Error('must not fetch'),onlySalina);
 const r=await route.GET(request('lon=-101.5&lat=37&year=2024&v=2')),body=await r.json();
 assert.equal(body.station,null);assert.equal(body.state,'none');assert.equal(body.degreeDays,null);assert.equal(calls.length,0);assert.equal(r.headers.get('cache-control'),'no-store');
});
