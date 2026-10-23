import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, readFile, lstat, mkdir, symlink, readdir, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync, spawnSync } from 'node:child_process';
import { createServer } from 'node:http';
import { gzipSync } from 'node:zlib';
import { cli } from '../scripts/pc-pipeline/cli.mjs';
import { connectionCheck, CONNECTION_ENDPOINT } from '../scripts/pc-pipeline/connection.mjs';
import { createDatabaseCheck } from '../server/database-connection.mjs';

const success = { format: 'kfm-database-connection-v1', mode: 'connection-only', checkedAt: '2026-10-23T17:00:00.000Z',
  cacheSeconds: 60, uploadsEnabled: false, sqlWritesEnabled: false, connected: true, state: 'connected', transport: 'verified-tls' };
const unavailable = (reason, extra = {}) => ({ ...success, connected: false, state: 'unavailable', transport: undefined, reason, ...extra });
const response = (value = success, status = 200) => Response.json(value, { status });
async function privateRoot(t) {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-connection-'));
  t.after(() => rm(root, { recursive: true, force: true }));
  return root;
}

test('existing CLI makes exactly one fixed HTTPS GET and writes a private immutable receipt', async t => {
  const root = await privateRoot(t);
  let calls = 0;
  const result = await cli(['connection', root], { fetcher: async (url, options) => {
    calls++;
    assert.equal(url, CONNECTION_ENDPOINT);
    assert.deepEqual(Object.keys(options).sort(), ['cache', 'credentials', 'headers', 'method', 'redirect', 'signal']);
    assert.equal(options.method, 'GET'); assert.equal(options.redirect, 'manual');
    assert.equal(options.credentials, 'omit'); assert.equal(options.cache, 'no-store');
    assert.deepEqual(options.headers, { Accept: 'application/json' });
    assert.equal(options.body, undefined);
    return response();
  } });
  assert.equal(calls, 1); assert.equal(result.state, 'connected');
  assert.equal(result.serverCheckedAt, success.checkedAt);
  const { receiptPath, ...receipt } = result;
  assert.deepEqual(JSON.parse(await readFile(receiptPath, 'utf8')), receipt);
  assert.equal((await lstat(receiptPath)).mode & 0o777, 0o600);
  assert.equal((await lstat(dirname(receiptPath))).mode & 0o777, 0o700);
  assert.match(receiptPath, /data\/receipts\/pipeline\/connection\/[a-f0-9]{64}\.json$/);
  assert.equal(result.sqlWritesEnabled, false); assert.equal(result.uploadsEnabled, false);
  assert.deepEqual(await readdir(root), ['data']);
});

test('server configuration and TLS failure responses produce explicit private receipts', async t => {
  const root = await privateRoot(t);
  const missing = createDatabaseCheck({ environment: () => ({}), connect: () => assert.fail('no SQL connection') });
  const cases = [await missing(), unavailable('verified-tls-unavailable', { tlsFailure: 'certificate-hostname-mismatch' }),
    unavailable('authentication-failed'), unavailable('connection-unavailable'), unavailable('private-provider-network-required')];
  for (const value of cases) {
    const result = await cli(['connection', root], { fetcher: async () => response(value, 503) });
    assert.equal(result.reason, value.reason); assert.equal(result.connected, false); assert.equal(result.httpStatus, 503);
    assert.equal(result.tlsFailure, value.tlsFailure);
    assert.equal(JSON.parse(await readFile(result.receiptPath)).reason, value.reason);
  }
});

test('inaccessible hosting and certificate failures stay coarse and do not expose credentials', async t => {
  const root = await privateRoot(t);
  const secret = 'SYNTHETIC-password-db-user-host';
  const result = await cli(['connection', root], { fetcher: async () => { throw new Error(secret); } });
  assert.equal(result.reason, 'hosting-unreachable'); assert.equal(result.httpStatus, null);
  assert.doesNotMatch(JSON.stringify(result) + await readFile(result.receiptPath, 'utf8'), new RegExp(secret));
});

test('invalid status, redirect, content type, JSON, schema, flags and timestamps cannot pass', async () => {
  const invalid = [
    () => response(success, 503), () => response(unavailable('configuration-missing'), 200),
    () => new Response(null, { status: 302, headers: { Location: 'https://other.example.test/?secret=synthetic' } }),
    () => new Response('<html>login</html>', { status: 200 }),
    () => new Response('{', { headers: { 'content-type': 'application/json' } }),
    () => response({ ...success, sqlWritesEnabled: true }), () => response({ ...success, uploadsEnabled: true }),
    () => response({ ...success, password: 'synthetic-secret' }), () => response({ ...success, checkedAt: 'yesterday' }),
    () => response({ ...success, cacheSeconds: 0 }), () => response({ ...success, transport: 'unknown' }),
    () => response({ ...success, reason: 'synthetic-secret' }), () => response(null), () => response([]),
    () => response(unavailable('synthetic-secret'), 503),
    () => response(unavailable('verified-tls-unavailable', { tlsFailure: 'synthetic-secret' }), 503),
    () => new Response(new Uint8Array([255]), { headers: { 'content-type': 'application/json' } }),
  ];
  for (const fetcher of invalid) {
    const result = await connectionCheck({ fetcher });
    assert.equal(result.reason, 'invalid-response'); assert.equal(result.connected, false);
    assert.doesNotMatch(JSON.stringify(result), /synthetic-secret|other.example|login/);
  }
});

test('response budget bounds declared and streamed data and cancels the body', async () => {
  let cancelled = 0;
  for (const headers of [{ 'content-length': '8193' }, { 'content-length': 'bad' }, { 'content-length': '1' }, {}]) {
    const result = await connectionCheck({ fetcher: async () => new Response(new ReadableStream({
      pull(controller) { controller.enqueue(new Uint8Array(8193)); }, cancel() { cancelled++; },
    }), { headers: { 'content-type': 'application/json', ...headers } }) });
    assert.equal(result.reason, 'invalid-response');
  }
  assert.equal(cancelled, 4);
});

test('valid compressed endpoint responses survive native fetch decompression without losing the decoded cap', async t => {
  const compressed = gzipSync(JSON.stringify(success));
  const server = createServer((request, reply) => {
    assert.equal(request.method, 'GET');
    reply.writeHead(200, { 'content-type': 'application/json', 'content-encoding': 'gzip', 'content-length': compressed.length });
    reply.end(compressed);
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  t.after(() => new Promise(resolve => server.close(resolve)));
  const result = await connectionCheck({ fetcher: async (_, options) => {
    const decoded = await fetch(`http://127.0.0.1:${server.address().port}`, options);
    // Keep the production URL pinned; only the synthetic transport uses loopback.
    return new Response(decoded.body, { status: decoded.status, headers: decoded.headers });
  } });
  assert.equal(result.state, 'connected');
  const oversized = await connectionCheck({ fetcher: async () => new Response(' '.repeat(8193), {
    headers: { 'content-type': 'application/json', 'content-encoding': 'gzip', 'content-length': '100' },
  }) });
  assert.equal(oversized.reason, 'invalid-response');
});

test('one deadline covers a stalled request and a stalled body, saves receipts and aborts without retry', async t => {
  const root = await privateRoot(t);
  for (const stalledBody of [false, true]) {
    let signal, calls = 0;
    const result = await cli(['connection', root], { timeoutMs: 20, fetcher: async (_, options) => {
      calls++; signal = options.signal;
      return stalledBody ? new Response(new ReadableStream({ start() {} }), { headers: { 'content-type': 'application/json' } }) : new Promise(() => {});
    } });
    assert.equal(result.reason, 'request-timeout'); assert.equal(signal.aborted, true); assert.equal(calls, 1);
    assert.equal(JSON.parse(await readFile(result.receiptPath)).reason, 'request-timeout');
  }
});

test('provider-private and loopback SQL connectivity cannot satisfy verified TLS acceptance', async () => {
  for (const transport of ['host-loopback', 'provider-private-network']) {
    const result = await connectionCheck({ fetcher: async () => response({ ...success, transport }) });
    assert.equal(result.connected, true); assert.equal(result.transport, transport);
    assert.equal(result.state, 'held'); assert.equal(result.reason, 'verified-tls-required');
  }
});

test('an ambient HTTPS certificate-verification bypass is held before any request', async () => {
  const result = await connectionCheck({ environment: { NODE_TLS_REJECT_UNAUTHORIZED: '0' }, fetcher: () => assert.fail('TLS verification required') });
  assert.equal(result.state, 'held'); assert.equal(result.reason, 'tls-verification-disabled'); assert.equal(result.httpStatus, null);
});

test('unsafe roots, unexpected arguments and receipt-write errors fail explicitly without fetching local data', async t => {
  const root = await privateRoot(t);
  const options = { fetcher: () => assert.fail('no request for invalid invocation') };
  await assert.rejects(cli(['connection', root, 'synthetic-password'], options), /CONNECTION_USAGE_INVALID/);
  await assert.rejects(cli(['connection', '--insecure'], options), /CONNECTION_USAGE_INVALID/);
  await assert.rejects(cli(['connection', '.'], options), /ABSOLUTE_ROOT_REQUIRED/);
  await assert.rejects(cli(['connection', resolve('outputs')], options), /DATA_ROOT_MUST_BE_OUTSIDE_CHECKOUT/);
  const publicRoot = resolve(root, 'public'); await mkdir(publicRoot, { mode: 0o755 });
  await assert.rejects(cli(['connection', publicRoot], options), /PRIVATE_ROOT_REQUIRED/);
  const linked = resolve(root, 'linked'); await symlink(publicRoot, linked);
  await assert.rejects(cli(['connection', linked], options), /DIRECTORY_UNSAFE/);
  await symlink(publicRoot, resolve(root, 'data'));
  await assert.rejects(cli(['connection', root], { fetcher: async () => response() }), /CONNECTION_RECEIPT_WRITE_FAILED/);
});

test('real CLI process and npm entry return zero only for verified connectivity; no ambient DB secrets sent or printed', async t => {
  const root = await privateRoot(t);
  const checkout = fileURLToPath(new URL('..', import.meta.url));
  const packageJson = JSON.parse(await readFile(resolve(checkout, 'package.json')));
  assert.equal(packageJson.scripts['kfm-data'], 'node scripts/pc-pipeline/cli.mjs');
  for (const [value, status, exit] of [[success, 200, 0], [unavailable('configuration-missing'), 503, 1],
    [{ ...success, transport: 'provider-private-network' }, 200, 1]]) {
    const preload = 'data:text/javascript,' + encodeURIComponent(`globalThis.fetch = async (url, opts) => {
      if (url !== ${JSON.stringify(CONNECTION_ENDPOINT)} || opts.body || Object.keys(opts.headers).length !== 1) throw new Error('credential leak');
      return Response.json(${JSON.stringify(value)}, {status:${status}});
    };`);
    const result = spawnSync(process.execPath, ['--import', preload, resolve(checkout, 'scripts/pc-pipeline/cli.mjs'), 'connection', root], {
      cwd: checkout, encoding: 'utf8', timeout: 5000,
      env: { ...process.env, DB_PASSWORD: 'synthetic-ambient-secret', CREDENTIALS_DIRECTORY: '/nonexistent-synthetic-credentials' },
    });
    assert.equal(result.status, exit, result.stderr);
    const parsed = JSON.parse(result.stdout);
    assert.equal(parsed.connected, value.connected);
    assert.doesNotMatch(result.stdout + result.stderr + await readFile(parsed.receiptPath), /synthetic-ambient-secret|nonexistent-synthetic-credentials/);
  }
  const usage = execFileSync('npm', ['run', '--silent', 'kfm-data', '--', 'inventory'], { cwd: checkout, encoding: 'utf8' });
  assert.equal(JSON.parse(usage).format, 'kfm-pipeline-inventory-v1');
});
