import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const cropland=await compile('app/cropland.ts');
const ch=await compile('app/crop-history.ts',{'./cropland':cropland,'./map-keys':{}});
const maps=await compile('app/category-maps.ts');
const dockSource=await readFile('app/category-map-dock.tsx','utf8');
const page=await readFile('app/page.tsx','utf8');
const route=await readFile('app/api/cropland/history/route.ts','utf8');
const plain=v=>JSON.parse(JSON.stringify(v));

const CODE={corn:1,sorghum:4,soybeans:5,sunflower:6,wheat:24,double:26,hay:36,fallow:61,grass:176,forest:141,water:111};
const year=(y,family,state)=>({year:y,state:state??(family?'ready':'none'),crop:family?{value:CODE[family],category:family,color:'#000000'}:null});
// A run of families, one per year from 2008.
const history=families=>families.map((f,i)=>{const failed=f==='!';return year(2008+i,failed?null:f,failed?'failed':undefined);});
const pattern=families=>ch.rotationPattern(history(families));

test('crop families group the CDL classes, and their colours agree with the map\'s legend',()=>{
 assert.equal(ch.familyOf(1),'corn');assert.equal(ch.familyOf(176),'grass');assert.equal(ch.familyOf(141),'other','forest is another class');
 for(const entry of cropland.CDL_MAIN_CLASSES){const family=ch.familyOf(entry.value);if(family!=='other')assert.equal(ch.CROP_FAMILIES[family].color,entry.color,entry.name);}
 // The dock keeps its own copy of the colours (it imports types only); the copy must match the module.
 for(const [family,{color}] of Object.entries(ch.CROP_FAMILIES)){assert.match(dockSource,new RegExp(`"?${family}"?: "${color}"`),family);}
});

test('a corn and soybean rotation is read where the two alternate, and continuous corn where corn dominates',()=>{
 const alternating=pattern(['corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn']);
 assert.equal(alternating.label,'Corn–soybean rotation');
 assert.match(alternating.detail,/^16 of 16 corn and soybean years alternate · 17 years read · corn 9, soybeans 8 · 16 changes of crop$/);
 const continuous=pattern([...Array(16).fill('corn'),'soybeans']);
 assert.equal(continuous.label,'Continuous corn');assert.match(continuous.detail,/^Corn in 94% of years/);
 // Corn and soybeans appear in turn, but the pairs do not alternate: no rotation is claimed.
 const repeated=pattern(['corn','corn','corn','soybeans','soybeans','soybeans','corn','corn','corn','soybeans','soybeans','soybeans','corn','corn','corn','soybeans','soybeans']);
 assert.notEqual(repeated.label,'Corn–soybean rotation');
});

test('grassland and dominant families are read, and a field with no clear pattern is mixed',()=>{
 const pasture=pattern([...Array(15).fill('grass'),'wheat','hay']);
 assert.equal(pasture.label,'Grassland or pasture');assert.match(pasture.detail,/^Grass in 88% of years/);
 const wheat=pattern(['wheat','wheat','wheat','wheat','wheat','wheat','wheat','wheat','wheat','wheat','wheat','wheat','corn','soybeans','sorghum','hay','fallow']);
 assert.equal(wheat.label,'Mostly winter wheat');
 const mixed=pattern(['corn','sorghum','hay','soybeans','wheat','fallow','sunflower','corn','sorghum','hay','soybeans','wheat','fallow','sunflower','corn','sorghum','hay']);
 assert.equal(mixed.label,'Mixed cropping');
});

test('too few classified years read no pattern; unanswered years are counted apart and do not count as absences',()=>{
 const few=pattern(['corn','soybeans','corn','soybeans']);
 assert.equal(few.label,'Too few years to read a pattern');assert.equal(few.classified,4);
 const partial=pattern(['corn','soybeans','!','corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans']);
 assert.equal(partial.failed,1);assert.equal(partial.classified,10);assert.equal(partial.label,'Corn–soybean rotation');
 assert.match(partial.detail,/9 of 9 corn and soybean years alternate · 10 years read, 1 unanswered/);
 // A year with no class is not an absence of cropping, and is not read as one.
 const gaps=ch.rotationPattern([...history(['corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans'])]);
 assert.equal(gaps.classified,10);
});

test('the bars, the labels and the reading',()=>{
 const h={lon:-98.1,lat:38.2,retrievedAt:'x',years:[year(2008,'corn'),year(2009,null),year(2010,'grass','ready'),{year:2011,state:'failed',crop:null}]};
 const bars=ch.historyBars(h);
 assert.deepEqual(plain(bars.map(b=>[b.year,b.family,b.state,b.label])),[[2008,'corn','ready','corn (1)'],[2009,null,'none','no class here'],[2010,'grass','ready','grassland or pasture (176)'],[2011,null,'failed','not answered']]);
 const pattern=ch.rotationPattern(h.years);
 assert.equal(ch.cropHistoryReading(h,pattern),`${pattern.label} at 38.200°N, 98.100°W · 2008–2024 · ${pattern.detail}`);
 assert.equal(ch.CROP_HISTORY_API_PATH(-98.1,38.2),'/api/cropland/history?lon=-98.10000&lat=38.20000');
 assert.equal(ch.validCropHistory(h,-98.1,38.2),true);assert.equal(ch.validCropHistory(h,-98.2,38.2),false,'another point');
 assert.equal(ch.cropHistoryKey().items.length,9,'every family but other');
});

test('the route reads every CDL year at a point, a few at a time, and keeps a complete answer a day',async()=>{
 const original=globalThis.fetch;
 try{
  const asked=[];
  globalThis.fetch=async input=>{const url=String(input);asked.push(url);const y=Number(new URL(url).searchParams.get('year'));
   if(y===2010)return new Response('no answer',{status:503});
   return new Response(`{value: "${y%2?1:5}", category: "${y%2?'Corn':'Soybeans'}", color: "${y%2?'#ffd300':'#267000'}"}`);};
  const handler=await import('data:text/javascript;base64,'+Buffer.from(ts.transpileModule(route.replace('from "../../event-atlas/upstream"','from "data:text/javascript;base64,'+Buffer.from(ts.transpileModule(await readFile('app/api/event-atlas/upstream.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')+'"').replace('from "../../../cropland"','from "data:text/javascript;base64,'+Buffer.from(ts.transpileModule(await readFile('app/cropland.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')+'"'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64'));
  const bad=await handler.GET(new Request('https://kfm.test/api/cropland/history?lon=-120&lat=38'));assert.equal(bad.status,400);
  const extra=await handler.GET(new Request('https://kfm.test/api/cropland/history?lon=-98&lat=38&year=2010'));assert.equal(extra.status,400,'no other parameters');
  const first=await handler.GET(new Request('https://kfm.test/api/cropland/history?lon=-98.1&lat=38.2'));
  assert.equal(first.status,200);const body=await first.json();
  assert.equal(body.years.length,17);assert.deepEqual(body.years.map(y=>y.year),[...Array(17)].map((_,i)=>2008+i));
  assert.equal(body.years.find(y=>y.year===2010).state,'failed','an unanswered year is failed, not empty');
  assert.equal(body.years.find(y=>y.year===2009).crop.category,'Corn');
  assert.equal(asked.length,17,'every year asked once');
  assert.equal(first.headers.get('cache-control'),'no-store','a partial answer is not cached');
  await handler.GET(new Request('https://kfm.test/api/cropland/history?lon=-98.1&lat=38.2'));
  assert.equal(asked.length,34,'a partial answer is asked again');
 }finally{globalThis.fetch=original;}
 assert.match(route,/CONCURRENCY = 4/);
 assert.match(route,/Only a complete answer is kept/);
 // Codex on #5603: a key at four decimals served one click's body to a nearby click, which the page then rejected.
 assert.match(route,/const key = `\$\{lon\.toFixed\(5\)\},\$\{lat\.toFixed\(5\)\}`/);
});

test('the dock draws the history beside the year: loading, failed, and the timeline with its pattern and key',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const base={look:maps.CATEGORY_MAPS.agriculture,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  crops:{on:true,year:2024,years:[2024,2023],reading:'Corn',swatch:null,},onCrops(){},onCropsYear(){}};
 const bars=ch.historyBars({lon:0,lat:0,retrievedAt:'x',years:history(['corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn'])});
 const pattern=ch.rotationPattern(history(['corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn','soybeans','corn']));
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,history:{state:'loading',bars:[],pattern:null,reading:null}})),/Reading every CDL year at this point/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,history:{state:'failed',bars:[],pattern:null,reading:null}})),/CropScape did not answer for this point/);
 const partialBars=[...bars.slice(0,3),{year:2011,family:null,state:'failed',label:'not answered'},...bars.slice(4)];
 const partialText=JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,history:{state:'partial',bars:partialBars,pattern:null,reading:null}}));
 assert.match(partialText,/\(dashed\)\./);assert.match(partialText,/No pattern is read from a partial history/);
 assert.doesNotMatch(partialText,/Corn–soybean rotation/,'no pattern from a partial history');
 assert.ok(findNode(h.render(h.exports.CategoryMapDock,{...base,history:{state:'partial',bars:partialBars,pattern:null,reading:null}}),n=>n.type===h.exports.CropHistoryTimeline),'the years that were read are still drawn');
 const tree=h.render(h.exports.CategoryMapDock,{...base,history:{state:'ready',bars,pattern,reading:ch.cropHistoryReading({lon:0,lat:0,retrievedAt:'x',years:[]},pattern)}});
 const text=JSON.stringify(tree);
 assert.match(text,/Corn–soybean rotation/);assert.equal(text.split('Corn–soybean rotation').length-1,1,'the pattern is named once');
 const timeline=findNode(tree,n=>n.type===h.exports.CropHistoryTimeline);const figure=timeline.type(timeline.props);
 assert.match(figure.props['aria-label'],/^Crop history, 2008 to 2024: 2008 corn \(1\); 2009 soybeans \(5\)/);
 assert.equal((JSON.stringify(figure).match(/"data-year"/g)||[]).length,17);
 assert.match(JSON.stringify(figure),/"fill":"#ffd300"/);
 assert.doesNotMatch(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,crops:{...base.crops,on:false},history:{state:'ready',bars,pattern,reading:'x'}})),/category-map-dock-crop-history/,'no history with crops off');
 assert.match(page,/history=\{activeCategoryMap\.tools\?\.includes\("crops"\)/);
 assert.match(page,/readCropHistoryRef\.current\(event\.lngLat\.lng, event\.lngLat\.lat\);/,'a click reads the whole history');
 // The route answers with the point to five decimals; the page must hold that same point or every answer fails validation.
 assert.match(page,/const lon = Number\(clickLon\.toFixed\(5\)\), lat = Number\(clickLat\.toFixed\(5\)\);/);
 assert.equal(ch.validCropHistory({lon:Number((-98.1234567).toFixed(5)),lat:38.2,years:[]},Number((-98.1234567).toFixed(5)),38.2),true);

 assert.match(page,/cropHistoryRequestRef\.current\?\.abort\(\);\s*surveySoilRequestRef\.current\?\.abort\(\);\s*degreeDaysRequestRef\.current\?\.abort\(\);\s*frostRequestRef\.current\?\.abort\(\);\s*seasonRainRequestRef\.current\?\.abort\(\);\s*setCropPoint\(null\);\s*setCropHistory\(null\);\s*setSurveySoil\(null\);\s*setDegreeDays\(null\);\s*setFrostDates\(null\);\s*setSeasonRain\(null\);\s*\};/,'turning crops off clears it');
 assert.match(page,/\.\.\.\(cropsOn && cropHistory\?\.data \? \[cropHistoryKey\(\)\] : \[\]\)/);
 assert.doesNotMatch(page,/readCropHistory\(\w+, \w+\); \/\/ years/,'years do not refetch the history');
});
