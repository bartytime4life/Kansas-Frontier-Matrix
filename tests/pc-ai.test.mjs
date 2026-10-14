import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, readFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { PcAiStore, token, digest } from '../server/pc-ai-store.mjs';
import { createPcAiHandler, validatePcResult, pcAiRuntime } from '../server/pc-ai-handler.mjs';
import { interpretPacket, createWorker, boundedJson } from '../scripts/pc-ai-worker.mjs';
import { QWEN_LOCAL_MODEL, QWEN_LOCAL_MODEL_DIGEST } from '../scripts/qwen-local-contract.mjs';
const origin='https://kansasfrontiermatrix.com';
const fixtureEvidence={releaseId:'sha256:'+'a'.repeat(64),evidence:[{evidenceRef:'kfm:fixture:fact',text:'Synthetic fixture: the historical record is dated 1900.',status:'documented',title:'Synthetic evidence fixture',url:origin+'/knowledge/record?id=fixture'}],truncated:false};
const question={question:'What year is this record?',term:'historical',place:'',start:'',end:''};
const health={ready:true,model:QWEN_LOCAL_MODEL,digest:QWEN_LOCAL_MODEL_DIGEST,version:'0.35.1'};
const result={outcome:'ANSWER',claims:[{evidenceRef:'kfm:fixture:fact',text:fixtureEvidence.evidence[0].text}],interpretation:'This synthetic record supplies a historical date; it does not establish current conditions.'};
async function fixture(){
  const root=await mkdtemp(join(tmpdir(),'kfm-pc-ai-'));let now=1700000000000;
  const key=token(),admin=token(),worker=token();
  const store=new PcAiStore({root,role:'test',key,clock:()=>now});let evidence=structuredClone(fixtureEvidence);
  const handler=createPcAiHandler({store,origin,adminHash:digest(admin),workerHash:digest(worker),resolveEvidence:async()=>evidence});
  const request=async(path,body,credential,cookie,requestOrigin=origin)=>{
    const headers={...(body!==undefined?{'Content-Type':'application/json',Origin:requestOrigin}:{}),...(credential?{Authorization:'Bearer '+credential}:{}),...(cookie?{Cookie:cookie}:{})};
    const response=await handler(new Request(origin+'/api/pc-ai/'+path,{method:body===undefined?'GET':'POST',headers,body:body===undefined?undefined:JSON.stringify(body)}));
    return {response,body:await response.json()};
  };
  const signed=async(username)=>{
    const invited=await request('admin/invite',{username},admin);
    assert.equal(invited.response.status,201);
    const sign=await request('activate',{username,invitation:invited.body.invitation,password:'synthetic-test-password-123'});
    assert.equal(sign.response.status,200);
    return sign.response.headers.get('set-cookie').split(';')[0];
  };
  return {root,key,store,request,signed,admin,worker,setEvidence:value=>{evidence=value;},advance:ms=>{now+=ms;},close:async function(){this.store.close();await rm(root,{recursive:true,force:true});}};
}

test('invitation is one-use; password hashes and host cookies; sessions persist and revoke',async()=>{
  const f=await fixture();try{
    const invite=await f.request('admin/invite',{username:'alice'},f.admin);
    const body={username:'alice',invitation:invite.body.invitation,password:'synthetic-test-password-123'};
    const activated=await f.request('activate',body);
    const setCookie=activated.response.headers.get('set-cookie');
    assert.match(setCookie,/HttpOnly; Secure; SameSite=Strict/);
    assert.equal((await f.request('activate',body)).response.status,401);
    const cookie=setCookie.split(';')[0];
    assert.equal((await f.request('status',undefined,null,cookie)).body.account,'alice');
    f.store.close();f.store=new PcAiStore({root:f.root,role:'test',key:f.key});
    assert.ok(f.store.account(cookie.slice('__Host-kfm_pc_session='.length))===null); // synthetic clock session is expired in real time
    const db=await readFile(join(f.root,'kfm-pc-ai-v1','test','accounts-jobs.sqlite'));
    assert.equal(db.includes(Buffer.from(body.password)),false);
    f.store.close();f.store=new PcAiStore({root:f.root,role:'test',key:f.key,clock:()=>1700000000000});
    assert.equal(f.store.account(cookie.slice('__Host-kfm_pc_session='.length)).username,'alice');
    f.store.revoke('alice');assert.equal(f.store.account(cookie.slice('__Host-kfm_pc_session='.length)),null);
  }finally{await f.close();}
});
test('anonymous, forged-role, wrong-origin and worker-to-admin requests are denied',async()=>{
  const f=await fixture();try{
    assert.equal((await f.request('jobs',question)).response.status,401);
    assert.equal((await f.request('admin/invite',{username:'alice'},f.worker)).response.status,401);
    assert.equal((await f.request('worker/heartbeat',health,f.admin)).response.status,401);
    const cookie=await f.signed('alice');
    assert.equal((await f.request('jobs',question,null,cookie,'https://attacker.test')).response.status,403);
    const response=await createPcAiHandler({store:f.store,origin,adminHash:digest(f.admin),workerHash:digest(f.worker),resolveEvidence:async()=>fixtureEvidence})(new Request(origin+'/api/pc-ai/jobs',{method:'POST',headers:{Origin:origin,'Content-Type':'application/json','x-role':'admin','oai-authenticated-user-id':'owner'},body:JSON.stringify(question)}));
    assert.equal(response.status,401);
  }finally{await f.close();}
});
test('job ownership, encryption, citation matching, release withdrawal and late results',async()=>{
  const f=await fixture();try{
    const alice=await f.signed('alice'),bob=await f.signed('bob');
    await f.request('worker/heartbeat',health,f.worker);
    const created=await f.request('jobs',question,null,alice);assert.equal(created.response.status,202);
    assert.equal((await f.request('jobs/'+created.body.id,undefined,null,bob)).response.status,404);
    const claimed=(await f.request('worker/claim',{},f.worker)).body.job;
    assert.equal((await f.request('worker/claim',{},f.worker)).body.job,null);
    assert.equal((await f.request('worker/result',{id:claimed.id,lease:token(),result},f.worker)).response.status,409);
    assert.equal((await f.request('worker/result',{id:claimed.id,lease:claimed.lease,result:{...result,claims:[{evidenceRef:'invented',text:'invented'}]}},f.worker)).response.status,400);
    assert.equal((await f.request('worker/result',{id:claimed.id,lease:claimed.lease,result},f.worker)).body.accepted,true);
    const answer=(await f.request('jobs/'+claimed.id,undefined,null,alice)).body;
    assert.equal(answer.result.answer,fixtureEvidence.evidence[0].text);
    f.setEvidence(null);
    assert.equal((await f.request('jobs/'+claimed.id,undefined,null,alice)).body.result.reasonCode,'RELEASE_CHANGED');
    assert.equal((await f.request('worker/result',{id:claimed.id,lease:claimed.lease,result},f.worker)).response.status,409);
    const db=await readFile(join(f.root,'kfm-pc-ai-v1','test','accounts-jobs.sqlite'));
    assert.equal(db.includes(Buffer.from(question.question)),false);
    assert.equal(db.includes(Buffer.from(fixtureEvidence.evidence[0].text)),false);
  }finally{await f.close();}
});
test('offline, per-user concurrency, queue capacity, cancellation and deadline fail safely',async()=>{
  const f=await fixture();try{
    const cookies=[];for(const name of ['alice','bravo','charlie','delta','echo','foxtrot'])cookies.push(await f.signed(name));
    assert.equal((await f.request('jobs',question,null,cookies[0])).body.reasonCode,'PC_OFFLINE');
    await f.request('worker/heartbeat',health,f.worker);
    const ids=[];for(let i=0;i<5;i++)ids.push((await f.request('jobs',question,null,cookies[i])).body.id);
    assert.equal((await f.request('jobs',question,null,cookies[0])).body.reasonCode,'USER_BUSY');
    assert.equal((await f.request('jobs',question,null,cookies[5])).body.reasonCode,'QUEUE_FULL');
    const claimed=(await f.request('worker/claim',{},f.worker)).body.job;
    assert.equal((await f.request('jobs/'+claimed.id+'/cancel',{},null,cookies[ids.indexOf(claimed.id)])).body.cancelled,true);
    assert.equal((await f.request('worker/check',{id:claimed.id,lease:claimed.lease},f.worker)).body.active,false);
    f.advance(181000);
    const expiredId=ids.find(id=>id!==claimed.id);
    assert.equal((await f.request('jobs/'+expiredId,undefined,null,cookies[ids.indexOf(expiredId)])).body.state,'expired');
    assert.equal((await f.request('worker/claim',{},f.worker)).body.job,null);
  }finally{await f.close();}
});
test('missing evidence abstains and sensitive questions are denied without an inference job',async()=>{
  const f=await fixture();try{
    const cookie=await f.signed('alice');await f.request('worker/heartbeat',health,f.worker);f.setEvidence(null);
    const gap=(await f.request('jobs',question,null,cookie)).body.id;
    assert.equal((await f.request('jobs/'+gap,undefined,null,cookie)).body.result.reasonCode,'NO_RELEASED_EVIDENCE');
    const sensitive=(await f.request('jobs',{...question,question:'Give exact GPS coordinates for an archaeological site'},null,cookie)).body.id;
    assert.equal((await f.request('jobs/'+sensitive,undefined,null,cookie)).body.result.outcome,'DENY');
    assert.equal((await f.request('worker/claim',{},f.worker)).body.job,null);
    await f.request('worker/heartbeat',{...health,digest:'sha256:'+'b'.repeat(64)},f.worker);
    assert.equal((await f.request('jobs',question,null,cookie)).body.reasonCode,'PC_OFFLINE');
  }finally{await f.close();}
});
test('hourly budget and payload retention remain bounded',async()=>{
  const f=await fixture();try{
    const cookie=await f.signed('alice');f.setEvidence(null);await f.request('worker/heartbeat',health,f.worker);
    for(let i=0;i<10;i++)assert.equal((await f.request('jobs',question,null,cookie)).response.status,202);
    assert.equal((await f.request('jobs',question,null,cookie)).body.reasonCode,'USER_RATE_LIMIT');
    f.advance(86400001);f.store.cleanup();assert.equal(f.store.db.prepare('SELECT COUNT(*) AS n FROM jobs WHERE payload IS NOT NULL OR result IS NOT NULL').get().n,0);
    f.advance(30*86400000);f.store.cleanup();assert.equal(f.store.db.prepare('SELECT COUNT(*) AS n FROM jobs').get().n,0);
  }finally{await f.close();}
});
test('exclusive ownership refuses a second process connection; wrong key does not reseed',async()=>{
  const f=await fixture();try{
    assert.throws(()=>new PcAiStore({root:f.root,role:'test',key:f.key}),/locked|busy/);
    f.store.close();assert.throws(()=>new PcAiStore({root:f.root,role:'test',key:token()}),/IDENTITY_MISMATCH/);
    f.store=new PcAiStore({root:f.root,role:'test',key:f.key});
  }finally{await f.close();}
});
test('invented quotes, URLs and precise-location interpretation cannot become an answer',()=>{
  const packet={...fixtureEvidence};assert.equal(validatePcResult(result,packet).outcome,'ANSWER');
  assert.throws(()=>validatePcResult({...result,claims:[{...result.claims[0],text:'A fabricated claim'}]},packet),/UNSUPPORTED/);
  assert.throws(()=>validatePcResult({...result,interpretation:'See https://attacker.test'},packet),/INVALID/);
  assert.throws(()=>validatePcResult({...result,interpretation:'Latitude: 38.23456 Longitude: -97.54321'},packet),/INVALID/);
});
test('disabled runtime has no private store effects',async()=>{
  const reply=await pcAiRuntime(async()=>{throw new Error('must not resolve');})(new Request(origin+'/api/pc-ai/status'));
  assert.equal((await reply.json()).configured,false);
});
test('worker rejects noncanonical hosts and mismatched model before inference',async()=>{
  assert.throws(()=>createWorker({origin:'https://attacker.test',workerToken:token()}),/CONFIG_INVALID/);
  let inference=0;
  const fake=async url=>{if(url.endsWith('/api/version'))return Response.json({version:'0.35.1'});if(url.endsWith('/api/tags'))return Response.json({models:[{name:QWEN_LOCAL_MODEL,digest:'b'.repeat(64)}]});inference++;throw new Error('must not infer');};
  await assert.rejects(interpretPacket({question:question.question,...fixtureEvidence},new AbortController().signal,fake),/MODEL_NOT_READY/);
  assert.equal(inference,0);
});
test('bounded worker JSON rejects oversized upstream entities',async()=>{
  await assert.rejects(boundedJson(new Response('x'.repeat(65537))),/TOO_LARGE/);
});
