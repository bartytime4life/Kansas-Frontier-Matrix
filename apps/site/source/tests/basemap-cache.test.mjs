import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import vm from 'node:vm';
import ts from 'typescript';
import {spawnSync} from 'node:child_process';
const source=await readFile('app/basemap-cache.ts','utf8');
const code=ts.transpileModule(source,{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText;
const url='https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/8/97/58';
const status={schema:'kfm-basemap-cache/v1',limitBytes:10_000_000_000,usedBytes:4096,destination:'/pc/KFM-data/data/work/basemap-cache',sessionToken:'a'.repeat(43),job:{state:'idle'}};
function harness(fetch){const exports={},saved=new Map();vm.runInNewContext(code,{exports,URL,Date,fetch,AbortSignal,DOMException,localStorage:{getItem:k=>saved.get(k),setItem:(k,v)=>saved.set(k,v)}});return exports;}
test('only allowed basemap tiles use the local transport; observation and evidence URLs stay exact',()=>{
 const m=harness();
 for(const u of ['/api/fire?day=2026-10-08','https://gibs.earthdata.nasa.gov/fire/2026-10-08.png','https://nowcoast.noaa.gov/wms?TIME=2026-10-08T12:02:00Z','/earth-engine/2023/1.png','https://tile.openstreetmap.org/8/1/2.png','https://server.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/8/1/2',url+'?TIME=2020',url.replace('https:','http:'),url.replace('nationalmap.gov','nationalmap.gov.evil')]) assert.equal(m.basemapCacheRequest(u,'Tile').url,u);
 assert.match(m.basemapCacheRequest(url,'Tile').url,/^kfm-basemap:/);assert.equal(m.basemapCacheRequest(url,'Source').url,url);
 assert.equal(m.cacheableBasemap('https://tiles.openfreemap.org/planet/20261004_113936_pt/8/2/3.pbf'),true);
});
test('disk hit serves original bytes, direct fallback works, and disabling cache avoids loopback',async()=>{
 const calls=[];let fail=false;
 const m=harness(async u=>{calls.push(u);if(u.endsWith('/status'))return{ok:true,text:async()=>JSON.stringify(status)};if(fail&&u.startsWith('http:'))throw Error('Stopped');return{ok:true,arrayBuffer:async()=>new Uint8Array([1,7,19]).buffer};});
 const request=m.basemapCacheRequest(url,'Tile'),controller=new AbortController();
 assert.deepEqual([...new Uint8Array((await m.basemapCacheProtocol(request,controller)).data)],[1,7,19]);assert.match(calls.at(-1),/127.0.0.1:8770\/resource/);
 fail=true;await m.basemapCacheProtocol(request,controller);assert.equal(calls.at(-1),url);
 m.setBasemapCacheEnabled(false);calls.length=0;await m.basemapCacheProtocol(request,controller);assert.deepEqual(calls,[url]);
});
test('offline companion failure is shared, backs off and preserves cancellation',async()=>{
 const calls=[];const m=harness(async u=>{calls.push(u);if(u.includes('/status'))throw Error('offline');return{ok:true,arrayBuffer:async()=>new ArrayBuffer(2)};});
 await Promise.all([1,2,3].map(()=>m.basemapCacheProtocol(m.basemapCacheRequest(url,'Tile'),new AbortController())));
 assert.equal(calls.filter(x=>x.includes('/status')).length,1);
 const controller=new AbortController();controller.abort();await assert.rejects(m.basemapCacheProtocol(m.basemapCacheRequest(url,'Tile'),controller),{name:'AbortError'});
});
test('every map that supplies the cutaway uses the shared transport without changing styles',async()=>{
 for(const file of ['page.tsx','selected-surface-map.tsx','cutaway-surface-detail.ts','snapshot-map.tsx'])assert.match(await readFile('app/'+file,'utf8'),/transformRequest: basemapCacheRequest/);
 const ui=await readFile('app/basemap-cache-controls.tsx','utf8');for(const label of ['Save Kansas overview','Stop download','10 GB','Display context, not KFM evidence.','Download time is not observation time.'])assert.ok(ui.includes(label));
});
test('local filesystem, eviction, provider and authorization regressions',()=>{
 const r=spawnSync('python3',['tests/basemap_cache_test.py'],{encoding:'utf8'});assert.equal(r.status,0,r.stdout+r.stderr);
});

test('rendered controls connect, toggle, start and cancel the bounded download',async()=>{
 const {componentHarness,findNode,settle}=await import('./component-harness.mjs');let enabled=true,current={...status,tiles:1,hits:2,job:{state:'idle',completed:0,total:0}},interval;
 const actions=[];
 const h=await componentHarness('app/basemap-cache-controls.tsx',{'./basemap-cache':{basemapCacheEnabled:()=>enabled,setBasemapCacheEnabled:v=>{enabled=v},connectBasemapCache:async()=>current,basemapCacheAction:async name=>{actions.push(name);current={...current,job:{state:name==='overview'?'running':'cancelled',completed:1,total:20}};return current}}},{setInterval:fn=>{interval=fn;return 1},clearInterval(){}});
 const draw=()=>h.render(h.exports.BasemapCacheControls,{});draw();h.commit();await settle();let tree=draw();
 const button=label=>findNode(tree,n=>n.type==='button'&&n.props.children===label);
 assert.equal(button('Save Kansas overview').props.disabled,false);
 findNode(tree,n=>n.type==='input').props.onChange({target:{checked:false}});assert.equal(enabled,false);
 button('Save Kansas overview').props.onClick();await settle();tree=draw();assert.equal(button('Save Kansas overview').props.disabled,true);assert.ok(button('Stop download'));
 button('Stop download').props.onClick();await settle();tree=draw();assert.deepEqual(actions,['overview','cancel']);
 current=null;interval();await settle();tree=draw();assert.equal(button('Save Kansas overview').props.disabled,true);assert.match(findNode(tree,n=>n.props?.role==='status').props.children,/unavailable/);h.dispose();
});
