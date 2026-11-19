import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { matchesAtlasStory } from '../app/labs/atlas-model.mjs';
import { BRIDGE_LAB_SNAPSHOTS } from '../app/labs/bridge-snapshots.mjs';
import { bridgeInventoryHref, bridgeMarker } from '../app/labs/then-now/crossing.mjs';
import { decodeLabView } from '../app/labs/view-state.mjs';
import { filterRecords, recordModel } from '../app/living-welcome/stories/record-model.mjs';
import { storyById } from '../app/living-welcome/stories/registry.mjs';

const pair = JSON.parse(await readFile(new URL('../app/labs/then-now/pair.json', import.meta.url), 'utf8'));
const crossing = JSON.parse(await readFile(new URL('../app/labs/then-now/crossing.json', import.meta.url), 'utf8'));

test('Garden City imagery retains a single RGB footprint and verifies both bundled display copies', async () => {
  assert.equal(pair.license, 'CC0 1.0');
  assert.deepEqual(pair.editions.map(edition => edition.year), [2021, 2024]);
  const { crs, bounds, width, height } = pair.footprint;
  assert.equal(crs, 'EPSG:3857');
  assert.deepEqual([bounds[2] - bounds[0], bounds[3] - bounds[1]], [width, height]);
  assert.deepEqual([width, height], [768, 768]);
  assert.equal(new Set(pair.editions.map(edition => edition.sourceSha256)).size, 2);
  assert.equal(new Set(pair.editions.map(edition => edition.previewSha256)).size, 2);
  for (const edition of pair.editions) {
    const original = new URL(edition.export);
    assert.equal(original.protocol, 'https:');
    assert.equal(original.searchParams.get('bbox'), bounds.join(','));
    assert.equal(original.searchParams.get('imageSR'), '3857');
    assert.equal(original.searchParams.get('bandIds'), '0,1,2');
    assert.equal(original.searchParams.get('size'), '768,768');
    assert.match(edition.sourceSha256, /^[a-f0-9]{64}$/);
    assert.equal(edition.preview, `/labs/then-now/garden-city-${edition.year}.webp`);
    const file = await readFile(new URL(`../public${edition.preview}`, import.meta.url));
    assert.equal(file.toString('ascii', 8, 12), 'WEBP');
    assert.equal(createHash('sha256').update(file).digest('hex'), edition.previewSha256);
  }
});

test('Garden City is discoverable as a guided comparison of fixed public imagery', () => {
  const story = storyById('kansas-then-and-now');
  assert.equal(story.status, 'guided');
  assert.equal(story.href, '/labs/then-now');
  assert.ok(matchesAtlasStory(story, { query: 'Garden City river', availability: 'available' }));
});

test('the bridge point aligns with both images at the inventory coordinates', () => {
  const { left, top } = bridgeMarker(crossing.location, pair.footprint.bounds);
  assert.equal(Number.parseFloat(left).toFixed(2), '48.45');
  assert.equal(Number.parseFloat(top).toFixed(2), '72.41');
});

test('the bridge link selects exactly one record and is held when the snapshot changes', async () => {
  const story = 'built-kansas';
  const snapshot = BRIDGE_LAB_SNAPSHOTS[story];
  const url = new URL(bridgeInventoryHref(crossing), 'http://localhost');
  assert.equal(url.pathname, '/labs');
  assert.equal(url.searchParams.get('story'), story);
  const options = decodeLabView(url.searchParams.get('view'), { story, snapshotSha256: snapshot.sha256 });
  assert.ok(options);
  const bundle = JSON.parse(await readFile(new URL(`../public${snapshot.path}`, import.meta.url), 'utf8'));
  const records = filterRecords(recordModel(bundle), options);
  assert.equal(records.length, 1);
  const [record] = records;
  assert.equal(options.controls.selectedId, record.id);
  assert.equal(record.id, crossing.snapshot.recordId);
  assert.equal(record.structure, crossing.structure);
  assert.equal(record.county, crossing.county);
  assert.equal(record.crossing, 'ARKANSAS RIVER');
  assert.equal(record.year, 2024);
  assert.ok(Math.abs(record.longitude - crossing.location[0]) < 0.00002);
  assert.ok(Math.abs(record.latitude - crossing.location[1]) < 0.00002);
  assert.equal(bridgeInventoryHref(crossing, { ...snapshot, sha256: '0'.repeat(64) }), null);
  assert.equal(new URL(crossing.inventoryQuery).searchParams.get('where'), `PROJECT_NUMBER='${crossing.project}'`);
});
