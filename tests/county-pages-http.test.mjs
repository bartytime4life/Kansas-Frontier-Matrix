import test from 'node:test';
import assert from 'node:assert/strict';
import { startProdServer } from 'vinext/server/prod-server';
import facts from '../app/county-facts.generated.json' with { type: 'json' };
import { installPublicDelivery } from '../server/browser-headers.mjs';

test('the production server renders each county profile with both county changes', async t => {
  const { server, port } = await startProdServer({ port: 0, host: '127.0.0.1', outDir: 'dist' });
  installPublicDelivery(server);
  t.after(() => new Promise(resolve => { server.closeAllConnections(); server.close(resolve); }));
  const origin = `http://127.0.0.1:${port}`;

  for (const { slug, name, fips } of facts.counties) {
    const response = await fetch(`${origin}/counties/${slug}`, { signal: AbortSignal.timeout(10_000) });
    assert.equal(response.status, 200, slug);
    const html = await response.text();
    // The framework's error boundary can also return 200. Require the actual page heading.
    const heading = html.match(/<h1[^>]*>(.*?)<\/h1>/)?.[1].replaceAll('<!-- -->', '');
    assert.equal(heading, `${name}, Kansas`, slug);
    assert.ok(html.includes('people lived in'), `${slug} population`);
    assert.ok(html.includes('<h2>Bridges</h2>'), `${slug} bridge inventory`);
    assert.ok(html.includes('Census Bureau comparison method'), `${slug} survey methodology`);
    assert.ok(html.includes(`href="/labs/observatory?county=${fips}"`), `${slug} Observatory link`);
    if (slug === 'anderson') {
      assert.ok(html.includes('17.5% (±3.3)'));
      assert.ok(html.includes('Difference uncertain'));
    }
  }
});
