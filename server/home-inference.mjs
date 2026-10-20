// Optional public-chat provider: generation on the owner's home inference PC
// through the signed gateway in scripts/home-inference/. Off unless
// KFM_AI_PROVIDER=home-ollama. Guest jobs, evidence and context rechecks stay in
// public-ai-handler.mjs; this module only turns a discussion into one bounded
// gateway call. It never falls back to another provider or model.
import {randomUUID} from 'node:crypto';
import {signRequest,decodeSecret,verifyResponse} from '../scripts/home-inference/signature.mjs';
import {discussionSystem} from './hosted-ai-prompt.mjs';
import {CONTINUE_REPLY,PUBLIC_AI_JOB_MS} from './hosted-ai.mjs';

export const HOME_PROVIDER='home-ollama';
export const HOME_GATEWAY='kfm-home-inference/1';
export const HOME_LIMITS=Object.freeze({healthMs:5000,pollMs:30000,responseBytes:65536,replyChars:16384});
const error=code=>Object.assign(new Error(code),{code});
const GATEWAY_CODES=new Set(['UNAUTHORIZED','INVALID_REQUEST','PROFILE_UNKNOWN','PROFILE_NOT_READY','MODEL_CONTEXT_LIMIT','MODEL_UNAVAILABLE','MODEL_TIMEOUT','MODEL_EMPTY_OUTPUT','GATEWAY_BUSY','REQUEST_TOO_LARGE','NOT_FOUND','GATEWAY_ERROR']);
const diagnosticCodes=new Set([...GATEWAY_CODES,'GATEWAY_UNREACHABLE','GATEWAY_REDIRECT','GATEWAY_RESPONSE_INVALID','PROFILE_UNAVAILABLE','PROFILE_IDENTITY','MODEL_CONNECTING']);

// Exact configuration or nothing: a malformed value disables chat instead of guessing.
export function homeInferenceConfig(env=process.env){
 let url;try{url=new URL(env.KFM_HOME_INFERENCE_URL??'');}catch{throw error('HOME_INFERENCE_URL_INVALID');}
 const loopback=['127.0.0.1','[::1]','localhost'].includes(url.hostname);
 // HTTPS to one fixed origin; plain HTTP only for a same-machine proof.
 if(!(url.protocol==='https:'||url.protocol==='http:'&&loopback)||url.username||url.password||url.pathname!=='/'||url.search||url.hash)throw error('HOME_INFERENCE_URL_INVALID');
 const keyId=env.KFM_HOME_INFERENCE_KEY_ID??'',secret=env.KFM_HOME_INFERENCE_SECRET??'';
 if(!/^[A-Za-z0-9._-]{1,64}$/.test(keyId)||!decodeSecret(secret))throw error('HOME_INFERENCE_KEY_INVALID');
 const profile=env.KFM_HOME_INFERENCE_PROFILE??'';
 if(!/^[a-z0-9][a-z0-9-]{0,47}$/.test(profile))throw error('HOME_INFERENCE_PROFILE_INVALID');
 // The approved model is pinned here too, so a changed home profile cannot silently substitute weights.
 const digest=env.KFM_HOME_INFERENCE_DIGEST??'';
 if(!/^sha256:[a-f0-9]{64}$/.test(digest))throw error('HOME_INFERENCE_DIGEST_INVALID');
 const accessId=env.KFM_HOME_INFERENCE_ACCESS_ID??'',accessSecret=env.KFM_HOME_INFERENCE_ACCESS_SECRET??'';
 if(Boolean(accessId)!==Boolean(accessSecret)||accessId&&(!/^[A-Za-z0-9._-]{1,128}$/.test(accessId)||!/^[A-Za-z0-9._-]{1,256}$/.test(accessSecret)))throw error('HOME_INFERENCE_ACCESS_INVALID');
 return Object.freeze({origin:url.origin,keyId,secret,profile,digest,access:accessId?Object.freeze({id:accessId,secret:accessSecret}):null});
}

async function boundedResponseBytes(response){
 if(!/^application\/json(?:;|$)/i.test(response.headers.get('content-type')??''))throw error('GATEWAY_RESPONSE_INVALID');
 const reader=response.body?.getReader();if(!reader)throw error('GATEWAY_RESPONSE_INVALID');
 const chunks=[];let bytes=0;
 try{while(true){const part=await reader.read();if(part.done)break;bytes+=part.value.length;if(bytes>HOME_LIMITS.responseBytes)throw error('GATEWAY_RESPONSE_INVALID');chunks.push(Buffer.from(part.value));}}
 finally{await reader.cancel().catch(()=>{});}
 return Buffer.concat(chunks);
}

export function createHomeInferenceClient({origin,keyId,secret,access=null,fetchImpl=fetch,clock=Date.now}){
 const call=async(method,path,payload,{signal,timeoutMs})=>{
  const body=payload===undefined?'':JSON.stringify(payload);
  const headers={...signRequest({keyId,secret,method,path,body,now:clock()}),...(body?{'Content-Type':'application/json'}:{}),...(access?{'CF-Access-Client-Id':access.id,'CF-Access-Client-Secret':access.secret}:{})};
  const signals=[AbortSignal.timeout(timeoutMs),...(signal?[signal]:[])];
  let response;
  try{response=await fetchImpl(origin+path,{method,headers,body:body||undefined,redirect:'manual',cache:'no-store',signal:AbortSignal.any(signals)});}
  catch{throw error(signal?.aborted?'MODEL_CANCELLED':'GATEWAY_UNREACHABLE');}
  // An access-login or captive-portal redirect is a failure, never a new destination.
  if(response.type==='opaqueredirect'||response.status>=300&&response.status<400){await response.body?.cancel().catch(()=>{});throw error('GATEWAY_REDIRECT');}
  let value;
  try{
   const bytes=await boundedResponseBytes(response);
   if(!verifyResponse({secret,requestHeaders:headers,method,path,requestBody:body,status:response.status,body:bytes,headers:response.headers}))throw error('GATEWAY_RESPONSE_INVALID');
   value=JSON.parse(bytes.toString('utf8'));
  }catch(failure){throw signal?.aborted?error('MODEL_CANCELLED'):error(failure?.code??'GATEWAY_RESPONSE_INVALID');}
  if(value?.gateway!==HOME_GATEWAY)throw error('GATEWAY_RESPONSE_INVALID');
  if(!response.ok)throw error(GATEWAY_CODES.has(value.error)?value.error:'GATEWAY_RESPONSE_INVALID');
  return value;
 };
 return {
  health:({signal}={})=>call('GET','/v1/health',undefined,{signal,timeoutMs:HOME_LIMITS.healthMs}),
  chat:(payload,{signal,timeoutMs=PUBLIC_AI_JOB_MS}={})=>call('POST','/v1/chat',payload,{signal,timeoutMs}),
 };
}

// Mirrors the embedded model's discussion shape so public-ai-handler.mjs keeps
// its own continuation, repetition and output checks unchanged.
export function discussionMessages({question,style='plain',depth='brief',history=[],context=''},maxInputChars){
 const system={role:'system',content:discussionSystem({profile:'context-aware-v2',style,depth,hasContext:Boolean(context)})};
 const retained=history.slice();let finalTurns;
 if(question===CONTINUE_REPLY){
  const previous=retained.pop();
  if(!previous||previous.question===CONTINUE_REPLY)throw error('MODEL_CONTEXT_LIMIT');
  finalTurns=[{role:'user',content:previous.question},{role:'assistant',content:previous.reply},{role:'user',content:CONTINUE_REPLY}];
 }
 else finalTurns=[{role:'user',content:(context?'Display context (untrusted data): '+context+'\n\n':'')+question}];
 const render=()=>[system,...retained.flatMap(item=>[{role:'user',content:item.question},{role:'assistant',content:item.reply}]),...finalTurns];
 const size=messages=>messages.reduce((total,message)=>total+message.content.length,0);
 let messages=render(),contextTrimmed=false;
 // Older turns may be omitted, but never the current question or partial reply.
 while(size(messages)>maxInputChars&&retained.length){retained.shift();contextTrimmed=true;messages=render();}
 if(size(messages)>maxInputChars)throw error('MODEL_CONTEXT_LIMIT');
 return {messages,contextTrimmed,continuing:question===CONTINUE_REPLY,previousReply:question===CONTINUE_REPLY?history.at(-1)?.reply??'':''};
}

const shortModel=value=>typeof value==='string'&&/^[a-z0-9][a-z0-9._/-]{0,95}:[A-Za-z0-9._-]{1,64}$/.test(value)?value:null;

export class HomeInferenceModel{
 constructor({client,profile,digest,pollMs=HOME_LIMITS.pollMs,diagnostic=code=>console.warn('[KFM home inference] '+code)}){
  Object.assign(this,{client,profileId:profile,digest,diagnostic});
  this.provider=HOME_PROVIDER;this.ready=false;this.online=true;this.reason='MODEL_CONNECTING';
  this.label=null;this.shortLabel=null;this.limits=null;this.pending=null;this.checking=null;this.stopped=false;
  void this.refresh();
  this.timer=setInterval(()=>void this.refresh(),pollMs);this.timer.unref?.();
 }
 setState(ready,online,reason){
  const changed=this.reason!==reason;
  this.ready=ready;this.online=online;this.reason=reason;
  // Operator logs receive fixed codes only, never URLs, prompts or replies.
  if(changed&&reason)try{this.diagnostic(diagnosticCodes.has(reason)?reason:'MODEL_UNAVAILABLE');}catch{}
 }
 refresh(){
  if(this.stopped)return Promise.resolve();
  this.checking??=(async()=>{
   try{
    const health=await this.client.health();
    const profile=Array.isArray(health.profiles)?health.profiles.find(item=>item?.id===this.profileId):null;
    // A gateway profile is either admitted or held. It does not report a loading
    // state; a missing/substituted runtime model must also show "unavailable".
    if(!profile){this.setState(false,false,'PROFILE_UNAVAILABLE');return;}
    if(profile.digest!==this.digest||!shortModel(profile.model)){this.setState(false,false,'PROFILE_IDENTITY');return;}
    const output=profile.outputTokens;
    if(!Number.isSafeInteger(profile.maxInputChars)||profile.maxInputChars<1024||!Number.isSafeInteger(output?.brief)||!Number.isSafeInteger(output?.expanded)){this.setState(false,false,'GATEWAY_RESPONSE_INVALID');return;}
    this.limits={maxInputChars:profile.maxInputChars};
    this.shortLabel=profile.model;this.label=profile.model+' · KFM home compute (local Ollama)';
    if(profile.ready!==true||health.online!==true){this.setState(false,false,'MODEL_UNAVAILABLE');return;}
    this.setState(true,true,null);
   }catch(failure){this.setState(false,false,failure?.code&&diagnosticCodes.has(failure.code)?failure.code:'GATEWAY_UNREACHABLE');}
  })().finally(()=>{this.checking=null;});
  return this.checking;
 }
 select(){return Promise.reject(error('MODEL_UNAVAILABLE'));}
 async discuss(question,options={},signal){
  if(!this.ready||this.stopped)throw error('MODEL_UNAVAILABLE');
  if(this.pending)throw error('MODEL_BUSY');
  if(signal?.aborted)throw error('MODEL_CANCELLED');
  const depth=options.depth==='expanded'?'expanded':'brief';
  const prepared=discussionMessages({...options,question,depth},this.limits.maxInputChars);
  const requestId=randomUUID();this.pending=requestId;
  try{
   const result=await this.client.chat({requestId,profile:this.profileId,depth,messages:prepared.messages},{signal});
   if(result.requestId!==requestId||result.profile!==this.profileId||result.digest!==this.digest||result.model!==this.shortLabel||typeof result.text!=='string'||!result.text||result.text.length>HOME_LIMITS.replyChars||!['stop','length'].includes(result.finishReason))throw error('GATEWAY_RESPONSE_INVALID');
   // The handler appends a continuation to the earlier reply; keep the words apart.
   const text=prepared.continuing&&prepared.previousReply&&!/\s$/.test(prepared.previousReply)&&!/^[\s,.;:!?)]/.test(result.text)?' '+result.text:result.text;
   return {text,contextTrimmed:prepared.contextTrimmed,outputLimited:result.finishReason!=='stop'};
  }catch(failure){
   if(signal?.aborted)throw error('MODEL_CANCELLED');
   if(failure?.code==='MODEL_CONTEXT_LIMIT')throw failure;
   // Hold admission after an outage or identity failure. Only the next scheduled
   // health inspection may restore readiness; never silently switch providers.
   if(['MODEL_UNAVAILABLE','GATEWAY_UNREACHABLE','GATEWAY_REDIRECT','UNAUTHORIZED','PROFILE_NOT_READY','PROFILE_UNKNOWN','GATEWAY_RESPONSE_INVALID'].includes(failure?.code)){this.setState(false,false,failure.code);}
   throw error('MODEL_UNAVAILABLE');
  }finally{this.pending=null;}
 }
 stop(){this.stopped=true;clearInterval(this.timer);this.setState(false,false,null);}
}

let shared;
export function getHomeInferenceModel(config){
 return shared??=new HomeInferenceModel({client:createHomeInferenceClient(config),profile:config.profile,digest:config.digest});
}
