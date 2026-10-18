import test from 'node:test';
import assert from 'node:assert/strict';
import {createPublicAiHandler} from '../server/public-ai-handler.mjs';

const origin='https://kansasfrontiermatrix.com';
const context={version:1,frame:2026,view:'2D',layers:[],selection:{kind:'subsurface',tileId:'tile-0-0',recordId:'synthetic-core',intervalIndex:null}};
const source=()=>({key:'synthetic-one',prompt:'Synthetic source context only.',label:'Synthetic core',boundary:'Source context, not admitted evidence',sourceSummary:'Synthetic logged depth: 10 ft. Recovery is unknown.'});
const input={question:'Explain the selected record.',term:'record',mode:'explore',context};
const turn=()=>new Promise(resolve=>setImmediate(resolve));
function fixture(resolveContext=async()=>source(),resolveEvidence=async()=>null){
 let now=1700000000000,calls=0;
 const handler=createPublicAiHandler({origin,clock:()=>now,resolveContext,resolveEvidence,model:{ready:false,online:false,discuss:async()=>{calls++;throw Error('No inference expected');}}});
 const request=async(path,value,cookie)=>{
  const response=await handler(new Request(origin+'/api/ai/'+path,{method:value===undefined?'GET':'POST',headers:{...(value===undefined?{}:{'content-type':'application/json',origin}),...(cookie?{cookie}:{})},body:value===undefined?undefined:JSON.stringify(value)}));
  return {status:response.status,body:await response.json(),cookie:response.headers.get('set-cookie')?.split(';')[0],retryAfter:response.headers.get('retry-after')};
 };
 const create=async(value=input)=>{const job=await request('jobs',value);assert.equal(job.status,202);await turn();return job;};
 return {request,create,advance:ms=>{now+=ms;},calls:()=>calls};
}

test('overlapping owned completed reads share one fresh source check and do not invoke inference',async()=>{
 let hold=false,reads=0;const pending=[];
 const f=fixture(async()=>{reads++;return hold?new Promise(resolve=>pending.push(resolve)):source();});
 const job=await f.create();hold=true;const before=reads;
 const first=f.request('jobs/'+job.body.id,undefined,job.cookie),second=f.request('jobs/'+job.body.id,undefined,job.cookie);
 await turn();const excess=await f.request('jobs/'+job.body.id,undefined,job.cookie);
 assert.equal(excess.status,429);assert.equal(excess.body.reasonCode,'AI_READ_BUSY');assert.equal(excess.body.result,undefined);assert.equal(excess.retryAfter,'2');
 for(const resolve of pending)resolve(source());
 const results=await Promise.all([first,second]);
 assert.equal(reads-before,1,'duplicate GETs must not repeat tile resolution');
 assert.ok(results.every(result=>result.status===200&&result.body.result.reasonCode==='SOURCE_CONTEXT_ONLY'));
 assert.equal(f.calls(),0);
});

test('sequential completed polling has a read budget, preserves source checks and recovers',async()=>{
 let reads=0;const f=fixture(async()=>{reads++;return source();}),job=await f.create();const before=reads;
 for(let i=0;i<60;i++)assert.equal((await f.request('jobs/'+job.body.id,undefined,job.cookie)).status,200);
 const blocked=await f.request('jobs/'+job.body.id,undefined,job.cookie);
 assert.equal(blocked.status,429);assert.equal(blocked.body.reasonCode,'AI_READ_RATE_LIMIT');assert.equal(blocked.retryAfter,'60');
 assert.equal(blocked.body.result,undefined);assert.equal(reads-before,60);
 f.advance(60001);assert.equal((await f.request('jobs/'+job.body.id,undefined,job.cookie)).body.result.reasonCode,'SOURCE_CONTEXT_ONLY');
 assert.equal(reads-before,61);
});

test('cookie resets cannot bypass the shared read budget',async()=>{
 const f=fixture();let next;
 for(let g=0;g<6;g++){
  const job=await f.create();
  if(g===5){next=job;break;}
  for(let i=0;i<60;i++)assert.equal((await f.request('jobs/'+job.body.id,undefined,job.cookie)).status,200);
 }
 const held=await f.request('jobs/'+next.body.id,undefined,next.cookie);
 assert.equal(held.status,429);assert.equal(held.body.reasonCode,'AI_READ_RATE_LIMIT');assert.equal(held.body.result,undefined);
 assert.equal((await f.request('status')).status,200);
 assert.equal((await f.request('jobs/'+next.body.id+'/cancel',{},next.cookie)).status,200);
 assert.equal((await f.request('jobs/'+next.body.id)).status,401);
});

test('distinct jobs share the actual read cap and overload does not withdraw valid data',async()=>{
 let held=false,active=0,peak=0;const release=[];
 const f=fixture(async()=>{
  if(!held)return source();
  peak=Math.max(peak,++active);await new Promise(resolve=>release.push(resolve));active--;return source();
 });
 const jobs=[];for(let i=0;i<11;i++)jobs.push(await f.create());held=true;
 const waiting=jobs.slice(0,10).map(job=>f.request('jobs/'+job.body.id,undefined,job.cookie));
 await turn();assert.equal(active,2);
 const excess=await f.request('jobs/'+jobs[10].body.id,undefined,jobs[10].cookie);
 assert.equal(excess.status,429);assert.equal(excess.body.result,undefined);
 // Eight bounded waiters expire without reaching the resolver.
 await new Promise(resolve=>setTimeout(resolve,1100));
 held=false;release.splice(0).forEach(resolve=>resolve());
 const results=await Promise.all(waiting);assert.equal(peak,2);
 assert.equal(results.filter(r=>r.status===429&&r.body.reasonCode==='AI_READ_BUSY').length,8);
 assert.equal(results.filter(r=>r.status===200).length,2);
 const recovered=await f.request('jobs/'+jobs[2].body.id,undefined,jobs[2].cookie);
 assert.equal(recovered.body.result.reasonCode,'SOURCE_CONTEXT_ONLY');assert.equal(recovered.body.context.label,'Synthetic core');
});

test('resolver response timeout cannot release actual work slots and capacity recovers on settlement',async()=>{
 const pending=[];let reads=0;
 const f=fixture(async()=>{reads++;return new Promise(resolve=>pending.push(resolve));});
 const first=await f.create(),second=await f.create();assert.equal(reads,2);
 await new Promise(resolve=>setTimeout(resolve,5100));
 for(const job of [first,second])assert.equal((await f.request('jobs/'+job.body.id,undefined,job.cookie)).body.result.reasonCode,'CONTEXT_UNAVAILABLE');
 const next=await f.create();await turn();assert.equal(reads,2,'timed-out callers must not free unresolved work slots');
 pending.splice(0).forEach(resolve=>resolve(source()));await turn();assert.equal(reads,3);
 pending.splice(0).forEach(resolve=>resolve(source()));await turn();
 const result=f.request('jobs/'+next.body.id,undefined,next.cookie);await turn();pending.splice(0).forEach(resolve=>resolve(source()));
 assert.equal((await result).body.result.reasonCode,'SOURCE_CONTEXT_ONLY');
});

test('an ordinary completed source summary is freshly checked without model readiness',async()=>{
 let current=source(),reads=0;const f=fixture(async()=>{reads++;return current;});
 const job=await f.create();const first=await f.request('jobs/'+job.body.id,undefined,job.cookie);
 assert.equal(first.body.result.sourceSummary,source().sourceSummary);const before=reads;
 current={...source(),key:'changed-source'};
 const withdrawn=await f.request('jobs/'+job.body.id,undefined,job.cookie);
 assert.equal(reads,before+1);assert.equal(withdrawn.body.result.reasonCode,'RELEASE_CHANGED');
 current=source();assert.equal((await f.request('jobs/'+job.body.id,undefined,job.cookie)).body.result.reasonCode,'RELEASE_CHANGED');
});

test('job expiry during a shared queued read returns no retained source summary',async()=>{
 let hold=false;const pending=[];
 const f=fixture(async()=>hold?new Promise(resolve=>pending.push(resolve)):source()),job=await f.create();hold=true;
 const result=f.request('jobs/'+job.body.id,undefined,job.cookie);await turn();f.advance(900001);
 pending.splice(0).forEach(resolve=>resolve(source()));
 const expired=await result;assert.equal(expired.status,404);assert.equal(expired.body.reasonCode,'JOB_NOT_FOUND');assert.equal(expired.body.context,undefined);
});

test('verified evidence withdrawal survives a sibling context check rejected by queue pressure',async()=>{
 const original={releaseId:'sha256:'+'a'.repeat(64),evidence:[{evidenceRef:'kfm:synthetic:one',text:'Synthetic source assertion.',title:'Synthetic only',status:'documented',url:origin+'/knowledge/record?id=synthetic'}]};
 let evidence=original,hold=false;const pending=[];
 const f=fixture(async()=>hold?new Promise(resolve=>pending.push(resolve)):source(),async()=>evidence);
 const jobs=[];for(let i=0;i<9;i++)jobs.push(await f.create());
 const target=await f.create({...input,mode:'evidence'});hold=true;
 const occupied=jobs.map(job=>f.request('jobs/'+job.body.id,undefined,job.cookie));await turn();
 assert.equal(pending.length,2);evidence=null;
 const checking=f.request('jobs/'+target.body.id,undefined,target.cookie);await turn();
 // The evidence check is eighth in the queue; its context sibling is rejected.
 hold=false;pending.splice(0).forEach(resolve=>resolve(source()));await Promise.all([...occupied,checking]);
 evidence=original;
 const later=await f.request('jobs/'+target.body.id,undefined,target.cookie);
 assert.equal(later.body.result.reasonCode,'RELEASE_CHANGED');assert.equal(later.body.result.citations,undefined);assert.equal(later.body.context,null);
});

test('cancelling a preparing job while its source read is queued prevents late context and inference',async()=>{
 const pending=[];let reads=0;
 const f=fixture(async()=>{reads++;return new Promise(resolve=>pending.push(resolve));});
 await f.create();await f.create();const queued=await f.create();assert.equal(reads,2);
 assert.equal((await f.request('jobs/'+queued.body.id+'/cancel',{},queued.cookie)).body.cancelled,true);
 pending.splice(0).forEach(resolve=>resolve(source()));await turn();
 pending.splice(0).forEach(resolve=>resolve(source()));await turn();
 const cancelled=await f.request('jobs/'+queued.body.id,undefined,queued.cookie);
 assert.equal(cancelled.body.state,'cancelled');assert.equal(cancelled.body.result,null);assert.equal(cancelled.body.context,null);assert.equal(f.calls(),0);
});
