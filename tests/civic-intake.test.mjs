import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, writeFile, symlink, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { CIVIC_INTAKE_LIMITS, createCivicIntake, normalizeCivicResearch, readCivicResearchFile } from '../scripts/pc-pipeline/civic-intake.mjs';

const packet = () => ({
  schemaVersion: 1,
  observations: [{ id: 'observation:ks-counties:20261024', sourceId: 'source:ks-counties', title: 'Synthetic county reference fixture', url: 'https://www.census.gov/geographies/reference-files.html', observedAt: '2026-10-24T12:00:00.000Z', evidence: [{ url: 'https://www.census.gov/geographies/reference-files.html', locator: 'Synthetic test reference, not a captured source record' }] }],
  countyReferencePoints: [{ id: 'point:20053', geoid: '20053', name: 'Ellsworth County', longitude: -98.23, latitude: 38.69, observationId: 'observation:ks-counties:20261024' }],
  countyDirectoryCandidates: [{ id: 'directory:20053', geoid: '20053', name: 'Synthetic directory candidate', url: 'https://www.kansas.gov/', observationId: 'observation:ks-counties:20261024' }],
});
function withStore(run) { const store = createCivicIntake(); try { return run(store); } finally { store.close(); } }

test('offline SQLite intake preserves source linkage and always holds all records', () => withStore(store => {
  assert.deepEqual(store.ingest(packet()), { inserted: 3, unchanged: 0, state: 'held', evidenceStatus: 'research_only', releaseEligible: false });
  const snapshot = store.snapshot();
  assert.deepEqual(snapshot.counts, { observations: 1, countyReferencePoints: 1, countyDirectoryCandidates: 1 });
  assert.equal(snapshot.coverage, 'not_assessed');
  assert.equal(snapshot.countyReferencePoints[0].observationId, snapshot.observations[0].id);
  for (const row of [...snapshot.observations, ...snapshot.countyReferencePoints, ...snapshot.countyDirectoryCandidates]) {
    assert.equal(row.state, 'held'); assert.equal(row.evidenceStatus, 'research_only'); assert.equal(row.releaseEligible, false);
    assert.match(row.contentSha256, /^[a-f0-9]{64}$/);
  }
}));

test('canonical identity is deterministic across key order and repeated imports', () => withStore(store => {
  const first = packet(); store.ingest(first);
  const before = store.snapshot();
  const reordered = { ...first };
  reordered.observations = first.observations.map(row => Object.fromEntries(Object.entries(row).reverse()));
  assert.equal(store.ingest(reordered).unchanged, 3);
  assert.deepEqual(store.snapshot(), before);
  withStore(other => { other.ingest(first); assert.deepEqual(other.snapshot(), before); });
}));

test('conflicting identities roll back preceding inserts in the same transaction', () => withStore(store => {
  store.ingest(packet()); const before = store.snapshot();
  const batch = packet();
  batch.observations.unshift({ ...batch.observations[0], id: 'observation:new' });
  batch.countyDirectoryCandidates[0].name = 'Conflicting change';
  assert.throws(() => store.ingest(batch), /CIVIC_IDENTITY_CONFLICT/);
  assert.deepEqual(store.snapshot(), before);
}));

test('duplicate identical rows are idempotent, conflicting rows abort the whole empty import', () => withStore(store => {
  const same = packet(); same.observations.push(structuredClone(same.observations[0]));
  assert.equal(store.ingest(same).unchanged, 1);
  withStore(empty => {
    const conflict = packet(); conflict.observations.push({ ...conflict.observations[0], title: 'Different content' });
    assert.throws(() => empty.ingest(conflict), /CIVIC_IDENTITY_CONFLICT/);
    assert.equal(empty.snapshot().counts.observations, 0);
  });
}));

test('missing evidence references roll back observations and earlier linked rows', () => withStore(store => {
  const batch = packet(); batch.countyDirectoryCandidates[0].observationId = 'observation:missing';
  assert.throws(() => store.ingest(batch), /CIVIC_EVIDENCE_MISSING/);
  assert.deepEqual(store.snapshot().counts, { observations: 0, countyReferencePoints: 0, countyDirectoryCandidates: 0 });
  batch.observations[0].evidence = [];
  assert.throws(() => store.ingest(batch), /CIVIC_EVIDENCE_REQUIRED/);
}));

test('malformed records and attempted publication fields never mutate the store', () => withStore(store => {
  store.ingest(packet()); const before = store.snapshot();
  for (const mutate of [
    p => { p.schemaVersion = 2; },
    p => { p.state = 'published'; },
    p => { p.observations[0].releaseEligible = true; },
    p => { p.countyReferencePoints[0].state = 'published'; },
    p => { p.countyDirectoryCandidates[0].evidenceStatus = 'confirmed'; },
    p => { p.observations[0].id = "x'); DROP TABLE civic_source_observations;--"; },
    p => { p.observations[0].observedAt = '2026-02-30T12:00:00.000Z'; },
    p => { p.countyReferencePoints[0].geoid = '06001'; },
    p => { p.countyReferencePoints[0].latitude = Infinity; },
    p => { p.countyReferencePoints[0].longitude = 181; },
    p => { p.observations[0].title = 'a'.repeat(201); },
  ]) {
    const changed = packet(); mutate(changed);
    assert.throws(() => store.ingest(changed), /CIVIC_/);
    assert.deepEqual(store.snapshot(), before);
  }
}));

test('URLs reject credentials, non-HTTPS, local/IP hosts, unsafe ports and credential query strings', () => {
  for (const hostile of ['http://www.kansas.gov/', 'javascript:alert(1)', 'https://user:pass@www.kansas.gov/', 'https://localhost/', 'https://sub.localhost/', 'https://127.0.0.1/', 'https://2130706433/', 'https://[::1]/', 'https://server.internal/', 'https://www.kansas.gov:8443/', 'https://www.kansas.gov/?api_key=secret', 'https://www.kansas.gov/?access_token=secret', 'https://www.kansas.gov/#access_token=secret', 'https://www.kansas.gov\\@evil.org/']) {
    const changed = packet(); changed.countyDirectoryCandidates[0].url = hostile;
    assert.throws(() => normalizeCivicResearch(changed), /CIVIC_URL/);
  }
  const evidence = packet(); evidence.observations[0].evidence[0].url = 'https://user:secret@www.kansas.gov/';
  assert.throws(() => normalizeCivicResearch(evidence), /CIVIC_URL/);
});

test('SQL-looking display text is stored as data through bound parameters', () => withStore(store => {
  const input = packet(); input.observations[0].title = "O'Brien; DROP TABLE civic_source_observations; --";
  store.ingest(input);
  assert.equal(store.snapshot().observations[0].title, input.observations[0].title);
  assert.equal(store.snapshot().counts.countyDirectoryCandidates, 1);
}));

test('array, byte, accessor and schema bounds reject malformed local JSON shapes', () => {
  const many = packet(); many.observations = Array.from({ length: CIVIC_INTAKE_LIMITS.observations + 1 }, () => packet().observations[0]);
  assert.throws(() => normalizeCivicResearch(many), /CIVIC_LIMIT/);
  const large = packet(); large.observations = Array.from({ length: 400 }, (_, index) => ({ ...packet().observations[0], id: 'observation:' + index, notes: 'x'.repeat(2000) }));
  assert.throws(() => normalizeCivicResearch(large), /CIVIC_LIMIT/);
  const access = packet(); Object.defineProperty(access.observations[0], 'title', { get() { throw new Error('GETTER_MUST_NOT_RUN'); }, enumerable: true });
  assert.throws(() => normalizeCivicResearch(access), /CIVIC_SCHEMA_INVALID/);
  const sparse = packet(); sparse.observations = new Array(1);
  assert.throws(() => normalizeCivicResearch(sparse), /CIVIC_SCHEMA_INVALID/);
});

test('105 reference points do not assert statewide completeness or approve a release', () => withStore(store => {
  const input = packet();
  input.countyReferencePoints = Array.from({ length: 105 }, (_, index) => ({ ...input.countyReferencePoints[0], id: 'point:fixture-' + index }));
  store.ingest(input);
  const snapshot = store.snapshot();
  assert.equal(snapshot.counts.countyReferencePoints, 105);
  assert.equal(snapshot.coverage, 'not_assessed');
  assert.equal(snapshot.releaseEligible, false);
}));

test('explicit file reader rejects symlinks, oversized files, invalid JSON, and relative paths', async () => {
  const root = await mkdtemp(join(tmpdir(), 'kfm-civic-intake-'));
  try {
    const path = join(root, 'research.json'); await writeFile(path, JSON.stringify(packet()));
    assert.equal((await readCivicResearchFile(path)).observations.length, 1);
    const linked = join(root, 'linked.json'); await symlink(path, linked);
    await assert.rejects(readCivicResearchFile(linked));
    await assert.rejects(readCivicResearchFile('research.json'), /CIVIC_PATH_INVALID/);
    await writeFile(path, 'x'.repeat(CIVIC_INTAKE_LIMITS.bytes + 1));
    await assert.rejects(readCivicResearchFile(path), /FILE_LIMIT|CIVIC_LIMIT/);
    await writeFile(path, '{broken'); await assert.rejects(readCivicResearchFile(path), /CIVIC_JSON_INVALID/);
    await writeFile(path, Buffer.from([0xff])); await assert.rejects(readCivicResearchFile(path), /CIVIC_JSON_INVALID/);
  } finally { await rm(root, { recursive: true, force: true }); }
});

test('stores are isolated, cannot accept disk paths, and close safely', () => {
  assert.throws(() => createCivicIntake('/tmp/civic.sqlite'), /CIVIC_OPTIONS_UNSUPPORTED/);
  const first = createCivicIntake(), second = createCivicIntake();
  first.ingest(packet()); assert.equal(second.snapshot().counts.observations, 0);
  first.close(); first.close(); second.close();
  assert.throws(() => first.snapshot(), /CIVIC_CLOSED/);
  assert.throws(() => first.ingest(packet()), /CIVIC_CLOSED/);
});
