import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {getSolarPosition} from 'sunrise-sunset-js';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const sun=await compile('app/sun-chart.ts');
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const plain=v=>JSON.parse(JSON.stringify(v));
const WICHITA={lat:37.69,lon:-97.34};

test('every event lands where NREL\'s Solar Position Algorithm puts the Sun at that altitude, to a few seconds of time',()=>{
 for(const day of ['2026-01-15','2026-03-20','2026-06-21','2026-09-22','2026-12-21']){
  const t=Date.parse(`${day}T00:00:00Z`);
  for(const [limit,altitude] of Object.entries(sun.SUN_EVENTS))for(const morning of [true,false]){
   const at=sun.sunEvent(t,WICHITA.lat,WICHITA.lon,altitude,morning);
   // Pressure 0 turns refraction off: the SPA's geometric altitude of the Sun's centre.
   const spa=getSolarPosition(WICHITA.lat,WICHITA.lon,new Date(at),{pressure:0}).elevation;
   assert.ok(Math.abs(spa-altitude)<0.01,`${day} ${limit} ${morning?'dawn':'dusk'}: SPA ${spa.toFixed(4)}° against ${altitude}°`);
  }
  const noon=sun.sunEvent(t,WICHITA.lat,WICHITA.lon,'noon');
  const [before,at,after]=[-60e3,0,60e3].map(d=>getSolarPosition(WICHITA.lat,WICHITA.lon,new Date(noon+d),{pressure:0}).elevation);
  assert.ok(at>=before&&at>=after,`${day}: solar noon is the Sun's highest`);
 }
});

test('a Kansas year in Central clock time: the solstices, the daylight-saving steps, and a day that never reaches astronomical night is none here',()=>{
 const days=sun.sunYear(2026,WICHITA.lat,WICHITA.lon);
 assert.equal(days.length,365);
 const day=date=>days.find(d=>d.date===date);
 const jun=day('2026-06-21'),dec=day('2026-12-21');
 assert.deepEqual([sun.clock(jun.sunrise),sun.clock(jun.sunset,jun.offset)],['6:08 AM','8:54 PM CDT']);
 assert.deepEqual([sun.clock(dec.sunrise),sun.clock(dec.sunset,dec.offset)],['7:41 AM','5:14 PM CST']);
 assert.equal(Math.round(jun.length),886);assert.equal(Math.round(dec.length),573);
 // Clocks spring forward on March 8, 2026 and fall back on November 1: the sunrise jumps an hour, the daylight does not.
 const [mar7,mar8]=[day('2026-03-07'),day('2026-03-08')];
 assert.deepEqual([mar7.offset,mar8.offset],[-360,-300]);assert.ok(Math.abs(mar8.sunrise-mar7.sunrise-58)<3);assert.ok(Math.abs(mar8.length-mar7.length)<3);
 assert.deepEqual([day('2026-10-31').offset,day('2026-11-01').offset],[-300,-360]);
 assert.ok(days.every(d=>d.astroDawn!==null&&d.astroDusk!==null),'Kansas has full night all year');
 assert.ok(days.every(d=>d.astroDawn<d.nauticalDawn&&d.nauticalDawn<d.civilDawn&&d.civilDawn<d.sunrise&&d.sunrise<d.noon&&d.noon<d.sunset&&d.sunset<d.civilDusk&&d.civilDusk<d.nauticalDusk&&d.nauticalDusk<d.astroDusk));
 assert.equal(sun.sunEvent(Date.UTC(2026,5,21),70,25,-0.833,true),null,'midnight sun: no sunrise');
});

test('the day\'s line and the chart',()=>{
 const days=sun.sunYear(2026,WICHITA.lat,WICHITA.lon);
 assert.equal(sun.sunReading(days,'2026-10-29'),'Oct 29: first light 7:25 AM, sunrise 7:52 AM, solar noon 1:13 PM, sunset 6:34 PM, last light 7:01 PM CDT · 10 h 42 min of daylight (−2 min 11 s on the day before) · longest Jun 21, 14 h 46 min; shortest Dec 21, 9 h 33 min');
 assert.equal(sun.sunReading(days,'2025-01-01'),null);
 const chart=sun.sunChart(days,'2026-10-29');
 assert.deepEqual(chart.bands.map(b=>b.id),['astronomical','nautical','civil','day']);
 assert.deepEqual(chart.bands.map(b=>b.color),['#1d2c5c','#2f4a8a','#5f7fbf','#f2d27a']);
 assert.ok(chart.bands.every(b=>/^M[\d.,L]+Z/.test(b.d)));
 assert.equal(chart.months.length,12);assert.equal(chart.months[0].label,'Jan');
 assert.deepEqual(chart.hours.map(h=>h.label),['12a','6a','12p','6p','12a']);
 assert.ok(chart.hours[0].y>chart.hours[2].y,'time runs up: midnight at the foot');
 assert.ok(Math.abs(chart.today-(chart.left+(days.findIndex(d=>d.date==='2026-10-29')+0.5)/365*chart.plotWidth))<1e-9);
 assert.equal(sun.sunChart(days,null).today,null);
 assert.equal(sun.inKansasBox(-98.7,38.5),true);assert.equal(sun.inKansasBox(-104.9,39.7),false);
 assert.equal(sun.mayKeepMountainTime(-101.8),true);assert.equal(sun.mayKeepMountainTime(-100),false);
 assert.equal(sun.coordinateLabel(-98.698,38.498),'38.50°N, 98.70°W');
});

test('a gold point marks the charted place and goes with it',()=>{
 const layers=[],sources={};
 const map={getSource:id=>sources[id]&&{setData(d){sources[id].data=d;}},addSource:(id,s)=>{sources[id]=s;},removeSource:id=>{delete sources[id];},
  getLayer:id=>layers.find(l=>l.id===id),removeLayer:id=>{layers.splice(layers.findIndex(l=>l.id===id),1);},addLayer:spec=>{layers.push({id:spec.id,spec});}};
 sun.syncSunPlace(map,sun.KANSAS_CENTRE);assert.deepEqual(plain(sources[sun.SUN_PLACE_SOURCE_ID].data.features[0].geometry.coordinates),[-98.698,38.498]);
 sun.syncSunPlace(map,{lon:-95.7,lat:39});assert.deepEqual(plain(sources[sun.SUN_PLACE_SOURCE_ID].data.features[0].geometry.coordinates),[-95.7,39]);assert.equal(layers.length,1);
 sun.syncSunPlace(map,null);assert.deepEqual(layers,[]);assert.deepEqual(Object.keys(sources),[]);
});

test('the Sky globe offers daylight through the year; a click in Kansas charts that place',async()=>{
 const days=sun.sunYear(2026,WICHITA.lat,WICHITA.lon);
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.sky,mode:'globe',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  onSunYear:v=>calls.push(['on',v]),onSunYearCentre:()=>calls.push(['centre'])};
 const off={on:false,place:null,outside:false,reading:null,chart:null,note:null,atCentre:true};
 const tool=tree=>findNode(tree,n=>n.type==='button'&&/daylight through the year/i.test(String(n.props.children)));
 let tree=h.render(h.exports.CategoryMapDock,{...base,sunYear:off});
 assert.equal(tool(tree).props.children,'Daylight through the year');tool(tree).props.onClick();
 const on={on:true,place:'37.69°N, 97.34°W',outside:false,reading:sun.sunReading(days,'2026-10-29'),chart:sun.sunChart(days,'2026-10-29'),note:null,atCentre:false};
 tree=h.render(h.exports.CategoryMapDock,{...base,sunYear:on});
 assert.equal(tool(tree).props.children,'Hide daylight through the year');
 assert.match(JSON.stringify(tree),/At 37\.69°N, 97\.34°W · click the map in Kansas for another place/);
 const chart=findNode(tree,n=>n.type===h.exports.SunYearChart);const figure=chart.type(chart.props);
 assert.equal(figure.props['aria-label'],'Sunrise, sunset and twilight through the year at 37.69°N, 97.34°W, in Central clock time');
 const svg=JSON.stringify(figure);assert.match(svg,/"data-band":"day"/);assert.match(svg,/"data-today"/);assert.match(svg,/the steps are the clock changing/);
 findNode(tree,n=>n.type==='button'&&n.props.children==='Back to the centre of Kansas').props.onClick();
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,sunYear:{...on,outside:true}})),/the chart is for places in Kansas/);
 assert.equal(findNode(h.render(h.exports.CategoryMapDock,{...base,sunYear:{...on,atCentre:true}}),n=>n.type==='button'&&n.props.children==='Back to the centre of Kansas'),undefined);
 assert.deepEqual(calls,[['on',true],['centre']]);
 assert.equal(tool(h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.water,sunYear:off})),undefined,'only maps that offer it');
 assert.match(page,/if \(sunYearOnRef\.current\) \{\s*const \{ lng, lat \} = event\.lngLat;\s*if \(inKansasBox\(lng, lat\)\) \{ setSunPlace\(\{ lon: lng, lat \}\); setSunOutside\(false\); \} else setSunOutside\(true\);/);
 assert.match(page,/setSunYearOn\(false\);\s*setSunPlace\(null\);/,'closes with its map');
});
