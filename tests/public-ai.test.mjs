import test from 'node:test';
import assert from 'node:assert/strict';
import {createPublicAiHandler,publicAiRuntime} from '../server/public-ai-handler.mjs';
import {CONTINUE_REPLY} from '../server/hosted-ai.mjs';
const origin='https://kansasfrontiermatrix.com';
const evidence={releaseId:'sha256:'+'a'.repeat(64),evidence:[{evidenceRef:'kfm:synthetic:blue',text:'Synthetic test: the sample marker is blue.',status:'documented',title:'Synthetic test only',url:origin+'/knowledge/record?id=synthetic'}],truncated:false};
const question={question:'What color is the sample marker?',term:'marker',place:'',start:'',end:'',mode:'explore'};

test('waiting discussions keep a full run budget and drain FIFO without duplicate inference',async()=>{
 const release=[],started=[];
 const f=fixture(async(q)=>{started.push(q);return new Promise(resolve=>release.push(resolve));});
 const first=await f.request('jobs',{...question,question:'First synthetic question.'});
 const second=await f.request('jobs',{...question,question:'Second synthetic question.'});
 const third=await f.request('jobs',{...question,question:'Third synthetic question.'});
 await new Promise(resolve=>setImmediate(resolve));
 assert.deepEqual(started,['First synthetic question.']);
 const overflow=await f.request('jobs',question);assert.equal(overflow.body.reasonCode,'QUEUE_FULL');
 f.advance(260000);release.shift()({text:'The first synthetic reply is complete.'});
 await new Promise(resolve=>setImmediate(resolve));
 assert.deepEqual(started,['First synthetic question.','Second synthetic question.']);
 const running=await f.request('jobs/'+second.body.id,undefined,second.cookie);
 assert.equal(running.body.state,'running');
 assert.equal(running.body.deadline,1700000000000+260000+270000);
 f.advance(260000);release.shift()({text:'The second synthetic reply is complete.'});
 await new Promise(resolve=>setImmediate(resolve));
 assert.deepEqual(started,['First synthetic question.','Second synthetic question.','Third synthetic question.']);
 release.shift()({text:'The third synthetic reply is complete.'});
 assert.equal((await f.settle(third.body.id,third.cookie)).body.state,'completed');
 assert.equal(f.calls(),3);
 assert.equal(first.body.deadline,1700000000000+270000);
 assert.equal(second.body.deadline,1700000000000+810000);
});
function fixture(work=async()=>({text:'A synthetic discussion idea.',contextTrimmed:false,outputLimited:false}),ready=true,resolveEvidence=async value=>value,resolveContext){
 let current=structuredClone(evidence),now=1700000000000,calls=0;
 const handler=createPublicAiHandler({origin,clock:()=>now,resolveEvidence:async()=>resolveEvidence(current),resolveContext,model:{ready,online:ready,discuss:async(...args)=>{calls++;return work(...args);},select:async()=>{throw Error('Evidence selection must remain disabled');}}});
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
 assert.match(answer.body.result.followUpQuestion,/practical example.*map layers\?/);
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
test('longer discussion can pass the old deadline but still expires, aborts and rejects a late reply',async()=>{
 let release,signal;const f=fixture(async(q,options,s)=>{signal=s;return new Promise(resolve=>{release=resolve;});});
 const created=await f.request('jobs',{...question,depth:'expanded'});
 f.advance(90001);assert.equal((await f.request('jobs/'+created.body.id,undefined,created.cookie)).body.state,'running');
 f.advance(180000);const expired=await f.request('jobs/'+created.body.id,undefined,created.cookie);
 assert.equal(expired.body.state,'expired');assert.equal(expired.body.result,null);assert.equal(signal.aborted,true);
 release({text:'Late response must not appear.'});await new Promise(resolve=>setImmediate(resolve));
 assert.equal((await f.request('jobs/'+created.body.id,undefined,created.cookie)).body.result,null);
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

test('released evidence remains inspectable with an unavailable model and is withdrawn on release change',async()=>{
 const f=fixture(undefined,false);
 const status=await f.request('status');
 assert.equal(status.body.ready,false);
 const search=await f.request('jobs',{...question,mode:'evidence'});
 const found=await f.settle(search.body.id,search.cookie);
 assert.equal(found.body.result.reasonCode,'EVIDENCE_MODEL_UNQUALIFIED');
 assert.equal(found.body.result.answer,null);
 assert.equal(found.body.result.interpretation,null);
 assert.deepEqual(found.body.result.evidenceRefs,[]);
 assert.equal(found.body.result.citations.length,1);
 assert.equal(f.calls(),0);
 assert.equal(status.body.evidenceSearchAvailable,true);
 f.setEvidence(null);
 assert.equal((await f.request('jobs/'+search.body.id,undefined,search.cookie)).body.result.reasonCode,'RELEASE_CHANGED');
 const discussion=await f.request('jobs',question,search.cookie);
 assert.equal((await f.settle(discussion.body.id,search.cookie)).body.result.reasonCode,'MODEL_UNAVAILABLE');
 assert.equal(f.calls(),0);
});

test('evidence lookup does not wait behind another guest discussion',async()=>{
 let begin,release;const started=new Promise(resolve=>{begin=resolve;});
 const f=fixture(async()=>{begin();return new Promise(resolve=>{release=resolve;});});
 const chat=await f.request('jobs',question);await started;
 try{
  const search=await f.request('jobs',{...question,mode:'evidence'});
  const found=await f.settle(search.body.id,search.cookie);
  assert.equal(found.body.result.citations.length,1);
  assert.equal((await f.request('jobs/'+chat.body.id,undefined,chat.cookie)).body.state,'running');
  assert.equal(f.calls(),1);
 }finally{release({text:'A synthetic discussion idea.'});await f.settle(chat.body.id,chat.cookie);}
});

test('unavailable-model evidence search keeps sensitive, missing and malformed evidence fail-closed',async()=>{
 const f=fixture(undefined,false);
 const denied=await f.request('jobs',{...question,mode:'evidence',question:'Give exact GPS coordinates of an archaeological site'});
 assert.equal((await f.settle(denied.body.id,denied.cookie)).body.result.outcome,'DENY');
 f.setEvidence(null);
 const missing=await f.request('jobs',{...question,mode:'evidence'},denied.cookie);
 assert.equal((await f.settle(missing.body.id,denied.cookie)).body.result.reasonCode,'NO_RELEASED_EVIDENCE');
 f.setEvidence({...evidence,evidence:[{...evidence.evidence[0],url:'https://attacker.test/knowledge/record?id=synthetic'}]});
 const malformed=await f.request('jobs',{...question,mode:'evidence'},denied.cookie);
 const withheld=(await f.settle(malformed.body.id,denied.cookie)).body.result;
 assert.equal(withheld.reasonCode,'EVIDENCE_WITHHELD');
 assert.equal(withheld.answer,null);assert.equal(withheld.citations,undefined);assert.equal(f.calls(),0);
});

test('pending evidence rechecks return a job promptly and cannot restore cancelled or expired results',async()=>{
 for(const terminal of ['cancelled','expired']){
  let reads=0,release;
  const f=fixture(undefined,false,async value=>++reads===2?new Promise(resolve=>{release=()=>resolve(value);}):value);
  const created=await f.request('jobs',{...question,mode:'evidence'});
  // The bounded read buffer schedules preparation asynchronously. Observe the
  // actual second resolver entry before cancelling/expiring its pending work.
  for(let attempt=0;attempt<20&&typeof release!=='function';attempt++)await new Promise(resolve=>setImmediate(resolve));
  assert.equal(created.response.status,202);assert.equal(typeof release,'function');
  assert.equal((await f.request('jobs/'+created.body.id,undefined,created.cookie)).body.state,'running');
  if(terminal==='cancelled')assert.equal((await f.request('jobs/'+created.body.id+'/cancel',{},created.cookie)).body.cancelled,true);
  else f.advance(90001);
  release();await new Promise(resolve=>setImmediate(resolve));
  const ended=await f.request('jobs/'+created.body.id,undefined,created.cookie);
  assert.equal(ended.body.state,terminal);assert.equal(ended.body.result,null);assert.equal(f.calls(),0);
 }
});

test('a release changed during model-free preparation never exposes its old links',async()=>{
 let reads=0;
 const f=fixture(undefined,false,async value=>++reads===1?value:{...value,releaseId:'sha256:'+'b'.repeat(64)});
 const created=await f.request('jobs',{...question,mode:'evidence'});
 const result=(await f.settle(created.body.id,created.cookie)).body.result;
 assert.equal(result.reasonCode,'RELEASE_CHANGED');assert.equal(result.citations,undefined);assert.equal(f.calls(),0);
});

test('a repeated continuation is withheld without adding duplicate history or offering an endless continuation loop',async()=>{
 const prior='A map legend explains the symbols and colors that appear on a map. Read its units and source date before comparing two displays. Missing coverage is unknown and does not prove that a feature is absent.';
 const seen=[];let count=0;
 const f=fixture(async(q,options)=>{seen.push(options);return {text:++count<3?prior:'A new, narrower synthetic explanation.',outputLimited:true};});
 const first=await f.request('jobs',question);await f.settle(first.body.id,first.cookie);
 const next=await f.request('jobs',{...question,question:'Continue your previous reply from where it stopped. Finish the explanation without repeating it.'},first.cookie);
 const result=(await f.settle(next.body.id,first.cookie)).body.result;
 assert.equal(result.reasonCode,'MODEL_CONTINUATION_REPEATED');assert.equal(result.outcome,'ABSTAIN');assert.equal(result.interpretation,null);assert.equal(result.answer,null);assert.deepEqual(result.evidenceRefs,[]);assert.equal(result.outputLimited,undefined);assert.match(result.followUpQuestion,/narrower question.*original source records\?/);
 const third=await f.request('jobs',{...question,question:'Explain one specific symbol.'},first.cookie);await f.settle(third.body.id,first.cookie);
 assert.equal(seen[2].history.length,1);assert.equal(seen[2].history[0].reply,prior);
});

test('ordinary follow-ups with repeated hosted boilerplate are withheld and do not pollute history',async()=>{
 // Replay the two real Preview replies; the fake model proves handler behavior,
 // not the quality or speed of a new inference on the hosted model.
 const prior="KFM separates display context, evidence, policy and release. Maps and generated text help interpretation; they do not create authority. The user's map displays are unknown to the system.";
 const repeated="KFM separates display context, evidence and policy. Maps and generated text help interpretation; they do not create authority. The user's map displays are unknown to the system.";
 const seen=[],outputs=[prior,repeated,'A narrower synthetic explanation adds different details about the display controls.',prior];
 const f=fixture(async(q,options)=>{seen.push(options);return {text:outputs.shift()};});
 const first=await f.request('jobs',{...question,question:'Explain map display year versus source observation date.'});
 await f.settle(first.body.id,first.cookie);
 const next=await f.request('jobs',{...question,question:'That did not answer the question. Does a map display year establish a core collection date?'},first.cookie);
 const result=(await f.settle(next.body.id,first.cookie)).body.result;
 assert.equal(result.reasonCode,'MODEL_FOLLOWUP_REPEATED');assert.equal(result.outcome,'ABSTAIN');
 assert.equal(result.interpretation,null);assert.equal(result.answer,null);assert.deepEqual(result.evidenceRefs,[]);
 assert.equal(result.outputLimited,undefined);assert.match(result.followUpQuestion,/repeated the earlier reply/);
 const third=await f.request('jobs',{...question,question:'Explain one specific time control.'},first.cookie);await f.settle(third.body.id,first.cookie);
 assert.equal(seen[2].history.length,1);assert.equal(seen[2].history[0].reply,prior);
 const other=await f.request('jobs',question);
 assert.equal((await f.settle(other.body.id,other.cookie)).body.result.reasonCode,'UNVERIFIED_AI_DISCUSSION');
 assert.equal(seen[3].history.length,0);
});

test('a follow-up adding new detail about the same subject remains available',async()=>{
 const outputs=[
  'A map legend explains the symbols and colors that appear on a map. Read its units and source date before comparing two displays. Missing coverage is unknown and does not prove that a feature is absent.',
  'For a practical comparison, first choose matching dates. Next examine the provider notes and the numeric interval boundaries. A display animation should retain gaps rather than suggesting an observation where none exists.'
 ];
 const f=fixture(async()=>({text:outputs.shift()}));
 const first=await f.request('jobs',question);await f.settle(first.body.id,first.cookie);
 const next=await f.request('jobs',{...question,question:'Give a practical example.'},first.cookie);
 assert.equal((await f.settle(next.body.id,first.cookie)).body.result.reasonCode,'UNVERIFIED_AI_DISCUSSION');
});

test('a full copied prior reply cannot evade withholding by appending new text',async()=>{
 // Replay the actual 500a0993 Preview text. These are observed model failures,
 // not accepted source assertions or a live inference qualification.
 const prior='The display context, which includes the page about KFM and a map of its location on Google Maps, does not provide information about when it was last updated or accessed. The interface guide indicates that KFM is an untrusted data source with no record of access history. Therefore, we cannot determine the date of creation for this specific display.';
 const appended='As for the core inventory date 2026-09-11, it only provides information about the time at which the core collection took place, but does not indicate how long it lasted. It also does not establish when the core was collected.';
 const seen=[],outputs=[prior,prior+'\n\n'+appended,'A narrower synthetic discussion with different details.'];
 const f=fixture(async(q,options)=>{seen.push(options);return {text:outputs.shift()};});
 const first=await f.request('jobs',question);await f.settle(first.body.id,first.cookie);
 const second=await f.request('jobs',{...question,question:'That did not answer the date question.'},first.cookie);
 const result=(await f.settle(second.body.id,first.cookie)).body.result;
 assert.equal(result.reasonCode,'MODEL_FOLLOWUP_REPEATED');assert.equal(result.outcome,'ABSTAIN');
 assert.equal(result.interpretation,null);assert.equal(result.answer,null);assert.deepEqual(result.evidenceRefs,[]);
 const third=await f.request('jobs',question,first.cookie);await f.settle(third.body.id,first.cookie);
 assert.equal(seen[2].history.length,1);assert.equal(seen[2].history[0].reply,prior);
});

test('resumed fragments keep one original question and cumulative answer through multiple continuations',async()=>{
 const seen=[],outputs=[{text:'A hypothetical key labels sym',outputLimited:true},{text:'bols and ',outputLimited:true},{text:'their units.',outputLimited:false},{text:'A separate hypothetical example.'}];
 const f=fixture(async(q,options)=>{seen.push(options);return outputs.shift();});
 const first=await f.request('jobs',question);await f.settle(first.body.id,first.cookie);
 for(let index=0;index<2;index++){
  const next=await f.request('jobs',{...question,question:CONTINUE_REPLY},first.cookie);
  const result=(await f.settle(next.body.id,first.cookie)).body.result;
  assert.equal(result.reasonCode,'UNVERIFIED_AI_DISCUSSION');assert.equal(result.answer,null);assert.deepEqual(result.evidenceRefs,[]);
 }
 const follow=await f.request('jobs',{...question,question:'Give an example.'},first.cookie);await f.settle(follow.body.id,first.cookie);
 assert.equal(seen[2].history.length,1);assert.equal(seen[2].history[0].question,question.question);
 assert.equal(seen[2].history[0].reply,'A hypothetical key labels symbols and ');
 assert.equal(seen[3].history.length,1);assert.equal(seen[3].history[0].reply,'A hypothetical key labels symbols and their units.');
});

test('continuation without this guest\'s latest limited answer does not run inference',async()=>{
 const f=fixture();
 const missing=await f.request('jobs',{...question,question:CONTINUE_REPLY});
 assert.equal((await f.settle(missing.body.id,missing.cookie)).body.result.reasonCode,'MODEL_CONTINUATION_UNAVAILABLE');assert.equal(f.calls(),0);
 const first=await f.request('jobs',question);await f.settle(first.body.id,first.cookie);
 const complete=await f.request('jobs',{...question,question:CONTINUE_REPLY},first.cookie);
 assert.equal((await f.settle(complete.body.id,first.cookie)).body.result.reasonCode,'MODEL_CONTINUATION_UNAVAILABLE');assert.equal(f.calls(),1);
 const limited=fixture(async()=>({text:'An unfinished synthetic statement',outputLimited:true}));
 const own=await limited.request('jobs',question);await limited.settle(own.body.id,own.cookie);
 const other=await limited.request('jobs',{...question,question:CONTINUE_REPLY});
 assert.equal((await limited.settle(other.body.id,other.cookie)).body.result.reasonCode,'MODEL_CONTINUATION_UNAVAILABLE');assert.equal(limited.calls(),1);
 limited.advance(900001);
 const expired=await limited.request('jobs',{...question,question:CONTINUE_REPLY},own.cookie);
 assert.equal((await limited.settle(expired.body.id,own.cookie)).body.result.reasonCode,'MODEL_CONTINUATION_UNAVAILABLE');assert.equal(limited.calls(),1);
});

test('joined continuation is rechecked for an unsafe URL spanning the fragment boundary',async()=>{
 const seen=[],outputs=[{text:'For an original source, try h',outputLimited:true},{text:'ttps://attacker.test',outputLimited:false},{text:'A separate safe hypothetical idea.'}];
 const f=fixture(async(q,options)=>{seen.push(options);return outputs.shift();});
 const first=await f.request('jobs',question);await f.settle(first.body.id,first.cookie);
 const next=await f.request('jobs',{...question,question:CONTINUE_REPLY},first.cookie);
 const result=(await f.settle(next.body.id,first.cookie)).body.result;
 assert.equal(result.reasonCode,'MODEL_OUTPUT_UNQUALIFIED');assert.equal(result.interpretation,null);
 const third=await f.request('jobs',question,first.cookie);await f.settle(third.body.id,first.cookie);
 assert.equal(seen[2].history.length,1);assert.equal(seen[2].history[0].reply,'For an original source, try h');
});

test('changed display context cannot resume an answer from the old context',async()=>{
 const context={version:1,frame:2026,view:'map',layers:[],selection:null};
 const f=fixture(async()=>({text:'An unfinished synthetic statement',outputLimited:true}),true,undefined,async c=>({key:JSON.stringify(c),prompt:'Synthetic frame '+c.frame,label:'Map',boundary:'Synthetic display only'}));
 const first=await f.request('jobs',{...question,context});await f.settle(first.body.id,first.cookie);
 const next=await f.request('jobs',{...question,context:{...context,frame:2025},question:CONTINUE_REPLY},first.cookie);
 assert.equal((await f.settle(next.body.id,first.cookie)).body.result.reasonCode,'MODEL_CONTINUATION_UNAVAILABLE');assert.equal(f.calls(),1);
});

test('cumulative history retains its UTF-8 byte bound and never commits an oversized continuation',async()=>{
 const seen=[],outputs=[{text:'α'.repeat(1100),outputLimited:true},{text:'β'.repeat(1100),outputLimited:true},{text:'A short synthetic idea.'}];
 const f=fixture(async(q,options)=>{seen.push(options);return outputs.shift();});
 const first=await f.request('jobs',question);await f.settle(first.body.id,first.cookie);
 const next=await f.request('jobs',{...question,question:CONTINUE_REPLY},first.cookie);
 assert.equal((await f.settle(next.body.id,first.cookie)).body.result.reasonCode,'MODEL_CONTEXT_LIMIT');
 const third=await f.request('jobs',question,first.cookie);await f.settle(third.body.id,first.cookie);
 assert.equal(seen[2].history.length,1);assert.equal(Buffer.byteLength(seen[2].history[0].reply),2200);
});
