import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';

const compile=async path=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,()=>({}));return exports;};
const hd=await compile('app/hd-rasters.ts');
const perf=await compile('app/map-performance.ts');
const live=await readFile('app/live-context.ts','utf8');
const page=await readFile('app/page.tsx','utf8');
const runtime=await readFile('app/map-runtime.ts','utf8');

test('the map draws at the screen density: 2× by default, 3× on High detail, 1× only on Battery saver',()=>{
 assert.equal(perf.renderBudget('auto',2).pixelRatio,2,'a retina laptop is not drawn at 1.5×');
 assert.equal(perf.renderBudget('auto',3,false,true).pixelRatio,2,'a phone is not drawn at 1.25×');
 assert.equal(perf.renderBudget('detail',3).pixelRatio,3);
 assert.equal(perf.renderBudget('auto',1).pixelRatio,1,'never above the device');
 assert.equal(perf.renderBudget('efficient',3).pixelRatio,1);
 assert.equal(perf.renderBudget('auto',3,true).pixelRatio,1,'Save-Data keeps Battery saver');
});

test('ArcGIS exports ask for twice the pixels and dpi on high-DPI screens, so symbols keep their size',()=>{
 const url='https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Transportation/Roads/MapServer/export?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&transparent=true&layers=show%3A0&f=image';
 assert.equal(hd.hiDpiExportUrl(url,2),url.replace('size=256%2C256','size=512%2C512')+'&dpi=192');
 assert.equal(hd.hiDpiExportUrl(url,1.25),url,'1× screens keep the 256-pixel request');
 assert.equal(hd.hiDpiExportUrl(url+'&dpi=96',2),url+'&dpi=96','an explicit dpi is left alone');
 const image='https://example.gov/arcgis/rest/services/x/ImageServer/exportImage?bbox={bbox-epsg-3857}&size=256%2C256&f=image';
 assert.equal(hd.hiDpiExportUrl(image,2),image,'image services are not MapServer exports');
 assert.match(live,/tiles: \[hiDpiExportUrl\(raster\.mapUrl!, typeof map\.getPixelRatio === \"function\" \? map\.getPixelRatio\(\) : 1\)\]/,'every provider raster overlay goes through it');
});

test('photographic imagery draws the next zoom level on high-DPI screens; labelled topo and OpenStreetMap keep their tile size',()=>{
 const style={version:8,sources:{'esri-imagery':{type:'raster',tiles:['e'],tileSize:256},'kansas-ng911-2024':{type:'raster',tiles:['k'],tileSize:512},'usgs-topo-context':{type:'raster',tiles:['u'],tileSize:256},'osm-context':{type:'raster',tiles:['o'],tileSize:256},'basemap-relief-dem':{type:'raster-dem',tiles:['d'],tileSize:256}},layers:[]};
 const sharp=hd.hiDpiBasemapStyle(style,2);
 assert.deepEqual(Object.fromEntries(Object.entries(sharp.sources).map(([id,s])=>[id,s.tileSize])),{'esri-imagery':128,'kansas-ng911-2024':256,'usgs-topo-context':256,'osm-context':256,'basemap-relief-dem':256});
 assert.equal(style.sources['esri-imagery'].tileSize,256,'the shared style is not mutated');
 assert.equal(hd.hiDpiBasemapStyle(style,1),style);
 assert.equal(hd.hiDpiBasemapStyle('https://tiles.example/style.json',2),'https://tiles.example/style.json');
 assert.match(page,/style: hiDpiBasemapStyle\(BASEMAPS\[basemapRef\.current\]\.style, renderBudget\.pixelRatio\)/);
 assert.match(page,/map\.setStyle\(hiDpiBasemapStyle\(BASEMAPS\[basemap\]\.style, map\.getPixelRatio\(\)\), \{ diff: false \}\)/);
});

test('the local styles carry real shaded relief, so no map sits on an empty colour',async()=>{
 for(const name of ['midnight','prairie']){
  const block=runtime.slice(runtime.indexOf(`  ${name}: {`),runtime.indexOf('  },\n',runtime.indexOf(`  ${name}: {`)));
  assert.match(block,/\[BASEMAP_RELIEF_DEM_SOURCE_ID\]: reliefDemSource\(\)/,`${name} has the DEM`);
  assert.match(block,/withLocalRelief\(orientationLayers\(/,`${name} draws its relief`);
 }
 assert.match(runtime,/\.\.\.orientation\.slice\(0, land \+ 1\), relief, \.\.\.orientation\.slice\(land \+ 1\)/,'relief over the land fill, under the state line');
 assert.match(page,/basemapStyle\.sources\[sourceId\]\?\.type === "raster-dem"/,'a missing DEM tile is a basemap gap, not a map failure');
});
