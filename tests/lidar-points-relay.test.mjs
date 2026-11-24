import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtempSync,writeFileSync,chmodSync,symlinkSync,linkSync,unlinkSync,rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createHash} from 'node:crypto';
import {LIDAR_POINTS_COLUMNS,loadLidarPoints,validLidarPointsManifest,validLidarPointsChunk,lidarPointsConfig} from '../scripts/local-data/lidar-points.mjs';
import {LOCAL_DATA_LIMITS,LOCAL_DATA_ROUTES} from '../scripts/local-data/protocol.mjs';
import {createGateway} from '../scripts/local-data/gateway.mjs';
import {createLocalDataService} from '../server/local-data.mjs';
import {newSecret,decodeSecret,signRequest,RESPONSE_SIGNATURE_HEADER} from '../scripts/home-inference/signature.mjs';

const sha=b=>'sha256:'+createHash('sha256').update(b).digest('hex');
function fixture(t){
 const directory=mkdtempSync(join(tmpdir(),'kfm-native-points-test-'));chmodSync(directory,0o700);t.after(()=>rmSync(directory,{recursive:true,force:true}));
 // Deliberately synthetic unit inputs; never a native-data delivery fixture.
 const chunk={format:'kfm-lidar-points-chunk-v1',captureId:'synthetic-unit-only',chunkId:0,points:[[-10751800,4734600,350,120,2,1,2,0,100,0,0],[-10751799,4734601,351,130,7,2,2,4,101,0,1]]};
 const bytes=Buffer.from(JSON.stringify(chunk));writeFileSync(join(directory,'chunk-0.json'),bytes,{mode:0o600});
 const manifest={format:'kfm-lidar-points-manifest-v1',captureId:chunk.captureId,generatedAt:'2026-11-24T02:00:00Z',source:{provider:'USGS',project:'KS_Statewide_B6A_2018',eptUrl:'https://usgs-lidar-public.s3.amazonaws.com/KS_Statewide_B6A_2018/ept.json',horizontalCrs:'EPSG:3857',verticalReference:'Synthetic unit input; no observation',acquisition:'Synthetic unit input',coordinateEncodingM:[.001,.001,.001],selection:'Synthetic unit input',assets:[{id:0,url:'https://usgs-lidar-public.s3.amazonaws.com/KS_Statewide_B6A_2018/ept-data/8-92-179-127.laz',sha256:'sha256:'+'a'.repeat(64),bytes:258444,pointCount:30058}],notes:['Synthetic unit input, no observations']},review:{status:'pending',source_admitted:false,released:false,scientific_accuracy_verified:false},pointCount:2,bounds3857:[-10751800,4734600,-10751799,4734601],heightRange:[350,351],chunks:[{id:0,pointCount:2,bytes:bytes.length,sha256:sha(bytes)}],columns:[...LIDAR_POINTS_COLUMNS]};
 const m=Buffer.from(JSON.stringify(manifest));writeFileSync(join(directory,'manifest.json'),m,{mode:0o600});return {directory,manifest,chunk,config:{directory,manifestSha256:sha(m)}};
}
test('pinned native point artifacts preserve native attributes and reject unsafe/replaced bytes',t=>{
 const f=fixture(t);assert.deepEqual(loadLidarPoints(f.config),f.manifest);assert.deepEqual(loadLidarPoints(f.config,0),f.chunk);
 const path=join(f.directory,'chunk-0.json');writeFileSync(path,JSON.stringify({...f.chunk,captureId:'wrong'}));assert.throws(()=>loadLidarPoints(f.config,0),/NOT_READY/);
 writeFileSync(path,JSON.stringify(f.chunk));chmodSync(path,0o644);assert.throws(()=>loadLidarPoints(f.config,0),/NOT_READY/);chmodSync(path,0o600);
 linkSync(path,join(f.directory,'hardlink'));assert.throws(()=>loadLidarPoints(f.config,0),/NOT_READY/);unlinkSync(join(f.directory,'hardlink'));
 const original=join(f.directory,'original');linkSync(path,original);unlinkSync(path);symlinkSync(original,path);assert.throws(()=>loadLidarPoints(f.config,0),/NOT_READY/);
 assert.equal(lidarPointsConfig({KFM_LIDAR_POINTS_DIR:'relative',KFM_LIDAR_POINTS_MANIFEST_SHA256:f.config.manifestSha256}),null);
 assert.throws(()=>loadLidarPoints({...f.config,manifestSha256:'sha256:'+'0'.repeat(64)}),/NOT_READY/);
});
test('native schema binds capture, chunks, original record identity, quality flags and public allowlist',t=>{
 const {manifest:m,chunk:c}=fixture(t);assert.equal(validLidarPointsManifest(m),true);assert.equal(validLidarPointsChunk(c,m,0),true);
 for(const change of [x=>x.review.source_admitted=true,x=>x.pointCount=100001,x=>x.chunks[0].id=1,x=>x.source.assets[0].url='https://evil.test/private',x=>x.source.privatePath='/home/private',x=>x.source.notes=['https://example.test/?X-Amz-Signature=secret']]){const b=structuredClone(m);change(b);assert.equal(validLidarPointsManifest(b),false);}
 for(const change of [x=>x.captureId='wrong',x=>x.points[0][0]=0,x=>x.points[0][7]=16,x=>x.points[0][9]=5,x=>x.points[0][10]=30058,x=>x.points[1]=[...x.points[0]],x=>x.points.pop(),x=>x.points[0][8]=Infinity]){const b=structuredClone(c);change(b);assert.equal(validLidarPointsChunk(b,m,0),false);}
 assert.equal(LOCAL_DATA_LIMITS.replyBytes,1000000);assert.equal(LOCAL_DATA_ROUTES.get('/v1/lidar/points/15'),'GET');assert.equal(LOCAL_DATA_ROUTES.has('/v1/lidar/points/16'),false);assert.equal(LOCAL_DATA_ROUTES.has('/v1/lidar/points/../manifest.json'),false);
});
test('native point gateway requires signatures and exposes only fixed bounded read routes',t=>{
 const f=fixture(t),keyId='test-native',secret=newSecret(),gateway=createGateway({keyId,secret,lidarPoints:f.config,open(){throw Error('SQL must not open');}});
 const call=(path,method='GET',body='')=>gateway({method,path,body,headers:signRequest({keyId,secret,method,path,body})});
 assert.equal(gateway({method:'GET',path:'/v1/lidar/points',headers:{}}).status,401);
 assert.equal(call('/v1/lidar/points').status,200);assert.equal(call('/v1/lidar/points/0').status,200);assert.equal(call('/v1/lidar/points/16').status,404);assert.equal(call('/v1/lidar/points/00').status,404);assert.equal(call('/v1/lidar/points','POST').status,404);assert.equal(call('/v1/lidar/points','GET','{}').status,400);
 assert.equal(call('/v1/lidar/points/1').status,503);
});
test('public native relay verifies signed manifest/chunks and shares cache without enlarging limits',async t=>{
 const f=fixture(t),keyId='test-native',secret=newSecret(),bytes=decodeSecret(secret),gateway=createGateway({keyId,secret,lidarPoints:f.config,open(){throw Error('SQL must not open');}});let now=1000,trips=0;
 const relay={lastSeen:now,async submit({method,path,body}){trips++;const headers=signRequest({keyId,secret,method,path,body});const r=gateway({method,path,body,headers});return {status:r.status,bytes:r.body,requestHeaders:headers,headers:new Headers({'content-type':'application/json',[RESPONSE_SIGNATURE_HEADER]:r.signature})};}};
 const service=createLocalDataService({config:{keyId,secret:bytes},relay,clock:()=>now}),request=()=>new Request('https://kansasfrontiermatrix.com/api/lidar/points');
 let r=await service.lidarPoints(request(),0);assert.equal(r.status,200);let j=await r.json();assert.deepEqual(j.points,f.chunk.points);assert.equal(j.cache.state,'live');assert.equal(trips,2);assert.equal('gateway'in j,false);
 r=await service.lidarPoints(request(),0);assert.equal((await r.json()).cache.state,'fresh');assert.equal(trips,2);
 now+=31000;relay.lastSeen=0;r=await service.lidarPoints(request(),0);assert.equal((await r.json()).cache.state,'stale');assert.equal(trips,2);
 assert.equal((await service.lidarPoints(new Request(request().url+'?file=/etc/passwd'))).status,400);assert.equal((await service.lidarPoints(request(),16)).status,400);
});
