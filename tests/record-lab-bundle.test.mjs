import assert from 'node:assert/strict';
import test from 'node:test';
import { modelUrl } from '../scripts/lib/typescript-model.mjs';

const { createLabBundle, openLabBundle } = await import(await modelUrl('app/data-lab/lab-bundle.ts'));
const { recoveredCollection } = await import(await modelUrl('app/recovered-collections.ts'));
const { measurementDistribution, profileCollection } = await import(await modelUrl('app/collection-lab.ts'));
const collection = recoveredCollection('observations-usgs-daily-values');
const values = { parameter_code: '00060', unit_of_measure: 'ft3/s', statistic_id: '00003' };
const rows = [1, 3, 5, 10].map((value, index) => ({
  id: `fixture-${index}`, values: { ...values, value }, provenance: { source_id: 'fixture' },
}));
const snapshot = {
  rows, pages: 1, hasMore: true,
  answers: [{ generatedAt: '2026-11-17T12:00:00Z', source: { provider: 'Fixture' }, rows, cache: { state: 'stale', at: '2026-11-16T00:00:00Z' } }],
};
const question = 'What changed in this reach?';
const profile = profileCollection(collection, snapshot);
const context = profile.fields.find(field => field.name === 'value').groups[0].context;
const [{ lower, upper, includeUpper }] = measurementDistribution(collection, snapshot, 'value', context).bins;
const view = { field: 'value', context, range: { lower, upper, includeUpper } };

test('Record Lab bundle reopens source rows, read receipts, question and exact selected range', () => {
  const exported = createLabBundle(collection, snapshot, question, view, profile);
  const parsed = JSON.parse(exported);
  assert.deepEqual(parsed.records, rows);
  assert.ok(!Object.hasOwn(parsed.capture.reads[0], 'rows'));
  assert.match(parsed.brief, /What changed in this reach/);
  const saved = openLabBundle(exported);
  assert.equal(saved.collection.id, collection.id);
  assert.deepEqual(saved.snapshot.rows, rows);
  assert.deepEqual(saved.view, view);
  assert.equal(saved.question, question);
  assert.equal(saved.snapshot.hasMore, true);
  const restored = profileCollection(collection, saved.snapshot);
  assert.deepEqual(restored.fields, profile.fields);
  assert.deepEqual(restored.provenance, profile.provenance);
  assert.deepEqual(restored.sample.retrievedAt, profile.sample.retrievedAt);
  assert.equal(restored.sample.inputOrigin, 'saved-bundle');
  assert.match(JSON.parse(createLabBundle(collection, saved.snapshot, question, saved.view)).brief, /user-supplied file/);
});

test('Record Lab opens prior JSON downloads and saves the default measurement on new downloads', () => {
  const legacy = openLabBundle(JSON.stringify({ profile, question, records: rows, brief: 'An old export' }));
  assert.deepEqual(legacy.snapshot.rows, rows);
  assert.equal(legacy.view, null);
  assert.equal(profileCollection(collection, legacy.snapshot).sample.stale, true);
  assert.deepEqual(openLabBundle(createLabBundle(collection, snapshot, question, null)).view, { field: 'value', context, range: null });
});

test('Record Lab rejects foreign collections, duplicate identities and altered ranges without reinterpreting them', () => {
  const parsed = JSON.parse(createLabBundle(collection, snapshot, question, view));
  const open = input => openLabBundle(JSON.stringify(input));
  assert.throws(() => open({ ...parsed, collection: 'unlisted' }), /unknown collection/);
  assert.throws(() => open({ ...parsed, records: [rows[0], rows[0]] }), /repeated record identity/);
  assert.throws(() => open({ ...parsed, capture: { ...parsed.capture, reads: [] } }), /every captured read/);
  assert.throws(() => open({ ...parsed, view: { ...view, context: 'other unit' } }), /does not match/);
  assert.throws(() => open({ ...parsed, view: { ...view, range: { ...view.range, upper: 999 } } }), /does not match/);
  const nonFinite = JSON.stringify({ ...parsed, view: null, records: [{ id: 'unexpected-value', values: { value: 'non-finite-marker' } }] })
    .replace('"non-finite-marker"', '1e999');
  assert.throws(() => openLabBundle(nonFinite), /could not be read/);
});
