import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createHash, webcrypto } from 'node:crypto';
import { analyseClimate, climateReading, climateCsv, climateReceipt, readingLabel, validateSnapshot } from '../app/labs/heat-and-rain/climate-model.mjs';
import { loadClimateSnapshot } from '../app/labs/heat-and-rain/snapshot-loader.mjs';

const root = new URL('../', import.meta.url);
const manifest = JSON.parse(await readFile(new URL('app/labs/heat-and-rain/snapshot-manifest.json', root), 'utf8'));
const descriptor = manifest.stations[1];
const bytes = await readFile(new URL(`public${descriptor.url}`, root));
const actual = JSON.parse(bytes);
const raw = (n, m = '', q = '', s = 'W') => [n, m, q, s];
const copy = () => structuredClone(actual);

test('NOAA scale, genuine zero, trace and qualification have distinct meanings', () => {
  assert.equal(climateReading(raw(322), 'tmax').value, 32.2);
  assert.equal(climateReading(raw(125), 'prcp').value, 12.5);
  assert.equal(climateReading(raw(0), 'prcp').value, 0);
  assert.equal(climateReading(raw(0, 'T'), 'prcp').state, 'trace');
  assert.equal(climateReading(raw(0, 'T'), 'prcp').value, null);
  for (const [tuple, state] of [[raw(-9999), 'missing'], [null, 'missing'], [raw(0, 'P'), 'missing-presumed-zero'],
    [raw(10, '', 'X'), 'quality-withheld'], [raw(0, 'H'), 'precipitation-noted'], [raw(0, 'I'), 'precipitation-not-reported'],
    [raw(-1), 'unqualified'], [raw(0, 'Z'), 'unqualified'], [raw(0, '', '', ''), 'unqualified'], [raw(10, 'T'), 'unqualified']]) {
    const r = climateReading(tuple, 'prcp'); assert.equal(r.state, state); assert.equal(r.value, null);
  }
  assert.equal(climateReading(raw(340, 'H'), 'tmax').value, 34);
  assert.equal(climateReading(raw(340, 'T'), 'tmax').state, 'unqualified');
  assert.throws(() => climateReading(['0', '', '', 'W'], 'prcp'));
});

test('partial GHCN precipitation periods preserve raw readings without counting as completed days', () => {
  for (const flag of ['A', 'C', 'E']) {
    for (const amount of [0, 125]) {
      const reading = climateReading(raw(amount, flag), 'prcp');
      assert.equal(reading.state, 'partial-period');
      assert.equal(reading.value, null);
      assert.equal(reading.raw, amount);
      assert.equal(reading.measurementFlag, flag);
      assert.match(readingLabel(reading, 'prcp'), /partial precipitation period/);
    }
    assert.equal(climateReading(raw(125, flag, 'X'), 'prcp').state, 'quality-withheld');
  }
  for (const flag of ['B', 'D', 'F', 'G']) assert.equal(climateReading(raw(125, flag), 'prcp').value, 12.5);
  const s = copy();
  s.records = s.records.map(row => ({ ...row, prcp: null }));
  s.records[0].prcp = raw(125, 'A');
  s.records[1].prcp = raw(40, 'D');
  const analysis = analyseClimate(s, { year: 2020, month: 1, wetMm: 1 });
  assert.equal(analysis.valid.prcp, 1);
  assert.equal(analysis.wetDays, 1);
  assert.equal(analysis.rainMm, 4);
  assert.equal(analysis.partialPrecipitationDays, 1);
  assert.match(climateCsv(analysis), /,partial-period,125,A,,W,/);
  assert.equal(climateReceipt(analysis, descriptor).support.partialPrecipitationDays, 1);
});

test('all shipped station calendars, source identity and hashes are checked', async () => {
  assert.equal(manifest.scope, 'provider-context');
  for (const item of manifest.stations) {
    const data = await readFile(new URL(`public${item.url}`, root));
    assert.equal(data.length, item.bytes);
    assert.equal(createHash('sha256').update(data).digest('hex'), item.sha256);
    const snapshot = validateSnapshot(JSON.parse(data), item);
    assert.equal(snapshot.records.length, 2192);
    for (let year = 2020; year <= 2025; year++) {
      const result = analyseClimate(snapshot, { year });
      assert.equal(result.expected, year % 4 === 0 ? 366 : 365);
      assert.equal(result.monthly.reduce((n, month) => n + month.expected, 0), result.expected);
      assert.equal(result.monthly.reduce((n, month) => n + month.traceDays, 0), result.traceDays);
    }
  }
});

test('calendar validation rejects a wrong station, duplicate date, sparse field or different source receipt', () => {
  let s = copy(); s.station.id = manifest.stations[0].id; assert.throws(() => validateSnapshot(s, descriptor));
  s = copy(); s.records[1].date = s.records[0].date; assert.throws(() => validateSnapshot(s, descriptor));
  s = copy(); s.records.pop(); assert.throws(() => validateSnapshot(s, descriptor));
  s = copy(); delete s.records[0].prcp; assert.throws(() => validateSnapshot(s, descriptor));
  s = copy(); s.source.sha256 = '0'.repeat(64); assert.throws(() => validateSnapshot(s, descriptor));
});

test('February leap-day support, thresholds, zero and trace sums use independent support', () => {
  const s = copy();
  s.records = s.records.map(row => ({ date: row.date, tmax: null, tmin: null, prcp: null }));
  Object.assign(s.records.find(row => row.date === '2024-02-28'), { tmax: raw(350), tmin: raw(0), prcp: raw(10) });
  Object.assign(s.records.find(row => row.date === '2024-02-29'), { tmax: raw(349), tmin: raw(1), prcp: raw(0, 'T') });
  Object.assign(s.records.find(row => row.date === '2024-02-27'), { tmax: raw(999, '', 'X'), tmin: raw(-9999), prcp: raw(0) });
  const a = analyseClimate(s, { year: 2024, month: 2, heatC: 35, wetMm: 1 });
  assert.equal(a.expected, 29); assert.deepEqual(a.valid, { tmax: 2, tmin: 2, prcp: 2 });
  assert.equal(a.hotDays, 1); assert.equal(a.frostDays, 1); assert.equal(a.wetDays, 1);
  assert.equal(a.rainMm, 1); assert.equal(a.traceDays, 1);
  assert.equal(a.excluded.prcp, 27);
  assert.equal(analyseClimate(s, { year: 2023, month: 2 }).expected, 28);
  assert.equal(analyseClimate(s, { year: 2024, month: 1 }).rainMm, null);
});

test('physically inconsistent daily temperatures are excluded together', () => {
  const s = copy(); Object.assign(s.records[0], { tmax: raw(10), tmin: raw(20) });
  const a = analyseClimate(s, { year: 2020, month: 1 });
  assert.equal(a.days[0].tmax.state, 'inconsistent-temperatures');
  assert.equal(a.days[0].tmin.value, null);
});

test('invalid selections cannot silently become different calendar windows', () => {
  for (const options of [{ year: 2019 }, { year: 2026 }, { month: 13 }, { month: -1 }, { heatC: NaN }, { wetMm: 0 }, { wetMm: 501 }]) {
    assert.throws(() => analyseClimate(actual, options));
  }
});

test('CSV and JSON receipts preserve qualification, units, source identity and exact settings', () => {
  const s = copy(); s.records[0].prcp = raw(0, 'T'); s.records[1].tmin = raw(0);
  const a = analyseClimate(s, { year: 2020, month: 1, heatC: 35, wetMm: 2.54 });
  const csv = climateCsv(a, 'imperial');
  assert.match(csv, /tmax_F/); assert.match(csv, /prcp_in/); assert.match(csv, /trace,0,T,,W/);
  assert.match(csv, /PRCP is liquid-equivalent precipitation/);
  assert.match(csv, new RegExp(descriptor.source.sha256));
  assert.equal(csv.split('\r\n').length, 33);
  assert.equal(readingLabel(climateReading(raw(254), 'prcp'), 'prcp', 'imperial'), '1.00 in');
  assert.equal(readingLabel(climateReading(raw(0), 'tmin'), 'tmin', 'imperial'), '32.0 °F');
  assert.equal(readingLabel(climateReading(raw(0, 'T'), 'prcp'), 'prcp'), 'Trace (unquantified)');
  const receipt = climateReceipt(a, descriptor, 'imperial');
  assert.equal(receipt.selection.wetMm, 2.54); assert.equal(receipt.snapshot.sha256, descriptor.sha256);
  assert.match(receipt.method, /can include melted snow/);
  assert.ok(receipt.limitations.some(s => /occurrence of frost/.test(s)));
  assert.equal(receipt.scope, 'provider-context'); assert.throws(() => climateReceipt(a, manifest.stations[0]));
});

const loaderOptions = fetchImpl => ({ fetchImpl, cryptoImpl: webcrypto });
test('loader verifies exact source snapshot bytes before returning data', async () => {
  const result = await loadClimateSnapshot(descriptor, loaderOptions(async () => new Response(bytes)));
  assert.equal(result.station.id, descriptor.id);
});

test('loader rejects non-2xx, truncated, overlong and hash-tampered replies', async () => {
  const tampered = Buffer.from(bytes); tampered[100] ^= 1;
  for (const response of [new Response('oops', { status: 503 }), new Response(bytes.subarray(0, 100)),
    new Response(Buffer.concat([bytes, Buffer.from('extra')])), new Response(tampered),
    new Response(bytes, { headers: { 'content-length': '2000000' } })]) {
    await assert.rejects(loadClimateSnapshot(descriptor, loaderOptions(async () => response)));
  }
});

test('loader times out stalled headers and body even when a transport ignores AbortSignal', async () => {
  const fast = fetchImpl => ({ ...loaderOptions(fetchImpl), timeoutMs: 50 });
  await assert.rejects(loadClimateSnapshot(descriptor, fast(() => new Promise(() => {}))), /timed out/);
  let cancelled = false;
  const stream = new ReadableStream({ start(controller) { controller.enqueue(new Uint8Array([123])); }, cancel() { cancelled = true; } });
  await assert.rejects(loadClimateSnapshot(descriptor, fast(async () => new Response(stream))), /timed out/);
  assert.equal(cancelled, true);
});

test('aborting a superseded station prevents a successful completion', async () => {
  const controller = new AbortController();
  const read = loadClimateSnapshot(descriptor, { ...loaderOptions(() => new Promise(() => {})), signal: controller.signal });
  controller.abort(); await assert.rejects(read, { name: 'AbortError' });
});
