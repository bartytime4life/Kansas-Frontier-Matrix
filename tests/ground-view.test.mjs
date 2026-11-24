import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtempSync,chmodSync,rmSync,readdirSync,writeFileSync,readFileSync,symlinkSync} from 'node:fs';
import {join} from 'node:path';
import {tmpdir} from 'node:os';
import {GROUND_ROUTE,GROUND_SERVICE,normalizeGroundQuery,parseGroundSearch,groundKey,groundBounds,groundSourceUrl,groundCatalogUrl,validGroundView} from '../scripts/local-data/ground-model.mjs';
import {groundConfig,groundAtomic,initialGround,requestGround} from '../scripts/local-data/ground-store.mjs';
import {groundSource,catalogCandidates,GROUND_LIMITS} from '../scripts/local-data/ground-worker.mjs';
import {createGateway} from '../scripts/local-data/gateway.mjs';
import {createLocalDataService} from '../server/local-data.mjs';
import {newSecret,decodeSecret,signRequest,RESPONSE_SIGNATURE_HEADER} from '../scripts/home-inference/signature.mjs';
import {LOCAL_DATA_ROUTES,LOCAL_DATA_LIMITS} from '../scripts/local-data/protocol.mjs';
const query=()=>({bbox:[-97.35,37.68,-97.34,37.69],size:96}),stamp='2026-11-24T05:00:00.000Z',sha='sha256:'+'a'.repeat(64);
function config(t){const root=mkdtempSync(join(tmpdir(),'kfm-ground-test-'));chmodSync(root,0o700);t.after(()=>rmSync(root,{recursive:true,force:true}));return {root};}
function fixture(q=query()){
 // Synthetic schema/transport data only, never claimed as captured elevations.
 const key=groundKey(q),b=groundBounds(q);return {...initialGround(q),generatedAt:stamp,state:'ready',grid:{format:'kfm-3dep-ground-grid-v1',requestKey:key,width:96,height:96,bounds3857:b,cellSize3857:[(b[2]-b[0])/96,(b[3]-b[1])/96],ground:Array(9216).fill(Math.fround(301.125)),excludedValues:0,source:{provider:'USGS',service:GROUND_SERVICE,requestUrl:groundSourceUrl(q),sha256:sha,bytes:66682,retrievedAt:stamp,horizontalCrs:'EPSG:3857',verticalReference:'Synthetic schema data; no field accuracy',acquisition:'Synthetic schema data; not observations',catalog:{state:'unavailable',url:groundCatalogUrl(q),sha256:null,bytes:0,retrievedAt:null,complete:false,candidateCount:0,candidates:[]}},method:{sampling:'nearest-neighbor',output:'provider-resampled-F32-DEM',nativeResolution:'mixed; output spacing is not native resolution',catalogRole:'intersecting candidates, not per-cell lineage',limitations:['Synthetic transport fixture only']},review:{status:'pending',source_admitted:false,released:false,scientific_accuracy_verified:false}}};
}
function ready(c,q=query(),value=fixture(q)){requestGround(c,q);const key=groundKey(q),dir=join(c.root,'jobs',key),hash=groundAtomic(dir,'view.json',value);groundAtomic(dir,'ready.json',{requestKey:key,sha256:hash,completedAt:stamp});return value;}
test('Ground query canonicalizes only the fixed Kansas view, size and endpoint',()=>{
 const q=query();assert.deepEqual(parseGroundSearch(new URLSearchParams('bbox=-97.35,37.68,-97.34,37.69&size=96')),q);assert.match(groundKey(q),/^[a-f0-9]{64}$/);assert.equal(groundKey({...q,bbox:[-97.35000001,37.68,-97.34,37.69]}),groundKey(q));
 for(const v of [{...q,size:128},{...q,bbox:[-180,30,180,50]},{...q,bbox:[-97.34,37.68,-97.35,37.69]},{...q,url:'file:///secret'},{...q,bbox:[NaN,37,-96,38]}])assert.throws(()=>normalizeGroundQuery(v));
 for(const s of ['bbox=-97,37,-96,38&size=96&size=96','bbox=-97,37,-96,38&size=96&url=evil','bbox=-97,37,-96,38&size=Infinity'])assert.throws(()=>parseGroundSearch(new URLSearchParams(s)));
 const url=new URL(groundSourceUrl(q));assert.equal(url.origin,'https://elevation.nationalmap.gov');for(const [k,v] of Object.entries({format:'tiff',pixelType:'F32',interpolation:'RSP_NearestNeighbor',adjustAspectRatio:'false',bboxSR:'3857',imageSR:'3857'}))assert.equal(url.searchParams.get(k),v);assert.equal(url.searchParams.has('renderingRule'),false);assert.equal(groundConfig({KFM_GROUND_VIEW_ROOT:'relative'}),null);
});
test('Ground schema binds every numeric cell to the actual view geometry and honest provenance',()=>{
 const v=fixture();assert.equal(validGroundView(v,query()),true);
 const changes=[v=>v.requestKey='0'.repeat(64),v=>v.grid.bounds3857[0]+=1,v=>v.grid.cellSize3857[0]*=2,v=>v.grid.width=64,v=>v.grid.ground.pop(),v=>v.grid.ground[0]=Infinity,v=>v.grid.ground[0]=9001,v=>v.grid.source.requestUrl='https://evil.test/',v=>v.grid.source.catalog.url='https://evil.test',v=>v.grid.method.output='native-1m-lidar',v=>v.grid.review.scientific_accuracy_verified=true];
 for(const change of changes){const x=structuredClone(v);change(x);assert.equal(validGroundView(x,query()),false);}
 const partial=structuredClone(v);partial.state='partial';partial.grid.ground[0]=null;assert.equal(validGroundView(partial,query()),true);partial.state='ready';assert.equal(validGroundView(partial,query()),false);
});
test('Ground private queue is bounded, idempotent and hash-readback checked',t=>{
 const c=config(t),q=query();assert.equal(requestGround(c,q).state,'processing');requestGround(c,q);assert.equal(readdirSync(join(c.root,'queue')).length,1);ready(c,q);assert.deepEqual(requestGround(c,q),fixture(q));
 const dir=join(c.root,'jobs',groundKey(q));writeFileSync(join(dir,'view.json'),'{}',{mode:0o600});assert.throws(()=>requestGround(c,q));
 chmodSync(c.root,0o755);assert.throws(()=>requestGround(c,q));
});
test('Ground source originals are immutable, size bounded and stored under hash receipts',async t=>{
 const c=config(t),url=groundSourceUrl(query());let calls=0;const fetcher=async()=>{calls++;return new Response('synthetic-raster-transport');};
 const a=await groundSource(c.root,url,{fetcher});assert.equal(calls,1);assert.equal((await groundSource(c.root,url,{fetcher})).sha256,a.sha256);assert.equal(calls,1);assert.equal(JSON.parse(readFileSync(join(c.root,'sources','ledger.json'))).bytes,a.bytes);
 await assert.rejects(groundSource(c.root,'http://127.0.0.1/private',{fetcher}),/GROUND_SOURCE_DENIED/);await assert.rejects(groundSource(c.root,GROUND_SERVICE+'/identify',{fetcher}),/GROUND_SOURCE_DENIED/);
 writeFileSync(a.path,'tampered',{mode:0o600});await assert.rejects(groundSource(c.root,url,{fetcher}));
 const next=groundSourceUrl({...query(),bbox:[-97.36,37.68,-97.34,37.69]});await assert.rejects(groundSource(c.root,next,{fetcher:async()=>new Response('x',{headers:{'content-length':String(GROUND_LIMITS.sourceBytes+1)}})}),/GROUND_SOURCE_SIZE/);
 groundAtomic(join(c.root,'sources'),'ledger.json',{bytes:GROUND_LIMITS.cacheBytes});await assert.rejects(groundSource(c.root,next,{fetcher}),/GROUND_CACHE_BUDGET/);
});
test('Ground source read refuses symlink substitution',async t=>{
 const c=config(t),url=groundSourceUrl(query()),a=await groundSource(c.root,url,{fetcher:async()=>new Response('synthetic')});const outside=join(c.root,'outside');writeFileSync(outside,'synthetic',{mode:0o600});rmSync(a.path);symlinkSync(outside,a.path);await assert.rejects(groundSource(c.root,url));
});
test('Catalog preserves raw provider date/resolution meaning and exposes no provider local paths',()=>{
 const a=catalogCandidates({exceededTransferLimit:true,features:[{attributes:{OBJECTID:12,Name:'example',DEM_Type:1,Source:'USGS',VerticalDatum:'NAVD88',AcquisitionDate:1702944000000,StartDate:20101115,EndDate:'20231219',Resolution_X:'0.000277',Resolution_Y:-.000277,Metadata:'D:\\provider\\source.xml'}}]});assert.equal(a.complete,false);assert.equal(a.candidates[0].endDate,'20231219');assert.equal(a.candidates[0].resolutionY,-.000277);assert.equal(a.candidates[0].metadataUrl,null);assert.throws(()=>catalogCandidates({error:{code:500}}));
});
test('Signed Ground relay validates query/schema, refreshes preparation and retains stale label',async t=>{
 const c=config(t),q=query(),secret=newSecret(),keyId='ground-unit',gateway=createGateway({keyId,secret,ground:c,open(){throw Error('SQL forbidden');}});let now=100000,online=true,calls=0;
 const relay={get lastSeen(){return online?now:0;},async submit({method,path,body}){calls++;assert.equal(path,GROUND_ROUTE);const requestHeaders=signRequest({keyId,secret,method,path,body}),r=gateway({method,path,body,headers:requestHeaders});return {status:r.status,bytes:r.body,requestHeaders,headers:new Headers({'content-type':'application/json',[RESPONSE_SIGNATURE_HEADER]:r.signature})};}};
 const service=createLocalDataService({config:{keyId,secret:decodeSecret(secret)},clock:()=>now,relay}),req=new Request('https://kansasfrontiermatrix.com/api/terrain/ground?bbox='+q.bbox.join(',')+'&size=96');
 assert.equal((await(await service.ground(req)).json()).state,'processing');assert.equal((await(await service.ground(req)).json()).cache.state,'fresh');assert.equal(calls,1);ready(c,q);now+=2001;const value=await(await service.ground(req)).json();assert.equal(value.state,'ready');assert.equal(value.cache.state,'live');assert.equal(value.gateway,undefined);assert.equal(value.grid.ground.length,9216);online=false;now+=1000000;assert.equal((await(await service.ground(req)).json()).cache.state,'stale');
 assert.equal((await service.ground(new Request(req.url+'&url=evil'))).status,400);assert.equal((await service.ground(new Request(req.url,{method:'POST'}))).status,405);assert.equal(LOCAL_DATA_ROUTES.get(GROUND_ROUTE),'POST');assert.equal(LOCAL_DATA_LIMITS.replyBytes,1000000);
});

test('Ground queue capacity refuses a new view and preserves failed attempts during bounded retry',t=>{
 const c=config(t),q=query();requestGround(c,q);const queue=join(c.root,'queue');for(let i=1;i<16;i++)writeFileSync(join(queue,i.toString(16).padStart(64,'0')+'.json'),'{}',{mode:0o600});
 const other={...q,bbox:[-97.36,37.68,-97.34,37.69]};assert.equal(requestGround(c,other).state,'unavailable');assert.equal(readdirSync(queue).length,16);
 const dir=join(c.root,'jobs',groundKey(q));const fail=()=>{const v=initialGround(q,'unavailable','Synthetic transient failure'),h=groundAtomic(dir,'view.json',v);groundAtomic(dir,'ready.json',{requestKey:groundKey(q),sha256:h,completedAt:new Date(Date.now()-61000).toISOString()});};
 for(let i=1;i<=2;i++){fail();assert.equal(requestGround(c,q).state,'processing');assert.equal(readdirSync(join(c.root,'jobs')).filter(n=>n.startsWith('.failed-')).length,i);}
 fail();assert.equal(requestGround(c,q).state,'unavailable');assert.equal(readdirSync(join(c.root,'jobs')).filter(n=>n.startsWith('.failed-')).length,2);
});
