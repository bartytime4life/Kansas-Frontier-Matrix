import test from 'node:test';
import assert from 'node:assert/strict';
import { startProdServer } from 'vinext/server/prod-server';
import facts from '../app/county-facts.generated.json' with { type: 'json' };
import { installPublicDelivery } from '../server/browser-headers.mjs';

test('the production server links to the directory and renders all county profiles', async t => {
  const { server, port } = await startProdServer({ port: 0, host: '127.0.0.1', outDir: 'dist' });
  installPublicDelivery(server);
  t.after(() => new Promise(resolve => { server.closeAllConnections(); server.close(resolve); }));
  const origin = `http://127.0.0.1:${port}`;
  const guidesResponse = await fetch(origin + '/explore');
  assert.equal(guidesResponse.status, 200);
  const guides = await guidesResponse.text();
  const directoryLink = guides.indexOf('href="/counties"');
  const firstGuide = guides.indexOf('href="/explore/frontier-trails"');
  assert.ok(directoryLink !== -1 && firstGuide !== -1 && directoryLink < firstGuide);
  assert.ok(guides.includes('href="/records"'));

  const directoryResponse = await fetch(origin + '/counties');
  assert.equal(directoryResponse.status, 200);
  const directory = await directoryResponse.text();
  assert.ok(directory.includes('Search by county name'));
  assert.ok(directory.includes('href="/records"'));
  const links = [...directory.matchAll(/href="(\/counties\/[a-z-]+)"/g)].map(match => match[1]);
  assert.deepEqual(links.sort(), facts.counties.map(({slug}) => `/counties/${slug}`).sort());

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
