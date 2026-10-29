import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import { webcrypto, createHash } from 'node:crypto';
import { gunzipSync } from 'node:zlib';
import vm from 'node:vm';
import ts from 'typescript';
import { componentHarness, findNode, settle } from './component-harness.mjs';
const compile=async name=>ts.transpileModule(await readFile(name,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
const materials={},model={};
new Function('exports',await compile('app/subsurface-materials.ts'))(materials);
new Function('exports','require',await compile('app/subsurface-model.ts'))(model,()=>materials);
const sourceCode=await compile('app/living-welcome/geology-source.ts');
const compressed=await readFile('public/data/subsurface/tile-164-257311.json.gz'),decoded=gunzipSync(compressed),raw=JSON.parse(decoded);
function load(fetch){const exports={};vm.runInNewContext(sourceCode,{exports,require:id=>id==='../subsurface-model'?model:materials,fetch,DOMException,TextDecoder,Uint8Array,Blob,DecompressionStream,crypto:webcrypto});return exports;}
const source=load(()=>{throw Error('No eager request');}),record=source.geologyRecord(raw);
const signal=()=>new AbortController().signal;
const tick=()=>new Promise(resolve=>setTimeout(resolve,0));
const text=node=>typeof node==='string'||typeof node==='number'?String(node):[node?.props?.children].flat(Infinity).filter(v=>v!=null).map(text).join(' ');

test('the only welcome source is the existing manifest-pinned small tile; gzip and transparent decoding agree',async()=>{
 const manifest=JSON.parse(await readFile('public/data/subsurface/manifest.json','utf8')),pin=source.WELCOME_GEOLOGY_SOURCE;
 const entry=manifest.tiles.find(row=>row.url===pin.url);assert.ok(entry);
 assert.equal(entry.bytes,pin.maxBytes);assert.equal(entry.uncompressedBytes,pin.maxDecodedBytes);
 assert.equal(entry.sha256,pin.sha256);assert.equal(entry.decodedSha256,pin.decodedSha256);
 assert.equal(createHash('sha256').update(compressed).digest('hex'),pin.sha256);assert.equal(createHash('sha256').update(decoded).digest('hex'),pin.decodedSha256);
 for(const bytes of [compressed,decoded]){
  let request;const reader=load(async(url,options)=>{request={url,options};return new Response(bytes,{headers:{'content-length':String(compressed.length)}});});
  const value=await reader.readWelcomeGeology(signal());assert.equal(JSON.stringify(value),JSON.stringify(record));
  assert.equal(request.url,pin.url+'?sha256='+pin.sha256);assert.equal(request.options.redirect,'error');assert.equal(request.options.cache,'force-cache');
 }
});
test('failed, redirected, changed and oversized source responses stay unavailable',async()=>{
 for(const make of [()=>new Response('failed',{status:503}),()=>{const response=new Response(compressed);Object.defineProperty(response,'redirected',{value:true});return response;},()=>new Response(new Uint8Array(source.WELCOME_GEOLOGY_SOURCE.maxDecodedBytes+1)),()=>new Response(new Uint8Array([0x1f,0x8b,...new Uint8Array(5680)])),()=>new Response(Buffer.from(decoded.toString().replace('top soil','not soil')))])await assert.rejects(load(async()=>make()).readWelcomeGeology(signal()));
 let cancelled=false;const body=new ReadableStream({cancel(){cancelled=true;}});
 await assert.rejects(load(async()=>new Response(body,{headers:{'content-length':'60441'}})).readWelcomeGeology(signal()));assert.equal(cancelled,true,'early size rejection cancels the body');
});
test('aborting a slow source cancels its owned reader and rejects partial data',async()=>{
 let streamController,cancelled=false;const abort=new AbortController();
 const body=new ReadableStream({start(controller){streamController=controller;},cancel(){cancelled=true;}});
 const pending=load(async()=>new Response(body)).readWelcomeGeology(abort.signal);streamController.enqueue(compressed.subarray(0,18));await tick();abort.abort();await assert.rejects(pending);assert.equal(cancelled,true);
 await assert.rejects(load(async()=>new Response(compressed)).readWelcomeGeology(abort.signal));
});
test('schema, exact identity, date, original units, depth reference and ordered intervals are required',()=>{
 for(const mutate of [rows=>rows.pop(),rows=>rows[0].coordinates=[0,0],rows=>rows.find(r=>r.id===record.id).id='wrong',rows=>rows.push({...record}),rows=>rows.find(r=>r.id===record.id).sourceTime='2025-04-09',rows=>rows.find(r=>r.id===record.id).depthUnit='m',rows=>rows.find(r=>r.id===record.id).depthReference='unknown',rows=>rows.find(r=>r.id===record.id).intervals.reverse(),rows=>rows.find(r=>r.id===record.id).intervals[1].top=3]){
  const value=structuredClone(raw);mutate(value);assert.throws(()=>source.geologyRecord(value));
 }
 assert.throws(()=>source.geologyRecord({records:raw}));
});
test('all eight original descriptions and depths retain exact proportional geometry and material neutrality',()=>{
 const intervals=source.geologyIntervals(record);
 assert.equal(intervals.length,8);assert.deepEqual(intervals.map(r=>[r.top,r.bottom]),[[0,2],[2,6],[6,18],[18,20],[20,25],[25,35],[35,50],[50,60]]);
 intervals.forEach((row,i)=>{assert.equal(row.description,record.intervals[i].description);assert.equal(row.y,record.intervals[i].top/60*204);assert.equal(row.height,(record.intervals[i].bottom-record.intervals[i].top)/60*204);});
 assert.equal(intervals.reduce((sum,row)=>sum+row.height,0),204);
 const uncertain=structuredClone(record);uncertain.intervals[0].description='possible clay and sand';assert.equal(source.geologyIntervals(uncertain)[0].material.id,'unknown');
});
async function specimen({paused=false,reduced=false}={},reader=async()=>record){
 const listeners=new Map();let reads=0,aborted=false;
 const props={paused,reduced,expanded:true};
 const document={hidden:false,addEventListener:(id,fn)=>listeners.set(id,fn),removeEventListener:id=>listeners.delete(id)};
 const harness=await componentHarness('app/living-welcome/GeologyGlimpse.jsx',{'./geology-source':{geologyIntervals:source.geologyIntervals,readWelcomeGeology:async signal=>{reads++;signal.addEventListener('abort',()=>aborted=true);return reader(signal);}}},{document});
 const render=()=>{const tree=harness.render(harness.exports.GeologyGlimpse,props);harness.commit();return tree;};
 return {harness,props,render,listeners,document,reads:()=>reads,aborted:()=>aborted};
}
test('one finite reveal honors pause, reduced motion and hidden documents; manual comparison reuses the exact log',async()=>{
 for(const start of [{paused:false,reduced:false},{paused:true,reduced:false},{paused:false,reduced:true}]){
  const h=await specimen(start);try{
   let tree=h.render();assert.equal(tree.props['data-state'],'loading');await settle();tree=h.render();assert.equal(tree.props['data-state'],'ready');assert.equal(h.reads(),1);
   assert.equal(tree.props['data-auto'],!start.paused&&!start.reduced);assert.equal(tree.props['data-lifted'],true);
   assert.match(text(tree),/One recorded well · 2024 log/);assert.match(text(tree),/0–60 ft below local land surface/);assert.match(text(tree),/Width illustrative; unknown between observations/);
   record.intervals.forEach(row=>assert.ok(text(tree).includes(row.description)));
   h.props.paused=true;tree=h.render();assert.equal(tree.props['data-paused'],true);
   h.props.paused=false;tree=h.render();assert.equal(tree.props['data-paused'],false);
   h.document.hidden=true;h.listeners.get('visibilitychange')();tree=h.render();assert.equal(tree.props['data-paused'],true,'hidden document freezes the reveal');h.document.hidden=false;h.listeners.get('visibilitychange')();tree=h.render();assert.equal(tree.props['data-paused'],false);
   const plate=findNode(tree,node=>node.props?.className==='welcome-geology-plate');plate.props.onAnimationEnd();tree=h.render();assert.equal(tree.props['data-auto'],false,'ending holds without an animation loop');
   const button=findNode(tree,node=>node.type==='button');button.props.onClick();tree=h.render();assert.equal(tree.props['data-lifted'],false);findNode(tree,node=>node.type==='button').props.onClick();tree=h.render();assert.equal(tree.props['data-lifted'],true);assert.equal(h.reads(),1,'manual replay does not request data again');
   assert.equal(findNode(tree,node=>node.type==='a').props.href,record.sourceUrl);
  }finally{h.harness.dispose();}assert.equal(h.aborted(),true);assert.equal(h.listeners.size,0);
 }
});
test('late completion cannot populate an obsolete specimen, and failure draws no fallback column',async()=>{
 let resolve;const h=await specimen({},()=>new Promise(done=>resolve=done));h.render();h.harness.dispose();resolve(record);await settle();assert.equal(h.render().props['data-state'],'loading');
 const failed=await specimen({},async()=>{throw Error('digest mismatch');});try{failed.render();await settle();const tree=failed.render();assert.equal(tree.props['data-state'],'unavailable');assert.match(text(tree),/No substitute geology is drawn/);assert.equal(findNode(tree,node=>node.type==='svg'),undefined);}finally{failed.harness.dispose();}
});
test('settled Geology alone lazy-loads its component and a stale import cannot surface under another category',async()=>{
 let imports=0,next=0;const timers=new Map();
 const importsObject={'../map-runtime':{BASEMAPS:{standard:{note:'Provider credit'}}},'../live-context':{OFFICIAL_CONTEXT_BY_ID:{}},'../welcome-map-view':{welcomeView:topic=>({topic,name:'Map',basemap:'standard',detail:'Context'})}};
 Object.defineProperty(importsObject,'./GeologyGlimpse.jsx',{get(){imports++;return {GeologyGlimpse:'geology-glimpse'};}});
 const stage=await componentHarness('app/living-welcome/DomainStage.jsx',importsObject,{window:{requestIdleCallback:()=>1,cancelIdleCallback(){}},setTimeout:(fn,ms)=>{const id=++next;timers.set(id,{fn,ms});return id;},clearTimeout:id=>timers.delete(id)});
 const props={topic:'weather',paused:false,reduced:false,expanded:true};const render=()=>{const tree=stage.render(stage.exports.DomainStage,props);stage.commit();return tree;};
 try{render();assert.equal(timers.size,0);assert.equal(imports,0);props.topic='geology';render();assert.equal(imports,0);assert.equal(timers.size,1);props.topic='weather';render();assert.equal(timers.size,0,'leaving before settling cancels import');props.topic='geology';render();const timer=[...timers.values()].find(t=>t.ms===220);timer.fn();props.topic='weather';render();await settle();assert.equal(findNode(render(),node=>node.type==='geology-glimpse'),undefined,'stale import cannot mount a log in weather');props.topic='geology';render();[...timers.values()].at(-1).fn();await settle();assert.ok(findNode(render(),node=>node.type==='geology-glimpse'));assert.equal(findNode(render(),node=>node.type==='canvas'),undefined);}finally{stage.dispose();}
});
