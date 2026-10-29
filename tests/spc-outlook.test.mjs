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
 assert.match(page,/const OUTLOOK_REFRESH_MS = 15 \* 60_000;/);
 assert.match(page,/const age = current && readAt !== undefined \? Date\.now\(\) - readAt : Infinity;/,'age is this browser\'s own, never the provider\'s retrievedAt, so an old answer cannot loop the read');
 assert.match(page,/outlookReadAtRef\.current\.set\(outlookId, Date\.now\(\)\);\s*setOutlooks/);
 assert.doesNotMatch(page,/Date\.parse\(current\.retrievedAt\)/);
 assert.match(page,/if \(age < OUTLOOK_REFRESH_MS\) \{[\s\S]{0,160}const timer = setTimeout\(\(\) => setOutlookTick\(tick => tick \+ 1\), OUTLOOK_REFRESH_MS - age\);\s*return \(\) => clearTimeout\(timer\);/,'a shown outlook re-reads itself when it turns a quarter-hour old');
 assert.match(page,/\}, \[outlookDay, outlookProduct, outlookId, outlooks, outlookFailed, outlookTick, announce\]\);/);
 assert.match(page,/const shownOutlook = outlookId \? outlooks\[outlookId\] \?\? null : null;/);
 assert.match(page,/\.\.\.\(shownOutlook \? \[spcOutlookKey\(shownOutlook\.day, shownOutlook\.product\)\] : \[\]\)/);
 assert.match(page,/setOutlookDay\(null\);\s*setOutlookHazard\("cat"\);[\s\S]{0,80}\/\/ Each map opens on its own subject/);
 assert.match(page,/if \(outlookDay\) params\.set\("outlook", String\(outlookDay\)\);/);
 assert.match(page,/categoryMap\(restoredTopic\)\?\.tools\?\.includes\("outlook"\) \? restoredOutlook : null/);
});

// The shape SPC publishes in dayNotlk_torn.lyr.geojson: DN is the percent, LABEL the fraction.
const hazard=(dn,label,geometry)=>({type:'Feature',geometry,properties:{DN:dn,VALID:'202610261200',EXPIRE:'202610271200',ISSUE:'202610261630',ISSUE_ISO:'2026-10-26T16:30:00+00:00',LABEL:label,LABEL2:`${dn}% Tornado Risk`}});
const tornado={type:'FeatureCollection',features:[
 {type:'Feature',geometry:{type:'GeometryCollection',geometries:[]},properties:{DN:0,LABEL:'Less Than 2% All Areas'}},
 hazard(5,'0.05',{type:'Polygon',coordinates:box(-99,36,-95,39)}),// reaches Kansas
 hazard(2,'0.02',{type:'Polygon',coordinates:box(-101,35,-94,40)}),
 hazard(10,'0.10',{type:'Polygon',coordinates:box(-96,33,-94,35)}),// Oklahoma and Arkansas, south of Kansas
 hazard(3,'0.03',{type:'Polygon',coordinates:box(-98,37,-97,38)}),// not an SPC tornado band
 {type:'Feature',geometry:{type:'Polygon',coordinates:box(-98,37,-97,38)},properties:{DN:10,LABEL:'SIGN'}},// pre-2026 hatching in the hazard file
]};
// The shape of dayNotlk_cigtorn.lyr.geojson: one feature per conditional-intensity group.
const intensity={type:'FeatureCollection',features:[
 {type:'Feature',geometry:{type:'Polygon',coordinates:box(-96,33,-94,35)},properties:{DN:3,LABEL:'CIG3'}},// south of Kansas
 {type:'Feature',geometry:{type:'Polygon',coordinates:box(-99,36,-96,38.5)},properties:{DN:2,LABEL:'CIG2'}},
 {type:'Feature',geometry:{type:'Polygon',coordinates:box(-99,36,-95,39)},properties:{DN:1,LABEL:'CIG1'}},
]};

test('the hazard outlooks read SPC\'s tornado, wind and hail files with their intensity areas, for days 1 and 2',()=>{
 assert.equal(spc.spcOutlookProviderUrl(1,'torn'),'https://www.spc.noaa.gov/products/outlook/day1otlk_torn.lyr.geojson');
 assert.equal(spc.spcIntensityProviderUrl(2,'hail'),'https://www.spc.noaa.gov/products/outlook/day2otlk_cighail.lyr.geojson');
 assert.deepEqual(JSON.parse(JSON.stringify(spc.outlookProducts(1))),['cat','torn','wind','hail']);
 assert.deepEqual(JSON.parse(JSON.stringify(spc.outlookProducts(3))),['cat'],'day 3 is categorical');
 assert.match(route,/!outlookProducts\(day as OutlookDay\)\.includes\(product\)\) return refuse\(/);
 assert.match(route,/spcIntensityProviderUrl\(day, product\)[\s\S]{0,120}\.catch\(\(\) => undefined\)/,'the probabilities stand without the intensity file');
 assert.match(route,/const id = `\$\{day\}-\$\{product\}`;/);
});

test('a tornado outlook keeps SPC\'s bands and intensity groups, and finds the highest of each over Kansas',()=>{
 const outlook=spc.parseSpcOutlook(tornado,1,'2026-10-26T17:00:00.000Z','src','torn',intensity);
 assert.deepEqual(outlook.data.features.map(f=>f.properties.category),['2','5','10','CIG1','CIG1','CIG2','CIG3'],'bands lowest to highest, intensity over them; the old SIGN hatching reads as CIG1');
 assert.equal(outlook.product,'torn');assert.equal(outlook.kansas,'5','10% lies south of Kansas');
 assert.equal(outlook.intensity,'CIG2','CIG3 lies south of Kansas');
 assert.equal(outlook.issuedAt,'2026-10-26T16:30:00.000Z');
 assert.equal(spc.validSpcOutlook(JSON.parse(JSON.stringify(outlook))),true);
 assert.equal(spc.validSpcOutlook({...outlook,day:3}),false,'no hazard outlook on day 3');
 assert.equal(spc.validSpcOutlook({...outlook,kansas:'3'}),false);
 assert.equal(spc.validSpcOutlook({...outlook,intensity:'SIGN'}),false);
 assert.equal(spc.spcOutlookReading(outlook),'Tornado: 5% chance within 25 miles of a point, highest in Kansas · intensity level 2 of 3 reaches Kansas · issued Oct 26, 16:30 UTC · valid Oct 26, 12:00 UTC to Oct 27, 12:00 UTC');
 const bare=spc.parseSpcOutlook(tornado,1,'2026-10-26T17:00:00.000Z','src','torn');
 assert.equal(bare.intensity,'CIG1','without the intensity file, the hazard file\'s own hatching still counts');
 assert.match(spc.spcOutlookReading({...bare,kansas:null,intensity:null}),/^Tornado: below 2% across Kansas · issued/);
});

test('wind and hail read the fraction when SPC leaves out DN, and an empty outlook reads as below the lowest band',()=>{
 const wind={type:'FeatureCollection',features:[{type:'Feature',geometry:{type:'Polygon',coordinates:box(-99,36,-95,39)},properties:{LABEL:'0.15'}},{type:'Feature',geometry:{type:'Polygon',coordinates:box(-99,36,-95,39)},properties:{LABEL:'0.10'}}]};
 const outlook=spc.parseSpcOutlook(wind,2,'2026-10-26T17:00:00.000Z','src','wind',{type:'GeometryCollection',geometries:[]});
 assert.deepEqual(outlook.data.features.map(f=>f.properties.category),['15'],'10% is not a wind band');
 assert.deepEqual(spc.SPC_PROBABILITIES.wind.map(b=>b.id),['5','15','30','45','60','75','90'],'the wind ladder runs to 90% since March 2026');
 const high=spc.parseSpcOutlook({type:'FeatureCollection',features:[{type:'Feature',geometry:{type:'Polygon',coordinates:box(-99,36,-95,39)},properties:{DN:90,LABEL:'0.90'}},{type:'Feature',geometry:{type:'Polygon',coordinates:box(-100,35,-94,40)},properties:{DN:75,LABEL:'0.75'}}]},1,'2026-10-26T17:00:00.000Z','src','wind');
 assert.deepEqual(high.data.features.map(f=>f.properties.category),['75','90']);assert.equal(high.kansas,'90');
 assert.deepEqual(spc.spcOutlookKey(1,'wind').items.slice(5,7).map(i=>[i.label,i.color]),[['75%','#5f9fe0'],['90%','#4fe3e3']]);
 assert.equal(outlook.kansas,'15');assert.equal(outlook.intensity,null);
 const empty=spc.parseSpcOutlook({type:'GeometryCollection',geometries:[]},1,'2026-10-26T17:00:00.000Z','src','hail');
 assert.equal(empty.data.features.length,0);
 assert.equal(spc.spcOutlookReading(empty),'Hail: below 5% everywhere in this outlook');
});

test('the hazard key pairs SPC\'s probability colours with dashed intensity lines, and a new product redraws on its own scale',async()=>{
 const key=spc.spcOutlookKey(1,'hail');
 assert.equal(key.title,'SPC hail outlook · Day 1');
 assert.deepEqual(key.items.map(i=>i.label),['5%','15%','30%','45%','60%','CIG1 Intensity level 1','CIG2 Intensity level 2'],'hail has two intensity groups');
 assert.deepEqual(key.items.slice(0,5).map(i=>i.color),['#c08a5e','#ffd84d','#ff5c5c','#ff66ff','#b77cf2'],'SPC\'s wind and hail hues: brown, yellow, red, magenta, purple');
 assert.ok(key.items.slice(5).every(i=>i.dashed&&i.shape==='line'));
 assert.match(key.note,/within 25 miles of a point/);assert.match(key.note,/Not an observation or a warning/);
 assert.deepEqual(spc.spcOutlookKey(1,'torn').items.slice(0,7).map(i=>i.color),['#4fbf4f','#c08a5e','#ffd84d','#ff5c5c','#ff66ff','#b77cf2','#5f9fe0'],'SPC\'s tornado hues: green through blue');
 const added=[];let source;const layers=[{id:'radar'},{id:'kfm-labels'}];
 const map={getSource:()=>source,addSource:(id,spec)=>{source={spec,setData(){}};},getLayer:id=>layers.find(l=>l.id===id),addLayer:(spec,before)=>{added.push(spec);layers.splice(layers.findIndex(l=>l.id===before),0,{id:spec.id});},getStyle:()=>({layers}),removeLayer:id=>layers.splice(layers.findIndex(l=>l.id===id),1),removeSource:()=>{source=undefined;}};
 const torn=spc.parseSpcOutlook(tornado,1,'2026-10-26T17:00:00.000Z','src','torn',intensity);
 spc.syncSpcOutlook(map,torn);
 assert.deepEqual(layers.map(l=>l.id),['radar',spc.SPC_OUTLOOK_LAYER_ID,spc.SPC_INTENSITY_LAYER_ID,'kfm-labels']);
 const [lines,cig]=added;
 assert.deepEqual(lines.paint['line-color'].slice(2,6),['2','#4fbf4f','5','#c08a5e']);
 const {validateStyleMin}=await import('@maplibre/maplibre-gl-style-spec');
 assert.deepEqual(validateStyleMin({version:8,sources:{[spc.SPC_OUTLOOK_SOURCE_ID]:{type:'geojson',data:torn.data}},layers:[lines,cig]}).map(e=>e.message),[]);
 spc.syncSpcOutlook(map,spc.parseSpcOutlook(fixture,1,'2026-10-26T17:00:00.000Z','src'));
 assert.deepEqual(layers.map(l=>l.id),['radar',spc.SPC_OUTLOOK_LAYER_ID,'kfm-labels'],'the categorical outlook has no intensity layer');
 assert.equal(added.at(-1).paint['line-color'][2],'TSTM','redrawn on the categorical scale');
});

test('the dock offers the outlook products, with hazards only on days 1 and 2',async()=>{
 const storm=maps.categoryMap('weather');
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const picked=[];
 const base={look:storm,mode:'2d',depth:1,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},onOutlook(){},onOutlookProduct:p=>picked.push(p)};
 const on={day:1,product:'torn',products:['cat','torn','wind','hail'],loading:false,failed:false,reading:'Tornado: 5% chance',url:'https://www.spc.noaa.gov/products/outlook/'};
 let tree=h.render(h.exports.CategoryMapDock,{...base,outlook:on});
 let products=findNode(tree,n=>n.props?.['aria-label']==='Outlook product').props.children;
 assert.deepEqual(JSON.parse(JSON.stringify(products.map(b=>[b.props.children,b.props['aria-pressed'],b.props.disabled]))),[['Risk',false,false],['Tornado',true,false],['Wind',false,false],['Hail',false,false]]);
 products[3].props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,outlook:{...on,day:3,product:'cat',products:['cat']}});
 products=findNode(tree,n=>n.props?.['aria-label']==='Outlook product').props.children;
 assert.deepEqual(JSON.parse(JSON.stringify(products.map(b=>[b.props['aria-pressed'],b.props.disabled]))),[[true,false],[false,true],[false,true],[false,true]]);
 assert.match(products[1].props.title,/days 1 and 2/);
 assert.deepEqual(picked,['hail']);
 h.dispose?.();
});

test('the page reads each day and product on its own, keeps a hazard through day 3 as categorical, and shares the product',()=>{
 assert.match(page,/const outlookProduct: OutlookProduct = outlookDay && outlookProducts\(outlookDay\)\.includes\(outlookHazard\) \? outlookHazard : "cat";/);
 assert.match(page,/const outlookId = outlookDay \? `\$\{outlookDay\}-\$\{outlookProduct\}` : null;/);
 assert.match(page,/fetch\(`\/api\/spc-outlook\?day=\$\{outlookDay\}&product=\$\{outlookProduct\}`/);
 assert.match(page,/value\.product !== outlookProduct\) throw new Error\("Invalid SPC outlook\."\);/);
 assert.match(page,/if \(outlookDay && outlookHazard !== "cat"\) params\.set\("outlookHazard", outlookHazard\);/);
 assert.match(page,/setOutlookHazard\(isOutlookProduct\(restoredHazard\) \? restoredHazard : "cat"\);/);
 assert.match(page,/onOutlookProduct=\{chooseOutlookHazard\}/);
});


// Synthetic forecasts, never observations. Both contours cross Kansas's western
// border; this exercises a crossing rather than just a polygon wholly in-state.
const highWindFeature = (percent, encoding = 'DN', geometry = {type:'Polygon', coordinates:box(-103,37.2,-99,38.2)}, iso = false) => ({
 type:'Feature', geometry,
 properties:{LABEL:String(percent / 100), ...(encoding === 'DN' ? {DN:percent} : {}),
  ...(iso ? {ISSUE_ISO:'2026-10-28T16:30:00+00:00',VALID_ISO:'2026-10-28T16:30:00Z',EXPIRE_ISO:'2026-10-29T12:00:00+00:00'}
   : {ISSUE:'202610281630',VALID:'202610281630',EXPIRE:'202610291200'})},
});
const highWind = (features, day = 1, intensityRaw) => spc.parseSpcOutlook({type:'FeatureCollection',features},day,'2026-10-28T17:05:00.000Z','synthetic-wind','wind',intensityRaw);

test('high-wind 75% and 90% survive DN and LABEL parsing on both forecast days with valid clocks',()=>{
 for (const day of [1,2]) for (const percent of [75,90]) for (const encoding of ['DN','LABEL']) for (const iso of [false,true]) {
  const outlook=highWind([highWindFeature(percent,encoding,undefined,iso)],day);
  assert.deepEqual(outlook.data.features.map(f=>f.properties.category),[String(percent)],JSON.stringify({day,percent,encoding,iso}));
  assert.equal(outlook.kansas,String(percent));
  assert.equal(outlook.issuedAt,'2026-10-28T16:30:00.000Z');
  assert.equal(outlook.validFrom,'2026-10-28T16:30:00.000Z');
  assert.equal(outlook.validUntil,'2026-10-29T12:00:00.000Z');
  assert.ok(Date.parse(outlook.issuedAt) <= Date.parse(outlook.validFrom));
  assert.ok(Date.parse(outlook.validFrom) < Date.parse(outlook.validUntil));
  assert.ok(Date.parse(outlook.validFrom) <= Date.parse(outlook.retrievedAt) && Date.parse(outlook.retrievedAt) < Date.parse(outlook.validUntil));
  assert.equal(spc.validSpcOutlook(JSON.parse(JSON.stringify(outlook))),true,'both bands survive the client envelope validator');
  assert.equal(spc.spcOutlookReading(outlook),'Wind: '+percent+'% chance within 25 miles of a point, highest in Kansas · issued Oct 28, 16:30 UTC · valid Oct 28, 16:30 UTC to Oct 29, 12:00 UTC');
 }
});

test('high-wind Kansas maximum ignores a higher out-of-state contour and is independent of feature order',()=>{
 const seventyFive=highWindFeature(75);
 const ninetyElsewhere=highWindFeature(90,'DN',{type:'Polygon',coordinates:box(-92,33,-90,35)});
 for (const features of [[ninetyElsewhere,seventyFive],[seventyFive,ninetyElsewhere]]) {
  const outlook=highWind(features);
  assert.deepEqual(outlook.data.features.map(f=>f.properties.category),['75','90'],'retain national contours while summarizing Kansas');
  assert.equal(outlook.kansas,'75');
  assert.equal(spc.outlookBandAt(outlook,-100,37.7).id,'75');
  assert.equal(spc.outlookBandAt(outlook,-91,34).id,'90');
  assert.match(spc.spcOutlookReading(outlook),/^Wind: 75% chance/);
 }
 // A band crossing the entire state has all vertices outside Kansas.
 const ninetyCrossing=highWindFeature(90,'LABEL',{type:'MultiPolygon',coordinates:[box(-103,38.3,-93,38.7),box(-90,32,-89,33)]});
 for (const features of [[ninetyCrossing,seventyFive],[seventyFive,ninetyCrossing]]) {
  const outlook=highWind(features,2);
  assert.equal(outlook.kansas,'90');
  assert.equal(spc.outlookBandAt(outlook,-100,38.5).id,'90');
  assert.match(spc.spcOutlookReading(outlook),/^Wind: 90% chance/);
 }
 const lower=highWindFeature(60,'DN',{type:'Polygon',coordinates:box(-103,36,-93,41)});
 const hole=highWindFeature(90,'DN',{type:'Polygon',coordinates:[...box(-104,34,-90,43),...box(-103,36,-93,41)]});
 const withHole=highWind([hole,lower]);
 assert.equal(withHole.kansas,'60','an enclosing 90% polygon with Kansas in its hole must not raise the state maximum');
 assert.equal(spc.outlookBandAt(withHole,-98,38).id,'60');
});

test('high-wind map paint and key agree for 75% blue and 90% cyan while intensity stays separate',async()=>{
 const added=[];let source;const layers=[{id:'radar'},{id:'kfm-labels'}];
 const map={getSource:()=>source,addSource:(id,spec)=>{source={spec,setData(data){this.spec.data=data;}};},getLayer:id=>layers.find(l=>l.id===id),addLayer:(spec,before)=>{added.push(spec);layers.splice(layers.findIndex(l=>l.id===before),0,spec);},getStyle:()=>({layers}),removeLayer:id=>layers.splice(layers.findIndex(l=>l.id===id),1),removeSource:()=>{source=undefined;}};
 const cig={type:'FeatureCollection',features:[{type:'Feature',geometry:{type:'Polygon',coordinates:box(-103,37.2,-99,38.2)},properties:{LABEL:'CIG3',DN:3}}]};
 const outlook=highWind([highWindFeature(90),highWindFeature(75)],1,cig);
 spc.syncSpcOutlook(map,outlook);
 assert.deepEqual(source.spec.data.features.map(f=>f.properties.category),['75','90','CIG3']);
 assert.equal(outlook.kansas,'90');assert.equal(outlook.intensity,'CIG3');
 assert.match(spc.spcOutlookReading(outlook),/90% chance.*intensity level 3 of 3 reaches Kansas/);
 const key=spc.spcOutlookKey(1,'wind'), line=layers.find(l=>l.id===spc.SPC_OUTLOOK_LAYER_ID), intensityLine=layers.find(l=>l.id===spc.SPC_INTENSITY_LAYER_ID);
 const {validateStyleMin,expression}=await import('@maplibre/maplibre-gl-style-spec');
 assert.deepEqual(validateStyleMin({version:8,sources:{[spc.SPC_OUTLOOK_SOURCE_ID]:{type:'geojson',data:outlook.data}},layers:[line,intensityLine]}).map(e=>e.message),[]);
 const paint=expression.createExpression(line.paint['line-color'], 'layers[0].paint.line-color');
 assert.equal(paint.result,'success');
 for (const [id,color] of [['75','#5f9fe0'],['90','#4fe3e3']]) {
  assert.equal(paint.value.evaluate({zoom:5},{type:3,properties:{category:id}}),color,'evaluate actual MapLibre paint for '+id);
  assert.equal(key.items.find(i=>i.label===id+'%').color,color);
 }
 assert.deepEqual(key.items.slice(0,7).map(i=>i.label),['5%','15%','30%','45%','60%','75%','90%']);
 assert.ok(key.items.slice(7).every(i=>i.dashed&&i.color===spc.SPC_INTENSITY_COLOR));
 assert.match(key.note,/forecast probability/);assert.match(key.note,/Not an observation or a warning/);
 assert.deepEqual(intensityLine.paint['line-dasharray'],[2.5,1.8]);
 assert.deepEqual(layers.map(l=>l.id),['radar',spc.SPC_OUTLOOK_LAYER_ID,spc.SPC_INTENSITY_LAYER_ID,'kfm-labels']);
 // A product switch must replace the extended wind scale with hail's scale.
 const hail=spc.parseSpcOutlook({type:'FeatureCollection',features:[highWindFeature(60)]},1,outlook.retrievedAt,'synthetic-hail','hail');
 spc.syncSpcOutlook(map,hail);
 assert.equal(added.at(-2).paint['line-color'].includes('90'),false);
 assert.equal(source.spec.data,hail.data);
});

test('high-wind additions preserve tornado and hail ladders and reject their unsupported 75% and 90%',()=>{
 assert.deepEqual(spc.SPC_PROBABILITIES.torn.map(b=>b.id),['2','5','10','15','30','45','60']);
 assert.deepEqual(spc.SPC_PROBABILITIES.hail.map(b=>b.id),['5','15','30','45','60']);
 for (const product of ['torn','hail']) {
  const outlook=spc.parseSpcOutlook({type:'FeatureCollection',features:[highWindFeature(60),highWindFeature(75),highWindFeature(90)]},1,'2026-10-28T17:05:00.000Z','synthetic-'+product,product);
  assert.deepEqual(outlook.data.features.map(f=>f.properties.category),['60']);
  assert.equal(outlook.kansas,'60');
  assert.equal(spc.validSpcOutlook({...outlook,kansas:'90'}),false);
 }
});
