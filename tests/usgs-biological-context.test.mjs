import test from 'node:test';
import assert from 'node:assert/strict';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';
const {recoveredCollection}=await import(await modelUrl('app/recovered-collections.ts'));
const {profileCollection,measurementDistribution}=await import(await modelUrl('app/collection-lab.ts'));
const {createLabBundle,openLabBundle}=await import(await modelUrl('app/data-lab/lab-bundle.ts'));
const {previousBiologicalView}=await import(await modelUrl('app/data-lab/previous-quality-view.ts'));
const c=recoveredCollection('observations-usgs-samples-results');
const V2='water-quality-2026-11-27-v2',V3='water-quality-2026-11-27-v3';
const row=(id,species,value,patch={})=>({id:String(id),values:{file_id:91,row_number:id,result_biological_taxon:'SyntheticGenus',
 result_biological_unidentified_species_identifier:species,result_biological_group_summary_count:value,
 group_summary_weight_measure:value,group_summary_weight_measure_unit:'g',...patch},provenance:{source_id:'synthetic-biological-context-QA',sha256:'b'.repeat(64)}});
const snapshot=rows=>({rows,pages:1,hasMore:true,answers:[{generatedAt:'2026-11-27T12:00:00Z',cache:{state:'stale',at:'2026-11-26T12:00:00Z'},source:{provider:'Synthetic QA'}}]});
const oldContext=field=>JSON.stringify({...(field==='result_biological_group_summary_count'?{unit:'count'}:{group_summary_weight_measure_unit:'g'}),result_biological_taxon:'SyntheticGenus'});
function oldBundle(s,field,range=null){
 const b=JSON.parse(createLabBundle(c,s,'Preserve my unresolved-species investigation',null));
 b.fieldDictionaryRevision=V2;b.view={field,context:oldContext(field),range};
 b.profile={fields:[{name:field,role:'value',groups:[{context:b.view.context}]}],credit:{aiReview:'forged'}};
 return b;
}

for(const field of ['result_biological_group_summary_count','group_summary_weight_measure']){
 test(`${field} keeps distinct unresolved species within a recorded genus separate`,()=>{
  const s=snapshot([row(1,'Species A','2'),row(2,'Species B','8'),row(3,null,'4')]),before=JSON.stringify(s);
  const p=profileCollection(c,s),groups=p.fields.find(f=>f.name===field).groups;
  assert.equal(groups.length,3);assert.deepEqual(groups.map(g=>g.mean),[2,8,4]);
  assert.deepEqual(groups.map(g=>JSON.parse(g.context).result_biological_unidentified_species_identifier),['Species A','Species B',undefined]);
  assert.equal(measurementDistribution(c,s,field,groups[0].context).count,1);
  assert.deepEqual(p.fields.find(f=>f.name==='result_biological_unidentified_species_identifier').groups,[]);
  assert.equal(p.credit.aiReview,null);assert.equal(JSON.stringify(s),before);
 });
 test(`known v2 ${field} ranges reset after exact old-context/bin validation`,()=>{
  const s=snapshot([row(1,'Species A','2'),row(2,'Species B','8')]);
  const b=oldBundle(s,field,{lower:2,upper:5,includeUpper:false});
  assert.equal(previousBiologicalView(c,s,b.view,V2),true);
  const opened=openLabBundle(JSON.stringify(b));
  assert.equal(opened.view,null);assert.match(opened.notice,/USGS sample definitions and comparison contexts have changed/);
  assert.deepEqual(opened.snapshot.rows,s.rows);assert.deepEqual(opened.snapshot.answers,s.answers);
  assert.equal(opened.question,b.question);assert.equal(opened.snapshot.hasMore,true);
  const exported=JSON.parse(createLabBundle(c,opened.snapshot,opened.question,opened.view));
  assert.equal(exported.fieldDictionaryRevision,V3);assert.deepEqual(exported.records,s.rows);
  assert.equal(exported.profile.credit.aiReview,null);assert.equal(exported.profile.fields.find(f=>f.name===field).groups.length,2);
 });
}

test('identifier leading zeros, genus boundaries, literal zero and weight units survive grouping',()=>{
 const s=snapshot([row(1,'0007','0'),row(2,'7','3'),row(3,'0007','2',{result_biological_taxon:'OtherSyntheticGenus'}),
  row(4,'0007','2',{group_summary_weight_measure_unit:'kg'})]);
 const p=profileCollection(c,s);
 assert.equal(p.fields.find(f=>f.name==='result_biological_group_summary_count').groups.length,3);
 const weights=p.fields.find(f=>f.name==='group_summary_weight_measure').groups;
 assert.equal(weights.length,4);assert.equal(weights[0].mean,0);
 assert.equal(s.rows[0].values.result_biological_unidentified_species_identifier,'0007');
 assert.equal(JSON.parse(weights[0].context).group_summary_weight_measure_unit,'g');
 assert.equal(JSON.parse(weights[3].context).group_summary_weight_measure_unit,'kg');
});

test('compatible v2 biology and ordinary result selections retain their exact views',()=>{
 for(const field of ['result_biological_group_summary_count','group_summary_weight_measure']){
  const s=snapshot([row(1,null,'2')]),b=oldBundle(s,field,{lower:2,upper:2,includeUpper:true});
  const opened=openLabBundle(JSON.stringify(b));assert.deepEqual(opened.view,b.view);assert.equal(opened.notice,null);
 }
 const s=snapshot([row(1,'Species A','2',{result_measure:'1',result_measure_unit:'mg/L'})]);
 const b=JSON.parse(createLabBundle(c,s,'Question',null));b.fieldDictionaryRevision=V2;
 const context=profileCollection(c,s).fields.find(f=>f.name==='result_measure').groups[0].context;
 b.view={field:'result_measure',context,range:null};
 assert.equal(previousBiologicalView(c,s,b.view,V2),false);
 assert.deepEqual(openLabBundle(JSON.stringify(b)).view,b.view);
});

test('only an exact v2 biological view can trigger this reset',()=>{
 const s=snapshot([row(1,'Species A','2'),row(2,'Species B','8')]);
 const b=oldBundle(s,'result_biological_group_summary_count');
 for(const revision of [V3,'water-quality-2026-12-01-v4',V2+' ',17,{}]){
  b.fieldDictionaryRevision=revision;
  assert.equal(previousBiologicalView(c,s,b.view,revision),false);
  assert.throws(()=>openLabBundle(JSON.stringify(b)),/does not match/);
 }
 b.fieldDictionaryRevision=V2;
 for(const view of [{...b.view,context:'{"unit":"count","invented":"context"}'},
  {...b.view,range:{lower:2,upper:8,includeUpper:true}},
  {...b.view,range:{lower:2,upper:5,includeUpper:true}},
  {...b.view,range:{lower:5,upper:2,includeUpper:false}},
  {...b.view,field:'result_biological_unidentified_species_identifier'}]){
  assert.equal(previousBiologicalView(c,s,view,V2),false);
  assert.throws(()=>openLabBundle(JSON.stringify({...b,view})),/does not match/);
 }
});

test('new v3 selections stay exact, and the fallback never reinterprets censored or missing numbers',()=>{
 const s=snapshot([row(1,'Species A','2'),row(2,'Species B','8')]);
 const b=JSON.parse(createLabBundle(c,s,'Question',null));assert.equal(b.fieldDictionaryRevision,V3);
 assert.deepEqual(openLabBundle(JSON.stringify(b)).view,b.view);
 b.view={field:'result_biological_group_summary_count',context:oldContext('result_biological_group_summary_count'),range:null};
 assert.throws(()=>openLabBundle(JSON.stringify(b)),/does not match/);
 for(const value of [null,'<2','02',true,{longField:true,preview:'2'}]){
  const invalid=snapshot([row(1,'Species A',value)]),old=oldBundle(invalid,'result_biological_group_summary_count');
  assert.equal(previousBiologicalView(c,invalid,old.view,V2),false);
  assert.throws(()=>openLabBundle(JSON.stringify(old)),/does not match/);
 }
});

test('v2 first-twelve-context bound still applies to fallback validation',()=>{
 const s=snapshot(Array.from({length:13},(_,i)=>row(i+1,'Species A',String(i+1),{result_biological_taxon:'SyntheticGenus '+i})));
 const b=oldBundle(s,'result_biological_group_summary_count');
 b.view.context=JSON.stringify({unit:'count',result_biological_taxon:'SyntheticGenus 12'});
 assert.equal(previousBiologicalView(c,s,b.view,V2),false);
 assert.throws(()=>openLabBundle(JSON.stringify(b)),/does not match/);
 b.view.context=JSON.stringify({unit:'count',result_biological_taxon:'SyntheticGenus 0'});
 assert.equal(previousBiologicalView(c,s,b.view,V2),true);
 assert.equal(openLabBundle(JSON.stringify(b)).view,null);
});
