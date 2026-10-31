import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';

const context = {};
new Function('exports', ts.transpileModule(await readFile('app/earth-engine-context.ts', 'utf8'), {
  compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
}).outputText)(context);
const page = ts.createSourceFile('page.tsx', await readFile(process.env.KFM_SETUP_PAGE ?? 'app/page.tsx', 'utf8'), ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
let startupExpression;
function visit(node) {
  if (ts.isJsxSelfClosingElement(node) && node.tagName.getText(page) === 'EarthEngineDisplayControls') {
    startupExpression = node.attributes.properties.find(p => p.name?.getText(page) === 'allowStartupFallback')?.initializer.expression.getText(page);
  }
  ts.forEachChild(node, visit);
}
visit(page);
// Evaluate the actual parent prop: an absent prop uses the component's default.
const allowStartup = session => startupExpression === undefined ? undefined : new Function('categoryMapSession', `return ${startupExpression}`)(session);
const manifests = [{ setId: 'ks-2024-testfixture', layers: [{ id: 'ee-3dep', status: 'approved', resolutionMeters: 10, tileIndexes: { 6: {} } }] }];
async function mount(rendererState, session, available = manifests) {
  const h = await componentHarness('app/earth-engine-display.tsx', {
    'next/link': { default: 'a' }, '../scripts/earth-engine/cdl_2024_palette.json': { default: { classes: {} } },
    './earth-engine-data': { EARTH_ENGINE_DISPLAY_RAMPS: {} }, './earth-engine-context': context,
    './layer-workspaces': { imageryTopics: () => [], layerEntryMatches: () => true },
    './earth-engine-display.module.css': { default: {} }, './map-layer-composition': {},
    './earth-engine-comparison-panel': { EarthEngineComparisonPanel: 'comparison' },
  });
  let display;
  const props = { map: null, mapYear: 2024, manifests: available, loading: false, error: null, onReload() {},
    rendererState, allowStartupFallback: allowStartup(session), onDisplayChange: value => { display = value; } };
  const render = () => { const tree = h.render(h.exports.EarthEngineDisplayControls, props); h.commit(); return tree; };
  const checkbox = () => findNode(findNode(render(), node => node.type === 'label' && node.props.children?.[1]?.props?.children === 'Elevation mosaic'), node => node.type === 'input' && node.props.type === 'checkbox');
  return { h, props, render, checkbox, get display() { return display; } };
}

for (const renderer of ['unsupported', 'ready']) test(`${renderer}: off choice survives repeated category remounts; explicit selection still works`, async () => {
  let owner = await mount(renderer, 0);
  owner.render();
  assert.equal(Boolean(owner.display.visible['ee-3dep']), renderer === 'unsupported', 'only unsupported startup selects approved elevation');
  owner.checkbox().props.onChange({ target: { checked: false } });
  owner.render();
  assert.equal(Boolean(owner.display.visible['ee-3dep']), false);
  owner.props.catalogTopic = 'geology'; owner.render();
  assert.equal(Boolean(owner.display.visible['ee-3dep']), false, 'catalogue browsing preserves off');
  owner.h.dispose();
  for (let session = 1; session <= 4; session++) {
    owner = await mount(renderer, session); owner.render();
    assert.equal(Boolean(owner.display.visible['ee-3dep']), false, `category session ${session} stays off`);
    owner.checkbox().props.onChange({ target: { checked: true } }); owner.render();
    assert.equal(owner.display.visible['ee-3dep'], true, 'manual selection remains available');
    owner.checkbox().props.onChange({ target: { checked: false } }); owner.render();
    assert.equal(owner.display.visible['ee-3dep'], false);
    owner.h.dispose();
  }
});

test('late approved imagery may initialize startup, but cannot initialize a new category', async () => {
  for (const session of [0, 1, 2]) {
    const owner = await mount('unsupported', session, []); owner.render();
    assert.equal(Boolean(owner.display.visible['ee-3dep']), false);
    owner.props.manifests = manifests; owner.render();
    assert.equal(Boolean(owner.display.visible['ee-3dep']), session === 0);
    owner.h.dispose();
  }
});
