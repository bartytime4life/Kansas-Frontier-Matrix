import test from 'node:test';
import assert from 'node:assert/strict';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';
const {recoveredCollection}=await import(await modelUrl('app/recovered-collections.ts'));
const {collectionMetadata}=await import(await modelUrl('app/collection-metadata.ts'));
const {recordedUnit,documentedCode}=await import(await modelUrl('app/collection-field-dictionary.ts'));
const {waterQualityDimensions,previousWaterQualityDimensions}=await import(await modelUrl('app/water-quality-context.ts'));
const {profileCollection,measurementDistribution,storyBrief}=await import(await modelUrl('app/collection-lab.ts'));
const {createLabBundle,openLabBundle}=await import(await modelUrl('app/data-lab/lab-bundle.ts'));
const cases=[
 {id:'observations-wqp-results',value:'result_measure_value',unit:'result_measure_unit_code',condition:'result_detection_condition_text',
  limit:'detection_quantitation_limit_value',limitUnit:'detection_quantitation_limit_unit_code',type:'detection_quantitation_limit_type_name'},
 {id:'observations-usgs-samples-results',value:'result_measure',unit:'result_measure_unit',condition:'result_result_detection_condition',
  limit:'detection_limit_measure_a',limitUnit:'detection_limit_measure_unit_a',type:'detection_limit_type_a'},
];
const sample=rows=>({rows,pages:1,hasMore:true,answers:[{generatedAt:'2026-11-19T12:00:00Z',cache:{state:'stale',at:'2026-11-18T00:00:00Z'}}]});
const row=(id,values)=>({id:String(id),values:{file_id:7,row_number:id,...values},provenance:{source_id:'synthetic-water-quality-QA',source_url:'https://example.org/synthetic',sha256:'a'.repeat(64)}});

test('all 49 legacy fields and 183 WQX3 fields have verified aliases, roles and cited definitions',()=>{
 for(const [i,c] of cases.entries()){
  const collection=recoveredCollection(c.id),m=collectionMetadata(collection),sources=new Set(m.documentation.map(d=>d.id));
  assert.equal(m.fields.filter(f=>f.definition).length,[49,183][i]);
  for(const f of m.fields.filter(f=>f.definition)){
   assert.ok(f.sources.length&&f.sources.every(id=>sources.has(id)),f.name);
   if(!collection.keys.includes(f.name))assert.ok(f.sourceField,f.name);
   if(f.unitField)assert.ok(collection.columns.includes(f.unitField),f.name);
  }
  assert.equal(m.fields.find(f=>f.name===c.value).unitField,c.unit);
  assert.equal(m.fields.find(f=>f.name===c.limit).unitField,c.limitUnit);
  assert.equal(m.provenance.reviewCredit,null);assert.equal(m.temporal.edition,null);
  assert.match(m.fieldNotes.join(' '),/nondetect is not zero/);
  assert.equal(documentedCode(c.id,c.condition,'2'),null);
 }
 assert.ok(collectionMetadata(recoveredCollection(cases[1].id)).fields.find(f=>f.name==='project_name').definition);
});

test('every declared result-comparison dimension separates numeric rows and remains in distribution identity',()=>{
 for(const c of cases){
  const collection=recoveredCollection(c.id),dimensions=waterQualityDimensions[c.id][c.value];
  for(const dimension of dimensions){
   const s=sample([row(1,{[c.value]:'1.00',[dimension]:'A'}),row(2,{[c.value]:'9.00',[dimension]:'B'})]);
   const p=profileCollection(collection,s),groups=p.fields.find(f=>f.name===c.value).groups;
   assert.equal(groups.length,2,dimension);assert.equal(groups[0].mean,1);assert.equal(groups[1].mean,9);
   assert.equal(measurementDistribution(collection,s,c.value,groups[0].context).count,1);
  }
 }
});

test('limits retain their own units, methods, types, qualifiers and matrices without grouping by their own value',()=>{
 for(const c of cases){
  const collection=recoveredCollection(c.id),common={[c.unit]:'mg/L',[c.limitUnit]:'µg/L',[c.type]:'Reporting limit',[c.condition]:'Not Detected'};
  const s=sample([row(1,{...common,[c.value]:'<0.1',[c.limit]:'1'}),row(2,{...common,[c.value]:'<0.2',[c.limit]:'3'})]);
  const p=profileCollection(collection,s),limits=p.fields.find(f=>f.name===c.limit).groups;
  assert.equal(limits.length,1);assert.equal(limits[0].mean,2);assert.equal(JSON.parse(limits[0].context)[c.limit],undefined);
  assert.equal(JSON.parse(limits[0].context)[c.type],'Reporting limit');
  assert.equal(p.fields.find(f=>f.name===c.value).numericCount,0);
  assert.equal(recordedUnit(c.id,c.value,s.rows[0].values),'mg/L');
  assert.equal(recordedUnit(c.id,c.limit,s.rows[0].values),'µg/L');
  assert.equal(recordedUnit(c.id,c.limit,{[c.unit]:'mg/L'}),null);
  assert.equal(recordedUnit(c.id,c.value,Object.create({[c.unit]:'mg/L'})),null);
 }
 const c=cases[1],collection=recoveredCollection(c.id);
 const s=sample([row(1,{[c.value]:'2',detection_limit_measure_b:'1',detection_limit_type_b:'Detection limit',detection_limit_measure_unit_b:'ng/L'})]);
 assert.equal(recordedUnit(c.id,'detection_limit_measure_b',s.rows[0].values),'ng/L');
 const group=profileCollection(collection,s).fields.find(f=>f.name===c.value).groups[0];
 assert.equal(JSON.parse(group.context).detection_limit_measure_b,'1');
});

test('censoring, literal zero, unknown units, QA status and original provenance survive exports',()=>{
 for(const c of cases){
  const collection=recoveredCollection(c.id),s=sample([row(1,{[c.value]:'0.00',[c.condition]:'Not Detected'}),row(2,{[c.value]:'<0.1'}),row(3,{[c.value]:null})]);
  const before=JSON.stringify(s),p=profileCollection(collection,s),value=p.fields.find(f=>f.name===c.value);
  assert.equal(value.numericCount,1);assert.equal(value.groups[0].mean,0);assert.equal(recordedUnit(c.id,c.value,s.rows[0].values),null);
  assert.equal(p.credit.aiReview,null);assert.equal(p.credit.approval,null);assert.equal(p.spatial.mappable,0);
  const bundle=JSON.parse(createLabBundle(collection,s,'Synthetic question',null));
  assert.deepEqual(bundle.records,s.rows);assert.deepEqual(openLabBundle(JSON.stringify(bundle)).snapshot.rows,s.rows);
  const brief=storyBrief(collection,s,'Synthetic question');assert.match(brief,/analytical detection\/quantitation limits/);assert.match(brief,/No AI review or approval/);
  assert.match(brief,/Unit source: each record's/);assert.match(brief,/stale cached/);assert.equal(JSON.stringify(s),before);
 }
});

test('numeric-looking detection conditions, characteristic names, method labels and precision remain metadata',()=>{
 for(const c of cases){
  const collection=recoveredCollection(c.id),names=c.id===cases[0].id?
   [c.condition,'characteristic_name','result_value_type_name','result_weight_basis_text','precision_value','laboratory_name']:
   [c.condition,'result_characteristic','result_method_speciation','result_measure_type','data_quality_precision_value','result_cas_number'];
  const p=profileCollection(collection,sample([row(1,Object.fromEntries(names.map(n=>[n,'2'])))]));
  for(const name of names)assert.deepEqual(p.fields.find(f=>f.name===name).groups,[],name);
 }
});

test('known pre-dictionary views reset with a notice and preserve rows, question and source receipts',()=>{
 for(const c of cases){
  const collection=recoveredCollection(c.id),values={[c.value]:'2',[c.unit]:'mg/L',[c.limit]:'1',[c.limitUnit]:'µg/L',[c.type]:'Reporting limit'};
  const s=sample([row(1,values)]),bundle=JSON.parse(createLabBundle(collection,s,'Keep my question',null));
  delete bundle.fieldDictionaryRevision;
  bundle.view={field:c.value,context:JSON.stringify({[c.unit]:'mg/L'}),range:null};
  assert.ok(previousWaterQualityDimensions[c.id][c.value].includes(c.unit));
  const reopened=openLabBundle(JSON.stringify(bundle));assert.equal(reopened.view,null);assert.match(reopened.notice,/Water-quality definitions/);
  assert.deepEqual(reopened.snapshot.rows,s.rows);assert.equal(reopened.question,'Keep my question');assert.equal(reopened.snapshot.answers[0].cache.state,'stale');
  bundle.view.context='invented context';assert.throws(()=>openLabBundle(JSON.stringify(bundle)),/does not match/);
  bundle.fieldDictionaryRevision='water-quality-2026-11-19-v1';bundle.view.context=JSON.stringify({[c.unit]:'mg/L'});
  assert.throws(()=>openLabBundle(JSON.stringify(bundle)),/does not match/);
 }
});

test('pre-dictionary numeric metadata views can reopen, while nonexistent or nonnumeric views cannot',()=>{
 const c=cases[0],collection=recoveredCollection(c.id),s=sample([row(1,{result_weight_basis_text:'1'})]);
 const bundle=JSON.parse(createLabBundle(collection,s,'Question',null));delete bundle.fieldDictionaryRevision;
 bundle.view={field:'result_weight_basis_text',context:'Unit and measurement context not supplied',range:null};
 assert.equal(openLabBundle(JSON.stringify(bundle)).view,null);
 bundle.records[0].values.result_weight_basis_text='dry';assert.throws(()=>openLabBundle(JSON.stringify(bundle)),/does not match/);
 bundle.view.field='not_a_field';assert.throws(()=>openLabBundle(JSON.stringify(bundle)),/does not match/);
});

test('new water-quality contexts reopen exactly, recompute profiles and reject modified views',()=>{
 for(const c of cases){
  const collection=recoveredCollection(c.id),s=sample([row(1,{[c.value]:'1',[c.unit]:'mg/L',[c.limit]:'0.1'}),row(2,{[c.value]:'3',[c.unit]:'mg/L',[c.limit]:'0.2'})]);
  const bundle=JSON.parse(createLabBundle(collection,s,'Question',null));bundle.profile.credit={aiReview:'forged'};
  assert.deepEqual(openLabBundle(JSON.stringify(bundle)).view,bundle.view);
  assert.equal(profileCollection(collection,openLabBundle(JSON.stringify(bundle)).snapshot).credit.aiReview,null);
  bundle.view.context='other';assert.throws(()=>openLabBundle(JSON.stringify(bundle)),/does not match/);
 }
});
