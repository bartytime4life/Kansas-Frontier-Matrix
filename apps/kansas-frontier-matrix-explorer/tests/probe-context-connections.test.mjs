import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { CONNECTIONS, validateOrigin, probeContextConnections } from '../scripts/probe-context-connections.mjs';
const origin = 'http://127.0.0.1:5173';
const png = () => {
  const b = new Uint8Array(33), v = new DataView(b.buffer);
  b.set([137, 80, 78, 71, 13, 10, 26, 10]);
  v.setUint32(8, 13); v.setUint32(12, 0x49484452); v.setUint32(16, 256); v.setUint32(20, 256);
  return new Response(b, { headers: { 'content-type': 'image/png' } });
};
const ok = (url) => url.includes('/api/terrain-tile?') ? png() : Response.json({ notValidated: true });
const run = (fetchImpl, extras = {}) => probeContextConnections({ origin, fetchImpl, ...extras });
const networkRows = (r) => r.results.filter((x) => x.path !== null);

test('inventory has 15 unique logical layers but only 10 same-origin probes', () => {
  assert.equal(CONNECTIONS.length, 15); assert.equal(new Set(CONNECTIONS.map((c) => c.id)).size, 15);
  assert.equal(CONNECTIONS.filter((c) => c.path).length, 10);
  for (const c of CONNECTIONS) if (c.path) assert.ok(c.path.startsWith('/api/'));
});
test('import and invocation without CLI origin do not contact any source', () => {
  const moduleUrl = new URL('../scripts/probe-context-connections.mjs', import.meta.url).href;
  const imported = spawnSync(
    process.execPath,
    ['--input-type=module', '-e', "globalThis.fetch=()=>{throw Error('unexpected fetch')}; await import(process.env.PROBE_MODULE_URL);"],
    { env: { ...process.env, PROBE_MODULE_URL: moduleUrl } }
  );
  assert.equal(imported.status, 0);
  const cli = spawnSync(process.execPath, [fileURLToPath(moduleUrl)]);
  assert.equal(cli.status, 2); assert.match(cli.stderr.toString(), /Usage:/);
});
for (const value of ['https://example.com', 'http://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site',
  'https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site:8443',
  'http://localhost:5173/path', 'http://user:secret@localhost:5173', 'http://localhost:5173/?token=secret',
  'http://localhost:5173/#fragment', 'file:///etc/passwd', 'http://192.168.0.1']) {
  test(`origin is rejected before any network request: ${value.replace('secret', 'REDACTED')}`, async () => {
    let calls = 0;
    await assert.rejects(probeContextConnections({ origin: value, fetchImpl: () => { calls++; } }));
    assert.equal(calls, 0);
  });
}
test('only explicit official origin and loopback origins are accepted', () => {
  assert.equal(validateOrigin(origin), origin);
  assert.equal(validateOrigin('http://localhost:5173/'), 'http://localhost:5173');
  assert.equal(validateOrigin('http://[::1]:5173'), 'http://[::1]:5173');
  assert.equal(validateOrigin('https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site'),
    'https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site');
});
test('JSON and PNG delivery never claim payload validation, freshness, rendering or acceptance', async () => {
  const r = await run(async (url, options) => {
    assert.equal(options.method, 'GET'); assert.equal(options.redirect, 'manual');
    assert.equal(options.credentials, 'same-origin'); assert.equal(options.cache, 'no-store');
    return ok(url);
  });
  assert.equal(r.results.filter((x) => x.status === 'JSON_RECEIVED_SCHEMA_UNVERIFIED').length, 8);
  assert.equal(r.results.filter((x) => x.status === 'PNG_HEADER_ONLY_RENDER_UNPROVED').length, 2);
  assert.equal(r.results.filter((x) => x.status === 'NOT_PROBED_RENDERER').length, 5);
  for (const row of r.results) assert.equal(row.payloadValidated || row.freshnessVerified || row.rendered, false);
  assert.equal(r.activeSiteParity, 'UNVERIFIED'); assert.equal(r.operationalAcceptance, 'NOT_ESTABLISHED');
});
for (const [status, expected] of [[302, 'REDIRECT_OR_AUTH_UNVERIFIED'], [401, 'AUTH_REQUIRED'], [403, 'AUTH_REQUIRED'],
  [404, 'ROUTE_MISSING'], [429, 'RATE_LIMITED'], [502, 'UPSTREAM_OR_ADAPTER_ERROR'],
  [204, 'EMPTY_HTTP_RESPONSE_UNVALIDATED'], [400, 'HTTP_ERROR']]) {
  test(`HTTP ${status} has a finite classification, not a healthy feed`, async () => {
    const r = await run(async () => new Response(null, { status }));
    assert.ok(networkRows(r).every((row) => row.status === expected));
  });
}
test('an HTML sign-in or SPA fallback returned as HTTP 200 is not a working API', async () => {
  const r = await run(async () => new Response('<html>Sign in</html>', { headers: { 'content-type': 'text/html' } }));
  assert.ok(networkRows(r).every((row) => row.status === 'UNEXPECTED_MEDIA_TYPE'));
});
test('malformed JSON and invalid UTF-8 fail without leaking payloads', async () => {
  for (const body of ['{"password":"DO_NOT_LOG",', new Uint8Array([0xff])]) {
    const r = await run(async (url) => url.includes('terrain-tile') ? png() : new Response(body, { headers: { 'content-type': 'application/json' } }));
    assert.equal(r.results[0].status, 'INVALID_JSON_OR_UTF8'); assert.doesNotMatch(JSON.stringify(r), /DO_NOT_LOG|password/);
  }
});
test('declared or streamed oversized bodies are bounded', async () => {
  for (const declared of [true, false]) {
    const r = await run(async (url) => url.includes('feed=census-counties')
      ? new Response(declared ? '{}' : new Uint8Array(4 * 1024 * 1024 + 1), {
        headers: { 'content-type': 'application/json', ...(declared ? { 'content-length': '4194305' } : {}) } }) : ok(url));
    assert.equal(r.results[0].status, 'BODY_LIMIT');
    assert.equal(r.results[1].status, 'JSON_RECEIVED_SCHEMA_UNVERIFIED');
  }
});
test('PNG dimensions and signature are inspected but header success is not image decode proof', async () => {
  const r = await run(async (url) => url.includes('terrain-tile')
    ? new Response(new Uint8Array(33), { headers: { 'content-type': 'image/png' } }) : ok(url));
  assert.equal(r.results[11].status, 'INVALID_PNG_HEADER');
});
test('requests that never resolve settle as individual timeouts', async () => {
  const r = await run(() => new Promise(() => {}), { timeoutMs: 10 });
  assert.ok(networkRows(r).every((row) => row.status === 'TIMEOUT'));
});
test('timeout also covers body streaming and cancels a stalled reader', async () => {
  let cancelled = 0;
  const r = await run(async (url) => url.includes('feed=census-counties')
    ? new Response(new ReadableStream({ cancel() { cancelled++; } }), { headers: { 'content-type': 'application/json' } }) : ok(url), { timeoutMs: 10 });
  assert.equal(r.results[0].status, 'TIMEOUT'); assert.equal(cancelled, 1);
  assert.equal(r.results[1].status, 'JSON_RECEIVED_SCHEMA_UNVERIFIED');
});
test('one failure is isolated and raw exception text is never included', async () => {
  const r = await run(async (url) => {
    if (url.includes('feed=census-counties')) throw new Error('SECRET_COOKIE https://private.invalid');
    return ok(url);
  });
  assert.equal(r.results[0].status, 'NETWORK_OR_STREAM_ERROR');
  assert.equal(r.results[1].status, 'JSON_RECEIVED_SCHEMA_UNVERIFIED');
  assert.doesNotMatch(JSON.stringify(r), /SECRET_COOKIE|private.invalid/);
});
test('at most two requests run concurrently and results preserve manifest order', async () => {
  let active = 0, maximum = 0, calls = 0;
  const r = await run(async (url) => {
    active++; calls++; maximum = Math.max(maximum, active);
    await new Promise((resolve) => setTimeout(resolve, 2)); active--;
    return ok(url);
  });
  assert.equal(maximum, 2); assert.equal(calls, 10);
  assert.deepEqual(r.results.map((row) => row.id), CONNECTIONS.map((c) => c.id));
});
test('invalid bounds are refused without fetching', async () => {
  for (const timeoutMs of [0, 9, 15001, NaN, 11.5]) {
    await assert.rejects(run(() => { throw Error('unexpected fetch'); }, { timeoutMs }));
  }
});
