#!/usr/bin/env node
// KFM home inference worker: the outbound-only link between the KFM website and
// the loopback gateway, for homes where no tunnel or DNS change is wanted. It
// long-polls the site for gateway requests, relays each one unchanged to
// 127.0.0.1:8787, and posts the gateway's reply bytes back. It holds no gateway
// key: the site signs every request and verifies every reply, so this worker
// cannot create, alter or replay either. No dependencies.
//
//   node worker.mjs            run (systemd does this)
//   node worker.mjs --check    one signed idle poll: proves the site accepts this worker key
import {readFileSync,statSync} from 'node:fs';
import {join} from 'node:path';
import {pathToFileURL} from 'node:url';
import {setTimeout as sleep} from 'node:timers/promises';
import {decodeSecret,signRequest,isSystemdCredentialDirectory,RESPONSE_SIGNATURE_HEADER,SIGNATURE_HEADERS} from './signature.mjs';

export const WORKER_VERSION='kfm-home-worker/1';
export const WORKER_LIMITS=Object.freeze({leaseMs:30000,siteMs:15000,relayMs:230000,statusEveryMs:5000,leaseBytes:65536,replyBytes:65536,backoffMinMs:1000,backoffMaxMs:60000});
// Only the gateway's two routes, and only these request headers, ever reach the gateway.
const ROUTES=new Map([['/v1/health','GET'],['/v1/chat','POST']]);
const FORWARD=[SIGNATURE_HEADERS.keyId,SIGNATURE_HEADERS.timestamp,SIGNATURE_HEADERS.nonce,SIGNATURE_HEADERS.signature,'content-type'];
const LEASE_ID=/^[A-Za-z0-9_-]{24}$/;
const fail=code=>Object.assign(new Error(code),{code});
const isLoopback=host=>['127.0.0.1','::1','[::1]','localhost'].includes(host);

function exactOrigin(value,{loopbackOnly=false}={}){
 let url;try{url=new URL(value);}catch{return null;}
 const httpLoopback=url.protocol==='http:'&&isLoopback(url.hostname);
 if(loopbackOnly?!httpLoopback:!(url.protocol==='https:'||httpLoopback))return null;
 if(url.username||url.password||url.pathname!=='/'||url.search||url.hash)return null;
 return url.origin;
}

export function loadWorkerConfig(env=process.env,{credentialsRoot}={}){
 // The website must be one exact HTTPS origin; plain HTTP only for a same-machine proof.
 const site=exactOrigin(env.KFM_WORKER_SITE??'');if(!site)throw fail('WORKER_SITE_INVALID');
 const gateway=exactOrigin(env.KFM_WORKER_GATEWAY||'http://127.0.0.1:8787',{loopbackOnly:true});if(!gateway)throw fail('WORKER_GATEWAY_NOT_LOOPBACK');
 const path=env.KFM_WORKER_KEY_FILE||(env.CREDENTIALS_DIRECTORY?join(env.CREDENTIALS_DIRECTORY,'worker-key.json'):'');
 const credential=!env.KFM_WORKER_KEY_FILE&&isSystemdCredentialDirectory(env.CREDENTIALS_DIRECTORY,{root:credentialsRoot});
 if(!path)throw fail('WORKER_KEY_NOT_CONFIGURED');
 const stat=statSync(path);
 if(!stat.isFile()||stat.size>4096)throw fail('WORKER_KEY_INVALID');
 // As for the gateway's key file: systemd's credential ACL shows as group read.
 if(stat.mode&(credential?0o007:0o077))throw fail('WORKER_KEY_PERMISSIONS');
 let value;try{value=JSON.parse(readFileSync(path,'utf8'));}catch{throw fail('WORKER_KEY_INVALID');}
 const secret=decodeSecret(value?.secret);
 if(!/^[A-Za-z0-9._-]{1,64}$/.test(value?.id??'')||!secret)throw fail('WORKER_KEY_INVALID');
 return {site,gateway,keyId:value.id,secret};
}

async function boundedBytes(response,limit){
 const reader=response.body?.getReader();if(!reader)return Buffer.alloc(0);
 const chunks=[];let bytes=0;
 try{while(true){const part=await reader.read();if(part.done)break;bytes+=part.value.length;if(bytes>limit)throw fail('RESPONSE_TOO_LARGE');chunks.push(Buffer.from(part.value));}}
 finally{await reader.cancel().catch(()=>{});}
 return Buffer.concat(chunks);
}

// The lease is site content, so it is checked before anything is sent to the gateway.
export function validLease(value){
 if(!value||typeof value!=='object'||!LEASE_ID.test(value.leaseId??''))return false;
 const request=value.request;
 if(!request||typeof request!=='object'||ROUTES.get(request.path)!==request.method)return false;
 if(typeof request.body!=='string'||Buffer.byteLength(request.body)>32768||request.method==='GET'&&request.body)return false;
 const headers=request.headers;
 if(!headers||typeof headers!=='object'||Array.isArray(headers))return false;
 return Object.entries(headers).every(([name,header])=>FORWARD.includes(name)&&typeof header==='string'&&header.length<=200&&!/[\r\n]/.test(header));
}

export function createWorker({site,gateway,keyId,secret,fetchImpl=fetch,clock=Date.now,log=line=>console.log(JSON.stringify(line))}){
 const record=(event,fields={})=>{try{log({at:new Date(clock()).toISOString(),event,...fields});}catch{}};
 const post=(path,payload,timeoutMs,signal)=>{
  const body=JSON.stringify(payload);
  const headers={...signRequest({keyId,secret,method:'POST',path,body,now:clock()}),'Content-Type':'application/json'};
  return fetchImpl(site+path,{method:'POST',headers,body,redirect:'error',cache:'no-store',signal:signal?AbortSignal.any([signal,AbortSignal.timeout(timeoutMs)]):AbortSignal.timeout(timeoutMs)});
 };
 const report=async(payload)=>{const response=await post('/api/home-worker/v1/result',payload,WORKER_LIMITS.siteMs);await response.body?.cancel().catch(()=>{});return response.status;};

 // One lease: relay it, and stop early if the site cancels it.
 const relay=async lease=>{
  const {request}=lease,started=clock(),controller=new AbortController();
  const watch=setInterval(async()=>{
   try{const response=await post('/api/home-worker/v1/status',{leaseId:lease.leaseId},WORKER_LIMITS.siteMs);const state=response.ok?await response.json():null;if(state&&state.active===false)controller.abort();}catch{}
  },WORKER_LIMITS.statusEveryMs);watch.unref?.();
  try{
   let response;
   try{response=await fetchImpl(gateway+request.path,{method:request.method,headers:Object.fromEntries(Object.entries(request.headers).filter(([name])=>FORWARD.includes(name))),body:request.body||undefined,redirect:'manual',cache:'no-store',signal:AbortSignal.any([controller.signal,AbortSignal.timeout(WORKER_LIMITS.relayMs)])});}
   catch{
    if(controller.signal.aborted){record('relay_cancelled',{path:request.path,ms:clock()-started});return;}
    record('relay_failed',{path:request.path,code:'GATEWAY_UNREACHABLE'});await report({leaseId:lease.leaseId,error:'GATEWAY_UNREACHABLE'});return;
   }
   if(response.status>=300&&response.status<400){await response.body?.cancel().catch(()=>{});await report({leaseId:lease.leaseId,error:'GATEWAY_REDIRECT'});return;}
   let bytes;
   try{bytes=await boundedBytes(response,WORKER_LIMITS.replyBytes);}
   catch{if(controller.signal.aborted)return;await report({leaseId:lease.leaseId,error:'GATEWAY_RESPONSE_INVALID'});return;}
   const status=await report({leaseId:lease.leaseId,status:response.status,contentType:response.headers.get('content-type')??'',signature:response.headers.get(RESPONSE_SIGNATURE_HEADER)??'',body:bytes.toString('base64')});
   // Operational metadata only: never prompts, replies or keys.
   record('relayed',{path:request.path,gatewayStatus:response.status,siteStatus:status,ms:clock()-started});
  }finally{clearInterval(watch);}
 };

 // One poll. Returns 'idle', 'relayed' or throws a fixed code for back-off.
 const once=async signal=>{
  const response=await post('/api/home-worker/v1/lease',{worker:WORKER_VERSION},WORKER_LIMITS.leaseMs,signal);
  if(response.status===204){await response.body?.cancel().catch(()=>{});return 'idle';}
  if(response.status!==200){await response.body?.cancel().catch(()=>{});throw fail('SITE_HTTP_'+response.status);}
  let lease;try{lease=JSON.parse((await boundedBytes(response,WORKER_LIMITS.leaseBytes)).toString('utf8'));}catch{throw fail('LEASE_INVALID');}
  if(!validLease(lease)){
   if(LEASE_ID.test(lease?.leaseId??''))await report({leaseId:lease.leaseId,error:'GATEWAY_RESPONSE_INVALID'}).catch(()=>{});
   throw fail('LEASE_INVALID');
  }
  await relay(lease);
  return 'relayed';
 };

 const run=async signal=>{
  let backoff=0,lastCode=null;
  record('started',{worker:WORKER_VERSION,site:new URL(site).host,gateway:new URL(gateway).host});
  while(!signal?.aborted){
   try{await once(signal);if(lastCode){record('reconnected');lastCode=null;}backoff=0;}
   catch(error){
    if(signal?.aborted)break;
    const code=error?.code??(error?.name==='TimeoutError'?'SITE_TIMEOUT':'SITE_UNREACHABLE');
    if(code!==lastCode){record('poll_failed',{code});lastCode=code;}
    // Exponential back-off with jitter, so an outage at either end does not hammer the site.
    backoff=Math.min(WORKER_LIMITS.backoffMaxMs,Math.max(WORKER_LIMITS.backoffMinMs,backoff*2));
    await sleep(backoff/2+Math.random()*backoff/2,undefined,{signal}).catch(()=>{});
   }
  }
  record('stopped');
 };
 return {once,run,relay};
}

async function main(argv){
 let config;
 try{config=loadWorkerConfig();}catch(error){console.error(JSON.stringify({event:'config_refused',code:error.code??'CONFIG_INVALID'}));return 1;}
 const worker=createWorker(config);
 if(argv[0]==='--check'){
  try{const outcome=await worker.once();console.log(JSON.stringify({event:'check',result:outcome==='idle'?'SITE_ACCEPTS_WORKER_KEY':'RELAYED_ONE_JOB'}));return 0;}
  catch(error){console.error(JSON.stringify({event:'check',result:'FAILED',code:error?.code??'SITE_UNREACHABLE'}));return 1;}
 }
 const controller=new AbortController();
 process.once('SIGTERM',()=>controller.abort());process.once('SIGINT',()=>controller.abort());
 await worker.run(controller.signal);
 return 0;
}

if(import.meta.url===pathToFileURL(process.argv[1]??'').href)main(process.argv.slice(2)).then(code=>{process.exitCode=code;});
