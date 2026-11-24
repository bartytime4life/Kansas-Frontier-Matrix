import test from 'node:test';
import assert from 'node:assert/strict';
import {componentHarness,findNode,settle} from './component-harness.mjs';
const Workspace=()=>null,module={default:Workspace};
const gate=()=>{let resolve;const promise=new Promise(r=>resolve=r);return {promise,resolve};};
async function fixture(importer){let imports=0;const deps={};Object.defineProperty(deps,'./workspace',{get(){imports++;return importer();}});const document={body:{},activeElement:null};const h=await componentHarness('app/assistant/loader.tsx',deps,{document,Node:class{}});return {...h,document,count:()=>imports,draw:props=>h.render(h.exports.default,props)};}
test('ordinary map downloads no chat module; first opening shares one import and forwards the latest context',async()=>{
 const g=gate(),h=await fixture(()=>g.promise);assert.equal(h.draw({active:false}),null);h.commit();await settle();assert.equal(h.count(),0);
 const loading=h.draw({active:true});assert.equal(loading.props['aria-busy'],true);h.commit();await settle();assert.equal(h.count(),1);g.resolve(module);await settle();
 const focus={id:'current'},ready=h.draw({active:true,focus});assert.equal(ready.type,Workspace);assert.equal(ready.props.focus,focus);h.commit();
 const hidden=h.draw({active:false,focus});assert.equal(hidden.type,Workspace,'retain same mounted component and its drafts when closed');assert.equal(hidden.props.active,false,'existing job cancellation remains active');h.commit();
 assert.equal(h.draw({active:true}).type,Workspace);assert.equal(h.count(),1);h.dispose();
});
test('closing during download ignores late completion; reopening uses the completed import without downloading twice',async()=>{
 const g=gate(),h=await fixture(()=>g.promise);h.draw({active:true});h.commit();await settle();assert.equal(h.draw({active:false}),null);h.commit();g.resolve(module);await settle();assert.equal(h.draw({active:false}),null);
 h.draw({active:true});h.commit();await settle();assert.equal(h.draw({active:true}).type,Workspace);assert.equal(h.count(),1);h.dispose();
});
test('failed download has an inline retry and does not reveal transport details',async()=>{
 let calls=0;const h=await fixture(()=>{if(++calls===1)throw Error('private-host/token');return module;});h.draw({active:true});h.commit();await settle();const failed=h.draw({active:true});assert.equal(failed.props['aria-busy'],false);assert.equal(findNode(failed,n=>n.type==='p').props.role,'alert');assert.doesNotMatch(JSON.stringify(failed),/private-host/);findNode(failed,n=>n.type==='button').props.onClick();h.draw({active:true});h.commit();await settle();assert.equal(h.draw({active:true}).type,Workspace);h.dispose();
});
test('loading-owned focus transfers to composer, but never steals focus from another tool',async()=>{
 const h=await fixture(()=>module);let focused=0;const inputRef={current:{focus(){focused++;}}};const loading=h.draw({active:true,inputRef});loading.props.onFocusCapture();h.commit();await settle();h.document.activeElement=h.document.body;h.draw({active:true,inputRef});h.commit();assert.equal(focused,1);
 h.document.activeElement={};h.draw({active:false,inputRef});h.commit();h.draw({active:true,inputRef});h.commit();assert.equal(focused,1);h.dispose();
});
