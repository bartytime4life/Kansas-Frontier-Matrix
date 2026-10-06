import assert from 'node:assert/strict';
import { test } from 'node:test';
import { readFile } from 'node:fs/promises';
import { gzipSync } from 'node:zlib';
import { createHash, webcrypto } from 'node:crypto';
import vm from 'node:vm';
import ts from 'typescript';
const compile = async name => ts.transpileModule(await readFile(new URL(`../app/${name}.ts`,import.meta.url),'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const materialUrl=`data:text/javascript;base64,${Buffer.from(await compile('subsurface-materials')).toString('base64')}`;
const moduleText=(await compile('subsurface-model')).replace('from "./subsurface-materials"', `from "${materialUrl}"`);
const model=await import(`data:text/javascript;base64,${Buffer.from(moduleText).toString('base64')}`);
const code=(await compile('subsurface-worker')).replace(/^import[^;]+;/m,'const { inKansas, nearbyColumns, validBorehole, validPosition } = model;');
const well=(id,date='2000-01-01')=>({id,sourceId:'kgs-wwc5',kind:'well',name:id,coordinates:[-95,39],coordinateReference:'WGS84',locationMethod:'PLSS',sourceUrl:'https://www.kgs.ku.edu/',sourceTime:date,depthUnit:'ft',depthReference:'land-surface',totalDepth:100,intervals:[{top:0,bottom:10,description:'sand'}]});
const bytes=gzipSync(JSON.stringify([well('a'),well('b','2026-01-01'),well('unknown','Unknown'),{...well('invalid'),coordinates:null}]));
const sha=createHash('sha256').update(bytes).digest('hex');
const manifest={version:1,sources:[],tiles:[{id:'one',bounds:[-95.2,38.8,-94.8,39.2],url:'/data/subsurface/tile-one.json.gz',sha256:sha}],counties:[]};
function harness(fetcher) {
 const messages=[];const scope={postMessage:v=>messages.push(v),onmessage:null,location:{origin:"https://kfm-worker.invalid"}};
 const context=vm.createContext({self:scope,model,fetch:fetcher,Blob,Response,AbortController,DecompressionStream,crypto:webcrypto,console,URL,Uint8Array,Date,setTimeout,clearTimeout});
 vm.runInContext(code,context);
 return {messages,send:q=>scope.onmessage({origin:scope.location.origin,data:{id:1,kind:'probe',anchor:[-95,39],route:[],sources:['kgs-wwc5'],year:2026,...q}}),sendForeign:q=>scope.onmessage({origin:"https://foreign.invalid",data:{id:1,kind:'probe',anchor:[-95,39],route:[],sources:['kgs-wwc5'],year:2026,...q}})};
}
const sleep=()=>new Promise(r=>setTimeout(r,15));
async function wait(h,n=1){for(let i=0;i<100&&h.messages.length<n;i++)await sleep();assert.equal(h.messages.length,n);return h.messages.at(-1);}
test('real gzip integrity, record validation, date holds, and source filters',async()=>{
 const h=harness(async url=>new Response(url.endsWith('manifest.json')?JSON.stringify(manifest):bytes));
 h.send({year:2020});let r=await wait(h);assert.equal(r.columns.length,1);assert.equal(r.columns[0].record.id,'a');assert.equal(r.rejected,1);assert.equal(r.timeHeld,2);
 h.send({id:2,sources:[]});r=await wait(h,2);assert.equal(r.columns.length,0);
});
test('stale or canceled source requests cannot replace a newer result',async()=>{
 let resolveOld;let manifestReads=0;
 const h=harness(async url=>{if(url.endsWith('manifest.json')){manifestReads++;if(manifestReads===1)return new Promise(resolve=>{resolveOld=resolve;});return new Response(JSON.stringify(manifest));}return new Response(bytes);});
 h.send({id:1});h.send({id:2,sources:[]});const r=await wait(h);assert.equal(r.id,2);resolveOld(new Response(JSON.stringify(manifest)));await sleep();await sleep();assert.equal(h.messages.length,1);
});
test('missing and corrupt source tiles give explicit partial coverage with no invented records',async()=>{
 const h=harness(async url=>new Response(url.endsWith('manifest.json')?JSON.stringify(manifest):gzipSync('[]')));
 h.send({});const r=await wait(h);assert.equal(r.columns.length,0);assert.equal(r.partial,true);assert.equal(r.failures.length,1);
});
test('Kansas extent rejects outside probes; manifests cannot redirect reads to another origin',async()=>{
 const h=harness(async()=>new Response(JSON.stringify(manifest)));h.send({anchor:[0,0]});assert.match((await wait(h)).error,/Kansas/);
 const bad=harness(async()=>new Response(JSON.stringify({...manifest,tiles:[{...manifest.tiles[0],url:'https://example.org/private'}]})));bad.send({});assert.match((await wait(bad)).error,/manifest/);
});
test('foreign worker messages are ignored before any source read',async()=>{
 let reads=0;const h=harness(async()=>{reads++;return new Response(JSON.stringify(manifest));});h.sendForeign({});await sleep();assert.equal(h.messages.length,0);assert.equal(reads,0);
});
