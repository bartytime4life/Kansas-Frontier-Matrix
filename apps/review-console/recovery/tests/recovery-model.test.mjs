import test from 'node:test';
import assert from 'node:assert/strict';
import { newWorkspace, blankRun, validateRecord, gapsFor, isSupported, parseWorkspace, mergeImport, safeUrl, latestAfterRun, supportedFeedCount } from '../src/recovery-model.ts';

const observedAt = '2026-11-08T20:00:00Z';
function completeWorkspace() {
  const w = newWorkspace();
  const types = ['release identity', 'database preservation', 'read-only status', 'journal', 'provider response', 'backfill receipt'];
  w.evidence = types.map((type, i) => ({id:`e-${i}`,type,title:`QA evidence ${type}`,observedAt,reference:'local QA fixture',excerpt:'Synthetic review evidence, never an operational receipt.',sha256:'',scope:'Synthetic model test',limitations:'No actual provider or machine inspected.',createdAt:observedAt}));
  const record = {...blankRun(), runId:'QA-RUN-1', observedAt, release:'sql-feeds-QA', commit:'205e344ea8d05077414d3a0f8606512b66272be5', catalogIdentity:'iem-wind-observations', readOnly:'confirmed read-only',journal:'QA journal excerpt',providerResponse:'QA: HTTP_429 followed by HTTP_200',retryAfter:'60',attempts:'3',actualWaits:'60,120',waitedSeconds:'180',outcome:'completed',cursorBefore:'2003/01/0',cursorAfter:'2003/02/0',rowsRetained:'12',rowsLoaded:'4',rowsUnchanged:'8',rowsPending:'100',receipt:'QA-RECEIPT',retest:'QA independent resume result',evidenceIds:w.evidence.map(e=>e.id)};
  w.runs = [{id:record.runId,revisions:[{revision:1,savedAt:observedAt,record}]}];
  w.decisions = [{id:'QA-DECISION',runId:record.runId,revision:1,reviewer:'QA synthetic reviewer',decision:'accepted for stated scope',scope:'Recovery assessment',rationale:'Synthetic test of complete gate.',evidenceIds:record.evidenceIds,retest:'QA test only',createdAt:observedAt}];
  return w;
}

test('merged source baseline contains no machine or execution attestations', () => {
  const w = newWorkspace();
  assert.equal(w.runs.length, 0);
  assert.equal(w.decisions.length, 0);
  const run = {id:'QA',revisions:[{revision:1,savedAt:observedAt,record:{...blankRun(),runId:'QA',observedAt,outcome:'completed'}}]};
  assert.ok(gapsFor(w,run).length >= 5);
  assert.equal(isSupported(w,run),false);
});

test('review applies only to its exact run revision and stated scope', () => {
  const w = completeWorkspace();
  assert.equal(gapsFor(w,w.runs[0]).length,0);
  assert.equal(isSupported(w,w.runs[0]),true);
  w.decisions[0].scope = 'Release identity';
  assert.equal(isSupported(w,w.runs[0]),false);
  w.decisions[0].scope = 'Recovery assessment';
  w.runs[0].revisions.push({revision:2,savedAt:observedAt,record:{...w.runs[0].revisions[0].record,providerResponse:'Corrected response'}});
  assert.equal(isSupported(w,w.runs[0]),false);
  assert.equal(w.runs[0].revisions[0].record.providerResponse,'QA: HTTP_429 followed by HTTP_200');
});

test('accepted failed execution does not imply recovered feed', () => {
  const w = completeWorkspace();
  w.runs[0].revisions[0].record.outcome = 'failed';
  assert.equal(isSupported(w,w.runs[0]),false);
});

test('import retains historical review notes and requires a fresh local decision', () => {
  const incoming = parseWorkspace(JSON.stringify(completeWorkspace()));
  const w = mergeImport(newWorkspace(),incoming);
  assert.equal(w.runs[0].imported,true);
  assert.equal(w.decisions.length,0);
  assert.equal(isSupported(w,w.runs[0]),false);
  assert.match(w.importHistory[0].note,/QA-DECISION/);
});

test('import rejects collisions and missing evidence references without replacing records', () => {
  const w = completeWorkspace();
  const before = JSON.stringify(w);
  assert.throws(()=>mergeImport(w,completeWorkspace()),/conflict/i);
  assert.equal(JSON.stringify(w),before);
  const orphan = completeWorkspace();
  orphan.runs[0].revisions[0].record.evidenceIds.push('missing');
  assert.throws(()=>parseWorkspace(JSON.stringify(orphan)),/missing or invalid evidence/);
});

test('invalid numbers and normalized impossible dates cannot become recorded evidence', () => {
  const r = {...blankRun(),runId:'QA',observedAt};
  assert.deepEqual(validateRecord(r),[]);
  for (const value of ['-1','Infinity','NaN','1e10000']) assert.ok(validateRecord({...r,attempts:value}).length);
  assert.ok(validateRecord({...r,observedAt:'2026-02-30T20:00:00Z'}).length);
  assert.ok(validateRecord({...r,attempts:'1.5'}).length);
  assert.deepEqual(validateRecord({...r,attempts:'0',rowsLoaded:'0'}),[]);
});

test('references cannot turn pasted content into active scripts', () => {
  assert.equal(safeUrl('javascript:alert(1)'),undefined);
  assert.equal(safeUrl('data:text/html,<script>alert(1)</script>'),undefined);
  assert.equal(safeUrl('/local/journal.txt'),undefined);
  const w = completeWorkspace();
  w.evidence[0].reference = 'javascript:alert(1)';
  assert.throws(()=>parseWorkspace(JSON.stringify(w)),/reference/);
});

test('contradictory wait totals require correction and over-budget observations stay unverified', () => {
  const w = completeWorkspace();
  const r = w.runs[0].revisions[0].record;
  assert.ok(validateRecord({...r,waitedSeconds:'90'}).length,'60 + 120 cannot be recorded as 90 seconds');
  r.actualWaits = '3000';
  r.waitedSeconds = '3000';
  assert.equal(isSupported(w,w.runs[0]),false,'an observed budget violation may be recorded but cannot support bounded recovery');
});

test('a later adverse retest reopens a feed gap while preserving its earlier assessment', () => {
  const w = completeWorkspace();
  assert.equal(supportedFeedCount(w),1);
  const laterRecord = {...w.runs[0].revisions[0].record,runId:'QA-LATER-FAILURE',observedAt:'2026-11-08T21:00:00Z',outcome:'failed'};
  w.runs.unshift({id:laterRecord.runId,revisions:[{revision:1,savedAt:'2026-11-08T21:01:00Z',record:laterRecord}]});
  assert.equal(latestAfterRun(w,'iem').id,'QA-LATER-FAILURE','ordering follows observed UTC time, not insertion order');
  assert.equal(supportedFeedCount(w),0);
  assert.equal(w.decisions[0].decision,'accepted for stated scope');
});
