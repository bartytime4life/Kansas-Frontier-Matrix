import test from 'node:test';
import assert from 'node:assert/strict';
import { atlasCoverage, atlasFacts, atlasStatus, matchesAtlasStory, storyFromSearch, storyLocation } from './atlas-model.mjs';

const stories = [
  { id: 'river-memory', title: 'River Memory', kicker: 'Water', summary: 'Streamflow observations', group: 'Living record', sources: ['USGS'], status: 'ready' },
  { id: 'species', title: 'Species', kicker: 'Life', group: 'Data to come', sources: ['GBIF'], status: 'planned' },
];
test('availability uses a fetched snapshot rather than implementation status', () => {
  assert.equal(matchesAtlasStory(stories[0], { availability: 'ready' }), false);
  assert.equal(matchesAtlasStory(stories[0], { availability: 'ready', states: { 'river-memory': 'ready' } }), true);
  assert.equal(atlasStatus(stories[0], 'waiting').tone, 'waiting');
  assert.equal(atlasStatus(stories[1], 'ready').tone, 'planned');
});
test('catalogue searches source names and combines all terms with group filters', () => {
  assert.equal(matchesAtlasStory(stories[0], { query: 'USGS water', group: 'Living record' }), true);
  assert.equal(matchesAtlasStory(stories[0], { query: 'USGS water', group: 'Deep time' }), false);
  assert.equal(matchesAtlasStory(stories[0], { query: 'USGS fossil' }), false);
});
test('catalogue metadata counts present records and excludes missing categories', () => {
  assert.deepEqual(atlasFacts({ data: { records: [{ category: 'a' }, { category: 'b' }, { category: null }], categoryField: 'category', columns: [{ key: 'category' }] } }), [{ value: 3, label: 'source records' }, { value: 2, label: 'groups to compare' }]);
  assert.deepEqual(atlasFacts(null), []);
});
test('lab URLs preserve unrelated parameters and reject unknown story ids', () => {
  assert.equal(storyFromSearch('?story=river-memory', stories), 'river-memory');
  assert.equal(storyFromSearch('?story=missing', stories), null);
  assert.equal(storyLocation('http://localhost/labs?filter=water#research', 'river-memory'), '/labs?filter=water&story=river-memory#research');
  assert.equal(storyLocation('http://localhost/labs?filter=water&story=river-memory', null), '/labs?filter=water');
});
test('coverage preserves geological age direction and shortens calendar timestamps', () => {
  assert.equal(atlasCoverage({ observed: { from: '-121.8', to: '-69.1' }, data: { timeUnit: 'Ma' } }), '121.8–69.1 Ma');
  assert.equal(atlasCoverage({ observed: { from: '2010-09-10T08:37:17.480000+00:00', to: '2026-11-05T12:00:00Z' } }), '2010–2026');
  assert.equal(atlasCoverage(null), null);
});
