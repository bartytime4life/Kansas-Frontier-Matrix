import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';
function nodes(tree, predicate) { if (!tree || typeof tree !== 'object') return []; return [...(predicate(tree) ? [tree] : []), ...[tree.props?.children].flat(Infinity).flatMap(child => nodes(child, predicate))]; }
const css = { default: new Proxy({}, { get: (_target, key) => key }) };
const content = node => JSON.stringify(node?.props?.children);
const button = (tree, text) => findNode(tree, node => node.type === 'button' && content(node).includes(text));
async function moduleAt(path) { return import(`data:text/javascript;base64,${Buffer.from(ts.transpileModule(await readFile(path, 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString('base64')}`); }
const activity = await moduleAt('app/download-activity.ts');
const datasets = await moduleAt('app/earth-engine-data.ts');
const eeStatus = { schema: 'kfm-ee-download-control/v1', active: null, jobs: [], sessionToken: 'a'.repeat(43) };
const mapStatus = { schema: 'kfm-public-map-download-control/v1', active: null, jobs: [], sessionToken: 'b'.repeat(43), refresh: { state: 'idle' } };

test('one workbench keeps all source controllers and views mounted, defaults to Find data, and shares connect and pending state', async () => {
  const calls = [], events = new Map(); let options;
  const local = { status: eeStatus, connection: 'idle', starting: false, library: null, connect: () => calls.push('ee-connect'), refreshLibrary() {}, announcement: '' };
  const maps = { status: mapStatus, connection: 'idle', busy: null, connect: () => calls.push('maps-connect'), announcement: '' };
  const h = await componentHarness('app/downloads/workspace.tsx', {
    'next/link': { default: 'a' }, '../use-local-downloads': { useLocalDownloads: () => local }, '../use-public-map-downloads': { usePublicMapDownloads: value => { options = value; return maps; } },
    '../earth-engine-context-client': { useEarthEngineContext: () => ({ manifests: [] }) }, '../download-activity': activity,
    '../download-activity-panel': { ActivityWorkspace: 'activity', TransferPanel: 'transfer-panel' }, '../public-map-browser': { default: 'maps' }, '../earth-engine-picker': { default: 'satellite' }, '../download-library': { default: 'library' }, './workspace.module.css': css,
  }, { window: { location: { hash: '' }, addEventListener: (name, callback) => events.set(name, callback), removeEventListener: name => events.delete(name) } });
  const render = () => { const tree = h.render(h.exports.default); h.commit(); return tree; };
  let tree = render(); const view = id => findNode(tree, n => n.props?.id === id);
  assert.equal(view('download-find').props.hidden, false); assert.equal(view('download-library').props.hidden, true); assert.equal(view('download-activity').props.hidden, true);
  button(tree, 'Connect this computer').props.onClick(); assert.deepEqual(calls, ['ee-connect', 'maps-connect']);
  const mounted = () => ['maps', 'satellite', 'library', 'activity', 'transfer-panel'].map(type => findNode(tree, n => n.type === type));
  assert.ok(mounted().every(Boolean)); assert.equal(findNode(tree, n => n.type === 'maps').props.downloads, maps); assert.equal(findNode(tree, n => n.type === 'satellite').props.downloads, local);
  button(tree, 'My library').props.onClick(); tree = render(); assert.equal(view('download-library').props.hidden, false); assert.equal(view('download-find').props.hidden, true); assert.ok(mounted().every(Boolean));
  button(tree, 'Activity').props.onClick(); tree = render(); assert.equal(view('download-activity').props.hidden, false); assert.ok(mounted().every(Boolean));
  local.starting = true; tree = render(); assert.equal(findNode(tree, n => n.type === 'maps').props.blockedByOtherDownload, true); assert.equal(options.blockedByOtherDownload, true);
  maps.busy = 'download'; tree = render(); assert.equal(findNode(tree, n => n.type === 'satellite').props.blockedByOtherDownload, true);
  h.dispose(); assert.equal(events.size, 0);
});

test('activity cards use native units and cancel through the correct provider; stop limits never become total progress', async () => {
  const calls = [];
  const local = { connection: 'connected', cancelling: false, cancelJob: () => calls.push('ee') }, maps = { connection: 'connected', busy: null, cancelJob: id => calls.push(`map:${id}`) };
  const h = await componentHarness('app/download-activity-panel.tsx', { './earth-engine-data': datasets, './local-download-client': { formatDownloadBytes: value => `${value} bytes`, downloadReasons: {}, jobStateLabels: { downloading: 'Downloading', failed: 'Failed', downloaded: 'Downloaded' } }, './public-map-client': { publicMapJobLabels: { downloading: 'Downloading', cancelled: 'Cancelled', downloaded: 'Stored' }, publicMapReason: value => value }, './downloads/workspace.module.css': css });
  const ee = { id: 'a'.repeat(32), selection: { dataset: 'ee-cdl', year: 2024, maxBytes: 8e9 }, state: 'downloading', bytes: 100, completed: 2, total: 9, destination: '/local/ee', createdAt: '2026-10-08T12:00:00Z' };
  const map = { id: 'b'.repeat(32), title: 'Original PDF', state: 'downloading', assetId: 'pdf', bytes: 300, expectedBytes: 1000, maxBytes: 5000, destination: '/local/map', sha256: null, reason: null, createdAt: '2026-10-08T13:00:00Z' };
  const eeItem = activity.normalizeDownloadActivity({ ...eeStatus, jobs: [ee], active: ee.id }, null)[0], mapItem = activity.normalizeDownloadActivity(null, { ...mapStatus, jobs: [map], active: map.id })[0];
  let tree = h.render(h.exports.ActivityCard, { item: eeItem, local, maps }); let progress = findNode(tree, n => n.type === 'progress'); assert.equal(progress.props.max, 9); assert.equal(progress.props.value, 2); button(tree, 'Cancel transfer').props.onClick();
  tree = h.render(h.exports.ActivityCard, { item: mapItem, local, maps }); progress = findNode(tree, n => n.type === 'progress'); assert.equal(progress.props.max, 1000); assert.equal(progress.props.value, 300); button(tree, 'Cancel transfer').props.onClick(); assert.deepEqual(calls, ['ee', `map:${map.id}`]);
  const unknown = activity.normalizeDownloadActivity(null, { ...mapStatus, jobs: [{ ...map, expectedBytes: null }], active: map.id })[0]; tree = h.render(h.exports.ActivityCard, { item: unknown, local, maps }); progress = findNode(tree, n => n.type === 'progress'); assert.equal(progress.props.max, undefined); assert.equal(progress.props.value, undefined);
  maps.connection = 'unavailable'; tree = h.render(h.exports.ActivityCard, { item: unknown, local, maps }); assert.equal(button(tree, 'Cancel transfer').props.disabled, true); assert.match(JSON.stringify(tree), /Last known state/);
  const cancelled = activity.normalizeDownloadActivity(null, { ...mapStatus, jobs: [{ ...map, state: 'cancelled', sha256: 'c'.repeat(64) }] })[0]; tree = h.render(h.exports.ActivityCard, { item: cancelled, local, maps }); assert.match(JSON.stringify(tree), /Retained bytes/); assert.doesNotMatch(JSON.stringify(tree), /Saved candidate/); assert.match(JSON.stringify(tree), /Not performed/); h.dispose();
});

test('unified activity history exposes every job through filters and paging', async () => {
  const items = Array.from({ length: 19 }, (_, i) => ({ key: `public-map:${i}`, kind: 'public-map', nativeId: String(i), state: i === 0 ? 'downloading' : i === 1 ? 'cancelled' : 'downloaded' }));
  const h = await componentHarness('app/download-activity-panel.tsx', { './earth-engine-data': datasets, './local-download-client': { formatDownloadBytes: String }, './public-map-client': {}, './downloads/workspace.module.css': css });
  const local = { status: eeStatus, connection: 'connected' }, maps = { status: mapStatus, connection: 'connected' };
  const render = () => { const tree = h.render(h.exports.ActivityWorkspace, { items, local, maps }); h.commit(); return tree; };
  let tree = render(); const rows = () => nodes(tree, n => n.type === h.exports.ActivityCard); assert.equal(rows().length, 8);
  button(tree, 'Next').props.onClick(); tree = render(); assert.equal(rows()[0].props.item.nativeId, '8'); button(tree, 'Next').props.onClick(); tree = render(); assert.equal(rows().length, 3);
  findNode(tree, n => n.type === 'select').props.onChange({ target: { value: 'stopped' } }); tree = render(); assert.equal(rows().length, 1); assert.equal(rows()[0].props.item.state, 'cancelled'); h.dispose();
});

test('compact Earth Engine choice keeps valid source/year links and returns keyboard focus after selection', async () => {
  const focus = [];
  const h = await componentHarness('app/earth-engine-picker.tsx', { 'next/link': { default: 'a' }, './earth-engine-data': datasets, './earth-engine-downloads': { default: 'ee-download' }, './downloads/workspace.module.css': css, './public-map-browser.module.css': css }, { window: { matchMedia: () => ({ matches: true }) } });
  const local = { status: eeStatus };
  const render = () => { const tree = h.render(h.exports.default, { downloads: local, blockedByOtherDownload: true, onViewActivity() {} }); for (const n of nodes(tree, n => n.props?.ref)) n.props.ref.current = { focus: () => focus.push(n.type), scrollIntoView() {} }; h.commit(); return tree; };
  let tree = render(); button(tree, 'Cropland Data Layer').props.onClick(); tree = render(); let form = findNode(tree, n => n.type === 'ee-download'); assert.equal(form.props.downloads, local); assert.equal(form.props.blockedByOtherDownload, true); assert.equal(form.props.year, 2024); assert.equal(form.props.invalid, false);
  findNode(tree, n => n.type === 'input' && n.props.type === 'number').props.onChange({ target: { value: '2001' } }); tree = render(); form = findNode(tree, n => n.type === 'ee-download'); assert.equal(form.props.invalid, true); assert.equal(findNode(tree, n => n.type === 'a' && n.props.href.startsWith('/earth-engine?')).props.href, '/earth-engine?dataset=ee-cdl');
  button(tree, 'Back to datasets').props.onClick(); tree = render(); assert.ok(focus.includes('h2')); assert.ok(focus.includes('h3')); assert.equal(findNode(tree, n => n.type === 'ee-download'), undefined); h.dispose();
});

test('persistent panel shows pending acknowledgement without inventing a job or percentage', async () => {
  const h = await componentHarness('app/download-activity-panel.tsx', { './earth-engine-data': datasets, './local-download-client': { formatDownloadBytes: String }, './public-map-client': {}, './downloads/workspace.module.css': css });
  const local = { status: eeStatus, connection: 'connected', starting: true }, maps = { status: mapStatus, connection: 'connected', busy: null };
  let tree = h.render(h.exports.TransferPanel, { items: [], local, maps, onViewActivity() {} }); assert.match(JSON.stringify(tree), /Confirming transfer/); assert.doesNotMatch(JSON.stringify(tree), /Ready when you are/); assert.equal(tree.props['data-pending'], true);
  const progress = findNode(tree, n => n.type === 'progress'); assert.equal(progress.props.value, undefined); assert.equal(progress.props.max, undefined); assert.equal(nodes(tree, n => n.type === h.exports.ActivityCard).length, 0);
  local.starting = false; maps.busy = 'download'; tree = h.render(h.exports.TransferPanel, { items: [], local, maps, onViewActivity() {} }); assert.match(JSON.stringify(tree), /Confirming transfer/); h.dispose();
});
