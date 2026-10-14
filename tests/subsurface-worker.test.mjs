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
const code=(await compile('subsurface-worker')).replace(/^import[^;]+;/m,'const { inKansas, nearbyColumns, areaColumns, displayColumns, validAreaBounds, validBorehole, validPosition } = model;');
const well=(id,date='2000-01-01')=>({id,sourceId:'kgs-wwc5',kind:'well',name:id,coordinates:[-95,39],coordinateReference:'WGS84',locationMethod:'PLSS',sourceUrl:'https://www.kgs.ku.edu/',sourceTime:date,depthUnit:'ft',depthReference:'land-surface',totalDepth:100,intervals:[{top:0,bottom:10,description:'sand'}]});
const bytes=gzipSync(JSON.stringify([well('a'),well('b','2026-01-01'),well('unknown','Unknown'),{...well('invalid'),coordinates:null}]));
const sha=createHash('sha256').update(bytes).digest('hex');
const manifest={version:1,sources:[],tiles:[{id:'one',bounds:[-95.2,38.8,-94.8,39.2],url:'/data/subsurface/tile-one.json.gz',sha256:sha}],counties:[]};
function harness(fetcher) {
 const messages=[];const scope={postMessage:v=>messages.push(v),onmessage:null,location:{origin:"https://kfm-worker.invalid"}};
 const context=vm.createContext({self:scope,model,fetch:fetcher,Blob,Response,AbortController,DecompressionStream,crypto:webcrypto,TextDecoder,console,URL,Uint8Array,Date,setTimeout,clearTimeout});
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
 assert.match(r.error,/source-delivery failure/);
});
test('all missing HTTP tiles are a delivery failure rather than a geological absence',async()=>{
 const h=harness(async url=>url.endsWith('manifest.json')?new Response(JSON.stringify(manifest)):new Response('Not Found',{status:404}));
 h.send({});const r=await wait(h);assert.equal(r.columns.length,0);assert.equal(r.partial,true);assert.match(r.error,/not evidence that no records exist/);
});
test('Kansas extent rejects outside probes; manifests cannot redirect reads to another origin',async()=>{
 const h=harness(async()=>new Response(JSON.stringify(manifest)));h.send({anchor:[0,0]});assert.match((await wait(h)).error,/Kansas/);
 const bad=harness(async()=>new Response(JSON.stringify({...manifest,tiles:[{...manifest.tiles[0],url:'https://example.org/private'}]})));bad.send({});assert.match((await wait(bad)).error,/manifest/);
});
test('foreign worker messages are ignored before any source read',async()=>{
 let reads=0;const h=harness(async()=>{reads++;return new Response(JSON.stringify(manifest));});h.sendForeign({});await sleep();assert.equal(h.messages.length,0);assert.equal(reads,0);
});

test('area queries filter exact bounds before ranking/cap and count temporal holds only inside the frame',async()=>{
 const bounds=[-96,38.5,-95.2,39.3];
 const outside=Array.from({length:60},(_,i)=>well(`outside-${i}`,'2026-01-01'));
 const inside={...well('inside'),coordinates:[-95.9,38.6]};
 const future={...well('future','2026-01-01'),coordinates:[-95.5,39]};
 const data=gzipSync(JSON.stringify([...outside,inside,future])),digest=createHash('sha256').update(data).digest('hex');
 const meta={...manifest,tiles:[{...manifest.tiles[0],bounds:[-96.2,38.2,-94.8,39.6],sha256:digest}]};
 const h=harness(async url=>new Response(url.endsWith('manifest.json')?JSON.stringify(meta):data));
 h.send({kind:'area',bounds,anchor:[-95,39],route:[[-95,39],[-94.9,39.1]],year:2020});const r=await wait(h);
 assert.deepEqual(Array.from(r.columns,c=>c.record.id),['inside']);assert.equal(r.timeHeld,1);assert.deepEqual(Array.from(r.bounds),bounds);assert.match(r.coverage,/selected map area/);assert.equal(r.partial,false);
 assert.ok(r.columns[0].distanceMeters>25000,'area records are not limited to a 25 km probe radius');
});
test('area queries keep the 50-record limit, stable ordering and inclusive rectangular edges',async()=>{
 const bounds=[-95.4,38.6,-94.6,39.4];
 const rows=Array.from({length:60},(_,i)=>({...well(`inside-${String(i).padStart(2,'0')}`),coordinates:[-95,39]}));
 const data=gzipSync(JSON.stringify(rows)),meta={...manifest,tiles:[{...manifest.tiles[0],sha256:createHash('sha256').update(data).digest('hex')}]};
 const h=harness(async url=>new Response(url.endsWith('manifest.json')?JSON.stringify(meta):data));h.send({kind:'area',bounds});const r=await wait(h);
 assert.equal(r.columns.length,50);assert.equal(r.total,60);assert.equal(r.partial,true);assert.equal(r.columns[0].record.id,'inside-00');assert.equal(r.columns.at(-1).record.id,'inside-49');assert.match(r.coverage,/Record limit reached/);
 const edges=bounds.slice(0,2);assert.equal(model.areaColumns([{...well('edge'),coordinates:edges}],bounds).length,1);
 for(const value of [[-95,39,-94,40.01],[-95,39,-94,39],[-200,39,-199,40],[NaN,39,-94,40]])assert.equal(model.validAreaBounds(value),false);
});
test('area queries retain eight-tile request budget and fail closed for invalid bounds',async()=>{
 const tiles=Array.from({length:9},(_,i)=>({...manifest.tiles[0],id:String(i),url:`/data/subsurface/tile-${i}.json.gz`}));let reads=0;
 const h=harness(async url=>{if(url.endsWith('manifest.json'))return new Response(JSON.stringify({...manifest,tiles}));reads++;return new Response(bytes);});
 h.send({kind:'area',bounds:[-95.2,38.8,-94.8,39.2]});const r=await wait(h);assert.equal(reads,8);assert.equal(r.partial,true);assert.match(r.coverage,/9 intersect/);
 h.send({id:2,kind:'area',bounds:[-100,37,-95,40]});assert.match((await wait(h,2)).error,/one degree/);assert.equal(reads,8);
});
test('a canceled area cannot replace later area or source-filter results',async()=>{
 let releaseOld,manifestReads=0;
 const h=harness(async url=>{if(url.endsWith('manifest.json')){if(++manifestReads===1)return new Promise(resolve=>releaseOld=resolve);return new Response(JSON.stringify(manifest));}return new Response(bytes);});
 h.send({id:10,kind:'area',bounds:[-95.2,38.8,-94.8,39.2]});
 const latest=[-95.1,38.9,-94.9,39.1];h.send({id:11,kind:'area',bounds:latest,sources:[]});const r=await wait(h);assert.equal(r.id,11);assert.deepEqual(Array.from(r.bounds),latest);assert.equal(r.columns.length,0);
 releaseOld(new Response(JSON.stringify(manifest)));await sleep();await sleep();assert.equal(h.messages.length,1);
});

test('opening Underground warms only the manifest; the exact area still controls tile reads',async()=>{
 const reads=[],h=harness(async url=>{reads.push(url);return new Response(url.endsWith('manifest.json')?JSON.stringify(manifest):bytes);});
 h.send({id:0,kind:'prepare'});const prepared=await wait(h);assert.equal(prepared.prepared,true);assert.equal('columns' in prepared,false);
 assert.deepEqual(reads,['/data/subsurface/manifest.json']);
 h.send({id:1,kind:'area',bounds:[-95.2,38.8,-94.8,39.2]});const result=await wait(h,2);
 assert.deepEqual(reads,['/data/subsurface/manifest.json','/data/subsurface/tile-one.json.gz?sha256='+sha]);assert.equal(result.columns.length,3);assert.equal(result.rejected,1);
});

test('dense wells cannot crowd eligible cores out of the 50-record area budget',async()=>{
 const core={...well('core-last'),sourceId:'kgs-core',kind:'core',coordinates:[-95.15,39],intervals:[{top:4094,bottom:4893,description:'inventory envelope'}]};
 const rows=[...Array.from({length:70},(_,i)=>well(`well-${i}`)),core];
 const data=gzipSync(JSON.stringify(rows)),meta={...manifest,tiles:[{...manifest.tiles[0],sha256:createHash('sha256').update(data).digest('hex')}]};
 const h=harness(async url=>new Response(url.endsWith('manifest.json')?JSON.stringify(meta):data));
 h.send({kind:'area',bounds:[-95.2,38.8,-94.8,39.2],sources:['kgs-wwc5','kgs-core']});let r=await wait(h);
 assert.equal(r.columns.length,50);assert.equal(r.total,71);assert.equal(r.partial,true);assert.ok(r.columns.some(c=>c.record.id===core.id));
 assert.equal(r.columns.filter(c=>c.record.kind==='well').length,49);assert.match(r.coverage,/represented separately/);
 h.send({id:2,kind:'area',bounds:[-95.2,38.8,-94.8,39.2],sources:['kgs-core']});r=await wait(h,2);assert.deepEqual(Array.from(r.columns,c=>c.record.id),['core-last']);
 h.send({id:3,kind:'area',bounds:[-95.2,38.8,-94.8,39.2],sources:['kgs-core'],year:1833});r=await wait(h,3);assert.equal(r.columns.length,0);assert.equal(r.timeHeld,1);
});
test('inventory search honors source choice and Kansas location without claiming interval eligibility',async()=>{
 const locations=[['core-123','',[-95,39],'one'],['well-123','KS',[-95,39],'one'],['core-123-outside','',[-90,39],'one']];
 const data=gzipSync(JSON.stringify(locations)),meta={...manifest,locator:{url:'/data/subsurface/locator.json.gz',sha256:createHash('sha256').update(data).digest('hex')}};
 const h=harness(async url=>new Response(url.endsWith('manifest.json')?JSON.stringify(meta):data));
 h.send({kind:'search',search:'123',sources:['kgs-core'],year:1833});let r=await wait(h);assert.deepEqual(Array.from(r.matches,x=>x[0]),['core-123']);assert.equal('columns' in r,false);
 h.send({id:2,kind:'search',search:'123',sources:['kgs-wwc5']});r=await wait(h,2);assert.deepEqual(Array.from(r.matches,x=>x[0]),['well-123']);
 h.send({id:3,kind:'search',search:'123',sources:[]});r=await wait(h,3);assert.equal(r.matches.length,0);
});

test('content-addressed reads verify original gzip or exact transparently decoded entities',async()=>{
 const raw=JSON.stringify([well('same')]),packed=gzipSync(raw),sha256=createHash('sha256').update(packed).digest('hex'),decodedSha256=createHash('sha256').update(raw).digest('hex');
 const meta={...manifest,tiles:[{...manifest.tiles[0],sha256,decodedSha256}]};
 for(const entity of [packed,raw]){
  const reads=[],h=harness(async url=>{reads.push(url);return new Response(url.endsWith('manifest.json')?JSON.stringify(meta):entity);});
  h.send({});const r=await wait(h);assert.equal(r.columns[0].record.id,'same');assert.equal(r.failures.length,0);assert.ok(reads[1].endsWith('?sha256='+sha256));
 }
 const altered=harness(async url=>new Response(url.endsWith('manifest.json')?JSON.stringify(meta):JSON.stringify([well('changed')])));
 altered.send({});const bad=await wait(altered);assert.equal(bad.columns.length,0);assert.match(bad.error,/SOURCE_DIGEST_MISMATCH/);
 const noEntityDigest=harness(async url=>new Response(url.endsWith('manifest.json')?JSON.stringify({...meta,tiles:[{...meta.tiles[0],decodedSha256:undefined}]}):raw));
 noEntityDigest.send({});assert.match((await wait(noEntityDigest)).error,/SOURCE_DIGEST_MISMATCH/);
});
test('delivery status is disclosed as a safe bounded code without response content',async()=>{
 const h=harness(async url=>url.endsWith('manifest.json')?new Response(JSON.stringify(manifest)):new Response('private diagnostic body',{status:404}));
 h.send({});const r=await wait(h);assert.match(r.error,/SOURCE_HTTP_404/);assert.doesNotMatch(JSON.stringify(r),/private diagnostic/);
});

test('decoded transport bodies over 5 MB retain the original 25 MB decoded ceiling; overflow cancels before parsing',async()=>{
 const raw=JSON.stringify([well('large')])+' '.repeat(5_100_000),packed=gzipSync(raw);
 const meta={...manifest,tiles:[{...manifest.tiles[0],sha256:createHash('sha256').update(packed).digest('hex'),decodedSha256:createHash('sha256').update(raw).digest('hex')}]};
 const h=harness(async url=>new Response(url.endsWith('manifest.json')?JSON.stringify(meta):raw));h.send({});assert.equal((await wait(h)).columns[0].record.id,'large');
 let canceled=false,reads=0;const oversized=new ReadableStream({pull(controller){reads++;controller.enqueue(new Uint8Array(1_000_000));},cancel(){canceled=true;}});
 const bad=harness(async url=>url.endsWith('manifest.json')?new Response(JSON.stringify(meta)):new Response(oversized));bad.send({});const r=await wait(bad);
 assert.equal(canceled,true);assert.ok(reads<=27);assert.equal(r.columns.length,0);assert.match(r.error,/SOURCE_SIZE_LIMIT/);
});
