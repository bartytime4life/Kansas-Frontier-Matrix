import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';
const load=async path=>{const exports={};new Function('exports',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports);return exports;};
const f=await load('app/flora-context.ts'), maps=await load('app/category-maps.ts'), topics=await load('app/layer-workspaces.ts');
function fakeMap(){
 const layers=[{id:'background',type:'background'},{id:'labels',type:'symbol'}],sources={},events=new Map();
 return {layers,sources,events,getStyle:()=>({layers:[...layers],sources}),isStyleLoaded:()=>true,
  getSource:id=>sources[id],addSource:(id,spec)=>{sources[id]=spec;},removeSource:id=>{assert.ok(!layers.some(l=>l.source===id));delete sources[id];},
  getLayer:id=>layers.find(l=>l.id===id),removeLayer:id=>{layers.splice(layers.findIndex(l=>l.id===id),1);},
  addLayer:(spec,before)=>{const i=layers.findIndex(l=>l.id===before);layers.splice(i<0?layers.length:i,0,spec);},
  moveLayer(id,before){const layer=this.getLayer(id);this.removeLayer(id);this.addLayer(layer,before);},
  setPaintProperty(id,k,v){this.getLayer(id).paint[k]=v;},setLayoutProperty(id,k,v){const l=this.getLayer(id);l.layout={...l.layout,[k]:v};},
  on(k,fn){if(!events.has(k))events.set(k,new Set());events.get(k).add(fn);},off(k,fn){events.get(k)?.delete(fn);},emit(k,event){for(const fn of [...events.get(k)??[]])fn(event);}
 };
}
test('Flora is a separate category with vegetation, records and crop tools; exact sites are withheld',()=>{
 assert.equal(topics.topicDefinition('flora').group,'Earth & environment');
 assert.deepEqual([...topics.registryLayerTopics('flora')],['ecology','flora']);
 assert.ok(!topics.registryLayerTopics('fauna').includes('flora'));
 assert.deepEqual([...maps.CATEGORY_MAPS.flora.tools],['landcover','plants','crops','area']);
 assert.match(topics.topicDefinition('flora').limitation,/Exact plant sites.*not connected/);
 assert.match(f.floraKey(2021).note,/not a count legend/);
});
test('plant layers use only the fixed annual proxy and coarse source budget, with no old year retained',()=>{
 for(const year of [1994,2026,2021.5,NaN])assert.throws(()=>f.floraTileUrl(year));
 assert.equal(f.floraTileUrl(2021),'/api/event-atlas/tile?kind=flora&date=2021-01-01&z={z}&x={x}&y={y}');
 const m=fakeMap(),id=f.floraSourceId(2021);
 f.syncFloraContext(m,2021);
 assert.equal(m.sources[id].maxzoom,6);assert.equal(m.sources[id].tileSize,512);
 assert.deepEqual(m.sources[id].bounds,[-102.1,36.9,-94.5,40.1]);
 f.syncFloraContext(m,2021,0.35);assert.equal(m.getLayer(id).paint['raster-opacity'],0.35);
 f.syncFloraContext(m,2020);assert.equal(m.getSource(id),undefined);assert.equal(m.getLayer(id),undefined);
 assert.deepEqual(Object.keys(m.sources),[f.floraSourceId(2020)]);
 f.syncFloraContext(m,null);assert.deepEqual(Object.keys(m.sources),[]);
});
test('tile failures hide records until retry; late events and unrelated failures cannot settle a different year',()=>{
 const m=fakeMap(),states=[],id=f.floraSourceId(2021);
 let stop=f.watchFloraContext(m,2021,0,()=>0.75,s=>states.push(s));
 const lateLoaded=[...m.events.get('sourcedata')][0];
 m.emit('error',{sourceId:'basemap'});assert.deepEqual(states,['loading']);
 m.emit('sourcedata',{sourceId:id,isSourceLoaded:true});assert.equal(states.at(-1),'settled');
 m.emit('error',{sourceId:id});assert.equal(states.at(-1),'failed');assert.equal(m.getLayer(id).layout.visibility,'none');
 m.emit('sourcedata',{sourceId:id,isSourceLoaded:true});assert.equal(states.at(-1),'failed');
 stop();stop=f.watchFloraContext(m,2021,1,()=>0.4,s=>states.push(s));
 assert.equal(m.getLayer(id),undefined);assert.equal(states.at(-1),'loading');
 lateLoaded({sourceId:id,isSourceLoaded:true});assert.equal(states.at(-1),'loading');
 m.emit('sourcedata',{sourceId:f.floraSourceId(2021,1),isSourceLoaded:true});assert.equal(states.at(-1),'settled');
 stop();f.watchFloraContext(m,null,1,()=>0.4,()=>{});assert.deepEqual(Object.keys(m.sources),[]);
 for(const listeners of m.events.values())assert.equal(listeners.size,0);
});
test('style replacement restores the selected year; later cover layers remain below the plant records',()=>{
 const m=fakeMap(),states=[],id=f.floraSourceId(2021),stop=f.watchFloraContext(m,2021,0,()=>0.65,s=>states.push(s));
 m.addLayer({id:'tool-nlcd-land-cover-raster',type:'raster'});m.emit('styledata',{});
 assert.ok(m.layers.findIndex(l=>l.id===id)>m.layers.findIndex(l=>l.id==='tool-nlcd-land-cover-raster'));
 m.removeLayer(id);m.removeSource(id);m.emit('styledata',{});
 assert.ok(m.getSource(id));assert.equal(m.getLayer(id).paint['raster-opacity'],0.65);assert.equal(states.at(-1),'loading');stop();
});
test('dock exposes annual, opacity and retry controls with source limits, and opening another category clears plants',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{}),calls=[];
 const base={look:maps.CATEGORY_MAPS.flora,mode:'2d',depth:1,azimuth:315,onMode(){},onDepth(){},onAzimuth(){},onReset(){},onLayers(){},onClose(){},
  flora:{on:true,year:2021,years:f.FLORA_YEARS,opacity:0.75,failed:true,reading:f.floraReading(2021,'failed')},onFlora:v=>calls.push(v),onFloraYear:v=>calls.push(v),onFloraOpacity:v=>calls.push(v),onFloraRetry:()=>calls.push('retry')};
 const tree=h.render(h.exports.CategoryMapDock,base);
 findNode(tree,n=>n.type==='button'&&n.props.children==='Hide plant records').props.onClick();
 findNode(tree,n=>n.type==='select'&&n.props.value===2021).props.onChange({target:{value:'2020'}});
 findNode(tree,n=>n.type==='input'&&n.props.value===0.75).props.onChange({target:{value:'0.4'}});
 findNode(tree,n=>n.type==='button'&&n.props.children==='Retry plant records').props.onClick();assert.deepEqual(calls,[false,2020,0.4,'retry']);
 assert.match(JSON.stringify(tree),/independent of the map calendar/);assert.match(JSON.stringify(tree),/not a guarantee of coverage/);
 const other=h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.fauna});assert.doesNotMatch(JSON.stringify(other),/Plant record year/);
 const page=await readFile('app/page.tsx','utf8');assert.match(page,/showLandCover\(topic === "flora"\);\s*setFloraOn\(false\);\s*setFloraYear\(FLORA_DEFAULT_YEAR\)/);
 h.dispose();
});
