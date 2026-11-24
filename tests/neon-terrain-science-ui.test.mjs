import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { createElement } from 'react';
import { renderToStaticMarkup } from 'react-dom/server';
import { componentHarness, findNode } from './component-harness.mjs';
import * as recordModel from '../app/living-welcome/stories/record-model.mjs';
import * as scienceModel from '../app/living-welcome/stories/science-model.mjs';
import * as kit from '../app/living-welcome/stories/story-kit.mjs';
import { STORIES } from '../app/living-welcome/stories/registry.mjs';
import { PUBLIC_LAB_SNAPSHOTS } from '../app/labs/public-snapshots.mjs';

const url = source => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;
const compile = source => ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX } }).outputText;
const previewUrl = url(compile(await readFile('app/neon-lidar-preview.ts', 'utf8')));
const boundedUrl = url(compile(await readFile('app/bounded-json.ts', 'utf8')));
const pilotUrl = url(compile((await readFile('app/neon-lidar-pilot-client.ts', 'utf8')).replace('"./bounded-json"', JSON.stringify(boundedUrl)).replace('"./neon-lidar-preview"', JSON.stringify(previewUrl))));
const scienceUrl = url(compile((await readFile('app/neon-lidar-science.ts', 'utf8')).replace('"./neon-lidar-pilot-client"', JSON.stringify(pilotUrl)).replace('"./neon-lidar-preview"', JSON.stringify(previewUrl))));
const adapter = await import(scienceUrl);
const css = { default: new Proxy({}, { get: (_, key) => key }) };
function receiptFixture() {
  const tile = 'NEON_D06_KONZ_DP3_706000_4336000';
  return { format: 'kfm-neon-relay-pilot-v1', generatedAt: '2026-11-23T23:00:00Z', cache: { state: 'stale', at: '2026-11-23T22:00:00Z' },
    review: { status: 'pending', scientific_accuracy_verified: false, source_admitted: false, canopy_native_max_m: 83.41000366210938, canopy_native_cells_above_50m: 5, surface_minus_ground_native_max_m: 32.5, notes: ['Native outliers retained; independent accuracy unverified.'] },
    preview: { schema_version: 'kfm-neon-lidar-preview-v1', data_kind: 'provider-files', generated_at: '2026-11-23T21:00:00Z',
      source: { site: 'KONZ', month: '2024-09', acquisition_run: '2024_KONZ_10', release: 'RELEASE-2026', tile, attribution: 'Analytic unit-test fixture; not a real provider observation', horizontal_crs: 'PROJCRS["Test projected reference"]', vertical_reference: 'Unverified test reference', vertical_reference_basis: 'Unit-test fixture', canopy_floor_m: null, canopy_floor_basis: 'Unknown', files: ['dtm','dsm','chm'].map((kind, index) => ({ kind, name: `${tile}_${kind.toUpperCase()}.tif`, product: kind === 'chm' ? 'DP3.30015.001' : 'DP3.30024.001', bytes: 1000, sha256: String(index+1).repeat(64) })) },
      grid: { width: 8, height: 8, bounds: [706000,4336000,707000,4337000], source_resolution_m: 1, preview_resolution_m: 125, sampling: 'nearest-neighbor', dtm: Array(64).fill(309.65), dsm: Array(64).fill(321.65), chm: [0,null,...Array(62).fill(12.25)] }, lifecycle: 'local-preview-only', source_admitted: false, released: false } };
}
const componentImports = (controller, extra = {}) => ({ '../../lidar-source-panel': { LidarSourcePanel: 'lidar-catalog' }, 'next/link': { default: 'a' }, '../../neon-lidar-panel': { useNeonLidarPreview: () => controller, NeonLidarWorkspace: 'raster-workspace' }, '../../neon-lidar-science': adapter, '../../living-welcome/stories/record-lab.jsx': { default: 'record-lab', toCSV: (bundle, options) => recordModel.recordsCSV(bundle, options) }, '../../living-welcome/stories/story-kit.mjs': kit, './terrain.module.css': css, ...extra });
const controllerFor = receipt => ({ pilotReceipt: receipt, preview: receipt?.preview ?? null, coordinateDraft: { row: '', column: '' }, setCoordinateDraft(next) { this.coordinateDraft = next; } });

test('the terrain route passes one exact loaded preview to raster and science and excludes a local-only import', async () => {
  const controller = controllerFor(receiptFixture());
  const harness = await componentHarness('app/labs/terrain/TerrainScience.jsx', componentImports(controller));
  let tree = harness.render(harness.exports.default);
  const raster = findNode(tree, node => node.type === 'raster-workspace');
  const analysis = findNode(tree, node => typeof node.type === 'function' && node.type.name === 'TerrainAnalysis');
  assert.equal(raster.props.controller, controller); assert.equal(analysis.props.controller, controller);
  assert.equal(analysis.props.dataset.receipt.preview, controller.preview);
  controller.pilotReceipt = null;
  tree = harness.render(harness.exports.default);
  assert.equal(findNode(tree, node => typeof node.type === 'function' && node.type.name === 'TerrainAnalysis'), undefined);
  assert.equal(findNode(tree, node => node.type === 'raster-workspace').props.controller.preview, controller.preview);
  harness.dispose();
});

test('analysis selection links actual rows and native samples to the raster, and exports the current filter with provenance', async () => {
  const controller = controllerFor(receiptFixture()), dataset = adapter.createNeonScienceDataset(controller.pilotReceipt), downloads = [];
  const harness = await componentHarness('app/labs/terrain/TerrainScience.jsx', componentImports(controller, { '../../living-welcome/stories/story-kit.mjs': { ...kit, downloadCSV: (name, rows) => downloads.push({ name, rows }) } }));
  const render = () => harness.render(harness.exports.TerrainAnalysis, { dataset, controller });
  let tree = render(), instrument = findNode(tree, node => node.type === 'record-lab');
  assert.equal(instrument.props.controls.view, 'chart'); assert.equal(instrument.props.controls.metric, 'chm_m'); assert.equal(instrument.props.controls.xMetric, 'chm_m'); assert.equal(instrument.props.controls.yMetric, 'surface_above_ground_m');
  const selected = dataset.bundle.data.records[1];
  instrument.props.onControls({ ...instrument.props.controls, selectedId: selected.id, minValue: '10' });
  assert.deepEqual({ ...controller.coordinateDraft }, { row: '1', column: '2' });
  tree = render(); instrument = findNode(tree, node => node.type === 'record-lab'); assert.equal(instrument.props.controls.selectedId, selected.id);
  controller.coordinateDraft = { row: '3', column: '4' }; tree = render(); instrument = findNode(tree, node => node.type === 'record-lab'); assert.equal(instrument.props.controls.selectedId, dataset.bundle.data.records[19].id);
  findNode(tree, node => node.type === 'button' && node.props.children === 'Download selection CSV ↓').props.onClick();
  const csv = downloads[0].rows, header = csv[0]; assert.equal(csv.length, 63); assert.ok(header.includes('analysis_context'));
  const context = JSON.parse(csv[1][header.indexOf('analysis_context')]); assert.equal(context.review.scientific_accuracy_verified, false);
  assert.ok(csv[1][header.indexOf('snapshot_sha256')].includes('1'.repeat(64))); assert.ok(csv[1][header.indexOf('snapshot_sha256')].includes('3'.repeat(64)));
  assert.equal(csv[1][header.indexOf('chm_m')], 12.25); harness.dispose();
});

test('leading-zero raster coordinates select the same science sample and invalid drafts select none', async () => {
  const receipt = receiptFixture(), grid = receipt.preview.grid;
  grid.width = grid.height = 100; grid.preview_resolution_m = 10;
  for (const mode of ['dtm', 'dsm', 'chm']) grid[mode] = Array(10_000).fill(mode === 'dtm' ? 309.65 : mode === 'dsm' ? 321.65 : 12.25);
  const controller = controllerFor(receipt), dataset = adapter.createNeonScienceDataset(receipt);
  const harness = await componentHarness('app/labs/terrain/TerrainScience.jsx', componentImports(controller));
  const selectedId = () => findNode(harness.render(harness.exports.TerrainAnalysis, { dataset, controller }), node => node.type === 'record-lab').props.controls.selectedId;
  controller.coordinateDraft = { row: '026', column: '046' };
  assert.equal(selectedId(), dataset.bundle.data.records[25 * 100 + 45].id);
  controller.coordinateDraft = { row: '26', column: '46' };
  assert.equal(selectedId(), dataset.bundle.data.records[25 * 100 + 45].id);
  for (const draft of [{ row: '', column: '46' }, { row: '0', column: '46' }, { row: '101', column: '46' }, { row: '26.0', column: '46' }, { row: '2.6e1', column: '46' }, { row: ' 26', column: '46' }, { row: '26', column: '-1' }, { row: '26', column: '101' }]) {
    controller.coordinateDraft = draft; assert.equal(selectedId(), null, JSON.stringify(draft));
  }
  harness.dispose();
});

async function recordHarness(downloads = []) {
  return componentHarness('app/living-welcome/stories/record-lab.jsx', { 'next/link': { default: 'a' }, '../../labs/then-now/crossing.json': { default: {} }, './story-kit.mjs': { ...kit, useStoryCanvas: () => ({ current: null }), downloadCSV: (name, rows) => downloads.push({ name, rows }) }, './record-model.mjs': recordModel, './science-model.mjs': scienceModel, './record-lab.css': {} }, {}, '\nexports.RecordInstrument=RecordInstrument; exports.SciencePanel=SciencePanel; exports.RecordTable=RecordTable; exports.Provenance=Provenance;');
}
test('RecordLab preview presentation omits time claims, retains precision and exposes all source-file receipts', async () => {
  const dataset = adapter.createNeonScienceDataset(receiptFixture()), bundle = dataset.bundle, model = recordModel.recordModel(bundle), harness = await recordHarness();
  const tree = harness.render(harness.exports.RecordInstrument, { bundle, time: null, controls: { view: 'chart' } });
  const text = JSON.stringify(tree, (_key, value) => typeof value === 'function' ? value.name : value);
  assert.ok(text.includes('PROVIDER PREVIEW · REVIEW PENDING')); assert.ok(!text.includes('REAL SOURCE SNAPSHOT')); assert.ok(!text.includes('Playback adds'));
  assert.equal(findNode(tree, node => node.type === 'button' && node.props.children === 'Trend'), undefined);
  const tableHarness = await recordHarness();
  const table = tableHarness.render(tableHarness.exports.RecordTable, { model, records: model.records, controls: {}, change() {}, onSelect() {} });
  const tableText = JSON.stringify(table); assert.ok(tableText.includes('309.65')); assert.ok(tableText.includes('706,062.5')); assert.ok(tableText.includes('Not recorded')); assert.ok(tableText.includes('0.00'));
  const empty = tableHarness.render(tableHarness.exports.RecordTable, { model, records: [], controls: {}, change() {}, onSelect() {} });
  assert.ok(JSON.stringify(empty).includes('No samples match. Clear a selection filter or change the measurement bounds.'));
  assert.ok(!JSON.stringify(empty).includes('selected period')); tableHarness.dispose();
  const evidence = harness.render(harness.exports.Provenance, { bundle, model, records: model.records });
  const evidenceText = JSON.stringify(evidence); for (const source of bundle.data.sourceSnapshots) assert.ok(evidenceText.includes(source.rawSha256));
  assert.ok(!evidenceText.includes('have no numeric time coordinate')); harness.dispose();
});

test('group-summary CSV includes identical bounded analysis context only for opted-in datasets', async () => {
  const dataset = adapter.createNeonScienceDataset(receiptFixture()), downloads = [], harness = await recordHarness(downloads);
  const render = bundle => { const model = recordModel.recordModel(bundle); return harness.render(harness.exports.SciencePanel, { bundle, model, records: model.records, controls: {}, change() {}, metric: recordModel.metricOf(model), time: null, onSelect() {} }); };
  let tree = render(dataset.bundle); findNode(tree, node => node.type === 'button' && node.props.children === 'Download summary CSV ↓').props.onClick();
  const csv = downloads[0].rows, header = csv[0], context = csv[1][header.indexOf('analysis_context')]; assert.equal(context, recordModel.analysisContextCSV(dataset.bundle.data.analysisContext));
  assert.equal(csv[1][header.indexOf('records')], 64); assert.equal(csv[1][header.indexOf('missing')], 1); assert.ok(Math.abs(csv[1][header.indexOf('mean')] - (62*12.25)/63) < 1e-12);
  const ordinary = structuredClone(dataset.bundle); delete ordinary.data.analysisContext;
  tree = render(ordinary); findNode(tree, node => node.type === 'button' && node.props.children === 'Download summary CSV ↓').props.onClick(); assert.ok(!downloads[1].rows[0].includes('analysis_context'));
  harness.dispose();
});

test('RecordLab renders actual spatial preview through React with readable defaults and preserved legacy badge', async () => {
  let source = compile(await readFile('app/living-welcome/stories/record-lab.jsx', 'utf8'));
  const crossing = url('export default {}'), empty = url('export default {}');
  for (const [from,to] of [['react',import.meta.resolve('react')],['react/jsx-runtime',import.meta.resolve('react/jsx-runtime')],['next/link',url('export default "a"')],['../../labs/then-now/crossing.json',crossing],['./story-kit.mjs',new URL('../app/living-welcome/stories/story-kit.mjs',import.meta.url).href],['./record-model.mjs',new URL('../app/living-welcome/stories/record-model.mjs',import.meta.url).href],['./science-model.mjs',new URL('../app/living-welcome/stories/science-model.mjs',import.meta.url).href]]) source=source.replaceAll(`from '${from}'`,`from '${to}'`).replaceAll(`from "${from}"`,`from "${to}"`);
  source=source.replace(/import ['"]\.\/record-lab\.css['"];?/,`import '${empty}';`);
  const { default: RecordLab } = await import(url(source)), bundle = adapter.createNeonScienceDataset(receiptFixture()).bundle;
  const html = renderToStaticMarkup(createElement(RecordLab,{bundle,time:null,controls:{view:'chart'},onControls(){}})); assert.match(html,/309\.65/); assert.doesNotMatch(html,/Date not recorded|Playback adds an upper-year boundary|REAL SOURCE SNAPSHOT/);
  const legacy=structuredClone(bundle);delete legacy.data.sourceLabel;delete legacy.data.recordKind; assert.match(renderToStaticMarkup(createElement(RecordLab,{bundle:legacy})),/REAL SOURCE SNAPSHOT/);
});

test('terrain is discoverable as a guided lab without entering static snapshot manifests', async () => {
  assert.equal(STORIES.find(story => story.id === 'neon-terrain')?.href, '/labs/terrain'); assert.equal(STORIES.find(story => story.id === 'neon-terrain')?.status, 'guided'); assert.ok(!Object.hasOwn(PUBLIC_LAB_SNAPSHOTS,'neon-terrain'));
  const acquisition = await readFile('app/acquisition/workspace.tsx','utf8'); assert.ok(acquisition.indexOf('<NeonLidarPanel') < acquisition.indexOf('<StoragePanel'));
  assert.ok(!acquisition.includes('This page does not connect to your computer'));
});
