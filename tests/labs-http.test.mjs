import test from 'node:test';
import assert from 'node:assert/strict';
import { request } from 'node:http';
import { startProdServer } from 'vinext/server/prod-server';
import { installPublicDelivery } from '../server/browser-headers.mjs';
import { DATASETS, PENDING_DATASETS } from '../scripts/local-data/datasets.mjs';
import { PUBLIC_LAB_SNAPSHOTS } from '../app/labs/public-snapshots.mjs';
import { createHash } from 'node:crypto';

test('production atlas serves its assets and retains the story publication boundary', async t => {
  const { server, port } = await startProdServer({ port: 0, host: '127.0.0.1', outDir: 'dist' });
  installPublicDelivery(server);
  t.after(() => new Promise(resolve => { server.closeAllConnections(); server.close(resolve); }));
  const origin = `http://127.0.0.1:${port}`;
  const response = await fetch(origin + '/labs?story=climate-stripes');
  assert.equal(response.status, 200);
  const html = await response.text();
  for (const text of ['Ask more of the record.', 'County Observatory', 'Signal Studio', 'Climate Stripes', 'Research instruments', 'Source observatory', 'Return to the Kansas map']) assert.ok(html.includes(text), text);
  assert.ok(html.includes('Open labs with data ('));
  assert.ok(html.includes('These open labs include public records from NOAA'));
  assert.ok(!html.includes('kfm-story-bundle-v1'), 'no private snapshot is embedded in the HTML');
  assert.ok(!html.includes('127.0.0.1:4360'), 'no owner-PC address is a public dependency');
  const assets = [...new Set([...html.matchAll(/(?:src|href)="(\/assets\/[^"?]+\.(?:js|css))"/g)].map(match => match[1]))];
  assert.ok(assets.length > 0);
  for (const path of assets) assert.equal((await fetch(origin + path)).status, 200, path);
  for (const [route, expected] of [['/labs/observatory', 'Where do the patterns live?'], ['/labs/signals', 'Question the connection.']]) {
    const reply = await fetch(origin + route); assert.equal(reply.status, 200, route);
    const content = await reply.text();
    // The county content waits for exact-byte public data in the browser.
    assert.ok(content.includes(route === '/labs/observatory' ? 'County Observatory' : expected), route);
    assert.ok(!content.includes('127.0.0.1'), route);
  }
  for (const [id, snapshot] of Object.entries(PUBLIC_LAB_SNAPSHOTS)) {
    const reply = await fetch(origin + snapshot.path);
    assert.equal(reply.status, 200, id);
    const bytes = Buffer.from(await reply.arrayBuffer());
    assert.equal(bytes.length, snapshot.bytes);
    assert.equal(createHash('sha256').update(bytes).digest('hex'), snapshot.sha256);
    assert.equal(JSON.parse(bytes).story, id);
  }
  assert.ok(PENDING_DATASETS.has('stories'));
  assert.ok(!DATASETS.has('stories'));
  const data = await fetch(origin + '/api/local-data/stories?story=climate-stripes');
  assert.equal(data.status, 404, 'production must not serve private preview bundles');
  const body = await data.text();
  assert.ok(!body.includes('kfm-story-bundle-v1'));
  const home = await (await fetch(origin)).text();
  assert.ok(home.includes('href="/labs"'), 'the map navigation links to the atlas');

  // The existing canonical-host redirect must preserve the new route and selection.
  const redirect = await new Promise((resolve, reject) => {
    const req = request(origin + '/labs?story=river-memory', { headers: { Host: 'www.kansasfrontiermatrix.com' } }, res => {
      res.resume();
      resolve({ status: res.statusCode, location: res.headers.location });
    });
    req.on('error', reject); req.end();
  });
  assert.deepEqual(redirect, { status: 308, location: 'https://kansasfrontiermatrix.com/labs?story=river-memory' });
});
