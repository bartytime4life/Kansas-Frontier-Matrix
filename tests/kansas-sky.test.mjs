import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile, mkdtemp, rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import ts from 'typescript';
const compile=async path=>import(`data:text/javascript;base64,${Buffer.from(ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`);
const sky=await compile('app/kansas-sky.ts'),traffic=await compile('app/aviation-traffic.ts');
const epoch=Date.parse('2026-11-03T12:00:00Z');
const point=(ms=0,extra={})=>({hex:'a00001',callsign:'TEST',registration:null,type:null,category:null,lat:38,lon:-98,onGround:false,altBaroFt:30000,altGeomFt:31000,groundSpeedKt:400,trackDeg:350,verticalRateFpm:0,squawk:null,emergency:null,military:false,positionAgeS:0,observedAt:epoch+ms,providerId:'adsb-lol',...extra});
const envelope=(ms=0,points=[point(ms)])=>({retrievedAt:new Date(epoch+ms).toISOString(),provider:traffic.TRAFFIC_PROVIDERS[0],records:points.map(p=>({...p,observedAt:new Date(p.observedAt).toISOString()})),dropped:0,limitation:'test',evidenceRole:'EXTERNAL_CONTEXT_ONLY'});

test('session ingests observation time, deduplicates, sorts out-of-order samples and never relabels retrieval as observation',()=>{
 const b=new sky.SkyBuffer();b.ingest(envelope(20000,[point(10000)]));b.ingest(envelope(20000,[point(0)]));b.ingest(envelope(20000,[point(10000,{lon:-99})]));
 assert.deepEqual(b.range(),[epoch,epoch+10000]); assert.equal(b.tracks().get('a00001').length,2);assert.equal(b.tracks().get('a00001')[1].lon,-98);
 b.ingest({...envelope(20000),retrievedAt:'bad'});assert.equal(b.tracks().get('a00001').length,2);
});
test('replay interpolates only bracketing observations, separates the rendered turn and leaves optional instruments unknown',()=>{
 const tracks=new Map([['a00001',[point(),point(20000,{lat:38.04,trackDeg:10,altBaroFt:null})]]]);
 const [sample]=sky.samplesAt(tracks,epoch+10000);assert.ok(sample.lon<-98);assert.ok(Math.abs(sample.lat-38.02)<1e-9);assert.equal(sample.trackDeg,350);assert.ok(Math.min(sample.renderedTrackDeg,360-sample.renderedTrackDeg)<1e-6);assert.equal(sample.altBaroFt,null);assert.equal(sample.rollDeg,null);assert.equal(sample.interpolated,true);assert.equal(sample.observedAt,new Date(epoch).toISOString());
 assert.deepEqual(sky.samplesAt(tracks,epoch-1),[]);assert.deepEqual(sky.samplesAt(tracks,epoch+20001),[]);assert.equal(sky.samplesAt(tracks,epoch)[0].interpolated,false);
});
test('gaps, provider changes, ground transitions and explicit breaks never become continuous flights',()=>{
 for(const end of [point(60001),point(20000,{providerId:'adsb-fi'}),point(20000,{onGround:true}),point(20000,{positionMethod:"mlat"}),point(20000,{breakBefore:true})]) {
  const tracks=new Map([['a00001',[point(),end]]]);assert.deepEqual(sky.samplesAt(tracks,epoch+10000),[]);assert.deepEqual(sky.trailSegments(tracks,epoch+70000),[]);
 }
});
test('regional and selected retention are separate; out-of-region, future and stale observations are rejected',()=>{
 const b=new sky.SkyBuffer();b.select('a00001');
 for(let t=0;t<=3600000;t+=20000)b.ingest(envelope(t,[point(t),point(t,{hex:'a00002'})]));
 assert.equal(b.range('a00001')[0],epoch);assert.equal(b.range('a00002')[0],epoch+3000000);
 b.select('a00002');assert.equal(b.range('a00001')[0],epoch+3000000);
 b.ingest(envelope(3600000,[point(3700000,{hex:'a00003'}),point(0,{hex:'a00004'}),point(3600000,{hex:'a00005',lon:50})]));
 for(const id of ['a00003','a00004','a00005'])assert.equal(b.tracks().has(id),false);
 b.clear();assert.equal(b.range(),null);
});
test('3000-aircraft bounded history reduces trail detail without dropping current aircraft',()=>{
 const b=new sky.SkyBuffer();
 for(let t=0;t<800000;t+=10000)b.ingest(envelope(t,Array.from({length:3000},(_,i)=>point(t,{hex:(i+1).toString(16).padStart(6,'0')}))));
 assert.ok([...b.tracks().values()].reduce((n,p)=>n+p.length,0)<=sky.SKY_MAX_REGIONAL_POINTS);assert.equal(b.truncated,true);assert.equal(b.at(epoch+790000).length,3000);
 const trails=sky.trailSegments(b.tracks(),epoch+790000);assert.ok(trails.reduce((n,t)=>n+t.points.length,0)<=sky.SKY_MAX_TRAIL_POINTS);
});
test('equal-time identity churn cannot exceed the hard history cap or evict the current snapshot',()=>{
 const b=new sky.SkyBuffer();let current=[];
 for(let batch=0;batch<35;batch++){
  current=Array.from({length:3000},(_,i)=>point(0,{hex:(batch*3000+i+1).toString(16).padStart(6,'0')}));
  b.ingest(envelope(0,current));
 }
 assert.ok([...b.tracks().values()].reduce((n,p)=>n+p.length,0)<=sky.SKY_MAX_REGIONAL_POINTS);
 for(const p of current)assert.equal(b.tracks().has(p.hex),true);
 assert.equal(b.truncated,true);
});
test('live parser preserves UTC observations, position method and optional instruments without confusing height datums',()=>{
 const raw={hex:'a00001',lat:38,lon:-98,seen_pos:2,alt_baro:30000,alt_geom:31000,type:'mlat',roll:8,ias:250,mach:0.7};
 const {records}=traffic.parseTraffic({now:epoch/1000,ac:[raw]},epoch+1000);
 assert.equal(records[0].observedAt,new Date(epoch-2000).toISOString());assert.equal(records[0].positionAgeS,3);assert.equal(records[0].positionMethod,'mlat');assert.equal(records[0].timestampBasis,'provider');assert.equal(records[0].rollDeg,8);assert.equal(records[0].mach,0.7);
 assert.equal(traffic.aircraftDisplayAltitude(records[0]),31000);assert.equal(traffic.aircraftAltitudeMsl,undefined);
 assert.throws(()=>traffic.parseTraffic({now:epoch/1000-3600,ac:[raw]},epoch),/stale/);
 const {records:unknown}=traffic.parseTraffic({ac:[{...raw,roll:undefined,ias:undefined,mach:undefined}]},epoch);assert.equal(unknown[0].rollDeg,null);assert.equal(unknown[0].timestampBasis,'retrieval-estimate');
});
test('parser exposes truncation and accounts for every omitted record',()=>{
 const ac=Array.from({length:7000},(_,i)=>({hex:(i+1).toString(16).padStart(6,'0'),lat:38,lon:-98,seen_pos:1}));const parsed=traffic.parseTraffic({ac},epoch);
 assert.equal(parsed.records.length,3000);assert.equal(parsed.dropped,4000);assert.equal(parsed.truncated,true);
});
test('real dated artifacts reproduce byte-for-byte from hash-bound open archive members',async()=>{
 const catalog=JSON.parse(await readFile('public/data/aviation/replays/index.json','utf8'));assert.equal(catalog.flights.length,2);
 const temp=await mkdtemp(join(tmpdir(),'kfm-sky-'));
 try { for(const entry of catalog.flights){
  const path='public'+entry.url,bytes=await readFile(path),artifact=JSON.parse(bytes);assert.equal(createHash('sha256').update(bytes).digest('hex'),entry.sha256);
  const raw='tests/fixtures/kansas-sky/'+artifact.sourceMember.split('/').at(-1)+'.gz';assert.equal(createHash('sha256').update(await readFile(raw)).digest('hex'),artifact.sourceSha256);
  const out=join(temp,entry.id+'.json');execFileSync('python3',['scripts/prepare-kansas-sky-replay.py',raw,artifact.sourceUrl,artifact.sourceMember,out]);assert.deepEqual(await readFile(out),bytes);
  assert.ok(artifact.points.every(sky.validSkyPoint));assert.ok(artifact.points.length>50);assert.equal(artifact.license,'ODbL-1.0');assert.equal(entry.start,new Date(artifact.points[0].observedAt).toISOString());
  assert.ok(artifact.points.slice(1).every((p,i)=>sky.connected(artifact.points[i],p)));assert.ok(bytes.length<4*1024*1024);
 }}finally{await rm(temp,{recursive:true,force:true});}
});

test('unknown position age is refused even when a recent non-position message exists',()=>{
 const parsed=traffic.parseTraffic({now:epoch/1000,ac:[{hex:'a00001',lat:38,lon:-98,seen:0}]},epoch);
 assert.equal(parsed.records.length,0);assert.equal(parsed.dropped,1);
 const b=new sky.SkyBuffer();assert.doesNotThrow(()=>b.ingest({...envelope(),records:[null]}));assert.equal(b.range(),null);
});
test('selected history has its own hard point cap and preserves its newest observation',()=>{
 const b=new sky.SkyBuffer();b.select('a00001');
 for(let i=0;i<sky.SKY_MAX_SELECTED_POINTS+5;i++)b.ingest(envelope(i,[point(i)]));
 assert.equal(b.tracks().get('a00001').length,sky.SKY_MAX_SELECTED_POINTS);assert.equal(b.range()[1],epoch+sky.SKY_MAX_SELECTED_POINTS+4);assert.equal(b.truncated,true);
});
test('vertical rate does not blend incompatible barometric and geometric measurements',()=>{
 const tracks=new Map([['a00001',[point(0,{verticalRateReference:'barometric',verticalRateFpm:100}),point(20000,{verticalRateReference:'geometric',verticalRateFpm:500})]]]);
 assert.equal(sky.samplesAt(tracks,epoch+10000)[0].verticalRateFpm,null);
});
test('archive preparation rejects oversized expansion and unrelated source URLs',()=>{
 const check=String.raw`import importlib.util,gzip,json
spec=importlib.util.spec_from_file_location('sky','scripts/prepare-kansas-sky-replay.py');sky=importlib.util.module_from_spec(spec);spec.loader.exec_module(sky)
for raw,url,expected in [(gzip.compress(b'x'*(16*1024*1024+1)),'https://github.com/adsblol/globe_history/releases/download/v/x','EXPANDED_INPUT_TOO_LARGE'),(gzip.compress(b'{}'),'https://example.invalid/data','SOURCE_NOT_ARCHIVE')]:
 try: sky.prepare(raw,url,'trace')
 except ValueError as e: assert str(e)==expected,(str(e),expected)
 else: raise AssertionError('invalid archive accepted')
`;
 execFileSync('python3',['-c',check]);
});


test('resuming an expired cursor advances immediately within the actual retained interval',()=>{
 assert.equal(sky.advanceSkyCursor(epoch,[epoch+600000,epoch+700000],200,4),epoch+600800);
 assert.equal(sky.advanceSkyCursor(epoch+699900,[epoch+600000,epoch+700000],200,4),epoch+700000);
 assert.equal(sky.advanceSkyCursor(epoch+650000,[epoch+600000,epoch+700000],-200,4),epoch+650000);
});


test('reported right bank lowers the right wing; absent roll adds no bank',()=>{
 assert.ok(sky.bankHeightOffset(100,20)<0);assert.ok(sky.bankHeightOffset(-100,20)>0);
 assert.ok(sky.bankHeightOffset(-100,-20)<0);assert.equal(Math.abs(sky.bankHeightOffset(100,null)),0);
});

// Exercise the production renderer's preparation expression, not a duplicate
// implementation. WebGL rendering is separate from this bounded geometry proof.
const renderSource=await readFile('app/kansas-sky-layer.ts','utf8');
const renderTree=ts.createSourceFile('kansas-sky-layer.ts',renderSource,ts.ScriptTarget.Latest,true,ts.ScriptKind.TS);
let drawableExpression;
const findDrawable=node=>{if(ts.isVariableDeclaration(node)&&node.name.getText(renderTree)==='drawable')drawableExpression=node.initializer?.getText(renderTree);ts.forEachChild(node,findDrawable);};
findDrawable(renderTree);
assert.ok(drawableExpression,'production renderer exposes its drawable trail preparation');
const drawableCode=ts.transpileModule(`const prepare=()=>(${drawableExpression});`,{compilerOptions:{target:ts.ScriptTarget.ES2022,module:ts.ModuleKind.None}}).outputText;
const rendererTrails=(trails,flat=false)=>{
 const scope={...sky,trails,flat,TRAIL_VERTICES:60000};
 return new Function(...Object.keys(scope),`${drawableCode}\nreturn prepare();`)(...Object.values(scope));
};

test('crowded continuous observations retain a bounded 3D trail for every aircraft after thinning',()=>{
 const tracks=new Map(Array.from({length:3000},(_,index)=>{
  const hex=(index+1).toString(16).padStart(6,'0');
  return [hex,Array.from({length:31},(_,sample)=>point(sample*20000,{hex,lon:-98+sample*.001,positionMethod:'adsb_icao',breakBefore:sample===0}))];
 }));
 const trails=sky.trailSegments(tracks,epoch+600000),drawable=rendererTrails(trails);
 assert.ok(trails.reduce((sum,trail)=>sum+trail.points.length,0)<=sky.SKY_MAX_TRAIL_POINTS);
 assert.ok(trails.some(trail=>trail.points.some((sample,index)=>index>0&&sample.observedAt-trail.points[index-1].observedAt>sky.SKY_MAX_GAP_MS)), 'the fixture actually exercises a thinning interval larger than a source gap');
 const visible=new Set(drawable.filter(trail=>trail.points.length>1).map(trail=>trail.hex));
 assert.equal(visible.size,3000,'display thinning must not reinterpret continuous source history as missing observations');
 assert.ok(drawable.reduce((sum,trail)=>sum+trail.points.length,0)<=sky.SKY_MAX_TRAIL_POINTS);
});

test('3D display segments preserve genuine gaps and height-reference changes before thinning',()=>{
 for(const change of [{providerId:'adsb-fi'},{positionMethod:'mlat'},{onGround:true},{breakBefore:true},{altGeomFt:null},{altGeomFt:null,altBaroFt:null},{gap:true}]){
  const offset=change.gap?100001:40000,rest={...change};delete rest.gap;
  const points=[point(0,{positionMethod:'adsb_icao'}),point(20000,{positionMethod:'adsb_icao'}),point(offset,{positionMethod:'adsb_icao',...rest}),point(offset+20000,{positionMethod:'adsb_icao',...rest,breakBefore:false})];
  const drawable=rendererTrails(sky.trailSegments(new Map([['a00001',points]]),epoch+offset+20000));
  assert.ok(drawable.some(trail=>trail.points.some(sample=>sample.observedAt===epoch)&&trail.points.some(sample=>sample.observedAt===epoch+20000)),'known continuous observations remain visible beside the gap');
  for(const trail of drawable)for(let index=1;index<trail.points.length;index++){
   const before=trail.points[index-1],after=trail.points[index];
   assert.equal(sky.connected(before,after),true,`a real discontinuity cannot be joined: ${JSON.stringify(change)}`);
   assert.equal(sky.skyHeightReference(before),sky.skyHeightReference(after),'pressure and WGS84 height references stay separate');
  }
 }
});
