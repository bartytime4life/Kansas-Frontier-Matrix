import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,rm,readdir,readFile,writeFile,symlink,mkdir,utimes} from 'node:fs/promises';
import {join} from 'node:path';
import {tmpdir} from 'node:os';
import {gzipSync,gunzipSync} from 'node:zlib';
import {createHostedTerrainCache,HOSTED_TERRAIN_LIMITS} from '../server/hosted-terrain-cache.mjs';
import {createLocalDataService} from '../server/local-data.mjs';
import {groundFixture} from './kansas-ground-fixtures.mjs';
import {kansasFixture} from './kansas-lidar-fixtures.mjs';
import {validGroundView} from '../scripts/local-data/ground-model.mjs';
import {newSecret,decodeSecret,signRequest,signResponse,RESPONSE_SIGNATURE_HEADER} from '../scripts/home-inference/signature.mjs';
import {LOCAL_DATA_GATEWAY} from '../scripts/local-data/protocol.mjs';
const origin='https://kansasfrontiermatrix.com',withoutCache=({cache:ignored,...v})=>{void ignored;return v;};
async function setup(t,{limits={}}={}){
 const root=await mkdtemp(join(tmpdir(),'kfm-host-terrain-'));t.after(()=>rm(root,{recursive:true,force:true}));let now=Date.now();
 const secret=decodeSecret(newSecret()),config={keyId:'host-cache-test',secret,origin},cache=createHostedTerrainCache({root,secret,origin,clock:()=>now,limits});
 return {root,secret,config,cache,clock:()=>now,tick:ms=>now+=ms,files:async()=>(await readdir(root)).filter(n=>n.endsWith('.json.gz'))};
}
function signedRelay(c,clock,answer){let calls=0;return {get calls(){return calls;},get lastSeen(){return clock();},async submit({method,path,body}){calls++;const requestHeaders=signRequest({keyId:c.keyId,secret:c.secret,method,path,body}),bytes=Buffer.from(JSON.stringify({...answer(path,JSON.parse(body)),gateway:LOCAL_DATA_GATEWAY}));return {status:200,bytes,requestHeaders,headers:new Headers({'content-type':'application/json',[RESPONSE_SIGNATURE_HEADER]:signResponse({secret:c.secret,requestHeaders,method,path,requestBody:body,status:200,body:bytes})})};}};}
const offline={lastSeen:0,submit(){throw Error('dev must not be contacted');}};
test('host cache roundtrips exact public float values in compressed copies, preserving original age and rejecting tamper/key/origin changes',async t=>{
 const c=await setup(t),f=groundFixture(),value=withoutCache(f.receipt),key='ground:'+f.requestKey,validate=v=>validGroundView(v,f.query);
 assert.ok(validate(value));assert.equal(await c.cache.write(key,value),true);const files=await c.files();assert.equal(files.length,1);
 const packed=await readFile(join(c.root,files[0]));assert.ok(packed.length<Buffer.byteLength(JSON.stringify(value))*.6);
 const hit=await c.cache.read(key,validate);assert.deepEqual(hit.value,value);assert.equal(hit.at,c.clock());
 assert.equal(await createHostedTerrainCache({root:c.root,secret:decodeSecret(newSecret()),origin,clock:c.clock}).read(key,validate),null);
 assert.equal(await createHostedTerrainCache({root:c.root,secret:c.secret,origin:'https://other.example',clock:c.clock}).read(key,validate),null);
 const record=JSON.parse(gunzipSync(packed));record.payload=record.payload.replace('350,','999,');record.at++;await writeFile(join(c.root,files[0]),gzipSync(JSON.stringify(record)));assert.equal(await c.cache.read(key,validate),null);
});
test('host cache enforces byte/entry/free-space limits without deleting data, and never stores processing/error/raw points',async t=>{
 const c=await setup(t,{limits:{entries:1}}),f=groundFixture(),value=withoutCache(f.receipt),key='ground:'+f.requestKey;assert.equal(await c.cache.write(key,value),true);const before=await c.files();
 const g=groundFixture([-96.58,38.98,-96.57,38.99]);assert.equal(await c.cache.write('ground:'+g.requestKey,withoutCache(g.receipt)),false);assert.deepEqual(await c.files(),before);
 assert.equal(await c.cache.write(key,{...value,state:'processing',grid:null}),false);assert.equal(await c.cache.write(key,{...value,state:'unavailable',grid:null}),false);assert.equal(await c.cache.write('chunk:'+'a'.repeat(64)+':0',{format:'kfm-lidar-points-chunk-v2'}),false);
 assert.equal(await createHostedTerrainCache({root:c.root,secret:c.secret,origin,clock:c.clock,limits:{bytes:1}}).write(key,value),false);
 assert.equal(await createHostedTerrainCache({root:c.root,secret:c.secret,origin,clock:c.clock,limits:{reserveBytes:Number.MAX_SAFE_INTEGER}}).write(key,value),false);
 assert.deepEqual(await c.files(),before);c.tick(HOSTED_TERRAIN_LIMITS.staleMs);assert.equal(await c.cache.read(key,v=>validGroundView(v,f.query)),null);
});
test('host cache rejects file and ancestor symlinks, oversize expansion and unsafe keys without touching outside originals',async t=>{
 const c=await setup(t),f=groundFixture(),value=withoutCache(f.receipt),key='ground:'+f.requestKey;await c.cache.write(key,value);const name=(await c.files())[0],outside=join(c.root,'outside-original');await writeFile(outside,'keep-original');await rm(join(c.root,name));await symlink(outside,join(c.root,name));assert.equal(await c.cache.read(key,()=>true),null);assert.equal(await readFile(outside,'utf8'),'keep-original');
 const alias=join(c.root,'alias');await symlink(c.root,alias);assert.equal(await createHostedTerrainCache({root:alias,secret:c.secret,origin,clock:c.clock}).write(key,value),false);
 await rm(join(c.root,name));await writeFile(join(c.root,name),gzipSync(' '.repeat(HOSTED_TERRAIN_LIMITS.entryBytes+1)));assert.equal(await c.cache.read(key,()=>true),null);
 for(const k of ['../../outside','ground:../secret','ground:'+'a'.repeat(64)+'/x'])assert.equal(await c.cache.write(k,value),false);
});
test('host cache writes serialize across instances and an old empty writer lock can recover after a crashed writer',async t=>{
 const c=await setup(t),f=groundFixture(),key='ground:'+f.requestKey,value=withoutCache(f.receipt),lock=join(c.root,'.writer-lock');await mkdir(lock);assert.equal(await c.cache.write(key,value),false);await utimes(lock,new Date(c.clock()-120000),new Date(c.clock()-120000));assert.equal(await c.cache.write(key,value),true);assert.deepEqual(await c.cache.read(key,v=>validGroundView(v,f.query)).then(v=>v.value),value);
});
test('Ground API serves persisted prepared data after a service restart with dev offline, no source mutation and truthful stale label',async t=>{
 const c=await setup(t),f=groundFixture(),value=withoutCache(f.receipt),relay=signedRelay(c.config,c.clock,()=>value),request=new Request(origin+'/api/terrain/ground?bbox='+f.query.bbox+'&size=96');
 let service=createLocalDataService({config:c.config,clock:c.clock,terrainCache:c.cache,relay});const first=await service.ground(request);assert.equal(first.status,200);assert.equal(first.headers.get('X-KFM-Terrain-Cache'),'relay');assert.equal((await first.json()).cache.state,'live');assert.equal(relay.calls,1);
 assert.equal((await(await service.ground(request)).json()).cache.state,'fresh');assert.equal(relay.calls,1);
 service=createLocalDataService({config:c.config,clock:c.clock,terrainCache:createHostedTerrainCache({root:c.root,secret:c.secret,origin,clock:c.clock}),relay:offline});const response=await service.ground(request),hit=await response.json();assert.equal(response.status,200);assert.equal(response.headers.get('X-KFM-Terrain-Cache'),'disk');assert.equal(hit.cache.state,'stale');assert.deepEqual(withoutCache(hit),value);assert.equal(relay.calls,1);
 c.tick(HOSTED_TERRAIN_LIMITS.staleMs);assert.equal((await service.ground(request)).status,503);
});
test('processing receipts remain short-lived in memory and are never persisted as a ready host result',async t=>{
 const c=await setup(t),f=groundFixture(),value={...withoutCache(f.receipt),state:'processing',grid:null},relay=signedRelay(c.config,c.clock,()=>value),service=createLocalDataService({config:c.config,clock:c.clock,terrainCache:c.cache,relay}),req=new Request(origin+'/api/terrain/ground?bbox='+f.query.bbox+'&size=96');await service.ground(req);assert.equal((await c.files()).length,0);c.tick(2001);await service.ground(req);assert.equal(relay.calls,2);
});
test('native manifest and compact grid restore together after restart; grid is bound to the exact parent receipt',async t=>{
 const c=await setup(t),f=kansasFixture(['surface','canopy']),view=withoutCache(f.receipt),grid=withoutCache(f.grid),relay=signedRelay(c.config,c.clock,path=>path.endsWith('/grid')?grid:view),request=new Request(origin+'/api/lidar/view?bbox='+f.query.bbox+'&zoom='+f.query.zoom+'&layers='+f.query.layers),artifact=new Request(origin+'/api/lidar/view/'+f.key+'/grid');
 let service=createLocalDataService({config:c.config,clock:c.clock,terrainCache:c.cache,relay});assert.equal((await service.lidarView(request)).status,200);assert.equal((await service.lidarViewArtifact(artifact,f.key,'grid')).status,200);assert.equal(relay.calls,2);assert.equal((await c.files()).length,2);
 service=createLocalDataService({config:c.config,clock:c.clock,terrainCache:createHostedTerrainCache({root:c.root,secret:c.secret,origin,clock:c.clock}),relay:offline});const result=await(await service.lidarViewArtifact(artifact,f.key,'grid')).json();assert.deepEqual(withoutCache(result),grid);assert.equal(result.cache.state,'stale');
 const altered={...view,generatedAt:'2026-11-24T07:00:00Z'};await c.cache.write('view:'+f.key,altered);service=createLocalDataService({config:c.config,clock:c.clock,terrainCache:createHostedTerrainCache({root:c.root,secret:c.secret,origin,clock:c.clock}),relay:offline});assert.equal((await service.lidarViewArtifact(artifact,f.key,'grid')).status,503);
});
test('one-instance concurrent writes are bounded and serialized so different visitors keep independent reusable copies',async t=>{
 const c=await setup(t),fixtures=Array.from({length:5},(_,i)=>groundFixture([-96.58+i*.01,38.98,-96.575+i*.01,38.985]));const outcomes=await Promise.all(fixtures.map(f=>c.cache.write('ground:'+f.requestKey,withoutCache(f.receipt))));assert.deepEqual(outcomes,[true,true,true,true,true]);assert.equal((await c.files()).length,5);
});
test('the versioned whole-Kansas baseline serves exact saved data without dev, retains dated provenance, and is not substituted for a different footprint',async t=>{
 const {readGroundBaseline,GROUND_BASELINE}=await import('../server/terrain-baseline.mjs'),c=await setup(t),baseline=await readGroundBaseline('ground:'+GROUND_BASELINE.key);assert.ok(baseline);assert.equal(baseline.bytes,195650);assert.equal(baseline.value.grid.ground.length,9216);assert.equal(baseline.value.grid.source.provider,'USGS');assert.equal(baseline.value.grid.review.scientific_accuracy_verified,false);
 const service=createLocalDataService({config:c.config,clock:()=>c.clock()+8*86400000,terrainCache:c.cache,groundBaseline:readGroundBaseline,relay:offline}),request=new Request(origin+'/api/terrain/ground?bbox='+GROUND_BASELINE.query.bbox+'&size=96'),response=await service.ground(request),v=await response.json();assert.equal(response.status,200);assert.equal(response.headers.get('X-KFM-Terrain-Cache'),'baseline');assert.equal(v.cache.state,'stale');assert.deepEqual(withoutCache(v),baseline.value);
 assert.equal(await readGroundBaseline('ground:'+'b'.repeat(64)),null);assert.equal(await readGroundBaseline('ground:'+GROUND_BASELINE.key,{root:c.root}),null);assert.equal((await service.ground(new Request(origin+'/api/terrain/ground?bbox=-97,38,-96,39&size=96'))).status,503);
});
