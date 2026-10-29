import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const tor=await compile('app/tornado-record.ts');
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const plain=v=>JSON.parse(JSON.stringify(v));
const esm=async(path,replace=s=>s)=>`data:text/javascript;base64,${Buffer.from(ts.transpileModule(replace(await readFile(path,'utf8')),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`;
const upstreamUrl=await esm('app/api/event-atlas/upstream.ts');
const torUrl=await esm('app/tornado-record.ts');
const route=async tag=>import(await esm('app/api/tornado-record/route.ts',s=>s.replace('from "../event-atlas/upstream"',`from "${upstreamUrl}"`).replace('from "../../tornado-record"',`from "${torUrl}"`)+`\n// ${tag}`));

// SPC-shaped rows (values illustrative): the 1955 Udall F5, a 2007 EF5 (Greensburg), an unrated one, an Oklahoma tornado that crossed into Kansas,
// one that stayed in Oklahoma, and a malformed row.
const CSV=['om,yr,mo,dy,date,time,tz,st,stf,mag,inj,fat,loss,closs,slat,slon,elat,elon,len,wid,ns,sn,f1,f2,f3,f4,fc',
 '11,1955,5,25,1955-05-25,22:15:00,3,KS,20,5,270,80,6,0,37.1000,-97.1000,37.4000,-96.9000,25.0,600,1,1,191,0,0,0,0',
 '55,2007,5,4,2007-05-04,21:00:00,3,KS,20,5,63,11,7,0,37.4900,-99.4300,37.7000,-99.1000,28.8,2970,1,1,97,0,0,0,0',
 '70,1980,6,2,1980-06-02,15:30:00,3,KS,20,-9,0,0,0,0,38.5,-98.2,0,0,0.1,10,1,1,53,0,0,0,0',
 '80,1999,5,3,1999-05-03,19:00:00,3,OK,40,4,5,1,5,0,36.9000,-97.4000,37.2000,-97.2000,20.0,500,2,0,71,0,0,0,0',
 '81,1999,5,3,1999-05-03,19:30:00,3,OK,40,2,0,0,0,0,35.5,-97.5,35.6,-97.4,5,100,1,1,0,0,0,0,0',
 '90,1953,4,1,1953-04-01,12:00:00,3,KS,20,1,-9,-9,0,0,39.0,-96.0,0,0,1.0,30,1,1,0,0,0,0,0',
 'x,yyyy,13,1,bad,,3,KS,20,1,0,0,0,0,38,-98,38.1,-97.9,1,10,1,1,0,0,0,0,0'].join('\n');

test('the newest yearly file is tried first, back four years; ratings use the F scale before February 2007 and EF after',()=>{
 assert.deepEqual(tor.tornadoCsvCandidates(new Date('2026-10-29T00:00:00Z')),['https://www.spc.noaa.gov/wcm/data/1950-2025_actual_tornadoes.csv','https://www.spc.noaa.gov/wcm/data/1950-2024_actual_tornadoes.csv','https://www.spc.noaa.gov/wcm/data/1950-2023_actual_tornadoes.csv','https://www.spc.noaa.gov/wcm/data/1950-2022_actual_tornadoes.csv']);
 assert.equal(tor.ratingName(3,'2007-01-31'),'F3');assert.equal(tor.ratingName(3,'2007-02-01'),'EF3');assert.equal(tor.ratingName(null,'2020-01-01'),'unrated');
 assert.deepEqual([0,5,null].map(tor.ratingColor),['#d9ef8b','#7f0000','#9e9e9e']);
});

test('Kansas tornadoes are read by column name: Kansas rows, and multi-state tracks that start or end in Kansas',()=>{
 const record=tor.parseTornadoCsv(CSV,'2026-10-29T21:00:00Z','x');
 assert.deepEqual(plain(record.tornadoes.map(t=>[t.id,t.rating,t.fatalities])),[['1953-90',1,null],['1955-11',5,80],['1980-70',null,0],['1999-80',4,1],['2007-55',5,11]]);
 assert.equal(record.skipped,1);assert.equal(record.firstYear,1950);assert.equal(record.lastYear,2007);
 const udall=record.tornadoes[1];
 assert.deepEqual([record.tornadoes[0].injuries,record.tornadoes[0].fatalities],[null,null],'-9 casualties stay unknown, not zero');
 assert.deepEqual(plain(udall),{id:'1955-11',year:1955,date:'1955-05-25',time:'22:15',rating:5,injuries:270,fatalities:80,start:[-97.1,37.1],end:[-96.9,37.4],lengthMiles:25,widthYards:600,states:1});
 assert.equal(record.tornadoes[2].end,null,'an end of 0,0 is no lift-off point');
 // Columns found by name: a reordered header reads the same.
 const [head,...rows]=CSV.split('\n');const cols=head.split(',');const order=cols.map((_,i)=>i).reverse();
 const reordered=[order.map(i=>cols[i]).join(','),...rows.map(r=>{const c=r.split(',');return order.map(i=>c[i]).join(',');})].join('\n');
 assert.deepEqual(plain(tor.parseTornadoCsv(reordered,'x','x').tornadoes.map(t=>t.id)),plain(record.tornadoes.map(t=>t.id)));
 assert.throws(()=>tor.parseTornadoCsv('a,b,c\n1,2,3','x','x'),/columns changed/);
 assert.throws(()=>tor.parseTornadoCsv(CSV.split('\n').filter(l=>!/,KS,|,OK,40,4/.test(l)).join('\n'),'x','x'),/no Kansas tornadoes/);
 assert.ok(tor.validTornadoRecord(plain(record)));assert.ok(!tor.validTornadoRecord({tornadoes:[{}]}));
});

test('the view filters by year and rating, stacks the years by rating, and lists the strongest and deadliest',()=>{
 const record=tor.parseTornadoCsv(CSV,'x','x');
 assert.deepEqual(tor.tornadoSelect(record,{year:null,minRating:4}).map(t=>t.id),['1955-11','1999-80','2007-55']);
 assert.deepEqual(tor.tornadoSelect(record,{year:1980,minRating:0}).map(t=>t.id),['1980-70'],'all ratings include the unrated');
 const years=tor.tornadoYears(record,{year:1955,minRating:0});
 assert.equal(years.length,58);assert.deepEqual(plain(years.find(y=>y.year===1955)),{year:1955,total:1,byRating:[0,0,0,0,0,1,0]});
 assert.deepEqual(plain(years.find(y=>y.year===1980).byRating),[0,0,0,0,0,0,1],'the unrated in the last place');
 assert.deepEqual(plain(tor.tornadoList(record.tornadoes)),[{id:'1955-11',label:'F5 · May 25, 1955 · 80 killed · 25.0 mi'},{id:'2007-55',label:'EF5 · May 4, 2007 · 11 killed · 28.8 mi'},
  {id:'1999-80',label:'F4 · May 3, 1999 · 1 killed · 20.0 mi'},{id:'1953-90',label:'F1 · Apr 1, 1953 · 1.0 mi'},{id:'1980-70',label:'unrated · Jun 2, 1980 · 0.1 mi'}]);
 assert.equal(tor.tornadoReading(record,tor.TORNADO_DEFAULT_FILTER,record.tornadoes),'5 tornadoes in Kansas, 1950–2007 · 92 deaths · 1 with deaths unknown','unknown deaths are counted apart, not as none');
 assert.equal(tor.tornadoReading(record,{year:2007,minRating:4},tor.tornadoSelect(record,{year:2007,minRating:4})),'1 tornado of F/EF4 or stronger in Kansas, in 2007 · 11 deaths');
 assert.equal(tor.tornadoDetail(record.tornadoes[1]),'F5 · May 25, 1955 22:15 CST · 80 deaths, 270 injuries · touchdown 37.10°N, 97.10°W · lift-off 37.40°N, 96.90°W · 25.0 mi long, 600 yd wide');
 assert.match(tor.tornadoDetail(record.tornadoes[3]),/crossed 2 states$/);
 assert.match(tor.tornadoDetail(record.tornadoes[2]),/no casualties recorded · touchdown 38\.50°N, 98\.20°W · 0\.1 mi long, 10 yd wide$/);
 assert.match(tor.tornadoDetail(record.tornadoes.find(t=>t.id==='1953-90')),/^F1 · Apr 1, 1953 12:00 CST · casualties unknown · touchdown/);
 const key=tor.tornadoKey(record,tor.TORNADO_DEFAULT_FILTER);
 assert.equal(key.title,'Kansas tornadoes · 1950–2007');assert.equal(key.items.length,7);assert.match(key.note,/not the path on the ground/);
});

test('the route reads the newest file that answers and keeps it a day; it fails closed',async()=>{
 const original=globalThis.fetch;const asked=[];
 const {GET}=await route('a');
 try{
  globalThis.fetch=async input=>{asked.push(String(input));return /1950-2025_/.test(String(input))?new Response('nope',{status:404}):new Response(CSV);};
  const ok=await GET();assert.equal(ok.status,200);
  const body=await ok.json();assert.equal(body.tornadoes.length,5);assert.match(body.source,/1950-2024_actual_tornadoes\.csv$/);
  assert.equal(asked.length,2,'the newest name first, then the year before');
  await GET();assert.equal(asked.length,2,'kept');
 }finally{globalThis.fetch=original;}
 const fresh=await route('b');
 try{
  globalThis.fetch=async()=>new Response('down',{status:503});
  const failed=await fresh.GET();assert.equal(failed.status,502);assert.match((await failed.json()).message,/SPC tornado database is unavailable/);
 }finally{globalThis.fetch=original;}
});

test('tracks are drawn strongest last, wider for stronger ratings, under the site overlays; the picked track is outlined',()=>{
 const record=tor.parseTornadoCsv(CSV,'x','x');
 const collection=tor.tornadoCollection(record.tornadoes);
 assert.deepEqual(plain(collection.features.map(f=>[f.id,f.geometry.type,f.properties.rating])),[['1980-70','Point',-1],['1953-90','Point',1],['1999-80','LineString',4],['1955-11','LineString',5],['2007-55','LineString',5]]);
 const layers=[{id:'background'},{id:'kfm-roads'}],sources={},filters={};
 const map={getSource:id=>sources[id]&&{setData(){}},addSource:(id,s)=>{sources[id]=s;},removeSource:id=>{delete sources[id];},setFilter:(id,f)=>{filters[id]=f;},
  getLayer:id=>layers.find(l=>l.id===id),removeLayer:id=>{layers.splice(layers.findIndex(l=>l.id===id),1);},
  addLayer:(spec,before)=>{const i=before?layers.findIndex(l=>l.id===before):-1;layers.splice(i<0?layers.length:i,0,{id:spec.id,spec});},getStyle:()=>({layers})};
 tor.syncTornadoRecord(map,collection,'1955-11');
 assert.deepEqual(layers.map(l=>l.id),['background',tor.TORNADO_SELECTED_LAYER_ID,tor.TORNADO_LINE_LAYER_ID,tor.TORNADO_POINT_LAYER_ID,tor.TORNADO_SELECTED_POINT_LAYER_ID,'kfm-roads']);
 assert.deepEqual(plain(filters[tor.TORNADO_SELECTED_LAYER_ID]),['all',['==',['geometry-type'],'LineString'],['==',['get','id'],'1955-11']]);
 assert.deepEqual(plain(filters[tor.TORNADO_SELECTED_POINT_LAYER_ID]),['all',['==',['geometry-type'],'Point'],['==',['get','id'],'1955-11']],'a touchdown-only report is ringed when picked');
 tor.syncTornadoRecord(map,collection,'1980-70');
 assert.deepEqual(plain(filters[tor.TORNADO_SELECTED_POINT_LAYER_ID]),['all',['==',['geometry-type'],'Point'],['==',['get','id'],'1980-70']]);
 assert.deepEqual(plain(layers[2].spec.paint['line-color']),['get','color']);
 tor.syncTornadoRecord(map,null);assert.deepEqual(layers.map(l=>l.id),['background','kfm-roads']);assert.deepEqual(Object.keys(sources),[]);
});

test('the dock offers the record on the Storm desk; the page hides and restores the alerts and radar, owns the track click, and closes it with its map',async()=>{
 const record=tor.parseTornadoCsv(CSV,'x','x');
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const base={look:maps.CATEGORY_MAPS.weather,mode:'2d',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  onTornadoes:v=>calls.push(['on',v]),onTornadoYear:v=>calls.push(['year',v]),onTornadoRating:v=>calls.push(['rating',v]),onTornadoPick:v=>calls.push(['pick',v]),onTornadoClear:()=>calls.push(['clear'])};
 const series=[...tor.TORNADO_RATINGS.map(r=>({name:r.name,color:r.color})),{name:'Unrated',color:tor.UNRATED_COLOR}];
 const off={on:false,loading:false,failed:false,reading:null,series,years:null,year:null,minRating:0,list:[],picked:null};
 const tool=tree=>findNode(tree,n=>n.type==='button'&&/tornado record/i.test(String(n.props.children)));
 let tree=h.render(h.exports.CategoryMapDock,{...base,tornadoes:off});
 assert.equal(tool(tree).props.children,'Tornado record since 1950');tool(tree).props.onClick();
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,tornadoes:{...off,on:true,loading:true}})),/Reading the SPC tornado database…/);
 assert.match(JSON.stringify(h.render(h.exports.CategoryMapDock,{...base,tornadoes:{...off,on:true,failed:true}})),/did not answer/);
 const years=tor.tornadoYears(record,tor.TORNADO_DEFAULT_FILTER);
 tree=h.render(h.exports.CategoryMapDock,{...base,tornadoes:{...off,on:true,reading:tor.tornadoReading(record,tor.TORNADO_DEFAULT_FILTER,record.tornadoes),years,list:tor.tornadoList(record.tornadoes),
  picked:{id:'1955-11',detail:tor.tornadoDetail(record.tornadoes[1])}}});
 assert.equal(tool(tree).props.children,'Hide the tornado record');
 const chart=findNode(tree,n=>n.type===h.exports.TornadoHistory);const figure=chart.type(chart.props);
 assert.match(figure.props['aria-label'],/^Kansas tornadoes per year, 1950–2007, by rating; the most in one year is 1$/);
 findNode(figure,n=>n.type==='g'&&n.props['data-year']===1955).props.onClick();
 assert.match(JSON.stringify(figure),/"fill":"#7f0000"/);
 const selects=[];findNode(tree,n=>{if(n.type==='select')selects.push(n);return false;});
 selects[0].props.onChange({target:{value:'2007'}});selects[1].props.onChange({target:{value:'4'}});
 const list=findNode(tree,n=>n.props?.label==='Kansas tornadoes, strongest first, then deadliest');assert.equal(list.props.summary,'Strongest and deadliest (5)');list.props.onPick('2007-55');
 assert.match(JSON.stringify(tree),/80 deaths, 270 injuries/);
 findNode(tree,n=>n.type==='button'&&n.props['aria-label']==='Clear the selected tornado').props.onClick();
 assert.deepEqual(calls,[['on',true],['year',1955],['year',2007],['rating',4],['pick','2007-55'],['clear']]);
 assert.equal(tool(h.render(h.exports.CategoryMapDock,{...base,look:maps.CATEGORY_MAPS.water,tornadoes:off})),undefined,'only maps that offer it');
 h.dispose?.();
 assert.ok(maps.CATEGORY_MAPS.weather.tools.includes('tornadoes'));
 assert.match(page,/tornadoHidRef\.current = \(\["nws-alerts", "nws-radar"\] as const\)\.filter\(id => officialVisibilityRef\.current\[id\]\);/);
 assert.match(page,/for \(const id of tornadoHidRef\.current\) setOfficialContextVisible\(id, true\);\s*tornadoHidRef\.current = \[\];/);
 assert.match(page,/if \(renderedHits\[0\]\?\.source === TORNADO_SOURCE_ID\) \{\s*const id = renderedHits\[0\]\.properties\?\.id;\s*if \(typeof id === "string"\) \{ setTornadoPicked\(id\); setCategoryDockHidden\(false\); \}/);
 assert.match(page,/void fetch\("\/api\/tornado-record", \{ signal: controller\.signal \}\)/);
 assert.match(page,/tornadoHidRef\.current = \[\];\s*setTornadoOn\(false\);\s*setTornadoPicked\(null\);/,'closes with its map');
 assert.match(page,/\.\.\.\(tornadoOn && tornadoRecord \? \[tornadoKey\(tornadoRecord, tornadoFilter\)\] : \[\]\)/);
});
