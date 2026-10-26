import test, {mock} from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async path=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,id=>{if(id==='react')return{useCallback:f=>f,useEffect(){},useRef:v=>({current:v}),useState:v=>[v,()=>{}]};if(id==='./bounded-json')return{readBoundedJson(){}};throw new Error(id);});return exports;};
const snapshots=await compile('app/reviewed-snapshots.ts');
const layers=await compile('app/reviewed-snapshot-layers.ts');
const id=c=>c.repeat(64);
const product=(over={})=>({state:'available',sourceId:'usgs-streamflow',releaseId:id('a'),evidenceRole:'EXTERNAL_CONTEXT_ONLY',retrievedAt:'2026-10-26T17:05:00Z',bucketAt:'2026-10-26T17:00:00Z',approvalExpiresAt:'2099-01-01T00:00:00Z',freshness:'current',measurementFreshness:'current',limitation:'Provisional USGS values.',
 data:{type:'FeatureCollection',features:[{type:'Feature',id:'g1',geometry:{type:'Point',coordinates:[-97.3,38.9]},properties:{stationId:'USGS-06887500',value:1520,unit:'ft^3/s',provisional:true}}]},...over});

test('the release history runs oldest to newest, keeps only signed release ids, and names why it is empty',()=>{
 const parsed=snapshots.parseReviewedHistory({items:[{releaseId:id('b'),publishedAt:'2026-10-26T17:02:00Z'},{releaseId:id('a'),publishedAt:'2026-10-26T15:02:00Z'},{releaseId:'not-a-release',publishedAt:'2026-10-26T16:00:00Z'},{releaseId:id('c'),publishedAt:'never'}]});
 assert.deepEqual(parsed.items.map(i=>i.releaseId),[id('a'),id('b')]);assert.equal(parsed.reason,null);
 assert.equal(snapshots.parseReviewedHistory({items:[],state:'setup-pending'}).reason,'PIPELINE_NOT_CONFIGURED','the pipeline switch is off');
 assert.equal(snapshots.parseReviewedHistory({state:'withheld',reason:'HISTORY_UNAVAILABLE'}).reason,'HISTORY_UNAVAILABLE');
 assert.equal(snapshots.parseReviewedHistory({items:[]}).reason,'NO_APPROVED_RELEASE');
 for(const reason of ['PIPELINE_NOT_CONFIGURED','NO_APPROVED_RELEASE','RELEASE_STORE_UNAVAILABLE','HISTORY_UNAVAILABLE'])assert.ok(snapshots.REVIEWED_REASONS[reason],reason);
});

test('a release is shown only when it is the requested source, context-only and well formed; expired alerts leave the display',()=>{
 const ok=snapshots.parseReviewedProduct(product(),'usgs-streamflow');
 assert.equal(ok.releaseId,id('a'));assert.equal(ok.bucketAt,'2026-10-26T17:00:00Z');assert.equal(ok.data.features.length,1);
 assert.deepEqual(snapshots.parseReviewedProduct({state:'withheld',reason:'NO_APPROVED_RELEASE'},'usgs-streamflow'),{withheld:'NO_APPROVED_RELEASE'});
 for(const bad of [{sourceId:'nws-alerts'},{evidenceRole:'EVIDENCE'},{releaseId:'x'},{bucketAt:'later'},{data:{type:'Feature'}}])
  assert.ok('withheld' in snapshots.parseReviewedProduct(product(bad),'usgs-streamflow'),JSON.stringify(bad));
 const now=Date.parse('2026-10-26T18:00:00Z');
 assert.equal(snapshots.parseReviewedProduct(product({approvalExpiresAt:'2026-10-26T18:30:00Z'}),'usgs-streamflow',now).approvalExpiresAt,'2026-10-26T18:30:00Z','the approval expiry is kept');
 assert.deepEqual(snapshots.parseReviewedProduct(product({approvalExpiresAt:'2026-10-26T18:00:00Z'}),'usgs-streamflow',now),{withheld:'APPROVAL_EXPIRED'},'an expired approval is not shown');
 assert.deepEqual(snapshots.parseReviewedProduct(product({approvalExpiresAt:undefined}),'usgs-streamflow',now),{withheld:'RELEASE_STORE_UNAVAILABLE'},'nor one without an expiry');
 assert.ok(snapshots.REVIEWED_REASONS.APPROVAL_EXPIRED);
 const alerts=snapshots.parseReviewedProduct(product({sourceId:'nws-alerts',data:{type:'FeatureCollection',features:[{type:'Feature',properties:{event:'Flood Warning',severity:'Severe',expired:false}},{type:'Feature',properties:{event:'Wind Advisory',severity:'Minor',expired:true}}]}}),'nws-alerts');
 assert.deepEqual(alerts.data.features.map(f=>f.properties.event),['Flood Warning']);
 assert.deepEqual({...snapshots.REVIEWED_SOURCE_BY_TOPIC},{water:'usgs-streamflow',weather:'nws-alerts',disaster:'nws-alerts'});
});

test('gauge circles grow in area with discharge, provisional values ring amber, alert areas take their NWS severity',()=>{
 const [areas,,gauges]=layers.reviewedLayers();
 const radius=gauges.paint['circle-radius'];
 assert.deepEqual(radius[2],['sqrt',['max',0,['to-number',['get','value'],0]]],'radius follows the square root, so area follows discharge');
 const stops=radius.slice(3);
 assert.deepEqual(stops.filter((_,i)=>i%2===0),[0,100,250],'stops at 0, 10,000 and 62,500 cfs');
 assert.ok(stops.filter((_,i)=>i%2===1).every((r,i,all)=>i===0||r>all[i-1]),'bigger flow, bigger circle');
 assert.deepEqual(gauges.paint['circle-stroke-color'],['case',['==',['get','provisional'],true],'#f2b84b','#f4fbfb']);
 assert.match(JSON.stringify(gauges.filter),/typeof.*value.*number/,'a gauge without a value is not drawn as zero');
 assert.deepEqual(areas.paint['fill-color'].slice(0,2),['match',['get','severity']]);
 assert.deepEqual(layers.NWS_SEVERITY_COLORS.map(([s])=>s),['Extreme','Severe','Moderate','Minor']);
 for(const layer of layers.reviewedLayers())assert.ok(layer.id.startsWith('external-'),'composed with the provider overlays');
});

test('the dock steps through the stored snapshots and says plainly when there are none',async()=>{
 const maps={};new Function('exports',ts.transpileModule(await readFile('app/category-maps.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(maps);
 for(const topic of ['water','weather','disaster'])assert.ok(maps.CATEGORY_MAPS[topic].tools.includes('reviewed'),topic);
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.water,mode:'2d',depth:2.5,azimuth:315,sun:null,sunAvailable:true,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  onReviewed:v=>calls.push(['on',v]),onReviewedIndex:v=>calls.push(['index',v]),onReviewedPlay:v=>calls.push(['play',v])};
 const reviewed={source:'USGS discharge',on:false,loading:false,reason:null,count:0,index:-1,publishedAt:null,capturedFor:null,features:null,freshness:null,playing:false,motionAllowed:true};
 const button=(tree,label)=>findNode(tree,n=>n.type==='button'&&n.props.children===label);
 let tree=h.render(h.exports.CategoryMapDock,{...base,reviewed});
 button(tree,'Reviewed USGS discharge snapshots').props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,reviewed:{...reviewed,on:true,reason:'Reviewed snapshots are not switched on for this site yet.'}});
 assert.match(JSON.stringify(tree),/not switched on for this site yet/);const scrubber=tree=>findNode(tree,n=>n.type==='input'&&n.props['aria-labelledby']==='category-map-dock-reviewed');
 assert.equal(scrubber(tree),undefined,'no scrubber without snapshots');
 tree=h.render(h.exports.CategoryMapDock,{...base,reviewed:{...reviewed,on:true,count:3,index:2,publishedAt:'2026-10-26 17:02 UTC',capturedFor:'2026-10-26 17:00 UTC',features:48,freshness:'current'}});
 assert.match(JSON.stringify(tree),/Snapshot .*3.* of .*3.* captured for .*2026-10-26 17:00 UTC.* published .*2026-10-26 17:02 UTC.*48.*features/);
 scrubber(tree).props.onChange({target:{value:'0'}});
 button(tree,'Play').props.onClick();
 assert.deepEqual(calls,[['on',true],['play',false],['index',0],['play',true]]);
 h.dispose?.();
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/const reviewedSource = categoryMapOnScreen\?\.tools\?\.includes\("reviewed"\) \? REVIEWED_SOURCE_BY_TOPIC\[categoryMapOnScreen\.topic\] \?\? null : null;/);
 assert.match(page,/setReviewedSnapshot\(map, reviewedData\);/);
 const live=await readFile('app/live-context.ts','utf8');
 assert.match(live,/drawReviewedSnapshot\(map\);/,'drawn by the context renderer, so a style reload keeps it');
});

// A minimal hook runtime: state, refs and effects, committed after each render
// and re-rendered while state changes, so the hook runs as it does in React.
function hookRuntime(){
 const slots=[];let cursor=0,dirty=false,pending=[];
 const react={
  useState(init){const k=cursor++;if(!(k in slots))slots[k]={value:init};const slot=slots[k];return [slot.value,next=>{const value=typeof next==='function'?next(slot.value):next;if(!Object.is(value,slot.value)){slot.value=value;dirty=true;}}];},
  useRef(init){const k=cursor++;if(!(k in slots))slots[k]={current:init};return slots[k];},
  useCallback(fn){cursor++;return fn;},
  useEffect(fn,deps){const k=cursor++;const prev=slots[k];if(!prev||deps.some((d,j)=>!Object.is(d,prev.deps[j])))pending.push(()=>{prev?.cleanup?.();slots[k]={deps,cleanup:fn()};});},
 };
 const render=hook=>{for(let n=0;n<50;n++){let out;do{cursor=0;dirty=false;pending=[];out=hook();}while(dirty);const run=pending;pending=[];run.forEach(f=>f());if(!dirty)return out;}throw new Error('render loop');};
 return {react,render};
}

test('the snapshot player waits for each release, withholds one whose approval expires, and follows the history as it is revalidated',async()=>{
 const start=Date.parse('2026-10-26T18:00:00Z');
 mock.timers.enable({apis:['setTimeout','setInterval','Date'],now:start});
 globalThis.window=globalThis;
 try{
  const runtime=hookRuntime();
  const exports={};
  new Function('exports','require',ts.transpileModule(await readFile('app/reviewed-snapshots.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,id=>{if(id==='react')return runtime.react;if(id==='./bounded-json')return{readBoundedJson:response=>response.json()};throw new Error(id);});
  const at=minutes=>new Date(start+minutes*60_000).toISOString();
  let releases=[{releaseId:id('a'),publishedAt:at(-120)},{releaseId:id('b'),publishedAt:at(-60)}];
  const expiry={[id('a')]:at(5),[id('b')]:at(600)};
  const requests=[];
  globalThis.fetch=async url=>{requests.push(url);const release=new URL(url,'http://x').searchParams.get('release');
   return {json:async()=>release?product({releaseId:release,approvalExpiresAt:expiry[release]}):{sourceId:'usgs-streamflow',items:releases}};};
  const flush=async()=>{for(let n=0;n<6;n++)await new Promise(resolve=>setImmediate(resolve));};
  const view=()=>runtime.render(()=>exports.useReviewedSnapshots('usgs-streamflow',true));
  let s=view();
  assert.equal(s.status,'idle');
  s.setOn(true);s=view();
  assert.equal(s.status,'loading','reading the history');
  await flush();s=view();await flush();s=view();
  assert.equal(s.status,'ready');assert.equal(s.index,1,'the newest is shown first');assert.equal(s.product.releaseId,id('b'));

  s.setIndex(0);s=view();
  assert.equal(s.status,'loading','a newly picked release reads as loading until it is drawn');
  assert.equal(s.product.releaseId,id('b'),'the last release drawn stays on the map meanwhile');
  await flush();s=view();
  assert.equal(s.status,'ready');assert.equal(s.product.releaseId,id('a'));

  const historyReads=()=>requests.filter(url=>url.endsWith('/history')).length;
  const before=historyReads();
  mock.timers.tick(5*60_000);s=view();
  assert.equal(s.status,'withheld');assert.equal(s.reason,'APPROVAL_EXPIRED');assert.equal(s.product,null,'an expired release leaves the map at its expiry');
  // The history is read again; the server no longer lists the expired release.
  releases=[releases[1]];
  await flush();s=view();await flush();s=view();
  assert.ok(historyReads()>before,'expiry re-reads the history');
  assert.equal(s.history.length,1);assert.equal(s.index,0);assert.equal(s.status,'ready');assert.equal(s.product.releaseId,id('b'),'falls back to the newest release still approved');

  // A new release published later appears on the next revalidation, and the newest is followed.
  releases=[...releases,{releaseId:id('c'),publishedAt:at(30)}];expiry[id('c')]=at(600);
  mock.timers.tick(exports.REVIEWED_REVALIDATE_MS);s=view();
  await flush();s=view();await flush();s=view();
  assert.equal(s.history.length,2);assert.equal(s.product.releaseId,id('c'));
 }finally{mock.timers.reset();delete globalThis.window;}
});
