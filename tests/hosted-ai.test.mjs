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
test('operator diagnostics retain fixed startup codes without exposing worker secrets or changing denial',async()=>{
 for(const detail of ['HOSTED_MODEL_SELF_CHECK','ERR_MODULE_NOT_FOUND','SECRET_TOKEN /private/model user question']){
  const w=worker(),codes=[],model=new HostedAiModel({workerFactory:()=>w,memoryUsage:()=>({rss:10}),diagnostic:code=>codes.push(code)});
  w.emit('message',{type:'failed',reason:detail});
  await assert.rejects(model.loaded,/MODEL_UNAVAILABLE/);w.emit('exit',1);
  assert.deepEqual(codes,[detail.startsWith('SECRET')?'MODEL_UNAVAILABLE':'MODEL_UNAVAILABLE:'+detail]);
  assert.equal(w.terminated,true);assert.equal(model.online,false);assert.equal(model.reason,'MODEL_UNAVAILABLE');
  await assert.rejects(model.discuss('no inference'),/MODEL_UNAVAILABLE/);
 }
 const w=worker(),model=new HostedAiModel({workerFactory:()=>w,memoryUsage:()=>({rss:10}),diagnostic:()=>{throw Error('log failure');}});
 w.emit('error',Object.assign(new Error('secret path or stack'),{code:'ENOENT'}));
 await assert.rejects(model.loaded,/MODEL_UNAVAILABLE/);assert.equal(w.terminated,true);
});
test('successful qualification cleanup does not report an outage',async()=>{
 const w=worker(),codes=[],model=new HostedAiModel({workerFactory:()=>w,memoryUsage:()=>({rss:10}),diagnostic:code=>codes.push(code)});
 w.emit('message',{type:'ready'});await model.loaded;
 model.stop();w.emit('exit',0);
 assert.deepEqual(codes,[]);assert.equal(model.ready,false);assert.equal(w.terminated,true);
 await assert.rejects(model.discuss('after cleanup'),/MODEL_UNAVAILABLE/);
});
