import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const load=async path=>{const exports={};new Function('exports',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports);return exports;};
const topics=await load('app/layer-workspaces.ts');
const maps=await load('app/category-maps.ts');
const runtime=await readFile('app/map-runtime.ts','utf8');
const live=await readFile('app/live-context.ts','utf8');
const categoryKeys=await load('app/category-basemap-keys.ts');
const basemapKeys=runtime.match(/export type BasemapKey = ([^;]+);/)[1].split('|').map(part=>part.trim()).flatMap(part=>part==='CategoryBasemapKey'?[...categoryKeys.CATEGORY_BASEMAP_KEYS]:[JSON.parse(part)]);
const officialIds=JSON.parse(`[${live.match(/export type OfficialContextId = ([^;]+);/)[1].replaceAll('|',',')}]`);

test('every start-page category has exactly one map look with a real basemap, scene, camera and starters',()=>{
 const ids=topics.TOPIC_STRUCTURE.map(t=>t.id);
 assert.deepEqual(Object.keys(maps.CATEGORY_MAPS).sort(),[...ids].sort());
 for(const [id,look] of Object.entries(maps.CATEGORY_MAPS)){
  assert.equal(look.topic,id);
  assert.ok(basemapKeys.includes(look.basemap),`${id}: ${look.basemap} is a BASEMAPS key`);
  assert.ok(['2d','terrain','globe'].includes(look.scene),id);
  const {center:[lon,lat],zoom,pitch,bearing}=look.camera;
  assert.ok(lon>-106&&lon<-90&&lat>34&&lat<43,`${id}: camera is over Kansas`);
  assert.ok(zoom>=2&&zoom<=12&&pitch>=0&&pitch<=65&&Math.abs(bearing)<=180,id);
  if(look.scene!=='terrain')assert.equal(pitch,0,`${id}: only 3D looks start tilted`);
  for(const starter of look.starters)assert.ok(officialIds.includes(starter),`${id}: ${starter} is an official context id`);
  assert.equal(look.swatch.length,3);for(const color of look.swatch)assert.match(color,/^#[0-9a-f]{6}$/);
  assert.ok(look.name.length<=24&&look.lede.length<=150,`${id}: copy fits the card and dock`);
 }
 assert.equal(maps.categoryMap('__proto__'),undefined);assert.equal(maps.categoryMap('all'),undefined);
});

test('aviation and government are categories with their own specialized basemaps',()=>{
 const aviation=topics.TOPIC_STRUCTURE.find(t=>t.id==='aviation'),government=topics.TOPIC_STRUCTURE.find(t=>t.id==='government');
 assert.equal(aviation.group,'Built systems');assert.equal(government.group,'People & place');
 assert.match(aviation.limitation,/not for navigation/i);
 assert.equal(government.resources[0].href,'/civic');
 assert.equal(maps.CATEGORY_MAPS.aviation.basemap,'aviation-chart');assert.equal(maps.CATEGORY_MAPS.aviation.scene,'terrain');
 assert.equal(maps.CATEGORY_MAPS.government.basemap,'civic');assert.deepEqual([...maps.CATEGORY_MAPS.government.starters],['census-counties']);
 assert.ok(topics.officialSourceTopics('census-counties').includes('government'));
 assert.equal(topics.restoreTopic('aviation'),'aviation');assert.equal(topics.restoreTopic('government'),'government');
});

test('opening a category map applies its look additively and follows the same category in Layers',async()=>{
 const page=await readFile('app/page.tsx','utf8');
 const body=page.slice(page.indexOf('  const openCategoryMap = (topic: TopicId) => {'),page.indexOf('  const runWelcomeMap ='));
 const order=['activateMapRepresentation(look.scene)','basemapRef.current = look.basemap','setBasemap(look.basemap)','setOfficialContextVisible(id, true)','setOfficialWorkspace(topic)','map.flyTo('];
 let at=-1;for(const step of order){const next=body.indexOf(step);assert.ok(next>at,`${step} follows the previous step`);at=next;}
 assert.doesNotMatch(body,/setOfficialContextVisible\([^)]*false\)|setVisibility\(/,'starters only add; nothing the visitor chose is switched off');
 assert.match(body,/motionDuration\(1800\)/,'camera flight honours reduced motion');
 assert.match(page,/onTopic=\{runWelcomeTopic\} onMap=\{runWelcomeMap\}/);
 assert.match(page,/<CategoryMapDock look=\{activeCategoryMap\} mode=\{categoryMode\}/);
});

test('the dock reflects the view and routes every control to an existing handler',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];const look=maps.CATEGORY_MAPS.aviation;
 const props={look,mode:'terrain',depth:2.5,azimuth:315,terrainAvailable:true,onMode:v=>calls.push(['mode',v]),onDepth:v=>calls.push(['depth',v]),onAzimuth:v=>calls.push(['azimuth',v]),onReset:()=>calls.push(['reset']),onLayers:()=>calls.push(['layers']),onClose:()=>calls.push(['close'])};
 let tree=h.render(h.exports.CategoryMapDock,props);
 const button=label=>findNode(tree,n=>n.type==='button'&&n.props.children===label);
 assert.equal(button('3D').props['aria-pressed'],true);assert.equal(button('2D').props['aria-pressed'],false);
 button('2D').props.onClick();button('Globe').props.onClick();
 const ranges=[];findNode(tree,n=>{if(n.type==='input'&&n.props.type==='range')ranges.push(n);return false;});
 assert.equal(ranges.length,2,'relief and sun in 3D');
 ranges[0].props.onChange({target:{value:'1.5'}});ranges[1].props.onChange({target:{value:'90'}});
 button('Reset view').props.onClick();button('Layers for this map').props.onClick();
 findNode(tree,n=>n.type==='button'&&n.props['aria-label']==='Hide Aviation chart controls').props.onClick();
 assert.deepEqual(calls,[['mode','2d'],['mode','globe'],['depth',1.5],['azimuth',90],['reset'],['layers'],['close']]);
 tree=h.render(h.exports.CategoryMapDock,{...props,mode:'2d',terrainAvailable:false});
 assert.equal(button('3D').props.disabled,true,'3D waits for terrain');
 const flat=[];findNode(tree,n=>{if(n.type==='input'&&n.props.type==='range')flat.push(n);return false;});
 assert.equal(flat.length,1,'no relief slider on a flat map');
 assert.equal(h.exports.azimuthLabel(315),'NW');assert.equal(h.exports.azimuthLabel(-90),'W');assert.equal(h.exports.azimuthLabel(359),'N');
 h.dispose?.();
});
