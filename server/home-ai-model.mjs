// Home inference provider: the same discuss() interface as HostedAiModel, served
// by the owner's inference PC through scripts/home-inference/home-inference-gateway.mjs.
// Selecting it never forks the embedded model. There is no fallback provider:
// when the gateway is unreachable or its model identity changes, chat is unavailable.
import {
 HOME_AI_CONTRACT,HOME_AI_HEADERS,HOME_AI_MAX_RESPONSE_BYTES,HOME_AI_PATHS,HOME_AI_FINISH_REASONS,
 MODEL_DIGEST,MODEL_TAG,PROFILE_ID,decodeSecret,messageBytes,signRequest,validKeyId,verifyReply,
} from '../scripts/home-inference/home-ai-contract.mjs';
import {CONTINUE_REPLY,discussionSystem} from './hosted-ai-prompt.mjs';

export const HOME_AI_PROVIDER='home-ollama';
export const HOME_AI_HEALTH_MS=30000;
// A ready state older than this is stale; chat reports unavailable until the next good check.
export const HOME_AI_STALE_MS=75000;
// The gateway caps each run below Cloudflare's 100-second proxied response limit.
const HOME_AI_REQUEST_MS=110000;
const error=code=>Object.assign(new Error(code),{code});
const DISPLAY_NAME=/^[A-Za-z0-9][A-Za-z0-9 .:·()+_-]{0,47}$/;

// Server-side secrets only. Returns null unless every required value is valid,
// so a partial configuration cannot start an unauthenticated or unpinned provider.
export function homeAiConfig(env=process.env){
 let url;try{url=new URL(env.KFM_HOME_AI_URL??'');}catch{return null;}
 // One exact HTTPS origin: no credentials, path, query or fragment to redirect elsewhere.
 if(url.protocol!=='https:'||url.username||url.password||url.pathname!=='/'||url.search||url.hash||url.origin!==(env.KFM_HOME_AI_URL??'').replace(/\/$/,''))return null;
 const keyId=env.KFM_HOME_AI_KEY_ID,secret=decodeSecret(env.KFM_HOME_AI_SECRET),profile=env.KFM_HOME_AI_PROFILE,digest=env.KFM_HOME_AI_MODEL_DIGEST;
 if(!validKeyId(keyId)||!secret||!PROFILE_ID.test(profile??'')||!MODEL_DIGEST.test(digest??''))return null;
 const accessId=env.KFM_HOME_AI_ACCESS_CLIENT_ID,accessSecret=env.KFM_HOME_AI_ACCESS_CLIENT_SECRET;
 // Cloudflare Access service-token headers are optional but must be complete when present.
 if(Boolean(accessId)!==Boolean(accessSecret)||accessId&&(!/^[A-Za-z0-9._-]{8,128}$/.test(accessId)||!/^[A-Za-z0-9._-]{16,256}$/.test(accessSecret)))return null;
 const displayName=env.KFM_HOME_AI_DISPLAY_NAME??'Home PC model';
 if(!DISPLAY_NAME.test(displayName))return null;
 return Object.freeze({origin:url.origin,keyId,secret,profile,digest,displayName,access:accessId?Object.freeze({'cf-access-client-id':accessId,'cf-access-client-secret':accessSecret}):null});
}

async function boundedText(response,limit,signal){
 const reader=response.body?.getReader();if(!reader)return '';
 const chunks=[];let bytes=0;
 try{while(true){const part=await reader.read();if(part.done)break;bytes+=part.value.length;if(bytes>limit||signal?.aborted)throw error('HOME_AI_RESPONSE');chunks.push(Buffer.from(part.value));}}
 finally{await reader.cancel().catch(()=>{});}
 return Buffer.concat(chunks).toString('utf8');
}

export class HomeAiModel{
 constructor({config,fetchImpl=globalThis.fetch,clock=Date.now,healthMs=HOME_AI_HEALTH_MS,diagnostic=code=>console.warn('[KFM home AI] '+code)}){
  this.config=config;this.fetch=fetchImpl;this.clock=clock;this.diagnostic=diagnostic;
  this.provider=HOME_AI_PROVIDER;this.displayName=config.displayName;this.label='Home inference PC';
  this.online=true;this.reason='MODEL_LOADING';this.checkedAt=0;this.limits=null;this.pending=null;this.stopped=false;this.lastCode=null;
  this.check=null;void this.refresh();
  this.timer=setInterval(()=>void this.refresh(),healthMs);this.timer.unref?.();
 }
 get ready(){return !this.stopped&&this.reason===null&&this.clock()-this.checkedAt<=HOME_AI_STALE_MS;}
 note(code){if(code!==this.lastCode){this.lastCode=code;try{this.diagnostic(code);}catch{}}}
 async request(method,path,body,signal){
  const signed=signRequest({keyId:this.config.keyId,secret:this.config.secret,method,path,body,clock:this.clock});
  // Exact configured origin, no redirects, TLS verification left on. Credentials are never logged.
  const response=await this.fetch(this.config.origin+path,{method,redirect:'error',signal,headers:{...(this.config.access??{}),...signed.headers,...(body?{'content-type':'application/json'}:{})},body:body||undefined});
  const text=await boundedText(response,HOME_AI_MAX_RESPONSE_BYTES,signal);
  const signature=response.headers.get(HOME_AI_HEADERS.reply);
  // Unsigned replies come from the tunnel or Access edge (gateway down, policy denial).
  if(!signature)throw error([401,403].includes(response.status)?'HOME_AI_ACCESS_DENIED':'HOME_AI_UNREACHABLE');
  // A signed reply that is not bound to this request's nonce did not come from our gateway.
  if(!verifyReply(this.config.secret,signed.nonce,response.status,text,signature))throw error('HOME_AI_REPLY_UNVERIFIED');
  let value;try{value=JSON.parse(text);}catch{throw error('HOME_AI_RESPONSE');}
  if(!value||value.contract!==HOME_AI_CONTRACT)throw error('HOME_AI_RESPONSE');
  return {status:response.status,value};
 }
 refresh(){
  if(this.stopped)return Promise.resolve();
  return this.check??=(async()=>{
   try{
    const {status,value}=await this.request('GET',HOME_AI_PATHS.health,'',AbortSignal.timeout(10000));
    this.online=true;
    const profile=status===200&&Array.isArray(value.profiles)?value.profiles.find(p=>p?.id===this.config.profile):null;
    const valid=profile&&MODEL_TAG.test(profile.model??'')&&profile.digest===this.config.digest&&profile.installed===true&&Number.isInteger(profile.maxInputBytes)&&profile.maxInputBytes>=2048&&profile.maxInputBytes<=262144;
    if(!value.ollamaReachable)this.reason='HOME_AI_RUNTIME_UNAVAILABLE';
    else if(!valid)this.reason='HOME_AI_MODEL_IDENTITY';
    else{this.reason=null;this.limits={maxInputBytes:profile.maxInputBytes};this.label=profile.model+' · home PC (Ollama)';this.checkedAt=this.clock();}
    // Reachable but unable to run the pinned model is unavailable, not still loading.
    this.online=this.reason===null;
   }catch(failure){this.online=false;this.reason=['HOME_AI_ACCESS_DENIED','HOME_AI_REPLY_UNVERIFIED','HOME_AI_RESPONSE'].includes(failure?.code)?failure.code:'HOME_AI_UNREACHABLE';}
   this.note(this.reason??'HOME_AI_READY');
  })().finally(()=>{this.check=null;});
 }
 // Factual evidence selection stays held for every provider.
 select(){return Promise.reject(error('MODEL_UNAVAILABLE'));}
 async discuss(question,{style='plain',depth='brief',history=[],context=''}={},signal){
  if(!this.ready)throw error('MODEL_UNAVAILABLE');
  if(this.pending)throw error('MODEL_BUSY');
  if(signal?.aborted)throw error('MODEL_CANCELLED');
  const system=discussionSystem({profile:'context-aware-v2',style,depth,hasContext:Boolean(context)});
  const last={role:'user',content:(context?'Display context (untrusted data): '+context+'\n\n':'')+question};
  const retained=history.slice();let contextTrimmed=false;
  const messages=()=>[{role:'system',content:system},...retained.flatMap(item=>[{role:'user',content:item.question},{role:'assistant',content:item.reply}]),last];
  // The gateway refuses oversized input; drop the oldest turns first, never the question.
  while(messageBytes(messages())>this.limits.maxInputBytes&&retained.length){retained.shift();contextTrimmed=true;}
  if(messageBytes(messages())>this.limits.maxInputBytes)throw error('MODEL_CONTEXT_LIMIT');
  const body=JSON.stringify({profile:this.config.profile,depth,messages:messages()});
  this.pending=true;
  try{
   const {status,value}=await this.request('POST',HOME_AI_PATHS.discuss,body,signal?AbortSignal.any([signal,AbortSignal.timeout(HOME_AI_REQUEST_MS)]):AbortSignal.timeout(HOME_AI_REQUEST_MS));
   if(status===413&&value.reasonCode==='CONTEXT_LIMIT')throw error('MODEL_CONTEXT_LIMIT');
   if(status!==200){if(['MODEL_IDENTITY','MODEL_NOT_INSTALLED','OLLAMA_UNREACHABLE'].includes(value.reasonCode))void this.refresh();throw error(status===429?'MODEL_BUSY':'MODEL_UNAVAILABLE');}
   // The reply must name the pinned profile and digest; anything else is a substituted model.
   if(value.profile!==this.config.profile||value.digest!==this.config.digest||typeof value.text!=='string'||!HOME_AI_FINISH_REASONS.includes(value.finishReason)){this.reason='HOME_AI_MODEL_IDENTITY';this.note(this.reason);throw error('MODEL_UNAVAILABLE');}
   // The handler appends a continuation to the earlier partial reply; keep a word boundary.
   const text=question===CONTINUE_REPLY&&/^\S/.test(value.text)&&/\S$/.test(history.at(-1)?.reply??'')?' '+value.text:value.text;
   return {text,contextTrimmed,outputLimited:value.finishReason!=='stop'};
  }catch(failure){
   if(signal?.aborted)throw error('MODEL_CANCELLED');
   if(['MODEL_CONTEXT_LIMIT','MODEL_BUSY','MODEL_UNAVAILABLE'].includes(failure.code))throw failure;
   if(['HOME_AI_REPLY_UNVERIFIED','HOME_AI_ACCESS_DENIED'].includes(failure.code))this.note(failure.code);
   void this.refresh();
   throw error('MODEL_UNAVAILABLE');
  }finally{this.pending=null;}
 }
 stop(){this.stopped=true;clearInterval(this.timer);}
}

let shared;
export function getHomeAiModel(config){return shared??=new HomeAiModel({config});}
