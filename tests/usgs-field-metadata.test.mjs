import test from 'node:test';
import assert from 'node:assert/strict';
import {modelUrl} from '../scripts/lib/typescript-model.mjs';
const {recoveredCollection}=await import(await modelUrl('app/recovered-collections.ts'));
const {collectionMetadata}=await import(await modelUrl('app/collection-metadata.ts'));
const {recordedUnit,documentedCode}=await import(await modelUrl('app/collection-field-dictionary.ts'));
const {profileCollection,measurementDistribution,measurementLayer,storyBrief}=await import(await modelUrl('app/collection-lab.ts'));
const {createLabBundle,openLabBundle}=await import(await modelUrl('app/data-lab/lab-bundle.ts'));
const daily=recoveredCollection('observations-usgs-daily-values');
const field=recoveredCollection('observations-usgs-field-measurements');
const peaks=recoveredCollection('observations-usgs-peaks');
const row=(id,patch={})=>({id,values:{file_id:1,row_number:Number(id),value:'0.00',unit_of_measure:'ft',parameter_code:'72019',
 kind:'groundwater_level',reading_type:'ReferencePrimary',vertical_datum:'Local Assumed Datum',approval_status:'Approved',qualifier:'Static',
 time:'2020-01-01',last_modified:'2026-11-18T00:00:00Z',...patch},provenance:{source_id:'synthetic-usgs-qa'}});
const sample=rows=>({rows,pages:1,hasMore:true,answers:[{generatedAt:'2026-11-18T12:00:00Z'}]});
const oldFieldDimensions=['parameter_code','unit_of_measure','kind','reading_type','vertical_datum','approval_status','qualifier'];
const oldContext=values=>JSON.stringify(Object.fromEntries(oldFieldDimensions.map(k=>[k,String(values[k])])));

test('54 water fields have source-backed definitions with per-row rather than guessed units',()=>{
 assert.equal([daily,field,peaks].reduce((n,c)=>n+collectionMetadata(c).fields.length,0),54);
 for(const c of [daily,field,peaks]){
  const m=collectionMetadata(c),sources=new Set(m.documentation.map(d=>d.id));
  for(const f of m.fields){assert.ok(f.definition,f.name);assert.ok(f.sources.length);assert.ok(f.sources.every(id=>sources.has(id)));}
  assert.equal(m.fields.find(f=>f.name==='value').unit,null);
  assert.equal(m.fields.find(f=>f.name==='value').unitField,'unit_of_measure');
  assert.equal(m.temporal.edition,null);assert.equal(m.provenance.reviewCredit,null);
  assert.match(m.fields.find(f=>f.name==='last_modified').definition,/refresh need not indicate a changed observation/);
  assert.equal(m.documentation[0].sha256.length,64);
 }
 assert.equal(documentedCode(daily.id,'statistic_id','00003'),'Mean');
 assert.equal(documentedCode(daily.id,'approval_status','Provisional'),'USGS provisional; subject to revision');
 assert.equal(documentedCode(daily.id,'approval_status','toString'),null);
 assert.deepEqual(collectionMetadata(recoveredCollection('observations-usgs-sites')).documentation,[]);
});

test('peak comparison years, partial dates and measurement-quality codes are not numeric observations',()=>{
 const s=sample([row('1',{peak_since:'1907',water_year:2020,year:'2019',month:null,day:null,time_of_day:null,measurement_rated:'2'})]);
 const p=profileCollection(peaks,s);
 for(const name of ['peak_since','water_year','year','month','day','time_of_day','last_modified']){
  const f=p.fields.find(f=>f.name===name);assert.equal(f.role,'time');assert.deepEqual(f.groups,[],name);
 }
 assert.deepEqual(profileCollection(field,s).fields.find(f=>f.name==='measurement_rated').groups,[]);
 assert.equal(s.rows[0].values.month,null);assert.equal(s.rows[0].values.value,'0.00');
});

test('field measurements keep methods, ratings, locations, agencies and conditions separate',()=>{
 const baseline={observing_procedure_code:'A',observing_procedure:'Synthetic method',sublocation_identifier:'one',
  measuring_agency:'QA',control_condition:'clear',measurement_rated:'Good'};
 const rows=[row('1',baseline),row('2',{...baseline,value:'2.00'}),
  ...Object.keys(baseline).map((key,i)=>row(String(i+3),{...baseline,[key]:'Other',value:'10.00'}))];
 const s=sample(rows),p=profileCollection(field,s),v=p.fields.find(f=>f.name==='value');
 assert.equal(v.groups.length,7);assert.equal(v.groups[0].count,2);assert.equal(v.groups[0].mean,1);
 const context=JSON.parse(v.groups[0].context);for(const [k,value] of Object.entries(baseline))assert.equal(context[k],value);
 assert.equal(measurementDistribution(field,s,'value',v.groups[0].context).count,2);
 for(const name of ['kind','reading_type','vertical_datum','measurement_rated','observing_procedure_code'])assert.deepEqual(p.fields.find(f=>f.name===name).groups,[]);
});

test('units stay literal and unknown units are not inferred from parameter codes',()=>{
 const s=sample([row('1',{unit_of_measure:'ft^3/s',parameter_code:'00060'}),row('2',{unit_of_measure:'m^3/s',parameter_code:'00060'}),
  row('3',{unit_of_measure:null,parameter_code:'00060'})]);
 const v=profileCollection(daily,s).fields.find(f=>f.name==='value');assert.equal(v.groups.length,3);
 assert.equal(recordedUnit(daily.id,'value',s.rows[0].values),'ft^3/s');
 assert.equal(recordedUnit(daily.id,'value',s.rows[1].values),'m^3/s');
 assert.equal(recordedUnit(daily.id,'value',s.rows[2].values),null);
 assert.equal(recordedUnit(daily.id,'value',Object.create({unit_of_measure:'ft'})),null);
 assert.equal(recordedUnit('observations-faa-obstacles','agl_height_ft',{}),'ft');
});

test('peak periods remain distinct and dynamic units accompany geometry derivatives when geometry exists',()=>{
 const s=sample([row('1',{peak_since:null}),row('2',{peak_since:'1907'}),row('3',{peak_since:'1950'})]);
 const v=profileCollection(peaks,s).fields.find(f=>f.name==='value');assert.equal(v.groups.length,3);
 const c={...daily,geometry:'geometry_geojson'};
 const source=sample([row('1',{geometry_geojson:'{"type":"Point","coordinates":[-98,38]}'})]);
 const before=JSON.stringify(source.rows),context=profileCollection(c,source).fields.find(f=>f.name==='value').groups[0].context;
 const layer=measurementLayer(c,source,'value',context);
 assert.equal(layer.features[0].properties.unit,'ft');assert.equal(layer.features[0].properties.reference,null);
 assert.equal(layer.kfm.fieldDefinition.unitField,'unit_of_measure');assert.equal(layer.kfm.reviewCredit,null);
 assert.equal(JSON.stringify(source.rows),before);
 const brief=storyBrief(c,source,'Synthetic QA question');assert.match(brief,/Unit source: each record's unit_of_measure/);
 assert.match(brief,/record-refresh time/);assert.match(brief,/No AI review or approval/);
});

test('older pooled field contexts reopen unchanged records with a reset notice while daily views stay intact',()=>{
 const s=sample([row('1',{observing_procedure_code:'A'}),row('2',{observing_procedure_code:'B'})]);
 const bundle=JSON.parse(createLabBundle(field,s,'Original question',null));delete bundle.fieldDictionaryRevision;
 bundle.view={field:'value',context:oldContext(s.rows[0].values),range:null};
 const reopened=openLabBundle(JSON.stringify(bundle));assert.deepEqual(reopened.snapshot.rows,s.rows);
 assert.equal(reopened.question,'Original question');assert.equal(reopened.view,null);assert.match(reopened.notice,/USGS field definitions have changed/);
 bundle.view.context='other unit';assert.throws(()=>openLabBundle(JSON.stringify(bundle)),/does not match/);
 const dailyBundle=JSON.parse(createLabBundle(daily,s,'Daily question',null));const view=dailyBundle.view;delete dailyBundle.fieldDictionaryRevision;
 assert.deepEqual(openLabBundle(JSON.stringify(dailyBundle)).view,view);
});

test('new documented contexts reopen exactly and reject modified views rather than using legacy upgrades',()=>{
 const s=sample([row('1',{observing_procedure_code:'A'})]);const bundle=JSON.parse(createLabBundle(field,s,'Question',null));
 assert.equal(bundle.fieldDictionaryRevision,'usgs-field-measurements-2026-11-18-v1');
 assert.deepEqual(openLabBundle(JSON.stringify(bundle)).view,bundle.view);
 bundle.view.context=oldContext(s.rows[0].values);assert.throws(()=>openLabBundle(JSON.stringify(bundle)),/does not match/);
 const peakBundle=JSON.parse(createLabBundle(peaks,s,'Question',null));delete peakBundle.fieldDictionaryRevision;
 peakBundle.view={field:'peak_since',context:'Unit and measurement context not supplied',range:null};
 assert.equal(openLabBundle(JSON.stringify(peakBundle)).view,null);
 peakBundle.view.range={lower:null,upper:100,includeUpper:true};assert.throws(()=>openLabBundle(JSON.stringify(peakBundle)),/does not match/);
});
