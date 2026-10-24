import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';
import { assistantSurfaceForPath } from '../app/assistant-surfaces.mjs';

// Exercises hooks and handlers with synthetic inputs; it is not browser/layout QA.
async function moduleUrl(name) {
  let js = ts.transpileModule(await readFile(new URL(`../app/${name}.ts`, import.meta.url), 'utf8'), {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  for (const [, dependency] of [...js.matchAll(/from "\.\/([a-z-]+)"/g)]) {
    js = js.replaceAll(`from "./${dependency}"`, `from "${await moduleUrl(dependency)}"`);
  }
  return `data:text/javascript;base64,${Buffer.from(js).toString('base64')}`;
}
const civic = await import(await moduleUrl('civic-model'));
const fixtureSources = Array.from({ length: 29 }, (_, index) => ({
  id: `synthetic-${index}`, title: `Synthetic source ${String(index).padStart(2, '0')}`,
  organization: 'Synthetic test publisher', url: `https://example.test/source/${index}`,
  category: index < 15 ? 'money' : 'laws', description: 'Synthetic records for handler tests only',
  geography: 'Synthetic geography', checkedAt: '2026-10-24', status: 'needs-verification',
  limitation: 'Not real public records', tags: ['fixture'],
}));

function textOf(node) {
  if (node === null || node === undefined || typeof node === 'boolean') return '';
  if (typeof node !== 'object') return String(node);
  if (Array.isArray(node)) return node.map(textOf).join('');
  return textOf(node.props?.children);
}
function nodes(node, predicate) {
  if (!node || typeof node !== 'object') return [];
  if (Array.isArray(node)) return node.flatMap(child => nodes(child, predicate));
  return [...(predicate(node) ? [node] : []), ...nodes(node.props?.children, predicate)];
}
const button = (tree, label) => {
  const found = findNode(tree, node => node.type === 'button' && textOf(node) === label);
  assert.ok(found, `Expected button: ${label}`);
  return found;
};
const field = (tree, id) => {
  const found = findNode(tree, node => node.props?.id === id);
  assert.ok(found, `Expected field: ${id}`);
  return found;
};
const cards = tree => nodes(tree, node => node.type === 'article');
const question = tree => field(tree, 'civic-question').props.value;

async function atlas(t, globals = {}) {
  const h = await componentHarness(new URL('../app/civic/civic-atlas.tsx', import.meta.url), {
    'next/link': { default: 'a' }, '../civic-sources': { CIVIC_SOURCES: fixtureSources },
    '../civic-model': civic, './civic.module.css': { default: {} },
  }, {
    fetch: () => assert.fail('Unexpected network request'),
    document: { getElementById: () => null },
    navigator: { clipboard: { writeText: () => assert.fail('Unexpected clipboard write') } },
    ...globals,
  });
  t.after(() => h.dispose());
  return {
    h,
    render() { const tree = h.render(h.exports.default, {}); h.commit(); return tree; },
  };
}

// Repeated boxes and invented county names test the adapter contract, not real geography.
const countyInventory = () => ({ edition: '2020', data: { type: 'FeatureCollection',
  features: Array.from({ length: 105 }, (_, index) => {
    const geoid = `20${String(index * 2 + 1).padStart(3, '0')}`;
    return { type: 'Feature', properties: { geoid, featureId: `us-census-county-${geoid}`,
      name: `Synthetic ${String(index).padStart(3, '0')}`, vintage: '2020' },
    geometry: { type: 'Polygon', coordinates: [[[-99, 38], [-98.5, 38], [-98.5, 38.5], [-99, 38.5], [-99, 38]]] } };
  }),
} });

test('source cards expand without omissions and collapse to a useful focus target', async t => {
  const ui = await atlas(t);
  let tree = ui.render();
  assert.equal(cards(tree).length, 12);
  assert.match(textOf(tree), /Showing 12 of 29 matching sources/);
  button(tree, 'Show 12 more sources').props.onClick(); tree = ui.render();
  assert.equal(cards(tree).length, 24);
  button(tree, 'Show 5 more sources').props.onClick(); tree = ui.render();
  assert.equal(cards(tree).length, 29);
  assert.deepEqual(cards(tree).map(card => findNode(card, node => node.type === 'a').props.href),
    fixtureSources.map(source => source.url));
  const focusCalls = [], scrollCalls = [];
  field(tree, 'source-heading').props.ref.current = {
    focus: options => focusCalls.push(options), scrollIntoView: options => scrollCalls.push(options),
  };
  button(tree, 'Show fewer sources').props.onClick(); tree = ui.render();
  assert.equal(cards(tree).length, 12);
  assert.equal(focusCalls.length, 1); assert.equal(focusCalls[0].preventScroll, true);
  assert.equal(scrollCalls.length, 1); assert.equal(scrollCalls[0].block, 'start');
});

test('subject and search filters compose, reset an expanded window, and recover from no results', async t => {
  const ui = await atlas(t);
  let tree = ui.render();
  button(tree, 'Show 12 more sources').props.onClick(); tree = ui.render();
  button(tree, 'Money & disclosures').props.onClick(); tree = ui.render();
  assert.equal(button(tree, 'Money & disclosures').props['aria-pressed'], true);
  assert.equal(button(tree, 'All sources').props['aria-pressed'], false);
  assert.equal(cards(tree).length, 12);
  assert.match(textOf(tree), /Showing 12 of 15 matching sources/);
  button(tree, 'Show 3 more sources').props.onClick(); tree = ui.render();
  assert.equal(cards(tree).length, 15);
  findNode(tree, node => node.type === 'input' && node.props.type === 'search').props.onChange({ target: { value: 'SOURCE 03' } });
  tree = ui.render();
  assert.equal(cards(tree).length, 1);
  assert.equal(findNode(cards(tree)[0], node => node.type === 'a').props.href, fixtureSources[3].url);
  assert.match(textOf(tree), /Showing 1 of 1 matching source/);
  button(tree, 'Laws & decisions').props.onClick(); tree = ui.render();
  assert.equal(cards(tree).length, 0);
  assert.ok(findNode(tree, node => node.type === 'h3' && textOf(node) === 'No source matches those filters'));
  button(tree, 'Reset filters').props.onClick(); tree = ui.render();
  assert.equal(cards(tree).length, 12);
  assert.equal(button(tree, 'All sources').props['aria-pressed'], true);
  assert.equal(findNode(tree, node => node.type === 'input' && node.props.type === 'search').props.value, '');
});

test('county loading is deliberate, retryable, and scopes only map framing and the prepared question', async t => {
  const requests = [];
  const ui = await atlas(t, { fetch: (url, options) => new Promise(resolve => requests.push({ url, options, resolve })) });
  let tree = ui.render();
  assert.equal(requests.length, 0);
  const first = button(tree, 'Load county choices').props.onClick(); tree = ui.render();
  assert.equal(requests.length, 1);
  assert.equal(requests[0].url, '/api/event-atlas/counties?edition=2020');
  assert.equal(button(tree, 'Loading county choices…').props.disabled, true);
  requests[0].resolve({ ok: false }); await first; tree = ui.render();
  assert.match(textOf(tree), /County choices are unavailable/);
  assert.equal(findNode(tree, node => node.type === 'select'), undefined);
  assert.equal(cards(tree).length, 12, 'statewide source navigation remains available');
  const retry = button(tree, 'Retry county choices').props.onClick(); tree = ui.render();
  assert.equal(requests.length, 2); assert.equal(requests[0].options.signal.aborted, true);
  requests[1].resolve({ ok: true, json: async () => countyInventory() }); await retry; tree = ui.render();
  const select = field(tree, 'civic-county');
  assert.equal(nodes(select, node => node.type === 'option').length, 106);
  select.props.onChange({ target: { value: '20001' } }); tree = ui.render();
  assert.match(question(tree), /^For Synthetic 000 County, Kansas:/);
  const map = findNode(tree, node => node.type === 'a' && textOf(node) === 'View Synthetic 000 County on the map↗');
  assert.ok(map);
  const params = new URL(map.props.href, 'https://example.test').searchParams;
  assert.deepEqual([...params.keys()].sort(), ['c', 'ctx', 'z']);
  assert.equal(params.get('ctx'), 'census-counties'); assert.equal(params.get('c'), '-98.75000,38.25000');
  assert.equal(cards(tree).length, 12, 'county selection does not silently filter the statewide source desk');
  field(tree, 'civic-county').props.onChange({ target: { value: '' } }); tree = ui.render();
  assert.match(question(tree), /^For Kansas:/);
  assert.ok(findNode(tree, node => node.type === 'a' && node.props.href === '/?ctx=census-counties'));
});

test('an incomplete county response cannot present a successful county picker', async t => {
  const incomplete = countyInventory(); incomplete.data.features.pop();
  const ui = await atlas(t, { fetch: async () => ({ ok: true, json: async () => incomplete }) });
  let tree = ui.render();
  await button(tree, 'Load county choices').props.onClick(); tree = ui.render();
  assert.ok(button(tree, 'Retry county choices'));
  assert.equal(findNode(tree, node => node.type === 'select'), undefined);
  assert.match(question(tree), /^For Kansas:/);
});

test('private reflection and chosen values never enter the copied question and clear together', async t => {
  const writes = [], privateText = 'PRIVATE_REFLECTION_DO_NOT_SEND_7841';
  const ui = await atlas(t, { navigator: { clipboard: { writeText: async value => writes.push(value) } } });
  let tree = ui.render();
  assert.equal(button(tree, 'Clear reflection').props.disabled, true);
  button(tree, 'Voting & candidates').props.onClick(); tree = ui.render();
  const originalQuestion = question(tree);
  field(tree, 'civic-reflection').props.onChange({ target: { value: privateText } });
  findNode(tree, node => node.type === 'input' && node.props.type === 'checkbox').props.onChange({ target: { checked: true } });
  tree = ui.render();
  assert.equal(field(tree, 'civic-reflection').props.value, privateText);
  assert.equal(nodes(tree, node => node.type === 'input' && node.props.type === 'checkbox' && node.props.checked).length, 1);
  assert.equal(question(tree), originalQuestion);
  await button(tree, 'Copy question').props.onClick(); tree = ui.render();
  assert.deepEqual(writes, [originalQuestion]); assert.doesNotMatch(writes[0], /PRIVATE_REFLECTION/);
  assert.match(writes[0], /without recommending a candidate/);
  assert.match(textOf(tree), /Question copied/);
  button(tree, 'Clear reflection').props.onClick(); tree = ui.render();
  assert.equal(field(tree, 'civic-reflection').props.value, '');
  assert.equal(nodes(tree, node => node.type === 'input' && node.props.type === 'checkbox' && node.props.checked).length, 0);
  assert.equal(button(tree, 'Clear reflection').props.disabled, true);
  assert.equal(question(tree), originalQuestion);
  button(tree, 'Money & disclosures').props.onClick(); tree = ui.render();
  assert.doesNotMatch(textOf(tree), /Question copied/, 'a changed question must not retain a stale copied status');
});

test('clipboard rejection exposes a selectable fallback without sending the question', async t => {
  const attempted = [], selected = [];
  const ui = await atlas(t, { navigator: { clipboard: { writeText: async value => { attempted.push(value); throw new Error('denied'); } } } });
  let tree = ui.render();
  const prepared = question(tree);
  field(tree, 'civic-question').props.ref.current = { focus: () => selected.push('focus'), select: () => selected.push('select') };
  await button(tree, 'Copy question').props.onClick(); tree = ui.render();
  assert.deepEqual(attempted, [prepared]); assert.deepEqual(selected, ['focus', 'select']);
  assert.equal(field(tree, 'civic-question').props.readOnly, true);
  assert.equal(question(tree), prepared);
  assert.match(textOf(tree), /Copy is unavailable in this browser/);
  assert.ok(findNode(tree, node => node.type === 'a' && node.props.href === '/?kfm-chat=1'));
});

test('the civic page assistant receives fixed public context without private form or query values', async t => {
  const privateMarker = 'PRIVATE_CIVIC_NOTE_1192';
  const Panel = () => null;
  const h = await componentHarness(new URL('../app/site-assistant.tsx', import.meta.url), {
    'next/navigation': { usePathname: () => '/civic', useSearchParams: () => new URLSearchParams({
      id: privateMarker, reflection: privateMarker, values: privateMarker, candidate: privateMarker,
    }) },
    './assistant-surfaces.mjs': { assistantSurfaceForPath }, './assistant-panel': { default: Panel },
    './build-clock': { BUILD_UTC_YEAR: 2026 }, './assistant-panel.module.css': { default: {} },
  }, { document: {
    get body() { assert.fail('Private page contents must not be read for assistant context'); },
    querySelector() { assert.fail('Private form fields must not be read for assistant context'); },
    querySelectorAll() { assert.fail('Private form fields must not be read for assistant context'); },
  } });
  t.after(() => h.dispose());
  const render = () => { const tree = h.render(h.exports.PageAssistant, {}); h.commit(); return tree; };
  let tree = render();
  findNode(tree, node => node.type === 'button').props.onClick(); tree = render();
  const panel = findNode(tree, node => node.type === Panel);
  assert.ok(panel);
  assert.deepEqual(JSON.parse(JSON.stringify(panel.props.focus.context)), {
    version: 1, frame: 2026, view: 'Page', layers: [], surface: 'civic', selection: null,
  });
  assert.doesNotMatch(JSON.stringify(panel.props.focus), new RegExp(privateMarker));
  panel.props.onClose();
  assert.equal(findNode(render(), node => node.type === Panel), undefined);
});
