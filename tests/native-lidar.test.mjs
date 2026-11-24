import test from 'node:test';import assert from 'node:assert/strict';import {readFile} from 'node:fs/promises';import ts from 'typescript';import {MercatorCoordinate} from 'maplibre-gl';import {pointFixture} from './native-lidar-fixtures.mjs';import {nativeCloudFixture,nativeLidarBrowserFixtures} from './native-lidar-browser-fixtures.mjs';
const dataURL=s=>'data:text/javascript;base64,'+Buffer.from(s).toString('base64');
const modelURL=dataURL(ts.transpileModule(await readFile('app/native-lidar.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText),model=await import(modelURL);
const layer=await import(dataURL(ts.transpileModule((await readFile('app/native-lidar-layer.ts','utf8')).replace("from './native-lidar'","from '"+modelURL+"'"),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText));
const clientSource=ts.transpileModule((await readFile('app/native-lidar-client.ts','utf8')).replace("from './native-lidar'","from '"+modelURL+"'"),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const client=await import(dataURL(clientSource));
const dataset=()=>{const f=pointFixture(),m=model.parseNativeManifest(f.manifest);return model.assembleNativeDataset(m,f.chunks);};
test('native schema preserves all eleven original attributes, quality flags and exact EPT asset/record identity',()=>{
 const f=pointFixture(),m=model.parseNativeManifest(f.manifest);assert.ok(m);const d=model.assembleNativeDataset(m,f.chunks);assert.deepEqual(d.points,f.points);assert.equal(model.nativePointEligible(d.points[2]),false);assert.equal(model.nativePointEligible(d.points[3]),true);assert.equal(d.points[0][8],123456789.125);assert.equal(d.points[0][10],4);
 const chunk=model.parseNativeChunk(f.chunks[0],m,0);f.chunks[0].points[0][2]=999;assert.equal(chunk.points[0][2],305.125,'validated rows own their data');
});
test('native manifests reject missing, forged, unbounded and scientifically stronger identities',()=>{
 for(const mutate of [m=>m.columns.pop(),m=>m.source.horizontalCrs='EPSG:32614',m=>m.review.scientific_accuracy_verified=true,m=>m.review.released=true,m=>m.pointCount=100001,m=>m.chunks[0].id=2,m=>m.chunks[0].bytes=900000,m=>m.chunks[0].pointCount++,m=>m.source.assets[0].url='https://evil.test/node.laz',m=>m.source.assets[0].sha256='a'.repeat(64),m=>m.source.coordinateEncodingM[2]=1,m=>m.generatedAt='2026-02-30T00:00:00Z',m=>m.cache.state='ready']){const f=pointFixture();mutate(f.manifest);assert.equal(model.parseNativeManifest(f.manifest),null);}
});
test('chunk validation rejects wrong captures, truncated/duplicate nodes, bounds, attributes and source-record overflow',()=>{
 for(const mutate of [f=>f.chunks[0].captureId='other',f=>f.chunks[0].chunkId=1,f=>f.chunks[0].points.pop(),f=>f.chunks[0].points[0].push(3),f=>f.chunks[0].points[0][0]=-1,f=>f.chunks[0].points[0][2]=NaN,f=>f.chunks[0].points[0][3]=65536,f=>f.chunks[0].points[0][4]=256,f=>f.chunks[0].points[0][5]=1.5,f=>f.chunks[0].points[0][7]=16,f=>f.chunks[0].points[0][8]=Infinity,f=>f.chunks[0].points[0][9]=1,f=>f.chunks[0].points[0][10]=63514]){const f=pointFixture(),m=model.parseNativeManifest(f.manifest);mutate(f);assert.equal(model.parseNativeChunk(f.chunks[0],m,0),null);}
 const f=pointFixture(),m=model.parseNativeManifest(f.manifest);f.chunks[1].points[0][10]=4;assert.equal(model.assembleNativeDataset(m,f.chunks),null,'duplicate original node record is not a new return');assert.equal(model.assembleNativeDataset(m,f.chunks.slice(0,1)),null);
 const g=pointFixture(),gm=model.parseNativeManifest(g.manifest);g.chunks[1].points[0][2]=319;assert.equal(model.assembleNativeDataset(gm,g.chunks),null,'reported capture extrema must agree with complete rows');
});
test('source projection agrees with installed MapLibre conversion while keeping original XYZ and vertical exaggeration distinct',()=>{
 const d=dataset();for(const p of d.points){const before=[...p],position=model.nativePointPosition(p),expected=MercatorCoordinate.fromLngLat({lng:position.longitude,lat:position.latitude},p[2]);for(let i=0;i<3;i++)assert.ok(Math.abs(position.mercator[i]-[expected.x,expected.y,expected.z][i])<1e-14);assert.deepEqual(p,before);for(const scale of [.1,.2,.4,3]){const exaggerated=model.nativePointPosition(p,scale);assert.equal(exaggerated.mercator[0],position.mercator[0]);assert.equal(exaggerated.mercator[1],position.mercator[1]);assert.ok(Math.abs(exaggerated.mercator[2]-position.mercator[2]*scale)<1e-18);}}
 const zero=model.nativePointPosition([0,0,100]);assert.deepEqual(zero.mercator.slice(0,2),[.5,.5]);assert.ok(Math.abs(zero.mercator[2]-100/(2*Math.PI*6371008.8))<1e-18);assert.notEqual(zero.mercator[2],100/(2*Math.PI*6378137));assert.throws(()=>model.nativePointPosition([0,0,1],.09));assert.throws(()=>model.nativePointPosition([0,0,1],99));
});
test('local-origin translation retains sub-metre offsets and GPU pixel IDs use matching DPR/Y orientation with no background hit',()=>{
 const origin=[.232,.38,.00001],matrix=[1e6,0,0,0,0,1e6,0,0,0,0,1,0,-232000,-380000,0,1],translated=layer.nativeTranslatedMatrix(matrix,origin);assert.ok(Math.abs(translated[12])<1e-8);assert.equal(translated[13],0);const offset=0.001/(2*Math.PI*6378137);assert.ok(Math.abs(translated[0]*Math.fround(offset)-1e6*offset)<1e-12);
 assert.deepEqual(layer.nativePickPixel({x:25,y:10},100,50,200,100),[50,79]);assert.deepEqual(layer.nativePickPixel({x:0,y:0},100,50,100,50),[0,49]);assert.equal(layer.nativePickPixel({x:100,y:1},100,50,200,100),null);assert.equal(layer.nativeDecodePick([0,0,0,0],100000),null);for(const id of [0,254,255,65535,99999]){const n=id+1;assert.equal(layer.nativeDecodePick([n&255,(n>>8)&255,(n>>16)&255,255],100000),id);}
});
test('native client uses fixed paths, complete validation, max-two chunk concurrency and retains stale cache provenance',async()=>{
 const old=globalThis.fetch,f=pointFixture(),paths=[];let concurrent=0,max=0;globalThis.fetch=async path=>{paths.push(path);if(path==='/api/lidar/points')return Response.json(f.manifest);concurrent++;max=Math.max(max,concurrent);await new Promise(r=>setTimeout(r,2));concurrent--;const chunk=structuredClone(f.chunks[Number(path.split('/').at(-1))]);chunk.cache.state='stale';return Response.json(chunk);};try{const d=await client.readNativeLidar(new AbortController().signal);assert.equal(d.points.length,4);assert.equal(max,2);assert.deepEqual(paths,['/api/lidar/points','/api/lidar/points/0','/api/lidar/points/1']);assert.equal(d.chunkCaches[0].state,'stale');}finally{globalThis.fetch=old;}
});
test('native client rejects non-2xx before decoding, byte overflow and incomplete capture; abort blocks late responses',async()=>{
 const old=globalThis.fetch;try{
  globalThis.fetch=async()=>new Response('not JSON',{status:503});await assert.rejects(client.readNativeLidar(new AbortController().signal),/unavailable/);
  globalThis.fetch=async()=>new Response(' '.repeat(1_000_001));await assert.rejects(client.readNativeLidar(new AbortController().signal),/byte budget/);
  const f=pointFixture();globalThis.fetch=async path=>Response.json(path==='/api/lidar/points'?f.manifest:{...f.chunks[0],captureId:'forged'});await assert.rejects(client.readNativeLidar(new AbortController().signal),/validation/);
  const c=new AbortController();globalThis.fetch=async()=>{c.abort();return Response.json(f.manifest);};await assert.rejects(client.readNativeLidar(c.signal),/abort/i);
 }finally{globalThis.fetch=old;}
});

test('the explicitly synthetic CI GPU transport is complete and its native-receiver instrumentation compiles without running a browser',async()=>{
 const fixture=nativeCloudFixture(),manifest=model.parseNativeManifest(fixture.manifest),d=model.assembleNativeDataset(manifest,fixture.chunks);assert.ok(d);assert.equal(d.points.length,1681);assert.equal(d.points.filter(model.nativePointEligible).length,1680);assert.match(d.manifest.source.selection,/Synthetic/);assert.equal(fixture.manifest.chunks[0].bytes,Buffer.byteLength(JSON.stringify(fixture.chunks[0])));
 const fixtures=await nativeLidarBrowserFixtures(new URL('http://127.0.0.1:4173')),scripts=[];await fixtures.setup(async(method,args)=>{if(method==='Page.addScriptToEvaluateOnNewDocument')scripts.push(args.source);});for(const source of scripts)new Function(source);assert.ok(scripts.some(s=>s.includes('__nativeVisiblePoint')),'CI helper projects actual source candidates then reads production GPU IDs');
});
