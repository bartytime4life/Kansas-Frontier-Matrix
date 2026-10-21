import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
import vm from 'node:vm';
import { componentHarness } from './component-harness.mjs';

const topics = await componentHarness('app/layer-workspaces.ts', {});
const startup = await componentHarness('app/explorer-startup.ts', { './layer-workspaces': topics.exports });
const destination = search => startup.exports.hasExplorerDestination(new URLSearchParams(search));

test('all catalogue subjects and existing tool links are intentional destinations', () => {
  for (const topic of topics.exports.TOPIC_STRUCTURE) {
    assert.equal(destination(`topic=${topic.id}`), true, topic.id);
    for (const resource of topic.resources) {
      if (resource.href.startsWith('/?')) assert.equal(destination(resource.href.slice(2)), true, resource.href);
    }
  }
});

test('source-status compatibility, explicit views and shared URLs bypass welcome', () => {
  for (const search of ['layers=sources', 'maptab=localAtlas', 'topic=all', 'layerView=imagery', 'layerView=selected', 'mapui=open', 'tm=comparison', 'c=-98.2,38.6&z=7&t=2026', 'f=shared-record']) {
    assert.equal(destination(search), true, search);
  }
});

test('plain startup and unrelated or invalid query values retain welcome', () => {
  for (const search of ['', 'utm_source=topics', 'topic=', 'topic=unknown', 'topic=__proto__', 'mapui=closed', 'maptab=measure', 'layerView=unknown', 'c=,', 'c=no,38', 'c=1,2,3']) {
    assert.equal(destination(search), false, search);
  }
  assert.equal(startup.exports.hasExplorerDestination(new URLSearchParams('c=-98,38&mapui=closed'), new URLSearchParams()), false, 'automatically saved default camera is not an explicit destination');
});

test('actual restoration decision reads incoming state once, closes on history and never persists bypass', async () => {
  const page = await readFile('app/page.tsx', 'utf8');
  const source = page.slice(page.indexOf('      const hasDestination = hasExplorerDestination('), page.indexOf('      setStarterPanelOpen(', page.indexOf('  const restoreExplorerFromUrl')));
  assert.ok(source.includes('setGuideOpen'), 'execute the production decision, not a copied model');
  const decide = (search, restored, dismissed, current = false, focused = false) => {
    let open = current, focusReturns = 0, preferenceReads = 0;
    vm.runInNewContext(ts.transpile(source), {
      params: new URLSearchParams(search), hasExplorerDestination: startup.exports.hasExplorerDestination,
      URLSearchParams, window: { location: { search } },
      explorerRestoredRef: { current: restored }, setGuideOpen: value => { open = value; }, setWelcomeSourcesOpen: () => {},
      readExplorerGuideDismissed: () => { preferenceReads++; return dismissed; },
      document: { activeElement: { closest: () => focused }, querySelector: () => ({ focus: () => { focusReturns++; } }) },
    });
    return { open, focusReturns, preferenceReads };
  };
  assert.equal(decide('', false, false).open, true);
  assert.equal(decide('', false, true).open, false);
  assert.deepEqual(decide('topic=water', false, false), { open: false, focusReturns: 0, preferenceReads: 0 });
  assert.deepEqual(decide('mapui=open', true, false, true, true), { open: false, focusReturns: 1, preferenceReads: 0 });
  assert.equal(decide('', true, false).open, false, 'history never automatically reopens welcome');
  assert.equal(decide('', true, false, true).open, true, 'plain history does not close manual help');
});

test('v2 opt-out remains explicit, legacy and blocked storage retain welcome', async () => {
  const values = new Map([['kfm.explorer.guide.dismissed.v1', '1']]);
  const storage = { getItem: key => values.get(key) ?? null, setItem: (key, value) => values.set(key, value), removeItem: key => values.delete(key) };
  const guide = await componentHarness('app/explorer-guide.tsx', { './map-starters': {} }, { window: { localStorage: storage } });
  assert.equal(guide.exports.readExplorerGuideDismissed(), false);
  guide.exports.writeExplorerGuideDismissed(true);
  assert.equal(guide.exports.readExplorerGuideDismissed(), true);
  guide.exports.writeExplorerGuideDismissed(false);
  assert.equal(guide.exports.readExplorerGuideDismissed(), false);
  assert.equal(values.get('kfm.explorer.guide.dismissed.v1'), '1');
  storage.getItem = storage.setItem = storage.removeItem = () => { throw new Error('storage blocked'); };
  assert.equal(guide.exports.readExplorerGuideDismissed(), false);
  assert.doesNotThrow(() => guide.exports.writeExplorerGuideDismissed(true));
});
