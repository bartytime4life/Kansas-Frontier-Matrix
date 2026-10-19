import test from 'node:test';
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { probeNodeStartup, reportNodeStartup, reportPublicDelivery } from '../server/startup-probe.mjs';
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


test('transport diagnostics distinguish refused and reset connections without raw errors', async t => {
  const closed = await listening(t, () => {});
  const address = closed.address();
  await new Promise(resolve => closed.close(resolve));
  const refused = await probeNodeStartup({ address: () => address });
  assert.equal(refused.outcome, 'UNREACHABLE');
  assert.equal(refused.errorCode, 'ECONNREFUSED');
  assert.equal(refused.transportStage, 'CONNECTING');
  const reset = await listening(t, request => request.socket.destroy());
  const result = await probeNodeStartup(reset);
  assert.equal(result.outcome, 'UNREACHABLE');
  assert.equal(result.errorCode, 'ECONNRESET');
  assert.equal(result.transportStage, 'CONNECTED');
  assert.doesNotMatch(JSON.stringify(result), /127\.0\.0\.1|socket hang up/);
});

test('public delivery observes one real request/response and removes its listeners', async t => {
  const server = await listening(t, (_request, response) => {
    response.writeHead(200, { 'Content-Type': 'application/json' });
    response.end(JSON.stringify(identity));
  });
  const before = { request: server.listenerCount('request'), close: server.listenerCount('close') };
  const lines = [];
  const delivery = reportPublicDelivery(server, { write: line => lines.push(line) });
  await probeNodeStartup(server);
  assert.deepEqual(lines, [], 'the marked loopback check does not count as gateway delivery');
  await fetch('http://127.0.0.1:' + server.address().port + '/api/build', {
    headers: { Cookie: 'NEVER_LOG_COOKIE', Authorization: 'Bearer NEVER_LOG_TOKEN' },
  });
  const result = await delivery;
  assert.deepEqual(result, { profile: 'kfm.node-delivery/v1', outcome: 'RESPONSE_FINISHED', route: 'BUILD', httpStatus: 200 });
  assert.equal(lines.length, 2);
  assert.doesNotMatch(lines.join(''), /NEVER_LOG|Cookie|Authorization|127\.0\.0\.1|sourceDigest/);
  assert.equal(server.listenerCount('request'), before.request);
  assert.equal(server.listenerCount('close'), before.close);
  await fetch('http://127.0.0.1:' + server.address().port + '/');
  assert.equal(lines.length, 2, 'later requests do not produce diagnostic traffic logs');
});

test('delivery ignores private paths and query text, and expires without retaining listeners', async t => {
  const server = await listening(t, (_request, response) => response.end('NEVER_LOG_BODY'));
  const before = server.listenerCount('request');
  const lines = [];
  const delivery = reportPublicDelivery(server, { timeoutMs: 100, write: line => lines.push(line) });
  for (const path of ['/api/private/NEVER_LOG_PATH', '/?NEVER_LOG_QUERY', '/api/build?NEVER_LOG_QUERY']) {
    await fetch('http://127.0.0.1:' + server.address().port + path);
  }
  assert.equal((await delivery).outcome, 'NO_PUBLIC_REQUEST_OBSERVED');
  assert.equal(server.listenerCount('request'), before);
  assert.equal(lines.length, 1);
  assert.doesNotMatch(lines[0], /NEVER_LOG/);
});

test('delivery distinguishes a received request whose response stalls or closes', async t => {
  for (const close of [false, true]) {
    const server = await listening(t, (request, response) => {
      if (close) request.socket.destroy();
      else { response.writeHead(200); response.write('NEVER_LOG_BODY'); }
    });
    const lines = [];
    const delivery = reportPublicDelivery(server, { timeoutMs: 50, write: line => lines.push(line) });
    const controller = new AbortController();
    const response = fetch('http://127.0.0.1:' + server.address().port + '/', { signal: controller.signal }).catch(() => null);
    const result = await delivery;
    controller.abort(); await response;
    assert.equal(result.outcome, close ? 'RESPONSE_CLOSED' : 'RESPONSE_TIMEOUT');
    assert.equal(result.route, 'ROOT');
    assert.equal(lines.length, 2);
    assert.doesNotMatch(lines.join(''), /NEVER_LOG/);
  }
});


test('unknown parser errors are reduced to a fixed code without response details', async t => {
  const server = await listening(t, (_request, response) => {
    response.socket.end('HTTP/1.1 200 OK\r\nNEVER_LOG_PRIVATE_HEADER:\x00\r\n\r\n');
  });
  const lines = [];
  const result = await reportNodeStartup(server, line => lines.push(line));
  assert.equal(result.outcome, 'UNREACHABLE');
  assert.equal(result.errorCode, 'OTHER_ERROR');
  assert.doesNotMatch(lines.join(''), /NEVER_LOG|Parse Error|rawPacket|stack/);
});
