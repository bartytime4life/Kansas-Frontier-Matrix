import test from 'node:test';
import assert from 'node:assert/strict';
import { startProdServer } from 'vinext/server/prod-server';
import { installPublicDelivery } from '../server/browser-headers.mjs';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
const pathwayJavascript = ts.transpileModule(await readFile('app/research/pathways.ts', 'utf8'), {compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const {RESEARCH_PATHWAYS,pathwayComparisonHref} = await import(`data:text/javascript;base64,${Buffer.from(pathwayJavascript).toString('base64')}`);

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
  for (const text of ['registered map sources', 'Compare before you combine.', 'Explore Kansas, across disciplines.', 'EXTERNAL_CONTEXT_ONLY']) assert.ok(html.includes(text), text);
  for (const href of ['/labs', '/data-library', '/observatory', '/observatory/sources', '/science', '/labs/heat-and-rain', '/labs/county-drought', '/labs/soil-profile', '/labs/daily-air-quality', '/labs/sunlight-and-sky']) assert.ok(html.includes(`href="${href}"`), href);
  assert.ok(html.includes('id="observation-tools"'), 'science entry remains in the body at phone widths');
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


test('research cards expose registered data access and readable reuse credits without comparison', async t => {
  const {server, port} = await startProdServer({port:0, host:'127.0.0.1', outDir:'dist'});
  installPublicDelivery(server);
  t.after(() => new Promise(resolve => { server.closeAllConnections(); server.close(resolve); }));
  const origin = `http://127.0.0.1:${port}`;
  const response = await fetch(origin + '/research?q=DeFlock');
  assert.equal(response.status, 200);
  const html = await response.text();
  const credit = html.match(/<dt>Attribution<\/dt><dd>([\s\S]*?)<\/dd>/)?.[1];
  assert.ok(credit, 'the visible card retains its attribution');
  assert.ok(credit.includes('href="https://www.openstreetmap.org/copyright"'));
  assert.ok(credit.includes('href="https://opendatacommons.org/licenses/odbl/1-0/"'));
  assert.ok(credit.includes('OpenStreetMap contributors'));
  assert.ok(!credit.includes('&lt;a'), 'credits render as text and safe links, not raw HTML');
  assert.match(html, /href="\/api\/live-context\?feed=deflock-alpr" aria-label="Generalized report cells · ODbL 1.0: DeFlock · reported ALPR areas"/);
  assert.ok(html.includes('aria-label="Open on map: DeFlock · reported ALPR areas"'));
  assert.ok(html.includes('aria-label="Provider: DeFlock · reported ALPR areas"'));
  assert.ok(!html.includes('aria-label="Selected source comparison"'), 'data access needs no comparison selection');

  const selected = await fetch(origin + '/research?compare=census-congress-119');
  const selectedHtml = await selected.text();
  assert.ok(selectedHtml.includes('Attribution &amp; reuse'));
  assert.ok(selectedHtml.includes('href="/civic-history-license.txt"'));
});


test('statewide pathways expose real tool routes and fragments with equal subject coverage before the case study', async t => {
  const {server, port} = await startProdServer({port:0, host:'127.0.0.1', outDir:'dist'});
  installPublicDelivery(server);
  t.after(() => new Promise(resolve => { server.closeAllConnections(); server.close(resolve); }));
  const origin = `http://127.0.0.1:${port}`;
  const html = await (await fetch(origin + '/research')).text();
  const escape = value => value.replaceAll('&', '&amp;').replaceAll('"', '&quot;');
  assert.deepEqual([...html.matchAll(/data-research-pathway="([^"]+)"/g)].map(match => match[1]), RESEARCH_PATHWAYS.map(pathway => pathway.id));
  assert.ok(html.indexOf('id="research-pathways"') < html.indexOf('id="terrain-pilot-title"'), 'all subjects lead the optional Konza example');
  assert.match(html, /<details[^>]*><summary id="terrain-pilot-title">Konza Prairie/);
  assert.ok(html.includes('One 1 km KONZ tile'));
  assert.ok(html.includes('Provider canopy is distinct from surface minus ground'));
  const responses = new Map();
  async function route(href) {
    const url = new URL(href, origin);
    const path = url.pathname + url.search;
    if (!responses.has(path)) {
      const response = await fetch(origin + path);
      assert.equal(response.status, 200, href);
      responses.set(path, await response.text());
    }
    if (url.hash) assert.ok(responses.get(path).includes(`id="${url.hash.slice(1)}"`), `real target for ${href}`);
  }
  for (const pathway of RESEARCH_PATHWAYS) {
    assert.ok(html.includes(escape(pathway.scope)), pathway.id + ' scope remains visible');
    assert.ok(html.includes(escape(pathway.boundary)), pathway.id + ' limits remain visible');
    assert.ok(html.includes(`href="${escape(pathwayComparisonHref(pathway))}"`), pathway.id + ' comparison');
    for (const tool of pathway.tools) {
      assert.ok(html.includes(`href="${escape(tool.href)}"`), tool.label);
      await route(tool.href);
    }
    await route(pathway.topicHref);
  }
});
