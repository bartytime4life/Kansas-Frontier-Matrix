import test from 'node:test';
import assert from 'node:assert/strict';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';

const {recoveredCollection}=await import(await modelUrl('app/recovered-collections.ts'));
const {collectionMetadata,fieldRole}=await import(await modelUrl('app/collection-metadata.ts'));
const {documentedCode}=await import(await modelUrl('app/collection-field-dictionary.ts'));
const {profileCollection,measurementDistribution,measurementLayer,storyBrief}=await import(await modelUrl('app/collection-lab.ts'));
const {createLabBundle,openLabBundle}=await import(await modelUrl('app/data-lab/lab-bundle.ts'));
const c=recoveredCollection('observations-faa-obstacles');
const row=(id,patch={})=>({id,values:{file_id:1,row_number:Number(id),quantity:1,
 agl_height_ft:0,amsl_height_ft:1000,verification_status:'O',horizontal_accuracy:'1',vertical_accuracy:'A',
 julian_date:'2024366',geometry_geojson:'{"type":"Point","coordinates":[-98,38]}',...patch},
 provenance:{source_id:'synthetic-faa-qa',source_url:'https://example.org/qa',sha256:'a'.repeat(64)}});
const rows=[row('1'),row('2',{agl_height_ft:100,amsl_height_ft:1100,quantity:2}),
 row('3',{agl_height_ft:200,verification_status:'U'}),row('4',{agl_height_ft:300,horizontal_accuracy:'2'}),
 row('5',{agl_height_ft:400,vertical_accuracy:'B'}),row('6',{agl_height_ft:null})];
const sample={rows,pages:1,hasMore:true,answers:[{generatedAt:'2026-11-18T12:00:00Z'}]};
const profile=profileCollection(c,sample);
const height=profile.fields.find(f=>f.name==='agl_height_ft');
const context=height.groups[0].context;

test('all FAA fields cite documented definitions while record edition and review stay unknown',()=>{
 const m=collectionMetadata(c),ids=new Set(m.documentation.map(d=>d.id));
 assert.equal(m.fields.length,31);
 for(const field of m.fields){
  assert.ok(field.definition,field.name);assert.equal(field.roleBasis,'documented');
  assert.ok(field.sources.length);assert.ok(field.sources.every(id=>ids.has(id)));
 }
 assert.equal(m.fields.find(f=>f.name==='agl_height_ft').unit,'ft');
 assert.equal(m.fields.find(f=>f.name==='amsl_height_ft').reference,'AMSL');
 assert.equal(m.fields.find(f=>f.name==='julian_date').encoding,'YYYYDDD');
 assert.match(m.fields.find(f=>f.name==='julian_date').definition,/Action date/);
 assert.equal(m.documentation[0].edition,'2026-05-21');
 assert.equal(m.documentation[0].sha256,'9d845743b688a0a032a3bfff661de9f756d5f947f158e7c92fcd00e17222514c');
 assert.equal(m.temporal.edition,null);assert.equal(m.provenance.reviewCredit,null);
 assert.equal(m.fields.find(f=>f.name==='horizontal_accuracy').unit,null);
});

test('numeric accuracy codes and other categories are excluded from distributions and map measurements',()=>{
 for(const name of ['horizontal_accuracy','vertical_accuracy','verification_status','lighting','marking','action','obstacle_type']){
  const f=profile.fields.find(f=>f.name===name);
  assert.equal(f.numericCount,0,name);assert.deepEqual(f.groups,[]);
  assert.deepEqual(measurementDistribution(c,sample,name,context),{count:0,bins:[]});
  assert.throws(()=>measurementLayer(c,sample,name,context),/measurement field/);
 }
});

test('feet, AGL/AMSL and each quality category stay distinct without losing zero or missing values',()=>{
 assert.equal(height.numericCount,5);assert.equal(height.missing,1);assert.equal(height.groups.length,4);
 assert.equal(height.groups[0].count,2);assert.equal(height.groups[0].min,0);assert.equal(height.groups[0].mean,50);
 assert.deepEqual(JSON.parse(context),{unit:'ft',reference:'AGL',verification_status:'O',horizontal_accuracy:'1',vertical_accuracy:'A'});
 const amsl=profile.fields.find(f=>f.name==='amsl_height_ft');
 assert.equal(JSON.parse(amsl.groups[0].context).reference,'AMSL');
 assert.notEqual(amsl.groups[0].context,context);
 assert.equal(measurementDistribution(c,sample,'agl_height_ft',context).count,2);
 assert.equal(JSON.parse(profile.fields.find(f=>f.name==='quantity').groups[0].context).unit,'obstacles');
});

test('tolerance legends preserve unknowns, nautical-mile codes and collection-specific semantics',()=>{
 assert.equal(documentedCode(c.id,'horizontal_accuracy','7'),'±0.5 NM');
 assert.equal(documentedCode(c.id,'horizontal_accuracy','9'),'Unknown');
 assert.equal(documentedCode(c.id,'vertical_accuracy','I'),'Unknown');
 for(const value of ['Z','0','toString','__proto__'])assert.equal(documentedCode(c.id,'horizontal_accuracy',value),null);
 assert.equal(fieldRole('horizontal_accuracy',[],c.id),'quality');
 assert.equal(fieldRole('horizontal_accuracy',[],'observations-other'),'value');
 assert.equal(fieldRole('agl_height_ft',['agl_height_ft'],c.id),'identity');
 const other=collectionMetadata(recoveredCollection('observations-wqp-stations'));
 assert.deepEqual(other.documentation,[]);
 assert.equal(other.fields.find(f=>f.name==='horizontal_accuracy_value').definition,null);
});

test('layer and story export source-backed units, definitions and scope while retaining original rows',()=>{
 const original=JSON.stringify(rows),layer=measurementLayer(c,sample,'agl_height_ft',context);
 assert.equal(layer.features.length,2);assert.equal(layer.kfm.omitted.otherContext,3);assert.equal(layer.kfm.omitted.notNumeric,1);
 assert.deepEqual(layer.features.map(f=>f.id),['1','2']);
 assert.equal(layer.features[0].properties.unit,'ft');assert.equal(layer.features[0].properties.reference,'AGL');
 assert.equal(layer.kfm.fieldDefinition.unit,'ft');assert.equal(layer.kfm.documentation.length,3);
 assert.equal(layer.kfm.contextDefinitions.find(f=>f.name==='horizontal_accuracy').codes['1'],'±20 ft');
 assert.equal(layer.kfm.reviewCredit,null);
 const brief=storyBrief(c,sample,'How do these synthetic records differ?');
 assert.match(brief,/Field definitions and units/);assert.match(brief,/Unit: ft/);
 assert.match(brief,/documentation edition 2026-05-21/);assert.match(brief,/YYYYDDD/);
 assert.match(brief,/legacy array/);assert.match(brief,/No AI review or approval/);
 assert.equal(JSON.stringify(rows),original);
});

test('new FAA bundles reopen the exact documented context and reject altered selections',()=>{
 const bin=measurementDistribution(c,sample,'agl_height_ft',context).bins[0];
 const view={field:'agl_height_ft',context,range:{lower:bin.lower,upper:bin.upper,includeUpper:bin.includeUpper}};
 const parsed=JSON.parse(createLabBundle(c,sample,'QA question',view));
 assert.equal(parsed.fieldDictionaryRevision,'faa-ddof-2026-05-21-v1');
 const reopened=openLabBundle(JSON.stringify(parsed));
 assert.deepEqual(reopened.view,view);assert.deepEqual(reopened.snapshot.rows,rows);assert.equal(reopened.notice,null);
 assert.throws(()=>openLabBundle(JSON.stringify({...parsed,view:{...view,context:'Unit and measurement context not supplied'}})),/does not match/);
});

test('older pooled FAA bundles preserve records and question with an explicit selection-reset notice',()=>{
 const parsed=JSON.parse(createLabBundle(c,sample,'Original QA question',null));
 delete parsed.fieldDictionaryRevision;
 for(const field of ['agl_height_ft','horizontal_accuracy']){
  parsed.view={field,context:'Unit and measurement context not supplied',range:{lower:0,upper:500,includeUpper:true}};
  const reopened=openLabBundle(JSON.stringify(parsed));
  assert.deepEqual(reopened.snapshot.rows,rows);assert.equal(reopened.question,'Original QA question');
  assert.equal(reopened.view,null);assert.match(reopened.notice,/records and question were preserved/);
  assert.equal(reopened.snapshot.origin,'saved-bundle');
 }
 parsed.view.field='unlisted';assert.throws(()=>openLabBundle(JSON.stringify(parsed)),/does not match/);
 parsed.view.field='agl_height_ft';parsed.view.range.lower=null;
 assert.throws(()=>openLabBundle(JSON.stringify(parsed)),/does not match/);
});
