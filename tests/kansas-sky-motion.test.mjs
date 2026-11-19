import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
import ts from 'typescript';

const compile=async path=>import(`data:text/javascript;base64,${Buffer.from(ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`);
const sky=await compile('app/kansas-sky.ts'),traffic=await compile('app/aviation-traffic.ts');
const epoch=Date.parse('2026-11-03T12:00:00Z');
const point=(ms=0,extra={})=>({hex:'a00001',providerId:'adsb-lol',observedAt:epoch+ms,lat:38,lon:-98,onGround:false,altBaroFt:30000,altGeomFt:31000,groundSpeedKt:400,trackDeg:90,verticalRateFpm:0,verticalRateReference:'barometric',positionMethod:'adsb_icao',timestampBasis:'provider',positionAgeS:0,...extra});
const distance=(a,b)=>{const rad=Math.PI/180,p=a.lat*rad,q=b.lat*rad,h=Math.sin((q-p)/2)**2+Math.cos(p)*Math.cos(q)*Math.sin((b.lon-a.lon)*rad/2)**2;return 12742017.6*Math.asin(Math.min(1,Math.sqrt(h)));};

test('motion never manufactures a height-reference transition or connects an impossible displacement',()=>{
 const start=point(),height=point(20000,{altGeomFt:null}),jump=point(1000,{lon:-94,lat:40});
 for(const end of [height,jump]){
  const tracks=new Map([[start.hex,[start,end]]]);
  assert.equal(sky.connected(start,end),false);
  assert.deepEqual(sky.samplesAt(tracks,(start.observedAt+end.observedAt)/2),[]);
  assert.deepEqual(sky.trailSegments(tracks,end.observedAt),[]);
  assert.equal(sky.samplesAt(tracks,start.observedAt)[0].lon,start.lon,'source observations remain exact');
  assert.equal(sky.samplesAt(tracks,end.observedAt)[0].lon,end.lon,'an anomaly does not delete the source report');
 }
 assert.equal(sky.SKY_MAX_SPEED_KT,traffic.TRAFFIC_MAX_SPEED_KT,'animation ceiling and accepted provider-speed ceiling remain aligned');
 const fast=point(60000,{lon:-97.5});assert.equal(sky.connected(start,fast),true,'the guard is not a normal-airline-speed filter');
});

test('interpolation states its sampled time and source bracket while retaining reported speed and track',()=>{
 const start=point(0,{trackDeg:80}),end=point(20000,{lon:-97.95,trackDeg:100,groundSpeedKt:450});
 const [sample]=sky.samplesAt(new Map([[start.hex,[start,end]]]),epoch+10000);
 assert.equal(sample.sampledAt,new Date(epoch+10000).toISOString());
 assert.deepEqual(sample.interpolation,{fromObservedAt:new Date(epoch).toISOString(),toObservedAt:new Date(epoch+20000).toISOString(),model:'bounded-hermite'});
 assert.equal(sample.observedAt,new Date(epoch).toISOString());
 assert.equal(sample.groundSpeedKt,400);assert.equal(sample.trackDeg,80);
 assert.ok(sample.renderedTrackDeg>80&&sample.renderedTrackDeg<100);
 assert.equal(start.lon,-98);assert.equal(end.lon,-97.95);
});

test('the shared bounded curve follows retained turn evidence and the selected path uses that same sampler',async()=>{
 const file=JSON.parse(await readFile('public/data/aviation/replays/days/2026-11-03/2026-11-03-aae1ea-p0001.json','utf8'));
 const index=file.points.findIndex(p=>p.observedAt===1793717289940),actual=file.points[index],start=file.points[index-1],end=file.points[index+1];
 const tracks=new Map([[start.hex,[start,end]]]),[sample]=sky.samplesAt(tracks,actual.observedAt);
 assert.ok(distance(sample,actual)<10,'held-out provider sample is within 10 m; old straight interpolation missed by about 44 m');
 assert.equal(sample.interpolation.model,'bounded-hermite');
 const midpoint=(start.observedAt+end.observedAt)/2,at=sky.sampleSkySpan(start,end,midpoint);
 const trail=sky.trailSegments(tracks,end.observedAt)[0],display=trail.points.find(p=>p.observedAt===midpoint);
 assert.ok(display,'curve tessellation includes the midpoint');assert.equal(display.lon,at.lon);assert.equal(display.lat,at.lat);
 const journey=sky.selectedJourney([start,end],actual.observedAt);
 assert.equal(journey[0].points.at(-1).lon,sample.lon);assert.equal(journey[1].points[0].lat,sample.lat);
 assert.equal(trail.points[0],start);assert.equal(trail.points.at(-1),end,'source endpoints retain their identity');
});

test('inconsistent, missing, stationary and ground velocity inputs use a bounded geodesic without extrapolation',()=>{
 const start=point(),end=point(20000,{lon:-97.95});
 for(const change of [{groundSpeedKt:null},{groundSpeedKt:1501},{groundSpeedKt:-1},{groundSpeedKt:1500},{groundSpeedKt:800},{trackDeg:null},{trackDeg:361},{trackDeg:NaN},{trackDeg:270},{trackDeg:0},{groundSpeedKt:0},{onGround:true}]){
  const a={...start,...change},b={...end,...change},sample=sky.sampleSkySpan(a,b,epoch+10000);
  assert.equal(sample.interpolation.model,'great-circle',JSON.stringify(change));
  assert.ok(sample.lon>a.lon&&sample.lon<b.lon);assert.ok(Number.isFinite(sample.lat));
  assert.equal(sky.sampleSkySpan(a,b,epoch-1),null);assert.equal(sky.sampleSkySpan(a,b,epoch+20001),null);
 }
 const stationary=sky.sampleSkySpan(start,point(20000),epoch+10000);
 assert.equal(stationary.lon,start.lon);assert.equal(stationary.lat,start.lat);assert.equal(stationary.renderedTrackDeg,null);
});

test('bounded curves keep their control hull, source endpoints and display budget',()=>{
 const start=point(0,{trackDeg:60}),end=point(20000,{lon:-97.95,trackDeg:120});
 let previousLon=start.lon;
 for(let i=0;i<=100;i++){
  const sample=sky.sampleSkySpan(start,end,epoch+i*200);
  assert.ok(sample.lon>=previousLon-1e-12&&sample.lon<=end.lon+1e-12);
  assert.ok(distance({...sample,lat:start.lat},sample)<=distance(start,end)*.25+1);
  previousLon=sample.lon;
 }
 const tracks=new Map(Array.from({length:3000},(_,i)=>{const hex=i.toString(16).padStart(6,'0');return[hex,[{...start,hex},{...end,hex}]];}));
 const trails=sky.trailSegments(tracks,epoch+20000);
 assert.equal(trails.length,3000);assert.ok(trails.reduce((sum,trail)=>sum+trail.points.length,0)<=sky.SKY_MAX_TRAIL_POINTS);
});

test('selected geometry reuse never reuses the cursor split or a replaced source interval',()=>{
 const start=point(),end=point(20000,{lon:-97.95}),points=Object.freeze([start,end]);
 const first=sky.selectedJourney(points,epoch+5000),second=sky.selectedJourney(points,epoch+15000);
 assert.equal(first[0].points.at(-1).observedAt,epoch+5000);assert.equal(second[0].points.at(-1).observedAt,epoch+15000);
 assert.notEqual(first[0].points.at(-1).lon,second[0].points.at(-1).lon);
 const replacement=Object.freeze([start,{...end,lon:-97.96}]);
 const changed=sky.selectedJourney(replacement,epoch+15000);
 assert.notEqual(changed[0].points.at(-1).lon,second[0].points.at(-1).lon);
 assert.equal(sky.selectedJourney(points,epoch+15000)[0].points.at(-1).lon,second[0].points.at(-1).lon);
});

test('ground trace heading and live true heading remain distinct from ground track',()=>{
 const code=String.raw`import importlib.util,gzip,json
spec=importlib.util.spec_from_file_location('sky','scripts/prepare-kansas-sky-replay.py');sky=importlib.util.module_from_spec(spec);spec.loader.exec_module(sky)
raw=gzip.compress(json.dumps({'icao':'a00001','timestamp':1793664000,'trace':[[100,38,-98,'ground',0,123,0,None,None,'adsb_icao',None,None,None,None]]}).encode())
p=sky.prepare(raw,'https://github.com/adsblol/globe_history_2026/releases/download/v2026.11.03/trace.tar','traces/01/trace_full_a00001.json',all_segments=True,utc_day='2026-11-03')['points'][0]
assert p['trackDeg'] is None,p
assert p['trueHeadingDeg']==123,p
`;
 execFileSync('python3',['-c',code]);
 const [sample]=traffic.parseTraffic({now:epoch/1000,ac:[{hex:'a00001',lon:-98,lat:38,seen_pos:0,alt_baro:'ground',track:90,true_heading:123}]},epoch).records;
 assert.equal(sample.trackDeg,90);assert.equal(sample.trueHeadingDeg,123);
});
