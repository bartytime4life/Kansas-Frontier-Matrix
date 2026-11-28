import assert from 'node:assert/strict';
import test from 'node:test';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';

const {measurementContexts,measurementDistribution,profileCollection,loadLabSample}=await import(await modelUrl('app/collection-lab.ts'));
const {createLabBundle,openLabBundle}=await import(await modelUrl('app/data-lab/lab-bundle.ts'));
const {recoveredCollection}=await import(await modelUrl('app/recovered-collections.ts'));
const collection=recoveredCollection('observations-usgs-samples-results');
const field='result_measure';
const common={result_characteristic:'Nitrate',result_measure_unit:'mg/L',activity_media:'Water'};
const row=(id,values)=>({id,values:{...common,...values},provenance:{source_id:'synthetic-context-QA',source_url:'https://example.org/synthetic-context',sha256:'a'.repeat(64)}});
const read={generatedAt:'2026-11-27T12:00:00Z',source:{provider:'Synthetic context QA'},cache:{state:'stale',at:'2026-11-26T12:00:00Z'}};
const snapshot=rows=>({rows,pages:1,hasMore:true,answers:[read]});
const manyRows=Array.from({length:250},(_,index)=>row(`context-${index}`,{
 [field]:String(index),result_analytical_method_identifier:`method-${index}`,
}));
const fullSnapshot={rows:manyRows,pages:5,hasMore:true,answers:Array.from({length:5},()=>({...read}))};

test('every loaded context is available beyond the twelve-group profile overview',()=>{
 const before=JSON.stringify(fullSnapshot);
 const contexts=measurementContexts(collection,fullSnapshot,field);
 const profile=profileCollection(collection,fullSnapshot);
 const summary=profile.fields.find(candidate=>candidate.name===field);
 assert.equal(contexts.length,250);
 assert.deepEqual(contexts.map(({context})=>JSON.parse(context).result_analytical_method_identifier),
  manyRows.map(record=>record.values.result_analytical_method_identifier));
 assert.ok(contexts.every(context=>context.count===1));
 assert.equal(summary.groups.length,12);
 assert.equal(summary.additionalGroups,238);
 assert.deepEqual(contexts.slice(0,12),summary.groups.map(({context,count})=>({context,count})));
 assert.equal(summary.numericCount,250);
 assert.deepEqual(measurementDistribution(collection,fullSnapshot,field,contexts.at(-1).context).bins[0].records,[{
  id:'context-249',value:249,sourceId:'synthetic-context-QA',sourceUrl:'https://example.org/synthetic-context',
 }]);
 assert.equal(JSON.stringify(fullSnapshot),before);
});

test('full contexts keep recorded units, methods, limits and qualifiers separate without interpreting sentinels',()=>{
 const base={...common,[field]:'0',result_analytical_method_identifier:'method',result_measure_qualifier_code:'Estimated',
  detection_limit_type_a:'Reporting limit',detection_limit_measure_a:'0.1',detection_limit_measure_unit_a:'mg/L'};
 const alternatives={result_measure_unit:'µg/L',result_analytical_method_identifier:'other method',
  result_measure_qualifier_code:'Provisional',detection_limit_type_a:'Detection limit',detection_limit_measure_a:'0.2',
  detection_limit_measure_unit_a:'ng/L',activity_media:'Sediment',result_sample_fraction:'Filtered',
  result_weight_basis:'Dry',result_time_basis:'Daily',result_method_speciation:'Nitrate as N',
  sample_collection_method_identifier:'Other collection method',lab_info_name:'Other laboratory'};
 const rows=[row('zero',base),...Object.entries(alternatives).map(([dimension,value],index)=>
  row(`separate-${index}`,{...base,[field]:String(index+1),[dimension]:value}))];
 rows.push(row('same-context',{...base,[field]:'4'}));
 for(const [index,value] of [null,'','  ','<0.1','02','9007199254740992',Number.MAX_SAFE_INTEGER+1,{longField:true}].entries()){
  rows.push(row(`excluded-${index}`,{...base,[field]:value}));
 }
 const sample=snapshot(rows),before=JSON.stringify(sample);
 const contexts=measurementContexts(collection,sample,field);
 assert.equal(contexts.length,14);
 assert.equal(contexts[0].count,2);
 assert.equal(contexts.reduce((total,context)=>total+context.count,0),15);
 assert.deepEqual(measurementDistribution(collection,sample,field,contexts[0].context).bins.flatMap(bin=>bin.records.map(record=>record.value)),[0,4]);
 assert.equal(JSON.parse(contexts.at(-1).context).lab_info_name,'Other laboratory');
 assert.deepEqual(measurementContexts(collection,sample,'result_characteristic'),[]);
 assert.deepEqual(measurementContexts(collection,sample,'not_a_field'),[]);
 assert.equal(JSON.stringify(sample),before);
});

test('the last loaded context and its exact range reopen with all original records and receipts',()=>{
 const context=measurementContexts(collection,fullSnapshot,field).at(-1).context;
 const view={field,context,range:{lower:249,upper:249,includeUpper:true}};
 const question='Compare only this recorded analytical method.';
 const bundle=JSON.parse(createLabBundle(collection,fullSnapshot,question,view));
 assert.equal(bundle.profile.fields.find(candidate=>candidate.name===field).groups.length,12);
 assert.equal(bundle.profile.fields.find(candidate=>candidate.name===field).groups.some(group=>group.context===context),false);
 const reopened=openLabBundle(JSON.stringify(bundle));
 assert.deepEqual(reopened.view,view);
 assert.deepEqual(reopened.snapshot.rows,manyRows);
 assert.deepEqual(reopened.snapshot.answers,fullSnapshot.answers);
 assert.equal(reopened.snapshot.pages,5);
 assert.equal(reopened.snapshot.hasMore,true);
 assert.equal(reopened.question,question);
 assert.equal(reopened.notice,null);
 assert.equal(profileCollection(collection,reopened.snapshot).credit.aiReview,null);
 bundle.view.range=null;
 assert.deepEqual(openLabBundle(JSON.stringify(bundle)).view,{field,context,range:null});
 const defaultView=openLabBundle(createLabBundle(collection,fullSnapshot,question,null)).view;
 assert.equal(defaultView.context,measurementContexts(collection,fullSnapshot,field)[0].context);
});

test('expanded selection still rejects forged contexts, metadata fields, altered bins and oversized captures',()=>{
 const context=measurementContexts(collection,fullSnapshot,field).at(-1).context;
 const view={field,context,range:{lower:249,upper:249,includeUpper:true}};
 const bundle=JSON.parse(createLabBundle(collection,fullSnapshot,'Keep the evidence',view));
 const open=change=>openLabBundle(JSON.stringify({...bundle,...change}));
 const forged='invented comparison context';
 bundle.profile.fields.find(candidate=>candidate.name===field).groups.push({context:forged,count:1,min:249,max:249});
 assert.throws(()=>open({view:{field,context:forged,range:null}}),/context does not match/);
 assert.throws(()=>open({view:{...view,range:{...view.range,upper:250}}}),/range does not match/);
 assert.throws(()=>open({view:{field:'result_characteristic',context,range:null}}),/context does not match/);
 assert.throws(()=>open({view:{field:'not_a_field',context,range:null}}),/context does not match/);
 assert.throws(()=>open({records:[...manyRows,row('overflow',{[field]:'250'})]}),/valid Record Lab JSON/);
 assert.throws(()=>open({capture:{...bundle.capture,pages:6,reads:[...bundle.capture.reads,read]}}),/invalid sample receipt/);
});

test('enumerating all contexts leaves the live sample bounded to five fifty-record reads',async()=>{
 const calls=[];
 const sample=await loadLabSample(collection,new AbortController().signal,async(_dataset,options)=>{
  calls.push(options);
  const page=calls.length-1;
  return {collection:collection.id,rows:manyRows.slice(page*50,page*50+50),hasMore:true,nextCursor:`page-${page+1}`,...read};
 });
 assert.equal(calls.length,5);
 assert.ok(calls.every(call=>call.limit==='50'));
 assert.equal(sample.rows.length,250);
 assert.equal(sample.pages,5);
 assert.equal(sample.hasMore,true);
 assert.equal(measurementContexts(collection,sample,field).length,250);
});
