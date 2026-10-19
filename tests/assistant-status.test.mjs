import test from 'node:test';
import assert from 'node:assert/strict';
import * as surfaces from '../app/assistant-surfaces.mjs';
import ts from 'typescript';
import {readFile} from 'node:fs/promises';
import {componentHarness,findNode,settle} from './component-harness.mjs';
const investigation=await import('data:text/javascript;base64,'+Buffer.from(ts.transpileModule(await readFile(new URL('../app/assistant-investigation.ts',import.meta.url),'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64'));

async function workspace(fetch,props={},fields={},extra={}){
 const polls=[];
 const h=await componentHarness(new URL('../app/assistant/workspace.tsx',import.meta.url),{'./workspace.module.css':{default:{}},'../assistant-surfaces.mjs':surfaces,'../assistant-investigation':investigation},{fetch,Response,TextEncoder,FormData:class {get(name){return fields[name]??null;}},queueMicrotask,setInterval:fn=>{polls.push(fn);return polls.length;},clearInterval:()=>{},...extra});
 const render=(next=props)=>{const tree=h.render(h.exports.default,next);h.commit();return tree;};
 render();await settle();
 return {h,polls,render};
}
const ready=()=>Response.json({configured:true,online:true,ready:true,evidenceSearchAvailable:true,requiresLogin:false});
const text=node=>[node?.props?.children].flat(Infinity).map(value=>typeof value==='string'?value:typeof value==='object'?text(value):'').join(' ');
const status=tree=>findNode(tree,node=>node.props?.role==='status');
const send=tree=>findNode(tree,node=>node.type==='button'&&node.props.children==='Send');
const message=tree=>findNode(tree,node=>node.type==='textarea');
const alert=tree=>findNode(tree,node=>node.props?.role==='alert');
const lifecycleFocus=(record='one')=>({title:'Synthetic '+record,detail:'Synthetic source context',context:{version:1,frame:2026,view:'2D',layers:[],selection:{kind:'knowledge',recordId:record}}});
const deferred=()=>{let resolve,reject;const promise=new Promise((done,fail)=>{resolve=done;reject=fail;});return {promise,resolve,reject};};

test('A to B to A cannot resurrect a late accepted question and its opaque job is cancelled',async()=>{
 const admission=deferred(),cancelled=[],focus=lifecycleFocus();
 const {h,render}=await workspace(async(url,options)=>{
  if(url.endsWith('/status'))return ready();
  if(url.endsWith('/cancel')){cancelled.push(url);return Response.json({cancelled:true});}
  if(options.method==='POST')return admission.promise;
  return Response.json({id:'late-admission',state:'completed',deadline:0,result:{outcome:'ABSTAIN',reasonCode:'UNVERIFIED_AI_DISCUSSION',interpretation:'OBSOLETE_REPLY'}});
 },{focus});
 try{
  let tree=render();message(tree).props.onChange({target:{value:'Preserve this question draft.'}});tree=render();
  const submitted=findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
  render({focus:lifecycleFocus('two')});await settle();render({focus});await settle();
  admission.resolve(Response.json({id:'late-admission'}));await submitted;tree=render();await settle();tree=render();
  assert.deepEqual(cancelled,['/api/ai/jobs/late-admission/cancel']);
  assert.doesNotMatch(text(tree),/OBSOLETE_REPLY/);
  assert.equal(message(tree).props.value,'Preserve this question draft.');
 }finally{h.dispose();}
});

test('accepting a question never erases a newer draft typed while admission was pending',async()=>{
 const admission=deferred();
 const {h,render}=await workspace(async(url,options)=>{
  if(url.endsWith('/status'))return ready();
  if(url.endsWith('/cancel'))return Response.json({cancelled:true});
  if(options.method==='POST')return admission.promise;
  return Response.json({id:'draft-preserving',state:'completed',deadline:0,result:{outcome:'ABSTAIN',reasonCode:'NO_RELEASED_EVIDENCE'}});
 });
 try{
  let tree=render();message(tree).props.onChange({target:{value:'First submitted question.'}});tree=render();
  const submitted=findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
  tree=render();message(tree).props.onChange({target:{value:'Keep this next unsent draft.'}});render();
  admission.resolve(Response.json({id:'draft-preserving'}));await submitted;tree=render();assert.equal(message(tree).props.value,'Keep this next unsent draft.');
 }finally{h.dispose();}
});

test('a result read already in flight cannot revive a request after A to B to A',async()=>{
 const response=deferred(),focus=lifecycleFocus();let reads=0,cancellations=0;
 const {h,render}=await workspace(async(url,options)=>{
  if(url.endsWith('/status'))return ready();
  if(url.endsWith('/cancel')){cancellations++;return Response.json({cancelled:true});}
  if(options.method==='POST')return Response.json({id:'old-read'});
  reads++;return response.promise;
 },{focus});
 try{
  let tree=render();message(tree).props.onChange({target:{value:'Explain the original selection.'}});tree=render();
  await findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
  render();await settle();assert.equal(reads,1);
  render({focus:lifecycleFocus('two')});await settle();render({focus});await settle();
  response.resolve(Response.json({id:'old-read',state:'completed',deadline:0,result:{outcome:'ABSTAIN',reasonCode:'UNVERIFIED_AI_DISCUSSION',interpretation:'OBSOLETE_POLL_REPLY'}}));
  await settle();tree=render();
  assert.equal(cancellations,1);assert.doesNotMatch(text(tree),/OBSOLETE_POLL_REPLY/);
 }finally{h.dispose();}
});

test('Stop remains available during admission and cancellation is claimed only after acknowledgement',async()=>{
 const admission=deferred(),cancellation=deferred();
 const {h,render}=await workspace(async(url,options)=>{
  if(url.endsWith('/status'))return ready();
  if(url.endsWith('/cancel'))return cancellation.promise;
  if(options.method==='POST')return admission.promise;
  throw new Error('A stopped question must not begin polling');
 },{focus:lifecycleFocus()});
 try{
  let tree=render();message(tree).props.onChange({target:{value:'Stop this pending request.'}});tree=render();
  const submitted=findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
  tree=render();const stop=findNode(tree,node=>node.type==='button'&&node.props.children==='Stop');assert.ok(stop);assert.equal(stop.props.disabled,false);stop.props.onClick();
  tree=render();assert.match(text(tree),/not yet confirmed/i);assert.doesNotMatch(text(tree),/Question cancelled\./);
  admission.resolve(Response.json({id:'stop-before-accept'}));await settle();tree=render();assert.doesNotMatch(text(tree),/Question cancelled\./);
  cancellation.resolve(Response.json({cancelled:true}));await submitted;await settle();tree=render();assert.match(text(tree),/cancellation confirmed/i);
 }finally{h.dispose();}
});

test('guest readiness does not wait for the separate account request',async()=>{
 const {h,render}=await workspace(url=>url.includes('/api/pc-ai/')?new Promise(()=>{}):Promise.resolve(ready()));
 try{
  let tree=render();assert.equal(text(status(tree)),'Qwen3 0.6B ready');
  assert.equal(findNode(tree,node=>node.type==='select'&&node.props.name==='depth').props.defaultValue,'expanded');
  message(tree).props.onChange({target:{value:'Suggest a fictional story.'}});
  tree=render();assert.equal(send(tree).props.disabled,false);
  assert.equal(findNode(tree,node=>node.type==='section'&&node.props['aria-label']==='Account controls'),undefined);
 }finally{h.dispose();}
});

test('a limited reply offers continuation only for the latest turn with unchanged source context',async()=>{
 let sequence=0;
 const focus={context:{version:1,frame:2026,view:'2D',layers:[],selection:null},title:'Map view',detail:'Display context'};
 const {h,render}=await workspace(async(url,options)=>{
  if(url.includes('/api/pc-ai/'))return Response.json({configured:false,account:null});
  if(url.endsWith('/status'))return ready();
  if(options.method==='POST')return Response.json({id:'synthetic-job-'+(++sequence)});
  return Response.json({id:url.split('/').at(-1),state:'completed',deadline:0,result:{outcome:'ABSTAIN',reasonCode:'UNVERIFIED_AI_DISCUSSION',answer:null,interpretation:'Synthetic partial reply.',outputLimited:true,followUpQuestion:'Would you like a practical example?'}});
 },{focus});
 try{
  let tree=render();message(tree).props.onChange({target:{value:'Explain map context.'}});tree=render();
  await findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
  tree=render();await settle();tree=render();const next=findNode(tree,node=>node.type==='button'&&node.props.children==='Continue reply');assert.equal(next.props.disabled,false);next.props.onClick();
  tree=render();assert.match(message(tree).props.value,/Finish the explanation/);assert.match(text(tree),/Would you like a practical example\?/);
  message(tree).props.onChange({target:{value:'Explain a second topic.'}});tree=render();
  await findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
  tree=render();await settle();tree=render();
  assert.equal(findNode(tree,node=>node.type==='button'&&node.props.children==='Continue reply').props.disabled,true);
  assert.ok(findNode(tree,node=>node.type==='button'&&node.props.children==='Continue reply'&&node.props.disabled===false));
  tree=render({focus:{...focus,context:{...focus.context,frame:2025}}});
  assert.equal(findNode(tree,node=>node.type==='button'&&node.props.children==='Continue reply').props.disabled,true);
  assert.equal(findNode(tree,node=>node.type==='button'&&node.props.children==='Continue reply'&&node.props.disabled===false),undefined);
   tree=render({focus});assert.equal(findNode(tree,node=>node.type==='button'&&node.props.children==='Continue reply'&&node.props.disabled===false),undefined,'returning to the same serialized context does not revive an earlier generation');
 }finally{h.dispose();}
});

test('hiding and reopening unchanged chat preserves completed compatible follow-ups',async()=>{
 const focus=lifecycleFocus();
 const {h,render}=await workspace(async(url,options)=>{
  if(url.endsWith('/status'))return ready();
  if(options.method==='POST')return Response.json({id:'compatible-completed'});
  return Response.json({id:'compatible-completed',state:'completed',deadline:0,result:{outcome:'ABSTAIN',reasonCode:'UNVERIFIED_AI_DISCUSSION',interpretation:'Synthetic limited reply.',outputLimited:true}});
 },{focus});
 try{
  let tree=render();message(tree).props.onChange({target:{value:'Explain this selected source.'}});tree=render();
  await findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});render();await settle();tree=render();
  const continuation=tree=>findNode(tree,node=>node.type==='button'&&node.props.children==='Continue reply');
  assert.equal(continuation(tree).props.disabled,false);
  render({focus,active:false});tree=render({focus,active:true});assert.equal(continuation(tree).props.disabled,false);
  render({focus:lifecycleFocus('other')});tree=render({focus});assert.equal(continuation(tree).props.disabled,true,'a real context A to B to A still invalidates the older follow-up');
 }finally{h.dispose();}
});

test('failed status becomes a visible error, keeps the draft, and recovers on retry',async()=>{
 let connected=false;
 const {h,polls,render}=await workspace(async url=>url.includes('/api/pc-ai/')?Response.json({configured:false,account:null}):connected?ready():Response.json({reasonCode:'AI_UNAVAILABLE'},{status:503}));
 try{
  let tree=render();assert.equal(text(status(tree)),'AI connection unavailable');
  assert.match(text(alert(tree)),/Could not connect/);
  message(tree).props.onChange({target:{value:'Keep this draft.'}});
  tree=render();assert.equal(send(tree).props.disabled,true);assert.equal(message(tree).props.value,'Keep this draft.');
  connected=true;polls[0]();await settle();tree=render();
  assert.equal(text(status(tree)),'Qwen3 0.6B ready');assert.equal(alert(tree),undefined);
  assert.equal(message(tree).props.value,'Keep this draft.');assert.equal(send(tree).props.disabled,false);
 }finally{h.dispose();}
});

test('origin holds show an owner setup message without exposing raw server errors',async()=>{
 const {h,render}=await workspace(async url=>url.includes('/api/pc-ai/')?Response.json({configured:false,account:null}):Response.json({reasonCode:'AI_ORIGIN_HOLD'},{status:503}));
 try{
  const tree=render();assert.match(text(alert(tree)),/site owner/);
  assert.doesNotMatch(text(tree),/AI_ORIGIN_HOLD/);assert.equal(send(tree).props.disabled,true);
 }finally{h.dispose();}
});

test('evidence mode stays usable when the model is offline and switching modes preserves the draft',async()=>{
 const {h,render}=await workspace(async url=>url.includes('/api/pc-ai/')?Response.json({configured:false,account:null}):Response.json({configured:true,online:false,ready:false,evidenceSearchAvailable:true,requiresLogin:false}));
 try{
  let tree=render();assert.equal(text(status(tree)),'AI unavailable');
  assert.match(text(tree),/Choose Find evidence/);
  message(tree).props.onChange({target:{value:'Find river records.'}});
  tree=render();assert.equal(send(tree).props.disabled,true);
  findNode(tree,node=>node.type==='select'&&node.props.name==='mode').props.onChange({target:{value:'evidence'}});
  tree=render();assert.equal(text(status(tree)),'Evidence search available');
  assert.equal(findNode(tree,node=>node.type==='button'&&node.props.children==='Search').props.disabled,false);
  assert.equal(message(tree).props.value,'Find river records.');
  assert.match(text(tree),/Released records · no model required/);
  findNode(tree,node=>node.type==='select'&&node.props.name==='mode').props.onChange({target:{value:'explore'}});
  tree=render();assert.equal(send(tree).props.disabled,true);assert.equal(message(tree).props.value,'Find river records.');
 }finally{h.dispose();}
});

test('evidence search fails closed when its capability is missing or the runtime is disabled',async()=>{
 for(const chatStatus of [{configured:true,online:true,ready:true},{configured:false,online:false,ready:false,evidenceSearchAvailable:true}]){
  const {h,render}=await workspace(async url=>url.includes('/api/pc-ai/')?Response.json({configured:false,account:null}):Response.json(chatStatus));
  try{
   let tree=render();message(tree).props.onChange({target:{value:'Find river records.'}});
   findNode(tree,node=>node.type==='select'&&node.props.name==='mode').props.onChange({target:{value:'evidence'}});
   tree=render();assert.equal(findNode(tree,node=>node.type==='button'&&node.props.children==='Search').props.disabled,true);
  }finally{h.dispose();}
 }
});


test('selection context is visible without sign-in and changing samples preserves the draft',async()=>{
 const focus={context:{version:1,frame:2026,view:'2D',layers:[],selection:{kind:'subsurface',tileId:'tile-160-255',recordId:'core-one',intervalIndex:1}},title:'Synthetic sample one',detail:'10–40 ft · synthetic shale · source context'};
 const {h,render}=await workspace(async url=>url.includes('/api/pc-ai/')?Response.json({configured:false,account:null}):ready(),{focus});
 try{
  let tree=render();assert.match(text(tree),/Synthetic sample one/);assert.match(text(tree),/No login needed/);
  assert.equal(findNode(tree,node=>node.type==='button'&&node.props.children==='Log in'),undefined);
  message(tree).props.onChange({target:{value:'Explain this interval.'}});
  tree=render({focus:{...focus,title:'Synthetic sample two',detail:'20–30 ft · synthetic sand'}});
  assert.match(text(tree),/Synthetic sample two/);assert.equal(message(tree).props.value,'Explain this interval.');
  assert.equal(send(tree).props.disabled,false);
  assert.equal(findNode(tree,node=>node.type==='section'&&node.props['aria-label']==='Account controls'),undefined);
 }finally{h.dispose();}
});

test('a submitted question carries the current selected interval without account credentials',async()=>{
 const focus={context:{version:1,frame:2026,view:'2D',layers:[],selection:{kind:'subsurface',tileId:'tile-160-255',recordId:'core-one',intervalIndex:1}},title:'Synthetic sample one',detail:'Synthetic shale'};let sent;
 const {h,render}=await workspace(async(url,options)=>{
  if(url.includes('/api/pc-ai/'))return Response.json({configured:false,account:null});
  if(url.endsWith('/status'))return ready();
  if(options.method==='POST'){sent=JSON.parse(options.body);return Response.json({id:'synthetic-job'});}
  return Response.json({id:'synthetic-job',state:'completed',deadline:0,result:{outcome:'ABSTAIN',reasonCode:'SOURCE_CONTEXT_ONLY',answer:null,interpretation:null,sourceSummary:'Synthetic source: collection date not established.'}});
 },{focus});
 try{
  let tree=render();message(tree).props.onChange({target:{value:'Explain this selected interval.'}});tree=render();
  await findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
  assert.deepEqual(JSON.parse(JSON.stringify(sent.context)),focus.context);assert.equal(sent.question,'Explain this selected interval.');
  assert.equal(Object.hasOwn(sent,'password'),false);assert.equal(Object.hasOwn(sent,'role'),false);
  tree=render();await settle();tree=render();assert.match(text(tree),/SOURCE CONTEXT/);assert.match(text(tree),/Source summary · not admitted evidence/);assert.match(text(tree),/collection date not established/);assert.doesNotMatch(text(tree),/Generated discussion · unverified/);
 }finally{h.dispose();}
});

test('the visitor question supplies search terms and status retry never resubmits an accepted job',async()=>{
 const focus={title:'Selected source title',detail:'Synthetic only',context:{version:1,frame:2026,view:'Page',surface:'knowledge-record',layers:[],selection:{kind:'knowledge',recordId:'synthetic-one'}}};
 let posts=0,reads=0,sent;
 const {h,render}=await workspace(async(url,options)=>{
  assert.equal(url.includes('/api/pc-ai/'),false);
  if(url.endsWith('/status'))return ready();
  if(options.method==='POST'){posts++;sent=JSON.parse(options.body);return Response.json({id:'synthetic-job'});}
  reads++;if(reads===1)throw Error('interrupted');
  return Response.json({id:'synthetic-job',state:'completed',deadline:0,result:{outcome:'ABSTAIN',reasonCode:'UNVERIFIED_AI_DISCUSSION',interpretation:'Synthetic only'}});
 },{focus});
 try{
  let tree=render();message(tree).props.onChange({target:{value:'What limits this observation?'}});tree=render();
  await findNode(tree,n=>n.type==='form'&&n.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
  tree=render();await settle();tree=render();
  assert.equal(sent.term,'What limits this observation?');assert.equal(posts,1);assert.equal(message(tree).props.value,'');
  message(tree).props.onChange({target:{value:'Keep the next draft.'}});tree=render();
  findNode(tree,n=>n.type==='button'&&n.props.children==='Retry status').props.onClick();tree=render();await settle();tree=render();
  assert.equal(posts,1);assert.equal(reads,2);assert.equal(message(tree).props.value,'Keep the next draft.');assert.match(text(tree),/Synthetic only/);
 }finally{h.dispose();}
});

test('read pressure honors Retry-After and retries the accepted job without losing the next draft',async()=>{
 let posts=0,reads=0;const timers=[];
 const {h,render}=await workspace(async(url,options)=>{
  if(url.endsWith('/status'))return ready();
  if(options.method==='POST'){posts++;return Response.json({id:'synthetic-job'});}
  if(++reads===1)return Response.json({reasonCode:'AI_READ_RATE_LIMIT'},{status:429,headers:{'Retry-After':'60'}});
  return Response.json({id:'synthetic-job',state:'completed',deadline:0,result:{outcome:'ABSTAIN',reasonCode:'SOURCE_CONTEXT_ONLY',sourceSummary:'Synthetic source summary only.'}});
 },{}, {},{setTimeout:(fn,ms)=>{timers.push({fn,ms});return timers.length;},clearTimeout:()=>{}});
 try{
  let tree=render();message(tree).props.onChange({target:{value:'Explain this record.'}});tree=render();
  await findNode(tree,n=>n.type==='form'&&n.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
  tree=render();await settle();tree=render();assert.match(text(alert(tree)),/source checks are busy.*accepted question is retained/);
  assert.equal(timers.at(-1).ms,60000);assert.equal(posts,1);
  message(tree).props.onChange({target:{value:'Keep this next draft.'}});tree=render();
  await timers.at(-1).fn();await settle();tree=render();
  assert.equal(posts,1);assert.equal(reads,2);assert.equal(message(tree).props.value,'Keep this next draft.');assert.match(text(tree),/Synthetic source summary only/);
 }finally{h.dispose();}
});

test('successful cancellation remains usable when follow-up result reads are throttled',async()=>{
 let reads=0,posts=0,cancels=0;
 const {h,render}=await workspace(async(url,options)=>{
  if(url.endsWith('/status'))return ready();
  if(url.endsWith('/cancel')){cancels++;return Response.json({cancelled:true});}
  if(options.method==='POST'){posts++;return Response.json({id:'synthetic-job'});}
  if(++reads>2)return Response.json({reasonCode:'AI_READ_RATE_LIMIT'},{status:429,headers:{'Retry-After':'60'}});
  return Response.json({id:'synthetic-job',state:'running',deadline:Date.now()+60000,result:null});
 });
 try{
  let tree=render();message(tree).props.onChange({target:{value:'Explain this record.'}});tree=render();
  await findNode(tree,n=>n.type==='form'&&n.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
  tree=render();await settle();tree=render();
  message(tree).props.onChange({target:{value:'Keep my next draft.'}});tree=render();const beforeCancel=reads;
  await findNode(tree,n=>n.type==='button'&&n.props.children==='Stop').props.onClick();tree=render();
  assert.equal(cancels,1);assert.equal(posts,1);assert.equal(reads,beforeCancel,'successful cancellation must not depend on another read');
  assert.equal(findNode(tree,n=>n.type==='button'&&n.props.children==='Stop'),undefined);
  assert.equal(send(tree).props.disabled,false);assert.equal(message(tree).props.value,'Keep my next draft.');
 }finally{h.dispose();}
});

test('a selected sample can resolve a source summary while inference is offline, without enabling ordinary discussion',async()=>{
 const focus={context:{version:1,frame:2026,view:'Underground',layers:[],selection:{kind:'subsurface',recordId:'synthetic-core'}},title:'Synthetic core',detail:'Original source'};
 let payload;
 const {h,render}=await workspace(async(url,options)=>{
  if(url.endsWith('/status'))return Response.json({configured:true,online:false,ready:false,evidenceSearchAvailable:true,requiresLogin:false});
  if(options.method==='POST'){payload=JSON.parse(options.body);return Response.json({id:'source-job'});}
  return Response.json({id:'source-job',state:'completed',deadline:0,result:{outcome:'ABSTAIN',reasonCode:'SOURCE_CONTEXT_ONLY',answer:null,interpretation:null,sourceSummary:'Synthetic recorded interval; collection date unknown.',followUpQuestion:'Would you like to inspect its original intervals?'}});
 },{focus},{mode:'explore',depth:'expanded'});
 try{
  let tree=render();assert.equal(text(status(tree)),'Source summary available');assert.match(text(tree),/do not require the AI model/);
  message(tree).props.onChange({target:{value:'Explain this source.'}});tree=render();assert.equal(send(tree).props.disabled,false);
  await findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
  tree=render();await settle();tree=render();assert.deepEqual(payload.context,focus.context);assert.match(text(tree),/Source summary · not admitted evidence/);assert.match(text(tree),/collection date unknown/);
  tree=render({focus:{...focus,context:{...focus.context,selection:null}}});message(tree).props.onChange({target:{value:'General discussion.'}});tree=render({focus:{...focus,context:{...focus.context,selection:null}}});
  assert.equal(text(status(tree)),'AI unavailable');assert.equal(send(tree).props.disabled,true);
 }finally{h.dispose();}
});

test('a withheld repeated continuation explains the limit and leaves no enabled continuation button',async()=>{
 let sequence=0;
 const {h,render}=await workspace(async(url,options)=>{
  if(url.endsWith('/status'))return ready();
  if(options.method==='POST')return Response.json({id:'turn-'+(++sequence)});
  return Response.json({id:url.split('/').at(-1),state:'completed',deadline:0,result:sequence===1?{outcome:'ABSTAIN',reasonCode:'UNVERIFIED_AI_DISCUSSION',answer:null,interpretation:'Synthetic limited explanation.',outputLimited:true}:{outcome:'ABSTAIN',reasonCode:'MODEL_CONTINUATION_REPEATED',answer:null,interpretation:null,followUpQuestion:'Would you like to ask a narrower question?'}});
 });
 try{
  let tree=render();message(tree).props.onChange({target:{value:'Explain the display.'}});tree=render();
  await findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});tree=render();await settle();tree=render();
  findNode(tree,node=>node.type==='button'&&node.props.children==='Continue reply').props.onClick();tree=render();
  await findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});tree=render();await settle();tree=render();
  assert.match(text(tree),/duplicate was withheld/);assert.match(text(tree),/Ask a narrower question/);
  assert.equal(findNode(tree,node=>node.type==='button'&&node.props.children==='Continue reply'&&node.props.disabled===false),undefined);
 }finally{h.dispose();}
});

test('a repeated ordinary follow-up explains withholding and offers no duplicate draft or continuation',async()=>{
 const {h,render}=await workspace(async(url,options)=>{
  if(url.endsWith('/status'))return ready();
  if(options.method==='POST')return Response.json({id:'repeated-followup'});
  return Response.json({id:'repeated-followup',state:'completed',deadline:0,result:{outcome:'ABSTAIN',reasonCode:'MODEL_FOLLOWUP_REPEATED',answer:null,interpretation:null}});
 });
 try{
  let tree=render();message(tree).props.onChange({target:{value:'That did not answer my date question.'}});tree=render();
  await findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});tree=render();await settle();tree=render();
  assert.match(text(tree),/instead of answering the follow-up/);assert.match(text(tree),/duplicate was withheld/);
  for(const label of ['Continue reply','Copy draft outline'])assert.equal(findNode(tree,node=>node.type==='button'&&node.props.children===label),undefined);
 }finally{h.dispose();}
});

const exportFocus={title:'Synthetic selected interval',detail:'Original source context',context:{version:1,frame:2026,view:'2D',layers:[],selection:{kind:'subsurface',tileId:'tile-160-255',recordId:'synthetic-one',intervalIndex:1}}};
const exportJob=()=>({id:'synthetic-export',state:'completed',deadline:0,checkedAt:'2026-10-18T06:00:00Z',sourceRevision:'sha256:'+'a'.repeat(64),releaseId:null,result:{outcome:'ABSTAIN',reasonCode:'SOURCE_CONTEXT_ONLY',answer:null,interpretation:null,sourceSummary:'Synthetic interval: 10–40 ft. Not admitted evidence.'},context:{label:'synthetic-one',boundary:'KGS source context, not admitted evidence',references:[{label:'KGS original',url:'https://www.kgs.ku.edu/',role:'SOURCE_CONTEXT'}]}});
async function submitExportQuestion(render){
 let tree=render();message(tree).props.onChange({target:{value:'Explain the selected interval.'}});tree=render();
 await findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
 render();await settle();return render();
}
test('copy rechecks the existing job, uses its submitted selection after focus changes, and omits unrelated history',async()=>{
 let reads=0,posts=0,copied='';
 const {h,render}=await workspace(async(url,options)=>{
  if(url.endsWith('/status'))return ready();
  if(options.method==='POST'){posts++;return Response.json({id:'synthetic-export'});}
  reads++;return Response.json(exportJob());
 },{focus:exportFocus},{},{navigator:{clipboard:{writeText:async value=>{copied=value;}}}});
 try{
  let tree=await submitExportQuestion(render);const initialReads=reads;
  tree=render({focus:{...exportFocus,context:{...exportFocus.context,frame:2025,selection:{...exportFocus.context.selection,intervalIndex:0}}}});
  findNode(tree,node=>node.type==='button'&&node.props.children==='Copy investigation').props.onClick();
  for(let attempt=0;attempt<20;attempt++){
   await new Promise(resolve=>setImmediate(resolve));tree=render();
   if(/Investigation copied\./.test(text(tree)))break;
  }
  assert.equal(reads,initialReads+1);assert.equal(posts,1);assert.match(copied,/10–40 ft/);assert.match(copied,/Map display year: 2026/);assert.match(copied,/intervalIndex.*1/);assert.doesNotMatch(copied,/Map display year: 2025/);assert.match(text(tree),/Investigation copied\. Sources rechecked; draft only, not published\./);
 }finally{h.dispose();}
});
test('withdrawal at export replaces cached source text and produces a withheld draft; failed rechecks copy nothing',async()=>{
 for(const failure of ['withdrawn','offline']){
  let exporting=false,copied='';
  const {h,render}=await workspace(async(url,options)=>{
   if(url.endsWith('/status'))return ready();
   if(options.method==='POST')return Response.json({id:'synthetic-export'});
   if(exporting&&failure==='offline')return Response.json({reasonCode:'AI_READ_BUSY'},{status:429,headers:{'Retry-After':'2'}});
   return Response.json(exporting?{...exportJob(),context:null,sourceRevision:null,result:{outcome:'ABSTAIN',reasonCode:'RELEASE_CHANGED',answer:null,interpretation:null}}:exportJob());
  },{focus:exportFocus},{},{navigator:{clipboard:{writeText:async value=>{copied=value;}}}});
  try{
   let tree=await submitExportQuestion(render);exporting=true;
   findNode(tree,node=>node.type==='button'&&node.props.children==='Copy investigation').props.onClick();await settle();tree=render();
   if(failure==='withdrawn'){assert.match(copied,/RELEASE_CHANGED/);assert.doesNotMatch(copied,/10–40 ft/);assert.doesNotMatch(text(tree),/Synthetic interval: 10–40 ft/);}
   else{assert.equal(copied,'');assert.match(text(alert(tree)),/Sources must be rechecked first/);assert.match(text(tree),/Explain the selected interval/);}
  }finally{h.dispose();}
 }
});
test('JSON download contains only the checked investigation and never resubmits or invokes inference',async()=>{
 const urls=[],anchors=[];let posts=0;
 class DownloadUrl extends URL{static createObjectURL(blob){urls.push(blob);return 'blob:synthetic';}static revokeObjectURL(){}}
 const document={body:{append(){}},createElement(){const anchor={click(){anchors.push(this);},remove(){}};return anchor;}};
 const {h,render}=await workspace(async(url,options)=>{
  if(url.endsWith('/status'))return ready();
  if(options.method==='POST'){posts++;return Response.json({id:'synthetic-export'});}
  return Response.json(exportJob());
 },{focus:exportFocus},{},{URL:DownloadUrl,Blob,document});
 try{
  const tree=await submitExportQuestion(render);findNode(tree,node=>node.type==='button'&&node.props.children==='Download investigation JSON').props.onClick();await settle();
  assert.equal(posts,1);assert.equal(anchors[0].download,'kfm-investigation-draft.json');
  const draft=JSON.parse(await urls[0].text());assert.equal(draft.status,'DRAFT');assert.equal(draft.scope.selection.intervalIndex,1);assert.equal(draft.result.answer,null);assert.match(draft.result.sourceSummary,/10–40 ft/);
 }finally{h.dispose();}
});

test('obsolete export and recheck completions cannot unlock a newer admission or publish a stale copy',async()=>{
 for(const action of ['Copy investigation','Recheck sources']){
  const oldRead=deferred(),admission=deferred();let reads=0,posts=0,copied='';
  const {h,render}=await workspace(async(url,options)=>{
   if(url.endsWith('/status'))return ready();
   if(url.endsWith('/cancel'))return Response.json({cancelled:true});
   if(options.method==='POST'){posts++;return posts===1?Response.json({id:'synthetic-export'}):admission.promise;}
   reads++;return reads===1?Response.json(exportJob()):oldRead.promise;
  },{focus:exportFocus},{},{navigator:{clipboard:{writeText:async value=>{copied=value;}}}});
  try{
   let tree=await submitExportQuestion(render);const operation=findNode(tree,node=>node.type==='button'&&node.props.children===action).props.onClick();
   tree=render({focus:lifecycleFocus('new-source')});await settle();tree=render({focus:lifecycleFocus('new-source')});
   message(tree).props.onChange({target:{value:'Keep the new request busy.'}});tree=render({focus:lifecycleFocus('new-source')});
   const submitted=findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
   assert.equal(posts,2,'scope change releases the obsolete read without waiting for a signal-ignoring transport');
   oldRead.resolve(Response.json(exportJob()));await operation;await settle();tree=render({focus:lifecycleFocus('new-source')});
   assert.equal(copied,'');assert.equal(findNode(tree,node=>node.type==='button'&&node.props.children==='Copy investigation').props.disabled,true,'obsolete finally must preserve newer busy ownership');
   h.dispose();admission.resolve(Response.json({id:'new-admission'}));await submitted;
  }finally{h.dispose();}
 }
});

test('closing the active panel aborts old polls and late failures cannot add alerts or schedule retries',async()=>{
 const oldRead=deferred(),scheduled=[],focus=lifecycleFocus();let signal,cancels=0;
 const {h,render}=await workspace(async(url,options)=>{
  if(url.endsWith('/status'))return ready();
  if(url.endsWith('/cancel')){cancels++;return Response.json({cancelled:true});}
  if(options.method==='POST')return Response.json({id:'closing-job'});
  signal=options.signal;return oldRead.promise;
 },{focus},{},{setTimeout:(callback,delay)=>{scheduled.push(delay);return scheduled.length;},clearTimeout:()=>{}});
 try{
  let tree=render();message(tree).props.onChange({target:{value:'Explain this source.'}});tree=render();
  await findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});render();await settle();
  render({focus,active:false});assert.equal(signal.aborted,true);await settle();
  oldRead.reject(new Error('OBSOLETE_NETWORK_FAILURE'));await settle();tree=render({focus,active:false});
  assert.equal(cancels,1);assert.equal(alert(tree),undefined);assert.deepEqual(scheduled,[]);
 }finally{h.dispose();}
});

test('unmounting before admission still cancels a late observable ID without restoring the question',async()=>{
 const admission=deferred(),cancelled=[];
 const {h,render}=await workspace(async(url,options)=>{
  if(url.endsWith('/status'))return ready();
  if(url.endsWith('/cancel')){cancelled.push(url);return Response.json({cancelled:true});}
  if(options.method==='POST')return admission.promise;
  throw new Error('Unmounted admission must not be polled');
 });
 let tree=render();message(tree).props.onChange({target:{value:'Explain this before unmount.'}});tree=render();
 const submitted=findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
 h.dispose();admission.resolve(Response.json({id:'unmounted-admission'}));await submitted;assert.deepEqual(cancelled,['/api/ai/jobs/unmounted-admission/cancel']);
});

test('an actor change invalidates pending admission while retaining the unsent draft',async()=>{
 const admission=deferred(),focus=lifecycleFocus();let account='synthetic-owner',cancels=0;
 const {h,polls,render}=await workspace(async(url,options)=>{
  if(url.includes('/api/pc-ai/'))return Response.json({configured:true,account,role:'administrator'});
  if(url.endsWith('/status'))return ready();
  if(url.endsWith('/cancel')){cancels++;return Response.json({cancelled:true});}
  if(options.method==='POST')return admission.promise;
  throw new Error('Earlier actor request must not be polled');
 },{focus,onAccount(){}});
 try{
  let tree=render();await settle();tree=render();message(tree).props.onChange({target:{value:'Keep my actor-change draft.'}});tree=render();
  const submitted=findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
  account='synthetic-new-owner';await polls[0]();await settle();render();await settle();
  admission.resolve(Response.json({id:'previous-actor'}));await submitted;tree=render();assert.equal(cancels,1);assert.equal(message(tree).props.value,'Keep my actor-change draft.');
 }finally{h.dispose();}
});

test('failed cancellation reports uncertainty while suppressing the old response',async()=>{
 const oldRead=deferred();
 const {h,render}=await workspace(async(url,options)=>{
  if(url.endsWith('/status'))return ready();
  if(url.endsWith('/cancel'))throw new Error('Synthetic unreachable cancellation');
  if(options.method==='POST')return Response.json({id:'uncertain-cancel'});
  return oldRead.promise;
 });
 try{
  let tree=render();message(tree).props.onChange({target:{value:'Explain the old source.'}});tree=render();
  await findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});tree=render();await settle();
  await findNode(tree,node=>node.type==='button'&&node.props.children==='Stop').props.onClick();
  oldRead.resolve(Response.json({id:'uncertain-cancel',state:'completed',result:{outcome:'ABSTAIN',reasonCode:'UNVERIFIED_AI_DISCUSSION',interpretation:'OBSOLETE_CANCEL_REPLY'}}));await settle();tree=render();
  assert.match(text(tree),/cancellation could not be confirmed/i);assert.doesNotMatch(text(tree),/OBSOLETE_CANCEL_REPLY|cancellation confirmed\./i);
 }finally{h.dispose();}
});
