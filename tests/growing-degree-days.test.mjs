import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness} from './component-harness.mjs';

const esm=async path=>ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const dataUrl=code=>'data:text/javascript;base64,'+Buffer.from(code).toString('base64');
const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const gdd=await compile('app/growing-degree-days.ts');
const maps=await compile('app/category-maps.ts');
const routeSource=await readFile('app/api/farming/degree-days/route.ts','utf8');
const page=await readFile('app/page.tsx','utf8');
const dockSource=await readFile('app/category-map-dock.tsx','utf8');

/** The route with its three local imports inlined, so it runs under node:test without a bundler. */
const loadRoute=async()=>{
  const upstream=await esm('app/api/event-atlas/upstream.ts'), cropland=await esm('app/cropland.ts'), days=await esm('app/growing-degree-days.ts');
  const stations=(await esm('app/kansas-stations.ts')).replace('from "./api/event-atlas/upstream"',`from "${dataUrl(upstream)}"`).replace('from "./growing-degree-days"',`from "${dataUrl(days)}"`);
  const source=(await esm('app/iem-daily-source.ts')).replace('from "./api/event-atlas/upstream"',`from "${dataUrl(upstream)}"`);
  const code=ts.transpileModule(routeSource,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText
    .replace('from "../../../iem-daily-source"',`from "${dataUrl(source)}"`)
    .replace('from "../../event-atlas/upstream"',`from "${dataUrl(upstream)}"`)
    .replace('from "../../../cropland"',`from "${dataUrl(cropland)}"`)
    .replace('from "../../../kansas-stations"',`from "${dataUrl(stations)}"`)
    .replace('from "../../../growing-degree-days"',`from "${dataUrl(days)}"`);
  return import(dataUrl(code));
};
const STATIONS={type:'FeatureCollection',features:[
 {properties:{sid:'SLN',sname:'Salina',network:'KS_ASOS',state:'KS',tzname:'America/Chicago',archive_begin:'1942-11-06',archive_end:null},geometry:{type:'Point',coordinates:[-97.65,38.79]}},
 {properties:{sid:'HYS',sname:'Hays',network:'KS_ASOS',state:'KS',tzname:'America/Chicago',archive_begin:'1948-01-01',archive_end:null},geometry:{type:'Point',coordinates:[-99.27,38.84]}},
]};
const DAILY_HEADER='station,day,max_temp_f,min_temp_f';
const json=(body,status=200)=>new Response(JSON.stringify(body),{status,headers:{'content-type':'application/json'}});
const text=(body,status=200)=>{const lines=body.trimEnd().split('\n'); if(lines[0].startsWith('station,day,')){if(!lines[0].includes('precip_in')){lines[0]+=',precip_in';for(let i=1;i<lines.length;i++)lines[i]+=',M';}lines[0]+=',network';for(let i=1;i<lines.length;i++)lines[i]+=',KS_ASOS';}return new Response(lines.join('\n')+'\n',{status,headers:{'content-type':'text/csv'}});};

test('a day\'s degree days cap the high at 86 °F, floor the low at 50 °F, and never go below zero',()=>{
 assert.equal(gdd.dailyDegreeDays(90,60),23,'capped high 86, low 60: (86+60)/2 − 50');
 assert.equal(gdd.dailyDegreeDays(70,40),10,'low floored at 50: (70+50)/2 − 50');
 assert.equal(gdd.dailyDegreeDays(100,80),33,'both ends capped');
 assert.equal(gdd.dailyDegreeDays(45,30),0,'a cold day counts nothing, not a negative');
 assert.equal(gdd.dailyDegreeDays(null,60),null,'a missing reading is not a zero');
});

test('a season covers every date from April 1 to October 31: an absent date and a blank reading are both missing, never guessed',()=>{
 const dates=gdd.seasonDates(2024);
 assert.equal(dates.length,214);assert.equal(dates[0],'2024-04-01');assert.equal(dates.at(-1),'2024-10-31');
 const season=gdd.seasonDegreeDays([{day:'2024-04-01',maxF:90,minF:60},{day:'2024-04-02',maxF:null,minF:60},{day:'2024-04-03',maxF:70,minF:40}],2024);
 assert.deepEqual(season,{degreeDays:33,daysRead:2,daysMissing:212},'211 absent dates and one blank reading');
});

test('the daily CSV is read by its headers, a missing reading is M or blank, and an unexpected header is refused',()=>{
 const rows=gdd.parseDailyCsv(`${DAILY_HEADER}\nSLN,2024-04-01,90,60\nSLN,2024-04-02,M,40\nSLN,2024-04-03,70,\n`);
 assert.deepEqual(rows,[{day:'2024-04-01',maxF:90,minF:60,precipIn:null},{day:'2024-04-02',maxF:null,minF:40,precipIn:null},{day:'2024-04-03',maxF:70,minF:null,precipIn:null}]);
 assert.throws(()=>gdd.parseDailyCsv('station,date,high\nSLN,2024-04-01,90'),/Unrecognised daily summary columns/);
 assert.throws(()=>gdd.parseDailyCsv(''),/Empty daily summary/);
});

test('the nearest station is chosen, and a point beyond 150 km gets none',()=>{
 const stations=[{id:'SLN',name:'Salina',lon:-97.65,lat:38.79},{id:'HYS',name:'Hays',lon:-99.27,lat:38.84}];
 assert.equal(gdd.nearestStation(stations,-97.6,38.8).id,'SLN');
 assert.equal(gdd.nearestStation(stations,-99.2,38.8).id,'HYS');
 assert.equal(gdd.nearestStation([{id:'SLN',name:'Salina',lon:-97.65,lat:38.79}],-101.5,37.0),null,'beyond 150 km');
});

test('the route reads the nearest station\'s season, reports the days it could not read, and keeps only a complete season',async()=>{
 const route=await loadRoute();
 const original=globalThis.fetch;
 try{
  const asked=[];
  globalThis.fetch=async input=>{const url=String(input);asked.push(url);
   if(url.includes('geojson'))return json(STATIONS);
   return text(`${DAILY_HEADER}\nSLN,2024-04-01,90,60\nSLN,2024-04-02,70,40\nSLN,2024-04-03,M,40\n`);};
  const partial=await route.GET(new Request('https://kfm.test/api/farming/degree-days?lon=-97.6&lat=38.8&year=2024'));
  assert.equal(partial.status,200);
  const body=await partial.json();
  assert.match(asked.at(-1),/stations=SLN&year1=2024&month1=4&day1=1&year2=2024&month2=10&day2=31/,'the nearest station, for April to October');
  assert.equal(body.station.id,'SLN');assert.equal(body.state,'ready');
  assert.equal(body.degreeDays,33);assert.equal(body.daysRead,2);assert.equal(body.daysMissing,212,'the absent dates are counted, not read as a complete season');
  assert.equal(partial.headers.get('cache-control'),'no-store','a season with a missing day is not kept');
  assert.equal(gdd.validDegreeDays(body,-97.6,38.8,2024),true,'the page accepts what the route sends');

  const everyDay=gdd.seasonDates(2024).map(date=>`SLN,${date},80,60,0.1`).join('\n');
  globalThis.fetch=async input=>String(input).includes('geojson')?json(STATIONS):text(`${DAILY_HEADER},precip_in\n${everyDay}\n`);
  const complete=await route.GET(new Request('https://kfm.test/api/farming/degree-days?lon=-97.6&lat=38.8&year=2024'));
  assert.equal(complete.headers.get('cache-control'),'public, max-age=86400, s-maxage=86400','a season with every day read is kept a day');
 }finally{globalThis.fetch=original;}
});

test('a point with no station in reach says so, and a source that does not answer gives no degree days',async()=>{
 const route=await loadRoute();
 const original=globalThis.fetch;
 try{
  globalThis.fetch=async input=>String(input).includes('geojson')?json(STATIONS):text('');
  const far=await(await route.GET(new Request('https://kfm.test/api/farming/degree-days?lon=-101.5&lat=37.0&year=2024'))).json();
  assert.equal(far.state,'none');assert.equal(far.station,null);assert.equal(far.degreeDays,null);

  globalThis.fetch=async()=>new Response('down',{status:503});
  const down=await route.GET(new Request('https://kfm.test/api/farming/degree-days?lon=-97.6&lat=38.8&year=2024'));
  assert.equal(down.status,502);assert.equal(down.headers.get('cache-control'),'no-store');
  assert.match(await down.text(),/No growing degree days are inferred/);

  globalThis.fetch=async input=>String(input).includes('geojson')?json(STATIONS):text('station,date,high\nSLN,2024-04-01,90');
  assert.equal((await route.GET(new Request('https://kfm.test/api/farming/degree-days?lon=-97.6&lat=38.8&year=2024'))).status,502,'an unexpected answer is not read as an empty season');
 }finally{globalThis.fetch=original;}
 const route2=await loadRoute();
 assert.equal((await route2.GET(new Request('https://kfm.test/api/farming/degree-days?lon=-97.6&lat=38.8&year=1999'))).status,400,'before 2000');
 assert.equal((await route2.GET(new Request('https://kfm.test/api/farming/degree-days?lon=-120&lat=38&year=2024'))).status,400,'outside Kansas');
 assert.equal((await route2.GET(new Request('https://kfm.test/api/farming/degree-days?lon=-97.6&lat=38.8&year=2024&station=SLN'))).status,400,'no other parameters');
});

test('the dock shows the reading beside the crops, with its station and its limit, and the failure and no-station messages',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const base={look:maps.CATEGORY_MAPS.agriculture,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  crops:{on:true,year:2024,years:[2024,2023],reading:'Corn',swatch:null},onCrops(){},onCropsYear(){}};
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,degreeDays:{state:'loading',year:2024,line:null}})),/Reading the season at the nearest Kansas station/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,degreeDays:{state:'failed',year:2024,line:null}})),/No growing degree days are inferred/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,degreeDays:{state:'none',year:2024,line:null}})),/No Kansas airport station is within 150 km/);
 const ready=JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,degreeDays:{state:'ready',year:2024,line:'33 growing degree days, base 50 °F, capped at 86 °F, Apr 1–Oct 31 2024 · from Salina, 3 km away · 2 days read, 1 missing',rain:'Partial: 0.75 in precipitation, Apr 1–Oct 31 2024 · 212 days missing'}}));
 assert.match(ready,/33 growing degree days/);assert.match(ready,/0\.75 in precipitation/);assert.match(ready,/A station reading, not the field/);
 assert.doesNotMatch(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,degreeDays:null})),/Growing degree days, 2024/,'nothing without a click');
});

test('the page reads the degree days with each click, for the crop year on show, and clears them with the crops',()=>{
 assert.match(page,/readDegreeDaysRef\.current\(event\.lngLat\.lng, event\.lngLat\.lat, cropsRef\.current\)/);
 assert.match(page,/degreeDaysRequestRef\.current\?\.abort\(\);\n    frostRequestRef\.current\?\.abort\(\);\n    seasonRainRequestRef\.current\?\.abort\(\);\n    setCropPoint\(null\);/,'turning crops off aborts the reading');
 assert.match(page,/import \{ GDD_API_PATH, degreeDaysLine, rainLine, validDegreeDays/);
 assert.match(dockSource,/degreeDays\?: Readonly</);
});

test('season rainfall totals the inches over every date of the season, and counts an absent or blank day as missing',()=>{
 const rain=gdd.seasonRainfall([{day:'2024-04-01',maxF:80,minF:60,precipIn:0.5},{day:'2024-04-02',maxF:80,minF:60,precipIn:0.25},{day:'2024-04-03',maxF:80,minF:60,precipIn:null}],2024);
 assert.deepEqual(rain,{inches:0.75,daysRead:2,daysMissing:212,traceDays:0});
 assert.equal(gdd.seasonRainfall([],2024).daysMissing,214,'no precipitation column reads as every day missing');
});

test('the daily CSV reads precipitation when the column is there, and reads none when it is not',()=>{
 const withRain=gdd.parseDailyCsv(`${DAILY_HEADER},precip_in\nSLN,2024-04-01,90,60,M\nSLN,2024-04-02,70,40,0.3\n`);
 assert.deepEqual(withRain.map(d=>d.precipIn),[null,0.3]);
 assert.deepEqual(gdd.parseDailyCsv(`${DAILY_HEADER}\nSLN,2024-04-01,90,60\n`).map(d=>d.precipIn),[null]);
});

test('the rain line says the inches and whether every day was read',()=>{
 const reading={lon:-97.6,lat:38.8,retrievedAt:'2026-10-30T18:00:00Z',year:2024,state:'ready',station:{id:'SLN',name:'Salina',km:3},degreeDays:33,daysRead:2,daysMissing:212,rainInches:0.75,rainDaysMissing:212};
 assert.equal(gdd.rainLine(reading),'Partial: 0.75 in precipitation, Apr 1–Oct 31 2024 · 212 days missing');
 assert.match(gdd.rainLine({...reading,rainInches:null}),/unavailable/,'no rain read is not zero');
});

test('the route reports the season rain and keeps it out of the cache while any day is missing',async()=>{
 const route=await loadRoute();
 const original=globalThis.fetch;
 try{
  globalThis.fetch=async input=>String(input).includes('geojson')?json(STATIONS):text(`${DAILY_HEADER},precip_in\nSLN,2024-04-01,90,60,0.5\nSLN,2024-04-02,70,40,0.25\n`);
  const response=await route.GET(new Request('https://kfm.test/api/farming/degree-days?lon=-97.6&lat=38.8&year=2024'));
  const body=await response.json();
  assert.equal(body.rainInches,0.75);assert.equal(body.rainDaysMissing,212);
  assert.equal(response.headers.get('cache-control'),'no-store');
  assert.equal(gdd.validDegreeDays(body,-97.6,38.8,2024),true,'the page accepts the rain fields');
 }finally{globalThis.fetch=original;}
});
