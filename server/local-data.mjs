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

export function createLocalDataService({config,clock=Date.now,relay=createHomeRelay({keyId:config.keyId,secret:config.secret,worker:config.worker,clock,limits:LOCAL_DATA_RELAY_LIMITS,routes:LOCAL_DATA_ROUTES,workerPrefix:LOCAL_DATA_WORKER_PREFIX,diagnostic:code=>console.warn('[KFM local data] '+code)})}){
 const cache=new Map(),pending=new Map();let cachedBytes=0;
 const forget=key=>{const hit=cache.get(key);if(hit){cachedBytes-=hit.bytes;cache.delete(key);}};
 const remember=(key,value,bytes)=>{
  forget(key);cache.set(key,{value,bytes,at:clock()});cachedBytes+=bytes;
  while(cache.size>LOCAL_DATA_CACHE.entries||cachedBytes>LOCAL_DATA_CACHE.bytes)forget(cache.keys().next().value);
 };

 // A reply is parsed only after the gateway's signature over this exact request, status and body checks out.
 const call=async(method,path,payload)=>{
  if(clock()-relay.lastSeen>LOCAL_DATA_CACHE.workerSeenMs)throw error('LOCAL_DATA_UNAVAILABLE');
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
  if(hit&&age<LOCAL_DATA_CACHE.freshMs)return answer(hit.value,'fresh',hit.at,300);
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
   if(hit&&age<LOCAL_DATA_CACHE.staleMs)return answer(hit.value,'stale',hit.at,60);
   if(failure.code==='DATASET_NOT_READY')return json({state:'local-data-preparing',reasonCode:'DATASET_NOT_READY'},503);
   return json({state:'local-data-offline',reasonCode:'LOCAL_DATA_UNAVAILABLE'},503);
  }
 };

 /** GET /api/local-data: what can be asked, and whether the PC is connected. No trip to the PC. */
 const catalog=async request=>{
  if(request.method!=='GET')return json({reasonCode:'METHOD_DENIED'},405);
  return json({format:'kfm-local-data-catalog-v1',online:clock()-relay.lastSeen<=LOCAL_DATA_CACHE.workerSeenMs,datasets:datasetCatalog()},200,'public, max-age=60');
 };
 return {query,catalog,workerHandler:relay.handler,relay};
}

// One service per process: the worker route and the public routes must share one relay.
const SHARED=Symbol.for('kfm.local-data');
function service(env){
 try{return globalThis[SHARED]??=createLocalDataService({config:localDataConfig(env)});}catch{return null;}
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
