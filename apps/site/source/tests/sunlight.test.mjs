import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createHash, webcrypto } from 'node:crypto';
import test from 'node:test';
import { analyseSunlight, sunlightReading, sunlightCsv, sunlightReceipt, validateSunlightSnapshot } from '../app/labs/sunlight-and-sky/sunlight-model.mjs';
import { loadSunlightSnapshot } from '../app/labs/sunlight-and-sky/snapshot-loader.mjs';

const manifest = JSON.parse(await readFile(new URL('../app/labs/sunlight-and-sky/snapshot-manifest.json', import.meta.url)));
const bytes = await Promise.all(manifest.points.map(p => readFile(new URL(`../public${p.url}`, import.meta.url))));
const snapshots = bytes.map((raw, i) => validateSunlightSnapshot(JSON.parse(raw), manifest.points[i]));
const near = (a, b) => assert.ok(Math.abs(a - b) < 1e-10, `${a} != ${b}`);
function synthetic(index, change) {
  const snapshot = JSON.parse(bytes[index]);
  change(snapshot);
  return validateSunlightSnapshot(snapshot, manifest.points[index]);
}

test('all three published display assets match their hashes, source and complete leap calendar', () => {
  for (let i = 0; i < bytes.length; i++) {
    const descriptor = manifest.points[i];
    assert.equal(bytes[i].length, descriptor.bytes);
    assert.equal(createHash('sha256').update(bytes[i]).digest('hex'), descriptor.sha256);
    assert.equal(snapshots[i].records.length, 2192);
    assert.equal(snapshots[i].records.filter(row => row.date === '2024-02-29').length, 1);
    assert.ok(Object.isFrozen(snapshots[i].records[0]));
  }
  assert.deepEqual([manifest.review, manifest.admission, manifest.release], ['PENDING', 'PENDING', 'UNRELEASED']);
});

test('real default values and every month preserve the selected period denominator', () => {
  const analysis = analyseSunlight(snapshots[0], snapshots[2]);
  assert.equal(analysis.expected, 365);
  assert.equal(analysis.summary.paired.days, 365);
  near(analysis.summary.primary.sum, 1751.4821);
  near(analysis.summary.comparison.sum, 1570.5941);
  near(analysis.summary.paired.meanDifference, 0.49558356164383555);
  assert.deepEqual(analysis.summary.primary.peak, { date: '2025-05-16', value: 8.5404 });
  for (const year of [2020, 2024, 2025]) for (let month = 0; month <= 12; month++) {
    const a = analyseSunlight(snapshots[0], snapshots[1], { year, month });
    assert.equal(a.expected, month ? new Date(Date.UTC(year, month, 0)).getUTCDate() : year === 2025 ? 365 : 366);
    assert.equal(a.monthly.length, 12);
    assert.equal(a.monthly.reduce((sum, row) => sum + row.expected, 0), year === 2025 ? 365 : 366);
  }
});

test('zero is valid, sentinel is missing, pairs have their own denominator and values above clear-sky are retained', () => {
  const primary = synthetic(0, snapshot => {
    for (const row of snapshot.records.filter(r => r.date.startsWith('2025-01'))) { row.allSky = -999; row.clearSky = -999; }
    const first = snapshot.records.find(r => r.date === '2025-01-01'); first.allSky = 0; first.clearSky = 2;
    const second = snapshot.records.find(r => r.date === '2025-01-02'); second.allSky = 10; second.clearSky = 5;
    snapshot.records.find(r => r.date === '2025-01-03').allSky = 4;
  });
  const comparison = synthetic(1, snapshot => {
    for (const row of snapshot.records.filter(r => r.date.startsWith('2025-01'))) row.allSky = -999;
    snapshot.records.find(r => r.date === '2025-01-02').allSky = 6;
  });
  const a = analyseSunlight(primary, comparison, { year: 2025, month: 1 });
  assert.deepEqual(sunlightReading(0), { raw: 0, value: 0, state: 'modeled' });
  assert.deepEqual(sunlightReading(-999), { raw: -999, value: null, state: 'missing' });
  assert.equal(a.summary.primary.validDays, 3);
  assert.equal(a.summary.primary.missingDays, 28);
  near(a.summary.primary.mean, 14 / 3);
  assert.deepEqual(a.summary.paired, { days: 1, primaryMean: 10, comparisonMean: 6, meanDifference: 4 });
  assert.deepEqual(a.summary.clearSky, { days: 2, allSkyMean: 5, clearSkyMean: 3.5, meanDifference: 1.5 });
  assert.equal(a.days[1].primary.allSky.value, 10);
  assert.equal(sunlightReceipt(a).metrics.primary.validDays, 3);
  const csv = sunlightCsv(a);
  assert.match(csv, /2025-01-01,20250101,2025,1,NASA Local Solar Time,kWh\/m2\/day,dodge-city,37\.7608,-99\.9689,0,modeled,0/);
  assert.match(csv, /,missing,-999/);
});

test('a fully missing window has unavailable means, sums, peaks and pairwise metrics', () => {
  const empty = synthetic(0, snapshot => { for (const row of snapshot.records) row.allSky = row.clearSky = -999; });
  const a = analyseSunlight(empty, empty, { year: 2024, month: 2 });
  assert.equal(a.expected, 29);
  assert.deepEqual(a.summary.primary, { validDays: 0, missingDays: 29, sum: null, mean: null, peak: null });
  assert.equal(a.summary.paired.meanDifference, null);
  assert.equal(a.summary.clearSky.clearSkyMean, null);
  assert.equal(sunlightCsv(a).trimEnd().split('\r\n').length, 30);
});

test('same-area comparisons are valid and exports remain bound to immutable analysis sources', () => {
  const a = analyseSunlight(snapshots[1], snapshots[1]);
  assert.equal(a.summary.paired.meanDifference, 0);
  const receipt = sunlightReceipt(a);
  assert.equal(receipt.sources.primary.sha256, manifest.points[1].sha256);
  assert.equal(receipt.sources.primary.source.sha256, manifest.points[1].source.sha256);
  assert.equal(receipt.selection.timeStandard, 'NASA Local Solar Time');
  assert.equal(receipt.metrics.paired.days, 365);
  assert.equal(receipt.release, 'UNRELEASED');
  receipt.metrics.primary.mean = 100;
  assert.notEqual(a.summary.primary.mean, 100);
  assert.throws(() => { a.summary.primary.mean = 100; });
  assert.throws(() => sunlightReceipt({ ...a }), /source-bound/);
  assert.throws(() => sunlightCsv({ ...a }), /source-bound/);
  assert.throws(() => analyseSunlight(JSON.parse(bytes[0]), snapshots[1]), /Validate/);
});

test('schema validation rejects wrong point, units, clock, product, malformed dates and invalid numeric values', () => {
  for (const change of [s => { s.point.latitude += 1; }, s => { s.provider.timeStandard = 'UTC'; },
    s => { s.provider.sources = ['FLASHFLUX']; }, s => { s.parameters.ALLSKY_SFC_SW_DWN.units = 'W/m2'; },
    s => { s.records[0].date = '2020-02-30'; }, s => { s.records.pop(); },
    s => { s.records[0].allSky = -1; }, s => { s.records[0].allSky = null; }, s => { s.records[0].allSky = true; }]) {
    const value = JSON.parse(bytes[0]); change(value);
    assert.throws(() => validateSunlightSnapshot(value, manifest.points[0]));
  }
  for (const value of [NaN, Infinity, '0', null, undefined, -1, 31]) assert.throws(() => sunlightReading(value));
  for (const selection of [{ year: 2026 }, { year: '2025' }, { month: 13 }, { month: NaN }]) assert.throws(() => analyseSunlight(snapshots[0], snapshots[1], selection));
});

test('loader validates real bytes and rejects mismatched bytes, response failures and aborted reads', async () => {
  const descriptor = manifest.points[0];
  const fetchImpl = async () => new Response(bytes[0], { headers: { 'content-length': String(bytes[0].length) } });
  const loaded = await loadSunlightSnapshot(descriptor, { fetchImpl, cryptoImpl: webcrypto });
  assert.equal(loaded.point.id, 'dodge-city');
  await assert.rejects(loadSunlightSnapshot(descriptor, { fetchImpl: async () => new Response('Error', { status: 503 }), cryptoImpl: webcrypto }), /could not/);
  const altered = Buffer.from(bytes[0]); altered[altered.indexOf('2020-01-01')] = 51;
  await assert.rejects(loadSunlightSnapshot(descriptor, { fetchImpl: async () => new Response(altered), cryptoImpl: webcrypto }), /integrity/);
  const controller = new AbortController(); controller.abort();
  await assert.rejects(loadSunlightSnapshot(descriptor, { fetchImpl, cryptoImpl: webcrypto, signal: controller.signal }), { name: 'AbortError' });
});
