import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const fema=await compile('app/fema-record.ts');
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const plain=v=>JSON.parse(JSON.stringify(v));
const esm=async(path,replace=s=>s)=>`data:text/javascript;base64,${Buffer.from(ts.transpileModule(replace(await readFile(path,'utf8')),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`;
const upstreamUrl=await esm('app/api/event-atlas/upstream.ts');
const femaUrl=await esm('app/fema-record.ts');
const {GET}=await import(await esm('app/api/fema-record/route.ts',s=>s.replace('from "../event-atlas/upstream"',`from "${upstreamUrl}"`).replace('from "../../fema-record"',`from "${femaUrl}"`)));

// OpenFEMA-shaped rows (synthetic): a 1993 flood in two counties, a 2007 ice storm in three, a 2007 tornado in one,
// a statewide 2020 biological emergency, a tribal row, a bad row and a duplicate.
const row=(id,n,type,date,incident,title,county,area)=>({id,disasterNumber:n,declarationType:type,declarationDate:`${date}T00:00:00.000Z`,incidentType:incident,declarationTitle:title,
 incidentBeginDate:`${date}T00:00:00.000Z`,incidentEndDate:null,fipsStateCode:'20',fipsCountyCode:county,designatedArea:area});
const rows=[
 row('a1',1000,'DR','1993-07-22','Flood','FLOODING','045','Douglas (County)'),row('a2',1000,'DR','1993-07-22','Flood','FLOODING','177','Shawnee (County)'),
 row('b1',1741,'DR','2007-12-21','Severe Ice Storm','SEVERE WINTER STORMS','173','Sedgwick (County)'),row('b2',1741,'DR','2007-12-21','Severe Ice Storm','SEVERE WINTER STORMS','177','Shawnee (County)'),
 row('b3',1741,'DR','2007-12-21','Severe Ice Storm','SEVERE WINTER STORMS','045','Douglas (County)'),
 row('c1',1699,'DR','2007-05-06','Tornado','SEVERE STORMS, TORNADOES','097','Kiowa (County)'),
 row('d1',3443,'EM','2020-03-13','Biological','COVID-19','000','Statewide'),
 row('e1',1800,'DR','2008-06-01','Severe Storm(s)','SEVERE STORMS','000','Kickapoo Tribe'),
 {id:'f1',disasterNumber:'x'},row('a1',1000,'DR','1993-07-22','Flood','FLOODING','045','Douglas (County)'),
];
const counties={type:'FeatureCollection',features:['20045','20173','20177','20097','20001'].map((geoid,i)=>({type:'Feature',properties:{geoid,name:['Douglas','Sedgwick','Shawnee','Kiowa','Allen'][i]},
 geometry:{type:'Polygon',coordinates:[[[i,0],[i+1,0],[i+1,1],[i,1],[i,0]]]}}))};
const geoids=counties.features.map(f=>f.properties.geoid);

test('the OpenFEMA query asks for Kansas rows, the fields used, a page at a time in a stable order',()=>{
 const url=new URL(fema.femaRecordPageUrl(2));
 assert.equal(url.origin+url.pathname,'https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries');
 assert.equal(url.searchParams.get('$filter'),"state eq 'KS'");assert.equal(url.searchParams.get('$orderby'),'id');
 assert.equal(url.searchParams.get('$top'),'1000');assert.equal(url.searchParams.get('$skip'),'2000');
 assert.match(url.searchParams.get('$select'),/disasterNumber,declarationType,declarationDate,incidentType,declarationTitle/);
 assert.equal(fema.femaDisasterPage(1741),'https://www.fema.gov/disaster/1741');
});

test('rows gather into declarations with their counties; statewide is kept, tribal and bad rows are skipped',()=>{
 const record=fema.parseFemaRecord(rows,'2026-10-29T17:00:00Z',fema.FEMA_RECORD_SOURCE);
 assert.deepEqual(plain(record.disasters.map(d=>[d.type,d.number,d.family,d.year,d.counties,d.statewide])),[
  ['DR',1000,'flood',1993,['20045','20177'],false],['DR',1699,'storm',2007,['20097'],false],['DR',1741,'winter',2007,['20045','20173','20177'],false],['EM',3443,'biological',2020,[],true]]);
 assert.equal(record.skipped,3,'the tribal row, the bad row and the duplicate');
 assert.equal(record.firstYear,1993);assert.equal(record.lastYear,2020);assert.equal(record.rows,10);
 assert.equal(record.disasters[2].title,'SEVERE WINTER STORMS');assert.equal(record.disasters[2].declared,'2007-12-21');
 assert.deepEqual(['Severe Storm(s)','severe storm','Tornado','Flood','Snowstorm','Fire','Drought','Biological','Earthquake',null].map(fema.hazardFamily),
  ['storm','storm','storm','flood','winter','fire','drought','biological','other','other']);
 assert.ok(fema.validFemaRecord(plain(record)));assert.ok(!fema.validFemaRecord({disasters:[{}]}));
});

test('the route reads OpenFEMA page by page until a short page, and says when the record was cut short',async()=>{
 const original=globalThis.fetch;const asked=[];
 try{
  globalThis.fetch=async input=>{const url=new URL(String(input));asked.push(url.searchParams.get('$skip'));
   const skip=Number(url.searchParams.get('$skip'));
   const page=skip===0?Array.from({length:1000},(_,i)=>row(`p${i}`,1000+(i%3),'DR','2001-02-0'+(1+i%3),'Flood','F',String(1+2*(i%50)).padStart(3,'0'),'X')):rows;
   return Response.json({metadata:{},DisasterDeclarationsSummaries:page});};
  const response=await GET();assert.equal(response.status,200);
  const record=await response.json();
  assert.deepEqual(asked,['0','1000'],'stops after the short second page');
  assert.equal(record.truncated,false);assert.equal(record.firstYear,1993);
  assert.ok(record.disasters.find(d=>d.number===1000).counties.length>2,'rows of one disaster on both pages are gathered');
  // A fresh answer is kept: the next call asks nothing.
  await GET();assert.equal(asked.length,2);
 }finally{globalThis.fetch=original;}
 const fresh=await import(await esm('app/api/fema-record/route.ts',s=>s.replace('from "../event-atlas/upstream"',`from "${upstreamUrl}"`).replace('from "../../fema-record"',`from "${femaUrl}"`)+'\n// fresh'));
 try{
  globalThis.fetch=async()=>new Response('nope',{status:503});
  const failed=await fresh.GET();assert.equal(failed.status,502);assert.match((await failed.json()).message,/OpenFEMA is unavailable/);
 }finally{globalThis.fetch=original;}
 assert.match(await readFile('app/api/event-atlas/upstream.ts','utf8'),/"https:\/\/www\.fema\.gov"/,'fema.gov is on the allowlist');
});

test('the view counts major disasters by year, family and county; a statewide declaration counts for every county',()=>{
 const record=fema.parseFemaRecord(rows,'2026-10-29T17:00:00Z','x');
 const dr=fema.FEMA_DEFAULT_FILTER;
 assert.deepEqual(fema.femaSelect(record,dr).map(d=>d.number),[1000,1699,1741],'emergencies are left out by default');
 assert.deepEqual(fema.femaSelect(record,{...dr,emergencies:true}).map(d=>d.number),[1000,1699,1741,3443]);
 assert.deepEqual(fema.femaSelect(record,{...dr,family:'winter'}).map(d=>d.number),[1741]);
 assert.deepEqual(fema.femaSelect(record,{...dr,year:2007}).map(d=>d.number),[1699,1741]);
 const years=fema.femaYears(record,{...dr,year:2007});
 assert.equal(years.length,28,'every year 1993–2020; the year filter does not narrow the chart');
 assert.deepEqual(plain(years.find(y=>y.year===2007)),{year:2007,total:2,byFamily:[1,0,1,0,0,0,0]});
 assert.equal(years.find(y=>y.year===2000).total,0);
 const counts=fema.femaCountyCounts(fema.femaSelect(record,dr),geoids);
 assert.deepEqual(Object.fromEntries(counts),{'20045':2,'20173':1,'20177':2,'20097':1,'20001':0});
 const withEm=fema.femaCountyCounts(fema.femaSelect(record,{...dr,emergencies:true}),geoids);
 assert.deepEqual([...withEm.values()],[3,2,3,2,1],'the statewide emergency counts everywhere');
 const names=new Map(counties.features.map(f=>[f.properties.geoid,f.properties.name]));
 assert.deepEqual(plain(fema.femaCountyList(counts,names)),[{id:'20045',label:'Douglas · 2'},{id:'20177',label:'Shawnee · 2'},{id:'20097',label:'Kiowa · 1'},{id:'20173',label:'Sedgwick · 1'},{id:'20001',label:'Allen · 0'}]);
 assert.deepEqual(plain(fema.femaCountyDisasters(fema.femaSelect(record,dr),'20177')),[{id:'1741',label:'DR-1741 · SEVERE WINTER STORMS · Dec 2007'},{id:'1000',label:'DR-1000 · FLOODING · Jul 1993'}]);
});

test('counties are classed in five round, equal steps from one to the most, with none in its own pale colour',()=>{
 assert.deepEqual(plain(fema.femaClasses(23)),[{from:1,to:5,color:'#fdd0a2'},{from:6,to:10,color:'#fdae6b'},{from:11,to:15,color:'#f16913'},{from:16,to:20,color:'#d94801'},{from:21,to:25,color:'#8c2d04'}]);
 assert.deepEqual(plain(fema.femaClasses(3)).map(c=>[c.from,c.to]),[[1,1],[2,2],[3,3]],'small counts get one class each');
 assert.deepEqual(plain(fema.femaClasses(0)),[]);
 const classes=fema.femaClasses(23);
 assert.deepEqual([0,1,5,6,23,40].map(n=>fema.femaCountColor(n,classes)),[fema.FEMA_NONE_COLOR,'#fdd0a2','#fdd0a2','#fdae6b','#8c2d04','#8c2d04']);
 const collection=fema.femaCountyCollection(counties,new Map([['20045',2],['20173',0]]));
 assert.deepEqual(plain(collection.features.map(f=>[f.properties.geoid,f.properties.count,f.properties.color])),[['20045',2,'#fdae6b'],['20173',0,fema.FEMA_NONE_COLOR]],'only counted counties are drawn');
 const key=fema.femaKey(classes,fema.FEMA_DEFAULT_FILTER,1953,2026);
 assert.equal(key.title,'FEMA major disaster declarations per county · 1953–2026');
 assert.deepEqual(plain(key.items.map(i=>i.label)),['None','1–5','6–10','11–15','16–20','21–25']);
 assert.match(key.note,/not a map of the damage/);
 assert.equal(fema.femaKey(classes,{family:'flood',emergencies:true,year:1993},1953,2026).title,'FEMA declarations per county · 1993 · Floods');
});

test('the readings give the statewide record and the picked county\'s',()=>{
 const record=fema.parseFemaRecord(rows,'2026-10-29T17:00:00Z','x');
 const dr=fema.FEMA_DEFAULT_FILTER;
 assert.equal(fema.femaReading(record,dr,fema.femaYears(record,dr)),'3 major disaster declarations in Kansas, 1993–2020 · most in 2007 (2)');
 assert.equal(fema.femaReading(record,{...dr,year:2007,family:'storm'},fema.femaYears(record,{...dr,family:'storm'})),'1 major disaster declaration in Kansas in 2007 · severe storms & tornadoes · choose All years for the record');
 assert.match(fema.femaReading({...record,truncated:true},dr,fema.femaYears(record,dr)),/the OpenFEMA answer was cut short$/);
 assert.equal(fema.femaCountyReading('Shawnee','20177',fema.femaSelect(record,dr),dr,1993),'Shawnee County: 2 major disaster declarations since 1993 · most often floods (1) · latest DR-1741, declared Dec 2007');
 assert.equal(fema.femaCountyReading('Allen','20001',fema.femaSelect(record,dr),dr,1993),'Allen County: no major disaster declarations since 1993');
 assert.equal(fema.femaCountyReading('Allen','20001',fema.femaSelect(record,{...dr,emergencies:true}),{...dr,emergencies:true},1993),'Allen County: 1 declaration since 1993 · most often biological (1) · latest EM-3443, declared Mar 2020');
});

test('the choropleth sits under the site\'s overlays, outlines the picked county, and is removed with the record',()=>{
 const layers=[{id:'background'},{id:'external-nws-alerts-fill'},{id:'kfm-roads'}],sources={};let filter=null;
 const map={getSource:id=>sources[id]&&{setData:d=>{sources[id].data=d;}},addSource:(id,s)=>{sources[id]=s;},removeSource:id=>{delete sources[id];},
  getLayer:id=>layers.find(l=>l.id===id),removeLayer:id=>{layers.splice(layers.findIndex(l=>l.id===id),1);},
  addLayer:(spec,before)=>{const i=before?layers.findIndex(l=>l.id===before):-1;layers.splice(i<0?layers.length:i,0,{id:spec.id,spec});},
  getStyle:()=>({layers}),setFilter:(id,f)=>{filter=[id,f];}};
 const collection=fema.femaCountyCollection(counties,new Map([['20045',2]]));
 fema.syncFemaRecord(map,collection,'20045');
 assert.deepEqual(layers.map(l=>l.id),['background','external-nws-alerts-fill',fema.FEMA_RECORD_FILL_LAYER_ID,fema.FEMA_RECORD_LINE_LAYER_ID,fema.FEMA_RECORD_SELECTED_LAYER_ID,'kfm-roads']);
 assert.deepEqual(plain(filter),[fema.FEMA_RECORD_SELECTED_LAYER_ID,['==',['get','geoid'],'20045']]);
 assert.deepEqual(plain(layers[2].spec.paint['fill-color']),['get','color']);
 fema.syncFemaRecord(map,collection,null);assert.deepEqual(plain(filter[1]),['==',['get','geoid'],'']);
 fema.syncFemaRecord(map,null);
 assert.deepEqual(layers.map(l=>l.id),['background','external-nws-alerts-fill','kfm-roads']);assert.deepEqual(Object.keys(sources),[]);
});

test('the dock offers the record on Hazard watch: chart, filters, county list and the picked county\'s declarations',async()=>{
 const record=fema.parseFemaRecord(rows,'2026-10-29T17:00:00Z','x');
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.disaster,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  onFema:v=>calls.push(['on',v]),onFemaYear:v=>calls.push(['year',v]),onFemaFamily:v=>calls.push(['family',v]),onFemaEmergencies:v=>calls.push(['em',v]),onFemaCounty:v=>calls.push(['county',v]),onFemaCountyClear:()=>calls.push(['clear'])};
 const off={on:false,loading:false,failed:false,reading:null,families:fema.HAZARD_FAMILIES,years:null,year:null,family:null,emergencies:false,counties:null};
 const tool=tree=>findNode(tree,n=>n.type==='button'&&/FEMA disaster record|current hazards/.test(String(n.props.children)));
 let tree=h.render(h.exports.CategoryMapDock,{...base,fema:off});
 assert.equal(tool(tree).props.children,'FEMA disaster record since 1953');tool(tree).props.onClick();
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,fema:{...off,on:true,loading:true}})),/Reading the OpenFEMA declarations…/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,fema:{...off,on:true,failed:true}})),/OpenFEMA did not answer/);
 const years=fema.femaYears(record,fema.FEMA_DEFAULT_FILTER);
 const on={...off,on:true,reading:'3 major disaster declarations in Kansas, 1993–2020 · most in 2007 (2)',years,
  counties:{list:[{id:'20045',label:'Douglas · 2'}],picked:'20177',reading:'Shawnee County: 2 major disaster declarations since 1993',declarations:[{id:'1741',label:'DR-1741 · SEVERE WINTER STORMS · Dec 2007'}]}};
 tree=h.render(h.exports.CategoryMapDock,{...base,fema:on});
 assert.equal(tool(tree).props.children,'Back to current hazards');assert.equal(tool(tree).props['aria-pressed'],true);
 const chart=findNode(tree,n=>n.type===h.exports.FemaHistory);
 const figure=chart.type(chart.props);
 assert.match(figure.props['aria-label'],/FEMA declarations per year, 1993–2020, by hazard; the most in one year is 2/);
 const bar=findNode(figure,n=>n.type==='g'&&n.props['data-year']===2007);bar.props.onClick();
 const svg=JSON.stringify(figure);
 assert.match(svg,/"fill":"#6a51a3"/);assert.match(svg,/"fill":"#41b6c4"/);
 assert.match(svg,/Severe storms & tornadoes/);assert.doesNotMatch(svg,/Drought/,'only families in the record are named');
 const selects=[];findNode(tree,n=>{if(n.type==='select')selects.push(n);return false;});
 selects[0].props.onChange({target:{value:'1993'}});selects[0].props.onChange({target:{value:''}});selects[1].props.onChange({target:{value:'flood'}});
 findNode(tree,n=>n.type==='input'&&n.props.type==='checkbox').props.onChange({target:{checked:true}});
 const list=findNode(tree,n=>n.props?.label==='Kansas counties by FEMA declarations, most first');
 assert.equal(list.props.summary,'Counties, most declarations first (1)');list.props.onPick('20045');
 assert.match(JSON.stringify(tree),/"href":"https:\/\/www\.fema\.gov\/disaster\/1741"/);
 findNode(tree,n=>n.type==='button'&&n.props['aria-label']==='Clear the selected county').props.onClick();
 assert.deepEqual(calls,[['on',true],['year',2007],['year',1993],['year',null],['family','flood'],['em',true],['county','20045'],['clear']]);
 assert.equal(tool(h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.water,fema:off})),undefined,'only maps that offer it');
 // A chosen year stays in the select (at 0) when a hazard filter leaves it empty, so the select shows what the map counts.
 const empty=h.render(h.exports.CategoryMapDock,{...base,fema:{...on,year:2000,family:'fire',years:fema.femaYears(record,{...fema.FEMA_DEFAULT_FILTER,family:'fire'})}});
 const yearSelect=findNode(empty,n=>n.type==='select');
 assert.equal(yearSelect.props.value,2000);
 assert.deepEqual(JSON.parse(JSON.stringify(yearSelect.props.children[1].map(o=>o.props.value))),[2000]);
 h.dispose?.();
 assert.deepEqual(plain(maps.CATEGORY_MAPS.disaster.tools),['fema','reviewed']);
});

test('the page reads the record, hides and restores the current hazards, owns the county click, and closes it with its map',()=>{
 assert.match(page,/void fetch\("\/api\/fema-record", \{ signal: controller\.signal \}\)/);
 assert.match(page,/if \(!validFemaRecord\(value\)\) throw new Error\("Invalid FEMA record\."\);/);
 assert.match(page,/femaHidRef\.current = \(\["nws-alerts", "nasa-gibs-fire-points", "nifc-fire-reports"\] as const\)\.filter\(id => officialVisibilityRef\.current\[id\]\);\s*for \(const id of femaHidRef\.current\) setOfficialContextVisible\(id, false\);/);
 assert.match(page,/for \(const id of femaHidRef\.current\) setOfficialContextVisible\(id, true\);\s*femaHidRef\.current = \[\];/,'only what it hid comes back');
 assert.match(page,/if \(renderedHits\[0\]\?\.source === FEMA_RECORD_SOURCE_ID\) \{\s*const geoid = renderedHits\[0\]\.properties\?\.geoid;\s*if \(typeof geoid === "string"\) \{ setFemaCounty\(geoid\); setCategoryDockHidden\(false\); \}/);
 assert.match(page,/syncFemaRecord\(map, femaOn \? femaCollection : null, femaCounty\)/);
 assert.match(page,/femaHidRef\.current = \[\];\s*setFemaOn\(false\);\s*setFemaCounty\(null\);/,'closes with its map');
 assert.match(page,/void refreshOfficialContext\("census-counties"\);\s*\}, \[femaOn, officialPayloads, refreshOfficialContext\]\);/);
 assert.match(page,/\.\.\.\(femaOn && femaRecord && femaCounts \? \[femaKey\(femaClassList, femaFilter, femaRecord\.firstYear, femaRecord\.lastYear\)\] : \[\]\)/);
});
