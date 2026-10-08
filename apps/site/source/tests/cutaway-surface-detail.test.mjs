import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';
const compile=source=>ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
const code=compile(await readFile('app/cutaway-surface-detail.ts','utf8'));
const bounds=[-100.7,38.3,-100.3,38.7];
function harness(){
 const maps=[],containers=[],timers=new Map(),statuses=[],frames=[];let seq=0;
 const canvas=()=>({width:0,height:0,getContext:()=>({drawImage(){},getImageData(){return{data:[0,0,0,255]}}})});
 const document={body:{append(node){containers.push(node)}},createElement(tag){return tag==='canvas'?canvas():{style:{},setAttribute(){},remove(){this.removed=true}}}};
 class FakeMap{
  constructor(options){this.options=options;this.zoom=options.zoom;this.extent=bounds;this.events={};this.jumps=[];maps.push(this)}
  on(name,fn){this.events[name]=fn}emit(name,event){this.events[name]?.(event)}
  setPaintProperty(){}resize(){}triggerRepaint(){}hasImage(){return false}addImage(){}
  jumpTo(frame){this.zoom=frame.zoom;this.jumps.push(frame)}getZoom(){return this.zoom}areTilesLoaded(){return true}
  getBounds(){return{getWest:()=>this.extent[0],getSouth:()=>this.extent[1],getEast:()=>this.extent[2],getNorth:()=>this.extent[3]}}
  getCanvas(){return{width:parseInt(this.options.container.style.width),height:parseInt(this.options.container.style.height)}}
  remove(){this.removed=true}
 }
 const exports={};vm.runInNewContext(code,{exports,document,require:name=>name==='./maplibre-seam'?{loadMapLibre:async()=>({Map:FakeMap,setWorkerUrl(){}})}:{surfaceRasterSampling:()=>[]},setTimeout:(fn,ms)=>{const id=++seq;timers.set(id,{fn,ms});return id},clearTimeout:id=>timers.delete(id)});
 const capture={bounds,images:[],style:{version:8,sources:{radar:{type:'raster',tiles:['/radar?TIME=2026-10-07T13:02:00Z']},fire:{type:'geojson',data:{type:'FeatureCollection',features:[{properties:{checkedDay:'2026-10-07',acquisitionTime:'2026-10-07T13:02:00Z'}}]}}},layers:[{id:'radar',type:'raster',source:'radar'}]}};
 return{m:exports,maps,containers,timers,statuses,frames,capture,flush(ms){for(const [id,t] of [...timers])if(t.ms===ms){timers.delete(id);t.fn()}},start(pixels=4096){return exports.startCutawaySurfaceDetail({capture,pixels,onFrame:f=>frames.push(f),onStatus:s=>statuses.push(s)})}};
}
test('detail footprint stays inside the accepted slice and geographic scale increases with zoom',()=>{
 const {m}=harness();
 assert.deepEqual(Array.from(m.detailBoundsFromSurface(bounds,[{x:-9,z:-9},{x:9,z:9}])),bounds);
 assert.equal(m.detailBoundsFromSurface(bounds,[]),null);
 assert.equal(m.detailBoundsFromSurface(bounds,[{x:8,z:1},{x:9,z:2}]),null);
 const close=m.detailBoundsFromSurface(bounds,[{x:-.2,z:-.2},{x:.2,z:.2}]);
 assert.ok(close[0]>bounds[0]&&close[2]<bounds[2]&&close[1]>bounds[1]&&close[3]<bounds[3]);
 const wide=m.surfaceRenderFrame(bounds,4096),zoomed=m.surfaceRenderFrame(close,4096);
 assert.equal(Math.max(wide.width,wide.height),4096);assert.ok(zoomed.zoom>wide.zoom+3);
 assert.ok(wide.center[1]>38.5); // Mercator midpoint, not a shifted linear latitude crop.
 assert.equal(m.surfaceRenderFrame([-100,38,-99.999999,38.000001],4096).zoom,22);
});
test('detail requests are bounded, debounced and preserve exact radar/fire source values',async()=>{
 const h=harness(),before=JSON.stringify(h.capture),controller=h.start();await Promise.resolve();const map=h.maps[0];
 assert.equal(map.options.pixelRatio,1);assert.equal(map.options.maxTileCacheSize,96);
 assert.equal(map.options.style.layers[0].paint['raster-resampling'],'nearest');assert.equal(JSON.stringify(h.capture),before);
 map.emit('load');map.emit('idle');assert.equal(h.frames[0].image.height,4096);assert.match(h.statuses.at(-1),/Surface detail ready/);
 const close=[-100.6,38.4,-100.4,38.6];controller.update(close);controller.update(close);assert.equal([...h.timers.values()].filter(t=>t.ms===200).length,1);
 h.flush(200);assert.equal(map.jumps.length,2);controller.update(close);h.flush(200);assert.equal(map.jumps.length,2);
 assert.equal(map.options.style.sources.radar.tiles[0],h.capture.style.sources.radar.tiles[0]);assert.equal(JSON.stringify(map.options.style.sources.fire),JSON.stringify(h.capture.style.sources.fire));
 controller.dispose();assert.equal(h.timers.size,0);assert.ok(map.removed&&h.containers[0].removed);
});
test('preload tile errors stay visible after idle; timeout and late completion cannot imply complete coverage',async()=>{
 const h=harness(),controller=h.start(2048);await Promise.resolve();const map=h.maps[0];
 map.emit('error');map.emit('load');map.emit('idle');assert.match(h.statuses.at(-1),/Partial surface detail/);
 controller.update([-100.6,38.4,-100.4,38.6]);h.flush(200);h.flush(12000);assert.match(h.statuses.at(-1),/Missing tiles are unknown/);
 map.emit('idle');assert.match(h.statuses.at(-1),/Partial surface detail/);
 controller.dispose();const count=h.frames.length;map.emit('idle');assert.equal(h.frames.length,count);
 const late=harness(),stopped=late.start();stopped.dispose();await Promise.resolve();assert.equal(late.maps.length,0);assert.ok(late.containers[0].removed);
});

test('a slow optional overlay cannot hold already rendered basemap detail until global load',async()=>{
 const h=harness(),controller=h.start();await Promise.resolve();const map=h.maps[0];
 map.emit('style.load');map.emit('render');map.emit('render');assert.equal([...h.timers.values()].filter(t=>t.ms===1000).length,1);
 h.flush(1000);assert.equal(h.frames.length,1);assert.match(h.statuses.at(-1),/partial preview/);assert.match(h.statuses.at(-1),/Unfinished tiles are unknown/);
 map.emit('error');map.emit('render');h.flush(1000);assert.equal(h.frames.length,2);
 map.emit('idle');assert.match(h.statuses.at(-1),/Partial surface detail/);
 controller.dispose();assert.equal(h.timers.size,0);
});
