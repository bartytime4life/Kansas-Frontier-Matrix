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
 const props={look,mode:'terrain',depth:2.5,azimuth:315,sun:null,terrainAvailable:true,onMode:v=>calls.push(['mode',v]),onDepth:v=>calls.push(['depth',v]),onAzimuth:v=>calls.push(['azimuth',v]),onRealSun:v=>calls.push(['sun',v]),onSunTime:v=>calls.push(['time',v]),sunPlaying:false,motionAllowed:true,onSunPlay:v=>calls.push(['play',v]),onReset:()=>calls.push(['reset']),onLayers:()=>calls.push(['layers']),onClose:()=>calls.push(['close'])};
 let tree=h.render(h.exports.CategoryMapDock,props);
 const button=label=>findNode(tree,n=>n.type==='button'&&n.props.children===label);
 assert.equal(button('3D').props['aria-pressed'],true);assert.equal(button('2D').props['aria-pressed'],false);
 button('2D').props.onClick();button('Globe').props.onClick();
 const ranges=[];findNode(tree,n=>{if(n.type==='input'&&n.props.type==='range')ranges.push(n);return false;});
 assert.equal(ranges.length,2,'relief and sun in 3D');
 ranges[0].props.onChange({target:{value:'1.5'}});ranges[1].props.onChange({target:{value:'90'}});
 button('Reset view').props.onClick();button('Layers for this map').props.onClick();
 assert.equal(button('Use the real sun now').props['aria-pressed'],false);button('Use the real sun now').props.onClick();
 findNode(tree,n=>n.type==='button'&&n.props['aria-label']==='Hide Aviation chart controls').props.onClick();
 assert.deepEqual(calls,[['mode','2d'],['mode','globe'],['depth',1.5],['azimuth',90],['reset'],['layers'],['sun',true],['close']]);
 // Following the computed sun, the hand-set slider would be a dead control: it gives way to the reading.
 const at=Date.UTC(2026,5,21,21,0);
 const sunLight={preset:'clear',azimuth:245,altitude:52,source:'sun',solarElevation:52.4};
 tree=h.render(h.exports.CategoryMapDock,{...props,sun:{light:sunLight,at,dayFraction:16/24,live:true}});
 const sunRanges=[];findNode(tree,n=>{if(n.type==='input'&&n.props.type==='range')sunRanges.push(n);return false;});
 assert.equal(sunRanges.length,2,'relief, then the time of day in place of the hand-set direction');
 const timeOfDay=sunRanges[1];
 assert.equal(timeOfDay.props['aria-labelledby'],'category-map-dock-sun-time');
 assert.equal(timeOfDay.props.value,64,'quarter-hour steps: 4 PM is step 64 of 96');
 assert.equal(timeOfDay.props.max,95,'the last step is 11:45 PM, never tomorrow\'s midnight');
 const lateTree=h.render(h.exports.CategoryMapDock,{...props,sun:{light:sunLight,at,dayFraction:1,live:false}});
 const late=[];findNode(lateTree,n=>{if(n.type==='input'&&n.props.type==='range')late.push(n);return false;});
 assert.equal(late[1].props.value,95,'a fraction at the day edge stays on the last step');
 assert.equal(button('Now').props.disabled,true,'already following the clock');
 timeOfDay.props.onChange({target:{value:'30'}});assert.deepEqual(calls.at(-1),['time',30/96]);
 assert.match(JSON.stringify(findNode(tree,n=>n.props?.className==='category-map-dock-sun-reading')),/Real sun/);
 tree=h.render(h.exports.CategoryMapDock,{...props,sun:{light:sunLight,at,dayFraction:16/24,live:false}});
 assert.match(JSON.stringify(findNode(tree,n=>n.props?.className==='category-map-dock-sun-reading')),/Sun at/,'a study time is never shown as the live sun');
 button('Now').props.onClick();assert.deepEqual(calls.at(-1),['time',null]);
 // Play the day sweeps the study forward; reduced motion leaves only the slider.
 assert.equal(button('Play the day').props['aria-pressed'],false);button('Play the day').props.onClick();assert.deepEqual(calls.at(-1),['play',true]);
 tree=h.render(h.exports.CategoryMapDock,{...props,sun:{light:sunLight,at,dayFraction:16/24,live:false},sunPlaying:true});
 assert.equal(button('Pause').props['aria-pressed'],true);button('Pause').props.onClick();assert.deepEqual(calls.at(-1),['play',false]);
 tree=h.render(h.exports.CategoryMapDock,{...props,sun:{light:sunLight,at,dayFraction:16/24,live:false},sunPlaying:true,motionAllowed:false});
 assert.equal(button('Play the day').props.disabled,true,'no time-lapse under reduced motion');assert.equal(button('Play the day').props['aria-pressed'],false);
 assert.equal(h.exports.nextSunStep(0),1/96);assert.equal(h.exports.nextSunStep(64/96),65/96);
 assert.equal(h.exports.nextSunStep(64.5/96),65/96,'a time between steps moves to the next quarter hour');
 assert.equal(h.exports.nextSunStep(94/96),95/96);assert.equal(h.exports.nextSunStep(95/96),null,'playback stops at 11:45 PM');assert.equal(h.exports.nextSunStep(1),null);
 assert.equal(h.exports.SUN_PLAY_RESTART_STEP/h.exports.SUN_TIME_STEPS*24,5,'a played-out day restarts at 5:00 AM');
 assert.match(JSON.stringify(findNode(tree,n=>n.props?.className==='category-map-dock-sun-reading')),/52° up, from SW · 4:00\u202fPM CDT|52° up, from SW · 4:00 PM CDT/);
 assert.equal(button('Set light by hand').props['aria-pressed'],true);button('Set light by hand').props.onClick();
 assert.deepEqual(calls.at(-1),['sun',false]);
 assert.match(h.exports.sunReading({preset:'night',azimuth:60,altitude:35,source:'moon',solarElevation:-20},at),/^Below the horizon · night fill · /);
 tree=h.render(h.exports.CategoryMapDock,{...props,mode:'globe'});
 assert.equal(button('Use the real sun now'),undefined,'no light controls on the globe');
 tree=h.render(h.exports.CategoryMapDock,{...props,mode:'2d',terrainAvailable:false});
 assert.equal(button('3D').props.disabled,true,'3D waits for terrain');
 const flat=[];findNode(tree,n=>{if(n.type==='input'&&n.props.type==='range')flat.push(n);return false;});
 assert.equal(flat.length,1,'no relief slider on a flat map');
 assert.equal(h.exports.azimuthLabel(315),'NW');assert.equal(h.exports.azimuthLabel(-90),'W');assert.equal(h.exports.azimuthLabel(359),'N');
 h.dispose?.();
});

test('relief looks offer a cross-section through the existing terrain investigation',async()=>{
 const withTransect=Object.entries(maps.CATEGORY_MAPS).filter(([,look])=>look.tools?.includes('transect')).map(([id])=>id).sort();
 assert.deepEqual(withTransect,['engineering','geology','terrain']);
 for(const id of withTransect)assert.equal(maps.CATEGORY_MAPS[id].scene,'terrain',`${id}: a cross-section is offered on 3D relief looks`);
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];const base={mode:'terrain',depth:2.5,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onTransect:()=>calls.push('transect'),onReset(){},onLayers(){},onClose(){}};
 const tool=tree=>findNode(tree,n=>n.type==='button'&&n.props.children==='Draw a cross-section');
 let tree=h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.terrain});
 tool(tree).props.onClick();assert.deepEqual(calls,['transect']);assert.equal(tool(tree).props.disabled,false);
 tree=h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.terrain,terrainAvailable:false});
 assert.equal(tool(tree).props.disabled,true,'the transect samples the 3D terrain, so it waits for it');
 tree=h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.aviation});
 assert.equal(tool(tree),undefined,'looks without the tool show no button');
 h.dispose?.();
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/onTransect=\{startCategoryTransect\}/);
 const start=page.slice(page.indexOf('  const startCategoryTransect = () => {'),page.indexOf('  const toggleTopographicHeightOverlay ='));
 assert.match(start,/startTerrainInvestigation\(\);\s*window\.requestAnimationFrame\(\(\) => \{\s*const steps = document\.querySelector<HTMLElement>\("\.map-utility-panel \.terrain-investigation"\);\s*steps\?\.closest\("details"\)\?\.setAttribute\("open", ""\);\s*steps\?\.scrollIntoView\(\{ behavior: reducedMotion \? "auto" : "smooth", block: "start" \}\);/,'the dock reuses the existing investigation, opens its collapsed section and brings its steps into view');
 assert.match(page,/<details className="explorer-secondary"><summary>Terrain tools, sources &amp; rendering<\/summary>[\s\S]{0,9000}?className="terrain-investigation"/,'the steps live in that uncontrolled section');
});

test('the Layers topic guide shows the category map look and opens it only when it is not on',async()=>{
 const h=await componentHarness('app/topic-navigation.tsx',{'next/link':{default:'a'},'./layer-workspaces':topics},{URLSearchParams});
 const look=maps.CATEGORY_MAPS.aviation;let opened=0;
 const mapLook={name:look.name,lede:look.lede,sceneLabel:maps.categorySceneLabel(look.scene),swatch:look.swatch,active:false};
 let tree=h.render(h.exports.TopicGuide,{value:'aviation',mapLook,onOpenMap:()=>opened++});
 const card=findNode(tree,n=>n.props?.className==='topic-map-look');
 assert.ok(card);assert.match(JSON.stringify(card),/Aviation chart/);assert.match(JSON.stringify(card),/3D terrain/);
 findNode(tree,n=>n.type==='button'&&n.props.children==='Open this map').props.onClick();assert.equal(opened,1);
 tree=h.render(h.exports.TopicGuide,{value:'aviation',mapLook:{...mapLook,active:true},onOpenMap:()=>opened++});
 assert.equal(findNode(tree,n=>n.type==='button'&&n.props.children==='Open this map'),undefined,'no button once the look is on');
 assert.match(JSON.stringify(findNode(tree,n=>n.props?.className==='topic-map-look')),/on the map now/);
 tree=h.render(h.exports.TopicGuide,{value:'aviation'});
 assert.equal(findNode(tree,n=>n.props?.className==='topic-map-look'),undefined,'callers without a look render the guide as before');
 h.dispose?.();
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/<TopicGuide value=\{officialWorkspace\}[\s\S]{0,200}?mapLook=\{activeCategoryMap \? \{ name: activeCategoryMap\.name[\s\S]{0,300}?active: activeCategoryMap\.basemap === basemap \} : null\}/);
 assert.match(page,/onOpenMap=\{activeCategoryMap \? \(\) => openCategoryMap\(activeCategoryMap\.topic\) : undefined\}/);
});

test('each look can open under its own light, applied as atmosphere and sun only',async()=>{
 const studio=await readFile('app/scene-studio.ts','utf8');
 const recipes=[...studio.matchAll(/^  (\w+): \{ label:/gm)].map(m=>m[1]);
 assert.deepEqual(recipes,['daylight','golden','blue','survey']);
 for(const [id,look] of Object.entries(maps.CATEGORY_MAPS))if(look.light!==undefined)assert.ok(recipes.includes(look.light),`${id}: ${look.light} is a scene recipe`);
 assert.equal(maps.CATEGORY_MAPS.terrain.light,'golden','relief under a raking sun');
 assert.equal(maps.CATEGORY_MAPS.weather.light,'blue','weather on a dark sky');
 const page=await readFile('app/page.tsx','utf8');
 const open=page.slice(page.indexOf('  const openCategoryMap = (topic: TopicId) => {'),page.indexOf('  const runWelcomeMap ='));
 assert.match(open,/if \(look\.light\) applyCategoryLight\(look\.light\);/);
 assert.ok(open.indexOf('applyCategoryLight')>open.indexOf('activateMapRepresentation(look.scene)')&&open.indexOf('applyCategoryLight')>open.indexOf('basemapRef.current = look.basemap'),'the look light wins over the representation default and sees the new basemap');
 assert.doesNotMatch(open,/updateSceneEffects|chooseSceneRecipe|sceneRecipePresentation/,'effect settings the visitor chose are never rewritten');
 const helper=page.slice(page.indexOf('  const applyCategoryLight = (recipe: SceneRecipe) => {'),page.indexOf('  const openCategoryMap = (topic: TopicId) => {'));
 assert.match(helper,/changeStudioLight\(\{ atmosphere, azimuth \}\);/,'state follows the look');
 assert.match(helper,/runMapMutation\("Category light", \(\) => \{\s*applySceneEnvironment\(map, atmosphere, azimuth\);/,'and the map is lit now, even when state was already equal');
 assert.match(helper,/syncSceneOverlays\(map, atmosphere, azimuth, renderEfficientRef\.current\)/,'basemap hillshade re-aims too');
 assert.doesNotMatch(helper,/updateSceneEffects/);
 assert.match(page,/sun=\{sceneEffects\.sunSync \? \{ light: sunSceneLight\(sunAt, view\.center\[0\], view\.center\[1\]\), at: sunAt,/,'the dock reads the same computed sun as the renderer');
 assert.match(page,/const sunAt = sunStudyAt \?\? sunClock;/);
 assert.match(page,/registerSceneEffects\(map, sceneEffects\);\s*registerSunInstant\(map, sunStudyAt\);/,'the renderer lights the study time');
 assert.equal((page.match(/light=\{sceneEffects\.sunSync \? sunSceneLight\(sunAt,/g)||[]).length,2,'the Scene studio reads the same instant');
 assert.match(page,/onRealSun=\{\(sunSync\) => updateSceneEffects\(\{ \.\.\.sceneEffectsRef\.current, sunSync \}\)\}/,'only the visitor turns the real sun on or off');
 const update=page.slice(page.indexOf('  const updateSceneEffects = (next: SceneEffectSettings) => {'),page.indexOf('  const playSunDay ='));
 assert.match(update,/if \(next\.sunSync !== sceneEffectsRef\.current\.sunSync\) \{ setSunStudyAt\(null\); setSunPlaying\(false\); \}\s*sceneEffectsRef\.current = next;/,'every control that turns the real sun on or off (dock, Scene studio, recipes, looks) ends a study and its playback, read before the ref moves on');
 const play=page.slice(page.indexOf('  // Play the day runs only while its controls are on screen'),page.indexOf('}, [reducedMotion, sceneEffects.sunSync, sunAt, sunControlsShown, sunPlaying]);')+80);
 assert.ok(page.indexOf('  const showCategoryDock = Boolean(')<page.indexOf('  const sunControlsShown ='),'playback reads the dock visibility computed just above it');
 assert.match(play,/const sunControlsShown = showCategoryDock && categoryMode !== "globe";\s*if \(sunPlaying && !sunControlsShown\) setSunPlaying\(false\);/,'clearing the topic, hiding the dock, opening the guide or going to the globe stops playback');
 assert.match(play,/if \(!sunPlaying \|\| !sunControlsShown \|\| !sceneEffects\.sunSync \|\| reducedMotion\) return;/,'playback only runs while its controls are shown, following the sun, with motion allowed');
 assert.match(play,/window\.setTimeout\([\s\S]*?if \(next === null\) setSunPlaying\(false\);\s*else setSunStudyAt\(instantAtIntervalFraction\(day, next\)\);[\s\S]*?SUN_PLAY_STEP_MS\);\s*return \(\) => window\.clearTimeout\(timer\);/,'one step per timer, cleared on every change, stopping at the last step');
 assert.match(page,/onSunTime=\{\(fraction\) => \{ setSunPlaying\(false\);/,'moving Time or pressing Now stops playback');
 assert.match(page,/onClose=\{\(\) => setCategoryDockHidden\(true\)\}/,'hiding the dock stops playback through sunControlsShown');
 assert.match(page,/motionAllowed=\{!reducedMotion\}/);
 assert.equal((page.match(/setSceneEffects\(/g)||[]).length,2,'settings change only in updateSceneEffects and the stored-settings restore');
 const reset=page.slice(page.indexOf('  const resetCategoryView = () => {'),page.indexOf('announce(`${activeCategoryMap.name} view reset`)'));
 assert.match(reset,/if \(activeCategoryMap\.light\) applyCategoryLight\(activeCategoryMap\.light\);/,'Reset view restores the look light too');
});
