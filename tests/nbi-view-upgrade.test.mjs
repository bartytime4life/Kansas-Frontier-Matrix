import assert from 'node:assert/strict';
import test from 'node:test';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';

const {recoveredCollection}=await import(await modelUrl('app/recovered-collections.ts'));
const {profileCollection,measurementDistribution}=await import(await modelUrl('app/collection-lab.ts'));
const {createLabBundle,openLabBundle}=await import(await modelUrl('app/data-lab/lab-bundle.ts'));
const {previousNbiView}=await import(await modelUrl('app/data-lab/previous-nbi-view.ts'));
const collection=recoveredCollection('bulk-nbi-bridges');
const absent='Unit and measurement context not supplied';
const question='Preserve my archived bridge investigation.';
const row=(id,values)=>({id:String(id),values:{file_id:91,row_number:id,nbi_year:1992,state_code_001:'20',structure_number_008:'000001',...values},
 provenance:{source_id:'synthetic-NBI-upgrade-QA',source_url:'https://example.org/synthetic-nbi',sha256:'b'.repeat(64),review_credit:null}});
const snapshot=rows=>({rows,pages:1,hasMore:true,answers:[{generatedAt:'2026-11-27T12:00:00Z',cache:{state:'stale',at:'2026-11-20T00:00:00Z'},source:{provider:'Synthetic NBI QA'}}]});
const view=(field,range=null,context=absent)=>({field,context,range});
function bundle(source,selection){
 const data=JSON.parse(createLabBundle(collection,source,question,selection));
 delete data.fieldDictionaryRevision;
 // Imported summaries and credits do not establish old measurement eligibility.
 data.profile={fields:[{name:selection.field,role:'value',groups:[{context:selection.context}]}],credit:{aiReview:'forged'}};
 return data;
}
const open=data=>openLabBundle(JSON.stringify(data));

test('known legacy numeric-code views reset only after exact old bin validation',()=>{
 const source=snapshot([0,1,4,8,9,12].map((value,index)=>row(index+1,{deck_cond_058:String(value)})));
 for(const range of [null,{lower:0,upper:4,includeUpper:false},{lower:4,upper:8,includeUpper:false},{lower:8,upper:12,includeUpper:true}]){
  const selection=view('deck_cond_058',range);
  assert.equal(previousNbiView(collection,source,selection,undefined),true);
  assert.equal(previousNbiView(collection,source,selection,null),true);
  const data=bundle(source,selection),saved=open(data);
  assert.equal(saved.view,null);
  assert.equal(saved.notice,'Legacy NBI field definitions have changed. Your records and question were preserved; condition and classification codes are not measurements.');
  assert.deepEqual(saved.snapshot.rows,source.rows);
  assert.deepEqual(saved.snapshot.answers,source.answers);
  assert.equal(saved.snapshot.hasMore,true);
  assert.equal(saved.question,question);
  const profile=profileCollection(collection,saved.snapshot);
  assert.equal(profile.credit.aiReview,null);
  assert.equal(profile.credit.approval,null);
 }
 const zero=snapshot([row(1,{deck_cond_058:'0'})]);
 assert.equal(previousNbiView(collection,zero,view('deck_cond_058',{lower:0,upper:0,includeUpper:true}),null),true);
});

test('plausible but altered ranges, invented contexts and forged profile eligibility are rejected',()=>{
 const source=snapshot([row(1,{deck_cond_058:'1'}),row(2,{deck_cond_058:'9'})]);
 for(const range of [undefined,{},[],{lower:1,upper:5,includeUpper:true},{lower:1,upper:9,includeUpper:true},
  {lower:5,upper:1,includeUpper:false},{lower:1,upper:5,includeUpper:'false'},{lower:null,upper:5,includeUpper:false}]){
  const selection=view('deck_cond_058',range);
  // An omitted range is invalid, unlike an explicit null range.
  if(range===undefined)delete selection.range;
  assert.equal(previousNbiView(collection,source,selection,null),false);
  assert.throws(()=>open(bundle(source,selection)),/does not match|range is invalid/);
 }
 const invented=view('deck_cond_058',null,'{"new_context":"forged"}');
 assert.equal(previousNbiView(collection,source,invented,null),false);
 assert.throws(()=>open(bundle(source,invented)),/does not match/);
});

test('only explicitly frozen former measurement fields can use the NBI fallback',()=>{
 const fields=['record_type_005a','design_load_031',
  'deck_cond_058','superstructure_cond_059','substructure_cond_060','channel_cond_061','culvert_cond_062',
  'opr_rating_meth_063','inv_rating_meth_065','bridge_condition','lowest_rating','structural_eval_067','undclrence_eval_069',
  'posting_eval_070','waterway_eval_071','appr_road_eval_072','fracture_092a','undwater_look_see_092b','spec_inspect_092c'];
 for(const field of fields){
  const source=snapshot([row(1,{[field]:'2'})]);
  assert.equal(previousNbiView(collection,source,view(field),null),true,field);
 }
 for(const field of ['not_a_column','date_of_inspect_090','fracture_last_date_093a','appr_rail_end_036d',
  'deck_geometry_eval_068','state_code_001','main_unit_spans_045','adt_029','inspect_freq_months_091',
  'structure_kind_043a','structure_type_043b','appr_kind_044a','appr_type_044b','scour_critical_113']){
  const source=snapshot([row(1,{[field]:'2'})]);
  assert.equal(previousNbiView(collection,source,view(field),null),false,field);
 }
});

test('null revision NBI fallback rejects current, future and malformed revisions and other collections',()=>{
 const source=snapshot([row(1,{deck_cond_058:'2'})]),selection=view('deck_cond_058');
 for(const revision of ['nbi-2026-11-27-v1','nbi-future-v2','',0,{},false]){
  assert.equal(previousNbiView(collection,source,selection,revision),false);
  assert.throws(()=>open({...bundle(source,selection),fieldDictionaryRevision:revision}),/does not match/);
 }
 assert.equal(previousNbiView(recoveredCollection('observations-usgs-sites'),source,selection,null),false);
 assert.equal(previousNbiView(recoveredCollection('observations-faa-obstacles'),source,selection,null),false);
});

test('legacy eligibility never interprets censored, leading-zero, missing or unsafe values',()=>{
 for(const value of [null,'','Not supplied','<2','02',true,{longField:true,preview:'2'},'9007199254740992',Number.MAX_SAFE_INTEGER+1]){
  const source=snapshot([row(1,{deck_cond_058:value})]),selection=view('deck_cond_058');
  assert.equal(previousNbiView(collection,source,selection,null),false);
  assert.throws(()=>open(bundle(source,selection)),/does not match/);
 }
});

test('frozen generic context dimensions retain exact order and text, including contexts after twelve',()=>{
 const source=snapshot(Array.from({length:250},(_,index)=>row(index+1,{deck_cond_058:String(index),
  nbi_year:1992+index,unit:' code ',qualifier:`qualifier-${index}`,quality_flag:0})));
 const context='{"unit":" code ","qualifier":"qualifier-249","quality_flag":"0"}';
 const selection=view('deck_cond_058',{lower:249,upper:249,includeUpper:true},context);
 assert.equal(previousNbiView(collection,source,selection,null),true);
 const saved=open(bundle(source,selection));
 assert.equal(saved.view,null);
 assert.deepEqual(saved.snapshot.rows,source.rows);
 assert.equal(previousNbiView(collection,source,{...selection,context:'{"qualifier":"qualifier-249","unit":" code ","quality_flag":"0"}'},null),false);
 assert.equal(previousNbiView(collection,{...source,rows:[...source.rows,row('overflow',{deck_cond_058:'250'})]},selection,null),false);
 const differentYears=snapshot([row(1,{deck_cond_058:'1',nbi_year:1992}),row(2,{deck_cond_058:'9',nbi_year:1993})]);
 assert.equal(previousNbiView(collection,differentYears,view('deck_cond_058',{lower:1,upper:5,includeUpper:false}),null),true);
});

test('valid current contexts keep their exact view even when the dictionary revision is absent',()=>{
 const source=snapshot([row(1,{inspect_freq_months_091:'12'}),row(2,{inspect_freq_months_091:'24'})]);
 const profile=profileCollection(collection,source),group=profile.fields.find(field=>field.name==='inspect_freq_months_091').groups[0];
 const {lower,upper,includeUpper}=measurementDistribution(collection,source,'inspect_freq_months_091',group.context).bins[0];
 const selection=view('inspect_freq_months_091',{lower,upper,includeUpper},group.context);
 const current=JSON.parse(createLabBundle(collection,source,question,selection));
 assert.deepEqual(open(current).view,selection);
 assert.equal(open(current).notice,null);
 delete current.fieldDictionaryRevision;
 assert.deepEqual(open(current).view,selection);
 assert.equal(open(current).notice,null);
});
