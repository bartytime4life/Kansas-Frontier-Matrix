import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { matchesAtlasStory } from '../app/labs/atlas-model.mjs';
import { storyById } from '../app/living-welcome/stories/registry.mjs';

const stops = JSON.parse(await readFile(new URL('../app/labs/fort-larned/stops.json', import.meta.url), 'utf8'));

test('Fort Larned appears in the guided catalog under Historic Places', () => {
  const story = storyById('historic-places');
  assert.equal(story.status, 'guided');
  assert.equal(story.href, '/labs/fort-larned');
  assert.ok(matchesAtlasStory(story, { query: 'Fort Larned', availability: 'available' }));
});

test('the three compass stops use the exact named Library of Congress photographs', async () => {
  assert.deepEqual(stops.map(({ id, side }) => [id, side]), [
    ['barracks', 'North'], ['quarters', 'West'], ['commissary', 'South'],
  ]);
  for (const stop of stops) {
    const photo = new URL(stop.photo);
    const original = new URL(stop.original);
    const match = photo.pathname.match(/\/(ks\d{4})\.photos\.(\d{6}p)\/$/);
    assert.ok(match);
    assert.equal(photo.origin, 'https://www.loc.gov');
    assert.equal(original.origin, 'https://tile.loc.gov');
    assert.ok(original.pathname.endsWith(`/${match[1]}/photos/${match[2]}v.jpg`));
    const bytes = await readFile(new URL(`../public/labs/fort-larned/${stop.id}.jpg`, import.meta.url));
    assert.equal(bytes.readUInt16BE(0), 0xffd8);
    assert.equal(createHash('sha256').update(bytes).digest('hex'), stop.sha256);
  }
});
