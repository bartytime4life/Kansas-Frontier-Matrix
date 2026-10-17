import test from 'node:test';
import assert from 'node:assert/strict';
import * as surfaces from '../app/assistant-surfaces.mjs';
import {componentHarness,findNode,settle} from './component-harness.mjs';

async function workspace(fetch,props={},fields={},extra={}){
 const polls=[];
 const h=await componentHarness(new URL('../app/assistant/workspace.tsx',import.meta.url),{'./workspace.module.css':{default:{}},'../assistant-surfaces.mjs':surfaces},{fetch,Response,TextEncoder,FormData:class {get(name){return fields[name]??null;}},queueMicrotask,setInterval:fn=>{polls.push(fn);return polls.length;},clearInterval:()=>{},...extra});
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

test('guest readiness does not wait for the separate account request',async()=>{
 const {h,render}=await workspace(url=>url.includes('/api/pc-ai/')?new Promise(()=>{}):Promise.resolve(ready()));
 try{
  let tree=render();assert.equal(text(status(tree)),'SmolLM2 ready');
  assert.equal(findNode(tree,node=>node.type==='select'&&node.props.name==='depth').props.defaultValue,'expanded');
  message(tree).props.onChange({target:{value:'Suggest a fictional story.'}});
  tree=render();assert.equal(send(tree).props.disabled,false);
  assert.equal(findNode(tree,node=>node.type==='section'&&node.props['aria-label']==='Account controls'),undefined);
 }finally{h.dispose();}
});

test('a limited reply offers continuation only while its source context is unchanged',async()=>{
 const focus={context:{version:1,frame:2026,view:'2D',layers:[],selection:null},title:'Map view',detail:'Display context'};
 const {h,render}=await workspace(async(url,options)=>{
  if(url.includes('/api/pc-ai/'))return Response.json({configured:false,account:null});
  if(url.endsWith('/status'))return ready();
  if(options.method==='POST')return Response.json({id:'synthetic-job'});
  return Response.json({id:'synthetic-job',state:'completed',deadline:0,result:{outcome:'ABSTAIN',reasonCode:'UNVERIFIED_AI_DISCUSSION',answer:null,interpretation:'Synthetic partial reply.',outputLimited:true,followUpQuestion:'Would you like a practical example?'}});
 },{focus});
 try{
  let tree=render();message(tree).props.onChange({target:{value:'Explain map context.'}});tree=render();
  await findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
  tree=render();await settle();tree=render();const next=findNode(tree,node=>node.type==='button'&&node.props.children==='Continue reply');assert.equal(next.props.disabled,false);next.props.onClick();
  tree=render();assert.match(message(tree).props.value,/Finish the explanation/);assert.match(text(tree),/Would you like a practical example\?/);
  tree=render({focus:{...focus,context:{...focus.context,frame:2025}}});
  assert.equal(findNode(tree,node=>node.type==='button'&&node.props.children==='Continue reply').props.disabled,true);
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
  assert.equal(text(status(tree)),'SmolLM2 ready');assert.equal(alert(tree),undefined);
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
