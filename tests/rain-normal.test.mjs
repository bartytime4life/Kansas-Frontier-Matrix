import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness} from './component-harness.mjs';

const esm=async path=>ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const dataUrl=code=>'data:text/javascript;base64,'+Buffer.from(code).toString('base64');
const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const rn=await compile('app/rain-normal.ts');
const maps=await compile('app/category-maps.ts');
const routeSource=await readFile('app/api/farming/rain-normal/route.ts','utf8');
const page=await readFile('app/page.tsx','utf8');
const dockSource=await readFile('app/category-map-dock.tsx','utf8');

/** The route with its local imports inlined, so it runs under node:test without a bundler. */
const loadRoute=async()=>{
  const upstream=await esm('app/api/event-atlas/upstream.ts'), cropland=await esm('app/cropland.ts'), days=await esm('app/growing-degree-days.ts'), normal=await esm('app/rain-normal.ts');
  const stations=(await esm('app/kansas-stations.ts')).replace('from "./api/event-atlas/upstream"',`from "${dataUrl(upstream)}"`).replace('from "./growing-degree-days"',`from "${dataUrl(days)}"`);
  const source=(await esm('app/iem-daily-source.ts')).replace('from "./api/event-atlas/upstream"',`from "${dataUrl(upstream)}"`);
  const code=ts.transpileModule(routeSource,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText
    .replace('from "../../../iem-daily-source"',`from "${dataUrl(source)}"`)
    .replace('from "../../event-atlas/upstream"',`from "${dataUrl(upstream)}"`)
    .replace('from "../../../cropland"',`from "${dataUrl(cropland)}"`)
    .replace('from "../../../kansas-stations"',`from "${dataUrl(stations)}"`)
    .replace('from "../../../growing-degree-days"',`from "${dataUrl(days)}"`)
    .replace('from "../../../rain-normal"',`from "${dataUrl(normal)}"`);
  return import(dataUrl(code));
};
const STATIONS={type:'FeatureCollection',features:[
 {properties:{sid:'SLN',sname:'Salina',network:'KS_ASOS',state:'KS',tzname:'America/Chicago',archive_begin:'1942-01-01',archive_end:null},geometry:{type:'Point',coordinates:[-97.65,38.79]}},
 {properties:{sid:'HYS',sname:'Hays',network:'KS_ASOS',state:'KS',tzname:'America/Chicago',archive_begin:'1942-01-01',archive_end:null},geometry:{type:'Point',coordinates:[-99.27,38.84]}},
]};
const json=(body,status=200)=>new Response(JSON.stringify(body),{status,headers:{'content-type':'application/json'}});
const text=(body,status=200)=>new Response(body,{status,headers:{'content-type':'text/csv'}});
/** The April 1 to October 31 dates of a year, each with a rain reading of `inches`. */
const season=(year,inches)=>{const rows=['station,day,max_temp_f,min_temp_f,precip_in,network'];for(let t=Date.UTC(year,3,1);t<=Date.UTC(year,9,31);t+=86_400_000){rows.push(`SLN,${new Date(t).toISOString().slice(0,10)},70,50,${inches},KS_ASOS`);}return rows.join('\n')+'\n';};

test('the normal is the ten years before the year on show',()=>{
 assert.deepEqual(rn.normalYears(2024),[2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]);
});

test('the normal averages the complete earlier years, leaves out a year with a missing day, and reads none with too few',()=>{
 const years=[2014,2015,2016,2017,2018,2019].map(year=>({year,inches:20,daysMissing:0}));
 assert.deepEqual(rn.rainNormal(years),{average:20,years:6});
 const withGap=[...years,{year:2020,inches:99,daysMissing:3}];
 assert.deepEqual(rn.rainNormal(withGap),{average:20,years:6},'a year with a missing day is left out, not counted');
 assert.deepEqual(rn.rainNormal(years.slice(0,4)),{average:null,years:4},'four years are too few for a normal');
});

test('a season is a percentage of the normal, and none without one',()=>{
 assert.equal(rn.percentOfNormal(10.7,21.4),50);
 assert.equal(rn.percentOfNormal(10.7,null),null);
});

test('the line says the season, the normal and the share of it, or that there is no normal',()=>{
 const station={id:'SLN',name:'Salina',km:3};
 const reading={lon:-97.6,lat:38.8,retrievedAt:'2026-10-30T00:00:00Z',year:2024,state:'ready',station,seasonInches:10.7,seasonDaysMissing:0,normal:{average:21.4,years:9},percentOfNormal:50};
 assert.equal(rn.rainNormalLine(reading),'10.70 in precipitation, Apr 1–Oct 31 2024 · 9-year average 21.40 in · 50% of earlier-year average · from Salina, 3 km away');
 assert.match(rn.rainNormalLine({...reading,normal:{average:null,years:3},percentOfNormal:null}),/no earlier-year average: 3 of 10 earlier years are complete, and 5 are needed/);
 assert.match(rn.rainNormalLine({...reading,seasonDaysMissing:2,percentOfNormal:null}),/\(2 days missing\)/);
 assert.equal(rn.validRainNormal(reading,-97.6,38.8,2024),true,'the page accepts the reading');
});

test('the route reads the season and the ten years before it, leaves out a year it cannot read, and keeps each complete season',async()=>{
 const route=await loadRoute();
 const original=globalThis.fetch;
 try{
  const asked=[];
  globalThis.fetch=async input=>{const url=String(input);
   if(url.includes('geojson'))return json(STATIONS);
   const year=Number(new URL(url).searchParams.get('year1'));asked.push(year);
   if(year===2019)return new Response('down',{status:503});
   return text(season(year,year===2024?0.05:0.1));};
  const response=await route.GET(new Request('https://kfm.test/api/farming/rain-normal?lon=-97.6&lat=38.8&year=2024'));
  assert.equal(response.status,200);
  const body=await response.json();
  assert.equal(body.station.id,'SLN');assert.equal(body.state,'ready');
  assert.equal(body.seasonInches,10.7,'the season, 214 days at 0.05 in');
  assert.equal(body.normal.years,9,'2019 cannot be read, so nine earlier years are averaged');
  assert.equal(body.normal.average,21.4);
  assert.equal(body.percentOfNormal,50);
  assert.equal(rn.validRainNormal(body,-97.6,38.8,2024),true);
  assert.equal(asked.length,11,'the season and the ten earlier years are asked for once each');
  asked.length=0;
  await route.GET(new Request('https://kfm.test/api/farming/rain-normal?lon=-97.6&lat=38.8&year=2024'));
  assert.deepEqual(asked,[2019],'only the year that could not be read is asked for again: each complete season is kept');
 }finally{globalThis.fetch=original;}
});

test('a point with no station in reach says so, and a bad request is refused',async()=>{
 const route=await loadRoute();
 const original=globalThis.fetch;
 try{
  globalThis.fetch=async input=>String(input).includes('geojson')?json({type:'FeatureCollection',features:[STATIONS.features[0]]}):text('');
  const far=await(await route.GET(new Request('https://kfm.test/api/farming/rain-normal?lon=-101.5&lat=37.0&year=2024'))).json();
  assert.equal(far.state,'none');assert.equal(far.station,null);
  globalThis.fetch=async()=>new Response('down',{status:503});
  const down=await route.GET(new Request('https://kfm.test/api/farming/rain-normal?lon=-97.6&lat=38.8&year=2003'));
  assert.equal(down.status,502);assert.equal(down.headers.get('cache-control'),'no-store');
 }finally{globalThis.fetch=original;}
 const route2=await loadRoute();
 assert.equal((await route2.GET(new Request('https://kfm.test/api/farming/rain-normal?lon=-97.6&lat=38.8&year=1999'))).status,400,'before 2000');
 assert.equal((await route2.GET(new Request('https://kfm.test/api/farming/rain-normal?lon=-120&lat=38&year=2024'))).status,400,'outside Kansas');
 assert.equal((await route2.GET(new Request('https://kfm.test/api/farming/rain-normal?lon=-97.6&lat=38.8&year=2024&station=SLN'))).status,400,'no other parameters');
});

test('the dock shows the season against normal beside the crops: loading, failed, none, and the reading with its limit',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const base={look:maps.CATEGORY_MAPS.agriculture,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  crops:{on:true,year:2024,years:[2024,2023],reading:'Corn',swatch:null},onCrops(){},onCropsYear(){}};
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,seasonRain:{state:'loading',year:2024,line:null}})),/Reading the season and the ten years before it/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,seasonRain:{state:'failed',year:2024,line:null}})),/No rain normal is inferred/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,seasonRain:{state:'none',year:2024,line:null}})),/No eligible Kansas airport station is within 150 km/);
 const ready=JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,seasonRain:{state:'ready',year:2024,line:'10.70 in precipitation, Apr 1–Oct 31 2024 · 9-year average 21.40 in · 50% of earlier-year average · from Salina, 3 km away'}}));
 assert.match(ready,/Season rain, /);assert.match(ready,/50% of earlier-year average/);assert.match(ready,/A station's precipitation, not the field/);
 assert.doesNotMatch(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,seasonRain:null})),/Season rain, /,'nothing without a click');
});

test('the page reads the season against normal with each click, for the crop year on show, and clears it with the crops',()=>{
 assert.match(page,/readSeasonRainRef\.current\(event\.lngLat\.lng, event\.lngLat\.lat, cropsRef\.current\)/);
 assert.match(page,/seasonRainRequestRef\.current\?\.abort\(\);\s*setCropPoint\(null\);/,'turning crops off aborts the reading');
 assert.match(page,/import \{ RAIN_NORMAL_API_PATH, rainNormalLine, validRainNormal/);
 assert.match(dockSource,/seasonRain\?: Readonly</);
});
