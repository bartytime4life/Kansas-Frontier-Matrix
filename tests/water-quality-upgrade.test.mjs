import test from 'node:test';
import assert from 'node:assert/strict';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';
const {recoveredCollection}=await import(await modelUrl('app/recovered-collections.ts'));
const {profileCollection}=await import(await modelUrl('app/collection-lab.ts'));
const {createLabBundle,openLabBundle}=await import(await modelUrl('app/data-lab/lab-bundle.ts'));
const {previousQualityView}=await import(await modelUrl('app/data-lab/previous-quality-view.ts'));
const samples=recoveredCollection('observations-usgs-samples-results');
const V1='water-quality-2026-11-19-v1',V2='water-quality-2026-11-27-v2';
const row=(id,values)=>({id:String(id),values:{file_id:91,row_number:id,...values},provenance:{source_id:'synthetic-upgrade-QA',sha256:'b'.repeat(64)}});
const snapshot=rows=>({rows,pages:1,hasMore:true,answers:[{generatedAt:'2026-11-27T12:00:00Z',cache:{state:'stale',at:'2026-11-20T00:00:00Z'},source:{provider:'Synthetic QA'}}]});
function bundle(source,view,collection=samples){
 const data=JSON.parse(createLabBundle(collection,source,'Preserve my source investigation',null));
 data.fieldDictionaryRevision=V1;data.view=view;
 // An imported profile is a claim. It must not supply old role/context eligibility.
 data.profile={fields:[{name:view?.field,role:'value',groups:[{context:view?.context}]}],credit:{aiReview:'forged'}};
 return data;
}
const absent='Unit and measurement context not supplied';

test('known v1 activity-depth range resets after its captured vertical references become separate contexts',()=>{
 const source=snapshot([row(1,{activity_depth_height_measure:'1',activity_depth_height_measure_unit:'m',activity_bottom_depth_altitude_reference_point:'Water surface'}),
  row(2,{activity_depth_height_measure:'9',activity_depth_height_measure_unit:'m',activity_bottom_depth_altitude_reference_point:'Land surface'})]);
 const view={field:'activity_depth_height_measure',context:'{"activity_depth_height_measure_unit":"m"}',range:{lower:1,upper:5,includeUpper:false}};
 assert.equal(previousQualityView(samples,source,view,V1),true);
 const data=bundle(source,view),saved=openLabBundle(JSON.stringify(data));
 assert.equal(saved.view,null);assert.match(saved.notice,/USGS sample definitions/);
 assert.deepEqual(saved.snapshot.rows,source.rows);assert.deepEqual(saved.snapshot.answers,source.answers);
 assert.equal(saved.question,data.question);assert.equal(saved.snapshot.hasMore,true);
 assert.equal(profileCollection(samples,saved.snapshot).credit.aiReview,null);
});

test('v1 metadata values reopen without trusting a forged numeric role or profile',()=>{
 const source=snapshot([row(1,{location_state:'20'}),row(2,{location_state:'21'})]);
 const view={field:'location_state',context:absent,range:{lower:20,upper:20.5,includeUpper:false}};
 assert.equal(previousQualityView(samples,source,view,V1),true);
 const saved=openLabBundle(JSON.stringify(bundle(source,view)));
 assert.equal(saved.view,null);assert.match(saved.notice,/records and question were preserved/);
 assert.deepEqual(saved.snapshot.rows,source.rows);
 // V1 already knew this field was categorical, even if the source happened to look numeric.
 const categorical=snapshot([row(1,{result_characteristic:'20'})]);
 const forged={field:'result_characteristic',context:absent,range:null};
 assert.equal(previousQualityView(samples,categorical,forged,V1),false);
 assert.throws(()=>openLabBundle(JSON.stringify(bundle(categorical,forged))),/does not match/);
});

test('compatible v1 result, analytical-limit and result-depth selections retain their exact views',()=>{
 for(const [values,view] of [
  [{result_measure:'2',result_measure_unit:'mg/L'},
   {field:'result_measure',context:'{"result_measure_unit":"mg/L"}',range:{lower:2,upper:2,includeUpper:true}}],
  [{detection_limit_measure_a:'0.2',detection_limit_type_a:'Reporting limit',detection_limit_measure_unit_a:'µg/L'},
   {field:'detection_limit_measure_a',context:'{"detection_limit_type_a":"Reporting limit","detection_limit_measure_unit_a":"µg/L"}',range:null}],
  [{result_depth_height_measure:'2',result_depth_height_measure_unit:'m',result_depth_height_altitude_reference_point:'Land surface'},
   {field:'result_depth_height_measure',context:'{"reference":"Land surface","result_depth_height_measure_unit":"m","result_depth_height_altitude_reference_point":"Land surface"}',range:null}],
 ]){
  const source=snapshot([row(1,values)]);assert.equal(previousQualityView(samples,source,view,V1),true);
  const saved=openLabBundle(JSON.stringify(bundle(source,view)));assert.deepEqual(saved.view,view);assert.equal(saved.notice,null);
 }
 const missing=snapshot([row(1,{result_depth_height_measure:'2',result_depth_height_measure_unit:'m'})]);
 const unknown={field:'result_depth_height_measure',context:'{"reference":"Not supplied","result_depth_height_measure_unit":"m"}',range:null};
 assert.equal(previousQualityView(samples,missing,unknown,V1),true);
 assert.deepEqual(openLabBundle(JSON.stringify(bundle(missing,unknown))).view,unknown);
});

test('v1 upgrade rejects invented context, nonnumeric values and unavailable old fields',()=>{
 const source=snapshot([row(1,{location_state:'20',result_characteristic:'20'})]);
 for(const field of ['not_a_column','result_characteristic','result_measure_identifier']){
  const view={field,context:absent,range:null};assert.equal(previousQualityView(samples,source,view,V1),false);
 }
 const invented={field:'location_state',context:'{"new_context":"forged"}',range:null};
 assert.equal(previousQualityView(samples,source,invented,V1),false);
 assert.throws(()=>openLabBundle(JSON.stringify(bundle(source,invented))),/does not match/);
 for(const value of [null,'Not supplied','<20','020',true,{longField:true,preview:'20'}]){
  const invalid=snapshot([row(1,{location_state:value})]),view={field:'location_state',context:absent,range:null};
  assert.equal(previousQualityView(samples,invalid,view,V1),false);
  assert.throws(()=>openLabBundle(JSON.stringify(bundle(invalid,view))),/does not match/);
 }
});

test('v1 reset requires an exact former bin rather than a merely plausible numeric range',()=>{
 const source=snapshot([row(1,{location_state:'1'}),row(2,{location_state:'9'})]);
 const view={field:'location_state',context:absent,range:{lower:1,upper:5,includeUpper:false}};
 for(const range of [{lower:1,upper:5,includeUpper:false},{lower:5,upper:9,includeUpper:true}]){
  assert.equal(previousQualityView(samples,source,{...view,range},V1),true);
 }
 for(const range of [undefined,{},[],{lower:1,upper:5,includeUpper:true},{lower:1,upper:9,includeUpper:true},
  {lower:5,upper:1,includeUpper:false},{lower:1,upper:5,includeUpper:'false'},{lower:null,upper:5,includeUpper:false}]){
  const invalid={...view,range};assert.equal(previousQualityView(samples,source,invalid,V1),false);
  assert.throws(()=>openLabBundle(JSON.stringify(bundle(source,invalid))),/does not match|range is invalid/);
 }
 const one=snapshot([row(1,{location_state:'0'})]);
 assert.equal(previousQualityView(samples,one,{...view,range:{lower:0,upper:0,includeUpper:true}},V1),true);
});

test('historical range validation reproduces multi-bin edges rather than merely containing retained values',()=>{
 const source=snapshot([0,1,4,8,9,12].map((value,index)=>row(index+1,{location_state:String(value)})));
 const base={field:'location_state',context:absent};
 for(const range of [{lower:0,upper:4,includeUpper:false},{lower:4,upper:8,includeUpper:false},{lower:8,upper:12,includeUpper:true}]){
  assert.equal(previousQualityView(samples,source,{...base,range},V1),true);
  assert.equal(openLabBundle(JSON.stringify(bundle(source,{...base,range}))).view,null);
 }
 assert.equal(previousQualityView(samples,source,{...base,range:{lower:0,upper:6,includeUpper:false}},V1),false);
});

test('modified/current/future revisions and other collections never trigger the modern-v1 reset',()=>{
 const source=snapshot([row(1,{location_state:'20'})]),view={field:'location_state',context:absent,range:null};
 for(const revision of [V1+' ',V2,'water-quality-2026-12-01-v3',{},17]){
  assert.equal(previousQualityView(samples,source,view,revision),false);
  const data=bundle(source,view);data.fieldDictionaryRevision=revision;
  assert.throws(()=>openLabBundle(JSON.stringify(data)),/does not match/);
 }
 assert.equal(previousQualityView(recoveredCollection('observations-wqp-results'),source,view,V1),false);
 const collection=recoveredCollection('observations-wqp-results'),wqp=snapshot([row(1,{result_measure_value:'1',result_measure_unit_code:'mg/L'})]);
 const current=JSON.parse(createLabBundle(collection,wqp,'Legacy profile remains unchanged',null));
 assert.equal(current.fieldDictionaryRevision,V1);assert.deepEqual(openLabBundle(JSON.stringify(current)).view,current.view);
});

test('the v1 context picker limit remains part of validating a historical selection',()=>{
 const source=snapshot(Array.from({length:13},(_,i)=>row(i+1,{result_measure:String(i+1),result_measure_unit:'unit-'+i})));
 assert.equal(previousQualityView(samples,source,{field:'result_measure',context:'{"result_measure_unit":"unit-11"}',range:null},V1),true);
 assert.equal(previousQualityView(samples,source,{field:'result_measure',context:'{"result_measure_unit":"unit-12"}',range:null},V1),false);
});
