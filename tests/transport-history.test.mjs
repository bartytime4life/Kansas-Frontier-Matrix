import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
import * as THREE from 'three';
import { validateStyleMin } from '@maplibre/maplibre-gl-style-spec';
const compile = async (path, replace = s => s) => `data:text/javascript;base64,${Buffer.from(ts.transpileModule(replace(await readFile(new URL(path, import.meta.url), 'utf8')), {compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText).toString('base64')}`;
const historyUrl = await compile('../app/transport-history.ts');
const h = await import(historyUrl);
const modelsUrl = await compile('../app/transport-crew-models.ts', s => s.replace('"three"', JSON.stringify(import.meta.resolve('three'))));
const models = await import(modelsUrl);
const layer = await import(await compile('../app/transport-construction-layer.ts', s => s.replace('"three"', JSON.stringify(import.meta.resolve('three'))).replace('"./transport-history"', JSON.stringify(historyUrl)).replace('"./transport-crew-models"', JSON.stringify(modelsUrl))));
const example = JSON.parse(await readFile(new URL('../public/transport-construction-study-example.json', import.meta.url), 'utf8'));
const clone = () => structuredClone(example);
const inspect = input => h.inspectTransportStudy(JSON.stringify(input));
const [work] = inspect(example);
const mutate = (fn, pattern) => { const input = clone(); fn(input.routes[0], input); assert.throws(() => inspect(input), pattern); };
test('bounded local studies retain only safe fields and cannot admit source claims', () => {
  const input=clone(); input.routes[0].script='fetch("https://example.invalid/")'; input.routes[0].metadata={private:true};
  const [result]=inspect(input); assert.equal(result.script, undefined); assert.equal(result.metadata, undefined); assert.equal(result.synthetic,true);
  assert.equal(result.progress.length,3); assert.equal(result.positionAccuracyM,1);
  assert.throws(()=>h.inspectTransportStudy('x'.repeat(2_000_001)),/2 MB/);
  mutate((r,i)=>i.routes=Array(13).fill(r),/1–12/);
  mutate(r=>r.coordinates[0]=[-80,38],/inside Kansas/);
  mutate(r=>r.coordinates[1]=r.coordinates[0],/length/);
  mutate(r=>r.progress=undefined,/chainage observations/);
  mutate(r=>r.sourceUrl='javascript:alert(1)',/HTTPS/);
  mutate(r=>r.sourceUrl='https://user:pass@example.invalid',/HTTPS/);
  mutate(r=>r.progress[1].sourceUrl='http://example.invalid',/individually sourced/);
});
test('invalid dates and contradictory progress are rejected instead of producing plausible motion',()=>{
  assert.equal(h.transportDay('2024-02-30'),null); assert.equal(h.transportDay('2024-02-29'),Date.UTC(2024,1,29));
  mutate(r=>r.start='2024-02-30',/ordered actual/);
  mutate(r=>r.end=r.start,/ordered actual/);
  mutate(r=>r.progress[1].chainageM=-1,/monotonic/);
  mutate(r=>r.progress[1].date=r.progress[0].date,/chronological/);
  mutate(r=>r.progress[1].chainageM=10_000,/within/);
  mutate(r=>r.progress[2].chainageM=100,/route length/);
  mutate(r=>r.reopenedAt='2023-01-01',/closure/);
  mutate(r=>r.action='remove',/closure/);
  mutate(r=>r.widthM=Infinity,/width/);
  mutate(r=>r.positionAccuracyM=0,/uncertainty/);
});
test('observations hold through missing days, follow reverse seeking and distinguish closure from completion',()=>{
  const before=h.transportFrame(work,'2023-12-31');assert.equal(before.state,'planned');assert.equal(before.chainageM,0);assert.equal(before.closed,false);
  const gap=h.transportFrame(work,'2024-01-05');assert.equal(gap.state,'working');assert.equal(gap.chainageM,0);assert.equal(gap.basis,'observed');assert.equal(gap.sourceDate,'2024-01-01');assert.equal(gap.closed,true);
  const mid=h.transportFrame(work,'2024-01-06');assert.equal(mid.chainageM,work.progress[1].chainageM);assert.equal(mid.closed,true);
  const done=h.transportFrame(work,'2024-01-11');assert.equal(done.state,'complete');assert.equal(done.closed,false);
  assert.deepEqual(h.transportFrame(work,'2024-01-05'),gap);
  const neverReopened={...work,reopenedAt:undefined};assert.equal(h.transportFrame(neverReopened,'2024-01-12').closed,true);
  const noClosure={...work,closedFrom:undefined,reopenedAt:undefined};assert.equal(h.transportFrame(noClosure,'2024-01-06').closed,false);
});
test('explicit interpolation labels the inferred front and reports interval averages only',()=>{
  const interpolated=h.transportFrame({...work,interpolate:true},'2024-01-03');
  assert.equal(interpolated.basis,'interpolated');assert.ok(Math.abs(interpolated.chainageM-work.progress[1].chainageM*.4)<1e-7);
  assert.equal(interpolated.rateMPerDay,work.progress[1].chainageM/5);
  assert.equal(h.transportFrame({...work,interpolate:true},'2024-01-06').basis,'observed');
});
test('removal requires explicit action and never draws a construction reversal as demolition',()=>{
  const removal={...work,action:'remove',reopenedAt:undefined};
  assert.equal(h.transportFrame(removal,'2024-01-11').state,'removed');
  const features=layer.transportLineData([removal],'2024-01-06').features;
  assert.deepEqual(new Set(features.map(f=>f.properties.state)),new Set(['closed','removed']));
  const built=layer.transportLineData([work],'2024-01-11').features;
  assert.equal(built.length,1);assert.equal(built[0].properties.state,'built');
});
test('physical distances, reverse path slicing and level of detail preserve metre scaling',()=>{
  const length=h.routeLengthM(work.coordinates);assert.ok(length>260&&length<262);
  const middle=h.routePose(work.coordinates,length/2);assert.ok(Math.abs(middle.coordinate[0]+98.4985)<1e-7);assert.ok(Math.abs(middle.heading-Math.PI/2)<1e-7);
  const sliced=h.routeSlice(work.coordinates,length*.25,length*.75);assert.ok(Math.abs(h.routeLengthM(sliced)-length*.5)<.01);
  assert.equal(h.transportDetail(8,38.5,1),'overview');assert.equal(h.transportDetail(16,38.5,1),'equipment');assert.equal(h.transportDetail(19,38.5,1),'crew');assert.equal(h.transportDetail(22,38.5,25),'overview');
});
test('original metre-based road and rail models have finite geometry, no external assets, and release resources',()=>{
  for(const mode of ['road','rail'])for(const year of [1867,1956,2024]){
    const crew=models.createTransportCrew(mode,year,true);const bounds=new THREE.Box3().setFromObject(crew.group);assert.ok(bounds.max.z<7&&bounds.max.z>1.5);assert.ok(bounds.max.y-bounds.min.y<7);
    let geometries=0,disposed=0;crew.group.traverse(o=>{if(o.isMesh){geometries++;o.geometry.addEventListener('dispose',()=>disposed++);assert.ok(Array.from(o.geometry.attributes.position.array).every(Number.isFinite));}});
    for(const time of [0,1,1000])crew.update(time);crew.dispose();assert.equal(disposed,geometries);
  }
});
test('map styles validate and teardown removes every overlay without touching other map layers',()=>{
  const sources=new Map(),layers=new Map(),handlers=new Map();
  const oldDocument=globalThis.document;globalThis.document={hidden:false,addEventListener(){},removeEventListener(){}};
  const map={isStyleLoaded:()=>true,getSource:id=>sources.get(id),addSource(id,s){sources.set(id,{...s,setData(data){this.data=data;}});},getLayer:id=>layers.get(id),addLayer(l){layers.set(l.id,l);},removeLayer(id){layers.delete(id);},removeSource(id){sources.delete(id);},on(n,fn){handlers.set(n,fn);},off(n){handlers.delete(n);},triggerRepaint(){}};
  try{
    const control=layer.attachTransportConstruction(map,[work],'2024-01-06',false);
    const spec={version:8,sources:{'kfm-local-transport-work':{type:'geojson',data:layer.transportLineData([work],'2024-01-06')}},layers:[layers.get('kfm-local-transport-work-line')]};
    assert.deepEqual(validateStyleMin(spec).map(e=>e.message),[]);
    control.update([work],'2024-01-11');assert.equal(sources.get('kfm-local-transport-work').data.features.length,1);
    control.dispose();assert.equal(layers.size,0);assert.equal(sources.size,0);assert.equal(handlers.size,0);
  }finally{globalThis.document=oldDocument;}
});

test('worksite fit rejects tight bends and narrow footprints while retaining a straight route',()=>{
  assert.equal(h.transportWorkSectionFits(work,150),true);
  assert.equal(h.transportWorkSectionFits({...work,widthM:3},150),false);
  assert.equal(h.transportWorkSectionFits(work,20),false);
  const bent={...work,coordinates:[[-98.5,38.5],[-98.499,38.5],[-98.499,38.501]]};
  const corner=h.routeDistanceM(bent.coordinates[0],bent.coordinates[1]);
  assert.equal(h.transportWorkSectionFits(bent,corner+10),false);
});
test('all supplied closure geometry is red even before the first built segment',()=>{
  const data=layer.transportLineData([work],'2024-01-01');
  assert.equal(data.features.length,1);assert.equal(data.features[0].properties.state,'closed');
});
test('failed style installation removes partial resources and keeps pre-existing layers',()=>{
  const oldDocument=globalThis.document;globalThis.document={hidden:false,addEventListener(){},removeEventListener(){}};
  const sources=new Map(),layers=new Map([['original',{id:'original'}]]);
  const map={isStyleLoaded:()=>true,getSource:id=>sources.get(id),addSource(id,s){sources.set(id,s);},getLayer:id=>layers.get(id),addLayer(){throw Error('injected style failure');},removeLayer(id){layers.delete(id);},removeSource(id){sources.delete(id);}};
  try{assert.throws(()=>layer.attachTransportConstruction(map,[work],'2024-01-06',false),/injected/);assert.equal(sources.size,0);assert.deepEqual([...layers.keys()],['original']);}finally{globalThis.document=oldDocument;}
});

const pilot = JSON.parse(await readFile(new URL('../data/work/transport/junction-city-i70-2024.study.json', import.meta.url), 'utf8'));
const [milestoneWork] = inspect(pilot);
test('real milestone reports never create a moving front, completion fraction, closure or average rate', () => {
  for (const day of ['2024-04-28', '2024-04-29', '2024-05-01', '2024-05-02', '2024-08-01', '2024-11-22', '2025-01-01']) {
    const frame = h.transportFrame(milestoneWork, day);
    assert.equal(frame.state, 'unknown'); assert.equal(frame.basis, 'unknown');
    assert.equal(frame.chainageM, 0); assert.equal(frame.rateMPerDay, null); assert.equal(frame.closed, false);
    const features = layer.transportLineData([milestoneWork], day).features;
    assert.equal(features.length, 1); assert.equal(features[0].properties.state, 'context');
    assert.equal(features[0].properties.basis, 'unknown');
    assert.ok(Math.abs(h.routeLengthM(features[0].geometry.coordinates) - h.routeLengthM(milestoneWork.coordinates)) < .01);
  }
  const gap = h.transportFrame(milestoneWork, '2024-08-01');
  assert.equal(gap.sourceDate, '2024-05-02');
  assert.equal(h.transportFrame(milestoneWork, '2024-04-28').sourceDate, null);
  assert.deepEqual(h.transportFrame(milestoneWork, '2024-08-01'), gap);
});
test('milestone mode rejects invented front semantics and unsafe or contradictory reports', () => {
  const reject = (fn, re) => { const v = structuredClone(pilot); fn(v.routes[0]); assert.throws(() => inspect(v), re); };
  for (const field of ['widthM', 'positionAccuracyM', 'closedFrom', 'reopenedAt']) reject(r => r[field] = field.endsWith('M') ? 8 : '2024-05-01', /cannot assert/);
  reject(r => r.progress = [{date:r.start,chainageM:0,sourceUrl:r.sourceUrl}], /cannot assert/);
  reject(r => r.interpolate = true, /cannot assert/);
  reject(r => r.progressMode = 'trust-me', /choose front/);
  reject(r => r.milestones = [], /1–400/);
  reject(r => r.milestones = Array(401).fill(r.milestones[0]), /1–400/);
  reject(r => r.milestones[1].date = r.milestones[0].date, /ordered report/);
  reject(r => r.milestones[0].date = '2024-02-30', /ordered report/);
  reject(r => r.milestones[0].kind = 'observed-front', /ordered report/);
  reject(r => r.milestones[0].title = 'x'.repeat(501), /ordered report/);
  reject(r => r.milestones[0].sourceUrl = 'https://user:pass@example.invalid', /ordered report/);
  reject(r => r.end = r.start, /report-window/);
  const safe=structuredClone(pilot);safe.routes[0].milestones[0].asset='https://example.invalid/script';
  assert.equal(inspect(safe)[0].milestones[0].asset,undefined);
});
test('pilot geometry is reproducible from KDOT vertices and consistent reference-post anchors', async () => {
  const g = JSON.parse(await readFile(new URL('../data/work/transport/junction-city-i70-2024.geometry.json', import.meta.url), 'utf8'));
  assert.equal(g.status, 'CANDIDATE_NOT_ADMITTED'); assert.equal(g.crs, 'EPSG:4326');
  const expected = [g.anchors[0].projectedCoordinate, ...g.routeExcerpt.slice(1,-1).map(p=>p.slice(0,2)), g.anchors[1].projectedCoordinate];
  assert.deepEqual(milestoneWork.coordinates, expected);
  assert.equal(expected.length, 79);
  assert.ok(h.routeLengthM(expected)>6300 && h.routeLengthM(expected)<6600);
  assert.ok(g.routeExcerpt.every((p,i)=>i===0||p[2]>g.routeExcerpt[i-1][2]));
  assert.ok(expected[0][0]<expected.at(-1)[0]); // indexing only, never work direction
  for (const anchor of g.anchors) {
    const i=anchor.excerptSegmentIndex,a=g.routeExcerpt[i],b=g.routeExcerpt[i+1],f=anchor.fraction;
    assert.ok(f>=0&&f<=1);
    assert.deepEqual(anchor.projectedCoordinate,[a[0]+f*(b[0]-a[0]),a[1]+f*(b[1]-a[1])]);
    const marker=g.markers.find(m=>m.attributes.RouteID==='0311000700100000'&&m.attributes.ReferencePost===anchor.referencePost);
    assert.ok(h.routeDistanceM([marker.geometry.x,marker.geometry.y],anchor.projectedCoordinate)<1);
    assert.ok(h.routeDistanceM([marker.attributes.MeasuredLongitude,marker.attributes.MeasuredLatitude],anchor.projectedCoordinate)<15);
  }
  const bad=g.markers.find(m=>m.attributes.OBJECTID===g.excludedMarker.objectId);
  assert.ok(h.routeDistanceM([bad.geometry.x,bad.geometry.y],[bad.attributes.MeasuredLongitude,bad.attributes.MeasuredLatitude])>8000);
  assert.ok(g.anchors.every(a=>a.referencePost!==bad.attributes.ReferencePost||g.markers.some(m=>m.attributes.RouteID==='0311000700100000'&&m.attributes.ReferencePost===a.referencePost)));
});
test('candidate source reports retain date precision and do not enter public assets or source registry', async () => {
  const s=JSON.parse(await readFile(new URL('../data/work/transport/junction-city-i70-2024.sources.json', import.meta.url),'utf8'));
  assert.equal(s.status,'CANDIDATE_NOT_ADMITTED');assert.equal(s.qualification.rawAdmission,'not_performed');
  assert.equal(s.qualification.publicRelease,'not_authorized');
  assert.deepEqual(milestoneWork.milestones.map(m=>m.date),s.reports.map(r=>r.date));
  assert.equal(milestoneWork.milestones.at(-1).kind,'completion-reported');
  assert.match(milestoneWork.milestones.at(-1).title,/Exact completion day is unknown/);
  for(const report of s.reports){assert.match(report.sha256,/^[0-9a-f]{64}$/);assert.ok(milestoneWork.milestones.some(m=>m.sourceUrl===report.url));}
  assert.equal(pilot.routes[0].widthM,undefined);assert.equal(pilot.routes[0].positionAccuracyM,undefined);
  const control=await readFile(new URL('../app/transport-history-control.tsx',import.meta.url),'utf8');
  assert.doesNotMatch(control,/junction-city-i70|data\/work|fetch\(/);
});
