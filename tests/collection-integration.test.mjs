import test from 'node:test';
import assert from 'node:assert/strict';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';
const catalog=await import(await modelUrl('app/recovered-collections.ts'));
const metadata=await import(await modelUrl('app/collection-metadata.ts'));
const lab=await import(await modelUrl('app/collection-lab.ts'));
const api=await import(await modelUrl('app/api/collection-metadata/route.ts'));
const browser=await import(await modelUrl('app/data-library/collection-browser.ts'));
const collection={id:'observations-fixture',title:'Fixture',database:'observations',table:'fixture',keys:['file_id','row_number'],geometry:'geometry_geojson',columns:['file_id','row_number','value','unit','variable','date','quality_flag','geometry_geojson','notes']};
const row=(id,value,unit='m',extra={})=>({id,values:{file_id:1,row_number:Number(id),value,unit,variable:'stage',date:'1994-01-01',quality_flag:0,geometry_geojson:'{"type":"Point","coordinates":[-97,38]}',...extra},provenance:{source_id:'fixture',source_url:'https://example.org/source',sha256:'a'.repeat(64)}});
const answer=(rows,patch={})=>({format:'kfm-local-data-v1',dataset:'recovered-observations',collection:collection.id,count:rows.length,total:null,rows,hasMore:false,nextCursor:null,generatedAt:'2026-11-17T12:00:00Z',source:{provider:'Fixture',notes:'Original units',coverage:'Fixture'},...patch});
const snapshot=(rows,patch={})=>({rows,answers:[answer(rows,patch)],pages:1,hasMore:false});

test('every collection has rich metadata, valid record/lab links and honest unknowns',()=>{
 assert.equal(catalog.RECOVERED_COLLECTIONS.length,183);
 for(const c of catalog.RECOVERED_COLLECTIONS){
  const m=metadata.collectionMetadata(c);assert.equal(m.id,c.id);assert.ok(m.description.length>80);assert.ok(m.topics.length);assert.equal(m.fields.length,c.columns.length);
  assert.equal(m.temporal.observationPeriod,null);assert.equal(m.spatial.crs,null);assert.equal(m.provenance.reviewCredit,null);
  assert.equal(new URL(m.access.records,'https://example.org').searchParams.get('collection'),c.id);
  assert.equal(!!m.access.map,!!c.geometry);assert.ok(metadata.collectionPacks(c.id).length,`No research connection for ${c.id}`);
  for(const r of metadata.relatedCollections(c)){assert.notEqual(r.collection.id,c.id);assert.ok(catalog.recoveredCollection(r.collection.id));assert.ok(r.reason);}
 }
});
test('research map bundles and missed domain connections use actual collections',()=>{
 for(const pack of metadata.RESEARCH_PACKS){const c=metadata.packCollections(pack.id);assert.ok(c.length);assert.equal(new Set(c.map(x=>x.id)).size,c.length);}
 assert.ok(catalog.recoveredTopics('observations-nid-dams').includes('water'));
 assert.ok(catalog.recoveredTopics('observations-usgs-earthquakes').includes('disaster'));
 assert.ok(catalog.recoveredTopics('observations-nps-boundaries').includes('ecology'));
 assert.ok(catalog.recoveredTopics('observations-usfs-ceded-lands').includes('people'));
 for(const field of ['parameter_cd','station_number','variable','element','oas_number','obstacle_number','structure_number_008'])assert.equal(metadata.fieldRole(field),'identity');
});
test('topic discovery extends the existing multi-word browser filters without losing geometry filtering',()=>{
 const collections=catalog.RECOVERED_COLLECTIONS.map(c=>({...c,topics:catalog.recoveredTopics(c.id)}));
 const result=browser.matchingCollections(collections,'water engineering',true);
 assert.ok(result.some(c=>c.id==='observations-nid-dams'));
 assert.ok(result.every(c=>c.geometry));
 assert.equal(browser.matchingCollections(collections,'no-such-field-or-topic-at-all',true).length,0);
});
test('zero and missing values remain distinct, units and variables never get pooled',()=>{
 const s=snapshot([row('1',0),row('2','4'),row('3',null),row('4',10,'ft'),row('5',100,'m',{variable:'depth'}),row('6','<0.2')]);
 const p=lab.profileCollection(collection,s),v=p.fields.find(f=>f.name==='value');
 assert.equal(v.present,5);assert.equal(v.missing,1);assert.equal(v.numericCount,4);assert.equal(v.groups.length,3);
 assert.equal(v.groups[0].count,2);assert.equal(v.groups[0].mean,2);assert.equal(v.groups[0].min,0);
 for(const f of p.fields.filter(f=>['file_id','row_number','date','quality_flag'].includes(f.name)))assert.equal(f.groups.length,0);
 assert.equal(p.provenance[0].sha256,'a'.repeat(64));assert.equal(p.sample.retrievedAt[0],'2026-11-17T12:00:00Z');
 assert.deepEqual(p.collection.provenance.sourceUrls,['https://example.org/source']);assert.deepEqual(p.spatial.sampleBoundingBox,[-97,38,-97,38]);
});
test('measurement distribution assigns each eligible record once with exact interval boundaries',()=>{
 const values=[0,1,2,3,'4',5,6,7,9];
 const rows=values.map((value,index)=>row(String(index),value));
 rows[0].provenance={source_id:'provider',source_url:'https://user:pass@example.org/source'};
 const sample=snapshot([
  ...rows,
  row('other-unit',4,'ft'),
  row('other-variable',4,'m',{variable:'depth'}),
  row('other-quality',4,'m',{quality_flag:'provisional'}),
  row('censored','<0.2'),
  row('missing',null),
  row('unsafe',Number.MAX_VALUE),
 ]);
 const profile=lab.profileCollection(collection,sample).fields.find(field=>field.name==='value');
 const result=lab.measurementDistribution(collection,sample,'value',profile.groups[0].context);
 assert.equal(result.count,profile.groups[0].count);
 assert.deepEqual(result.bins.map(({lower,upper,includeUpper,count})=>[lower,upper,includeUpper,count]),[
  [0,3,false,3],[3,6,false,3],[6,9,true,3],
 ]);
 assert.deepEqual(result.bins.flatMap(bin=>bin.records.map(({id,value})=>[id,value])),
  values.map((value,index)=>[String(index),Number(value)]));
 assert.deepEqual(result.bins[0].records[0],{id:'0',value:0,sourceId:'provider',sourceUrl:null});
 assert.equal(result.bins[0].records[1].sourceUrl,'https://example.org/source');
});
test('measurement distribution handles empty, constant and closely spaced values',()=>{
 const unlocated={...collection,geometry:null};
 const profileAndDistribute=values=>{
  const sample=snapshot(values.map((value,index)=>row(String(index),value)));
  const group=lab.profileCollection(unlocated,sample).fields.find(field=>field.name==='value').groups[0];
  const distribution=lab.measurementDistribution(unlocated,sample,'value',group.context);
  assert.deepEqual(lab.measurementDistribution(unlocated,sample,'file_id',group.context),{count:0,bins:[]});
  assert.deepEqual(lab.measurementDistribution(unlocated,sample,'value','unknown context'),{count:0,bins:[]});
  return distribution;
 };
 const constant=profileAndDistribute([0,0]);
 assert.deepEqual(constant.bins.map(({lower,upper,includeUpper,count})=>[lower,upper,includeUpper,count]),[[0,0,true,2]]);
 const tiny=profileAndDistribute([Number.MIN_VALUE,2*Number.MIN_VALUE,Number.MIN_VALUE,2*Number.MIN_VALUE]);
 assert.deepEqual(tiny.bins.map(({lower,upper,count})=>[lower,upper,count]),[[Number.MIN_VALUE,2*Number.MIN_VALUE,4]]);
 const span=profileAndDistribute([-Number.MAX_SAFE_INTEGER,-1,0,Number.MAX_SAFE_INTEGER]);
 assert.deepEqual(span.bins.map(({lower,upper,count})=>[lower,upper,count]),[
  [-Number.MAX_SAFE_INTEGER,0,2],[0,Number.MAX_SAFE_INTEGER,2],
 ]);
 const full=profileAndDistribute(Array.from({length:250},(_,index)=>index));
 assert.equal(full.bins.length,6);
 assert.equal(full.bins.reduce((total,bin)=>total+bin.count,0),250);
 assert.equal(new Set(full.bins.flatMap(bin=>bin.records.map(record=>record.id))).size,250);
});
test('USGS daily values separate parameter, statistic, unit and approval in profiles and layers',()=>{
 const daily=catalog.recoveredCollection('observations-usgs-daily-values');
 const dimensions={parameter_code:'00060',statistic_id:'00003',unit_of_measure:'ft3/s',approval_status:'Approved',qualifier:'Estimated'};
 const alternatives={parameter_code:'00065',statistic_id:'00001',unit_of_measure:'m3/s',approval_status:'Provisional',qualifier:'Ice'};
 for(const field of Object.keys(dimensions))assert.ok(daily.columns.includes(field));
 const rows=[row('1',1,'unused',dimensions),...Object.entries(alternatives).map(([field,value],index)=>
  row(String(index+2),index+2,'unused',{...dimensions,[field]:value})
 ),{id:'7',values:{value:7}}];
 const sample=snapshot(rows);
 const groups=lab.profileCollection(daily,sample).fields.find(field=>field.name==='value').groups;
 assert.deepEqual(groups.map(group=>[group.count,group.min]),[[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]);
 assert.deepEqual(JSON.parse(groups[0].context),dimensions);
 assert.equal(groups.at(-1).context,'Unit and measurement context not supplied');

 // Exercise the export with a stored geometry field added to the same schema.
 const mappable={...daily,geometry:'geometry_geojson',columns:[...daily.columns,'geometry_geojson']};
 const layer=lab.measurementLayer(mappable,sample,'value',groups[0].context);
 assert.deepEqual(layer.features.map(feature=>feature.id),['1']);
 assert.deepEqual(layer.kfm.omitted,{otherContext:6,notNumeric:0,noUsableGeometry:0});
});
test('USGS field and peak values and AQS concentrations use their archived context columns',()=>{
 const cases=[
  {id:'observations-usgs-field-measurements',fields:['value'],context:{parameter_code:'00065',unit_of_measure:'ft'},column:'vertical_datum',values:['NAVD88','NGVD29']},
  {id:'observations-usgs-peaks',fields:['value'],context:{parameter_code:'00060',unit_of_measure:'ft3/s'},column:'qualifier',values:['Estimated','Regulated']},
  {id:'observations-aqs-daily',fields:['arithmetic_mean','first_max_value'],context:{parameter_code:'44201',units_of_measure:'Parts per million',sample_duration:'1 HOUR'},column:'pollutant_standard',values:['Ozone 1-hour','Ozone 8-hour']},
 ];
 for(const {id,fields,context,column,values} of cases){
  const source=catalog.recoveredCollection(id);
  for(const field of [...fields,...Object.keys(context),column])assert.ok(source.columns.includes(field));
  const rows=values.map((value,index)=>({id:String(index),values:{
   ...Object.fromEntries(fields.map(field=>[field,index+1])),...context,[column]:value,
  }}));
  const profile=lab.profileCollection(source,snapshot(rows));
  for(const field of fields){
   const groups=profile.fields.find(entry=>entry.name===field).groups;
   assert.deepEqual(groups.map(group=>JSON.parse(group.context)),values.map(value=>({...context,[column]:value})),`${id}: ${field}`);
  }
 }
});
test('AQS counts, percentages and AQI share observation context without concentration units',()=>{
 const aqs=catalog.recoveredCollection('observations-aqs-daily');
 const measurements={observation_count:8,observation_percent:80,aqi:40};
 const original={...measurements,first_max_hour:14,parameter_code:'44201',pollutant_standard:'Ozone 8-hour',units_of_measure:'Parts per million'};
 const rows=[original,{...original,units_of_measure:'Parts per billion'},{...original,pollutant_standard:'Ozone 1-hour'}]
  .map((values,index)=>({id:String(index),values}));
 const profile=lab.profileCollection(aqs,snapshot(rows));
 for(const field of Object.keys(measurements)){
  const groups=profile.fields.find(entry=>entry.name===field).groups;
  assert.deepEqual(groups.map(group=>group.count),[2,1]);
  assert.deepEqual(groups.map(group=>JSON.parse(group.context)),[
   {parameter_code:'44201',pollutant_standard:'Ozone 8-hour'},
   {parameter_code:'44201',pollutant_standard:'Ozone 1-hour'},
  ]);
 }
 const hour=profile.fields.find(entry=>entry.name==='first_max_hour');
 assert.equal(hour.role,'time');
 assert.deepEqual(hour.groups,[]);
 assert.deepEqual(hour.exampleValues,['14']);
});
test('USGS Samples and WQP keep result qualifiers and ancillary measurement units separate',()=>{
 const cases=[
  {
   id:'observations-usgs-samples-results',result:'result_measure',unit:'result_measure_unit',
   qualifier:'result_measure_qualifier_code',subdivision:'activity_media_subdivision',
   depth:'activity_depth_height_measure',depthUnit:'activity_depth_height_measure_unit',
   limit:'detection_limit_measure_a',limitUnit:'detection_limit_measure_unit_a',
  },
  {
   id:'observations-wqp-results',result:'result_measure_value',unit:'result_measure_unit_code',
   qualifier:'measure_qualifier_code',subdivision:'activity_media_subdivision_name',
   depth:'activity_depth_height_value',depthUnit:'activity_depth_height_unit_code',
   limit:'detection_quantitation_limit_value',limitUnit:'detection_quantitation_limit_unit_code',
  },
 ];
 const method='result_analytical_method_identifier',methodContext='result_analytical_method_identifier_context';
 for(const {id,result,unit,qualifier,subdivision,depth,depthUnit,limit,limitUnit} of cases){
  const source=catalog.recoveredCollection(id);
  for(const field of [result,unit,qualifier,subdivision,method,methodContext,depth,depthUnit,limit,limitUnit])assert.ok(source.columns.includes(field));
  const baseline={[unit]:'mg/L',[qualifier]:'Observed',[subdivision]:'Surface water',[method]:'123',[methodContext]:'Example A'};
  const expected=[baseline,{...baseline,[qualifier]:'Estimated'},{...baseline,[subdivision]:'Groundwater'},
   {...baseline,[method]:'456'},{...baseline,[methodContext]:'Example B'}];
  const rows=expected.map((context,index)=>({id:String(index),values:{
   [result]:index+1,...context,[depth]:3,[depthUnit]:'m',[limit]:1,[limitUnit]:'µg/L',
  }}));
  const profile=lab.profileCollection(source,snapshot(rows));
  const groupsFor=field=>profile.fields.find(entry=>entry.name===field).groups;
  assert.deepEqual(groupsFor(result).map(group=>JSON.parse(group.context)),expected.map(context=>({...context,[limit]:'1',[limitUnit]:'µg/L'})));
  assert.equal(groupsFor(depth)[0].count,expected.length);
  assert.deepEqual(JSON.parse(groupsFor(depth)[0].context),{[depthUnit]:'m'});
  assert.equal(groupsFor(limit).length,expected.length);
  assert.deepEqual(groupsFor(limit).map(group=>JSON.parse(group.context)),expected.map(context=>({...context,[limitUnit]:'µg/L'})));
 }
});
test('long fields, stale cache, unknown units and summary group limits stay visible',()=>{
 const rows=Array.from({length:14},(_,i)=>row(String(i),i,`unit-${i}`,{notes:{longField:true,preview:'partial'}}));
 const p=lab.profileCollection(collection,snapshot(rows,{cache:{state:'stale',at:'2026-11-16'}}));
 assert.equal(p.sample.stale,true);assert.equal(p.fields.find(f=>f.name==='notes').longFields,14);
 assert.equal(p.fields.find(f=>f.name==='value').groups.length,12);assert.equal(p.fields.find(f=>f.name==='value').additionalGroups,2);
 const brief=lab.storyBrief(collection,snapshot(rows,{cache:{state:'stale'}}),'What happened?');assert.match(brief,/stale cached/);assert.match(brief,/not observation dates/);assert.match(brief,/No AI review or approval/);
});
test('GeoJSON layers retain exact geometry, one measurement context and omission counts',()=>{
 const rows=[row('1',0),row('2',2,'ft'),row('3',null),row('4',5,'m',{geometry_geojson:'broken'}),row('5',9,'m',{geometry_geojson:'{"type":"Point","coordinates":[0,0]}'})];
 const p=lab.profileCollection(collection,snapshot(rows));const g=lab.measurementLayer(collection,snapshot(rows),'value',p.fields.find(f=>f.name==='value').groups[0].context);
 assert.equal(g.features.length,1);assert.equal(g.features[0].properties.value,0);assert.deepEqual(g.features[0].geometry.coordinates,[-97,38]);
 assert.deepEqual(g.kfm.omitted,{otherContext:1,notNumeric:1,noUsableGeometry:2});assert.equal(g.kfm.reviewCredit,null);
 assert.throws(()=>lab.measurementLayer(collection,snapshot(rows),'file_id','x'));
});
test('lab reads at most five seek pages / 250 rows and preserves remaining-record indication',async()=>{
 let calls=0;const read=async(dataset,q)=>{assert.equal(dataset,'recovered-observations');assert.equal(q.limit,'50');const start=calls++*50;return answer(Array.from({length:50},(_,i)=>row(String(start+i),i)),{hasMore:true,nextCursor:String(calls)});};
 const s=await lab.loadLabSample(collection,new AbortController().signal,read);assert.equal(calls,5);assert.equal(s.rows.length,250);assert.equal(s.hasMore,true);
});
test('cancelled reads, repeated pages and collection mismatches fail without substituting data',async()=>{
 const controller=new AbortController();controller.abort();let called=false;
 await assert.rejects(lab.loadLabSample(collection,controller.signal,async()=>{called=true;}));assert.equal(called,false);
 await assert.rejects(lab.loadLabSample(collection,new AbortController().signal,async()=>answer([row('1',1)],{hasMore:true,nextCursor:'same'})),/Repeated/);
 await assert.rejects(lab.loadLabSample(collection,new AbortController().signal,async()=>answer([],{collection:'wrong'})),/selected collection/);
});
test('metadata API is bounded to the catalog, with no raw store or arbitrary SQL access',async()=>{
 const all=await api.GET(new Request('https://example.org/api/collection-metadata')).json();assert.equal(all.collections.length,183);assert.ok(all.researchPacks.length);
 assert.equal(Object.keys(all.datasetUses).length,22);assert.ok(all.mapLayers.length>=90);assert.match(all.datasetUses['nwm-streamflow'],/hold/);
 const id=catalog.RECOVERED_COLLECTIONS[0].id;
 assert.equal((await api.GET(new Request(`https://example.org/api/collection-metadata?collection=${id}`)).json()).collections.length,1);
 assert.equal(api.GET(new Request('https://example.org/api/collection-metadata?table=kfm_secret')).status,400);
 assert.equal(api.GET(new Request('https://example.org/api/collection-metadata?collection=wrong')).status,404);
 assert.equal(api.GET(new Request(`https://example.org/api/collection-metadata?collection=${id}&collection=${id}`)).status,400);
});
test('layer derivatives label XY geometry, retain original records and separate quality qualifiers',()=>{
 const a=row('1',3,'m',{geometry_geojson:'{"type":"Point","coordinates":[-97,38,200]}',quality_flag:'approved'}),b=row('2',4,'m',{quality_flag:'provisional'});
 const s=snapshot([a,b]),p=lab.profileCollection(collection,s),f=p.fields.find(f=>f.name==='value');assert.equal(f.groups.length,2);
 const layer=lab.measurementLayer(collection,s,'value',f.groups[0].context);
 assert.deepEqual(layer.features[0].geometry.coordinates,[-97,38]);assert.match(layer.kfm.scope,/XY/);
 assert.equal(JSON.parse(a.values.geometry_geojson).coordinates[2],200);assert.equal(layer.kfm.omitted.otherContext,1);
 assert.match(lab.storyBrief(collection,s,'Inspect dates'),/1994-01-01/);
});
