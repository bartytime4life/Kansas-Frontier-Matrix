import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile, mkdtemp, mkdir, writeFile, rm, symlink } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { promisify } from 'node:util';
import { execFile } from 'node:child_process';
import vm from 'node:vm';
import ts from 'typescript';
const run = promisify(execFile);
const read = name => readFile(new URL(`../${name}`, import.meta.url), 'utf8');
async function load(name, dependencies = {}) {
  const exports = {};
  const code = ts.transpileModule(await read(name), { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
  vm.runInNewContext(code, { exports, require: id => dependencies[id] ?? {}, URL, Response, TextDecoder, TextEncoder, Uint8Array });
  return exports;
}
const routes = await load('app/public-route-policy.ts');
test('public routes refuse legacy stores, companion APIs, mutation and encoded traversal', () => {
  for (const path of ['/data/subsurface/manifest.json', '/history/all.json', '/public/data/x.json', '/api/qwen', '/api/intake/status', '/api/local-atlas', '/api/daily-archive', '/api/water-direction', '/_vinext/image', '/api/governed/public/assets/subsurface/a%2fb.json'])
    assert.equal(routes.publicRouteDecision(path).allowed, false, path);
  assert.equal(routes.publicRouteDecision('/', 'POST').allowed, false);
  for (const method of ['DELETE', 'PUT', 'PATCH']) assert.equal(routes.publicRouteDecision('/api/governed/water-admin/activate', method).allowed, false);
  for (const path of ['/', '/topics', '/almanacs?topic=weather', '/almanacs/farmers-winter-2026-2027.jpg', '/assets/index-123.js', '/api/governed/v1/layers', '/api/governed/weather/v1/layers', '/api/governed/public/catalog', '/api/governed/public/assets/subsurface/manifest.json', '/governed/subsurface-release'])
    assert.equal(routes.publicRouteDecision(path).allowed, true, path);
  assert.equal(routes.publicRouteDecision('/api/governed/subsurface-admin/activate', 'POST').reason, 'OWNER_AUTHORIZATION_REQUIRED');
});

class AdminError extends Error { constructor(reason, status) { super(reason); this.status = status; } }
const admin = await load('app/governed-water-admin-server.ts', { './governed-water-admin': { WaterAdminError: AdminError } });
test('bounded upload cancels oversized chunked bodies without trusting Content-Length', async () => {
  let cancelled = false;
  const stream = new ReadableStream({ start(controller) { controller.enqueue(new Uint8Array(3)); controller.enqueue(new Uint8Array(3)); }, cancel() { cancelled = true; } });
  const request = new Request('https://preview.test/upload', { method: 'POST', body: stream, duplex: 'half' });
  await assert.rejects(admin.readBoundedText(request, 5), error => error.status === 413 && error.message === 'REQUEST_TOO_LARGE');
  assert.equal(cancelled, true);
  assert.equal(await admin.readBoundedText(new Request('https://preview.test/upload', { method: 'POST', body: 'real bytes' }), 10), 'real bytes');
  await assert.rejects(admin.readBoundedText(new Request('https://preview.test/upload', { method: 'POST', body: new Uint8Array([255]) }), 10), /REQUEST_NOT_UTF8/);
});

test('static scanner rejects private stores and links; clean application assets pass', async () => {
  const dir = await mkdtemp(join(tmpdir(), 'kfm-public-asset-test-'));
  try {
    await writeFile(join(dir, 'ui.js'), 'console.log("UI");');
    const script = new URL('../scripts/verify-public-assets.mjs', import.meta.url).pathname;
    assert.equal(JSON.parse((await run(process.execPath, [script, dir])).stdout).outcome, 'PASS');
    await mkdir(join(dir, 'data'));
    await writeFile(join(dir, 'data/private.json'), '{"private":true}');
    await symlink(join(dir, 'ui.js'), join(dir, 'unsafe-link'));
    await assert.rejects(run(process.execPath, [script, dir]), error => {
      const result = JSON.parse(error.stdout);
      return result.outcome === 'HOLD' && result.unapproved_paths.includes('data') && result.unapproved_paths.includes('unsafe-link');
    });
  } finally { await rm(dir, { recursive: true, force: true }); }
});

test('owner activation accepts package selection only and server readers enforce the trusted list', async () => {
  const console = await read('app/water-release-console.tsx');
  assert.doesNotMatch(console, /decisionText|<textarea|decision,/);
  assert.match(console, /authorized_packages/);
  for (const family of ['water','weather','soil','storm-events','earthquakes']) {
    const activate = await read(`app/api/governed/${family}-admin/activate/route.ts`);
    assert.match(activate, /publicDecisionForActivation/);
    assert.match(activate, /Object.keys\(publicRequest\)/);
    assert.match(await read(`app/governed-${family}-server.ts`), /await publicFamilyAuthorization/);
  }
});


test('alternate Worker origins cannot reach public or privileged application routes', () => {
  const hosted = 'https://kfm-public-staging-20261012.blackbart-55.chatgpt.site';
  const canonical = 'https://kansasfrontiermatrix.com';
  for (const input of [hosted + '/', canonical + '/api/governed/water-admin/withdraw', 'https://www.kansasfrontiermatrix.com/map', 'http://127.0.0.1:4328/'])
    assert.equal(routes.publicApplicationOriginAllowed(input, hosted, canonical), true);
  for (const input of ['https://alternate.workers.dev/api/governed/water-admin/withdraw', 'http://kansasfrontiermatrix.com/', 'https://kansasfrontiermatrix.com:444/', 'https://evil.test/', 'https://name:password@kansasfrontiermatrix.com/'])
    assert.equal(routes.publicApplicationOriginAllowed(input, hosted, canonical), false);
});
