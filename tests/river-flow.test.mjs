import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { PUBLIC_LAB_SNAPSHOTS } from '../app/labs/public-snapshots.mjs';
import { FLOW_SITES, buildFlowComparison, daysAtFlow, flowAtFrequency, flowCsvRows, flowPeriods, flowSettings, watershedHref } from '../app/labs/river-flow/flow-model.mjs';

const [first, second, third] = FLOW_SITES;
const snapshot = PUBLIC_LAB_SNAPSHOTS['river-memory'];
const { data: { records } } = JSON.parse(readFileSync(new URL(`../public${snapshot.path}`, import.meta.url)));

test('flow duration uses paired dates, keeps zero and counts every tied reading', () => {
  const series = (site, values) => values.map(([day, discharge, qualifiers]) => ({ siteCode: site.id, date: day, discharge, qualifiers }));
  const comparison = buildFlowComparison([
    ...series(first, [['2020-02-27', 10], ['2020-02-28', 10], ['2020-02-29', 0], ['2020-03-01', null, 'P, Bkw']]),
    ...series(second, [['2020-02-27', 2], ['2020-02-28', 4], ['2020-02-29', 0], ['2020-03-01', 4], ['2020-03-02', 13]]),
  ], { from: '2020-02-27', to: '2020-03-02' }, first.id, second.id);
  assert.equal(comparison.count, 3);
  assert.equal(comparison.days.length, 5);
  assert.deepEqual(comparison.missing, [2, 0]);
  const [curve, other] = comparison.curves;
  assert.deepEqual(curve, [{ value: 10, count: 2 }, { value: 0, count: 3 }]);
  assert.deepEqual(flowAtFrequency(curve, 3, 50), { value: 10, count: 2 });
  assert.deepEqual(flowAtFrequency(curve, 3, 90), { value: 0, count: 3 });
  assert.equal(daysAtFlow(curve, 10), 2);
  assert.equal(daysAtFlow(curve, 10.01), 0);
  assert.equal(daysAtFlow(other, 0), 3);
  assert.equal(flowAtFrequency([], 0, 50), null);
  const csv = flowCsvRows(comparison.days, first.id, second.id);
  assert.deepEqual(csv[3], ['2020-02-29', 0, '', 0, '', true]);
  assert.deepEqual(csv[4], ['2020-03-01', null, 'P, Bkw', 4, '', false]);
  assert.deepEqual(csv[5], ['2020-03-02', null, '', 13, '', false]);
});

test('the published snapshot exposes actual matched coverage and empirical thresholds', () => {
  const periods = flowPeriods(records);
  const recent = periods.find(period => period.id === '2026');
  assert.equal(recent.label, '2026 (partial year)');
  assert.equal(recent.to, '2026-11-15');
  const comparison = buildFlowComparison(records, recent, third.id, first.id);
  assert.equal(comparison.days.length, 319);
  assert.equal(comparison.count, 307);
  assert.deepEqual(comparison.missing, [5, 7]);

  const baseline = buildFlowComparison(records, periods[0], first.id, second.id);
  assert.equal(baseline.count, 2192);
  assert.deepEqual(baseline.missing, [0, 0]);
  for (const [index, curve] of baseline.curves.entries()) {
    const total = baseline.count;
    const raw = baseline.days.filter(day => day.included).map(day => day.readings[index].value);
    assert.equal(daysAtFlow(curve, 1000), raw.filter(value => value >= 1000).length);
    for (const frequency of [1, 10, 50, 90, 100]) {
      const point = flowAtFrequency(curve, total, frequency);
      assert.equal(daysAtFlow(curve, point.value), raw.filter(value => value >= point.value).length);
      assert.ok(point.count >= Math.ceil(frequency * total / 100));
      assert.ok(raw.filter(value => value > point.value).length < Math.ceil(frequency * total / 100));
    }
  }
});

test('view URLs validate inputs and center existing sources on the chosen gauge', () => {
  assert.deepEqual(flowSettings({ first: third.id, second: third.id, period: ['2026'], threshold: 'Infinity', frequency: '101', scale: 'tampered' }), {
    first: third.id, second: first.id, period: 'baseline', frequency: 50, threshold: 1000, scale: 'compressed',
  });
  assert.deepEqual(flowSettings({ first: second.id, second: first.id, period: '2026', threshold: '0', frequency: '100', scale: 'linear' }), {
    first: second.id, second: first.id, period: '2026', frequency: 100, threshold: 0, scale: 'linear',
  });
  const href = new URL(watershedHref(third), 'https://example.test');
  assert.equal(href.searchParams.get('ctx'), 'usgs-streamflow,usgs-wbd-watersheds');
  assert.deepEqual(href.searchParams.get('c').split(',').map(Number), third.center);
});
