import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const civic=await compile('app/civic-districts.ts');
const leg=await compile('app/state-legislature.ts',{'./civic-districts':civic});
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const plain=v=>JSON.parse(JSON.stringify(v));
const esm=async(path,replace=s=>s)=>`data:text/javascript;base64,${Buffer.from(ts.transpileModule(replace(await readFile(path,'utf8')),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`;
const upstreamUrl=await esm('app/api/event-atlas/upstream.ts');
const civicUrl=await esm('app/civic-districts.ts');
const legUrl=await esm('app/state-legislature.ts',s=>s.replace('from "./civic-districts"',`from "${civicUrl}"`));
const route=async tag=>import(await esm('app/api/state-legislature/route.ts',s=>s.replace('from "../event-atlas/upstream"',`from "${upstreamUrl}"`).replace('from "../../state-legislature"',`from "${legUrl}"`)+`\n// ${tag}`));

// A TIGERweb-shaped answer (synthetic squares across Kansas), one feature per district plus a "ZZZ" area in no district.
const square=(i,n)=>{const w=-102+(i%10)*0.7,s=37+Math.floor(i/10)*(2.9/Math.ceil(n/10));return [[[w,s],[w+0.6,s],[w+0.6,s+0.2],[w,s+0.2],[w,s]]];};
const answer=n=>({type:'FeatureCollection',features:[...Array.from({length:n},(_,i)=>({type:'Feature',properties:{GEOID:`20${String(i+1).padStart(3,'0')}`,STATE:'20',BASENAME:String(i+1),NAME:`State Senate District ${i+1}`},geometry:{type:'Polygon',coordinates:square(i,n)}})),
 {type:'Feature',properties:{GEOID:'20ZZZ',STATE:'20'},geometry:{type:'Polygon',coordinates:square(0,n)}}]});

test('each chamber is a TIGERweb layer of the same 2025 legislative service, asked for Kansas in longitude and latitude',()=>{
 assert.deepEqual(plain(leg.CHAMBERS),{senate:{layer:8,name:'Kansas Senate',districts:40,title:'Senate'},house:{layer:9,name:'Kansas House',districts:125,title:'House'}});
 const url=new URL(leg.legislatureProviderUrl('house'));
 assert.equal(url.origin+url.pathname,'https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2025/Legislative/MapServer/9/query');
 assert.deepEqual(['where','outSR','f','returnGeometry'].map(k=>url.searchParams.get(k)),["STATE='20'",'4326','geojson','true']);
 assert.ok(leg.isChamber('senate')&&!leg.isChamber('congress'));
 assert.equal(leg.legislatureApiPath('senate'),'/api/state-legislature?chamber=senate');
});

test('the complete edition or nothing: every district once, valid Kansas polygons; areas in no district are dropped',()=>{
 const senate=leg.parseLegislature(answer(40),'senate','2026-10-29T21:00:00Z');
 assert.equal(senate.data.features.length,40);assert.deepEqual(plain(senate.data.features[0].properties),{district:1,geoid:'20001',chamber:'senate',name:'Kansas Senate District 1'});
 assert.ok(leg.validLegislature(plain(senate),'senate'));assert.ok(!leg.validLegislature(plain(senate),'house'));
 assert.throws(()=>leg.parseLegislature(answer(39),'senate','x'),/Expected 40 districts, found 39/);
 const dup=answer(40);dup.features[1].properties.GEOID='20001';assert.throws(()=>leg.parseLegislature(dup,'senate','x'),/repeated/);
 const extra=answer(41);assert.throws(()=>leg.parseLegislature(extra,'senate','x'),/Unexpected/);
 const other=answer(40);other.features[3].properties.STATE='29';assert.throws(()=>leg.parseLegislature(other,'senate','x'),/identity/);
 const outside=answer(40);outside.features[5].geometry.coordinates=[[[-90,37],[-89,37],[-89,38],[-90,37]]];assert.throws(()=>leg.parseLegislature(outside,'senate','x'));
 assert.throws(()=>leg.parseLegislature({...answer(40),exceededTransferLimit:true},'senate','x'),/Incomplete/);
 assert.equal(leg.parseLegislature(answer(125),'house','x').data.features.length,125);
 assert.deepEqual(plain(leg.legislatureList(senate).slice(0,2)),[{id:'1',label:'Senate District 1'},{id:'2',label:'Senate District 2'}]);
 assert.equal(leg.legislatureReading('house',57),'Kansas House: 125 districts · 2024 plan · Census January 2025 geography, generalized to 1:500,000 · House District 57 picked');
 const key=leg.legislatureKey('senate');assert.equal(key.title,'Kansas Senate districts · 2024 plan');assert.match(key.note,/not for deciding which district an address is in/);
});

test('the route checks the chamber, keeps an edition a day, and refuses part of a plan',async()=>{
 const original=globalThis.fetch;const asked=[];
 const {GET}=await route('a');
 try{
  globalThis.fetch=async input=>{asked.push(String(input));return Response.json(answer(40));};
  assert.equal((await GET(new Request('http://x/api/state-legislature?chamber=congress'))).status,400);assert.equal(asked.length,0);
  const ok=await GET(new Request('http://x/api/state-legislature?chamber=senate'));
  assert.equal(ok.status,200);assert.equal((await ok.json()).data.features.length,40);assert.equal(asked[0],leg.legislatureProviderUrl('senate'));
  await GET(new Request('http://x/api/state-legislature?chamber=senate'));assert.equal(asked.length,1,'kept');
 }finally{globalThis.fetch=original;}
 const fresh=await route('b');
 try{
  globalThis.fetch=async()=>Response.json(answer(120));
  const partial=await fresh.GET(new Request('http://x/api/state-legislature?chamber=house'));
  assert.equal(partial.status,502);assert.match((await partial.json()).message,/nothing is drawn from part of a plan/);
 }finally{globalThis.fetch=original;}
});

test('districts draw as a faint fill, outlines, the picked district and numbers, under the site overlays, and are removed',()=>{
 const layers=[{id:'background',type:'background'},{id:'kfm-roads',type:'line'}],sources={};let filter=null,paint=null;
 const map={getSource:id=>sources[id]&&{setData(d){sources[id].data=d;}},addSource:(id,s)=>{sources[id]=s;},removeSource:id=>{delete sources[id];},
  getLayer:id=>layers.find(l=>l.id===id),removeLayer:id=>{layers.splice(layers.findIndex(l=>l.id===id),1);},setFilter:(id,f)=>{filter=f;},setPaintProperty:(id,k,v)=>{paint=v;},
  addLayer:(spec,before)=>{const i=before?layers.findIndex(l=>l.id===before):-1;layers.splice(i<0?layers.length:i,0,{id:spec.id,type:spec.type,spec});},getStyle:()=>({layers})};
 const senate=leg.parseLegislature(answer(40),'senate','x');
 leg.syncLegislature(map,senate,12);
 assert.deepEqual(layers.map(l=>l.id),['background',leg.LEGISLATURE_FILL_LAYER_ID,leg.LEGISLATURE_LINE_LAYER_ID,leg.LEGISLATURE_SELECTED_LAYER_ID,leg.LEGISLATURE_LABEL_LAYER_ID,'kfm-roads']);
 assert.deepEqual(plain(filter),['==',['get','district'],12]);
 assert.deepEqual(plain(layers[1].spec.paint['fill-opacity']),['case',['==',['get','district'],12],0.22,0.06]);
 assert.deepEqual(plain(layers[4].spec.layout['text-field']),['to-string',['get','district']]);
 leg.syncLegislature(map,senate,null);assert.deepEqual(plain(filter),['==',['get','district'],-1]);assert.deepEqual(plain(paint),['case',['==',['get','district'],-1],0.22,0.06]);
 leg.syncLegislature(map,null);assert.deepEqual(layers.map(l=>l.id),['background','kfm-roads']);assert.deepEqual(Object.keys(sources),[]);
});

test('the dock offers U.S. House, Kansas Senate and Kansas House; the page swaps the layers, owns the district click, and closes with its map',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.government,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  onLegislature:v=>calls.push(['chamber',v]),onLegislaturePick:v=>calls.push(['pick',v]),onLegislatureClear:()=>calls.push(['clear'])};
 const off={chamber:null,loading:false,failed:false,reading:null,list:[],picked:null};
 let tree=h.render(h.exports.CategoryMapDock,{...base,legislature:off});
 const group=findNode(tree,n=>n.props?.['aria-label']==='District plan');
 assert.deepEqual(plain(group.props.children.map(b=>[b.props.children,b.props['aria-pressed']])),[['U.S. House',true],['Kansas Senate',false],['Kansas House',false]]);
 group.props.children[1].props.onClick();group.props.children[0].props.onClick();
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,legislature:{...off,chamber:'house',loading:true}})),/Reading the Census legislative districts…/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,legislature:{...off,chamber:'house',failed:true}})),/nothing is drawn from part of a plan/);
 tree=h.render(h.exports.CategoryMapDock,{...base,legislature:{...off,chamber:'senate',reading:leg.legislatureReading('senate',3),list:[{id:'3',label:'Senate District 3'}],picked:'3'}});
 const list=findNode(tree,n=>n.props?.label==='Kansas Senate districts');assert.equal(list.props.summary,'Districts (1)');list.props.onPick('3');
 findNode(tree,n=>n.type==='button'&&n.props['aria-label']==='Clear the selected district').props.onClick();
 assert.deepEqual(calls,[['chamber','senate'],['chamber',null],['pick','3'],['clear']]);
 assert.equal(findNode(h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.water,legislature:off}),n=>n.props?.['aria-label']==='District plan'),undefined,'only maps that offer it');
 h.dispose?.();
 assert.deepEqual(plain(maps.CATEGORY_MAPS.government.tools),['legislature','reviewed']);
 assert.match(page,/legislatureHidCivicRef\.current = Boolean\(officialVisibilityRef\.current\[CIVIC_ID\]\);\s*if \(legislatureHidCivicRef\.current\) setOfficialContextVisible\(CIVIC_ID, false\);/);
 assert.match(page,/legislatureHidCivicRef\.current = false;\s*setOfficialContextVisible\(CIVIC_ID, true\);/,'the U.S. House districts come back only if they were on');
 assert.match(page,/if \(renderedHits\[0\]\?\.source === LEGISLATURE_SOURCE_ID\) \{\s*const district = renderedHits\[0\]\.properties\?\.district;\s*if \(typeof district === "number"\) \{ setLegislaturePicked\(district\); setCategoryDockHidden\(false\); \}/);
 assert.match(page,/syncLegislature\(map, shownLegislature, legislaturePicked\)/);
 assert.match(page,/const civicShown = Boolean\(officialVisibility\[CIVIC_ID\]\);\s*useEffect\(\(\) => \{\s*if \(!legislatureChamber \|\| !civicShown\) return;\s*legislatureHidCivicRef\.current = false;\s*setLegislatureChamber\(null\);\s*setLegislaturePicked\(null\);\s*\}, \[legislatureChamber, civicShown\]\);/,'turning the U.S. House districts on by any control returns to U.S. House: one plan at a time');
 assert.match(page,/legislatureHidCivicRef\.current = false;\s*setLegislatureChamber\(null\);\s*setLegislaturePicked\(null\);/,'closes with its map');
 assert.match(page,/\.\.\.\(shownLegislature \? \[legislatureKey\(shownLegislature\.chamber\)\] : \[\]\)/);
});
