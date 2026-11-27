import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';
import { PUBLIC_LAB_SNAPSHOTS } from '../app/labs/public-snapshots.mjs';
import { catalogCsv, catalogSettings, catalogWindow, compareCatalog, PERIODS } from '../app/labs/earthquakes/catalog-model.mjs';

const snapshot = PUBLIC_LAB_SNAPSHOTS['shaking-ground'];
const { data: { records, sourceSnapshot } } = JSON.parse(readFileSync(new URL(`../public${snapshot.path}`, import.meta.url)));
const window = catalogWindow(sourceSnapshot.url);

test('earthquake rates use an inclusive threshold and four full UTC calendar years', () => {
  const [first, second] = compareCatalog(records, [PERIODS[1], PERIODS[3]], 2.5, window);
  assert.deepEqual(first.years.map(year => year.count), [378, 706, 294, 215]);
  assert.deepEqual(second.years.map(year => year.count), [47, 29, 15, 67]);
  assert.equal(first.perYear, 398.25);
  assert.equal(second.perYear, 39.5);
  assert.equal(first.selected.length, 1593);
  assert.equal(second.selected.length, 158);
  assert.ok(first.selected.some(row => row.magnitude === 2.5));
  for (const { curve, selected, medianDepth } of [first, second]) {
    assert.equal(medianDepth, 5);
    assert.ok(selected.every(row => row.magnitude >= 2.5));
    assert.ok(curve.every((point, index) => index === 0 || point.perYear <= curve[index - 1].perYear));
    assert.equal(curve.find(point => point.mag === 4.5).perYear, .25);
    assert.equal(curve.at(-1).perYear, 0);
  }
  const rows = catalogCsv([first, second]);
  assert.equal(rows.length, 1752);
  assert.equal(new Set(rows.slice(1).map(row => row[1])).size, 1751);
  assert.ok(rows.slice(1).every(row => row[5] && row.at(-1).startsWith('https://earthquake.usgs.gov/earthquakes/eventpage/')));
});

test('partial source coverage is not a rate and a zero depth remains a value', () => {
  const early = PERIODS[0];
  const [uncovered] = compareCatalog(records, [early], 1, { start: '2010-01-02', end: '2014-01-01' });
  const [partial] = compareCatalog(records, [early], 1, { start: '2010-01-01', end: '2013-12-31' });
  assert.equal(uncovered, null);
  assert.equal(partial, null);
  const zero = { id: 'a', magnitude: 2, year: 2012, longitude: -98, latitude: 38, depth: 0 };
  const noDepth = { ...zero, id: 'b', depth: null };
  const [result] = compareCatalog([zero, noDepth], [early], 2, window);
  assert.deepEqual(result.years.map(year => year.count), [0, 0, 2, 0]);
  assert.equal(result.medianDepth, 0);
  assert.equal(result.depthCount, 1);
  const [empty] = compareCatalog([zero, noDepth], [early], 5, window);
  assert.equal(empty.perYear, 0);
  assert.equal(empty.medianDepth, null);
});

test('shared comparisons fall back to distinct valid periods and bounded thresholds', () => {
  assert.deepEqual(catalogSettings(), { first: '2014', second: '2022', mag: 2.5 });
  assert.deepEqual(catalogSettings({ first: '2022', second: '2022', mag: '-1' }), { first: '2022', second: '2018', mag: 2.5 });
  assert.deepEqual(catalogSettings({ first: '2018', second: '2010', mag: '3.333' }), { first: '2018', second: '2010', mag: 3.3 });
  assert.equal(catalogWindow('unknown'), null);
  assert.deepEqual(window, { start: '2010-01-01', end: '2026-11-16' });
});
