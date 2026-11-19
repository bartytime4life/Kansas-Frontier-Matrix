import test from 'node:test';
import assert from 'node:assert/strict';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';
const {recoveredCollection}=await import(await modelUrl('app/recovered-collections.ts'));
const {collectionMetadata}=await import(await modelUrl('app/collection-metadata.ts'));
const {recordedReference}=await import(await modelUrl('app/collection-field-dictionary.ts'));
const {profileCollection,measurementLayer,storyBrief}=await import(await modelUrl('app/collection-lab.ts'));
const {createLabBundle,openLabBundle}=await import(await modelUrl('app/data-lab/lab-bundle.ts'));
const {collectionRelationships}=await import(await modelUrl('app/collection-relationships.ts'));
const {GET}=await import(await modelUrl('app/api/collection-metadata/route.ts'));
const sites=recoveredCollection('observations-usgs-sites'),series=recoveredCollection('observations-usgs-series');
const row=(id,values={})=>({id,values:{file_id:1,row_number:Number(id),monitoring_location_id:'USGS-001',site_type_code:'ST',
 drainage_area:'0',altitude:'0',altitude_accuracy:'0.1',vertical_datum:'NGVD29',...values},provenance:{source_id:'synthetic-context-qa'}});
const sample=rows=>({rows,pages:1,hasMore:true,answers:[{generatedAt:'2026-11-18T12:00:00Z'}]});

test('50 station and series fields have documented aliases, units and identities',()=>{
 assert.equal(sites.columns.length+series.columns.length,50);
 for(const c of [sites,series]){
  const m=collectionMetadata(c),ids=new Set(m.documentation.map(d=>d.id));
  for(const f of m.fields){assert.ok(f.definition,f.name);assert.ok(f.sources.length);assert.ok(f.sources.every(id=>ids.has(id)));}
  assert.deepEqual(m.recordIdentity,['file_id','row_number']);assert.equal(m.provenance.reviewCredit,null);assert.equal(m.temporal.edition,null);
 }
 const site=collectionMetadata(sites),s=collectionMetadata(series);
 assert.equal(site.fields.find(f=>f.name==='altitude').unit,'ft');
 assert.equal(site.fields.find(f=>f.name==='altitude').referenceField,'vertical_datum');
 assert.equal(site.fields.find(f=>f.name==='drainage_area').unit,'mi²');
 assert.equal(site.fields.find(f=>f.name==='site_no').sourceField,'monitoring_location_number');
 assert.equal(s.fields.find(f=>f.name==='time_series_id').sourceField,'id');
 assert.equal(s.fields.find(f=>f.name==='period_begin').sourceField,'begin');
 assert.equal(s.fields.find(f=>f.name==='primary_flag').sourceField,'primary');
});

test('altitudes keep datum and accuracy context while unknown references stay unknown',()=>{
 const rows=[row('1'),row('2',{altitude:'2'}),row('3',{altitude:'100',vertical_datum:'NAVD88'}),
  row('4',{altitude:'100',altitude_accuracy:'2'}),row('5',{vertical_datum:null})];
 const p=profileCollection(sites,sample(rows)),altitude=p.fields.find(f=>f.name==='altitude');
 assert.equal(altitude.groups.length,4);assert.equal(altitude.groups[0].mean,1);assert.equal(altitude.groups[0].min,0);
 assert.equal(JSON.parse(altitude.groups[0].context).reference,'NGVD29');
 assert.equal(JSON.parse(altitude.groups.at(-1).context).reference,'Not supplied');
 assert.deepEqual(p.fields.find(f=>f.name==='altitude_accuracy').groups,[]);
 assert.equal(recordedReference(sites.id,'altitude',Object.create({vertical_datum:'NAVD88'})),null);
 assert.equal(recordedReference(sites.id,'well_constructed_depth',{}),'Land surface');
});

test('station quality, identifiers, timezone flags and dates never become numeric measurements',()=>{
 const p=profileCollection(sites,sample([row('1',{horizontal_positional_accuracy:'1',uses_daylight_savings:'1',
  hydrologic_unit_code:'001',time_zone_abbreviation:'2',construction_date:'1970',aquifer_type_code:'3'})]));
 for(const name of ['altitude_accuracy','horizontal_positional_accuracy','uses_daylight_savings','hydrologic_unit_code','time_zone_abbreviation','construction_date','aquifer_type_code'])
  assert.deepEqual(p.fields.find(f=>f.name===name).groups,[],name);
});

test('series flags, limits and period boundaries describe metadata rather than observations',()=>{
 const p=profileCollection(series,sample([row('1',{time_series_id:'s',data_type:'42',primary_flag:'1',thresholds:'10',
  period_begin:'1900',period_end:'2026',last_modified:'2026',parameter_name:'2',parameter_description:'3'})]));
 assert.ok(p.fields.every(f=>f.groups.length===0));
 const brief=storyBrief(series,sample([row('1',{time_series_id:'s',data_type:'Daily values'})]),'QA question');
 assert.match(brief,/boundaries do not prove continuous coverage/);assert.match(brief,/not observations/);
 assert.match(brief,/Station and series context/);assert.match(brief,/comparison plans, not joined records/);
});

test('provider identity summaries retain repeated captures, missing identities and leading zeros',()=>{
 const rows=[row('1'),row('2',{file_id:2}),row('3',{monitoring_location_id:'USGS-1'}),row('4',{monitoring_location_id:null})];
 const before=JSON.stringify(rows),p=profileCollection(sites,sample(rows));
 assert.equal(p.providerIdentity.distinct,2);assert.equal(p.providerIdentity.repeatedIdentifiers,1);
 assert.equal(p.providerIdentity.additionalRows,1);assert.equal(p.providerIdentity.missing,1);assert.equal(p.sample.rows,4);
 assert.equal(JSON.stringify(rows),before);
 const s=profileCollection(series,sample([row('1',{time_series_id:'same',data_type:'Daily values'}),row('2',{time_series_id:'same',data_type:'Peaks'})]));
 assert.equal(s.providerIdentity.distinct,2);assert.equal(s.providerIdentity.additionalRows,0);
});

test('12 comparison plans use existing provider fields and preserve the field-series namespace boundary',()=>{
 let count=0;
 for(const name of ['daily-values','field-measurements','peaks','sites','series']){
  const c=recoveredCollection('observations-usgs-'+name);
  for(const r of collectionMetadata(c).relationships){
   count++;const target=recoveredCollection(r.targetCollection);assert.ok(target);
   for(const key of r.keys){assert.ok(c.columns.includes(key.source));assert.ok(target.columns.includes(key.target));}
   assert.equal(r.joinStatus,'not_executed');assert.equal(r.cardinality,'unverified_across_captures');
   assert.ok(r.checks.some(v=>v.includes('Archived captures')));assert.equal(r.documentation.sha256.length,64);
  }
 }
 assert.equal(count,12);
 assert.deepEqual(collectionMetadata(recoveredCollection('observations-usgs-field-measurements')).relationships.map(r=>r.targetCollection),[sites.id]);
 assert.deepEqual(collectionRelationships('__proto__'),[]);
});

test('geometry derivatives carry the actual station datum without conversion when geometry exists',()=>{
 const c={...sites,geometry:'geometry_geojson'},s=sample([row('1',{vertical_datum:'NAVD88',geometry_geojson:'{"type":"Point","coordinates":[-98,38]}'})]);
 const before=JSON.stringify(s.rows),context=profileCollection(c,s).fields.find(f=>f.name==='altitude').groups[0].context;
 const layer=measurementLayer(c,s,'altitude',context);
 assert.equal(layer.features[0].properties.unit,'ft');assert.equal(layer.features[0].properties.reference,'NAVD88');
 assert.ok(layer.kfm.contextDefinitions.some(f=>f.name==='vertical_datum'));
 assert.equal(JSON.stringify(s.rows),before);assert.equal(layer.kfm.reviewCredit,null);
});

test('older station and series selections preserve source rows with an explicit context notice',()=>{
 const s=sample([row('1')]);
 for(const [c,field] of [[sites,'drainage_area'],[series,'thresholds']]){
  const old=JSON.parse(createLabBundle(c,s,'Original question',null));delete old.fieldDictionaryRevision;
  old.view={field,context:'Unit and measurement context not supplied',range:null};
  const saved=openLabBundle(JSON.stringify(old));assert.deepEqual(saved.snapshot.rows,s.rows);
  assert.equal(saved.question,'Original question');assert.equal(saved.view,null);assert.match(saved.notice,/records and question were preserved/);
  old.view.field='file_id';assert.throws(()=>openLabBundle(JSON.stringify(old)),/does not match/);
 }
 const next=createLabBundle(sites,s,'Question',null);assert.deepEqual(openLabBundle(next).view,JSON.parse(next).view);
 const forged=JSON.parse(next);forged.view.context='Unit and measurement context not supplied';
 assert.throws(()=>openLabBundle(JSON.stringify(forged)),/does not match/);
});

test('metadata API exports comparison plans without adding an executable join interface',async()=>{
 const response=GET(new Request('https://example.org/api/collection-metadata?collection='+sites.id));
 const body=await response.json();assert.equal(body.collections[0].relationships.length,4);
 assert.deepEqual(body.collections[0].providerIdentity.fields,['monitoring_location_id']);
 assert.equal(GET(new Request('https://example.org/api/collection-metadata?collection='+sites.id+'&join=series')).status,400);
});
