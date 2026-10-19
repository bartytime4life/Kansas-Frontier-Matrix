import test from 'node:test';
import assert from 'node:assert/strict';
import {createServer} from 'node:http';
import {once} from 'node:events';
import {createGateway,parseGatewayConfig,runOllamaChat,stripReasoning} from '../scripts/home-inference/home-inference-gateway.mjs';
import {HOME_AI_HEADERS,HOME_AI_PATHS,createNonceCache,decodeSecret,signRequest,validDiscussRequest,verifyReply,verifyRequest} from '../scripts/home-inference/home-ai-contract.mjs';
import {HomeAiModel,homeAiConfig} from '../server/home-ai-model.mjs';
import {selectAiModel,createPublicAiHandler} from '../server/public-ai-handler.mjs';
import {CONTINUE_REPLY} from '../server/hosted-ai-prompt.mjs';

const secret='k'.repeat(43),digest='sha256:'+'d'.repeat(64),model='synthetic-model:1b';
const profile={id:'kfm-general-v1',model,digest,think:false,options:{num_ctx:4096,temperature:0.2},brief:{tokens:64,milliseconds:5000},expanded:{tokens:128,milliseconds:5000}};
const rawConfig={keys:{'kfm-test':secret},profiles:[profile]};
const env={KFM_HOME_AI_URL:'https://inference.example.test',KFM_HOME_AI_KEY_ID:'kfm-test',KFM_HOME_AI_SECRET:secret,KFM_HOME_AI_PROFILE:'kfm-general-v1',KFM_HOME_AI_MODEL_DIGEST:digest};
const messages=[{role:'system',content:'Synthetic system.'},{role:'user',content:'What color is the sample marker?'}];

// A stand-in for local Ollama: identity endpoints plus a streamed /api/chat.
function fakeOllama({chunks=[{message:{content:'Blue.'}},{done:true,done_reason:'stop',prompt_eval_count:9,eval_count:2}],installedDigest='d'.repeat(64),hang=false}={}){
 const seen=[];
 const fetchImpl=async(url,init={})=>{
  const path=new URL(url).pathname;seen.push({path,body:init.body?JSON.parse(init.body):null});
  if(path==='/api/version')return Response.json({version:'0.12.0'});
  if(path==='/api/tags')return Response.json({models:[{name:model,digest:installedDigest}]});
  if(path==='/api/ps')return Response.json({models:[]});
  if(path==='/api/chat'){
   const stream=new ReadableStream({async start(controller){
    for(const chunk of chunks)controller.enqueue(new TextEncoder().encode(JSON.stringify(chunk)+'\n'));
    if(hang)await new Promise(resolve=>init.signal.addEventListener('abort',resolve,{once:true}));
    controller.close();
   }});
   return new Response(stream,{status:200});
  }
  return new Response('not found',{status:404});
 };
 return {fetchImpl,seen};
}

async function gatewayServer(options={},config=parseGatewayConfig(rawConfig)){
 const ollama=fakeOllama(options);const logs=[];
 const {handler}=createGateway({config,fetchImpl:ollama.fetchImpl,log:line=>logs.push(line)});
 const server=createServer(handler);server.listen(0,'127.0.0.1');await once(server,'listening');
 const origin='http://127.0.0.1:'+server.address().port;
 return {origin,logs,ollama,close:()=>new Promise(resolve=>server.close(resolve))};
}
// The provider requires HTTPS; tests rewrite only the scheme to reach the loopback gateway.
const toGateway=origin=>(url,init)=>fetch(url.replace('https://inference.example.test',origin),init);

test('gateway config admits loopback, pinned profiles and bounded run time only',()=>{
 assert.equal(parseGatewayConfig(rawConfig).listen.host,'127.0.0.1');
 for(const bad of [
  {...rawConfig,listen:{host:'0.0.0.0',port:8787}},
  {...rawConfig,ollama:'http://192.168.1.20:11434'},
  {...rawConfig,keys:{'kfm-test':'short'}},
  {...rawConfig,keys:{}},
  {...rawConfig,profiles:[{...profile,digest:'latest'}]},
  {...rawConfig,profiles:[{...profile,options:{num_ctx:4096,tools:1}}]},
  {...rawConfig,profiles:[{...profile,expanded:{tokens:128,milliseconds:300000}}]},
  {...rawConfig,profiles:[{...profile,think:'no'}]},
 ])assert.throws(()=>parseGatewayConfig(bad),/CONFIG_/);
});

test('signed requests verify once, within the clock window, with the right key',()=>{
 const keys=new Map([['kfm-test',decodeSecret(secret)]]);let now=1700000000000;
 const nonces=createNonceCache({clock:()=>now});
 const signed=signRequest({keyId:'kfm-test',secret:decodeSecret(secret),method:'POST',path:'/v1/discuss',body:'{}',clock:()=>now});
 const get=headers=>name=>headers[name];
 assert.equal(verifyRequest({get:get(signed.headers),method:'POST',path:'/v1/discuss',body:'{}',keys,nonces,clock:()=>now}),'kfm-test');
 assert.throws(()=>verifyRequest({get:get(signed.headers),method:'POST',path:'/v1/discuss',body:'{}',keys,nonces,clock:()=>now}),/GATEWAY_UNAUTHORIZED/,'replay');
 const second=signRequest({keyId:'kfm-test',secret:decodeSecret(secret),method:'POST',path:'/v1/discuss',body:'{}',clock:()=>now});
 assert.throws(()=>verifyRequest({get:get(second.headers),method:'POST',path:'/v1/discuss',body:'{"x":1}',keys,nonces,clock:()=>now}),/GATEWAY_UNAUTHORIZED/,'body changed');
 assert.throws(()=>verifyRequest({get:get(second.headers),method:'POST',path:'/v1/health',body:'{}',keys,nonces,clock:()=>now}),/GATEWAY_UNAUTHORIZED/,'path changed');
 now+=61000;
 assert.throws(()=>verifyRequest({get:get(second.headers),method:'POST',path:'/v1/discuss',body:'{}',keys,nonces,clock:()=>now}),/GATEWAY_UNAUTHORIZED/,'expired');
 const other=signRequest({keyId:'kfm-test',secret:Buffer.alloc(32,1),method:'GET',path:'/v1/health',clock:()=>now});
 assert.throws(()=>verifyRequest({get:get(other.headers),method:'GET',path:'/v1/health',keys,nonces,clock:()=>now}),/GATEWAY_UNAUTHORIZED/,'wrong secret');
});

test('discuss contract refuses tools, model names, images and malformed turns',()=>{
 assert.equal(validDiscussRequest({profile:'kfm-general-v1',depth:'brief',messages}),true);
 assert.equal(validDiscussRequest({profile:'kfm-general-v1',depth:'brief',messages,tools:[]}),false);
 assert.equal(validDiscussRequest({profile:'kfm-general-v1',depth:'brief',messages,model:'other'}),false);
 assert.equal(validDiscussRequest({profile:'kfm-general-v1',depth:'unlimited',messages}),false);
 assert.equal(validDiscussRequest({profile:'kfm-general-v1',depth:'brief',messages:[messages[0],{...messages[1],images:['x']}]}),false);
 assert.equal(validDiscussRequest({profile:'kfm-general-v1',depth:'brief',messages:[messages[1]]}),false);
 assert.equal(validDiscussRequest({profile:'kfm-general-v1',depth:'brief',messages:[messages[0],{role:'assistant',content:'x'}]}),false);
 assert.equal(validDiscussRequest({profile:'kfm-general-v1',depth:'brief',messages:[messages[0],{role:'user',content:'bad\u0007'}]}),false);
});

test('gateway denies unauthenticated, unknown routes and raw Ollama paths',async()=>{
 const g=await gatewayServer();
 try{
  for(const path of ['/api/chat','/api/pull','/api/tags','/v1/health?x=1','/']){
   const response=await fetch(g.origin+path);assert.equal(response.status,404,path);
  }
  const unsigned=await fetch(g.origin+HOME_AI_PATHS.health);
  assert.equal(unsigned.status,401);assert.equal(unsigned.headers.get(HOME_AI_HEADERS.reply),null);
  const body=JSON.stringify({profile:'kfm-general-v1',depth:'brief',messages});
  const forged=signRequest({keyId:'kfm-test',secret:Buffer.alloc(32,7),method:'POST',path:HOME_AI_PATHS.discuss,body});
  assert.equal((await fetch(g.origin+HOME_AI_PATHS.discuss,{method:'POST',headers:forged.headers,body})).status,401);
  assert.equal(g.ollama.seen.filter(x=>x.path==='/api/chat').length,0);
 }finally{await g.close();}
});

test('gateway runs one pinned profile, signs the reply and logs no text',async()=>{
 const g=await gatewayServer();
 try{
  const body=JSON.stringify({profile:'kfm-general-v1',depth:'brief',messages});
  const signed=signRequest({keyId:'kfm-test',secret:decodeSecret(secret),method:'POST',path:HOME_AI_PATHS.discuss,body});
  const response=await fetch(g.origin+HOME_AI_PATHS.discuss,{method:'POST',headers:signed.headers,body});
  const text=await response.text();
  assert.equal(response.status,200);
  assert.ok(verifyReply(decodeSecret(secret),signed.nonce,200,text,response.headers.get(HOME_AI_HEADERS.reply)));
  const value=JSON.parse(text);assert.equal(value.text,'Blue.');assert.equal(value.finishReason,'stop');assert.equal(value.digest,digest);
  const chat=g.ollama.seen.find(x=>x.path==='/api/chat').body;
  assert.equal(chat.model,model);assert.equal(chat.options.num_ctx,4096);assert.equal(chat.options.num_predict,64);assert.equal(chat.think,false);
  assert.equal(chat.tools,undefined);assert.equal(chat.format,undefined);
  assert.ok(g.logs.length>0);assert.ok(g.logs.every(line=>!/sample marker|Blue|kkkk/.test(line)));
 }finally{await g.close();}
});

test('gateway refuses a model whose installed digest no longer matches the profile',async()=>{
 const g=await gatewayServer({installedDigest:'e'.repeat(64)});
 try{
  const body=JSON.stringify({profile:'kfm-general-v1',depth:'brief',messages});
  const signed=signRequest({keyId:'kfm-test',secret:decodeSecret(secret),method:'POST',path:HOME_AI_PATHS.discuss,body});
  const response=await fetch(g.origin+HOME_AI_PATHS.discuss,{method:'POST',headers:signed.headers,body});
  assert.equal(response.status,503);assert.equal((await response.json()).reasonCode,'MODEL_IDENTITY');
  assert.equal(g.ollama.seen.filter(x=>x.path==='/api/chat').length,0);
 }finally{await g.close();}
});

test('a time limit returns the bounded partial reply and stops generation',async()=>{
 const {fetchImpl,seen}=fakeOllama({chunks:[{message:{content:'<think>hidden</think>Partial '}},{message:{content:'reply'}}],hang:true});
 const config=parseGatewayConfig({...rawConfig,profiles:[{...profile,brief:{tokens:64,milliseconds:50}}]});
 const result=await runOllamaChat({ollama:config.ollama,profile:config.profiles.get('kfm-general-v1'),depth:'brief',messages,signal:new AbortController().signal,fetchImpl});
 assert.equal(result.finishReason,'time_limit');assert.equal(result.text,'Partial reply');assert.equal(seen.length,1);
 assert.equal(stripReasoning('<think>unfinished'),'');
});

test('provider config fails closed unless complete, exact and HTTPS',()=>{
 assert.equal(homeAiConfig(env).origin,'https://inference.example.test');
 for(const change of [{KFM_HOME_AI_URL:'http://inference.example.test'},{KFM_HOME_AI_URL:'https://inference.example.test/api'},{KFM_HOME_AI_URL:'https://user:pw@inference.example.test'},{KFM_HOME_AI_URL:'https://inference.example.test/?x=1'},
  {KFM_HOME_AI_SECRET:'short'},{KFM_HOME_AI_MODEL_DIGEST:undefined},{KFM_HOME_AI_PROFILE:'Bad Profile'},{KFM_HOME_AI_ACCESS_CLIENT_ID:'abcdefgh.access'},{KFM_HOME_AI_DISPLAY_NAME:'<script>'}])
  assert.equal(homeAiConfig({...env,...change}),null,JSON.stringify(change));
});

test('provider selection is exclusive and never falls back to another model',()=>{
 assert.deepEqual(selectAiModel({KFM_AI_PROVIDER:'home-ollama'}),{reasonCode:'HOME_AI_NOT_CONFIGURED'});
 assert.deepEqual(selectAiModel({KFM_AI_PROVIDER:'paid-api'}),{reasonCode:'AI_PROVIDER_UNKNOWN'});
});

test('home provider becomes ready only for the pinned digest and runs a discussion end to end',async()=>{
 const g=await gatewayServer();const diagnostics=[];
 const provider=new HomeAiModel({config:homeAiConfig(env),fetchImpl:toGateway(g.origin),healthMs:3600000,diagnostic:code=>diagnostics.push(code)});
 try{
  await provider.refresh();
  assert.equal(provider.ready,true);assert.equal(provider.label,model+' · home PC (Ollama)');
  const reply=await provider.discuss('What color is the sample marker?',{depth:'brief',history:[{question:'Earlier question?',reply:'Earlier reply.'}]});
  assert.deepEqual(reply,{text:'Blue.',contextTrimmed:false,outputLimited:false});
  const sent=g.ollama.seen.find(x=>x.path==='/api/chat').body.messages;
  assert.deepEqual(sent.map(m=>m.role),['system','user','assistant','user']);
  await assert.rejects(provider.select('q',['fact']),/MODEL_UNAVAILABLE/);
  const continued=await provider.discuss(CONTINUE_REPLY,{history:[{question:'Earlier question?',reply:'An unfinished'}]});
  assert.equal(continued.text,' Blue.');
  const {think,...thinkless}=profile;assert.equal(think,false);
  assert.equal(parseGatewayConfig({...rawConfig,profiles:[thinkless]}).profiles.get('kfm-general-v1').think,undefined);
  assert.deepEqual(diagnostics,['HOME_AI_READY']);
 }finally{provider.stop();await g.close();}
 const other=await gatewayServer();
 const pinned=new HomeAiModel({config:homeAiConfig({...env,KFM_HOME_AI_MODEL_DIGEST:'sha256:'+'f'.repeat(64)}),fetchImpl:toGateway(other.origin),healthMs:3600000,diagnostic:()=>{}});
 try{await pinned.refresh();assert.equal(pinned.ready,false);assert.equal(pinned.online,false);assert.equal(pinned.reason,'HOME_AI_MODEL_IDENTITY');}finally{pinned.stop();await other.close();}
});

test('home provider rejects unsigned or forged replies and reports unavailable',async()=>{
 const edge=async()=>new Response('<html>Bad gateway</html>',{status:502});
 const down=new HomeAiModel({config:homeAiConfig(env),fetchImpl:edge,healthMs:3600000,diagnostic:()=>{}});
 await down.refresh();assert.equal(down.online,false);assert.equal(down.reason,'HOME_AI_UNREACHABLE');down.stop();
 const denied=new HomeAiModel({config:homeAiConfig(env),fetchImpl:async()=>new Response('denied',{status:403}),healthMs:3600000,diagnostic:()=>{}});
 await denied.refresh();assert.equal(denied.reason,'HOME_AI_ACCESS_DENIED');denied.stop();
 const forged=async()=>new Response(JSON.stringify({contract:'kfm-home-inference-v1',ollamaReachable:true,profiles:[]}),{status:200,headers:{[HOME_AI_HEADERS.reply]:'0'.repeat(64)}});
 const spoof=new HomeAiModel({config:homeAiConfig(env),fetchImpl:forged,healthMs:3600000,diagnostic:()=>{}});
 await spoof.refresh();assert.equal(spoof.ready,false);assert.equal(spoof.reason,'HOME_AI_REPLY_UNVERIFIED');spoof.stop();
});

test('home provider goes stale without health and trims history before the question',async()=>{
 const g=await gatewayServer({},parseGatewayConfig({...rawConfig,profiles:[{...profile,maxInputBytes:2048}]}));
 // Signatures use this clock too, so it starts at real time to pass the gateway's skew check.
 let now=Date.now();
 const provider=new HomeAiModel({config:homeAiConfig(env),fetchImpl:toGateway(g.origin),clock:()=>now,healthMs:3600000,diagnostic:()=>{}});
 try{
  await provider.refresh();assert.equal(provider.ready,true);
  const history=[{question:'Old '+'q'.repeat(900),reply:'r'.repeat(900)},{question:'Recent question?',reply:'Recent reply.'}];
  const reply=await provider.discuss('Current question?',{history},undefined);
  assert.equal(reply.contextTrimmed,true);
  const sent=g.ollama.seen.find(x=>x.path==='/api/chat').body.messages;
  assert.equal(sent.at(-1).content,'Current question?');assert.equal(sent.length,4);
  await assert.rejects(provider.discuss('x'.repeat(2100),{}),/MODEL_CONTEXT_LIMIT/);
  now+=76000;assert.equal(provider.ready,false);
  await assert.rejects(provider.discuss('Current question?',{}),/MODEL_UNAVAILABLE/);
 }finally{provider.stop();await g.close();}
});

test('public chat keeps guest controls and reports the home provider identity',async()=>{
 const g=await gatewayServer();
 const origin='https://kansasfrontiermatrix.com';
 const provider=new HomeAiModel({config:homeAiConfig({...env,KFM_HOME_AI_DISPLAY_NAME:'Synthetic 1B · KFM home PC'}),fetchImpl:toGateway(g.origin),healthMs:3600000,diagnostic:()=>{}});
 try{
  await provider.refresh();
  const handler=createPublicAiHandler({origin,resolveEvidence:async()=>null,model:provider});
  const status=await(await handler(new Request(origin+'/api/ai/status'))).json();
  assert.equal(status.provider,'home-ollama');assert.equal(status.displayName,'Synthetic 1B · KFM home PC');assert.equal(status.requiresLogin,false);
  assert.doesNotMatch(JSON.stringify(status),/inference\.example|127\.0\.0\.1|kkkk|kfm-test/);
  const submit=await handler(new Request(origin+'/api/ai/jobs',{method:'POST',headers:{'Content-Type':'application/json',Origin:origin},body:JSON.stringify({question:'What color is the sample marker?',term:'marker',mode:'explore'})}));
  assert.equal(submit.status,202);const {id}=await submit.json();const cookie=submit.headers.get('set-cookie').split(';')[0];
  let result;for(let i=0;i<50&&!['completed','expired'].includes(result?.state);i++){await new Promise(resolve=>setTimeout(resolve,10));result=await(await handler(new Request(origin+'/api/ai/jobs/'+id,{headers:{Cookie:cookie}}))).json();}
  assert.equal(result.result.reasonCode,'UNVERIFIED_AI_DISCUSSION');assert.equal(result.result.answer,null);assert.equal(result.result.interpretation,'Blue.');
 }finally{provider.stop();await g.close();}
});
