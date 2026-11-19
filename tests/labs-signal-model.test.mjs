import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { annualSignal, analyzeSignals, signalCatalog, SIGNAL_PRESETS } from '../app/labs/signal-model.mjs';
import { PUBLIC_LAB_SNAPSHOTS } from '../app/labs/public-snapshots.mjs';
const energy = (xs, ys) => ({ 'energy-shift': { data: { records: [...xs.map(([year, value]) => ({ year, value, seriesId: 'X', name: 'X', unit: 'unit' })), ...ys.map(([year, value]) => ({ year, value, seriesId: 'Y', name: 'Y', unit: 'unit' }))] } } });
const controls = { x: 'energy:X', y: 'energy:Y', from: 2000, to: 2005, lag: 0, transform: 'raw' };
test('positive lag joins X(t) to later Y(t+lag), with both years inside selection', () => {
  const bundles = energy([[2000, 1], [2001, 4], [2002, 2], [2003, 8]], [[2001, 2], [2002, 8], [2003, 4], [2004, 16]]), fit = analyzeSignals(bundles, { ...controls, lag: 1 });
  assert.equal(fit.count, 4); assert.equal(fit.pearson, 1); assert.equal(fit.slope, 2); assert.deepEqual(fit.pairs.map(row => [row.xYear, row.yYear]), [[2000, 2001], [2001, 2002], [2002, 2003], [2003, 2004]]);
  assert.equal(analyzeSignals(bundles, { ...controls, lag: 1, to: 2003 }).count, 3);
  assert.equal(fit.lagProfile.find(row => row.lag === 1).pearson, 1);
});
test('first difference never bridges missing calendar years and standardized values use all transformed pairs', () => {
  const data = [[2000, 1], [2001, 3], [2003, 8], [2004, 9], [2005, 12]], fit = analyzeSignals(energy(data, data), { ...controls, transform: 'difference' });
  assert.deepEqual(fit.pairs.map(row => [row.year, row.x]), [[2001, 2], [2004, 1], [2005, 3]]);
  assert.equal(fit.pearson, 1); assert.ok(Math.abs(fit.pairs.reduce((sum, row) => sum + row.zX, 0)) < 1e-12);
});
test('detrending removes a shared linear passage of time and suppresses constant residual correlation', () => {
  const fit = analyzeSignals(energy([[2000, 1], [2001, 2], [2002, 3], [2003, 4]], [[2000, 10], [2001, 20], [2002, 30], [2003, 40]]), { ...controls, transform: 'detrended' });
  assert.equal(fit.pearson, null); assert.ok(fit.pairs.every(row => row.x === 0 && row.zX === null));
});
test('annual climate requires all twelve monthly values and preserves source scale and sum', () => {
  const bundle = { data: { years: [2024, 2025], elements: { pcpn: { scale: 100, annual: 'sum', unit: 'in' } }, values: { pcpn: { '20': [...Array(12).fill(100), ...Array(11).fill(200), null] } } } };
  const result = annualSignal(bundle, { kind: 'climate', area: '20', element: 'pcpn' });
  assert.equal(result.rows[0].value, 12); assert.equal(result.rows.length, 1); assert.equal(result.excluded[0].count, 11);
});
test('river annual eligibility counts leap-year days and excludes partial calendar years', () => {
  const rows = (year, count) => Array.from({ length: count }, (_, index) => ({ year, date: new Date(Date.UTC(year, 0, index + 1)).toISOString().slice(0, 10), siteCode: 'A', discharge: 10 }));
  const result = annualSignal({ built_at: '2026-11-16', data: { records: [...rows(2024, 329), ...rows(2025, 329), ...rows(2026, 330)] } }, { kind: 'river', site: 'A' });
  assert.deepEqual(result.rows.map(row => row.year), [2025]); assert.equal(result.excluded[0].expected, 366); assert.match(result.excluded[1].reason, /progress/);
});
test('event zeros occur only within declared completed coverage and unknown impact is not zero', () => {
  const bundle = { built_at: '2026-11-16', observed: { from: '2023', to: '2026' }, data: { records: [{ year: 2024, fatalities: null, magnitude: 3 }] } };
  assert.deepEqual(annualSignal(bundle, { kind: 'quake', measure: 'count' }).rows.map(row => [row.year, row.value]), [[2023, 0], [2024, 1], [2025, 0]]);
  assert.deepEqual(annualSignal(bundle, { kind: 'tornado', measure: 'fatalities' }).rows.map(row => [row.year, row.value]), [[2023, 0], [2025, 0]]);
  assert.equal(annualSignal(bundle, { kind: 'quake', measure: 'maxMagnitude' }).rows.length, 1);
});
test('shipping presets resolve real source signals and complete years; empty and reversed selections fail gracefully', () => {
  const bundles = Object.fromEntries(['climate-stripes', 'energy-shift', 'river-memory', 'tornado-tracks', 'shaking-ground'].map(id => [id, JSON.parse(fs.readFileSync(new URL('../public' + PUBLIC_LAB_SNAPSHOTS[id].path, import.meta.url)))]));
  const catalog = signalCatalog(bundles); assert.equal(catalog.length, 66);
  for (const preset of SIGNAL_PRESETS) { const result = analyzeSignals(bundles, preset.controls); assert.ok(result.count >= 3, preset.id); assert.ok(result.pairs.every(row => row.xYear <= 2025 && row.yYear <= 2025)); assert.ok(Object.keys(result.bindings).length >= 1); }
  const river = analyzeSignals(bundles, SIGNAL_PRESETS.find(row => row.id === 'rain-and-river').controls); assert.equal(river.count, 6);
  assert.equal(analyzeSignals().count, 0); assert.match(analyzeSignals(bundles, { ...SIGNAL_PRESETS[0].controls, from: 2025, to: 2000 }).reason, /Start year/);
});
