import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
const moduleUrl = source => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;
const compile = async file => ts.transpileModule(await readFile(`app/${file}`, 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const modelUrl = moduleUrl(await compile('public-map-catalog.ts'));
const model = await import(modelUrl);
const boundedUrl = moduleUrl(await compile('bounded-json.ts'));
const client = await import(moduleUrl((await compile('public-map-client.ts')).replace('"./bounded-json"', JSON.stringify(boundedUrl)).replace('"./public-map-catalog"', JSON.stringify(modelUrl))));
const seed = JSON.parse(await readFile('app/public-map-catalog.json', 'utf8'));
const all = { text: '', publisher: 'all', county: 'all', year: 'all', format: 'all', availability: 'all' };
const catalog = overrides => ({ schema: 'kfm-public-map-catalog/v1', generatedAt: '2026-10-08T18:00:00Z', coverage: [{ sourceId: 'test', title: 'Synthetic catalog', state: 'complete', recordCount: 1, expectedCount: 1, reason: '', checkedAt: null }], records: [{ id: 'test-map', sourceId: 'test', publisher: 'USGS', title: 'Synthetic Kansas map', counties: ['Allen'], mapYear: 1930, digitalYear: 2020, scale: '1:24,000', scaleUnit: 'denominator', metadataUrl: 'https://pubs.usgs.gov/test/', rights: { status: 'unknown', text: 'Synthetic fixture only.', url: null }, description: 'A test record.', geometryRole: 'catalog extent, not workings', bbox: [-96,37,-95,38], point: null, assets: [{ id: 'test-pdf', title: 'Synthetic PDF', format: 'PDF', url: 'https://pubs.usgs.gov/test/map.pdf', expectedBytes: 100, kind: 'download', availability: 'verified', checkedAt: null }] }], ...overrides });
test('checked seed is a bounded reference catalog, preserving unknown sizes, dates and source rights', () => {
  assert.ok(model.parsePublicMapCatalog(seed));
  assert.ok(seed.coverage.every(row => row.state === 'seed'));
  assert.ok(seed.records.some(row => row.rights.status === 'held'));
  assert.ok(seed.records.flatMap(row => row.assets).some(row => row.expectedBytes === null));
  assert.equal(model.parsePublicMapCatalog(catalog())?.records[0].digitalYear, 2020);
  const withSeed = catalog(); Object.assign(withSeed.coverage[0], { recordCount: 2, discoveredCount: 1, seedReferenceCount: 1 });
  withSeed.records.push({ ...structuredClone(withSeed.records[0]), id: 'retained-seed', assets: [] });
  assert.ok(model.parsePublicMapCatalog(withSeed), 'retained starting references do not inflate discovered counts');
});
test('catalog parsing rejects duplicate assets, unsafe links, invalid extent and false complete counts', () => {
  for (const change of [
    v => v.records.push(structuredClone(v.records[0])),
    v => v.records[0].assets.push(structuredClone(v.records[0].assets[0])),
    v => v.records[0].metadataUrl = 'javascript:alert(1)',
    v => v.records[0].assets[0].url = 'https://username:password@example.com/map.pdf',
    v => v.records[0].bbox = [-95,37,-96,38],
    v => v.coverage[0].expectedCount = 99,
    v => v.records[0].sourceId = 'undeclared-source',
    v => v.coverage[0].recordCount = 0,
  ]) { const v = catalog(); change(v); assert.equal(model.parsePublicMapCatalog(v), null); }
  const query = catalog(); query.records[0].assets[0].url = 'https://ngmdb.usgs.gov/ngm-bin/gems_download.pl?id=3200&pid=110305'; assert.ok(model.parsePublicMapCatalog(query), 'source reference query parameters are retained, not transport authority');
});
test('source navigation accepts bounded HTTPS references and older catalogs without sourceUrls', () => {
  assert.ok(model.parsePublicMapCatalog(catalog()));
  const withSources = catalog({ sourceUrls: seed.sourceUrls });
  assert.deepEqual(model.parsePublicMapCatalog(withSources).sourceUrls, seed.sourceUrls);
  for (const sourceUrls of ['https://mmr.osmre.gov/', [null], ['javascript:alert(1)'],
    ['http://mmr.osmre.gov/'], ['https://user:secret@mmr.osmre.gov/'],
    ['https://127.0.0.1/'], ['https://mmr.osmre.gov:8443/'], Array(33).fill('https://mmr.osmre.gov/')]) {
    assert.equal(model.parsePublicMapCatalog(catalog({ sourceUrls })), null);
  }
});
test('NMMR navigation uses only the pinned official search and request references', () => {
  assert.deepEqual(model.publicMapNmmrLinks(model.parsePublicMapCatalog(seed)), {
    search: 'https://mmr.osmre.gov/', request: 'https://mmr.osmre.gov/Request',
  });
  const input = structuredClone(seed);
  input.sourceUrls = ['https://mmr.osmre.gov.attacker.example/', 'https://mmr.osmre.gov/?redirect=elsewhere'];
  const request = input.records.find(r => r.sourceId === 'osmre-nmmr').assets.find(a => a.kind === 'request');
  request.url = 'https://mmr.osmre.gov.attacker.example/Request';
  assert.deepEqual(model.publicMapNmmrLinks(model.parsePublicMapCatalog(input)), { search: null, request: null });
  assert.deepEqual(model.publicMapNmmrLinks(null), { search: null, request: null });
  request.url = 'https://mmr.osmre.gov/Request'; request.kind = 'download'; request.availability = 'verified';
  assert.equal(model.publicMapNmmrLinks(model.parsePublicMapCatalog(input)).request, null);
});
test('filters distinguish publication year, unknown counties, available files and request-only originals', () => {
  const first = catalog().records[0], other = { ...first, id: 'unknown', counties: [], mapYear: null, assets: [{ ...first.assets[0], kind: 'request', availability: 'request-only' }] };
  assert.equal(model.filterPublicMaps([first, other], { ...all, year: '2020' }).length, 0, 'digital year does not substitute for map year');
  assert.deepEqual(model.filterPublicMaps([first, other], { ...all, county: 'Allen', year: '1930', format: 'PDF', availability: 'download' }).map(r => r.id), ['test-map']);
  assert.deepEqual(model.filterPublicMaps([first, other], { ...all, county: 'unknown', availability: 'request' }).map(r => r.id), ['unknown']);
  assert.equal(model.canDownloadPublicMap(other.assets[0]), false);
});
test('map CRS and spatial accuracy remain source metadata, including explicit unknowns', () => {
  const input = catalog(); Object.assign(input.records[0], { crs: null, spatialAccuracy: null });
  assert.equal(model.parsePublicMapCatalog(input).records[0].crs, null);
  Object.assign(input.records[0], { crs: 'NAD27 / source map grid', spatialAccuracy: 'Accuracy not evaluated by publisher' });
  assert.equal(model.parsePublicMapCatalog(input).records[0].crs, 'NAD27 / source map grid');
  for (const patch of [{ crs: 4326 }, { spatialAccuracy: 25 }, { crs: '' }, { spatialAccuracy: 'x'.repeat(4001) }]) {
    const invalid = structuredClone(input); Object.assign(invalid.records[0], patch); assert.equal(model.parsePublicMapCatalog(invalid), null);
  }
});
test('selected transfer maximum must be explicit and cover a known original size', () => {
  const asset = catalog().records[0].assets[0];
  for (const value of ['', '-1', 'NaN', 'Infinity', '5e5', '0', '99999999999999999999']) assert.equal(model.publicMapSelectedLimit(value, asset), null);
  assert.equal(model.publicMapSelectedLimit('1', { ...asset, expectedBytes: 2 * 1024 * 1024 }), null);
  assert.equal(model.publicMapSelectedLimit('2', { ...asset, expectedBytes: null }), 2 * 1024 * 1024);
});
const status = () => ({ schema: 'kfm-public-map-download-control/v1', sessionToken: 'a'.repeat(43), active: null, limitBytes: 500_000_000_000, jobs: [], refresh: { state: 'idle' } });
test('job state never turns a completed capture into map approval or fabricated checksum verification', () => {
  const v = status(); v.jobs.push({ id: 'a'.repeat(32), assetId: 'test-pdf', title: 'Test', state: 'downloaded', bytes: 100, expectedBytes: 100, maxBytes: 200, sha256: 'b'.repeat(64), destination: '/private/candidate', reason: null, mapReady: false, createdAt: '2026-10-08T18:00:00Z', updatedAt: '2026-10-08T18:00:00Z' });
  assert.ok(client.parsePublicMapStatus(v));
  for (const patch of [{ mapReady: true }, { sha256: null }, { bytes: 201 }, { expectedBytes: 101 }]) assert.equal(client.parsePublicMapStatus({ ...v, jobs: [{ ...v.jobs[0], ...patch }] }), null);
  assert.equal(client.parsePublicMapStatus({ ...v, active: 'f'.repeat(32) }), null);
});
test('public-map client uses only existing loopback worker routes and refuses caller-controlled destinations', async () => {
  const previous = globalThis.fetch, calls = [];
  globalThis.fetch = async (url, options) => { calls.push({ url, options }); return Response.json(status()); };
  try {
    await client.publicMapRequest('/downloads', new AbortController().signal, { assetId: 'test' }, 'a'.repeat(43));
    assert.equal(calls[0].url, 'http://127.0.0.1:8769/public-maps/downloads');
    assert.equal(calls[0].options.redirect, 'error'); assert.equal(calls[0].options.credentials, 'omit'); assert.equal(calls[0].options.headers['X-KFM-Session'], 'a'.repeat(43));
    await assert.rejects(client.publicMapRequest('https://elsewhere.example/', new AbortController().signal));
    await assert.rejects(client.publicMapRequest('/downloads', new AbortController().signal, {}, 'bad-token'));
    const aborted = new AbortController(); aborted.abort(); await assert.rejects(client.publicMapRequest('/status', aborted.signal));
    assert.equal(calls.length, 1);
  } finally { globalThis.fetch = previous; }
});
test('response bodies share the deadline and byte bound; oversized or stalled bodies do not parse', async () => {
  const previous = globalThis.fetch;
  try {
    globalThis.fetch = async () => new Response('x'.repeat(256_001));
    await assert.rejects(client.publicMapRequest('/status', new AbortController().signal));
    const controller = new AbortController();
    globalThis.fetch = async () => new Response(new ReadableStream({ start() {} }));
    const waiting = client.publicMapRequest('/status', controller.signal); controller.abort(); await assert.rejects(waiting);
  } finally { globalThis.fetch = previous; }
});
