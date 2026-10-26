import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const load=async path=>{const exports={};new Function('exports',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports);return exports;};
const {PHOTOREAL_LANDSCAPES}=await load('app/photoreal-landscapes.ts');
const maps=await load('app/category-maps.ts');

test('each landscape is a real Kansas place framed in 3D, with a caption on what the ground is',()=>{
 assert.deepEqual(PHOTOREAL_LANDSCAPES.map(l=>l.id),['red-hills','monument-rocks','little-jerusalem','konza','arikaree','wichita']);
 for(const {id,name,caption,camera:{center:[lon,lat],zoom,pitch,bearing}} of PHOTOREAL_LANDSCAPES){
  assert.ok(lon>-102.06&&lon<-94.6&&lat>36.99&&lat<40.01,`${id}: inside Kansas`);
  assert.ok(zoom>=12.5&&zoom<=16,`${id}: close enough for the one-foot aerial, within the 3DEP tiles' overzoom`);
  assert.ok(pitch>=60&&pitch<=72&&Math.abs(bearing)<=180,`${id}: an oblique 3D view within the map's pitch limit`);
  assert.ok(name.includes(' · ')&&caption.length<=130&&/\.$/.test(caption),`${id}: named with its county or region, one-sentence caption`);
 }
 assert.match(PHOTOREAL_LANDSCAPES[1].caption,/Niobrara Chalk/);assert.match(PHOTOREAL_LANDSCAPES[0].caption,/Permian red beds capped by gypsum/);
 assert.match(PHOTOREAL_LANDSCAPES[4].caption,/loess/);
 assert.ok(maps.CATEGORY_MAPS.terrain.tools.includes('photoreal'));
});

test('the photo-real basemap is the photographed ground: world imagery, the 2024 Kansas aerial over it, buildings at recorded heights',async()=>{
 const runtime=await readFile('app/map-runtime.ts','utf8');
 const block=runtime.slice(runtime.indexOf('  photoreal: {'),runtime.indexOf('  midnight: {'));
 assert.match(block,/"esri-imagery": \{ type: "raster", tiles: \[esriImageryContext\.requestUrl\]/);
 assert.match(block,/"kansas-ng911-2024": \{ type: "raster", tiles: \[kansasAerialContext\.requestUrl\]/);
 assert.ok(block.indexOf('photoreal-world-imagery')<block.indexOf('photoreal-kansas-aerial'),'the Kansas aerial draws over the world imagery');
 assert.match(block,/"fill-extrusion-height": \["coalesce", \["get", "render_height"\], 0\]/,'heights as OpenMapTiles records them, nothing invented');
 assert.match(block,/"fill-extrusion-base": \["coalesce", \["get", "render_min_height"\], 0\]/);
 assert.doesNotMatch(block,/"symbol"|hillshade/,'no labels or painted shading over the photograph');
 const sources=await readFile('app/external-context-sources.ts','utf8');
 for(const id of ['openfreemap-liberty','esri-world-imagery','kansas-ng911-2024'])assert.match(sources.slice(sources.indexOf(`id: "${id}"`)),/activatesWhen: Object\.freeze\(\[[^\]]*"photoreal"/,`${id} discloses the photo-real basemap`);
 assert.match(await readFile('app/saved-workspaces.ts','utf8'),/"kansas-aerial", "photoreal"/,'a saved workspace can restore it');
});

test('the Relief model dock enters photo-real 3D at true scale, names the scale and the ground, and returns',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.terrain,mode:'terrain',depth:1,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},onTransect(){},onPhotoreal:v=>calls.push(v)};
 const button=(tree,label)=>findNode(tree,n=>n.type==='button'&&n.props.children===label);
 let tree=h.render(h.exports.CategoryMapDock,{...base,photoreal:{on:false,landscapes:PHOTOREAL_LANDSCAPES,place:null,depth:2.5}});
 button(tree,'Photo-real 3D').props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,photoreal:{on:true,landscapes:PHOTOREAL_LANDSCAPES,place:'monument-rocks',depth:1}});
 assert.equal(button(tree,'Monument Rocks · Gove County').props['aria-pressed'],true);
 assert.match(JSON.stringify(tree),/Niobrara Chalk.*True vertical scale \(1×\).*· USGS 3DEP bare earth · Kansas aerial 2024, 1 ft/);
 button(tree,'Konza Prairie · Flint Hills').props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,depth:2,photoreal:{on:true,landscapes:PHOTOREAL_LANDSCAPES,place:'konza',depth:2}});
 assert.match(JSON.stringify(tree),/Vertical ×2\.0/,'an exaggerated view says so');
 button(tree,'Back to relief colours').props.onClick();
 assert.deepEqual(calls,['red-hills','konza',null]);
 h.dispose?.();
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/if \(basemapRef\.current !== "photoreal"\) \{\n      basemapRef\.current = "photoreal"; setBasemap\("photoreal"\); changeTerrainDepth\(1\);/,'true vertical scale on entry');
 assert.match(page,/photorealHidHillshadeRef\.current = Boolean\(officialVisibilityRef\.current\["usgs-3dep-hillshade"\]\);\n      if \(photorealHidHillshadeRef\.current\) setOfficialContextVisible\("usgs-3dep-hillshade", false\);/,'the provider hillshade leaves the photograph');
 assert.match(page,/if \(photorealHidHillshadeRef\.current\) \{ photorealHidHillshadeRef\.current = false; setOfficialContextVisible\("usgs-3dep-hillshade", true\); \}/,'and returns with the relief colours');
 assert.match(page,/if \(terrainProviderRef\.current !== "usgs-3dep"\) chooseTerrainProvider\("usgs-3dep"\);/,'the USGS 3DEP bare-earth DEM');
 assert.match(page,/if \(!sceneEffectsRef\.current\.sunSync\) updateSceneEffects\(\{ \.\.\.sceneEffectsRef\.current, sunSync: true \}\);/,'lit by the real sun');
});
