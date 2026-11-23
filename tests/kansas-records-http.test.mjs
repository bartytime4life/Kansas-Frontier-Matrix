import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import test from 'node:test';
import { startProdServer } from 'vinext/server/prod-server';
import records from '../app/kansas-records.generated.json' with { type: 'json' };
import { installPublicDelivery } from '../server/browser-headers.mjs';

test('the records page offers group navigation, interactive views and exact published inputs', async t => {
  const { server, port } = await startProdServer({ port: 0, host: '127.0.0.1', outDir: 'dist' });
  installPublicDelivery(server);
  t.after(() => new Promise(resolve => server.close(resolve)));
  const origin = `http://127.0.0.1:${port}`;
  const get = path => fetch(origin + path, { signal: AbortSignal.timeout(10_000), redirect: 'error' });

  const page = await get('/records');
  assert.equal(page.status, 200);
  const html = await page.text();
  const navigation = html.split('aria-label="Record groups">')[1]?.split('</nav>')[0];
  assert.ok(navigation);
  const destinations = {
    people: '/labs?story=census-mosaic',
    survey: '/labs/observatory',
    bridges: '/labs?story=built-kansas',
    tornadoes: '/labs?story=tornado-tracks',
  };
  for (const { id, snapshot } of records.sections) {
    assert.ok(navigation.includes(`href="#records-${id}"`), id + ' section link');
    const section = html.split(`<section aria-labelledby="records-${id}">`)[1]?.split('</section>')[0];
    assert.ok(section?.includes(`id="records-${id}"`), id + ' heading');
    assert.ok(section.includes(`href="${destinations[id]}"`), id + ' interactive view');
    assert.ok(section?.includes(`href="${snapshot.path}" download=""`), id + ' download');
    assert.ok(section.includes(snapshot.sha256), id + ' checksum');
    const response = await get(snapshot.path);
    assert.equal(response.status, 200, id);
    assert.match(response.headers.get('content-type') ?? '', /^application\/json\b/);
    const bytes = Buffer.from(await response.arrayBuffer());
    assert.equal(bytes.length, snapshot.bytes, id);
    assert.equal(createHash('sha256').update(bytes).digest('hex'), snapshot.sha256, id);
  }
});
