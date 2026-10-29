import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const sr=await compile('app/storm-reports.ts');
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const route=await readFile('app/api/storm-reports/route.ts','utf8');

// The shape of SPC's dayN_filtered.csv: three sections, each opened by its own header row.
const csv=['Time,F_Scale,Location,County,State,Lat,Lon,Comments',
 '2215,EF2,3 W Sharon Springs,Wallace,KS,38.89,-101.81,Tornado crossed K-27, damage to outbuildings. (GLD)',
 '0130,UNK,2 N Enid,Garfield,OK,36.42,-97.88,Brief tornado reported by chasers. (OUN)',
 'Time,Speed,Location,County,State,Lat,Lon,Comments',
 '2300,UNK,Hays,Ellis,KS,38.88,-99.33,Trees down. (DDC)',
 '2310,80,5 S Russell,Russell,KS,38.82,-98.86,Measured gust at a mesonet site. (GID)',
 'Time,Size,Location,County,State,Lat,Lon,Comments',
 '2245,175,Pratt,Pratt,KS,37.64,-98.74,"Golf to tennis ball size, ""many"" reports (DDC)"',
 '2250,200,1 E Medicine Lodge,Barber,KS,3728,9857,Hen egg size. (DDC)',
 '2255,100,Nowhere,Nowhere,KS,0,0,No position.',
 ''].join('\n');
const now=new Date('2026-10-29T03:00:00Z');// before 12 UTC: "today" began Oct 28 12:00 UTC

test('the route reads one SPC convective day, allowlisted, bounded and briefly kept',()=>{
 assert.equal(sr.stormReportsProviderUrl('yesterday'),'https://www.spc.noaa.gov/climo/reports/yesterday_filtered.csv');
 assert.match(route,/if \(day !== "today" && day !== "yesterday"\)/);
 assert.match(route,/boundedFetch\(source, MAX_BYTES/);
 assert.match(route,/today: 5 \* 60 \* 1000, yesterday: 30 \* 60 \* 1000/);
});

test('the convective day runs 12:00 to 11:59 UTC, and yesterday is the one before',()=>{
 const today=sr.convectiveDay('today',now);
 assert.equal(today.from.toISOString(),'2026-10-28T12:00:00.000Z');assert.equal(today.until.toISOString(),'2026-10-29T11:59:00.000Z');
 assert.equal(sr.convectiveDay('yesterday',now).from.toISOString(),'2026-10-27T12:00:00.000Z');
 assert.equal(sr.convectiveDay('today',new Date('2026-10-28T12:00:00Z')).from.toISOString(),'2026-10-28T12:00:00.000Z');
});

test('the parser reads each section, its magnitude, time and place, and SPC\'s significant thresholds',()=>{
 const r=sr.parseStormReports(csv,'today',now,'src');
 assert.deepEqual(r.reports.map(x=>[x.kind,x.magnitude,x.significant]),[['torn',2,true],['torn',null,false],['wind',null,false],['wind',80,true],['hail',1.75,false],['hail',2,true]],'the row without a position is left out');
 const [ks]=r.reports;
 assert.equal(ks.time,'2026-10-28T22:15:00.000Z');
 assert.equal(r.reports[1].time,'2026-10-29T01:30:00.000Z','reports before 12 UTC fall on the morning that ends the day');
 assert.equal(ks.comments,'Tornado crossed K-27, damage to outbuildings. (GLD)','commas in comments survive');
 assert.equal(r.reports[4].comments,'Golf to tennis ball size, "many" reports (DDC)','a quoted comment reads as written');
 assert.deepEqual([r.reports[5].latitude,r.reports[5].longitude],[37.28,-98.57],'hundredths with west-positive longitude read as SPC means them');
 assert.equal(r.from,'2026-10-28T12:00:00.000Z');
 assert.equal(ks.id,'torn-2215-38.8900--101.8100','a report is known by kind, time and place');
 const inserted=sr.parseStormReports(csv.replace('Time,F_Scale,Location,County,State,Lat,Lon,Comments\n','Time,F_Scale,Location,County,State,Lat,Lon,Comments\n2100,EF0,Colby,Thomas,KS,39.4,-101.05,New. (GLD)\n'),'today',now,'src');
 assert.equal(inserted.reports.find(x=>x.id===ks.id)?.location,'3 W Sharon Springs','a row inserted above keeps every other id on its report');
 const twice=sr.parseStormReports('Time,Size,Location,County,State,Lat,Lon,Comments\n2245,100,A,B,KS,37.6,-98.7,x\n2245,125,A,B,KS,37.6,-98.7,y\n','today',now,'src');
 assert.deepEqual(twice.reports.map(x=>x.id),['hail-2245-37.6000--98.7000','hail-2245-37.6000--98.7000-2'],'two reports at one time and place stay distinct');
 assert.equal(sr.validStormReports(JSON.parse(JSON.stringify(r))),true);
 assert.equal(sr.validStormReports({...r,day:'tomorrow'}),false);
 assert.equal(sr.validStormReports({...r,reports:[{...ks,kind:'flood'}]}),false);
 assert.throws(()=>sr.parseStormReports('<html>Not found</html>','today',now,'src'),/no report sections/);
 assert.equal(sr.parseStormReports('Time,F_Scale,Location,County,State,Lat,Lon,Comments\nTime,Speed,Location,County,State,Lat,Lon,Comments\n','today',now,'src').reports.length,0);
});

test('the reading counts Kansas by kind, the country, and the day; magnitudes read as SPC states them',()=>{
 const r=sr.parseStormReports(csv,'today',now,'src');
 assert.equal(sr.stormReportsReading(r),'Kansas: 1 tornado, 2 wind, 2 hail reports (3 significant) · 6 across the US · Oct 28, 12:00 UTC to Oct 29, 11:59 UTC');
 assert.match(sr.stormReportsReading({...r,reports:r.reports.filter(x=>x.state!=='KS')}),/^No reports in Kansas · 1 across the US/);
 assert.match(sr.stormReportsReading({...r,reports:[]}),/^No reports yet this convective day · /);
 assert.deepEqual(r.reports.map(sr.reportMagnitude),['EF2','EF rating not yet known','speed not measured','80 mph','1.75 in','2.00 in']);
});

test('the key and the points share SPC\'s report colours, significant reports ringed, and the layers validate',async()=>{
 const key=sr.stormReportsKey('yesterday');
 assert.equal(key.title,'SPC storm reports · Yesterday');
 assert.deepEqual(key.items.map(i=>[i.label,i.color]),[['Tornado','#ff4d4d'],['Wind damage or gust','#4f8dff'],['Hail','#3fcf5f'],['Significant: EF2+, 75 mph+, 2 in+ hail','#9aa5ad']]);
 assert.equal(key.items[3].stroke,'#ffffff');assert.match(key.note,/Unverified/);
 const added=[];let source;const filters={};const layers=[{id:'radar'},{id:'kfm-spc-outlook-lines'},{id:'kfm-labels'}];
 const map={getSource:()=>source,addSource:(id,spec)=>{source={spec,setData(d){this.spec.data=d;}};},getLayer:id=>layers.find(l=>l.id===id),addLayer:(spec,before)=>{added.push([spec,before]);layers.splice(layers.findIndex(l=>l.id===before),0,{id:spec.id});},getStyle:()=>({layers}),removeLayer:id=>layers.splice(layers.findIndex(l=>l.id===id),1),removeSource:()=>{source=undefined;},setFilter:(id,f)=>{filters[id]=f;}};
 const r=sr.parseStormReports(csv,'today',now,'src');
 sr.syncStormReports(map,r,r.reports[5].id);
 assert.deepEqual(layers.map(l=>l.id),['radar','kfm-spc-outlook-lines',sr.STORM_REPORTS_LAYER_ID,sr.STORM_REPORTS_SELECTED_LAYER_ID,'kfm-labels'],'over the outlook, under the labels');
 assert.deepEqual(filters[sr.STORM_REPORTS_SELECTED_LAYER_ID],['==',['get','id'],r.reports[5].id]);
 const data=source.spec.data;
 assert.deepEqual(data.features[0].properties,{id:'torn-2215-38.8900--101.8100',kind:'torn',significant:true,rank:25});
 const {validateStyleMin}=await import('@maplibre/maplibre-gl-style-spec');
 assert.deepEqual(validateStyleMin({version:8,sources:{[sr.STORM_REPORTS_SOURCE_ID]:{type:'geojson',data}},layers:added.map(([spec])=>spec)}).map(e=>e.message),[]);
 sr.syncStormReports(map,null,null);
 assert.equal(source,undefined);assert.ok(!layers.some(l=>l.id.startsWith(sr.STORM_REPORTS_SOURCE_ID)));
});

test('the Storm desk dock offers the reports by day with the selected report',async()=>{
 const storm=maps.categoryMap('weather');
 assert.deepEqual(JSON.parse(JSON.stringify(storm.tools)),['radar','outlook','reports','rainfall','tornadoes','reviewed']);
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];let cleared=0;
 const base={look:storm,mode:'2d',depth:1,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},onReports:d=>calls.push(d),onReportClear:()=>cleared++};
 const off={day:null,loading:false,failed:false,reading:null,url:'https://www.spc.noaa.gov/climo/reports/',selected:null};
 let tree=h.render(h.exports.CategoryMapDock,{...base,reports:off});
 assert.equal(findNode(tree,n=>n.props?.['aria-label']==='Report day'),undefined);
 findNode(tree,n=>n.type==='button'&&n.props.children==='Show SPC storm reports').props.onClick();
 const report=sr.parseStormReports(csv,'today',now,'src').reports[0];
 tree=h.render(h.exports.CategoryMapDock,{...base,reports:{...off,day:'today',reading:'Kansas: 1 tornado report',selected:{report,title:'Tornado · EF2',when:'Oct 28, 22:15 UTC'}}});
 const days=findNode(tree,n=>n.props?.['aria-label']==='Report day').props.children;
 assert.deepEqual(JSON.parse(JSON.stringify(days.map(b=>[b.props.children,b.props['aria-pressed']]))),[['Today',true],['Yesterday',false]]);
 days[1].props.onClick();
 const text=JSON.stringify(tree);
 assert.match(text,/Tornado · EF2/);assert.match(text,/3 W Sharon Springs, Wallace Co\., KS/);assert.match(text,/damage to outbuildings/);
 findNode(tree,n=>n.props?.['aria-label']==='Clear the selected storm report').props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,reports:{...off,day:'today',failed:true}});
 assert.match(JSON.stringify(tree),/did not answer/);
 findNode(tree,n=>n.type==='button'&&n.props.children==='Hide storm reports').props.onClick();
 assert.deepEqual(calls,['today','yesterday',null]);assert.equal(cleared,1);
 h.dispose?.();
});

test('the page reads each day on its own clock, selects a report on the map, shares the day and closes with its map',()=>{
 assert.match(page,/fetch\(`\/api\/storm-reports\?day=\$\{reportsDay\}`/);
 assert.match(page,/const refresh = reportsDay === "today" \? 5 \* 60_000 : 30 \* 60_000;/);
 assert.match(page,/const readAt = reportsReadAtRef\.current\.get\(reportsDay\);\s*const age = current && readAt !== undefined \? Date\.now\(\) - readAt : Infinity;/,'aged by this browser\'s clock, so an old answer cannot loop the read');
 assert.match(page,/\}, \[reportsDay, stormReports, reportsFailed, reportsTick, announce\]\);/);
 assert.match(page,/if \(renderedHits\[0\]\?\.source === STORM_REPORTS_SOURCE_ID\) \{[\s\S]{0,200}if \(report\) \{ setReportSelected\(report\); setCategoryDockHidden\(false\); \}\s*return;/,'a closed dock comes back to show the report');
 assert.match(page,/if \(reportsDay\) params\.set\("reports", reportsDay\);/);
 assert.match(page,/setReportSelected\(selected => selected \? value\.reports\.find\(report => report\.id === selected\.id\) \?\? null : null\);/,'a refresh reconciles the selected report');
 assert.match(page,/categoryMap\(restoredTopic\)\?\.tools\?\.includes\("reports"\) \? restoredReports : null/);
 assert.match(page,/setReportsDay\(null\);\s*setReportSelected\(null\);\s*\/\/ Each map opens on its own subject/);
});

test('Kansas reports can be picked from a keyboard list, newest first, without the map',async()=>{
 const r=sr.parseStormReports(csv,'today',now,'src');
 const list=sr.kansasReportList(r);
 assert.equal(list.length,5,'the Oklahoma report is not listed');
 assert.deepEqual(JSON.parse(JSON.stringify(list.map(i=>i.label))),[
  '23:10 UTC · Wind damage or gust · 80 mph · 5 S Russell','23:00 UTC · Wind damage or gust · speed not measured · Hays',
  '22:50 UTC · Hail · 2.00 in · 1 E Medicine Lodge','22:45 UTC · Hail · 1.75 in · Pratt','22:15 UTC · Tornado · EF2 · 3 W Sharon Springs']);
 assert.equal(sr.kansasReportList(r,2).length,2);
 const storm=maps.categoryMap('weather');
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const picked=[];
 const base={look:storm,mode:'2d',depth:1,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},onReports(){},onReportClear(){},onReportPick:id=>picked.push(id)};
 const on={day:'today',loading:false,failed:false,reading:'Kansas: 5 reports',url:'u',selected:{report:r.reports[0],title:'Tornado · EF2',when:null},kansas:list};
 const tree=h.render(h.exports.CategoryMapDock,{...base,reports:on});
 const pick=findNode(tree,n=>n.props?.label==='Kansas storm reports, newest first');
 assert.equal(pick.props.summary,'Kansas reports (5)');
 const items=findNode(pick.type(pick.props),n=>n.props?.['aria-label']==='Kansas storm reports, newest first').props.children;
 assert.equal(items.length,5);
 const buttons=items.map(li=>li.props.children);
 assert.deepEqual(JSON.parse(JSON.stringify(buttons.map(b=>b.props['aria-pressed']))),[false,false,false,false,true],'the selected report is marked');
 buttons[3].props.onClick();
 assert.deepEqual(picked,[list[3].id]);
 h.dispose?.();
 assert.match(page,/kansas: shownReports \? kansasReportList\(shownReports\) : \[\]/);
 assert.match(page,/onReportPick=\{\(id\) => \{[\s\S]{0,260}setReportSelected\(report\);\s*easeToPicked\(\[report\.longitude, report\.latitude\]\);/);
 assert.match(page,/const easeToPicked = \(center: \[number, number\]\) => mapRef\.current\?\.easeTo\(\{ center, zoom: Math\.max\(mapRef\.current\.getZoom\(\), 8\), duration: motionDuration\(600\) \}\);/);
});
