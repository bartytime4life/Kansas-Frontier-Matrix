import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';

const load = async (file, imports = {}, globals = {}) => {
  const exports = {};
  new Function('exports', 'require', ...Object.keys(globals), ts.transpileModule(await readFile(file, 'utf8'), {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
  }).outputText)(exports, name => { assert.ok(name in imports, name); return imports[name]; }, ...Object.values(globals));
  return exports;
};
const topics = await load('app/layer-workspaces.ts');
const maps = await load('app/category-maps.ts');
const science = await load('app/science-events.ts');
const capabilities = await load('app/category-capabilities.ts', { './category-maps': maps, './layer-workspaces': topics });
const page = await readFile('app/page.tsx', 'utf8');

class FocusElement {
  parentElement = null; isConnected = true; hidden = false; inert = false; boxes = [{}];
  constructor(document, calls, name) { Object.assign(this, { document, calls, name }); }
  contains(node) { for (; node; node = node.parentElement) if (node === this) return true; return false; }
  getClientRects() { return this.boxes; }
  closest(selector) {
    assert.equal(selector, '[hidden], [inert]');
    for (let node = this; node; node = node.parentElement) if (node.hidden || node.inert) return node;
    return null;
  }
  scrollIntoView(options) { this.calls.push(['scroll', this.name, options]); }
  focus(options) { this.document.activeElement = this; this.calls.push(['focus', this.name, options]); }
}
class FocusDetails extends FocusElement {
  open = false; summary = null;
  querySelector(selector) { assert.equal(selector, ':scope > summary'); return this.summary; }
}
const focusHelpers = await load('app/modal-background.ts', {}, { HTMLElement: FocusElement, HTMLDetailsElement: FocusDetails });
const dockActionBody = page.slice(page.indexOf('  const revealCategoryTool ='), page.indexOf('  // The dock follows'));
const dockActionCode = ts.transpileModule(`${dockActionBody}; return { revealCategoryTool, closeCategoryDock };`, {
  compilerOptions: { target: ts.ScriptTarget.ES2022 },
}).outputText;
function dockActionHarness() {
  const calls = [], frames = [], document = {};
  const element = name => new FocusElement(document, calls, name);
  const body = element('body'), tool = element('tool'), dock = element('dock'), layers = element('layers');
  const opener = element('direct-opener'), layersOpener = element('layers-opener'), capability = element('capability');
  capability.parentElement = layers; tool.parentElement = dock;
  dock.querySelector = selector => { assert.match(selector, /^\[data-category-tool="[a-z-]+"\]:not\(:disabled\)$/); return tool; };
  const dom = { dock, welcome: null, explorer: element('explorer'), fallback: [layersOpener] };
  document.body = body; document.activeElement = opener;
  document.querySelector = selector => {
    if (selector === '.category-map-dock') return dom.dock;
    if (selector === '.category-map-dock, .living-welcome') return dom.dock ?? dom.welcome;
    assert.equal(selector, '.explorer-shell'); return dom.explorer;
  };
  document.querySelectorAll = selector => { assert.equal(selector, '[data-category-dock-return]'); return dom.fallback; };
  const refs = {
    categoryToolFocusRequestRef: { current: 0 }, categoryDockReturnRef: { current: null },
    leftPanelRef: { current: layers }, leftPanelReturnRef: { current: layersOpener },
  };
  const names = ['markExplorerNavigation', 'setCategoryToolsOnCurrentMap', 'setPrimaryWorkspace', 'setGuideOpen', 'setUndergroundOpen', 'setOfficialWorkspace', 'setCategoryDockTopic', 'setCategoryDockHidden', 'setLeftOpen', 'setRightOpen', 'dismissMapUtilityWithoutFocus'];
  const scope = {
    categoryMap: maps.categoryMap, window: { requestAnimationFrame: fn => frames.push(fn) }, document,
    HTMLElement: FocusElement, ...refs, ...focusHelpers,
    ...Object.fromEntries(names.map(name => [name, (...args) => calls.push([name, ...args])])),
  };
  const actions = new Function(...Object.keys(scope), dockActionCode)(...Object.values(scope));
  const flushFrames = () => {
    let count = 0;
    while (frames.length) { assert.ok(++count <= 3, 'focus handoff must finish in bounded frames'); frames.shift()(); }
  };
  return { ...actions, ...refs, calls, frames, document, dom, element, body, tool, dock, layers, opener, layersOpener, capability, flushFrames };
}

test('all 22 cards have real discoverable tools or workbenches and every dock tool is indexed', async () => {
  assert.equal(topics.TOPIC_STRUCTURE.length, 22);
  assert.deepEqual(Object.keys(capabilities.CATEGORY_WORKBENCHES).sort(), topics.TOPIC_STRUCTURE.map(t => t.id).sort());
  const dock = await readFile('app/category-map-dock.tsx', 'utf8');
  for (const topic of topics.TOPIC_STRUCTURE) {
    const groups = capabilities.categoryCapabilityGroups(topic.id, '');
    assert.equal(groups.length, 1, topic.id);
    assert.deepEqual(groups[0].tools, maps.CATEGORY_MAPS[topic.id].tools ?? []);
    for (const id of groups[0].tools) {
      assert.ok(capabilities.CATEGORY_TOOL_DETAILS[id], `${topic.id}/${id}`);
      assert.ok(dock.includes(`data-category-tool="${id}"`), `${id} has a real destination`);
    }
    for (const link of groups[0].workbenches) {
      const url = new URL(link.href, 'https://kfm.invalid');
      assert.equal(url.origin, 'https://kfm.invalid');
      assert.ok(['/observatory', '/observatory/sources', '/earth-engine', '/knowledge', '/civic', '/history/people-events', '/history/prentis-1909'].includes(url.pathname));
      if (url.searchParams.has('panel')) {
        const entry = science.scienceWorkbenchLocation(url.search);
        assert.ok(entry);
        assert.ok(science.filterScienceEvents(science.SCIENCE_EVENTS, 'all', entry.query).length, `${link.href} is not an empty lab search`);
      }
    }
  }
});

test('search recovers farming analysis and Science phenomena beyond the starter map', () => {
  for (const query of ['frost', 'growing degree', 'SSURGO', 'crop history', 'season rain']) {
    assert.ok(capabilities.categoryCapabilityGroups('agriculture', query).some(group => group.tools.includes('crops')), query);
  }
  for (const query of ['snow', 'ice', 'resources', 'wildlife']) {
    assert.ok(capabilities.categoryCapabilityGroups('science', query).some(group => group.workbenches.length), query);
  }
  assert.deepEqual(capabilities.categoryCapabilityGroups('agriculture', 'unobtainium'), []);
  assert.ok(topics.officialSourceTopics('nws-radar').includes('agriculture'));
  assert.ok(topics.specialtyLayerTopics('reviewed-weather').includes('agriculture'));
  assert.ok(topics.imageryTopics('ee-sentinel2').includes('agriculture'));
});

test('tool shortcuts route to controls without executing a tool or leaving the current map', async () => {
  const h = await componentHarness('app/category-capability-panel.tsx', {
    'next/link': { default: 'a' }, './category-capabilities': capabilities,
  });
  const calls = [];
  const tree = h.render(h.exports.CategoryCapabilityPanel, { topic: 'agriculture', query: 'frost', onTool: (...args) => calls.push(args) });
  assert.deepEqual(calls, []);
  findNode(tree, n => n.type === 'button').props.onClick();
  assert.deepEqual(calls, [['agriculture', 'crops']]);
  const scienceTree = h.render(h.exports.CategoryCapabilityPanel, { topic: 'science', query: 'snow', onTool() {} });
  const link = findNode(scienceTree, n => n.type === 'a');
  assert.equal(link.props.href, '/observatory?panel=science');
  assert.equal(link.props.target, '_blank', 'keep the map and its selections open');
  assert.equal(link.props.prefetch, false, 'discovery must not eagerly load workbenches');
});

test('reveal action preserves source, camera and stored state, validates the destination and focuses after commit', () => {
  for (const origin of ['direct', 'layers']) {
    const h = dockActionHarness();
    h.document.activeElement = origin === 'direct' ? h.opener : h.capability;
    h.revealCategoryTool('agriculture', 'crops');
    assert.equal(h.categoryDockReturnRef.current, origin === 'direct' ? h.opener : h.layersOpener,
      'a Layers capability retains the visible Layers opener; a direct shortcut retains itself');
    assert.ok(h.calls.some(([name, value]) => name === 'setCategoryToolsOnCurrentMap' && value === true), 'tool-only presentation does not depend on whether basemap names happen to match');
    assert.ok(h.calls.some(([name, value]) => name === 'setCategoryDockTopic' && value === 'agriculture'));
    assert.equal(h.calls.some(([name]) => name === 'focus'), false);
    if (origin === 'layers') h.document.activeElement = h.body; // The Layers capability unmounts on commit.
    h.flushFrames();
    assert.deepEqual(h.calls.slice(-2), [['scroll', 'tool', { block: 'nearest' }], ['focus', 'tool', { preventScroll: true }]]);
    const before = h.calls.length, generation = h.categoryToolFocusRequestRef.current, returnTarget = h.categoryDockReturnRef.current;
    h.revealCategoryTool('agriculture', 'underground');
    assert.equal(h.calls.length, before, 'cannot navigate to a tool the category does not own');
    assert.equal(h.categoryToolFocusRequestRef.current, generation);
    assert.equal(h.categoryDockReturnRef.current, returnTarget);
  }
  // No implicit globals are provided for fetching, resetting, changing visibility or moving the map.
});

test('closing a category dock restores its visible opener after unmount, with a usable Layers fallback', () => {
  for (const origin of ['direct', 'layers', 'disconnected', 'hidden', 'closed-menu']) {
    const h = dockActionHarness();
    h.document.activeElement = origin === 'layers' ? h.capability : h.opener;
    h.revealCategoryTool('agriculture', 'crops'); h.flushFrames(); h.calls.length = 0;
    let expected = origin === 'layers' ? h.layersOpener : h.opener;
    if (origin === 'disconnected') { h.opener.isConnected = false; expected = h.layersOpener; }
    if (origin === 'hidden') { h.opener.hidden = true; expected = h.layersOpener; }
    if (origin === 'closed-menu') {
      const menu = new FocusDetails(h.document, h.calls, 'menu');
      menu.summary = h.element('menu-summary'); menu.summary.parentElement = menu; h.opener.parentElement = menu;
      expected = menu.summary;
    }
    const unavailableFallback = h.element('hidden-layers'); unavailableFallback.boxes = [];
    h.dom.fallback.unshift(unavailableFallback);
    h.closeCategoryDock();
    assert.equal(h.categoryDockReturnRef.current, null, 'a closed dock releases its retained opener');
    assert.deepEqual(h.calls, [['setCategoryDockHidden', true]], 'focus waits until the closing render commits');
    h.dom.dock = null; h.document.activeElement = h.body;
    h.flushFrames();
    assert.equal(h.document.activeElement, expected, origin);
    assert.deepEqual(h.calls.at(-1), ['focus', expected.name, { preventScroll: true }]);
  }
});

test('delayed category dock close never reverses a newer focus choice or navigation owner', () => {
  for (const owner of ['new-focus', 'new-generation', 'reopened-dock', 'welcome', 'other-workspace']) {
    const h = dockActionHarness();
    h.revealCategoryTool('agriculture', 'crops'); h.flushFrames(); h.calls.length = 0;
    h.closeCategoryDock(); h.dom.dock = null; h.document.activeElement = h.body;
    if (owner === 'new-focus') h.document.activeElement = h.element('new-control');
    if (owner === 'new-generation') h.categoryToolFocusRequestRef.current += 1;
    if (owner === 'reopened-dock') h.dom.dock = h.element('new-dock');
    if (owner === 'welcome') h.dom.welcome = h.element('welcome');
    if (owner === 'other-workspace') h.dom.explorer.inert = true;
    const chosenFocus = h.document.activeElement;
    h.flushFrames();
    assert.deepEqual(h.calls, [['setCategoryDockHidden', true]], owner);
    assert.equal(h.document.activeElement, chosenFocus, owner);
  }
});

test('farm center action is explicit and only present when crops are enabled', async () => {
  const h = await componentHarness('app/category-map-dock.tsx', {});
  let calls = 0;
  const props = { look: maps.CATEGORY_MAPS.agriculture, mode: '2d', depth: 1, azimuth: 315, sun: null, terrainAvailable: true,
    crops: { on: false, year: 2025, years: [2025], reading: '', swatch: null }, onCrops() {}, onCropCentre: () => calls++ };
  const center = tree => findNode(tree, n => n.type === 'button' && n.props.onClick === props.onCropCentre);
  assert.equal(center(h.render(h.exports.CategoryMapDock, props)), undefined);
  const tree = h.render(h.exports.CategoryMapDock, { ...props, crops: { ...props.crops, on: true } });
  assert.equal(calls, 0);
  center(tree).props.onClick();
  assert.equal(calls, 1);
  assert.ok(findNode(tree, n => n.props?.['data-category-tool'] === 'crops'));
  const customMapTree = h.render(h.exports.CategoryMapDock, { ...props, currentMapOnly: true });
  const description = findNode(customMapTree, n => n.props?.className === 'category-map-dock-lede');
  assert.match(JSON.stringify(description), /These controls work on your current map/);
  assert.ok(!JSON.stringify(description).includes(maps.CATEGORY_MAPS.agriculture.lede), 'do not claim the aerial preset replaced the retained map');
});

test('Science deep links are bounded navigation, including malformed and unknown requests', () => {
  assert.equal(science.scienceWorkbenchLocation('?panel=admin'), null);
  assert.equal(science.scienceWorkbenchLocation('?q=snow'), null);
  assert.deepEqual(science.scienceWorkbenchLocation('?panel=science&q=water-levels'), { query: 'Water levels & flow' });
  assert.equal(science.scienceWorkbenchLocation('?panel=science&q=' + 'x'.repeat(400)).query.length, 200);
  assert.deepEqual(Object.keys(science.scienceWorkbenchLocation('?panel=science&track=fauna&play=true')), ['query']);
  assert.equal(science.scienceWorkbenchLocation('?panel=science&q=%E0%A4%A').query.includes('%'), true);
});

test('a matching map style never hides the category setup or claims its source layers are on', async () => {
  const h = await componentHarness('app/topic-navigation.tsx', { 'next/link': { default: 'a' }, './layer-workspaces': topics });
  let calls = 0;
  const props = { value: 'science', mapLook: { name: 'Satellite view', sceneLabel: '2D', lede: 'GOES source context', swatch: ['#000', '#111', '#222'], active: true }, onOpenMap: () => calls++ };
  const tree = h.render(h.exports.TopicGuide, props);
  const open = findNode(tree, node => node.type === 'button' && node.props.onClick === props.onOpenMap);
  assert.ok(open, 'the map setup remains reachable with matching styles and no selected sources');
  assert.equal(calls, 0, 'browsing a category must not apply its setup');
  open.props.onClick();
  assert.equal(calls, 1);
  assert.match(JSON.stringify(tree), /Default view:/);
  assert.ok(!JSON.stringify(tree).includes('on the map now'));
});
