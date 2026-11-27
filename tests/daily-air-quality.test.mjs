import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { webcrypto, createHash } from 'node:crypto';
import { validateAirSnapshot, analyseAir, airCsv, airReceipt, categoryForAqi, CATEGORIES, YEARS } from '../app/labs/daily-air-quality/air-model.mjs';
import { loadAirSnapshot } from '../app/labs/daily-air-quality/snapshot-loader.mjs';

const manifest = JSON.parse(fs.readFileSync(new URL('../app/labs/daily-air-quality/snapshot-manifest.json', import.meta.url)));
const bytes = fs.readFileSync(new URL(`../public${manifest.snapshot.url}`, import.meta.url));
const captured = JSON.parse(bytes);
const copy = value => structuredClone(value);
const verified = () => validateAirSnapshot(copy(captured), manifest);

function fixture(entries) {
  const data = copy(captured), m = copy(manifest);
  const values = data.dates.map((day, index) => entries[day] === undefined ? null : [String(entries[day]), categoryForAqi(entries[day]), 'PM2.5', '20-173-0010', '2', index + 2]);
  data.counties = [{ id: '20173', name: 'Sedgwick County', values }];
  const reportedDays = values.filter(value => value !== null).length;
  m.counties = [{ id: '20173', name: 'Sedgwick County', reportedDays }];
  m.snapshot.records = reportedDays;
  m.coverageByYear = Object.fromEntries(YEARS.map(year => {
    const count = data.dates.filter((day, index) => day.startsWith(`${year}-`) && values[index] !== null).length;
    return [year, { reportedCountyDays: count, reportingCounties: count ? 1 : 0 }];
  }));
  return validateAirSnapshot(data, m);
}

test('captured display identity and all source coverage are exact', () => {
  assert.equal(bytes.length, 1131068);
  assert.equal(createHash('sha256').update(bytes).digest('hex'), manifest.snapshot.sha256);
  const data = verified();
  assert.equal(data.counties.length, 12);
  assert.equal(data.dates.length, 2192);
  assert.equal(manifest.snapshot.records, 22458);
  assert.equal(data.counties.reduce((sum, county) => sum + county.values.filter(Boolean).length, 0), 22458);
  assert.deepEqual(Object.values(manifest.coverageByYear).map(v => v.reportingCounties), [11, 11, 11, 11, 11, 12]);
});

test('EPA category boundary checks preserve zero and AQI above 500', () => {
  for (const [aqi, label] of [[0, 'Good'], [50, 'Good'], [51, 'Moderate'], [100, 'Moderate'], [101, CATEGORIES[2]], [150, CATEGORIES[2]],
    [151, 'Unhealthy'], [200, 'Unhealthy'], [201, 'Very Unhealthy'], [300, 'Very Unhealthy'], [301, 'Hazardous'], [501, 'Hazardous']]) assert.equal(categoryForAqi(aqi), label);
  for (const value of [-1, 10001, '50', 50.5, NaN, null]) assert.throws(() => categoryForAqi(value));
});

test('Sedgwick 2023 results match the independently inspected original EPA rows', () => {
  const analysis = analyseAir(verified());
  assert.deepEqual([analysis.expected, analysis.reported, analysis.missing, analysis.thresholdDays], [365, 365, 0, 5]);
  assert.equal(analysis.thresholdPct, 500 / 365);
  assert.equal(analysis.peak.date, '2023-09-06');
  assert.equal(analysis.peak.rawAqi, '157');
  assert.equal(analysis.peak.parameter, 'PM2.5');
  assert.equal(analysis.peak.site, '20-173-0010');
  assert.equal(analysis.peak.sourceRow, 103181);
  assert.deepEqual(analysis.longestRun, { count: 2, from: '2023-06-07', to: '2023-06-08', leftBoundary: null, rightBoundary: null });
  assert.equal(analysis.categoryCounts.reduce((sum, v) => sum + v.count, 0), 365);
  assert.equal(analysis.pollutantCounts.reduce((sum, v) => sum + v.count, 0), 365);
});

test('missing dates break observed runs; ties retain earliest run and zero remains reported', () => {
  const data = fixture({ '2024-01-01': 101, '2024-01-02': 151, '2024-01-04': 200, '2024-01-05': 0, '2024-01-06': 100, '2024-01-07': 101, '2024-01-08': 101 });
  const a = analyseAir(data, { year: 2024, month: 1 });
  assert.deepEqual([a.expected, a.reported, a.missing, a.thresholdDays, a.medianAqi], [31, 7, 24, 5, 101]);
  assert.equal(a.thresholdPct, 500 / 7);
  assert.deepEqual(a.longestRun, { count: 2, from: '2024-01-01', to: '2024-01-02', leftBoundary: 'window', rightBoundary: 'missing' });
  assert.equal(a.days[4].aqi, 0);
  assert.equal(a.days[4].missing, false);
  assert.equal(a.days[2].aqi, null);
  assert.equal(a.days[2].meets, null);
  assert.equal(analyseAir(data, { year: 2024, month: 1, threshold: 0 }).thresholdDays, 7);
});

test('leap-month and no-report windows retain their true calendar denominator', () => {
  const data = fixture({ '2024-01-31': 101, '2024-02-01': 151 });
  const january = analyseAir(data, { year: 2024, month: 1 });
  assert.equal(january.longestRun.count, 1);
  assert.equal(january.longestRun.rightBoundary, 'window');
  const february = analyseAir(data, { year: 2024, month: 2 });
  assert.equal(february.expected, 29);
  assert.equal(february.days.at(-1).date, '2024-02-29');
  const empty = analyseAir(data, { year: 2024, month: 3 });
  assert.deepEqual([empty.expected, empty.reported, empty.missing, empty.thresholdDays, empty.thresholdPct, empty.medianAqi, empty.peak], [31, 0, 31, 0, null, null, null]);
  assert.deepEqual(empty.siteCountRange, { min: null, max: null });
});

test('sparse counties remain selectable for years with no reports', () => {
  const a = analyseAir(verified(), { countyId: '20045', year: 2020 });
  assert.deepEqual([a.expected, a.reported, a.missing], [366, 0, 366]);
  assert.equal(a.thresholdPct, null);
  assert.equal(a.peak, null);
  assert.equal(a.categoryCounts.reduce((sum, value) => sum + value.count, 0), 0);
});

test('invalid settings and unverified objects cannot produce analysis or exports', () => {
  const data = verified();
  for (const settings of [{ countyId: '20001' }, { countyId: 20173 }, { year: '2023' }, { year: 2026 }, { month: 13 }, { month: 1.5 }, { threshold: -1 }, { threshold: 101.5 }, { threshold: 501 }]) assert.throws(() => analyseAir(data, settings));
  assert.throws(() => analyseAir(copy(captured)), /verify/);
  assert.throws(() => airCsv({}), /verified/);
  assert.throws(() => airReceipt({}, manifest.snapshot), /matching/);
});

test('complete schema rejects altered calendars, provenance, counts, categories and raw identities', () => {
  const edits = [
    d => { d.dates[0] = '2020-02-30'; },
    d => { d.sources[0].url = 'https://example.com/source.zip'; },
    d => { d.sources[0].capturedAt = '2026-02-30T00:00:00Z'; },
    (d, m) => { m.snapshot.records++; },
    (d, m) => { m.counties[0].reportedDays++; },
    (d, m) => { m.coverageByYear['2020'].reportingCounties++; },
    d => { d.counties[0].id = d.counties[1].id; },
    (d, m) => { m.review = 'APPROVED'; },
    d => { d.counties[6].values[0][1] = 'Hazardous'; },
    d => { d.counties[6].values[0][0] = ''; },
    d => { d.counties[6].values[0][3] = '=FORMULA()'; },
    d => { d.counties[6].values[0][3] = '20-091-0010'; },
    d => { d.counties[6].values[0][4] = '0'; },
    d => { d.counties[6].values[0][5] = 1; },
    d => { d.counties[6].values[1][5] = d.counties[6].values[0][5]; },
  ];
  for (const edit of edits) { const d = copy(captured), m = copy(manifest); edit(d, m); assert.throws(() => validateAirSnapshot(d, m), /schema|coverage/); }
  for (const value of [null, {}, [], 'data']) assert.throws(() => validateAirSnapshot(value, manifest), /schema/);
});

test('tied defining-site text survives validation and export without being split', () => {
  const d = copy(captured), m = copy(manifest);
  d.counties[6].values[0][3] = '20-173-0010; 20-173-0012';
  const a = analyseAir(validateAirSnapshot(d, m), { year: 2020, month: 1 });
  assert.equal(a.days[0].site, '20-173-0010; 20-173-0012');
  assert.ok(airCsv(a).includes('"20-173-0010; 20-173-0012"'));
});

test('CSV and analysis receipt retain exact selected tokens, gaps, source rows and inspection', () => {
  const a = analyseAir(verified(), { year: 2023, month: 9 });
  const output = airCsv(a);
  assert.equal(output.split('\r\n').filter(Boolean).length, 31);
  assert.ok(output.includes('"2023-09-06","reported","157","Unhealthy","PM2.5","20-173-0010","1","103181"'));
  const r = airReceipt(a, manifest.snapshot, { inspectedDate: '2023-09-06' });
  assert.equal(r.selection.inspectedDate, '2023-09-06');
  assert.equal(r.inspectedRecord.rawAqi, '157');
  assert.equal(r.sources[0].year, 2023);
  assert.equal(r.display.sha256, manifest.snapshot.sha256);
  assert.deepEqual([r.review, r.admission, r.release], ['PENDING', 'PENDING', 'UNRELEASED']);
  assert.throws(() => airReceipt(a, { ...manifest.snapshot, sha256: '0'.repeat(64) }));
  assert.throws(() => airReceipt(a, manifest.snapshot, { inspectedDate: '2023-02-30' }));
  assert.throws(() => airReceipt(a, manifest.snapshot, { inspectedDate: '2023-10-01' }));
  const empty = analyseAir(verified(), { countyId: '20045', year: 2020, month: 2 });
  assert.equal(airCsv(empty).split('\r\n').filter(Boolean).length, 30);
  assert.equal(airReceipt(empty, manifest.snapshot, { inspectedDate: '2020-02-29' }).inspectedRecord.missing, true);
});

test('bounded same-origin reader verifies the actual display before exposing records', async () => {
  const options = { cryptoImpl: webcrypto, fetchImpl: async () => new Response(bytes, { headers: { 'Content-Length': String(bytes.length) } }) };
  const data = await loadAirSnapshot(manifest, options);
  assert.equal(analyseAir(data).thresholdDays, 5);
  const bad = Buffer.from(bytes); bad[bad.length - 2] ^= 1;
  await assert.rejects(loadAirSnapshot(manifest, { ...options, fetchImpl: async () => new Response(bad) }), /integrity/);
  await assert.rejects(loadAirSnapshot(manifest, { ...options, fetchImpl: async () => new Response(bytes, { status: 503 }) }), /could not/);
  await assert.rejects(loadAirSnapshot({ ...manifest, snapshot: { ...manifest.snapshot, url: 'https://example.com/data' } }, options), /manifest/);
});
