import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import test from 'node:test';
import ts from 'typescript';
const digest = b => createHash('sha256').update(new Uint8Array(b)).digest('hex');
const buffer = text => new TextEncoder().encode(text).buffer;
const source = await readFile('app/local-geopdf-review.ts', 'utf8');
const compile = code => `data:text/javascript;base64,${Buffer.from(ts.transpileModule(code, {compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`;
const actual = await import(compile(source));
// Synthetic bytes replace only the pin constants in this test module. There is
// no runtime pin override in the application, and no source PDF enters Git.
const payloads = new Map([['input.pdf',buffer('%PDF-1.7 synthetic only')], ['page.png',buffer('synthetic page')], ['viewport-preview.png',buffer('synthetic preview')], ['viewport.tif',buffer('synthetic raster')]]);
const artifacts = Object.fromEntries([...payloads].map(([n,b])=>[n,{bytes:b.byteLength,sha256:digest(b)}]));
const tiles = {};
for(let i=0;i<181;i++){ const b=buffer(`synthetic tile ${i}`);payloads.set(`tiles/10/${i}/1.png`,b);tiles[`10/${i}/1`]={bytes:b.byteLength,sha256:digest(b)}; }
const manifest = {version:1,candidateId:actual.ALLEN_REVIEW.candidateId,state:'LOCAL_REVIEW_ONLY',siteServing:false,source:{sha256:artifacts['input.pdf'].sha256},holds:['ACTIVATION','RELEASE_REVIEW'],artifacts,display:{boundsWgs84:[-95.56,37.72,-95.04,38.05],minZoom:10,maxZoom:13,tiles}};
payloads.set('candidate.json',buffer(JSON.stringify(manifest)));
const pins={...actual.ALLEN_REVIEW,manifestSha256:digest(payloads.get('candidate.json')),sourceSha256:artifacts['input.pdf'].sha256,totalBytes:[...payloads.values()].reduce((n,b)=>n+b.byteLength,0)};
const fixtureSource=source.replace(/export const ALLEN_REVIEW = Object.freeze\(\{[\s\S]*?\}\);/,`export const ALLEN_REVIEW = Object.freeze(${JSON.stringify(pins)});`);
assert.notEqual(fixtureSource,source);
const {inspectLocalReview}=await import(compile(fixtureSource));
const files=()=>[...payloads].map(([name,bytes])=>({name:name.split('/').at(-1),webkitRelativePath:`prepared/${name}`,size:bytes.byteLength,arrayBuffer:async()=>bytes.slice(0)}));
const signal=()=>new AbortController().signal;
test('pins bind the real private candidate and contain no hosted location',()=>{
 assert.equal(actual.ALLEN_REVIEW.manifestSha256,'7796ae7a428286be480704a5e80c27e41bbcdc75edbed87fc794331dc4914cf4');
 assert.equal(actual.ALLEN_REVIEW.fileCount,186);
 assert.doesNotMatch(source,/fetch\(|localStorage|indexedDB|XMLHttpRequest/);
});
test('complete package verifies every file, retains exact tile bytes and makes no request',async()=>{
 const saved=globalThis.fetch;globalThis.fetch=()=>{throw new Error('network forbidden')};
 try{const pack=await inspectLocalReview(files(),signal());assert.equal(pack.tiles.size,181);assert.equal(pack.original.type,'application/pdf');assert.deepEqual(pack.tiles.get('10/0/1'),payloads.get('tiles/10/0/1.png'));assert.deepEqual(pack.bounds,manifest.display.boundsWgs84);}finally{globalThis.fetch=saved;}
});
test('wrong, missing, extra, duplicate and traversing selections are refused before payload reads',async()=>{
 for(const alter of [f=>f.slice(1),f=>[...f,f[0]],f=>{f[1]={...f[0]};return f},f=>{f[0].webkitRelativePath='prepared/../input.pdf';return f},f=>{f[0].size=3_000_000;return f}]){
  const selected=alter(files());let reads=0;for(const f of selected)f.arrayBuffer=async()=>{reads++;return new ArrayBuffer(0)};
  await assert.rejects(inspectLocalReview(selected,signal()));assert.equal(reads,0);
 }
});
test('a changed manifest cannot grant approval or substitute transforms',async()=>{
 const f=files(),m=f.find(x=>x.name==='candidate.json');m.arrayBuffer=async()=>{const b=payloads.get('candidate.json').slice(0);new Uint8Array(b)[0]^=1;return b};
 await assert.rejects(inspectLocalReview(f,signal()),/manifest differs/);
});
test('changed tile bytes and artifact sizes withhold the whole package',async()=>{
 for(const name of ['tiles/10/1/1.png','input.pdf','viewport.tif']){
  const f=files(),item=f.find(x=>x.webkitRelativePath===`prepared/${name}`);item.arrayBuffer=async()=>{const b=payloads.get(name).slice(0);new Uint8Array(b)[0]^=1;return b};
  await assert.rejects(inspectLocalReview(f,signal()),/integrity check/);
 }
});
test('cancellation discards a native file read and starts no following read',async()=>{
 const f=files(),abort=new AbortController();let release,reads=0;
 const first=f.find(x=>x.name==='candidate.json');first.arrayBuffer=()=>{reads++;return new Promise(r=>{release=r})};
 const pending=inspectLocalReview(f,abort.signal);abort.abort();release(payloads.get('candidate.json').slice(0));
 await assert.rejects(pending,{name:'AbortError'});assert.equal(reads,1);
});
const {attachLocalReview,LOCAL_REVIEW_SOURCE,LOCAL_REVIEW_LAYER}=await import(compile(await readFile('app/local-geopdf-map.ts','utf8')));
function harness(){
 const sources=new Map(),layers=new Map(),listeners=new Map(),protocols=new Map();let state;
 const map={pitch:0,terrain:null,projection:'mercator',getPitch(){return this.pitch},getTerrain(){return this.terrain},getProjection(){return{type:this.projection}},addSource:(n,s)=>sources.set(n,s),getSource:n=>sources.get(n),removeSource:n=>sources.delete(n),addLayer:l=>layers.set(l.id,structuredClone(l)),getLayer:n=>layers.get(n),removeLayer:n=>layers.delete(n),setLayoutProperty:(n,k,v)=>{layers.get(n).layout[k]=v},setPaintProperty:(n,k,v)=>{layers.get(n).paint[k]=v},on:(n,f)=>listeners.set(n,f),off:(n,f)=>{if(listeners.get(n)===f)listeners.delete(n)}};
 const runtime={addProtocol:(n,f)=>protocols.set(n,f),removeProtocol:n=>protocols.delete(n)};
 const pack={bounds:manifest.display.boundsWgs84,minZoom:10,maxZoom:13,tiles:new Map([['10/1/1',buffer('exact')]])};
 const start=()=>attachLocalReview(map,runtime,pack,true,s=>{state=s},'test');
 return{map,runtime,pack,sources,layers,listeners,protocols,start,state:()=>state};
}
test('tiles use geographic addresses with nearest colors, opacity and no raster fade',async()=>{
 const h=harness(),control=h.start(),s=h.sources.get(LOCAL_REVIEW_SOURCE),l=h.layers.get(LOCAL_REVIEW_LAYER);
 assert.deepEqual(s.bounds,manifest.display.boundsWgs84);assert.equal(s.maxzoom,13);assert.equal(l.paint['raster-resampling'],'nearest');assert.equal(l.paint['raster-fade-duration'],0);assert.equal(l.paint['raster-opacity'],.65);
 const tile=await h.protocols.get('kfm-review-test')({url:'kfm-review-test://10/1/1.png'},new AbortController());
 assert.deepEqual(tile.data,h.pack.tiles.get('10/1/1'));assert.notEqual(tile.data,h.pack.tiles.get('10/1/1'));
 control.setOpacity(.2);assert.equal(l.paint['raster-opacity'],.2);control.setVisible(false);assert.equal(l.layout.visibility,'none');assert.equal(h.state(),'hidden');control.dispose();
});
test('tilt, globe and terrain suspend the overlay, and failed tiles stay withheld',async()=>{
 const h=harness(),control=h.start(),l=h.layers.get(LOCAL_REVIEW_LAYER);
 for(const [key,value] of [['pitch',30],['projection','globe'],['terrain',{}]]){
  const old=h.map[key];h.map[key]=value;h.listeners.get('move')();assert.equal(l.layout.visibility,'none');assert.equal(h.state(),'flat-map-required');h.map[key]=old;h.listeners.get('move')();assert.equal(l.layout.visibility,'visible');
 }
 await assert.rejects(h.protocols.get('kfm-review-test')({url:'kfm-review-test://10/2/1.png'},new AbortController()),/unavailable/);
 assert.equal(l.layout.visibility,'none');control.setVisible(true);assert.equal(h.state(),'unavailable');control.dispose();
});
test('teardown releases layers, source, protocol and listeners; late requests are cancelled',async()=>{
 const h=harness(),control=h.start(),loader=h.protocols.get('kfm-review-test');control.dispose();control.dispose();
 assert.equal(h.layers.size+h.sources.size+h.protocols.size+h.listeners.size,0);
 await assert.rejects(loader({url:'kfm-review-test://10/1/1.png'},new AbortController()),{name:'AbortError'});
});
test('partial map setup failure removes the private source and protocol',()=>{
 const h=harness();h.map.addLayer=()=>{throw new Error('style unavailable')};const control=h.start();assert.equal(h.state(),'unavailable');assert.equal(h.sources.size+h.protocols.size,0);control.dispose();
});
test('overview uses the original coarsest tile at its Mercator corners with a nonoverlapping zoom handoff',()=>{
 const h=harness(),control=h.start();
 const source=h.sources.get(`${LOCAL_REVIEW_SOURCE}-10-1-1`),layer=h.layers.get(`${LOCAL_REVIEW_LAYER}-10-1-1`);
 assert.equal(source.type,'image');assert.match(source.url,/^blob:/);assert.equal(source.coordinates[0][0],1/1024*360-180);assert.equal(source.coordinates[1][0],2/1024*360-180);
 assert.ok(source.coordinates[0][1]>source.coordinates[3][1]);assert.equal(layer.maxzoom,9);assert.equal(h.layers.get(LOCAL_REVIEW_LAYER).minzoom,9);
 assert.equal(layer.paint['raster-resampling'],'nearest');control.setOpacity(.4);assert.equal(layer.paint['raster-opacity'],.4);control.dispose();
});
test('initial review UI exposes local file selection and no activation control or loaded original',async()=>{
 const {createElement}=await import('react'),{renderToStaticMarkup}=await import('react-dom/server');
 let js=ts.transpileModule(await readFile('app/local-geopdf-review-control.tsx','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022,jsx:ts.JsxEmit.ReactJSX}}).outputText;
 const seam=compile('export const loadMapLibre=()=>{throw new Error("renderer must stay unloaded during static render")};');
 for(const [from,to] of [['react',import.meta.resolve('react')],['react/jsx-runtime',import.meta.resolve('react/jsx-runtime')],['./maplibre-seam',seam],['./local-geopdf-review',compile(source)],['./local-geopdf-map',compile(await readFile('app/local-geopdf-map.ts','utf8'))]])js=js.replaceAll(`from "${from}"`,`from "${to}"`);
 const {default:Control}=await import(`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`);
 const html=renderToStaticMarkup(createElement(Control,{map:null,styleReady:false,flatMap:true,onFlatMap(){}}));
 assert.match(html,/Device only/);assert.match(html,/Choose prepared folder/);assert.match(html,/No prepared map loaded/);assert.doesNotMatch(html,/<iframe|<img|blob:|Activate reviewed|Approve/);
});
