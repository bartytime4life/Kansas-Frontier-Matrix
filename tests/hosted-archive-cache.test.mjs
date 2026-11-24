import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,rm,readdir,readFile,writeFile} from 'node:fs/promises';
import {join} from 'node:path';
import {tmpdir} from 'node:os';
import {gzipSync,gunzipSync} from 'node:zlib';
import {DATASETS} from '../scripts/local-data/datasets.mjs';
import {RECOVERED_COLLECTIONS} from '../scripts/local-data/recovered.mjs';
import {createHostedArchiveCache,archiveCacheKey,validArchiveAnswer,HOSTED_ARCHIVE_LIMITS} from '../server/hosted-archive-cache.mjs';
import {createHostedTerrainCache} from '../server/hosted-terrain-cache.mjs';
import {createLocalDataService} from '../server/local-data.mjs';
import {newSecret,decodeSecret,signRequest,signResponse,RESPONSE_SIGNATURE_HEADER} from '../scripts/home-inference/signature.mjs';
import {LOCAL_DATA_GATEWAY} from '../scripts/local-data/protocol.mjs';
const origin='https://kansasfrontiermatrix.com';
async function setup(t,limits={}){
 const root=await mkdtemp(join(tmpdir(),'kfm-host-archive-'));t.after(()=>rm(root,{recursive:true,force:true}));let now=Date.now();
 const secret=decodeSecret(newSecret()),config={keyId:'archive-test',secret,origin},options={root,secret,origin,clock:()=>now,limits};
 return {root,config,options,cache:createHostedArchiveCache(options),clock:()=>now,tick:ms=>now+=ms,files:async()=>(await readdir(root)).filter(n=>n.endsWith('.json.gz'))};
}
function fixture(id='ghcndex-indices',input={}){
 const d=DATASETS.get(id),query=d.parse(input),rows=id==='ghcndex-indices'?[{code:'TN10p',definition:'Cool nights',unit:'%'}]:[];
 const v={format:d.format??'kfm-local-data-v1',dataset:id,query,total:rows.length,count:rows.length,rows,source:d.source,generatedAt:'2026-11-20T12:00:00.000Z'};
 if(id.startsWith('recovered-')){const c=RECOVERED_COLLECTIONS.find(c=>c.id===query.collection);Object.assign(v,{total:null,collection:c.id,hasMore:false,nextCursor:null,columns:c.columns,coverage:'One record page',geometryField:c.geometry});}
 return v;
}
function signedRelay(c,clock,value){let calls=0;return {get calls(){return calls;},get lastSeen(){return clock();},async submit({method,path,body}){calls++;const requestHeaders=signRequest({keyId:c.keyId,secret:c.secret,method,path,body}),bytes=Buffer.from(JSON.stringify({...value,gateway:LOCAL_DATA_GATEWAY}));return {status:200,bytes,requestHeaders,headers:new Headers({'content-type':'application/json',[RESPONSE_SIGNATURE_HEADER]:signResponse({secret:c.secret,requestHeaders,method,path,requestBody:body,status:200,body:bytes})})};}};}
const offline={lastSeen:0,submit(){assert.fail('offline must not submit');}};
const stripped=({cache,...v})=>v;
test('public archive answers survive restart, retain exact source values and original times, and expire without refreshing their own age',async t=>{
 const c=await setup(t),value=fixture(),relay=signedRelay(c.config,c.clock,value),req=new Request(origin+'/api/local-data/ghcndex-indices');
 const make=rel=>createLocalDataService({config:c.config,clock:c.clock,archiveCache:createHostedArchiveCache(c.options),relay:rel});
 let service=make(relay),first=await service.query(req,value.dataset),body=await first.json();assert.equal(first.headers.get('X-KFM-Data-Cache'),'relay');assert.deepEqual(stripped(body),value);assert.equal(relay.calls,1);
 let warm=await service.query(req,value.dataset);assert.equal(warm.headers.get('X-KFM-Data-Cache'),'memory');assert.equal(relay.calls,1);
 service=make(offline);const disk=await service.query(req,value.dataset),saved=await disk.json();assert.equal(disk.status,200);assert.equal(disk.headers.get('X-KFM-Data-Cache'),'disk');assert.equal(saved.cache.state,'stale');assert.equal(saved.cache.at,body.cache.at);assert.deepEqual(stripped(saved),value);
 c.tick(HOSTED_ARCHIVE_LIMITS.staleMs);assert.equal((await make(offline).query(req,value.dataset)).status,503);
});
test('online restart reuses fresh disk result, and expired freshness revalidates once for simultaneous visitors',async t=>{
 const c=await setup(t),v=fixture(),key=archiveCacheKey(v.dataset,v.query),relay=signedRelay(c.config,c.clock,v),req=new Request(origin+'/api/local-data/ghcndex-indices');await c.cache.write(key,v,c.clock());
 const service=createLocalDataService({config:c.config,clock:c.clock,archiveCache:c.cache,relay});assert.equal((await(await service.query(req,v.dataset)).json()).cache.state,'fresh');assert.equal(relay.calls,0);
 c.tick(HOSTED_ARCHIVE_LIMITS.freshMs+1);await Promise.all(Array.from({length:8},()=>service.query(req,v.dataset)));assert.equal(relay.calls,1);
});
test('only public shared first pages are eligible; searches, locations, cursors, long fields, live observations and pending datasets are excluded',()=>{
 for(const id of ['ghcn-stations','wind-stations','ghcndex-indices']){const v=fixture(id);assert.ok(validArchiveAnswer(v));assert.ok(archiveCacheKey(id,v.query));}
 for(const id of ['recovered-bulk','recovered-observations']){const c=RECOVERED_COLLECTIONS.find(c=>c.database===id.slice(10)),v=fixture(id,{collection:c.id});assert.ok(validArchiveAnswer(v));assert.ok(archiveCacheKey(id,v.query));for(const changed of [{after:['x']},{record:['x'],field:c.columns[0]},{start:1}])assert.equal(archiveCacheKey(id,{...v.query,...changed}),null);}
 for(const id of ['archive-search','near-bulk','near-observations','nws-alerts','usgs-streamflow','story-bundles','storm-events'])assert.equal(archiveCacheKey(id,{}),null);
 const stations=fixture('ghcn-stations');for(const change of [{name:'WICHITA'},{bbox:{west:-97.2,east:-97.1,south:38,north:39}},{offset:100},{limit:501},{arbitrary:'x'}])assert.equal(archiveCacheKey(stations.dataset,{...stations.query,...change}),null);
});
test('public disk cache binds source, dataset, normalized query, version, origin and secret; malformed or altered copies are misses',async t=>{
 const c=await setup(t),v=fixture(),key=archiveCacheKey(v.dataset,v.query);assert.equal(await c.cache.write(key,v),true);
 assert.deepEqual((await c.cache.read(key,validArchiveAnswer)).value,v);
 assert.equal(await c.cache.write(key,{...v,dataset:'wind-stations'}),false);assert.equal(await c.cache.write(key,{...v,source:{provider:'invented'}}),false);assert.equal(await c.cache.write(key,{...v,count:2}),false);assert.equal(await c.cache.write(key,{...v,private:'secret'}),false);
 assert.equal(await createHostedArchiveCache({...c.options,secret:decodeSecret(newSecret())}).read(key,validArchiveAnswer),null);
 assert.equal(await createHostedArchiveCache({...c.options,origin:'https://other.example'}).read(key,validArchiveAnswer),null);
 assert.equal(await createHostedTerrainCache(c.options).read(key,()=>true),null);
 const path=join(c.root,(await c.files())[0]),record=JSON.parse(gunzipSync(await readFile(path)));record.payload=record.payload.replace('Cool nights','Fabricated');await writeFile(path,gzipSync(JSON.stringify(record)));assert.equal(await c.cache.read(key,validArchiveAnswer),null);
});
test('host archive storage bounds degrade to normal relay service without deleting sources',async t=>{
 const c=await setup(t,{bytes:1}),v=fixture(),relay=signedRelay(c.config,c.clock,v),req=new Request(origin+'/api/local-data/ghcndex-indices');
 const service=createLocalDataService({config:c.config,clock:c.clock,archiveCache:c.cache,relay});assert.equal((await service.query(req,v.dataset)).status,200);assert.equal((await c.files()).length,0);
});

test('enabling archive storage preserves live catalogue health and never persists the raw health envelope',async t=>{
 const c=await setup(t),value={ok:true,datasets:[],collections:{},generatedAt:'2026-11-24T00:00:00.000Z'},relay=signedRelay(c.config,c.clock,value);
 const service=createLocalDataService({config:c.config,clock:c.clock,archiveCache:c.cache,relay});const response=await service.catalog(new Request(origin+'/api/local-data')),body=await response.json();
 assert.equal(response.status,200);assert.equal(body.online,true);assert.equal(body.status.state,'live');assert.equal(body.status.generatedAt,value.generatedAt);assert.equal(relay.calls,1);assert.equal((await c.files()).length,0);
});
