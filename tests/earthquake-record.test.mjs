import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const orientation=await compile('app/kansas-orientation.ts');
const quakes=await compile('app/earthquake-record.ts',{'./kansas-orientation':orientation});
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const route=await readFile('app/api/earthquake-record/route.ts','utf8');
const upstream=await readFile('app/api/event-atlas/upstream.ts','utf8');

const feature=(id,time,mag,lon,lat,depth=5,extra={})=>({type:'Feature',id,geometry:{type:'Point',coordinates:[lon,lat,depth]},properties:{mag,time:Date.parse(time),magType:'mb_lg',place:'Kansas',status:'reviewed',type:'earthquake',...extra}});

test('the USGS query asks for the state, M2.5 and up, from 1973, oldest first, and one past the limit',()=>{
 const url=new URL(quakes.earthquakeRecordProviderUrl(new Date('2026-10-26T12:00:00Z')));
 assert.equal(url.origin+url.pathname,'https://earthquake.usgs.gov/fdsnws/event/1/query');
 const p=Object.fromEntries(url.searchParams);
 assert.equal(p.starttime,'1973-01-01T00:00:00Z');assert.equal(p.endtime,'2026-10-26T12:00:00.000Z');
 assert.equal(p.minmagnitude,'2.5');assert.equal(p.eventtype,'earthquake');assert.equal(p.orderby,'time-asc');
 assert.equal(Number(p.limit),quakes.EARTHQUAKE_RECORD_LIMIT+1);
 assert.deepEqual([p.minlongitude,p.minlatitude,p.maxlongitude,p.maxlatitude].map(Number),[-102.06,36.99,-94.58,40.01]);
 assert.match(upstream,/"https:\/\/earthquake\.usgs\.gov"/,'the origin is on the bounded fetch allowlist');
 assert.match(route,/boundedFetch\(source, MAX_BYTES/);
 assert.match(route,/s-maxage=21600/);
});

test('only epicentres inside the Census state outline are kept',()=>{
 assert.equal(quakes.insideKansas(-97.6,37.3),true,'Harper/Sumner counties');
 assert.equal(quakes.insideKansas(-98.2,36.95),false,'northern Oklahoma, inside the bounding box');
 assert.equal(quakes.insideKansas(-94.85,39.77),false,'St. Joseph, Missouri, east of the river');
 assert.equal(quakes.insideKansas(-95.68,39.05),true,'Topeka');
 assert.equal(quakes.insideKansas(-101.5,39.0),true,'western Kansas');
});

test('the parser keeps valid Kansas events, sorted, and says what it left out',()=>{
 const raw={type:'FeatureCollection',features:[
  feature('us2000abcd','2015-03-01T10:00:00Z',3.4,-97.7,37.2),
  feature('ok2015xyz','2015-03-02T10:00:00Z',3.9,-98.0,36.95),// Oklahoma
  feature('us1980aaaa','1989-06-15T00:00:00Z',4.0,-96.6,39.2,null),
  feature('bad id!','2016-01-01T00:00:00Z',3.0,-97.5,37.5),
  feature('us2016bbbb','2016-01-01T00:00:00Z',null,-97.5,37.5),
  feature('us2016cccc','2016-02-01T00:00:00Z',2.7,-97.5,37.5,5,{type:'quarry blast'}),
  {type:'Feature',id:'us2017dddd',geometry:null,properties:{mag:3,time:Date.parse('2017-01-01T00:00:00Z')}},
 ]};
 const record=quakes.parseEarthquakeRecord(raw,'2026-10-26T00:00:00.000Z','https://earthquake.usgs.gov/fdsnws/event/1/query?x');
 assert.deepEqual(record.events.map(e=>e.id),['us1980aaaa','us2000abcd']);
 assert.equal(record.outsideKansas,1);assert.equal(record.truncated,false);assert.equal(record.endYear,2026);
 assert.deepEqual({...record.events[1]},{id:'us2000abcd',time:'2015-03-01T10:00:00.000Z',year:2015,magnitude:3.4,magnitudeType:'mb_lg',depthKilometers:5,place:'Kansas',status:'reviewed',longitude:-97.7,latitude:37.2});
 assert.equal(record.events[0].depthKilometers,null,'a missing depth stays missing');
 assert.equal(quakes.validEarthquakeRecord(JSON.parse(JSON.stringify(record))),true);
 assert.equal(quakes.validEarthquakeRecord({events:[{id:1}],startYear:1973,endYear:2026,minMagnitude:2.5,truncated:false,retrievedAt:'x'}),false);
 assert.equal(quakes.validEarthquakeRecord({...JSON.parse(JSON.stringify(record)),minMagnitude:undefined}),false);
 assert.throws(()=>quakes.parseEarthquakeRecord({error:'x'},'2026-10-26T00:00:00.000Z','s'));
 const many={features:Array.from({length:quakes.EARTHQUAKE_RECORD_LIMIT+1},(_,i)=>feature(`us${String(i).padStart(8,'0')}`,'2015-01-01T00:00:00Z',2.6,-97.6,37.3))};
 const cut=quakes.parseEarthquakeRecord(many,'2026-10-26T00:00:00.000Z','s');
 assert.equal(cut.truncated,true);assert.equal(cut.events.length,quakes.EARTHQUAKE_RECORD_LIMIT);
});

test('annual counts cover every year of the record, empty years included',()=>{
 const counts=quakes.annualCounts({startYear:1973,endYear:1976,events:[{year:1974},{year:1974},{year:1976}]});
 assert.deepEqual(counts.map(c=>[c.year,c.count]),[[1973,0],[1974,2],[1975,0],[1976,1]]);
});

test('the year colours, the map expression and the key share one ramp',()=>{
 const end=2026;
 assert.equal(quakes.recordYearColor(1975,end),quakes.RECORD_RAMP[0],'every year before 2010 shares the first colour');
 assert.equal(quakes.recordYearColor(2010,end),quakes.RECORD_RAMP[0]);
 assert.equal(quakes.recordYearColor(end,end),quakes.RECORD_RAMP[4]);
 assert.equal(quakes.recordYearColor(2018,end),quakes.RECORD_RAMP[2],'the middle stop sits at the middle year');
 const expression=quakes.recordColor(end);
 assert.deepEqual(expression.slice(0,3),['interpolate',['linear'],['get','year']]);
 assert.deepEqual(expression.slice(3).filter((_,i)=>i%2===0),[2010,2014,2018,2022,2026]);
 const key=quakes.earthquakeRecordKey(end);
 assert.equal(key.title,'Earthquakes M2.5+ by year');
 assert.deepEqual(key.ramp.ticks.map(t=>t.label),['≤2009','2015','2020','2025']);
 assert.ok(key.ramp.ticks.every((t,i,a)=>i===0||t.at>a[i-1].at+12),'ticks do not crowd each other');
 assert.match(key.ramp.css,new RegExp(`^linear-gradient\\(to right, ${quakes.RECORD_RAMP[0]} 0% 20%, ${quakes.RECORD_RAMP[0]} 20%,.* ${quakes.RECORD_RAMP[4]} 100%\\)$`));
 // Diameters at zoom 5: radius 2.2 at M2.5, 4.5 at M4, 7 at M5.
 assert.deepEqual(key.items.map(i=>[i.label,i.size]),[['M 2.5',4],['M 3',6],['M 4',9],['M 5',14]]);
 assert.match(key.note,/Detection improved/);
});

test('the map layers draw the record, filter a year and ring the selected event',()=>{
 const calls=[];const layers=[{id:'background'},{id:'kfm-roads'}];let source=null;
 const map={getSource:id=>id===quakes.EARTHQUAKE_RECORD_SOURCE_ID?source:undefined,addSource:(id,spec)=>{source={spec,setData(d){calls.push(['setData',d.features.length]);}};calls.push(['addSource',id,spec.data.features.length]);},
  getLayer:id=>layers.find(l=>l.id===id),addLayer:(spec,before)=>{layers.splice(layers.findIndex(l=>l.id===before),0,{id:spec.id,spec});calls.push(['addLayer',spec.id,before]);},
  getStyle:()=>({layers}),setFilter:(id,f)=>calls.push(['setFilter',id,f]),removeLayer:id=>{layers.splice(layers.findIndex(l=>l.id===id),1);calls.push(['removeLayer',id]);},removeSource:id=>{source=null;calls.push(['removeSource',id]);}};
 const record={endYear:2026,events:[{id:'a',year:2015,magnitude:3,longitude:-97.6,latitude:37.3},{id:'b',year:1989,magnitude:4,longitude:-96.6,latitude:39.2}]};
 quakes.syncEarthquakeRecord(map,record,2015,'a');
 assert.deepEqual(calls.slice(0,3),[['addSource','kfm-earthquake-record',2],['addLayer','kfm-earthquake-record-points','kfm-roads'],['addLayer','kfm-earthquake-record-selected','kfm-roads']]);
 assert.deepEqual(layers.map(l=>l.id),['background','kfm-earthquake-record-points','kfm-earthquake-record-selected','kfm-roads'],'above the base, under the site overlays');
 const points=layers[1].spec;
 assert.deepEqual(points.paint['circle-color'],quakes.recordColor(2026));
 assert.deepEqual(points.layout['circle-sort-key'],['get','magnitude'],'larger events draw on top');
 assert.deepEqual(calls.filter(c=>c[0]==='setFilter'),[['setFilter','kfm-earthquake-record-points',['==',['get','year'],2015]],['setFilter','kfm-earthquake-record-selected',['==',['get','id'],'a']]]);
 calls.length=0;
 quakes.syncEarthquakeRecord(map,record,null,null);
 assert.deepEqual(calls,[['setFilter','kfm-earthquake-record-points',null],['setFilter','kfm-earthquake-record-selected',['==',['get','id'],'']]],'the same record is not sent again');
 calls.length=0;
 quakes.syncEarthquakeRecord(map,null,null,null);
 assert.deepEqual(calls.map(c=>c[0]),['removeLayer','removeLayer','removeSource']);
 assert.equal(quakes.earthquakeEventUrl('us2000abcd'),'https://earthquake.usgs.gov/earthquakes/eventpage/us2000abcd');
});

test('both record layers pass the MapLibre style validator, filters included',async()=>{
 const {validateStyleMin}=await import('@maplibre/maplibre-gl-style-spec');
 const added=[];
 const map={getSource:()=>undefined,addSource(){},getLayer:()=>undefined,addLayer:spec=>added.push(spec),getStyle:()=>({layers:[]}),setFilter:(id,filter)=>{const layer=added.find(l=>l.id===id);if(filter)layer.filter=filter;}};
 quakes.syncEarthquakeRecord(map,{endYear:2026,events:[]},2015,'us2000abcd');
 const style={version:8,sources:{[quakes.EARTHQUAKE_RECORD_SOURCE_ID]:{type:'geojson',data:{type:'FeatureCollection',features:[]}}},layers:added};
 assert.deepEqual(validateStyleMin(JSON.parse(JSON.stringify(style))).map(e=>e.message),[]);
 const ring=added.find(l=>l.id===quakes.EARTHQUAKE_RECORD_SELECTED_LAYER_ID).paint['circle-radius'];
 assert.deepEqual(ring.slice(0,3),['interpolate',['linear'],['zoom']],'zoom stays the top-level input');
 assert.deepEqual(ring[4].slice(3),[2.5,5.7,4,8,5,10.5],'the ring sits 3.5 px outside the event');
});

test('the Landform relief dock offers the record, with the histogram, a year, and the selected event',async()=>{
 const geology=maps.categoryMap('geology');
 assert.ok(geology.tools.includes('quakes'));
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const calls=[];
 const counts=[{year:2014,count:3,color:'#7e03a8'},{year:2015,count:9,color:'#cc4778'},{year:2016,count:0,color:'#f89540'}];
 const base={look:geology,mode:'terrain',depth:2.5,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
  onQuakes:v=>calls.push(['on',v]),onQuakeYear:v=>calls.push(['year',v]),onQuakeClear:()=>calls.push(['clear'])};
 const state={on:false,loading:false,failed:false,counts:null,total:0,startYear:1973,endYear:2026,minMagnitude:2.5,truncated:false,year:null,selected:null,selectedUrl:null};
 let tree=h.render(h.exports.CategoryMapDock,{...base,quakes:state});
 findNode(tree,n=>n.type==='button'&&n.props.children==='Earthquake record since 1973').props.onClick();
 tree=h.render(h.exports.CategoryMapDock,{...base,quakes:{...state,on:true,loading:true}});
 assert.match(JSON.stringify(tree),/Reading the USGS earthquake catalog/);
 tree=h.render(h.exports.CategoryMapDock,{...base,quakes:{...state,on:true,counts,total:12}});
 assert.match(JSON.stringify(tree),/12 earthquakes M2\.5\+ inside Kansas, 1973–2026 · most in 2015 \(9\)/);
 const histogram=findNode(tree,n=>typeof n.type==='function'&&n.props.counts===counts);
 assert.ok(histogram,'the histogram gets the counts with their colours');
 const select=findNode(tree,n=>n.type==='select');
 assert.deepEqual(select.props.children[1].map(o=>o.props.value),[2014,2015],'only years with events are offered');
 select.props.onChange({target:{value:'2015'}});
 tree=h.render(h.exports.CategoryMapDock,{...base,quakes:{...state,on:true,counts,total:12,year:2015,
  selected:{id:'us2000abcd',time:'2015-03-01T10:00:00.000Z',year:2015,magnitude:3.4,magnitudeType:'mb_lg',depthKilometers:5,place:'8 km SW of Anthony, Kansas',status:'reviewed',longitude:-98.1,latitude:37.1},selectedUrl:'https://earthquake.usgs.gov/earthquakes/eventpage/us2000abcd'}});
 const text=JSON.stringify(tree);
 assert.match(text,/9 earthquakes M2\.5\+ in 2015/);
 assert.match(text,/"M ","3\.4"," mb_lg".*"2015-03-01 10:00"," UTC".*"8 km SW of Anthony, Kansas"," · depth 5 km"," · reviewed"/);
 assert.equal(findNode(tree,n=>n.type==='a').props.href,'https://earthquake.usgs.gov/earthquakes/eventpage/us2000abcd');
 findNode(tree,n=>n.type==='button'&&n.props.children==='Clear').props.onClick();
 findNode(tree,n=>n.type==='button'&&n.props.children==='Back to the past 30 days').props.onClick();
 assert.deepEqual(calls,[['on',true],['year',2015],['clear'],['on',false]]);
 assert.match(h.exports.quakeReading({...state,failed:true}),/did not answer/);
 assert.match(h.exports.quakeReading({...state,counts,total:12,truncated:true}),/cut short/);
 h.dispose?.();
});

test('the page hides the 30-day catalog while the record is shown, and the record leaves with its map',()=>{
 assert.match(page,/quakeLiveWasOnRef\.current = Boolean\(officialVisibilityRef\.current\["usgs-earthquakes"\]\);\s*if \(quakeLiveWasOnRef\.current\) setOfficialContextVisible\("usgs-earthquakes", false\);/);
 assert.match(page,/else if \(quakeLiveWasOnRef\.current\) \{\s*quakeLiveWasOnRef\.current = false;\s*setOfficialContextVisible\("usgs-earthquakes", true\);/);
 assert.match(page,/quakeLiveWasOnRef\.current = false;\s*setQuakeRecordOn\(false\);[\s\S]{0,240}\/\/ Each map opens on its own subject/);
 assert.match(page,/if \(quakeRecordOn\) params\.set\("quakes", "record"\);/);
 assert.match(page,/renderedHits\[0\]\?\.source === EARTHQUAKE_RECORD_SOURCE_ID\) \{\s*const id = renderedHits\[0\]\.properties\?\.id;/,'a click selects the event, not the basemap beneath it');
 assert.match(page,/fetch\("\/api\/earthquake-record", \{ signal: controller\.signal \}\)/);
 assert.match(page,/map\.on\("styledata", restore\);/,'a new style gets the record back');
 assert.match(page,/params\.get\("quakes"\) === "record" && restoredTopic !== "all" && Boolean\(categoryMap\(restoredTopic\)\?\.tools\?\.includes\("quakes"\)\)/,'a shared record view opens only on a map that offers it');
 assert.match(route,/body \? JSON\.parse\(body\) as unknown : \{ features: \[\] \}/,'an empty FDSN answer (204) is an empty record');
});
