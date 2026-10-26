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
 assert.match(page,/keys=\{withElevationKey\(\[\.\.\.\(quakeRecordOn && quakeRecord \? \[earthquakeRecordKey\(quakeRecord\.endYear\)\] : \[\]\), \.\.\.withReviewedKey\(mapKeysFor\(activeCategoryMap\.starters, id => Boolean\(officialVisibility\[id as OfficialContextId\]\)\), reviewedData \? reviewedSource : null\)\],/);
});

const luminance=hex=>{const c=rgb(hex).map(v=>v/255).map(v=>v<=0.03928?v/12.92:((v+0.055)/1.055)**2.4);return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2];};
const contrast=(a,b)=>{const [x,y]=[luminance(a),luminance(b)].sort((p,q)=>p-q);return (y+0.05)/(x+0.05);};

test('KDOT lines read on their own light maps and on the dark ones, and no two datasets share a colour',async()=>{
 const basemaps=await readFile('app/category-basemaps.ts','utf8');
 const ground=name=>basemaps.slice(basemaps.indexOf(`function ${name}(`)).match(/"background-color": "(#[0-9a-f]{6})"/)[1];
 const light={network:ground('networkLayers'),historic:ground('historicLayers'),civic:ground('civicLayers')};
 const dark={storm:ground('stormLayers'),navy:'#0b1d2a'};
 const symbols=Object.entries(keys.KDOT_LINE_SYMBOLS);
 for(const [id,{color}] of symbols)for(const [base,bg] of Object.entries({...light,...dark}))
  assert.ok(contrast(color,bg)>=3,`${id} on ${base}: ${contrast(color,bg).toFixed(2)}:1`);
 assert.equal(new Set(symbols.map(([,s])=>s.color)).size,symbols.length,'one colour per dataset');
 assert.deepEqual(symbols.filter(([,s])=>s.dashed).map(([id])=>id),['kdot-rail-abandoned'],'only the former rail is dashed');
 assert.deepEqual(keys.esriColor('#0f8a80'),[15,138,128,255]);
});

test('the requests KDOT draws use the same symbols the key shows',async()=>{
 const reference=await readFile('app/kansas-reference-layers.ts','utf8');
 for(const id of Object.keys(keys.KDOT_LINE_SYMBOLS)){
  assert.match(reference,new RegExp(`kdotLine\\("[A-Za-z_]+", \\d, "${id}"\\)`),`${id} request`);
  assert.match(reference,new RegExp(`color: KDOT_LINE_SYMBOLS\\["${id}"\\]\\.color`),`${id} registry colour`);
 }
 assert.match(reference,/color: esriColor\(color\), width: 1\.5/);
 assert.doesNotMatch(reference,/\[24[5-7], 1[67]\d, 1[01]\d, 255\]/,'the old near-identical oranges are gone');
});

test('each map keys its own lines, grouped under one title',()=>{
 const network=keys.mapKeysFor(maps.CATEGORY_MAPS.transport.starters,()=>true);
 assert.deepEqual(network.map(k=>k.title),['KDOT roads and rail']);
 assert.deepEqual(network[0].items.map(i=>[i.label,i.shape,Boolean(i.dashed)]),[['Public roads','line',false],['Active railroads','line',false]]);
 const historic=keys.mapKeysFor(maps.CATEGORY_MAPS.history.starters,()=>true);
 assert.deepEqual(historic.map(k=>k.title),['1918 roads and former rail']);
 assert.deepEqual(historic[0].items.map(i=>[i.label,Boolean(i.dashed)]),[['1918 state highways',false],['Abandoned railroads',true]]);
 assert.match(historic[0].note,/inked lines with ties/,'the base map draws today\'s rail; the key says so');
 assert.deepEqual(keys.mapKeysFor(maps.CATEGORY_MAPS.history.starters,id=>id==='kdot-rail-abandoned')[0].items.map(i=>i.label),['Abandoned railroads'],'only the lines that are on');
});

test('the Hazard watch keys alerts, satellite detections and reported incidents, each as the map draws it',()=>{
 const hazard=keys.mapKeysFor(maps.CATEGORY_MAPS.disaster.starters,()=>true);
 assert.deepEqual(hazard.map(k=>k.id),['nws-alerts','nasa-gibs-fire-points','nifc-fire-reports']);
 const [,detections,reports]=hazard;
 assert.deepEqual(detections.items.map(i=>[i.label,i.color,i.shape]),[['High confidence',keys.FIRE_CONFIDENCE_COLORS.high,'dot'],['Nominal confidence',keys.FIRE_CONFIDENCE_COLORS.nominal,'dot'],['Low confidence',keys.FIRE_CONFIDENCE_COLORS.low,'dot']]);
 assert.match(detections.note,/375 m detection pixel[\s\S]*not a perimeter/);
 assert.deepEqual(reports.items.map(i=>[i.label,i.shape]),[['Wildfire','ring'],['Prescribed fire','ring'],['Incident complex','ring']],'a ring, never a detection dot');
 assert.deepEqual(reports.items.map(i=>i.color),keys.FIRE_REPORT_COLORS.map(([,c])=>c));
});

test('reviewed discharge snapshots get a proportional-symbol key at the sizes the gauges are drawn',async()=>{
 const key=keys.REVIEWED_DISCHARGE_KEY;
 // radius = 3 + 0.06·√Q px: 100 → 3.6, 1,000 → 4.9, 10,000 → 9, 62,500 → 18 (the cap).
 assert.deepEqual(key.items.slice(0,4).map(i=>[i.label,i.size]),[['100',7],['1,000',10],['10,000',18],['62,500+',36]]);
 assert.deepEqual(key.items.slice(4).map(i=>[i.label,i.stroke]),[['Provisional',keys.GAUGE_PROVISIONAL_RING],['Approved',keys.GAUGE_APPROVED_RING]]);
 assert.match(key.note,/area grows with discharge from a 3 px floor[\s\S]*above 62,500/);
 assert.deepEqual(keys.dischargeRadius().slice(3),keys.DISCHARGE_RADIUS_STOPS.flat());
 const layers=await readFile('app/reviewed-snapshot-layers.ts','utf8');
 assert.match(layers,/"circle-radius": dischargeRadius\(\), "circle-color": GAUGE_FILL_COLOR/,'the gauges use the keyed scale');
 assert.match(layers,/GAUGE_PROVISIONAL_RING, GAUGE_APPROVED_RING\]/);
});

test('a drawn reviewed snapshot adds its key once, and alerts share the live severity key',async()=>{
 const live=keys.mapKeysFor(maps.CATEGORY_MAPS.water.starters,()=>true);
 assert.deepEqual(keys.withReviewedKey(live,'usgs-streamflow').map(k=>k.id),[...live.map(k=>k.id),'reviewed-discharge']);
 assert.equal(keys.withReviewedKey(live,null),live,'no snapshot drawn, no key');
 const storm=keys.mapKeysFor(maps.CATEGORY_MAPS.weather.starters,()=>true);
 assert.deepEqual(keys.withReviewedKey(storm,'nws-alerts').map(k=>k.id),['nws-alerts'],'not shown twice');
 assert.deepEqual(keys.withReviewedKey([],'nws-alerts').map(k=>k.id),['nws-alerts'],'shown when the live alerts are off');
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/keys=\{withElevationKey\(\[\.\.\.\(quakeRecordOn && quakeRecord \? \[earthquakeRecordKey\(quakeRecord\.endYear\)\] : \[\]\), \.\.\.withReviewedKey\(mapKeysFor\(activeCategoryMap\.starters, id => Boolean\(officialVisibility\[id as OfficialContextId\]\)\), reviewedData \? reviewedSource : null\)\],/);
});

test('the relief and chart bases key their elevation colours from the ramps the styles draw',async()=>{
 const basemaps=await readFile('app/category-basemaps.ts','utf8');
 const ramp=JSON.parse(basemaps.match(/export const RELIEF_RAMP[^=]*= Object\.freeze\((\[[\s\S]*?\])\);/)[1].replace(/\s/g,'').replace(/,\]$/,']'));
 const relief=keys.reliefElevationKey(ramp);
 assert.equal(relief.title,'Elevation (m above sea level)');
 // 200–1300 m across the bar: the 150 m stop sits just before it, 1100 m at 81.8 %.
 assert.match(relief.ramp.css,/^linear-gradient\(to right, #5f8f5a -4\.5%, #86a866 9\.1%,[\s\S]*#c9a77a 81\.8%/);
 assert.deepEqual(relief.ramp.ticks.map(t=>[t.label,t.at]),[['300',9.1],['600',36.4],['900',63.6],['1,200',90.9]]);
 assert.match(relief.note,/207 m[\s\S]*1,231 m at Mount Sunflower/);
 const bands=[[0,'#bcd6a4'],[305,'#cfe0ae'],[610,'#e2e4b8'],[914,'#ead7ab'],[1219,'#e1c597'],[1524,'#d6b48a']];
 const chart=keys.chartElevationKey(bands);
 assert.equal(chart.title,'Terrain elevation (ft)');
 // Hard 1,000 ft bands: each colour runs from its band to the next.
 assert.match(chart.ramp.css,/#cfe0ae 12\.5% 37\.5%, #e2e4b8 37\.5% 62\.5%, #ead7ab 62\.5% 87\.5%/);
 assert.deepEqual(chart.ramp.ticks.map(t=>t.label),['1,000','2,000','3,000','4,000']);
 assert.match(chart.note,/680 to 4,040 ft/);
 assert.deepEqual(keys.withElevationKey([keys.MAP_KEYS['usgs-earthquakes']],relief).map(k=>k.id),['elevation-relief','usgs-earthquakes'],'the base comes first');
 assert.deepEqual(keys.withElevationKey([],null),[]);
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/basemap === "relief" \? reliefElevationKey\(RELIEF_RAMP\) : basemap === "aviation-chart" \? chartElevationKey\(AVIATION_TINT_BANDS\) : null/,'only while that base is drawn (not the photograph)');
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const tree=h.render(h.exports.CategoryMapDock,{look:maps.CATEGORY_MAPS.terrain,mode:'terrain',depth:2.5,azimuth:315,sun:null,sunAvailable:true,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},keys:[relief]});
 const bar=findNode(tree,n=>n.props?.className==='category-map-dock-key-ramp-bar');
 assert.equal(bar.props.style.background,relief.ramp.css);
 assert.match(JSON.stringify(tree),/"left":"36\.4%"[\s\S]*600/);
 h.dispose?.();
});
