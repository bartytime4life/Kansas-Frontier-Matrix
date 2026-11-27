import test from 'node:test';
import assert from 'node:assert/strict';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';
const {recoveredCollection}=await import(await modelUrl('app/recovered-collections.ts'));
const {collectionMetadata}=await import(await modelUrl('app/collection-metadata.ts'));
const {recordedUnit,recordedReference}=await import(await modelUrl('app/collection-field-dictionary.ts'));
const {profileCollection,measurementDistribution,storyBrief}=await import(await modelUrl('app/collection-lab.ts'));
const {createLabBundle,openLabBundle}=await import(await modelUrl('app/data-lab/lab-bundle.ts'));
const collection=recoveredCollection('observations-usgs-samples-results');
const row=(id,values)=>({id:String(id),values:{file_id:12,row_number:id,...values},provenance:{source_id:'synthetic-sample-completion-QA',source_url:'https://example.org/synthetic',sha256:'a'.repeat(64)}});
const sample=rows=>({rows,pages:1,hasMore:true,answers:[{generatedAt:'2026-11-27T00:00:00Z',cache:{state:'stale',at:'2026-11-26T00:00:00Z'}}]});

test('all 183 captured sample columns have cited definitions and provider aliases without implying source approval',()=>{
 const metadata=collectionMetadata(collection),documents=new Set(metadata.documentation.map(d=>d.id));
 assert.equal(metadata.fields.length,183);assert.equal(metadata.fields.filter(f=>f.definition).length,183);
 assert.equal(metadata.fieldDictionaryRevision,'water-quality-2026-11-27-v2');
 for(const field of metadata.fields){
  assert.ok(field.sources.length&&field.sources.every(id=>documents.has(id)),field.name);
  if(!collection.keys.includes(field.name))assert.ok(field.sourceField,field.name);
  if(field.unitField)assert.ok(collection.columns.includes(field.unitField),field.name);
  if(field.referenceField)assert.ok(collection.columns.includes(field.referenceField),field.name);
 }
 assert.equal(metadata.provenance.reviewCredit,null);assert.equal(metadata.temporal.edition,null);
 assert.equal(metadata.spatial.geometryField,null);assert.equal(metadata.unknowns.some(x=>x.includes('Undocumented field')),false);
});

test('numeric-looking provider identities, plan flags, preparation metadata and source text never become observations',()=>{
 const names=[
  'activity_activity_identifier_user_supplied','result_depth_height_record_identifier_user_supplied','result_data_logger_line',
  'alternate_location_identifier_count','project_qapp_approved','project_qapp_approval_agency','location_state',
  'location_tribal_land_indicator','lab_info_lab_accreditation_indicator','lab_info_taxon_accreditation_indicator',
  'sample_prep_method_identifier_context','lab_sample_prep_method_identifier_context','sample_prep_method_container_label',
  'sample_collection_method_qualifier_type_name','result_statistical_n_value','lab_info_lab_sample_split_ratio',
  'lab_sample_prep_method_dilution_factor','result_attachment_file_download','activity_attachment_file_download',
  'location_description','activity_location_source_map_scale','result_biological_individual_identifier',
 ];
 const p=profileCollection(collection,sample([row(1,Object.fromEntries(names.map(name=>[name,'2'])))]));
 for(const name of names){assert.ok(collection.columns.includes(name),name);assert.deepEqual(p.fields.find(f=>f.name===name).groups,[],name);}
});

test('activity, top and bottom depths keep units and vertical references separate, including missing references',()=>{
 for(const [field,unitField] of [
  ['activity_depth_height_measure','activity_depth_height_measure_unit'],
  ['activity_top_depth_measure','activity_top_depth_measure_unit'],
  ['activity_bottom_depth_measure','activity_bottom_depth_measure_unit'],
 ]){
  const s=sample([row(1,{[field]:'1',[unitField]:'m',activity_bottom_depth_altitude_reference_point:'Water surface'}),
   row(2,{[field]:'9',[unitField]:'m',activity_bottom_depth_altitude_reference_point:'Land surface'}),
   row(3,{[field]:'3',[unitField]:'m'}),row(4,{[field]:'0',[unitField]:'ft',activity_bottom_depth_altitude_reference_point:'Water surface'})]);
  const before=JSON.stringify(s),profile=profileCollection(collection,s),groups=profile.fields.find(f=>f.name===field).groups;
  assert.equal(groups.length,4,field);assert.deepEqual(groups.map(g=>g.mean),[1,9,3,0]);
  assert.equal(JSON.parse(groups[0].context).reference,'Water surface');assert.equal(JSON.parse(groups[1].context).reference,'Land surface');
  assert.equal(JSON.parse(groups[2].context).reference,'Not supplied');
  assert.equal(measurementDistribution(collection,s,field,groups[0].context).count,1);
  assert.equal(recordedUnit(collection.id,field,s.rows[0].values),'m');
  assert.equal(recordedReference(collection.id,field,s.rows[2].values),null);
  assert.equal(JSON.stringify(s),before);
 }
});

test('biological counts and weights keep taxa, tissue, sample media and own units separate',()=>{
 const common={result_biological_group_summary_count:'2',group_summary_weight_measure:'1',group_summary_weight_measure_unit:'g',
  result_biological_taxon:'Synthetic taxon A',activity_media:'Tissue',result_biological_sample_tissue_anatomy:'Whole'};
 const s=sample([row(1,common),row(2,{...common,result_biological_taxon:'Synthetic taxon B'}),
  row(3,{...common,result_biological_sample_tissue_anatomy:'Part'}),row(4,{...common,activity_media:'Sediment'}),
  row(5,{...common,group_summary_weight_measure_unit:'kg'})]);
 const profile=profileCollection(collection,s),weight=profile.fields.find(f=>f.name==='group_summary_weight_measure');
 assert.equal(weight.groups.length,5);assert.equal(profile.fields.find(f=>f.name==='result_biological_group_summary_count').groups.length,4);
 assert.equal(recordedUnit(collection.id,'group_summary_weight_measure',s.rows[0].values),'g');
 assert.equal(recordedUnit(collection.id,'group_summary_weight_measure',{result_measure_unit:'mg/L'}),null);
 assert.equal(recordedUnit(collection.id,'group_summary_weight_measure',Object.create({group_summary_weight_measure_unit:'g'})),null);
});

test('original and standardized coordinates retain separate datums and do not fabricate stored geometry',()=>{
 const values={location_latitude:'38.5',location_longitude:'-98',location_horz_coord_reference_system_datum:'NAD27',
  location_latitude_standardized:'38.50001',location_longitude_standardized:'-98.00001',location_horz_coord_standardized_datum:'NAD83',
  activity_location_latitude:'38.4',activity_location_longitude:'-98.1',activity_location_horz_coord_reference_system_datum:'NAD27',
  activity_location_latitude_standardized:'38.40001',activity_location_longitude_standardized:'-98.10001',activity_location_horz_coord_standardized_datum:'NAD83'};
 const s=sample([row(1,values)]),profile=profileCollection(collection,s);
 for(const name of ['location_latitude','location_longitude','location_latitude_standardized','location_longitude_standardized',
  'activity_location_latitude','activity_location_longitude','activity_location_latitude_standardized','activity_location_longitude_standardized']){
  assert.deepEqual(profile.fields.find(f=>f.name===name).groups,[],name);
  assert.equal(recordedUnit(collection.id,name,values),null);
  assert.equal(recordedReference(collection.id,name,values),name.includes('standardized')?'NAD83':'NAD27');
 }
 assert.equal(profile.spatial.mappable,0);assert.equal(profile.collection.spatial.geometryField,null);
 assert.deepEqual(s.rows[0].values,{file_id:12,row_number:1,...values});
});

test('complete metadata and reference groups round-trip all original text, source credits and source clocks',()=>{
 const s=sample([row(1,{activity_depth_height_measure:'0.00',activity_depth_height_measure_unit:'m',activity_bottom_depth_altitude_reference_point:'Water surface',
  activity_start_time_zone:'CST',activity_end_time_zone:null,lab_info_analysis_start_time:'09:05',lab_sample_prep_method_end_time_zone:'UTC',
  result_measure:'<0.1',result_measure_unit:'mg/L',data_quality_bias_value:'2',result_data_logger_line:'000007'})]);
 const before=JSON.stringify(s),profile=profileCollection(collection,s),bundle=JSON.parse(createLabBundle(collection,s,'Synthetic question',null));
 assert.equal(bundle.profile.collection.fields.filter(f=>f.definition).length,183);
 assert.deepEqual(openLabBundle(JSON.stringify(bundle)).snapshot.rows,s.rows);assert.equal(bundle.profile.credit.aiReview,null);
 for(const name of ['activity_start_time_zone','activity_end_time_zone','lab_info_analysis_start_time','lab_sample_prep_method_end_time_zone']){
  assert.equal(profile.fields.find(f=>f.name===name).role,'time');assert.deepEqual(profile.fields.find(f=>f.name===name).groups,[]);
 }
 assert.match(storyBrief(collection,s,'Question'),/Reference source: each record's activity_bottom_depth_altitude_reference_point/);
 assert.equal(JSON.stringify(s),before);
});

test('a v1 biological-count selection resets rather than carrying a pooled taxon range into v2',()=>{
 const s=sample([row(1,{result_biological_group_summary_count:'2',result_biological_taxon:'Synthetic A'}),
  row(2,{result_biological_group_summary_count:'8',result_biological_taxon:'Synthetic B'})]);
 const saved=JSON.parse(createLabBundle(collection,s,'Preserve the biological question',null));
 saved.fieldDictionaryRevision='water-quality-2026-11-19-v1';
 saved.view={field:'result_biological_group_summary_count',context:'Unit and measurement context not supplied',range:null};
 const opened=openLabBundle(JSON.stringify(saved));
 assert.equal(opened.view,null);assert.match(opened.notice,/USGS sample definitions/);
 assert.deepEqual(opened.snapshot.rows,s.rows);assert.equal(opened.question,'Preserve the biological question');
 const groups=profileCollection(collection,opened.snapshot).fields.find(f=>f.name==='result_biological_group_summary_count').groups;
 assert.equal(groups.length,2);assert.deepEqual(groups.map(g=>g.mean),[2,8]);
});
