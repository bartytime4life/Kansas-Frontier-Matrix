import test from 'node:test';
import assert from 'node:assert/strict';
import {componentHarness,findNode,settle} from './component-harness.mjs';

async function workspace(fetch){
 const polls=[];
 const h=await componentHarness(new URL('../app/assistant/workspace.tsx',import.meta.url),{'./workspace.module.css':{default:{}}},{fetch,Response,queueMicrotask,setInterval:fn=>{polls.push(fn);return polls.length;},clearInterval:()=>{}});
 const render=()=>{const tree=h.render(h.exports.default,{});h.commit();return tree;};
 render();await settle();
 return {h,polls,render};
}
const ready=()=>Response.json({configured:true,online:true,ready:true,requiresLogin:false});
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
