import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { stripTypeScriptTypes } from 'node:module';
import { probeContextConnections } from '../scripts/probe-context-connections.mjs';
const source = await readFile(new URL('../worker/index.ts', import.meta.url), 'utf8');
const { default: worker } = await import(`data:text/javascript;base64,${Buffer.from(stripTypeScriptTypes(source)).toString('base64')}`);
const origin = 'http://127.0.0.1:5173';
const context = { waitUntil() {}, passThroughOnException() {} };
const serve = (path, assets, method = 'GET') => worker.fetch(new Request(`${origin}${path}`, { method }), { ASSETS: { fetch: assets } }, context);

for (const path of ['/api', '/api/live-context?feed=usgs-earthquakes', '/api/terrain-tile?kind=slope&z=8&x=58&y=98',
  '/%61pi/live-context', '//api/live-context', '/API/live-context']) {
  test(`API path is unavailable JSON, never an HTML app shell: ${path}`, async () => {
    let assetCalls = 0;
    const r = await serve(path, async () => { assetCalls++; return new Response('<html>shell</html>', { headers: { 'content-type': 'text/html' } }); });
    assert.equal(r.status, 503); assert.equal(assetCalls, 0);
    assert.match(r.headers.get('content-type'), /application\/json/); assert.equal(r.headers.get('cache-control'), 'no-store');
    assert.equal(r.headers.get('x-content-type-options'), 'nosniff');
    const body = await r.json(); assert.equal(body.code, 'KFM_API_NOT_CONFIGURED'); assert.equal(body.state, 'unavailable');
  });
}
test('API HEAD returns no body and unsupported method cannot submit data', async () => {
  const forbidden = async () => { throw Error('assets must not be called'); };
  assert.equal(await (await serve('/api/live-context', forbidden, 'HEAD')).text(), '');
  assert.equal((await serve('/api/live-context', forbidden, 'POST')).status, 503);
});
test('invalid encoded path is a finite error, not an unhandled decode exception', async () => {
  const r = await serve('/%zz', async () => { throw Error('must not fetch'); });
  assert.equal(r.status, 400); assert.equal((await r.json()).code, 'KFM_INVALID_PATH');
});
test('error body does not echo supplied URLs or query values', async () => {
  const r = await serve('/api/live-context?token=PRIVATE_VALUE', async () => { throw Error('must not fetch'); });
  assert.doesNotMatch(await r.text(), /PRIVATE_VALUE|token|127\.0\.0\.1/);
});
test('ordinary extensionless route retains SPA fallback', async () => {
  const calls = [];
  const r = await serve('/about', async (request) => {
    const path = new URL(request.url).pathname; calls.push(path);
    return path === '/index.html' ? new Response('<html>shell</html>') : new Response(null, { status: 404 });
  });
  assert.equal(r.status, 200); assert.deepEqual(calls, ['/about', '/index.html']);
});
test('API-like non-API route remains a page', async () => {
  const r = await serve('/apiary', async () => new Response('page'));
  assert.equal(r.status, 200); assert.equal(await r.text(), 'page');
});
test('real assets, dotted missing assets, and non-GET page requests retain behavior', async () => {
  assert.equal(await (await serve('/assets/site.js', async () => new Response('script'))).text(), 'script');
  for (const [path, method] of [['/missing.js', 'GET'], ['/about', 'POST']]) {
    let calls = 0;
    const r = await serve(path, async () => { calls++; return new Response(null, { status: 404 }); }, method);
    assert.equal(r.status, 404); assert.equal(calls, 1);
  }
});
test('actual Worker-to-probe integration reports unconfigured APIs for every adapter route', async () => {
  const report = await probeContextConnections({ origin, fetchImpl: (url, options) => worker.fetch(
    new Request(url, options), { ASSETS: { fetch: async () => new Response('<html>shell</html>') } }, context) });
  assert.equal(report.results.filter((x) => x.status === 'API_NOT_CONFIGURED').length, 10);
  assert.equal(report.results.filter((x) => x.status === 'NOT_PROBED_RENDERER').length, 5);
  assert.ok(report.results.every((x) => !x.rendered && !x.payloadValidated && !x.freshnessVerified));
});

test('real Worker failure to probe to starter decision preserves error and synthetic provenance', async () => {
  const moduleText = await readFile(new URL('../app/feed-startup.ts', import.meta.url), 'utf8');
  const { resolveFeedStartup } = await import(`data:text/javascript;base64,${Buffer.from(stripTypeScriptTypes(moduleText)).toString('base64')}`);
  const bytes = await readFile(new URL('../fixtures/feed-startup.synthetic.json', import.meta.url));
  const fixture = JSON.parse(bytes);
  const report = await probeContextConnections({ origin, fetchImpl: (url, options) => worker.fetch(
    new Request(url, options), { ASSETS: { fetch: async () => new Response('shell') } }, context) });
  const quake = report.results.find((row) => row.id === 'usgs-earthquakes');
  const r = resolveFeedStartup({ now: '2026-09-22T12:00:00.000Z', sourceId: quake.id, scopeKey: 'ks:quakes:30d',
    direction: 'auto', enabled: true, access: 'allowed', timeSupported: true, zoomSupported: true,
    phase: 'error', failureCode: quake.status,
    demo: { id: fixture.properties.artifactId, sourceId: fixture.properties.sourceId, scopeKey: fixture.properties.scopeKey,
      kind: 'synthetic', dataRole: 'synthetic', sha256: createHash('sha256').update(bytes).digest('hex'), validation: 'passed', displayAllowed: true,
      dataTime: fixture.properties.dataTime, retrievedAt: null, freshnessAnchor: null, validUntil: null, featureCount: fixture.features.length } });
  assert.equal(r.display, 'SYNTHETIC_DEMO'); assert.equal(r.connectionFailure, 'API_NOT_CONFIGURED');
  assert.equal(r.liveAvailable, false); assert.equal(r.renderedLive, false);
});
