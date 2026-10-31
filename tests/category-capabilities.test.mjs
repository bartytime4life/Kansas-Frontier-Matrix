import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';

const load = async (file, imports = {}) => {
  const exports = {};
  new Function('exports', 'require', ts.transpileModule(await readFile(file, 'utf8'), {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
  }).outputText)(exports, name => { assert.ok(name in imports, name); return imports[name]; });
  return exports;
};
const topics = await load('app/layer-workspaces.ts');
const maps = await load('app/category-maps.ts');
const science = await load('app/science-events.ts');
const capabilities = await load('app/category-capabilities.ts', { './category-maps': maps, './layer-workspaces': topics });
const page = await readFile('app/page.tsx', 'utf8');

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
  const body = page.slice(page.indexOf('  const revealCategoryTool ='), page.indexOf('  // The dock follows'));
  const names = ['setCategoryToolsOnCurrentMap', 'setPrimaryWorkspace', 'setGuideOpen', 'setUndergroundOpen', 'setOfficialWorkspace', 'setCategoryDockTopic', 'setCategoryDockHidden', 'setLeftOpen', 'setRightOpen', 'dismissMapUtilityWithoutFocus'];
  const calls = [], frames = [];
  const target = { scrollIntoView: () => calls.push(['scroll']), focus: () => calls.push(['focus']) };
  const js = ts.transpileModule(`${body}; return revealCategoryTool;`, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
  const action = new Function('categoryMap', 'window', 'document', ...names, js)(
    maps.categoryMap, { requestAnimationFrame: fn => frames.push(fn) }, { querySelector: () => ({ querySelector: () => target }) },
    ...names.map(name => (...args) => calls.push([name, ...args])),
  );
  action('agriculture', 'crops');
  assert.ok(calls.some(([name, value]) => name === 'setCategoryToolsOnCurrentMap' && value === true), 'tool-only presentation does not depend on whether basemap names happen to match');
  assert.ok(calls.some(([name, value]) => name === 'setCategoryDockTopic' && value === 'agriculture'));
  assert.equal(calls.some(([name]) => name === 'focus'), false);
  while (frames.length) frames.shift()();
  assert.deepEqual(calls.slice(-2), [['scroll'], ['focus']]);
  const before = calls.length;
  action('agriculture', 'underground');
  assert.equal(calls.length, before, 'cannot navigate to a tool the category does not own');
  // No implicit globals are provided for fetching, resetting, changing visibility or moving the map.
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
