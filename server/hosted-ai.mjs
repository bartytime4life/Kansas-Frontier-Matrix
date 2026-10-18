import {Worker} from 'node:worker_threads';
import {randomUUID} from 'node:crypto';
import {resolve} from 'node:path';
export const HOSTED_MODEL='SmolLM2-360M-Instruct q4 · server WebAssembly';
// Isolated qualification branch only; do not activate without hosted resource acceptance.
export const HOSTED_LIMITS=Object.freeze({loadMs:90000,inferenceMs:255000,maximumRssBytes:2048*1024*1024});
export const HOSTED_REPLY_LIMITS=Object.freeze({brief:Object.freeze({tokens:160,milliseconds:120000}),expanded:Object.freeze({tokens:384,milliseconds:240000})});
export const PUBLIC_AI_JOB_MS=270000;
// Three admitted discussions can wait for each other, but each run stays bounded.
export const PUBLIC_AI_MAX_LIFETIME_MS=3*PUBLIC_AI_JOB_MS;
export {CONTINUE_REPLY} from './hosted-ai-prompt.mjs';
const error=code=>Object.assign(new Error(code),{code});
const diagnosticCodes=new Set(['MODEL_UNAVAILABLE','MODEL_LOAD_TIMEOUT','MODEL_MEMORY_LIMIT','MODEL_TIMEOUT','HOSTED_MODEL_FAILED','HOSTED_MODEL_FILES_UNSAFE','HOSTED_MODEL_IDENTITY','HOSTED_MODEL_INTEGRITY','HOSTED_MODEL_CONFIG','HOSTED_MODEL_INPUTS','HOSTED_MODEL_SELF_CHECK','HOSTED_PROFILE_IDENTITY','MODULE_NOT_FOUND','ERR_MODULE_NOT_FOUND','ENOENT','EACCES','ENOMEM','ERR_WORKER_OUT_OF_MEMORY']);
export class HostedAiModel{
 constructor({discussionProfile='concise-sampled-v1',modelDirectory='/private/kfm-embedded-smollm2-360m-q4-wasm-20261016/model',workerFactory=(path,options)=>new Worker(path,options),memoryUsage=process.memoryUsage,diagnostic=code=>console.warn('[KFM hosted AI] '+code)}={}){
  this.diagnostic=diagnostic;
  this.ready=false;this.online=true;this.reason='MODEL_LOADING';this.peakRssBytes=memoryUsage().rss;this.pending=null;this.stopped=false;
  this.worker=workerFactory(resolve('server/hosted-ai-worker.mjs'),{workerData:{modelDirectory,discussionProfile},execArgv:process.execArgv.filter(x=>!x.startsWith('--input-type=')),resourceLimits:{maxOldGenerationSizeMb:256}});
  this.loaded=new Promise((resolveReady,rejectReady)=>{this.resolveReady=resolveReady;this.rejectReady=rejectReady;});
  this.loaded.catch(()=>{});
  this.loadTimer=setTimeout(()=>this.stop('MODEL_LOAD_TIMEOUT'),HOSTED_LIMITS.loadMs);this.loadTimer.unref?.();
  this.monitor=setInterval(()=>{this.peakRssBytes=Math.max(this.peakRssBytes,memoryUsage().rss);if(this.peakRssBytes>HOSTED_LIMITS.maximumRssBytes)this.stop('MODEL_MEMORY_LIMIT');},100);this.monitor.unref?.();
  this.worker.on('message',message=>{
   if(message?.type==='ready'&&!this.stopped){clearTimeout(this.loadTimer);this.ready=true;this.reason=null;this.resolveReady();}
   if(message?.type==='failed')this.stop('MODEL_UNAVAILABLE',message.reason);
   if(message?.type==='result'&&this.pending?.id===message.id){
    const pending=this.pending;this.pending=null;pending.cleanup();
    if(pending.signal?.aborted)pending.reject(error('MODEL_CANCELLED'));
    else if(message.error)pending.reject(error(['MODEL_CONTEXT_LIMIT','MODEL_CANCELLED'].includes(message.error)?message.error:'MODEL_UNAVAILABLE'));
    else pending.resolve(pending.kind==='discuss'?{text:message.discussion,contextTrimmed:Boolean(message.contextTrimmed),outputLimited:message.finishReason?message.finishReason!=='stop':Boolean(message.outputLimited)}:message.selection);
   }
  });
  this.worker.once('error',failure=>this.stop('MODEL_UNAVAILABLE',failure?.code));this.worker.once('exit',()=>this.stop('MODEL_UNAVAILABLE'));
 }
 select(question,facts,signal){return this.call('select',{question,facts},signal);}
 discuss(question,{style='plain',depth='brief',history=[],context=''}={},signal){return this.call('discuss',{question,style,depth,history,context},signal);}
 call(kind,payload,signal){
  if(!this.ready||this.stopped)return Promise.reject(error('MODEL_UNAVAILABLE'));
  if(this.pending)return Promise.reject(error('MODEL_BUSY'));
  if(signal?.aborted)return Promise.reject(error('MODEL_CANCELLED'));
  return new Promise((resolveResult,reject)=>{
   const id=randomUUID(),cancel=new SharedArrayBuffer(4),abort=()=>Atomics.store(new Int32Array(cancel),0,1);
   const timer=setTimeout(()=>this.stop('MODEL_TIMEOUT'),HOSTED_LIMITS.inferenceMs);
   const cleanup=()=>{clearTimeout(timer);signal?.removeEventListener('abort',abort);};
   this.pending={id,kind,resolve:resolveResult,reject,signal,cleanup};signal?.addEventListener('abort',abort,{once:true});
   this.worker.postMessage({type:kind,id,...payload,cancel});
  });
 }
 stop(reason,detail){
  const intentional=reason===undefined;reason??='MODEL_UNAVAILABLE';
  if(this.stopped)return;this.stopped=true;this.ready=false;this.online=false;this.reason=reason;
  clearTimeout(this.loadTimer);clearInterval(this.monitor);this.rejectReady(error(reason));
  if(this.pending){const p=this.pending;this.pending=null;p.cleanup();p.reject(error(reason));}
  // Operator logs receive fixed codes only, never messages, paths, prompts or stacks.
  if(!intentional)try{this.diagnostic((diagnosticCodes.has(reason)?reason:'MODEL_UNAVAILABLE')+(diagnosticCodes.has(detail)?':'+detail:''));}catch{}
  void this.worker.terminate();
 }
}

let shared;
export function getHostedAiModel(){return shared??=new HostedAiModel();}

export function hasRepeatedPhrase(value){
 const words=value.toLowerCase().match(/[a-z0-9]+/g)??[],counts=new Map();
 for(let i=0;i+3<words.length;i++){const phrase=words.slice(i,i+4).join(' '),n=(counts.get(phrase)??0)+1;if(n>=3)return true;counts.set(phrase,n);}
 return false;
}

// A continuation that mostly copies its preceding reply is not new progress.
// Compare phrases, not shared subject words; short answers are excluded.
export function repeatsPriorReply(value,prior){
 const words=text=>(text??'').toLowerCase().match(/[\p{L}\p{N}]+/gu)??[];
 const current=words(value),previous=words(prior);
 if(current.length<24||previous.length<24)return false;
 // A complete leading replay is still repetition when appended text dilutes
 // the phrase-overlap percentage. Partial shared introductions remain allowed.
 if(previous.every((word,index)=>current[index]===word))return true;
 const phrases=new Set();for(let i=0;i+3<previous.length;i++)phrases.add(previous.slice(i,i+4).join(' '));
 let matches=0;for(let i=0;i+3<current.length;i++)if(phrases.has(current.slice(i,i+4).join(' ')))matches++;
 return matches/(current.length-3)>=0.75;
}

