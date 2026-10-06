import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import * as Three from 'three';
const compile = source => ts.transpileModule(source, {compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022,esModuleInterop:true}}).outputText;
const moduleUrl = source => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;
const modelUrl = moduleUrl(compile(await readFile('app/aquifer-volume.ts','utf8')).replace('from "polygon-clipping"', `from ${JSON.stringify(new URL('../node_modules/polygon-clipping/dist/polygon-clipping.esm.js',import.meta.url).href)}`));
const m = await import(modelUrl);
const session = await import(moduleUrl(compile(await readFile('app/aquifer-view-session.ts','utf8')).replace('from "./aquifer-volume"', `from ${JSON.stringify(modelUrl)}`)));
const meshes = await import(moduleUrl(compile(await readFile('app/aquifer-volume-mesh.ts','utf8')).replace('from "./aquifer-volume"', `from ${JSON.stringify(modelUrl)}`)));
const bounds = [-100.8,38.3,-100.2,38.7];
function harness({ready=false,failCapture=false,extent=bounds}={}) {
  const listeners=new Map(),tasks=new Map(),requests=[],snapshots=[],statuses=[],surfaceStatuses=[];let timerId=0,captures=0;
  const map={ready,extent,moving:false,projection:'mercator', getPitch:()=>0,getBearing:()=>0,getProjection(){return {type:this.projection}},
    getBounds(){return {getWest:()=>this.extent[0],getSouth:()=>this.extent[1],getEast:()=>this.extent[2],getNorth:()=>this.extent[3]}},
    isMoving(){return this.moving},areTilesLoaded(){return this.ready},triggerRepaint(){this.emit('render')},
    on(event,fn){if(!listeners.has(event))listeners.set(event,new Set());listeners.get(event).add(fn)},off(event,fn){listeners.get(event)?.delete(fn)},emit(event){for(const fn of [...(listeners.get(event)??[])])fn()}};
  const worker={onmessage:null,onerror:null,postMessage:message=>requests.push(message)};
  const stop=session.startAquiferView({map,worker,onSnapshot:v=>snapshots.push(v),onStatus:v=>statuses.push(v),onSurfaceStatus:v=>surfaceStatuses.push(v),
    sampleSurface:()=>{captures++;if(failCapture)throw new Error('tainted');return 'same-view-image'},
    timers:{set:(cb,delay)=>{const id=++timerId;tasks.set(id,{cb,delay});return id},clear:id=>tasks.delete(id)}});
  const reply=(id=requests.at(-1).id,volume={bounds:map.extent,envelopes:[{id:'verified-shape'}],heldClasses:0,truncated:false,period:'2022–2024'})=>worker.onmessage?.({data:{id,volume}});
  return {map,worker,stop,reply,requests,snapshots,statuses,surfaceStatuses,listeners,tasks,get captures(){return captures},flush(delay){for(const [id,task] of [...tasks])if(task.delay===delay){tasks.delete(id);task.cb()}}};
}
test('aquifer geometry appears while unrelated map tiles remain incomplete, including after timeout',()=>{
  const h=harness();assert.equal(h.requests.length,1,'must request geometry before any surface image');h.reply();
  assert.equal(h.snapshots.at(-1).volume.envelopes.length,1);assert.equal(h.snapshots.at(-1).image,null);
  h.flush(8000);assert.equal(h.snapshots.at(-1).volume.envelopes.length,1);assert.match(h.surfaceStatuses.at(-1),/incomplete/);assert.equal(h.captures,0);h.stop();
});
test('failed canvas readback cannot suppress geometry',()=>{
  const h=harness({ready:true,failCapture:true});h.reply();assert.equal(h.snapshots.at(-1).volume.envelopes.length,1);assert.equal(h.snapshots.at(-1).image,null);assert.match(h.surfaceStatuses.at(-1),/unavailable/);h.stop();
});
test('late complete image attaches to the same geometry without replacing geometry identity',()=>{
  const h=harness();h.reply();const v=h.snapshots.at(-1).volume;h.map.ready=true;h.map.emit('render');assert.equal(h.snapshots.at(-1).image,'same-view-image');assert.equal(h.snapshots.at(-1).volume,v);h.stop();
});
test('rapid movement invalidates old geometry and imagery; late responses cannot mix extents',()=>{
  const h=harness();const old=h.requests[0].id;h.map.emit('movestart');h.reply(old);assert.equal(h.snapshots.at(-1),null);
  h.map.extent=[-101,38,-100.5,38.5];h.map.emit('moveend');h.map.emit('resize');h.flush(250);assert.equal(h.requests.length,2);
  h.reply(old);assert.equal(h.snapshots.at(-1),null);h.reply();assert.deepEqual(h.snapshots.at(-1).volume.bounds,h.map.extent);h.stop();
});
test('outside-scope view remains an explicit hold; disposal releases every listener and timer',()=>{
  const h=harness({extent:[-102,37,-94,40]});assert.equal(h.requests.length,0);assert.match(h.statuses.at(-1),/Zoom into Kansas/);h.stop();
  assert.equal([...h.listeners.values()].reduce((n,s)=>n+s.size,0),0);assert.equal(h.tasks.size,0);assert.equal(h.worker.onmessage,null);assert.equal(h.worker.onerror,null);
});
test('actual source polygons create finite three-dimensional meshes below their registered surface',async()=>{
  const inputs=await Promise.all(m.AQUIFER_VOLUME_ASSETS.map(async a=>JSON.parse(await readFile(`public${a.url}`,'utf8'))));
  for(const extent of [bounds,[-100.53,38.48,-100.47,38.52]]) {
    const volume=m.buildAquiferVolume(...inputs,extent),shapes=meshes.aquiferGeometries(Three,volume);assert.ok(shapes.length>0);
    for(const {geometry,envelope} of shapes){geometry.computeBoundingBox();const b=geometry.boundingBox,k=m.volumeDepthScale(extent);
      assert.ok(geometry.attributes.position.count>=12);assert.ok([...geometry.attributes.position.array].every(Number.isFinite));
      assert.ok(b.min.x>=-3.00001&&b.max.x<=3.00001);assert.ok(b.max.y<=1e-7);assert.ok(b.max.y>b.min.y);
      assert.ok(Math.abs(b.min.y+envelope.deepMeters*k)<1e-6);assert.ok(Math.abs(b.max.y+envelope.shallowMeters*k)<1e-6);
      geometry.dispose();
    }
  }
});
test('mesh extrusion preserves real holes instead of covering absent source areas',()=>{
  const outer=[[-100.7,38.35],[-100.3,38.35],[-100.3,38.65],[-100.7,38.65],[-100.7,38.35]];
  const hole=[[-100.55,38.45],[-100.55,38.55],[-100.45,38.55],[-100.45,38.45],[-100.55,38.45]];
  const volume={bounds,envelopes:[{id:'hole',geometry:[[outer,hole]],shallowMeters:0,deepMeters:50}],period:'2022–2024',heldClasses:0,truncated:false};
  const [{geometry}]=meshes.aquiferGeometries(Three,volume),mesh=new Three.Mesh(geometry,new Three.MeshBasicMaterial({side:Three.DoubleSide}));mesh.updateMatrixWorld();
  const ray=new Three.Raycaster(new Three.Vector3(0,1,0),new Three.Vector3(0,-1,0));assert.equal(ray.intersectObject(mesh).length,0);
  const p=m.projectVolumePosition(-100.65,38.5,bounds);ray.set(new Three.Vector3(p.x,1,p.z),new Three.Vector3(0,-1,0));assert.ok(ray.intersectObject(mesh).length>0);geometry.dispose();mesh.material.dispose();
});
