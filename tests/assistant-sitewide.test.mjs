import test from 'node:test';
import assert from 'node:assert/strict';
import ts from 'typescript';
import vm from 'node:vm';
import {readFile} from 'node:fs/promises';
import {componentHarness,findNode,settle} from './component-harness.mjs';
import {ASSISTANT_SURFACES,assistantSurfaceForPath} from '../app/assistant-surfaces.mjs';
import {createAssistantContextResolver,validAssistantContext} from '../server/assistant-context.mjs';
import {createPublicAiHandler} from '../server/public-ai-handler.mjs';

test('only existing public surfaces get page help; private route/query values are not harvested',async()=>{
 for(const path of ['/stewards','/source-operations','/daily-archive','/acquisition','/unknown','/'])assert.equal(assistantSurfaceForPath(path),null);
 for(const surface of ASSISTANT_SURFACES.filter(s=>!['map','reports','stories'].includes(s.id)))assert.equal(assistantSurfaceForPath(surface.path).id,surface.id);
 let pathname='/downloads',id='released-record-one';
 const Panel=()=>null,h=await componentHarness(new URL('../app/site-assistant.tsx',import.meta.url),{
  'next/navigation':{usePathname:()=>pathname,useSearchParams:()=>new URLSearchParams({id,token:'DO_NOT_SEND',password:'DO_NOT_SEND',query:'DO_NOT_SEND'})},
  './assistant-surfaces.mjs':{assistantSurfaceForPath},'./assistant-panel':{default:Panel},'./build-clock':{BUILD_UTC_YEAR:2026},'./assistant-panel.module.css':{default:{}}
 });
 const render=()=>{const tree=h.render(h.exports.PageAssistant,{});h.commit();return tree;};
 try{
  let tree=render();findNode(tree,n=>n.type==='button').props.onClick();tree=render();
  let focus=findNode(tree,n=>n.type===Panel).props.focus;assert.equal(focus.context.surface,'downloads');assert.doesNotMatch(JSON.stringify(focus),/DO_NOT_SEND/);
  pathname='/knowledge/record';tree=render();focus=findNode(tree,n=>n.type===Panel).props.focus;assert.deepEqual(JSON.parse(JSON.stringify(focus.context.selection)),{kind:'knowledge',recordId:id});
  id='../private';tree=render();assert.equal(findNode(tree,n=>n.type===Panel).props.focus.context.selection,null);
  pathname='/stewards';assert.equal(render(),null);
 }finally{h.dispose();}
});

test('report and story snapshots carry permitted filters and comparison but never private draft text or camera positions',async()=>{
 const source=await readFile(new URL('../app/assistant-context.ts',import.meta.url),'utf8'),exports={};
 vm.runInNewContext(ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText,{exports});
 const snapshot={camera:{center:[-98,38]},representation:'2D',temporalSweep:{frame:2026,mode:'comparison'},committedTime:{start:2026},visibleLayers:[{id:'layer-one'}],comparison:{timeA:1910,timeB:2026},evidenceFilter:'ALL',privateText:'DO_NOT_SEND'};
 const normal=exports.snapshotAssistantFocus(snapshot,'reports');
 assert.equal(normal.context.surface,'reports');assert.equal(normal.context.comparison.frameA,1910);assert.doesNotMatch(JSON.stringify(normal),/DO_NOT_SEND|-98/);
 const redacted=exports.snapshotAssistantFocus({...snapshot,camera:{center:'WITHHELD_BROWSER_LOCATION'}},'stories');
 assert.deepEqual(JSON.parse(JSON.stringify(redacted.context.layers)),[]);assert.equal(redacted.context.comparison,undefined);assert.equal(redacted.context.selection,null);
});

test('surface, filter and comparison fields are closed and interface guides resolve without model claims',async()=>{
 const base={version:1,frame:2026,view:'Page',layers:[],selection:null};
 for(const surface of ASSISTANT_SURFACES){
  const result=await createAssistantContextResolver()({...base,surface:surface.id});
  assert.match(result.boundary,/guide.*display context/);assert.ok(result.prompt.includes(surface.guide));
 }
 for(const extra of [{surface:'stewards'},{filters:{evidence:'ALL',temporalMode:'snapshot',privateNotes:'NO'}},{comparison:{frameA:2026,frameB:Infinity}},{selection:{kind:'knowledge',recordId:'../../private'}}])assert.equal(validAssistantContext({...base,...extra}),false);
 const scoped=await createAssistantContextResolver({layers:ids=>ids.map(id=>'Resolved '+id)})({...base,view:'2D',surface:'map',layers:['one'],filters:{evidence:'ALL',temporalMode:'comparison'},comparison:{frameA:1910,frameB:2026}});
 assert.match(scoped.prompt,/Resolved one/);assert.match(scoped.prompt,/matching observations are not established/);
});

function runtime(resolveContext){
 const origin='https://kansasfrontiermatrix.com';let calls=0;
 const handler=createPublicAiHandler({origin,resolveEvidence:async()=>null,resolveContext,model:{ready:true,online:true,discuss:async()=>{calls++;return {text:'Synthetic interpretation only.'};}}});
 const request=async(path,value,cookie)=>{const response=await handler(new Request(origin+'/api/ai/'+path,{method:value?'POST':'GET',headers:{...(value?{'content-type':'application/json',origin}:{}),...(cookie?{cookie}:{})},body:value?JSON.stringify(value):undefined}));return {status:response.status,body:await response.json(),cookie:response.headers.get('set-cookie')?.split(';')[0]};};
 const settleJob=async(id,cookie)=>{for(let i=0;i<40;i++){const next=await request('jobs/'+id,null,cookie);if(!['preparing','queued','running'].includes(next.body.state))return next;await new Promise(resolve=>setImmediate(resolve));}throw Error('did not settle');};
 return {request,settleJob,calls:()=>calls};
}
const input={question:'Explain this selected record.',term:'record',mode:'explore',context:{version:1,frame:2026,view:'Page',layers:[],surface:'knowledge-record',selection:{kind:'knowledge',recordId:'synthetic-one'}}};
const released=()=>({key:'release-one',prompt:'Synthetic documented observation only.',label:'Synthetic record',boundary:'Released record references; interpretation unverified',releaseId:'sha256:'+'a'.repeat(64),references:[{label:'Synthetic record',url:'/knowledge/record?id=synthetic-one',role:'RELEASED_RECORD'}]});

test('knowledge selection uses its reviewed reader and missing records have no display fallback',async()=>{
 const context=input.context;
 await assert.rejects(createAssistantContextResolver()(context),/CONTEXT_UNAVAILABLE/);
 const good=await createAssistantContextResolver({knowledge:()=>({title:'Synthetic',releaseId:'sha256:'+'a'.repeat(64),prompt:'Synthetic documented context',references:[]})})(context);
 assert.match(good.boundary,/Released record/);assert.equal(good.releaseId,'sha256:'+'a'.repeat(64));
});

test('released context is rechecked before inference and on every result read; withdrawal stays withheld',async()=>{
 let current=released();const f=runtime(async()=>current);
 const created=await f.request('jobs',input),done=await f.settleJob(created.body.id,created.cookie);
 assert.equal(done.body.result.reasonCode,'UNVERIFIED_AI_DISCUSSION');assert.equal(done.body.context.references[0].role,'RELEASED_RECORD');assert.equal(f.calls(),1);
 current=null;
 for(let i=0;i<2;i++){const withdrawn=await f.request('jobs/'+created.body.id,null,created.cookie);assert.equal(withdrawn.body.result.reasonCode,'RELEASE_CHANGED');assert.equal(withdrawn.body.result.interpretation,null);assert.equal(withdrawn.body.context,null);}
 const other=await f.request('jobs',{...input,context:{...input.context,selection:null}});
 assert.equal((await f.request('jobs/'+created.body.id,null,other.cookie)).status,404);
});

test('withdrawal between resolution and inference withholds the result without calling the model',async()=>{
 let reads=0;const f=runtime(async()=>++reads===1?released():null);
 const created=await f.request('jobs',input),done=await f.settleJob(created.body.id,created.cookie);
 assert.equal(done.body.result.reasonCode,'RELEASE_CHANGED');assert.equal(done.body.context,null);assert.equal(f.calls(),0);
});

test('concurrent result reads cannot resurrect interpretation after another read withdraws its release',async()=>{
 const pending=[];let race=false;
 const f=runtime(async()=>race?new Promise(resolve=>pending.push(resolve)):released());
 const created=await f.request('jobs',input);await f.settleJob(created.body.id,created.cookie);
 race=true;
 const first=f.request('jobs/'+created.body.id,null,created.cookie),second=f.request('jobs/'+created.body.id,null,created.cookie);
 await settle();assert.equal(pending.length,2);
 pending[0](null);assert.equal((await first).body.result.reasonCode,'RELEASE_CHANGED');
 pending[1](released());const late=await second;
 assert.equal(late.body.result.reasonCode,'RELEASE_CHANGED');assert.equal(late.body.result.interpretation,null);assert.equal(late.body.context,null);
});

test('external source recheck resolves source fingerprints even without a KFM release ID',async()=>{
 let key='source-hash-one',reads=0;
 const f=runtime(async()=>{reads++;return {key,prompt:'Synthetic external source context.',label:'Synthetic KGS source',boundary:'External source context only',references:[{label:'Synthetic source archive',url:'https://www.kgs.ku.edu/',role:'SOURCE_CONTEXT'}]};});
 const created=await f.request('jobs',input);await f.settleJob(created.body.id,created.cookie);
 const before=reads;key='source-hash-two';
 const changed=await f.request('jobs/'+created.body.id,null,created.cookie);
 assert.ok(reads>before);assert.equal(changed.body.result.reasonCode,'RELEASE_CHANGED');assert.equal(changed.body.result.interpretation,null);assert.equal(changed.body.context,null);
});

test('catalog selections without links are rechecked before inference and on result reads',async()=>{
 const selected={...input,context:{...input.context,surface:'map',view:'2D',selection:{kind:'registry',layerId:'synthetic-layer',featureId:'synthetic-feature'}}};
 let record={title:'Synthetic catalogue record',year:2026,prompt:'Original synthetic context.'};
 const resolver=createAssistantContextResolver({catalog:()=>record});
 const f=runtime(resolver),created=await f.request('jobs',selected);
 const done=await f.settleJob(created.body.id,created.cookie);
 assert.equal(done.body.result.reasonCode,'UNVERIFIED_AI_DISCUSSION');
 assert.deepEqual(done.body.context.references,[]);assert.equal(f.calls(),1);
 record={...record,prompt:'Corrected synthetic context.'};
 const changed=await f.request('jobs/'+created.body.id,null,created.cookie);
 assert.equal(changed.body.result.reasonCode,'RELEASE_CHANGED');
 assert.equal(changed.body.result.interpretation,null);assert.equal(changed.body.context,null);
 record={...record,prompt:'Original synthetic context.'};
 assert.equal((await f.request('jobs/'+created.body.id,null,created.cookie)).body.result.reasonCode,'RELEASE_CHANGED');

 let reads=0;
 const beforeInference=runtime(async selector=>{if(++reads>1)record={...record,denied:true};return resolver(selector);});
 const blocked=await beforeInference.request('jobs',selected);
 assert.equal((await beforeInference.settleJob(blocked.body.id,blocked.cookie)).body.result.reasonCode,'RELEASE_CHANGED');
 assert.equal(beforeInference.calls(),0);
});

test('admission returns a job before source resolution; cancellation suppresses a late context without inference',async()=>{
 let release;const f=runtime(()=>new Promise(resolve=>{release=resolve;}));
 const created=await f.request('jobs',input);assert.equal(created.status,202);assert.equal(typeof release,'function');assert.equal((await f.request('jobs/'+created.body.id,null,created.cookie)).body.state,'preparing');
 await f.request('jobs/'+created.body.id+'/cancel',{},created.cookie);release(released());await settle();
 const cancelled=await f.request('jobs/'+created.body.id,null,created.cookie);assert.equal(cancelled.body.state,'cancelled');assert.equal(cancelled.body.context,null);assert.equal(cancelled.body.result,null);assert.equal(f.calls(),0);
});

test('untrusted source URLs and sensitive search filters cannot enter model context',async()=>{
 const unsafe=runtime(async()=>({...released(),references:[{label:'spoof',url:'https://attacker.test/record',role:'RELEASED_RECORD'}]}));
 const bad=await unsafe.request('jobs',input);assert.equal((await unsafe.settleJob(bad.body.id,bad.cookie)).body.result.reasonCode,'CONTEXT_UNAVAILABLE');assert.equal(unsafe.calls(),0);
 const sensitive=runtime(async()=>released()),denied=await sensitive.request('jobs',{...input,term:'exact GPS coordinates of an archaeological site'});
 assert.equal((await sensitive.settleJob(denied.body.id,denied.cookie)).body.result.outcome,'DENY');assert.equal(sensitive.calls(),0);
});
