import test from 'node:test';
import assert from 'node:assert/strict';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';
const {recoveredCollection}=await import(await modelUrl('app/recovered-collections.ts'));
const {connectRecordContexts,recordContextPlans,recordContextBrief}=await import(await modelUrl('app/data-lab/record-context.ts'));
const {createLabBundle,openLabBundle,MAX_LAB_BUNDLE_BYTES}=await import(await modelUrl('app/data-lab/lab-bundle.ts'));
const daily=recoveredCollection('observations-usgs-daily-values'),peaks=recoveredCollection('observations-usgs-peaks');
const sites=recoveredCollection('observations-usgs-sites'),series=recoveredCollection('observations-usgs-series');
const row=(id,values={})=>({id,values:{monitoring_location_id:'USGS-001',time_series_id:'001',parameter_code:'00060',statistic_id:'00003',unit_of_measure:'ft3/s',...values},provenance:{source_id:'synthetic-context-links',sha256:'a'.repeat(64)}});
const sample=rows=>({rows,pages:1,hasMore:true,answers:[{generatedAt:'2026-11-18T12:00:00Z',source:{provider:'Synthetic QA'},cache:{state:'stale',at:'2026-11-17T12:00:00Z'}}]});
const attached=(collectionId,rows)=>({collectionId,snapshot:sample(rows)});
const link=(source,context)=>connectRecordContexts(daily,sample(source),[context]).relations[0];

test('bounded metadata matching preserves duplicate captures and every unmatched observation',()=>{
 const original=[row('o1'),row('o2',{monitoring_location_id:'USGS-002'}),row('o3',{monitoring_location_id:null}),row('o4',{monitoring_location_id:'USGS-003'})];
 const metadata=[row('c1'),row('c2'),row('c3',{monitoring_location_id:'USGS-002'}),row('c4',{monitoring_location_id:null})];
 const before=JSON.stringify({original,metadata});
 const result=link(original,attached(sites.id,metadata));
 assert.deepEqual(result.rows.map(r=>r.status),['multiple_matches','one_match','missing_key','no_match']);
 assert.deepEqual(result.rows[0].matches.map(m=>m.targetRecordId),['c1','c2']);
 assert.equal(result.counts.sourceRows,4);assert.equal(result.counts.multipleMatches,1);
 assert.equal(result.counts.oneMatch,1);assert.equal(result.counts.noMatch,1);assert.equal(result.counts.missingKey,1);
 assert.equal(result.targetSample.missingKeys,1);assert.equal(result.targetSample.hasMore,true);assert.equal(result.targetSample.stale,true);
 assert.equal(JSON.stringify({original,metadata}),before);
});

test('identity matching preserves leading zeros, exact strings and own properties',()=>{
 const inherited=Object.create({monitoring_location_id:'USGS-001'});
 const originals=[row('1'),row('2',{monitoring_location_id:'USGS-1'}),row('3',{monitoring_location_id:' USGS-001'}),row('4',{monitoring_location_id:1}),{id:'5',values:inherited}];
 const result=link(originals,attached(sites.id,[row('c1')]));
 assert.deepEqual(result.rows.map(r=>r.status),['one_match','no_match','no_match','missing_key','missing_key']);
 assert.deepEqual(result.rows[0].matches[0].conflicts,[]);
});

test('daily and peak series require the documented data-type namespace; field series cannot attach',()=>{
 const context=attached(series.id,[row('daily',{data_type:'Daily values'}),row('peak',{data_type:'Peaks'}),row('unknown'),row('wrongcase',{data_type:'daily values'})]);
 const d=link([row('o')],context);
 assert.deepEqual(d.rows[0].matches.map(m=>m.targetRecordId),['daily']);assert.equal(d.targetSample.namespaceExcluded,3);
 const p=connectRecordContexts(peaks,sample([row('o')]),[context]).relations[0];
 assert.deepEqual(p.rows[0].matches.map(m=>m.targetRecordId),['peak']);
 assert.equal(p.expectedDataType,'Peaks');
 assert.throws(()=>connectRecordContexts(recoveredCollection('observations-usgs-field-measurements'),sample([row('o')]),[context]),/unsupported/);
 assert.deepEqual(recordContextPlans('observations-faa-obstacles'),[]);
 assert.deepEqual(recordContextPlans('__proto__'),[]);
});

test('same series identity retains conflicting and unknown comparison fields without replacing observation values',()=>{
 const original=row('o',{value:'17',monitoring_location_id:'USGS-001'});
 const context=attached(series.id,[row('different',{data_type:'Daily values',unit_of_measure:'m3/s',monitoring_location_id:'USGS-002',parameter_code:'00065',statistic_id:null})]);
 const result=link([original],context),match=result.rows[0].matches[0];
 assert.equal(result.rows[0].status,'one_match');
 assert.deepEqual(match.conflicts,['monitoring_location_id','parameter_code','unit_of_measure']);
 assert.deepEqual(match.unverified,['statistic_id']);
 assert.equal(result.counts.conflictingRows,1);assert.equal(result.counts.unverifiedRows,1);
 assert.equal(original.values.value,'17');assert.equal(original.values.unit_of_measure,'ft3/s');
 const report=connectRecordContexts(daily,sample([original]),[context]);
 assert.match(recordContextBrief(report),/not proof of a unique, current or applicable/);
 assert.match(recordContextBrief(report),/1 rows have conflicting shared series fields/);
 assert.match(recordContextBrief(report),/user-supplied file references/i);
});

test('metadata attachments reject unsupported collections, duplicates and samples beyond record/read bounds',()=>{
 const source=sample([row('o')]),a=attached(sites.id,[row('c')]);
 assert.throws(()=>connectRecordContexts(daily,source,[a,a]),/unsupported or already attached/);
 assert.throws(()=>connectRecordContexts(daily,source,[a,a,a]),/at most/);
 assert.throws(()=>connectRecordContexts(daily,source,[attached('observations-faa-obstacles',[])]),/unsupported/);
 assert.throws(()=>connectRecordContexts(daily,source,[attached(sites.id,Array.from({length:251},(_,i)=>row(String(i))))]),/bounded/);
 assert.throws(()=>connectRecordContexts(daily,source,[{...a,snapshot:{...a.snapshot,answers:[]}}]),/bounded/);
});

test('lab round trip preserves all observation/context records, receipts, question and selected measurement',()=>{
 const source=sample([row('o1',{value:1}),row('o2',{value:2})]);
 const contexts=[attached(sites.id,[row('c1',{name:'Synthetic station',altitude:'0',vertical_datum:'NAVD88'})]),attached(series.id,[row('c2',{data_type:'Daily values'})])];
 const question='Which station metadata applies to these archived observations?';
 const contents=createLabBundle(daily,source,question,null,undefined,contexts),json=JSON.parse(contents);
 assert.deepEqual(json.records,source.rows);assert.deepEqual(json.contexts.map(c=>c.records),contexts.map(c=>c.snapshot.rows));
 assert.equal(json.connections.relations[1].counts.oneMatch,2);assert.equal(json.profile.credit.aiReview,null);
 assert.match(json.brief,/Connected metadata samples/);assert.match(json.brief,/not observation dates/);
 const saved=openLabBundle(contents);
 assert.equal(saved.question,question);assert.deepEqual(saved.snapshot.rows,source.rows);assert.deepEqual(saved.view,json.view);
 for(let i=0;i<contexts.length;i++){
  assert.deepEqual(saved.contexts[i].snapshot.rows,contexts[i].snapshot.rows);
  assert.deepEqual(saved.contexts[i].snapshot.answers,contexts[i].snapshot.answers);
  assert.equal(saved.contexts[i].snapshot.origin,'saved-bundle');
 }
 const again=JSON.parse(createLabBundle(daily,saved.snapshot,saved.question,saved.view,undefined,saved.contexts));
 assert.deepEqual(again.connections.relations.map(r=>r.rows),json.connections.relations.map(r=>r.rows));
 assert.match(again.brief,/Origin: saved-bundle/);
});

test('imported connection summaries are recomputed; malformed/nested attachments cannot bypass bundle validation',()=>{
 const source=sample([row('o',{value:1})]),contexts=[attached(sites.id,[row('c')])];
 const original=JSON.parse(createLabBundle(daily,source,'Synthetic QA',null,undefined,contexts));
 const altered=structuredClone(original);altered.connections.relations[0].counts.oneMatch=999;
 altered.contexts[0].profile.credit.aiReview='forged';
 const opened=openLabBundle(JSON.stringify(altered));
 const rebuilt=JSON.parse(createLabBundle(daily,opened.snapshot,opened.question,opened.view,undefined,opened.contexts));
 assert.equal(rebuilt.connections.relations[0].counts.oneMatch,1);assert.equal(rebuilt.contexts[0].profile.credit.aiReview,null);
 for(const contexts of [null,{},[original.contexts[0],original.contexts[0]],Array(3).fill(original.contexts[0]),[{...original.contexts[0],contexts:[]}],[{...original.contexts[0],records:[row('c'),row('c')]}]]){
  assert.throws(()=>openLabBundle(JSON.stringify({...original,contexts})));
 }
 assert.deepEqual(openLabBundle(createLabBundle(daily,source,'No context',null)).contexts,[]);
});

test('UTF-8 bundle size limits apply to import and export without dropping source records',()=>{
 const large=sample([row('o',{value:1,note:'水'.repeat(Math.ceil(MAX_LAB_BUNDLE_BYTES/3))})]);
 assert.throws(()=>createLabBundle(daily,large,'Large synthetic QA',null),/8 MB/);
 const json=JSON.stringify({format:'kfm-record-lab-bundle-v1',question:'QA',records:[],note:'水'.repeat(Math.ceil(MAX_LAB_BUNDLE_BYTES/3))});
 assert.ok(json.length<MAX_LAB_BUNDLE_BYTES);
 assert.throws(()=>openLabBundle(json),/8 MB/);
 assert.ok(large.rows[0].values.note.length>0);
});
