import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,writeFile,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {pathToFileURL} from 'node:url';
import {createQueryPool} from '../scripts/local-data/query-pool.mjs';

async function poolFixture(t,overrides={}){
 const dir=await mkdtemp(join(tmpdir(),'kfm-query-pool-')),file=join(dir,'child.mjs');
 await writeFile(file,`process.on('message',m=>{
  if(m.kind==='init'){process.send({ready:true});return;}
  if(m.operation.kind==='hang')Atomics.wait(new Int32Array(new SharedArrayBuffer(4)),0,0);
  process.send({id:m.id,value:{pid:process.pid,secretInherited:'KFM_TEST_PRIVATE_KEY' in process.env}});
 });`);
 const pool=createQueryPool({databases:{},childFile:pathToFileURL(file),limits:{processes:2,queued:4,executionMs:500,totalMs:4000,heapMiB:64,...overrides}});
 t.after(async()=>{await pool.close();await rm(dir,{recursive:true,force:true});});
 return pool;
}

test('native blocking work is killed within budget while another process answers, then the pool recovers',async t=>{
 const pool=await poolFixture(t);
 const warm=await Promise.all([pool.run({kind:'echo'}),pool.run({kind:'echo'})]);
 assert.ok(warm.every(x=>x.pid));assert.equal(pool.children,2);
 let timedOut=false;
 const blocked=pool.run({kind:'hang'}).catch(e=>{assert.equal(e.code,'QUERY_TIMEOUT');timedOut=true;});
 const fast=await pool.run({kind:'echo'});
 assert.equal(timedOut,false,'unrelated work finishes while the native call is still blocked');
 assert.ok(fast.pid);
 await blocked;
 const recovered=await pool.run({kind:'echo'});assert.ok(recovered.pid);
 assert.ok(pool.children<=2);
});

test('queue length is bounded and cancelling a queued request does not execute it',async t=>{
 const pool=await poolFixture(t,{processes:1,queued:1});
 await pool.run({kind:'echo'});
 const blocked=pool.run({kind:'hang'});const caught=assert.rejects(blocked,{code:'QUERY_TIMEOUT'});
 const abort=new AbortController(),queued=pool.run({kind:'hang'},{signal:abort.signal});
 await assert.rejects(pool.run({kind:'echo'}),{code:'QUERY_BUSY'});
 abort.abort();await assert.rejects(queued,{code:'QUERY_CANCELLED'});
 assert.equal(pool.queued,0);await caught;
 assert.ok((await pool.run({kind:'echo'})).pid);
});

test('query children receive no private environment and shutdown rejects work without leaving children',async t=>{
 const previous=process.env.KFM_TEST_PRIVATE_KEY;process.env.KFM_TEST_PRIVATE_KEY='fixture-private-value';
 t.after(()=>{if(previous===undefined)delete process.env.KFM_TEST_PRIVATE_KEY;else process.env.KFM_TEST_PRIVATE_KEY=previous;});
 const pool=await poolFixture(t);
 assert.equal((await pool.run({kind:'echo'})).secretInherited,false);
 const pending=pool.run({kind:'hang'}),rejected=assert.rejects(pending,{code:'DATABASE_UNAVAILABLE'});
 await pool.close();await rejected;assert.equal(pool.children,0);
 await assert.rejects(pool.run({kind:'echo'}),{code:'DATABASE_UNAVAILABLE'});
});

test('cancelling active native work kills its process and frees capacity',async t=>{
 const pool=await poolFixture(t,{processes:1});await pool.run({kind:'echo'});
 const abort=new AbortController(),pending=pool.run({kind:'hang'},{signal:abort.signal});
 abort.abort();await assert.rejects(pending,{code:'QUERY_CANCELLED'});
 assert.ok((await pool.run({kind:'echo'})).pid);
});

test('a child that cannot initialize fails queued work rather than repeatedly respawning',async t=>{
 const dir=await mkdtemp(join(tmpdir(),'kfm-query-init-')),file=join(dir,'broken.mjs');
 await writeFile(file,'process.exit(1);');
 const pool=createQueryPool({databases:{},childFile:pathToFileURL(file)});
 t.after(async()=>{await pool.close();await rm(dir,{recursive:true,force:true});});
 await assert.rejects(pool.run({kind:'health'}),{code:'DATABASE_UNAVAILABLE'});
 assert.equal(pool.children,0);assert.equal(pool.queued,0);
});
