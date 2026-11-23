import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,writeFile,chmod,rm,symlink} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createHash} from 'node:crypto';
import {NEON_PREVIEW_ROUTE,NEON_PREVIEW_MAX_BYTES,loadNeonPreview,neonPreviewConfig} from '../scripts/local-data/neon-preview.mjs';
import {LOCAL_DATA_GATEWAY,LOCAL_DATA_ROUTES} from '../scripts/local-data/protocol.mjs';
import {createGateway} from '../scripts/local-data/gateway.mjs';
import {newSecret,decodeSecret,signRequest,verifyResponse,RESPONSE_SIGNATURE_HEADER} from '../scripts/home-inference/signature.mjs';
import {createLocalDataService,localNeonPreviewRuntime} from '../server/local-data.mjs';

const packageValue=()=>({format:'kfm-neon-relay-pilot-v1',generatedAt:'2026-11-23T22:00:00Z',preview:{schema_version:'kfm-neon-lidar-preview-v1',data_kind:'provider-files',source_admitted:false,released:false,
 source:{site:'KONZ',month:'2024-09',release:'RELEASE-2026',tile:'NEON_D06_KONZ_DP3_706000_4336000',acquisition_run:'2024_KONZ_10'},
 grid:{width:8,height:8,dtm:Array(64).fill(300),dsm:Array(64).fill(312),chm:Array(64).fill(8)}},
 review:{status:'pending',scientific_accuracy_verified:false,source_admitted:false,canopy_native_max_m:83.41000366210938,canopy_native_cells_above_50m:5,surface_minus_ground_native_max_m:32.5,notes:['Synthetic transport fixture only; real source QA is not asserted.']}});
const digest=bytes=>'sha256:'+createHash('sha256').update(bytes).digest('hex');
async function fixture(t,value=packageValue()){
 const dir=await mkdtemp(join(tmpdir(),'kfm-neon-relay-'));t.after(()=>rm(dir,{recursive:true,force:true}));
 const path=join(dir,'public.json'),bytes=JSON.stringify(value);await writeFile(path,bytes,{mode:0o600});
 return {path,sha256:digest(bytes),dir,value};
}
const secret=newSecret(),workerSecret=newSecret();
function request(path,{method='GET',body='',key=secret}={}){return {method,path,body,headers:signRequest({keyId:'gateway',secret:key,method,path,body})};}
const parse=answer=>JSON.parse(answer.body.toString('utf8'));

test('the only added relay route is a fixed GET; no NEON credential setting is consumed',()=>{
 assert.equal(LOCAL_DATA_ROUTES.get(NEON_PREVIEW_ROUTE),'GET');
 assert.equal(neonPreviewConfig({NEON_TOKEN:'dummy-unused'}),null);
 assert.equal(neonPreviewConfig({KFM_NEON_PREVIEW_FILE:'relative',KFM_NEON_PREVIEW_SHA256:'sha256:'+'a'.repeat(64)}),null);
 assert.equal(neonPreviewConfig({KFM_NEON_PREVIEW_FILE:'/private/public.json',KFM_NEON_PREVIEW_SHA256:'not-a-pin'}),null);
});

test('derived package needs an owner-private regular file, exact hash, shape and source identity',async t=>{
 const config=await fixture(t);assert.deepEqual(loadNeonPreview(config),config.value);
 assert.throws(()=>loadNeonPreview({...config,sha256:'sha256:'+'0'.repeat(64)}),{code:'NEON_PREVIEW_NOT_READY'});
 await chmod(config.path,0o644);assert.throws(()=>loadNeonPreview(config),{code:'NEON_PREVIEW_NOT_READY'});await chmod(config.path,0o600);
 const link=join(config.dir,'link.json');await symlink(config.path,link);assert.throws(()=>loadNeonPreview({...config,path:link}),{code:'NEON_PREVIEW_NOT_READY'});
 await chmod(config.dir,0o755);assert.throws(()=>loadNeonPreview(config),{code:'NEON_PREVIEW_NOT_READY'});await chmod(config.dir,0o700);
 for(const mutate of [v=>{v.preview.source.site='UKFS';},v=>{v.review.scientific_accuracy_verified=true;},v=>{v.preview.source.token='PRIVATE';},v=>{v.preview.source.url='https://storage.googleapis.com/x?X-Goog-Signature=PRIVATE';},v=>{v.preview.grid.chm=[1];}]){
  const value=packageValue();mutate(value);const bad=await fixture(t,value);
  assert.throws(()=>loadNeonPreview(bad),{code:'NEON_PREVIEW_NOT_READY'});
 }
 await writeFile(config.path,'x'.repeat(NEON_PREVIEW_MAX_BYTES+1));assert.throws(()=>loadNeonPreview(config),{code:'NEON_PREVIEW_NOT_READY'});
});

test('gateway requires an authenticated GET and signs the exact derived reply without opening SQL',async t=>{
 const config=await fixture(t);
 const gateway=createGateway({keyId:'gateway',secret,neonPreview:config,open(){throw new Error('SQL_MUST_NOT_OPEN');}});
 const good=request(NEON_PREVIEW_ROUTE),answer=gateway(good);
 assert.equal(answer.status,200);assert.equal(parse(answer).format,config.value.format);
 assert.equal(verifyResponse({secret:decodeSecret(secret),requestHeaders:good.headers,method:good.method,path:good.path,requestBody:good.body,status:answer.status,body:answer.body,headers:{[RESPONSE_SIGNATURE_HEADER]:answer.signature}}),true);
 assert.equal(gateway(request(NEON_PREVIEW_ROUTE,{key:newSecret()})).status,401);
 assert.equal(gateway(request(NEON_PREVIEW_ROUTE,{method:'POST'})).status,404);
 assert.equal(gateway(request(NEON_PREVIEW_ROUTE,{body:'{}'})).status,400);
 assert.equal(gateway(request(NEON_PREVIEW_ROUTE)).status,200);
 const off=createGateway({keyId:'gateway',secret});assert.equal(off(request(NEON_PREVIEW_ROUTE)).status,503);
});

test('site verifies gateway signatures, deduplicates/cache-marks the pilot, and refuses visitor parameters',async t=>{
 const file=await fixture(t);let now=Date.now(),trips=0,tamper=false;
 const gateway=createGateway({keyId:'gateway',secret,neonPreview:file,clock:()=>now});
 const relay={lastSeen:now,async submit({method,path,body}){
  trips++;const req=request(path,{method,body}),answer=gateway(req);
  const bytes=tamper?Buffer.from(answer.body.toString().replace('83.41000366210938','0')):answer.body;
  return {status:answer.status,bytes,requestHeaders:req.headers,headers:new Headers({'content-type':'application/json',[RESPONSE_SIGNATURE_HEADER]:answer.signature})};
 }};
 const config={origin:'https://kansasfrontiermatrix.com',keyId:'gateway',secret:decodeSecret(secret),worker:{keyId:'worker',secret:decodeSecret(workerSecret)}};
 const service=createLocalDataService({config,relay,clock:()=>now});
 const get=()=>service.neonPreview(new Request(config.origin+'/api/neon/preview'));
 const [one,two]=await Promise.all([get(),get()]);assert.equal(one.status,200);assert.equal(two.status,200);assert.equal(trips,1);
 const body=await one.json();assert.equal(body.cache.state,'live');assert.equal(body.gateway,undefined);assert.equal(body.review.scientific_accuracy_verified,false);
 assert.equal((await (await get()).json()).cache.state,'fresh');
 relay.lastSeen=now-31000;assert.equal((await (await get()).json()).cache.state,'stale');
 assert.equal((await service.neonPreview(new Request(config.origin+'/api/neon/preview?path=/private/token'))).status,400);
 assert.equal((await service.neonPreview(new Request(config.origin+'/api/neon/preview',{method:'POST'}))).status,405);
 const another=createLocalDataService({config,relay,clock:()=>now});relay.lastSeen=now;tamper=true;
 assert.equal((await another.neonPreview(new Request(config.origin+'/api/neon/preview'))).status,503);
 assert.equal((await localNeonPreviewRuntime({})(new Request(config.origin+'/api/neon/preview'))).status,404);
 assert.equal(parse(gateway(request('/v1/no-arbitrary-file'))).error,'ROUTE_NOT_FOUND');
 assert.equal(LOCAL_DATA_GATEWAY,'kfm-local-data/1');
});
