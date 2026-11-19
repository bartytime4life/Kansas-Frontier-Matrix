import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { BRIDGE_LAB_SNAPSHOTS } from '../app/labs/bridge-snapshots.mjs';
import { recordModel, filterRecords, recordsCSV } from '../app/living-welcome/stories/record-model.mjs';
import { validStoryBundle, storyBundleByteLimit, storyRecordLimit } from '../app/living-welcome/stories/story-bundle.mjs';
const snapshot = BRIDGE_LAB_SNAPSHOTS['built-kansas'];
const bundle = JSON.parse(await readFile(new URL('../public' + snapshot.path, import.meta.url)));
test('KDOT snapshot retains every enumerated source row, including repeated source identifiers', () => {
  const { records, sourceCounts } = bundle.data;
  assert.equal(records.length, 24877);
  assert.equal(new Set(records.map(row => row.id)).size, records.length);
  assert.equal(sourceCounts.reduce((n, source) => n + source.sourceRecords, 0), records.length);
  for (const source of sourceCounts) assert.equal(source.returnedRecords, source.sourceRecords);
  assert.equal(sourceCounts[0].sourceRecords - sourceCounts[0].uniqueObjectIds, 4);
  assert.equal(records.filter(row => row.year === null).length, 27);
  assert.ok(bundle.data.limits.some(text => text.includes('not unique physical bridges')));
  assert.equal(validStoryBundle(bundle, 'built-kansas'), true);
});
test('larger bridge limits are explicit and cannot expand an unrelated instrument', () => {
  assert.equal(storyBundleByteLimit('built-kansas'), 16000000);
  assert.equal(storyRecordLimit('built-kansas'), 40000);
  assert.equal(storyBundleByteLimit('census-mosaic'), 3000000);
  assert.equal(storyRecordLimit('__proto__'), 10000);
  assert.equal(validStoryBundle({ ...bundle, story: 'census-mosaic' }, 'census-mosaic'), false);
});
test('bridge year selection never assigns a construction year to undated records', () => {
  const model = recordModel(bundle);
  const early = filterRecords(model, { time: 1900 });
  assert.ok(early.length > 0 && early.length < model.records.length);
  assert.ok(early.every(row => row.year !== null && row.year <= 1900));
  assert.equal(filterRecords(model, { time: model.last }).length, model.records.length);
  assert.ok(filterRecords(model, { controls: { category: 'Local road' } }).every(row => row.network === 'Local road'));
});
test('a public inventory CSV binds the shipping file without repeating every acquisition receipt per row', () => {
  const csv = recordsCSV(bundle, { controls: { to: 1900 }, snapshotSha256: snapshot.sha256 });
  assert.ok(csv.rows.length > 1);
  assert.equal(csv.rows[0].at(-1), 'snapshot_sha256');
  for (const row of csv.rows.slice(1)) {
    assert.equal(row.at(-1), snapshot.sha256);
    assert.equal(row.at(-2), bundle.built_at);
  }
});
