import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import ts from 'typescript';
import { componentHarness, findNode, settle } from './component-harness.mjs';
const moduleAt = async file => import(`data:text/javascript;base64,${Buffer.from(ts.transpileModule(await readFile(file, 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString('base64')}`);
const model = await moduleAt('app/history-reader-model.ts'), maps = await moduleAt('app/public-map-catalog.ts');
const sources = JSON.parse(await readFile('app/history-sources.json')), seed = JSON.parse(await readFile('app/public-map-catalog.json'));
const text = await readFile('public/history/prentis-1909.txt');
const inventory = JSON.parse(await readFile('public/history/sources.json', 'utf8'));
const css = new Proxy({}, { get: (_, key) => String(key) });
function nodes(tree, predicate) { const rows = []; function visit(node) { if (!node || typeof node !== 'object') return; if (predicate(node)) rows.push(node); for (const child of [node.props?.children].flat(Infinity)) visit(child); } visit(tree); return rows; }
const button = (tree, label) => findNode(tree, node => node.type === 'button' && JSON.stringify(node.props.children).includes(label));

test('all 17 supplied sources stay explicit; only two bounded originals are downloadable', () => {
  assert.equal(sources.sources.length, 17); assert.equal(new Set(sources.sources.map(row => row.url)).size, 17);
  assert.ok(sources.sources.every(row => maps.publicMapHttps(row.url) && row.rights && row.accessNote && row.coverage));
  const originals = seed.records.filter(row => row.sourceId === 'history-originals');
  assert.equal(originals.length, 2); assert.equal(originals.flatMap(row => row.assets).reduce((sum, asset) => sum + asset.expectedBytes, 0), 50864070);
  assert.ok(originals.every(row => row.bbox === null && row.mapYear === null));
  assert.equal(originals.find(row => row.id === 'history-arnold-history').rights.status, 'held');
  assert.deepEqual(sources.sources.filter(row => row.assetId).map(row => row.assetId).sort(), originals.flatMap(row => row.assets.map(asset => asset.id)).sort());
  assert.deepEqual(inventory.sources.map(row => row.url), sources.sources.map(row => row.url));
});


test('bundled OCR matches exact source bytes; search is literal and preserves passage identities', async () => {
  assert.equal(text.length, model.OCR_BYTES); assert.equal(createHash('sha256').update(text).digest('hex'), model.OCR_SHA256);
  assert.equal(await model.readHistoryText(new Response(text)), text.toString('utf8'));
  const rows = model.historyParagraphs('Fort Scott\n\nA Kansas town\n\n<script>alert(1)</script>');
  assert.equal(model.searchHistory(rows, 'fort scott')[0].number, 1);
  assert.equal(model.searchHistory(rows, '.*').length, 0);
  assert.equal(model.searchHistory(rows, '<script>')[0].number, 3);
  assert.equal(model.searchHistory(model.historyParagraphs(text.toString('utf8')), 'Topeka').length > 0, true);
});

test('reader rejects truncated, oversized, failed and same-size modified OCR', async () => {
  await assert.rejects(model.readHistoryText(new Response(text.subarray(0, 100))), /incomplete/);
  await assert.rejects(model.readHistoryText(new Response(Buffer.concat([text, Buffer.from('x')]))), /exceeded/);
  const changed = Buffer.from(text); changed[50] ^= 1;
  await assert.rejects(model.readHistoryText(new Response(changed)), /checksum/);
  await assert.rejects(model.readHistoryText(new Response('no', { status: 503 })), /could not/);
});

test('history browsing never transfers; selection requires connection and a valid explicit limit', async () => {
  const calls = []; const downloads = { catalog: seed, status: { limitBytes: 500e9, jobs: [], assetStates: [], active: null }, connection: 'idle', busy: null, selectAsset: id => calls.push(['select', id]), startDownload: (asset, limit) => calls.push(['download', asset.id, limit]) };
  const harness = await componentHarness('app/history-browser.tsx', { 'next/link': { default: 'a' }, './history-sources.json': { default: sources }, './public-map-catalog': maps, './public-map-download-state': { publicMapDownloadState: () => ({ label: 'Not downloaded' }) }, './local-download-client': { formatDownloadBytes: String }, './downloads/workspace.module.css': css, './history.module.css': css });
  const props = { downloads, onConnect() {}, onViewActivity() {}, blocked: false };
  const render = () => { const tree = harness.render(harness.exports.default, props); harness.commit(); return tree; };
  let tree = render(); assert.equal(nodes(tree, n => n.type === 'article').length, 17); assert.equal(calls.some(row => row[0] === 'download'), false);
  button(tree, 'Save PDF').props.onClick(); tree = render(); assert.equal(button(tree, 'Download to this computer').props.disabled, true);
  downloads.connection = 'connected'; tree = render(); assert.equal(button(tree, 'Download to this computer').props.disabled, false);
  const maximum = () => findNode(tree, n => n.type === 'input' && n.props.type === 'number');
  maximum().props.onChange({ target: { value: '1' } }); tree = render(); assert.equal(button(tree, 'Download to this computer').props.disabled, true);
  maximum().props.onChange({ target: { value: '26' } }); tree = render(); button(tree, 'Download to this computer').props.onClick(); assert.deepEqual(calls.at(-1), ['download', 'history-prentis-1909-pdf', 26 * 1048576]);
  props.blocked = true; tree = render(); assert.equal(button(tree, 'Download to this computer').props.disabled, true);
  findNode(tree, n => n.type === 'select').props.onChange({ target: { value: 'book' } }); tree = render(); assert.equal(nodes(tree, n => n.type === 'article').length, 2);
  harness.dispose();
});


test('reader retry clears the error before starting another verified fetch', async () => {
  let attempts = 0;
  const responses = [];
  const harness = await componentHarness('app/history/prentis-1909/page.tsx', {
    '../../history-reader-model': model, '../../downloads/workspace.module.css': css, '../../history.module.css': css,
  }, { fetch: () => { attempts++; return new Promise(resolve => responses.push(resolve)); } });
  const render = () => { const tree = harness.render(harness.exports.default, {}); harness.commit(); return tree; };
  let tree = render();
  assert.equal(attempts, 1);
  responses.shift()(new Response('unavailable', { status: 503 })); await settle();
  tree = render(); assert.ok(findNode(tree, n => n.props?.role === 'alert'));
  button(tree, 'Retry loading').props.onClick();
  tree = render(); assert.equal(attempts, 2);
  assert.equal(findNode(tree, n => n.props?.role === 'alert'), undefined);
  assert.match(findNode(tree, n => n.type === 'output').props.children, /Loading/);
  harness.dispose();
});
