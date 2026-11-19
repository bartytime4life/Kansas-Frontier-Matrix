import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
import {createRequire} from 'node:module';
import {createElement} from 'react';
import {renderToStaticMarkup} from 'react-dom/server';
import {webcrypto,createHash} from 'node:crypto';
const compile=source=>ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const sky=await import(`data:text/javascript;base64,${Buffer.from(compile(await readFile('app/kansas-sky.ts','utf8'))).toString('base64')}`);
const epoch=Date.parse('2026-11-03T12:00:00Z');
const point=(time=0,extra={})=>({hex:'a00001',callsign:'TEST',registration:null,type:null,category:null,lat:38,lon:-98,onGround:false,altBaroFt:30000,altGeomFt:31000,groundSpeedKt:400,trackDeg:350,verticalRateFpm:0,squawk:null,emergency:null,military:false,positionAgeS:2,observedAt:epoch+time,providerId:'adsb-lol',positionMethod:'adsb_icao',...extra});

test('altitude profile preserves disconnected height references and bounds geometry before displaying it',()=>{
  const input=[point(),point(10000),point(20000,{altGeomFt:null}),point(30000,{altGeomFt:null}),point(40000,{altGeomFt:null,altBaroFt:null}),point(50000),point(120001),point(130000,{breakBefore:true}),point(140000,{onGround:true})];
  const segments=sky.heightProfile(input);
  assert.deepEqual(segments.map(part=>part.map(p=>p.observedAt-epoch)),[[0,10000],[20000,30000],[50000],[120001],[130000]]);
  const dense=Array.from({length:20000},(_,i)=>point(i*1000));const bounded=sky.heightProfile(dense,96);
  assert.ok(bounded.flat().length<=96);assert.equal(bounded[0][0],dense[0]);assert.equal(bounded[0].at(-1),dense.at(-1));
  for(const part of segments)assert.ok(part.every(p=>sky.skyHeightReference(p)===sky.skyHeightReference(part[0])));
});

test('whole recorded journey distinguishes past and retained future, keeps explicit gaps, and interpolates only observed spans',()=>{
  const points=[point(),point(20000,{lon:-97.95}),point(40000,{lon:-97.9}),point(120000),point(140000)];
  const journey=sky.selectedJourney(points,epoch+10000);
  assert.equal(journey.length,3);assert.equal(journey[0].future,false);assert.equal(journey[1].future,true);assert.equal(journey[2].future,true);
  assert.ok(Math.abs(journey[0].points.at(-1).lon+97.975)<1e-10);assert.equal(journey[1].points[0].observedAt,epoch+10000);
  assert.equal(journey[1].points.at(-1).observedAt,epoch+40000);assert.equal(journey[2].points[0].observedAt,epoch+120000);
  assert.deepEqual(sky.selectedJourney([point()],epoch),[],'an isolated observation is not a path');
  assert.equal(sky.samplesAt(new Map([['a00001',points]]),epoch)[0].positionAgeS,2,'original receipt-age metadata is retained');
});

function animation(reduced=false){
  let clock=0,serial=0,ended=0;const pending=new Map(),renders=[],readouts=[];
  const cancel=sky.animateSkyReplay({start:epoch,range:[epoch,epoch+2000],speed:1,reduced,now:()=>clock,requestFrame:callback=>{pending.set(++serial,callback);return serial;},cancelFrame:id=>pending.delete(id),render:time=>renders.push(time),readout:time=>readouts.push(time),ended:()=>ended++});
  const advance=stamp=>{clock=stamp;const next=pending.entries().next().value;if(next){pending.delete(next[0]);next[1](stamp);}};
  return {pending,renders,readouts,cancel,advance,ended:()=>ended};
}
test('smooth replay clock redraws independently of bounded readouts and cancels queued work',()=>{
  const run=animation();for(let t=0;t<=1000;t+=16)run.advance(t);
  assert.ok(run.renders.length>50);assert.ok(run.readouts.length<=6);assert.ok(run.renders.every((time,i)=>!i||time>run.renders[i-1]));
  const late=run.pending.values().next().value,count=run.renders.length;run.cancel();late(1200);
  assert.equal(run.renders.length,count);assert.equal(run.pending.size,0);assert.equal(run.ended(),0);
  const done=animation();done.advance(5000);assert.deepEqual(done.renders,[epoch+2000]);assert.equal(done.ended(),1);assert.equal(done.pending.size,0);
});
test('reduced motion uses coarse explicit playback; adaptive budget lowers frequency rather than aircraft count',()=>{
  const run=animation(true);for(let t=0;t<=1000;t+=16)run.advance(t);assert.ok(run.renders.length<=6);run.cancel();
  const budget=new sky.SkyFrameBudget();assert.equal(budget.interval(),1000/60);for(let i=0;i<20;i++)budget.record(100);assert.equal(budget.interval(),50);assert.equal(budget.interval(true),200);for(let i=0;i<100;i++)budget.record(0);assert.equal(budget.interval(),1000/60);
});

test('buffered live has one delayed clock, requires current eligibility and never extrapolates across a warm-up or gap',()=>{
  const tracks=new Map([['a00001',[point(),point(20000,{lon:-97.95})]],['b00002',[point(0,{hex:'b00002'}),point(20000,{hex:'b00002',lon:-97.9})]]]);
  const sampled=sky.bufferedSkySamples(tracks,epoch+10000,new Set(['a00001']));assert.equal(sampled.length,1);assert.ok(Math.abs(sampled[0].lon+97.975)<1e-10);
  assert.deepEqual(sky.bufferedSkySamples(tracks,epoch-1,new Set(['a00001'])),[]);
  assert.deepEqual(sky.bufferedSkySamples(tracks,epoch+20001,new Set(['a00001'])),[]);
  assert.deepEqual(sky.bufferedSkySamples(tracks,epoch+10000,new Set()),[],'expired or failed current-feed eligibility removes old buffered positions');
  let frame;const values=[];const stop=sky.animateSkyBuffered({requestFrame:callback=>{frame=callback;return 1;},cancelFrame:()=>{},now:()=>0,wallTime:()=>epoch+40000,render:time=>values.push(time),readout:()=>{}});
  frame(0);assert.deepEqual(values,[epoch+10000]);stop();frame(20);assert.equal(values.length,1,'cancelled delayed motion cannot keep rendering');
});

// Execute the actual production parsers without mounting the component or weakening bounds.
const source=await readFile('app/kansas-sky-control.tsx','utf8');
const ast=ts.createSourceFile('control.tsx',source,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
const names=new Set(['catalog','archive','archiveDays']);const declarations=[];
for(const node of ast.statements)if(ts.isFunctionDeclaration(node)&&names.has(node.name?.text))declarations.push(node.getText(ast));
const parsers=new Function('isObject','external',compile(declarations.join('\n')+'\nreturn {catalog,archive,archiveDays:typeof archiveDays==="function"?archiveDays:undefined};'))(v=>!!v&&typeof v==='object'&&!Array.isArray(v),v=>typeof v==='string'&&/^https:\/\/[^\s]+$/.test(v));
const entry={id:'2026-11-03-a00001-p0001',title:'Regional observation',start:new Date(epoch).toISOString(),end:new Date(epoch).toISOString(),url:'/data/aviation/replays/days/2026-11-03/2026-11-03-a00001-p0001.json',sha256:'a'.repeat(64),provider:'adsb.lol',license:'ODbL-1.0',sourceUrl:'https://github.com/adsblol/example',hex:'a00001',pointCount:1};
test('day catalogs accept bounded single-observation parts and reject identity/count substitution',()=>{
  assert.equal(parsers.catalog({schemaVersion:1,flights:[entry]}).length,1);
  const file={schemaVersion:1,id:entry.id,provider:entry.provider,license:entry.license,sourceUrl:entry.sourceUrl,sourceSha256:'b'.repeat(64),points:[point()]};
  assert.equal(parsers.archive(file,entry).get('a00001').length,1);
  assert.throws(()=>parsers.archive({...file,points:[point(0,{hex:'b00002'})]},entry),/aircraft/);
  assert.throws(()=>parsers.archive(file,{...entry,pointCount:2}),/count/);
  assert.throws(()=>parsers.catalog({schemaVersion:1,flights:Array(10001).fill(entry)}),/invalid/);
  assert.throws(()=>parsers.catalog({schemaVersion:1,flights:[{...entry,url:'https://untrusted.test/flight.json'}]}),/invalid/);
});
test('archive day discovery permits only exact local published catalog paths and explicit coverage',()=>{
  const day={day:'2026-11-03',coverage:'selected-recordings',aircraftCount:2,pointCount:412,indexUrl:'/data/aviation/replays/index.json'};
  assert.equal(parsers.archiveDays({schemaVersion:1,days:[day]})[0].coverage,'selected-recordings');
  assert.throws(()=>parsers.archiveDays({schemaVersion:1,days:[{...day,indexUrl:'/private/archive.json'}]}),/invalid/);
  assert.throws(()=>parsers.archiveDays({schemaVersion:1,days:[{...day,coverage:'complete-live-collection'}]}),/invalid/);
});


// The browser acceptance fixture must cover the archive discovery chain that the
// production control actually follows, not silently fall through to public files.
const browserSource=await readFile('tests/kansas-sky.browser.mjs','utf8');
const browserAst=ts.createSourceFile('browser.mjs',browserSource,ts.ScriptTarget.ES2022,true,ts.ScriptKind.JS);
function browserArchiveFixture(){
  const names=new Set(['at','aircraft','record','recordText','catalog','archiveIndex','archiveResponses']),declarations=[];
  for(const statement of browserAst.statements)if(ts.isVariableStatement(statement))for(const declaration of statement.declarationList.declarations)if(names.has(declaration.name.getText(browserAst)))declarations.push(`const ${declaration.getText(browserAst)};`);
  return new Function('createHash',declarations.join('\n')+'\nreturn {responses:typeof archiveResponses==="undefined"?new Map():archiveResponses,record};')(createHash);
}

const partEntry=(part,extra={})=>({...entry,id:`2026-11-03-a00001-p000${part}`,day:'2026-11-03',part,partCount:3,start:new Date(epoch+(part-1)*60000).toISOString(),end:new Date(epoch+(part-1)*60000+20000).toISOString(),url:`/data/aviation/replays/days/2026-11-03/2026-11-03-a00001-p000${part}.json`,...extra});
test('multipart catalogs require an unambiguous aircraft, UTC day, part number and declared count',()=>{
  const parts=[partEntry(1),partEntry(2),partEntry(3)];
  assert.deepEqual(parsers.catalog({schemaVersion:1,flights:parts}),parts);
  assert.equal(parsers.catalog({schemaVersion:1,flights:[parts[0],parts[2]]}).length,2,'missing parts remain an explicit catalog gap');
  for(const change of [{part:0},{part:1.2},{part:4},{partCount:10001},{partCount:undefined},{part:undefined},{hex:undefined},{day:undefined},{day:'2026-11-04'},{end:'2026-11-04T00:00:00Z'}])assert.throws(()=>parsers.catalog({schemaVersion:1,flights:[partEntry(1,change)]}),/part|UTC/);
  assert.throws(()=>parsers.catalog({schemaVersion:1,flights:[parts[0],partEntry(2,{partCount:2})]}),/ambiguous/);
  assert.throws(()=>parsers.catalog({schemaVersion:1,flights:[parts[0],partEntry(1,{id:'different-id'})]}),/ambiguous/);
  assert.throws(()=>parsers.catalog({schemaVersion:1,flights:[entry,entry]}),/Duplicate/);
});
test('part navigation selects only the immediate same-aircraft same-day neighbor and never bridges catalog gaps',()=>{
  const parts=[partEntry(1),partEntry(2),partEntry(3)];
  assert.deepEqual(sky.skyPartNeighbors(parts,parts[1]),{previous:parts[0],next:parts[2],available:3,expected:3,multipart:true});
  assert.equal(sky.skyPartNeighbors(parts,parts[0]).previous,null);assert.equal(sky.skyPartNeighbors(parts,parts[2]).next,null);
  for(const change of [{hex:'b00002'},{day:'2026-11-04'},{provider:'other-provider'},{partCount:4},{start:parts[0].start}])assert.equal(sky.skyPartNeighbors([parts[0],partEntry(2,change),parts[2]],parts[0]).next,null);
  const gap=sky.skyPartNeighbors([parts[0],parts[2]],parts[0]);assert.equal(gap.next,null);assert.equal(gap.available,2);
  assert.equal(sky.skyPartNeighbors([parts[0],parts[1],parts[1]],parts[0]).next,null,'duplicate neighbors are never chosen arbitrarily');
  assert.equal(sky.skyPartNeighbors([entry],entry).multipart,false,'legacy single files stay compatible');
});

// Drive the actual component loader with controlled I/O to exercise cancellation,
// verification failure and one-file replacement without a browser or fake fetch result.
let loaderInitializer;
const findLoader=node=>{if(ts.isVariableDeclaration(node)&&node.name.getText(ast)==='loadRecorded')loaderInitializer=node.initializer.getText(ast);ts.forEachChild(node,findLoader);};findLoader(ast);
function loaderHarness(flights){
  const calls=[],pending=[],request={current:null},setters=['setMode','setFlightView','setRecorded','setEntry','setPlaying','setCamera','setError','setArchiveState','setSelected','setCursor'];
  const scope={flights,request,archive:parsers.archive,crypto:webcrypto,boundedBytes:(url,signal,max)=>new Promise((resolve,reject)=>pending.push({url,signal,max,resolve,reject})),...Object.fromEntries(setters.map(name=>[name,value=>calls.push({name,value})]))};
  const load=new Function(...Object.keys(scope),compile(`return (${loaderInitializer});`))(...Object.values(scope));
  return {load,calls,pending,request};
}
async function verifiedPart(part){
  const record=partEntry(part),file={schemaVersion:1,id:record.id,provider:record.provider,license:record.license,sourceUrl:record.sourceUrl,sourceSha256:'b'.repeat(64),points:[point((part-1)*60000)]};
  const bytes=new TextEncoder().encode(JSON.stringify(file)),sha256=Buffer.from(await webcrypto.subtle.digest('SHA-256',bytes)).toString('hex');
  return {entry:{...record,sha256},bytes};
}
test('browser archive fixture follows discovered day, verifies exact bytes and refuses an altered digest',async()=>{
  const fixture=browserArchiveFixture(),discovery=fixture.responses.get('/data/aviation/replays/archive-index.json');
  assert.ok(discovery,'browser fixture must intercept the daily discovery index');
  const days=parsers.archiveDays(JSON.parse(discovery));assert.equal(days.length,1);assert.equal(days[0].coverage,'selected-recordings');
  const dayCatalog=fixture.responses.get(days[0].indexUrl);assert.ok(dayCatalog,'discovered day catalog must not fall through to real files');
  const flights=parsers.catalog(JSON.parse(dayCatalog));assert.equal(flights.length,1);
  const flight=flights[0],text=fixture.responses.get(flight.url);assert.ok(text,'digest-verified record must use the declared daily path');
  assert.ok(flight.url.startsWith(`/data/aviation/replays/days/${days[0].day}/`));
  const bytes=new TextEncoder().encode(text);assert.equal(createHash('sha256').update(bytes).digest('hex'),flight.sha256);
  assert.equal(parsers.archive(JSON.parse(text),flight).get(flight.hex).length,days[0].pointCount);
  assert.deepEqual(parsers.catalog(JSON.parse(fixture.responses.get('/data/aviation/replays/index.json'))),[],'an empty legacy catalog prevents an accidental root-catalog pass');
  const h=loaderHarness(flights),loading=h.load(flight.id);assert.equal(h.pending[0].url,flight.url);h.pending[0].resolve(bytes);await loading;
  assert.equal(h.calls.findLast(c=>c.name==='setArchiveState').value,'ready');
  const corrupt=loaderHarness(flights),rejected=corrupt.load(flight.id);corrupt.pending[0].resolve(new TextEncoder().encode(text+' '));await rejected;
  assert.equal(corrupt.calls.findLast(c=>c.name==='setArchiveState').value,'error');assert.match(corrupt.calls.findLast(c=>c.name==='setError').value,/digest/);
});

test('part loading verifies one bounded file, replaces instead of joins tracks, and stays paused',async()=>{
  const first=await verifiedPart(1),next=await verifiedPart(2),h=loaderHarness([first.entry,next.entry]);
  const loading=h.load(next.entry.id,true);assert.equal(h.pending.length,1);assert.equal(h.pending[0].url,next.entry.url);assert.equal(h.pending[0].max,4*1024*1024);
  h.pending[0].resolve(next.bytes);await loading;
  assert.deepEqual(h.calls.filter(c=>c.name==='setRecorded').map(c=>c.value.size),[0,1]);
  assert.equal(h.calls.findLast(c=>c.name==='setRecorded').value.get('a00001')[0].observedAt,Date.parse(next.entry.start));
  assert.deepEqual(h.calls.filter(c=>c.name==='setPlaying').map(c=>c.value),[false]);
  assert.deepEqual(h.calls.filter(c=>c.name==='setCamera').map(c=>c.value),['free']);
  assert.deepEqual(h.calls.filter(c=>c.name==='setFlightView').map(c=>c.value),[true],'loading cannot reopen a view closed after the request started');
  assert.equal(h.calls.findLast(c=>c.name==='setArchiveState').value,'ready');assert.equal(h.pending.length,1,'no next-part prefetch');
});
test('a failed or superseded part cannot replace the selected file or start motion',async()=>{
  const first=await verifiedPart(1),next=await verifiedPart(2),h=loaderHarness([first.entry,next.entry]);
  const before=h.load(first.entry.id,true),after=h.load(next.entry.id,true);assert.equal(h.pending[0].signal.aborted,true);
  h.pending[1].resolve(next.bytes);await after;h.pending[0].resolve(first.bytes);await before;
  assert.equal(h.calls.filter(c=>c.name==='setRecorded'&&c.value.size).length,1);
  assert.equal(h.calls.findLast(c=>c.name==='setRecorded').value.get('a00001')[0].observedAt,Date.parse(next.entry.start));
  const cancelled=loaderHarness([first.entry]),cancelledLoad=cancelled.load(first.entry.id);cancelled.request.current.abort();cancelled.pending[0].resolve(first.bytes);await cancelledLoad;
  assert.equal(cancelled.calls.some(c=>c.name==='setRecorded'&&c.value.size),false);assert.equal(cancelled.calls.some(c=>c.name==='setArchiveState'&&c.value==='ready'),false);
  const failed=loaderHarness([first.entry]),failedLoad=failed.load(first.entry.id);failed.pending[0].resolve(next.bytes);await failedLoad;
  assert.equal(failed.calls.findLast(c=>c.name==='setArchiveState').value,'error');assert.match(failed.calls.findLast(c=>c.name==='setError').value,/digest/);
  assert.equal(failed.calls.some(c=>c.name==='setRecorded'&&c.value.size),false);assert.equal(failed.calls.some(c=>c.name==='setPlaying'&&c.value),false);
});

const detailsExports={},require=createRequire(import.meta.url);
new Function('exports','require',ts.transpileModule(await readFile('app/kansas-sky-details.tsx','utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022,jsx:ts.JsxEmit.ReactJSX}}).outputText)(detailsExports,name=>name==='./kansas-sky'?sky:require(name));
test('the production aircraft dossier renders every field group with honest unavailable values',()=>{
  const html=renderToStaticMarkup(createElement(detailsExports.SkyAircraftDossier,{aircraft:{...point(),observedAt:new Date(epoch).toISOString(),positionQuality:{nic:7,nacP:null,sil:2,rcM:185,rssi:-21},traceFlags:8,mach:.73,indicatedAirSpeedKt:260,rollDeg:4,timestampBasis:'provider'},source:'adsb.lol'}));
  for(const field of ['Callsign','ICAO / address','Registration','Emitter category','Provider military flag','Latitude','Longitude','Observation time','Time basis','Position method','Position age at receipt','Pressure altitude','Geometric height','Indicated airspeed','Mach','Reported roll','Vertical-rate reference','Squawk','Emergency declaration','NIC','NACp','SIL','Containment radius','Signal strength','Trace flags'])assert.ok(html.includes(field),field);
  assert.ok(html.includes('Unavailable'));assert.ok(html.includes('0.73'));assert.ok(html.includes('185 m'));assert.ok(html.includes('-21 dBFS'));assert.equal(html.includes('undefined'),false);
});
test('production altitude profile supplies a shared-time keyboard control and disconnected paths',()=>{
  const html=renderToStaticMarkup(createElement(detailsExports.SkyAltitudeProfile,{points:[point(),point(10000),point(100000),point(110000)],cursor:epoch+5000,canSeek:true,onSeek:()=>{}}));
  const groups=[...html.matchAll(/<g class="sky-profile-(?:geom|baro)">(.*?)<\/g>/g)];
  assert.equal(groups.length,2,'the source gap splits both line and shaded area');
  for(const [,group]of groups){
    const paths=[...group.matchAll(/<path(?: class="(sky-profile-area)")? d="([^"]+)"/g)];
    assert.equal(paths.length,2);assert.equal(paths.filter(([,kind])=>kind==='sky-profile-area').length,1);
    const area=paths.find(([,kind])=>kind),line=paths.find(([,kind])=>!kind);
    assert.ok(area[2].startsWith(line[2]+' L'),'the area follows only its own observed line before closing to the baseline');
    assert.equal((line[2].match(/M/g)??[]).length,1);
  }
  assert.ok(html.includes('aria-label="Altitude profile time"'));assert.ok(html.includes(`value="${epoch+5000}"`));assert.ok(html.includes('Gaps remain disconnected'));
});

test('interpolated dossier values have deliberate display precision with exact values separately disclosed',()=>{
 const plane={...point(),observedAt:new Date(epoch).toISOString(),interpolated:true,altGeomFt:17849.061957074402,groundSpeedKt:370.76247828297613,verticalRateFpm:-1610.9814391210375,trackDeg:178.5824,mach:.734567};
 const html=renderToStaticMarkup(createElement(detailsExports.SkyAircraftDossier,{aircraft:plane,source:'adsb.lol'}));
 assert.ok(html.includes('17,849 ft · WGS84'));assert.ok(html.includes('370.8 kt'));assert.ok(html.includes('-1,611 ft/min'));assert.ok(html.includes('178.6°'));assert.ok(html.includes('0.735'));
 const displayed=html.split('Exact displayed values')[0];assert.equal(displayed.includes('17849.061957074402'),false);assert.ok(html.includes('17849.061957074402'),'exact values remain inspectable separately');
 const compact=renderToStaticMarkup(createElement(detailsExports.SkyAltitudeProfile,{points:[point(),point(10000)],cursor:epoch,canSeek:true,showRange:false,onSeek:()=>{}}));assert.equal(compact.includes('type="range"'),false,'dock profile reuses its single visible timeline');
 const brief=renderToStaticMarkup(createElement(detailsExports.SkyAircraftBrief,{aircraft:plane,observationCount:10,gap:true}));assert.ok(brief.includes('Observation gap'));assert.ok(brief.includes('TEST'));assert.equal(brief.includes('370.762478'),false);
});

test('flight brief separates evaluated motion, source reports, heading and height references',()=>{
 const aircraft={...point(),observedAt:new Date(epoch).toISOString(),sampledAt:new Date(epoch+5000).toISOString(),interpolated:true,renderedTrackDeg:90,trueHeadingDeg:null,interpolation:{fromObservedAt:new Date(epoch).toISOString(),toObservedAt:new Date(epoch+10000).toISOString(),model:'bounded-hermite'}};
 const brief=renderToStaticMarkup(createElement(detailsExports.SkyAircraftBrief,{aircraft,observationCount:2}));
 for(const text of ['estimated position is displayed near','Estimated position','12:00:05 UTC','12:00:00 UTC','12:00:10 UTC','bounded curve','Reported ground speed','not reported aircraft heading','do not measure clearance'])assert.ok(brief.includes(text),text);
 assert.equal(brief.includes('Interpolated ground speed'),false);
 const dossier=renderToStaticMarkup(createElement(detailsExports.SkyAircraftDossier,{aircraft,source:'adsb.lol'}));
 for(const text of ['Evaluated playback time','Earlier bounding report','Later bounding report','Reported ground track','Reported true heading','Estimated path direction','Interpolated roll'])assert.ok(dossier.includes(text),text);
 const unknown=renderToStaticMarkup(createElement(detailsExports.SkyAircraftBrief,{aircraft:{...aircraft,renderedTrackDeg:null,trackDeg:null},observationCount:2}));assert.ok(unknown.includes('Direction is unavailable'));
});

test('archive loader preserves reported true heading and rejects calculated motion fields in source points',()=>{
 const file={schemaVersion:1,id:entry.id,provider:entry.provider,license:entry.license,sourceUrl:entry.sourceUrl,sourceSha256:'b'.repeat(64),points:[point(0,{trueHeadingDeg:123})]};
 assert.equal(parsers.archive(file,entry).get('a00001')[0].trueHeadingDeg,123);
 for(const bad of [{interpolated:true},{trueHeadingDeg:361},{trueHeadingDeg:'90'},{sampledAt:new Date(epoch).toISOString()},{interpolation:{model:'bounded-hermite'}},{renderedTrackDeg:90}])assert.throws(()=>parsers.archive({...file,points:[point(0,bad)]},entry),/heading|observations/);
});
