import test from 'node:test';
import assert from 'node:assert/strict';
import {componentHarness,findNode,settle} from './component-harness.mjs';

async function workspace(fetch,props={}){
 const polls=[];
 const h=await componentHarness(new URL('../app/assistant/workspace.tsx',import.meta.url),{'./workspace.module.css':{default:{}}},{fetch,Response,TextEncoder,FormData:class {get(){return null;}},queueMicrotask,setInterval:fn=>{polls.push(fn);return polls.length;},clearInterval:()=>{}});
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
  message(tree).props.onChange({target:{value:'Suggest a fictional story.'}});
  tree=render();assert.equal(send(tree).props.disabled,false);
  assert.equal(findNode(tree,node=>node.type==='section'&&node.props['aria-label']==='Account controls'),undefined);
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
  return Response.json({id:'synthetic-job',state:'completed',deadline:0,result:{outcome:'ABSTAIN',reasonCode:'UNVERIFIED_AI_DISCUSSION',interpretation:'Synthetic only'}});
 },{focus});
 try{
  let tree=render();message(tree).props.onChange({target:{value:'Explain this selected interval.'}});tree=render();
  await findNode(tree,node=>node.type==='form'&&node.props.onSubmit).props.onSubmit({preventDefault(){},currentTarget:{}});
  assert.deepEqual(JSON.parse(JSON.stringify(sent.context)),focus.context);assert.equal(sent.question,'Explain this selected interval.');
  assert.equal(Object.hasOwn(sent,'password'),false);assert.equal(Object.hasOwn(sent,'role'),false);
 }finally{h.dispose();}
});
