import assert from 'node:assert/strict';
import test from 'node:test';
import {readFile} from 'node:fs/promises';
import {createRequire} from 'node:module';
import {build} from 'esbuild';
import ts from 'typescript';
const require=createRequire(import.meta.url);
const bundle=await build({stdin:{contents:"export {GlobeTransform} from './node_modules/maplibre-gl/src/geo/projection/globe_transform.ts';export {LngLat} from './node_modules/maplibre-gl/src/geo/lng_lat.ts';export {OverscaledTileID} from './node_modules/maplibre-gl/src/tile/tile_id.ts';export {MercatorCoordinate} from './node_modules/maplibre-gl/src/geo/mercator_coordinate.ts';export {angularCoordinatesToSurfaceVector} from './node_modules/maplibre-gl/src/geo/projection/globe_utils.ts';",resolveDir:process.cwd(),loader:'ts'},bundle:true,write:false,platform:'node',format:'cjs',target:'es2022',tsconfigRaw:{compilerOptions:{useDefineForClassFields:false}}});
const module={exports:{}};new Function('module','exports','require',bundle.outputFiles[0].text)(module,module.exports,require);
const {GlobeTransform,LngLat,OverscaledTileID,MercatorCoordinate,angularCoordinatesToSurfaceVector}=module.exports;
const sky={};new Function('exports',ts.transpileModule(await readFile('app/kansas-sky.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(sky);
const renderer={};new Function('exports','require','document',ts.transpileModule(await readFile(process.env.KFM_SKY_LAYER_PATH??'app/kansas-sky-layer.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(renderer,name=>name==='./kansas-sky'?sky:name==='./aviation-traffic'?{TRAFFIC_ALTITUDE_COLORS:[[0,'#cccccc']]}:require(name),{hidden:false});
const mult=(m,v)=>Array.from({length:4},(_,r)=>m[r]*v[0]+m[4+r]*v[1]+m[8+r]*v[2]+m[12+r]*v[3]);
const ndc=v=>v.slice(0,3).map(x=>x/v[3]);
const close=(a,b,message)=>{for(let i=0;i<a.length;i++)assert.ok(Math.abs(a[i]-b[i])<1e-4,`${message}: axis${i}, actual${a[i]}, expected${b[i]}`);};
const plane={hex:'abc123',lon:-98.35,lat:38.5,onGround:false,altGeomFt:5000,altBaroFt:4800,trackDeg:90,rollDeg:null,emergency:null};
function harness(transition,requested='globe',zoom=8,terrainElevation=0,onProjection,maxPointSize=256){
 const tr=new GlobeTransform();tr.resize(1280,800);tr.setCenter(new LngLat(plane.lon,plane.lat));tr.setZoom(zoom);tr.setPitch(55);tr.setTransitionState(transition);tr.setElevation(terrainElevation);
 const shaders=[],fragments=[],uniforms={},draws=[];let layer,depthWrites=false,bound,serial=0;const uploads=[];
 const gl=new Proxy({VERTEX_SHADER:35633,ONE:1,ONE_MINUS_SRC_ALPHA:771,LINES:1,TRIANGLES:4,POINTS:0,getParameter:()=>[1,maxPointSize],createShader:kind=>({kind}),shaderSource:(shader,source)=>{shader.source=source;if(shader.kind===35633)shaders.push(source);else fragments.push(source);},getShaderParameter:()=>true,getProgramParameter:()=>true,getAttribLocation:()=>0,getUniformLocation:(_p,name)=>name,uniformMatrix4fv:(name,_transpose,value)=>uniforms[name]=Array.from(value),uniform4f:(name,...value)=>uniforms[name]=value,uniform2f:(name,...value)=>uniforms[name]=value,uniform1f:(name,value)=>uniforms[name]=value,depthMask:value=>depthWrites=value,drawArrays:(mode,start,count)=>draws.push({mode,start,count,depthWrites}),createBuffer:()=>({id:++serial}),bindBuffer:(_target,buffer)=>bound=buffer,bufferSubData:(_target,offset,data)=>uploads.push({buffer:bound.id,offset,data:new Float32Array(data)})},{get:(o,k)=>k in o?o[k]:()=>({})});
 const map={isStyleLoaded:()=>true,getLayer:()=>layer,getZoom:()=>zoom,getCenter:()=>tr.center,getProjection:()=>({type:requested}),getCanvas:()=>({clientWidth:1280,clientHeight:800}),on(){},off(){},triggerRepaint(){},queryTerrainElevation:()=>0,addLayer:l=>{layer=l;l.onAdd(map,gl);},removeLayer(){layer.onRemove();layer=undefined;}};
 const selected=[];const attachment=renderer.attachKansasSky(map,hex=>selected.push(hex),message=>assert.fail(message),onProjection);
 const input={modelViewProjectionMatrix:tr.modelViewProjectionMatrix,shaderData:{variantName:transition?'globe':'mercator',vertexShaderPrelude:'uniform mat4 u_projection_matrix;',define:transition?'#define GLOBE':'#define PROJECTION_MERCATOR'},defaultProjectionData:tr.getProjectionDataForCustomLayer(),getProjectionData:({tileID,applyGlobeMatrix})=>tr.getProjectionData({overscaledTileID:new OverscaledTileID(tileID.canonical.z,0,tileID.canonical.z,tileID.canonical.x,tileID.canonical.y),applyGlobeMatrix})};
 return {tr,map,gl,attachment,uniforms,draws,uploads,shaders,fragments,input,selected,draw(observed=plane){attachment.update([observed],[],observed.hex,false,false,false);layer.render(gl,input);}};
}
// Evaluate the actual renderer's position expression with installed MapLibre
// matrices. This is shader algebra/CPU evidence, not a GPU/browser result.
function projected(h,observed=plane){
 const source=h.shaders[0],body=source.slice(source.indexOf('void main()'));
 const xy=MercatorCoordinate.fromLngLat([observed.lon,observed.lat]),height=observed.altGeomFt*.3048;
 if(body.includes('u_matrix*vec4'))return mult(h.uniforms.u_matrix,[xy.x*h.uniforms.u_world,xy.y*h.uniforms.u_world,height,1]);
 const tileScale=/projectTile(?:For3D|WithElevation)\(\(u_origin\+a_position.xy\)\*8192/.test(body)?8192:1;
 const flat=mult(h.uniforms.u_projection_fallback_matrix??h.uniforms.u_projection_matrix,[xy.x*tileScale,xy.y*tileScale,height,1]);
 if(!h.input.shaderData.define.includes('GLOBE'))return mult(h.uniforms.u_projection_matrix,[xy.x*tileScale,xy.y*tileScale,height,1]);
 const sphere=Array.from(angularCoordinatesToSurfaceVector(new LngLat(observed.lon,observed.lat)),x=>x*(1+height/6371008.8)),globe=mult(h.uniforms.u_projection_matrix,[...sphere,1]),t=h.uniforms.u_projection_transition;
 if(body.includes('projectTileWithElevation')){const p=h.uniforms.u_projection_clipping_plane;globe[2]=(1-(sphere[0]*p[0]+sphere[1]*p[1]+sphere[2]*p[2]+p[3]))*globe[3];if(t>.999)return globe;return globe.map((x,i)=>i===2?x*Math.max(0,Math.min(1,(t-.2)/.8)):flat[i]*(1-t)+x*t);}
 return t>.999?globe:globe.map((x,i)=>flat[i]*(1-t)+x*t);
}
for(const [name,transition,requested]of [['ordinary Mercator',0,'mercator'],['globe request with actual Mercator shader',0,'globe'],['projection transition',.5,'globe'],['true globe',1,'globe']])for(const terrainElevation of [0,620])test(`aircraft meter heights preserve actual3D projection in ${name}, camera elevation${terrainElevation}m`,()=>{
 const h=harness(transition,requested,8,terrainElevation);h.draw();const p=MercatorCoordinate.fromLngLat([plane.lon,plane.lat]),height=plane.altGeomFt*.3048;
 const worldData=h.tr.getProjectionData({overscaledTileID:new OverscaledTileID(0,0,0,0,0),applyGlobeMatrix:true});
 const flat=mult(worldData.fallbackMatrix,[p.x*8192,p.y*8192,height,1]);const sphere=Array.from(angularCoordinatesToSurfaceVector(new LngLat(plane.lon,plane.lat)),x=>x*(1+height/6371008.8));const globe=mult(worldData.mainMatrix,[...sphere,1]);
 const expected=transition===0?flat:transition===1?globe:globe.map((x,i)=>flat[i]*(1-transition)+x*transition);
 close(ndc(projected(h)),ndc(expected),'aircraft elevation/clip depth matches installed projection');h.attachment.dispose();
});
test('opaque aircraft establish depth while transparent effects leave the depth buffer unchanged',()=>{const h=harness(0,'mercator');h.draw();assert.equal(h.draws.find(d=>d.mode===4&&d.count===24).depthWrites,true);assert.ok(h.draws.filter(d=>d.mode===1||d.mode===0).every(d=>!d.depthWrites));h.attachment.dispose();});
test('close zoom keeps schematic wings bounded in screen space',()=>{const spans=[];for(const zoom of [9.7,12,16]){const h=harness(0,'mercator',zoom);h.draw();const data=h.uploads.find(u=>u.buffer===1&&u.offset===0).data;spans.push(Math.hypot(data[12*6]-data[17*6],data[12*6+1]-data[17*6+1])*512*2**zoom);h.attachment.dispose();}assert.ok(Math.max(...spans)<65,JSON.stringify(spans));assert.ok(Math.min(...spans)>40,JSON.stringify(spans));});


test('globe horizon clipping remains independent from projected3D depth',()=>{
 const h=harness(1,'globe',3);h.draw();
 const assignments=[...h.shaders[0].matchAll(/v_visibility=([^;]+);/g)];assert.equal(assignments.length,2);
 const expression=assignments[1][1],p=h.uniforms.u_projection_clipping_plane;
 const visibility=coordinate=>{
  const elevated=Array.from(angularCoordinatesToSurfaceVector(new LngLat(...coordinate)),x=>x*(1+1524/6371008.8));
  return new Function('elevated','globeComputeClippingZ','clamp','u_projection_transition',`return ${expression}`)(elevated,v=>1-(v[0]*p[0]+v[1]*p[1]+v[2]*p[2]+p[3]),(v,min,max)=>Math.max(min,Math.min(max,v)),1);
 };
 const predicate=h.fragments[0].match(/if\((v_visibility[^)]+)\)discard;/)?.[1];assert.ok(predicate);
 const discarded=value=>new Function('v_visibility',`return ${predicate}`)(value);
 assert.equal(discarded(visibility([plane.lon,plane.lat])),false,'front-side elevated aircraft remains visible');
 assert.equal(discarded(visibility([plane.lon+180,-plane.lat])),true,'hidden hemisphere remains clipped without replacing actual depth');h.attachment.dispose();
});


test('schematic orientation distinguishes supplied heading from path direction and preserves rigid reported bank',()=>{
 for(const [extra,axis,sign]of [[{trueHeadingDeg:90,renderedTrackDeg:0},0,1],[{trueHeadingDeg:null,renderedTrackDeg:0},1,-1],[{trueHeadingDeg:null,renderedTrackDeg:null,trackDeg:270},0,-1]]){
  const h=harness(0,'mercator',9.7);h.draw({...plane,...extra});const p=h.uploads.find(u=>u.buffer===1&&u.offset===0).data;
  assert.ok(p[axis]*sign>0);assert.ok(Math.abs(p[1-axis])<1e-9,'the first nose vertex uses the selected direction basis');h.attachment.dispose();
 }
 const spans=[];for(const roll of [0,30,90]){
  const h=harness(0,'mercator',9.7);h.draw({...plane,trackDeg:0,rollDeg:roll});const p=h.uploads.find(u=>u.buffer===1&&u.offset===0).data,left=12*6,right=17*6,unit=1/(40075016.686*Math.cos(plane.lat*Math.PI/180));
  const east=(p[right]-p[left])/unit,north=(p[right+1]-p[left+1])/unit,up=p[right+2]-p[left+2];spans.push(Math.hypot(east,north,up));if(roll)assert.ok(up<0,'reported right bank lowers the right wing');h.attachment.dispose();
 }
 assert.ok(Math.max(...spans)-Math.min(...spans)<.002,'bank rotates the enlarged rigid symbol without stretching its wings');
});

const controlSource=await readFile(process.env.KFM_SKY_CONTROL_PATH??'app/kansas-sky-control.tsx','utf8'),controlAst=ts.createSourceFile('control.tsx',controlSource,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
const controlParts={};let followEffect,followCall;function visitControl(node){if(ts.isVariableDeclaration(node)&&['cameraElevation','flightPadding'].includes(node.name.getText(controlAst)))controlParts[node.name.getText(controlAst)]=node.initializer.getText(controlAst);if(ts.isFunctionDeclaration(node)&&node.name?.text==='flightCamera')controlParts.flightCamera=node.getText(controlAst);if(ts.isCallExpression(node)&&node.expression.getText(controlAst)==='useEffect'&&node.arguments[0].getText(controlAst).includes('camera!=="follow"')){followEffect=node.arguments[0].getText(controlAst);followCall=node.getText(controlAst);}ts.forEachChild(node,visitControl);}visitControl(controlAst);
const evaluateControl=(source,scope)=>new Function(...Object.keys(scope),ts.transpileModule(`return (${source});`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText)(...Object.values(scope));
const cameraScope={cameraElevation:evaluateControl(controlParts.cameraElevation,{}),flightPadding:evaluateControl(controlParts.flightPadding,{})};if(controlParts.flightCamera)cameraScope.flightCamera=evaluateControl(controlParts.flightCamera,cameraScope);
for(const [width,height,dockTop]of [[375,730,319.65625],[390,762,351],[768,970,144],[1440,846,144]])test(`actual Follow callback keeps elevated aircraft and halo clear at ${width}px across projection phases`,()=>{
 for(const phase of [0,.25,.5,.75,1])for(const bearing of [0,90,180,255.4])for(const zoom of [9.7,16]){
  const observed={...plane,lon:-93.601844,lat:39.100571,altGeomFt:18600,trackDeg:bearing},h=harness(phase,'globe',zoom,observed.altGeomFt*.3048);h.tr.resize(width,height);h.tr.setFov(42);
  Object.assign(h.map,{getCanvas:()=>({clientWidth:width,clientHeight:height,getBoundingClientRect:()=>({top:54,bottom:height+54,right:width})}),getContainer:()=>({querySelector:()=>({getBoundingClientRect:()=>({left:width>760?width-400:10,top:dockTop})}),querySelectorAll:()=>width<=760?[{getBoundingClientRect:()=>({top:120,bottom:165.34375,width:187.5,height:45.34375})}]:[]}),getZoom:()=>h.tr.zoom,getBearing:()=>bearing,getVerticalFieldOfView:()=>h.tr.fov,jumpTo:options=>{h.tr.setCenter(new LngLat(...options.center));if(options.zoom!==undefined)h.tr.setZoom(options.zoom);h.tr.setElevation(options.elevation);h.tr.setPitch(options.pitch);h.tr.setBearing(options.bearing);h.tr.setPadding(options.padding);}});
  evaluateControl(followEffect,{...cameraScope,mapRef:{current:h.map},picked:observed,camera:'follow',mode:'recorded',playing:false,reduced:false,flat:false,hidden:false,enabled:true,projectionPhase:phase,layer:{current:{projection:()=>phase}},ownCameraMove:{current:false}})();h.draw(observed);
  const v=projected(h,observed),x=(v[0]/v[3]+1)*width/2,y=(1-v[1]/v[3])*height/2,center=h.tr.centerPoint;
  assert.ok(v[3]>0,`${width}px phase${phase} zoom${zoom}: aircraft is in front of the camera`);
  assert.ok(Math.hypot(x-center.x,y-center.y)<2,`${width}px phase${phase} zoom${zoom} bearing${bearing}: aircraft center [${x},${y}] misses camera focal point [${center.x},${center.y}]`);
  if(width<=760){assert.ok(y+54-30>165.34375,'aircraft/halo clears the fixed replay badge');assert.ok(y+54+30<dockTop,'aircraft/halo clears the flight deck');}
  h.attachment.dispose();
 }
});

test('projection phase notifications are actual-frame based, coalesced, and cancelled on disposal',async()=>{
 const received=[],h=harness(0,'globe',9.7,0,phase=>received.push(phase));
 assert.equal(h.attachment.projection(),null,'requested globe does not imply a rendered projection');h.draw();h.draw();assert.equal(h.attachment.projection(),0);assert.deepEqual(received,[]);await Promise.resolve();assert.deepEqual(received,[0]);
 h.tr.setTransitionState(.5);h.input.shaderData.variantName='globe';h.input.shaderData.define='#define GLOBE';h.draw();h.tr.setTransitionState(1);h.draw();await Promise.resolve();assert.deepEqual(received,[0,1],'one queued notification uses the latest rendered phase');
 h.draw();await Promise.resolve();assert.deepEqual(received,[0,1],'stationary projection emits no repaint notification loop');
 h.tr.setTransitionState(.25);h.draw();h.attachment.dispose();await Promise.resolve();assert.deepEqual(received,[0,1],'disposed layer cannot reframe a paused camera');
});

test('paused Follow reacts to actual projection changes and releases that ownership in free explore',()=>{
 let phase=null,previous,cleanup;const moves=[],mapRef={current:{getZoom:()=>9.7,getBearing:()=>90,getVerticalFieldOfView:()=>42,getCanvas:()=>({clientWidth:375,clientHeight:730}),jumpTo:options=>moves.push(options),queryTerrainElevation:()=>0}},layer={current:{projection:()=>phase}},picked={...plane,altGeomFt:18600},ownCameraMove={current:false};
 const useEffect=(effect,deps)=>{if(!previous||deps.some((value,index)=>!Object.is(value,previous[index]))){cleanup?.();cleanup=effect();previous=deps;}};
 const render=(camera='follow')=>evaluateControl(`()=>{${followCall};}`,{...cameraScope,useEffect,mapRef,picked,camera,mode:'recorded',playing:false,reduced:false,flat:false,hidden:false,enabled:true,projectionPhase:phase,layer,ownCameraMove})();
 render();assert.equal(moves.length,0,'unknown render phase waits for the actual frame');phase=0;render();assert.equal(moves.length,1);assert.deepEqual(moves[0].center,[picked.lon,picked.lat]);
 phase=1;render();assert.equal(moves.length,2);assert.notDeepEqual(moves[1].center,moves[0].center,'a paused globe camera aims through the elevated position');render();assert.equal(moves.length,2,'unchanged phase does not restart camera work');
 render('free');phase=.5;render('free');assert.equal(moves.length,2,'manual exploration cancels projection-driven reframing');assert.equal(ownCameraMove.current,false);
});

test('Mercator picking matches the elevated public world-tile render position',()=>{
 for(const requested of ['mercator','globe'])for(const zoom of [9.7,16]){
  const h=harness(0,requested,zoom,plane.altGeomFt*.3048);h.draw();const clip=projected(h),point={x:(clip[0]/clip[3]+1)*1280/2,y:(1-clip[1]/clip[3])*800/2};
  assert.equal(renderer.pickKansasSkyAircraft(h.map,point),true,`${requested} zoom${zoom}: rendered aircraft center is pickable`);
  assert.equal(renderer.pickKansasSkyAircraft(h.map,{x:point.x+40,y:point.y+40}),false,'outside the symbol hit radius remains a miss');h.attachment.dispose();
 }
});


test('actual globe and transition aircraft centers are selectable without claiming surrounding map clicks',()=>{
 for(const phase of [0,.25,.5,.75,1])for(const zoom of [3,6,9.7]){
  const h=harness(phase,'globe',zoom);h.draw();const clip=projected(h),point={x:(clip[0]/clip[3]+1)*1280/2,y:(1-clip[1]/clip[3])*800/2};
  assert.equal(renderer.pickKansasSkyAircraft(h.map,point),true,`phase${phase} zoom${zoom}: actual rendered aircraft center is selectable`);
  assert.deepEqual(h.selected,[plane.hex]);
  assert.equal(renderer.pickKansasSkyAircraft(h.map,{x:point.x+45,y:point.y+45}),false,'surrounding geography remains available to ordinary map picking');h.attachment.dispose();
 }
});

test('globe hidden hemisphere and offscreen aircraft cannot own clicks',()=>{
 for(const observed of [{...plane,lon:plane.lon+180,lat:-plane.lat},{...plane,lon:plane.lon+80}]){
  const h=harness(1,'globe',3);h.draw(observed);const clip=projected(h,observed),point={x:(clip[0]/clip[3]+1)*1280/2,y:(1-clip[1]/clip[3])*800/2};
  assert.equal(renderer.pickKansasSkyAircraft(h.map,point),false,'hidden or clipped geometry cannot be selected through the map');h.attachment.dispose();
 }
});

test('regional and close aircraft receive a bounded high contrast screen locator at the observed center',()=>{
 for(const phase of [0,.5,1])for(const zoom of [3,6,9.7,16]){
  const h=harness(phase,'globe',zoom);h.draw();
  const markerShader=h.shaders.find(source=>source.includes('v_marker_direction'));
  assert.ok(markerShader,'a GPU locator remains available when world-size wings become tiny');
  assert.ok(h.draws.some(draw=>draw.mode===0&&draw.count===1),'selected and unselected locators use bounded point draws');
  assert.ok(h.uniforms.u_marker_size>=18&&h.uniforms.u_marker_size<=42,'the locator has deliberate CSS pixel bounds at every zoom');
  assert.match(h.fragments.find(source=>source.includes('v_marker_direction')),/vec3\(\.02,\.08,\.12\)/,'a dark backing keeps the silhouette legible on light terrain');
  h.attachment.dispose();
 }
});


test('decorative Kansas curtain uses public world-tile 3D depth and bounded non-additive light in both projections',async()=>{
 const curtain={};new Function('exports',ts.transpileModule(await readFile('app/aurora-curtain-layer.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(curtain);
 for(const phase of [0,.5,1]){
  const h=harness(phase,'globe',6),blend=[];
  h.gl.blendFunc=(...args)=>blend.push(args);Object.assign(h.map,{getTerrain:()=>({source:'dem',exaggeration:2.5}),getBounds:()=>({getWest:()=>-110,getEast:()=>-90,getSouth:()=>30,getNorth:()=>45})});
  const layer=curtain.createAuroraCurtainLayer({id:'test-curtain',ring:[[plane.lon,plane.lat],[plane.lon+.01,plane.lat],[plane.lon,plane.lat+.01],[plane.lon,plane.lat]],clock:()=>null});layer.onAdd(h.map,h.gl);layer.render(h.gl,h.input);
  assert.match(h.shaders[0],/projectTileFor3D\(a_pos\s*\*\s*8192/,'the curtain uses the same public 3D position contract as aircraft');
  const expected=h.tr.getProjectionData({overscaledTileID:new OverscaledTileID(0,0,0,0,0),applyGlobeMatrix:true});
  close(h.uniforms.u_projection_matrix,Array.from(expected.mainMatrix),'world-tile matrix matches installed MapLibre');
  assert.ok(h.uniforms.u_height<=8000,'decorative height stays modest statewide and is independent of DEM exaggeration');
  assert.equal(blend.at(-1)[1],h.gl.ONE_MINUS_SRC_ALPHA,'premultiplied alpha preserves basemap contrast instead of adding white');
  assert.match(h.fragments[0],/v_visibility<0\./,'hidden hemisphere clipping is independent of 3D depth');
  layer.onRemove(h.map,h.gl);h.attachment.dispose();
 }
});


test('locator point limits are sampled on attachment and hit extents match high-density hardware clamping',()=>{
 const h=harness(0,'mercator',6,0,undefined,32);h.map.getCanvas=()=>({clientWidth:1280,clientHeight:800,width:2560});h.draw();
 assert.equal(h.uniforms.u_pixel_ratio,2);assert.equal(h.uniforms.u_marker_max_size,32);
 const clip=projected(h),point={x:(clip[0]/clip[3]+1)*640,y:(1-clip[1]/clip[3])*400};
 assert.equal(renderer.pickKansasSkyAircraft(h.map,point),true);assert.equal(renderer.pickKansasSkyAircraft(h.map,{x:point.x+9,y:point.y}),false,'a hardware-limited 16 CSS-pixel locator owns only its visible radius');
 assert.match(h.shaders.find(source=>source.includes('v_marker_direction')),/gl_PointSize=min\(/,'the actual shader applies the one-time capability limit');h.attachment.dispose();
});
