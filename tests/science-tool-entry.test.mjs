import assert from 'node:assert/strict';
import { readFile, access } from 'node:fs/promises';
import test from 'node:test';
import { componentHarness, findNode } from './component-harness.mjs';
import { STORIES, STORY_GROUPS, storyById } from '../app/living-welcome/stories/registry.mjs';
import { PUBLIC_LAB_SNAPSHOTS } from '../app/labs/public-snapshots.mjs';
import * as atlas from '../app/labs/atlas-model.mjs';

const ids = ['heat-and-rain', 'county-drought', 'soil-profile', 'daily-air-quality'];
const styles = new Proxy({}, { get: (_target, key) => String(key) });
function nodes(tree, predicate) {
  const found = [];
  function visit(node) {
    if (!node || typeof node !== 'object') return;
    if (predicate(node)) found.push(node);
    for (const child of [node.props?.children].flat(Infinity)) visit(child);
  }
  visit(tree);
  return found;
}

test('observation tools are direct guided routes and preserve the independent public snapshot boundary', async () => {
  for (const id of ids) {
    const story = storyById(id);
    assert.equal(story.status, 'guided');
    assert.equal(story.href, `/labs/${id}`);
    assert.equal(story.load, null);
    assert.equal(story.tables.length, 0);
    assert.equal(story.feeds.length, 0);
    assert.ok(!Object.hasOwn(PUBLIC_LAB_SNAPSHOTS, id));
    assert.match(story.summary, /2020–2025/);
    assert.match(story.limit, /review and dataset admission remain pending/);
    await access(`app${story.href}/page.tsx`);
    const manifest = JSON.parse(await readFile(`app${story.href}/snapshot-manifest.json`, 'utf8'));
    assert.equal(manifest.scope, 'provider-context');
  }
  assert.equal(storyById('drought-replay-2012').href, '/labs/drought-replay');
  assert.equal(storyById('water-chemistry').href, '/labs/water-chemistry');
  assert.equal(storyById('air-and-health').status, 'ready');
  assert.equal(storyById('air-and-health').relatedLab.href, '/labs/daily-air-quality');
  assert.ok(Object.hasOwn(PUBLIC_LAB_SNAPSHOTS, 'air-and-health'), 'the annual air story keeps its existing public snapshot');
});

test('the hosted atlas renders observation questions as links instead of opening a modal loader', async () => {
  const harness = await componentHarness('app/labs/page.jsx', {
    'next/link': { default: 'a' },
    '../living-welcome/stories/registry.mjs': { STORIES, STORY_GROUPS, storyById },
    '../living-welcome/stories/story-parts.jsx': {},
    '../living-welcome/stories/useStoryBundle.js': {},
    './atlas-model.mjs': atlas,
    './public-snapshots.mjs': { PUBLIC_LAB_SNAPSHOTS },
    '../living-welcome/stories/story-kit.mjs': {},
    '../living-welcome/stories/science-model.mjs': {},
    '../living-welcome/stories/stories.css': {},
    './page.module.css': { default: styles },
  });
  const tree = harness.render(harness.exports.default, {});
  const questions = findNode(tree, (node) => node.props?.['aria-labelledby'] === 'questions-title');
  const questionLinks = nodes(questions, (node) => node.type === 'a');
  for (const id of ids) {
    const link = questionLinks.find((node) => node.props.href === `/labs/${id}`);
    assert.ok(link, id);
    assert.equal(link.props.onClick, undefined, 'dedicated questions do not open StoryLab');
  }
  const navigation = findNode(tree, (node) => node.props?.['aria-label'] === 'Atlas navigation');
  assert.ok(findNode(navigation, (node) => node.type === 'a' && node.props.href === '/science'));
  harness.dispose();
});

test('Research Discovery keeps observation links in a body section and retains the existing terrain handoff', async () => {
  const harness = await componentHarness('app/research/workspace.tsx', {
    'next/link': { default: 'a' },
    '../science-events': { SCIENCE_SUPPORT_LABELS: {} },
    './discovery': { INVESTIGATIONS: [], RESEARCH_FRONTIER: [], RESEARCH_READING: [], REPRESENTATIONS: {}, discoverySearch: () => [], discoveryParams: () => new URLSearchParams() },
    './research.module.css': { default: styles },
  }, { URLSearchParams });
  const tree = harness.render(harness.exports.default, { sources: [], instruments: [], initialState: { query: '', domain: '', kind: '', compare: [] } });
  const observationSection = findNode(tree, (node) => node.type === 'section' && node.props.id === 'observation-tools');
  assert.ok(observationSection);
  const links = nodes(observationSection, (node) => node.type === 'a').map((node) => node.props.href);
  for (const href of ['/science', ...ids.map((id) => `/labs/${id}`)]) assert.ok(links.includes(href), href);
  assert.ok(findNode(tree, (node) => node.props?.href === '/acquisition#neon-lidar-lab'));
  const scope = findNode(tree, (node) => node.props?.['aria-label'] === 'Catalogue scope');
  assert.ok(scope, 'source-directory metrics remain separate from the new observation tools');
  harness.dispose();
});

test('only the new observation pages opt into document scrolling and fluid narrow sizing', async () => {
  for (const file of ['app/science/science.module.css', ...ids.map((id) => `app/labs/${id}/${id}.module.css`)]) {
    const source = await readFile(file, 'utf8');
    assert.match(source, /:global\(body\):has\(\.page\)\s*\{[^}]*min-width:\s*0;[^}]*overflow:\s*auto;/, file);
    assert.doesNotMatch(source, /:global\(body\)\s*\{/, 'body scroll behavior remains conditional on this page');
  }
});
