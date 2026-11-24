import test from 'node:test';import assert from 'node:assert/strict';import {readFile} from 'node:fs/promises';import ts from 'typescript';import {groundFixture} from './kansas-ground-fixtures.mjs';
const url=s=>'data:text/javascript;base64,'+Buffer.from(ts.transpileModule(s,{compilerOptions:{target:ts.ScriptTarget.ES2022,module:ts.ModuleKind.ESNext}}).outputText).toString('base64');
const modelURL=url(await readFile('app/kansas-ground.ts','utf8')),model=await import(modelURL),client=await import(url((await readFile('app/kansas-ground-client.ts','utf8')).replace("from './kansas-ground'","from '"+modelURL+"'")));
test('Ground canonical query and SHA bind only Kansas bounds/fixed96 size and no native EPT query',async()=>{
 assert.deepEqual(model.canonicalGroundQuery([-105,35,-95,42]),{bbox:[-102.2,36.8,-95,40.2],size:96});assert.equal(model.canonicalGroundQuery([-90,38,-89,39]),null);assert.equal(model.canonicalGroundQuery([NaN,38,-96,39]),null);
 const f=groundFixture();assert.equal(await model.groundRequestKey(f.query),f.requestKey);assert.equal(model.groundPath(f.query),'/api/terrain/ground?bbox='+f.query.bbox.join(',')+'&size=96');assert.ok(model.parseGroundReceipt(f.receipt,f.query,f.requestKey));
});
test('Ground schema preserves exact F32 samples/masks and rejects wrong source, query, footprint, state and catalog semantics',()=>{
 const f=groundFixture();for(const mutate of [r=>r.requestKey='b'.repeat(64),r=>r.query.size=64,r=>r.grid.width=64,r=>r.grid.bounds3857[0]+=1,r=>r.grid.cellSize3857[0]*=2,r=>r.grid.ground.pop(),r=>r.grid.ground[0]=9001,r=>r.grid.ground[0]=.1,r=>r.grid.source.requestUrl=r.grid.source.requestUrl.replace('tiff','png'),r=>r.grid.source.provider='NEON',r=>r.grid.source.sha256='bad',r=>r.grid.review.scientific_accuracy_verified=true,r=>r.grid.method.sampling='bilinear',r=>r.grid.source.catalog.candidates=[{}],r=>r.grid.source.catalog.complete=true,r=>r.state='partial']){
  const r=structuredClone(f.receipt);mutate(r);assert.equal(model.parseGroundReceipt(r,f.query,f.requestKey),null);
 }
 const masked=structuredClone(f.receipt);masked.grid.ground[1]=null;masked.grid.excludedValues=1;masked.state='partial';const parsed=model.parseGroundReceipt(masked,f.query,f.requestKey);assert.equal(parsed.grid.ground[1],null);assert.equal(parsed.grid.ground[2],masked.grid.ground[2]);masked.grid.ground.fill(null);masked.state='no-coverage';assert.ok(model.parseGroundReceipt(masked,f.query,f.requestKey));
 const c=structuredClone(f.receipt);Object.assign(c.grid.source.catalog,{state:'available',sha256:'sha256:'+'c'.repeat(64),bytes:1200,retrievedAt:f.receipt.generatedAt,complete:true,candidateCount:1,candidates:[{id:1,name:'Synthetic candidate',demType:1,source:null,verticalDatum:null,acquisitionDate:1600000000000,startDate:null,endDate:'Raw provider date',resolutionX:-.0001,resolutionY:.0001,metadataUrl:'https://example.test/metadata'}]});assert.ok(model.parseGroundReceipt(c,f.query,f.requestKey));c.grid.source.catalog.candidates[0].metadataUrl='javascript:alert(1)';assert.equal(model.parseGroundReceipt(c,f.query,f.requestKey),null);
});
test('actual Mercator north-to-south footprints and center samples are inverse transformed, with spacing explicitly approximate',()=>{
 const f=groundFixture(),g=f.receipt.grid,corners=model.groundCorners(g),first=model.groundCell(g,0),last=model.groundCell(g,9215);assert.equal(corners.length,97*97);assert.ok(Math.abs(corners[0][0]-f.query.bbox[0])<1e-10);assert.ok(Math.abs(corners[0][1]-f.query.bbox[3])<1e-10);assert.ok(first.y3857>last.y3857);assert.ok(first.x3857<last.x3857);assert.equal(first.row,1);assert.equal(last.column,96);assert.equal(last.row,96);assert.equal(first.ground,g.ground[0]);assert.ok(first.approximateSpacingM[0]<g.cellSize3857[0]);assert.equal(model.groundCell(g,-1),null);
});
test('Ground reader uses only bounded same-origin Ground endpoint and rejects non2xx/oversize/schema/cancelled replies',async()=>{
 const old=globalThis.fetch,f=groundFixture(),paths=[];try{
  globalThis.fetch=async path=>{paths.push(path);return Response.json(f.receipt);};const r=await client.readKansasGround(f.query,new AbortController().signal);assert.equal(r.grid.ground[0],f.receipt.grid.ground[0]);assert.deepEqual(paths,[model.groundPath(f.query)]);
  globalThis.fetch=async()=>new Response('not JSON',{status:503});await assert.rejects(client.readKansasGround(f.query,new AbortController().signal),/unavailable/);
  globalThis.fetch=async()=>new Response(' '.repeat(1000001));await assert.rejects(client.readKansasGround(f.query,new AbortController().signal),/budget/);
  globalThis.fetch=async()=>Response.json({...f.receipt,requestKey:'b'.repeat(64)});await assert.rejects(client.readKansasGround(f.query,new AbortController().signal),/validation/);
  globalThis.fetch=async()=>Response.json(f.receipt);const c=new AbortController();await assert.rejects(client.readKansasGround(f.query,c.signal,()=>c.abort()),/abort/i);
 }finally{globalThis.fetch=old;}
});
test('Ground processing polls at2seconds and stops at120seconds with explicit processing state',async t=>{
 t.mock.timers.enable({apis:['setTimeout','Date'],now:Date.parse('2026-11-24T06:00:00Z')});const old=globalThis.fetch,f=groundFixture(),times=[],controller=new AbortController(),waiters=[];let count=0;const observed=n=>count>=n?Promise.resolve():new Promise((resolve,reject)=>waiters.push({n,resolve,reject}));
 globalThis.fetch=async()=>{times.push(Date.now());return Response.json({...f.receipt,state:'processing',grid:null});};const pending=client.readKansasGround(f.query,controller.signal,()=>{count++;for(const w of waiters)if(count>=w.n)w.resolve();});pending.catch(e=>waiters.forEach(w=>w.reject(e)));
 try{await observed(1);t.mock.timers.tick(1999);await Promise.resolve();assert.equal(times.length,1);t.mock.timers.tick(1);await observed(2);for(let i=3;i<=61;i++){t.mock.timers.tick(2000);await observed(i);}assert.equal((await pending).state,'processing');assert.equal(times.length,61);assert.ok(times.every((v,i)=>!i||v-times[i-1]>=2000));}finally{controller.abort();await pending.catch(()=>{});globalThis.fetch=old;t.mock.timers.reset();}
});
