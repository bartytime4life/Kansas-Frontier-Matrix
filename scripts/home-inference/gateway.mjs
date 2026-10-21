#!/usr/bin/env node
// KFM home inference gateway. Runs on the owner's inference PC in front of a
// loopback-only Ollama. It accepts exactly two signed routes, one bounded chat
// shape and owner-approved model profiles. It never exposes Ollama's own API,
// model management, tools, URL fetching or shell access. No dependencies.
import {createServer} from 'node:http';
import {readFileSync,statSync} from 'node:fs';
import {join} from 'node:path';
import {pathToFileURL} from 'node:url';
import {createNonceCache,decodeSecret,newSecret,verifyRequest,signResponse,isSystemdCredentialDirectory,RESPONSE_SIGNATURE_HEADER} from './signature.mjs';

export const GATEWAY_VERSION='kfm-home-inference/1';
export const GATEWAY_LIMITS=Object.freeze({requestBytes:32768,bodyMs:5000,messages:16,inspectMs:3000,inspectCacheMs:10000,outputBytes:32768,replyBytes:4096,chatMs:90000});
const DEPTHS=['brief','expanded'];
const ROLES=['system','user','assistant'];
const OPTION_KEYS=['temperature','top_p','top_k','min_p','repeat_penalty','presence_penalty','frequency_penalty','seed'];
const PROFILE_ID=/^[a-z0-9][a-z0-9-]{0,47}$/;
const SCOPE=/^[a-z][a-z0-9-]{0,31}$/;
const MODEL_TAG=/^[a-z0-9][a-z0-9._/-]{0,95}:[A-Za-z0-9._-]{1,64}$/;
const REQUEST_ID=/^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/;

const fail=(code,status)=>Object.assign(new Error(code),{code,status});
const isLoopback=host=>['127.0.0.1','::1','[::1]','localhost'].includes(host);
const safeText=(value,max)=>typeof value==='string'&&value.length>0&&value.length<=max&&!/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/.test(value);
const digestHex=value=>typeof value==='string'&&/^(?:sha256:)?[a-f0-9]{64}$/.test(value)?value.replace(/^sha256:/,''):null;
const positive=(value,max)=>Number.isSafeInteger(value)&&value>0&&value<=max;

// ---------------------------------------------------------------- configuration

export function parseProfiles(value){
 if(!value||typeof value!=='object'||!Array.isArray(value.profiles)||!value.profiles.length||value.profiles.length>16)throw fail('PROFILES_INVALID');
 const concurrency=value.concurrency??1,maxQueue=value.maxQueue??2;
 if(!positive(concurrency,4)||!Number.isSafeInteger(maxQueue)||maxQueue<0||maxQueue>16)throw fail('PROFILES_INVALID');
 const profiles=new Map();
 for(const p of value.profiles){
  const invalid=()=>fail('PROFILE_INVALID:'+(typeof p?.id==='string'?p.id.slice(0,48):'?'));
  if(!p||typeof p!=='object'||!PROFILE_ID.test(p.id??'')||profiles.has(p.id))throw invalid();
  if(!safeText(p.label,80)||!MODEL_TAG.test(p.model??'')||!digestHex(p.digest)||!safeText(p.license,120))throw invalid();
  // Cloud-marked models execute remotely; the home-compute requirement excludes them.
  if(/(?:^|[:-])cloud$/i.test(p.model))throw invalid();
  if(!Array.isArray(p.scopes)||!p.scopes.length||!p.scopes.every(scope=>SCOPE.test(scope)))throw invalid();
  if(!Array.isArray(p.capabilities)||!p.capabilities.includes('chat'))throw invalid();
  if(!positive(p.contextTokens,131072)||!positive(p.maxInputChars,262144))throw invalid();
  if(!DEPTHS.every(depth=>positive(p.outputTokens?.[depth],8192)&&positive(p.timeoutMs?.[depth],GATEWAY_LIMITS.chatMs)))throw invalid();
  if(DEPTHS.some(depth=>p.outputTokens[depth]>=p.contextTokens))throw invalid();
  const options=p.options??{};
  if(typeof options!=='object'||Object.keys(options).some(key=>!OPTION_KEYS.includes(key)||!Number.isFinite(options[key])))throw invalid();
  if(p.think!==undefined&&typeof p.think!=='boolean')throw invalid();
  if(p.keepAlive!==undefined&&!/^(?:0|-1|[1-9][0-9]{0,4}[smh])$/.test(p.keepAlive))throw invalid();
  profiles.set(p.id,Object.freeze({...p,digest:digestHex(p.digest),scopes:[...p.scopes],options:{...options}}));
 }
 return {profiles,concurrency,maxQueue};
}

export function parseKeys(value){
 if(!value||typeof value!=='object'||!Array.isArray(value.keys)||value.keys.length>8)throw fail('KEYS_INVALID');
 const keys=new Map();
 for(const entry of value.keys){
  const secret=decodeSecret(entry?.secret);
  if(!entry||!/^[A-Za-z0-9._-]{1,64}$/.test(entry.id??'')||keys.has(entry.id)||!SCOPE.test(entry.scope??'')||!secret)throw fail('KEYS_INVALID');
  keys.set(entry.id,Object.freeze({id:entry.id,scope:entry.scope,secret}));
 }
 return keys;
}

function readJson(path,{privateFile=false,credential=false}={}){
 const stat=statSync(path);
 if(!stat.isFile()||stat.size>65536)throw fail('CONFIG_FILE_INVALID');
 // A key file readable by other local accounts is a credential leak; refuse it.
 // systemd grants a DynamicUser read access to its credential through an ACL,
 // which shows in the group bits. Only inside its verified private credential
 // directory is group read accepted; world access is always refused.
 if(privateFile&&(stat.mode&(credential?0o007:0o077)))throw fail('KEYS_FILE_PERMISSIONS');
 return JSON.parse(readFileSync(path,'utf8'));
}

export function loadConfig(env=process.env,{credentialsRoot}={}){
 const keysPath=env.KFM_GATEWAY_KEYS||(env.CREDENTIALS_DIRECTORY?join(env.CREDENTIALS_DIRECTORY,'gateway-keys.json'):'');
 if(!keysPath)throw fail('KEYS_NOT_CONFIGURED');
 const ollama=new URL(env.KFM_OLLAMA_URL||'http://127.0.0.1:11434');
 // Raw Ollama must stay on loopback; this gateway is not a way to reach another host.
 if(ollama.protocol!=='http:'||!isLoopback(ollama.hostname)||ollama.username||ollama.password||ollama.pathname!=='/'||ollama.search)throw fail('OLLAMA_URL_NOT_LOOPBACK');
 const host=env.KFM_GATEWAY_HOST||'127.0.0.1',port=Number(env.KFM_GATEWAY_PORT||8787);
 if(!isLoopback(host))throw fail('GATEWAY_HOST_NOT_LOOPBACK');
 if(!positive(port,65535))throw fail('GATEWAY_PORT_INVALID');
 return {
  host,port,ollamaUrl:ollama.origin,
  profiles:parseProfiles(readJson(env.KFM_GATEWAY_PROFILES||'/etc/kfm-inference/profiles.json')),
  keys:parseKeys(readJson(keysPath,{privateFile:true,credential:!env.KFM_GATEWAY_KEYS&&isSystemdCredentialDirectory(env.CREDENTIALS_DIRECTORY,{root:credentialsRoot})})),
 };
}

// ---------------------------------------------------------------- admission

export function createAdmission({concurrency=1,maxQueue=2}={}){
 let active=0;const waiting=[];
 const drain=()=>{while(active<concurrency&&waiting.length){active++;waiting.shift().grant();}};
 const release=()=>{let done=false;return ()=>{if(done)return;done=true;active--;drain();};};
 return {
  get active(){return active;},
  get queued(){return waiting.length;},
  updateLimits({concurrency:nextConcurrency,maxQueue:nextMaxQueue}){
   // Accepted work retains its slots and FIFO order. Lower limits apply as it
   // drains; higher concurrency can immediately admit existing waiters.
   concurrency=nextConcurrency;maxQueue=nextMaxQueue;drain();
  },
  enter(signal){
   if(signal?.aborted)return Promise.reject(fail('REQUEST_CANCELLED',499));
   if(active<concurrency){active++;return Promise.resolve(release());}
   if(waiting.length>=maxQueue)return Promise.reject(fail('GATEWAY_BUSY',429));
   return new Promise((resolve,reject)=>{
    const entry={grant:()=>{signal?.removeEventListener('abort',abort);resolve(release());}};
    const abort=()=>{const index=waiting.indexOf(entry);if(index>=0)waiting.splice(index,1);reject(fail('REQUEST_CANCELLED',499));};
    signal?.addEventListener('abort',abort,{once:true});
    waiting.push(entry);
   });
  },
 };
}

// ---------------------------------------------------------------- Ollama access

async function ollamaJson(fetchImpl,url,signal){
 const response=await fetchImpl(url,{signal,redirect:'error'});
 if(!response.ok)throw fail('MODEL_UNAVAILABLE',503);
 const text=await response.text();
 if(text.length>1048576)throw fail('MODEL_UNAVAILABLE',503);
 return JSON.parse(text);
}

export function createInspector({ollamaUrl,profiles,fetchImpl=fetch,clock=Date.now}){
 let cached=null,inflight=null,sequence=0,cachedSequence=0;
 const inspect=async()=>{
  const signal=AbortSignal.timeout(GATEWAY_LIMITS.inspectMs);
  try{
   const [version,tags]=await Promise.all([ollamaJson(fetchImpl,ollamaUrl+'/api/version',signal),ollamaJson(fetchImpl,ollamaUrl+'/api/tags',signal)]);
   const installed=new Map((Array.isArray(tags?.models)?tags.models:[]).filter(m=>m&&typeof m.name==='string').map(m=>[m.name,m]));
   const state=new Map();
   for(const profile of profiles.values()){
    const model=installed.get(profile.model);
    // Remote-hosted entries are cloud models even when they carry a local-looking tag.
    state.set(profile.id,!model?'MODEL_NOT_INSTALLED':model.remote_host||model.remote_model?'MODEL_IS_REMOTE':digestHex(model.digest)!==profile.digest?'PROFILE_DIGEST_MISMATCH':null);
   }
   return {at:clock(),online:true,runtime:typeof version?.version==='string'&&version.version.length<=40?version.version:null,state};
  }catch{
   return {at:clock(),online:false,runtime:null,state:new Map([...profiles.keys()].map(id=>[id,'MODEL_UNAVAILABLE']))};
  }
 };
 const run=()=>{
  const started=++sequence;
  return inspect().then(value=>{if(started>cachedSequence){cached=value;cachedSequence=started;}return value;});
 };
 return async({fresh=false}={})=>{
  // Admission must start its own reads: an older health check may already have
  // fetched tags while still awaiting version. Its eventual result must not
  // overwrite the cache from a newer admission inspection either.
  if(fresh)return run();
  if(!fresh&&cached&&clock()-cached.at<GATEWAY_LIMITS.inspectCacheMs)return cached;
  inflight??=run().finally(()=>{inflight=null;});
  return inflight;
 };
}

// Ollama streams NDJSON; reading it incrementally lets the gateway stop at the
// output bound, honour cancellation and never buffer an unbounded reply.
async function thinkingMode({fetchImpl,ollamaUrl,profile,signal}){
 const response=await fetchImpl(ollamaUrl+'/api/show',{method:'POST',redirect:'error',
  signal:AbortSignal.any([signal,AbortSignal.timeout(GATEWAY_LIMITS.inspectMs)]),
  headers:{'Content-Type':'application/json'},body:JSON.stringify({model:profile.model})});
 if(!response.ok)throw fail('MODEL_UNAVAILABLE',503);
 const metadata=await response.json(),values=metadata.thinking?.values;
 let think=profile.think;
 // Some pinned templates always reason. Asking those models for think:false
 // disables Ollama's reasoning parser without disabling their reasoning, so
 // their private preamble lands in content. Use their supported parser mode.
 if(think===false&&Array.isArray(values)&&values.length&&!values.includes(false)){
  think=values.includes(true)?true:metadata.thinking.default;
  if(think!==true&&!(typeof think==='string'&&values.includes(think)))throw fail('MODEL_UNAVAILABLE',503);
 }
 const implicit=think===true||typeof think==='string'||think===undefined&&metadata.thinking?.default!==false&&Array.isArray(values)&&values.some(value=>value!==false);
 return {think,implicit};
}

// Also accept older streams that put tagged reasoning in content. A missing
// opening tag means the model template opened it; a closing tag discards the
// entire preamble. Incomplete blocks never become deadline/length partials.
function answerText(raw,{implicit,separated,complete}){
 // A native parser may omit an empty thinking channel. Its clean completed
 // answer is valid; an unclosed implicit preamble is never a partial answer.
 let preamble=implicit&&!separated&&!complete,depth=0,cursor=0,text='';
 for(const match of raw.matchAll(/<\/?think>/gi)){
  if(!preamble&&!depth)text+=raw.slice(cursor,match.index);
  if(match[0][1]==='/'){
   if(depth)depth--;
   else{text='';preamble=false;}
  }else{depth++;preamble=false;}
  cursor=match.index+match[0].length;
 }
 if(!preamble&&!depth)text+=raw.slice(cursor);
 const partial=text.lastIndexOf('<');
 if(partial>=0&&['<think>','</think>'].some(marker=>marker.startsWith(text.slice(partial).toLowerCase())))text=text.slice(0,partial);
 return text;
}

async function streamChat({fetchImpl,ollamaUrl,profile,depth,messages,signal,progress}){
 const mode=await thinkingMode({fetchImpl,ollamaUrl,profile,signal});
 const response=await fetchImpl(ollamaUrl+'/api/chat',{method:'POST',signal,redirect:'error',headers:{'Content-Type':'application/json'},body:JSON.stringify({
  model:profile.model,messages,stream:true,
  ...(mode.think===undefined?{}:{think:mode.think}),
  ...(profile.keepAlive===undefined?{}:{keep_alive:profile.keepAlive}),
  options:{...profile.options,num_ctx:profile.contextTokens,num_predict:profile.outputTokens[depth]},
 })});
 if(!response.ok||!response.body)throw fail('MODEL_UNAVAILABLE',503);
 const decoder=new TextDecoder();let buffer='',raw='',text='',separated=false,final=null,limited=false;
 const reader=response.body.getReader();
 try{
  while(!final&&!limited){
   const part=await reader.read();if(part.done)break;
   buffer+=decoder.decode(part.value,{stream:true});
   if(buffer.length>GATEWAY_LIMITS.outputBytes*2)throw fail('MODEL_UNAVAILABLE',503);
   let newline;
   while((newline=buffer.indexOf('\n'))>=0){
    const line=buffer.slice(0,newline).trim();buffer=buffer.slice(newline+1);
    if(!line)continue;
    const chunk=JSON.parse(line);
    if(chunk.error)throw fail('MODEL_UNAVAILABLE',503);
    if(chunk.model!==profile.model)throw fail('PROFILE_NOT_READY',503);
    // Ollama's separate reasoning channel is never retained or returned.
    if(typeof chunk.message?.thinking==='string'&&chunk.message.thinking)separated=true;
    if(typeof chunk.message?.content==='string')raw+=chunk.message.content;
    text=answerText(raw,{implicit:mode.implicit,separated,complete:chunk.done===true&&chunk.done_reason==='stop'});
    // Generation tokens include private reasoning. Bound the visible answer
    // separately so extra reasoning allowance cannot exceed public chat's cap.
    const bytes=Buffer.from(text);
    if(bytes.length>GATEWAY_LIMITS.replyBytes){
     text=new TextDecoder().decode(bytes.subarray(0,GATEWAY_LIMITS.replyBytes),{stream:true});limited=true;
    }
    progress.text=text;
    if(limited)break;
    if(Buffer.byteLength(raw)>GATEWAY_LIMITS.outputBytes){limited=true;break;}
    if(chunk.done){final=chunk;break;}
   }
  }
 }finally{await reader.cancel().catch(()=>{});}
 if(!final&&!limited)throw fail('MODEL_UNAVAILABLE',503);
 return {text,final:final??{},limited};
}

// ---------------------------------------------------------------- request handling

// Ollama renders message text into the model's chat template verbatim. Break up
// role-control markers so visitor or retrieved text cannot open a new turn.
export const neutralizeTemplate=value=>value.replaceAll('<|','< |').replace(/<(\/?)(start_of_turn|end_of_turn|think)>/g,'< $1$2>').replace(/\[(\/?)INST\]/g,'[ $1INST]');

function validateChat(value,profiles,scope){
 if(!value||typeof value!=='object'||Array.isArray(value))throw fail('INVALID_REQUEST',400);
 if(Object.keys(value).some(key=>!['requestId','profile','depth','messages'].includes(key)))throw fail('INVALID_REQUEST',400);
 if(!REQUEST_ID.test(value.requestId??'')||!DEPTHS.includes(value.depth))throw fail('INVALID_REQUEST',400);
 const profile=profiles.get(value.profile);
 // An unknown profile and one outside this key's scope look the same to the caller.
 if(!profile||!profile.scopes.includes(scope))throw fail('PROFILE_UNKNOWN',422);
 const messages=value.messages;
 if(!Array.isArray(messages)||!messages.length||messages.length>GATEWAY_LIMITS.messages)throw fail('INVALID_REQUEST',400);
 let chars=0;
 messages.forEach((message,index)=>{
  if(!message||typeof message!=='object'||Object.keys(message).some(key=>!['role','content'].includes(key)))throw fail('INVALID_REQUEST',400);
  if(!ROLES.includes(message.role)||typeof message.content!=='string'||!message.content.length||/[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]/.test(message.content))throw fail('INVALID_REQUEST',400);
  if(message.role==='system'&&index!==0)throw fail('INVALID_REQUEST',400);
  chars+=message.content.length;
 });
 if(messages.at(-1).role!=='user')throw fail('INVALID_REQUEST',400);
 if(chars>profile.maxInputChars)throw fail('MODEL_CONTEXT_LIMIT',422);
 return {profile,depth:value.depth,requestId:value.requestId,messages:messages.map(({role,content})=>({role,content:role==='system'?content:neutralizeTemplate(content)}))};
}

function readBody(req){
 return new Promise((resolve,reject)=>{
  const chunks=[];let bytes=0;
  const timer=setTimeout(()=>{reject(fail('BODY_TIMEOUT',408));req.destroy();},GATEWAY_LIMITS.bodyMs);
  // Over the limit: stop buffering and answer 413; the connection closes after the reply.
  req.on('data',chunk=>{if(bytes>GATEWAY_LIMITS.requestBytes)return;bytes+=chunk.length;if(bytes>GATEWAY_LIMITS.requestBytes){clearTimeout(timer);chunks.length=0;reject(fail('REQUEST_TOO_LARGE',413));}else chunks.push(chunk);});
  req.on('end',()=>{clearTimeout(timer);resolve(Buffer.concat(chunks).toString('utf8'));});
  req.on('error',()=>{clearTimeout(timer);reject(fail('INVALID_REQUEST',400));});
 });
}

function untilAbort(promise,signal){
 return new Promise((resolve,reject)=>{
  const abort=()=>reject(fail('REQUEST_CANCELLED',499));
  if(signal.aborted){abort();return;}
  signal.addEventListener('abort',abort,{once:true});
  promise.then(resolve,reject).finally(()=>signal.removeEventListener('abort',abort));
 });
}

export function createGateway({profiles:profileConfig,keys,ollamaUrl='http://127.0.0.1:11434',fetchImpl=fetch,clock=Date.now,log=line=>console.log(JSON.stringify(line))}){
 const state={profiles:profileConfig.profiles,keys};
 const admission=createAdmission(profileConfig);
 let inspector=createInspector({ollamaUrl,profiles:state.profiles,fetchImpl,clock});
 const nonces=createNonceCache({clock});
 const active=new Set();

 const health=async scope=>{
  // Keep metadata paired with the inspector selected before asynchronous I/O.
  // A reload may replace the profile map while this inspection is pending.
  const profileSnapshot=state.profiles;
  const inspection=await inspector();
  const profiles=[...profileSnapshot.values()].filter(p=>p.scopes.includes(scope)).map(p=>({
   id:p.id,label:p.label,model:p.model,digest:'sha256:'+p.digest,license:p.license,capabilities:[...p.capabilities],
   contextTokens:p.contextTokens,maxInputChars:p.maxInputChars,outputTokens:{...p.outputTokens},
   ready:inspection.state.get(p.id)===null,reason:inspection.state.get(p.id)??null,
  }));
  return {gateway:GATEWAY_VERSION,online:inspection.online,runtime:inspection.runtime?{name:'ollama',version:inspection.runtime}:null,active:admission.active,queued:admission.queued,profiles};
 };

 const chat=async(value,scope,signal,record)=>{
  const request=validateChat(value,state.profiles,scope);
  // A queued request keeps the inspector for its validated profile snapshot,
  // so a reload cannot check a different digest before serving the old profile.
  const inspect=inspector;
  Object.assign(record,{profile:request.profile.id,depth:request.depth,requestId:request.requestId});
  const queuedAt=clock();let release;
  const controller=new AbortController(),timeout=request.profile.timeoutMs[request.depth];
  const abort=()=>controller.abort();signal.addEventListener('abort',abort,{once:true});
  if(signal.aborted)controller.abort();
  // One deadline covers waiting, fresh identity inspection and generation.
  const timer=setTimeout(()=>controller.abort(),timeout);active.add(controller);
  try{
   release=await admission.enter(controller.signal);
   record.queueMs=clock()-queuedAt;
   const ready=(await untilAbort(inspect({fresh:true}),controller.signal)).state.get(request.profile.id);
   if(ready!==null)throw fail(ready==='MODEL_UNAVAILABLE'?'MODEL_UNAVAILABLE':'PROFILE_NOT_READY',503);
   if(controller.signal.aborted)throw fail('MODEL_TIMEOUT',504);
   let output;const progress={text:''};
   try{output=await streamChat({fetchImpl,ollamaUrl,profile:request.profile,depth:request.depth,messages:request.messages,signal:controller.signal,progress});}
   catch(error){
    if(signal.aborted)throw fail('REQUEST_CANCELLED',499);
    // At the deadline, return what was written as a length-limited reply the visitor may continue.
    if(controller.signal.aborted&&progress.text.trim())output={text:progress.text,final:{},limited:true};
    else if(controller.signal.aborted)throw fail('MODEL_TIMEOUT',504);
    else if(error.code)throw error;
    else throw fail('MODEL_UNAVAILABLE',503);
   }
   const final=output.final,promptTokens=Number.isSafeInteger(final.prompt_eval_count)?final.prompt_eval_count:null,outputTokens=Number.isSafeInteger(final.eval_count)?final.eval_count:null;
   // Ollama silently truncates an over-long prompt; treat a full window as a refusal, not an answer.
   if(promptTokens!==null&&promptTokens>request.profile.contextTokens-request.profile.outputTokens[request.depth])throw fail('MODEL_CONTEXT_LIMIT',422);
   const text=output.text.trim();
   if(!text)throw fail('MODEL_EMPTY_OUTPUT',502);
   const finishReason=output.limited||final.done_reason==='length'?'length':'stop';
   const seconds=Number.isFinite(final.eval_duration)&&final.eval_duration>0?final.eval_duration/1e9:null;
   Object.assign(record,{promptTokens,outputTokens,finishReason});
   return {
    gateway:GATEWAY_VERSION,requestId:request.requestId,profile:request.profile.id,model:request.profile.model,digest:'sha256:'+request.profile.digest,
    text,finishReason,usage:{promptTokens,outputTokens},
    timings:{queueMs:record.queueMs,loadMs:Number.isFinite(final.load_duration)?Math.round(final.load_duration/1e6):null,totalMs:clock()-queuedAt,tokensPerSecond:seconds&&outputTokens?Math.round(outputTokens/seconds*10)/10:null},
   };
  }catch(error){
   if(signal.aborted)throw fail('REQUEST_CANCELLED',499);
   if(controller.signal.aborted)throw fail('MODEL_TIMEOUT',504);
   throw error;
  }finally{clearTimeout(timer);signal.removeEventListener('abort',abort);active.delete(controller);controller.abort();release?.();}
 };

 const send=(res,status,body,authentication)=>{
  if(res.headersSent||res.destroyed)return;
  const payload=JSON.stringify(body);
  const close=status===413||status===408;
  const signed=authentication?{[RESPONSE_SIGNATURE_HEADER]:signResponse({...authentication,status,body:payload})}:{};
  res.writeHead(status,{'Content-Type':'application/json; charset=utf-8','Content-Length':Buffer.byteLength(payload),'Cache-Control':'no-store','X-Content-Type-Options':'nosniff',...signed,...(close?{Connection:'close'}:{})});
  res.end(payload,close?()=>res.socket?.destroy():undefined);
 };

 const handler=async(req,res)=>{
  const started=clock(),record={event:'request',method:req.method,path:null,status:0,code:null};
  // The response closing before we finish means the caller went away: stop generating.
  const disconnected=new AbortController();
  let authentication;
  res.on('close',()=>{if(!res.writableFinished)disconnected.abort();});
  try{
   const path=req.url??'';
   if(!['GET','POST'].includes(req.method))throw fail('METHOD_DENIED',405);
   if(!/^\/v1\/[a-z]+$/.test(path))throw fail('UNAUTHORIZED',401);
   record.path=path;
   const body=await readBody(req);
   if(req.method==='GET'&&body)throw fail('INVALID_REQUEST',400);
   const auth=verifyRequest({headers:req.headers,method:req.method,path,body,keys:state.keys,nonces,now:clock()});
   if(!auth.ok){record.authFailure=auth.reason;throw fail('UNAUTHORIZED',401);}
   authentication={secret:auth.key.secret,requestHeaders:req.headers,method:req.method,path,requestBody:body};
   record.keyId=auth.key.id;
   let result;
   if(path==='/v1/health'&&req.method==='GET')result=await health(auth.key.scope);
   else if(path==='/v1/chat'&&req.method==='POST'){
    if(!/^application\/json(?:;|$)/i.test(req.headers['content-type']??''))throw fail('INVALID_REQUEST',400);
    let value;try{value=JSON.parse(body);}catch{throw fail('INVALID_REQUEST',400);}
    result=await chat(value,auth.key.scope,disconnected.signal,record);
   }
   else throw fail('NOT_FOUND',404);
   record.status=200;send(res,200,result,authentication);
  }catch(error){
   const status=Number.isInteger(error?.status)?error.status:500,code=status===500?'GATEWAY_ERROR':error.code;
   Object.assign(record,{status,code});
   if(status===429)res.setHeader?.('Retry-After','5');
   send(res,status===499?400:status,{gateway:GATEWAY_VERSION,error:code},authentication);
  }finally{
   record.totalMs=clock()-started;
   // Operational metadata only: never prompts, replies, headers or secrets.
   try{log({at:new Date(started).toISOString(),...record});}catch{}
  }
 };

 return {
  handler,
  get admission(){return admission;},
  reload({profiles:nextProfiles,keys:nextKeys}){
   if(nextKeys)state.keys=nextKeys;
   if(nextProfiles){state.profiles=nextProfiles.profiles;admission.updateLimits(nextProfiles);inspector=createInspector({ollamaUrl,profiles:state.profiles,fetchImpl,clock});}
  },
  abortAll(){for(const controller of active)controller.abort();},
  inspect:options=>inspector(options),
 };
}

export function startGateway(config,options={}){
 const gateway=createGateway({profiles:config.profiles,keys:config.keys,ollamaUrl:config.ollamaUrl,...options});
 const server=createServer({maxHeaderSize:8192},gateway.handler);
 server.headersTimeout=5000;server.requestTimeout=10000;server.keepAliveTimeout=5000;server.maxHeadersCount=40;
 return new Promise((resolve,reject)=>{server.once('error',reject);server.listen(config.port,config.host,()=>resolve({server,gateway}));});
}

// ---------------------------------------------------------------- command line

async function main(argv){
 if(argv[0]==='--new-key'){
  const id=argv[1],scope=argv[2]??'production';
  if(!/^[A-Za-z0-9._-]{1,64}$/.test(id??'')||!SCOPE.test(scope)){console.error('usage: gateway.mjs --new-key <key-id> [scope]');return 2;}
  console.log(JSON.stringify({id,scope,secret:newSecret()}));
  return 0;
 }
 let config;
 try{config=loadConfig();}catch(error){console.error(JSON.stringify({event:'config_refused',code:error.code??'CONFIG_INVALID'}));return 1;}
 if(argv[0]==='--check'){
  const gateway=createGateway({profiles:config.profiles,keys:config.keys,ollamaUrl:config.ollamaUrl,log:()=>{}});
  const inspection=await gateway.inspect({fresh:true});
  const profiles=Object.fromEntries([...inspection.state].map(([id,reason])=>[id,reason??'READY']));
  console.log(JSON.stringify({gateway:GATEWAY_VERSION,listen:config.host+':'+config.port,ollama:inspection.online?inspection.runtime:'UNREACHABLE',keys:[...config.keys.values()].map(k=>({id:k.id,scope:k.scope})),profiles},null,1));
  return inspection.online&&Object.values(profiles).some(value=>value==='READY')?0:1;
 }
 const {server,gateway}=await startGateway(config);
 console.log(JSON.stringify({event:'listening',gateway:GATEWAY_VERSION,listen:config.host+':'+config.port,profiles:[...config.profiles.profiles.keys()],keys:config.keys.size}));
 // SIGHUP reloads keys and profiles: revoke a key by deleting it and reloading.
 process.on('SIGHUP',()=>{try{const next=loadConfig();gateway.reload({profiles:next.profiles,keys:next.keys});console.log(JSON.stringify({event:'reloaded',profiles:[...next.profiles.profiles.keys()],keys:next.keys.size}));}catch(error){console.error(JSON.stringify({event:'reload_refused',code:error.code??'CONFIG_INVALID'}));}});
 const stop=()=>{server.close();gateway.abortAll();setTimeout(()=>process.exit(0),2000).unref();};
 process.once('SIGTERM',stop);process.once('SIGINT',stop);
 return null;
}

if(import.meta.url===pathToFileURL(process.argv[1]??'').href)main(process.argv.slice(2)).then(code=>{if(code!==null)process.exitCode=code;});
