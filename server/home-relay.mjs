// Outbound-only transport for home inference (KFM_HOME_INFERENCE_TRANSPORT=poll).
// The inference PC's worker long-polls this server for gateway requests and posts
// back the gateway's replies, so the PC needs no inbound route, tunnel or DNS.
// The worker is a relay only: this server signs each gateway request when it is
// leased and verifies each signed reply itself (server/home-inference.mjs), so a
// worker cannot create, alter or replay a request or a reply.
import {randomBytes} from 'node:crypto';
import {createNonceCache,decodeSecret,signRequest,verifyRequest,RESPONSE_SIGNATURE_HEADER} from '../scripts/home-inference/signature.mjs';

import {INFERENCE_BUDGETS} from '../scripts/home-inference/budgets.mjs';

export const RELAY_LIMITS=Object.freeze({
 queue:8,requestBytes:131072,bodyMs:5000,replyBytes:65536,
 // A long-poll is held this long before an idle 204; the worker re-polls at once.
 leaseWaitMs:20000,
 // A job nobody leases within this time means no worker is connected.
 unleasedMs:15000,
 // Allow the complete gateway queue and run, plus signed return overhead.
 leasedMs:Object.freeze({'/v1/health':15000,'/v1/chat':INFERENCE_BUDGETS.relayMs}),
});
const ROUTES=new Map([['/v1/health','GET'],['/v1/chat','POST']]);
const WORKER_ERRORS=new Set(['GATEWAY_UNREACHABLE','GATEWAY_REDIRECT','GATEWAY_RESPONSE_INVALID']);
const LEASE_ID=/^[A-Za-z0-9_-]{24}$/;
const error=code=>Object.assign(new Error(code),{code});
const json=(value,status=200)=>Response.json(value,{status,headers:{'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}});

// The worker key must differ from the gateway key, so neither can stand in for the other.
export function homeWorkerKey(env,gatewaySecret){
 const keyId=env.KFM_HOME_WORKER_KEY_ID??'',secret=decodeSecret(env.KFM_HOME_WORKER_SECRET??'');
 if(!/^[A-Za-z0-9._-]{1,64}$/.test(keyId)||!secret)throw error('HOME_WORKER_KEY_INVALID');
 const gateway=decodeSecret(gatewaySecret);
 if(gateway&&gateway.equals(secret))throw error('HOME_WORKER_KEY_REUSED');
 return Object.freeze({keyId,secret});
}

async function readBody(request){
 const reader=request.body?.getReader();if(!reader)return '';
 const chunks=[];let bytes=0,timer;
 const timeout=new Promise((_,reject)=>{timer=setTimeout(()=>reject(error('BODY_TIMEOUT')),RELAY_LIMITS.bodyMs);});
 try{while(true){const part=await Promise.race([reader.read(),timeout]);if(part.done)break;bytes+=part.value.length;if(bytes>RELAY_LIMITS.requestBytes)throw error('REQUEST_TOO_LARGE');chunks.push(Buffer.from(part.value));}}
 finally{clearTimeout(timer);await reader.cancel().catch(()=>{});}
 return Buffer.concat(chunks).toString('utf8');
}

export function createHomeRelay({keyId,secret,worker,clock=Date.now,limits=RELAY_LIMITS,diagnostic=code=>console.warn('[KFM home relay] '+code)}){
 const queue=[],leased=new Map(),nonces=createNonceCache({clock}),workerKeys=new Map([[worker.keyId,{id:worker.keyId,secret:worker.secret}]]);
 let waiter=null,lastSeen=0;const noted=new Map();
 // Fixed codes only, and each at most once a minute so refused traffic cannot flood logs.
 const note=code=>{const now=clock();if(now-(noted.get(code)??-Infinity)<60000)return;noted.set(code,now);try{diagnostic(code);}catch{}};
 const settle=(job,outcome)=>{
  if(job.done)return;job.done=true;clearTimeout(job.timer);job.signal?.removeEventListener('abort',job.onAbort);
  const index=queue.indexOf(job);if(index>=0)queue.splice(index,1);
  leased.delete(job.id);
  if(outcome instanceof Error)job.reject(outcome);else job.resolve(outcome);
 };
 const arm=(job,ms,code)=>{clearTimeout(job.timer);job.timer=setTimeout(()=>settle(job,error(code)),Math.max(1,Math.min(ms,job.deadline-clock())));job.timer.unref?.();};
 const take=()=>{
  const job=queue.shift();if(!job)return null;
  // Sign at hand-over so the gateway's 60 s freshness window covers the relay.
  const requestHeaders={...signRequest({keyId,secret,method:job.method,path:job.path,body:job.body,now:clock()}),...(job.body?{'content-type':'application/json'}:{})};
  job.requestHeaders=requestHeaders;job.state='leased';leased.set(job.id,job);
  arm(job,limits.leasedMs[job.path],'GATEWAY_UNREACHABLE');
  return {leaseId:job.id,request:{method:job.method,path:job.path,headers:requestHeaders,body:job.body}};
 };

 // Server side: one gateway call, resolved with the raw signed reply for the caller to verify.
 const submit=({method,path,body='',signal,timeoutMs})=>new Promise((resolve,reject)=>{
  if(ROUTES.get(path)!==method)return reject(error('GATEWAY_RESPONSE_INVALID'));
  if(signal?.aborted)return reject(error('MODEL_CANCELLED'));
  if(queue.length>=limits.queue)return reject(error('GATEWAY_BUSY'));
  const job={id:randomBytes(18).toString('base64url'),method,path,body,state:'queued',deadline:clock()+timeoutMs,resolve,reject,signal,done:false};
  job.onAbort=()=>settle(job,error('MODEL_CANCELLED'));
  signal?.addEventListener('abort',job.onAbort,{once:true});
  // The PC worker is serial. A known leased chat can occupy it while another
  // connection waits; that wait must not be mistaken for an absent worker.
  const occupied=[...leased.values()].some(item=>item.path==='/v1/chat');
  const ahead=[...leased.values(),...queue].filter(item=>item.path==='/v1/chat').length;
  const waitMs=path==='/v1/chat'&&occupied?Math.min(INFERENCE_BUDGETS.queueMs,ahead*INFERENCE_BUDGETS.queueSlotMs):0;
  arm(job,limits.unleasedMs+waitMs,'GATEWAY_UNREACHABLE');
  queue.push(job);
  if(waiter){const wake=waiter;waiter=null;wake();}
 });

 const lease=async request=>{
  const ready=take();if(ready)return json(ready);
  // Hold one long-poll. A newer poll from the worker replaces an older one.
  if(waiter){const previous=waiter;waiter=null;previous();}
  await new Promise(resolve=>{
   const timer=setTimeout(done,limits.leaseWaitMs);timer.unref?.();
   function done(){clearTimeout(timer);request.signal?.removeEventListener?.('abort',done);if(waiter===done)waiter=null;resolve();}
   waiter=done;request.signal?.addEventListener?.('abort',done,{once:true});
  });
  const next=take();
  return next?json(next):new Response(null,{status:204,headers:{'Cache-Control':'no-store'}});
 };

 const result=value=>{
  const job=LEASE_ID.test(value?.leaseId??'')?leased.get(value.leaseId):undefined;
  // Unknown, expired, cancelled or already answered: a late or duplicate reply is dropped.
  if(!job)return json({reasonCode:'LEASE_GONE'},410);
  if(typeof value.error==='string'){settle(job,error(WORKER_ERRORS.has(value.error)?value.error:'GATEWAY_UNREACHABLE'));return json({accepted:true});}
  const status=value.status,bytes=typeof value.body==='string'&&/^[A-Za-z0-9+/]*={0,2}$/.test(value.body)?Buffer.from(value.body,'base64'):null;
  if(!Number.isInteger(status)||status<200||status>599||!bytes||bytes.length>limits.replyBytes||typeof value.contentType!=='string'||value.contentType.length>100||typeof value.signature!=='string'||value.signature.length>100){
   settle(job,error('GATEWAY_RESPONSE_INVALID'));return json({reasonCode:'RESULT_INVALID'},400);
  }
  settle(job,{status,bytes,requestHeaders:job.requestHeaders,headers:new Headers({'content-type':value.contentType,[RESPONSE_SIGNATURE_HEADER]:value.signature})});
  return json({accepted:true});
 };

 // Worker side: signed POST /api/home-worker/v1/{lease,status,result}.
 const handler=async request=>{
  const url=new URL(request.url),path=url.pathname;
  if(request.method!=='POST')return json({reasonCode:'METHOD_DENIED'},405);
  if(url.search||!/^\/api\/home-worker\/v1\/(?:lease|status|result)$/.test(path))return json({reasonCode:'ROUTE_NOT_FOUND'},404);
  let body;try{body=await readBody(request);}catch(failure){return json({reasonCode:failure.code==='REQUEST_TOO_LARGE'?'REQUEST_TOO_LARGE':'INVALID_REQUEST'},failure.code==='REQUEST_TOO_LARGE'?413:400);}
  const auth=verifyRequest({headers:request.headers,method:'POST',path,body,keys:workerKeys,nonces,now:clock()});
  if(!auth.ok){note('WORKER_UNAUTHORIZED:'+auth.reason);return json({reasonCode:'UNAUTHORIZED'},401);}
  if(clock()-lastSeen>60000)note('WORKER_CONNECTED');
  lastSeen=clock();
  let value;try{value=body?JSON.parse(body):{};}catch{return json({reasonCode:'INVALID_REQUEST'},400);}
  if(!value||typeof value!=='object'||Array.isArray(value))return json({reasonCode:'INVALID_REQUEST'},400);
  if(path.endsWith('/lease'))return lease(request);
  if(path.endsWith('/status'))return json({active:leased.get(value.leaseId)?.state==='leased'});
  return result(value);
 };

 return {submit,handler,get queued(){return queue.length;},get leased(){return leased.size;},get lastSeen(){return lastSeen;}};
}

// One relay per process: the worker route and the public chat provider must share it.
const SHARED=Symbol.for('kfm.home-relay');
export function getHomeRelay(config){
 return globalThis[SHARED]??=createHomeRelay({keyId:config.keyId,secret:config.secret,worker:config.worker});
}
