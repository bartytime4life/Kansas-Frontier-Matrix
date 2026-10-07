import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import * as THREE from 'three';
const compile = (value) => ts.transpileModule(value,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const materialsURL = `data:text/javascript;base64,${Buffer.from(compile(await readFile('app/subsurface-materials.ts','utf8'))).toString('base64')}`;
const model = compile(await readFile('app/subsurface-model.ts','utf8')).replace('"./subsurface-materials"',JSON.stringify(materialsURL));
const modelURL = `data:text/javascript;base64,${Buffer.from(model).toString('base64')}`;
const source = compile(await readFile('app/cutaway-model.ts','utf8')).replace('"./subsurface-model"', JSON.stringify(modelURL));
const {cutawayRecords,cutawayCameraFit,pickCutawaySource} = await import(`data:text/javascript;base64,${Buffer.from(source).toString('base64')}`);
const volume = {bounds:[-100.6,38.4,-100.4,38.6],envelopes:[]};
const record=(id,intervals,coordinates=[-100.5,38.5])=>({id,coordinates,depthUnit:'ft',intervals});
const interval=(top,bottom,description='sand')=>({top,bottom,description});
test('cutaway fit includes valid plotted log depths without an aquifer and keeps gaps and source intervals',()=>{
  const original=record('well',[interval(0,20),interval(40,500)]);
  const before=JSON.stringify(original);
  const result=cutawayRecords(volume,[original]);
  assert.equal(result.recordCount,1);assert.equal(result.intervals.length,2);
  assert.equal(result.deepest,152.4);assert.equal(result.intervals[1].top,12.192);
  assert.equal(result.intervals[1].interval,original.intervals[1]);assert.equal(JSON.stringify(original),before);
});
test('cutaway rendering excludes outside, invalid and clipped-away records, and retains measured-unit references',()=>{
  const result=cutawayRecords(volume,[record('outside',[interval(0,50)],[-101,39]),record('deep',[interval(2000,2500)]),record('mixed',[interval(-1,2),interval(4,1),interval(0,Infinity),interval(100,2000)])]);
  assert.equal(result.recordCount,1);assert.equal(result.intervals.length,1);assert.equal(result.intervals[0].bottom,500);
  assert.equal(result.intervals[0].interval.bottom,2000);assert.equal(result.clipped,true);
});
test('cutaway shares existing 50-record/400-interval and envelope-plus-50-m depth budgets',()=>{
  const bounded={...volume,envelopes:[{deepMeters:100}]};
  const result=cutawayRecords(bounded,Array.from({length:51},(_,i)=>record(String(i),Array.from({length:10},(_,j)=>interval(j,j+1)))));
  assert.equal(result.intervals.length,400);assert.equal(result.recordCount,40);assert.equal(result.clipped,true);assert.equal(result.limit,150);
  const recordBudget=cutawayRecords(volume,Array.from({length:51},(_,i)=>record(String(i),[interval(0,1)])));
  assert.equal(recordBudget.recordCount,50);
});
test('projected corner fit retains every corner and readable depth label across presets and viewport sizes',()=>{
  for(const [screenWidth,screenHeight] of [[1158,462],[994,282],[343,264],[320,240]])
    for(const direction of [[.55,.6,1],[0,1,.001],[.2,0,1]]) for(const depth of [.001,2,1000,100000]){
      const width=6,length=3.7,aspect=screenWidth/screenHeight;
      const fit=cutawayCameraFit(width,length,depth,aspect,direction,screenHeight);
      assert.ok(Object.values(fit).every(Number.isFinite));assert.ok(fit.near>0);
      const camera=new THREE.PerspectiveCamera(40,aspect,fit.near,fit.far);
      camera.setViewOffset(screenWidth,screenHeight,fit.offsetX*screenWidth/2,-fit.offsetY*screenHeight/2,screenWidth,screenHeight);
      camera.position.copy(new THREE.Vector3(...direction).normalize().multiplyScalar(fit.distance));
      camera.lookAt(0,0,0);camera.updateMatrixWorld(true);
      const check=(point,labelHalfWidth=0,labelHalfHeight=0)=>{
        const p=new THREE.Vector3(...point).project(camera);
        assert.ok(Math.abs(p.x)+labelHalfWidth*2/screenWidth<1,`horizontal clip: ${JSON.stringify({screenWidth,screenHeight,direction,depth,point,p})}`);
        assert.ok(Math.abs(p.y)+labelHalfHeight*2/screenHeight<1,`vertical clip: ${JSON.stringify({screenWidth,screenHeight,direction,depth,point,p})}`);
        assert.ok(p.z>-1&&p.z<1,'source corner is within near/far planes');
      };
      for(const x of [-3,3])for(const y of [-depth/2,depth/2])for(const z of [-length/2,length/2])check([x,y,z]);
      for(const f of [0,.25,.5,.75,1])check([-3.42,depth/2-depth*f,length/2],45,12);
    }
});
test('initial projected fit uses the scene instead of retreating to an oversized sphere',()=>{
  const aspect=1158/462,fit=cutawayCameraFit(6,3.7,1.32,aspect,[.55,.6,1],462);
  const camera=new THREE.PerspectiveCamera(40,aspect,fit.near,fit.far);
  camera.setViewOffset(1158,462,fit.offsetX*1158/2,-fit.offsetY*462/2,1158,462);
  camera.position.copy(new THREE.Vector3(.55,.6,1).normalize().multiplyScalar(fit.distance));camera.lookAt(0,0,0);camera.updateMatrixWorld(true);
  const corners=[];for(const x of [-3,3])for(const y of [-.66,.66])for(const z of [-1.85,1.85])corners.push(new THREE.Vector3(x,y,z).project(camera));
  const height=(Math.max(...corners.map(p=>p.y))-Math.min(...corners.map(p=>p.y)))/2;
  const width=(Math.max(...corners.map(p=>p.x))-Math.min(...corners.map(p=>p.x)))/2*1158;
  assert.ok(height>.7&&height<.95,`initial object height fraction ${height}`);
  assert.ok(width>500,`initial object width ${width}`);
});

test('source picking ignores broad decorative edge hits and returns the actual owner mesh',()=>{
  const geometry=new THREE.CylinderGeometry(.5,.5,2,12),paint=new THREE.MeshBasicMaterial();
  const owner=new THREE.Mesh(geometry,paint);owner.userData.record={id:'source-record'};
  const edgeGeometry=new THREE.EdgesGeometry(geometry,50),edgePaint=new THREE.LineBasicMaterial();
  const decoration=new THREE.LineSegments(edgeGeometry,edgePaint);owner.add(decoration);owner.updateMatrixWorld(true);
  const ray=new THREE.Raycaster(new THREE.Vector3(.7,.9,3),new THREE.Vector3(0,0,-1));
  // Three's default line threshold catches the decoration outside the record cylinder.
  assert.ok(ray.intersectObjects([owner]).some(hit=>hit.object===decoration));
  assert.equal(pickCutawaySource(ray,[owner]),undefined);
  ray.set(new THREE.Vector3(0,0,3),new THREE.Vector3(0,0,-1));
  const hit=pickCutawaySource(ray,[owner]);assert.equal(hit.object,owner);assert.equal(hit.object.userData.record.id,'source-record');
  geometry.dispose();paint.dispose();edgeGeometry.dispose();edgePaint.dispose();
});
