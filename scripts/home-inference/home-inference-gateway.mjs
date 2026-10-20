#!/usr/bin/env node
// KFM home inference gateway. Runs on the dedicated inference PC, listens on
// loopback only, and is reached through an authenticated tunnel. It accepts the
// small signed contract in home-ai-contract.mjs, runs one approved profile
// against local Ollama, and returns a bounded, signed reply. It never exposes
// Ollama's own API, model management, tools, images or arbitrary URLs.
//
//   node home-inference-gateway.mjs serve   run the service (systemd does this)
//   node home-inference-gateway.mjs check   validate config and local Ollama identity
//   node home-inference-gateway.mjs keygen <key-id>   print a new key entry
//   node home-inference-gateway.mjs smoke <https-origin>   signed synthetic request
import {createServer} from 'node:http';
import {readFileSync,realpathSync,statSync} from 'node:fs';
import {join} from 'node:path';
import {performance} from 'node:perf_hooks';
import {fileURLToPath} from 'node:url';
import {
 HOME_AI_CONTRACT,HOME_AI_HEADERS,HOME_AI_MAX_REQUEST_BYTES,HOME_AI_MAX_RESPONSE_BYTES,HOME_AI_PATHS,
 MODEL_DIGEST,MODEL_TAG,PROFILE_ID,createNonceCache,decodeSecret,messageBytes,newSecret,signReply,signRequest,
 validDiscussRequest,validKeyId,verifyReply,verifyRequest,
} from './home-ai-contract.mjs';

const LOOPBACK=new Set(['127.0.0.1','::1']);
export const MAX_RUN_MS=90000;
const fail=code=>{throw Object.assign(new Error(code),{code});};
const positive=(value,max)=>Number.isInteger(value)&&value>0&&value<=max;
// Only these Ollama options may be pinned by a profile. num_predict comes from depth.
const OPTION_KEYS=new Set(['num_ctx','temperature','top_k','top_p','min_p','repeat_penalty','repeat_last_n','presence_penalty','seed']);

// Config is owner-written JSON. Under systemd it arrives through LoadCredential,
// so the service account never needs read access to /etc.
export function loadGatewayConfig(path=process.env.KFM_GATEWAY_CONFIG??(process.env.CREDENTIALS_DIRECTORY?join(process.env.CREDENTIALS_DIRECTORY,'gateway.json'):'/etc/kfm-inference/gateway.json')){
 // The file holds HMAC secrets: refuse it when other local users could read it.
 if(statSync(path).mode&0o007)fail('CONFIG_PERMISSIONS');
 return parseGatewayConfig(JSON.parse(readFileSync(path,'utf8')));
}

export function parseGatewayConfig(raw){
 if(!raw||typeof raw!=='object')fail('CONFIG_INVALID');
 const listen={host:raw.listen?.host??'127.0.0.1',port:raw.listen?.port??8787};
 // The tunnel connector runs on this machine; nothing else should reach the gateway.
 if(!LOOPBACK.has(listen.host)||!positive(listen.port,65535))fail('CONFIG_LISTEN');
 const ollama=new URL(raw.ollama??'http://127.0.0.1:11434');
 if(ollama.protocol!=='http:'||!LOOPBACK.has(ollama.hostname.replace(/^\[|\]$/g,''))||ollama.pathname!=='/'||ollama.search||ollama.username)fail('CONFIG_OLLAMA');
 const keys=new Map();
 for(const [id,secret]of Object.entries(raw.keys??{})){const value=decodeSecret(secret);if(!validKeyId(id)||!value)fail('CONFIG_KEYS');keys.set(id,value);}
 if(!keys.size||keys.size>4)fail('CONFIG_KEYS');
 const profiles=new Map();
 for(const p of raw.profiles??[]){
  if(!p||!PROFILE_ID.test(p.id??'')||!MODEL_TAG.test(p.model??'')||!MODEL_DIGEST.test(p.digest??'')||profiles.has(p.id))fail('CONFIG_PROFILE');
  const options=p.options??{};
  if(Object.keys(options).some(key=>!OPTION_KEYS.has(key)||typeof options[key]!=='number')||!positive(options.num_ctx,131072))fail('CONFIG_PROFILE');
  // Set think only for thinking-capable models; Ollama may reject it for others.
  if(p.think!==undefined&&typeof p.think!=='boolean')fail('CONFIG_PROFILE');
  // Cloudflare answers 524 when a proxied origin takes 100 s to respond, so a run
  // returns its bounded partial reply before then; visitors can choose Continue.
  for(const depth of ['brief','expanded'])if(!positive(p[depth]?.tokens,4096)||!positive(p[depth]?.milliseconds,MAX_RUN_MS))fail('CONFIG_PROFILE');
  // Leave room for the reply; the server trims history to this byte budget.
  const maxInputBytes=p.maxInputBytes??Math.max(2048,(options.num_ctx-p.expanded.tokens-256)*2);
  if(!positive(maxInputBytes,262144))fail('CONFIG_PROFILE');
  profiles.set(p.id,Object.freeze({id:p.id,model:p.model,digest:p.digest,options:Object.freeze({...options}),think:p.think,keepAlive:typeof p.keepAlive==='string'&&/^\d{1,4}[smh]$/.test(p.keepAlive)?p.keepAlive:'30m',brief:Object.freeze({...p.brief}),expanded:Object.freeze({...p.expanded}),maxInputBytes}));
 }
 if(!profiles.size||profiles.size>4)fail('CONFIG_PROFILE');
 const admission={concurrency:1,queue:raw.admission?.queue??2};
 if(!Number.isInteger(admission.queue)||admission.queue<0||admission.queue>8)fail('CONFIG_ADMISSION');
 return Object.freeze({listen,ollama:ollama.origin,keys,profiles,admission});
}

// One run at a time (Ollama is pinned to one parallel slot as well), a short
// waiting line, and immediate refusal beyond it.
function createAdmission({concurrency,queue}){
 let running=0;const waiting=[];
 const next=()=>{while(running<concurrency&&waiting.length){const item=waiting.shift();if(!item.signal.aborted){running++;item.resolve();}}};
 return {
  get running(){return running;},get waiting(){return waiting.length;},
  async enter(signal){
   if(running<concurrency){running++;return;}
   if(waiting.length>=queue)fail('GATEWAY_BUSY');
   await new Promise((resolve,reject)=>{const item={resolve,signal};waiting.push(item);signal.addEventListener('abort',()=>{const i=waiting.indexOf(item);if(i>=0)waiting.splice(i,1);reject(Object.assign(new Error('GATEWAY_CANCELLED'),{code:'GATEWAY_CANCELLED'}));},{once:true});});
  },
  leave(){running--;next();},
 };
}

// Qwen-style models may emit a reasoning block even when asked not to.
export const stripReasoning=value=>value.replace(/<think>[\s\S]*?<\/think>\s*/g,'').replace(/<think>[\s\S]*$/,'');

// Streams NDJSON from Ollama so a time limit can return the bounded partial
// reply. Aborting the fetch closes the connection, which stops generation.
export async function runOllamaChat({ollama,profile,depth,messages,signal,fetchImpl=fetch,budgetMs=MAX_RUN_MS}){
 const tokens=profile[depth].tokens,milliseconds=Math.min(profile[depth].milliseconds,budgetMs);
 const timeLimit=new AbortController(),timer=setTimeout(()=>timeLimit.abort(),milliseconds);
 const began=performance.now();let text='',finishReason='time_limit',done=false,stats={};
 try{
  const response=await fetchImpl(ollama+'/api/chat',{method:'POST',redirect:'error',signal:AbortSignal.any([signal,timeLimit.signal]),headers:{'content-type':'application/json'},
   body:JSON.stringify({model:profile.model,messages,stream:true,...(profile.think===undefined?{}:{think:profile.think}),keep_alive:profile.keepAlive,options:{...profile.options,num_predict:tokens}})});
  if(!response.ok||!response.body)fail(response.status===404?'MODEL_NOT_INSTALLED':'OLLAMA_FAILED');
  const decoder=new TextDecoder();let pending='';
  try{for await(const chunk of response.body){
   pending+=decoder.decode(chunk,{stream:true});
   if(pending.length>65536)fail('OLLAMA_FAILED');
   let line;while((line=pending.indexOf('\n'))>=0){
    const part=JSON.parse(pending.slice(0,line));pending=pending.slice(line+1);
    if(part.error)fail('OLLAMA_FAILED');
    text+=part.message?.content??'';
    if(Buffer.byteLength(text)>HOME_AI_MAX_RESPONSE_BYTES/2){finishReason='length';timeLimit.abort();break;}
    if(part.done){done=true;finishReason=part.done_reason==='stop'?'stop':'length';stats={promptTokens:part.prompt_eval_count??null,outputTokens:part.eval_count??null};}
   }
   if(finishReason!=='time_limit')break;
  }}catch(error){if(!timeLimit.signal.aborted||signal.aborted)throw error;}
  // A stream that ends early without a time or length limit is a failed run, not a short reply.
  if(!done&&finishReason==='time_limit'&&!timeLimit.signal.aborted)fail('OLLAMA_FAILED');
 }catch(error){
  if(signal.aborted)fail('GATEWAY_CANCELLED');
  if(!timeLimit.signal.aborted)throw error.code?error:Object.assign(new Error('OLLAMA_FAILED'),{code:error instanceof SyntaxError?'OLLAMA_FAILED':'OLLAMA_UNREACHABLE'});
 }finally{clearTimeout(timer);}
 return {text:stripReasoning(text).trim(),finishReason,timings:{totalMs:Math.round(performance.now()-began),...stats}};
}

async function ollamaJson(ollama,path,fetchImpl=fetch,init={}){
 const response=await fetchImpl(ollama+path,{redirect:'error',signal:AbortSignal.timeout(5000),...init});
 if(!response.ok)fail('OLLAMA_FAILED');
 return response.json();
}

// The installed model must match the pinned digest; a re-pulled or swapped tag fails closed.
export async function ollamaIdentity(config,fetchImpl=fetch){
 const [version,tags,ps]=await Promise.all([ollamaJson(config.ollama,'/api/version',fetchImpl),ollamaJson(config.ollama,'/api/tags',fetchImpl),ollamaJson(config.ollama,'/api/ps',fetchImpl)]);
 const installed=new Map((tags.models??[]).map(m=>[m.name,'sha256:'+m.digest]));
 const loaded=new Set((ps.models??[]).map(m=>m.name));
 const profiles={};
 for(const profile of config.profiles.values())profiles[profile.id]={model:profile.model,digest:profile.digest,installedDigest:installed.get(profile.model)??null,installed:installed.get(profile.model)===profile.digest,loaded:loaded.has(profile.model)};
 return {ollama:typeof version.version==='string'?version.version.slice(0,32):'unknown',profiles};
}

const readBody=(request,limit)=>new Promise((resolve,reject)=>{
 const chunks=[];let bytes=0;
 const timer=setTimeout(()=>{request.destroy();reject(Object.assign(new Error('BODY_TIMEOUT'),{code:'BODY_TIMEOUT'}));},5000);
 request.on('data',chunk=>{bytes+=chunk.length;if(bytes>limit){clearTimeout(timer);request.destroy();reject(Object.assign(new Error('REQUEST_TOO_LARGE'),{code:'REQUEST_TOO_LARGE'}));}else chunks.push(chunk);});
 request.on('end',()=>{clearTimeout(timer);resolve(Buffer.concat(chunks).toString('utf8'));});
 request.on('error',error=>{clearTimeout(timer);reject(error);});
});

const STATUS={GATEWAY_UNAUTHORIZED:401,ROUTE_NOT_FOUND:404,METHOD_DENIED:405,REQUEST_TOO_LARGE:413,INVALID_REQUEST:400,BODY_TIMEOUT:408,PROFILE_UNKNOWN:400,CONTEXT_LIMIT:413,GATEWAY_BUSY:429,MODEL_IDENTITY:503,MODEL_NOT_INSTALLED:503,OLLAMA_UNREACHABLE:502,OLLAMA_FAILED:502};

export function createGateway({config,fetchImpl=fetch,clock=Date.now,log=line=>console.log(line)}){
 const nonces=createNonceCache({clock}),admission=createAdmission(config.admission);
 // Logs carry fixed codes and timings only: never prompts, replies, headers or keys.
 const record=(event,fields={})=>{try{log('[KFM gateway] '+JSON.stringify({event,...fields}));}catch{}};
 const handler=async(request,response)=>{
  const controller=new AbortController();
  response.on('close',()=>{if(!response.writableFinished)controller.abort();});
  let secret=null,nonce=null;
  const send=(status,value)=>{
   const body=JSON.stringify(value);
   const headers={'content-type':'application/json; charset=utf-8','cache-control':'no-store','x-content-type-options':'nosniff'};
   if(secret&&nonce)headers[HOME_AI_HEADERS.reply]=signReply(secret,nonce,status,body);
   response.writeHead(status,headers);response.end(body);
  };
  const path=new URL(request.url??'/','http://gateway.invalid').pathname;
  try{
   if(request.url!==HOME_AI_PATHS.health&&request.url!==HOME_AI_PATHS.discuss)fail('ROUTE_NOT_FOUND');
   if(!(request.method==='GET'&&path===HOME_AI_PATHS.health)&&!(request.method==='POST'&&path===HOME_AI_PATHS.discuss))fail('METHOD_DENIED');
   const body=request.method==='POST'?await readBody(request,HOME_AI_MAX_REQUEST_BYTES):'';
   const get=name=>{const value=request.headers[name];return typeof value==='string'?value:undefined;};
   const keyId=verifyRequest({get,method:request.method,path,body,keys:config.keys,nonces,clock});
   secret=config.keys.get(keyId);nonce=get(HOME_AI_HEADERS.nonce);
   if(path===HOME_AI_PATHS.health){
    const identity=await ollamaIdentity(config,fetchImpl).catch(()=>null);
    const profiles=[...config.profiles.values()].map(p=>({id:p.id,model:p.model,digest:p.digest,installed:identity?.profiles[p.id]?.installed??false,loaded:identity?.profiles[p.id]?.loaded??false,maxInputBytes:p.maxInputBytes,brief:p.brief,expanded:p.expanded}));
    return send(200,{contract:HOME_AI_CONTRACT,ollamaReachable:Boolean(identity),ollama:identity?.ollama??null,profiles,running:admission.running,waiting:admission.waiting});
   }
   let value;try{value=JSON.parse(body);}catch{fail('INVALID_REQUEST');}
   if(!validDiscussRequest(value))fail('INVALID_REQUEST');
   const profile=config.profiles.get(value.profile);if(!profile)fail('PROFILE_UNKNOWN');
   if(messageBytes(value.messages)>profile.maxInputBytes)fail('CONTEXT_LIMIT');
   const queued=performance.now();
   await admission.enter(controller.signal);
   try{
    const waitMs=Math.round(performance.now()-queued);
    // Waiting counts against the same proxied-response budget as generation.
    const budgetMs=MAX_RUN_MS-waitMs;if(budgetMs<5000)fail('GATEWAY_BUSY');
    // Recheck identity per run: a model re-pulled under the same tag changes its digest.
    const identity=await ollamaIdentity(config,fetchImpl).catch(()=>fail('OLLAMA_UNREACHABLE'));
    if(!identity.profiles[profile.id].installed)fail('MODEL_IDENTITY');
    const result=await runOllamaChat({ollama:config.ollama,profile,depth:value.depth,messages:value.messages,signal:controller.signal,fetchImpl,budgetMs});
    record('discuss',{profile:profile.id,depth:value.depth,finishReason:result.finishReason,waitMs,...result.timings});
    return send(200,{contract:HOME_AI_CONTRACT,profile:profile.id,model:profile.model,digest:profile.digest,text:result.text,finishReason:result.finishReason,timings:{waitMs,...result.timings}});
   }finally{admission.leave();}
  }catch(error){
   const code=STATUS[error.code]?error.code:error.code==='GATEWAY_CANCELLED'?'GATEWAY_CANCELLED':'GATEWAY_FAILED';
   if(code!=='ROUTE_NOT_FOUND')record('refused',{code});
   if(response.headersSent||response.destroyed)return;
   send(STATUS[code]??503,{contract:HOME_AI_CONTRACT,reasonCode:code});
  }
 };
 return {handler,admission};
}

export async function serve(config=loadGatewayConfig()){
 const {handler}=createGateway({config});
 const server=createServer({requestTimeout:120000,headersTimeout:10000,maxHeaderSize:8192},handler);
 server.keepAliveTimeout=65000;
 await new Promise((resolve,reject)=>{server.once('error',reject);server.listen(config.listen.port,config.listen.host,resolve);});
 console.log('[KFM gateway] '+JSON.stringify({event:'listening',host:config.listen.host,port:config.listen.port,profiles:[...config.profiles.keys()]}));
 // Warm the first profile so the first visitor does not pay the full load time.
 const first=config.profiles.values().next().value;
 fetch(config.ollama+'/api/generate',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({model:first.model,keep_alive:first.keepAlive}),signal:AbortSignal.timeout(300000)}).then(r=>r.body?.cancel()).catch(()=>{});
 const stop=()=>server.close(()=>process.exit(0));
 process.once('SIGTERM',stop);process.once('SIGINT',stop);
 return server;
}

async function check(){
 const config=loadGatewayConfig();
 const identity=await ollamaIdentity(config);
 let ok=true;
 console.log('Ollama '+identity.ollama+' at '+config.ollama);
 for(const [id,state]of Object.entries(identity.profiles)){ok&&=state.installed;console.log((state.installed?'PASS ':'FAIL ')+id+' '+state.model+' pinned '+state.digest+(state.installed?'':' installed '+(state.installedDigest??'none'))+(state.loaded?' (loaded)':''));}
 if(!ok)console.log('A FAIL means the installed tag is missing or its digest differs from the pinned profile. Run `ollama list` and update the profile only after re-qualifying the model.');
 process.exitCode=ok?0:1;
}

async function smoke(origin){
 const url=new URL(origin);if(url.protocol!=='https:'&&!LOOPBACK.has(url.hostname))fail('SMOKE_ORIGIN');
 const keyId=process.env.KFM_HOME_AI_KEY_ID,secret=decodeSecret(process.env.KFM_HOME_AI_SECRET),profile=process.env.KFM_HOME_AI_PROFILE;
 if(!validKeyId(keyId)||!secret||!PROFILE_ID.test(profile??''))fail('SMOKE_ENV: set KFM_HOME_AI_KEY_ID, KFM_HOME_AI_SECRET and KFM_HOME_AI_PROFILE');
 const access=process.env.KFM_HOME_AI_ACCESS_CLIENT_ID?{'cf-access-client-id':process.env.KFM_HOME_AI_ACCESS_CLIENT_ID,'cf-access-client-secret':process.env.KFM_HOME_AI_ACCESS_CLIENT_SECRET??''}:{};
 const call=async(method,path,body='')=>{
  const signed=signRequest({keyId,secret,method,path,body});const began=performance.now();
  const response=await fetch(url.origin+path,{method,redirect:'error',headers:{...access,...signed.headers,...(body?{'content-type':'application/json'}:{})},body:body||undefined,signal:AbortSignal.timeout(300000)});
  const text=await response.text();
  const verified=verifyReply(secret,signed.nonce,response.status,text,response.headers.get(HOME_AI_HEADERS.reply));
  console.log(method+' '+path+' -> HTTP '+response.status+' reply-signature '+(verified?'VERIFIED':'MISSING/INVALID')+' in '+Math.round(performance.now()-began)+' ms');
  return {status:response.status,verified,value:JSON.parse(text)};
 };
 const health=await call('GET',HOME_AI_PATHS.health);
 console.log(JSON.stringify(health.value,null,1));
 const reply=await call('POST',HOME_AI_PATHS.discuss,JSON.stringify({profile,depth:'brief',messages:[{role:'system',content:'Answer using only the supplied synthetic test sentence.'},{role:'user',content:'Synthetic test: The sample marker is blue. What color is the sample marker? Answer with one word.'}]}));
 const pass=health.verified&&reply.verified&&reply.status===200&&/\bblue\b/i.test(reply.value.text??'');
 console.log((pass?'SYNTHETIC_PASS':'SYNTHETIC_FAIL')+' finishReason='+reply.value.finishReason+' timings='+JSON.stringify(reply.value.timings??null));
 process.exitCode=pass?0:1;
}

const invoked=process.argv[1]&&realpathSync(process.argv[1])===realpathSync(fileURLToPath(import.meta.url));
if(invoked){
 const [command,arg]=process.argv.slice(2);
 const run=command==='serve'?()=>serve():command==='check'?check:command==='smoke'?()=>smoke(arg??''):command==='keygen'&&validKeyId(arg)?async()=>console.log(JSON.stringify({[arg]:newSecret()})):null;
 if(!run){console.error('usage: home-inference-gateway.mjs serve | check | keygen <key-id> | smoke <https-origin>');process.exit(2);}
 run().catch(error=>{console.error('[KFM gateway] '+(error.code??'FAILED'));process.exit(1);});
}
