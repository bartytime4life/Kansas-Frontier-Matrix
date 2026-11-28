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
const categories=['record_type_005a','design_load_031','opr_rating_meth_063','inv_rating_meth_065'];
const qualities=['deck_cond_058','superstructure_cond_059','substructure_cond_060','channel_cond_061','culvert_cond_062',
 'bridge_condition','lowest_rating','structural_eval_067','deck_geometry_eval_068','undclrence_eval_069',
 'posting_eval_070','waterway_eval_071','appr_road_eval_072','fracture_092a','undwater_look_see_092b','spec_inspect_092c'];
const times=['nbi_year','year_built_027','year_reconstructed_106','date_of_inspect_090','fracture_last_date_093a','undwater_last_date_093b','spec_last_date_093c'];
const identities=['file_id','row_number','state_code_001','structure_number_008','county_code_003'];
const row=(id,values={})=>({id,values:{file_id:1,row_number:Number(id),state_code_001:'20',county_code_003:'001',
 structure_number_008:'000000000000001',nbi_year:2025,...Object.fromEntries([...categories,...qualities].map(field=>[field,'4'])),
 date_of_inspect_090:'0325',fracture_last_date_093a:'1123',year_built_027:'1950',year_reconstructed_106:'0000',
 structure_len_mt_049:'20',geometry_geojson:'{"type":"Point","coordinates":[-98,38]}',...values},
 provenance:{source_id:'synthetic-nbi-metadata-QA',source_url:'https://example.org/synthetic-nbi',sha256:'a'.repeat(64)}});
const snapshot=rows=>({rows,pages:1,hasMore:true,answers:[{generatedAt:'2026-11-28T00:00:00Z',cache:{state:'stale',at:'2026-11-27T00:00:00Z'}}]});

test('the expanded legacy NBI dictionary preserves the original field roles, clocks and source identity',()=>{
 const metadata=collectionMetadata(collection),documents=new Set(metadata.documentation.map(source=>source.id));
 assert.equal(metadata.fields.length,147);
 assert.equal(metadata.fields.filter(field=>field.definition).length,89);
 assert.equal(metadata.fieldDictionaryRevision,'nbi-legacy-2026-11-27-v2');
 for(const [role,names] of [['category',categories],['quality',qualities],['time',times],['identity',identities]]){
  for(const name of names){
   const field=metadata.fields.find(field=>field.name===name);
   assert.ok(field,name);assert.equal(field.role,role,name);assert.equal(field.roleBasis,'documented');
   assert.ok(field.definition);assert.ok(field.sources.length&&field.sources.every(id=>documents.has(id)),name);
  }
 }
 assert.deepEqual(metadata.recordIdentity,['file_id','row_number']);
 assert.equal(metadata.temporal.edition,null);assert.equal(metadata.provenance.reviewCredit,null);
 assert.ok(metadata.unknowns.some(value=>value.includes('Undocumented field definitions')));
 assert.equal(documentedField(collection.id,'structure_len_mt_049'),undefined);
 assert.equal(documentedField('observations-other','deck_cond_058'),undefined);
 assert.equal(fieldRole('deck_geometry_eval_068',[],collection.id),'quality');
 assert.equal(fieldRole('deck_geometry_eval_068',[],'observations-other'),'location');
 assert.equal(fieldRole('deck_cond_058',['deck_cond_058'],collection.id),'identity');
});

test('numeric condition, appraisal and load codes cannot become measurements, distributions or layers',()=>{
 const s=snapshot([row('1'),row('2',{deck_cond_058:'0',design_load_031:'0',lowest_rating:0})]),before=JSON.stringify(s);
 const profile=profileCollection(collection,s);
 for(const name of [...categories,...qualities,...times,...identities]){
  assert.deepEqual(profile.fields.find(field=>field.name===name).groups,[],name);
  assert.deepEqual(measurementContexts(collection,s,name),[],name);
  assert.deepEqual(measurementDistribution(collection,s,name,'Unit and measurement context not supplied'),{count:0,bins:[]},name);
 }
 assert.throws(()=>measurementLayer(collection,s,'deck_cond_058','Unit and measurement context not supplied'),/measurement field/);
 const length=profile.fields.find(field=>field.name==='structure_len_mt_049');
 assert.equal(length.groups[0].count,2);assert.equal(length.groups[0].mean,20);
 assert.equal(recordedUnit(collection.id,'operating_rating_064',{}),null,'method categories do not assign units to rating values');
 assert.equal(JSON.stringify(s),before);
});

test('raw zero, N/A, unknown codes, encoded dates and leading-zero IDs survive a complete bundle roundtrip',()=>{
 const s=snapshot([row('1',{deck_cond_058:'0',superstructure_cond_059:'N',channel_cond_061:'Z',design_load_031:'0',
  opr_rating_meth_063:'A',date_of_inspect_090:'0325',fracture_last_date_093a:'0000',bridge_condition:'X'}),
  row('2',{deck_cond_058:'N',culvert_cond_062:'N',design_load_031:'C',state_code_001:'020',date_of_inspect_090:'424'})]);
 const before=JSON.stringify(s),bundle=JSON.parse(createLabBundle(collection,s,'Inspect the archived codes',null));
 const reopened=openLabBundle(JSON.stringify(bundle));
 assert.deepEqual(reopened.snapshot.rows,s.rows);assert.deepEqual(reopened.snapshot.answers,s.answers);
 assert.equal(reopened.question,'Inspect the archived codes');assert.equal(reopened.notice,null);
 assert.equal(bundle.profile.credit.aiReview,null);assert.equal(bundle.profile.collection.provenance.reviewCredit,null);
 assert.equal(bundle.fieldDictionaryRevision,'nbi-legacy-2026-11-27-v2');
 assert.match(documentedField(collection.id,'date_of_inspect_090').encoding,/^MMYY; century not supplied$/);
 for(const code of ['Z','05','__proto__','constructor'])assert.equal(documentedCode(collection.id,'deck_cond_058',code),null);
 assert.equal(JSON.stringify(s),before);
});

test('edition-sensitive load codes and item-specific condition/appraisal meanings stay distinct',()=>{
 const load=documentedCode(collection.id,'design_load_031','0');
 assert.match(load,/1995.*Other or Unknown/);assert.match(load,/2011.*Unknown/);
 assert.match(documentedCode(collection.id,'design_load_031','9'),/2011.*greater loads/);
 assert.match(documentedCode(collection.id,'opr_rating_meth_063','A'),/Assigned.*metric tons/);
 assert.notEqual(documentedCode(collection.id,'deck_cond_058','N'),documentedCode(collection.id,'channel_cond_061','N'));
 assert.notEqual(documentedCode(collection.id,'deck_cond_058','N'),documentedCode(collection.id,'culvert_cond_062','N'));
 assert.match(documentedCode(collection.id,'structural_eval_067','0'),/without actual closure/);
 assert.match(documentedField(collection.id,'waterway_eval_071').definition,/functional-class/);
 assert.match(documentedField(collection.id,'lowest_rating').definition,/channel item 61 is excluded/);
 assert.equal(documentedCode(collection.id,'waterway_eval_071','5'),null,'no invented generic condition label for an item-specific functional-class table');
 assert.match(documentedCode(collection.id,'record_type_005a','2'),/Single route/);
 assert.match(documentedCode(collection.id,'record_type_005a','A'),/record 1 .*multiple-route/);
 assert.match(documentedCode(collection.id,'record_type_005a','Z'),/record 26 .*multiple-route/);
 assert.equal(documentedCode(collection.id,'record_type_005a','a'),null,'provider route codes remain case-sensitive');
 for(const code of ['0','6','7','8'])assert.match(documentedCode(collection.id,'opr_rating_meth_063',code),/added February 2011/);
});

test('metadata API and story briefs carry legacy scope and code definitions without a safety or AI-review decision',async()=>{
 const response=GET(new Request('https://example.org/api/collection-metadata?collection='+collection.id)),body=await response.json();
 assert.equal(response.status,200);assert.equal(body.collections[0].fields.filter(field=>field.definition).length,89);
 assert.ok(body.collections[0].documentation.some(source=>source.url.includes('fhwa.dot.gov')));
 const brief=storyBrief(collection,snapshot([row('1')]),'Which recorded codes need edition checks?');
 assert.match(brief,/Field definitions and units/);assert.match(brief,/MMYY/);
 assert.match(brief,/legacy|Legacy/);assert.match(brief,/No AI review or approval/);
 assert.equal(/^\- deck_cond_058 \(/m.test(brief),false,'no numeric range for a condition code');
 assert.equal(GET(new Request('https://example.org/api/collection-metadata?collection='+collection.id+'&sql=anything')).status,400);
});
