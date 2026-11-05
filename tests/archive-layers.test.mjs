import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {DATASETS} from '../scripts/local-data/datasets.mjs';
import {TIGER_LAYERS} from '../scripts/local-data/tiger.mjs';

async function compile(path,modules={}) {
 const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,id=>{if(id in modules)return modules[id];throw Error(id);});return exports;
}
const recovered=await compile('app/recovered-collections.ts',{'../scripts/local-data/recovered-catalog.json':{default:JSON.parse(await readFile('scripts/local-data/recovered-catalog.json','utf8'))},'./recovered-topics.mjs':await import('../app/recovered-topics.mjs')});
const catalog=await compile('app/archive-layer-catalog.ts',{'./recovered-collections':recovered});
const data=await compile('app/archive-layer-data.ts',{'./bounded-json':await compile('app/bounded-json.ts')});
const get=id=>catalog.archiveLayer('archive-'+id);
const polygon={type:'Polygon',coordinates:[[[-99,38],[-98,38],[-98,39],[-99,38]]]};
const answer=(dataset,rows,extra={})=>({format:'kfm-local-data-v1',dataset,total:rows.length,count:rows.length,rows,source:{provider:'Fixture',coverage:'Synthetic test only',notes:'Not observations'},generatedAt:'2026-11-03T12:00:00Z',...extra});

test('every existing public dataset and TIGER layer has an explicit map use or accuracy hold',()=>{
 assert.deepEqual(Object.keys(catalog.ARCHIVE_DATASET_USES).sort(),[...DATASETS.keys()].sort());
 assert.deepEqual(catalog.ARCHIVE_LAYERS.filter(l=>l.kind==='tiger').map(l=>l.reference),TIGER_LAYERS);
 assert.equal(new Set(catalog.ARCHIVE_LAYERS.map(l=>l.id)).size,catalog.ARCHIVE_LAYERS.length);
 assert.match(catalog.ARCHIVE_DATASET_USES['nwm-streamflow'],/hold.*v3.1.*v3.0/);
 assert.equal(catalog.ARCHIVE_LAYERS.some(l=>l.dataset==='nwm-streamflow'),false);
 assert.deepEqual(catalog.normalizeArchiveSelection(['bad','archive-wind','archive-wind']),['archive-wind']);
});
test('all layer queries conform to the gateway allowlist and its bounded geographic contract',()=>{
 for(const layer of catalog.ARCHIVE_LAYERS){const q=data.archiveQuery(layer,data.archiveArea([-98.5,38.5]),'2026-09','ppt');assert.doesNotThrow(()=>DATASETS.get(layer.dataset).parse(q),layer.id);}
 assert.throws(()=>data.archiveArea([0,0]));assert.throws(()=>data.archiveQuery(get('prism'),'','2026-13','ppt'));
});
test('invalid positions and malformed geometries are withheld, including nulls and unclosed rings',()=>{
 for(const geometry of [null,{type:'Point',coordinates:[null,38]},{type:'Point',coordinates:['-98',38]},{type:'Point',coordinates:[190,38]},{type:'Point',coordinates:[-98,NaN]},{type:'LineString',coordinates:[[-98,38]]},{type:'Polygon',coordinates:[[[-99,38],[-98,38],[-98,39],[-97,38]]]}]) assert.equal(data.validArchiveGeometry(geometry),null);
 assert.deepEqual(data.validArchiveGeometry({type:'Point',coordinates:[-98,38,5]}),{type:'Point',coordinates:[-98,38]});
 assert.deepEqual(data.validArchiveGeometry(polygon),polygon);
});
test('storm begin points are not converted into invented tracks or county centres',()=>{
 const rows=[{eventId:1,type:'Tornado',location:{begin:{lat:38,lon:-98},end:{lat:39,lon:-97}}},{eventId:2,type:'Hail',area:{name:'Example'},location:{begin:{lat:null,lon:null}}},{eventId:1,type:'Tornado',location:{begin:{lat:38,lon:-98}}}];
 const result=data.archiveFeatures(get('storms'),rows);
 assert.equal(result.collection.features.length,1);assert.equal(result.collection.features[0].geometry.type,'Point');assert.equal(result.unlocated,1);assert.equal(result.duplicate,1);
 assert.equal(rows.length,3,'unlocated source records remain available');
});
test('alerts without provider polygons stay unlocated and station nulls never become zero coordinates',()=>{
 assert.equal(data.archiveFeatures(get('alerts'),[{id:'a',geometry:null,properties:{areaDesc:'Kansas'}}]).unlocated,1);
 assert.equal(data.archiveFeatures(get('ghcn'),[{id:'x',lat:null,lon:null}]).collection.features.length,0);
 assert.equal(data.archiveFeatures(get('ghcn'),[{id:'placeholder',lat:0,lon:0}]).unlocated,1);
 assert.equal(data.archiveFeatures(get('water'),[{site:'USGS-07144100',geometry:{type:'Point',coordinates:[0,0]}}]).unlocated,1);
});
test('PRISM uses exact county identities and distinguishes zero, missing cells and absent geometry',()=>{
 const rows=[{county:{geoid:'20001'},mean:0,validCells:5,unit:'mm',period:'2026-09'},{county:{geoid:'20003'},mean:null,validCells:0,unit:'mm',period:'2026-09'},{county:{geoid:'20005'},mean:9,validCells:5}];
 const result=data.archiveFeatures(get('prism'),rows,new Map([['20001',polygon],['20003',polygon]]));
 assert.deepEqual(result.collection.features.map(f=>f.properties.value),[0,null]);assert.equal(result.missingValues,1);assert.equal(result.unlocated,1);
 assert.equal(result.collection.features[0].properties.period,'2026-09');
});
test('drilldowns use exact station identifiers and keep local-standard-time ASOS separate',()=>{
 for(const [layer,row] of [[get('ghcn'),{id:'USW00003928'}],[get('wind'),{id:'ICT'}],[get('water'),{site:'USGS-07144100'}]])
  for(const detail of data.archiveDetails(layer,row,'2020-01-01','2020-01-31'))assert.doesNotThrow(()=>DATASETS.get(detail.dataset).parse(detail.query));
 assert.equal(data.archiveDetails(get('wind'),{id:'ICT'},'2020-01-01','2020-01-31').at(-1).query.station,'KICT');
 assert.equal(data.archiveDetails(get('wind'),{id:'13K'},'2020-01-01','2020-01-31').some(d=>d.dataset==='asos-5min'),false);
 assert.equal(data.archiveDetails(get('reaches'),{featureId:1},'2020-01-01','2020-01-31').length,0,'unverified NWM cross-version join is withheld');
});
test('bounded reads retain stale metadata and reject unexpected datasets and malformed counts',async()=>{
 const controller=new AbortController();
 const rows=[{id:'x',lat:38,lon:-98}];
 const response=await data.fetchArchive('ghcn-stations',{},controller.signal,async()=>Response.json(answer('ghcn-stations',rows,{cache:{state:'stale',at:'2026-11-01T00:00:00Z'}})));
 assert.equal(response.cache.state,'stale');
 for(const value of [answer('wrong',rows),answer('ghcn-stations',rows,{count:5}),answer('ghcn-stations',rows,{total:0})])await assert.rejects(data.fetchArchive('ghcn-stations',{},controller.signal,async()=>Response.json(value)));
 await assert.rejects(data.fetchArchive('ghcn-stations',{},controller.signal,async()=>Response.json({reasonCode:'LOCAL_DATA_UNAVAILABLE'},{status:503})),/unavailable/);
});
test('spatial replies retain a boolean count-cap flag and reject missing or malformed qualifications',async()=>{
 const rows=[{id:'[1,1]',values:{name:'Fixture'}}],query={collection:'observations-faa-obstacles',bbox:'-99,38,-98,39',limit:'50'};
 for(const totalCapped of [true,false]){
  const result=await data.fetchArchive('near-observations',query,new AbortController().signal,async()=>Response.json(answer('near-observations',rows,{total:10000,totalCapped,collection:query.collection})));
  assert.equal(result.totalCapped,totalCapped);
 }
 for(const totalCapped of [undefined,null,'false',0])await assert.rejects(data.fetchArchive('near-observations',query,new AbortController().signal,async()=>Response.json(answer('near-observations',rows,{total:10000,totalCapped,collection:query.collection}))),/Incomplete archive response/);
});
test('oversized geometry responses reduce page size without dropping the original filter or offset',async()=>{
 const requests=[];
 const result=await data.fetchArchive('tiger-features',{layer:'county',geometry:'1',limit:'20',offset:'40'},new AbortController().signal,async url=>{
  const q=new URL(url,'http://localhost').searchParams;requests.push(Object.fromEntries(q));
  return Number(q.get('limit'))>5?Response.json({reasonCode:'REPLY_TOO_LARGE'},{status:413}):Response.json(answer('tiger-features',[{id:'20001',geometry:polygon}]));
 });
 assert.deepEqual(requests.map(q=>q.limit),['20','10','5']);assert.ok(requests.every(q=>q.offset==='40'&&q.layer==='county'));assert.equal(result.count,1);
});
test('county joins page by actual returned counts and reject non-Kansas IDs',async()=>{
 const offsets=[];const shapes=await data.countyShapes(new AbortController().signal,async url=>{
  const offset=Number(new URL(url,'http://localhost').searchParams.get('offset'));offsets.push(offset);
  const rows=offset===0?[{id:'20001',geometry:polygon},{id:'31001',geometry:polygon}]:[{id:'20003',geometry:polygon}];
  return Response.json(answer('tiger-features',rows,{total:3}));
 });
 assert.deepEqual(offsets,[0,2]);assert.deepEqual([...shapes.keys()],['20001','20003']);
});
test('aborted reads never dispatch another request',async()=>{
 const controller=new AbortController();controller.abort();let calls=0;
 await assert.rejects(data.fetchArchive('wind-stations',{},controller.signal,async()=>{calls++;return Response.json({});}));assert.equal(calls,0);
});

const views=await compile('app/archive-layer-view.ts',{'./archive-layer-catalog':catalog});
test('shared archive queries preserve applied dates and redact a location-derived search area',()=>{
 const value={month:'2026-09',variable:'ppt',from:'2020-01-01',to:'2020-01-31',area:'-99,38,-98,39'};
 const saved={'archive-ghcn':value,'archive-prism':{...value,area:''},bad:value};
 const selected=['archive-ghcn','archive-prism','bad'];
 const normal=views.parseArchiveViews(views.serializeArchiveViews(selected,saved,false));
 assert.deepEqual(normal,{'archive-ghcn':value,'archive-prism':{...value,area:''}});
 const redacted=views.parseArchiveViews(views.serializeArchiveViews(selected,saved,true));
 assert.equal(redacted['archive-ghcn'].area,'');assert.equal(redacted['archive-ghcn'].from,'2020-01-01');
 for(const bad of ['{','[]',JSON.stringify({'archive-ghcn':['2026-13','ppt','2020-01-01','2020-01-02','']}),JSON.stringify({'archive-ghcn':['2026-09','ppt','2020-02-30','2020-03-02','']}),JSON.stringify({'archive-ghcn':['2026-09','ppt','2020-01-01','2020-01-02','0,0,100,100']})])assert.deepEqual(views.parseArchiveViews(bad),{});
});

import {componentHarness,findNode,settle} from './component-harness.mjs';
const pause=()=>new Promise(resolve=>setTimeout(resolve,5));
const nodeText=node=>Array.isArray(node)?node.map(nodeText).join(''):node&&typeof node==='object'?nodeText(node.props?.children):String(node??'');
async function rowHarness(fetchArchive){
 const sources=new Map(),layers=new Map(),events=new Map(),saves=[];
 const map={getStyle:()=>({layers:[...layers.values()]}),queryRenderedFeatures:()=>[],getCenter:()=>({lng:-98.5,lat:38.5}),getSource:id=>sources.get(id),getLayer:id=>layers.get(id),addSource:(id,v)=>sources.set(id,v),addLayer:v=>layers.set(v.id,v),removeLayer:id=>layers.delete(id),removeSource:id=>sources.delete(id),on:(e,id,fn)=>events.set(e+id,fn),off:(e,id)=>events.delete(e+id),once:(e,fn)=>fn(),triggerRepaint:()=>{}};
 const harness=await componentHarness('app/archive-layer-control.tsx',{'./archive-layer-catalog':catalog,'./archive-layer-data':{...data,fetchArchive},'./archive-layer-view':views,'./archive-layer-control.module.css':{default:{}}},{},'\nexports.TestRow=ArchiveLayerRow;');
 const props={layer:get('ghcn'),mapRef:{current:map},styleReady:false,selected:['archive-ghcn'],shown:new Set(['archive-ghcn']),onChange:()=>{},onInspect:()=>{},pickingEnabled:()=>true,views:{},onView:(id,view)=>saves.push([id,view])};
 const render=()=>{const node=harness.render(harness.exports.TestRow,props);harness.commit();return node;};
 return {harness,props,render,sources,layers,events,saves,map};
}
test('a restored archive selection waits for the map and removes all geometry on deselection',async()=>{
 const calls=[];const h=await rowHarness(async(_id,q)=>{calls.push(q);return answer('ghcn-stations',[{id:'USW00003928',lat:38,lon:-98,name:'Fixture'}]);});
 h.render();await pause();assert.equal(calls.length,0);
 h.props.styleReady=true;h.render();await pause();await settle();h.render();h.render();
 assert.equal(calls.length,1);assert.equal(h.sources.size,1);assert.equal(h.layers.size,3);
 h.props.styleReady=false;h.render();assert.equal(h.sources.size,0);
 h.props.styleReady=true;h.render();await pause();h.render();assert.equal(calls.length,1,'style changes redraw without querying again');assert.equal(h.layers.size,3);
 h.props.selected=[];h.render();assert.equal(h.sources.size,0);assert.equal(h.layers.size,0);await pause();h.render();h.harness.dispose();assert.equal(h.events.size,0);
});
test('late archive replies cannot recreate layers after deselection',async()=>{
 let resolve,signal;const h=await rowHarness((_id,_q,s)=>{signal=s;return new Promise(r=>resolve=r);});
 h.props.styleReady=true;h.render();await pause();assert.ok(signal);
 h.props.selected=[];h.render();await pause();assert.equal(signal.aborted,true);
 resolve(answer('ghcn-stations',[{id:'USW00003928',lat:38,lon:-98}]));await settle();const tree=h.render();
 assert.equal(h.sources.size,0);assert.equal(h.saves.length,0);assert.ok(findNode(tree,n=>n.type==='small'&&n.props.children==='Not selected'));h.harness.dispose();
});
test('recovered map layers ask for the map area, page by offset and keep displayed records when the next read fails',async()=>{
 const collection='observations-faa-obstacles',id='archive-records-'+collection,calls=[];
 const row=n=>({id:JSON.stringify([1,n]),values:{geometry_geojson:JSON.stringify({type:'Point',coordinates:[-98,38]})}});
 const h=await rowHarness(async(_id,q)=>{calls.push(q);if(calls.length===3)throw Error('Temporary outage');const rows=[row(calls.length)];return answer('near-observations',rows,{total:3,collection});});
 h.props.layer=catalog.archiveLayer(id);h.props.selected=[id];h.props.shown=new Set([id]);h.props.styleReady=true;
 h.render();await pause();await settle();h.render();let tree=h.render();
 assert.equal(catalog.archiveLayer(id).dataset,'near-observations');
 assert.equal(calls[0].collection,collection);assert.match(calls[0].bbox,/^-?\d+\.\d{5},-?\d+\.\d{5},-?\d+\.\d{5},-?\d+\.\d{5}$/);assert.equal(calls[0].limit,'50');assert.equal(calls[0].after,undefined);
 await findNode(tree,n=>n.type==='button'&&n.props.children==='Load next page').props.onClick();await settle();h.render();tree=h.render();
 assert.equal(calls[1].offset,'1');assert.equal(calls[1].bbox,calls[0].bbox);assert.equal(calls[1].after,undefined);
 assert.equal(h.sources.get('kfm-'+id).data.features.length,2);
 await findNode(tree,n=>n.type==='button'&&n.props.children==='Load next page').props.onClick();await settle();h.render();h.render();
 assert.equal(calls[2].offset,'2');assert.equal(h.sources.get('kfm-'+id).data.features.length,2);h.harness.dispose();
});
test('capped archive totals display as lower bounds across pages and retained failures; exact and unknown totals remain distinct',async()=>{
 const collection='observations-faa-obstacles',id='archive-records-'+collection;
 for(const [total,totalCapped,label] of [[10000,true,'10,000+'],[10000,false,'10,000'],[null,undefined,null]]){
  let calls=0;
  const h=await rowHarness(async()=>{
   calls++;if(calls===3)throw Error('Temporary outage');
   return answer('near-observations',[{id:`[1,${calls}]`,values:{geometry_geojson:JSON.stringify({type:'Point',coordinates:[-98,38]})}}],{total,totalCapped,hasMore:true,collection});
  });
  try{
   h.props.layer=catalog.archiveLayer(id);h.props.selected=[id];h.props.shown=new Set([id]);h.props.styleReady=true;
   h.render();await pause();await settle();h.render();let tree=h.render();
   const expected=n=>label?`${n} of ${label} matching records loaded`:`${n} records loaded; this is a page of the archive`;
   assert.ok(nodeText(tree).includes(expected(1)),nodeText(tree));
   await findNode(tree,n=>n.type==='button'&&n.props.children==='Load next page').props.onClick();await settle();h.render();tree=h.render();
   assert.ok(nodeText(tree).includes(expected(2)));
   await findNode(tree,n=>n.type==='button'&&n.props.children==='Load next page').props.onClick();await settle();h.render();tree=h.render();
   assert.ok(nodeText(tree).includes(expected(2)),'failed next page retains the qualified count');
  }finally{h.harness.dispose();}
 }
});
test('shared area and climate controls restore before the first acquisition',async()=>{
 const calls=[];const h=await rowHarness(async(_id,q)=>{calls.push(q);return answer('ghcn-stations',[]);});
 h.props.views={'archive-ghcn':{month:'2026-09',variable:'ppt',from:'2020-01-01',to:'2020-01-31',area:'-100,38,-99,39'}};
 h.props.styleReady=true;h.render();await pause();await settle();const tree=h.render();
 assert.equal(calls[0].bbox,'-100,38,-99,39');assert.equal(findNode(tree,n=>n.type==='input'&&n.props.type==='date').props.value,'2020-01-01');assert.equal(h.saves[0][1].area,'-100,38,-99,39');h.harness.dispose();
});

test('multiple archive layers share two relay slots and cancelled queued reads never dispatch',async()=>{
 const pending=[],calls=[];
 const fetcher=(url)=>{calls.push(url);return new Promise(resolve=>pending.push(()=>resolve(Response.json(answer('wind-stations',[])))));};
 const first=data.fetchArchive('wind-stations',{},new AbortController().signal,fetcher);
 const second=data.fetchArchive('wind-stations',{},new AbortController().signal,fetcher);
 const cancel=new AbortController();const third=data.fetchArchive('wind-stations',{},cancel.signal,fetcher);const rejected=assert.rejects(third);
 await settle();assert.equal(calls.length,2);cancel.abort();await rejected;
 const fourth=data.fetchArchive('wind-stations',{},new AbortController().signal,fetcher);await settle();assert.equal(calls.length,2);
 pending.shift()();await first;await settle();assert.equal(calls.length,3);
 pending.shift()();pending.shift()();await Promise.all([second,fourth]);
});

test('only the topmost archive feature owns inspection, leaving other selected layers accessible',async()=>{
 const h=await rowHarness(async()=>answer('ghcn-stations',[{id:'USW00003928',lat:38,lon:-98}]));
 const inspected=[];h.props.onInspect=id=>inspected.push(id);h.props.styleReady=true;h.render();await pause();await settle();h.render();h.render();
 const id='kfm-archive-ghcn-point',feature={source:'kfm-archive-ghcn',layer:{id},properties:{key:'USW00003928'}},event={point:{x:0,y:0},features:[feature]};
 h.map.queryRenderedFeatures=()=>[{source:'other-visible-layer',layer:{id:'other'}},feature];h.events.get('click'+id)(event);assert.equal(inspected.length,0);
 h.map.queryRenderedFeatures=()=>[feature];h.events.get('click'+id)(event);assert.deepEqual(inspected,['archive-ghcn']);h.harness.dispose();
});
