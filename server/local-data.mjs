// Read-only data from the pipeline PC's local SQL databases, carried by an outbound-only relay:
// the PC's worker long-polls this server (/api/local-data-worker/v1/*), relays each signed request
// to the PC's loopback gateway (scripts/local-data/gateway.mjs) and posts the signed reply back.
// This server signs every request with the gateway key and verifies every reply itself, so the
// worker can neither forge nor alter one. It is a second relay instance, separate from home
// inference, with its own keys. Off unless KFM_LOCAL_DATA=1 and KFM_LOCAL_DATA_ORIGIN is one of the
// controlled hosting origins (server/hosted-ai-origins.mjs).
// Answers are cached; when the PC is unreachable the last answer is served, marked stale.
import {decodeSecret,verifyResponse} from '../scripts/home-inference/signature.mjs';
import {createHomeRelay,RELAY_LIMITS} from './home-relay.mjs';
import {hostedAiOriginAllowed} from './hosted-ai-origins.mjs';
import {LOCAL_DATA_GATEWAY,LOCAL_DATA_ROUTES,LOCAL_DATA_LIMITS,LOCAL_DATA_DATA_PREFIX} from '../scripts/local-data/protocol.mjs';
import {DATASETS,datasetCatalog} from '../scripts/local-data/datasets.mjs';
import {RECOVERED_COLLECTIONS} from '../scripts/local-data/recovered.mjs';
import {LIDAR_POINTS_ROUTE,validLidarPointsManifest,validLidarPointsChunk} from '../scripts/local-data/lidar-points.mjs';
import {parseLidarViewSearch,lidarViewKey,validViewKey,validLidarView,validNativeViewChunk,validLidarGrid,LIDAR_VIEW_ROUTES} from '../scripts/local-data/lidar-view-model.mjs';

import {GROUND_ROUTE,parseGroundSearch,groundKey,validGroundView} from '../scripts/local-data/ground-model.mjs';
import {createHostedTerrainCache,HOSTED_TERRAIN_LIMITS} from './hosted-terrain-cache.mjs';
import {createHash} from 'node:crypto';
import {terrainResponse} from './terrain-response.mjs';
import {readGroundBaseline} from './terrain-baseline.mjs';

export const LOCAL_DATA_WORKER_PREFIX='/api/local-data-worker/v1';
// workerSeenMs: the worker re-polls at least every leaseWaitMs (20 s) and pings /status while relaying,
// so a longer silence means the PC is away and a visitor gets the cached or offline answer at once
// instead of waiting out unleasedMs. (A job handed to a poll whose connection already died still
// waits out leasedMs once; the proxy may not pass that disconnect on.)
// bytes caps the memory held by cached answers, whatever their number.
export const LOCAL_DATA_CACHE=Object.freeze({freshMs:15*60000,staleMs:7*24*3600000,entries:500,bytes:64*1024*1024,workerSeenMs:30000});
// The worker's /result carries up to replyBytes base64-encoded, over a home upload link.
export const LOCAL_DATA_RELAY_LIMITS=Object.freeze({...RELAY_LIMITS,queue:16,requestBytes:Math.ceil(LOCAL_DATA_LIMITS.replyBytes*4/3)+4096,bodyMs:15000,
 replyBytes:LOCAL_DATA_LIMITS.replyBytes,unleasedMs:8000,
 leasedMs:Object.freeze(Object.fromEntries([...LOCAL_DATA_ROUTES.keys()].map(path=>[path,LOCAL_DATA_LIMITS.gatewayMs+5000])))});
const error=code=>Object.assign(new Error(code),{code});
const json=(value,status=200,cache='no-store')=>Response.json(value,{status,headers:{'Cache-Control':cache,'X-Content-Type-Options':'nosniff'}});
const publicCollectionIds=new Set(RECOVERED_COLLECTIONS.map(collection=>collection.id));

export function localDataConfig(env=process.env){
 if(env.KFM_LOCAL_DATA!=='1')throw error('LOCAL_DATA_OFF');
 const origin=env.KFM_LOCAL_DATA_ORIGIN;if(!hostedAiOriginAllowed(origin))throw error('LOCAL_DATA_ORIGIN_INVALID');
 const key=(id,secret)=>{const bytes=decodeSecret(secret??'');if(!/^[A-Za-z0-9._-]{1,64}$/.test(id??'')||!bytes)throw error('LOCAL_DATA_KEY_INVALID');return {keyId:id,secret:bytes};};
 const gateway=key(env.KFM_LOCAL_DATA_GATEWAY_KEY_ID,env.KFM_LOCAL_DATA_GATEWAY_SECRET);
 const worker=key(env.KFM_LOCAL_DATA_WORKER_KEY_ID,env.KFM_LOCAL_DATA_WORKER_SECRET);
 // Neither key may stand in for the other.
 if(gateway.secret.equals(worker.secret))throw error('LOCAL_DATA_KEY_REUSED');
 return Object.freeze({origin,keyId:gateway.keyId,secret:gateway.secret,worker});
}

export function createLocalDataService({config,clock=Date.now,terrainCache=null,groundBaseline=null,relay=createHomeRelay({keyId:config.keyId,secret:config.secret,worker:config.worker,clock,limits:LOCAL_DATA_RELAY_LIMITS,routes:LOCAL_DATA_ROUTES,workerPrefix:LOCAL_DATA_WORKER_PREFIX,diagnostic:code=>console.warn('[KFM local data] '+code)})}){
 const cache=new Map(),pending=new Map();let cachedBytes=0;
 const workerOnline=()=>clock()-relay.lastSeen<=LOCAL_DATA_CACHE.workerSeenMs;
 const forget=key=>{const hit=cache.get(key);if(hit){cachedBytes-=hit.bytes;cache.delete(key);}};
 const remember=(key,value,bytes,at=clock(),tier='memory',binding='')=>{
  forget(key);cache.set(key,{value,bytes,at,tier,binding});cachedBytes+=bytes;
  while(cache.size>LOCAL_DATA_CACHE.entries||cachedBytes>LOCAL_DATA_CACHE.bytes)forget(cache.keys().next().value);
 };

 // Only validated compact terrain receipts/grids are persisted on the web host.
 // No SQL answers, raw point chunks, private paths, source files or secrets enter it.
 const terrainFreshMs=terrainCache?HOSTED_TERRAIN_LIMITS.freshMs:LOCAL_DATA_CACHE.freshMs;
 const restoreTerrain=async(key,diskKey,validate,binding='')=>{
  if(cache.has(key)&&cache.get(key).binding!==binding)forget(key);
  if(!cache.has(key)){
   const hit=await terrainCache?.read(diskKey,validate,binding)??(groundBaseline&&diskKey.startsWith('ground:')?await groundBaseline(diskKey):null);
   if(hit&&validate(hit.value))remember(key,hit.value,hit.bytes,hit.at,hit.tier??'disk',binding);
  }
  return cache.get(key);
 };
 const rememberTerrain=async(key,diskKey,value,bytes,binding='')=>{
  const at=clock();remember(key,value,bytes,at,'memory',binding);
  if(terrainCache)await terrainCache.write(diskKey,value,at,binding);
  return value;
 };
 const terrainAnswer=(value,state,at,maxAge,tier='memory',request=null)=>terrainResponse(value,{state,at,maxAge,tier,request,replyBytes:LOCAL_DATA_LIMITS.replyBytes});
 const viewBinding=value=>createHash('sha256').update(JSON.stringify(value)).digest('hex');

 // A reply is parsed only after the gateway's signature over this exact request, status and body checks out.
 const call=async(method,path,payload)=>{
  if(!workerOnline())throw error('LOCAL_DATA_UNAVAILABLE');
  const body=payload===undefined?'':JSON.stringify(payload);
  const reply=await relay.submit({method,path,body,timeoutMs:LOCAL_DATA_LIMITS.clientMs});
  const {status,headers,bytes,requestHeaders}=reply;
  if(!/^application\/json(?:;|$)/i.test(headers.get('content-type')??'')||bytes.length>LOCAL_DATA_LIMITS.replyBytes)throw error('GATEWAY_RESPONSE_INVALID');
  if(!verifyResponse({secret:config.secret,requestHeaders,method,path,requestBody:body,status,body:bytes,headers}))throw error('GATEWAY_RESPONSE_INVALID');
  let value;try{value=JSON.parse(bytes.toString('utf8'));}catch{throw error('GATEWAY_RESPONSE_INVALID');}
  if(value?.gateway!==LOCAL_DATA_GATEWAY)throw error('GATEWAY_RESPONSE_INVALID');
  if(status===400)throw error('QUERY_INVALID');
  if(status===413)throw error('REPLY_TOO_LARGE');
  if(status===503&&value.error==='DATASET_NOT_READY')throw error('DATASET_NOT_READY');
  if(status<200||status>299)throw error('LOCAL_DATA_UNAVAILABLE');
  return {value,bytes:bytes.length};
 };

 const answer=(value,state,at,maxAge)=>{
  const body={...value,cache:{state,at:new Date(at).toISOString()}};
  // The public envelope is larger than the signed gateway reply after cache metadata is added.
  if(Buffer.byteLength(JSON.stringify(body))>LOCAL_DATA_LIMITS.replyBytes)return json({reasonCode:'REPLY_TOO_LARGE',hint:'Ask for fewer rows (limit) or a shorter range.'},413);
  return json(body,200,'public, max-age='+maxAge);
 };
 /** GET /api/local-data/{id}: one dataset question, answered from cache or the PC. */
 const query=async(request,id)=>{
  if(request.method!=='GET')return json({reasonCode:'METHOD_DENIED'},405);
  const dataset=DATASETS.get(id);
  if(!dataset)return json({reasonCode:'DATASET_NOT_FOUND'},404);
  const search=new URL(request.url).searchParams;
  // A parameter has one meaning; never silently select the last repeated value.
  if([...search.keys()].some(key=>search.getAll(key).length!==1))return json({reasonCode:'QUERY_INVALID'},400);
  const input=Object.fromEntries(search);
  let normalized;
  try{normalized=dataset.parse(input);}catch{return json({reasonCode:'QUERY_INVALID'},400);}
  const key=id+'\n'+JSON.stringify(normalized),hit=cache.get(key),age=hit?clock()-hit.at:Infinity;
  if(hit&&age<LOCAL_DATA_CACHE.freshMs)return workerOnline()?answer(hit.value,'fresh',hit.at,300):answer(hit.value,'stale',hit.at,60);
  try{
   // Identical questions arriving together share one trip to the PC. The PC re-validates the
   // visitor's own parameters, which parse() has just accepted.
   let trip=pending.get(key);
   if(!trip){
    trip=call('POST',LOCAL_DATA_DATA_PREFIX+id,input)
     .then(({value,bytes})=>{delete value.gateway;remember(key,value,bytes);return value;}).finally(()=>pending.delete(key));
    pending.set(key,trip);
   }
   const value=await trip;
   return answer(value,'live',cache.get(key)?.at??clock(),300);
  }catch(failure){
   if(failure.code==='QUERY_INVALID')return json({reasonCode:'QUERY_INVALID'},400);
   if(failure.code==='REPLY_TOO_LARGE')return json({reasonCode:'REPLY_TOO_LARGE',hint:'Ask for fewer rows (limit) or a shorter range.'},413);
   // The PC is off, busy, not ready or unreachable: the last answer, clearly marked, or a plain offline state.
   if(hit&&clock()-hit.at<LOCAL_DATA_CACHE.staleMs)return answer(hit.value,'stale',hit.at,60);
   if(failure.code==='DATASET_NOT_READY')return json({state:'local-data-preparing',reasonCode:'DATASET_NOT_READY'},503);
   return json({state:'local-data-offline',reasonCode:'LOCAL_DATA_UNAVAILABLE'},503);
  }
 };

 // A single hash-pinned derived pilot; the NEON download token remains on dev.
 const neonPreview=async request=>{
  if(request.method!=='GET')return json({reasonCode:'METHOD_DENIED'},405);
  if(new URL(request.url).search)return json({reasonCode:'QUERY_INVALID'},400);
  const key='\nneon-preview',hit=cache.get(key),age=hit?clock()-hit.at:Infinity;
  if(hit&&age<LOCAL_DATA_CACHE.freshMs)return answer(hit.value,workerOnline()?'fresh':'stale',hit.at,workerOnline()?300:60);
  try{
   let trip=pending.get(key);
   if(!trip){
    trip=call('GET','/v1/neon/preview').then(({value,bytes})=>{
     if(value?.format!=='kfm-neon-relay-pilot-v1'||value.review?.scientific_accuracy_verified!==false||value.review?.source_admitted!==false)throw error('GATEWAY_RESPONSE_INVALID');
     delete value.gateway;remember(key,value,bytes);return value;
    }).finally(()=>pending.delete(key));
    pending.set(key,trip);
   }
   return answer(await trip,'live',cache.get(key)?.at??clock(),300);
  }catch{
   if(hit&&clock()-hit.at<LOCAL_DATA_CACHE.staleMs)return answer(hit.value,'stale',hit.at,60);
   return json({state:'local-data-offline',reasonCode:'NEON_PREVIEW_UNAVAILABLE'},503);
  }
 };

 // Fixed native return capture, chunked below the unchanged reply budget.
 const lidarPoints=async(request,/** @type {number|null} */ id=null)=>{
  if(request.method!=='GET')return json({reasonCode:'METHOD_DENIED'},405);
  if(new URL(request.url).search||id!==null&&(!Number.isInteger(id)||id<0||id>15))return json({reasonCode:'QUERY_INVALID'},400);
  const route=LIDAR_POINTS_ROUTE+(id===null?'':'/'+id),key='\nlidar-points'+(id===null?'':'/'+id),hit=cache.get(key),age=hit?clock()-hit.at:Infinity;
  if(hit&&age<LOCAL_DATA_CACHE.freshMs)return answer(hit.value,workerOnline()?'fresh':'stale',hit.at,workerOnline()?300:60);
  try{
   let trip=pending.get(key);
   if(!trip){
    trip=(async()=>{
     // Bind every chunk to the same validated manifest identity, not merely a URL.
     let manifest=null;
     if(id!==null){const response=await lidarPoints(new Request(new URL('/api/lidar/points',request.url)));if(!response.ok)throw error('LIDAR_POINTS_UNAVAILABLE');const body=await response.json();const {cache:ignored,...m}=body;void ignored;if(!validLidarPointsManifest(m)||!m.chunks[id])throw error('GATEWAY_RESPONSE_INVALID');manifest=m;}
     const {value,bytes}=await call('GET',route);const {gateway:ignored,...body}=value;void ignored;
     if(id===null?!validLidarPointsManifest(body):!validLidarPointsChunk(body,manifest,id))throw error('GATEWAY_RESPONSE_INVALID');
     remember(key,body,bytes);return body;
    })().finally(()=>pending.delete(key));pending.set(key,trip);
   }
   return answer(await trip,'live',cache.get(key)?.at??clock(),300);
  }catch{
   if(hit&&clock()-hit.at<LOCAL_DATA_CACHE.staleMs)return answer(hit.value,'stale',hit.at,60);
   return json({state:'local-data-offline',reasonCode:'LIDAR_POINTS_UNAVAILABLE'},503);
  }
 };

 // Kansas-wide viewport data. Processing receipts have a short cache lifetime;
 // completed immutable artifacts share the existing bounded cache.
 const viewCacheKey=key=>'\nlidar-view:'+key;
 const viewTTL=v=>['processing','idle'].includes(v.state)?2000:v.state==='unavailable'?15000:terrainFreshMs;
 const cachedView=async(key,query=null)=>{
  const cacheKey=viewCacheKey(key),hit=await restoreTerrain(cacheKey,'view:'+key,v=>validLidarView(v,query??v.query)&&v.requestKey===key);
  if(hit&&clock()-hit.at<viewTTL(hit.value))return hit.value;
  let trip=pending.get(cacheKey);
  if(!trip){trip=call('POST',LIDAR_VIEW_ROUTES.view,query??{requestKey:key}).then(async({value,bytes})=>{
   delete value.gateway;if(!validLidarView(value,query??value.query)||value.requestKey!==key)throw error('GATEWAY_RESPONSE_INVALID');return rememberTerrain(cacheKey,'view:'+key,value,bytes);
  }).finally(()=>pending.delete(cacheKey));pending.set(cacheKey,trip);}
  return trip;
 };
 const lidarView=async request=>{
  if(request.method!=='GET')return json({reasonCode:'METHOD_DENIED'},405);
  let query;try{query=parseLidarViewSearch(new URL(request.url).searchParams);}catch{return json({reasonCode:'QUERY_INVALID'},400);}
  const key=lidarViewKey(query),cacheKey=viewCacheKey(key),hit=await restoreTerrain(cacheKey,'view:'+key,v=>validLidarView(v,query)),fresh=hit&&clock()-hit.at<viewTTL(hit.value);
  try{const value=await cachedView(key,query);return terrainAnswer(value,workerOnline()?(fresh?'fresh':'live'):'stale',cache.get(cacheKey)?.at??clock(),value.state==='processing'?0:workerOnline()?60:0,fresh?hit.tier:'relay',request);}
  catch{if(hit&&clock()-hit.at<LOCAL_DATA_CACHE.staleMs)return answer(hit.value,'stale',hit.at,0);return json({state:'local-data-offline',reasonCode:'LIDAR_VIEW_UNAVAILABLE'},503);}
 };
 const lidarViewArtifact=async(request,key,/** @type {number|'grid'} */ part)=>{
  if(request.method!=='GET')return json({reasonCode:'METHOD_DENIED'},405);
  if(new URL(request.url).search||!validViewKey(key)||part!=='grid'&&(!Number.isInteger(part)||part<0||part>15))return json({reasonCode:'QUERY_INVALID'},400);
  const cacheKey=viewCacheKey(key)+'/'+part;
  const parent=part==='grid'?await restoreTerrain(viewCacheKey(key),'view:'+key,v=>validLidarView(v,v.query)&&v.requestKey===key):null;
  const hit=part==='grid'&&parent?.value.grid?await restoreTerrain(cacheKey,'grid:'+key,v=>validLidarGrid(v,key)&&v.source.project===parent.value.grid.sourceProject&&v.width===parent.value.grid.width&&v.height===parent.value.grid.height,viewBinding(parent.value)):cache.get(cacheKey),age=hit?clock()-hit.at:Infinity;
  if(hit&&age<(part==='grid'?terrainFreshMs:LOCAL_DATA_CACHE.freshMs))return terrainAnswer(hit.value,workerOnline()?'fresh':'stale',hit.at,workerOnline()?300:60,hit.tier,request);
  try{
   let trip=pending.get(cacheKey);
   if(!trip){trip=(async()=>{
    const view=await cachedView(key);if(part==='grid'?!view.grid:!view.points?.chunks[part])throw error('LIDAR_VIEW_UNAVAILABLE');
    const {value,bytes}=await call('POST',part==='grid'?LIDAR_VIEW_ROUTES.grid:LIDAR_VIEW_ROUTES.chunk,part==='grid'?{requestKey:key}:{requestKey:key,chunkId:part});delete value.gateway;
    if(part==='grid'?!validLidarGrid(value,key)||value.source.project!==view.grid.sourceProject||value.width!==view.grid.width||value.height!==view.grid.height:!validNativeViewChunk(value,view.points,key,part))throw error('GATEWAY_RESPONSE_INVALID');if(part==='grid')return rememberTerrain(cacheKey,'grid:'+key,value,bytes,viewBinding(view));remember(cacheKey,value,bytes);return value;
   })().finally(()=>pending.delete(cacheKey));pending.set(cacheKey,trip);}
   return terrainAnswer(await trip,'live',cache.get(cacheKey)?.at??clock(),300,'relay',request);
  }catch{if(hit&&clock()-hit.at<LOCAL_DATA_CACHE.staleMs)return answer(hit.value,'stale',hit.at,60);return json({state:'local-data-offline',reasonCode:'LIDAR_VIEW_UNAVAILABLE'},503);}
 };

 // Provider DEM Ground is a distinct resampled raster receipt, not a native EPT grid.
 const ground=async request=>{
  if(request.method!=='GET')return json({reasonCode:'METHOD_DENIED'},405);
  let query;try{query=parseGroundSearch(new URL(request.url).searchParams);}catch{return json({reasonCode:'QUERY_INVALID'},400);}
  const diskKey='ground:'+groundKey(query),key='\n'+diskKey,hit=await restoreTerrain(key,diskKey,v=>validGroundView(v,query)),fresh=hit&&clock()-hit.at<viewTTL(hit.value);
  if(fresh)return terrainAnswer(hit.value,workerOnline()?'fresh':'stale',hit.at,hit.value.state==='processing'?0:60,hit.tier,request);
  try{
   let trip=pending.get(key);if(!trip){trip=call('POST',GROUND_ROUTE,query).then(async({value,bytes})=>{delete value.gateway;if(!validGroundView(value,query))throw error('GATEWAY_RESPONSE_INVALID');return rememberTerrain(key,diskKey,value,bytes);}).finally(()=>pending.delete(key));pending.set(key,trip);}
   const value=await trip;return terrainAnswer(value,'live',cache.get(key)?.at??clock(),value.state==='processing'?0:60,'relay',request);
  }catch{if(hit&&(hit.tier==='baseline'||clock()-hit.at<LOCAL_DATA_CACHE.staleMs))return terrainAnswer(hit.value,'stale',hit.at,0,hit.tier,request);return json({state:'local-data-offline',reasonCode:'GROUND_VIEW_UNAVAILABLE'},503);}
 };

 /**
  * The gateway's health (readiness and freshness per dataset and recovered collection), asked at
  * most once per freshMs and served stale for up to staleMs when the PC is away, like answers.
  * Resolves to null when there is nothing to serve; never throws.
  */
 const health=async()=>{
  const key='\nhealth',hit=cache.get(key),age=hit?clock()-hit.at:Infinity;
  if(hit&&age<LOCAL_DATA_CACHE.freshMs)return {value:hit.value,state:workerOnline()?'fresh':'stale',at:hit.at};
  try{
   let trip=pending.get(key);
   if(!trip){
    trip=call('GET','/v1/health').then(({value,bytes})=>{delete value.gateway;remember(key,value,bytes);return value;}).finally(()=>pending.delete(key));
    pending.set(key,trip);
   }
   const value=await trip;
   return {value,state:'live',at:cache.get(key)?.at??clock()};
  }catch{
   return hit&&clock()-hit.at<LOCAL_DATA_CACHE.staleMs?{value:hit.value,state:'stale',at:hit.at}:null;
  }
 };

 /**
  * GET /api/local-data: what can be asked, whether the PC is connected, and, when the PC has
  * answered health recently, each dataset's readiness and freshness and each recovered
  * collection's newest file. Without a health answer the catalog is served without them.
  */
 const catalog=async request=>{
  if(request.method!=='GET')return json({reasonCode:'METHOD_DENIED'},405);
  const status=workerOnline()||cache.has('\nhealth')?await health():null;
  const byId=new Map((status?.value?.datasets??[]).map(d=>[d.id,d]));
  const datasets=datasetCatalog().map(d=>{const s=byId.get(d.id);return s?{...d,ready:s.ready,...(s.reason?{reason:s.reason}:{}),freshness:s.freshness??null}:d;});
  const body={format:'kfm-local-data-catalog-v1',online:workerOnline(),datasets};
  if(status){
   // Older gateway versions may still report collections outside this build's public catalogue.
   const collections=Object.fromEntries(Object.entries(status.value.collections??{}).filter(([id])=>publicCollectionIds.has(id)));
   body.status={state:status.state,at:new Date(status.at).toISOString(),generatedAt:status.value.generatedAt??null,collections};
  }
  return json(body,200,'public, max-age=60');
 };
 return {query,catalog,health,neonPreview,lidarPoints,lidarView,lidarViewArtifact,ground,workerHandler:relay.handler,relay};
}

// One service per process: the worker route and the public routes must share one relay.
const SHARED=Symbol.for('kfm.local-data');
function service(env){
 try{if(globalThis[SHARED])return globalThis[SHARED];const config=localDataConfig(env);return globalThis[SHARED]=createLocalDataService({config,terrainCache:createHostedTerrainCache({secret:config.secret,origin:config.origin}),groundBaseline:readGroundBaseline});}catch{return null;}
}
const off=async()=>json({state:'not-configured',reasonCode:'LOCAL_DATA_OFF'},404);

/** /api/local-data/{dataset}: public, cached, read-only. The dataset is the path's last segment. */
export function localDataRuntime(env=process.env){
 const local=service(env);
 if(!local)return off;
 return request=>local.query(request,decodeURIComponent(new URL(request.url).pathname.split('/').pop()??''));
}

/** /api/local-data: the public catalog. */
export function localDataCatalogRuntime(env=process.env){
 const local=service(env);
 return local?local.catalog:off;
}

/** /api/local-data-worker/v1/*: only for the PC's worker, only on the configured origin. */
export function localDataWorkerRuntime(env=process.env){
 const local=service(env);
 if(!local)return async()=>json({reasonCode:'ROUTE_NOT_FOUND'},404);
 const origin=localDataConfig(env).origin;
 return async request=>new URL(request.url).origin===origin?local.workerHandler(request):json({reasonCode:'LOCAL_DATA_ORIGIN_HOLD'},503);
}

/** /api/neon/preview: public derived context through the existing signed dev relay. */
export function localNeonPreviewRuntime(env=process.env){
 const local=service(env);
 return local?local.neonPreview:off;
}

/** Fixed native-point manifest/chunks; no visitor-controlled file or upstream URL. */
export function localLidarPointsRuntime(env=process.env){
 const local=service(env);
 return local?((request,/** @type {number|null} */ id=null)=>local.lidarPoints(request,id)):off;
}

/** Kansas viewport and immutable artifacts, through the same verified data relay. */
export function localLidarViewRuntime(env=process.env){const local=service(env);return local?local.lidarView:off;}
export function localLidarViewArtifactRuntime(env=process.env){const local=service(env);return local?((request,key,/** @type {number|'grid'} */ part)=>local.lidarViewArtifact(request,key,part)):off;}

export function localGroundRuntime(env=process.env){const local=service(env);return local?local.ground:off;}
