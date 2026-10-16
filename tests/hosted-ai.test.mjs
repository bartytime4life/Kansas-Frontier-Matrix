import test from 'node:test';
import assert from 'node:assert/strict';
import {EventEmitter} from 'node:events';
import {HostedAiModel} from '../server/hosted-ai.mjs';
function worker(){const w=new EventEmitter();w.terminate=async()=>{w.terminated=true;};w.postMessage=message=>{w.sent=message;};return w;}
test('guest inference uses one worker and propagates cancellation without accepting a late answer',async()=>{
 const w=worker(),model=new HostedAiModel({workerFactory:()=>w,memoryUsage:()=>({rss:10})});
 try{
  w.emit('message',{type:'ready'});await model.loaded;const controller=new AbortController(),result=model.discuss('question',{style:'plain',depth:'brief',history:[]},controller.signal);
  await assert.rejects(model.select('other',['fact']),/MODEL_BUSY/);
  controller.abort();assert.equal(Atomics.load(new Int32Array(w.sent.cancel),0),1);
  w.emit('message',{type:'result',id:w.sent.id,selection:1});await assert.rejects(result,/MODEL_CANCELLED/);
  const next=model.select('next',['fact']);w.emit('message',{type:'result',id:w.sent.id,selection:1});assert.equal(await next,1);
 }finally{model.stop();}
 assert.equal(w.terminated,true);
});
test('worker failure and sampled memory excess hold the model without retry',async()=>{
 const w=worker(),model=new HostedAiModel({workerFactory:()=>w,memoryUsage:()=>({rss:3_000_000_000})});
 await Promise.all([assert.rejects(model.loaded,/MODEL_MEMORY_LIMIT/),new Promise(resolve=>setTimeout(resolve,120))]);assert.equal(model.ready,false);assert.equal(w.terminated,true);
 await assert.rejects(model.select('question',['fact']),/MODEL_UNAVAILABLE/);
});
