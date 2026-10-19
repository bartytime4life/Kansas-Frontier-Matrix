import test from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { readFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { createHash } from 'node:crypto';
import { collectModules } from '../scripts/serve-local-worker.mjs';
import { applicationIdentity } from '../scripts/build-identity.mjs';

// Exercises the compiled Worker in disposable storage, without a hosted session.
test('built Staging serves its guide/identity/assets and preserves private and unreleased denials', async t => {
  const require = createRequire(import.meta.url);
  const runtimeRequire = createRequire(require.resolve('wrangler'));
  const { unstable_getMiniflareWorkerOptions } = require('wrangler');
  const { Miniflare, convertV4MiniflareOptions, Log, LogLevel } = runtimeRequire('miniflare');
  const translated = unstable_getMiniflareWorkerOptions(resolve('dist/server/wrangler.json'));
  const worker = { ...translated.workerOptions, modules: collectModules(resolve('dist/server')), modulesRoot: resolve('dist/server') };
  delete worker.modulesRules;
  const runtime = new Miniflare(convertV4MiniflareOptions({ host: '127.0.0.1', port: 0, log: new Log(LogLevel.ERROR), workers: [worker] }));
  t.after(() => runtime.dispose());
  const origin = 'https://kfm-public-staging-20261012.blackbart-55.chatgpt.site';
  const get = path => runtime.dispatchFetch(origin + path);
  const response = await get('/api/build');
  assert.equal(response.status, 200);
  assert.equal(response.headers.get('cache-control'), 'no-store');
  const actual = await response.json(), expected = await applicationIdentity();
  assert.equal(actual.application, 'appgprj_6acd1aafe0d88191a4306ea2ab44ed91');
  assert.equal(actual.sourceDigest, expected.sourceDigest);
  assert.equal(actual.sourceFileCount, expected.sourceFileCount);
  assert.deepEqual(Object.keys(actual).sort(), ['application','commitState','profile','scope','sourceCommit','sourceDigest','sourceFileCount'].sort());
  const about = await (await get('/about')).text();
  for (const id of ['about-main','workflow','capabilities','evidence','project','sources']) {
    assert.ok(about.includes(`id="${id}"`), id);
    assert.ok(about.includes(`href="#${id}"`), 'jump target '+id);
  }
  assert.ok(about.includes(actual.sourceDigest));
  assert.ok(about.includes('No observational or subsurface package is approved'));
  assert.ok(about.includes('held records are not transferred'));
  assert.ok(about.includes('GoDaddy Node 22'));
  const account = await get('/api/staging/account');assert.equal(account.status,200);assert.equal((await account.json()).account,null);
  const ai = await (await get('/api/ai/status')).json();assert.equal(ai.ready,false);assert.equal(ai.requiresLogin,true);
  assert.equal((await runtime.dispatchFetch(origin+'/api/ai/jobs',{method:'POST',headers:{Origin:origin,'Content-Type':'application/json'},body:'{}'})).status,401);
  const signed = await runtime.dispatchFetch(origin+'/api/ai/status',{headers:{'oai-authenticated-user-id':'synthetic','oai-authenticated-user-email':'synthetic@example.test'}});
  const status=await signed.json();assert.equal(status.reasonCode,'QWEN_CONNECTION_NOT_CONFIGURED');assert.equal(status.ready,false);
  assert.ok(about.includes('docs/runbooks/godaddy-node-hosting.md'));
  for (const path of ['/','/topics','/almanacs','/observatory/sources']) assert.equal((await get(path)).status, 200, path);
  for (const path of ['/api/qwen','/api/intake/status','/data/subsurface/manifest.json','/downloads','/api/build/private']) assert.equal((await get(path)).status, 404, path);
  assert.equal((await runtime.dispatchFetch(origin+'/api/build', {method:'POST'})).status, 404);
  assert.equal((await runtime.dispatchFetch('https://alternate.workers.dev/api/build')).status, 403);
  const catalog = await get('/api/governed/public/catalog');
  assert.notEqual((await catalog.json()).envelope?.outcome, 'ANSWER', 'empty catalog cannot approve data');
  const assets = [...new Set([...about.matchAll(/(?:href|src)="(\/assets\/[^"?]+\.(?:js|css))"/g)].map(match => match[1]))];
  assert.ok(assets.length > 0);
  for (const path of assets) {
    const response = await get(path);
    assert.equal(response.status, 200, path);
    const hash = data => createHash('sha256').update(data).digest('hex');
    assert.equal(hash(Buffer.from(await response.arrayBuffer())), hash(await readFile('dist/client'+path)), path);
  }
});
