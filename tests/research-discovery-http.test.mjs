import test from 'node:test';
import assert from 'node:assert/strict';
import { startProdServer } from 'vinext/server/prod-server';
import { installPublicDelivery } from '../server/browser-headers.mjs';

test('Research Discovery serves through production delivery with working assets, entry points and canonical identity', async t => {
  const {server, port} = await startProdServer({port:0, host:'127.0.0.1', outDir:'dist'});
  installPublicDelivery(server);
  t.after(() => new Promise(resolve => { server.closeAllConnections(); server.close(resolve); }));
  const origin = `http://127.0.0.1:${port}`;
  const response = await fetch(origin + '/research');
  assert.equal(response.status, 200);
  const html = await response.text();
  assert.match(html, /Research Discovery · Kansas Frontier Matrix/);
  assert.match(html, /rel="canonical" href="https:\/\/kansasfrontiermatrix.com\/research"/);
  for (const text of ['registered map sources', 'Compare before you combine.', 'Prairie science, across scales.', 'EXTERNAL_CONTEXT_ONLY']) assert.ok(html.includes(text), text);
  for (const href of ['/labs', '/data-library', '/observatory', '/observatory/sources']) assert.ok(html.includes(`href="${href}"`), href);
  assert.ok(!html.includes('href="/data"'), 'retired public contribution UI is not reintroduced');
  const pilotHref = '/acquisition#neon-lidar-lab';
  assert.ok(html.includes(`href="${pilotHref}"`), 'research readers can reach the working terrain lab');
  const lab = await fetch(origin + pilotHref);
  assert.equal(lab.status, 200);
  const labHtml = await lab.text();
  assert.ok(labHtml.includes('id="neon-lidar-lab"'), 'the discovery fragment resolves to the actual lab');
  assert.ok(labHtml.includes('Load Konza Prairie pilot'), 'the pilot still loads only through the explicit action');

  const assets = [...new Set([...html.matchAll(/(?:src|href)="(\/assets\/[^"?]+\.(?:js|css))"/g)].map(match => match[1]))];
  assert.ok(assets.length > 0);
  for (const path of assets) assert.equal((await fetch(origin + path)).status, 200, path);
  for (const path of ['/', '/about', '/observatory/sources', '/labs']) {
    const reply = await fetch(origin + path);
    assert.equal(reply.status, 200, path);
    assert.ok((await reply.text()).includes('href="/research"'), `${path} links to the new route`);
  }
  const sitemap = await (await fetch(origin + '/sitemap.xml')).text();
  assert.ok(sitemap.includes('<loc>https://kansasfrontiermatrix.com/research</loc>'));
});

test('production research deep links retain only known comparison IDs and keep searches inert', async t => {
  const {server, port} = await startProdServer({port:0, host:'127.0.0.1', outDir:'dist'});
  installPublicDelivery(server);
  t.after(() => new Promise(resolve => { server.closeAllConnections(); server.close(resolve); }));
  const origin = `http://127.0.0.1:${port}`;
  const compare = 'kgs-depth-to-water,kgs-saturated-thickness,kgs-monitoring-wells';
  const valid = await fetch(origin + '/research?compare=' + encodeURIComponent(compare));
  assert.equal(valid.status, 200);
  const html = await valid.text();
  assert.ok(html.includes('Selected source comparison'));
  assert.ok(html.includes('2022–2024 regional classified estimates'));
  assert.ok(html.includes('2026 monitoring locations'));
  assert.ok(html.includes('Explore selected sources on the map'));
  const invalid = await fetch(origin + '/research?' + new URLSearchParams({compare:'unknown-provider',q:'<img src=x onerror=alert(1)>'}));
  const invalidHtml = await invalid.text();
  assert.equal(invalid.status, 200);
  assert.ok(!invalidHtml.includes('aria-label="Selected source comparison"'));
  assert.ok(!invalidHtml.includes('<img src=x onerror=alert(1)>'));
});
