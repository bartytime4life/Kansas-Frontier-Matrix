import {Worker} from 'node:worker_threads';
import {randomUUID} from 'node:crypto';
import {resolve} from 'node:path';
export const HOSTED_MODEL='SmolLM2-135M-Instruct · server WebAssembly';
export const HOSTED_LIMITS=Object.freeze({loadMs:90000,inferenceMs:30000,maximumRssBytes:1200*1024*1024});
const error=code=>Object.assign(new Error(code),{code});
export class HostedAiModel{
 constructor({modelDirectory='/private/kfm-embedded-smollm2-wasm-20261016/model',workerFactory=(path,options)=>new Worker(path,options),memoryUsage=process.memoryUsage}={}){
  this.ready=false;this.online=true;this.reason='MODEL_LOADING';this.peakRssBytes=memoryUsage().rss;this.pending=null;this.stopped=false;
  this.worker=workerFactory(resolve('server/hosted-ai-worker.mjs'),{workerData:{modelDirectory},execArgv:process.execArgv.filter(x=>!x.startsWith('--input-type=')),resourceLimits:{maxOldGenerationSizeMb:256}});
  this.loaded=new Promise((resolveReady,rejectReady)=>{this.resolveReady=resolveReady;this.rejectReady=rejectReady;});
  this.loaded.catch(()=>{});
  this.loadTimer=setTimeout(()=>this.stop('MODEL_LOAD_TIMEOUT'),HOSTED_LIMITS.loadMs);this.loadTimer.unref?.();
  this.monitor=setInterval(()=>{this.peakRssBytes=Math.max(this.peakRssBytes,memoryUsage().rss);if(this.peakRssBytes>HOSTED_LIMITS.maximumRssBytes)this.stop('MODEL_MEMORY_LIMIT');},100);this.monitor.unref?.();
  this.worker.on('message',message=>{
   if(message?.type==='ready'&&!this.stopped){clearTimeout(this.loadTimer);this.ready=true;this.reason=null;this.resolveReady();}
   if(message?.type==='failed')this.stop('MODEL_UNAVAILABLE');
   if(message?.type==='result'&&this.pending?.id===message.id){
    const pending=this.pending;this.pending=null;pending.cleanup();
    if(pending.signal?.aborted)pending.reject(error('MODEL_CANCELLED'));
    else if(message.error)pending.reject(error(['MODEL_CONTEXT_LIMIT','MODEL_CANCELLED'].includes(message.error)?message.error:'MODEL_UNAVAILABLE'));
    else pending.resolve(pending.kind==='discuss'?{text:message.discussion,contextTrimmed:Boolean(message.contextTrimmed),outputLimited:Boolean(message.outputLimited)}:message.selection);
   }
  });
  this.worker.once('error',()=>this.stop('MODEL_UNAVAILABLE'));this.worker.once('exit',()=>this.stop('MODEL_UNAVAILABLE'));
 }
 select(question,facts,signal){return this.call('select',{question,facts},signal);}
 discuss(question,{style='plain',depth='brief',history=[]}={},signal){return this.call('discuss',{question,style,depth,history},signal);}
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
 stop(reason='MODEL_UNAVAILABLE'){
  if(this.stopped)return;this.stopped=true;this.ready=false;this.online=false;this.reason=reason;
  clearTimeout(this.loadTimer);clearInterval(this.monitor);this.rejectReady(error(reason));
  if(this.pending){const p=this.pending;this.pending=null;p.cleanup();p.reject(error(reason));}
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
