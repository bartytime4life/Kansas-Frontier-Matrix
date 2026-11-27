import assert from 'node:assert/strict';
import { readFile, access } from 'node:fs/promises';
import test from 'node:test';
import { componentHarness, findNode } from './component-harness.mjs';
import { STORIES, STORY_GROUPS, storyById } from '../app/living-welcome/stories/registry.mjs';
import { PUBLIC_LAB_SNAPSHOTS } from '../app/labs/public-snapshots.mjs';
import * as atlas from '../app/labs/atlas-model.mjs';

const ids = ['heat-and-rain', 'county-drought', 'soil-profile', 'daily-air-quality', 'sunlight-and-sky'];
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

test('science tools are direct guided routes and preserve the independent public snapshot boundary', async () => {
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

test('the hosted atlas renders science questions as links instead of opening a modal loader', async () => {
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

test('Research Discovery composes statewide pathways with direct science links and a bounded terrain case', async t => {
  const model = await componentHarness('app/research/pathways.ts', {}, { URLSearchParams });
  const discovery = await componentHarness('app/research/discovery.ts', {}, { URLSearchParams });
  const pathways = await componentHarness('app/research/pathway-browser.tsx', {
    'next/link': { default: 'a' },
    './discovery': discovery.exports,
    './pathways': model.exports,
    './pathway-browser.module.css': { default: styles },
  });
  const harness = await componentHarness('app/research/workspace.tsx', {
    'next/link': { default: 'a' },
    '../science-events': { SCIENCE_SUPPORT_LABELS: {} },
    './discovery': discovery.exports,
    './pathway-browser': pathways.exports,
    './research.module.css': { default: styles },
  }, { URLSearchParams });
  t.after(() => { for (const entry of [harness, pathways, discovery, model]) entry.dispose(); });
  const tree = harness.render(harness.exports.default, { sources: [], instruments: [], initialState: { query: '', domain: '', kind: '', compare: [] } });
  const pathwayEntry = findNode(tree, node => node.type === pathways.exports.ResearchPathways);
  assert.ok(pathwayEntry, 'the Research workspace mounts the real pathway component');
  const pathwaySection = pathways.render(pathwayEntry.type, pathwayEntry.props);
  assert.equal(pathwaySection.type, 'section');
  assert.equal(pathwaySection.props.id, 'research-pathways');
  const cards = nodes(pathwaySection, node => node.type === 'article' && node.props['data-research-pathway']);
  assert.deepEqual(cards.map(node => node.props['data-research-pathway']), Array.from(model.exports.RESEARCH_PATHWAYS, pathway => pathway.id));
  assert.equal(cards.length, 8, 'science links belong to the complete statewide set of subjects');
  const links = nodes(pathwaySection, (node) => node.type === 'a').map((node) => node.props.href);
  for (const href of ['/science', ...ids.map((id) => `/labs/${id}`)]) assert.ok(links.includes(href), href);
  const text = node => typeof node === 'string' || typeof node === 'number' ? String(node)
    : node && typeof node === 'object' ? [node.props?.children].flat(Infinity).map(text).join('') : '';
  for (const card of cards) {
    const pathway = model.exports.RESEARCH_PATHWAYS.find(entry => entry.id === card.props['data-research-pathway']);
    const tools = findNode(card, node => node.type === 'ul' && node.props['aria-label'] === `${pathway.title} tools`);
    assert.deepEqual(nodes(tools, node => node.type === 'a').map(node => node.props.href), Array.from(pathway.tools, tool => tool.href));
    assert.ok(findNode(card, node => node.type === 'a' && node.props.href === model.exports.pathwayComparisonHref(pathway)), pathway.id);
    const context = findNode(card, node => node.type === 'details');
    const paragraphs = [card.props.children].flat(Infinity).filter(node => node?.type === 'p');
    for (const value of [pathway.scope, pathway.boundary]) {
      const paragraph = paragraphs.find(node => text(node).includes(value));
      assert.ok(paragraph, `${pathway.id} retains scope and scientific limits as direct card paragraphs`);
      assert.ok(!findNode(context, node => node === paragraph), `${pathway.id} qualifications remain outside the source disclosure`);
    }
  }
  const directories = findNode(tree, (node) => node.type === 'nav' && node.props.id === 'observation-tools');
  assert.ok(directories, 'the body retains a direct research directory entry');
  for (const href of ['/science', '/topics', '/data-library', '/observatory/sources']) assert.ok(findNode(directories, node => node.type === 'a' && node.props.href === href), href);
  const terrainCase = findNode(tree, node => node.type === 'details' && findNode(node, child => child.props?.id === 'terrain-pilot-title'));
  assert.ok(terrainCase, 'the Konza pilot remains a disclosure within the broader research page');
  assert.ok(!terrainCase.props.open, 'the local Konza case opens only when the reader chooses it');
  assert.ok(findNode(terrainCase, node => node.props?.href === '/labs/terrain'));
  assert.ok(findNode(tree, (node) => node.props?.href === '/acquisition#neon-lidar-lab'));
  const scope = findNode(tree, (node) => node.props?.['aria-label'] === 'Catalogue scope');
  assert.ok(scope, 'source-directory metrics remain separate from the working research tools');
});

test('only the new science pages opt into document scrolling and fluid narrow sizing', async () => {
  for (const file of ['app/science/science.module.css', 'app/labs/earthquakes/earthquake.module.css', ...ids.map((id) => `app/labs/${id}/${id}.module.css`)]) {
    const source = await readFile(file, 'utf8');
    assert.match(source, /:global\(body\):has\(\.page\)\s*\{[^}]*min-width:\s*0;[^}]*overflow:\s*auto;/, file);
    assert.doesNotMatch(source, /:global\(body\)\s*\{/, 'body scroll behavior remains conditional on this page');
  }
});
