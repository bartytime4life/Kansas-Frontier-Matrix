import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const pc=await compile('app/population-change.ts');
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const plain=v=>JSON.parse(JSON.stringify(v));

// Synthetic counts for Kansas's 105 counties (FIPS 001–209, odd): county i has 2,000 + 100·i people in 2010
// and changes by (i − 70)·20, so 70 lose people, one is unchanged and 34 grow.
const geoid=i=>`20${String(2*i+1).padStart(3,'0')}`;
const square=i=>({type:'Polygon',coordinates:[[[-100+i*0.05,38],[-99.96+i*0.05,38],[-99.96+i*0.05,38.04],[-100+i*0.05,38]]]});
const counties=population=>({type:'FeatureCollection',features:Array.from({length:105},(_,i)=>({type:'Feature',geometry:square(i),properties:{geoid:geoid(i),name:`C${i}`,population:population(i)}}))});
const then=counties(i=>2000+100*i), now=counties(i=>2000+100*i+(i-70)*20);

test('each county is compared with itself, and only a complete join of all 105 is drawn',()=>{
 const change=pc.populationChange(now,then);
 assert.equal(change.counties.length,105);
 assert.deepEqual(plain(change.counties[0]),{geoid:'20001',name:'C0',from:2000,to:600,change:-1400,percent:-70});
 assert.deepEqual([change.from,change.to,change.change,change.losing,change.gaining],[756000,718200,-37800,70,34]);
 assert.equal(change.percent.toFixed(1),'-5.0');
 assert.equal(pc.populationChange(counties(i=>i===3?null:2000),then),null,'a missing 2020 count');
 assert.equal(pc.populationChange(now,counties(i=>i===3?0:2000)),null,'a 2010 count of zero has no percent change');
 assert.equal(pc.populationChange({...now,features:now.features.slice(1)},then),null,'a missing county');
 const moved={...now,features:now.features.map((f,i)=>i===0?{...f,properties:{...f.properties,geoid:'20999'}}:f)};
 assert.equal(pc.populationChange(moved,then),null,'a county that does not join');
 assert.equal(pc.validCountyBaseline({data:then}),true);assert.equal(pc.validCountyBaseline({data:{...then,features:then.features.slice(5)}}),false);
 assert.equal(pc.populationChangeApiPath,'/api/event-atlas/counties?edition=2010');
});

test('classes diverge at zero, losses brown and gains blue-green, each lower bound inclusive',()=>{
 assert.deepEqual([-70,-10.01,-10,-5,-0.1,0,4.9,5,10,30].map(pc.changeColor),['#8c510a','#8c510a','#d8b365','#f6e8c3','#f6e8c3','#c7eae5','#c7eae5','#5ab4ac','#01665e','#01665e']);
 const key=pc.populationChangeKey();
 assert.equal(key.title,'Population change by county · 2010–2020');assert.equal(key.items.length,6);
 assert.deepEqual(key.items.map(i=>i.label),['Lost 10% or more','Lost 5 to 10%','Lost under 5%','Grew under 5%','Grew 5 to 10%','Grew 10% or more']);
 assert.match(key.note,/same 105 county boundaries/);
});

test('the reading, the list from largest gain to largest loss, and a picked county with its rank',()=>{
 const change=pc.populationChange(now,then);
 assert.equal(pc.populationChangeReading(change),'Kansas 756,000 → 718,200 (−37,800, −5.0%) · 70 of 105 counties lost people · largest gain C104 (+680) · largest loss C0 (−1,400)');
 const list=pc.populationChangeList(change);
 assert.equal(list.length,105);
 assert.deepEqual(list[0],{id:'20209',label:'C104 · +5.5% · 12,400 → 13,080'});
 assert.deepEqual(list[104],{id:'20001',label:'C0 · −70.0% · 2,000 → 600'});
 assert.equal(pc.countyPopulationReading(change,'20141'),'C70 County: 9,000 in 2010 → 9,000 in 2020 (0, 0.0%) · 35 of 105 by percent change');
 assert.equal(pc.countyPopulationReading(change,'20999'),null);
});

test('the choropleth sits under the site overlays, coloured by class, with the picked county outlined; it closes cleanly',()=>{
 const change=pc.populationChange(now,then);
 const collection=pc.populationChangeCollection(now,change);
 assert.equal(collection.features.length,105);
 assert.deepEqual(plain(collection.features[0].properties),{geoid:'20001',name:'C0',percent:-70,change:-1400,color:'#8c510a'});
 assert.equal(collection.features[104].properties.color,'#5ab4ac');
 const layers=[{id:'background'},{id:'external-census-counties-line'},{id:'kfm-roads'}],sources={},filters={};
 const map={getSource:id=>sources[id]&&{setData(){}},addSource:(id,s)=>{sources[id]=s;},removeSource:id=>{delete sources[id];},setFilter:(id,f)=>{filters[id]=f;},
  getLayer:id=>layers.find(l=>l.id===id),removeLayer:id=>{layers.splice(layers.findIndex(l=>l.id===id),1);},
  addLayer:(spec,before)=>{const i=before?layers.findIndex(l=>l.id===before):-1;layers.splice(i<0?layers.length:i,0,{id:spec.id,spec});},getStyle:()=>({layers})};
 pc.syncPopulationChange(map,collection,'20141');
 assert.deepEqual(layers.map(l=>l.id),['background','external-census-counties-line',pc.POPULATION_CHANGE_FILL_LAYER_ID,pc.POPULATION_CHANGE_LINE_LAYER_ID,pc.POPULATION_CHANGE_SELECTED_LAYER_ID,'kfm-roads']);
 assert.deepEqual(plain(layers[2].spec.paint['fill-color']),['get','color']);
 assert.deepEqual(plain(filters[pc.POPULATION_CHANGE_SELECTED_LAYER_ID]),['==',['get','geoid'],'20141']);
 pc.syncPopulationChange(map,null);
 assert.deepEqual(layers.map(l=>l.id),['background','external-census-counties-line','kfm-roads']);assert.deepEqual(Object.keys(sources),[]);
});

test('the People dock offers the change beside the prisms: chart, list and the picked county; the page keeps one county encoding at a time',async()=>{
 const change=pc.populationChange(now,then);
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.people,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  population:{on:false,groups:[],counties:105,statewide:35.9,metresPerPerson:100},onPopulation:v=>calls.push(['prisms',v]),
  onPopulationChange:v=>calls.push(['on',v]),onPopulationChangePick:v=>calls.push(['pick',v]),onPopulationChangeClear:()=>calls.push(['clear'])};
 const off={on:false,loading:false,failed:false,reading:null,bars:null,list:[],picked:null,county:null};
 const tool=tree=>findNode(tree,n=>n.type==='button'&&/since 2010|2010–2020 change/.test(String(n.props.children)));
 let tree=h.render(h.exports.CategoryMapDock,{...base,populationChange:off});
 assert.equal(tool(tree).props.children,'Show change since 2010');tool(tree).props.onClick();
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,populationChange:{...off,on:true,loading:true}})),/Reading the 2010 and 2020 Census counts…/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,populationChange:{...off,on:true,failed:true}})),/did not answer for both years; no change is shown/);
 const bars=pc.byPercent(change).map(c=>({id:c.geoid,name:c.name,percent:c.percent,color:pc.changeColor(c.percent)}));
 const on={...off,on:true,reading:pc.populationChangeReading(change),bars,list:pc.populationChangeList(change),picked:'20141',county:pc.countyPopulationReading(change,'20141')};
 tree=h.render(h.exports.CategoryMapDock,{...base,populationChange:on});
 assert.equal(tool(tree).props.children,'Hide the 2010–2020 change');assert.equal(tool(tree).props['aria-pressed'],true);
 assert.match(JSON.stringify(tree),/70 of 105 counties lost people/);
 const chart=findNode(tree,n=>n.type===h.exports.PopulationChangeChart);
 const figure=chart.type(chart.props);
 assert.equal(figure.props['aria-label'],'Percent change in people, 2010–2020, for 105 Kansas counties from C104 (+5.5%) to C0 (−70.0%); 70 below zero');
 const svg=JSON.stringify(figure);
 assert.match(svg,/"fill":"#8c510a"/);assert.match(svg,/"fill":"#5ab4ac"/);assert.match(svg,/C104 \+5\.5%/);
 findNode(figure,n=>n.type==='g'&&n.props['data-county']==='20001').props.onClick();
 assert.equal(findNode(figure,n=>n.type==='line'&&n.props['data-picked']==='20141').props.x1,35*4-2,'a marker at the picked county, 35th by percent change');
 const list=findNode(tree,n=>n.props?.label==='Kansas counties by percent change in people, 2010–2020, largest gain first');
 assert.equal(list.props.summary,'Counties, largest gain first (105)');list.props.onPick('20209');
 assert.match(JSON.stringify(tree),/C70 County: 9,000 in 2010/);
 findNode(tree,n=>n.type==='button'&&n.props['aria-label']==='Clear the selected county').props.onClick();
 assert.deepEqual(calls,[['on',true],['pick','20001'],['pick','20209'],['clear']]);
 assert.equal(tool(h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.water,populationChange:off})),undefined,'only maps that offer it');
 // The page: one encoding at a time, the prisms back when the change closes, the county click, the key, and the reset with the map.
 assert.match(page,/popChangePrismsRef\.current = populationPrisms;\s*setPopulationPrismsShown\(false\);/);
 assert.match(page,/if \(popChangePrismsRef\.current\) setPopulationPrismsShown\(true\);/);
 assert.match(page,/const showPopulationPrisms = \(on: boolean\) => \{\s*if \(on && popChangeOn\) closePopulationChange\(\);/);
 // The county outlines it covers are hidden while it is shown, and only those it hid come back.
 assert.match(page,/popChangeHidCountiesRef\.current = Boolean\(officialVisibilityRef\.current\["census-counties"\]\);\s*if \(popChangeHidCountiesRef\.current\) setOfficialContextVisible\("census-counties", false\);/);
 assert.match(page,/if \(popChangeHidCountiesRef\.current\) setOfficialContextVisible\("census-counties", true\);\s*popChangeHidCountiesRef\.current = false;/);
 assert.match(page,/onPopulation=\{showPopulationPrisms\}/);
 assert.match(page,/void fetch\(populationChangeApiPath, \{ signal: controller\.signal \}\)/);
 assert.match(page,/if \(renderedHits\[0\]\?\.source === POPULATION_CHANGE_SOURCE_ID\) \{\s*const geoid = renderedHits\[0\]\.properties\?\.geoid;\s*if \(typeof geoid === "string"\) \{ setPopChangeCounty\(geoid\); setCategoryDockHidden\(false\); \}/);
 assert.match(page,/\.\.\.\(popChangeOn && popChangeCollection \? \[populationChangeKey\(\)\] : \[\]\)/);
 assert.match(page,/popChangePrismsRef\.current = false;\s*popChangeHidCountiesRef\.current = false;\s*setPopChangeOn\(false\);\s*setPopChangeCounty\(null\);\s*if \(look\.overlays\?\.includes\("aviation"\)\)/,'closes with its map');
});
