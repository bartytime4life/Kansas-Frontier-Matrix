import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
const compile = source => ts.transpileModule(source,{compilerOptions:{target:ts.ScriptTarget.ES2022,module:ts.ModuleKind.CommonJS}}).outputText;
const camera={};new Function('exports',compile(await readFile('app/terrain-camera.ts','utf8')))(camera);
const radians=Math.PI/180;
const mercatorY=latitude=>(1-Math.log(Math.tan(Math.PI/4+latitude*radians/2))/Math.PI)/2;

test('pitched horizon bounds are replaced by a bounded local map-scale footprint without inventing native resolution',()=>{
  const view={center:[-98.2,38.7],zoom:14.3,width:1280,height:720};
  const bounds=camera.terrainViewFootprint(view,[-104,35,-92,43]);
  assert.ok(bounds[2]-bounds[0]<.05,'local longitude window instead of a multi-state horizon');
  assert.ok(bounds[3]-bounds[1]<.03);
  assert.equal((bounds[0]+bounds[2])/2,view.center[0]);
  const rotated=camera.terrainViewFootprint(view,[-103,36,-93,41]);
  assert.deepEqual(rotated,bounds,'bearing/pitch may change visible horizon, never acquisition scale');
  const closer=camera.terrainViewFootprint({...view,zoom:view.zoom+1},[-104,35,-92,43]);
  assert.ok(Math.abs((bounds[2]-bounds[0])/(closer[2]-closer[0])-2)<1e-9);
  assert.equal(camera.sameTerrainFootprint(bounds,closer),false);
  assert.equal(camera.sameTerrainFootprint(bounds,rotated),true);
  assert.equal(camera.sameTerrainFootprint(bounds,bounds.map(v=>v+1e-9)),true);
  assert.equal(camera.sameTerrainFootprint(bounds,bounds.map(v=>v+.001)),false);
});

test('invalid or inconsistent viewport transforms retain explicit bounds for downstream coverage validation',()=>{
  const visible=[-90,38,-89,39];
  for(const patch of [{center:[-98,38.5]},{center:[-89.5,38.5],width:0},{center:[-89.5,38.5],zoom:NaN}]){
    assert.deepEqual(camera.terrainViewFootprint({center:[-89.5,38.5],zoom:12,width:1000,height:700,...patch},visible),visible);
  }
});

test('inspection perspective fits all supported height-prism corners on desktop and mobile above the data',()=>{
  const corners=[[-96.59,39.085],[-96.58,39.085],[-96.58,39.095],[-96.59,39.095]];
  for(const [width,height] of [[1280,720],[390,660]])for(const bearing of [-135,-35,0,90])for(const scale of [1,2.5,3])for(const origin of [0,350,900]){
    const heights=[306.4,377.1,388.36];
    const pose=camera.terrainInspectionCamera({corners,heights,scale,width,height,bearing,fieldOfView:36.87,centerElevation:origin});
    assert.equal(pose.pitch,52);assert.equal(pose.bearing,bearing);
    assert.ok(pose.zoom>11&&pose.zoom<=18,'local tile stays local instead of zooming out to Kansas');
    const focal=height/(2*Math.tan(36.87*radians/2)),distance=focal/(512*2**pose.zoom),p=pose.pitch*radians,b=bearing*radians;
    const metres=2*Math.PI*6371008.8*Math.cos(pose.center[1]*radians);
    const cameraOrigin=pose.elevation??origin;
    assert.ok(cameraOrigin+distance*metres*Math.cos(p)>Math.max(...heights)*scale+79);
    let widest=0,tallest=0;
    for(const [lon,lat] of corners)for(const elevation of [Math.min(...heights),Math.max(...heights)]){
      const point=[(lon-pose.center[0])/360,mercatorY(pose.center[1])-mercatorY(lat),(elevation*scale-cameraOrigin)/metres];
      const location=[distance*Math.sin(b)*Math.sin(p),-distance*Math.cos(b)*Math.sin(p),distance*Math.cos(p)];
      const delta=point.map((v,i)=>v-location[i]),dot=axis=>axis.reduce((sum,v,i)=>sum+v*delta[i],0);
      const depth=dot([-Math.sin(b)*Math.sin(p),Math.cos(b)*Math.sin(p),-Math.cos(p)]);
      assert.ok(depth>0,'data cannot be behind the camera');
      const x=dot([Math.cos(b),Math.sin(b),0])/depth*focal/(width/2),y=dot([-Math.sin(b)*Math.cos(p),Math.cos(b)*Math.cos(p),Math.sin(p)])/depth*focal/(height/2);
      widest=Math.max(widest,Math.abs(x));tallest=Math.max(tallest,Math.abs(y));
      assert.ok(Math.abs(x)<=.761&&Math.abs(y)<=.701,`footprint cropped at ${width}×${height}`);
    }
    assert.ok(Math.max(widest,tallest)>.35,'landscape remains visibly large');
  }
});

test('inspection rejects unavailable framing without touching source values or camera state',()=>{
  const base={corners:[[-98,38],[-97.99,38],[-97.99,38.01],[-98,38.01]],heights:[300,320],scale:1,width:1000,height:700,bearing:0,fieldOfView:36,centerElevation:300};
  for(const patch of [{width:0},{fieldOfView:0},{heights:[]},{heights:[NaN]},{scale:0}])assert.throws(()=>camera.terrainInspectionCamera({...base,...patch}));
  const source=structuredClone(base);camera.terrainInspectionCamera(base);assert.deepEqual(base,source);
});

test('same-terrain activation is idempotent and preserves chosen scale, provider, camera and light',async()=>{
  const source=await readFile('app/page.tsx','utf8'),ast=ts.createSourceFile('page.tsx',source,ts.ScriptTarget.Latest,true,ts.ScriptKind.TSX);
  let callback;const walk=node=>{if(ts.isVariableDeclaration(node)&&node.name.getText(ast)==='activateMapRepresentation')callback=node.initializer.getText(ast);ts.forEachChild(node,walk);};walk(ast);assert.ok(callback);
  const calls=[],scope={setPrimaryWorkspace:value=>calls.push(['workspace',value]),projectionRef:{current:'mercator'},scenePresetRef:{current:'elevation-3d'},verticalExaggerationRef:{current:1.3},terrainProviderRef:{current:'usgs-3dep'}};
  const activate=new Function(...Object.keys(scope),compile('return ('+callback+');'))(...Object.values(scope));
  activate('terrain');activate('terrain');
  assert.deepEqual(calls,[['workspace','map'],['workspace','map']]);assert.equal(scope.verticalExaggerationRef.current,1.3);assert.equal(scope.terrainProviderRef.current,'usgs-3dep');
});

test('central 65 percent navigation lease stays anchored through cumulative pans and rejects zoom or viewport changes',()=>{
 const lease={bounds:[-98.02,38.48,-97.98,38.52],zoom:15,width:1000,height:760},pose={center:[-98,38.5],zoom:15,width:1000,height:760};
 const original=structuredClone(lease);
 for(const offset of [.001,.005,.0129])assert.equal(camera.terrainLeaseContains(lease,{...pose,center:[-98+offset,38.5]}),true);
 assert.equal(camera.terrainLeaseContains(lease,{...pose,center:[-97.9869,38.5]}),false,'cumulative boundary crossing loads a new window');
 for(const patch of [{zoom:15.1},{width:1200},{height:800},{center:[-99,38.5]},{center:[-98,38.514]},{center:[NaN,38.5]}])assert.equal(camera.terrainLeaseContains(lease,{...pose,...patch}),false);
 assert.deepEqual(lease,original,'a reuse decision cannot slide or enlarge source coverage');
});


test('pan-window translation preserves Mercator cell spacing and declines genuine zoom/resize changes',()=>{
 const lease={bounds:[-98.02,38.48,-97.98,38.52],zoom:13,width:1280,height:720},view={center:[-97.7,39.1],zoom:13,width:1280,height:720},source=structuredClone(lease);
 const next=camera.terrainPanFootprint(lease,view);assert.ok(next);assert.ok(Math.abs((next[0]+next[2])/2-view.center[0])<1e-12);assert.ok(Math.abs((next[2]-next[0])-(lease.bounds[2]-lease.bounds[0]))<1e-12);assert.ok(Math.abs((mercatorY(next[1])-mercatorY(next[3]))-(mercatorY(lease.bounds[1])-mercatorY(lease.bounds[3])))<1e-12);
 for(const patch of [{zoom:13.1},{width:1000},{height:800},{center:[NaN,38.5]}])assert.equal(camera.terrainPanFootprint(lease,{...view,...patch}),null);
 assert.deepEqual(lease,source,'translation describes only a new query, never relabels source coordinates');
});

test('a distant or missing context elevation cannot make native Fit 3D shrink to a speck',()=>{
 const input={corners:[[-96.587,39.091],[-96.583,39.091],[-96.583,39.089],[-96.587,39.089]],heights:[353.61,382.05],scale:2.5,width:1280,height:582,bearing:-35,fieldOfView:36.87,centerElevation:0};
 const source=structuredClone(input),pose=camera.terrainInspectionCamera(input);
 assert.ok(pose.elevation>=Math.min(...input.heights)*input.scale&&pose.elevation<=Math.max(...input.heights)*input.scale,'explicit fit aims at supported cell heights when context is far away');
 assert.ok(pose.zoom>16,'native detail should occupy a useful part of the view');assert.deepEqual(input,source,'camera targeting does not rebase source measurements');
 const normal=camera.terrainInspectionCamera({...input,centerElevation:900});assert.equal(normal.elevation,undefined,'nearby terrain context keeps its existing camera reference');
});
