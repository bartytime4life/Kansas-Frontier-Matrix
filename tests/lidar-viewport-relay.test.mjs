import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtempSync,mkdirSync,writeFileSync,readFileSync,chmodSync,readdirSync,rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createHash} from 'node:crypto';
import {normalizeLidarView,lidarViewKey,parseLidarViewSearch,validLidarView,validNativeViewManifest,validNativeViewChunk,validLidarGrid} from '../scripts/local-data/lidar-view-model.mjs';
import {loadLidarDiscovery,selectViewProjects,initialLidarView,requestLidarView,loadLidarViewArtifact} from '../scripts/local-data/lidar-view.mjs';
import {nodeBounds,discoverViewNodes,createSourceReader,PREPARE_LIMITS} from '../scripts/local-data/lidar-view-worker.mjs';
import {LOCAL_DATA_ROUTES,LOCAL_DATA_LIMITS} from '../scripts/local-data/protocol.mjs';
import {createGateway} from '../scripts/local-data/gateway.mjs';
import {createLocalDataService} from '../server/local-data.mjs';
import {newSecret,decodeSecret,signRequest,RESPONSE_SIGNATURE_HEADER} from '../scripts/home-inference/signature.mjs';
const digest=b=>'sha256:'+createHash('sha256').update(b).digest('hex'),review={status:'pending',source_admitted:false,released:false,scientific_accuracy_verified:false};
const query=()=>normalizeLidarView({bbox:[-96.586,39.089,-96.584,39.091],zoom:16,layers:['points']});
function root(t){const p=mkdtempSync(join(tmpdir(),'kfm-kansas-views-test-'));chmodSync(p,0o700);t.after(()=>rmSync(p,{recursive:true,force:true}));return {root:p};}
function ready(config,q){
 // Explicitly synthetic transport/schema input, not a captured survey fixture.
 const key=lidarViewKey(q),dir=join(config.root,'jobs',key);mkdirSync(join(config.root,'jobs'),{mode:0o700,recursive:true});mkdirSync(dir,{mode:0o700,recursive:true});
 const asset={id:0,project:'KS_Statewide_B6A_2018',eptUrl:'https://usgs-lidar-public.s3.amazonaws.com/KS_Statewide_B6A_2018/ept.json',url:'https://usgs-lidar-public.s3.amazonaws.com/KS_Statewide_B6A_2018/ept-data/8-92-179-127.laz',sha256:'sha256:'+'a'.repeat(64),bytes:258444,pointCount:30058,coordinateEncodingM:[.001,.001,.001],acquisition:'Synthetic transport only',verticalReference:'Synthetic input, no datum claim',gpsTimeType:'week'};
 const c={format:'kfm-lidar-points-chunk-v2',captureId:'view-'+key,chunkId:0,points:[[-10751800,4734600,350,100,2,1,1,0,100,0,0],[-10751799,4734601,351,110,7,1,1,4,101,0,1]]};
 const cb=Buffer.from(JSON.stringify(c));writeFileSync(join(dir,'chunk-0.json'),cb,{mode:0o600});
 const m={format:'kfm-lidar-points-manifest-v2',captureId:c.captureId,generatedAt:'2026-11-24T03:00:00Z',source:{provider:'USGS',project:'Kansas viewport',eptUrl:'https://usgs.entwine.io/',horizontalCrs:'EPSG:3857',verticalReference:'Synthetic transport only',acquisition:'Synthetic transport only',coordinateEncodingM:[.001,.001,.001],selection:'Synthetic rows, not observations',assets:[asset],notes:['Synthetic input only']},review,pointCount:2,bounds3857:[-10751800,4734600,-10751799,4734601],heightRange:[350,351],chunks:[{id:0,pointCount:2,bytes:cb.length,sha256:digest(cb)}],columns:['x','y','z','intensity','classification','returnNumber','numberOfReturns','classFlags','gpsTime','asset','record']};
 const v=initialLidarView(q,'ready');v.points=m;v.state='ready';v.layers=v.layers.map(l=>l.kind==='points'?{...l,state:'ready',message:'Synthetic rows for transport testing'}:l);
 const bytes=Buffer.from(JSON.stringify(v));writeFileSync(join(dir,'view.json'),bytes,{mode:0o600});writeFileSync(join(dir,'ready.json'),JSON.stringify({requestKey:key,viewSha256:digest(bytes),gridSha256:null}),{mode:0o600});return {key,dir,v,m,c,asset};
}
test('viewport canonicalization is strict, stable and geographically bounded',()=>{
 const q=query(),key=lidarViewKey(q);assert.match(key,/^[a-f0-9]{64}$/);assert.equal(lidarViewKey({...q,zoom:16.04}),key);
 assert.deepEqual(normalizeLidarView({...q,layers:['points','surface']}),{...q,layers:['surface','points']});
 assert.deepEqual(parseLidarViewSearch(new URLSearchParams('bbox=-96.586,39.089,-96.584,39.091&zoom=16&layers=points')),q);
 for(const q2 of [{...q,bbox:[-200,39,-96,40]},{...q,bbox:[-96,39,-97,40]},{...q,layers:['points','points']},{...q,layers:['https://evil.test']},{...q,zoom:NaN},{...q,file:'/etc/passwd'}])assert.throws(()=>normalizeLidarView(q2));
 for(const s of ['bbox=-96,39,-95,40&zoom=16&layers=points&zoom=17','bbox=-96,39,-95,40&zoom=16&layers=points&url=evil','bbox=-96,39,-95,40&zoom=Infinity&layers=points'])assert.throws(()=>parseLidarViewSearch(new URLSearchParams(s)));
});
test('actual discovery metadata spans western/central/eastern Kansas without name-based statewide substitution',()=>{
 assert.equal(loadLidarDiscovery().projects.size,127);
 const names=[[-101.7,39.3],[-97.3,37.7],[-95.7,39.0]].map(([x,y])=>selectViewProjects({bbox:[x-.001,y-.001,x+.001,y+.001],zoom:16,layers:['points']}).map(p=>p.id));
 assert(names.every(a=>a.length));assert(names[0].some(s=>s.startsWith('USGS_LPC_KS_')));assert(!names.flat().includes('KS_Statewide_2017'));
 const broad=initialLidarView({bbox:[-102,37,-95,40],zoom:7,layers:['surface','canopy']});assert.equal(broad.state,'detail-required');assert.equal(broad.points,null);assert.equal(broad.grid,null);assert.equal(broad.layers[0].state,'ready');
});
test('EPT hierarchy traverses all native Z siblings and cannot label budget-truncated analysis complete',async()=>{
 const p={eptUrl:'https://unit.invalid/project/ept.json',octreeBoundsXYZ:[0,0,0,8,8,8],span:128};
 const h={'0-0-0-0':1,'1-0-0-0':2,'1-0-0-1':3,'1-1-1-0':4};const reader={get:async()=>({bytesValue:Buffer.from(JSON.stringify(h))})};
 const r=await discoverViewNodes(p,[.1,.1,3.9,3.9],{complete:true,reader});assert.deepEqual(r.nodes.map(n=>n.key),['0-0-0-0','1-0-0-0','1-0-0-1']);assert.equal(r.complete,true);
 const bounded=await discoverViewNodes(p,[.1,.1,3.9,3.9],{complete:true,reader,maxNodes:2});assert.equal(bounded.complete,false);
 assert.deepEqual(nodeBounds(p.octreeBoundsXYZ,'1-0-0-1'),[0,0,4,4,4,8]);
});
test('preparation queue is private, bounded and idempotent; malformed views never create jobs',t=>{
 const config=root(t),q=query();const a=requestLidarView(config,q),b=requestLidarView(config,q);assert.equal(a.requestKey,b.requestKey);assert.equal(a.state,'processing');assert.equal(readdirSync(join(config.root,'queue')).length,1);assert.equal(validLidarView(a,q),true);
 assert.throws(()=>requestLidarView(config,{...q,bbox:[0,0,1,1]}));
 for(let i=1;i<16;i++)writeFileSync(join(config.root,'queue',i.toString(16).padStart(64,'0')+'.json'),'{}',{mode:0o600});
 assert.equal(requestLidarView(config,{...q,zoom:17}).state,'unavailable');chmodSync(config.root,0o755);assert.throws(()=>requestLidarView(config,q));
});
test('v2 rows bind asset GPS absence, flags, original records and view identity',t=>{
 const f=ready(root(t),query());assert.equal(validNativeViewManifest(f.m,f.key),true);assert.equal(validNativeViewChunk(f.c,f.m,f.key,0),true);assert.deepEqual(loadLidarViewArtifact({root:dirnameRoot(f.dir)},f.key,0),f.c);
 for(const change of [m=>m.source.assets[0].eptUrl='https://evil.test/ept.json',m=>m.source.assets[0].project='wrong',m=>m.source.coordinateEncodingM=[.01,.01,.01],m=>m.captureId='view-'+'0'.repeat(64)]){const m=structuredClone(f.m);change(m);assert.equal(validNativeViewManifest(m,f.key),false);}
 let c=structuredClone(f.c);c.points[0][8]=null;assert.equal(validNativeViewChunk(c,f.m,f.key,0),false);const m=structuredClone(f.m);m.source.assets[0].gpsTimeType='absent';c.points[1][8]=null;assert.equal(validNativeViewChunk(c,m,f.key,0),true);
 c=structuredClone(f.c);c.points[1]=[...c.points[0]];assert.equal(validNativeViewChunk(c,f.m,f.key,0),false);
 writeFileSync(join(f.dir,'chunk-0.json'),JSON.stringify({...f.c,captureId:'wrong'}));assert.throws(()=>loadLidarViewArtifact({root:dirnameRoot(f.dir)},f.key,0));
});
const dirnameRoot=dir=>join(dir,'..','..');
test('source cache accepts fixed public projects only, pins bytes and enforces storage limits',async t=>{
 const config=root(t),url='https://usgs-lidar-public.s3.amazonaws.com/KS_Statewide_B6A_2018/ept-data/0-0-0-0.laz';let calls=0;
 const fetcher=async()=>{calls++;return new Response('synthetic-network-unit-bytes',{headers:{'content-length':'28'}});};
 const reader=createSourceReader(config.root,{fetcher});const a=await reader.get(url,100);assert.equal(calls,1);assert.equal((await reader.get(url,100)).sha256,a.sha256);assert.equal(calls,1);
 for(const bad of ['http://127.0.0.1/secret','https://usgs-lidar-public.s3.amazonaws.com/unknown/ept-data/0-0-0-0.laz',url+'?X-Amz-Signature=x'])await assert.rejects(reader.get(bad,100));
 writeFileSync(a.path,'tampered');await assert.rejects(reader.get(url,100));
 writeFileSync(join(config.root,'cache','ledger.json'),JSON.stringify({bytes:PREPARE_LIMITS.sourceCacheBytes}),{mode:0o600});const full=createSourceReader(config.root,{fetcher});await assert.rejects(full.get(url.replace('0-0-0-0','1-0-0-0'),100),/SOURCE_CACHE_BUDGET/);
});
test('signed viewport relay publishes only validated key-bound artifacts and refreshes pending receipts',async t=>{
 const config=root(t),q=query(),key=lidarViewKey(q),secret=newSecret(),keyId='unit-viewport',gateway=createGateway({keyId,secret,lidarView:config,open(){throw Error('SQL forbidden');}});let now=1000;
 const relay={get lastSeen(){return now;},async submit({method,path,body}){const requestHeaders=signRequest({keyId,secret,method,path,body}),a=gateway({method,path,body,headers:requestHeaders});return{status:a.status,bytes:a.body,requestHeaders,headers:new Headers({'content-type':'application/json',[RESPONSE_SIGNATURE_HEADER]:a.signature})};}};
 const service=createLocalDataService({config:{keyId,secret:decodeSecret(secret)},clock:()=>now,relay});const req=new Request('https://kansasfrontiermatrix.com/api/lidar/view?bbox='+q.bbox.join(',')+'&zoom=16&layers=points');
 assert.equal((await(await service.lidarView(req)).json()).state,'processing');const f=ready(config,q);now+=2001;const v=await(await service.lidarView(req)).json();assert.equal(v.state,'ready');assert.equal(v.points.captureId,'view-'+key);assert.equal(v.cache.state,'live');
 const c=await(await service.lidarViewArtifact(new Request('https://kansasfrontiermatrix.com/api/lidar/view/'+key+'/0'),key,0)).json();assert.deepEqual(c.points,f.c.points);assert.equal(c.cache.state,'live');assert.equal(c.gateway,undefined);
 assert.equal((await service.lidarViewArtifact(req,'../escape',0)).status,400);assert.equal(LOCAL_DATA_LIMITS.replyBytes,1000000);assert.equal(LOCAL_DATA_ROUTES.get('/v1/lidar/view'),'POST');
});

test('failed immutable view receipts retry transient failures after backoff at most three times',t=>{
 const config=root(t),q=query(),f=ready(config,q),key=f.key;
 function failed(){const view=initialLidarView(q,'unavailable','Synthetic transient failure');view.state='unavailable';const bytes=Buffer.from(JSON.stringify(view));writeFileSync(join(f.dir,'view.json'),bytes,{mode:0o600});writeFileSync(join(f.dir,'ready.json'),JSON.stringify({requestKey:key,viewSha256:digest(bytes),gridSha256:null,completedAt:new Date(Date.now()-61000).toISOString()}),{mode:0o600});}
 let preservedOriginal;for(let n=0;n<2;n++){failed();assert.equal(requestLidarView(config,q).state,'processing');const archives=readdirSync(join(config.root,'jobs')).filter(s=>s.startsWith('.failed-'));assert.equal(archives.length,n+1);if(n===0)preservedOriginal=archives[0];assert.equal(readFileSync(join(config.root,'jobs',preservedOriginal,'chunk-0.json'),'utf8'),JSON.stringify(f.c));}
 failed();assert.equal(requestLidarView(config,q).state,'unavailable');assert.equal(readdirSync(join(config.root,'jobs')).filter(s=>s.startsWith('.failed-')).length,2);
});
test('source cache reserves retained bytes before output and validates decoded encoded-body lengths',async t=>{
 const config=root(t),url='https://usgs-lidar-public.s3.amazonaws.com/KS_Statewide_B6A_2018/ept-hierarchy/0-0-0-0.json';
 const bytes=Buffer.from('{"synthetic":"decoded test only"}');const reader=createSourceReader(config.root,{fetcher:async()=>new Response(bytes,{headers:{'content-length':'8','content-encoding':'gzip'}})});
 const r=await reader.get(url,100);assert.equal(r.bytes,bytes.length);assert.equal(JSON.parse(readFileSync(join(config.root,'cache','ledger.json'))).bytes,bytes.length);assert.equal(r.contentEncoding,'gzip');
});

test('the hierarchy budget is shared across source projects and cached replies',async t=>{
 const config=root(t),reader=createSourceReader(config.root,{fetcher:async()=>new Response('{}')});
 const urls=['KS_Statewide_B6A_2018','KS_Statewide_B5_2018'].map(p=>'https://usgs-lidar-public.s3.amazonaws.com/'+p+'/ept-hierarchy/0-0-0-0.json');
 for(let i=0;i<PREPARE_LIMITS.hierarchyReplies;i++)await reader.get(urls[i%2],100);
 await assert.rejects(reader.get(urls[0],100),/HIERARCHY_BUDGET/);
});
