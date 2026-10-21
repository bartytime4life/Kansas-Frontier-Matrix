import test from 'node:test';
import assert from 'node:assert/strict';
import {EventEmitter} from 'node:events';
import {randomUUID} from 'node:crypto';
import {newSecret,signRequest,signResponse,verifyResponse,RESPONSE_SIGNATURE_HEADER} from '../scripts/home-inference/signature.mjs';
import {createGateway,parseProfiles,parseKeys,GATEWAY_LIMITS} from '../scripts/home-inference/gateway.mjs';
import {createHomeInferenceClient,HomeInferenceModel} from '../server/home-inference.mjs';
import {probe} from '../scripts/home-inference/probe.mjs';

const secret=newSecret(),digest='sha256:'+'a'.repeat(64),other='b'.repeat(64);
const profile=(overrides={})=>({id:'test-chat',label:'Synthetic',model:'qwen3:8b',digest,license:'Apache-2.0',capabilities:['chat'],scopes:['production'],contextTokens:8192,maxInputChars:12000,outputTokens:{brief:64,expanded:128},timeoutMs:{brief:500,expanded:500},...overrides});
const payload=(overrides={})=>({requestId:randomUUID(),profile:'test-chat',depth:'brief',messages:[{role:'user',content:'Synthetic only'}],...overrides});
const tick=()=>new Promise(resolve=>setImmediate(resolve));
const waitFor=async predicate=>{
 for(let i=0;i<100&&!predicate();i++)await tick();
 assert.ok(predicate(),'gateway reached the expected admission state');
};
const reloadProfiles=(gateway,overrides={})=>gateway.reload({profiles:parseProfiles({profiles:[profile({timeoutMs:{brief:5000,expanded:5000}})],concurrency:1,maxQueue:1,...overrides})});

// Exercise the real gateway handler and client without opening a network port.
// The original home-inference suite separately covers actual HTTP sockets in CI.
function transport(handler){
 return (url,init={})=>new Promise((resolve,reject)=>{
  const req=new EventEmitter(),res=new EventEmitter();
  Object.assign(req,{method:init.method??'GET',url:new URL(url).pathname,headers:Object.fromEntries(new Headers(init.headers)),destroy(){}});
  const headers=new Headers();
  Object.assign(res,{headersSent:false,destroyed:false,writableFinished:false,
   setHeader(name,value){headers.set(name,String(value));},
   writeHead(status,values){this.status=status;this.headersSent=true;for(const [name,value]of Object.entries(values))headers.set(name,String(value));},
   end(body,callback){this.writableFinished=true;resolve(new Response(body,{status:this.status,headers}));this.emit('close');callback?.();},
  });
  const abort=()=>{res.destroyed=true;res.emit('close');reject(new DOMException('aborted','AbortError'));};
  if(init.signal?.aborted){abort();return;}
  init.signal?.addEventListener('abort',abort,{once:true});
  res.once('close',()=>init.signal?.removeEventListener('abort',abort));
  void handler(req,res);
  queueMicrotask(()=>{if(init.body)req.emit('data',Buffer.from(init.body));req.emit('end');});
 });
}

function fixture({profileOverrides={},hold=false,queue=1,inspectHold=null}={}){
 const runtime={tags:[{name:'qwen3:8b',digest:digest.slice(7)}],down:false,generations:[],reportedModel:'qwen3:8b',versionHolds:[],tagReads:0};
 const fetchImpl=async(url,init={})=>{
  if(runtime.down)throw new TypeError('offline');
  if(url.endsWith('/api/version')){if(inspectHold)await inspectHold;const hold=runtime.versionHolds.shift();if(hold)await hold;return Response.json({version:'synthetic'});}
  if(url.endsWith('/api/tags')){runtime.tagReads++;return Response.json({models:runtime.tags});}
  if(url.endsWith('/api/show'))return Response.json({thinking:{values:[false,true],default:false}});
  assert.ok(url.endsWith('/api/chat'));
  return new Response(new ReadableStream({start(controller){
   runtime.generations.push({signal:init.signal,messages:JSON.parse(init.body).messages,finish(){
    if(init.signal.aborted)return;
    controller.enqueue(new TextEncoder().encode(JSON.stringify({model:runtime.reportedModel,message:{content:'Synthetic reply'},done:true,prompt_eval_count:12,eval_count:2})+'\n'));
    controller.close();
   }});
   init.signal.addEventListener('abort',()=>{try{controller.error(new DOMException('aborted','AbortError'));}catch{}},{once:true});
   if(!hold)runtime.generations.at(-1).finish();
  }}));
 };
 const gateway=createGateway({profiles:parseProfiles({profiles:[profile(profileOverrides)],maxQueue:queue}),keys:parseKeys({keys:[{id:'test',scope:'production',secret}]}),fetchImpl,log:()=>{}});
 const wire=transport(gateway.handler);
 const client=createHomeInferenceClient({origin:'https://synthetic.invalid',keyId:'test',secret,fetchImpl:wire});
 return {runtime,gateway,wire,client};
}

test('response authentication binds exact bytes, status and every request component',()=>{
 const method='POST',path='/v1/chat',requestBody=JSON.stringify(payload()),status=200,body='{"text":"Synthetic"}';
 const requestHeaders=signRequest({keyId:'test',secret,method,path,body:requestBody});
 const args={secret,requestHeaders,method,path,requestBody,status,body};
 const headers={[RESPONSE_SIGNATURE_HEADER]:signResponse(args)};
 assert.equal(verifyResponse({...args,headers}),true);
 for(const changed of [{body:body+' '},{status:503},{method:'GET'},{path:'/v1/health'},{requestBody:requestBody+' '},{secret:newSecret()},
  ...['x-kfm-key-id','x-kfm-timestamp','x-kfm-nonce'].map(name=>({requestHeaders:{...requestHeaders,[name]:requestHeaders[name]+'x'}}))])
  assert.equal(verifyResponse({...args,...changed,headers}),false);
 assert.equal(verifyResponse({...args,headers:{}}),false);
 assert.equal(verifyResponse({...args,headers:{[RESPONSE_SIGNATURE_HEADER]:'bad'}}),false);
});

test('client rejects unsigned health, tampered bodies, changed status and replayed health',async()=>{
 const f=fixture();let first;
 for(const mode of ['unsigned','body','status','replay']){
  const client=createHomeInferenceClient({origin:'https://synthetic.invalid',keyId:'test',secret,fetchImpl:async(url,init)=>{
   if(mode==='replay'&&first)return new Response(first.body,{status:200,headers:first.headers});
   const response=await f.wire(url,init),body=await response.text(),headers=new Headers(response.headers);
   if(mode==='unsigned')headers.delete(RESPONSE_SIGNATURE_HEADER);
   if(mode==='replay')first={body,headers};
   return new Response(mode==='body'?body+' ':body,{status:mode==='status'?503:response.status,headers});
  }});
  if(mode==='replay')await client.health();
  await assert.rejects(client.health(),/GATEWAY_RESPONSE_INVALID/);
 }
 assert.equal(f.runtime.generations.length,0);
});

test('health, chat and authenticated refusal replies all verify through the real handler',async()=>{
 const f=fixture();
 assert.equal((await f.client.health()).online,true);
 const request=payload(),reply=await f.client.chat(request);
 assert.equal(reply.requestId,request.requestId);assert.equal(reply.digest,digest);
 await assert.rejects(f.client.chat(payload({profile:'unknown'})),/PROFILE_UNKNOWN/);
});

test('profiles accept the 90-second cap and reject longer or invalid deadlines at both depths',()=>{
 assert.equal(parseProfiles({profiles:[profile({timeoutMs:{brief:90000,expanded:90000}})]}).profiles.size,1);
 assert.equal(GATEWAY_LIMITS.chatMs,90000);
 for(const depth of ['brief','expanded'])for(const value of [90001,600000,0,-1,1.5,Infinity,'90000'])
  assert.throws(()=>parseProfiles({profiles:[profile({timeoutMs:{brief:500,expanded:500,[depth]:value}})]}),/PROFILE_INVALID/);
});

test('queue waiting consumes the same deadline and expired work never reaches Ollama',async()=>{
 const f=fixture({hold:true,profileOverrides:{timeoutMs:{brief:40,expanded:1000}}}),abort=new AbortController();
 const first=f.client.chat(payload({depth:'expanded'}),{signal:abort.signal});
 const cancelled=assert.rejects(first,/MODEL_CANCELLED/);
 while(!f.runtime.generations.length)await tick();
 try{
  await assert.rejects(f.client.chat(payload()),/MODEL_TIMEOUT/);
  assert.equal(f.gateway.admission.queued,0);assert.equal(f.gateway.admission.active,1);
  assert.equal(f.runtime.generations.length,1);
 }finally{abort.abort();await cancelled;await tick();}
 assert.equal(f.gateway.admission.active,0);assert.equal(f.runtime.generations[0].signal.aborted,true);
});

test('fresh identity inspection is inside the deadline and releases its admission slot',async()=>{
 let release;const inspectHold=new Promise(resolve=>{release=resolve;});
 const f=fixture({inspectHold,profileOverrides:{timeoutMs:{brief:30,expanded:30}}});
 try{
  await assert.rejects(f.client.chat(payload()),/MODEL_TIMEOUT/);
  assert.equal(f.gateway.admission.active,0);assert.equal(f.runtime.generations.length,0);
 }finally{release();await tick();}
});

test('cached health cannot admit a substituted model or an Ollama outage',async()=>{
 for(const mode of ['digest','remote','missing','offline']){
  const f=fixture();assert.equal((await f.client.health()).profiles[0].ready,true);
  if(mode==='digest')f.runtime.tags[0].digest=other;
  if(mode==='remote')f.runtime.tags[0].remote_host='https://synthetic.invalid';
  if(mode==='missing')f.runtime.tags=[];
  if(mode==='offline')f.runtime.down=true;
  await assert.rejects(f.client.chat(payload()),mode==='offline'?/MODEL_UNAVAILABLE/:/PROFILE_NOT_READY/);
  assert.equal(f.runtime.generations.length,0);
 }
});

test('a model changed while a request waits is rechecked after admission',async()=>{
 const f=fixture({hold:true});
 const first=f.client.chat(payload());
 while(!f.runtime.generations.length)await tick();
 const second=assert.rejects(f.client.chat(payload()),/PROFILE_NOT_READY/);
 while(!f.gateway.admission.queued)await tick();
 f.runtime.tags[0].digest=other;f.runtime.generations[0].finish();
 await first;await second;
 assert.equal(f.runtime.generations.length,1);assert.equal(f.gateway.admission.active,0);
});

test('profile reloads preserve active work, queued work, FIFO order and overflow refusal',async()=>{
 const f=fixture({hold:true,queue:2,profileOverrides:{timeoutMs:{brief:5000,expanded:5000}}}),work=[];
 const admission=f.gateway.admission;
 try{
  work.push(f.client.chat(payload({messages:[{role:'user',content:'FIFO 0'}]})));
  await waitFor(()=>f.runtime.generations.length===1);
  work.push(f.client.chat(payload({messages:[{role:'user',content:'FIFO 1'}]})));
  await waitFor(()=>admission.queued===1);
  work.push(f.client.chat(payload({messages:[{role:'user',content:'FIFO 2'}]})));
  await waitFor(()=>admission.queued===2);
  for(let i=0;i<2;i++)reloadProfiles(f.gateway,{maxQueue:2});
  assert.equal(f.gateway.admission,admission);
  const health=await f.client.health();
  assert.equal(health.active,1);assert.equal(health.queued,2);
  await assert.rejects(f.client.chat(payload()),/GATEWAY_BUSY/);
  assert.equal(f.runtime.generations.length,1);
  for(let i=0;i<3;i++){
   assert.equal(f.runtime.generations[i].messages[0].content,'FIFO '+i);
   f.runtime.generations[i].finish();await work[i];
   if(i<2)await waitFor(()=>f.runtime.generations.length===i+2);
   assert.equal(admission.active,i<2?1:0);
   assert.equal(admission.queued,Math.max(0,1-i));
  }
 }finally{f.gateway.abortAll();await Promise.allSettled(work);}
});

test('reload limit changes drain existing waiters within the new concurrency and queue bounds',async()=>{
 const f=fixture();
 reloadProfiles(f.gateway,{concurrency:2,maxQueue:2});
 const admission=f.gateway.admission;
 const first=await admission.enter(),second=await admission.enter();
 const granted=[],third=admission.enter().then(release=>{granted.push(3);return release;}),fourth=admission.enter().then(release=>{granted.push(4);return release;});
 reloadProfiles(f.gateway,{concurrency:1,maxQueue:0});
 assert.equal(admission.active,2);assert.equal(admission.queued,2);
 await assert.rejects(admission.enter(),/GATEWAY_BUSY/);
 first();first();await tick();
 assert.equal(admission.active,1);assert.equal(admission.queued,2);assert.deepEqual(granted,[]);
 second();const releaseThird=await third;
 assert.equal(admission.active,1);assert.equal(admission.queued,1);assert.deepEqual(granted,[3]);
 reloadProfiles(f.gateway,{concurrency:2,maxQueue:1});
 const releaseFourth=await fourth;
 assert.deepEqual(granted,[3,4]);assert.equal(admission.active,2);assert.equal(admission.queued,0);
 const cancelled=new AbortController(),fifth=assert.rejects(admission.enter(cancelled.signal),/REQUEST_CANCELLED/);
 await assert.rejects(admission.enter(),/GATEWAY_BUSY/);
 reloadProfiles(f.gateway,{concurrency:1,maxQueue:0});
 cancelled.abort();await fifth;
 assert.equal(admission.queued,0);
 releaseThird();releaseThird();releaseFourth();releaseFourth();
 assert.equal(admission.active,0);
 const last=await admission.enter();last();assert.equal(admission.active,0);
});

test('a waiter cancelled after profile reload frees its queue place without leaking a slot',async()=>{
 const f=fixture({hold:true,profileOverrides:{timeoutMs:{brief:5000,expanded:5000}}}),abort=new AbortController(),work=[];
 try{
  work.push(f.client.chat(payload()));
  await waitFor(()=>f.runtime.generations.length===1);
  const cancelled=assert.rejects(f.client.chat(payload(),{signal:abort.signal}),/MODEL_CANCELLED/);
  await waitFor(()=>f.gateway.admission.queued===1);
  reloadProfiles(f.gateway);
  abort.abort();await cancelled;
  await waitFor(()=>f.gateway.admission.queued===0);
  assert.equal(f.gateway.admission.active,1);
  work.push(f.client.chat(payload()));
  await waitFor(()=>f.gateway.admission.queued===1);
  f.runtime.generations[0].finish();await work[0];
  await waitFor(()=>f.runtime.generations.length===2);
  f.runtime.generations[1].finish();await work[1];
  assert.equal(f.gateway.admission.active,0);assert.equal(f.gateway.admission.queued,0);
 }finally{abort.abort();f.gateway.abortAll();await Promise.allSettled(work);}
});

test('queued work keeps its validated profile and matching inspector across a reload',async()=>{
 const f=fixture({hold:true,profileOverrides:{timeoutMs:{brief:5000,expanded:5000}}}),work=[];
 try{
  work.push(f.client.chat(payload()));
  await waitFor(()=>f.runtime.generations.length===1);
  work.push(f.client.chat(payload()));
  await waitFor(()=>f.gateway.admission.queued===1);
  reloadProfiles(f.gateway,{profiles:[profile({digest:'sha256:'+other,timeoutMs:{brief:5000,expanded:5000}})]});
  f.runtime.generations[0].finish();await work[0];
  await waitFor(()=>f.runtime.generations.length===2);
  f.runtime.generations[1].finish();
  assert.equal((await work[1]).digest,digest);
  // New requests inspect the newly pinned digest, while accepted work above
  // completes against the original pin. The installed model is still original.
  await assert.rejects(f.client.chat(payload()),/PROFILE_NOT_READY/);
  assert.equal(f.runtime.generations.length,2);assert.equal(f.gateway.admission.active,0);
 }finally{f.gateway.abortAll();await Promise.allSettled(work);}
});

test('health keeps profile metadata paired with its inspection when reload crosses pending I/O',async()=>{
 const f=fixture();let release;
 f.runtime.versionHolds.push(new Promise(resolve=>{release=resolve;}));
 const pending=f.client.health();
 try{
  await waitFor(()=>f.runtime.tagReads===1);
  reloadProfiles(f.gateway,{profiles:[profile({digest:'sha256:'+other})]});
  release();
  const before=await pending;
  assert.equal(before.profiles[0].digest,digest,'pending health describes the profile it inspected');
  assert.equal(before.profiles[0].ready,true);
  const after=await f.client.health();
  assert.equal(after.profiles[0].digest,'sha256:'+other);
  assert.equal(after.profiles[0].ready,false,'new health cannot approve the new pin using old readiness');
  assert.equal(after.profiles[0].reason,'PROFILE_DIGEST_MISMATCH');
  assert.equal(f.gateway.admission.active,0);assert.equal(f.gateway.admission.queued,0);
 }finally{release();await pending;}
});

test('admission cannot reuse older in-flight tags or let their late result overwrite its cache',async()=>{
 const f=fixture();let release;
 f.runtime.versionHolds.push(new Promise(resolve=>{release=resolve;}));
 const oldHealth=f.client.health();
 while(f.runtime.tagReads===0)await tick();
 f.runtime.tags[0].digest=other;
 try{
  // The old inspection has approved tags but is waiting for version. Admission
  // must inspect independently and refuse before that old request completes.
  await assert.rejects(f.client.chat(payload()),/PROFILE_NOT_READY/);
  assert.equal(f.runtime.tagReads,2);assert.equal(f.runtime.generations.length,0);
 }finally{release();await oldHealth;}
 assert.equal((await f.client.health()).profiles[0].ready,false,'late old health must not replace newer cached identity');
});

test('a mismatched runtime response model is refused',async()=>{
 const f=fixture();f.runtime.reportedModel='unapproved:latest';
 await assert.rejects(f.client.chat(payload()),/PROFILE_NOT_READY/);
});

test('Ollama failure after readiness immediately makes the adapter unavailable',async()=>{
 const f=fixture();const model=new HomeInferenceModel({client:f.client,profile:'test-chat',digest,pollMs:60000,diagnostic:()=>{}});
 try{
  await model.refresh();assert.equal(model.ready,true);
  f.runtime.down=true;
  await assert.rejects(model.discuss('Synthetic only'),/MODEL_UNAVAILABLE/);
  assert.equal(model.ready,false);assert.equal(model.online,false);
  await assert.rejects(model.discuss('No fallback'),/MODEL_UNAVAILABLE/);
  assert.equal(f.runtime.generations.length,0);
 }finally{model.stop();}
});

test('a reachable gateway holding a substituted runtime model reports unavailable',async()=>{
 const f=fixture();f.runtime.tags[0].digest=other;
 const model=new HomeInferenceModel({client:f.client,profile:'test-chat',digest,pollMs:60000,diagnostic:()=>{}});
 try{await model.refresh();assert.equal(model.ready,false);assert.equal(model.online,false);}
 finally{model.stop();}
});

test('adapter binds each successful reply to its request, profile, digest and model',async()=>{
 const f=fixture();const model=new HomeInferenceModel({client:f.client,profile:'test-chat',digest,pollMs:60000,diagnostic:()=>{}});
 try{
  for(const changed of [{requestId:randomUUID()},{profile:'other'},{digest:'sha256:'+other},{model:'other:latest'}]){
   await model.refresh();assert.equal(model.ready,true);
   model.client={...f.client,chat:async request=>({...request,model:'qwen3:8b',digest,text:'Synthetic',finishReason:'stop',...changed})};
   await assert.rejects(model.discuss('Synthetic'),/MODEL_UNAVAILABLE/);assert.equal(model.ready,false);
  }
 }finally{model.stop();}
});

test('transport probe rejects an unsigned successful gateway response',async()=>{
 const f=fixture();
 const result=await probe({env:{KFM_HOME_INFERENCE_URL:'https://synthetic.invalid',KFM_HOME_INFERENCE_KEY_ID:'test',KFM_HOME_INFERENCE_SECRET:secret,KFM_HOME_INFERENCE_PROFILE:'test-chat',KFM_HOME_INFERENCE_DIGEST:digest},runs:1,concurrency:1,fetchImpl:async(url,init)=>{
  const response=await f.wire(url,init);response.headers.delete(RESPONSE_SIGNATURE_HEADER);return response;
 }});
 assert.equal(result.summary.passed,false);
 assert.equal(result.checks.find(item=>item.name==='health_response_authenticated').result,'FAIL');
 assert.equal(f.runtime.generations.length,0);
});

test('transport probe completes signed health, refusal and synthetic chat checks',async()=>{
 const f=fixture();
 const result=await probe({env:{KFM_HOME_INFERENCE_URL:'https://synthetic.invalid',KFM_HOME_INFERENCE_KEY_ID:'test',KFM_HOME_INFERENCE_SECRET:secret,KFM_HOME_INFERENCE_PROFILE:'test-chat',KFM_HOME_INFERENCE_DIGEST:digest},runs:1,concurrency:2,fetchImpl:f.wire});
 assert.deepEqual(result.checks.filter(item=>item.result!=='PASS'),[]);
 assert.equal(result.summary.passed,true);assert.equal(result.samples.length,3);
 assert.doesNotMatch(JSON.stringify(result),new RegExp(secret));
});
