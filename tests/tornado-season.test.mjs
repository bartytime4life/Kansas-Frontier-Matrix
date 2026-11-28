import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';
import { PUBLIC_LAB_SNAPSHOTS } from '../app/labs/public-snapshots.mjs';
import { busiestDate, displayRating, mapCoverage, PERIODS, seasonCsv, seasonSettings, summarizeSeason } from '../app/labs/tornado-season/season-model.mjs';

const snapshot = PUBLIC_LAB_SNAPSHOTS['tornado-tracks'];
const { data: { records } } = JSON.parse(readFileSync(new URL(`../public${snapshot.path}`, import.meta.url)));

test('monthly shares count tracks and distinct reported dates with separate denominators', () => {
  const recent = summarizeSeason(records, PERIODS[0]);
  assert.equal(recent.tracks, 1306);
  assert.equal(recent.days, 329);
  assert.equal(recent.aprilJuneTracks, 1052);
  assert.equal(recent.aprilJuneDays, 220);
  assert.deepEqual(busiestDate(recent.months), { date: '2008-05-23', tracks: 68 });
  const all = summarizeSeason(records, PERIODS[2]);
  assert.equal(all.tracks, 4582);
  assert.equal(all.days, 1489);
  assert.equal(all.months.length, 12);
  assert.equal(new Set(all.months.flatMap(month => month.rows.map(row => row.id))).size, all.tracks);
});

test('the map limits location display independently of the count and free export', () => {
  const historical = summarizeSeason(records, PERIODS[1]);
  const cohort = historical.months.flatMap(month => month.rows);
  assert.equal(cohort.length, 3130);
  const coverage = mapCoverage(cohort);
  assert.equal(coverage.starts.length, 3127);
  assert.equal(coverage.paths.length, 1584);
  const outside = cohort.find(row => row.longitude === -90.68);
  assert.ok(outside);
  assert.ok(!coverage.starts.includes(outside));
  const [header, exportRow] = seasonCsv([outside]);
  assert.equal(exportRow[header.indexOf('start_longitude')], -90.68);
  assert.equal(exportRow[header.indexOf('end_latitude')], undefined);
  assert.equal(exportRow[header.indexOf('end_longitude')], undefined);
  assert.equal(displayRating({ date: '2007-01-31', magnitude: 2 }), 'F2');
  assert.equal(displayRating({ date: '2007-02-01', magnitude: 2 }), 'EF2');
  assert.equal(displayRating({ date: '2025-09-14', magnitude: null }), 'Unknown');
});

test('shared period and month settings are bounded and an empty selection has no busiest day', () => {
  assert.deepEqual(seasonSettings({ period: 'all', month: '12', layer: 'lines' }), { period: 'all', month: 12, layer: 'lines' });
  assert.deepEqual(seasonSettings({ period: 'forecast', month: '13', layer: 'unsupported' }), { period: 'recent', month: 0, layer: 'starts' });
  assert.equal(busiestDate(summarizeSeason([], PERIODS[0]).months), null);
});
