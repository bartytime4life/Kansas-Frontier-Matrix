import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
const js=ts.transpileModule(await readFile('app/dem-request-pool.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const m=await import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
const png=()=>Uint8Array.of(137,80,78,71,13,10,26,10,1,2,3,4);
const response=(headers={})=>new Response(png(),{headers:{'content-type':'image/png','cache-control':'public, max-age=900',...headers}});
const signal=()=>new AbortController();
const tick=()=>new Promise(resolve=>setImmediate(resolve));

test('DEM transport accepts only the fixed same-origin endpoint and canonicalizes coordinate order',()=>{
 const origin='https://kfm.test',good='/api/3dep-dem-tile?v=2&z=13&x=1900&y=3120';
 assert.equal(m.queuedDemUrl(good,origin),origin+good);
 assert.equal(m.queuedDemUrl('/api/3dep-dem-tile?x=1900&z=13&y=3120&v=2',origin),origin+good);
 for(const url of ['https://other.test'+good,good+'&token=private',good+'&z=13',good+'#x',good.replace('z=13','z=18'),good.replace('x=1900','x=-1'),good.replace('x=1900','x=9000'),good.replace('v=2','v=1'),'/api/other?v=2&z=13&x=1900&y=3120'])assert.equal(m.queuedDemUrl(url,origin),null,url);
});
test('two distinct reads coalesce consumers and discard abandoned queued zoom levels before network',async()=>{
 const calls=[],finish=new Map();const pool=m.createDemRequestPool(url=>{calls.push(url);return new Promise(resolve=>finish.set(url,resolve));});
 const a=signal(),b=signal(),old=signal(),latest=signal();
 const first=pool('a',a.signal),same=pool('a',b.signal),second=pool('b',signal().signal),abandoned=pool('old',old.signal).catch(e=>e),fresh=pool('new',latest.signal);
 assert.deepEqual(calls,['a','b']);old.abort();assert.equal((await abandoned).name,'AbortError');
 finish.get('a')(response());const [one,two]=await Promise.all([first,same]);await tick();assert.deepEqual(calls,['a','b','new']);assert.notEqual(one.data,two.data);assert.deepEqual([...new Uint8Array(one.data)],[...new Uint8Array(two.data)]);
 finish.get('b')(response());finish.get('new')(response());await Promise.all([second,fresh]);assert.equal(calls.includes('old'),false);
});
test('aborting every running consumer retains the slot until upstream finishes and later reuses immutable cached bytes',async()=>{
 let count=0;const finish=[];const pool=m.createDemRequestPool(()=>{count++;return new Promise(resolve=>finish.push(resolve));});
 const a=signal(),b=signal();const pa=pool('a',a.signal).catch(e=>e),pb=pool('b',b.signal).catch(e=>e),next=pool('c',signal().signal);
 a.abort();b.abort();assert.equal((await pa).name,'AbortError');assert.equal((await pb).name,'AbortError');assert.equal(count,2,'client cancellation cannot produce another server orphan');
 finish[0](response());await tick();assert.equal(count,3);finish[1](response());finish[2](response());await next;
 const cached=await pool('a',signal().signal);structuredClone(cached.data,{transfer:[cached.data]});const again=await pool('a',signal().signal);assert.equal(again.data.byteLength,png().byteLength);assert.equal(count,3);
});
test('volatile bytes expire without renewing source TTL or caching private/malformed/error responses',async()=>{
 let now=1000,calls=0;const pool=m.createDemRequestPool(async()=>{calls++;return response({'cache-control':'public, max-age=60',age:'10'});},()=>now);
 await pool('a',signal().signal);now+=20000;const hit=await pool('a',signal().signal);assert.equal(hit.cacheControl,'public, max-age=30');assert.equal(calls,1);
 now+=30001;await pool('a',signal().signal);assert.equal(calls,2);
 for(const headers of [{'cache-control':'no-store'},{'cache-control':'private, max-age=900'},{'cache-control':'public, max-age=900, no-cache'}]){
  let reads=0;const uncached=m.createDemRequestPool(async()=>{reads++;return response(headers);});await uncached('a',signal().signal);await uncached('a',signal().signal);assert.equal(reads,2);
 }
 const bad=m.createDemRequestPool(async()=>new Response('no',{status:503}));await assert.rejects(bad('a',signal().signal),e=>e.status===503);await assert.rejects(bad('a',signal().signal),e=>e.status===503,'a failed completion cannot strand new waiters');
 const invalid=m.createDemRequestPool(async()=>new Response('<html>',{headers:{'content-type':'image/png'}}));await assert.rejects(invalid('a',signal().signal),/encoding/);
 const oversized=m.createDemRequestPool(async()=>response({'content-length':String(512*1024+1)}));await assert.rejects(oversized('a',signal().signal),/response/);
});
test('memory cache is capped at twelve entries and cancelled requests do no work',async()=>{
 let calls=0;const pool=m.createDemRequestPool(async()=>{calls++;return response();});const stopped=signal();stopped.abort();await assert.rejects(pool('stopped',stopped.signal),{name:'AbortError'});assert.equal(calls,0);
 for(let n=0;n<13;n++)await pool(String(n),signal().signal);await pool('0',signal().signal);assert.equal(calls,14);
});

test('Date on an HTTP-cached response cannot restart the source cache lifetime',async()=>{
 const now=Date.parse('2026-11-25T18:05:00Z');let calls=0;
 const pool=m.createDemRequestPool(async()=>{calls++;return response({'cache-control':'public, max-age=60',date:'Wed, 25 Nov 2026 18:00:00 GMT'});},()=>now);
 const result=await pool('a',signal().signal);assert.equal(result.cacheControl,'public, max-age=0');await pool('a',signal().signal);assert.equal(calls,2);
});
test('the queue is capped and cancelled backlog never starts upstream work',async()=>{
 let calls=0;const finish=[];const pool=m.createDemRequestPool(()=>{calls++;return new Promise(resolve=>finish.push(resolve));});
 const controllers=Array.from({length:64},signal),pending=controllers.map((c,i)=>pool(String(i),c.signal).catch(e=>e));
 await assert.rejects(pool('over',signal().signal),/queue is full/);assert.equal(calls,2);
 controllers.forEach(c=>c.abort());assert.ok((await Promise.all(pending)).every(e=>e.name==='AbortError'));finish.forEach(done=>done(response()));await tick();assert.equal(calls,2);
});
test('volatile byte budget evicts before two MiB regardless of entry count',async()=>{
 let calls=0;const bytes=new Uint8Array(320000);bytes.set(png());
 const pool=m.createDemRequestPool(async()=>{calls++;return new Response(bytes,{headers:{'content-type':'image/png','cache-control':'public, max-age=900'}});});
 for(let i=0;i<7;i++)await pool(String(i),signal().signal);await pool('0',signal().signal);assert.equal(calls,8);
});
