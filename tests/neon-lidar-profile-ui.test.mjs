import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';

const compiled = ts.transpileModule(await readFile('app/neon-lidar-preview.ts', 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const helpers = await import(`data:text/javascript;base64,${Buffer.from(compiled).toString('base64')}`);
function fixture(width = 8) {
  const tile = 'NEON_D06_KONZ_DP3_666000_4328000';
  return helpers.parseNeonLidarPreview({ schema_version: 'kfm-neon-lidar-preview-v1', data_kind: 'synthetic-test', generated_at: '2026-11-25T12:00:00Z',
    source: { site: 'KONZ', month: '2024-06', acquisition_run: '2024_KONZ_1', release: 'RELEASE-2026', tile,
      attribution: 'Synthetic analytic component fixture; not observed terrain', horizontal_crs: 'PROJCRS["Synthetic test reference"]', vertical_reference: 'Synthetic test reference', vertical_reference_basis: 'Analytic fixture', canopy_floor_m: null, canopy_floor_basis: 'Unknown in analytic fixture',
      files: ['dtm', 'dsm', 'chm'].map(kind => ({ kind, name: `${tile}_${kind.toUpperCase()}.tif`, product: kind === 'chm' ? 'DP3.30015.001' : 'DP3.30024.001', bytes: 1, sha256: 'a'.repeat(64) })) },
    grid: { width, height: width, bounds: [666000,4328000,667000,4329000], source_resolution_m: 1, preview_resolution_m: 1000/width, sampling: 'nearest-neighbor', dtm: Array(width**2).fill(100), dsm: Array(width**2).fill(110), chm: Array(width**2).fill(8) }, lifecycle: 'local-preview-only', source_admitted: false, released: false });
}
async function harness() {
  return componentHarness('app/neon-lidar-panel.tsx', { './neon-lidar-preview': helpers, './neon-lidar-pilot-client': {}, './acquisition-client': {}, './neon-lidar-panel.module.css': { default: new Proxy({}, { get: (_, key) => key }) } }, {}, '\nexports.SampleProfile=SampleProfile; exports.ProfilePlot=ProfilePlot;');
}
const text = tree => JSON.stringify(tree, (_key, value) => typeof value === 'function' ? value.name : value);
const node = (tree, type, label) => findNode(tree, n => n.type === type && n.props['aria-label'] === label);
function allNodes(tree, predicate, result = []) {
  if (!tree || typeof tree !== 'object') return result;
  if (predicate(tree)) result.push(tree);
  for (const child of [tree.props?.children].flat(Infinity)) allNodes(child,predicate,result);
  return result;
}

test('row and column profiles keep the selected sample, expose native keyboard controls and retire invalid selection', async () => {
  const h = await harness(), preview = fixture(), selections = [];
  let selected = { row: 2, column: 4 };
  const render = () => h.render(h.exports.SampleProfile, { preview, selected, select: next => selections.push({...next}), id: 'test-profile' });
  let tree = render(), slider = findNode(tree, n => n.type === 'input' && n.props.type === 'range');
  assert.equal(slider.props.value, 5);
  assert.match(slider.props['aria-valuetext'], /Row 3, column 5, 500 projected meters/);
  node(tree,'button','Previous profile sample').props.onClick();
  assert.deepEqual(selections.pop(), { row:2,column:3 });
  slider.props.onChange({target:{value:'8'}}); assert.deepEqual(selections.pop(), {row:2,column:7});
  findNode(tree, n => n.type === 'button' && n.props['aria-pressed'] === false).props.onClick(); tree = render();
  slider = findNode(tree, n => n.type === 'input' && n.props.type === 'range');
  assert.equal(slider.props.value,3); assert.match(slider.props['aria-valuetext'], /Row 3, column 5, 250 projected meters/);
  node(tree,'button','Next profile sample').props.onClick(); assert.deepEqual(selections.pop(), {row:3,column:4});
  selected = null; tree = render();
  assert.equal(findNode(tree,n => n.type === 'input' && n.props.type === 'range'),undefined);
  assert.equal(findNode(tree,n => typeof n.type === 'function' && n.type.name === 'ProfilePlot'),undefined);
  assert.match(text(tree),/Clearing either coordinate removes the profile/);
  selected = {row:7,column:7}; tree = render();
  assert.equal(node(tree,'button','Next profile sample').props.disabled,true);
  h.dispose();
});

test('point plots use actual retained distance for pointer selection and link the original source row', async () => {
  const h = await harness(), preview = fixture(64), selections = [];
  const tree = h.render(h.exports.SampleProfile,{preview,selected:{row:3,column:1},select: value => selections.push({...value}),id:'profile'});
  const chartNode = findNode(tree,n => typeof n.type === 'function' && n.type.name === 'ProfilePlot');
  const chart = h.render(h.exports.ProfilePlot,chartNode.props), svg = findNode(chart,n => n.type === 'svg' && n.props.role === 'img');
  const samples = chartNode.props.profile.samples;
  assert.equal(samples[1].distance_m,16); assert.equal(samples[2].distance_m,32); assert.equal(samples[3].distance_m,47);
  const last = samples.at(-1).distance_m, wanted = samples[3].distance_m;
  svg.props.onPointerDown({clientX:100+(.02+.96*wanted/last)*400,currentTarget:{getBoundingClientRect:() => ({left:100,width:400})}});
  assert.deepEqual(selections.pop(),{row:3,column:3});
  const positions = allNodes(chart,n => n.type === 'svg' && n.props.width === 1);
  assert.equal(positions[3].props.x,`${2+wanted/last*96}%`);
  assert.match(text(chart),/discrete retained source samples/);
  h.dispose();
});

test('separate plots preserve zero, per-series NoData, negative QA and finite geometry at extreme source values', async () => {
  const h = await harness(), preview = fixture();
  preview.grid.dtm[0]=1e308; preview.grid.dsm[0]=-1e308; preview.grid.chm[0]=0;
  preview.grid.dtm[1]=0; preview.grid.dsm[1]=-2; preview.grid.chm[1]=null;
  preview.grid.dtm[2]=null;
  const tree = h.render(h.exports.SampleProfile,{preview,selected:{row:0,column:0},select(){},id:'extreme'});
  assert.match(text(tree),/Negative values are plotted; nonfinite differences remain missing/);
  const charts = allNodes(tree,n => typeof n.type === 'function' && n.type.name === 'ProfilePlot');
  assert.equal(charts[0].props.includeZero,false); assert.equal(charts[1].props.includeZero,true);
  for (const chart of charts) {
    const plot = h.render(h.exports.ProfilePlot,chart.props);
    for (const item of allNodes(plot,n => ['svg','line'].includes(n.type))) for (const key of ['x','y','x1','x2','y1','y2']) {
      if (typeof item.props[key] === 'number') assert.ok(Number.isFinite(item.props[key]),`${key} must stay finite`);
      if (typeof item.props[key] === 'string') assert.doesNotMatch(item.props[key],/NaN|Infinity/);
    }
    const series = allNodes(plot,n => n.type === 'g' && n.props['data-series']);
    if (chart.props.includeZero) {
      assert.equal(series[0].props.children.filter(Boolean).length,7);
      assert.equal(series[1].props.children.filter(Boolean).length,6);
      assert.ok(series[0].props.children[0]); // Zero CHM remains an actual plotted point.
      assert.ok(series[1].props.children[1]); // Negative difference remains an actual plotted point.
    }
  }
  preview.grid.dtm.fill(null); preview.grid.dsm.fill(null); preview.grid.chm.fill(null);
  const emptyProfile = helpers.neonLidarProfile(preview,'row',0);
  for (const chart of charts) {
    const plot = h.render(h.exports.ProfilePlot,{...chart.props,profile:emptyProfile});
    assert.match(text(plot),/No retained values on this profile/);
    assert.equal(allNodes(plot,n => n.type === 'g' && n.props['data-sample-index'] !== undefined).length,0);
  }
  h.dispose();
});
