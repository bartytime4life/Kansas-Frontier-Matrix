import assert from 'node:assert/strict';
import test from 'node:test';
import { filterTopics } from '../app/living-welcome/topic-search.mjs';

const topics = [
  { id: 'water', title: 'Water & watersheds', group: 'Earth & environment', description: 'Follow rivers.', facets: ['Streamflow'], look: { name: 'River network' } },
  { id: 'history', title: 'History & cultural context', group: 'People & place', description: 'Explore archives.', facets: ['Historic maps'], look: { name: 'Historic atlas' }, limitation: 'Water records are unavailable.' },
];
test('topic search finds all words across navigation fields in any order', () => {
  assert.deepEqual(filterTopics(topics, 'network WATER'), [topics[0]]);
  assert.deepEqual(filterTopics(topics, '  RÍVER — streamflow  '), [topics[0]]);
  assert.deepEqual(filterTopics(topics, 'people historic'), [topics[1]]);
});
test('topic search intersects words and groups without changing source order or identity', () => {
  assert.deepEqual(filterTopics(topics, '', 'People & place'), [topics[1]]);
  assert.deepEqual(filterTopics(topics, 'rivers', 'People & place'), []);
  assert.deepEqual(filterTopics(topics, 'rivers archives'), []);
  assert.deepEqual(filterTopics(topics, '  —  '), topics);
  assert.equal(filterTopics(topics, '')[0], topics[0]);
});
test('limitations do not make unavailable subjects look like navigation matches', () => {
  assert.deepEqual(filterTopics(topics, 'water'), [topics[0]]);
  assert.deepEqual(filterTopics(topics, 'unavailable'), []);
});
