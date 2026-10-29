import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const orientation=await compile('app/kansas-orientation.ts');
const spc=await compile('app/spc-outlook.ts',{'./kansas-orientation':orientation});
const sr=await compile('app/storm-reports.ts');
const ver=await compile('app/outlook-verification.ts',{'./spc-outlook':spc,'./storm-reports':sr});
const page=await readFile('app/page.tsx','utf8');

const box=(w,s,e,n)=>[[[w,s],[e,s],[e,n],[w,n],[w,s]]];
const props=(label,extra={})=>({LABEL:label,ISSUE:'202610281630',VALID:'202610281630',EXPIRE:'202610291200',...extra});
// A categorical Day 1 outlook: Marginal over south-central Kansas with Slight inside it.
const cat=spc.parseSpcOutlook({type:'FeatureCollection',features:[
 {type:'Feature',geometry:{type:'Polygon',coordinates:box(-101,35,-94,40)},properties:props('TSTM')},
 {type:'Feature',geometry:{type:'Polygon',coordinates:box(-100,36,-95,39)},properties:props('MRGL')},
 {type:'Feature',geometry:{type:'Polygon',coordinates:box(-99,37,-97,38.5)},properties:props('SLGT')},
]},1,'2026-10-28T17:00:00.000Z','src');
const now=new Date('2026-10-29T03:00:00Z');
const csv=['Time,F_Scale,Location,County,State,Lat,Lon,Comments',
 '2215,EF1,A,A,KS,37.8,-98.0,in Slight',
 '1500,UNK,B,B,KS,37.8,-98.0,before the outlook began',
 'Time,Speed,Location,County,State,Lat,Lon,Comments',
 '2300,UNK,C,C,KS,38.8,-96.0,in Marginal only',
 '0130,70,D,D,MO,38.9,-92.0,outside every area',
 'Time,Size,Location,County,State,Lat,Lon,Comments',
 '2245,175,E,E,KS,37.5,-98.5,in Slight',
 ''].join('\n');
const reports=sr.parseStormReports(csv,'today',now,'src');

test('the band at a point is the highest SPC area that holds it',()=>{
 assert.equal(spc.outlookBandAt(cat,-98,37.8).id,'SLGT');
 assert.equal(spc.outlookBandAt(cat,-96,38.8).id,'MRGL');
 assert.equal(spc.outlookBandAt(cat,-100.5,39.5).id,'TSTM');
 assert.equal(spc.outlookBandAt(cat,-80,30),null);
});

test('the categorical outlook is checked against every report made in its valid period, by nested band',()=>{
 const v=ver.verifyOutlook(cat,reports);
 assert.equal(v.total,4,'the 15:00 report came before the 16:30 outlook');
 assert.deepEqual(JSON.parse(JSON.stringify(v.bands)),[{id:'MRGL',name:'Marginal',count:3},{id:'SLGT',name:'Slight',count:2},{id:'ENH',name:'Enhanced',count:0},{id:'MDT',name:'Moderate',count:0},{id:'HIGH',name:'High',count:0}]);
 assert.equal(ver.verificationReading(v,'cat'),"4 reports since the outlook's 16:30 UTC start: 3 in Marginal or higher, 2 in Slight or higher; 1 outside every risk area");
});

test('a hazard outlook is checked against its own hazard only',()=>{
 const torn=spc.parseSpcOutlook({type:'FeatureCollection',features:[
  {type:'Feature',geometry:{type:'Polygon',coordinates:box(-100,36,-95,39)},properties:props('0.02',{DN:2})},
  {type:'Feature',geometry:{type:'Polygon',coordinates:box(-99,37,-97,38.5)},properties:props('0.05',{DN:5})},
 ]},1,'2026-10-28T17:00:00.000Z','src','torn');
 const v=ver.verifyOutlook(torn,reports);
 assert.equal(v.total,1);assert.equal(v.kind,'torn');
 assert.equal(ver.verificationReading(v,'torn'),"1 tornado report since the outlook's 16:30 UTC start: 1 in 2%+, 1 in 5%+");
 const none=ver.verifyOutlook(torn,{...reports,reports:[]});
 assert.equal(ver.verificationReading(none,'torn'),"No tornado reports yet since the outlook's 16:30 UTC start");
});

test('only the Day 1 outlook and today\'s reports for the same convective day are compared',()=>{
 assert.equal(ver.verifyOutlook({...cat,day:2},reports),null);
 assert.equal(ver.verifyOutlook(cat,{...reports,day:'yesterday'}),null);
 assert.equal(ver.verifyOutlook({...cat,validUntil:'2026-10-30T12:00:00.000Z'},reports),null,'a different day');
 assert.equal(ver.verifyOutlook({...cat,validFrom:null},reports),null);
});

test('the dock shows the check under the reports reading, and the page computes it from both on the map',async()=>{
 const maps=await compile('app/category-maps.ts');
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const base={look:maps.categoryMap('weather'),mode:'2d',depth:1,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},onReports(){},onReportClear(){}};
 const on={day:'today',loading:false,failed:false,reading:'Kansas: 3 reports',url:'u',selected:null};
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,reports:{...on,verification:'4 reports since the outlook'}})),/4 reports since the outlook/);
 assert.doesNotMatch(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,reports:{...on,verification:null}})),/since the outlook/);
 h.dispose?.();
 assert.match(page,/const check = shownOutlook && shownReports \? verifyOutlook\(shownOutlook, shownReports\) : null;/);
 assert.match(page,/url: STORM_REPORTS_PAGE, verification: outlookCheck,/);
});


test('high-wind report comparison retains 75% and 90% while respecting forecast clocks and hazard identity',()=>{
 const wind=spc.parseSpcOutlook({type:'FeatureCollection',features:[
  {type:'Feature',geometry:{type:'Polygon',coordinates:box(-103,37.2,-99,39)},properties:props('0.75',{DN:75})},
  {type:'Feature',geometry:{type:'Polygon',coordinates:box(-103,38.2,-99,38.8)},properties:props('0.90',{DN:90})},
 ]},1,'2026-10-28T17:00:00.000Z','synthetic-wind','wind');
 const raw=['Time,F_Scale,Location,County,State,Lat,Lon,Comments',
  '1700,EF1,Test,Test,KS,38.5,-100,tornado is a different hazard',
  'Time,Speed,Location,County,State,Lat,Lon,Comments',
  '1629,70,Test,Test,KS,38.5,-100,before the forecast valid start',
  '1630,70,Test,Test,KS,38.5,-100,at valid start in 90 percent',
  '2300,70,Test,Test,KS,37.5,-100,in 75 percent only',''].join('\n');
 const parsed=sr.parseStormReports(raw,'today',now,'synthetic-reports');
 const afterExpiry={...parsed.reports.find(r=>r.kind==='wind'),id:'after-expiry',time:'2026-10-29T12:00:01.000Z'};
 const observed={...parsed,reports:[...parsed.reports,afterExpiry]};
 const check=ver.verifyOutlook(wind,observed);
 assert.equal(check.total,2,'only wind reports within the forecast period count');
 assert.deepEqual(check.bands.map(b=>[b.id,b.count]),[['5',2],['15',2],['30',2],['45',2],['60',2],['75',2],['90',1]]);
 assert.equal(ver.verificationReading(check,'wind'),"2 wind reports since the outlook's 16:30 UTC start: 2 in 5%+, 2 in 15%+, 2 in 30%+, 2 in 45%+, 2 in 60%+, 2 in 75%+, 1 in 90%+");
 assert.equal(wind.kansas,'90','observations do not replace the forecast maximum');
 assert.equal(wind.data.features.length,2,'report comparison leaves forecast geometry unchanged');
 assert.equal(ver.verifyOutlook({...wind,validFrom:null},observed),null);
 assert.equal(ver.verifyOutlook({...wind,validUntil:'invalid'},observed),null);
 assert.equal(ver.verifyOutlook({...wind,day:2},observed),null);
});
