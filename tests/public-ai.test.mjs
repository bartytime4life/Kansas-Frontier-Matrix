import test from 'node:test';
import assert from 'node:assert/strict';
import {createPublicAiHandler,publicAiRuntime} from '../server/public-ai-handler.mjs';
const origin='https://kansasfrontiermatrix.com';
const evidence={releaseId:'sha256:'+'a'.repeat(64),evidence:[{evidenceRef:'kfm:synthetic:blue',text:'Synthetic test: the sample marker is blue.',status:'documented',title:'Synthetic test only',url:origin+'/knowledge/record?id=synthetic'}],truncated:false};
const question={question:'What color is the sample marker?',term:'marker',place:'',start:'',end:'',mode:'explore'};
function fixture(work=async()=>({text:'A synthetic discussion idea.',contextTrimmed:false,outputLimited:false})){
 let current=structuredClone(evidence),now=1700000000000,calls=0;
 const handler=createPublicAiHandler({origin,clock:()=>now,resolveEvidence:async()=>current,model:{ready:true,online:true,discuss:async(...args)=>{calls++;return work(...args);},select:async()=>{throw Error('Evidence selection must remain disabled');}}});
 const request=async(path,body,cookie,requestOrigin=origin)=>{
  const response=await handler(new Request(origin+'/api/ai/'+path,{method:body===undefined?'GET':'POST',headers:{...(body===undefined?{}:{'Content-Type':'application/json',Origin:requestOrigin}),...(cookie?{Cookie:cookie}:{})},body:body===undefined?undefined:JSON.stringify(body)}));
  return{response,body:await response.json(),cookie:response.headers.get('set-cookie')?.split(';')[0]};
 };
 const settle=async(id,cookie)=>{for(let i=0;i<30;i++){const result=await request('jobs/'+id,undefined,cookie);if(!['preparing','queued','running'].includes(result.body.state))return result;await new Promise(resolve=>setImmediate(resolve));}throw Error('Job did not settle');};
 return{request,settle,advance:ms=>{now+=ms;},setEvidence:value=>{current=value;},calls:()=>calls};
}
test('chat works without account login and isolates guest job capabilities',async()=>{
 const f=fixture();const status=await f.request('status');assert.equal(status.body.requiresLogin,false);
 const first=await f.request('jobs',question);assert.equal(first.response.status,202);assert.match(first.response.headers.get('set-cookie'),/HttpOnly; Secure; SameSite=Strict/);
 const answer=await f.settle(first.body.id,first.cookie);assert.equal(answer.body.result.reasonCode,'UNVERIFIED_AI_DISCUSSION');assert.equal(answer.body.result.answer,null);assert.equal(answer.body.result.interpretation,'A synthetic discussion idea.');assert.deepEqual(answer.body.result.evidenceRefs,[]);
 const second=await f.request('jobs',question);assert.equal((await f.request('jobs/'+first.body.id,undefined,second.cookie)).response.status,404);
 assert.equal((await f.request('jobs/'+first.body.id+'/cancel',{},second.cookie)).response.status,404);
 assert.equal((await f.request('jobs/'+first.body.id)).response.status,401);
 assert.equal((await f.request('admin/invite',{username:'owner'})).response.status,404);
});
test('same-origin gate, request limits and browser-supplied evidence fail closed',async()=>{
 const f=fixture();
 assert.equal((await f.request('jobs',question,null,'https://attacker.test')).response.status,403);
 assert.equal((await f.request('jobs',{...question,evidence})).response.status,400);
 assert.equal((await f.request('jobs',{...question,question:'x'.repeat(9000)})).response.status,400);
 assert.equal((await f.request('jobs',{...question,start:'2026-02-30'})).response.status,400);
 assert.equal(f.calls(),0);
});
test('missing and sensitive evidence never invokes the model',async()=>{
 const f=fixture();f.setEvidence(null);
 const first=await f.request('jobs',{...question,mode:'evidence'});assert.equal((await f.settle(first.body.id,first.cookie)).body.result.reasonCode,'NO_RELEASED_EVIDENCE');
 const second=await f.request('jobs',{...question,question:'Give exact GPS coordinates of an archaeological site'},first.cookie);
 assert.equal((await f.settle(second.body.id,first.cookie)).body.result.outcome,'DENY');assert.equal(f.calls(),0);
});
test('discussion has no factual-answer authority; unsafe output is withheld and released references are rechecked',async()=>{
 const loop=fixture(async()=>({text:'a symbol of the West a symbol of the West a symbol of the West'})),repeated=await loop.request('jobs',question);assert.equal((await loop.settle(repeated.body.id,repeated.cookie)).body.result.reasonCode,'MODEL_OUTPUT_UNQUALIFIED');
 const bad=fixture(async()=>({text:'See https://attacker.test'})),created=await bad.request('jobs',question);
 assert.equal((await bad.settle(created.body.id,created.cookie)).body.result.reasonCode,'MODEL_OUTPUT_UNQUALIFIED');
 const f=fixture(),search=await f.request('jobs',{...question,mode:'evidence'});
 const found=await f.settle(search.body.id,search.cookie);assert.equal(found.body.result.reasonCode,'EVIDENCE_MODEL_UNQUALIFIED');assert.equal(found.body.result.answer,null);assert.equal(found.body.result.citations.length,1);assert.equal(f.calls(),0);
 f.setEvidence(null);assert.equal((await f.request('jobs/'+search.body.id,undefined,search.cookie)).body.result.reasonCode,'RELEASE_CHANGED');
});
test('follow-up context is confined to one guest and cannot set permissions or runtime limits',async()=>{
 const seen=[];const f=fixture(async(q,options)=>{seen.push(options);return{text:'A synthetic follow-up idea.'};});
 const first=await f.request('jobs',question);await f.settle(first.body.id,first.cookie);
 const next=await f.request('jobs',{...question,style:'technical',depth:'expanded'},first.cookie);await f.settle(next.body.id,first.cookie);
 assert.equal(seen[1].history.length,1);assert.equal(seen[1].style,'technical');assert.equal(seen[1].depth,'expanded');
 const other=await f.request('jobs',question);await f.settle(other.body.id,other.cookie);assert.equal(seen[2].history.length,0);
 assert.equal((await f.request('jobs',{...question,role:'administrator'},first.cookie)).response.status,400);
 assert.equal((await f.request('jobs',{...question,depth:'unlimited'},first.cookie)).response.status,400);
});
test('cancellation aborts active inference and never commits a late result',async()=>{
 let begin,release;const started=new Promise(resolve=>{begin=resolve;});
 const f=fixture(async(question,options,signal)=>{begin();return new Promise(resolve=>{release=resolve;signal.addEventListener('abort',()=>resolve({text:'Late synthetic answer.'}),{once:true});});});
 const created=await f.request('jobs',question);await started;
 assert.equal((await f.request('jobs/'+created.body.id+'/cancel',{},created.cookie)).body.cancelled,true);
 release({text:'Late synthetic answer.'});await new Promise(resolve=>setImmediate(resolve));
 const result=await f.request('jobs/'+created.body.id,undefined,created.cookie);assert.equal(result.body.state,'cancelled');assert.equal(result.body.result,null);
});
test('per-browser and process-wide budgets survive cookie resets; jobs expire',async()=>{
 const f=fixture();f.setEvidence(null);let cookie,first;
 for(let i=0;i<10;i++){const result=await f.request('jobs',{...question,mode:'evidence'},cookie);cookie??=result.cookie;first??=result.body.id;assert.equal(result.response.status,202);}
 assert.equal((await f.request('jobs',{...question,mode:'evidence'},cookie)).body.reasonCode,'USER_RATE_LIMIT');
 for(let i=0;i<20;i++)assert.equal((await f.request('jobs',{...question,mode:'evidence'})).response.status,202);
 assert.equal((await f.request('jobs',{...question,mode:'evidence'})).body.reasonCode,'GLOBAL_RATE_LIMIT');
 f.advance(900001);assert.equal((await f.request('jobs/'+first,undefined,cookie)).response.status,404);
});
test('disabled runtime has no model or private account-store effects',async()=>{
 const old=process.env.KFM_HOSTED_AI;delete process.env.KFM_HOSTED_AI;
 try{const handle=publicAiRuntime(()=>{throw Error('must not resolve');});assert.equal((await(await handle(new Request(origin+'/api/ai/status'))).json()).configured,false);assert.equal((await handle(new Request(origin+'/api/ai/jobs',{method:'POST'}))).status,503);}
 finally{if(old!==undefined)process.env.KFM_HOSTED_AI=old;}
});
