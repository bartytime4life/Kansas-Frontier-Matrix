import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async path=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,id=>{if(id==='react')return{useCallback:f=>f,useEffect(){},useRef:v=>({current:v}),useState:v=>[v,()=>{}]};if(id==='./bounded-json')return{readBoundedJson(){}};throw new Error(id);});return exports;};
const snapshots=await compile('app/reviewed-snapshots.ts');
const layers=await compile('app/reviewed-snapshot-layers.ts');
const id=c=>c.repeat(64);
const product=(over={})=>({state:'available',sourceId:'usgs-streamflow',releaseId:id('a'),evidenceRole:'EXTERNAL_CONTEXT_ONLY',retrievedAt:'2026-10-26T17:05:00Z',bucketAt:'2026-10-26T17:00:00Z',freshness:'current',measurementFreshness:'current',limitation:'Provisional USGS values.',
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
