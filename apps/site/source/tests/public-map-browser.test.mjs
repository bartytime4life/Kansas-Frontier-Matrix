import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode, settle } from './component-harness.mjs';
const compile = async file => ts.transpileModule(await readFile(file, 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const url = source => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;
const modelUrl = url(await compile('app/public-map-catalog.ts')), model = await import(modelUrl);
const boundedUrl = url(await compile('app/bounded-json.ts'));
const client = await import(url((await compile('app/public-map-client.ts')).replace('"./bounded-json"', JSON.stringify(boundedUrl)).replace('"./public-map-catalog"', JSON.stringify(modelUrl))));
const css = { default: new Proxy({}, { get: (_, key) => key }) };
const pinnedSeed = JSON.parse(await readFile('app/public-map-catalog.json', 'utf8'));
const catalog = {
  schema: 'kfm-public-map-catalog/v1', generatedAt: '2026-10-08T18:00:00Z', coverage: [{ sourceId: 'test', title: 'Synthetic Kansas maps', state: 'partial', recordCount: 22, expectedCount: 30, reason: 'Remaining records not fetched.', checkedAt: '2026-10-08T18:00:00Z' }],
  records: Array.from({ length: 22 }, (_, i) => ({ id: `map-${i}`, sourceId: 'test', publisher: 'USGS', title: `Kansas test ${i}`, counties: ['Allen'], mapYear: 1900 + i, digitalYear: 2020, scale: '1:24,000', scaleUnit: 'denominator', metadataUrl: 'https://pubs.usgs.gov/test/', rights: { status: 'unknown', text: 'Synthetic fixture only.', url: null }, description: 'A test map.', geometryRole: 'catalog footprint', bbox: null, point: null, assets: [{ id: `asset-${i}`, title: `Original ${i}`, format: 'PDF', url: 'https://pubs.usgs.gov/test.pdf', expectedBytes: 100, kind: 'download', availability: 'verified', checkedAt: null }] })),
};
const status = () => ({ schema: 'kfm-public-map-download-control/v1', sessionToken: 'a'.repeat(43), active: null, limitBytes: 500_000_000_000, jobs: [], refresh: { state: 'idle' } });
const nmmrCatalog = () => ({ ...structuredClone(pinnedSeed),
  records: structuredClone(pinnedSeed.records.filter(row => row.sourceId === 'osmre-nmmr')),
  coverage: [{ sourceId: 'osmre-nmmr', title: 'OSMRE National Mine Map Repository', state: 'unavailable', recordCount: 1,
    discoveredCount: 0, seedReferenceCount: 1, expectedCount: null, checkedAt: '2026-10-08T18:00:00Z',
    reason: 'URLError: [SSL: CERTIFICATE_VERIFY_FAILED] unable to get local issuer certificate' }],
});
function nodes(node, predicate) { if (!node || typeof node !== 'object') return []; return [...(predicate(node) ? [node] : []), ...[node.props?.children].flat(Infinity).flatMap(child => nodes(child, predicate))]; }
async function harness(origin = 'https://site.example', fixtures = { catalog, status: status() }) {
  const calls = [], timers = new Map(); let timerId = 0;
  const h = await componentHarness('app/public-map-browser.tsx', {
    './public-map-catalog.json': { default: fixtures.catalog }, './public-map-catalog': model,
    './public-map-client': { ...client, publicMapRequest: (path, signal, payload, token) => new Promise(resolve => calls.push({ path, signal, payload, token, resolve })) },
    './local-download-client': { formatDownloadBytes: bytes => `${bytes} bytes` }, './public-map-preview': { PublicMapPreview: 'preview' }, 'next/link': { default: 'a' },
    './downloads/workspace.module.css': css, './public-map-browser.module.css': css,
  }, { window: { location: { origin } }, crypto: { randomUUID: () => '11111111-1111-1111-1111-111111111111' }, setTimeout: fn => { timers.set(++timerId, fn); return timerId; }, clearTimeout: id => timers.delete(id) });
  const render = () => { const tree = h.render(h.exports.default); h.commit(); return tree; };
  const respond = async (index, body, ok = true) => { calls[index].resolve({ response: { ok }, body }); await settle(); };
  const connect = async () => { let tree = render(); findNode(tree, n => n.type === 'button' && n.props.children === 'Connect map downloads').props.onClick(); render(); await respond(0, fixtures.status); await respond(1, fixtures.catalog); return render(); };
  const tick = async () => { const [id, fn] = timers.entries().next().value; timers.delete(id); void fn(); await settle(); };
  return { h, render, respond, connect, calls, timers, tick };
}
test('catalog renders 20 records per page, independent source coverage and no automatic transfer', async () => {
  const { h, render, calls } = await harness(); let tree = render();
  assert.equal(calls.length, 0, 'hosted browsing does not connect to the computer');
  const list = findNode(tree, n => n.type === 'ul' && n.props.className === 'records');
  assert.equal(nodes(list, n => n.type === 'li').length, 20); assert.match(JSON.stringify(tree), /Partial catalog/);
  findNode(tree, n => n.type === 'button' && n.props.children === 'Next maps').props.onClick(); tree = render();
  assert.equal(nodes(findNode(tree, n => n.type === 'ul' && n.props.className === 'records'), n => n.type === 'li').length, 2);
  const search = findNode(tree, n => n.type === 'input' && n.props.type === 'search'); search.props.onChange({ target: { value: 'Kansas test 21' } }); tree = render();
  assert.equal(nodes(findNode(tree, n => n.type === 'ul' && n.props.className === 'records'), n => n.type === 'li').length, 1);
  assert.equal(calls.length, 0); h.dispose();
});
test('the loopback Site connects to this computer on mount without a click', async () => {
  const { h, render, respond, calls } = await harness('http://127.0.0.1:4173'); render(); render();
  assert.equal(calls.length, 1, 'one status request on mount'); assert.equal(calls[0].path, '/status');
  await respond(0, status()); await respond(1, catalog);
  const tree = render(); assert.ok(findNode(tree, n => n.type === 'button' && n.props.children === 'Reconnect map downloads'));
  h.dispose();
});
test('a selection change clears file/limit and discards a delayed download notice without duplicating the request', async () => {
  const { h, render, calls, respond, connect } = await harness(); let tree = await connect();
  const selectMap = index => { const list = findNode(tree, n => n.type === 'ul' && n.props.className === 'records'); nodes(list, n => n.type === 'button')[index].props.onClick(); tree = render(); };
  selectMap(0); findNode(tree, n => n.type === 'button' && n.props.children === 'Select file to download').props.onClick(); tree = render();
  let submit = findNode(tree, n => n.type === 'button' && n.props.children === 'Download selected original'); assert.equal(submit.props.disabled, true);
  findNode(tree, n => n.type === 'input' && n.props.type === 'number').props.onChange({ target: { value: '1' } }); tree = render();
  submit = findNode(tree, n => n.type === 'button' && n.props.children === 'Download selected original'); assert.equal(submit.props.disabled, false); submit.props.onClick(); submit.props.onClick();
  assert.equal(calls.filter(c => c.path === '/downloads').length, 1); assert.equal(calls[2].payload.assetId, 'asset-0'); assert.equal(calls[2].payload.maxBytes, 1024 * 1024); assert.equal(calls[2].token, 'a'.repeat(43));
  tree = render(); selectMap(1); assert.equal(findNode(tree, n => n.type === 'input' && n.props.type === 'number'), undefined);
  await respond(2, { id: 'a'.repeat(32) }); tree = render();
  assert.doesNotMatch(JSON.stringify(tree), /Download requested/); assert.match(JSON.stringify(tree), /Kansas test 1/);
  h.dispose(); assert.ok(calls.filter(c => ['/status', '/catalog'].includes(c.path)).every(c => c.signal.aborted));
});
test('failed local reconnect retains metadata while disabling downloads and labels job freshness', async () => {
  const { h, render, connect, calls, respond } = await harness(); let tree = await connect();
  findNode(tree, n => n.type === 'button' && n.props.children === 'Reconnect map downloads').props.onClick(); render();
  await respond(2, {}, false); tree = render();
  assert.match(JSON.stringify(tree), /Public-map downloads are unavailable/); assert.match(JSON.stringify(tree), /Kansas test 0/);
  assert.equal(findNode(tree, n => n.type === 'button' && n.props.children === 'Refresh all Kansas records').props.disabled, true);
  assert.equal(calls.length, 3); h.dispose();
});
test('verified originals open their exact document or archive URL without starting a local download', async () => {
  const input = structuredClone(catalog), first = input.records[0];
  first.assets = ['PDF', 'JPEG', 'TIFF', 'ZIP'].map(format => ({ ...first.assets[0], id: `original-${format}`, format, url: `https://pubs.usgs.gov/original.${format.toLowerCase()}` }));
  const { h, render, calls } = await harness('https://site.example', { catalog: input, status: status() }); let tree = render();
  const list = findNode(tree, n => n.type === 'ul' && n.props.className === 'records'); nodes(list, n => n.type === 'button')[0].props.onClick(); tree = render();
  const assets = findNode(tree, n => n.type === 'ul' && n.props.className === 'assets'), links = nodes(assets, n => n.type === 'a');
  const detail = findNode(tree, n => n.type === 'aside' && n.props['aria-label'] === 'Selected public map');
  assert.match(JSON.stringify(detail), /Original map CRS/); assert.match(JSON.stringify(detail), /Spatial accuracy/);
  assert.equal(nodes(detail, n => n.type === 'dd' && n.props.children === 'Not supplied by catalog').length, 2);
  assert.equal(links.length, 4);
  for (const [index, link] of links.entries()) {
    assert.equal(link.props.href, first.assets[index].url); assert.equal(link.props.target, '_blank'); assert.equal(link.props.rel, 'noreferrer');
    assert.match(JSON.stringify(link.props.children), index === 3 ? /Open original file/ : /Open original document/);
  }
  assert.equal(nodes(assets, n => n.type === 'button' && n.props.children === 'Select file to download').length, 4);
  assert.equal(calls.length, 0); h.dispose();
});
test('selected storage impact and stored-file hash remain distinct from transfer maximum and provider verification', async () => {
  const checked = status(); checked.jobs.push({ id: 'b'.repeat(32), assetId: 'asset-0', title: 'Stored test original', state: 'downloaded', bytes: 100, expectedBytes: 100, maxBytes: 1048576, sha256: 'c'.repeat(64), destination: '/private/candidate', reason: null, mapReady: false, createdAt: '2026-10-08T18:00:00Z', updatedAt: '2026-10-08T18:00:00Z' });
  const { h, render, connect } = await harness('https://site.example', { catalog, status: checked }); let tree = await connect();
  const list = findNode(tree, n => n.type === 'ul' && n.props.className === 'records'); nodes(list, n => n.type === 'button')[0].props.onClick(); tree = render();
  findNode(tree, n => n.type === 'button' && n.props.children === 'Select file to download').props.onClick(); tree = render();
  findNode(tree, n => n.type === 'input' && n.props.type === 'number').props.onChange({ target: { value: '1' } }); tree = render();
  const impact = findNode(tree, n => n.type === 'p' && JSON.stringify(n.props.children).includes('Storage for this original'));
  assert.match(JSON.stringify(impact), /100 bytes at the currently reported size/); assert.match(JSON.stringify(impact), /1048576 bytes/); assert.match(JSON.stringify(impact), /additional space/);
  const details = findNode(tree, n => n.type === 'details' && n.props.className === 'jobDetails');
  assert.match(JSON.stringify(details), /Stored-file SHA-256/); assert.match(JSON.stringify(details), new RegExp('c'.repeat(64)));
  assert.match(JSON.stringify(details), /Provider checksum verification/); assert.match(JSON.stringify(details), /Not performed/); h.dispose();
});
test('unavailable source coverage stays unknown and unfinished jobs do not claim a stored original', async () => {
  const input = structuredClone(catalog); input.records = input.records.slice(0, 1);
  input.coverage = [{ sourceId: 'test', title: 'Unavailable source', state: 'unavailable', recordCount: 1, discoveredCount: 0, seedReferenceCount: 1, expectedCount: null, reason: 'URLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:997)', checkedAt: '2026-10-08T18:00:00Z' }];
  const checked = status(); checked.jobs = ['queued', 'downloading', 'cancelled', 'downloaded'].map((state, index) => ({ id: String(index + 1).repeat(32), assetId: 'asset-0', title: state, state, bytes: state === 'downloaded' ? 100 : 0, expectedBytes: 100, maxBytes: 1048576, sha256: state === 'downloaded' ? 'c'.repeat(64) : null, destination: '/private/candidate', reason: null, mapReady: false, createdAt: '2026-10-08T18:00:00Z', updatedAt: '2026-10-08T18:00:00Z' }));
  const { h, connect } = await harness('https://site.example', { catalog: input, status: checked }); const tree = await connect();
  const coverage = findNode(tree, n => n.type === 'details' && n.props.className === 'coverage');
  assert.match(JSON.stringify(coverage), /Coverage unknown/); assert.match(JSON.stringify(coverage), /1 starting references/);
  assert.doesNotMatch(JSON.stringify(coverage), /0 records|ssl\.c|CERTIFICATE_VERIFY_FAILED|URLError/);
  assert.match(JSON.stringify(coverage), /secure connection could not be verified/);
  const jobs = nodes(tree, n => n.type === 'article' && n.props.className === 'job');
  for (const job of jobs) {
    const note = findNode(job, n => n.type === 'p' && n.props.className === 'jobNote');
    assert.match(JSON.stringify(note), job.props['data-state'] === 'downloaded' ? /Stored original candidate/ : /Captured bytes remain candidates/);
    if (job.props['data-state'] !== 'downloaded') assert.doesNotMatch(JSON.stringify(note), /Stored original candidate/);
  }
  h.dispose();
});
const coverageOf = tree => findNode(tree, n => n.type === 'details' && n.props.className === 'coverage');
const researchLinks = tree => nodes(findNode(coverageOf(tree), n => n.type === 'nav' && n.props['aria-label'] === 'Official NMMR research'), n => n.type === 'a');
function assertResearchLinks(tree) {
  const links = researchLinks(tree);
  assert.deepEqual(links.map(link => link.props.href), ['https://mmr.osmre.gov/', 'https://mmr.osmre.gov/Request']);
  for (const link of links) {
    assert.equal(link.props.target, '_blank'); assert.equal(link.props.rel, 'noopener noreferrer');
    assert.match(link.props['aria-label'], /opens in a new tab/);
    assert.equal(link.props.tabIndex, undefined, 'native anchors keep their normal keyboard focus');
    assert.equal(link.props.onClick, undefined, 'navigation does not call the download service');
    assert.equal(link.props.disabled, undefined);
  }
}
test('unavailable NMMR coverage exposes native official links before selection and after zero filter matches', async () => {
  const { h, render, calls } = await harness('https://site.example', { catalog: nmmrCatalog(), status: status() });
  let tree = render(); assertResearchLinks(tree);
  assert.match(JSON.stringify(coverageOf(tree)), /Catalog unavailable.*Coverage unknown/);
  assert.match(JSON.stringify(coverageOf(tree)), /index points are finding aids, not mine boundaries/);
  assert.match(JSON.stringify(coverageOf(tree)), /Original archival scans require a separate request/);
  assert.doesNotMatch(JSON.stringify(coverageOf(tree)), /0 records|CERTIFICATE_VERIFY_FAILED/);
  findNode(tree, n => n.type === 'input' && n.props.type === 'search').props.onChange({ target: { value: 'no-such-synthetic-map' } });
  tree = render(); assertResearchLinks(tree);
  assert.match(JSON.stringify(tree), /No catalog records match these filters/);
  assert.match(JSON.stringify(coverageOf(tree)), /Coverage unknown/);
  assert.equal(calls.length, 0, 'search links require no local connection or automatic acquisition'); h.dispose();
});
test('a failed local connection leaves NMMR coverage and research navigation available', async () => {
  const { h, render, respond, calls } = await harness('https://site.example', { catalog: nmmrCatalog(), status: status() });
  let tree = render(); findNode(tree, n => n.type === 'button' && n.props.children === 'Connect map downloads').props.onClick(); render();
  await respond(0, {}, false); tree = render(); assertResearchLinks(tree);
  assert.match(JSON.stringify(tree), /Public-map downloads are unavailable/);
  assert.match(JSON.stringify(coverageOf(tree)), /Coverage unknown/); assert.equal(calls.length, 1); h.dispose();
});
test('successful refresh replaces unavailable coverage with checked zero results while retaining pinned navigation', async () => {
  const { h, render, respond, connect, calls, tick } = await harness('https://site.example', { catalog: nmmrCatalog(), status: status() });
  let tree = await connect();
  findNode(tree, n => n.type === 'button' && n.props.children === 'Refresh all Kansas records').props.onClick();
  assert.equal(calls[2].path, '/refresh'); await respond(2, {}); render();
  const running = status(); running.refresh.state = 'running'; await respond(3, running);
  await respond(4, nmmrCatalog()); tree = render(); assert.match(JSON.stringify(coverageOf(tree)), /Coverage unknown/); await tick();
  const complete = status(); complete.refresh.state = 'complete'; await respond(5, complete);
  assert.equal(calls[6].path, '/catalog');
  const recovered = nmmrCatalog(); Object.assign(recovered.coverage[0], { state: 'complete', expectedCount: 0, reason: 'Synthetic checked zero index-point results.' });
  recovered.sourceUrls = ['https://mmr.osmre.gov.attacker.example/'];
  recovered.records[0].assets.find(a => a.kind === 'request').url = 'https://mmr.osmre.gov.attacker.example/Request';
  await respond(6, recovered); tree = render(); assertResearchLinks(tree);
  assert.match(JSON.stringify(coverageOf(tree)), /Catalog checked.*0 \/ 0 records/);
  assert.doesNotMatch(JSON.stringify(coverageOf(tree)), /Coverage unknown|secure connection could not be verified|attacker/);
  assert.match(JSON.stringify(coverageOf(tree)), /No results do not establish absence of mining/);
  assert.equal(calls.some(c => c.path === '/downloads'), false); h.dispose();
});
test('a failed catalog read retains unknown coverage and retries on the next healthy status poll', async () => {
  const { h, render, respond, calls, tick } = await harness('https://site.example', { catalog: nmmrCatalog(), status: status() });
  let tree = render(); findNode(tree, n => n.type === 'button' && n.props.children === 'Connect map downloads').props.onClick(); render();
  await respond(0, status()); await respond(1, {}, false); tree = render(); assertResearchLinks(tree);
  assert.match(JSON.stringify(tree), /Previously checked metadata remains visible/);
  assert.match(JSON.stringify(coverageOf(tree)), /Coverage unknown/);
  await tick(); await respond(2, status());
  assert.equal(calls[3]?.path, '/catalog', 'a healthy idle service retries the failed catalog read');
  const recovered = nmmrCatalog(); Object.assign(recovered.coverage[0], { state: 'complete', expectedCount: 0, reason: 'Synthetic checked zero results.' });
  await respond(3, recovered); tree = render(); assertResearchLinks(tree);
  assert.doesNotMatch(JSON.stringify(tree), /Previously checked metadata remains visible|Coverage unknown/);
  await tick(); await respond(4, status()); assert.equal(calls.length, 5, 'successful recovery ends catalog retries');
  assert.equal(calls.some(c => c.path === '/downloads'), false); h.dispose();
});
