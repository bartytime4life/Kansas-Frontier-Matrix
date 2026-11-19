import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { matchesAtlasStory } from '../app/labs/atlas-model.mjs';
import { storyById } from '../app/living-welcome/stories/registry.mjs';

const pair = JSON.parse(await readFile(new URL('../app/labs/then-now/pair.json', import.meta.url), 'utf8'));

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
