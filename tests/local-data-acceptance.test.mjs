import test from 'node:test';
import assert from 'node:assert/strict';
import {newSecret,signRequest,signResponse,RESPONSE_SIGNATURE_HEADER} from '../scripts/home-inference/signature.mjs';
import {day,minute} from '../scripts/local-data/query.mjs';
import {parseStormQuery} from '../scripts/local-data/storm-events.mjs';
import {DATASETS,datasetCatalog} from '../scripts/local-data/datasets.mjs';
import {LOCAL_DATA_GATEWAY,LOCAL_DATA_LIMITS} from '../scripts/local-data/protocol.mjs';
import {localDataConfig,createLocalDataService,LOCAL_DATA_CACHE} from '../server/local-data.mjs';
const SITE='https://kansasfrontiermatrix.com';
function harness(){
 let now=Date.now(),calls=0,mode='ok',payload={format:'kfm-local-data-v1',dataset:'nws-alerts',rows:[],count:0,total:0,source:DATASETS.get('nws-alerts').source,generatedAt:new Date(now).toISOString()};
 const config=localDataConfig({KFM_LOCAL_DATA:'1',KFM_LOCAL_DATA_ORIGIN:SITE,KFM_LOCAL_DATA_GATEWAY_KEY_ID:'gw',KFM_LOCAL_DATA_GATEWAY_SECRET:newSecret(),KFM_LOCAL_DATA_WORKER_KEY_ID:'wk',KFM_LOCAL_DATA_WORKER_SECRET:newSecret()});
 const relay={lastSeen:now,handler:async()=>new Response(null,{status:204}),async submit({method,path,body}){
  calls++;if(mode==='outage')throw new Error('controlled outage');
  const status=mode==='large'?413:mode==='not-ready'?503:200;
  const value=status===413?{error:'REPLY_TOO_LARGE'}:status===503?{error:'DATASET_NOT_READY'}:payload;
  const bytes=Buffer.from(JSON.stringify({gateway:LOCAL_DATA_GATEWAY,...value}));
  const requestHeaders=signRequest({keyId:config.keyId,secret:config.secret,method,path,body});
  const signature=signResponse({secret:config.secret,requestHeaders,method,path,requestBody:body,status,body:bytes});
  return {status,bytes,requestHeaders,headers:new Headers({'content-type':'application/json',[RESPONSE_SIGNATURE_HEADER]:mode==='tamper'?'invalid':signature})};
 }};
 const service=createLocalDataService({config,relay,clock:()=>now});
 return {service,relay,get:(q='limit=1')=>service.query(new Request(SITE+'/api/local-data/nws-alerts?'+q),'nws-alerts'),calls:()=>calls,setMode:m=>{mode=m;},advance:ms=>{now+=ms;},online:()=>{relay.lastSeen=now;},payload:v=>{payload=v;}};
}
test('calendar dates are real across shared, minute, storm and PRISM parsers',()=>{
 for(const bad of ['2025-02-29','2025-02-30','2024-04-31','1900-02-29','2100-02-29']){
  for(const run of [()=>day(bad),()=>minute(bad+'T12:00'),()=>parseStormQuery({from:bad}),()=>DATASETS.get('prism-county').parse({variable:'ppt',county:'173',step:'daily',from:bad})])assert.throws(run,{code:'QUERY_INVALID'});
 }
 assert.equal(day('2000-02-29'),'2000-02-29');assert.equal(day('2024-02-29'),'2024-02-29');
 const q=DATASETS.get('prism-county').parse({variable:'ppt',county:'173',step:'daily',from:'2024-02',to:'2024-02'});
 assert.equal(q.to,'2024-02-29');
});
test('duplicate parameters are refused before a gateway trip',async()=>{
 const h=harness();for(const q of ['limit=1&limit=2','limit=1&limit=1','area=Ford&area=Riley']){
  const r=await h.get(q);assert.equal(r.status,400);assert.equal((await r.json()).reasonCode,'QUERY_INVALID');
 }assert.equal(h.calls(),0);
});
test('captured sources identify historical data independently of cache delivery state',()=>{
 for(const id of ['nws-alerts','usgs-earthquakes','usgs-streamflow-sites','usgs-streamflow']){
  const source=datasetCatalog().find(d=>d.id===id).source;
  assert.equal(source.temporalMode,'historical-capture');assert.match(source.notes,/not a live/i);
 }
 const source=DATASETS.get('nws-alerts').source;assert.match(source.notes,/cache/i);
});
test('signed answers retain source limitations and timestamps through fresh, stale, expiry and recovery',async()=>{
 const h=harness();let r=await h.get(),initial=await r.json();assert.equal(initial.cache.state,'live');
 const fresh=await (await h.get()).json();assert.equal(fresh.cache.state,'fresh');assert.equal(h.calls(),1);
 h.setMode('outage');h.advance(LOCAL_DATA_CACHE.freshMs);h.online();
 const stale=await (await h.get()).json();assert.equal(stale.cache.state,'stale');assert.deepEqual(stale.source,initial.source);assert.equal(stale.generatedAt,initial.generatedAt);assert.equal(stale.cache.at,initial.cache.at);
 assert.equal((await h.get('limit=2')).status,503);
 h.advance(LOCAL_DATA_CACHE.staleMs-LOCAL_DATA_CACHE.freshMs-1);h.online();assert.equal((await (await h.get()).json()).cache.state,'stale');
 h.advance(1);h.online();assert.equal((await h.get()).status,503);
 h.setMode('ok');assert.equal((await (await h.get()).json()).cache.state,'live');
});
test('tampering, missing indexes and gateway size refusal are bounded public errors',async()=>{
 for(const [mode,status,reason] of [['tamper',503,'LOCAL_DATA_UNAVAILABLE'],['not-ready',503,'DATASET_NOT_READY'],['large',413,'REPLY_TOO_LARGE']]){
  const h=harness();h.setMode(mode);const r=await h.get();assert.equal(r.status,status);assert.equal((await r.json()).reasonCode,reason);
 }
});
test('the public byte ceiling includes cache metadata on live and cached answers',async()=>{
 const h=harness(),base={format:'kfm-local-data-v1',dataset:'nws-alerts',rows:[],count:0,total:0,pad:''};
 const signedSize=Buffer.byteLength(JSON.stringify({gateway:LOCAL_DATA_GATEWAY,...base}));
 h.payload({...base,pad:'x'.repeat(LOCAL_DATA_LIMITS.replyBytes-signedSize)});
 for(let i=0;i<2;i++){const r=await h.get();assert.equal(r.status,413);assert.equal((await r.json()).reasonCode,'REPLY_TOO_LARGE');}
 h.advance(LOCAL_DATA_CACHE.freshMs);h.setMode('outage');h.online();assert.equal((await h.get()).status,413);
 // A smaller UTF-8 answer still succeeds and remains under the measured byte ceiling.
 const small=harness();small.payload({...base,pad:'é'.repeat(100)});const ok=await small.get();assert.equal(ok.status,200);assert.ok(Buffer.byteLength(await ok.text())<=LOCAL_DATA_LIMITS.replyBytes);
});
