import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';
const compile=source=>ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
const code=compile(await readFile('app/cutaway-surface-detail.ts','utf8'));
const surface={};vm.runInNewContext(compile(await readFile('app/selected-surface.ts','utf8')),{exports:surface});
const bounds=[-100.7,38.3,-100.3,38.7];
function harness(){
 const maps=[],containers=[],timers=new Map(),statuses=[],frames=[];let seq=0;
 const canvas=()=>({width:0,height:0,getContext:()=>({drawImage(){},getImageData(){return{data:[0,0,0,255]}}})});
 const document={body:{append(node){containers.push(node)}},createElement(tag){return tag==='canvas'?canvas():{style:{},setAttribute(){},remove(){this.removed=true}}}};
 class FakeMap{
  constructor(options){this.options=options;this.zoom=options.zoom;this.extent=bounds;this.events={};this.jumps=[];this.styles=[];maps.push(this)}
  on(name,fn){this.events[name]=fn}emit(name,event){this.events[name]?.(event)}
  setStyle(style,options){this.styles.push({style,options})}
  getSource(id){return this.options.style.sources[id]?.type==='geojson'?{type:'geojson',setData:data=>{this.dataUpdates??=[];this.dataUpdates.push({id,data})}}:undefined}
  setPaintProperty(){}resize(){}triggerRepaint(){}hasImage(){return false}addImage(){}
  jumpTo(frame){this.zoom=frame.zoom;this.jumps.push(frame)}getZoom(){return this.zoom}areTilesLoaded(){return true}
  getBounds(){return{getWest:()=>this.extent[0],getSouth:()=>this.extent[1],getEast:()=>this.extent[2],getNorth:()=>this.extent[3]}}
  getCanvas(){return{width:parseInt(this.options.container.style.width),height:parseInt(this.options.container.style.height)}}
  remove(){this.removed=true}
 }
 const exports={};vm.runInNewContext(code,{exports,document,require:name=>name==='./maplibre-seam'?{loadMapLibre:async()=>({Map:FakeMap,setWorkerUrl(){}})}:surface,setTimeout:(fn,ms)=>{const id=++seq;timers.set(id,{fn,ms});return id},clearTimeout:id=>timers.delete(id)});
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
test('same-area manual refresh retains the previous surface until replacement tiles render',async()=>{
 const h=harness(),controller=h.start();await Promise.resolve();const map=h.maps[0];
 assert.equal(controller.refresh(),true,'a click during initial tile preparation is harmless');
 assert.equal(map.styles.length,0,'pending preparation is not restarted');
 map.emit('style.load');map.emit('idle');const first=h.frames[0];
 assert.equal(controller.refresh(),true);assert.equal(h.frames.length,1,'the existing image is not cleared');
 assert.equal(map.styles.length,1,'refresh reloads provider tiles without changing capture identity');
 assert.equal(map.styles[0].options.diff,false);assert.equal(map.styles[0].style.sources.radar.tiles[0],h.capture.style.sources.radar.tiles[0]);
 assert.match(h.statuses.at(-1),/Previous surface remains visible/);
 map.emit('error');assert.match(h.statuses.at(-1),/previous surface remains visible/i);
 map.emit('style.load');assert.equal(h.frames.length,1,'style loading does not replace the old image');
 map.emit('render');assert.equal(h.frames.length,1,'a partial preview cannot replace the complete old image');
 map.emit('idle');assert.equal(h.frames.length,1,'failed new tiles leave the old image in place');
 assert.match(h.statuses.at(-1),/previous complete surface remains visible/i);
 assert.equal(controller.refresh(),true,'a failed refresh can be retried');
 map.emit('style.load');map.emit('render');assert.equal(h.frames.length,1,'the old image remains through the next partial render');
 map.emit('idle');assert.equal(h.frames.length,2);assert.notEqual(h.frames[1],first);
 assert.match(h.statuses.at(-1),/Surface detail ready/);
 controller.dispose();assert.equal(controller.refresh(),false);
});
test('an initial render preview is not promoted to a complete refresh fallback',async()=>{
 const h=harness(),controller=h.start();await Promise.resolve();const map=h.maps[0];
 map.emit('style.load');map.emit('render');assert.equal(h.frames.length,1);
 assert.match(h.statuses.at(-1),/partial preview/);
 assert.equal(controller.refresh(),true);
 assert.doesNotMatch(h.statuses.at(-1),/previous surface remains visible/i);
 assert.match(h.statuses.at(-1),/preview may be incomplete/i);
 map.emit('error');map.emit('style.load');map.emit('render');
 assert.equal(h.frames.length,2,'a second explicitly partial preview may replace the first');
 map.emit('idle');assert.match(h.statuses.at(-1),/Partial surface detail/);
 assert.equal(controller.refresh(),true);
 assert.doesNotMatch(h.statuses.at(-1),/previous surface remains visible/i);
 controller.dispose();
});

test('continuous camera movement cannot postpone the pending detail request and uses the latest footprint',async()=>{
 const h=harness(),controller=h.start();await Promise.resolve();const map=h.maps[0];map.emit('load');map.emit('idle');
 controller.update([-100.6,38.4,-100.4,38.6]);const scheduled=[...h.timers].find(([,t])=>t.ms===200)[0];
 const latest=[-100.51,38.49,-100.49,38.51];controller.update(latest);
 assert.ok(h.timers.has(scheduled),'moving again must not restart the refresh deadline');h.flush(200);
 assert.equal(map.jumps.length,2);assert.deepEqual(Array.from(map.jumps.at(-1).center),Array.from(h.m.surfaceRenderFrame(latest,4096).center));
 controller.update([-100.505,38.495,-100.495,38.505]);h.flush(200);assert.equal(map.jumps.length,3);controller.dispose();
});
test('a rendered image is bound synchronously to its geographic footprint before a later camera change',async()=>{
 const h=harness(),controller=h.start();await Promise.resolve();const map=h.maps[0];map.emit('style.load');map.emit('render');
 assert.equal(h.frames.length,1,'copy happens while the canvas and map transform describe the same frame');
 const original=Array.from(h.frames[0].bounds);map.extent=[-100.51,38.49,-100.49,38.51];h.flush(1000);
 assert.deepEqual(Array.from(h.frames[0].bounds),original);assert.equal(h.frames.length,1,'the throttle timer cannot relabel stale pixels with a newer extent');
 map.emit('render');assert.deepEqual(Array.from(h.frames[1].bounds),map.extent);controller.dispose();
});

test('inline record updates preserve the loaded basemap and complete pixels until exact new data settles',async()=>{
 const h=harness(),controller=h.start(2048);await Promise.resolve();const map=h.maps[0];map.emit('style.load');map.emit('idle');
 const next=structuredClone(h.capture);next.style.sources.fire.data.features[0].properties.acquisitionTime='2026-10-07T13:17:00Z';
 assert.equal(controller.updateCapture(next),true);assert.equal(map.styles.length,1);assert.equal(map.styles[0].options.diff,true,'existing basemap tile cache survives overlay changes');assert.equal(h.maps.length,1);
 assert.deepEqual(JSON.parse(JSON.stringify(map.styles[0].style.sources.fire.data)),next.style.sources.fire.data);assert.equal(h.frames.length,1);
 map.emit('render');assert.equal(h.frames.length,1,'prior complete frame is held during record update');
 map.emit('idle');assert.equal(h.frames.length,2);assert.match(h.statuses.at(-1),/Surface detail ready/);
 assert.equal(controller.updateCapture(next),true);assert.equal(map.styles.length,1,'identical content is not reparsed');
 for(const change of [c=>c.bounds[0]-=.01,c=>c.style.sources.radar.tiles[0]='/new-frame',c=>c.images.push({id:'new'})]){
  const changed=structuredClone(next);change(changed);assert.equal(controller.updateCapture(changed),false,'other content requires a fresh renderer');
 }
 const styled=structuredClone(next);styled.style.layers[0].paint={'raster-opacity':.5};assert.equal(controller.updateCapture(styled),true,'styling changes are applied exactly without losing unchanged tiles');assert.equal(map.styles.at(-1).style.layers[0].paint['raster-opacity'],.5);
 const added=structuredClone(next);added.style.sources.records={type:'geojson',data:{type:'FeatureCollection',features:[]}};added.style.layers.unshift({id:'new-records',type:'circle',source:'records'});
 assert.equal(controller.updateCapture(added),true,'new overlay layers retain unchanged tile sources');assert.equal(map.styles.at(-1).style.layers[0].id,'new-records');
 assert.equal(controller.updateCapture(next),true,'removing an overlay also applies without reloading tiles');assert.equal(map.styles.at(-1).style.sources.records,undefined);
 const latest=structuredClone(next);latest.style.sources.fire.data.features=[];assert.equal(controller.updateCapture(latest),true);
 map.emit('error');map.emit('render');map.emit('idle');assert.equal(h.frames.length,2,'failed new records cannot replace the complete image');assert.match(h.statuses.at(-1),/previous complete surface/);
 controller.refresh();assert.deepEqual(JSON.parse(JSON.stringify(map.styles.at(-1).style.sources.fire.data)),latest.style.sources.fire.data,'manual retry uses the newest capture');
 controller.dispose();assert.equal(h.timers.size,0);assert.equal(controller.updateCapture(latest),false);
});

test('detail construction starts at the latest requested geographic footprint before loading tiles',async()=>{
 const h=harness(),controller=h.start(2048),close=[-100.55,38.45,-100.45,38.55];controller.update(close);await Promise.resolve();
 assert.deepEqual(Array.from(h.maps[0].options.center),Array.from(h.m.surfaceRenderFrame(close,2048).center));
 assert.equal(h.maps[0].options.zoom,h.m.surfaceRenderFrame(close,2048).zoom);controller.dispose();
});

test('a later inline capture recovers from a failed update without publishing incomplete pixels',async()=>{
 const h=harness(),controller=h.start(2048);await Promise.resolve();const map=h.maps[0];map.emit('style.load');map.emit('idle');
 const failed=structuredClone(h.capture);failed.style.sources.fire.data.features=[];
 assert.equal(controller.updateCapture(failed),true);map.emit('error');map.emit('idle');
 assert.equal(h.frames.length,1);assert.match(h.statuses.at(-1),/previous complete surface/);
 const recovered=structuredClone(h.capture);recovered.style.sources.fire.data.features[0].properties.acquisitionTime='2026-10-07T13:32:00Z';
 assert.equal(controller.updateCapture(recovered),true);map.emit('render');
 assert.equal(h.frames.length,1,'hold the previous complete frame until new data settles');
 map.emit('idle');assert.equal(h.frames.length,2);assert.match(h.statuses.at(-1),/Surface detail ready/);
 assert.deepEqual(JSON.parse(JSON.stringify(map.styles.at(-1).style.sources.fire.data)),recovered.style.sources.fire.data);
 assert.equal(h.maps.length,1);assert.equal(map.options.pixelRatio,1);assert.equal(Math.max(h.frames.at(-1).image.width,h.frames.at(-1).image.height),2048);
 // A new error still prevents replacement: recovery never suppresses this attempt's failures.
 assert.equal(controller.updateCapture(failed),true);map.emit('error');map.emit('idle');assert.equal(h.frames.length,2);
 controller.dispose();assert.equal(h.timers.size,0);
});
