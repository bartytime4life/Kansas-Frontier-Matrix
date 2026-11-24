import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';
const catalog=await import('data:text/javascript;base64,'+Buffer.from(ts.transpileModule(await readFile('app/lidar-source-catalog.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64'));
const copy=node=>typeof node==='string'||typeof node==='number'?String(node):[node?.props?.children].flat(Infinity).filter(v=>v!=null).map(copy).join(' ').replace(/\s+/g,' ');
async function panel(){let reads=0,calls=0;const h=await componentHarness('app/lidar-source-panel.tsx',{'./lidar-source-catalog':catalog,'./lidar-source-panel.module.css':{default:new Proxy({},{get:(_t,k)=>k})}},{fetch:()=>{reads++;throw Error('No acquisition');}});const props={anchorId:'lidar-sources',onOpenContinuous:()=>calls++};return{h,props,render:()=>h.render(h.exports.LidarSourcePanel,props),reads:()=>reads,calls:()=>calls};}
test('shared catalog separates connected surface/sample tools from discovery and never acquires on render',async()=>{
 const p=await panel();try{let tree=p.render();p.h.commit();assert.equal(tree.props.id,'lidar-sources');assert.equal(tree.props.open,undefined);assert.equal(p.reads(),0);assert.equal(p.calls(),0);assert.match(copy(tree),/does not install files/);assert.match(copy(tree),/not independent observations/);
 findNode(tree,n=>n.type==='select').props.onChange({target:{value:'ready'}});tree=p.render();const ready=[];findNode(tree,n=>{if(n.type==='li'&&n.props['data-readiness'])ready.push(n);return false;});assert.equal(ready.length,2);assert.deepEqual(ready.map(n=>n.props['data-readiness']),['continuous-terrain','sampled-science']);assert.equal(findNode(ready[0],n=>n.type==='a'&&n.props.href==='/labs/terrain'),undefined,'continuousground is not sent to the Konza sample');assert.ok(findNode(ready[1],n=>n.type==='a'&&n.props.href==='/labs/terrain'));findNode(ready[0],n=>n.type==='button').props.onClick();assert.equal(p.calls(),1);assert.equal(p.reads(),0);
 }finally{p.h.dispose();}
});
test('access-unverified and orbital discoveries have source links and limits, not fabricated ready actions',async()=>{
 const p=await panel();try{let tree=p.render();findNode(tree,n=>n.type==='select').props.onChange({target:{value:'access-unverified'}});tree=p.render();assert.match(copy(tree),/KDOT/);assert.match(copy(tree),/Access not qualified/);assert.equal(findNode(tree,n=>n.type==='button'),undefined);assert.ok(findNode(tree,n=>n.type==='a'&&n.props.target==='_blank'));
 findNode(tree,n=>n.type==='select').props.onChange({target:{value:'discovery'}});tree=p.render();assert.match(copy(tree),/Sparse orbital profiles \/ footprints/);assert.match(copy(tree),/not.*continuous measured terrain/);assert.equal(findNode(tree,n=>n.type==='a'&&n.props.href==='/terrain'),undefined);assert.equal(p.reads(),0);
 }finally{p.h.dispose();}
});
