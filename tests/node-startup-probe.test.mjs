import test from 'node:test';
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { probeNodeStartup, reportNodeStartup } from '../server/startup-probe.mjs';
import { BUILD_PROFILE, BUILD_APPLICATION } from '../scripts/build-identity.mjs';

const identity = { profile: BUILD_PROFILE, application: BUILD_APPLICATION,
  sourceDigest: 'sha256:' + 'a'.repeat(64), sourceFileCount: 773 };
async function listening(t, handler) {
  const server = createServer(handler);
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  t.after(() => new Promise(resolve => { server.closeAllConnections(); server.close(resolve); }));
  return server;
}

test('startup checks the actual assigned port and existing build route without cookies or credentials', async t => {
  let requests = 0;
  const server = await listening(t, (request, response) => {
    requests++;
    assert.equal(request.method, 'GET'); assert.equal(request.url, '/api/build');
    assert.equal(request.headers.cookie, undefined); assert.equal(request.headers.authorization, undefined);
    response.writeHead(200, { 'Content-Type': 'application/json' });
    response.end(JSON.stringify({ ...identity, privateValue: 'NEVER_LOG_THIS' }));
  });
  const lines = [];
  const result = await reportNodeStartup(server, line => lines.push(line));
  assert.equal(requests, 1); assert.equal(result.outcome, 'LOOPBACK_BUILD_READY');
  assert.equal(result.listenPort, server.address().port); assert.equal(result.httpStatus, 200);
  assert.equal(result.sourceDigest, identity.sourceDigest); assert.equal(lines.length, 1);
  assert.doesNotMatch(lines[0], /NEVER_LOG_THIS|privateValue/);
});

test('HTTP failures and redirects are reported without following a different destination', async t => {
  for (const status of [302, 503]) {
    const server = await listening(t, (_request, response) => {
      response.writeHead(status, { Location: 'https://example.invalid/never-follow' }); response.end('private error text');
    });
    const result = await probeNodeStartup(server);
    assert.equal(result.outcome, 'HTTP_ERROR'); assert.equal(result.httpStatus, status);
    assert.doesNotMatch(JSON.stringify(result), /private error text|example.invalid/);
  }
});

test('a 200 placeholder, malformed JSON and another application are not readiness', async t => {
  for (const [type, body] of [
    ['text/html', '<h1>Coming Soon!</h1>'], ['application/json', '{'],
    ['application/json', JSON.stringify({ ...identity, application: 'different-app' })],
  ]) {
    const server = await listening(t, (_request, response) => { response.writeHead(200, { 'Content-Type': type }); response.end(body); });
    assert.equal((await probeNodeStartup(server)).outcome, 'INVALID_IDENTITY');
  }
});

test('oversized and stalled bodies cannot hold or inflate startup diagnostics', async t => {
  const oversized = await listening(t, (_request, response) => {
    response.writeHead(200, { 'Content-Type': 'application/json' }); response.end('x'.repeat(4097));
  });
  assert.equal((await probeNodeStartup(oversized)).outcome, 'RESPONSE_TOO_LARGE');
  const stalled = await listening(t, (_request, response) => {
    response.writeHead(200, { 'Content-Type': 'application/json' }); response.write('{');
  });
  assert.equal((await probeNodeStartup(stalled, { timeoutMs: 50 })).outcome, 'TIMEOUT');
});

test('an unbound server is reported without inventing a listening port', async () => {
  const result = await probeNodeStartup(createServer());
  assert.equal(result.outcome, 'NOT_LISTENING'); assert.equal(result.listenPort, null);
});
