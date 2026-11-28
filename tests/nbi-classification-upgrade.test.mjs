import assert from 'node:assert/strict';
import test from 'node:test';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';

const {recoveredCollection}=await import(await modelUrl('app/recovered-collections.ts'));
const {fieldDictionaryRevision}=await import(await modelUrl('app/collection-field-dictionary.ts'));
const {profileCollection,measurementContexts,measurementDistribution}=await import(await modelUrl('app/collection-lab.ts'));
const {createLabBundle,openLabBundle}=await import(await modelUrl('app/data-lab/lab-bundle.ts'));
const {previousNbiView}=await import(await modelUrl('app/data-lab/previous-nbi-view.ts'));
const collection=recoveredCollection('bulk-nbi-bridges');
const v1='nbi-legacy-2026-11-27-v1',v2='nbi-legacy-2026-11-27-v2';
const absent='Unit and measurement context not supplied';
const question='Keep my archived classification investigation and its original records.';
// The reviewed ad506 v1 field inventory, independent of current dictionary roles.
const demoted=[
 'route_prefix_005b','service_level_005c','route_number_005d','direction_005e','highway_district_002',
 'features_desc_006a','critical_facility_006b','facility_carried_007','location_009','base_hwy_network_012',
 'lrs_inv_route_013a','subroute_no_013b','toll_020','maintenance_021','owner_022','functional_class_026',
 'structure_flared_035','railings_036a','transitions_036b','appr_rail_036c','history_037','navigation_038',
 'open_closed_posted_041','service_on_042a','service_und_042b','structure_kind_043a','structure_type_043b',
 'appr_kind_044a','appr_type_044b','vert_clr_und_ref_054a','work_proposed_075a','work_done_by_075b',
 'othr_state_struc_no_099','strahnet_highway_100','parallel_structure_101','traffic_direction_102',
 'temp_structure_103','highway_system_104','federal_lands_105','deck_structure_type_107','surface_type_108a',
 'membrane_type_108b','deck_protection_108c','national_network_110','pier_protection_111','bridge_len_ind_112',
 'scour_critical_113','fed_agency','submitted_by',
];
const preDictionary=[
 'record_type_005a','design_load_031','deck_cond_058','superstructure_cond_059','substructure_cond_060',
 'channel_cond_061','culvert_cond_062','opr_rating_meth_063','inv_rating_meth_065','bridge_condition',
 'lowest_rating','structural_eval_067','undclrence_eval_069','posting_eval_070','waterway_eval_071',
 'appr_road_eval_072','fracture_092a','undwater_look_see_092b','spec_inspect_092c',
];
const priorNonValues=[
 'place_code_004','year_adt_030','median_code_033','appr_rail_end_036d','lat_und_ref_055a',
 'year_of_imp_097','other_state_code_098a','year_of_future_adt_115',
];
const row=(id,values)=>({id:String(id),values:{file_id:51,row_number:id,nbi_year:1992,state_code_001:'20',
 structure_number_008:'000000000000001',...values},provenance:{source_id:'synthetic-NBI-classification-QA',
 source_url:'https://example.org/synthetic-nbi-classification',sha256:'c'.repeat(64),review_credit:null}});
const snapshot=rows=>({rows,pages:1,hasMore:true,answers:[{generatedAt:'2026-11-27T12:00:00Z',
 cache:{state:'stale',at:'2026-11-20T00:00:00Z'},source:{provider:'Synthetic NBI QA'}}]});
const view=(field,range=null,context=absent)=>({field,context,range});
function bundle(source,selection,revision){
 const data=JSON.parse(createLabBundle(collection,source,question,selection));
 if(revision===undefined)delete data.fieldDictionaryRevision;else data.fieldDictionaryRevision=revision;
 data.profile={fields:[{name:selection.field,role:'value',groups:[{context:selection.context}]}],credit:{aiReview:'forged'}};
 return data;
}
const open=data=>openLabBundle(JSON.stringify(data));
function assertReset(source,selection,revision){
 const before=JSON.stringify(source);
 assert.equal(previousNbiView(collection,source,selection,revision),true);
 const saved=open(bundle(source,selection,revision));
 assert.equal(saved.view,null);assert.match(saved.notice,/Legacy NBI field definitions have changed/);
 assert.deepEqual(saved.snapshot.rows,source.rows);assert.deepEqual(saved.snapshot.answers,source.answers);
 assert.equal(saved.snapshot.pages,source.pages);assert.equal(saved.snapshot.hasMore,source.hasMore);
 assert.equal(saved.question,question);assert.equal(JSON.stringify(source),before);
 const profile=profileCollection(collection,saved.snapshot);
 assert.equal(profile.credit.aiReview,null);assert.equal(profile.credit.approval,null);
}

test('all 49 newly demoted fields preserve exact null-revision and explicit-v1 investigations',()=>{
 assert.equal(new Set(demoted).size,49);assert.equal(fieldDictionaryRevision(collection.id),v2);
 for(const field of demoted){
  const source=snapshot([row(1,{[field]:'1'}),row(2,{[field]:'9'})]);
  assert.deepEqual(measurementContexts(collection,source,field),[],field);
  for(const revision of [undefined,null,v1])for(const range of [null,
   {lower:1,upper:5,includeUpper:false},{lower:5,upper:9,includeUpper:true}]){
   assertReset(source,view(field,range),revision);
  }
 }
});

test('explicit v1 cannot authorize views of any of the 19 already nonmeasurement fields',()=>{
 assert.equal(new Set(preDictionary).size,19);
 for(const field of preDictionary){
  const source=snapshot([row(1,{[field]:'2'})]),selection=view(field,{lower:2,upper:2,includeUpper:true});
  for(const revision of [undefined,null])assertReset(source,selection,revision);
  assert.equal(previousNbiView(collection,source,selection,v1),false,field);
  assert.throws(()=>open(bundle(source,selection,v1)),/does not match/,field);
 }
});

test('newly documented prior identity, time and location fields never receive measurement resets',()=>{
 for(const field of [...priorNonValues,'file_id','row_number','nbi_year','deck_geometry_eval_068','main_unit_spans_045','geometry_geojson']){
  const source=snapshot([row(1,{[field]:'2'})]),selection=view(field);
  for(const revision of [undefined,null,v1]){
   assert.equal(previousNbiView(collection,source,selection,revision),false,field);
   assert.throws(()=>open(bundle(source,selection,revision)),/does not match/,field);
  }
 }
});

test('current v2, foreign and malformed revisions cannot authorize a classification reset',()=>{
 const source=snapshot([row(1,{structure_kind_043a:'2'})]),selection=view('structure_kind_043a');
 for(const revision of [v2,'nbi-legacy-2026-11-27-v3','nbi-2026-11-27-v1','',0,false,{},[]]){
  assert.equal(previousNbiView(collection,source,selection,revision),false);
  assert.throws(()=>open(bundle(source,selection,revision)),/does not match/);
 }
 for(const id of ['observations-usgs-sites','observations-faa-obstacles']){
  assert.equal(previousNbiView(recoveredCollection(id),source,selection,v1),false);
 }
});

test('invented contexts and plausible altered bins cannot use either classification migration path',()=>{
 const field='structure_kind_043a',source=snapshot([row(1,{[field]:'1'}),row(2,{[field]:'9'})]);
 for(const revision of [undefined,null,v1]){
  for(const range of [undefined,{},[],{lower:1,upper:5,includeUpper:true},{lower:1,upper:9,includeUpper:true},
   {lower:5,upper:1,includeUpper:false},{lower:1,upper:5,includeUpper:'false'},
   {lower:NaN,upper:5,includeUpper:false},{lower:1,upper:Infinity,includeUpper:false}]){
   const selection=view(field,range);if(range===undefined)delete selection.range;
   assert.equal(previousNbiView(collection,source,selection,revision),false);
   assert.throws(()=>open(bundle(source,selection,revision)),/does not match|range is invalid/);
  }
  const selection=view(field,null,'{"new_context":"forged"}');
  assert.equal(previousNbiView(collection,source,selection,revision),false);
  assert.throws(()=>open(bundle(source,selection,revision)),/does not match/);
 }
});

test('v1 context reconstruction retains original dimension order, text and all 250 contexts',()=>{
 const field='scour_critical_113';
 const source=snapshot(Array.from({length:250},(_,index)=>row(index+1,{[field]:String(index),
  nbi_year:1992+index,unit:' code ',qualifier:`qualifier-${index}`,quality_flag:0})));
 const context='{"unit":" code ","qualifier":"qualifier-249","quality_flag":"0"}';
 const selection=view(field,{lower:249,upper:249,includeUpper:true},context);
 for(const revision of [undefined,null,v1]){
  assertReset(source,selection,revision);
  assert.equal(previousNbiView(collection,source,{...selection,context:'{"qualifier":"qualifier-249","unit":" code ","quality_flag":"0"}'},revision),false);
  assert.equal(previousNbiView(collection,{...source,rows:[...source.rows,row(251,{[field]:'250'})]},selection,revision),false);
 }
 const pooled=snapshot([row(1,{[field]:'1',nbi_year:1992}),row(2,{[field]:'9',nbi_year:2025})]);
 assertReset(pooled,view(field,{lower:1,upper:5,includeUpper:false}),v1);
});

test('missing, censored, leading-zero and unsafe numbers cannot establish old measurement eligibility',()=>{
 for(const value of [null,'','Not supplied','N','U','T','<2','02',true,{longField:true,preview:'2'},
  '9007199254740992',Number.MAX_SAFE_INTEGER+1]){
  const source=snapshot([row(1,{scour_critical_113:value})]),selection=view('scour_critical_113');
  for(const revision of [undefined,null,v1]){
   assert.equal(previousNbiView(collection,source,selection,revision),false);
   assert.throws(()=>open(bundle(source,selection,revision)),/does not match/);
  }
 }
});

test('compatible physical measurement views and original encoded records remain unchanged',()=>{
 const source=snapshot([row(1,{structure_len_mt_049:'20',structure_kind_043a:'01',scour_critical_113:'U',year_of_imp_097:'1994'}),
  row(2,{structure_len_mt_049:'40',structure_kind_043a:'00',scour_critical_113:'7',year_of_imp_097:'0000'})]);
 const context=measurementContexts(collection,source,'structure_len_mt_049')[0].context;
 const {lower,upper,includeUpper}=measurementDistribution(collection,source,'structure_len_mt_049',context).bins[0];
 const selection=view('structure_len_mt_049',{lower,upper,includeUpper},context);
 for(const revision of [undefined,null,v1,v2]){
  assert.equal(previousNbiView(collection,source,selection,revision),false);
  const saved=open(bundle(source,selection,revision));
  assert.deepEqual(saved.view,selection);assert.equal(saved.notice,null);
  assert.deepEqual(saved.snapshot.rows,source.rows);assert.deepEqual(saved.snapshot.answers,source.answers);
 }
});
