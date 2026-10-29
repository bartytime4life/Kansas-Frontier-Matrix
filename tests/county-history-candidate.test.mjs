// Synthetic transport fixtures are NOT historical evidence. Real-report checks
// below are opt-in and use the independently recorded report-byte digest.
import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, writeFile, symlink, mkdir, rm, readFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';
import { canonical, sha, source } from '../server/pipeline-contract.mjs';
import { validateContext } from '../server/pipeline-normalize.mjs';
import { cli } from '../scripts/pc-pipeline/cli.mjs';
import { copyKit } from '../scripts/pc-pipeline/bundle.mjs';
import { adaptCountyHistoryReport as adapt, readCountyHistoryReport as read,
  countyHistoryCalendarView as calendar, countyHistoryDrawerRecord as drawer,
  COUNTY_ARCHIVE_SHA256 as ARCHIVE, COUNTY_REPORT_LIMIT } from '../server/county-history-candidate.mjs';

const shape = 'KS_AtlasHCB/KS_Historical_Counties/KS_Historical_Counties.';
const eventsMember = 'KS_AtlasHCB/KS_Comprehensive_Database/KS_Comprehensive_Database.txt';
const members = [
  [shape+'shp','43026f03b3d1d5a8020c64aa5a17d765687277311e792208c78d3620e98c35b4',3008116],
  [shape+'dbf','25730b7c0ed9bb300f6dd80e833e3c82f95e23b4e8e639fe263f7eeaaefa13ed',260015],
  [eventsMember,'1be56325d28ea82f512d09b8c005e09a20296b0cde6d5f478f9ed1e38bf832e6',232811],
  [shape+'prj','84cf5b9a3c1a444f83ac30ff76f8c5035990223027ba69b2f4d628388adcbd65',167],
  [shape+'shx','ee4c1d945d526da5952e35170cbcfd639ae60ac259529d0e04aca34c01111619',2828],
];
const url = 'https://publications.newberry.org/ahcb/downloads/gis/KS_AtlasHCB.zip';
const id = (kind,...values) => 'urn:kfm:work:county-history:'+sha(JSON.stringify([ARCHIVE,kind,...values]));
const artifacts = n => Object.fromEntries(members.slice(0,n).map(([member,sha256,bytes])=>['sha256:'+sha256,{member,sha256,bytes}]));
const reference = (index,recordNumber) => ({artifactId:'sha256:'+members[index][1],recordNumber,
  locatorKind:index===2?'tsv_data_record_1_based':'shape_dbf_record_1_based'});
function fixture(quarantine=false) {
  const selectedDay='1861-01-29';
  const rows = [1,2].map(n => ({id:id('boundary_version','synthetic_'+n,1,'1861-01-29','1880-01-01'),
    institutionSourceId:'synthetic_'+n,sourceVersion:1,sourceName:'SYNTHETIC '+n,sourceFullName:'Synthetic boundary '+n,
    sourceState:n===1?null:'MO',fips:n===1?null:'29001',sourceCountyType:'County',classificationStatus:'unreviewed_source_label',
    validFrom:'1861-01-29',validToExclusive:'1880-01-01',sourceLastDay:'1879-12-31',change:'Synthetic change, not historical evidence',
    citation:'Synthetic citation, not historical evidence',evidenceRefs:[reference(0,n),reference(1,n),reference(2,n)]}));
  const epoch={validFrom:'1804-10-01',validToExclusive:'2001-01-01',featureCount:2,coverageValid:!quarantine,
    interiorOverlapRecordPairs:quarantine?[[1,2]]:[],invalidEdgeRecordNumbers:quarantine?[1,2]:[]};
  const bundle = {lifecycle:'WORK',sourceUrl:url,archiveSha256:ARCHIVE,artifacts:artifacts(5)};
  const operation = {sourceCrs:'EPSG:4269',targetCrs:'OGC:CRS84',axisOrder:'longitude_latitude',operationId:'EPSG:1188',
    operationAccuracyMetres:4,networkEnabled:false,ballparkAllowed:false,
    sourceProjectionEvidenceRef:{artifactId:'sha256:'+members[3][1],locatorKind:'whole_archive_member'}};
  return {status:'HOLD',releaseEligible:false,qualification:quarantine?'offline_geometry_quarantined_for_selected_day':'offline_geometry_passed_for_selected_day',
    source:{archiveSha256:ARCHIVE,bytes:2131373,url,coverageStart:'1804-10-01',coverageLastDay:'2000-12-31'},
    counts:{boundaryVersions:341},members:members.map(([path,sha256,bytes])=>({path,sha256,bytes})),
    snapshot:{format:'county_history_date_query_v1',lifecycle:'WORK',releaseEligible:false,geometryIncluded:false,selectedDay,
      boundaryVersions:rows,eventOnlyRecordsOnDay:[{id:id('event_only',members[2][1],3),eventDate:selectedDay,institutionSourceId:null,
        sourceName:'',change:'Synthetic event with no institution',citation:'Synthetic event citation',evidenceRefs:[reference(2,3)]}],
      undatedNameCrossReferences:Array.from({length:16},(_,i)=>({id:id('name_cross_reference',members[2][1],100+i),
        targetInstitutionSourceId:'synthetic_1',sourceText:'SYNTHETIC ALIAS '+i,temporalApplicability:'unknown',evidenceRefs:[reference(2,100+i)]})),
      evidenceBundle:{...bundle,artifacts:artifacts(3)}},
    geometryQualification:{format:'county_history_geometry_work_v1',lifecycle:'WORK',releaseEligible:false,selectedDay,
      candidateState:quarantine?'QUARANTINE':'WORK',candidateSha256:'a'.repeat(64),individualSourceInvalid:[],individualTransformedInvalid:[],
      repairs:[],clipping:null,simplification:null,transforms:['EPSG:1188 with longitude/latitude axis order','RFC 7946 ring orientation'],
      sourceCoverageEpochs:[structuredClone(epoch)],transformedCoverageEpochs:[structuredClone(epoch)],selectedEpoch:epoch,coordinateOperation:operation},
    geometryCandidate:quarantine?null:{type:'FeatureCollection',lifecycle:'WORK',releaseEligible:false,selectedDay,evidenceBundle:bundle,coordinateOperation:operation,
      features:rows.map((r,i)=>({type:'Feature',id:r.id,properties:{...r,geometrySha256:'b'.repeat(64)},geometry:{type:'Polygon',
        coordinates:[[[-110+i,42],[-109+i,42],[-109+i,43],[-110+i,43],[-110+i,42]]]}}))}};
}
const encode = value => Buffer.from(JSON.stringify(value));
const adaptFixture = value => {const bytes=encode(value);return adapt(bytes,sha(bytes));};

test('private adapter preserves source identities, optional FIPS, predecessor extent and evidence',()=>{
  const packet=adaptFixture(fixture());
  assert.equal(packet.lifecycle,'WORK');assert.equal(packet.releaseEligible,false);assert.equal(packet.publicClientEligible,false);
  assert.equal(packet.data.features.length,2);assert.equal(packet.eventOnlyRecordsOnDay[0].institutionSourceId,null);
  assert.equal(packet.undatedNameCrossReferences.length,16);
  const missing=packet.records.find(r=>r.institutionSourceId==='synthetic_1');assert.equal(missing.fips,null);assert.equal(missing.sourceState,null);
  assert.ok(packet.data.features.some(f=>f.geometry.coordinates[0][0][0]===-110),'must not clip to modern Kansas');
  for(const r of packet.records)for(const ref of r.evidenceRefs)assert.ok(packet.evidenceBundle.artifacts[ref.artifactId]);
  assert.match(packet.source.limitation,/unreviewed/);assert.equal(packet.calendar.carryForward,false);
});
test('exact selected day is required, even within the reported membership epoch',()=>{
  const packet=adaptFixture(fixture());
  assert.equal(calendar(packet,'1861-01-29').state,'candidate-only');
  for(const day of ['1861-01-28','1861-01-30','1900-01-01'])assert.equal(calendar(packet,day).reason,'SNAPSHOT_NOT_PREPARED');
  for(const day of ['1804-09-30','2001-01-01','2026-10-29'])assert.equal(calendar(packet,day).reason,'OUTSIDE_SOURCE_COVERAGE');
  for(const day of ['18610129','1900-02-29','1861-01-29T00:00:00Z'])assert.throws(()=>calendar(packet,day),/DATE_INVALID/);
});
test('quarantined snapshot retains source inspection but supplies no map geometry',()=>{
  const packet=adaptFixture(fixture(true));
  assert.equal(packet.geometryState,'quarantine');assert.equal(packet.data.features.length,0);
  assert.equal(calendar(packet,'1861-01-29').reason,'QUARANTINED_COVERAGE');
  const record=drawer(packet,packet.records[0].id,'1861-01-29');
  assert.equal(record.geometryState,'held');assert.match(record.citation,/Synthetic/);assert.equal(record.releaseEligible,false);
});
test('source drawer binds exact-day identities and preserves unknown classification',()=>{
  const packet=adaptFixture(fixture()), r=packet.records[0];
  const card=drawer(packet,r.id,'1861-01-29');
  assert.equal(card.validToExclusive,'1880-01-01');assert.equal(card.sourceType,'County');
  assert.equal(card.classificationStatus,'unreviewed_source_label');assert.equal(card.reportSha256,packet.provenance.reportSha256);
  assert.equal(drawer(packet,r.id,'1861-01-30'),null);assert.equal(drawer(packet,'missing','1861-01-29'),null);
  card.evidenceRefs[0].recordNumber=200;assert.notEqual(packet.records[0].evidenceRefs[0].recordNumber,200);
});
test('raw byte digest is external, required and checked before parsing',()=>{
  const bytes=encode(fixture());assert.throws(()=>adapt(bytes),/REPORT_INPUT/);
  assert.throws(()=>adapt(bytes,'0'.repeat(64)),/REPORT_INTEGRITY/);
  assert.throws(()=>adapt(Buffer.concat([bytes,Buffer.from(' ')]),sha(bytes)),/REPORT_INTEGRITY/);
  const invalid=Buffer.from([0xff]);assert.throws(()=>adapt(invalid,sha(invalid)),/REPORT_JSON/);
  const malformed=Buffer.from('{');assert.throws(()=>adapt(malformed,sha(malformed)),/REPORT_JSON/);
  assert.throws(()=>adapt('x'.repeat(COUNTY_REPORT_LIMIT+1),'0'.repeat(64)),/REPORT_LIMIT/);
});
test('Python numeric spelling is preserved by byte provenance without a false JS digest comparison',()=>{
  const raw=JSON.stringify(fixture()).replace('-110,42','-110.0,42.0');
  const packet=adapt(raw,sha(raw));
  assert.equal(packet.provenance.reportSha256,sha(raw));assert.equal(packet.provenance.upstreamCandidateSha256,'a'.repeat(64));
  assert.match(packet.provenance.digestMeaning,/not recomputed/);
  const {adapterSha256,...content}=packet;assert.equal(adapterSha256,sha(canonical(content)));
  assert.notEqual(sha(raw),sha(JSON.stringify(JSON.parse(raw))));
});
test('release claims, wrong source, source-date drift and unqualified geometry are refused',()=>{
  const mutations=[r=>{r.status='APPROVED'},r=>{r.releaseEligible=true},r=>{r.source.archiveSha256='f'.repeat(64)},
    r=>{r.source.url='https://attacker.invalid/'},r=>{r.snapshot.lifecycle='PUBLISHED'},r=>{r.snapshot.releaseEligible=true},
    r=>{r.geometryCandidate.lifecycle='PUBLISHED'},r=>{r.geometryCandidate.selectedDay='1861-01-30'},
    r=>{r.geometryQualification.selectedDay='1861-01-30'},r=>{r.geometryQualification.repairs=['buffer(0)']},
    r=>{r.geometryQualification.individualSourceInvalid=[{recordNumber:1}]},r=>{r.geometryQualification.coordinateOperation.operationId='other'},
    r=>{r.geometryQualification.coordinateOperation.ballparkAllowed=true},r=>{r.geometryQualification.transforms.push('simplify')},
    r=>{r.geometryCandidate.evidenceBundle.artifacts['sha256:'+members[3][1]].bytes++}];
  for(const mutate of mutations){const r=fixture();mutate(r);assert.throws(()=>adaptFixture(r));}
});
test('duplicate/missing features, wrong identity, date and source-property substitution fail',()=>{
  const mutations=[r=>r.geometryCandidate.features.pop(),r=>{r.geometryCandidate.features[1]=r.geometryCandidate.features[0]},
    r=>{r.snapshot.boundaryVersions[0].id='urn:kfm:work:county-history:'+'f'.repeat(64)},
    r=>{r.geometryCandidate.features[0].properties.citation='substituted'},r=>{r.snapshot.boundaryVersions[0].validFrom='1862-01-01'},
    r=>{r.snapshot.boundaryVersions[0].fips=''},r=>{r.snapshot.boundaryVersions[0].classificationStatus='legal_county'}];
  for(const mutate of mutations){const r=fixture();mutate(r);assert.throws(()=>adaptFixture(r));}
});
test('dangling references, missing artifacts, changed members and SHP/DBF record mismatch fail',()=>{
  const mutations=[r=>{r.snapshot.boundaryVersions[0].evidenceRefs[0].artifactId='sha256:'+'f'.repeat(64)},
    r=>{r.snapshot.boundaryVersions[0].evidenceRefs[1].recordNumber=2},r=>{r.snapshot.boundaryVersions[0].evidenceRefs[0].recordNumber=0},
    r=>{r.snapshot.boundaryVersions[0].evidenceRefs[2].recordNumber=946},r=>{r.snapshot.evidenceBundle.artifacts={}},
    r=>{r.members[0].sha256='f'.repeat(64)},r=>{r.members.push({...r.members[0]})},r=>{r.snapshot.boundaryVersions[0].evidenceRefs.pop()}];
  for(const mutate of mutations){const r=fixture();mutate(r);assert.throws(()=>adaptFixture(r));}
});
test('events and aliases cannot turn into open-ended or inferred dated boundaries',()=>{
  for(const mutate of [r=>{r.snapshot.eventOnlyRecordsOnDay[0].eventDate='1861-01-30'},
    r=>{r.snapshot.undatedNameCrossReferences[0].temporalApplicability='1861'},r=>r.snapshot.undatedNameCrossReferences.pop(),
    r=>{r.snapshot.eventOnlyRecordsOnDay.push(r.snapshot.eventOnlyRecordsOnDay[0])}]){
    const r=fixture();mutate(r);assert.throws(()=>adaptFixture(r));
  }
});
test('malformed or unbounded transported geometry fails',()=>{
  for(const change of [g=>{g.type='Point'},g=>{g.coordinates=[]},g=>{g.coordinates[0].pop()},
    g=>{g.coordinates[0][0][0]=181},g=>{g.coordinates[0][0][0]=null},g=>{g.coordinates[0]=Array(100001).fill([-100,38])}]){
    const r=fixture();change(r.geometryCandidate.features[0].geometry);assert.throws(()=>adaptFixture(r));
  }
});
test('changed epoch coverage, source/target disagreement and bypassed quarantine fail',()=>{
  for(const mutate of [r=>{r.geometryQualification.sourceCoverageEpochs[0].validToExclusive='2000-01-01'},
    r=>{r.geometryQualification.transformedCoverageEpochs[0].featureCount=3},r=>{r.geometryQualification.selectedEpoch.featureCount=3},
    r=>{r.geometryQualification.sourceCoverageEpochs[0].interiorOverlapRecordPairs=[[1,2]]},r=>{r.geometryQualification.candidateState='QUARANTINE'}]){
    const r=fixture();mutate(r);assert.throws(()=>adaptFixture(r));
  }
});
test('adapter mutation cannot bypass the calendar hold and returned geometry is detached',()=>{
  const packet=adaptFixture(fixture()),view=calendar(packet,'1861-01-29');
  view.data.features.pop();assert.equal(packet.data.features.length,2);
  for(const mutate of [p=>{p.releaseEligible=true},p=>{p.publicClientEligible=true},p=>{p.selectedDay='1861-01-30'},p=>{p.data.features.pop()}]){
    const p=structuredClone(packet);mutate(p);assert.throws(()=>calendar(p,'1861-01-29'),/ADAPTER_INTEGRITY/);
  }
});
test('unknown fields and URLs do not enter the handoff, and public pipeline rejects it',()=>{
  const r=fixture();r.privateField='KEEP_PRIVATE';r.geometryCandidate.features[0].properties.privateUrl='https://attacker.invalid/';
  const packet=adaptFixture(r);assert.doesNotMatch(canonical(packet),/KEEP_PRIVATE|attacker/);
  assert.throws(()=>source('newberry-ahcb-kansas'),/SOURCE_NOT_ALLOWED/);assert.throws(()=>validateContext(packet),/CONTEXT_INVALID/);
});
test('local report reader and CLI reject unsafe paths, links, size and arguments without network',async t=>{
  const root=await mkdtemp(join(tmpdir(),'kfm-county-adapter-test-'));t.after(()=>rm(root,{recursive:true,force:true}));
  const path=join(root,'report.json'),bytes=encode(fixture());await writeFile(path,bytes);
  const packet=await read(path,sha(bytes));assert.equal(packet.data.features.length,2);
  await symlink(path,join(root,'link.json'));await mkdir(join(root,'folder'));
  await symlink(root,join(root,'parent-link'));
  for(const path of ['relative.json',join(root,'link.json'),join(root,'folder'),join(root,'parent-link','report.json')])await assert.rejects(read(path,sha(bytes)));
  await assert.rejects(cli(['county-history',path]),/COUNTY_HISTORY_USAGE/);
  await assert.rejects(cli(['county-history',path,sha(bytes),'extra']),/COUNTY_HISTORY_USAGE/);
  const old=globalThis.fetch;globalThis.fetch=()=>{throw Error('unexpected network')};
  try{assert.deepEqual(await cli(['county-history',path,sha(bytes)]),packet);}finally{globalThis.fetch=old;}
  const held=encode(fixture(true)),heldPath=join(root,'held.json');await writeFile(heldPath,held);
  const command=await cli(['county-history',heldPath,sha(held)]);
  assert.equal(command.geometryState,'quarantine');assert.equal(command.data.features.length,0);
});

test('installed kit includes the adapter and resolves its complete dependency chain',async t=>{
  const root=await mkdtemp(join(tmpdir(),'kfm-county-installed-test-'));t.after(()=>rm(root,{recursive:true,force:true}));
  await copyKit(root);
  const bytes=encode(fixture()),path=join(root,'report.json');await writeFile(path,bytes);
  const installed=await import(pathToFileURL(join(root,'scripts/pc-pipeline/cli.mjs')).href);
  const packet=await installed.cli(['county-history',path,sha(bytes)]);
  assert.equal(packet.data.features.length,2);assert.equal(packet.publicClientEligible,false);
});

test('exact real statehood report retains all records and cross-language identity',{
  skip:!process.env.KFM_COUNTY_REPORT || !process.env.KFM_COUNTY_REPORT_SHA256,
},async()=>{
  const packet=await read(process.env.KFM_COUNTY_REPORT,process.env.KFM_COUNTY_REPORT_SHA256);
  assert.equal(packet.selectedDay,'1861-01-29');assert.equal(packet.data.features.length,50);
  assert.equal(packet.calendar.coverageEpochs.length,71);assert.equal(packet.calendar.coverageEpochs.filter(e=>!e.coverageValid).length,2);
  assert.equal(packet.eventOnlyRecordsOnDay.length,52);assert.equal(packet.undatedNameCrossReferences.length,16);
  assert.equal(packet.provenance.upstreamCandidateSha256,'17955a7d60e690775b9dc3e90cf7202ce8d216958bfac71973c6e3c926bb5e32');
  const original=JSON.parse(await readFile(process.env.KFM_COUNTY_REPORT,'utf8'));
  assert.deepEqual(new Set(packet.records.map(r=>r.id)),new Set(original.snapshot.boundaryVersions.map(r=>r.id)));
  for(const f of packet.data.features){
    const raw=original.geometryCandidate.features.find(r=>r.id===f.id);assert.deepEqual(f.geometry,raw.geometry);
    assert.equal(f.properties.citation,raw.properties.citation);assert.deepEqual(f.properties.evidenceRefs,raw.properties.evidenceRefs);
    const card=drawer(packet,f.id,'1861-01-29');assert.equal(card.sourceId,raw.properties.institutionSourceId);
    assert.equal(card.releaseEligible,false);
  }
  assert.equal(calendar(packet,'1861-01-30').data.features.length,0);
  assert.throws(()=>validateContext(packet),/CONTEXT_INVALID/);
});
