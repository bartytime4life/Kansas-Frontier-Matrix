import assert from 'node:assert/strict';
import test from 'node:test';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';
import {componentHarness,findNode,settle} from './component-harness.mjs';

const css={default:new Proxy({},{get:(_,key)=>String(key)})};
const button=(tree,label)=>findNode(tree,n=>n.type==='button'&&JSON.stringify(n.props.children).includes(label));
const ocr=await readFile('public/history/prentis-1909.txt');
function clock(){
 let id=0;const pending=new Map();
 return{pending,set(fn,delay){pending.set(++id,{fn,delay});return id;},clear(id){pending.delete(id);},expire(){for(const [id,entry] of [...pending])if(entry.delay===15000){pending.delete(id);entry.fn();}}};
}
async function module(path,imports={},globals={}){
 const exports={};vm.runInNewContext(ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText,{exports,require(name){assert.ok(name in imports,name);return imports[name];},TextDecoder,Uint8Array,DOMException,AbortController,AbortSignal,crypto,...globals});return exports;
}
async function mount(kind){
 const timers=clock(),requests=[];
 const fetch=(url,options)=>new Promise((resolve,reject)=>{requests.push({url,options,resolve});options.signal.addEventListener('abort',()=>reject(options.signal.reason),{once:true});});
 const globals={fetch,DOMException,setTimeout:timers.set,clearTimeout:timers.clear,URLSearchParams};
 const bounded=await module('app/bounded-json.ts');
 const json=await module('app/browser-json-request.ts',{'./bounded-json':bounded},globals);
 let digest;
 const history=await module('app/history-reader-model.ts',{'./bounded-json':bounded},{crypto:{subtle:{digest(...args){return digest=crypto.subtle.digest(...args);}}}});
 const file=kind==='resources'?'app/underground-resources.tsx':'app/history/prentis-1909/page.tsx';
 const h=await componentHarness(file,kind==='resources'?{
  './underground-resources-model':{RESOURCE_SOURCES:{oilgas:{limitation:'Synthetic provider context',link:'https://example.test/source'}}},'./bounded-json':bounded,'./browser-json-request':json,'./subsurface.module.css':css,
 }:{'../../history-reader-model':history,'../../downloads/workspace.module.css':css,'../../history.module.css':css},globals);
 const props=kind==='resources'?{map:null,bounds:[-100.7,38.3,-100.3,38.7],revision:1,active:true,redacted:false,water:[],onInspect(){}}:{};
 let tree;const render=()=>{tree=h.render(h.exports.default,props);h.commit();return tree;};render();
 if(kind==='resources'){findNode(tree,n=>n.type==='details').props.onToggle({currentTarget:{open:true}});render();}
 return{h,render,requests,timers,get digest(){return digest;},get tree(){return tree;}};
}
async function drain(h,done){for(let i=0;i<20;i++){await settle();h.render();if(done())return;}assert.fail('request did not reach its expected terminal state');}
function stalled(){let controller,cancelled=false;const body=new ReadableStream({start(value){controller=value;},cancel(){cancelled=true;return new Promise(()=>{});}});return{body,get cancelled(){return cancelled;},finish(){try{controller.close();}catch{}}};}
for(const kind of ['resources','history']){
 test(`${kind}: stalled headers become a retryable failure and a later retry succeeds`,async()=>{
  const h=await mount(kind);
  try{
   assert.equal(h.requests.length,1);h.timers.expire();await settle();h.render();
   const retry=button(h.tree,kind==='resources'?'Retry':'Retry loading');assert.ok(retry,'deadline exposes local recovery');
   retry.props.onClick();h.render();assert.equal(h.requests.length,2);
   h.requests[1].resolve(kind==='resources'?Response.json({rows:[],partial:false,rejected:0,retrievedAt:'2026-11-11T12:00:00Z'}):new Response(ocr));
   if(kind==='history'){await drain(h,()=>Boolean(h.digest));await h.digest;}
   await drain(h,()=>kind==='resources'?JSON.stringify(h.tree).includes('No records returned'):String(findNode(h.tree,n=>n.type==='output').props.children).includes('total passages'));h.render();
   assert.equal(button(h.tree,kind==='resources'?'Retry':'Retry loading'),undefined);assert.equal(h.timers.pending.size,0);
   if(kind==='resources')assert.match(JSON.stringify(h.tree),/No records returned/);else assert.match(findNode(h.tree,n=>n.type==='output').props.children,/total.*passages/);
  }finally{h.h.dispose();}
 });
 test(`${kind}: a stalled body is cancelled at the deadline without waiting for cancel completion`,async()=>{
  const h=await mount(kind),stream=stalled();
  try{
   h.requests[0].resolve(new Response(stream.body));await settle();h.timers.expire();await settle();h.render();
   assert.ok(button(h.tree,kind==='resources'?'Retry':'Retry loading'),'body deadline exposes recovery');assert.equal(stream.cancelled,true);assert.equal(h.timers.pending.size,0);
  }finally{h.h.dispose();stream.finish();}
 });
}
