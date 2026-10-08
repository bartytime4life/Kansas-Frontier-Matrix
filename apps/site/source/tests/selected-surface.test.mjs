import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness,findNode,settle} from './component-harness.mjs';
const compiled=ts.transpileModule(await readFile('app/selected-surface.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const m=await import(`data:text/javascript;base64,${Buffer.from(compiled).toString('base64')}`);
const bounds=[-100.7,38.3,-100.3,38.7];
const style=()=>({version:8,sources:{satellite:{type:'raster',tiles:['/image/{z}/{x}/{y}?TIME=2007-05-05T12:35:00Z'],tileSize:256},fire:{type:'geojson',data:{type:'FeatureCollection',features:[{type:'Feature',geometry:{type:'Point',coordinates:[-100.5,38.5]},properties:{checkedDay:'2026-10-07',acquisitionTime:'2026-10-07T13:02:00Z',confidence:'nominal'}}]}},classes:{type:'raster',tiles:['/earth-engine/2023/{z}/{x}/{y}']},animation:{type:'canvas',canvas:'wind'}},layers:[{id:'satellite',type:'raster',source:'satellite'},{id:'thermal',type:'circle',source:'fire'},{id:'classification',type:'raster',source:'classes',paint:{'raster-resampling':'nearest'}},{id:'wind',type:'raster',source:'animation'},{id:'custom',type:'custom'},{id:'hidden',type:'line',source:'fire',layout:{visibility:'none'}}]});
function sourceMap(){const listeners=new Map();return{extent:[...bounds],style:style(),getBounds(){const b=this.extent;return{getWest:()=>b[0],getSouth:()=>b[1],getEast:()=>b[2],getNorth:()=>b[3]}},getStyle(){return this.style},listImages:()=>['pin'],getImage:()=>({data:{width:1,height:1,data:new Uint8Array([1,2,3,255])},pixelRatio:1,sdf:false}),on(name,fn){if(!listeners.has(name))listeners.set(name,new Set());listeners.get(name).add(fn)},off(name,fn){listeners.get(name)?.delete(fn)},emit(name){for(const fn of listeners.get(name)??[])fn()}};}
test('selected surface preserves exact source frames and point values in a detached copy',()=>{
 const source=sourceMap(),copy=m.captureSelectedSurface(source,bounds);
 assert.deepEqual(copy.bounds,bounds);assert.notEqual(copy.bounds,bounds);
 assert.equal(copy.style.sources.satellite.tiles[0],source.style.sources.satellite.tiles[0]);
 assert.deepEqual(copy.style.sources.fire.data,source.style.sources.fire.data);
 source.style.sources.fire.data.features[0].properties.confidence='changed';source.style.sources.satellite.tiles[0]='/other';
 assert.equal(copy.style.sources.fire.data.features[0].properties.confidence,'nominal');assert.match(copy.style.sources.satellite.tiles[0],/12:35:00Z/);
 assert.equal(copy.omitted,2);assert.deepEqual(copy.style.layers.map(l=>l.id),['satellite','thermal','classification']);
 assert.equal(copy.style.sources.animation,undefined);assert.equal(copy.style.projection.type,'mercator');
 assert.deepEqual([...copy.images[0].data.data],[1,2,3,255]);
});
test('preview extent drift cannot replace the fixed selected slice or its time-bound sources',()=>{
 const source=sourceMap();source.extent=[-99,38,-98.7,38.3];assert.equal(m.captureSelectedSurface(source,bounds),null);
 source.getBounds=()=>{throw new Error('style unavailable')};assert.equal(m.captureSelectedSurface(source,bounds),null);
});
test('mask and camera constraints use exactly the accepted bounds; crisp display preserves categorical sampling',()=>{
 const copy=m.captureSelectedSurface(sourceMap(),bounds),render=m.surfaceSliceStyle(copy);
 assert.deepEqual(m.constrainSurfaceCenter(bounds,{lng:-120,lat:55}),[-100.7,38.7]);
 assert.deepEqual(m.constrainSurfaceCenter(bounds,{lng:-70,lat:20}),[-100.3,38.3]);
 assert.deepEqual(m.surfaceCameraBounds(bounds),[[-100.7,38.3],[-100.3,38.7]]);
 const features=render.sources['kfm-selected-surface-mask'].data.features;
 assert.deepEqual(features[1].geometry.coordinates,[[-100.7,38.3],[-100.3,38.3],[-100.3,38.7],[-100.7,38.7],[-100.7,38.3]]);
 assert.equal(render.layers.at(-2).paint['fill-opacity'],1);assert.equal(copy.style.sources['kfm-selected-surface-mask'],undefined);
 assert.deepEqual(m.surfaceRasterSampling(copy.style,true),[{id:'satellite',value:'linear'},{id:'classification',value:'nearest'}]);
 assert.ok(m.surfaceRasterSampling(copy.style,false).every(x=>x.value==='nearest'));
});
const styles=new Proxy({},{get:(_,key)=>String(key)});
const button=(tree,label)=>findNode(tree,n=>n.type==='button'&&(n.props['aria-label']===label||n.props.children===label));
async function harness(){
 const maps=[],source=sourceMap();let tree;
 class FakeMap{
  constructor(options){this.options=options;this.center={lng:-100.5,lat:38.5};this.zoom=10;this.events=new Map();this.paint=[];this.canvas={setAttribute(){}};this.touchZoomRotate={disableRotation(){}};this.keyboard={disableRotation(){}};maps.push(this);}
  on(name,fn){if(!this.events.has(name))this.events.set(name,new Set());this.events.get(name).add(fn)}
  emit(name,event){for(const fn of this.events.get(name)??[])fn(event)}
  getCanvas(){return this.canvas}addControl(){}hasImage(){return true}setPaintProperty(...args){this.paint.push(args)}
  getCenter(){return this.center}getZoom(){return this.zoom}isStyleLoaded(){return true}
  jumpTo(value){this.center={lng:value.center[0],lat:value.center[1]};this.zoom=value.zoom;this.emit('moveend')}
  zoomIn(){this.zoom=this.options.transformConstrain(this.center,this.zoom+1).zoom;this.emit('moveend')}zoomOut(){this.zoom=this.options.transformConstrain(this.center,this.zoom-1).zoom;this.emit('moveend')}
  fitBounds(frame){this.fit=frame;this.jumpTo({center:[-100.5,38.5],zoom:10})}
  cameraForBounds(){return{zoom:10}}setMinZoom(value){this.minZoom=value}getMinZoom(){return this.minZoom??0}getMaxZoom(){return 22}resize(){}remove(){this.removed=true}
 }
 const h=await componentHarness('app/selected-surface-map.tsx',{'./maplibre-seam':{loadMapLibre:async()=>({Map:FakeMap,LngLat:class{constructor(lng,lat){this.lng=lng;this.lat=lat}},ScaleControl:class{},setWorkerUrl(){}})},'./selected-surface':m,'./map-performance':{browserRenderBudget:()=>({pixelRatio:1,tileCache:48})},'./subsurface.module.css':{default:styles}},{ResizeObserver:class{observe(){}disconnect(){}}});
 let props={source,bounds,image:null,active:true,smooth:true,onSmooth(){}};
 const render=async(patch={})=>{props={...props,...patch};tree=h.render(h.exports.default,props);findNode(tree,n=>n.props?.className==='surfaceMap').props.ref.current={};h.commit();await settle();return tree};
 await render();await render();maps.at(-1).emit('load');await render();
 return{h,source,maps,render,get tree(){return tree}};
}
test('right surface zoom, fit, layer reload and view switching never change the selector slice',async()=>{
 const h=await harness(),initial=h.source.extent.slice(),first=h.maps[0];
 assert.deepEqual(first.options.maxBounds,m.surfaceCameraBounds(bounds));assert.equal(first.options.maxPitch,0);
 button(h.tree,'Zoom selected surface in').props.onClick();await h.render();assert.equal(first.zoom,11);assert.deepEqual(h.source.extent,initial);
 first.center.lng=-100.44; // An in-flight pan has not emitted moveend yet.
 await h.render({active:false});assert.equal(first.removed,true);await h.render({active:true});h.maps.at(-1).emit('load');await h.render();assert.equal(h.maps.at(-1).zoom,11);assert.equal(h.maps.at(-1).center.lng,-100.44);
 button(h.tree,'Reload surface layers').props.onClick();await h.render();await h.render();h.maps.at(-1).emit('load');assert.equal(h.maps.at(-1).zoom,11);
 button(h.tree,'Fit selected slice').props.onClick();await h.render();assert.equal(h.maps.at(-1).zoom,10);assert.deepEqual(h.source.extent,initial);
 h.source.extent=[-99,38,-98.7,38.3];h.source.emit('moveend');await h.render();assert.equal(button(h.tree,'Reload surface layers').props.disabled,true);assert.deepEqual(h.maps.at(-1).options.maxBounds,m.surfaceCameraBounds(bounds));
 h.h.dispose();assert.ok(h.maps.every(map=>map.removed));
});
test('surface layer errors remain explicit after map load and smoothing never edits source values',async()=>{
 const h=await harness(),map=h.maps[0];map.emit('error');map.emit('load');await h.render();
 const status=findNode(h.tree,n=>n.props?.className==='surfaceStatus');assert.match(JSON.stringify(status),/Blank areas are gaps/);
 await h.render({smooth:false});assert.deepEqual(map.paint.at(-1),['classification','raster-resampling','nearest']);
 assert.equal(h.source.style.sources.fire.data.features[0].properties.confidence,'nominal');h.h.dispose();
});

test('custom surface constraint honors both zoom limits and immediately reverses after repeated boundary attempts',async()=>{
 const h=await harness(),map=h.maps[0],slice=[...h.source.extent];
 for(let i=0;i<50;i++)button(h.tree,'Zoom selected surface out').props.onClick();
 assert.equal(map.zoom,10);button(h.tree,'Zoom selected surface in').props.onClick();assert.equal(map.zoom,11);
 for(let i=0;i<50;i++)button(h.tree,'Zoom selected surface in').props.onClick();
 assert.equal(map.zoom,22);button(h.tree,'Zoom selected surface out').props.onClick();assert.equal(map.zoom,21);
 assert.deepEqual(h.source.extent,slice);h.h.dispose();
});
