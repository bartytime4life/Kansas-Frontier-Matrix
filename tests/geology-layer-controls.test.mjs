import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import { componentHarness, findNode } from './component-harness.mjs';

test('geology layer controls expose source and mine operation switches and three actual earthquake choices', async () => {
  const h = await componentHarness('app/geology-layer-controls.tsx', {'./geology-layer-controls.module.css': new Proxy({}, {get: (_, key) => String(key)})});
  const changes = [];
  const visibility = {well:true, core:true, oilgas:true, minerals:true};
  const render = (shown = visibility) => h.render(h.exports.GeologyLayerControls, {
    visibility: shown, mineVisibility: {surface:true,underground:true,solution:true,unspecified:true}, onMineVisibility: (kind, value) => changes.push(['mine',kind,value]), earthquakeMode: 'recent', onVisibility: (kind, value) => changes.push([kind, value]),
    onEarthquakeMode: mode => changes.push(['earthquake', mode]), onUnderground: () => changes.push(['underground']),
  });
  const tree = render();
  const inputs = [];
  const visit = node => { if (!node || typeof node !== 'object') return; if (node.type === 'input') inputs.push(node); for (const child of [node.props?.children].flat(Infinity)) visit(child); };
  visit(tree);
  const points = inputs.filter(node => node.props.type === 'checkbox');
  assert.equal(points.length, 8);
  assert.ok(points.every(node => node.props.checked));
  points[1].props.onChange({target:{checked:false}});
  findNode(tree, node => node.type === 'input' && node.props['aria-label'] === 'Show Underground mines').props.onChange({target:{checked:false}});
  const radios = inputs.filter(node => node.props.type === 'radio');
  assert.equal(radios.length, 3);
  radios[1].props.onChange(); radios[2].props.onChange();
  findNode(tree, node => node.type === 'button' && String(node.props.children?.[0] ?? '').includes('Open Underground')).props.onClick();
  assert.deepEqual(changes,[['core',false],['mine','underground',false],['earthquake','record'],['earthquake','off'],['underground']]);
  const hidden = render({...visibility, core:false});
  const hiddenInput = findNode(hidden, node => node.type === 'input' && node.props['aria-label'] === 'Show Core samples');
  assert.equal(hiddenInput.props.checked,false);
  const disabled = render({...visibility, minerals:false});
  assert.equal(findNode(disabled, node => node.type === 'fieldset' && node.props.disabled === true).props.disabled,true);
  h.dispose?.();
});

test('geology uses the same visibility state in the on-map card and left Map Layers panel', async () => {
  const page = await readFile('app/page.tsx','utf8');
  assert.match(page,/officialWorkspace === "geology" && <GeologyLayerControls visibility=\{geologyPointVisibility\} onVisibility=\{setGeologyPointKind\}/);
  assert.match(page,/<GeologyPointExplorer[\s\S]{0,500}visibility=\{geologyPointVisibility\} onVisibility=\{setGeologyPointKind\}/);
  assert.equal((page.match(/mineVisibility=\{geologyMineVisibility\} onMineVisibility=\{setGeologyMineKind\}/g) ?? []).length, 2);
  assert.match(page,/onQuakes=\{on => on \? showQuakeRecord\(true\) : setGeologyEarthquakeMode\("recent"\)\}/);
});
