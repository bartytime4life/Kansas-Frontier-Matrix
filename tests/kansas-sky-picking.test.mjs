import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
import Point from '@mapbox/point-geometry';
import {LngLatBounds,MercatorCoordinate} from 'maplibre-gl';
import {build} from 'esbuild';
import {createRequire} from 'node:module';
const globe=await import(`data:text/javascript;base64,${Buffer.from(ts.transpileModule(await readFile('app/globe-context.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`);
const skySource=await readFile('app/kansas-sky.ts','utf8');
const skyHelpers=await import(`data:text/javascript;base64,${Buffer.from(ts.transpileModule(skySource,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`);

// Exercise the actual renderer's projected-hit lifecycle with a mock GL seam;
// actual shader/GPU rendering remains the separate built-app browser test.
const source=await readFile('app/kansas-sky-layer.ts','utf8');
const code=ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
const exports={};
new Function('exports','require','document',code)(exports,name=>{
  if(name==='./aviation-traffic')return {TRAFFIC_ALTITUDE_COLORS:[[0,'#7d8a96']]};
  if(name==='./kansas-sky')return skyHelpers;
  throw Error(`Unexpected renderer dependency ${name}`);
},{hidden:false});
const {attachKansasSky,pickKansasSkyAircraft,attachKansasSkyFocus}=exports;
function fixture(loaded=true,{failStroke=false}={}){
  const layers=new Map(),events=[],listeners=new Map();
  let styleLoaded=loaded,vertices=new Float32Array(),bufferSerial=0,boundBuffer;const uploads=[],draws=[],blends=[],shaderSources=new Map();
  const gl=new Proxy({createBuffer:()=>({id:++bufferSerial}),bindBuffer:(_target,buffer)=>{boundBuffer=buffer;},LINES:1,TRIANGLES:4,POINTS:0,SRC_ALPHA:770,ONE_MINUS_SRC_ALPHA:771,ONE:1,createShader:()=>({}),shaderSource:(shader,source)=>shaderSources.set(shader,source),drawArrays:(...args)=>draws.push(args),blendFuncSeparate:(...args)=>blends.push(args),bufferSubData:(_target,_offset,value)=>{vertices=new Float32Array(value);uploads.push({buffer:boundBuffer?.id,offset:_offset,data:vertices});},getShaderParameter:shader=>!(failStroke&&shaderSources.get(shader)?.includes("in vec3 a_other")),getProgramParameter:()=>true,getAttribLocation:()=>0,getUniformLocation:()=>null},
    {get:(target,key)=>key in target?target[key]:()=>({})});
  const map={isStyleLoaded:()=>styleLoaded,getLayer:id=>layers.get(id),getZoom:()=>0,getProjection:()=>({type:'mercator'}),getCanvas:()=>({clientWidth:100,clientHeight:100}),
    on(name,fn){events.push(['on',name]);if(!listeners.has(name))listeners.set(name,new Set());listeners.get(name).add(fn);},
    off(name,fn){events.push(['off',name]);listeners.get(name)?.delete(fn);},triggerRepaint(){},queryTerrainElevation:()=>0,
    addLayer(layer){layers.set(layer.id,layer);layer.onAdd(map,gl);},removeLayer(id){layers.get(id)?.onRemove();layers.delete(id);}};
  const matrix=[1/512,0,0,0,0,1/512,0,0,0,0,0,0,-.25,-.5,0,1];
  return {map,events,uploads,draws,blends,vertices:()=>vertices,setStyleLoaded:value=>{styleLoaded=value;},emit:(name,event)=>{for(const fn of [...(listeners.get(name)??[])])fn(event);},listenerCount:name=>listeners.get(name)?.size??0,draw:()=>layers.get('kfm-kansas-sky').render(gl,{modelViewProjectionMatrix:matrix,shaderData:{variantName:'mercator',vertexShaderPrelude:'uniform mat4 u_projection_matrix;',define:'#define PROJECTION_MERCATOR'},getProjectionData:()=>({mainMatrix:matrix,fallbackMatrix:matrix,tileMercatorCoords:[0,0,1/8192,1/8192],clippingPlane:[0,0,0,1],projectionTransition:0})})};
}
const aircraft={hex:'abc123',lon:-90,lat:0,onGround:false,altGeomFt:5000,altBaroFt:4800,trackDeg:90,rollDeg:null,emergency:null};
for(const readyEvent of ['render','error'])for(const phase of ['initial attachment','replacement style'])test(`aircraft renderer recovers after pending ${phase} on ${readyEvent} and cancels disposed work`,()=>{
  const f=fixture(phase!=='initial attachment'),selected=[];
  const renderer=attachKansasSky(f.map,hex=>selected.push(hex),message=>assert.fail(message));
  renderer.update([aircraft],[],null);
  if(phase==='replacement style'){
    f.draw();
    f.map.removeLayer('kfm-kansas-sky');
    f.setStyleLoaded(false);
    f.emit('style.load');
  }
  assert.equal(f.map.getLayer('kfm-kansas-sky'),undefined,'pending source work cannot install the layer');
  f.setStyleLoaded(true);
  f.emit(readyEvent);
  assert.ok(f.map.getLayer('kfm-kansas-sky'),'a ready frame installs the retained renderer without another style.load');
  f.draw();
  assert.equal(pickKansasSkyAircraft(f.map,{x:50,y:50}),true,'observations received while waiting become pickable');
  assert.deepEqual(selected,['abc123']);
  assert.equal(f.listenerCount('render'),0,'the completed install releases its frame listener');
  assert.equal(f.listenerCount('error'),0,'the completed install releases its settlement listener');
  f.map.removeLayer('kfm-kansas-sky');f.setStyleLoaded(false);f.emit('style.load');
  renderer.dispose();f.setStyleLoaded(true);f.emit('render');f.emit('error');f.emit('style.load');
  assert.equal(f.map.getLayer('kfm-kansas-sky'),undefined,'disposal cannot resurrect a pending renderer');
  assert.equal(f.listenerCount('render'),0,'disposal removes pending frame work');
  assert.equal(f.listenerCount('error'),0,'disposal removes pending settlement work');
  assert.equal(pickKansasSkyAircraft(f.map,{x:50,y:50}),false);
});
test('aircraft click ownership uses projected hits, preserves misses, and unregisters on disposal',()=>{
  const f=fixture(),selected=[];
  assert.equal(pickKansasSkyAircraft(f.map,{x:50,y:50}),false,'unmounted layer owns no clicks');
  const renderer=attachKansasSky(f.map,hex=>selected.push(hex),message=>assert.fail(message));
  assert.equal(f.events.some(([,name])=>name==='click'),false,'page remains the sole aircraft click dispatcher');
  renderer.update([aircraft],[],null);f.draw();
  assert.equal(pickKansasSkyAircraft(f.map,{x:0,y:0}),false);
  assert.deepEqual(selected,[]);
  assert.equal(pickKansasSkyAircraft(f.map,{x:50,y:50}),true);
  assert.deepEqual(selected,['abc123']);
  renderer.update([],[],null);f.draw();
  assert.equal(pickKansasSkyAircraft(f.map,{x:50,y:50}),false,'cleared observations leave no clickable stale aircraft');
  renderer.update([aircraft],[],null);f.draw();renderer.dispose();
  assert.equal(pickKansasSkyAircraft(f.map,{x:50,y:50}),false,'disposed layer owns no clicks');
  assert.deepEqual(selected,['abc123']);
});
test('page dispatch respects dedicated pick modes, aircraft hits and ordinary-context misses',async()=>{
  const page=await readFile('app/page.tsx','utf8');
  const ast=ts.createSourceFile('page.tsx',page,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
  let callback;
  function visit(node){
    if(ts.isCallExpression(node)&&node.expression.getText(ast)==='map.on'&&node.arguments[0]?.getText(ast)==='"click"'&&node.arguments[1]?.getText(ast).includes('pickKansasSkyAircraft'))callback=node.arguments[1].getText(ast);
    ts.forEachChild(node,visit);
  }
  visit(ast);assert.ok(callback,'actual map dispatcher includes aircraft ownership');
  for(const mode of ['aviation','underground','measure','aircraft','miss']){
    let picks=0;
    const scope={aviationPickingRef:{current:mode==='aviation'},undergroundOpenRef:{current:mode==='underground'},measureModeRef:{current:mode==='measure'?'point':null},
      measureCoordinatesRef:{set current(_value){throw Error('measurement owns click');}},
      pickKansasSkyAircraft:()=>{picks++;return mode==='aircraft';},GEOLOGY_POINT_LAYER_IDS:[],map:{queryRenderedFeatures(){throw Error('ordinary context owns click');}}};
    const output=ts.transpileModule(`return ${callback};`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
    const click=new Function(...Object.keys(scope),output)(...Object.values(scope));
    if(mode==='measure')assert.throws(()=>click({point:{x:50,y:50},lngLat:{lng:-90,lat:0}}),/measurement owns click/);
    else if(mode==='miss')assert.throws(()=>click({point:{x:0,y:0}}),/ordinary context owns click/);
    else click({point:{x:50,y:50}});
    assert.equal(picks,mode==='aircraft'||mode==='miss'?1:0,'higher-priority tools prevent aircraft inspection');
  }
});

// Exercise the actual React camera callbacks, including release of shared map ownership.
const cameraControlSource=await readFile(process.env.KFM_SKY_CONTROL_PATH??'app/kansas-sky-control.tsx','utf8');
const cameraAst=ts.createSourceFile('camera.tsx',cameraControlSource,ts.ScriptTarget.ES2022,true,ts.ScriptKind.TSX);
const cameraEffects=[];let elevationInitializer,paddingInitializer,journeyFit,flightCameraDeclaration;
function cameraNodes(node){
 if(ts.isCallExpression(node)&&node.expression.getText(cameraAst)==='useEffect')cameraEffects.push(node.arguments[0].getText(cameraAst));
 if(ts.isVariableDeclaration(node)&&node.name.getText(cameraAst)==='cameraElevation')elevationInitializer=node.initializer.getText(cameraAst);
 if(ts.isVariableDeclaration(node)&&node.name.getText(cameraAst)==='flightPadding')paddingInitializer=node.initializer.getText(cameraAst);
 if(ts.isFunctionDeclaration(node)&&node.name?.text==='fitSkyJourney')journeyFit=node.getText(cameraAst);
 if(ts.isFunctionDeclaration(node)&&node.name?.text==='flightCamera')flightCameraDeclaration=node.getText(cameraAst);
 ts.forEachChild(node,cameraNodes);
}cameraNodes(cameraAst);
const executeCamera=(text,scope)=>{scope={projectionPhase:0,...scope};if(!scope.layer)scope.layer={current:{projection:()=>scope.projectionPhase}};if(text.includes('flightCamera(')&&text!==flightCameraDeclaration&&!scope.flightCamera)scope.flightCamera=executeCamera(flightCameraDeclaration,{cameraElevation:executeCamera(elevationInitializer,{}),flightPadding:executeCamera(paddingInitializer,{})});return new Function(...Object.keys(scope),ts.transpileModule(`return (${text});`,{compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText)(...Object.values(scope));};
const mapCameraSource=await readFile('node_modules/maplibre-gl/src/geo/projection/camera_helper.ts','utf8');
const mapCameraAst=ts.createSourceFile('mapCamera.ts',mapCameraSource,ts.ScriptTarget.ES2022,true);
const fittingFunction=mapCameraAst.statements.find(node=>ts.isFunctionDeclaration(node)&&node.name?.text==='cameraForBoxAndBearing');
const cameraForBounds=executeCamera(fittingFunction.getText(mapCameraAst).replace(/^export /,''),{Point,degreesToRadians:value=>value*Math.PI/180,scaleZoom:Math.log2,zoomScale:value=>2**value,cameraBoundsWarning:()=>{},projectToWorldCoordinates:(size,location)=>{const p=MercatorCoordinate.fromLngLat(location);return new Point(p.x*size,p.y*size);},unprojectFromWorldCoordinates:(size,point)=>new MercatorCoordinate(point.x/size,point.y/size).toLngLat()});
// Execute the installed renderer's Camera + MercatorTransform, including pitch,
// altitude projection, minZoom and maxBounds constraints. No GPU/FPS claim.
const cameraBundle=await build({stdin:{contents:"export {Camera} from './node_modules/maplibre-gl/src/ui/camera.ts'; export {LngLatBounds} from './node_modules/maplibre-gl/src/geo/lng_lat_bounds.ts'; export {MapMovementEvent} from './node_modules/maplibre-gl/src/ui/events.ts';",resolveDir:process.cwd(),loader:'ts'},bundle:true,write:false,platform:'node',format:'cjs',target:'es2022',tsconfigRaw:{compilerOptions:{useDefineForClassFields:false}}}),cameraModule={exports:{}};
new Function('module','exports','require','matchMedia',cameraBundle.outputFiles[0].text)(cameraModule,cameraModule.exports,createRequire(import.meta.url),()=>({matches:false,addEventListener(){}}));
const mapSourceAst=ts.createSourceFile('map.ts',await readFile('node_modules/maplibre-gl/src/ui/map.ts','utf8'),ts.ScriptTarget.ES2022,true);
const styleSourceAst=ts.createSourceFile('style.ts',await readFile('node_modules/maplibre-gl/src/style/style.ts','utf8'),ts.ScriptTarget.ES2022,true);
const actualMethod=(ast,name,scope={})=>{let method;const visit=node=>{if(ts.isMethodDeclaration(node)&&node.name.getText(ast)===name)method=node.getText(ast);ts.forEachChild(node,visit);};visit(ast);assert.ok(method,name);return executeCamera(`function ${method}`,scope);};
const actualMapBounds=actualMethod(mapSourceAst,'setMaxBounds',{LngLatBounds:cameraModule.exports.LngLatBounds});
const actualMapMinZoom=actualMethod(mapSourceAst,'setMinZoom',{defaultMinZoom:-2,MapMovementEvent:cameraModule.exports.MapMovementEvent});
const actualMapProjection=actualMethod(mapSourceAst,'setProjection'),actualStyleProjection=actualMethod(styleSourceAst,'setProjection');
const routePoints=JSON.parse(await readFile('public/data/aviation/replays/days/2026-11-03/2026-11-03-ac2fea-p0001.json','utf8')).points;
test('real pitched MapLibre camera keeps the observed route outside docks and retains its fit through projection updates',()=>{
 const fit=executeCamera(journeyFit,{flightPadding:executeCamera(paddingInitializer,{})});
 for(const [width,height,dock]of [[1280,610,{left:917,top:90}],[390,700,{left:12,top:370}],[820,800,{left:430,top:90}]]){
  const map=new cameraModule.exports.Camera({minZoom:4,maxZoom:16,maxPitch:72,renderWorldCopies:false,transformConstrain:null,centerClampedToGround:false,terrain:{getElevationForLngLat:()=>620,getElevationForLngLatZoom:()=>620,getMinTileElevationForLngLatZoom:()=>620},requestRenderFrame:()=>0,cancelRenderFrame:()=>{}});
  map.transform.resize(width,height);map.transform.setMaxBounds(new LngLatBounds(globe.REGIONAL_NAVIGATION_BOUNDS));
  Object.assign(map,{_camera:map,_update:()=>map,_lazyInitEmptyStyle:()=>{},style:{_checkLoaded:()=>{},stylesheet:{projection:{type:'mercator'}},projection:{name:'mercator'},setProjection:actualStyleProjection},getMaxBounds:()=>map.transform.getMaxBounds(),getMinZoom:()=>map.transform.minZoom,getProjection:()=>map.style.stylesheet.projection,setMaxBounds:actualMapBounds,setMinZoom:actualMapMinZoom,setProjection:actualMapProjection,getCanvas:()=>({clientWidth:width,clientHeight:height,getBoundingClientRect:()=>({right:width,bottom:height})}),getContainer:()=>({querySelector:()=>({getBoundingClientRect:()=>dock})})});
  map.jumpTo({center:[-98.38,38.48],zoom:5.45,pitch:55});
  assert.equal(map._requestedCameraState,undefined,'a completed MapLibre moveend releases its requested transform');
  map.setMinZoom(4);assert.ok(map._requestedCameraState,'terrain retains a requested transform even when this setting does not move the map');
  const ownership=cameraEffects.find(text=>text.includes('getCenterClampedToGround'));
  const cleanup=executeCamera(ownership,{mapRef:{current:map},enabled:true,hidden:false,flat:false,cameraLeaseActive:true,flightView:true,overview:true,camera:'free',frameRequest:1,latestPicked:{current:undefined},ownCameraMove:{current:false},cameraElevation:executeCamera(elevationInitializer,{}),flightPadding:executeCamera(paddingInitializer,{}),leaseProjectionNavigation:globe.leaseProjectionNavigation})();assert.equal(map.getMaxBounds(),null,'acquired camera has no regional maxBounds');fit(map,routePoints,false);assert.equal(map.getMaxBounds(),null,'fitting does not restore regional maxBounds');
  const check=()=>{const padding=map.getPadding();for(const point of routePoints)for(const elevationMeters of [0,Math.max(0,point.altGeomFt??point.altBaroFt??0)*.3048]){const p=map.transform.coordinatePoint(MercatorCoordinate.fromLngLat([point.lon,point.lat]),elevationMeters);assert.ok(p.x>=padding.left&&p.x<=width-padding.right,`${width}px: projected route x=${p.x} outside unobstructed rectangle`);assert.ok(p.y>=padding.top&&p.y<=height-padding.bottom,`${width}px: projected route y=${p.y} outside unobstructed rectangle`);}};
  check();const before=map.getCenter();globe.applyProjectionNavigationLimits(map,'mercator');map.setProjection({type:'mercator'});check();assert.deepEqual(map.getCenter(),before);
  fit(map,routePoints,false);check();cleanup();assert.deepEqual(map.getMaxBounds().toArray(),globe.REGIONAL_NAVIGATION_BOUNDS);assert.equal(map.getMinZoom(),4);
  map.setPadding({top:10,bottom:10,left:10,right:10});map.setProjection({type:'mercator'});assert.deepEqual(map.getMaxBounds().toArray(),globe.REGIONAL_NAVIGATION_BOUNDS,'cleanup stays restored through later terrain camera updates');assert.equal(map.getMinZoom(),4);
 }
});
test('whole-path camera uses MapLibre fitting geometry once and clears measured desktop/mobile controls',()=>{
 const fit=executeCamera(journeyFit,{flightPadding:executeCamera(paddingInitializer,{})});
 const route=[{lon:-95,lat:36.6,altGeomFt:20000},{lon:-93.8,lat:39.4,altGeomFt:30000}];
 for(const [width,height,dock]of [[390,700,{left:12,top:370}],[1280,610,{left:917,top:90}]]){
  let padding={top:0,bottom:0,left:0,right:0},result;const map={getCanvas:()=>({clientWidth:width,clientHeight:height,getBoundingClientRect:()=>({right:width,bottom:height})}),getContainer:()=>({querySelector:()=>({getBoundingClientRect:()=>dock})}),setPadding:value=>{padding=value;},setCenterElevation:()=>{},fitBounds:(bounds,options)=>{result=cameraForBounds({...options,offset:[0,0]},typeof options.padding==='number'?{top:options.padding,bottom:options.padding,left:options.padding,right:options.padding}:options.padding,new LngLatBounds(bounds),0,{padding,width,height,worldSize:512*64,scale:64});}};
  fit(map,route,false);assert.ok(result,`${width}px: a valid camera must be calculated, never a padding-induced no-op`);
  const scale=512*2**result.zoom,center=MercatorCoordinate.fromLngLat(result.center),cx=(width+padding.left-padding.right)/2,cy=(height+padding.top-padding.bottom)/2;
  for(const point of route){const p=MercatorCoordinate.fromLngLat([point.lon,point.lat]),x=(p.x-center.x)*scale+cx,y=(p.y-center.y)*scale+cy;assert.ok(x>=padding.left&&x<=width-padding.right,`${width}px: route x=${x} outside usable width`);assert.ok(y>=padding.top&&y<=height-padding.bottom,`${width}px: route y=${y} outside usable height`);}
  if(width>760)assert.ok(width-padding.right<dock.left,'desktop dock and margin are outside route rectangle');else assert.ok(height-padding.bottom<dock.top,'mobile dock and margin are outside route rectangle');
 }
});
test('whole-path fitting waits for layout, refits on resize, and cancels after close or hide',()=>{
 const effect=cameraEffects.find(text=>text.includes('fitSkyJourney(map,selectedPoints,flat)'));assert.ok(effect);
 const events=new Map(),pending=new Map(),calls=[];let serial=0,disconnected=false;
 const map={on:(name,callback)=>events.set(name,callback),off:name=>events.delete(name),getContainer:()=>({querySelector:()=>({})})},ownCameraMove={current:false};
 const scope={mapRef:{current:map},enabled:true,hidden:false,flightView:true,overview:true,selectedPoints:[aircraft],flat:false,ownCameraMove,fitSkyJourney:()=>{assert.equal(ownCameraMove.current,true);calls.push('fit');},requestAnimationFrame:callback=>{pending.set(++serial,callback);return serial;},cancelAnimationFrame:id=>pending.delete(id),ResizeObserver:class{observe(){}disconnect(){disconnected=true;}}};
 const cleanup=executeCamera(effect,scope)();assert.deepEqual(calls,[],'fitting happens after the dock can be measured');
 events.get('resize')();assert.equal(pending.size,1,'resize replaces pending fit instead of accumulating work');
 const first=pending.entries().next().value;pending.delete(first[0]);first[1]();assert.deepEqual(calls,['fit']);assert.equal(ownCameraMove.current,false);
 events.get('resize')();const late=pending.values().next().value;cleanup();late();assert.equal(calls.length,1);assert.equal(pending.size,0);assert.equal(events.size,0);assert.equal(disconnected,true);
 for(const block of [{hidden:true},{enabled:false},{flightView:false},{overview:false}])assert.equal(executeCamera(effect,{...scope,...block})(),undefined);
});
test('Follow targets the aircraft display height instead of the ground beneath it',()=>{
 const moves=[];const plane={...aircraft,altGeomFt:31000};
 const map={jumpTo:options=>moves.push(options),getZoom:()=>9.7,getBearing:()=>0,queryTerrainElevation:()=>700,getCanvas:()=>({clientWidth:375,clientHeight:700})};
 const height=elevationInitializer?executeCamera(elevationInitializer,{}):()=>undefined;
 const follow=cameraEffects.find(text=>text.includes('camera!=="follow"'));
 assert.ok(follow);
 executeCamera(follow,{mapRef:{current:map},picked:plane,camera:'follow',mode:'recorded',playing:false,reduced:false,flat:false,hidden:false,enabled:true,ownCameraMove:{current:false},cameraElevation:height,flightPadding:executeCamera(paddingInitializer,{})})();
 assert.equal(moves.length,1);assert.equal(moves[0].elevation,31000*.3048);
 assert.deepEqual(moves[0].center,[plane.lon,plane.lat]);
});
test('3D flight view acquires and restores camera elevation and ground clamping',()=>{
 const ownership=cameraEffects.find(text=>text.includes('getCenterClampedToGround'));
 assert.ok(ownership,'the flight view must release shared map camera ownership');
 let clamped=true,elevation=620,padding={top:1,bottom:2,left:3,right:4},bounds=globe.REGIONAL_NAVIGATION_BOUNDS,minZoom=4;const moves=[],resize=new Map();
 const map={getProjection:()=>({type:'mercator'}),getMaxBounds:()=>bounds,setMaxBounds:value=>{bounds=value;},getMinZoom:()=>minZoom,setMinZoom:value=>{minZoom=value;},getPadding:()=>padding,setPadding:value=>{padding=value;},getCanvas:()=>({clientWidth:375,clientHeight:700}),on:(name,fn)=>resize.set(name,fn),off:name=>resize.delete(name),getCenterClampedToGround:()=>clamped,getCenterElevation:()=>elevation,setCenterClampedToGround:v=>{clamped=v;},setCenterElevation:v=>{elevation=v;},jumpTo:v=>{moves.push(v);if(v.elevation!==undefined)elevation=v.elevation;if(v.padding)padding=v.padding;},getBearing:()=>0,queryTerrainElevation:()=>620};
 const height=executeCamera(elevationInitializer,{}),ownCameraMove={current:false};
 const cleanup=executeCamera(ownership,{mapRef:{current:map},enabled:true,hidden:false,flat:false,cameraLeaseActive:true,flightView:true,overview:false,camera:'follow',frameRequest:1,latestPicked:{current:{...aircraft,altGeomFt:31000}},ownCameraMove,cameraElevation:height,flightPadding:executeCamera(paddingInitializer,{}),leaseProjectionNavigation:globe.leaseProjectionNavigation})();
 assert.equal(clamped,false);assert.equal(elevation,620,'the lease does not itself move the camera');
 const frame=cameraEffects.find(text=>text.includes('framedRequest.current'));assert.ok(frame);
 executeCamera(frame,{mapRef:{current:map},enabled:true,hidden:false,flat:false,flightView:true,overview:false,frameRequest:1,framedRequest:{current:-1},latestPicked:{current:{...aircraft,altGeomFt:31000}},ownCameraMove,cameraElevation:height,flightPadding:executeCamera(paddingInitializer,{}),reduced:true})();
 assert.equal(elevation,31000*.3048,'explicit static framing works with reduced motion');assert.equal(moves.at(-1).zoom,9.7);
 assert.equal(bounds,null);assert.equal(minZoom,0);assert.ok(padding.bottom>300);assert.ok(resize.has("resize"));cleanup();assert.deepEqual(padding,{top:1,bottom:2,left:3,right:4});assert.equal(resize.size,0);assert.equal(clamped,true);assert.equal(elevation,620);assert.equal(ownCameraMove.current,false);assert.deepEqual(bounds,globe.REGIONAL_NAVIGATION_BOUNDS);assert.equal(minZoom,4);
 for(const block of [{enabled:false},{hidden:true},{flat:true},{flightView:false,camera:'free',cameraLeaseActive:false}]){
  const count=moves.length;const result=executeCamera(ownership,{mapRef:{current:map},enabled:true,hidden:false,flat:false,cameraLeaseActive:true,flightView:true,overview:false,camera:'follow',frameRequest:1,latestPicked:{current:aircraft},ownCameraMove,cameraElevation:height,flightPadding:executeCamera(paddingInitializer,{}),...block})();
  assert.equal(result,undefined);assert.equal(moves.length,count);
 }
});
test('manual camera release attaches when a map ref becomes ready after the Sky control mounted',()=>{
 let releaseCall;
 const find=node=>{if(ts.isCallExpression(node)&&node.expression.getText(cameraAst)==='useEffect'&&node.arguments[0]?.getText(cameraAst).includes('addEventListener("pointerdown",release)'))releaseCall=node.getText(cameraAst);ts.forEachChild(node,find);};find(cameraAst);assert.ok(releaseCall);
 const listeners=new Map(),canvasListeners=new Map(),changes=[],mapRef={current:null};
 const canvas={addEventListener:(name,fn)=>canvasListeners.set(name,fn),removeEventListener:name=>canvasListeners.delete(name)};
 const map={on:(name,fn)=>listeners.set(name,fn),off:name=>listeners.delete(name),getCanvas:()=>canvas};
 let previous,cleanup;
 const useEffect=(effect,deps)=>{if(!previous||deps.some((value,index)=>!Object.is(value,previous[index]))){cleanup?.();cleanup=effect();previous=deps;}};
 const render=styleReady=>executeCamera(`()=>{${releaseCall};}`,{useEffect,mapRef,enabled:true,styleReady,ownCameraMove:{current:false},setCamera:value=>changes.push(['camera',value]),setFlightView:()=>assert.fail('manual exploration keeps the flight controls open'),setOverview:value=>changes.push(['overview',value])})();
 render(false);assert.equal(canvasListeners.size,0,'the parent has not constructed the map yet');
 mapRef.current=map;render(true);
 assert.equal(typeof canvasListeners.get('pointerdown'),'function','readiness must attach manual-release input to the newly created map');
 canvasListeners.get('pointerdown')();assert.deepEqual(changes,[['camera','free'],['overview',false]]);
 assert.equal(typeof listeners.get('movestart'),'function','navigation controls must release the same camera');
 cleanup();assert.equal(canvasListeners.size,0);assert.equal(listeners.size,0);
});

test('closing Layers preserves the camera while navigation and canvas input release it',async()=>{
 const releaseEffect=cameraEffects.find(text=>text.includes('addEventListener("pointerdown",release)'));
 assert.ok(releaseEffect);
 const listeners=new Map(),canvasListeners=new Map(),changes=[];
 const canvas={addEventListener:(name,fn)=>canvasListeners.set(name,fn),removeEventListener:name=>canvasListeners.delete(name)};
 const map={on:(name,fn)=>listeners.set(name,fn),off:name=>listeners.delete(name),getCanvas:()=>canvas};
 const ownCameraMove={current:false};
 const cleanup=executeCamera(releaseEffect,{mapRef:{current:map},enabled:true,ownCameraMove,setCamera:value=>changes.push(['camera',value]),setFlightView:()=>assert.fail('manual exploration keeps the flight controls open'),setOverview:value=>changes.push(['overview',value])})();
 listeners.get('movestart')();listeners.get('resize')?.();await Promise.resolve();
 assert.deepEqual(changes,[],'panel resize must not release the flight view');
 ownCameraMove.current=true;listeners.get('movestart')();ownCameraMove.current=false;await Promise.resolve();
 assert.deepEqual(changes,[],'follow and orbit retain camera ownership');
 listeners.get('movestart')();await Promise.resolve();
 assert.ok(changes.some(([key,value])=>key==='camera'&&value==='free'),'external navigation releases the camera');
 changes.length=0;canvasListeners.get('pointerdown')();
 assert.ok(changes.some(([key,value])=>key==='camera'&&value==='free'),'manual map input releases immediately');
 changes.length=0;listeners.get('movestart')();cleanup();await Promise.resolve();
 assert.deepEqual(changes,[],'unmounted callbacks cannot mutate state');
 assert.equal(listeners.size,0);assert.equal(canvasListeners.size,0);
});

test('selected aircraft has bounded raised geometry while ordinary and 2D symbols remain compact',()=>{
 const f=fixture();const renderer=attachKansasSky(f.map,()=>{},message=>assert.fail(message));
 renderer.update([aircraft],[],null);f.draw();
 const ordinary=f.vertices();assert.equal(ordinary.length,12*6);
 renderer.update([aircraft],[],aircraft.hex);f.draw();
 const selected=f.vertices();assert.ok(selected.length>ordinary.length&&selected.length<=60*6);
 const heights=Array.from(selected).filter((_value,i)=>i%6===2);
 assert.ok(Math.max(...heights)>aircraft.altGeomFt*.3048,'selected fuselage and tail rise above the reference height');
 assert.ok(Math.min(...heights)<aircraft.altGeomFt*.3048,'selected fuselage has volume below its reference height');
 assert.ok(Array.from(selected).every(Number.isFinite));
 renderer.update([aircraft],[],aircraft.hex,true);f.draw();
 assert.equal(f.vertices().length,13*6,'12 silhouette vertices and one focal marker remain bounded');assert.ok(Array.from(f.vertices()).filter((_v,i)=>i%6===2).every(v=>v===0));
 renderer.dispose();
});

test('terrain guide stems use bounded cached DEM heights and plane-only frames do not upload trails',()=>{
 const f=fixture();let queries=0;f.map.queryTerrainElevation=()=>{queries++;return 333;};
 const renderer=attachKansasSky(f.map,()=>{},message=>assert.fail(message));
 const points=Array.from({length:2000},(_,i)=>({...aircraft,lon:-98+i*.0001,lat:38,observedAt:1000000+i*1000,providerId:'adsb-lol'}));
 const trails=[{hex:aircraft.hex,points}];renderer.update([aircraft],trails,aircraft.hex);f.draw();
 assert.ok(renderer.metrics().heightGuides>1);assert.ok(renderer.metrics().heightGuides<=96);assert.ok(queries<=96);
 const trailUpload=f.uploads.find(upload=>upload.offset>0);assert.ok(trailUpload);
 assert.ok(Array.from(trailUpload.data).some((value,index)=>index%6===2&&value===333),'stems end at actual queried terrain height');
 const before=queries,trailUploads=f.uploads.filter(upload=>upload.offset>0).length;
 renderer.updateAircraft([{...aircraft,lon:-97.9}]);f.draw();
 assert.equal(queries,before);assert.equal(f.uploads.filter(upload=>upload.offset>0).length,trailUploads,'smooth plane redraw reuses cached path GPU geometry');
 renderer.update([aircraft],trails,aircraft.hex,false,true,false);f.draw();assert.equal(renderer.metrics().heightGuides,0);
 renderer.dispose();
 const absent=fixture();absent.map.queryTerrainElevation=()=>null;const missing=attachKansasSky(absent.map,()=>{},message=>assert.fail(message));missing.update([aircraft],trails,aircraft.hex);absent.draw();assert.equal(missing.metrics().heightGuides,0,'missing DEM is not silently replaced with sea level');missing.dispose();
});

test('explicit flight focus restores owned context opacity without altering restrictions or another layer owner',()=>{
 const airport={id:'kfm-aviation-airports-dot',type:'circle'},restriction={id:'kfm-aviation-tfr-edge',type:'line'},water={id:'water-fill',type:'fill'};
 const layers=[airport,restriction,water],paint=new Map([['kfm-aviation-airports-dot:circle-opacity',.8],['kfm-aviation-tfr-edge:line-opacity',1],['water-fill:fill-opacity',.9]]),listeners=new Map();
 const map={getStyle:()=>({layers}),getLayer:id=>layers.find(l=>l.id===id),getPaintProperty:(id,key)=>paint.get(`${id}:${key}`),setPaintProperty:(id,key,value)=>paint.set(`${id}:${key}`,value),on:(name,fn)=>listeners.set(name,fn),off:name=>listeners.delete(name)};
 const restore=attachKansasSkyFocus(map);assert.equal(paint.get('kfm-aviation-airports-dot:circle-opacity'),.8*.12);assert.equal(paint.get('kfm-aviation-tfr-edge:line-opacity'),1);assert.equal(paint.get('water-fill:fill-opacity'),.9);
 paint.set('kfm-aviation-airports-dot:circle-opacity',.6);listeners.get('styledata')();assert.equal(paint.get('kfm-aviation-airports-dot:circle-opacity'),.6*.12);
 restore();assert.equal(paint.get('kfm-aviation-airports-dot:circle-opacity'),.6,'restores the latest owning layer setting');assert.equal(paint.get('kfm-aviation-airports-dot:circle-stroke-opacity'),undefined);assert.equal(listeners.size,0);
});

test('camera layout is measured once across 600 follow frames and refreshed for changed dock geometry',()=>{
 const padding=executeCamera(paddingInitializer,{});let reads=0,left=920;
 const map={getCanvas:()=>({clientWidth:1280,clientHeight:800,getBoundingClientRect:()=>{reads++;return{right:1280,bottom:800};}}),getContainer:()=>({querySelector:()=>({getBoundingClientRect:()=>{reads++;return{left,top:90};}})})};
 const initial=padding(map,true);assert.equal(reads,2);
 for(let frame=0;frame<600;frame++)assert.deepEqual(padding(map),initial);
 assert.equal(reads,2,'animation-frame reads must not force another canvas or dock measurement');
 left=850;const refreshed=padding(map,true);assert.equal(reads,4);assert.ok(refreshed.right>initial.right,'content and resize invalidation changes the reserved area');
});

test('manual camera-mode changes retain one navigation lease until the flight view closes',()=>{
 let call;const visit=node=>{if(ts.isCallExpression(node)&&node.expression.getText(cameraAst)==='useEffect'&&node.arguments[0]?.getText(cameraAst).includes('getCenterClampedToGround'))call=node.getText(cameraAst);ts.forEachChild(node,visit);};visit(cameraAst);assert.ok(call);
 let acquired=0,released=0,previous,cleanup;
 const map={getCenterClampedToGround:()=>true,getCenterElevation:()=>300,getPadding:()=>({top:0,bottom:0,left:0,right:0}),setCenterClampedToGround(){},setCenterElevation(){},setPadding(){},on(){},off(){},jumpTo:options=>{assert.equal(options.center,undefined,'a lease transition cannot recenter manual exploration');assert.equal(options.zoom,undefined,'a lease transition cannot rezoom manual exploration');assert.equal(options.elevation,300);},getCanvas:()=>({clientWidth:1280,clientHeight:800})};
 const useEffect=(effect,deps)=>{if(!previous||deps.some((value,index)=>!Object.is(value,previous[index]))){cleanup?.();cleanup=effect();previous=deps;}};
 const mapRef={current:map},ownCameraMove={current:false};
 const render=(camera,overview,flightView=true)=>executeCamera(`()=>{${call};}`,{useEffect,mapRef,ownCameraMove,enabled:true,hidden:false,flat:false,camera,overview,flightView,frameRequest:1,cameraLeaseActive:flightView||camera!=='free',latestPicked:{current:undefined},flightPadding:()=>({top:0,bottom:0,left:0,right:0}),leaseProjectionNavigation:()=>{acquired++;return()=>released++;}})();
 render('follow',false);render('free',false);render('free',true);render('orbit',false);
 assert.equal(acquired,1);assert.equal(released,0,'manual exploration cannot transiently restore regional constraints');
 render('free',false,false);assert.equal(released,1,'explicit close releases exactly once');cleanup?.();assert.equal(released,1);
});

test('explicit static framing supports reduced motion and cannot repeat after manual exploration',()=>{
 const effect=cameraEffects.find(text=>text.includes('framedRequest.current'));assert.ok(effect);
 const moves=[],map={jumpTo:value=>moves.push(value),getBearing:()=>28,queryTerrainElevation:()=>0,getCanvas:()=>({clientWidth:1280,clientHeight:800})};
 const scope={mapRef:{current:map},enabled:true,hidden:false,flat:false,flightView:true,overview:false,frameRequest:4,framedRequest:{current:-1},latestPicked:{current:aircraft},ownCameraMove:{current:false},reduced:true,camera:'free',cameraElevation:executeCamera(elevationInitializer,{}),flightPadding:()=>({top:0,bottom:0,left:0,right:0})};
 executeCamera(effect,scope)();assert.equal(moves.length,1);assert.equal(moves[0].bearing,28,'entry does not abruptly spin to the reported heading');
 executeCamera(effect,scope)();assert.equal(moves.length,1,'the same request is already consumed');
 executeCamera(effect,{...scope,overview:true})();assert.equal(moves.length,1);
});

test('flight focus recolors only map context and restores exact original chart and raster paint',()=>{
 const layers=[{id:'kfm-background',type:'background'},{id:'chart-elevation-tint',type:'color-relief'},{id:'chart-place-labels',type:'symbol'},{id:'chart-urban',type:'fill'},{id:'esri-imagery-raster',type:'raster'},{id:'kfm-aviation-tfr-edge',type:'line'}];
 const relief=['interpolate',['linear'],['elevation'],0,'#eeeeaa',2000,'#ffffff'];
 const paint=new Map([['chart-urban:fill-outline-color','#c9a92c'],['kfm-background:background-color','#efdda4'],['chart-elevation-tint:color-relief-color',relief],['esri-imagery-raster:raster-brightness-max',.9],['kfm-aviation-tfr-edge:line-opacity',1]]),listeners=new Map();
 const before=new Map(paint),map={getStyle:()=>({name:'KFM Aviation Chart',layers}),getLayer:id=>layers.find(layer=>layer.id===id),getPaintProperty:(id,key)=>paint.get(`${id}:${key}`),setPaintProperty:(id,key,value)=>{if(value===undefined)paint.delete(`${id}:${key}`);else paint.set(`${id}:${key}`,value);},on:(name,fn)=>listeners.set(name,fn),off:name=>listeners.delete(name)};
 const cleanup=attachKansasSkyFocus(map);assert.notEqual(paint.get('chart-urban:fill-outline-color'),'#c9a92c');assert.notDeepEqual(paint.get('chart-elevation-tint:color-relief-color'),relief);assert.ok(paint.get('esri-imagery-raster:raster-brightness-max')<.9);assert.equal(paint.get('kfm-aviation-tfr-edge:line-opacity'),1);
 cleanup();assert.deepEqual(paint,before,'paint values and absent defaults return exactly to their owner');
});


test('selected paths retain a bounded basic-line fallback if only the feathered shader fails',()=>{
 const points=[{...aircraft,observedAt:1000000,providerId:'adsb-lol'},{...aircraft,lon:-89.99,observedAt:1020000,providerId:'adsb-lol'}];
 for(const failStroke of [false,true]){
  const f=fixture(true,{failStroke}),reports=[];
  const renderer=attachKansasSky(f.map,()=>{},message=>reports.push(message));
  renderer.update([aircraft],[{hex:aircraft.hex,points}],aircraft.hex,false,true,false);f.draw();
  const lineVertices=f.draws.filter(([mode])=>mode===1).reduce((count,[,,vertices])=>count+vertices,0);
  assert.equal(lineVertices,failStroke?2:0,'fallback shows the same observed edge only when the optional shader is unavailable');
  assert.ok(f.draws.some(([mode,,vertices])=>mode===4&&vertices===24),'selected aircraft remains drawn');
  assert.equal(reports.length,failStroke?1:0,'graphics fallback remains visible as a diagnostic');
  assert.deepEqual(f.blends.at(-1),[770,771,1,771],'straight RGB alpha blending preserves opaque destination alpha');
  f.draw();assert.equal(reports.length,failStroke?1:0,'the failed optional shader is not retried each frame');
  renderer.dispose();
 }
});

test('explicit gap navigation offers only the next retained observation inside a genuine missing span',()=>{
 const point=(time,extra={})=>({...aircraft,observedAt:time,providerId:'adsb-lol',positionMethod:'adsb_icao',...extra});
 const points=[point(1000000),point(1020000),point(1400000,{breakBefore:true}),point(1420000)];
 const next=skyHelpers.nextSkyObservationAfterGap;
 assert.equal(next(points,1100000),1400000);
 for(const at of [999999,1000000,1010000,1020000,1400000,1410000,1420000,1500000,NaN])assert.equal(next(points,at),null,'no invented jump at an exact, interpolable or out-of-range instant');
 assert.equal(next([point(1000000),point(1020000,{breakBefore:true})],1010000),1020000,'explicit short source discontinuities also remain navigable');
 assert.equal(next([],1100000),null);
});


test('terrain tile completion refreshes stationary markers and guides without invalidating unrelated sources',()=>{
 let stamp=1000,height=0,queries=0,repaints=0,terrain={source:'terrain-dem',exaggeration:1};
 const isolated={};
 new Function('exports','require','document','performance',code)(isolated,name=>{
  if(name==='./kansas-sky')return skyHelpers;
  if(name==='./aviation-traffic')return {TRAFFIC_ALTITUDE_COLORS:[[0,'#7d8a96']]};
  throw Error(`Unexpected renderer dependency ${name}`);
 },{hidden:false},{now:()=>stamp});
 const f=fixture(),ground={...aircraft,hex:'def456',onGround:true,altGeomFt:null,altBaroFt:null};
 f.map.getTerrain=()=>terrain;f.map.queryTerrainElevation=()=>{queries++;return height;};f.map.triggerRepaint=()=>repaints++;
 const renderer=isolated.attachKansasSky(f.map,()=>{},message=>assert.fail(message));
 const points=[{...aircraft,observedAt:1000000,providerId:'adsb-lol'},{...aircraft,lon:-89.99,observedAt:1020000,providerId:'adsb-lol'}];
 renderer.update([ground,aircraft],[{hex:aircraft.hex,points}],aircraft.hex,false,true,true);f.draw();
 const snapshot=()=>({ground:f.uploads.findLast(u=>u.buffer===1&&u.offset===0).data[2],guide:f.uploads.findLast(u=>u.buffer===1&&u.offset>0).data.at(-4),queries,uploads:f.uploads.length,repaints});
 const first=snapshot();height=333;f.emit('sourcedata',{sourceId:'radar',tile:{state:'loaded'}});f.draw();
 assert.deepEqual(snapshot(),first,'unrelated source events do not query, upload or request repaint');
 f.emit('sourcedata',{sourceId:'terrain-dem',tile:{state:'loaded'},isSourceLoaded:false});
 f.emit('sourcedata',{sourceId:'terrain-dem',tile:{state:'loaded'},isSourceLoaded:true});f.draw();
 const loaded=snapshot();assert.equal(loaded.ground,333,'ordinary tile completion refreshes a stationary ground aircraft');assert.equal(loaded.guide,333,'finite guide bases refresh as terrain becomes available');
 assert.equal(loaded.queries-first.queries,3,'two completions before one draw query only one marker and two retained guide locations');
 renderer.updateAircraft([ground,aircraft]);f.draw();assert.equal(queries,loaded.queries,'ordinary aircraft frames reuse current terrain caches');
 stamp=7000;f.draw();assert.equal(queries,loaded.queries,'missing-value retry leaves finite cached heights intact');
 height=666;terrain={source:'terrain-dem',exaggeration:2};f.emit('terrain',{terrain});f.draw();
 assert.equal(snapshot().ground,666);assert.equal(snapshot().guide,666,'terrain option changes refresh both geometry caches');
 terrain=null;height=null;f.emit('terrain',{terrain});f.draw();assert.equal(renderer.metrics().heightGuides,0);assert.equal(snapshot().ground,0,'terrain off removes stale elevated ground locations');
 renderer.dispose();const disposedRepaints=repaints;f.emit('sourcedata',{sourceId:'terrain-dem'});f.emit('terrain',{terrain:null});assert.equal(repaints,disposedRepaints);
 assert.equal(f.listenerCount('sourcedata'),0);assert.equal(f.listenerCount('terrain'),0);
});

test('slower React readout cannot rewind a newer shared-clock aircraft frame',()=>{
 let render;const visit=node=>{if(ts.isCallExpression(node)&&node.expression.getText(cameraAst)==='animateSkyReplay')render=node.arguments[0].properties.find(p=>p.name?.getText(cameraAst)==='render').initializer.getText(cameraAst);ts.forEachChild(node,visit);};visit(cameraAst);
 const effect=cameraEffects.find(text=>text.includes('layer.current?.update('));assert.ok(render&&effect);
 const points=[{...aircraft,lon:-98,lat:38,observedAt:1000000,providerId:'adsb-lol'},{...aircraft,lon:-97.98,lat:38,observedAt:1020000,providerId:'adsb-lol'}],tracks=new Map([[aircraft.hex,points]]),writes=[];
 const layer={current:{projection:()=>0,updateAircraft:a=>writes.push(a[0].lon),update:a=>writes.push(a[0].lon)}},motionCursor={current:0};
 executeCamera(render,{motionCursor,motionState:{current:{tracks,enabled:true,hidden:false,selected:aircraft.hex}},samplesAt:skyHelpers.samplesAt,layer,latestPicked:{current:null},document:{hidden:false},performance:{now:()=>1000},previous:950,mapRef:{current:null}})(1010000);
 executeCamera(effect,{layer,aircraft:skyHelpers.samplesAt(tracks,1008000),trails:[],selected:aircraft.hex,flat:false,showPaths:true,showGuides:true,playing:true,replaying:true,mode:'recorded',reduced:false,motionCursor,tracks,samplesAt:skyHelpers.samplesAt})();
 assert.equal(writes[1],writes[0],'the lower-frequency readout uses the latest motion cursor, not its stale position snapshot');
});


test('flight focus terrain leases keep one display scale and restore the latest requested terrain',()=>{
 let terrain={source:'dem-a',exaggeration:2.5};const listeners=new Map(),writes=[];
 const emit=name=>{for(const listener of [...(listeners.get(name)??[])])listener();};
 const map={getTerrain:()=>terrain,setTerrain:value=>{terrain=value;writes.push(value);emit('terrain');},on:(name,fn)=>{if(!listeners.has(name))listeners.set(name,new Set());listeners.get(name).add(fn);},off:(name,fn)=>listeners.get(name)?.delete(fn)};
 const first=exports.leaseKansasSkyTerrain(map),second=exports.leaseKansasSkyTerrain(map);
 assert.equal(terrain.exaggeration,1);emit('style.load');first();first();assert.equal(terrain.exaggeration,1,'other focus owner remains active');
 second();assert.equal(terrain.exaggeration,2.5,'a style event does not overwrite the original requested scale');
 const third=exports.leaseKansasSkyTerrain(map);map.setTerrain({source:'dem-b',exaggeration:3});assert.equal(terrain.exaggeration,1);third();assert.deepEqual(terrain,{source:'dem-b',exaggeration:3},'latest provider and scale are restored');
 const fourth=exports.leaseKansasSkyTerrain(map);map.setTerrain({source:'dem-b',exaggeration:1});fourth();assert.equal(terrain.exaggeration,1,'a new explicit1× preference is preserved');
 const fifth=exports.leaseKansasSkyTerrain(map);map.setTerrain(null);fifth();assert.equal(terrain,null,'focus cleanup never reactivates disabled terrain');
 assert.equal(listeners.get('terrain').size,0);assert.equal(listeners.get('style.load').size,0);
});

test('flight framing reserves measured phone overlays and dock with a usable focal viewport',()=>{
 const padding=executeCamera(paddingInitializer,{});
 for(const [width,height,canvasTop,dockTop,badgeBottom]of [[375,730,54,319.65625,165.34375],[390,762,54,351,165.34375],[375,730,54,292.36,165.34375]]){
  const badge={getBoundingClientRect:()=>({top:120,bottom:badgeBottom,left:94,right:281,width:187,height:45})};
  const map={getCanvas:()=>({clientWidth:width,clientHeight:height,getBoundingClientRect:()=>({top:canvasTop,bottom:canvasTop+height,right:width})}),getContainer:()=>({querySelector:()=>({getBoundingClientRect:()=>({left:10,top:dockTop})}),querySelectorAll:()=>[badge]})};
  const p=padding(map,true),top=canvasTop+p.top,bottom=canvasTop+height-p.bottom,center=(top+bottom)/2;
  assert.ok(top>=badgeBottom+16,`${width}px: usable map begins below the replay badge, actual ${top}, badge bottom ${badgeBottom}`);
  assert.ok(center-30>badgeBottom&&center+30<dockTop,`${width}px: aircraft/halo has a 60px clear focal region`);
  assert.ok(bottom-top>=79.99,'expanded disclosures retain a bounded, nonnegative focal viewport');
 }
});

test('paused flight framing refreshes owned padding when status or dock layout changes',()=>{
 const effect=cameraEffects.find(text=>text.includes('Layout changes refresh this cache'));assert.ok(effect);
 const observed=[],events=new Map(),moves=[];let resizeCallback,disconnected=false;
 const canvas={},dock={},badge={},ownCameraMove={current:false};
 const map={getCanvas:()=>canvas,getContainer:()=>({querySelector:()=>dock,querySelectorAll:()=>[badge]}),on:(name,fn)=>events.set(name,fn),off:name=>events.delete(name),getCenterElevation:()=>5670,jumpTo:options=>{assert.equal(ownCameraMove.current,true);moves.push(options);}};
 const scope={mapRef:{current:map},enabled:true,cameraLeaseActive:true,ownCameraMove,flightPadding:()=>({top:135,bottom:488,left:35,right:35}),ResizeObserver:class{constructor(fn){resizeCallback=fn;}observe(node){observed.push(node);}disconnect(){disconnected=true;}}};
 const cleanup=executeCamera(effect,scope)();assert.equal(moves.length,1,'paused camera reserves the newly measured layout');assert.equal(moves[0].elevation,5670,'padding updates preserve the aircraft camera target height');
 assert.ok(observed.includes(badge),'status geometry participates in layout invalidation');resizeCallback();assert.equal(moves.length,2);assert.equal(ownCameraMove.current,false);
 cleanup();assert.equal(disconnected,true);assert.equal(events.size,0);
 const before=moves.length,release=executeCamera(effect,{...scope,cameraLeaseActive:false})();resizeCallback();assert.equal(moves.length,before,'outside the camera lease, layout measurement cannot move the map');release();
});
