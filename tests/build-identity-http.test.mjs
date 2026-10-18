import test from 'node:test';
import assert from 'node:assert/strict';
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
  assert.equal(actual.sourceCommit, expected.sourceCommit);
  assert.equal(actual.commitState, expected.commitState);
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

