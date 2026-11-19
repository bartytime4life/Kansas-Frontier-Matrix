import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import { storyById } from '../app/living-welcome/stories/registry.mjs';
import { matchesAtlasStory } from '../app/labs/atlas-model.mjs';

const snapshot = JSON.parse(await readFile(new URL('../app/labs/drought-replay/snapshot.json', import.meta.url), 'utf8'));
const dateAt = (start, offset) => {
  const day = new Date(`${start}T00:00:00Z`);
  day.setUTCDate(day.getUTCDate() + offset);
  return day.toISOString().slice(0, 10);
};

test('the Finney County replay pairs consecutive validity windows with distinct USGS daily means', () => {
  assert.equal(snapshot.county.fips, '20055');
  assert.deepEqual(
    [snapshot.station.id, snapshot.station.parameter, snapshot.station.statistic, snapshot.station.approval],
    ['USGS-07139000', '00060', '00003', 'Approved'],
  );
  assert.equal(snapshot.weeks.length, 17);
  assert.equal(snapshot.dailyFlow.length, 119);
  assert.equal(new Set(snapshot.dailyFlow.map(row => row.id)).size, 119);
  for (const [index, week] of snapshot.weeks.entries()) {
    assert.equal(week.validFrom, dateAt('2012-06-05', index * 7));
    assert.equal(week.validThrough, dateAt(week.validFrom, 6));
    assert.equal(week.shares.length, 5);
    assert.ok(week.shares.every(share => Number.isFinite(share) && share >= 0 && share <= 100));
    assert.deepEqual(week.shares, week.shares.toSorted((a, b) => b - a));
    const selected = snapshot.dailyFlow.slice(index * 7, (index + 1) * 7);
    assert.deepEqual(selected.map(row => row.date), Array.from({ length: 7 }, (_, day) => dateAt(week.validFrom, day)));
    assert.ok(selected.every(row => row.value === 0));
  }
  assert.equal(snapshot.weeks[0].shares[4], 0);
  assert.equal(snapshot.weeks.find(week => week.shares[4] === 100).validFrom, '2012-08-07');
  assert.equal(snapshot.weeks.at(-1).shares[4], 83.62);
  for (const source of Object.values(snapshot.sources)) assert.match(source.sha256, /^[a-f0-9]{64}$/);
});

test('the drought replay appears as a guided investigation in the existing Labs discovery', () => {
  const story = storyById('drought-replay-2012');
  assert.equal(story.status, 'guided');
  assert.equal(story.href, '/labs/drought-replay');
  assert.ok(matchesAtlasStory(story, { query: 'finney drought', availability: 'available' }));
});
