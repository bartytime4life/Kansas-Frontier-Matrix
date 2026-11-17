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
 assert.equal(catalog.RECOVERED_COLLECTIONS.length,189);
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
 const all=await api.GET(new Request('https://example.org/api/collection-metadata')).json();assert.equal(all.collections.length,189);assert.ok(all.researchPacks.length);
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
