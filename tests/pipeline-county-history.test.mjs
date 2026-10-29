// Synthetic release approvals/keys below are local test fixtures, never production authority.
import test from 'node:test';
import assert from 'node:assert/strict';
import { generateKeyPairSync, randomBytes, sign } from 'node:crypto';
import { mkdtemp, writeFile, readFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { resolve } from 'node:path';
import ts from 'typescript';
import { canonical, sha, recipeDigest, MAX_PACKAGE, ORIGIN, PipelineError } from '../server/pipeline-contract.mjs';
import { signRequest } from '../server/pipeline-auth.mjs';
import { handlePipeline, publicContext, publicArtifact, publicHistory } from '../server/pipeline-handler.mjs';
import { ArtifactFiles } from '../server/pipeline-files.mjs';
import { publish } from '../scripts/pc-pipeline/publisher.mjs';
import { readCountyHistoryReport, normalizeCountyCandidate } from '../server/county-history-candidate.mjs';
import { validateCountyRelease, COUNTY_SOURCE_ID, COUNTY_SOURCE_URL, COUNTY_RIGHTS_URL, COUNTY_LIMITATION, COUNTY_ARCHIVE } from '../server/county-history-release.mjs';
import { componentHarness, findNode } from './component-harness.mjs';
import { captureRequest, fetchCapture } from '../server/ingestion-sources.mjs';
import { normalizeCapture } from '../server/pipeline-normalize.mjs';

const now=Date.now();
const shapes=['43026f03b3d1d5a8020c64aa5a17d765687277311e792208c78d3620e98c35b4','25730b7c0ed9bb300f6dd80e833e3c82f95e23b4e8e639fe263f7eeaaefa13ed','1be56325d28ea82f512d09b8c005e09a20296b0cde6d5f478f9ed1e38bf832e6'];
function product(day='1861-01-29') {
 const p={name:'SYNTHETIC source area',institutionSourceId:'synthetic',sourceVersion:1,sourceState:null,fips:null,sourceCountyType:'County',classificationStatus:'unreviewed_source_label',
  validFrom:'1804-10-01',validToExclusive:'2001-01-01',sourceLastDay:'2000-12-31',sourceDay:day,change:'Synthetic test change',citation:'Synthetic test citation',
  sourceLocators:shapes.map((memberSha256,i)=>({memberSha256,recordNumber:1,kind:i===2?'tsv_data_record_1_based':'shape_dbf_record_1_based'}))};
 return {format:'kfm-curated-county-history-v1',sourceId:COUNTY_SOURCE_ID,sourceUrl:COUNTY_SOURCE_URL,rightsUrl:COUNTY_RIGHTS_URL,archiveSha256:COUNTY_ARCHIVE,
  qualificationReportSha256:'a'.repeat(64),preparedAt:new Date(now).toISOString(),effectiveDay:day,partial:false,evidenceRole:'EXTERNAL_CONTEXT_ONLY',evidenceEligible:false,limitation:COUNTY_LIMITATION,
  coordinateOperation:{id:'EPSG:1188',sourceCrs:'EPSG:4269',targetCrs:'OGC:CRS84',operationAccuracyMetres:4},
  data:{type:'FeatureCollection',features:[{type:'Feature',id:`ahcb-a233b4b3bcf3-synthetic-v1-${day}`,properties:p,geometry:{type:'Polygon',coordinates:[[[-110,42],[-109,42],[-109,43],[-110,43],[-110,42]]]}}]}};
}
class MemoryStore {
 rows=new Map();heads=new Map();nonces=new Set();
 async ready(){return{paused:false};} async claimNonce(n){if(this.nonces.has(n))return false;this.nonces.add(n);return true;}
 async stage(id,manifest){const r=this.rows.get(id)??{id,sourceId:manifest.sourceId,manifest,state:'STAGED'};this.rows.set(id,r);return r;}
 async release(id){return this.rows.get(id)??null;} async active(source){return this.release(this.heads.get(source));}
 async commit(id,expected,projection){if((this.heads.get(this.rows.get(id).sourceId)??null)!==expected)throw new PipelineError('ACTIVATION_CONFLICT');const r=this.rows.get(id);r.projection=projection;r.state='COMMITTED';this.heads.set(r.sourceId,id);return{releaseId:id,active:true};}
 async history(source){return [...this.rows.values()].filter(r=>r.state==='COMMITTED'&&r.sourceId===source).map(r=>({releaseId:r.id,manifest:r.manifest,publishedAt:now}));}
}
async function harness(t){
 const root=await mkdtemp(resolve(tmpdir(),'kfm-county-release-test-'));t.after(()=>rm(root,{recursive:true,force:true}));await writeFile(resolve(root,'.qualified'),'kfm-private-artifacts-v1');
 const store=new MemoryStore(),files=new ArtifactFiles(root),pair=generateKeyPairSync('ed25519'),secret=randomBytes(32).toString('hex'),recipe=await recipeDigest();
 const env={KFM_PIPELINE_ENABLED:'true',KFM_RUNTIME_ROLE:'published',KFM_PIPELINE_APPROVER_PUBLIC_KEY:pair.publicKey.export({format:'pem',type:'spki'}),KFM_PIPELINE_WORKER_SECRET:secret};
 const approval=(override={})=>{const profile={format:'kfm-pc-release-delegation-v1',id:'synthetic-county-approval',sourceId:COUNTY_SOURCE_ID,recipeSha256:recipe,approver:'synthetic-owner',
  validFrom:new Date(now-60000).toISOString(),expiresAt:new Date(now+86400000).toISOString(),rights:'redistribution-allowed',sensitivity:'public',sourceRef:'kfm://source/synthetic',rightsRef:'kfm://review/synthetic-rights',reviewRef:'kfm://review/synthetic',releaseProfileRef:'kfm://release/profile/synthetic',
  maxBytes:MAX_PACKAGE,maxRows:1000,staleAfterSeconds:7200,role:'external-context',...override};return{profile,signature:sign(null,Buffer.from(canonical(profile)),pair.privateKey).toString('base64url')};};
 const manifest=(p,over={})=>{const bytes=Buffer.from(canonical(p));return{format:'kfm-pc-release-transfer-v1',sourceId:COUNTY_SOURCE_ID,recipeSha256:recipe,byteLength:bytes.length,payloadSha256:sha(bytes),approval:approval(),expectedActive:null,...over};};
 const request=async(action,body)=>{const bytes=canonical(body),path='/api/pipeline/v1/'+action;return handlePipeline(new Request(ORIGIN+path,{method:'POST',body:bytes,headers:signRequest({secret,method:'POST',path,body:bytes,now})}),{store,files,environment:env,now});};
 const fetcher=(url,options)=>handlePipeline(new Request(url,options),{store,files,environment:env,now});
 const put=async p=>{const m=manifest(p),id=sha(canonical(m));await store.stage(id,m);const bytes=Buffer.from(canonical(p));for(let n=0;n<bytes.length;n+=262144)await files.put(id,n/262144,bytes.subarray(n,n+262144));return{id,m};};
 return{store,files,env,approval,manifest,request,fetcher,secret,put};
}
const compile=async(file,deps={})=>{const out={};new Function('exports','require',ts.transpileModule(await readFile(file,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(out,id=>{if(id==='react')return{};if(id==='./bounded-json')return{};if(id in deps)return deps[id];throw Error(id);});return out;};
const client=await compile('app/reviewed-snapshots.ts');

test('county public product retains geographic scope, missing FIPS and exact-day context role',()=>{
 const p=product();assert.equal(validateCountyRelease(p),p);assert.equal(p.data.features[0].properties.fips,null);
 assert.ok(p.data.features[0].geometry.coordinates[0][0][0]<-103,'predecessor extent is retained');
 for(const mutate of [p=>{p.lifecycle='WORK'},p=>{p.evidenceEligible=true},p=>{p.partial=true},p=>{p.archiveSha256='b'.repeat(64)},p=>{p.sourceUrl='https://attacker.invalid'},
  p=>{p.data.features[0].properties.sourceDay='1861-01-30'},p=>{p.data.features[0].properties.classificationStatus='legal_county'},p=>{p.data.features[0].properties.sourceLocators[0].memberSha256='c'.repeat(64)},
  p=>{p.data.features[0].geometry.coordinates[0][0]=[181,40]},p=>{p.data.features.push(p.data.features[0])}]){const r=product();mutate(r);assert.throws(()=>validateCountyRelease(r));}
 for(const day of ['1873-03-20','1874-03-17','2001-01-01'])assert.throws(()=>validateCountyRelease(product(day)));
 assert.ok(validateCountyRelease(product('1874-03-18')));
});
test('no approval or wrong recipe cannot stage, and staged data cannot become a public read',async t=>{
 const h=await harness(t),p=product(),m=h.manifest(p);
 const unsigned=await h.request('stage',{...m,approval:{}});assert.equal(unsigned.status,403);
 const old='a'.repeat(64),oldM={...m,recipeSha256:old,approval:h.approval({recipeSha256:old})};
 assert.equal((await (await h.request('stage',oldM)).json()).error,'RECIPE_CHANGED');
 const staged=await h.request('stage',m);assert.equal(staged.status,200);
 assert.equal((await publicContext(COUNTY_SOURCE_ID,{store:h.store,environment:h.env,now})).reason,'NO_APPROVED_RELEASE');
 const denied=await handlePipeline(new Request(ORIGIN+'/api/pipeline/v1/stage',{method:'POST',body:canonical(m)}),{store:h.store,files:h.files,environment:h.env,now});assert.equal(denied.status,401);
});
test('signed commit/read/history/download gates preserve historical day and recheck rights, integrity and withdrawal',async t=>{
 const h=await harness(t),p=product(),{id}=await h.put(p);
 assert.equal((await h.request('commit',{releaseId:id})).status,200);
 const out=await publicContext(COUNTY_SOURCE_ID,{store:h.store,environment:h.env,now});assert.equal(out.state,'available');assert.equal(out.freshness,'historical');assert.equal(out.effectiveDay,'1861-01-29');assert.equal(out.retrievedAt,undefined);
 const history=await publicHistory(COUNTY_SOURCE_ID,{store:h.store,environment:h.env,now});assert.equal(history.items[0].effectiveDay,'1861-01-29');
 assert.deepEqual(JSON.parse((await publicArtifact(COUNTY_SOURCE_ID,{store:h.store,environment:h.env,now},id)).toString()),p);
 const parsed=client.parseReviewedProduct(out,COUNTY_SOURCE_ID,now);assert.ok(!('withheld'in parsed));assert.equal(parsed.effectiveDay,'1861-01-29');
 assert.equal(client.reviewedDataForDay(parsed,'1861-01-29',true,now).features.length,1);
 for(const day of ['1861-01-01','1861-01-30','2026-10-29'])assert.equal(client.reviewedDataForDay(parsed,day,true,now),null);
 assert.equal(client.reviewedDataForDay(parsed,'1861-01-29',false,now),null);assert.equal(client.reviewedDataForDay(parsed,'1861-01-29',true,now+86400000),null);
 await assert.rejects(publicContext(COUNTY_SOURCE_ID,{store:h.store,environment:{...h.env,KFM_PIPELINE_REVOKED_PROFILES:'synthetic-county-approval'},now}),/APPROVAL_REVOKED/);
 await assert.rejects(publicContext(COUNTY_SOURCE_ID,{store:h.store,environment:h.env,now:now+86400000}),/APPROVAL_INVALID/);
 const row=h.store.rows.get(id),originalManifest=row.manifest;
 row.manifest={...row.manifest,sourceId:'nws-alerts',approval:h.approval({sourceId:'nws-alerts'})};
 await assert.rejects(publicContext(COUNTY_SOURCE_ID,{store:h.store,environment:h.env,now}),/RELEASE_SOURCE_MISMATCH/);
 assert.equal((await publicHistory(COUNTY_SOURCE_ID,{store:h.store,environment:h.env,now})).items.length,0);row.manifest=originalManifest;
 row.projection.data.features[0].properties.name='modified';await assert.rejects(publicContext(COUNTY_SOURCE_ID,{store:h.store,environment:h.env,now}),/PROJECTION_INTEGRITY/);
 row.state='WITHDRAWN';assert.equal((await publicContext(COUNTY_SOURCE_ID,{store:h.store,environment:h.env,now})).state,'withheld');assert.equal((await publicHistory(COUNTY_SOURCE_ID,{store:h.store,environment:h.env,now})).items.length,0);
});
test('fresh preparation and exact context schema are checked again at commit',async t=>{
 const h=await harness(t);
 for(const mutate of [p=>{p.preparedAt=new Date(now-7200001).toISOString()},p=>{p.preparedAt=new Date(now+120000).toISOString()},p=>{p.lifecycle='PUBLISHED'}]){
  const p=product();mutate(p);const{id}=await h.put(p);assert.notEqual((await h.request('commit',{releaseId:id})).status,200);assert.equal((await h.store.release(id)).state,'STAGED');
 }
});
test('actual previous recipe rejects new publication while existing signed NWS release remains readable',async t=>{
 const h=await harness(t),old='e8b85ea8ff6414e9dc46030835d2102ce7439cf7811615512b422b2386d5fab3';
 const req=captureRequest('nws-alerts',now);
 const captured=await fetchCapture(req,{fetcher:async()=>Response.json({type:'FeatureCollection',features:[{type:'Feature',id:'synthetic-cutover-alert',geometry:null,properties:{event:'Synthetic alert',severity:'Unknown',sent:new Date(now-60000).toISOString(),effective:new Date(now-60000).toISOString(),expires:new Date(now+60000).toISOString()}}]})});
 const {product:p}=normalizeCapture(req,captured),oldApproval=h.approval({sourceId:'nws-alerts',recipeSha256:old});
 const m=h.manifest(p,{sourceId:'nws-alerts',recipeSha256:old,approval:oldApproval}),id=sha(canonical(m));
 const row=await h.store.stage(id,m);row.projection=p;row.state='COMMITTED';h.store.heads.set('nws-alerts',id);
 assert.equal((await h.request('stage',m)).status,409);
 assert.equal((await (await h.request('stage',m)).json()).error,'RECIPE_CHANGED');
 const current={...m,recipeSha256:await recipeDigest()};assert.equal((await (await h.request('stage',current)).json()).error,'APPROVAL_INVALID');
 const readable=await publicContext('nws-alerts',{store:h.store,environment:h.env,now});
 assert.equal(readable.releaseId,id);assert.equal(readable.data.features[0].properties.event,'Synthetic alert');assert.equal(h.store.heads.get('nws-alerts'),id);
});
test('client rejects WORK, mismatched source days, malformed geometry and fake release ids',()=>{
 const p={...product(),state:'available',releaseId:'d'.repeat(64),approvalExpiresAt:new Date(now+86400000).toISOString()};
 for(const mutate of [p=>{p.lifecycle='WORK'},p=>{p.data.features[0].properties.sourceDay='1862-01-29'},p=>{p.releaseId='fake'},p=>{p.data.features[0].geometry.coordinates=[]},p=>{p.effectiveDay='1873-03-20'}]){const r=structuredClone(p);mutate(r);assert.ok('withheld'in client.parseReviewedProduct(r,COUNTY_SOURCE_ID,now));}
 const h=client.parseReviewedHistory({items:[{releaseId:'e'.repeat(64),publishedAt:'2026-10-29T16:00:00Z',effectiveDay:'1900-01-01'},{releaseId:'f'.repeat(64),publishedAt:'2026-10-29T17:00:00Z',effectiveDay:'1861-01-29'}]},COUNTY_SOURCE_ID);
 assert.deepEqual(h.items.map(i=>i.effectiveDay),['1861-01-29','1900-01-01']);
 assert.equal(client.parseReviewedHistory({items:[{releaseId:'e'.repeat(64),publishedAt:'2026-10-29T16:00:00Z'}]},COUNTY_SOURCE_ID).items.length,0);
});
test('county source card and keyboard controls expose source dates/citations and the calendar jump',async()=>{
 const p=product(),r=p.data.features[0].properties,summary=client.reviewedFeatureSummary(COUNTY_SOURCE_ID,r);
 assert.equal(summary.title,r.name);assert.ok(summary.lines.includes(r.citation));assert.ok(summary.lines.some(s=>s.includes('unreviewed')));assert.ok(summary.lines.includes('FIPS not reported'));
 const h=await componentHarness('app/category-map-dock.tsx',{}),calls=[];
 const tree=h.render(h.exports.CategoryMapDock,{look:{topic:'government',name:'County test',tools:['reviewed'],starters:[],swatch:['#fff','#aaa','#000']},mode:'2d',depth:1,azimuth:0,sun:null,sunAvailable:false,terrainAvailable:true,
  onClose(){},onReset(){},onLayers(){},onReviewed(){},onReviewedDate:day=>calls.push(day),
  reviewed:{source:'historical county',historical:true,on:true,loading:false,reason:null,count:1,index:0,publishedAt:'2026-10-29',capturedFor:'1861-01-29',features:1,freshness:'historical',playing:false,motionAllowed:false,effectiveDay:'1861-01-29',list:client.reviewedFeatureList(COUNTY_SOURCE_ID,p.data,107)}});
 const button=findNode(tree,n=>n.type==='button'&&n.props.children?.[0]==='Set map to ');assert.ok(button);button.props.onClick();assert.deepEqual(calls,['1861-01-29']);h.dispose?.();
 const page=await readFile('app/page.tsx','utf8'),ast=ts.createSourceFile('page.tsx',page,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);let callback;
 const walk=node=>{if(ts.isJsxAttribute(node)&&node.name.getText(ast)==='onReviewedPick')callback=node.initializer.expression.getText(ast);ts.forEachChild(node,walk);};walk(ast);assert.ok(callback);
 const code=ts.transpileModule('const callback='+callback,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
 const fitted=[],picked=[];const bounds=[[-110,42],[-109,43]];
 const run=new Function('reviewedData','reviewedSource','setReviewedPick','countySearchGeometry','mapRef','motionDuration','easeToPicked',code+';return callback;')
  (p.data,COUNTY_SOURCE_ID,id=>picked.push(id),()=>({bounds}),{current:{fitBounds:(...args)=>fitted.push(args)}},n=>n,()=>{throw Error('county must fit its full extent')});
 run(p.data.features[0].id);assert.equal(picked[0],p.data.features[0].id);assert.deepEqual(fitted[0][0],bounds);assert.equal(fitted[0][1].maxZoom,8);
});
test('real statehood qualification traverses normalize/sign/commit/read/client gates with all 50 geometries',{
 skip:!process.env.KFM_COUNTY_REPORT,
},async t=>{
 const packet=await readCountyHistoryReport(process.env.KFM_COUNTY_REPORT,'3e9da16b1379239e6f231e58ad6e2167bb1f7b6b627fcb349ce13133b644ed6a');
 const normalized=normalizeCountyCandidate(packet,new Date(now).toISOString());assert.equal(normalized.product.data.features.length,50);assert.ok(normalized.bytes.length<MAX_PACKAGE);
 assert.doesNotMatch(normalized.bytes.toString(),/urn:kfm:work|"lifecycle"|"publicClientEligible"|undatedNameCrossReferences/);
 const h=await harness(t),m=h.manifest(normalized.product),receipt=await publish(m,normalized.bytes,h.secret,{fetcher:h.fetcher});
 const result=await publicContext(COUNTY_SOURCE_ID,{store:h.store,environment:h.env,now},receipt.releaseId),parsed=client.parseReviewedProduct(result,COUNTY_SOURCE_ID,now);
 assert.ok(!('withheld'in parsed));assert.equal(client.reviewedDataForDay(parsed,'1861-01-29',true,now).features.length,50);
 assert.equal(client.reviewedFeatureList(COUNTY_SOURCE_ID,parsed.data,107).length,50);
 for(const f of parsed.data.features){const source=packet.records.find(r=>r.institutionSourceId===f.properties.institutionSourceId);const raw=packet.data.features.find(r=>r.properties.institutionSourceId===source.institutionSourceId);assert.deepEqual(f.geometry,raw.geometry);assert.equal(f.properties.citation,source.citation);}
});
