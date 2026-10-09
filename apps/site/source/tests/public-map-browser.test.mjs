import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode } from './component-harness.mjs';
const source = ts.transpileModule(await readFile('app/public-map-catalog.ts', 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const seed = JSON.parse(await readFile('app/public-map-catalog.json', 'utf8'));
const model = await import(`data:text/javascript;base64,${Buffer.from(source).toString('base64')}`);
function nodes(tree, predicate) { if (!tree || typeof tree !== 'object') return []; return [...(predicate(tree) ? [tree] : []), ...[tree.props?.children].flat(Infinity).flatMap(child => nodes(child, predicate))]; }
const css = { default: new Proxy({}, { get: (_target, key) => key }) };
const catalog = { schema: 'kfm-public-map-catalog/v1', coverage: [{ sourceId: 'test', title: 'Test source', state: 'complete', recordCount: 22, expectedCount: 22, reason: 'Synthetic catalog.', checkedAt: '2026-10-08T18:00:00Z' }], records: Array.from({ length: 22 }, (_, i) => ({ id: `map-${i}`, sourceId: 'test', publisher: 'USGS', title: `Kansas test ${i}`, counties: ['Allen'], mapYear: 1900 + i, digitalYear: 2020, scale: '1:24,000', scaleUnit: 'denominator', metadataUrl: 'https://pubs.usgs.gov/test/', rights: { status: 'unknown', text: 'Synthetic fixture only.', url: null }, description: 'A test map.', geometryRole: 'catalog footprint', bbox: null, point: null, assets: [{ id: `asset-${i}`, title: `Original ${i}`, format: 'PDF', url: 'https://pubs.usgs.gov/test.pdf', expectedBytes: 100, kind: 'download', availability: 'verified', checkedAt: null }] })) };
const status = () => ({ schema: 'kfm-public-map-download-control/v1', sessionToken: 'a'.repeat(43), active: null, limitBytes: 500_000_000_000, jobs: [], refresh: { state: 'idle' } });
const content = node => JSON.stringify(node?.props?.children);
const visibleText = node => typeof node === 'string' || typeof node === 'number' ? String(node) : [node?.props?.children].flat(Infinity).filter(child => child != null && child !== false).map(visibleText).join(' ');
const button = (tree, text) => findNode(tree, node => node.type === 'button' && content(node).includes(text));
async function harness(input = structuredClone(catalog)) {
  const calls = [], selected = [], focused = [], reveals = [], events = new Map(); const document = { activeElement: null };
  const downloads = { catalog: input, status: status(), connection: 'connected', busy: null, catalogError: null, notice: '', selectAsset: id => selected.push(id), refreshCatalog: async () => calls.push('refresh'), startDownload: async (asset, maximum) => calls.push({ assetId: asset.id, maximum }) };
  const h = await componentHarness('app/public-map-browser.tsx', { './public-map-catalog.json': { default: seed }, './public-map-catalog': model, './local-download-client': { formatDownloadBytes: value => `${value} bytes` }, './public-map-preview': { PublicMapPreview: 'preview' }, './download-focus': { revealTransferControls: (field, action) => reveals.push({ field, action }) }, './downloads/workspace.module.css': css, './public-map-browser.module.css': css }, { document, window: { matchMedia: () => ({ matches: true }), addEventListener: (name, callback) => events.set(name, callback), removeEventListener: name => events.delete(name) } });
  let blocked = false;
  const render = () => { const tree = h.render(h.exports.default, { downloads, blockedByOtherDownload: blocked, onViewActivity: () => calls.push('activity') }); for (const node of nodes(tree, n => n.props?.ref)) node.props.ref.current = { focus() { focused.push(node.type); document.activeElement = this; }, scrollIntoView: () => focused.push('scroll') }; h.commit(); return tree; };
  const choose = (tree, index = 0) => { button(tree, `Kansas test ${index}`).props.onClick(); return render(); };
  return { h, downloads, calls, selected, focused, reveals, events, document, render, choose, block: value => { blocked = value; } };
}
test('workbench pages every record in groups of eight, keeps filters progressive and browsing never starts transfers', async () => {
  const p = await harness(); let tree = p.render();
  const rows = () => nodes(findNode(tree, n => n.type === 'ul' && n.props.className === 'records'), n => n.type === 'li');
  assert.equal(rows().length, 8); assert.equal(findNode(tree, n => n.type === 'details' && n.props.className === 'coverage').props.open, undefined);
  assert.equal(findNode(tree, n => n.type === 'details' && n.props.className === 'filterDetails').props.open, undefined);
  button(tree, 'Next').props.onClick(); tree = p.render(); assert.match(content(rows()[0]), /Kansas test 8/);
  findNode(tree, n => n.type === 'input' && n.props.type === 'search').props.onChange({ target: { value: 'Kansas test 21' } }); tree = p.render(); assert.equal(rows().length, 1);
  assert.match(JSON.stringify(tree), /Clear /); button(tree, 'Clear ').props.onClick(); tree = p.render(); assert.equal(rows().length, 8); assert.deepEqual(p.calls, []); p.h.dispose();
});
test('known file uses a visible editable rounded-up maximum and requires a final explicit start; cross-provider work blocks it', async () => {
  const p = await harness(); let tree = p.choose(p.render()); button(tree, 'Download ').props.onClick(); tree = p.render();
  const maximum = findNode(tree, n => n.type === 'input' && n.props.type === 'number'); assert.equal(maximum.props.value, '1'); assert.deepEqual(p.calls, []);
  let start = button(tree, 'Download to this computer'); assert.equal(start.props.disabled, false);
  p.block(true); tree = p.render(); assert.equal(button(tree, 'Download to this computer').props.disabled, true); assert.match(JSON.stringify(tree), /already running/);
  p.block(false); p.downloads.connection = 'unavailable'; tree = p.render(); assert.equal(button(tree, 'Download to this computer').props.disabled, true);
  p.downloads.connection = 'connected'; tree = p.render(); button(tree, 'Download to this computer').props.onClick(); assert.deepEqual(p.calls, [{ assetId: 'asset-0', maximum: 1048576 }]);
  assert.match(JSON.stringify(tree), /Storage for this original/); assert.match(JSON.stringify(tree), /at the currently reported size/); p.h.dispose();
});
test('unknown file requires a cap, selection changes clear that cap and return focus to results', async () => {
  const input = structuredClone(catalog); input.records[0].assets[0].expectedBytes = null;
  const p = await harness(input); let tree = p.choose(p.render()); button(tree, 'Download ').props.onClick(); tree = p.render();
  let maximum = findNode(tree, n => n.type === 'input' && n.props.type === 'number'); assert.equal(maximum.props.value, ''); assert.equal(button(tree, 'Download to this computer').props.disabled, true);
  maximum.props.onChange({ target: { value: '2' } }); tree = p.render(); assert.equal(button(tree, 'Download to this computer').props.disabled, false);
  tree = p.choose(tree, 1); assert.equal(findNode(tree, n => n.type === 'input' && n.props.type === 'number'), undefined); assert.equal(p.selected.at(-1), null);
  button(tree, 'Back to results').props.onClick(); tree = p.render(); assert.equal(findNode(tree, n => n.props?.['data-selection'] === false).props['data-selection'], false); assert.ok(p.focused.includes('h2')); assert.ok(p.focused.includes('scroll')); p.h.dispose();
});
test('original links retain exact URLs and stored copies require a deliberate new capture', async () => {
  const input = structuredClone(catalog); input.records[0].assets.push({ ...input.records[0].assets[0], id: 'zip-0', format: 'ZIP', url: 'https://pubs.usgs.gov/original.zip' });
  const p = await harness(input); p.downloads.status.jobs = [{ id: 'b'.repeat(32), assetId: 'asset-0', state: 'downloaded', bytes: 100 }]; let tree = p.choose(p.render());
  const originals = nodes(tree, n => n.type === 'a' && content(n).includes('Open original')); assert.deepEqual(originals.map(n => n.props.href), ['https://pubs.usgs.gov/test.pdf', 'https://pubs.usgs.gov/original.zip']); for (const link of originals) { assert.equal(link.props.target, '_blank'); assert.equal(link.props.rel, 'noreferrer'); }
  button(tree, 'Download ').props.onClick(); tree = p.render(); assert.match(JSON.stringify(tree), /already stored/); assert.ok(button(tree, 'Download a new copy')); assert.deepEqual(p.calls, []); p.h.dispose();
});
test('unavailable source remains visible in collapsed summary, rights hold and unknown map CRS remain explicit', async () => {
  const input = structuredClone(catalog); input.records[0].rights.status = 'held'; input.coverage = [{ sourceId: 'test', title: 'OSMRE', state: 'unavailable', recordCount: 1, discoveredCount: 0, seedReferenceCount: 1, expectedCount: null, reason: 'URLError: [SSL: CERTIFICATE_VERIFY_FAILED] unable to get local issuer certificate (_ssl.c:997)', checkedAt: null }];
  const p = await harness(input); let tree = p.choose(p.render()); const coverage = findNode(tree, n => n.type === 'details' && n.props.className === 'coverage');
  assert.match(content(findNode(coverage, n => n.type === 'summary')), /OSMRE: unknown/); assert.match(JSON.stringify(coverage), /Coverage unknown/); assert.doesNotMatch(JSON.stringify(coverage), /0 records|ssl\.c|CERTIFICATE_VERIFY_FAILED/);
  assert.match(JSON.stringify(tree), /Source reuse terms are held/); assert.match(JSON.stringify(tree), /Original map CRS/); assert.match(JSON.stringify(tree), /Not supplied by catalog/); p.h.dispose();
});

test('file selection reveals the focused maximum and its final action together and rechecks after keyboard viewport changes', async () => {
  const p = await harness(); let tree = p.choose(p.render()); button(tree, 'Download ').props.onClick(); tree = p.render();
  assert.equal(p.reveals.length, 1); assert.equal(p.reveals[0].field, p.document.activeElement); assert.ok(p.reveals[0].action);
  p.events.get('resize')(); assert.equal(p.reveals.length, 2);
  p.document.activeElement = null; p.events.get('resize')(); assert.equal(p.reveals.length, 2, 'do not move the page after focus leaves the maximum');
  p.h.dispose(); assert.equal(p.events.size, 0);
});

test('seed and refreshed catalogs show only direct files and omit request-only sources even offline', async () => {
  const p = await harness(structuredClone(seed)); p.downloads.connection = 'unavailable';
  let tree = p.render();
  const records = () => nodes(findNode(tree, n => n.type === 'ul' && n.props.className === 'records'), n => n.type === 'li');
  assert.equal(records().length, 8);
  assert.doesNotMatch(JSON.stringify(tree), /NMMR|OSMRE|Request an original|No verified direct file|Source record \/ request/);
  assert.equal(button(tree, 'Next').props.disabled, true);
  const input = structuredClone(catalog);
  input.records[0].assets.push({ ...input.records[0].assets[0], id: 'request', title: 'Purchase archival scan', kind: 'request', availability: 'request-only' });
  input.records[1].assets = []; input.records[1].publisher = 'Metadata publisher';
  input.records[2].assets[0].availability = 'unverified';
  input.records[3].rights.status = 'purchase-required';
  p.downloads.catalog = input; tree = p.render(); tree = p.choose(tree);
  assert.doesNotMatch(visibleText(tree), /Purchase archival scan|Metadata publisher|Request from the archive|Check with publisher|No direct files/);
  assert.equal(nodes(tree, n => n.type === 'a' && content(n).includes('Open original')).length, 1);
  findNode(tree, n => n.type === 'input' && n.props.type === 'search').props.onChange({ target: { value: 'Kansas test 1' } });
  tree = p.render(); assert.equal(records().length, 8); // Matches 10–19, not metadata-only record 1.
  assert.ok(!records().some(row => nodes(row, n => n.type === 'strong').some(n => n.props.children === 'Kansas test 1')));
  assert.deepEqual(p.calls, []); p.h.dispose();
});
test('a refreshed catalog that loses the selected direct file clears transfer controls', async () => {
  const p = await harness(); let tree = p.choose(p.render()); button(tree, 'Download ').props.onClick(); tree = p.render();
  assert.ok(button(tree, 'Download to this computer'));
  const next = structuredClone(catalog); next.records[0].assets[0].availability = 'request-only';
  p.downloads.catalog = next; tree = p.render();
  assert.equal(button(tree, 'Download to this computer'), undefined);
  assert.equal(findNode(tree, n => n.type === 'input' && n.props.type === 'number'), undefined);
  assert.equal(p.selected.at(-1), null); assert.deepEqual(p.calls, []); p.h.dispose();
});
