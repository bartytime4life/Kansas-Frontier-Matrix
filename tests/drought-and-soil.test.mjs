import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createHash, webcrypto } from 'node:crypto';
import { createServer } from 'node:http';
import { gzipSync, brotliCompressSync } from 'node:zlib';
import { analyseDrought, assessmentDates, droughtCategories, droughtCsv, droughtReceipt, validateDroughtSnapshot } from '../app/labs/county-drought/drought-model.mjs';
import { analyseSoil, soilReading, soilReadingLabel, soilCsv, soilReceipt, validateSoilSnapshot } from '../app/labs/soil-profile/soil-model.mjs';
import { loadDroughtSnapshot } from '../app/labs/county-drought/snapshot-loader.mjs';
import { loadSoilSnapshot } from '../app/labs/soil-profile/snapshot-loader.mjs';

const root = new URL('../', import.meta.url);
const json = async path => JSON.parse(await readFile(new URL(path, root), 'utf8'));
const dm = await json('app/labs/county-drought/snapshot-manifest.json');
const sm = await json('app/labs/soil-profile/snapshot-manifest.json');
const db = await readFile(new URL(`public${dm.snapshot.url}`, root));
const drought = JSON.parse(db);
const soilData = await Promise.all(sm.stations.map(async descriptor => ({ descriptor, bytes: await readFile(new URL(`public${descriptor.url}`, root)) })));
const oakley = JSON.parse(soilData[1].bytes);

test('all shipped county and soil displays bind exact bytes, metadata, source identities and complete calendars', () => {
  assert.equal(db.length, dm.snapshot.bytes);
  assert.equal(createHash('sha256').update(db).digest('hex'), dm.snapshot.sha256);
  assert.equal(validateDroughtSnapshot(drought, dm).counties.length, 105);
  assert.equal(dm.snapshot.records, 32865);
  assert.equal(assessmentDates().length, 313);
  assert.equal(assessmentDates(2024, 2024).length, 53);
  for (const { descriptor, bytes } of soilData) {
    assert.equal(bytes.length, descriptor.bytes);
    assert.equal(createHash('sha256').update(bytes).digest('hex'), descriptor.sha256);
    const snapshot = validateSoilSnapshot(JSON.parse(bytes), descriptor);
    assert.equal(snapshot.records.length, 2192);
    assert.equal(analyseSoil(snapshot, { year: 2024, month: 2 }).expected, 29);
    assert.equal(analyseSoil(snapshot, { year: 2023, month: 2 }).expected, 28);
  }
});

test('cumulative severity becomes disjoint categories without counting overlap twice', () => {
  assert.deepEqual(droughtCategories([30, 70, 60, 40, 20, 10]), [30, 10, 20, 20, 10, 10]);
  assert.deepEqual(droughtCategories([99.99, 0.01, 0.01, 0, 0, 0]), [99.99, 0, 0.01, 0, 0, 0]);
  assert.equal(droughtCategories(null), null);
});

test('real county histories distinguish threshold weeks, complete runs and index points', () => {
  const a = analyseDrought(drought);
  assert.equal(a.expected, 313);
  assert.equal(a.primary.thresholdWeeks, 92);
  assert.equal(a.comparison.thresholdWeeks, 21);
  assert.deepEqual(a.primary.longestRun, { count: 71, from: '2022-03-15', to: '2023-07-18', leftBoundary: null, rightBoundary: null });
  assert.equal(a.ranking.length, 105);
  assert.ok(a.ranking.every((county, index) => !index || county.thresholdWeeks <= a.ranking[index - 1].thresholdWeeks));
  assert.equal(a.primary.weeks[0].through, '2020-01-13');
});

test('missing assessments break runs; runs touching missing or window boundaries remain censored', () => {
  const s = structuredClone(drought);
  const county = s.counties.find(item => item.id === '20055');
  county.values.fill(null);
  county.values[0] = [0, 100, 100, 50, 0, 0];
  county.values[1] = [0, 100, 100, 50, 0, 0];
  county.values[3] = [0, 100, 100, 49.99, 0, 0];
  let a = analyseDrought(s);
  assert.equal(a.primary.valid, 3); assert.equal(a.primary.thresholdWeeks, 2);
  assert.deepEqual(a.primary.longestRun, { count: 2, from: '2020-01-07', to: '2020-01-14', leftBoundary: 'window', rightBoundary: 'missing' });
  assert.equal(a.primary.weeks[2].share, null);
  county.values.fill(null);
  county.values[county.values.length - 1] = [0, 100, 100, 50, 0, 0];
  a = analyseDrought(s);
  assert.equal(a.primary.longestRun.leftBoundary, 'missing'); assert.equal(a.primary.longestRun.rightBoundary, 'window');
  assert.equal(a.primary.peakShare, 50);
  assert.equal(a.primary.meanDsci, 250);
});

test('source or calendar changes, duplicate counties and impossible cumulative shares fail validation', () => {
  const mutations = [s => { s.weeks[1] = s.weeks[0]; }, s => { s.counties[1].id = s.counties[0].id; },
    s => { s.counties[0].values[0] = [10, 90, 95, 0, 0, 0]; }, s => { s.counties[0].values[0][0] = 101; },
    s => { s.sources[0].sha256 = '0'.repeat(64); }, s => { s.statisticsType = 2; }, s => { s.counties.pop(); }];
  for (const mutate of mutations) { const s = structuredClone(drought); mutate(s); assert.throws(() => validateDroughtSnapshot(s, dm)); }
});

test('invalid windows and county or severity settings cannot become a different analysis', () => {
  for (const settings of [{ fromYear: 2019 }, { fromYear: 2025, toYear: 2024 }, { level: 0 }, { level: 2.1 },
    { threshold: 0 }, { threshold: 0.0000001 }, { threshold: 0.015 }, { threshold: NaN }, { threshold: 101 }, { countyId: '20002' }]) assert.throws(() => analyseDrought(drought, settings));
});

test('soil sentinels, real zero and range exceptions retain different states and exact tokens', () => {
  assert.deepEqual(soilReading('0.000', 'moisture'), { raw: '0.000', value: 0, state: 'reported' });
  assert.equal(soilReading('-99.000', 'moisture').state, 'missing');
  assert.equal(soilReading('-9999.0', 'temperature').value, null);
  assert.equal(soilReading('1.001', 'moisture').state, 'out-of-range');
  assert.equal(soilReading('-50.1', 'temperature').state, 'out-of-range');
  assert.equal(soilReading(null, 'temperature').state, 'absent');
  assert.throws(() => soilReading('0.2oops', 'moisture'));
  assert.equal(soilReadingLabel(soilReading('0.236', 'moisture'), 'moisture'), '0.236 m³/m³');
});

test('soil summaries use separate moisture and temperature coverage with no depth averaging', () => {
  const a = analyseSoil(oakley);
  assert.equal(a.valid, 331); assert.equal(a.missing, 34); assert.equal(a.median, 0.236);
  assert.equal(a.min, 0.144); assert.equal(a.max, 0.304);
  assert.equal(a.meanColdDays, 19); assert.equal(a.temperatureValid, 364);
  const deep = analyseSoil(JSON.parse(soilData[0].bytes), { depth: 50 });
  assert.equal(deep.valid, 8); assert.equal(deep.missing, 357); assert.equal(deep.temperatureValid, 214);
});

test('soil missing and invalid days do not fill curves or enter medians or cold-day counts', () => {
  const s = structuredClone(oakley);
  s.records = s.records.filter(row => row.date !== '2024-02-27');
  for (const row of s.records.filter(row => row.date.startsWith('2024-02'))) { row.moisture.fill('-99.000'); row.temperature.fill('-9999.0'); }
  Object.assign(s.records.find(row => row.date === '2024-02-28'), { moisture: ['0.000', '0.000', '0.200', '0.100', '0.100'], temperature: ['1.0', '1.0', '0.0', '1.0', '1.0'] });
  Object.assign(s.records.find(row => row.date === '2024-02-29'), { moisture: ['0.000', '0.000', '0.400', '0.100', '0.100'], temperature: ['1.0', '1.0', '-1.0', '1.0', '1.0'] });
  let a = analyseSoil(s, { year: 2024, month: 2 });
  assert.equal(a.expected, 29); assert.equal(a.valid, 2); assert.equal(a.missing, 27);
  assert.ok(Math.abs(a.median - 0.3) < 1e-12); assert.equal(a.meanColdDays, 2);
  assert.equal(a.days[26].moisture[2].state, 'absent');
  a = analyseSoil(s, { year: 2024, month: 1, variable: 'temperature' });
  assert.ok(a.valid > 0);
});

test('soil schema binds station, depth order, exact calendar, raw tokens and source receipts', () => {
  const mutations = [s => { s.station.id = '53974'; }, s => { s.depthsCm.reverse(); }, s => { s.records[1].date = s.records[0].date; },
    s => { s.records[0].moisture.pop(); }, s => { s.records[0].moisture[0] = 0.3; }, s => { s.sources[0].year = 2026; }];
  for (const mutate of mutations) { const s = structuredClone(oakley); mutate(s); assert.throws(() => validateSoilSnapshot(s, soilData[1].descriptor)); }
  for (const settings of [{ year: 2026 }, { month: 13 }, { depth: 30 }, { variable: 'saturation' }]) assert.throws(() => analyseSoil(oakley, settings));
});

test('CSV and analysis receipts retain raw qualification, settings and original/display provenance', () => {
  const a = analyseDrought(drought, { fromYear: 2025 });
  const d = droughtCsv(a);
  assert.equal(d.split('\r\n').length, 106);
  assert.match(d, /only_d0_percent/); assert.match(d, /"D2\+","50"/);
  const receipt = droughtReceipt(a, dm.snapshot);
  assert.equal(receipt.displaySnapshot.sha256, dm.snapshot.sha256); assert.equal(receipt.ranking.length, 105);
  assert.equal(receipt.sourceAdmission, 'PENDING');
  const b = analyseSoil(oakley, { month: 1, depth: 100 });
  const c = soilCsv(b);
  assert.equal(c.split('\r\n').length, 157);
  assert.match(c, /"-99.000",,"missing"/); assert.match(c, new RegExp(b.sources[5].sha256));
  const sr = soilReceipt(b, soilData[1].descriptor);
  assert.equal(sr.settings.depth, 100); assert.equal(sr.depths.length, 5); assert.equal(sr.releaseState, 'UNRELEASED');
  assert.throws(() => soilReceipt(b, soilData[0].descriptor));
});

const options = fetchImpl => ({ fetchImpl, cryptoImpl: webcrypto });
test('bounded loaders verify both scientific snapshots before exposing any result', async () => {
  const d = await loadDroughtSnapshot(dm, options(async () => new Response(db)));
  assert.equal(d.counties.length, 105);
  const s = await loadSoilSnapshot(soilData[1].descriptor, options(async () => new Response(soilData[1].bytes)));
  assert.equal(s.station.id, '03067');
});

test('real gzip and Brotli responses verify decoded bytes and still reject changed or incomplete content', async t => {
  let encoding = 'gzip';
  let soilBytes = soilData[1].bytes;
  const server = createServer((request, response) => {
    const raw = request.url === dm.snapshot.url ? db : soilBytes;
    const body = encoding === 'gzip' ? gzipSync(raw) : brotliCompressSync(raw);
    response.writeHead(200, { 'content-type': 'application/json', 'content-encoding': encoding, 'content-length': body.length });
    response.end(body);
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  t.after(() => new Promise(resolve => { server.closeAllConnections(); server.close(resolve); }));
  const origin = `http://127.0.0.1:${server.address().port}`;
  const compressed = options(url => fetch(origin + url));
  for (const format of ['gzip', 'br']) {
    encoding = format;
    assert.equal((await loadDroughtSnapshot(dm, compressed)).counties.length, 105, format);
    assert.equal((await loadSoilSnapshot(soilData[1].descriptor, compressed)).station.id, '03067', format);
    soilBytes = Buffer.from(soilData[1].bytes); soilBytes[100] ^= 1;
    await assert.rejects(loadSoilSnapshot(soilData[1].descriptor, compressed), /integrity/, format);
    soilBytes = soilData[1].bytes.subarray(0, 100);
    await assert.rejects(loadSoilSnapshot(soilData[1].descriptor, compressed), /incomplete/, format);
    soilBytes = soilData[1].bytes;
  }
});

test('non-2xx, truncated, overlong, changed hash, wrong byte header or malformed manifest fail closed', async () => {
  const bytes = soilData[1].bytes;
  const changed = Buffer.from(bytes); changed[100] ^= 1;
  for (const response of [new Response('bad', { status: 503 }), new Response(bytes.subarray(0, 100)), new Response(Buffer.concat([bytes, Buffer.from('x')])),
    new Response(changed), new Response(bytes, { headers: { 'content-length': String(bytes.length + 1) } })]) {
    await assert.rejects(loadSoilSnapshot(soilData[1].descriptor, options(async () => response)));
  }
  await assert.rejects(loadSoilSnapshot({ ...soilData[1].descriptor, url: 'https://example.org/source.json' }, options(() => { throw new Error('must not fetch'); })), /manifest/);
});

test('timeouts bound stalled headers and bodies even if transport ignores abort; superseded reads abort', async () => {
  const descriptor = soilData[1].descriptor;
  const fast = fetchImpl => ({ ...options(fetchImpl), timeoutMs: 15 });
  await assert.rejects(loadSoilSnapshot(descriptor, fast(() => new Promise(() => {}))), /timed out/);
  let cancelled = false;
  const body = new ReadableStream({ start(controller) { controller.enqueue(new Uint8Array([123])); }, cancel() { cancelled = true; } });
  await assert.rejects(loadSoilSnapshot(descriptor, fast(async () => new Response(body))), /timed out/);
  assert.equal(cancelled, true);
  const controller = new AbortController();
  const pending = loadSoilSnapshot(descriptor, { ...options(() => new Promise(() => {})), signal: controller.signal });
  controller.abort(); await assert.rejects(pending, { name: 'AbortError' });
});
