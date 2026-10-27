import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,mkdir,writeFile,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createHash} from 'node:crypto';
import {gzipSync} from 'node:zlib';
import {createAssistantContextResolver,validAssistantContext} from '../server/assistant-context.mjs';
import {createPublicAiHandler} from '../server/public-ai-handler.mjs';
const context={version:1,frame:2026,view:'2D',layers:[],selection:{kind:'subsurface',tileId:'tile-160-255',recordId:'synthetic-core-1',intervalIndex:1}};
test('map-only context supplies calendar orientation without claiming source availability or admission',async()=>{
 const resolve=createAssistantContextResolver({now:()=>new Date('2026-10-27T23:59:00Z')});
 const result=await resolve({...context,selection:null});
 assert.match(result.prompt,/Server clock date \(UTC\) 2026-10-27/);
 assert.match(result.prompt,/Map display year 2026 \(a selected display frame, not a collection or drilling date\)/);
 assert.match(result.prompt,/Recognized layers: none/);
 assert.match(result.prompt,/empty selection does not establish that sources are unavailable/);
 assert.equal(result.boundary,'Application guide and display context only');
 assert.equal(result.releaseId,undefined);assert.equal(result.sourceSummary,undefined);
});
async function fixture(){
 const root=await mkdtemp(join(tmpdir(),'kfm-ai-context-')),directory=join(root,'data/subsurface');await mkdir(directory,{recursive:true});
 const records=[{id:'synthetic-core-1',name:'Not transmitted name',sourceId:'kgs-core',kind:'core',sourceTime:'2025-05-01',depthUnit:'ft',depthReference:'unknown',totalDepth:40,coordinates:[-99.5,38],intervals:[{top:0,bottom:10,description:'Synthetic sand'},{top:10,bottom:40,description:'Synthetic shale',interpreted:'SH'}]}];
 const decoded=Buffer.from(JSON.stringify(records)),bytes=gzipSync(decoded),sha=value=>createHash('sha256').update(value).digest('hex');
 await writeFile(join(directory,'tile-160-255.json.gz'),bytes);
 const manifest={version:1,sources:[{id:'kgs-core',title:'KGS Core Library inventory',sourceTime:'2026-09-11'}],tiles:[{id:'tile-160-255',url:'/data/subsurface/tile-160-255.json.gz',sha256:sha(bytes),decodedSha256:sha(decoded)}]};
 await writeFile(join(directory,'manifest.json'),JSON.stringify(manifest));
 return {root,directory,manifest,resolve:createAssistantContextResolver({publicRoot:root}),close:()=>rm(root,{recursive:true,force:true})};
}
test('only closed bounded selectors cross the context boundary',()=>{
 assert.equal(validAssistantContext(context),true);
 for(const selection of [{...context.selection,sourceSummary:'Collected in 2026'},{...context.selection,coordinates:[-99,38]},{...context.selection,tileId:'../../private/accounts'},{...context.selection,intervalIndex:2000},{kind:'display',title:'a',source:'b',description:'c',time:'d',evidenceRef:'forged'}])assert.equal(validAssistantContext({...context,selection}),false);
 assert.equal(validAssistantContext({...context,role:'administrator'}),false);
 assert.equal(validAssistantContext({...context,layers:Array(15).fill('layer')}),false);
});
test('sample and interval are server resolved, source time stays separate, and names/coordinates are absent',async()=>{
 const f=await fixture();try{
  const result=await f.resolve(context);
  assert.match(result.prompt,/10.*40.*Synthetic shale/);assert.doesNotMatch(result.prompt,/Synthetic sand|Not transmitted name|-99.5/);
  assert.match(result.prompt,/2025-05-01.*2026-09-11/);assert.match(result.prompt,/does not prove recovery/);assert.match(result.boundary,/not admitted evidence/);
  assert.match(result.sourceSummary,/Map display year: 2026/);assert.match(result.sourceSummary,/Source record time: 2025-05-01/);assert.match(result.sourceSummary,/Archive edition: 2026-09-11/);
  assert.match(result.sourceSummary,/do not establish a collection or drilling date/);assert.match(result.sourceSummary,/Selected recorded interval: 10–40 ft/);assert.doesNotMatch(result.sourceSummary,/Not transmitted name|-99.5/);
  const whole=await f.resolve({...context,selection:{...context.selection,intervalIndex:null}});
  assert.match(whole.prompt,/intervalCount/);assert.doesNotMatch(whole.prompt,/Synthetic shale/);
  await assert.rejects(f.resolve({...context,selection:{...context.selection,intervalIndex:12}}),/CONTEXT_UNAVAILABLE/);
  await assert.rejects(f.resolve({...context,frame:2024}),/CONTEXT_TIME_MISMATCH/);
 }finally{await f.close();}
});
test('missing, changed and traversal assets fail closed without arbitrary file reads',async()=>{
 const f=await fixture();try{
  await assert.rejects(f.resolve({...context,selection:{...context.selection,recordId:'absent'}}),/CONTEXT_UNAVAILABLE/);
  await writeFile(join(f.directory,'tile-160-255.json.gz'),'tampered');
  await assert.rejects(f.resolve(context),/CONTEXT_UNAVAILABLE/);
  f.manifest.tiles[0].url='/private/accounts.json';await writeFile(join(f.directory,'manifest.json'),JSON.stringify(f.manifest));
  await assert.rejects(f.resolve(context),/CONTEXT_UNAVAILABLE/);
 }finally{await f.close();}
});
test('catalog denials and time mismatch are not converted to ordinary discussion',async()=>{
 const registry={...context,selection:{kind:'registry',layerId:'layer',featureId:'feature'}};
 await assert.rejects(createAssistantContextResolver({catalog:()=>({denied:true})})(registry),/POLICY_WITHHELD/);
 await assert.rejects(createAssistantContextResolver({catalog:()=>({title:'test',year:2025,exactTime:true,prompt:'synthetic'})})(registry),/CONTEXT_TIME_MISMATCH/);
});
test('selected samples return server source facts without model inventions and retain job ownership',async()=>{
 const f=await fixture(),seen=[],origin='https://kansasfrontiermatrix.com';
 const handler=createPublicAiHandler({origin,resolveEvidence:async()=>null,resolveContext:f.resolve,model:{ready:false,online:false,discuss:async(question,options)=>{seen.push(options);return {text:'This core was collected in 2026 and has been stored for one year.'};}}});
 const request=async(path,value,cookie)=>{
  const response=await handler(new Request(origin+'/api/ai/'+path,{method:value?'POST':'GET',headers:{...(value?{'content-type':'application/json',origin}:{}),...(cookie?{cookie}:{})},body:value?JSON.stringify(value):undefined}));return {body:await response.json(),cookie:response.headers.get('set-cookie')?.split(';')[0],status:response.status};
 };
 const ask=async(ctx,cookie)=>{
  const created=await request('jobs',{question:'Explain this selected interval.',term:'core',mode:'explore',context:ctx},cookie);cookie??=created.cookie;
  const deadline=Date.now()+2500;while(Date.now()<deadline){const next=await request('jobs/'+created.body.id,null,cookie);if(next.body.state==='completed')return {...next,cookie};await new Promise(resolve=>setTimeout(resolve,5));}throw Error('did not settle');
 };
 try{
  const first=await ask(context);assert.equal(first.body.result.reasonCode,'SOURCE_CONTEXT_ONLY');assert.equal(first.body.result.answer,null);assert.equal(first.body.result.interpretation,null);assert.deepEqual(first.body.result.evidenceRefs,[]);assert.match(first.body.result.sourceSummary,/Synthetic shale/);assert.equal(first.body.context.label,'synthetic-core-1');
  assert.match(first.body.sourceRevision,/^sha256:[a-f0-9]{64}$/);assert.equal(first.body.releaseId,null);assert.ok(Number.isFinite(Date.parse(first.body.checkedAt)));
  assert.doesNotMatch(JSON.stringify(first.body.result),/collected in 2026|stored for one year/);
  assert.match(first.body.result.followUpQuestion,/original source intervals.*aquifer ranges\?/);
  await ask(context,first.cookie);
  const changed=await ask({...context,selection:{...context.selection,intervalIndex:0}},first.cookie);assert.match(changed.body.result.sourceSummary,/Synthetic sand/);assert.doesNotMatch(changed.body.result.sourceSummary,/Synthetic shale/);assert.notEqual(changed.body.sourceRevision,first.body.sourceRevision);
  assert.equal((await request('jobs/'+changed.body.id)).status,401);
  const missing=await ask({...context,selection:{...context.selection,recordId:'absent'}},first.cookie);assert.equal(missing.body.result.reasonCode,'CONTEXT_UNAVAILABLE');assert.equal(seen.length,0);
  await writeFile(join(f.directory,'tile-160-255.json.gz'),'changed');
  const withdrawn=await request('jobs/'+first.body.id,null,first.cookie);assert.equal(withdrawn.body.result.reasonCode,'RELEASE_CHANGED');assert.equal(withdrawn.body.context,null);assert.equal(withdrawn.body.result.sourceSummary,undefined);
  assert.equal(withdrawn.body.sourceRevision,null);assert.equal(withdrawn.body.releaseId,null);
 }finally{await f.close();}
});

test('resolved source changes invalidate same-selector history and pending expiry cannot invoke inference',async()=>{
 const origin='https://kansasfrontiermatrix.com';let revision='one',now=1700000000000,release,calls=0;
 const seen=[],handler=createPublicAiHandler({origin,clock:()=>now,resolveEvidence:async()=>null,resolveContext:async()=>revision==='pending'?new Promise(resolve=>{release=resolve;}):{key:revision,prompt:'Synthetic source revision '+revision,label:'Synthetic source',boundary:'Unverified context'},model:{ready:true,online:true,discuss:async(q,options)=>{calls++;seen.push(options);return {text:'Synthetic only.'};}}});
 const request=async(path,value,cookie)=>{const response=await handler(new Request(origin+'/api/ai/'+path,{method:value?'POST':'GET',headers:{...(value?{'content-type':'application/json',origin}:{}),...(cookie?{cookie}:{})},body:value?JSON.stringify(value):undefined}));return {body:await response.json(),cookie:response.headers.get('set-cookie')?.split(';')[0]};};
 const input={question:'Explain this selected record.',term:'source',mode:'explore',context:{...context,selection:null}};
 const settle=async(id,cookie)=>{for(let i=0;i<20;i++){const result=await request('jobs/'+id,null,cookie);if(!['preparing','queued','running'].includes(result.body.state))return result;await new Promise(resolve=>setImmediate(resolve));}};
 const first=await request('jobs',input);await settle(first.body.id,first.cookie);
 revision='two';const second=await request('jobs',input,first.cookie);await settle(second.body.id,first.cookie);assert.equal(seen[1].history.length,0);
 revision='pending';const pending=request('jobs',input,first.cookie);while(!release)await new Promise(resolve=>setImmediate(resolve));now=(await pending).body.deadline+1;
 release({key:'late',prompt:'Late synthetic source',label:'Late source',boundary:'Unverified context'});
 const late=await pending;assert.equal((await settle(late.body.id,first.cookie)).body.state,'expired');assert.equal(calls,2);
});
