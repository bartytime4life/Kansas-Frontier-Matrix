import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const orientation=await compile('app/kansas-orientation.ts');
const spc=await compile('app/spc-outlook.ts',{'./kansas-orientation':orientation});
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const route=await readFile('app/api/spc-outlook/route.ts','utf8');
const upstream=await readFile('app/api/event-atlas/upstream.ts','utf8');

const box=(w,s,e,n)=>[[[w,s],[e,s],[e,n],[w,n],[w,s]]];
// The shape SPC publishes in dayNotlk_cat.lyr.geojson: one feature per category, layered.
const props=(label,label2,dn,stroke,fill)=>({DN:dn,VALID:'202610261200',EXPIRE:'202610271200',ISSUE:'202610261630',FORECASTER:'Test',LABEL:label,LABEL2:label2,stroke,fill});
const fixture={type:'FeatureCollection',features:[
 {type:'Feature',geometry:{type:'MultiPolygon',coordinates:[box(-104,33,-90,42),box(-80,30,-75,35)]},properties:props('TSTM','General Thunderstorms Risk',2,'#55BB55','#C1E9C1')},
 {type:'Feature',geometry:{type:'Polygon',coordinates:box(-100,35,-93,40)},properties:props('MRGL','Marginal Risk',3,'#005500','#66A366')},
 {type:'Feature',geometry:{type:'Polygon',coordinates:box(-98,36,-96,38)},properties:props('SLGT','Slight Risk',4,'#DDAA00','#FFE066')},
 {type:'Feature',geometry:{type:'Polygon',coordinates:box(-88,32,-86,34)},properties:props('ENH','Enhanced Risk',5,'#FF6600','#FFA366')},// Alabama
 {type:'Feature',geometry:{type:'Polygon',coordinates:[[[-97,37],[-96,37],[-96,38]]]},properties:props('MDT','Moderate Risk',6,'#CC0000','#E06666')},// too few points
 {type:'Feature',geometry:null,properties:props('HIGH','High Risk',8,'#CC00CC','#EE99EE')},
 {type:'Feature',geometry:{type:'Polygon',coordinates:box(-98,36,-96,38)},properties:{LABEL:'SIGN'}},
]};

test('the route reads one SPC day, allowlisted, bounded and briefly kept',()=>{
 assert.equal(spc.spcOutlookProviderUrl(2),'https://www.spc.noaa.gov/products/outlook/day2otlk_cat.lyr.geojson');
 assert.match(upstream,/"https:\/\/www\.spc\.noaa\.gov"/);
 assert.match(route,/if \(day !== 1 && day !== 2 && day !== 3\)/);
 assert.match(route,/boundedFetch\(source, MAX_BYTES/);
 assert.match(route,/s-maxage=600/);
});

test('SPC times read in both the compact and the ISO fields',()=>{
 assert.equal(spc.spcTime('202610261630'),'2026-10-26T16:30:00.000Z');
 assert.equal(spc.spcTime('2026-10-26T16:30:00+00:00'),'2026-10-26T16:30:00.000Z');
 assert.equal(spc.spcTime('soon'),null);assert.equal(spc.spcTime(null),null);
});

test('the parser keeps known categories with valid polygons, in rank order, and finds the highest over Kansas',()=>{
 const outlook=spc.parseSpcOutlook(fixture,1,'2026-10-26T17:00:00.000Z','src');
 assert.deepEqual(outlook.data.features.map(f=>f.properties.category),['TSTM','MRGL','SLGT','ENH']);
 assert.equal(outlook.data.features[0].geometry.type,'MultiPolygon');
 assert.deepEqual(Object.keys(outlook.data.features[1].properties),['category'],'provider properties do not travel');
 assert.equal(outlook.kansas,'SLGT','Enhanced is over Alabama; Slight reaches south-central Kansas');
 assert.equal(outlook.issuedAt,'2026-10-26T16:30:00.000Z');assert.equal(outlook.validFrom,'2026-10-26T12:00:00.000Z');assert.equal(outlook.validUntil,'2026-10-27T12:00:00.000Z');
 assert.equal(spc.validSpcOutlook(JSON.parse(JSON.stringify(outlook))),true);
 assert.equal(spc.validSpcOutlook({...outlook,day:4}),false);
 assert.equal(spc.validSpcOutlook({...outlook,kansas:'SIGN'}),false);
 const empty=spc.parseSpcOutlook({type:'FeatureCollection',features:[]},3,'2026-10-26T17:00:00.000Z','src');
 assert.equal(empty.kansas,null);assert.equal(empty.issuedAt,null);
 assert.match(spc.spcOutlookReading(empty),/^No thunderstorm areas in this outlook$/);
 assert.throws(()=>spc.parseSpcOutlook({error:1},1,'x','s'));
});

test('the reading names the Kansas risk on SPC\'s 1–5 scale with its clock',()=>{
 const outlook=spc.parseSpcOutlook(fixture,1,'2026-10-26T17:00:00.000Z','src');
 assert.equal(spc.spcOutlookReading(outlook),'Highest risk in Kansas: Slight (2 of 5) · issued Oct 26, 16:30 UTC · valid Oct 26, 12:00 UTC to Oct 27, 12:00 UTC');
 assert.match(spc.spcOutlookReading({...outlook,kansas:'TSTM'}),/^General thunderstorms forecast in Kansas, below the severe categories/);
 assert.match(spc.spcOutlookReading({...outlook,kansas:null}),/^No thunderstorm area reaches Kansas/);
});

test('the key and the lines share SPC\'s colours, and the layer validates',async()=>{
 const key=spc.spcOutlookKey(1);
 assert.equal(key.title,'SPC convective outlook · Day 1');
 assert.deepEqual(key.items.map(i=>i.label),['TSTM General thunderstorms','1 · MRGL Marginal','2 · SLGT Slight','3 · ENH Enhanced','4 · MDT Moderate','5 · HIGH High']);
 assert.deepEqual(key.items.map(i=>i.color),['#c1e9c1','#66a366','#ffe066','#ffa366','#e06666','#ee99ee'],'SPC fill colours, legible on the dark storm base');
 assert.ok(key.items.every(i=>i.shape==='line'));assert.match(key.note,/Not an observation or a warning/);
 const added=[];let source;const layers=[{id:'radar'},{id:'kfm-labels'}];
 const map={getSource:()=>source,addSource:(id,spec)=>{source={spec,setData(){}};},getLayer:id=>layers.find(l=>l.id===id),addLayer:(spec,before)=>{added.push([spec,before]);layers.splice(layers.findIndex(l=>l.id===before),0,{id:spec.id});},getStyle:()=>({layers}),removeLayer:id=>layers.splice(layers.findIndex(l=>l.id===id),1),removeSource:()=>{source=undefined;}};
 const outlook=spc.parseSpcOutlook(fixture,1,'2026-10-26T17:00:00.000Z','src');
 spc.syncSpcOutlook(map,outlook);
 assert.equal(added[0][1],'kfm-labels','under the site overlays and labels');
 const line=added[0][0];
 assert.deepEqual(line.paint['line-color'].slice(2,6),['TSTM','#c1e9c1','MRGL','#66a366']);
 const {validateStyleMin}=await import('@maplibre/maplibre-gl-style-spec');
 assert.deepEqual(validateStyleMin({version:8,sources:{[spc.SPC_OUTLOOK_SOURCE_ID]:{type:'geojson',data:outlook.data}},layers:[line]}).map(e=>e.message),[]);
 spc.syncSpcOutlook(map,null);
 assert.equal(source,undefined);assert.ok(!layers.some(l=>l.id===spc.SPC_OUTLOOK_LAYER_ID));
});

test('the Storm desk dock offers the outlook by day with its reading',async()=>{
 const storm=maps.categoryMap('weather');
 assert.ok(storm.tools.includes('outlook'));
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:storm,mode:'2d',depth:1,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},onOutlook:d=>calls.push(d)};
 const off={day:null,loading:false,failed:false,reading:null,url:'https://www.spc.noaa.gov/products/outlook/'};
 let tree=h.render(h.exports.CategoryMapDock,{...base,outlook:off});
 assert.equal(findNode(tree,n=>n.props?.['aria-label']==='Outlook day'),undefined,'no day choice while off');
 findNode(tree,n=>n.type==='button'&&n.props.children==='Show the SPC severe outlook').props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,outlook:{...off,day:1,loading:true}});
 assert.match(JSON.stringify(tree),/Reading the SPC outlook/);
 tree=h.render(h.exports.CategoryMapDock,{...base,outlook:{...off,day:2,reading:'Highest risk in Kansas: Slight (2 of 5)'}});
 const days=findNode(tree,n=>n.props?.['aria-label']==='Outlook day').props.children;
 assert.deepEqual(JSON.parse(JSON.stringify(days.map(b=>[b.props.children.join(''),b.props['aria-pressed']]))),[['Day 1',false],['Day 2',true],['Day 3',false]]);
 days[2].props.onClick();
 assert.match(JSON.stringify(tree),/Highest risk in Kansas: Slight \(2 of 5\)/);
 assert.equal(findNode(tree,n=>n.type==='a').props.href,'https://www.spc.noaa.gov/products/outlook/');
 findNode(tree,n=>n.type==='button'&&n.props.children==='Hide the SPC outlook').props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,outlook:{...off,day:1,failed:true}});
 assert.match(JSON.stringify(tree),/did not answer/);
 assert.deepEqual(calls,[1,3,null]);
 h.dispose?.();
});

test('the page reads each day once a quarter-hour, keys and draws only the day shown, and closes with its map',()=>{
 assert.match(page,/fetch\(`\/api\/spc-outlook\?day=\$\{outlookDay\}`/);
 assert.match(page,/Date\.now\(\) - Date\.parse\(current\.retrievedAt\) < 15 \* 60_000/);
 assert.match(page,/const shownOutlook = outlookDay \? outlooks\[outlookDay\] \?\? null : null;/);
 assert.match(page,/\.\.\.\(shownOutlook \? \[spcOutlookKey\(shownOutlook\.day\)\] : \[\]\)/);
 assert.match(page,/setOutlookDay\(null\);\s*\/\/ Each map opens on its own subject/);
 assert.match(page,/if \(outlookDay\) params\.set\("outlook", String\(outlookDay\)\);/);
 assert.match(page,/categoryMap\(restoredTopic\)\?\.tools\?\.includes\("outlook"\) \? restoredOutlook : null/);
});
