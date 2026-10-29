import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';

async function compile(file, deps = {}) {
  const exports = {};
  new Function('exports', 'require', ts.transpileModule(await readFile(file, 'utf8'), { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText)(exports, name => {
    if (name in deps) return deps[name]; throw new Error(`Unexpected import ${name}`);
  }); return exports;
}
const civic = await compile('app/civic-districts.ts');
const keys = await compile('app/map-keys.ts');
const bounded = await compile('app/bounded-json.ts');
const reader = await compile('app/api/live-context/civic-districts.ts', { '../../bounded-json': bounded, '../../civic-districts': civic });
const now = new Date('2026-10-29T05:00:00Z');
// Synthetic boxes exercise the contract; they are not real district boundaries.
const row = (n, patch = {}) => ({ type: 'Feature', properties: { GEOID: `200${n}`, STATE: '20', CDSESSN: '119', NAME: '<script>unsafe</script>', party: 'NOT_A_SOURCE_FIELD', ...patch }, geometry: { type: 'Polygon', coordinates: [[[-99,38],[-98,38],[-98,39],[-99,39],[-99,38]]] } });
const raw = () => ({ type: 'FeatureCollection', features: [4,2,1,3].map(n => row(n)) });
test('four distinct Kansas districts retain edition and stable IDs, with only allowlisted display properties', () => {
  const result = civic.parseCivicDistricts(raw(), now);
  assert.equal(result.featureCount, 4); assert.equal(result.state, 'ready'); assert.equal(result.upstreamUpdatedAt, null);
  assert.deepEqual(result.data.features.map(f => f.id), ['census-119-2001','census-119-2002','census-119-2003','census-119-2004']);
  assert.equal(result.data.features[0].properties.vintage, '2025-01-01');
  assert.equal(result.retrievedAt, now.toISOString());
  assert.ok(!JSON.stringify(result).includes('<script>')); assert.ok(!JSON.stringify(result).includes('NOT_A_SOURCE_FIELD'));
  assert.match(result.limitation, /not parties or election results/);
  const multi = raw(); multi.features[0].geometry = { type: 'MultiPolygon', coordinates: [multi.features[0].geometry.coordinates] };
  assert.equal(civic.parseCivicDistricts(multi, now).featureCount, 4);
});
test('partial, duplicate, wrong-state, wrong-Congress and malformed district shapes fail closed', () => {
  for (const value of [null, { ...raw(), error: {} }, { ...raw(), exceededTransferLimit: true }, { ...raw(), features: raw().features.slice(1) },
    { ...raw(), features: [row(1),row(1),row(3),row(4)] }, { ...raw(), features: [row(1,{CDSESSN:'120'}),row(2),row(3),row(4)] },
    { ...raw(), features: [row(1,{STATE:'29'}),row(2),row(3),row(4)] }]) assert.throws(() => civic.parseCivicDistricts(value, now));
  for (const geometry of [null, { type:'Point',coordinates:[-99,38] }, { type:'Polygon',coordinates:[] },
    {type:'Polygon',coordinates:[[[-120,38],[-98,38],[-98,39],[-120,38]]]},
    {type:'Polygon',coordinates:[[[-99,38],[-98,38],[-98,39],[-99,39]]]},
    {type:'Polygon',coordinates:[[[-99,38],[-99,38],[-99,38],[-99,38]]]},
    {type:'Polygon',coordinates:[Array.from({length:50_001},()=>[-99,38])]}]) {
    const bad=raw(); bad.features[0].geometry=geometry; assert.throws(()=>civic.parseCivicDistricts(bad,now));
  }
});
test('fixed, bounded source requests coalesce and an expired cache never conceals a failed refresh', async () => {
  let time=now.getTime(), calls=0, fail=false;
  const read=reader.createCivicDistrictReader(async (url,options)=>{
    calls++; const u=new URL(url); assert.equal(u.origin,'https://tigerweb.geo.census.gov');
    assert.equal(u.searchParams.get('where'),"STATE='20'"); assert.match(u.pathname,/Generalized_ACS2025\/Legislative\/MapServer\/5\/query$/);
    assert.equal(u.searchParams.get('resultRecordCount'),'5'); assert.equal(options.redirect,'manual');
    if(fail) throw new Error('internal upstream secret'); return Response.json(raw());
  },()=>time);
  const values=await Promise.all(Array.from({length:25},()=>read())); assert.equal(calls,1); assert.ok(values.every(v=>v===values[0]));
  time+=reader.CIVIC_CACHE_MS-1; assert.equal((await read()).retrievedAt,values[0].retrievedAt); assert.equal(calls,1);
  time++;fail=true;await assert.rejects(read(),/unavailable/);assert.equal(calls,2);
  await assert.rejects(read(),e=>!e.message.includes('secret'));assert.equal(calls,2);
  time+=60_000;fail=false;assert.notEqual((await read()).retrievedAt,values[0].retrievedAt);
});
test('redirects and declared or streamed excessive responses never reach the parser', async () => {
  for(const response of [new Response('',{status:302,headers:{location:'http://127.0.0.1/'}}),new Response('',{status:503}),
    new Response('{}',{headers:{'content-length':String(2*1024*1024+1)}}),new Response(' '.repeat(2*1024*1024+1))]) {
    await assert.rejects(reader.createCivicDistrictReader(async()=>response,()=>now.getTime())(),/unavailable/);
  }
});
test('the route rejects visitor SQL, coordinates, dates and duplicate parameters; successful responses are no-store', async () => {
  let calls=0;
  const route=await compile('app/api/live-context/route.ts',{
    './civic-history':{readCivicHistory:async()=>{throw new Error('No historical fixture');}},'../../civic-history':{civicCongressForDay:day=>day>='1861-01-29'&&day<'2027-01-03'?119:null},'./civic-districts':{readCivicDistricts:async()=>{calls++;return civic.parseCivicDistricts(raw(),now);}}, './deflock':{},
    'cloudflare:workers':{env:{}},'next/server':{NextResponse:Response},'../../bounded-json':bounded,
    '../../event-atlas':{eventDay:v=>/^\d{4}-\d{2}-\d{2}$/.test(v)},'../event-atlas/upstream':{},'../../county-baseline':{},'../../fema-declarations':{},'@mapbox/vector-tile':{},pbf:{},
  });
  const req=q=>({nextUrl:new URL(`https://kfm.invalid/api/live-context?${q}`),signal:new AbortController().signal});
  for(const extra of ['&url=https://evil.invalid','&where=1%3D1','&longitude=-99','&day=1860-01-01','&feed=census-congress-119']) assert.equal((await route.GET(req(`feed=census-congress-119${extra}`))).status,400);
  assert.equal(calls,0);const response=await route.GET(req('feed=census-congress-119'));assert.equal(response.status,200);assert.equal(response.headers.get('cache-control'),'no-store');assert.equal(calls,1);
});
const urls=new Map();
async function moduleUrl(file){
  file=path.resolve(file);if(urls.has(file))return urls.get(file);
  let js=ts.transpileModule(await readFile(file,'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
  for(const m of [...js.matchAll(/from ["'](\.[^"']+)["']/g)])js=js.replace(m[0],`from ${JSON.stringify(await moduleUrl(path.resolve(path.dirname(file),m[1])+'.ts'))}`);
  const url=`data:text/javascript;base64,${Buffer.from(js).toString('base64')}`;urls.set(file,url);return url;
}
const context=await import(await moduleUrl('app/live-context.ts'));
const maps=await compile('app/category-maps.ts'),topics=await compile('app/layer-workspaces.ts');
test('Government starts with real districts only; other topics leave them off, with a disclosed fixed edition',()=>{
  assert.deepEqual(maps.categoryMap('government').starters,[civic.CIVIC_ID]);
  assert.equal(context.defaultOfficialContextVisibility()[civic.CIVIC_ID],false);
  for(const [id,look]of Object.entries(maps.CATEGORY_MAPS))if(id!=='government')assert.ok(!look.starters.includes(civic.CIVIC_ID));
  assert.deepEqual(topics.officialSourceTopics(civic.CIVIC_ID),['government']);
  assert.deepEqual(context.OFFICIAL_CONTEXT_TEMPORAL_SUPPORT[civic.CIVIC_ID].supportedFrames,[context.OFFICIAL_CONTEXT_PRESENT_FRAME]);
  const shown={...context.defaultOfficialContextVisibility(),[civic.CIVIC_ID]:true};
  assert.equal(context.officialContextVisibilityForFrame(shown,context.OFFICIAL_CONTEXT_PRESENT_FRAME)[civic.CIVIC_ID],true);
  assert.equal(context.officialContextVisibilityForFrame(shown,1900)[civic.CIVIC_ID],false);
  assert.equal(context.officialContextVisibilityForFrame(shown,context.OFFICIAL_CONTEXT_PRESENT_FRAME,false)[civic.CIVIC_ID],false);
  assert.deepEqual(keys.MAP_KEYS[civic.CIVIC_ID].items.map(item=>item.color),keys.CIVIC_COLORS.slice(0,4).map(([,color])=>color));
});
test('four keyboard buttons select current records and pass the originating button for focus restoration; hidden/error/held states offer no stale picks',async()=>{
  const h=await componentHarness('app/category-map-dock.tsx',{}),picked=[],toggles=[];
  const base={look:maps.categoryMap('government'),mode:'2d',depth:1,azimuth:315,sun:null,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},
    layerVisibility:{'census-counties':false},onLayer:(...v)=>toggles.push(v),onCivicPick:(...v)=>picked.push(v)};
  const items=civic.parseCivicDistricts(raw(),now).data.features.map(f=>({id:f.id,label:f.properties.name}));
  const state={visible:true,state:'ready',items};
  const tree=h.render(h.exports.CategoryMapDock,{...base,civic:state});
  const buttons=findNode(tree,n=>n.props?.['aria-label']==='Inspect a Kansas U.S. House district').props.children.map(li=>li.props.children);
  assert.equal(buttons.length,4);const target={};buttons[2].props.onClick({currentTarget:target});assert.deepEqual(picked,[[items[2].id,target]]);
  findNode(tree,n=>n.type==='button'&&n.props?.children==='Compare Census counties').props.onClick();assert.deepEqual(toggles,[['census-counties',true]]);
  for(const patch of [{visible:false},{state:'error'},{state:'held'}])assert.ok(!findNode(h.render(h.exports.CategoryMapDock,{...base,civic:{...state,...patch}}),n=>n.props?.['aria-label']==='Inspect a Kansas U.S. House district'));
});
test('district fill, lines and labels restore after style replacement, share the legend palette, hide and clear correctly',async()=>{
  const make=()=>{const sources=new Map(),layers=new Map();return{sources,layers,map:{getSource:id=>sources.get(id),getLayer:id=>layers.get(id),getStyle:()=>({layers:[...layers.values()]}),getProjection:()=>({type:'mercator'}),
    addSource(id,s){sources.set(id,{...s,setData(data){this.data=data;}});},addLayer(l){layers.set(l.id,structuredClone(l));},moveLayer(id){const l=layers.get(id);layers.delete(id);layers.set(id,l);},
    getLayoutProperty:(id,k)=>layers.get(id)?.layout?.[k],getPaintProperty:(id,k)=>layers.get(id)?.paint?.[k],
    setLayoutProperty(id,k,v){const l=layers.get(id);l.layout={...l.layout,[k]:v};},setPaintProperty(id,k,v){const l=layers.get(id);l.paint={...l.paint,[k]:v};}}};};
  const visibility=Object.fromEntries(context.OFFICIAL_CONTEXT_SOURCES.map(s=>[s.id,false])),opacity=context.defaultOfficialContextOpacity(),payload=civic.parseCivicDistricts(raw(),now),first=make();
  context.applyOfficialContextState(first.map,visibility,opacity,{});assert.ok(!first.sources.has(civic.CIVIC_SOURCE.sourceId));
  visibility[civic.CIVIC_ID]=true;opacity[civic.CIVIC_ID]=0.4;const {validateStyleMin}=await import('@maplibre/maplibre-gl-style-spec');
  for(const h of[first,make()]){
    context.applyOfficialContextState(h.map,visibility,opacity,{[civic.CIVIC_ID]:payload});
    const layers=[...h.layers.values()].filter(l=>l.source===civic.CIVIC_SOURCE.sourceId);assert.equal(layers.length,4);
    assert.deepEqual(layers.find(l=>l.type==='fill').paint['fill-color'],keys.civicDistrictColor());
    assert.equal(layers.find(l=>l.type==='fill').paint['fill-opacity'],0.4);
    assert.deepEqual(validateStyleMin({version:8,glyphs:'https://example.invalid/{fontstack}/{range}.pbf',sources:{[civic.CIVIC_SOURCE.sourceId]:{type:'geojson',data:payload.data}},layers}).map(e=>e.message),[]);
    context.applyOfficialContextState(h.map,{...visibility,[civic.CIVIC_ID]:false},opacity,{[civic.CIVIC_ID]:payload});for(const l of layers)assert.equal(h.layers.get(l.id).layout.visibility,'none');
    context.clearOfficialContextFeed(h.map,civic.CIVIC_ID);assert.equal(h.sources.get(civic.CIVIC_SOURCE.sourceId).data.features.length,0);
  }
});
