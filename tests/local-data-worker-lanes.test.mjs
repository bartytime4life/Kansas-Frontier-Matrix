import test from 'node:test';
import assert from 'node:assert/strict';
import {runLocalDataWorkers,LOCAL_DATA_WORKER_LANES} from '../scripts/local-data/worker.mjs';

test('data-only relay starts two independent bounded lanes and aborts both together',async()=>{
 const stop=new AbortController(),lanes=[];let started;
 const ready=new Promise(resolve=>{started=resolve;});
 const running=runLocalDataWorkers({site:'https://kansasfrontiermatrix.com'},stop.signal,()=>({run:signal=>new Promise(resolve=>{lanes.push(signal);if(lanes.length===2)started();signal.addEventListener('abort',resolve,{once:true});})}));
 await ready;assert.equal(LOCAL_DATA_WORKER_LANES,2);assert.equal(lanes.length,2);assert.ok(lanes.every(signal=>!signal.aborted));stop.abort();await running;assert.ok(lanes.every(signal=>signal.aborted));
});

test('a failed lane cancels its peer instead of leaving a detached long poll',async()=>{
 let peer;let fail;
 const broken=new Promise((_,reject)=>{fail=reject;});let n=0;
 const running=runLocalDataWorkers({},undefined,()=>({run:signal=>++n===1?broken:new Promise(resolve=>{peer=signal;signal.addEventListener('abort',resolve,{once:true});})}));
 fail(Error('fixed test failure'));await assert.rejects(running,/fixed test failure/);assert.equal(peer.aborted,true);
});
