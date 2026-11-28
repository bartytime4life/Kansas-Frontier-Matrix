import test from 'node:test';
import assert from 'node:assert/strict';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';

const {recoveredCollection}=await import(await modelUrl('app/recovered-collections.ts'));
const {collectionMetadata,fieldRole}=await import(await modelUrl('app/collection-metadata.ts'));
const {documentedField,documentedCode,recordedUnit}=await import(await modelUrl('app/collection-field-dictionary.ts'));
const {profileCollection,measurementContexts,measurementDistribution,measurementLayer,storyBrief}=await import(await modelUrl('app/collection-lab.ts'));
const {createLabBundle,openLabBundle}=await import(await modelUrl('app/data-lab/lab-bundle.ts'));
const {GET}=await import(await modelUrl('app/api/collection-metadata/route.ts'));
const collection=recoveredCollection('bulk-nbi-bridges');
const roles={
 category:`route_prefix_005b service_level_005c direction_005e features_desc_006a critical_facility_006b facility_carried_007 location_009 base_hwy_network_012 toll_020 maintenance_021 owner_022 functional_class_026 median_code_033 structure_flared_035 history_037 navigation_038 open_closed_posted_041 service_on_042a service_und_042b structure_kind_043a structure_type_043b appr_kind_044a appr_type_044b vert_clr_und_ref_054a lat_und_ref_055a work_proposed_075a work_done_by_075b strahnet_highway_100 parallel_structure_101 traffic_direction_102 highway_system_104 federal_lands_105 deck_structure_type_107 surface_type_108a membrane_type_108b deck_protection_108c national_network_110 bridge_len_ind_112 fed_agency`.split(' '),
 identity:`route_number_005d highway_district_002 place_code_004 lrs_inv_route_013a subroute_no_013b other_state_code_098a othr_state_struc_no_099 submitted_by`.split(' '),
 time:`year_adt_030 year_of_imp_097 year_of_future_adt_115`.split(' '),
 quality:`railings_036a transitions_036b appr_rail_036c appr_rail_end_036d temp_structure_103 pier_protection_111 scour_critical_113`.split(' '),
};
const names=Object.values(roles).flat();
const row=(id,values={})=>({id:String(id),values:{file_id:1,row_number:id,nbi_year:2025,state_code_001:'20',
 structure_number_008:'000000000000001',...Object.fromEntries(names.map(name=>[name,'2'])),
 structure_len_mt_049:'20',operating_rating_064:'10',inventory_rating_066:'8',inspect_freq_months_091:'24',
 geometry_geojson:'{"type":"Point","coordinates":[-98,38]}',...values},
 provenance:{source_id:'synthetic-nbi-classification-QA',source_url:'https://example.org/synthetic-nbi',sha256:'a'.repeat(64)}});
const sample=rows=>({rows,pages:1,hasMore:true,answers:[{generatedAt:'2026-11-28T04:00:00Z',cache:{state:'stale',at:'2026-11-27T04:00:00Z'}}]});

test('89 retained fields have source-backed definitions, including all57 new classifications',()=>{
 const metadata=collectionMetadata(collection),documents=new Set(metadata.documentation.map(source=>source.id));
 assert.equal(names.length,57);assert.equal(new Set(names).size,57);
 assert.equal(metadata.fields.length,147);assert.equal(metadata.fields.filter(field=>field.definition).length,89);
 assert.equal(metadata.fieldDictionaryRevision,'nbi-legacy-2026-11-27-v2');
 for(const [role,fields] of Object.entries(roles))for(const name of fields){
  const field=metadata.fields.find(field=>field.name===name);
  assert.ok(field,name);assert.equal(field.role,role,name);assert.equal(field.roleBasis,'documented');
  assert.ok(field.definition);assert.ok(field.sources.length&&field.sources.every(id=>documents.has(id)),name);
  assert.equal(field.unit,null,name+' remains nonphysical metadata');
 }
 assert.equal(metadata.temporal.edition,null);assert.equal(metadata.provenance.reviewCredit,null);
 assert.deepEqual(metadata.recordIdentity,['file_id','row_number']);
 assert.ok(metadata.unknowns.some(value=>value.includes('Undocumented field definitions')));
 assert.equal(documentedField(collection.id,'operating_rating_064'),undefined);
 assert.equal(documentedField(collection.id,'cat23'),undefined,'historical summary alias is not silently assigned a current meaning');
});

test('classification, descriptive text and identifiers cannot produce numeric statistics, ranges or layers',()=>{
 const s=sample([row(1),row(2,Object.fromEntries(names.map(name=>[name,'8'])))]),before=JSON.stringify(s);
 const profile=profileCollection(collection,s);
 for(const name of names){
  assert.deepEqual(profile.fields.find(field=>field.name===name).groups,[],name);
  assert.deepEqual(measurementContexts(collection,s,name),[],name);
  assert.deepEqual(measurementDistribution(collection,s,name,'Unit and measurement context not supplied'),{count:0,bins:[]},name);
 }
 for(const name of ['structure_kind_043a','structure_type_043b','owner_022','route_number_005d','scour_critical_113'])
  assert.throws(()=>measurementLayer(collection,s,name,'Unit and measurement context not supplied'),/measurement field/);
 for(const [name,mean] of [['structure_len_mt_049',20],['operating_rating_064',10],['inventory_rating_066',8],['inspect_freq_months_091',24]])
  assert.equal(profile.fields.find(field=>field.name===name).groups[0].mean,mean,name+' is outside this classification change');
 assert.equal(recordedUnit(collection.id,'operating_rating_064',s.rows[0].values),null);
 assert.equal(JSON.stringify(s),before);
});

test('code dictionaries retain item-specific applicability instead of inventing a critical-facility or material interpretation',()=>{
 assert.match(documentedField(collection.id,'critical_facility_006b').definition,/blank|no longer coded|deprecated/i);
 assert.equal(documentedCode(collection.id,'critical_facility_006b','1'),null);
 assert.equal(documentedCode(collection.id,'structure_type_043b','20'),null,'mixed type20 is for approaches only');
 assert.match(documentedCode(collection.id,'appr_type_044b','20'),/mixed/i);
 assert.match(documentedField(collection.id,'appr_kind_044a').definition+' '+documentedField(collection.id,'appr_kind_044a').encoding,/000/);
 assert.match(documentedField(collection.id,'appr_type_044b').definition+' '+documentedField(collection.id,'appr_type_044b').encoding,/000/);
 assert.equal(documentedCode(collection.id,'structure_kind_043a','0'),'Other');
 assert.equal(documentedCode(collection.id,'structure_type_043b','00'),'Other');
 assert.match(documentedCode(collection.id,'appr_kind_044a','0'),/paired.*000.*not applicable/i);
 assert.match(documentedCode(collection.id,'appr_type_044b','00'),/paired.*000.*not applicable/i);
 for(const field of ['fed_agency','submitted_by'])assert.match(documentedField(collection.id,field).definition,/Download-only/);
 for(const field of ['structure_type_043b','appr_type_044b','owner_022','submitted_by'])
  for(const code of ['__proto__','constructor','unlisted-code'])assert.equal(documentedCode(collection.id,field,code),null);
 assert.equal(fieldRole('appr_rail_end_036d',[],collection.id),'quality');
 assert.equal(fieldRole('appr_rail_end_036d',[],'observations-other'),'time');
 assert.equal(fieldRole('lat_und_ref_055a',[],collection.id),'category');
 assert.equal(fieldRole('lat_und_ref_055a',[],'observations-other'),'location');
 assert.equal(fieldRole('median_code_033',[],collection.id),'category');
});

test('unknown codes, padded identifiers, deprecated values, partial clocks and source credits roundtrip unchanged',()=>{
 const s=sample([row(1,{route_number_005d:'00751',highway_district_002:'001',place_code_004:'00000',
  lrs_inv_route_013a:'0001A',subroute_no_013b:'00',other_state_code_098a:'000',othr_state_struc_no_099:'000000000000001',
  submitted_by:'0020',critical_facility_006b:'1',scour_critical_113:'U',structure_type_043b:'04',appr_kind_044a:'0',appr_type_044b:'00',
  open_closed_posted_041:'unknown',railings_036a:'N',appr_rail_end_036d:null,year_adt_030:'0000',year_of_imp_097:'1992',year_of_future_adt_115:'2045'}),
 row(2,{features_desc_006a:'2026',facility_carried_007:'17',location_009:'0000',owner_022:'  ',scour_critical_113:'T'})]);
 const before=JSON.stringify(s),bundle=JSON.parse(createLabBundle(collection,s,'Preserve my archived classifications',null));
 const opened=openLabBundle(JSON.stringify(bundle));
 assert.deepEqual(opened.snapshot.rows,s.rows);assert.deepEqual(opened.snapshot.answers,s.answers);
 assert.equal(opened.question,'Preserve my archived classifications');assert.equal(opened.notice,null);
 assert.equal(bundle.profile.credit.aiReview,null);assert.equal(bundle.profile.credit.approval,null);
 assert.equal(bundle.fieldDictionaryRevision,'nbi-legacy-2026-11-27-v2');
 assert.equal(JSON.stringify(s),before);
});

test('metadata and story exports carry89 definitions without asserting current bridge operation or recomputing source codes',async()=>{
 const response=GET(new Request('https://example.org/api/collection-metadata?collection=bulk-nbi-bridges')),body=await response.json();
 assert.equal(response.status,200);assert.equal(body.collections[0].fields.filter(field=>field.definition).length,89);
 const brief=storyBrief(collection,sample([row(1)]),'Which recorded categories need edition checks?');
 assert.match(brief,/No AI review or approval/);assert.match(brief,/legacy|Legacy/);
 for(const name of ['structure_kind_043a','owner_022','scour_critical_113'])assert.equal(new RegExp('^- '+name+' \\(', 'm').test(brief),false);
 assert.equal(GET(new Request('https://example.org/api/collection-metadata?collection=bulk-nbi-bridges&sql=anything')).status,400);
});
