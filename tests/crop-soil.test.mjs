import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness} from './component-harness.mjs';

const esm=async path=>ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const dataUrl=code=>'data:text/javascript;base64,'+Buffer.from(code).toString('base64');
const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const soil=await compile('app/crop-soil.ts');
const maps=await compile('app/category-maps.ts');
const routeSource=await readFile('app/api/cropland/soil/route.ts','utf8');
const page=await readFile('app/page.tsx','utf8');
const dockSource=await readFile('app/category-map-dock.tsx','utf8');

/** The route with its two local imports inlined, so it runs under node:test without a bundler. */
const loadRoute=async()=>{
  const bounded=await esm('app/bounded-json.ts'), cropland=await esm('app/cropland.ts');
  const code=ts.transpileModule(routeSource,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText
    .replace('from "../../../bounded-json"',`from "${dataUrl(bounded)}"`).replace('from "../../../cropland"',`from "${dataUrl(cropland)}"`);
  return import(dataUrl(code));
};
const NAMES=['mukey','muname','compname','comppct_r','majcompflag','drainagecl','hydgrp','nirrcapcl','aws0150wta'];
const sda=rows=>new Response(JSON.stringify({Table:[NAMES,...rows]}),{status:200,headers:{'content-type':'application/json'}});
const component=(mukey,muname,compname,pct,major,drainage,hg,cap,aws)=>[mukey,muname,compname,pct,major,drainage,hg,cap,aws];

test('a soil reading is checked against its point, and each component against its fields',()=>{
 const reading={lon:-98.1,lat:38.2,retrievedAt:'x',state:'ready',mapUnit:{key:'1',name:'Ellsworth silt loam'},components:[
  {name:'Ellsworth',percent:85,major:true,drainage:'Moderately well drained',hydrologicGroup:'C',capability:2,waterStorageCm:18.4}]};
 assert.equal(soil.validSoil(reading,-98.1,38.2),true);
 assert.equal(soil.validSoil(reading,-98.2,38.2),false,'another point');
 assert.equal(soil.validSoil({...reading,components:[{...reading.components[0],percent:'85'}]},-98.1,38.2),false,'a percentage that is text');
 assert.equal(soil.validSoil({...reading,state:'maybe'},-98.1,38.2),false);
 assert.equal(soil.SOIL_API_PATH(-98.1234567,38.2),'/api/cropland/soil?lon=-98.12346&lat=38.20000','the path carries the point at the page\'s precision');
});

test('a component reads as its share, drainage, hydrologic group, capability and water to 150 cm, and a missing field is left out',()=>{
 const full={name:'Ellsworth',percent:84.6,major:true,drainage:'Moderately well drained',hydrologicGroup:'C',capability:2,waterStorageCm:18.44};
 assert.equal(soil.soilLine(full),'85% of the map unit · moderately well drained drainage · hydrologic group C · non-irrigated capability class 2 of 8 · 18.4 cm of water to 150 cm');
 assert.equal(soil.soilLine({...full,drainage:null,hydrologicGroup:null,capability:null,waterStorageCm:null}),'85% of the map unit');
});

test('the route reads the dominant map unit\'s components, most of it first, and leaves out other map units at the point',async()=>{
 const route=await loadRoute();
 const original=globalThis.fetch;
 try{
  let sent=null;
  globalThis.fetch=async(url,init)=>{sent=JSON.parse(init.body);return sda([
   component('100','Ellsworth silt loam','Ellsworth',60,'Yes','Moderately well drained','C',2,18.4),
   component('100','Ellsworth silt loam','Lorain',25,'No','Well drained','B',3,16.9),
   component('200','Other map unit','Other',40,'Yes','Poorly drained','D',5,9),
  ]);};
  const response=await route.GET(new Request('https://kfm.test/api/cropland/soil?lon=-98.1&lat=38.2'));
  assert.equal(response.status,200);
  assert.match(sent.query,/SDA_Get_Mukey_from_intersection_with_WktWgs84\('POINT\(-98\.10000 38\.20000\)'\)/,'the query names the point');
  const body=await response.json();
  assert.equal(body.state,'ready');assert.deepEqual(body.mapUnit,{key:'100',name:'Ellsworth silt loam'});
  assert.deepEqual(body.components.map(c=>c.name),['Ellsworth','Lorain'],'the other map unit is not read');
  assert.equal(body.components[0].major,true);assert.equal(body.components[0].capability,2);
  assert.equal(response.headers.get('cache-control'),'public, max-age=86400, s-maxage=604800');
  assert.equal(soil.validSoil(body,-98.1,38.2),true,'the page accepts what the route sends');
 }finally{globalThis.fetch=original;}
});

test('a point with no map unit says so, and a source that does not answer gives no soil',async()=>{
 const route=await loadRoute();
 const original=globalThis.fetch;
 try{
  globalThis.fetch=async()=>sda([]);
  const none=await(await route.GET(new Request('https://kfm.test/api/cropland/soil?lon=-98.1&lat=38.2'))).json();
  assert.equal(none.state,'none');assert.deepEqual(none.components,[]);
  globalThis.fetch=async()=>new Response('down',{status:503});
  const down=await route.GET(new Request('https://kfm.test/api/cropland/soil?lon=-98.1&lat=38.2'));
  assert.equal(down.status,502);assert.equal(down.headers.get('cache-control'),'no-store','a failure is not cached');
  assert.match(await down.text(),/No soil is inferred/);
  globalThis.fetch=async()=>new Response(JSON.stringify({Table:[['a','b']]}),{status:200});
  assert.equal((await route.GET(new Request('https://kfm.test/api/cropland/soil?lon=-98.1&lat=38.2'))).status,502,'an unrecognised answer is not read');
  const outside=await route.GET(new Request('https://kfm.test/api/cropland/soil?lon=-120&lat=38'));
  assert.equal(outside.status,400);
  const extra=await route.GET(new Request('https://kfm.test/api/cropland/soil?lon=-98&lat=38&year=2024'));
  assert.equal(extra.status,400,'no other parameters');
 }finally{globalThis.fetch=original;}
});

test('the dock shows the soil beside the crop history: loading, failed, none, and the components with the limit stated',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const base={look:maps.CATEGORY_MAPS.agriculture,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  crops:{on:true,year:2024,years:[2024,2023],reading:'Corn',swatch:null},onCrops(){},onCropsYear(){}};
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,surveySoil:{state:'loading',mapUnit:null,lines:[]}})),/Reading the soil-map unit/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,surveySoil:{state:'failed',mapUnit:null,lines:[]}})),/did not answer for this point\. No soil is inferred/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,surveySoil:{state:'none',mapUnit:null,lines:[]}})),/No SSURGO soil-map unit covers this point/);
 const ready=JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,surveySoil:{state:'ready',mapUnit:'Ellsworth silt loam',lines:[{name:'Ellsworth',detail:'85% of the map unit · hydrologic group C'}]}}));
 assert.match(ready,/Soil survey at this point \(SSURGO\)"/);assert.match(ready,/ · Ellsworth silt loam"/,'the map unit is named in the heading');
 assert.match(ready,/hydrologic group C/);
 assert.match(ready,/They are not the soil at the point/,'the limit is stated');
 assert.doesNotMatch(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,surveySoil:null})),/Soil survey at this point/,'nothing without a click');
});

test('the page reads the soil at each click with the crop history, and clears it with the crops',()=>{
 assert.match(page,/readSurveySoilRef\.current\(event\.lngLat\.lng, event\.lngLat\.lat\)/);
 assert.match(page,/surveySoilRequestRef\.current\?\.abort\(\);\n    setSurveySoil\(null\);/,'turning crops off clears it');
 assert.match(page,/const lon = Number\(clickLon\.toFixed\(5\)\), lat = Number\(clickLat\.toFixed\(5\)\);\n    surveySoilRequestRef/,'the point is rounded as the crop history rounds it');
 assert.match(dockSource,/surveySoil\?: Readonly</);
});
