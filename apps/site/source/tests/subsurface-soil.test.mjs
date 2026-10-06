import assert from 'node:assert/strict';
import { test } from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
const compile = async path => ts.transpileModule(await readFile(new URL(`../app/${path}.ts`,import.meta.url),'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const bounded=`data:text/javascript;base64,${Buffer.from(await compile('bounded-json')).toString('base64')}`;
const code=(await compile('api/subsurface/soil/route')).replace('"../../../bounded-json"',JSON.stringify(bounded));
const {GET}=await import(`data:text/javascript;base64,${Buffer.from(code).toString('base64')}`);
test('soil endpoint bounds numeric Kansas coordinates before network access',async()=>{
 const original=globalThis.fetch;globalThis.fetch=()=>{throw new Error('unexpected network');};
 try{for(const q of ['', '?lon=x&lat=39','?lon=-95&lat=90','?lon=-95%27DROP&lat=39'])assert.equal((await GET(new Request('https://kfm.example/api/subsurface/soil'+q))).status,400);}finally{globalThis.fetch=original;}
});
test('USDA rows retain separate components, centimetres, capture time and a partial limit',async()=>{
 const original=globalThis.fetch;let sent;
 globalThis.fetch=async (url,options)=>{sent={url,body:JSON.parse(options.body)};return Response.json({Table:[Array(14).fill('column'),...Array.from({length:100},(_,i)=>['1','a','Mapunit',i%2?'2':'3','Component','50','Yes',String(i),'A','0','30','50','20','30'])]});};
 try{const response=await GET(new Request('https://kfm.example/api/subsurface/soil?lon=-95.25&lat=39'));const data=await response.json();assert.equal(response.status,200);assert.equal(data.rows.length,100);assert.equal(data.partial,true);assert.equal(data.depthUnit,'cm');assert.equal(new Set(data.rows.map(r=>r[3])).size,2);assert.ok(data.retrievedAt);assert.equal(sent.url,'https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest');assert.match(sent.body.query,/POINT\(-95.250000 39.000000\)/);}finally{globalThis.fetch=original;}
});
test('malformed and oversized soil responses are unavailable, never an inferred empty soil',async()=>{
 const original=globalThis.fetch;
 try{for(const payload of [{Table:[['wrong']]},{Table:Array(102).fill(Array(14).fill('x'))}]){globalThis.fetch=async()=>Response.json(payload);assert.equal((await GET(new Request('https://kfm.example/api/subsurface/soil?lon=-95&lat=39'))).status,502);}globalThis.fetch=async()=>new Response('x'.repeat(300001));assert.equal((await GET(new Request('https://kfm.example/api/subsurface/soil?lon=-95&lat=39'))).status,502);}finally{globalThis.fetch=original;}
});
