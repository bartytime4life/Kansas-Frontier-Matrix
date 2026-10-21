import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
const compile = (source, deps = {}) => {
  const code = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  const mod = { exports: {} }; new Function('require','module','exports',code)(name=>deps[name],mod,mod.exports); return mod.exports;
};
const deferred = () => { let resolve,reject; const promise = new Promise((a,b)=>{resolve=a;reject=b;}); return {promise,resolve,reject}; };
const readSource = await readFile('app/layer-json-reads.ts','utf8');
const hit = compile(await readFile('app/layer-hit-stack.ts','utf8'));
const tick = () => new Promise(resolve=>setTimeout(resolve,0));
function pool(concurrency=3) {
  const calls=[];let now=0;
  const { LayerJsonReads }=compile(readSource, {'./browser-json-request':{browserJsonRequest:(url,options)=>{const call={url,options,...deferred()};calls.push(call);return call.promise;}}});
  return {reads:new LayerJsonReads(concurrency,()=>now), calls, time: value=>{now=value;}};
}
const options = signal => ({signal,maxBytes:4096,cacheMs:300000,validate:body=>body.day==='2024-06-01'});
const result = () => ({response:{ok:true,status:200},body:{day:'2024-06-01',retrievedAt:'2024-06-02T00:00:00Z',state:'empty'}});
test('identical display reads share acquisition; one canceled consumer cannot cancel another', async()=>{
  const r=pool(),a=new AbortController(),b=new AbortController();
  const first=r.reads.read('/api/live-context?feed=usgs-earthquakes&day=2024-06-01',options(a.signal));
  const rejected=assert.rejects(first,{name:'AbortError'});
  const second=r.reads.read('/api/live-context?feed=usgs-earthquakes&day=2024-06-01',options(b.signal));
  assert.equal(r.calls.length,1);a.abort();assert.equal(r.calls[0].options.signal.aborted,false);
  r.calls[0].resolve(result());await rejected;assert.equal((await second).body.state,'empty');
});
test('hidden queued layers never fetch and freed capacity starts the next visible read',async()=>{
  const r=pool(1),controllers=Array.from({length:3},()=>new AbortController());
  const promises=controllers.map((c,i)=>r.reads.read(`/api/live-context?layer=${i}`,options(c.signal)));
  const rejection=assert.rejects(promises[1],{name:'AbortError'});controllers[1].abort();
  assert.equal(r.calls.length,1);r.calls[0].resolve(result());await promises[0];await tick();
  assert.equal(r.calls.length,2);assert.equal(r.calls[1].url,'/api/live-context?layer=2');
  r.calls[1].resolve(result());await promises[2];await rejection;
});
test('canceling the final consumer prevents caching late data and cannot delete its replacement',async()=>{
  const r=pool(),c=new AbortController();const first=r.reads.read('/api/live-context?day=old',options(c.signal));
  const rejected=assert.rejects(first,{name:'AbortError'});c.abort();
  const replacement=r.reads.read('/api/live-context?day=old',options(new AbortController().signal));
  assert.equal(r.calls.length,2);r.calls[0].resolve(result());r.calls[1].resolve(result());await rejected;await replacement;
  await tick();await r.reads.read('/api/live-context?day=old',options(new AbortController().signal));assert.equal(r.calls.length,2);
});
test('dated cache retains retrieved time, expires, obeys LRU cap, and current/forced reads bypass it',async()=>{
  const r=pool(),load=async(url,opt=options(new AbortController().signal))=>{const pending=r.reads.read(url,opt);r.calls.at(-1).resolve(result());return pending;};
  await load('/api/live-context?day=A');await tick();
  assert.equal((await r.reads.read('/api/live-context?day=A',options(new AbortController().signal))).body.retrievedAt,'2024-06-02T00:00:00Z');assert.equal(r.calls.length,1);
  await load('/api/live-context?day=A',{...options(new AbortController().signal),cacheMs:0});await tick();assert.equal(r.calls.length,2);
  for(const day of ['B','C','D','E']){await load(`/api/live-context?day=${day}`);await tick();}
  await load('/api/live-context?day=A');await tick();assert.equal(r.calls.length,7);
  r.time(300001);await load('/api/live-context?day=A');assert.equal(r.calls.length,8);
});
test('partial/empty responses are valid snapshots; failures and incompatible dates stay retryable',async()=>{
  const r=pool();const load=()=>r.reads.read('/api/live-context?day=A',options(new AbortController().signal));
  let pending=load(),rejected=assert.rejects(pending,/incompatible/);r.calls[0].resolve({...result(),body:{day:'2024-06-02'}});await rejected;await tick();
  pending=load();r.calls[1].resolve({...result(),body:{...result().body,state:'partial'}});assert.equal((await pending).body.state,'partial');
});
test('a fresh read immediately after success starts a new request instead of joining a completed job',async()=>{
  const r=pool(),url='/api/live-context?feed=usgs-earthquakes';
  const first=r.reads.read(url,options(new AbortController().signal));
  r.calls[0].resolve(result());await first;
  const controller=new AbortController();
  const next=r.reads.read(url,{...options(controller.signal),cacheMs:0});
  const settled=next.catch(error=>error);
  await tick();
  const count=r.calls.length;
  if(count===2) r.calls[1].resolve(result());else controller.abort();
  await settled;
  assert.equal(count,2,'a completed response must no longer accept consumers');
});
test('an immediate retry after failure starts acquisition again',async()=>{
  const r=pool(),url='/api/live-context?feed=usgs-earthquakes';
  const first=r.reads.read(url,options(new AbortController().signal));
  r.calls[0].reject(new Error('offline'));await assert.rejects(first,/offline/);
  const next=r.reads.read(url,options(new AbortController().signal));
  await tick();assert.equal(r.calls.length,2);
  r.calls[1].resolve(result());await next;
});
test('hover and click honor rendered overlap order across registry, gauges, and fire',()=>{
  const gauge={layer:{id:'gauge'},source:'water'},fire={layer:{id:'fire'},source:'external-nifc-fire-reports'},local={layer:{id:'local'},source:'local'};
  assert.equal(hit.layerHitStack([gauge,fire,local],['local'],['gauge','fire']).officialCandidate,gauge);
  assert.equal(hit.layerHitStack([local,gauge,fire],['local'],['gauge','fire']).candidate,local);
  assert.equal(hit.layerHitStack([fire,gauge],[],['gauge','fire']).officialCandidate,fire);
});
const page=await readFile('app/page.tsx','utf8');
function callback(name,end,ctx){const code=ts.transpileModule(page.slice(page.indexOf(`  const ${name} =`),page.indexOf(`  const ${end} =`)),{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;return new Function(...Object.keys(ctx),code+`\nreturn ${name};`)(...Object.values(ctx));}
const feed='usgs-earthquakes',ref=current=>({current});
function archiveContext(){
  const requests=[],states=[];
  const ctx={useCallback:fn=>fn,cancelSmokePlayback(){},announce:()=>{},currentUtcDay:()=>'2026-10-11',readFireDay:async()=>null,
    calendarArchiveLoads:ref(new Map()),officialRequestsRef:ref(new Map()),officialArchiveDaysRef:ref({}),officialArchivePayloadsRef:ref({}),officialPayloadsRef:ref({}),
    setOfficialArchiveDays:()=>{},setOfficialPayloads:()=>{},setOfficialStates:fn=>states.push(fn({})[feed]),setOfficialErrors:()=>{},setOfficialReadPhases:()=>{},setEarthquakeArchiveFrameIndex:()=>{},setSmokeArchiveFrameIndex:()=>{},
    OFFICIAL_CONTEXT_BY_ID:{[feed]:{apiPath:'/api/live-context?feed=usgs-earthquakes',shortTitle:'Earthquakes'}},
    layerJsonReadsRef:ref({read:(url,options)=>{const req={url,options,...deferred()};requests.push(req);return req.promise;}}),
    validLayerPayload:()=>true,earthquakeEventTimes:()=>[],smokeValidityTimes:()=>[],smokeInitialFrameIndex:()=>-1,smokeValidAt:v=>v};
  return {ctx,requests,states,load:callback('loadOfficialArchiveDay','returnOfficialSourceToCurrent',ctx)};
}
const snapshot=day=>({response:{ok:true,status:200},body:{feed,state:'empty',sourceDay:day,retrievedAt:'2024-06-03T00:00:00Z',featureCount:0,data:{type:'FeatureCollection',features:[]}}});
test('production date callback coalesces identical selection and ignores an older day completing last',async()=>{
  const r=archiveContext();const old=r.load(feed,'2024-06-01');await tick();const duplicate=r.load(feed,'2024-06-01');assert.equal(duplicate,old,'identical dates must share completion, not only acquisition');assert.equal(r.requests.length,1);
  const next=r.load(feed,'2024-06-02');await tick();assert.equal(r.requests[0].options.signal.aborted,true);
  r.requests[1].resolve(snapshot('2024-06-02'));await next;r.requests[0].resolve(snapshot('2024-06-01'));await old;
  assert.equal(r.ctx.officialPayloadsRef.current[feed].sourceDay,'2024-06-02');assert.equal(r.ctx.officialArchivePayloadsRef.current[feed].sourceDay,'2024-06-02');assert.equal(r.states.at(-1),'empty');
});
test('production date callback clears incompatible old geometry on failure and permits explicit retry',async()=>{
  const r=archiveContext();r.ctx.officialPayloadsRef.current[feed]=snapshot('2024-05-31').body;
  const first=r.load(feed,'2024-06-01');assert.equal(r.ctx.officialPayloadsRef.current[feed],undefined);await tick();r.requests[0].reject(new Error('offline'));await first;assert.equal(r.states.at(-1),'error');
  const retry=r.load(feed,'2024-06-01',true);await tick();assert.equal(r.requests[1].options.cacheMs,0);r.requests[1].resolve(snapshot('2024-06-01'));await retry;assert.equal(r.states.at(-1),'empty');
});
