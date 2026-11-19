import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { buildCountyModel } from '../app/labs/county-model.mjs';
import { countyHistory, findCountyPeers, HISTORY_METRICS } from '../app/labs/county-investigations.mjs';
import { validateInvestigationState, currentSourceBindings, SUPPORTED_SIGNAL_IDS } from '../app/labs/investigation-state.mjs';
import { signalCatalog } from '../app/labs/signal-model.mjs';
import { readCountyCSV } from '../app/labs/county-csv.mjs';
import { PUBLIC_LAB_SNAPSHOTS as snapshots } from '../app/labs/public-snapshots.mjs';
import { previewNotebookImport, importNotebook, getLocalInvestigation, saveLocalInvestigation, exportLocalInvestigations } from '../app/labs/notebook.mjs';
const bundles = Object.fromEntries(await Promise.all(Object.entries(snapshots).map(async ([id, snapshot]) => [id, JSON.parse(await readFile(new URL('../public' + snapshot.path, import.meta.url)))])));
const model = buildCountyModel(bundles, { snapshots });
const memory = () => { const map = new Map(); return { getItem: key => map.get(key) ?? null, setItem: (key, value) => map.set(key, value) }; };
const format = 'kfm-science-notebook-v1';
const entry = (id, extra = {}) => ({ id, workspace: 'county', title: 'County comparison', createdAt: '2026-11-16T12:00:00.000Z', state: { countyA: '20173', countyB: '20091', acsYear: 2024, historyMetric: 'povertyPct', peerKeys: 'population,medianIncome' }, sourceBindings: currentSourceBindings('county'), ...extra });
const doc = entries => JSON.stringify({ format, entries });
const simple = rows => ({ rows: rows.map((row, i) => ({ fips: `20${String(i * 2 + 1).padStart(3, '0')}`, name: `County ${i}`, ...row })), metrics: ['x', 'y', 'z'].map(key => ({ key, label: key, unit: 'units', period: '2024' })) });

test('history exposes every source period and correct MOEs without nominal-dollar inflation claims', () => {
  for (const metric of HISTORY_METRICS) {
    const history = countyHistory(model, { fipsA: '20173', fipsB: '20091', metric });
    assert.equal(history.reason, null); assert.deepEqual(history.population.map(row => row.year), [2020, 2021, 2022, 2023, 2024, 2025]);
    assert.deepEqual(history.conditions.map(row => row.period), ['2010–2014', '2015–2019', '2020–2024']);
    for (const row of history.conditions) {
      const raw = bundles['county-conditions'].data.records.find(item => item.fips === '20173' && item.year === row.year);
      assert.equal(row.valueA, raw[metric]); assert.equal(row.moeA, raw[metric + 'Moe']);
    }
    assert.equal(history.sources.length, 2); assert.match(history.method, /90%/);
  }
  assert.equal(countyHistory(model, { fipsA: '20173', fipsB: '20091' }).metric.unit, 'vintage-year dollars');
  assert.ok(countyHistory(model, { fipsA: '20173', fipsB: '20091', metric: 'bridgeMedianAge' }).reason);
  assert.ok(countyHistory(model, { fipsA: '99999', fipsB: '20091' }).reason);
});
test('history keeps missing observations and rejects ambiguous duplicate county-years', () => {
  const sparse = { ...model, bundles: { ...model.bundles, 'census-mosaic': { data: { records: [{ fips: '20173', year: 2020, population: 0 }, { fips: '20001', year: 2021, population: 2 }] } } } };
  const h = countyHistory(sparse, { fipsA: '20173', fipsB: '20091' });
  assert.deepEqual(h.population.map(row => [row.valueA, row.valueB]), [[0, null], [null, null]]);
  sparse.bundles['census-mosaic'].data.records.push({ fips: '20173', year: 2020, population: 1 });
  assert.match(countyHistory(sparse, { fipsA: '20173', fipsB: '20091' }).reason, /Duplicate/);
});
test('peer ranks use a shared complete cohort, average ties, and independent hand-calculated RMS', () => {
  const input = simple([{ x: 0, y: 10 }, { x: 0, y: 20 }, { x: 10, y: 20 }, { x: 100000, y: 30 }, { x: 4, y: null }]);
  const result = findCountyPeers(input, { fips: '20001', keys: ['x', 'y'] });
  assert.equal(result.cohortCount, 4); assert.equal(result.excludedCount, 1);
  const second = result.peers.find(row => row.fips === '20003');
  assert.equal(second.contributions[0].anchorPercentile, 100 / 6);
  assert.equal(second.contributions[0].percentile, 100 / 6);
  assert.equal(second.contributions[1].percentile, 50);
  assert.ok(Math.abs(second.distance - Math.sqrt(1250)) < 1e-12);
  assert.equal(result.peers.length, 3);
  const scaled = simple(input.rows.map(row => ({ x: row.x * 100 + 5, y: row.y === null ? null : row.y / 2 })));
  assert.deepEqual(findCountyPeers(scaled, { fips: '20001', keys: ['x', 'y'] }).peers.map(row => [row.fips, row.distance]), result.peers.map(row => [row.fips, row.distance]));
});
test('peer finder diagnoses incomplete anchors, constants, duplicates and insufficient cohorts', () => {
  const input = simple([{ x: 1, y: 1, z: 5 }, { x: 2, y: 2, z: 5 }, { x: 3, y: 3, z: 5 }]);
  const good = findCountyPeers(input, { fips: '20003', keys: ['x', 'y', 'z'], limit: 1 });
  assert.deepEqual(good.constantKeys, ['z']); assert.equal(good.peers.length, 1); assert.equal(good.peers[0].fips, '20001', 'equal distance ties resolve by FIPS');
  const oneVarying = findCountyPeers(input, { fips: '20003', keys: ['x', 'z'] });
  assert.match(oneVarying.reason, /two.*vary/); assert.equal(oneVarying.varyingCount, 1); assert.equal(oneVarying.cohortCount, 3); assert.equal(oneVarying.excludedCount, 0);
  const uncomputed = findCountyPeers(input, { fips: '20003', keys: ['x'] });
  assert.equal(uncomputed.cohortCount, null); assert.equal(uncomputed.excludedCount, null); assert.equal(uncomputed.varyingCount, null);
  assert.ok(findCountyPeers(input, { fips: '20003', keys: null }).reason);
  assert.ok(findCountyPeers(input, { fips: '20003', keys: ['x', 'x'] }).reason);
  input.rows[0].x = null;
  assert.match(findCountyPeers(input, { fips: '20001', keys: ['x', 'y'] }).reason, /missing/);
  assert.match(findCountyPeers(input, { fips: '20003', keys: ['x', 'y'] }).reason, /three/);
  input.rows.push({ ...input.rows[1] });
  assert.match(findCountyPeers(input, { fips: '20003', keys: ['x', 'y'] }).reason, /Duplicate/);
});
test('shipping data produces 104 explainable candidates from a 105-county cohort', () => {
  const r = findCountyPeers(model, { fips: '20173', keys: ['population', 'medianIncome', 'povertyPct', 'medianAge'], limit: 10 });
  assert.equal(r.reason, null); assert.equal(r.cohortCount, 105); assert.equal(r.excludedCount, 0); assert.equal(r.peers.length, 10);
  assert.ok(r.peers.every(row => row.fips !== '20173' && row.contributions.length === 4 && row.distance >= 0));
});
test('semantic state accepts exactly current county years, metrics and known signals', () => {
  assert.deepEqual(new Set(SUPPORTED_SIGNAL_IDS), new Set(signalCatalog(bundles).map(item => item.id)));
  for (const id of SUPPORTED_SIGNAL_IDS) assert.deepEqual(validateInvestigationState('signal', { x: id }), { x: id });
  for (const bad of [{ acsYear: 2020 }, { countyA: '20002' }, { mapMetric: 'unknown' }, { extra: true }, { peerKeys: 'population,population' }, { xMetric: 'csv_0' }]) assert.throws(() => validateInvestigationState('county', bad));
  for (const bad of [{ x: 'energy:made-up' }, { from: 2025, to: 2000 }, { lag: 6 }, { transform: 'magic' }, { from: '2024' }]) assert.throws(() => validateInvestigationState('signal', bad));
  assert.deepEqual(validateInvestigationState('county', { xMetric: 'csv_0', peerKeys: 'population,csv_0' }, { privateData: { columns: [{ key: 'csv_0' }] } }), { xMetric: 'csv_0', peerKeys: 'population,csv_0' });
});
test('notebook import previews and merges additively, canonical duplicates skip and conflicts are atomic', () => {
  const storage = memory(), first = entry('first');
  assert.deepEqual(previewNotebookImport(doc([first]), storage), { entries: [first], additions: 1, duplicates: 0, privateAttachments: 0 });
  assert.equal(storage.getItem(format), null, 'preview does not mutate');
  assert.deepEqual(importNotebook(doc([first]), storage), { added: 1, duplicates: 0, total: 1 });
  assert.equal(getLocalInvestigation('first', storage).title, first.title);
  const reordered = { ...first, state: Object.fromEntries(Object.entries(first.state).reverse()) };
  assert.deepEqual(importNotebook(doc([reordered, entry('second')]), storage), { added: 1, duplicates: 1, total: 2 });
  const before = storage.getItem(format);
  assert.throws(() => importNotebook(doc([entry('third'), { ...first, title: 'conflict' }]), storage), /conflicts/);
  assert.equal(storage.getItem(format), before);
  assert.throws(() => importNotebook(doc([first, first]), storage), /repeated/);
  assert.throws(() => getLocalInvestigation('bad/../id', storage));
});
test('notebook imports reject invalid state, wrong format, limits and corrupted destinations without mutation', () => {
  const storage = memory();
  for (const text of ['bad', JSON.stringify({ format: 'kfm-record-lab-v1', entries: [] }), doc([entry('bad', { state: { acsYear: 2020 } })]), doc(Array.from({ length: 13 }, (_, i) => entry('id-' + i))), ' '.repeat(2 * 1024 * 1024 + 1)]) assert.throws(() => importNotebook(text, storage));
  assert.equal(storage.getItem(format), null);
  storage.setItem(format, '{corrupt');
  assert.throws(() => importNotebook(doc([entry('first')]), storage), /unreadable/); assert.equal(storage.getItem(format), '{corrupt');
});
test('merge rechecks newly saved entries and storage quota before reporting success', () => {
  const storage = memory(), text = doc([entry('first')]); previewNotebookImport(text, storage);
  const saved = saveLocalInvestigation({ workspace: 'county', title: 'Another tab', state: { countyA: '20001' }, sourceBindings: currentSourceBindings('county') }, storage);
  assert.deepEqual(importNotebook(text, storage), { added: 1, duplicates: 0, total: 2 });
  assert.ok(JSON.parse(exportLocalInvestigations(storage)).entries.some(row => row.id === saved.id));
  assert.throws(() => importNotebook(text, { getItem: () => null, setItem: () => { throw new Error('quota'); } }), /could not save/);
});
test('private notebook round trip retains local values and validates private metric references', async () => {
  const storage = memory(), privateData = await readCountyCSV(new File(['FIPS,Local\n20001,42\n20003,NA'], 'local.csv'));
  const privateEntry = entry('private', { privateData, state: { countyA: '20001', xMetric: 'csv_0', peerKeys: 'population,csv_0' } });
  assert.equal(previewNotebookImport(doc([privateEntry]), storage).privateAttachments, 1);
  importNotebook(doc([privateEntry]), storage);
  assert.equal(getLocalInvestigation('private', storage).privateData.rows[0].csv_0, 42);
  assert.equal(getLocalInvestigation('private', storage).privateData.rows[1].csv_0, null);
  const clean = memory(); assert.throws(() => importNotebook(doc([{ ...privateEntry, workspace: 'signal', state: {} }]), clean), /cannot contain/);
  assert.throws(() => importNotebook(doc([{ ...privateEntry, state: { xMetric: 'csv_1' } }]), clean), /Unsupported/);
  assert.equal(clean.getItem(format), null);
});
test('capacity uses combined destination and damaged storage cannot be overwritten by save/delete', () => {
  const storage = memory(); importNotebook(doc(Array.from({ length: 12 }, (_, i) => entry('existing-' + i))), storage);
  const before = storage.getItem(format); assert.throws(() => importNotebook(doc([entry('new')]), storage), /12 investigations/); assert.equal(storage.getItem(format), before);
  storage.setItem(format, 'bad');
  assert.throws(() => saveLocalInvestigation({ workspace: 'county', title: 'New', state: {}, sourceBindings: currentSourceBindings('county') }, storage), /unreadable/);
  assert.equal(storage.getItem(format), 'bad');
});
