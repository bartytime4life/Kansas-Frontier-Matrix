import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { startProdServer } from 'vinext/server/prod-server';
import { installPublicDelivery } from '../server/browser-headers.mjs';
import { applicationIdentity, verifyHostedIdentity } from '../scripts/build-identity.mjs';

test('built public identity matches current inputs and About exposes usable project resources', async t => {
  const {server, port} = await startProdServer({port:0, host:'127.0.0.1', outDir:'dist'});
  installPublicDelivery(server);
  t.after(() => new Promise(resolve => { server.closeAllConnections(); server.close(resolve); }));
  const origin = `http://127.0.0.1:${port}`;
  const response = await fetch(origin + '/api/build');
  assert.equal(response.status, 200); assert.equal(response.headers.get('cache-control'), 'no-store');
  const actual = await response.json();
  assert.deepEqual(Object.keys(actual).sort(), ['application', 'commitState', 'profile', 'scope', 'sourceCommit', 'sourceDigest', 'sourceFileCount'].sort());
  const expected = await applicationIdentity();
  assert.equal((await verifyHostedIdentity(expected, origin)).outcome, 'APPLICATION_INPUTS_MATCH');
  const about = await (await fetch(origin + '/about')).text();
  for (const id of ['about-main', 'workflow', 'capabilities', 'project', 'sources']) {
    assert.ok(about.includes(`id="${id}"`), id);
    assert.ok(about.includes(`href="#${id}"`), 'keyboard/jump target '+id);
  }
  assert.ok(about.includes(actual.sourceDigest));
  assert.ok(about.includes('href="/api/build"'));
  assert.ok(about.includes('docs/runbooks/godaddy-hosting.md'));
  assert.ok(about.includes('Historical repository and Sites snapshots'));
  assert.ok(!about.includes('Canonical host:'));
  assert.ok(!about.includes('no inference endpoint is configured by default'));
  assert.ok(about.includes('responses can be incomplete or withheld'));
});

// Exercise both delivery paths: the production server and the provider's durable
// public asset directory must carry the exact emitted browser modules.
test('production browser modules match both emitted and staged bytes', async t => {
  const {server, port} = await startProdServer({port:0, host:'127.0.0.1', outDir:'dist'});
  installPublicDelivery(server);
  t.after(() => new Promise(resolve => { server.closeAllConnections(); server.close(resolve); }));
  const origin = `http://127.0.0.1:${port}`;
  const home = await (await fetch(origin)).text();
  const paths = [...new Set([...home.matchAll(/<link\b[^>]*>/g)]
    .filter(match => /rel="modulepreload"/.test(match[0]))
    .map(match => /href="([^\"]+)"/.exec(match[0])?.[1]).filter(Boolean))];
  assert.ok(paths.length > 0);
  const hash = bytes => createHash('sha256').update(bytes).digest('hex');
  for (const path of paths) {
    assert.match(path, /^\/assets\/[A-Za-z0-9_.-]+\.js$/);
    const response = await fetch(origin + path);
    assert.equal(response.status, 200, path);
    assert.match(response.headers.get('content-type'), /javascript/);
    const expected = hash(await readFile('dist/client' + path));
    assert.equal(hash(Buffer.from(await response.arrayBuffer())), expected, path);
    assert.equal(hash(await readFile('public' + path)), expected, 'staged ' + path);
  }
});
