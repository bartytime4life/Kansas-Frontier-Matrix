import assert from 'node:assert/strict';
import test from 'node:test';
import { compareGroups, comparisonMode, comparisonModes, describe, distribution, filterRecords, metricOf, monthlySeries, numeric, recordGeometry, recordModel, recordOutsideBounds, recordRange, recordsCSV, safeCell, timeText, yearCounts } from '../app/living-welcome/stories/record-model.mjs';

const bundle = (records, extra = {}) => ({ story: 'test-record', built_at: '2026-11-06T00:00:00Z', sources: [{ url: 'https://example.org/source' }], data: { kind: 'records', columns: [{ key: 'name', label: 'Name', type: 'string' }, { key: 'year', label: 'Year', type: 'number' }, { key: 'value', label: 'Value', type: 'number', unit: 'm' }, { key: 'other', label: 'Alternative', type: 'number' }, { key: 'category', label: 'Category', type: 'string' }], yearField: 'year', valueField: 'value', categoryField: 'category', records, ...extra } });
const source = bundle([
  { id: 'a', name: 'North River', year: 2020, value: 0, other: 10, category: 'A' },
  { id: 'b', name: 'South River', year: 2021, value: 10, other: null, category: 'B' },
  { id: 'c', name: 'Dry Hill', year: 2022, value: null, other: 30, category: 'A' },
  { id: 'd', name: 'Undated River', year: null, value: 30, other: 0, category: 'B' },
]);
const model = recordModel(source);

test('numeric data never treats null, empty string, numeric string or Infinity as zero', () => {
  for (const value of [null, undefined, '', '0', NaN, Infinity]) assert.equal(numeric(value), null);
  assert.equal(numeric(0), 0);
});
test('model chooses declared numeric metric and caches without modifying input', () => {
  assert.equal(recordModel(source), model); assert.equal(metricOf(model).key, 'value');
  assert.equal(metricOf(model, { metric: 'other' }).key, 'other');
  assert.equal(metricOf(model, { metric: 'made-up' }).key, 'value');
  assert.equal(source.data.records[2].value, null);
});
test('search, category, metric bounds and playback compose exactly', () => {
  assert.deepEqual(filterRecords(model, { controls: { query: ' RIVER ', category: 'A', minValue: '0', maxValue: '0' }, time: 2021 }).map(row => row.id), ['a']);
  assert.deepEqual(filterRecords(model, { controls: { metric: 'other', minValue: '20' } }).map(row => row.id), ['c']);
});
test('undated rows remain at final frame but cannot enter dated selections', () => {
  assert.equal(filterRecords(model, { time: 2022 }).length, 4);
  assert.deepEqual(filterRecords(model, { time: 2021 }).map(row => row.id), ['a', 'b']);
  assert.deepEqual(filterRecords(model, { controls: { from: '2020', to: '2022' } }).map(row => row.id), ['a', 'b', 'c']);
});
test('reversed bounds are empty and zero is a valid numeric boundary', () => {
  assert.equal(filterRecords(model, { controls: { minValue: 20, maxValue: 10 } }).length, 0);
  assert.deepEqual(filterRecords(model, { controls: { maxValue: 0 } }).map(row => row.id), ['a']);
});
test('sorting is stable, missing-last in both directions, and leaves input order unchanged', () => {
  assert.deepEqual(filterRecords(model, { controls: { sort: 'value', direction: 'desc' } }).map(row => row.id), ['d', 'b', 'a', 'c']);
  assert.deepEqual(filterRecords(model, { controls: { sort: 'value', direction: 'asc' } }).map(row => row.id), ['a', 'b', 'd', 'c']);
  assert.deepEqual(model.records.map(row => row.id), ['a', 'b', 'c', 'd']);
});
test('descriptive summaries exclude missing values and retain real zeros', () => {
  assert.deepEqual(describe(model.records, 'value'), { total: 4, count: 3, missing: 1, min: 0, max: 30, mean: 40 / 3, median: 10 });
  assert.deepEqual(describe([{ value: null }], 'value'), { total: 1, count: 0, missing: 1, min: null, max: null, mean: null, median: null });
  assert.equal(describe([{ v: 2 }, { v: 4 }], 'v').median, 3);
});
test('histogram accounts for every numeric value exactly once including maximum', () => {
  const bins = distribution(model.records, 'value', 3);
  assert.equal(bins.reduce((sum, bin) => sum + bin.count, 0), 3);
  assert.deepEqual(bins.map(bin => bin.count), [1, 1, 1]);
  assert.deepEqual(distribution([{ v: 0 }, { v: 0 }, { v: null }], 'v'), [{ from: 0, to: 0, count: 2 }]);
});
test('category comparison uses selected metric and matching rows only', () => {
  const [a, b] = compareGroups(model, model.records, { compareMode: 'category', compareA: 'A', compareB: 'B', metric: 'other' });
  assert.equal(a.mean, 20); assert.equal(a.missing, 0); assert.equal(b.mean, 0); assert.equal(b.missing, 1);
});
test('period comparison has inclusive boundaries and excludes undated rows', () => {
  const [a, b] = compareGroups(model, model.records, { compareMode: 'period', compareAFrom: 2020, compareATo: 2021, compareBFrom: 2022, compareBTo: 2022 });
  assert.equal(a.total, 2); assert.equal(a.mean, 5); assert.equal(b.total, 1); assert.equal(b.missing, 1);
});
test('geometry fallback requires finite real coordinates and never makes missing points', () => {
  assert.equal(recordGeometry({ longitude: null, latitude: 38 }), null);
  assert.equal(recordGeometry({ longitude: -200, latitude: 38 }), null);
  assert.deepEqual(recordGeometry({ longitude: -98, latitude: 38 }), { type: 'Point', coordinates: [-98, 38] });
  const geometry = { type: 'LineString', coordinates: [[-98, 38], [-97, 39]] };
  assert.equal(recordGeometry({ geometry }), geometry);
});
test('CSV has the identical filtered sorted record selection and preserves null as blank', () => {
  const options = { controls: { query: 'River', sort: 'value', direction: 'desc' }, time: 2021 }, csv = recordsCSV(source, options);
  assert.deepEqual(csv.rows.slice(1).map(row => row[csv.rows[0].indexOf('id')]), filterRecords(model, options).map(row => row.id));
  assert.equal(csv.rows[1][3], ''); assert.equal(csv.rows[2][2], 0);
  assert.equal(csv.rows[1][csv.rows[0].indexOf('source_urls')], 'https://example.org/source');
});
test('CSV carries all extraction hashes and geometry for reproducible selections', () => {
  const s = bundle([{ id: 'a', value: 1, geometry: { type: 'Point', coordinates: [0, 0] } }], { sourceSnapshots: [{ retrievedAt: 'first', rawSha256: 'aaa' }, { retrievedAt: 'second', rawSha256: 'bbb' }] });
  const csv = recordsCSV(s);
  assert.equal(csv.rows[1][csv.rows[0].indexOf('snapshot_sha256')], 'aaa | bbb');
  assert.equal(JSON.parse(csv.rows[1][csv.rows[0].indexOf('geometry')]).type, 'Point');
});
test('spreadsheet injection protection applies to text while negative numbers stay numeric', () => {
  assert.equal(safeCell('=WEBSERVICE("example")'), '\'=WEBSERVICE("example")');
  assert.equal(safeCell('  @SUM(1)'), "'  @SUM(1)"); assert.equal(safeCell(-5), -5); assert.equal(safeCell(null), '');
});
test('snapshot mode shows one observation year by default and during playback', () => {
  const b = bundle([{ id: 'a2020', year: 2020, value: 100 }, { id: 'a2021', year: 2021, value: 101 }, { id: 'b2021', year: 2021, value: 50 }], { temporalMode: 'snapshot' }), m = recordModel(b);
  assert.deepEqual(filterRecords(m).map(row => row.id), ['a2021', 'b2021']);
  assert.deepEqual(filterRecords(m, { time: 2020 }).map(row => row.id), ['a2020']);
  assert.equal(recordsCSV(b, { time: 2020 }).rows.length, 2);
});
test('historical interval mode shows year-end validity and timeline extends to end coverage', () => {
  const b = bundle([{ id: 'old', year: 1855, startDate: '1855-01-01', endDate: '1860-06-01', endYear: 1860 }, { id: 'new', year: 1860, startDate: '1860-06-02', endDate: '2000-12-31', endYear: 2000 }], { temporalMode: 'interval', dateField: 'startDate', endDateField: 'endDate', endYearField: 'endYear' }), m = recordModel(b);
  assert.equal(recordRange(b).max, 2000);
  assert.deepEqual(filterRecords(m, { time: 1860 }).map(row => row.id), ['new']);
  assert.deepEqual(filterRecords(m, { time: 1859 }).map(row => row.id), ['old']);
  assert.deepEqual(filterRecords(m).map(row => row.id), ['new']);
});
test('geological slider retains fractional Ma and presents positive before-present labels', () => {
  const b = bundle([{ year: -300.5, value: 2 }, { year: -.00585, value: 3 }], { timeUnit: 'Ma', timeStep: .1, timeLabel: 'Age before present' });
  assert.equal(recordRange(b).step, .1); assert.equal(recordRange(b).min, -300.5);
  assert.equal(timeText(recordModel(b), -.00585), '0.00585 Ma');
  assert.equal(recordRange(b).format(-300.5), '300.5 Ma');
});
test('year frequency excludes unknown dates without inferring any year', () => {
  assert.deepEqual(yearCounts(model.records, 'year'), [{ year: 2020, count: 1 }, { year: 2021, count: 1 }, { year: 2022, count: 1 }]);
});
test('monthly series keeps sources separate, ignores null, and retains missing-only months', () => {
  const rows = monthlySeries([{ date: '2020-01-01', value: 0, category: 'A' }, { date: '2020-01-02', value: 10, category: 'A' }, { date: '2020-02-01', value: null, category: 'A' }, { date: '2020-01-01', value: 100, category: 'B' }], 'date', 'value', 'category');
  assert.equal(rows.length, 3); assert.equal(rows.find(row => row.category === 'A' && row.date === '2020-01').mean, 5);
  assert.equal(rows.find(row => row.category === 'B').mean, 100);
  assert.equal(rows.find(row => row.date === '2020-02').mean, null);
});

test('single-category interval records cannot fabricate cohorts from boundary start years', () => {
  const m = recordModel(bundle([{ id: 'old-county', year: 1855, endYear: 2000, value: 500, category: 'County' }, { id: 'new-county', year: 1978, endYear: 2000, value: 900, category: 'County' }], { temporalMode: 'interval', endYearField: 'endYear' }));
  const selected = filterRecords(m, { time: 2000 });
  assert.equal(selected.length, 2);
  assert.deepEqual(comparisonModes(m), []);
  assert.equal(comparisonMode(m), null);
  assert.deepEqual(compareGroups(m, selected), []);
  assert.deepEqual(compareGroups(m, selected, { compareMode: 'period', compareAFrom: 1804, compareATo: 1902, compareBFrom: 1903, compareBTo: 2000 }), []);
});

test('snapshot comparisons offer category only; stale period selection resolves to supported categories', () => {
  const m = recordModel(bundle([{ year: 2020, value: 1, category: 'A' }, { year: 2021, value: 2, category: 'A' }, { year: 2021, value: 3, category: 'B' }], { temporalMode: 'snapshot' }));
  assert.deepEqual(comparisonModes(m), ['category']);
  assert.equal(comparisonMode(m, { compareMode: 'period' }), 'category');
  assert.deepEqual(compareGroups(m, filterRecords(m), { compareMode: 'period' }).map(group => [group.label, group.total, group.mean]), [['A', 1, 2], ['B', 1, 3]]);
});

test('map extent counts outlier coordinates without dropping source rows or crossing geometry', () => {
  const bounds = { west: -102, east: -94.5, south: 37, north: 40 };
  const records = [{ id: 'kansas', longitude: -98, latitude: 38 }, { id: 'outlier', longitude: -110, latitude: 46 }, { id: 'unknown', longitude: null, latitude: null }, { id: 'crossing', geometry: { type: 'LineString', coordinates: [[-104, 38], [-92, 38]] } }];
  assert.deepEqual(records.map(record => recordOutsideBounds(record, bounds)), [false, true, false, false]);
  const b = bundle(records), m = recordModel(b);
  assert.equal(filterRecords(m).length, 4);
  assert.equal(recordsCSV(b).rows.length - 1, 4);
});
