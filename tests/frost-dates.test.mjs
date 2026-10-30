import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness} from './component-harness.mjs';

const esm=async path=>ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const dataUrl=code=>'data:text/javascript;base64,'+Buffer.from(code).toString('base64');
const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const frost=await compile('app/frost-dates.ts',{'./growing-degree-days':{}});
const maps=await compile('app/category-maps.ts');
const routeSource=await readFile('app/api/farming/frost-dates/route.ts','utf8');
const page=await readFile('app/page.tsx','utf8');
const dockSource=await readFile('app/category-map-dock.tsx','utf8');

const DAY=86_400_000;
const SPRING='2024-04-14', FALL='2024-10-21';
/** A year of daily lows: 40 °F, with a freeze on the spring and fall dates; any date in `blank` has no reading. */
const year2024=({blank=[],today='2024-12-31'}={})=>frost.yearDates(2024).filter(date=>date<=today).map(date=>({day:date,maxF:60,minF:blank.includes(date)?null:(date===SPRING||date===FALL?31:40)}));

/** The route with its local imports inlined, so it runs under node:test without a bundler. */
const loadRoute=async()=>{
  const upstream=await esm('app/api/event-atlas/upstream.ts'), cropland=await esm('app/cropland.ts'), days=await esm('app/growing-degree-days.ts'), dates=await esm('app/frost-dates.ts');
  const stations=(await esm('app/kansas-stations.ts')).replace('from "./api/event-atlas/upstream"',`from "${dataUrl(upstream)}"`).replace('from "./growing-degree-days"',`from "${dataUrl(days)}"`);
  const code=ts.transpileModule(routeSource,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText
    .replace('from "../../event-atlas/upstream"',`from "${dataUrl(upstream)}"`)
    .replace('from "../../../cropland"',`from "${dataUrl(cropland)}"`)
    .replace('from "../../../kansas-stations"',`from "${dataUrl(stations)}"`)
    .replace('from "../../../growing-degree-days"',`from "${dataUrl(days)}"`)
    .replace('from "../../../frost-dates"',`from "${dataUrl(dates)}"`);
  return import(dataUrl(code));
};
const STATIONS={type:'FeatureCollection',features:[
 {properties:{sid:'SLN',sname:'Salina'},geometry:{type:'Point',coordinates:[-97.65,38.79]}},
 {properties:{sid:'HYS',sname:'Hays'},geometry:{type:'Point',coordinates:[-99.27,38.84]}},
]};
const json=(body,status=200)=>new Response(JSON.stringify(body),{status,headers:{'content-type':'application/json'}});
const text=(body,status=200)=>new Response(body,{status,headers:{'content-type':'text/csv'}});
const csvOf=days=>`station,day,max_temp_f,min_temp_f\n${days.map(d=>`SLN,${d.day},${d.maxF??'M'},${d.minF??'M'}`).join('\n')}\n`;

test('a year runs from January 1 to December 31, every date of it',()=>{
 const dates=frost.yearDates(2024);
 assert.equal(dates.length,366);assert.equal(dates[0],'2024-01-01');assert.equal(dates.at(-1),'2024-12-31');
});

test('the last spring freeze and the first fall freeze are found, with the frost-free days between them',()=>{
 const reading=frost.frostDates(year2024(),2024,'2024-12-31');
 assert.equal(reading.lastSpring,SPRING);assert.equal(reading.firstFall,FALL);
 assert.equal(reading.springKnown,true);assert.equal(reading.fallKnown,true);
 assert.equal(reading.frostFreeDays,Math.round((Date.parse(`${FALL}T00:00:00Z`)-Date.parse(`${SPRING}T00:00:00Z`))/DAY));
 assert.equal(reading.daysMissing,0);
});

test('a missing day after the last spring freeze, or before the first fall freeze, makes that date uncertain, since it could hide a freeze',()=>{
 const afterSpring=frost.frostDates(year2024({blank:['2024-04-20']}),2024,'2024-12-31');
 assert.equal(afterSpring.lastSpring,SPRING);assert.equal(afterSpring.springKnown,false,'a day after the freeze is missing');
 assert.equal(afterSpring.frostFreeDays,null);
 const beforeFall=frost.frostDates(year2024({blank:['2024-10-10']}),2024,'2024-12-31');
 assert.equal(beforeFall.fallKnown,false,'a day before the freeze is missing');
 assert.equal(beforeFall.frostFreeDays,null);
});

test('days after today are not yet due, so they are not missing',()=>{
 const earlyYear=frost.frostDates(year2024({today:'2024-05-01'}),2024,'2024-05-01');
 assert.equal(earlyYear.lastSpring,SPRING);assert.equal(earlyYear.firstFall,null,'no fall freeze is due yet');
 assert.equal(earlyYear.fallKnown,true);assert.equal(earlyYear.daysMissing,0);
 assert.equal(earlyYear.frostFreeDays,null,'no frost-free days until both freezes are known');
});

test('the frost line says each freeze, or that it is not certain, and the frost-free days',()=>{
 const station={id:'SLN',name:'Salina',km:3};
 const clean={lon:-97.6,lat:38.8,retrievedAt:'x',year:2024,state:'ready',station,lastSpring:SPRING,firstFall:FALL,springKnown:true,fallKnown:true,frostFreeDays:190,daysMissing:0};
 assert.equal(frost.frostLine(clean),'last spring freeze Apr 14 · first fall freeze Oct 21 · 190 frost-free days · from Salina, 3 km away');
 assert.match(frost.frostLine({...clean,springKnown:false,frostFreeDays:null}),/last spring freeze not certain, days missing/);
 assert.equal(frost.frostLine({...clean,state:'none',station:null}),null);
 assert.equal(frost.validFrostDates(clean,-97.6,38.8,2024),true,'the page accepts the reading');
});

test('the route reads the nearest station\'s whole year, reports both freezes, and keeps a finished year with both dates certain',async()=>{
 const route=await loadRoute();
 const original=globalThis.fetch;
 try{
  const asked=[];
  globalThis.fetch=async input=>{const url=String(input);asked.push(url);return url.includes('geojson')?json(STATIONS):text(csvOf(year2024()));};
  const response=await route.GET(new Request('https://kfm.test/api/farming/frost-dates?lon=-97.6&lat=38.8&year=2024'));
  assert.equal(response.status,200);
  assert.match(asked.at(-1),/stations=SLN&year1=2024&month1=1&day1=1&year2=2024&month2=12&day2=31/,'the whole year, at the nearest station');
  const body=await response.json();
  assert.equal(body.state,'ready');assert.equal(body.station.id,'SLN');
  assert.equal(body.lastSpring,SPRING);assert.equal(body.firstFall,FALL);
  assert.equal(body.springKnown,true);assert.equal(body.fallKnown,true);
  assert.equal(response.headers.get('cache-control'),'public, max-age=86400, s-maxage=604800','a finished year with both freezes certain is kept a day');
  assert.equal(frost.validFrostDates(body,-97.6,38.8,2024),true,'the page accepts what the route sends');
 }finally{globalThis.fetch=original;}
});

test('an uncertain freeze is not cached, and a source that does not answer gives no frost dates',async()=>{
 const route=await loadRoute();
 const original=globalThis.fetch;
 try{
  globalThis.fetch=async input=>String(input).includes('geojson')?json(STATIONS):text(csvOf(year2024({blank:['2024-10-10']})));
  const uncertain=await route.GET(new Request('https://kfm.test/api/farming/frost-dates?lon=-97.6&lat=38.8&year=2024'));
  assert.equal(uncertain.headers.get('cache-control'),'no-store','an uncertain year is not kept');
  assert.equal((await uncertain.json()).fallKnown,false);
  globalThis.fetch=async()=>new Response('down',{status:503});
  const down=await route.GET(new Request('https://kfm.test/api/farming/frost-dates?lon=-97.6&lat=38.8&year=2024'));
  assert.equal(down.status,502);assert.equal(down.headers.get('cache-control'),'no-store');
  assert.match(await down.text(),/No frost dates are inferred/);
  globalThis.fetch=async input=>String(input).includes('geojson')?json(STATIONS):text(csvOf(year2024({blank:[]})).replace('min_temp_f','low_f'));
  assert.equal((await route.GET(new Request('https://kfm.test/api/farming/frost-dates?lon=-97.6&lat=38.8&year=2024'))).status,502,'an unexpected answer is not read as a year');
 }finally{globalThis.fetch=original;}
 const route2=await loadRoute();
 assert.equal((await route2.GET(new Request('https://kfm.test/api/farming/frost-dates?lon=-97.6&lat=38.8&year=1999'))).status,400,'before 2000');
 assert.equal((await route2.GET(new Request('https://kfm.test/api/farming/frost-dates?lon=-120&lat=38&year=2024'))).status,400,'outside Kansas');
 assert.equal((await route2.GET(new Request('https://kfm.test/api/farming/frost-dates?lon=-97.6&lat=38.8&year=2024&station=SLN'))).status,400,'no other parameters');
});

test('the dock shows the frost dates beside the crops: loading, failed, none, and the reading with its limit',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const base={look:maps.CATEGORY_MAPS.agriculture,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  crops:{on:true,year:2024,years:[2024,2023],reading:'Corn',swatch:null},onCrops(){},onCropsYear(){}};
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,frost:{state:'loading',year:2024,line:null}})),/Reading the year at the nearest Kansas station/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,frost:{state:'failed',year:2024,line:null}})),/No frost dates are inferred/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,frost:{state:'none',year:2024,line:null}})),/No Kansas airport station is within 150 km/);
 const ready=JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,frost:{state:'ready',year:2024,line:'last spring freeze Apr 14 · first fall freeze Oct 21 · 190 frost-free days · from Salina, 3 km away'}}));
 assert.match(ready,/Frost dates, /);assert.match(ready,/click the point again for another year/);assert.match(ready,/last spring freeze Apr 14/);assert.match(ready,/not the field/);
 assert.doesNotMatch(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,frost:null})),/Frost dates, /,'nothing without a click');
});

test('the page reads the frost dates with each click, for the crop year on show, and clears them with the crops',()=>{
 assert.match(page,/readFrostRef\.current\(event\.lngLat\.lng, event\.lngLat\.lat, cropsRef\.current\)/);
 assert.match(page,/frostRequestRef\.current\?\.abort\(\);\s*seasonRainRequestRef\.current\?\.abort\(\);\s*setCropPoint\(null\);/,'turning crops off aborts the reading');
 assert.match(page,/import \{ FROST_API_PATH, frostLine, validFrostDates/);
 assert.match(dockSource,/frost\?: Readonly</);
});
