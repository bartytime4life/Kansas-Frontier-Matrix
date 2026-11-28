import assert from 'node:assert/strict';
import { readFile, readdir } from 'node:fs/promises';
import test from 'node:test';
import { PUBLIC_LAB_SNAPSHOTS } from '../app/labs/public-snapshots.mjs';
import { STORIES } from '../app/living-welcome/stories/registry.mjs';
import { atlasScienceDirectory } from '../app/science/atlas-directory.mjs';
import { filterScienceDirectory, nativeScienceDirectory } from '../app/science/science-directory.mjs';

const manifests = {
  climate: 'heat-and-rain',
  drought: 'county-drought',
  soil: 'soil-profile',
  air: 'daily-air-quality',
  sunlight: 'sunlight-and-sky',
};
const native = nativeScienceDirectory(Object.fromEntries(await Promise.all(
  Object.entries(manifests).map(async ([key, lab]) => {
    const content = await readFile(new URL(`../app/labs/${lab}/snapshot-manifest.json`, import.meta.url), 'utf8');
    return [key, JSON.parse(content)];
  }),
)));
const entries = atlasScienceDirectory(native);
const origin = 'https://kansasfrontiermatrix.com';

test('hosted science directory opens real lab pages, tools and bundled Atlas stories', async () => {
  for (const { href } of entries) {
    const url = new URL(href, origin);
    assert.equal(url.origin, origin);
    const files = await readdir(new URL(`../app${url.pathname}/`, import.meta.url));
    assert.ok(files.some(file => /^page\.[jt]sx?$/.test(file)), `${href} has an application route`);

    if (url.search) {
      assert.equal(url.pathname, '/labs');
      assert.deepEqual([...url.searchParams.keys()], ['story']);
      const id = url.searchParams.get('story');
      assert.ok(STORIES.some(story => story.id === id && story.status === 'ready'), `${href} has a ready story`);
      const snapshot = PUBLIC_LAB_SNAPSHOTS[id];
      assert.ok(snapshot?.path, `${href} has a bundled source entry`);
      await readFile(new URL(`../public${snapshot.path}`, import.meta.url));
    }
  }
});

test('the directory preserves unique native entries and leaves planned stories out', () => {
  assert.deepEqual(entries.slice(0, native.length), native);
  assert.equal(new Set(entries.map(entry => entry.id)).size, entries.length);
  assert.equal(new Set(entries.map(entry => entry.href)).size, entries.length);
  const routes = new Set(entries.map(entry => entry.href));
  for (const story of STORIES.filter(story => story.status === 'planned')) {
    assert.ok(!routes.has(story.href ?? `/labs?story=${encodeURIComponent(story.id)}`), story.id);
    assert.ok(entries.every(entry => entry.id !== `atlas-${story.id}`), story.id);
  }
  for (const route of ['/labs/observatory', '/labs/signals', '/labs/notebook', '/science/wheat-trade']) {
    assert.ok(entries.some(entry => entry.href === route && entry.kind === 'Workspace'), route);
  }
});

test('flow questions and USGS source searches both find River Flow', () => {
  const flow = filterScienceDirectory(entries, 'River flow', '').map(entry => entry.href);
  assert.ok(flow.includes('/labs/river-flow'));
  assert.ok(flow.includes('/labs?story=river-memory'));
  const usgs = filterScienceDirectory(entries, 'USGS', '').map(entry => entry.href);
  assert.ok(usgs.includes('/labs/river-flow'));
  assert.ok(usgs.includes('/labs/water-chemistry'));
});

test('search finds the earthquake threshold lab by catalog or epicenters', () => {
  for (const query of ['ComCat', 'epicenters', 'magnitude threshold']) {
    assert.ok(filterScienceDirectory(entries, query, '').some(entry => entry.href === '/labs/earthquakes'), query);
  }
});


test('population accounting questions discover the existing County Observatory', () => {
  for (const query of ['births deaths', 'migration remainder', 'population components']) {
    assert.ok(filterScienceDirectory(entries, query, '').some(entry => entry.href === '/labs/observatory'), query);
  }
});
