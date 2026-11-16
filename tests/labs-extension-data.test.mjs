import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { EXTENSION_LAB_SNAPSHOTS as snapshots } from '../app/labs/extension-snapshots.mjs';
import { validStoryBundle, STORY_BUNDLE_BYTES } from '../app/living-welcome/stories/story-bundle.mjs';
import { recordModel, filterRecords, recordsCSV } from '../app/living-welcome/stories/record-model.mjs';

const files = new Map(await Promise.all(Object.entries(snapshots).map(async ([id, entry]) => [id, await readFile(new URL('../public' + entry.path, import.meta.url))])));
const bundle = id => JSON.parse(files.get(id));

test('public science extensions bind valid bounded bundles to exact bytes and federal acquisition receipts', () => {
  assert.deepEqual(Object.keys(snapshots).sort(), ['air-and-health', 'energy-shift']);
  for (const [id, entry] of Object.entries(snapshots)) {
    const raw = files.get(id), b = bundle(id);
    assert.equal(raw.length, entry.bytes);
    assert.ok(raw.length <= STORY_BUNDLE_BYTES);
    assert.equal(createHash('sha256').update(raw).digest('hex'), entry.sha256);
    assert.equal(b.data.records.length, entry.records);
    assert.deepEqual(b.observed, entry.observed);
    assert.ok(validStoryBundle(b, id), id);
    assert.match(entry.path, new RegExp(`^/labs-data-extension/${id}-[a-f0-9]{16}\\.json$`));
    assert.ok(Date.parse(entry.retrievedAt));
    assert.equal(new Set(b.data.records.map(row => row.id)).size, entry.records);
    for (const source of b.data.sourceSnapshots) {
      assert.match(source.rawSha256, /^[a-f0-9]{64}$/);
      assert.ok(source.rawBytes > 0 && source.rawBytes <= 50_000_000);
      assert.ok(Date.parse(source.retrievedAt));
      assert.match(new URL(source.url).hostname, /(?:^|\.)(?:eia|epa|census)\.gov$/);
    }
    for (const source of b.sources) {
      assert.match(source.license, /public.domain/);
      assert.ok(source.citation.length > 30);
    }
  }
});

test('Energy Shift retains 26 complete Kansas annual series in one unit and separate accounting views', () => {
  const b = bundle('energy-shift'), d = b.data, rows = d.records, model = recordModel(b);
  assert.equal(rows.length, 1690);
  assert.equal(model.categories.length, 26);
  assert.equal(d.temporalMode, 'events');
  assert.equal(d.seriesPeriod, 'year');
  assert.equal(d.dateField, undefined, 'annual source data never acquire a fabricated daily date');
  assert.deepEqual(model.metrics.map(column => column.key), ['value']);
  assert.deepEqual([...new Set(rows.map(row => row.unit))], ['Billion Btu']);
  assert.deepEqual([...new Set(rows.map(row => row.flow))].sort(), ['Consumption', 'Production']);
  for (const label of model.categories) {
    const selected = filterRecords(model, { controls: { category: label } });
    assert.equal(selected.length, 65);
    assert.deepEqual(selected.map(row => row.year), Array.from({ length: 65 }, (_, i) => 1960 + i));
    assert.equal(new Set(selected.map(row => row.seriesId)).size, 1);
    for (const row of selected) {
      assert.match(row.seriesId, /^SEDS\.[A-Z]{5}\.KS\.A$/);
      assert.equal(row.id, `${row.seriesId}/${row.year}`);
      assert.ok(row.name.endsWith(', Kansas'));
      assert.ok(row.value === null || (Number.isFinite(row.value) && row.value >= 0));
    }
  }
  const total = rows.find(row => row.seriesId === 'SEDS.TETCB.KS.A' && row.year === 2024);
  assert.equal(total.value, 959338, 'Kansas annual total consumption anchor from EIA bulk source');
  const coal = rows.find(row => row.seriesId === 'SEDS.CLPRB.KS.A' && row.year === 2024);
  assert.equal(coal.value, 0, 'reported zero production remains zero');
  assert.ok(d.limits.some(limit => /overlap/.test(limit)));
  assert.ok(d.limits.some(limit => /Do not sum all displayed series/.test(limit)));
  assert.equal(recordsCSV(b, { controls: { category: 'Wind production', from: 2000, to: 2024 } }).rows.length, 26);
});

test('Air Quality selects one annual cohort and makes sparse county monitoring explicit', () => {
  const b = bundle('air-and-health'), d = b.data, model = recordModel(b);
  assert.equal(d.records.length, 333);
  assert.equal(model.categories.length, 17);
  assert.equal(d.temporalMode, 'snapshot');
  assert.equal(d.categoryField, 'name');
  assert.deepEqual([model.first, model.last], [2000, 2025]);
  assert.equal(filterRecords(model).length, 12, 'default selection is latest annual cohort');
  for (let year = 2000; year <= 2025; year++) {
    const selected = filterRecords(model, { time: year });
    assert.equal(selected.length, d.coverageByYear[year]);
    assert.ok(selected.length >= 11 && selected.length <= 16);
    assert.equal(new Set(selected.map(row => row.fips)).size, selected.length);
    assert.ok(selected.every(row => row.year === year && row.geometry && /^20\d{3}$/.test(row.fips)));
  }
  assert.equal(recordsCSV(b, { time: 2025 }).rows.length, 13);
  assert.ok(d.limits.some(limit => /Unmonitored counties are missing/.test(limit)));
  assert.ok(d.limits.some(limit => /not counts of violations/.test(limit)));
  assert.equal(d.sourceSnapshots.length, 27, '26 EPA annual responses plus the Census geometry response');
});

test('Air Quality denominators, categories and derived percentages reconcile without inventing exposure outcomes', () => {
  const rows = bundle('air-and-health').data.records;
  for (const row of rows) {
    const calendarDays = new Date(Date.UTC(row.year + 1, 0, 1)) - new Date(Date.UTC(row.year, 0, 1));
    const days = calendarDays / 86_400_000;
    assert.ok(row.daysWithAqi > 0 && row.daysWithAqi <= days);
    const categories = ['goodDays', 'moderateDays', 'sensitiveDays', 'unhealthyDays', 'veryUnhealthyDays', 'hazardousDays'];
    assert.equal(categories.reduce((sum, key) => sum + row[key], 0), row.daysWithAqi);
    assert.equal(row.daysAbove100, row.sensitiveDays + row.unhealthyDays + row.veryUnhealthyDays + row.hazardousDays);
    assert.ok(Math.abs(row.coveragePct - 100 * row.daysWithAqi / days) <= .0051);
    assert.ok(Math.abs(row.goodPct - 100 * row.goodDays / row.daysWithAqi) <= .0051);
    assert.ok(Math.abs(row.above100Pct - 100 * row.daysAbove100 / row.daysWithAqi) <= .0051);
    assert.ok(row.medianAqi <= row.aqi90th && row.aqi90th <= row.maxAqi);
  }
  assert.ok(rows.some(row => row.coveragePct < 25), 'sparse annual monitoring must remain visible');
  const sumner = rows.find(row => row.fips === '20191' && row.year === 2025);
  assert.equal(sumner.maxAqi, 370, 'EPA source extreme preserved without suppression or relabeling');
  assert.equal(sumner.hazardousDays, 1);
  assert.equal(sumner.daysWithAqi, 365);
});

test('acquisition parser preserves blank EPA values and rejects malformed numeric values and tampered cache bytes', () => {
  const script = new URL('../scripts/prepare-labs-science-data.py', import.meta.url);
  const result = spawnSync('python3', ['-c', `
import importlib.util, pathlib, tempfile, json, sys
spec = importlib.util.spec_from_file_location('science', sys.argv[1])
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
assert mod.number('') is None and mod.number('  ') is None and mod.number(None) is None
assert mod.number('0') == 0 and mod.number('365') == 365
for value in ['NaN', 'Infinity', '-1', '2.5']:
    try: mod.number(value)
    except ValueError: pass
    else: raise AssertionError(value)
with tempfile.TemporaryDirectory() as name:
    cache = pathlib.Path(name)
    url = mod.SEDS_URL
    key = mod.sha(url.encode())
    (cache / (key + '.raw')).write_bytes(b'tampered')
    (cache / (key + '.json')).write_text(json.dumps({'url':url,'rawSha256':mod.sha(b'original'),'rawBytes':8}))
    try: mod.Fetcher(cache, offline=True).get(url)
    except ValueError: pass
    else: raise AssertionError('tampered cache accepted')
` , script.pathname], { encoding: 'utf8' });
  assert.equal(result.status, 0, result.stderr || result.stdout);
});
