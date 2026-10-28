import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { webcrypto } from 'node:crypto';
import vm from 'node:vm';
const compile = async path => ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
const airspace={},chart={};
new Function('exports',await compile('app/aviation-airspace.ts'))(airspace);
new Function('exports',await compile('app/aviation-chart.ts'))(chart);
const code=await compile('app/living-welcome/aviation-preview.ts');
const bytes=await readFile('public/data/aviation/kansas-aviation-context.json');
const context=airspace.parseAviationContext(JSON.parse(bytes));
const load=(fetch)=>{const exports={};vm.runInNewContext(code,{exports,require:id=>id==='../aviation-airspace'?airspace:chart,fetch,AbortController,AbortSignal,TextDecoder,Uint8Array,crypto:webcrypto,Date,setTimeout,clearTimeout});return exports;};
const tick=()=>new Promise(resolve=>setTimeout(resolve,0));
async function until(condition){for(let i=0;i<100&&!condition();i++)await tick();assert.ok(condition(),'asynchronous reference read settled');}
class MapStandIn {
 constructor(){this.sources=new Map();this.layers=new Map();this.updates=0;}
 getSource(id){return this.sources.get(id);} getLayer(id){return this.layers.get(id);}
 addSource(id,value){assert.ok(!this.sources.has(id));this.sources.set(id,{...value,setData:data=>{this.sources.get(id).data=data;this.updates++;}});}
 addLayer(value){this.layers.set(value.id,{...value,layout:{...value.layout}});}
 setLayoutProperty(id,key,value){assert.ok(this.layers.has(id));this.layers.get(id).layout[key]=value;}
 removeLayer(id){this.layers.delete(id);} removeSource(id){this.sources.delete(id);}
}
test('welcome reads only the pinned local asset and rejects altered, oversized and failed bytes',async()=>{
 let request;const reader=load(async(url,options)=>{request={url,options};return new Response(bytes);});
 const parsed=await reader.readWelcomeAviation(new AbortController().signal);
 assert.equal(parsed.nasrCycle,context.nasrCycle);assert.equal(request.url,airspace.AVIATION_CONTEXT_ASSET.url);
 assert.equal(request.options.redirect,'error');assert.equal(request.options.cache,'force-cache');
 for(const response of [()=>new Response(bytes.toString().replace('2026-10-29','2026-10-28')),()=>new Response('x',{status:503}),()=>new Response('x',{headers:{'content-length':String(airspace.AVIATION_CONTEXT_ASSET.maxBytes+1)}}),()=>new Response(new Uint8Array(airspace.AVIATION_CONTEXT_ASSET.maxBytes+1))]) {
  await assert.rejects(load(async()=>response()).readWelcomeAviation(new AbortController().signal));
 }
});
test('aborted streamed reference is cancelled and cannot be accepted as complete',async()=>{
 const abort=new AbortController();let cancelled=false,enqueue;
 const stream=new ReadableStream({start(controller){enqueue=controller;},cancel(){cancelled=true;}});
 const pending=load(async()=>new Response(stream)).readWelcomeAviation(abort.signal);
 enqueue.enqueue(bytes.subarray(0,32));await tick();abort.abort();await assert.rejects(pending);assert.equal(cancelled,true);
});
test('rendered zones preserve existing geometry, group selection and 1× heights; slice uses MSL',async()=>{
 let calls=0,changes=0;const map=new MapStandIn();
 const adapter=load(async()=>{calls++;return new Response(bytes);}).createWelcomeAviation(map,()=>changes++);
 assert.equal(calls,0,'no request at construction');adapter.prepare();adapter.prepare();await until(()=>changes===1);
 assert.equal(calls,1);assert.equal(adapter.status().state,'ready');
 adapter.render(true,'3d');
 const zone=map.getSource('welcome-aviation-zones');
 const expected=airspace.airspaceFeatures(context,new Set(Object.keys(airspace.AIRSPACE_GROUPS).filter(id=>airspace.AIRSPACE_GROUPS[id].defaultOn)),1);
 assert.equal(JSON.stringify(zone.data),JSON.stringify(expected));
 assert.equal(map.getSource('welcome-aviation-airports').data.features.length,533);
 assert.equal(map.getLayer('welcome-aviation-zones-3d').layout.visibility,'visible');
 const updates=map.updates;adapter.render(true,'3d');assert.equal(map.updates,updates,'no geometry upload for unchanged view');
 adapter.render(true,'slice');assert.ok(zone.data.features.length>0&&zone.data.features.length<expected.features.length);
 for(const feature of zone.data.features){const span=chart.featureSpan(feature,1,()=>0);assert.ok(span.lowMsl<=4000&&4000<span.highMsl);}
 assert.equal(map.getLayer('welcome-aviation-zones-3d').layout.visibility,'none');
 adapter.render(false,'slice');assert.ok([...map.layers.values()].every(layer=>layer.layout.visibility==='none'));
 assert.equal(adapter.status(false).state,'hidden');adapter.render(true,'2d');assert.equal(JSON.stringify(zone.data),JSON.stringify(expected));
 map.sources.clear();map.layers.clear();adapter.render(true,'3d');assert.equal(map.layers.size,9,'style replacement recreates only owned layers');
 adapter.dispose();assert.equal(map.layers.size,0);assert.equal(map.sources.size,0);assert.equal(calls,1);
});
test('late completion and failures cannot reveal disposed or unavailable overlays',async()=>{
 let finish,changes=0;const map=new MapStandIn();const adapter=load(()=>new Promise(resolve=>finish=resolve)).createWelcomeAviation(map,()=>changes++);
 adapter.prepare();adapter.dispose();finish(new Response(bytes));await tick();await tick();assert.equal(changes,0);assert.equal(map.sources.size,0);
 const failed=load(async()=>new Response('bad')).createWelcomeAviation(map,()=>changes++);failed.prepare();await until(()=>changes===1);
 assert.equal(failed.status().state,'unavailable');failed.render(true,'3d');assert.equal(map.sources.size,0);failed.dispose();
});
