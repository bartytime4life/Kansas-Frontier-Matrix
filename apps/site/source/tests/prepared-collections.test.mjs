import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import test from 'node:test';
import ts from 'typescript';
const encode = text => new TextEncoder().encode(text).buffer;
const hash = b => createHash('sha256').update(new Uint8Array(b)).digest('hex');
const url = code => 'data:text/javascript;base64,' + Buffer.from(ts.transpileModule(code, {compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64');
const model = await readFile('app/prepared-collections.ts','utf8');
const pinsSource = await readFile('app/prepared-collection-pins.ts','utf8');
const realPins = (await import(url(pinsSource))).PREPARED_COLLECTIONS;
const payload = encode('station,value,flag\r\nA,M,T\r\n');
const outputs = [{file:'observations.csv',bytes:payload.byteLength,sha256:hash(payload)}];
const manifest = encode(JSON.stringify({profile:'kfm-private-collection-readiness/v1',readiness:'SUPPORTED_FOR_BOUNDED_PRIVATE_PREPARATION',review_state:'PENDING',source_admitted:false,released:false,published:false,outputs}));
const pin = {id:'fixture',title:'Synthetic only',fileCount:2,totalBytes:manifest.byteLength+payload.byteLength,manifestSha256:hash(manifest),members:outputs};
const syntheticPins=url('export const PREPARED_COLLECTIONS = '+JSON.stringify([pin])+';');
const fixture=await import(url(model.replace('"./prepared-collection-pins"',JSON.stringify(syntheticPins))));
const signal=()=>new AbortController().signal;
const files=()=>[{name:'review-manifest.json',webkitRelativePath:'review/review-manifest.json',size:manifest.byteLength,arrayBuffer:async()=>manifest.slice(0)}, {name:'observations.csv',webkitRelativePath:'review/observations.csv',size:payload.byteLength,arrayBuffer:async()=>payload.slice(0)}];
test('real bindings contain only the six exact preparations, no data or hosted fetch locator',()=>{
 assert.equal(realPins.length,6);assert.equal(realPins.reduce((n,p)=>n+p.fileCount,0),60);assert.equal(realPins.reduce((n,p)=>n+p.totalBytes,0),14423973);
 assert.doesNotMatch(model,/fetch\(|XMLHttpRequest|localStorage|indexedDB|innerHTML|eval\(/);
 assert.doesNotMatch(pinsSource,/\/home\/|geometry.*coordinates|api\/|ftp:/);
});
test('whole package closes exact identities before any preview and preserves missing flags',async()=>{
 const old=globalThis.fetch;globalThis.fetch=()=>{throw Error('network forbidden')};
 try {const selection=await fixture.inspectPreparedCollection('fixture',files(),signal());const table=fixture.preparedTable(fixture.preparedText(selection,'observations.csv'));assert.deepEqual(table.rows,[['A','M','T']]);} finally{globalThis.fetch=old;}
});
test('unknown, missing, extra, duplicate, traversing and over-cap selections fail before reads',async()=>{
 for(const alter of [f=>f.slice(1),f=>[...f,f[0]],f=>{f[1]={...f[1],name:'other.csv'};return f;},f=>{f[0].webkitRelativePath='root/../review-manifest.json';return f;},f=>{f[1].size=17*1024**2;return f;}]){
  let reads=0;const list=alter(files());for(const f of list)f.arrayBuffer=async()=>{reads++;return payload};await assert.rejects(fixture.inspectPreparedCollection('fixture',list,signal()));assert.equal(reads,0);
 }
 await assert.rejects(fixture.inspectPreparedCollection('unknown',files(),signal()));
});
test('tampered manifest, same-size changed member and dishonest read sizes are held',async()=>{
 for(const index of [0,1]){const list=files();list[index].arrayBuffer=async()=>{const b=index?payload.slice(0):manifest.slice(0);new Uint8Array(b)[0]^=1;return b};await assert.rejects(fixture.inspectPreparedCollection('fixture',list,signal()),/differs|digest/);}
 const list=files();list[1].arrayBuffer=async()=>payload.slice(0,2);await assert.rejects(fixture.inspectPreparedCollection('fixture',list,signal()),/digest/);
});
test('operator marker is ignored only in a complete bounded package, never rendered or used as authority',async()=>{
 const list=[...files(),{name:'.kfm-copy-plan.json',webkitRelativePath:'review/.kfm-copy-plan.json',size:120,arrayBuffer:async()=>{throw Error('marker must never be read')}}];
 const p=await fixture.inspectPreparedCollection('fixture',list,signal());assert.equal(p.files.size,1);
});
test('abort during pending verification cannot return a selection',async()=>{
 const controller=new AbortController(),list=files();let resolve;list[0].arrayBuffer=()=>new Promise(r=>resolve=r);
 const pending=fixture.inspectPreparedCollection('fixture',list,controller.signal);controller.abort();resolve(manifest);await assert.rejects(pending,/abort/i);
});
test('CSV quoting preserves embedded commas, CRLF, quotes, empty, missing and trace cells',()=>{
 const t=fixture.preparedTable('name,note,value\r\n"A, B","two\nlines and ""quote""",M\r\nC,,0\r\n');assert.deepEqual(t.rows,[['A, B','two\nlines and "quote"','M'],['C','','0']]);
 for(const t of ['a,a\n1,2\n','a,b\n1\n','a\n"unterminated','a\n"closed"x\n','a\n'+ 'x'.repeat(8001)])assert.throws(()=>fixture.preparedTable(t));
});
