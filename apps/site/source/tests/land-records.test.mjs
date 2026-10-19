import test from "node:test";
import { landFixtures } from "./helpers/land-fixture.mjs";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import ts from "typescript";
const url=text=>'data:text/javascript;base64,'+Buffer.from(ts.transpileModule(text,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64');
const src=await readFile(new URL('../app/land-records.ts',import.meta.url),'utf8'),landUrl=url(src),land=await import(landUrl);
const { bytes, rehash, fixture, clone } = landFixtures(land);
test('complete held bundle verifies original-byte and EvidenceBundle closure without releasing records',async()=>{const v=await fixture();assert.equal((await land.validateLandTransfer(bytes(v))).release_state,'UNRELEASED');assert.equal(land.landRecords(v).length,1);assert.equal(land.landRecords(v)[0].amount.value,'23.10');});
test('self-consistent hash edits cannot forge approval, geometry, source roles, county or sale completion',async()=>{
  const mutations=[r=>r.review_state='APPROVED',r=>r.source_admission='APPROVED',r=>r.geometry={type:'Point',coordinates:[-97,38]},r=>r.county='Reno',r=>r.transaction_status='RECORDED',r=>r.amount.kind='sale_price',r=>r.amount.currency='CAD',r=>r.event_date='2027-01-01',r=>r.sale_completion='CONFIRMED',r=>r.flags=[]];
  for(const edit of mutations){const v=await fixture();edit(v.captures[0].candidate.records[0]);await rehash(v);await assert.rejects(land.validateLandTransfer(bytes(v)),/failed integrity/);}
});
test('capture URLs, authority fields and malformed canonical envelopes fail closed',async()=>{
  for(const edit of [v=>v.authority='RELEASED',v=>v.extra='unrecognized',v=>v.captures[0].manifest.source_url='https://evil.test/private',v=>v.captures[0].manifest.source_url='https://cdn.snco.gov/?%74oken=secret',v=>v.captures[0].manifest.source_url='https://user@cdn.snco.gov/x',v=>v.captures[0].manifest.bytes++,v=>v.captures[0].candidate.records[0].extra=true]){const v=await fixture();edit(v);await rehash(v);await assert.rejects(land.validateLandTransfer(bytes(v)));}
  const v=await fixture();await assert.rejects(land.validateLandTransfer(new TextEncoder().encode(JSON.stringify(v))));
  await assert.rejects(land.validateLandTransfer(new TextEncoder().encode(land.canonicalLand(v).replace('"authority":','"authority":"PRIVATE_REVIEW_ONLY","authority":'))));
});
test('missing, substituted, unused and duplicate evidence refuses the entire bundle',async()=>{
  for(const edit of [v=>delete v.objects[v.captures[0].manifest.payload_sha256],v=>v.objects[v.captures[0].manifest.payload_sha256]=Buffer.from('TAMPER').toString('base64'),v=>v.captures[0].evidence[0].members=[],v=>v.captures.push(clone(v.captures[0])),v=>v.captures[0].candidate.locators={}]){const v=await fixture();edit(v);delete v.transfer_digest;v.transfer_digest=await land.landDigest(v);await assert.rejects(land.validateLandTransfer(bytes(v)));}
});
test('record filters are bounded, stable and reject duplicate or invalid date parameters',async()=>{
  const records=Array.from({length:120},(_,i)=>({event_date:'1901-01-01',record_digest:'sha256:'+String(i).padStart(64,'0'),source_id:'blm-glo',county:'Reno',instrument_type:'patent',source_record_id:'SYNTHETIC-'+i,parties:[],notes:null,legal_description:null}));
  const first=land.filterLandRecords(records,new URLSearchParams());assert.equal(first.records.length,50);assert.equal(first.total,120);assert.equal(land.filterLandRecords(records,new URLSearchParams({after:first.nextCursor})).records[0].source_record_id,'SYNTHETIC-50');
  assert.equal(land.filterLandRecords(records,new URLSearchParams({county:'Shawnee'})).total,0);
  for(const p of ['county=Reno&county=Shawnee','start=1901-02-30','start=1902-01-01&end=1901-01-01','q='+('a'.repeat(151)),'limit=100000','after=bad'])assert.throws(()=>land.filterLandRecords(records,new URLSearchParams(p)));
});
// Execute the actual API adapters with synthetic dispatch, D1 and R2 bindings.
const intakeUrl=url(await readFile(new URL('../app/data-intake.ts',import.meta.url),'utf8').then(t=>'const OFFICIAL_CONTEXT_SOURCES=[],SCIENCE_EVENTS=[],EARTH_ENGINE_DATASETS=[];\n'+t.replace(/^import .*;\n/gm,'')));
globalThis.__land={env:{}};
const serverUrl=url((await readFile(new URL('../app/data-intake-server.ts',import.meta.url),'utf8')).replace('import { env } from "cloudflare:workers";','const env=globalThis.__land.env;').replace('import { getRawDb } from "../db";','const getRawDb=()=>globalThis.__land.db;').replace('import { getChatGPTUser } from "./chatgpt-auth";','const getChatGPTUser=async()=>globalThis.__land.user;').replace('"./data-intake"',JSON.stringify(intakeUrl)));
const ownedUrl=url((await readFile(new URL('../app/land-records-server.ts',import.meta.url),'utf8')).replace('"./land-records"',JSON.stringify(landUrl)).replace('"./data-intake-server"',JSON.stringify(serverUrl)));
const api=await import(url((await readFile(new URL('../app/api/land-records/route.ts',import.meta.url),'utf8')).replace('"../../land-records"',JSON.stringify(landUrl)).replace('"../../data-intake-server"',JSON.stringify(serverUrl))));
const detailApi=await import(url((await readFile(new URL('../app/api/land-records/[id]/route.ts',import.meta.url),'utf8')).replace('"../../../land-records"',JSON.stringify(landUrl)).replace('"../../../land-records-server"',JSON.stringify(ownedUrl)).replace('"../../../data-intake-server"',JSON.stringify(serverUrl))));
const publicApi=await import(url(await readFile(new URL('../app/api/governed/land-records/v1/[view]/route.ts',import.meta.url),'utf8')));
async function runtime(){
  const v=await fixture(),raw=bytes(v);let puts=0;
  const row={id:'11111111-1111-1111-1111-111111111111',ownerKey:(await land.landDigest(new TextEncoder().encode('id:synthetic-user'))).slice(7),sourceId:'land-records',objectKey:'quarantine/test/object',fileBytes:raw.length,fileSha256:(await land.landDigest(raw)).slice(7),status:'submitted'};
  const runtimeState={user:{id:'synthetic-user',email:'synthetic@example.test',displayName:'Synthetic reviewer'},env:{BUCKET:{get:async()=>({size:raw.length,body:new Response(raw).body}),put:async()=>{puts++;},delete:async()=>{}}},db:{batch:async()=>[{meta:{changes:1}},{meta:{changes:1}}],prepare:sql=>({bind:()=>({first:async()=>sql.startsWith('SELECT COUNT')?{n:0}:sql.startsWith('SELECT id ')?null:row,all:async()=>({results:[]}),run:async()=>({})})})}};
  globalThis.__land.user=runtimeState.user;globalThis.__land.db=runtimeState.db;Object.assign(globalThis.__land.env,runtimeState.env);
  return {v,raw,row,puts:()=>puts};
}
function upload(v,origin='https://kfm.test',permission='yes'){const form=new FormData();form.set('title','Synthetic land review');form.set('permission',permission);form.set('file',new Blob([bytes(v)],{type:'application/json'}),'review.json');return new Request('https://kfm.test/api/land-records',{method:'POST',headers:{Origin:origin},body:form});}
test('API enforces sign-in, same-origin uploads and private owner scope before storing bytes',async()=>{
  let state=await runtime();globalThis.__land.user=null;assert.equal((await api.POST(upload(state.v))).status,401);assert.equal(state.puts(),0);
  state=await runtime();assert.equal((await api.POST(upload(state.v,'https://evil.test'))).status,403);assert.equal(state.puts(),0);assert.equal((await api.POST(upload(state.v,'https://kfm.test','no'))).status,400);assert.equal(state.puts(),0);
  assert.equal((await api.POST(upload(state.v))).status,201);assert.equal(state.puts(),1);
  const r=await detailApi.GET(new Request('https://kfm.test/api/land-records/'+state.row.id),{params:Promise.resolve({id:state.row.id})});assert.equal(r.status,200);const body=await r.json();assert.equal(body.publicRecords,0);assert.equal(body.normalizationReview,'PENDING');assert.equal(body.records.length,1);assert.equal(r.headers.get('cache-control'),'private, no-store');
  state.row.ownerKey='different-owner';assert.equal((await detailApi.GET(new Request('https://kfm.test/api/land-records/'+state.row.id),{params:Promise.resolve({id:state.row.id})})).status,404);
});
test('ordinary governed clients receive no candidates even with a signed-in review session',async()=>{await runtime();const r=await publicApi.GET();assert.equal(r.status,403);assert.deepEqual((await r.json()).records,[]);});
test('data and land topics link to the real signed-in workflow',async()=>{for(const p of ['app/data/workspace.tsx','app/layer-workspaces.ts','app/map-toolbar.tsx'])assert.match(await readFile(new URL('../'+p,import.meta.url),'utf8'),/\/data\/land-records/);assert.match(await readFile(new URL('../app/data/land-records/page.tsx',import.meta.url),'utf8'),/requireChatGPTUser/);});
