import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { setTimeout as delay } from 'node:timers/promises';
import { PcAiStore, token, digest } from '../server/pc-ai-store.mjs';
import { createPcAiHandler } from '../server/pc-ai-handler.mjs';

test('unknown-name floods cannot consume real-account budgets; failures stay generic', async () => {
  const root=await mkdtemp(join(tmpdir(),'kfm-login-admission-'));
  let now=1700000000000;
  const store=new PcAiStore({root,role:'test',key:token(),clock:()=>now,failureDelay:0});
  try {
    for(const name of ['alice','bravo']) {
      const invite=store.invite(name);
      await store.authenticate(name,'synthetic-test-password-123',invite.invitation);
    }
    const origin='https://kansasfrontiermatrix.com';
    const handler=createPcAiHandler({store,origin,adminHash:digest(token()),workerHash:digest(token()),resolveEvidence:async()=>null});
    const request=async(username,password='synthetic-wrong-password-123')=>{
      const response=await handler(new Request(origin+'/api/pc-ai/sign-in',{method:'POST',headers:{Origin:origin,'Content-Type':'application/json','X-Forwarded-For':token(),'CF-Connecting-IP':'203.0.113.7'},body:JSON.stringify({username,password})}));
      return {status:response.status,body:await response.json()};
    };
    const flood=Promise.all(Array.from({length:50},(_,i)=>request('unknown'+i)));
    assert.equal((await request('alice','synthetic-test-password-123')).status,200);
    const failures=await flood;
    assert.ok(failures.every(x=>x.status===401&&x.body.reasonCode==='SIGN_IN_DENIED'));
    assert.equal(store.db.prepare("SELECT COUNT(*) AS n FROM attempts WHERE username='@unknown'").get().n,30);
    for(let i=0;i<8;i++)assert.deepEqual(await request('alice'),failures[0]);
    assert.equal(store.db.prepare("SELECT COUNT(*) AS n FROM attempts WHERE username='alice'").get().n,5);
    assert.equal((await request('bravo','synthetic-test-password-123')).status,200);
    now+=900001;
    assert.equal((await request('alice','synthetic-test-password-123')).status,200);
  }finally{store.close();await rm(root,{recursive:true,force:true});}
});

test('hash work is asynchronous and independently bounded for unknown and real accounts',async()=>{
  const root=await mkdtemp(join(tmpdir(),'kfm-login-concurrency-'));
  const active={account:0,unknown:0},maximum={account:0,unknown:0};
  let work=0;
  const derive=async(_password,salt)=>{
    const kind=salt==='kfm-pc-dummy-salt'?'unknown':'account';
    active[kind]++;maximum[kind]=Math.max(maximum[kind],active[kind]);work++;
    await delay(10);active[kind]--;return Buffer.alloc(32);
  };
  const store=new PcAiStore({root,role:'test',key:token(),derive,failureDelay:0});
  try{
    for(const name of ['alice','bravo','charlie']){
      const invite=store.invite(name);await store.authenticate(name,'synthetic-test-password-123',invite.invitation);
    }
    let timerRan=false;setTimeout(()=>{timerRan=true;},0);
    const flood=Array.from({length:40},(_,i)=>store.authenticate('missing'+i,'synthetic-test-password-123').catch(e=>e.message));
    const signed=await Promise.all(['alice','bravo','charlie'].map(name=>store.authenticate(name,'synthetic-test-password-123')));
    assert.equal(signed.length,3);await Promise.all(flood);
    assert.equal(timerRan,true);
    assert.ok(maximum.unknown<=1&&maximum.account<=2);
    assert.ok(work<=36); // 3 activations + <=30 dummy hashes + 3 real sign-ins.
  }finally{store.close();await rm(root,{recursive:true,force:true});}
});

test('revocation during asynchronous password verification cannot create a session',async()=>{
  const root=await mkdtemp(join(tmpdir(),'kfm-login-revoke-'));
  let held=false,release;
  const derive=async()=>{if(held)await new Promise(resolve=>{release=resolve;});return Buffer.alloc(32);};
  const store=new PcAiStore({root,role:'test',key:token(),derive,failureDelay:0});
  try{
    const invite=store.invite('alice');await store.authenticate('alice','synthetic-test-password-123',invite.invitation);
    held=true;
    const signing=store.authenticate('alice','synthetic-test-password-123');
    await new Promise(resolve=>setImmediate(resolve));
    store.revoke('alice');release();
    await assert.rejects(signing,/SIGN_IN_DENIED/);
    assert.equal(store.db.prepare('SELECT COUNT(*) AS n FROM sessions').get().n,0);
  }finally{store.close();await rm(root,{recursive:true,force:true});}
});
