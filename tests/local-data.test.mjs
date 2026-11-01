import test from 'node:test';
import assert from 'node:assert/strict';
import {DatabaseSync} from 'node:sqlite';
import {mkdtemp,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {newSecret,decodeSecret,signRequest,verifyResponse,RESPONSE_SIGNATURE_HEADER} from '../scripts/home-inference/signature.mjs';
import {validLease} from '../scripts/home-inference/worker.mjs';
import {createHomeRelay} from '../server/home-relay.mjs';
import {LOCAL_DATA_ROUTES,LOCAL_DATA_LIMITS} from '../scripts/local-data/protocol.mjs';
import {parseStormQuery,stormEvent} from '../scripts/local-data/storm-events.mjs';
import {createGateway,startGateway} from '../scripts/local-data/gateway.mjs';
import {createLocalDataWorker} from '../scripts/local-data/worker.mjs';
import {localDataConfig,createLocalDataService,localDataStormEventsRuntime,localDataWorkerRuntime,LOCAL_DATA_CACHE,LOCAL_DATA_RELAY_LIMITS,LOCAL_DATA_WORKER_PREFIX} from '../server/local-data.mjs';

const SITE='https://kansasfrontiermatrix.com';
const gatewaySecret=newSecret(),workerSecret=newSecret();
const COLUMNS=['event_id','episode_id','event_type','cz_type','cz_fips','cz_name','wfo','begin_yearmonth','begin_day','begin_time',
 'end_yearmonth','end_day','end_time','cz_timezone','injuries_direct','injuries_indirect','deaths_direct','deaths_indirect',
 'damage_property','damage_crops','source','magnitude','magnitude_type','flood_cause','category','tor_f_scale','tor_length','tor_width',
 'begin_range','begin_azimuth','begin_location','end_range','end_azimuth','end_location','begin_lat','begin_lon','end_lat','end_lon',
 'episode_narrative','event_narrative','data_source'];
const row=fields=>({event_id:'1',episode_id:'10',event_type:'Hail',cz_type:'C',cz_fips:'173',cz_name:'SEDGWICK',wfo:'ICT',begin_yearmonth:'202405',begin_day:'3',
 begin_time:'1530',end_yearmonth:'202405',end_day:'3',end_time:'1545',cz_timezone:'CST-6',injuries_direct:'0',injuries_indirect:'0',deaths_direct:'0',deaths_indirect:'0',
 damage_property:'10.00K',damage_crops:'0.00K',source:'Trained Spotter',magnitude:'1.75',magnitude_type:'',flood_cause:'',category:'',tor_f_scale:'',tor_length:'',tor_width:'',
 begin_range:'2',begin_azimuth:'N',begin_location:'WICHITA',end_range:'',end_azimuth:'',end_location:'',begin_lat:'37.7',begin_lon:'-97.3',end_lat:'',end_lon:'',
 episode_narrative:'Storms moved east.',event_narrative:'Hail fell.',data_source:'CSV',...fields});

// A small Storm Events table shaped like the PC's observations.sqlite (TEXT columns as loaded from the CSVs).
async function fixtureDb(t,{bulk=0,narrative=''}={}){
 const dir=await mkdtemp(join(tmpdir(),'kfm-local-data-'));t.after(()=>rm(dir,{recursive:true,force:true}));
 const path=join(dir,'observations.sqlite'),db=new DatabaseSync(path);
 db.exec(`CREATE TABLE kfm_storm_event_details(${COLUMNS.map(c=>`"${c}" TEXT`).join(',')},"fatality_note" TEXT)`);
 const insert=db.prepare(`INSERT INTO kfm_storm_event_details(${COLUMNS.map(c=>`"${c}"`).join(',')}) VALUES(${COLUMNS.map(()=>'?').join(',')})`);
 const add=fields=>{const r=row(fields);insert.run(...COLUMNS.map(c=>r[c]));};
 add({event_id:'1001',event_type:'Tornado',begin_yearmonth:'202606',begin_day:'21',begin_time:'14',end_yearmonth:'202606',end_day:'21',end_time:'20',tor_f_scale:'EF1',tor_length:'2.1',tor_width:'150'});
 add({event_id:'1002'});
 add({event_id:'1003',event_type:'Tornado',cz_fips:'45',cz_name:'DOUGLAS',begin_yearmonth:'201905',begin_day:'28',begin_time:'1800'});
 add({event_id:'1004',event_type:'Winter Storm',cz_type:'Z',cz_fips:'83',cz_name:'SEDGWICK',begin_yearmonth:'202301',begin_day:'9',begin_time:'600'});
 for(let i=0;i<bulk;i++)add({event_id:String(5000+i),event_type:'Blizzard',cz_fips:'51',cz_name:'ELLIS',begin_yearmonth:'201101',begin_day:'31',begin_time:String(i),episode_narrative:narrative,event_narrative:narrative});
 db.close();
 return path;
}

const signed=(path,body='',{keyId='data-gw-1',secret=gatewaySecret,method=path==='/v1/health'?'GET':'POST'}={})=>({method,path,body,headers:{...signRequest({keyId,secret,method,path,body}),...(body?{'content-type':'application/json'}:{})}});
const parse=answer=>JSON.parse(answer.body.toString('utf8'));
const verified=(request,answer)=>verifyResponse({secret:decodeSecret(gatewaySecret),requestHeaders:request.headers,method:request.method,path:request.path,requestBody:request.body,status:answer.status,body:answer.body,headers:{[RESPONSE_SIGNATURE_HEADER]:answer.signature}});

test('storm queries are normalized and anything else is refused',()=>{
 assert.deepEqual(parseStormQuery({}),{county:null,from:'1950-01-01',to:'2100-12-31',type:null,limit:50,offset:0});
 assert.deepEqual(parseStormQuery({county:' sedgwick ',type:'tornado',from:'2020-01-01',limit:'200'}),{county:{name:'SEDGWICK'},from:'2020-01-01',to:'2100-12-31',type:'TORNADO',limit:200,offset:0});
 assert.deepEqual(parseStormQuery({county:'173'}).county,{fips:173});
 for(const bad of [{state:'KS'},{county:"1; DROP TABLE x"},{county:'SEDGWICK%'},{from:'2020-13-01'},{from:'2021-01-01',to:'2020-01-01'},{limit:'0'},{limit:'201'},{offset:'-1'},{offset:'50001'},{type:'HAIL;'},null,[]])
  assert.throws(()=>parseStormQuery(bad),{code:'QUERY_INVALID'},JSON.stringify(bad));
});

test('a public event carries allow-listed fields only, with zero-padded times',()=>{
 const event=stormEvent({...row({begin_time:'14',event_type:'Tornado',tor_f_scale:'EF1',tor_length:'2.1'}),fatality_note:'private'});
 assert.deepEqual(event.begin,{date:'2024-05-03',time:'00:14',timezone:'CST-6'});
 assert.deepEqual(event.tornado,{scale:'EF1',lengthMiles:2.1,widthYards:null});
 assert.equal(JSON.stringify(event).includes('private'),false);
 assert.deepEqual(Object.keys(event).sort(),['area','begin','category','damage','dataSource','deaths','end','episodeId','eventId','floodCause','injuries','location','magnitude','narrative','office','source','tornado','type'].sort());
});

test('the gateway answers signed questions read-only and signs every reply',async t=>{
 const dbPath=await fixtureDb(t),handle=createGateway({keyId:'data-gw-1',secret:gatewaySecret,dbPath});
 const health=signed('/v1/health'),healthy=handle(health);
 assert.equal(healthy.status,200);assert.ok(verified(health,healthy));
 assert.deepEqual(parse(healthy),{gateway:'kfm-local-data/1',ok:true,datasets:['storm-events'],stormEvents:4});

 const byFips=signed('/v1/data/storm-events',JSON.stringify({county:173})),fips=handle(byFips),fipsBody=parse(fips);
 assert.equal(fips.status,200);assert.ok(verified(byFips,fips));
 // County FIPS matches counties only, newest first; the zone that shares the name is left out.
 assert.deepEqual(fipsBody.events.map(e=>e.eventId),[1001,1002]);
 assert.equal(fipsBody.total,2);assert.equal(fipsBody.format,'kfm-local-data-storm-events-v1');
 assert.deepEqual(parse(handle(signed('/v1/data/storm-events',JSON.stringify({county:'Sedgwick'})))).events.map(e=>e.eventId),[1001,1002,1004]);
 assert.deepEqual(parse(handle(signed('/v1/data/storm-events',JSON.stringify({type:'Tornado',from:'2020-01-01'})))).events.map(e=>e.eventId),[1001]);
 const paged=parse(handle(signed('/v1/data/storm-events',JSON.stringify({limit:1,offset:1}))));
 assert.equal(paged.total,4);assert.deepEqual(paged.events.map(e=>e.eventId),[1002]);

 // A replayed request, a forged key, a bad query and an unknown route each get one fixed answer, still signed.
 const replay=handle(byFips);assert.equal(replay.status,401);assert.equal(parse(replay).error,'UNAUTHORIZED');
 assert.equal(handle(signed('/v1/health','',{secret:newSecret()})).status,401);
 assert.equal(handle({method:'GET',path:'/v1/health',headers:{},body:''}).status,401);
 const bad=signed('/v1/data/storm-events',JSON.stringify({county:'1 OR 1=1'})),refused=handle(bad);
 assert.equal(refused.status,400);assert.ok(verified(bad,refused));
 assert.equal(handle(signed('/v1/chat','{}')).status,404);
 assert.equal(handle(signed('/v1/health','',{method:'POST'})).status,404);
 assert.equal(handle(signed('/v1/health','',{keyId:'data-gw-1'})).status,200);
});

test('the gateway refuses a page larger than the reply ceiling and reports a missing database',async t=>{
 const dbPath=await fixtureDb(t,{bulk:200,narrative:'x'.repeat(3000)}),handle=createGateway({keyId:'data-gw-1',secret:gatewaySecret,dbPath});
 const big=handle(signed('/v1/data/storm-events',JSON.stringify({type:'Blizzard',limit:200})));
 assert.equal(big.status,413);assert.equal(parse(big).error,'REPLY_TOO_LARGE');
 const gone=createGateway({keyId:'data-gw-1',secret:gatewaySecret,dbPath:join(tmpdir(),'kfm-missing-'+Date.now()+'.sqlite')});
 assert.equal(gone(signed('/v1/health')).status,503);
});

test('site configuration needs the flag, an exact https origin and two different keys',()=>{
 const env={KFM_LOCAL_DATA:'1',KFM_LOCAL_DATA_ORIGIN:SITE,KFM_LOCAL_DATA_GATEWAY_KEY_ID:'data-gw-1',KFM_LOCAL_DATA_GATEWAY_SECRET:gatewaySecret,KFM_LOCAL_DATA_WORKER_KEY_ID:'data-worker-1',KFM_LOCAL_DATA_WORKER_SECRET:workerSecret};
 assert.equal(localDataConfig(env).origin,SITE);
 assert.throws(()=>localDataConfig({...env,KFM_LOCAL_DATA:'0'}),{code:'LOCAL_DATA_OFF'});
 // Only the controlled hosting origins: www redirects to the apex, so a worker polling it would never connect.
 for(const origin of ['https://www.kansasfrontiermatrix.com','http://kansasfrontiermatrix.com',SITE+'/',SITE+'/api','https://urdng3v1vk.preview.example','',undefined])
  assert.throws(()=>localDataConfig({...env,KFM_LOCAL_DATA_ORIGIN:origin}),{code:'LOCAL_DATA_ORIGIN_INVALID'},String(origin));
 assert.throws(()=>localDataConfig({...env,KFM_LOCAL_DATA_WORKER_SECRET:gatewaySecret}),{code:'LOCAL_DATA_KEY_REUSED'});
 assert.throws(()=>localDataConfig({...env,KFM_LOCAL_DATA_GATEWAY_SECRET:'short'}),{code:'LOCAL_DATA_KEY_INVALID'});
 assert.throws(()=>localDataConfig({...env,KFM_LOCAL_DATA_WORKER_KEY_ID:'bad id'}),{code:'LOCAL_DATA_KEY_INVALID'});
});

test('routes stay off unless configured, and the worker route answers only on the configured origin',async()=>{
 const off=await (localDataStormEventsRuntime({}))(new Request(SITE+'/api/local-data/storm-events'));
 assert.equal(off.status,404);assert.equal((await off.json()).reasonCode,'LOCAL_DATA_OFF');
 assert.equal((await (localDataWorkerRuntime({}))(new Request(SITE+LOCAL_DATA_WORKER_PREFIX+'/lease',{method:'POST'}))).status,404);
 const env={KFM_LOCAL_DATA:'1',KFM_LOCAL_DATA_ORIGIN:SITE,KFM_LOCAL_DATA_GATEWAY_KEY_ID:'data-gw-1',KFM_LOCAL_DATA_GATEWAY_SECRET:gatewaySecret,KFM_LOCAL_DATA_WORKER_KEY_ID:'data-worker-1',KFM_LOCAL_DATA_WORKER_SECRET:workerSecret};
 try{
  const worker=localDataWorkerRuntime(env);
  assert.equal((await worker(new Request('https://urdng3v1vk.preview.example'+LOCAL_DATA_WORKER_PREFIX+'/lease',{method:'POST',body:'{}'}))).status,503);
  assert.equal((await worker(new Request(SITE+LOCAL_DATA_WORKER_PREFIX+'/lease',{method:'POST',body:'{}'}))).status,401);
 }finally{delete globalThis[Symbol.for('kfm.local-data')];}
});

// The website, relay, worker and loopback gateway together; only the website is simulated in-process.
async function link(t,{dbPath,tamper=false}){
 let now=Date.now();const clock=()=>now;
 const config=localDataConfig({KFM_LOCAL_DATA:'1',KFM_LOCAL_DATA_ORIGIN:SITE,KFM_LOCAL_DATA_GATEWAY_KEY_ID:'data-gw-1',KFM_LOCAL_DATA_GATEWAY_SECRET:gatewaySecret,KFM_LOCAL_DATA_WORKER_KEY_ID:'data-worker-1',KFM_LOCAL_DATA_WORKER_SECRET:workerSecret});
 const relay=createHomeRelay({keyId:config.keyId,secret:config.secret,worker:config.worker,clock,limits:{...LOCAL_DATA_RELAY_LIMITS,leaseWaitMs:150},routes:LOCAL_DATA_ROUTES,workerPrefix:LOCAL_DATA_WORKER_PREFIX,diagnostic:()=>{}});
 const service=createLocalDataService({config,relay,clock});
 const server=await startGateway({host:'127.0.0.1',port:0,keyId:'data-gw-1',secret:gatewaySecret,dbPath});
 const gateway='http://127.0.0.1:'+server.address().port,trips=[];
 const transport=async(url,init)=>{
  if(url.startsWith(SITE))return relay.handler(new Request(url,init));
  trips.push(new URL(url).pathname);
  const response=await fetch(url,init);
  if(!tamper)return response;
  // A worker that alters a reply in transit: the website must notice.
  const text=(await response.text()).replaceAll('SEDGWICK','DOUGLAS');
  return new Response(text,{status:response.status,headers:response.headers});
 };
 const worker=createLocalDataWorker({site:SITE,gateway,keyId:'data-worker-1',secret:decodeSecret(workerSecret)},{fetchImpl:transport,log:()=>{}});
 const stop=new AbortController(),running=worker.run(stop.signal);
 const halt=async()=>{if(stop.signal.aborted)return;stop.abort();await running;};
 t.after(async()=>{await halt();server.closeAllConnections?.();await new Promise(resolve=>server.close(resolve));});
 while(relay.lastSeen===0)await new Promise(resolve=>setTimeout(resolve,10));
 const get=query=>service.stormEvents(new Request(SITE+'/api/local-data/storm-events?'+query));
 return {service,relay,trips,get,halt,advance:ms=>{now+=ms;}};
}

test('a public storm-events request travels to the PC and back, then is served from cache',async t=>{
 const {get,trips,service}=await link(t,{dbPath:await fixtureDb(t)});
 const live=await get('county=173');
 assert.equal(live.status,200);assert.equal(live.headers.get('cache-control'),'public, max-age=300');
 const body=await live.json();
 assert.equal(body.cache.state,'live');assert.deepEqual(body.events.map(e=>e.eventId),[1001,1002]);
 assert.equal('gateway' in body,false);assert.equal(body.source.provider,'NOAA NCEI Storm Events Database');
 const again=await (await get('county=173')).json();
 assert.equal(again.cache.state,'fresh');assert.deepEqual(trips,['/v1/data/storm-events']);

 // Identical questions in flight together make one trip.
 const [a,b]=await Promise.all([get('county=sedgwick&type=tornado'),get('type=Tornado&county=SEDGWICK')]);
 assert.equal(a.status,200);assert.equal(b.status,200);assert.equal(trips.length,2);
 assert.equal((await get('county=1%3BDROP')).status,400);
 assert.equal((await get('state=KS')).status,400);
 assert.equal((await get('limit=500')).status,400);
 assert.equal((await service.stormEvents(new Request(SITE+'/api/local-data/storm-events',{method:'POST',body:'{}'}))).status,405);
 assert.equal(trips.length,2);
});

test('a full page of long narratives fits through the relay',async t=>{
 const {get}=await link(t,{dbPath:await fixtureDb(t,{bulk:120,narrative:'Heavy snow and wind. '.repeat(75)})});
 const response=await get('type=blizzard&limit=120'),body=await response.json();
 assert.equal(response.status,200);assert.equal(body.count,120);assert.equal(body.total,120);
 assert.ok(JSON.stringify(body).length>LOCAL_DATA_LIMITS.replyBytes/3,'the page exceeds the chat relay ceiling');
});

test('when the PC goes away the last answer is served marked stale, then a plain offline state',async t=>{
 const {get,halt,advance}=await link(t,{dbPath:await fixtureDb(t)});
 assert.equal((await (await get('county=45')).json()).cache.state,'live');
 await halt();
 advance(LOCAL_DATA_CACHE.freshMs+1000);
 const started=Date.now(),stale=await get('county=45'),body=await stale.json();
 assert.ok(Date.now()-started<1000,'an absent worker is known at once, not after a relay timeout');
 assert.equal(stale.status,200);assert.equal(body.cache.state,'stale');assert.equal(stale.headers.get('cache-control'),'public, max-age=60');
 assert.deepEqual(body.events.map(e=>e.eventId),[1003]);
 const never=await get('county=173');
 assert.equal(never.status,503);assert.deepEqual(await never.json(),{state:'local-data-offline',reasonCode:'LOCAL_DATA_UNAVAILABLE'});
 advance(LOCAL_DATA_CACHE.staleMs);
 assert.equal((await get('county=45')).status,503);
});

test('a reply altered between the PC and the website is refused and never cached',async t=>{
 const {get}=await link(t,{dbPath:await fixtureDb(t),tamper:true});
 const response=await get('county=sedgwick');
 assert.equal(response.status,503);assert.equal((await response.json()).reasonCode,'LOCAL_DATA_UNAVAILABLE');
 assert.equal((await get('county=sedgwick')).status,503);
});

test('the data relay and the chat relay cannot carry each other\'s traffic',async t=>{
 // The relay's long-poll timer is unref'd; keep the loop alive while a poll is held.
 const alive=setInterval(()=>{},1000);t.after(()=>clearInterval(alive));
 const config=localDataConfig({KFM_LOCAL_DATA:'1',KFM_LOCAL_DATA_ORIGIN:SITE,KFM_LOCAL_DATA_GATEWAY_KEY_ID:'data-gw-1',KFM_LOCAL_DATA_GATEWAY_SECRET:gatewaySecret,KFM_LOCAL_DATA_WORKER_KEY_ID:'data-worker-1',KFM_LOCAL_DATA_WORKER_SECRET:workerSecret});
 const relay=createHomeRelay({keyId:config.keyId,secret:config.secret,worker:config.worker,limits:{...LOCAL_DATA_RELAY_LIMITS,leaseWaitMs:50},routes:LOCAL_DATA_ROUTES,workerPrefix:LOCAL_DATA_WORKER_PREFIX,diagnostic:()=>{}});
 const post=(path,{secret=workerSecret,keyId='data-worker-1'}={})=>{const body='{}';return relay.handler(new Request(SITE+path,{method:'POST',headers:{...signRequest({keyId,secret,method:'POST',path,body}),'Content-Type':'application/json'},body}));};
 assert.equal((await post('/api/home-worker/v1/lease')).status,404);
 assert.equal((await post(LOCAL_DATA_WORKER_PREFIX+'/lease',{secret:newSecret()})).status,401);
 assert.equal((await post(LOCAL_DATA_WORKER_PREFIX+'/lease')).status,204);
 await assert.rejects(relay.submit({method:'POST',path:'/v1/chat',body:'{}',timeoutMs:1000}),{code:'GATEWAY_RESPONSE_INVALID'});
 const lease=path=>({leaseId:'a'.repeat(24),request:{method:'POST',path,headers:{},body:'{}'}});
 assert.equal(validLease(lease('/v1/chat'),LOCAL_DATA_ROUTES),false);
 assert.equal(validLease(lease('/v1/data/storm-events'),LOCAL_DATA_ROUTES),true);
 assert.equal(validLease(lease('/v1/data/storm-events')),false);
});
