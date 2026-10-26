import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const load=async path=>{const exports={};new Function('exports',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports);return exports;};
const keys=await load('app/map-keys.ts');
const maps=await load('app/category-maps.ts');
const live=await readFile('app/live-context.ts','utf8');
const reviewed=await readFile('app/reviewed-snapshot-layers.ts','utf8');
const rgb=hex=>[1,3,5].map(i=>parseInt(hex.slice(i,i+2),16));

test('the earthquake key is drawn from the same stops the map draws from',()=>{
 const key=keys.MAP_KEYS['usgs-earthquakes'];
 assert.deepEqual(key.items.map(i=>i.label),['M 0','M 2','M 4','M 6+']);
 assert.deepEqual(key.items.map(i=>i.color),keys.EARTHQUAKE_MAGNITUDE_COLORS.map(([,c])=>c));
 // Diameters at zoom 4: radius 3 at M0, 7 at M3, 12 at M6, linear between.
 assert.deepEqual(key.items.map(i=>i.size),[6,11,17,24]);
 const radius=keys.earthquakeRadius();
 assert.deepEqual(radius.slice(0,3),['interpolate',['linear'],['zoom']]);
 assert.deepEqual(radius[4].slice(3),keys.EARTHQUAKE_RADIUS_Z4.flat());
 assert.deepEqual(keys.earthquakeColor().slice(3),keys.EARTHQUAKE_MAGNITUDE_COLORS.flat());
 assert.match(live,/"circle-color": earthquakeColor\(\),\s*"circle-radius": earthquakeRadius\(\),/,'the live layer uses them');
});

test('NWS severity has one ordinal palette for live and reviewed alerts, and unknown severity stays off the scale',()=>{
 assert.deepEqual(keys.NWS_SEVERITY_COLORS.map(([s])=>s),['Extreme','Severe','Moderate','Minor']);
 // Ordinal: lightness falls from Minor to Extreme.
 const lightness=keys.NWS_SEVERITY_COLORS.map(([,c])=>{const [r,g,b]=rgb(c);return 0.2126*r+0.7152*g+0.0722*b;});
 assert.ok(lightness.every((l,i)=>i===0||l>lightness[i-1]),JSON.stringify(lightness));
 const [r,g,b]=rgb(keys.NWS_SEVERITY_UNKNOWN_COLOR);
 assert.ok(Math.max(r,g,b)-Math.min(r,g,b)<24,'unknown is a neutral grey');
 assert.deepEqual(keys.nwsSeverityColor(),['match',['get','severity'],...keys.NWS_SEVERITY_COLORS.flat(),keys.NWS_SEVERITY_UNKNOWN_COLOR]);
 assert.match(live,/"fill-color": nwsSeverityColor\(\)[\s\S]*"line-color": nwsSeverityColor\(\)/,'live alert areas and outlines');
 assert.match(reviewed,/const severityColor = nwsSeverityColor\(\);/,'reviewed alert snapshots');
 assert.doesNotMatch(live,/"Minor", "#78c6d0"/,'the old categorical palette is gone');
 const key=keys.MAP_KEYS['nws-alerts'];
 assert.deepEqual(key.items.map(i=>i.label),['Extreme','Severe','Moderate','Minor','Unknown']);
});

test('a map shows keys only for its own starter layers that are on, in the map order',()=>{
 const on=new Set(['nws-alerts','nws-radar']);
 assert.deepEqual(keys.mapKeysFor(maps.CATEGORY_MAPS.weather.starters,id=>on.has(id)).map(k=>k.id),['nws-alerts'],'radar keeps its dBZ legend in its own panel');
 assert.deepEqual(keys.mapKeysFor(maps.CATEGORY_MAPS.geology.starters,()=>true).map(k=>k.id),['usgs-earthquakes']);
 assert.deepEqual(keys.mapKeysFor(maps.CATEGORY_MAPS.geology.starters,()=>false),[],'a starter switched off takes its key with it');
 assert.deepEqual(keys.mapKeysFor(maps.CATEGORY_MAPS.terrain.starters,()=>true),[]);
});

test('the dock draws each key as the map draws it, and the page passes the keys for the shown starters',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const base={look:maps.CATEGORY_MAPS.geology,mode:'2d',depth:2.5,azimuth:315,sun:null,sunAvailable:true,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){}};
 let tree=h.render(h.exports.CategoryMapDock,{...base,keys:[keys.MAP_KEYS['usgs-earthquakes'],keys.MAP_KEYS['nws-alerts']]});
 const sections=[];findNode(tree,n=>{if(n.type==='section'&&String(n.props?.className).includes('category-map-dock-key'))sections.push(n);return false;});
 assert.deepEqual(sections.map(s=>s.props['aria-label']),['Key: Earthquake magnitude','Key: NWS alert severity']);
 const text=JSON.stringify(tree);
 assert.match(text,/M 6\+/);assert.match(text,/"--size":"24px"/);assert.match(text,/"--key":"#c2188f"/);
 tree=h.render(h.exports.CategoryMapDock,{...base});
 assert.doesNotMatch(JSON.stringify(tree),/category-map-dock-key/,'no keys, no section');
 h.dispose?.();
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/keys=\{mapKeysFor\(activeCategoryMap\.starters, id => Boolean\(officialVisibility\[id as OfficialContextId\]\)\)\}/);
});
