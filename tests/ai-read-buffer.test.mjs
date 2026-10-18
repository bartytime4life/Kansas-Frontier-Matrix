import test from 'node:test';
import assert from 'node:assert/strict';
import {createAiReadBuffer,AI_READ_LIMITS,isAiReadPressure} from '../server/ai-read-buffer.mjs';
const turn=()=>new Promise(resolve=>setImmediate(resolve));
const busy=error=>isAiReadPressure(error)&&error.message==='AI_READ_BUSY';

test('source buffer has a fixed active/waiting bound and drains in order',async()=>{
 const buffer=createAiReadBuffer(),release=[],started=[];let active=0,peak=0;
 const tasks=Array.from({length:10},(_,id)=>buffer.run(async()=>{started.push(id);peak=Math.max(peak,++active);await new Promise(resolve=>release.push(resolve));active--;return id;}));
 await turn();assert.deepEqual(started,[0,1]);
 await assert.rejects(buffer.run(()=>assert.fail('overflow work must not run')),busy);
 for(let i=0;i<5;i++){release.splice(0).forEach(resolve=>resolve());await turn();}
 assert.deepEqual(await Promise.all(tasks),[0,1,2,3,4,5,6,7,8,9]);
 assert.equal(peak,AI_READ_LIMITS.active);assert.deepEqual(started,[0,1,2,3,4,5,6,7,8,9]);
 assert.equal(await buffer.run(()=>42),42);
});

test('abandoned callers retain actual work capacity and expired queued work never runs',async()=>{
 const buffer=createAiReadBuffer(),release=[];
 const active=[0,1].map(()=>buffer.run(()=>new Promise(resolve=>release.push(resolve))));
 await turn();assert.equal(await Promise.race([active[0],Promise.resolve('caller timeout')]),'caller timeout');
 let queuedCalls=0;const waiting=Array.from({length:AI_READ_LIMITS.waiting},()=>assert.rejects(buffer.run(()=>{queuedCalls++;}),busy));
 await assert.rejects(buffer.run(()=>assert.fail('real slots must remain occupied')),busy);
 await Promise.all(waiting);assert.equal(queuedCalls,0);
 release.forEach(resolve=>resolve());await Promise.all(active);
 assert.equal(await buffer.run(()=>7),7);assert.equal(queuedCalls,0);
});

test('guest and process read quotas recover without resetting job admission',()=>{
 let now=100000;const buffer=createAiReadBuffer({clock:()=>now}),guests=Array.from({length:6},()=>({}));
 for(let g=0;g<5;g++)for(let i=0;i<AI_READ_LIMITS.guestReads;i++)buffer.admit(guests[g])();
 assert.throws(()=>buffer.admit(guests[0]),error=>isAiReadPressure(error)&&error.message==='AI_READ_RATE_LIMIT'&&error.retryAfter===60);
 assert.throws(()=>buffer.admit(guests[5]),error=>error.message==='AI_READ_RATE_LIMIT');
 now+=60000;buffer.admit(guests[0])();buffer.admit(guests[5])();
});

test('pending response caps cover coalesced waiters and release is idempotent',()=>{
 const buffer=createAiReadBuffer(),guests=Array.from({length:6},()=>({})),release=[];
 release.push(buffer.admit(guests[0]),buffer.admit(guests[0]));
 assert.throws(()=>buffer.admit(guests[0]),busy);
 for(let g=1;g<5;g++)release.push(buffer.admit(guests[g]),buffer.admit(guests[g]));
 assert.throws(()=>buffer.admit(guests[5]),busy);
 release[0]();release[0]();const next=buffer.admit(guests[5]);
 assert.throws(()=>buffer.admit(guests[5]),busy);
 release.forEach(done=>done());next();buffer.admit(guests[5])();
 assert.equal(isAiReadPressure(new Error('AI_READ_BUSY')),false);
});
