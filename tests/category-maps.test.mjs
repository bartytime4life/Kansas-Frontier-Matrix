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
 assert.equal(maps.CATEGORY_MAPS.government.basemap,'civic');assert.deepEqual([...maps.CATEGORY_MAPS.government.starters],['census-congress-119']);
 assert.ok(topics.officialSourceTopics('census-counties').includes('government'));
 // A lede promises only what the map draws: county lines come from the civic base or the Census starter.
 for(const [id,look] of Object.entries(maps.CATEGORY_MAPS))if(look.basemap!=='civic'&&!look.starters.includes('census-counties'))assert.doesNotMatch(look.lede,/count(y|ies)/i,`${id}: no county lines on this map`);
 // Fire starts off everywhere and is a Hazard watch layer: its detections and reports are that map's starters.
 assert.deepEqual([...maps.CATEGORY_MAPS.disaster.starters],['nws-alerts','nasa-gibs-fire-points','nifc-fire-reports']);
 for(const id of ['nasa-gibs-fire-points','nifc-fire-reports'])assert.ok(topics.officialSourceTopics(id).includes('disaster'),`${id} is listed under Hazards`);
 assert.equal(topics.restoreTopic('aviation'),'aviation');assert.equal(topics.restoreTopic('government'),'government');
});

test('opening a category map opens on its own subject and follows the same category in Layers',async()=>{
 const page=await readFile('app/page.tsx','utf8');
 const body=page.slice(page.indexOf('  const openCategoryMap = (topic: TopicId) => {'),page.indexOf('  const runWelcomeMap ='));
 const order=['activateMapRepresentation(look.scene)','basemapRef.current = look.basemap','setBasemap(look.basemap)','setOfficialContextVisible(source.id, on)','setOfficialWorkspace(topic)','map.flyTo('];
 let at=-1;for(const step of order){const next=body.indexOf(step);assert.ok(next>at,`${step} follows the previous step`);at=next;}
 assert.match(body,/for \(const source of OFFICIAL_CONTEXT_SOURCES\) \{\s*const on = look\.starters\.includes\(source\.id\);\s*if \(on \|\| officialVisibilityRef\.current\[source\.id\]\) setOfficialContextVisible\(source\.id, on\);/,'only the look\'s starters are on, as a starter set does; untouched layers are not toggled');
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

test('the water map toggles the flowing-water effect from its dock and reports what it drew',async()=>{
 const withFlow=Object.entries(maps.CATEGORY_MAPS).filter(([,look])=>look.tools?.includes('flow')).map(([id])=>id);
 assert.deepEqual(withFlow,['water']);
 assert.ok(maps.CATEGORY_MAPS.water.starters.includes('usgs-streamflow'),'the gauges that light reaches are a starter of the same look');
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];const base={look:maps.CATEGORY_MAPS.water,mode:'2d',depth:2.5,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onTransect(){},onFlow:v=>calls.push(v),onReset(){},onLayers(){},onClose(){}};
 const button=(tree,label)=>findNode(tree,n=>n.type==='button'&&n.props.children===label);
 const reading=tree=>findNode(tree,n=>n.props?.className==='category-map-dock-reading');
 let tree=h.render(h.exports.CategoryMapDock,{...base,flow:{on:false,reading:null,still:null}});
 assert.equal(button(tree,'Show river flow').props['aria-pressed'],false);assert.equal(reading(tree),undefined);
 button(tree,'Show river flow').props.onClick();assert.deepEqual(calls,[true]);
 tree=h.render(h.exports.CategoryMapDock,{...base,flow:{on:true,reading:'1,204 reaches with a USGS flow direction · 12 lit by a gauge reading',still:null}});
 assert.match(JSON.stringify(reading(tree)),/1,204 reaches with a USGS flow direction · 12 lit by a gauge reading"/);
 button(tree,'Hide river flow').props.onClick();assert.deepEqual(calls,[true,false]);
 tree=h.render(h.exports.CategoryMapDock,{...base,flow:{on:true,reading:null,still:'reduced motion'}});
 assert.match(JSON.stringify(reading(tree)),/Starting river flow….*drawn still: .*reduced motion/,'the dock names why the rivers hold still');
 tree=h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.terrain,flow:{on:false,reading:null,still:null}});
 assert.equal(button(tree,'Show river flow'),undefined,'looks without the tool show no toggle');
 h.dispose?.();
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/flow=\{\{ on: sceneEffects\.waterFlow, reading: sceneReadings\.waterFlow, still: runtime\.kind === "degraded" \? "the map is degraded" : runtime\.kind !== "ready" \? "the map is still starting" : reducedMotion \? "reduced motion" : !dynamicEffects \? "ambient motion is off" : browserRenderBudget\(renderQuality\)\.efficient \? "efficient rendering" : null \}\}/,'the dock names each condition of the water animation\'s motion rule');
 assert.match(page,/onFlow=\{\(waterFlow\) => updateSceneEffects\(\{ \.\.\.sceneEffectsRef\.current, waterFlow \}\)\}/,'only the visitor turns it on or off, through the shared settings path');
 assert.match(page,/const flowing = motionAllowed && sceneEffects\.waterFlow;/);
 assert.match(page,/const motionAllowed = runtime\.kind === "ready" && dynamicEffects && !reducedMotion && !browserRenderBudget\(renderQuality\)\.efficient;/,'same rule as the dock reading');
});

test('the aquifer and geology maps open Underground from their dock through the guide\'s own entry',async()=>{
 const withUnderground=Object.entries(maps.CATEGORY_MAPS).filter(([,look])=>look.tools?.includes('underground')).map(([id])=>id).sort();
 assert.deepEqual(withUnderground,['geology','groundwater']);
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];const base={mode:'2d',depth:2.5,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onTransect(){},onUnderground:()=>calls.push('underground'),onReset(){},onLayers(){},onClose(){}};
 const tool=tree=>findNode(tree,n=>n.type==='button'&&n.props.children==='Explore underground');
 let tree=h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.groundwater});
 tool(tree).props.onClick();assert.deepEqual(calls,['underground']);
 tree=h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.geology,mode:'terrain'});
 assert.ok(tool(tree),'geology offers it beside the cross-section');
 assert.ok(findNode(tree,n=>n.type==='button'&&n.props.children==='Draw a cross-section'));
 tree=h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.water});
 assert.equal(tool(tree),undefined,'looks without the tool show no button');
 h.dispose?.();
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/onUnderground=\{enterUnderground\}/);
 assert.match(page,/const enterUnderground = \(\) => \{\s*if \(primaryWorkspace !== "map" \|\| !undergroundOpen\) toggleUnderground\(\);\s*setUndergroundFocusRequest\(\(request\) => request \+ 1\);\s*\};/,'opens Underground or keeps it open, then moves focus into it');
 assert.match(page,/else if \(action === "underground"\) enterUnderground\(\);/,'the guide uses the same entry');
 assert.match(page,/const showCategoryDock = Boolean\([^;]*!undergroundOpen/,'the dock steps aside while Underground is open');
});

test('Sky and Science show the calculated day and night from their dock, at the current time',async()=>{
 const withDaylight=Object.entries(maps.CATEGORY_MAPS).filter(([,look])=>look.tools?.includes('daylight')).map(([id])=>id).sort();
 assert.deepEqual(withDaylight,['science','sky']);
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];const base={look:maps.CATEGORY_MAPS.sky,mode:'globe',depth:2.5,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onDaylight:v=>calls.push(['show',v]),onDaylightPlay:v=>calls.push(['play',v]),onReset(){},onLayers(){},onClose(){}};
 const button=(tree,label)=>findNode(tree,n=>n.type==='button'&&n.props.children===label);
 const reading=tree=>findNode(tree,n=>n.props?.className==='category-map-dock-reading');
 const daylight={on:false,playing:false,time:'Mon, Oct 26, 3:42:10 PM CDT',reading:'Kansas center: Sun 31° up · daylight'};
 let tree=h.render(h.exports.CategoryMapDock,{...base,daylight});
 assert.equal(button(tree,'Show day and night').props['aria-pressed'],false);
 assert.equal(reading(tree),undefined);assert.equal(button(tree,'Play day and night'),undefined,'no clock until the layer is shown');
 button(tree,'Show day and night').props.onClick();assert.deepEqual(calls,[['show',true]]);
 tree=h.render(h.exports.CategoryMapDock,{...base,daylight:{...daylight,on:true}});
 assert.match(JSON.stringify(reading(tree)),/3:42:10 PM CDT.*Kansas center: Sun 31° up · daylight/);
 assert.equal(reading(tree).props['aria-live'],'polite');
 button(tree,'Play day and night').props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,daylight:{...daylight,on:true,playing:true}});
 assert.equal(reading(tree).props['aria-live'],'off','a running clock is not read out every frame');
 button(tree,'Pause day and night').props.onClick();
 button(tree,'Hide day and night').props.onClick();
 assert.deepEqual(calls,[['show',true],['play',true],['play',false],['show',false]]);
 tree=h.render(h.exports.CategoryMapDock,{...base,motionAllowed:false,daylight:{...daylight,on:true,playing:true}});
 assert.equal(button(tree,'Play day and night').props.disabled,true,'reduced motion keeps the clock still');
 tree=h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.water,mode:'2d',daylight});
 assert.equal(button(tree,'Show day and night'),undefined,'looks without the tool show no toggle');
 h.dispose?.();
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/onDaylight=\{showCategoryDaylight\} onDaylightPlay=\{setDaylightPlayback\}/);
 assert.match(page,/daylight=\{activeCategoryMap\.tools\?\.includes\("daylight"\) \? \{ on: daylightEnabled, playing: daylightPlaying, time: daylightDisplayTime\.central,\s*reading: `Kansas center: \$\{daylightPhaseReading\(solarReferenceElevation\(daylightInstant, activeCategoryMap\.camera\.center\[1\], activeCategoryMap\.camera\.center\[0\]\)\)\}` \} : undefined\}/,'the reading uses the layer\'s own clock at the look\'s center');
 const show=page.slice(page.indexOf('  const showCategoryDaylight = (on: boolean) => {'),page.indexOf('  // From the category dock the investigation'));
 assert.match(show,/toggleDaylightVisibility\(on\);\s*if \(!on\) return;/,'the layer card\'s own switch path');
 assert.match(show,/if \(now >= interval\.startMs && now < interval\.endMs\) seekDaylight\(intervalFractionAtInstant\(now, interval\)\);/,'it opens on the current time when the chosen range holds it');
});

test('the field and survey maps start a polygon measurement from their dock',async()=>{
 const withArea=Object.entries(maps.CATEGORY_MAPS).filter(([,look])=>look.tools?.includes('area')).map(([id])=>id).sort();
 assert.deepEqual(withArea,['agriculture','land']);
 const h=await componentHarness('app/category-map-dock.tsx',{});
 let calls=0;const base={look:maps.CATEGORY_MAPS.agriculture,mode:'2d',depth:2.5,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onMeasureArea:()=>calls++,onReset(){},onLayers(){},onClose(){}};
 const tool=tree=>findNode(tree,n=>n.type==='button'&&n.props.className==='category-map-dock-tool');
 let tree=h.render(h.exports.CategoryMapDock,{...base,measuringArea:false});
 assert.equal(tool(tree).props.children,'Measure an area');assert.equal(tool(tree).props['aria-pressed'],false);
 tool(tree).props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.land,measuringArea:true});
 assert.equal(tool(tree).props.children,'Cancel area');assert.equal(tool(tree).props['aria-pressed'],true);
 tool(tree).props.onClick();assert.equal(calls,2,'the same handler starts and cancels, as the Map menu\'s Polygon does');
 tree=h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.water});
 assert.equal(findNode(tree,n=>n.type==='button'&&n.props.children==='Measure an area'),undefined,'looks without the tool show no button');
 h.dispose?.();
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/measuringArea=\{measureMode === "area"\} onMeasureArea=\{\(\) => beginMapMeasurement\("area"\)\}/,'the Map menu\'s own Polygon entry');
 const css=await readFile('app/category-map-dock.css','utf8');
 assert.match(css,/\.map-stage:has\(\.measurement-readout\) \.category-map-dock\{bottom:calc\(76px/,'the dock lifts above the readout along the bottom edge');
 assert.match(css,/@media\(max-width:760px\)\{\.map-stage:has\(\.measurement-readout\) \.category-map-dock\{display:none\}\}/,'on a phone it steps aside so the map can be tapped');
});

test('the storm desk opens and closes the live radar loop from its dock, clear of the loop panel',async()=>{
 const withRadar=Object.entries(maps.CATEGORY_MAPS).filter(([,look])=>look.tools?.includes('radar')).map(([id])=>id);
 assert.deepEqual(withRadar,['weather']);
 assert.ok(maps.CATEGORY_MAPS.weather.starters.includes('nws-radar'));
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];const base={look:maps.CATEGORY_MAPS.weather,mode:'2d',depth:2.5,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onRadar:v=>calls.push(v),onReset(){},onLayers(){},onClose(){}};
 const tool=tree=>findNode(tree,n=>n.type==='button'&&n.props.className==='category-map-dock-tool');
 let tree=h.render(h.exports.CategoryMapDock,{...base,radar:{watching:false,available:true}});
 assert.equal(tool(tree).props.children,'Watch the radar loop');tool(tree).props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,radar:{watching:true,available:true}});
 assert.equal(tool(tree).props.children,'Close radar loop');assert.equal(tool(tree).props['aria-pressed'],true);tool(tree).props.onClick();
 assert.deepEqual(calls,[true,false]);
 tree=h.render(h.exports.CategoryMapDock,{...base,radar:{watching:false,available:false}});
 assert.equal(tool(tree).props.disabled,true,'the live loop waits for the present map time');
 h.dispose?.();
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/const watchRadarLoop = \(\) => \{ setOfficialContextVisible\("nws-radar", true\); setLiveInstrument\("radar"\); setInstrumentOpen\(true\); \};/);
 assert.match(page,/<button type="button" onClick=\{watchRadarLoop\}>Watch live loop<\/button>/,'the radar card shares the same entry');
 assert.match(page,/radar=\{\{ watching: liveDockVisible && showRadarDock, available: buildYearCurrent && temporalQuery\.frame === OFFICIAL_CONTEXT_PRESENT_FRAME \}\}\s*onRadar=\{\(watch\) => watch \? watchRadarLoop\(\) : closeLiveInstrument\(\)\}/);
 const css=await readFile('app/category-map-dock.css','utf8');
 assert.match(css,/\.map-stage\[data-live-dock="true"\] \.category-map-dock\{bottom:calc\(var\(--live-dock-clearance\) \+ 6px\)/,'the dock sits above the radar and lightning panels');
 assert.match(css,/@media\(max-width:760px\)\{\.map-stage\[data-live-dock="true"\] \.category-map-dock\{display:none\}\}/,'on a phone the loop panel has the bottom of the map to itself');
 assert.match(page,/className="noaa-radar-close" onClick=\{closeLiveInstrument\} aria-label="Close radar loop controls"/,'so the radar panel closes itself, giving the dock back on a phone');
 assert.match(css,/@media\(max-width:760px\)\{\.category-map-dock\{[^}]*max-height:calc\(100% - 152px - env\(safe-area-inset-bottom,0px\)\)/,'a tall dock stops below the map information button');
 assert.match(css,/\.category-map-dock-modes button\[aria-pressed=true\]:disabled\{color:#f1e6c2;/,'a requested but unavailable mode keeps a readable label');
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
 assert.deepEqual([...maps.CATEGORY_MAPS.terrain.starters],[],'the relief basemap is lit by the scene sun; no fixed-light provider hillshade over it');
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
 assert.match(play,/const sunControlsShown = showCategoryDock && categoryMode !== "globe" && categorySunAvailable;\s*if \(sunPlaying && !sunControlsShown\) setSunPlaying\(false\);/,'clearing the topic, hiding the dock, opening the guide, going to the globe or to a base without shading stops playback');
 assert.match(play,/if \(!sunPlaying \|\| !sunControlsShown \|\| !sceneEffects\.sunSync \|\| reducedMotion\) return;/,'playback only runs while its controls are shown, following the sun, with motion allowed');
 assert.match(play,/window\.setTimeout\([\s\S]*?if \(next === null\) setSunPlaying\(false\);\s*else setSunStudyAt\(instantAtIntervalFraction\(day, next\)\);[\s\S]*?SUN_PLAY_STEP_MS\);\s*return \(\) => window\.clearTimeout\(timer\);/,'one step per timer, cleared on every change, stopping at the last step');
 assert.match(page,/onSunTime=\{\(fraction\) => \{ setSunPlaying\(false\);/,'moving Time or pressing Now stops playback');
 assert.match(page,/onClose=\{\(\) => setCategoryDockHidden\(true\)\}/,'hiding the dock stops playback through sunControlsShown');
 assert.match(page,/motionAllowed=\{!reducedMotion\}/);
 assert.equal((page.match(/setSceneEffects\(/g)||[]).length,3,'only explicit controls, stored restore and the narrow river-flow navigation reset write settings');
 assert.match(page,/sceneEffectsForTopic\(sceneEffectsRef.current, officialWorkspace\)/,'navigation uses the water-only preference reset, not category lighting');
 const reset=page.slice(page.indexOf('  const resetCategoryView = () => {'),page.indexOf('announce(`${activeCategoryMap.name} view reset`)'));
 assert.match(reset,/if \(activeCategoryMap\.light\) applyCategoryLight\(activeCategoryMap\.light\);/,'Reset view restores the look light too');
});

test('the review fixes: a hint per map, sun controls only where the light shows, the open map named in the status bar',async()=>{
 for(const [id,look] of Object.entries(maps.CATEGORY_MAPS))assert.ok(look.tip&&look.tip.length<=110,`${id}: one short hint for the tip strip`);
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const base={look:maps.CATEGORY_MAPS.agriculture,mode:'2d',depth:2.5,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){}};
 const sunControls=tree=>JSON.stringify(tree).match(/Sun from|Use the real sun now/g)??[];
 assert.equal(sunControls(h.render(h.exports.CategoryMapDock,base)).length,2,'shown by default');
 assert.deepEqual(sunControls(h.render(h.exports.CategoryMapDock,{...base,sunAvailable:false})),[],'flat imagery has no shading for the light to move');
 h.dispose?.();
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/const categorySunAvailable = categoryMode === "terrain" \|\| isCategoryBasemapKey\(basemap\);/);
 assert.match(page,/const sunControlsShown = showCategoryDock && categoryMode !== "globe" && categorySunAvailable;/,'Play the day stops where the controls are not shown');
 assert.match(page,/<b>\{categoryMapOnScreen\?\.name \?\? activeAtlasView\?\.title \?\? "Kansas Overview"\}<\/b>/,'the status bar names the open map, not a view guessed from the basemap');
 assert.match(page,/hint=\{categoryMapOnScreen && primaryWorkspace === "map" \? \{ title: categoryMapOnScreen\.name, text: categoryMapOnScreen\.tip \} : null\}/);
 // Short landscape screens hide the tips' trailing arrow (the third span); a hint has two spans, title and text.
 const css=await readFile('app/globals.css','utf8');
 assert.doesNotMatch(css,/\.welcome-feature-item>span:last-child\{display:none\}/,'a hint\'s text is its last span and must stay visible');
 assert.match(css,/\.welcome-feature-item>span:nth-child\(3\)\{display:none\}/);
 assert.match(page,/styleDocumentLoadedRef\.current = true;\s*\/\/[^\n]*\n(?:\s*\/\/[^\n]*\n)*\s*styleFallbackAttempted = false;/,'a loaded style re-arms the basemap fallback, so a second outage falls back instead of failing the map');
});

test('the Field view shows NASA soil moisture at a chosen depth, names the day drawn, and keeps it to the maps that offer it',async()=>{
 assert.deepEqual([...maps.CATEGORY_MAPS.agriculture.tools],['area','soil','drought','rainfall','landcover','crops']);
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.agriculture,mode:'2d',depth:2.5,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},onSoil:v=>calls.push(['soil',v]),onSoilDepth:v=>calls.push(['depth',v])};
 const soil={on:false,depth:'surface',reading:'',legendUrl:'https://gibs.earthdata.nasa.gov/legends/SMAP_Analyzed_Soil_Moisture_H.svg'};
 const button=(tree,label)=>findNode(tree,n=>n.type==='button'&&n.props.children===label);
 let tree=h.render(h.exports.CategoryMapDock,{...base,soil});
 assert.equal(button(tree,'Surface 0–5 cm'),undefined,'no depth or scale while hidden');
 button(tree,'Show soil moisture').props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,soil:{...soil,on:true,reading:'Surface moisture · 0–5 cm · 2026-10-25 12:00 UTC · NASA SMAP L4, 9 km modelled cells'}});
 assert.equal(button(tree,'Surface 0–5 cm').props['aria-pressed'],true);
 button(tree,'Root zone 0–100 cm').props.onClick();
 assert.match(JSON.stringify(tree),/2026-10-25 12:00 UTC · NASA SMAP L4, 9 km modelled cells/);
 assert.equal(findNode(tree,n=>n.type==='img').props.src,soil.legendUrl,'NASA\'s own colour scale');
 button(tree,'Hide soil moisture').props.onClick();
 assert.deepEqual(calls,[['soil',true],['depth','root'],['soil',false]]);
 h.dispose?.();
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/if \(on && map && map\.getZoom\(\) > SOIL_REGIONAL_ZOOM \+ 0\.5\) map\.easeTo\(\{ zoom: SOIL_REGIONAL_ZOOM/,'a field-scale view pulls out to the region the 9 km cells describe');
 assert.match(page,/if \(!look\.tools\?\.includes\("soil"\)\) setSoilMapState\(current => current\.visible \? hideSoilContext\(current\) : current\);/,'soil moisture does not follow into other maps');
 assert.match(page,/soilMoistureContext\?\.renderedFrameTimeUtc \? `\$\{SOIL_VIEWS\[soilMapState\.view\]\.label\}/,'the reading names the frame actually rendered');
 const control=await readFile('app/soil-moisture-control.tsx','utf8');
 assert.match(control,/if \(enabled && availability === null && !checking\) void checkAvailability\(\);/,'switched on from outside the row, it still checks NASA\'s days');
});

test('the Aquifer map opens on saturated thickness and switches one KGS view at a time, with its classes as the legend',async()=>{
 const look=maps.CATEGORY_MAPS.groundwater;
 assert.deepEqual([...look.starters],['kgs-saturated-thickness']);assert.deepEqual([...look.tools],['aquifer','underground']);
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look,mode:'2d',depth:2.5,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},onUnderground(){},onAquiferView:v=>calls.push(v)};
 const legend=[{label:'Under 50',color:'#ffff73'},{label:'Over 300',color:'#0c2c84'}];
 const button=(tree,label)=>findNode(tree,n=>n.type==='button'&&n.props.children===label);
 let tree=h.render(h.exports.CategoryMapDock,{...base,aquifer:{view:'kgs-saturated-thickness',legend}});
 assert.equal(button(tree,'Thickness').props['aria-pressed'],true);
 assert.match(JSON.stringify(tree),/Under 50.*Over 300.*Saturated thickness.*feet · KGS High Plains Atlas, 2022–2024 classes, not well measurements/);
 button(tree,'Depth to water').props.onClick();button(tree,'Extent').props.onClick();
 assert.deepEqual(calls,['kgs-depth-to-water','kgs-aquifer-high-plains']);
 tree=h.render(h.exports.CategoryMapDock,{...base,aquifer:{view:'kgs-aquifer-high-plains',legend:null}});
 assert.doesNotMatch(JSON.stringify(tree),/feet ·/,'the extent has no classes');
 h.dispose?.();
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/for \(const id of AQUIFER_VIEW_IDS\) if \(id === view \|\| officialVisibilityRef\.current\[id\]\) setOfficialContextVisible\(id, id === view\);/,'one view at a time');
});
