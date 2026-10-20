import test from 'node:test';
import assert from 'node:assert/strict';
import {randomUUID} from 'node:crypto';
import {mkdtemp,writeFile,chmod,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {newSecret,decodeSecret,signRequest,RESPONSE_SIGNATURE_HEADER} from '../scripts/home-inference/signature.mjs';
import {parseProfiles,parseKeys,startGateway} from '../scripts/home-inference/gateway.mjs';
import {createWorker,loadWorkerConfig,validLease} from '../scripts/home-inference/worker.mjs';
import {createHomeRelay,RELAY_LIMITS} from '../server/home-relay.mjs';
import {homeInferenceConfig,createRelayClient,HomeInferenceModel,homeWorkerRuntime} from '../server/home-inference.mjs';

const DIGEST='c'.repeat(64),gatewaySecret=newSecret(),workerSecret=newSecret();
const SITE='https://kansasfrontiermatrix.com';
const fast={...RELAY_LIMITS,leaseWaitMs:150,unleasedMs:300,leasedMs:{'/v1/health':2000,'/v1/chat':3000}};
const profile={id:'kfm-default-chat',label:'KFM default',model:'qwen3:4b',digest:'sha256:'+DIGEST,license:'Apache-2.0',capabilities:['chat'],scopes:['production'],contextTokens:8192,maxInputChars:10000,outputTokens:{brief:320,expanded:700},timeoutMs:{brief:20000,expanded:20000},options:{temperature:0.5},think:false,keepAlive:'30m'};
const env={KFM_HOSTED_AI:'1',KFM_HOSTED_AI_ORIGIN:SITE,KFM_AI_PROVIDER:'home-ollama',KFM_HOME_INFERENCE_TRANSPORT:'poll',KFM_HOME_INFERENCE_KEY_ID:'prod-1',KFM_HOME_INFERENCE_SECRET:gatewaySecret,KFM_HOME_INFERENCE_PROFILE:'kfm-default-chat',KFM_HOME_INFERENCE_DIGEST:'sha256:'+DIGEST,KFM_HOME_WORKER_KEY_ID:'worker-1',KFM_HOME_WORKER_SECRET:workerSecret};

// Loopback Ollama stand-in: identity routes plus one streamed reply.
function fakeOllama({hold=null}={}){
 const calls=[];
 const fetchImpl=async(url,init={})=>{
  const path=new URL(url).pathname;calls.push(path);
  if(path==='/api/version')return Response.json({version:'0.12.6'});
  if(path==='/api/tags')return Response.json({models:[{name:'qwen3:4b',model:'qwen3:4b',digest:DIGEST}]});
  const encoder=new TextEncoder();
  return new Response(new ReadableStream({async start(controller){
   init.signal?.addEventListener('abort',()=>{try{controller.error(new DOMException('aborted','AbortError'));}catch{}});
   controller.enqueue(encoder.encode(JSON.stringify({model:'qwen3:4b',message:{role:'assistant',content:'Relayed reply.'},done:false})+'\n'));
   if(hold)await hold;
   if(!init.signal?.aborted){controller.enqueue(encoder.encode(JSON.stringify({model:'qwen3:4b',message:{role:'assistant',content:''},done:true,done_reason:'stop',prompt_eval_count:40,eval_count:2,eval_duration:1e8})+'\n'));controller.close();}
  }}),{headers:{'Content-Type':'application/x-ndjson'}});
 };
 return {fetchImpl,calls};
}

async function setup({hold,limits=fast}={}){
 const ollama=fakeOllama({hold});
 const {server}=await startGateway({host:'127.0.0.1',port:0,ollamaUrl:'http://127.0.0.1:11434',profiles:parseProfiles({concurrency:1,maxQueue:1,profiles:[profile]}),keys:parseKeys({keys:[{id:'prod-1',scope:'production',secret:gatewaySecret}]})},{fetchImpl:ollama.fetchImpl,log:()=>{}});
 const gatewayOrigin='http://127.0.0.1:'+server.address().port;
 const diagnostics=[];
 const relay=createHomeRelay({keyId:'prod-1',secret:gatewaySecret,worker:{keyId:'worker-1',secret:decodeSecret(workerSecret)},limits,diagnostic:code=>diagnostics.push(code)});
 // The worker reaches the "website" through the relay handler and the gateway over real loopback HTTP.
 const toSite=(url,init)=>url.startsWith(SITE)?relay.handler(new Request(url,init)):fetch(url,init);
 const logs=[];
 const worker=createWorker({site:SITE,gateway:gatewayOrigin,keyId:'worker-1',secret:decodeSecret(workerSecret),fetchImpl:toSite,log:line=>logs.push(line)});
 const stop=new AbortController();
 const running={promise:null,start(){this.promise=worker.run(stop.signal);}};
 const signedPost=(path,payload,{keyId='worker-1',secret=workerSecret}={})=>{const body=JSON.stringify(payload);return relay.handler(new Request(SITE+path,{method:'POST',headers:{...signRequest({keyId,secret,method:'POST',path,body}),'Content-Type':'application/json'},body}));};
 const close=async()=>{stop.abort();await running.promise;server.closeAllConnections?.();await new Promise(resolve=>server.close(resolve));};
 return {relay,worker,running,ollama,logs,diagnostics,signedPost,close,gatewayOrigin};
}
const chatPayload=()=>({requestId:randomUUID(),profile:'kfm-default-chat',depth:'brief',messages:[{role:'system',content:'You are KFM.'},{role:'user',content:'Synthetic question?'}]});

test('poll transport needs a separate worker key and no inbound URL',()=>{
 const config=homeInferenceConfig(env);
 assert.equal(config.transport,'poll');assert.equal(config.origin,null);assert.equal(config.worker.keyId,'worker-1');
 assert.throws(()=>homeInferenceConfig({...env,KFM_HOME_WORKER_SECRET:''}),/HOME_WORKER_KEY_INVALID/);
 assert.throws(()=>homeInferenceConfig({...env,KFM_HOME_WORKER_SECRET:gatewaySecret}),/HOME_WORKER_KEY_REUSED/);
 assert.throws(()=>homeInferenceConfig({...env,KFM_HOME_INFERENCE_TRANSPORT:'carrier-pigeon'}),/HOME_INFERENCE_TRANSPORT_INVALID/);
 // The tunnel transport is unchanged: it still requires its exact HTTPS origin.
 assert.throws(()=>homeInferenceConfig({...env,KFM_HOME_INFERENCE_TRANSPORT:'https'}),/HOME_INFERENCE_URL_INVALID/);
});

test('the worker relays signed gateway calls end to end and the site verifies every reply',async()=>{
 const s=await setup();
 try{
  s.running.start();
  const model=new HomeInferenceModel({client:createRelayClient({relay:s.relay,secret:gatewaySecret}),profile:'kfm-default-chat',digest:'sha256:'+DIGEST,pollMs:60000,diagnostic:()=>{}});
  try{
   await model.refresh();
   assert.equal(model.ready,true,model.reason);assert.match(model.label,/qwen3:4b/);
   assert.deepEqual(await model.discuss('Synthetic question?',{depth:'brief'}),{text:'Relayed reply.',contextTrimmed:false,outputLimited:false});
  }finally{model.stop();}
  // The site settles the job before the worker logs its own completion line.
  const relayedChat=line=>line.event==='relayed'&&line.path==='/v1/chat'&&line.gatewayStatus===200&&line.siteStatus===200;
  for(let i=0;i<50&&!s.logs.some(relayedChat);i++)await new Promise(resolve=>setTimeout(resolve,20));
  assert.ok(s.logs.some(relayedChat));
  // Logs carry fixed fields only: no prompt, reply or key material.
  assert.ok(s.logs.every(line=>!/Synthetic question|Relayed reply|worker-1|secret/i.test(JSON.stringify(line))));
  assert.ok(s.diagnostics.includes('WORKER_CONNECTED'));
 }finally{await s.close();}
});

test('unsigned, wrong-key and replayed worker calls are refused before any job is handed out',async()=>{
 const s=await setup();
 try{
  const pending=s.relay.submit({method:'GET',path:'/v1/health',timeoutMs:2000});pending.catch(()=>{});
  const unsigned=await s.relay.handler(new Request(SITE+'/api/home-worker/v1/lease',{method:'POST',headers:{'Content-Type':'application/json'},body:'{}'}));
  assert.equal(unsigned.status,401);
  assert.equal((await s.signedPost('/api/home-worker/v1/lease',{},{secret:newSecret()})).status,401);
  // The gateway key is not a worker key.
  assert.equal((await s.signedPost('/api/home-worker/v1/lease',{},{keyId:'prod-1',secret:gatewaySecret})).status,401);
  const body='{}',headers={...signRequest({keyId:'worker-1',secret:workerSecret,method:'POST',path:'/api/home-worker/v1/lease',body}),'Content-Type':'application/json'};
  assert.equal((await s.relay.handler(new Request(SITE+'/api/home-worker/v1/lease',{method:'POST',headers,body}))).status,200);
  assert.equal((await s.relay.handler(new Request(SITE+'/api/home-worker/v1/lease',{method:'POST',headers,body}))).status,401,'replayed nonce');
  assert.equal((await s.relay.handler(new Request(SITE+'/api/home-worker/v1/lease',{method:'GET'}))).status,405);
  assert.equal((await s.signedPost('/api/home-worker/v1/admin',{})).status,404);
  await assert.rejects(pending,/GATEWAY_UNREACHABLE/);
 }finally{await s.close();}
});

test('a relay cannot forge, alter or replay a gateway reply',async()=>{
 const s=await setup();
 try{
  const client=createRelayClient({relay:s.relay,secret:gatewaySecret});
  const lease=async()=>(await s.signedPost('/api/home-worker/v1/lease',{})).json();
  const answer=(leaseId,reply)=>s.signedPost('/api/home-worker/v1/result',{leaseId,...reply});
  // Fetch the gateway's real signed reply to a leased request, as a relay would see it.
  const genuine=async job=>{
   const response=await fetch(s.gatewayOrigin+job.request.path,{method:job.request.method,headers:job.request.headers});
   return {status:response.status,contentType:response.headers.get('content-type'),signature:response.headers.get(RESPONSE_SIGNATURE_HEADER),bytes:Buffer.from(await response.arrayBuffer())};
  };
  const asResult=reply=>({status:reply.status,contentType:reply.contentType,signature:reply.signature,body:reply.bytes.toString('base64')});

  // 1. A fabricated reply without the gateway's signature.
  let pending=client.health();let job=await lease();
  await answer(job.leaseId,{status:200,contentType:'application/json',signature:'',body:Buffer.from(JSON.stringify({gateway:'kfm-home-inference/1',online:true,profiles:[]})).toString('base64')});
  await assert.rejects(pending,/GATEWAY_RESPONSE_INVALID/);

  // 2. A genuine reply, relayed unchanged, is accepted.
  pending=client.health();job=await lease();
  const first=await genuine(job);
  assert.equal((await answer(job.leaseId,asResult(first))).status,200);
  assert.equal((await pending).online,true);

  // 3. The same genuine reply replayed for a later request: its signature binds the old nonce.
  pending=client.health();job=await lease();
  await answer(job.leaseId,asResult(first));
  await assert.rejects(pending,/GATEWAY_RESPONSE_INVALID/);

  // 4. A genuine reply with one byte altered.
  pending=client.health();job=await lease();
  const altered=await genuine(job);altered.bytes[altered.bytes.length-2]^=1;
  await answer(job.leaseId,asResult(altered));
  await assert.rejects(pending,/GATEWAY_RESPONSE_INVALID/);

  // Late and duplicate results for settled or unknown leases are dropped.
  assert.equal((await answer(job.leaseId,{error:'GATEWAY_UNREACHABLE'})).status,410);
  assert.equal((await answer('A'.repeat(24),{error:'GATEWAY_UNREACHABLE'})).status,410);
 }finally{await s.close();}
});

test('no connected worker means chat is unavailable quickly, never a queued hang',async()=>{
 const s=await setup();
 try{
  const model=new HomeInferenceModel({client:createRelayClient({relay:s.relay,secret:gatewaySecret}),profile:'kfm-default-chat',digest:'sha256:'+DIGEST,pollMs:60000,diagnostic:()=>{}});
  const started=Date.now();await model.refresh();
  assert.equal(model.ready,false);assert.equal(model.online,false);assert.equal(model.reason,'GATEWAY_UNREACHABLE');
  assert.ok(Date.now()-started<2000);
  model.stop();
  assert.equal(s.relay.queued,0);
 }finally{await s.close();}
});

test('a cancelled chat stops at the gateway and its late result is dropped',async()=>{
 let release;const hold=new Promise(resolve=>{release=resolve;});
 const s=await setup({hold});
 try{
  const controller=new AbortController();
  const client=createRelayClient({relay:s.relay,secret:gatewaySecret});
  const chat=client.chat(chatPayload(),{signal:controller.signal,timeoutMs:3000});chat.catch(()=>{});
  const lease=await (await s.signedPost('/api/home-worker/v1/lease',{})).json();
  assert.equal((await (await s.signedPost('/api/home-worker/v1/status',{leaseId:lease.leaseId})).json()).active,true);
  const relaying=s.worker.relay(lease);
  controller.abort();
  await assert.rejects(chat,/MODEL_CANCELLED/);
  assert.equal((await (await s.signedPost('/api/home-worker/v1/status',{leaseId:lease.leaseId})).json()).active,false);
  // The worker's status check aborts the gateway call within one interval.
  await Promise.race([relaying,new Promise((_,reject)=>setTimeout(()=>reject(Error('relay did not stop')),8000))]);
  assert.ok(s.logs.some(line=>line.event==='relay_cancelled'));
  release();
 }finally{release?.();await s.close();}
});

test('the worker refuses leases outside the two gateway routes and forwards only signature headers',()=>{
 const base={leaseId:'B'.repeat(24),request:{method:'POST',path:'/v1/chat',headers:{'x-kfm-key-id':'prod-1','x-kfm-timestamp':'1','x-kfm-nonce':'n','x-kfm-signature':'s','content-type':'application/json'},body:'{}'}};
 assert.equal(validLease(base),true);
 for(const bad of [
  {...base,request:{...base.request,path:'/api/pull'}},
  {...base,request:{...base.request,method:'GET'}},
  {...base,request:{...base.request,headers:{...base.request.headers,host:'evil.example'}}},
  {...base,request:{...base.request,headers:{...base.request.headers,'x-kfm-nonce':'a\r\nInjected: 1'}}},
  {...base,request:{...base.request,body:'x'.repeat(40000)}},
  {...base,leaseId:'short'},
 ])assert.equal(validLease(bad),false,JSON.stringify(bad).slice(0,80));
});

test('the relay bounds its queue and the worker route exists only in poll mode on the exact origin',async()=>{
 const relay=createHomeRelay({keyId:'prod-1',secret:gatewaySecret,worker:{keyId:'worker-1',secret:decodeSecret(workerSecret)},limits:{...fast,queue:2,unleasedMs:5000},diagnostic:()=>{}});
 const held=[relay.submit({method:'GET',path:'/v1/health',timeoutMs:5000}),relay.submit({method:'GET',path:'/v1/health',timeoutMs:5000})];held.forEach(p=>p.catch(()=>{}));
 await assert.rejects(relay.submit({method:'GET',path:'/v1/health',timeoutMs:5000}),/GATEWAY_BUSY/);
 await assert.rejects(relay.submit({method:'DELETE',path:'/api/delete',timeoutMs:5000}),/GATEWAY_RESPONSE_INVALID/);
 const off=homeWorkerRuntime({...env,KFM_HOME_INFERENCE_TRANSPORT:'https'});
 assert.equal((await off(new Request(SITE+'/api/home-worker/v1/lease',{method:'POST'}))).status,404);
 assert.equal((await homeWorkerRuntime({...env,KFM_HOSTED_AI:'0'})(new Request(SITE+'/api/home-worker/v1/lease',{method:'POST'}))).status,404);
 const on=homeWorkerRuntime(env);
 assert.equal((await on(new Request('https://www.kansasfrontiermatrix.com/api/home-worker/v1/lease',{method:'POST'}))).status,503);
 assert.equal((await on(new Request(SITE+'/api/home-worker/v1/lease',{method:'POST',body:'{}'}))).status,401);
});

test('the worker key file must be owner-only unless systemd provides it',async()=>{
 const dir=await mkdtemp(join(tmpdir(),'kfm-worker-'));
 try{
  const keyPath=join(dir,'worker-key.json');
  await writeFile(keyPath,JSON.stringify({id:'worker-1',scope:'worker',secret:workerSecret}));
  await chmod(keyPath,0o640);
  assert.throws(()=>loadWorkerConfig({KFM_WORKER_SITE:SITE,KFM_WORKER_KEY_FILE:keyPath}),/WORKER_KEY_PERMISSIONS/);
  assert.equal(loadWorkerConfig({KFM_WORKER_SITE:SITE,CREDENTIALS_DIRECTORY:dir}).keyId,'worker-1');
  await chmod(keyPath,0o600);
  assert.equal(loadWorkerConfig({KFM_WORKER_SITE:SITE,KFM_WORKER_KEY_FILE:keyPath}).gateway,'http://127.0.0.1:8787');
  assert.throws(()=>loadWorkerConfig({KFM_WORKER_SITE:'http://kansasfrontiermatrix.com',KFM_WORKER_KEY_FILE:keyPath}),/WORKER_SITE_INVALID/);
  assert.throws(()=>loadWorkerConfig({KFM_WORKER_SITE:SITE+'/api',KFM_WORKER_KEY_FILE:keyPath}),/WORKER_SITE_INVALID/);
  assert.throws(()=>loadWorkerConfig({KFM_WORKER_SITE:SITE,KFM_WORKER_GATEWAY:'http://192.168.86.25:8787',KFM_WORKER_KEY_FILE:keyPath}),/WORKER_GATEWAY_NOT_LOOPBACK/);
 }finally{await rm(dir,{recursive:true,force:true});}
});
