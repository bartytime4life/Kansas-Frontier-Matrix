import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createHash, webcrypto } from 'node:crypto';
import { PUBLIC_LAB_SNAPSHOTS as snapshots } from '../app/labs/public-snapshots.mjs';
import { loadPublicLabSnapshot } from '../app/labs/snapshot-loader.mjs';
import { validStoryBundle, storyBundleByteLimit } from '../app/living-welcome/stories/story-bundle.mjs';
import { recordModel, filterRecords, recordsCSV } from '../app/living-welcome/stories/record-model.mjs';
import { matchesAtlasStory } from '../app/labs/atlas-model.mjs';
import { storyById } from '../app/living-welcome/stories/registry.mjs';

const files = new Map(await Promise.all(Object.entries(snapshots).map(async ([id, entry]) => [id, await readFile(new URL('../public' + entry.path, import.meta.url))])));
const data = id => JSON.parse(files.get(id));

test('all eight shipping bundles are bounded, valid and bound to their exact file bytes', () => {
  assert.deepEqual(Object.keys(snapshots).sort(), ['air-and-health', 'built-kansas', 'census-mosaic', 'climate-stripes', 'energy-shift', 'river-memory', 'shaking-ground', 'tornado-tracks']);
  for (const [id, entry] of Object.entries(snapshots)) {
    const raw = files.get(id), bundle = data(id);
    assert.equal(raw.length, entry.bytes);
    assert.ok(raw.length <= storyBundleByteLimit(id));
    assert.equal(createHash('sha256').update(raw).digest('hex'), entry.sha256);
    assert.ok(validStoryBundle(bundle, id), id);
    assert.match(entry.path, new RegExp(`^/labs-data(?:-extension|-bridges)?/${id}-[a-f0-9]{16}\\.json$`));
    for (const source of bundle.data.sourceSnapshots) {
      assert.match(source.rawSha256, /^[a-f0-9]{64}$/);
      assert.ok(source.rawBytes > 0);
      assert.ok(Date.parse(source.retrievedAt));
      assert.match(new URL(source.url).hostname, /(?:^|\.)(?:noaa\.gov|census\.gov|usgs\.gov|eia\.gov|epa\.gov|ksdot\.gov)$/);
    }
    assert.equal(matchesAtlasStory(storyById(id), { availability: 'available' }), true);
  }
  assert.equal(matchesAtlasStory(storyById('iron-horse'), { availability: 'available' }), false);
});

test('the public loader rejects failed responses, tampering and held IDs without reading PC datasets', async () => {
  const id = 'climate-stripes';
  let calls = 0;
  const fetcher = async path => {
    calls++;
    assert.equal(path, snapshots[id].path);
    return new Response(files.get(id));
  };
  const reply = await loadPublicLabSnapshot(id, { fetcher, digest: webcrypto.subtle });
  assert.equal(reply.state, 'ready');
  assert.equal(reply.bundle.story, id);
  for (const held of ['iron-horse', 'shifting-lines', '../secrets', '__proto__']) {
    assert.equal((await loadPublicLabSnapshot(held, { fetcher })).state, 'waiting');
  }
  assert.equal(calls, 1);
  assert.equal((await loadPublicLabSnapshot(id, { fetcher: async () => new Response('bad gateway', { status: 503 }) })).state, 'offline');
  const raw = files.get(id).toString();
  await assert.rejects(loadPublicLabSnapshot(id, { fetcher: async () => new Response(raw + ' '), digest: webcrypto.subtle }), /size mismatch/);
  await assert.rejects(loadPublicLabSnapshot(id, { fetcher: async () => new Response(raw.replace('1895', '1896')), digest: webcrypto.subtle }), /integrity mismatch/);
});

test('climate contains NOAA Kansas state and nine divisions, missing future months and reproducible baseline means', () => {
  const d = data('climate-stripes').data;
  assert.equal(d.years[0], 1895);
  assert.equal(d.areas.length, 10);
  assert.deepEqual(d.values.tmpc['20'].slice(0, 3), [235, 239, 420], 'NOAA state code 014, not FIPS 20 or another state');
  for (const element of ['tmpc', 'pcpn', 'pdsi']) {
    for (const area of d.areas) {
      const flat = d.values[element][area.id];
      assert.equal(flat.length, d.years.length * 12);
      if (element === 'pcpn') assert.ok(flat.every(v => v === null || v >= 0), 'precipitation missing sentinel is never rain');
      for (let month = d.latest.month; month < 12; month++) assert.equal(flat[(d.latest.year - 1895) * 12 + month], null);
    }
  }
  for (const baseline of d.baselines) {
    const [first, last] = baseline.split('-').map(Number);
    for (const element of ['tmpc', 'pcpn']) for (const area of d.areas) for (let month = 0; month < 12; month++) {
      const sum = Array.from({ length: last - first + 1 }, (_, i) => d.values[element][area.id][(first + i - 1895) * 12 + month]).reduce((a, b) => a + b, 0);
      assert.ok(Math.abs(d.normals[baseline][element][area.id][month] - sum / (last - first + 1)) <= .501);
    }
  }
});

test('County Pulse selects all 105 counties in one year and exports exactly the selected source rows', () => {
  const b = data('census-mosaic'), model = recordModel(b);
  assert.equal(model.records.length, 630);
  for (let year = 2020; year <= 2025; year++) {
    const selected = filterRecords(model, { time: year });
    assert.equal(selected.length, 105);
    assert.equal(new Set(selected.map(r => r.fips)).size, 105);
    assert.ok(selected.every(r => r.year === year && r.population > 0 && r.geometry));
    const csv = recordsCSV(b, { time: year });
    assert.equal(csv.rows.length, 106);
    assert.ok(csv.rows[0].includes('snapshot_sha256'));
  }
  assert.equal(filterRecords(model, { controls: { query: 'Sedgwick' }, time: 2025 }).length, 1);
});

test('river records retain all three gauges, unique days and raw approval qualifiers', () => {
  const b = data('river-memory'), rows = b.data.records;
  assert.equal(new Set(rows.map(r => r.siteCode)).size, 3);
  assert.equal(new Set(rows.map(r => r.id)).size, rows.length);
  assert.ok(rows.length > 7000 && rows.length < 10000);
  assert.ok(rows.every(r => r.discharge === null || r.discharge >= 0));
  assert.ok(rows.some(r => r.qualifiers.includes('A')));
  const model = recordModel(b), gauge = model.categories[0];
  const selected = filterRecords(model, { controls: { category: gauge, from: 2025, to: 2025 } });
  assert.ok(selected.length > 300 && selected.length <= 366);
  assert.equal(recordsCSV(b, { controls: { category: gauge, from: 2025, to: 2025 } }).rows.length, selected.length + 1);
});

test('tornado identifiers retain two distinct source tracks sharing the 2002 SPC identifier', () => {
  const rows = data('tornado-tracks').data.records;
  assert.equal(rows.length, 4582);
  assert.equal(new Set(rows.map(r => r.id)).size, rows.length);
  const repeated = rows.filter(r => r.year === 2002 && r.sourceId === '506');
  assert.equal(repeated.length, 2);
  assert.notEqual(repeated[0].sourceTime, repeated[1].sourceTime);
  for (const row of rows) if (row.geometry) assert.ok(row.geometry.coordinates.every(([lon, lat]) => lon !== 0 && lat !== 0));
});

test('earthquake catalog is below its query cap and retains source IDs, bounds, magnitudes and record links', () => {
  const b = data('shaking-ground'), rows = b.data.records;
  assert.ok(rows.length > 6000 && rows.length < 10000);
  assert.equal(new Set(rows.map(r => r.id)).size, rows.length);
  for (const row of rows) {
    assert.ok(row.latitude >= 36.8 && row.latitude <= 40.1 && row.longitude >= -102.1 && row.longitude <= -94.5);
    assert.ok(row.magnitude >= 1);
    assert.match(row.url, /^https:\/\/earthquake\.usgs\.gov\//);
  }
  const model = recordModel(b), selected = filterRecords(model, { controls: { minValue: 4 } });
  assert.ok(selected.length > 0 && selected.every(r => r.magnitude >= 4));
});
