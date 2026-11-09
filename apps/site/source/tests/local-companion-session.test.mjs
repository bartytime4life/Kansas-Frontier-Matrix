import assert from 'node:assert/strict';
import test from 'node:test';
import vm from 'node:vm';
import { readFile } from 'node:fs/promises';
import { isAbsolute, join } from 'node:path';
import ts from 'typescript';

const source = await readFile('app/local-companion-session.ts', 'utf8');
const compile = text => ts.transpileModule(text, { compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 } }).outputText;
const tokens = { downloads: 'd'.repeat(43), intake: 'i'.repeat(43), basemap: 'b'.repeat(43) };
function browser(hash = '', saved = new Map(), disabled = false) {
  const location = { hash, pathname: '/downloads', search: '?tab=library' };
  const replaced = [];
  const window = { location, history: { replaceState(_state, _title, path) { replaced.push(path); location.hash = path.includes('#') ? '#' + path.split('#')[1] : ''; } },
    sessionStorage: { getItem(key) { if (disabled) throw Error(); return saved.get(key) ?? null; }, setItem(key, value) { if (disabled) throw Error(); saved.set(key, value); }, removeItem(key) { if (disabled) throw Error(); saved.delete(key); } } };
  return { window, saved, replaced };
}
function session(env) {
  const exports = {};
  vm.runInNewContext(compile(source), { exports, URLSearchParams, ...(env ? { window: env.window } : {}) });
  return exports;
}

test('owner fragments provision independent services, scrub URL and survive tab reload', () => {
  const env = browser('#section=library&' + Object.entries(tokens).map(([name, token]) => `kfm-${name}=${token}`).join('&'));
  const client = session(env);
  for (const name of Object.keys(tokens)) assert.equal(client.companionSession(name), tokens[name]);
  assert.deepEqual(env.replaced, ['/downloads?tab=library#section=library']);
  assert.equal(env.saved.size, 3);
  const reload = session(browser('', env.saved));
  for (const name of Object.keys(tokens)) assert.equal(reload.companionSession(name), tokens[name]);
});

test('missing, malformed and duplicate capabilities fail closed; storage denial still allows an owner link', () => {
  assert.equal(session().companionSession('downloads'), '');
  assert.equal(session(browser()).companionSession('downloads'), '');
  for (const hash of ['#kfm-downloads=bad', `#kfm-downloads=${tokens.downloads}&kfm-downloads=${tokens.downloads}`, '#kfm-downloads=%C3%A9', `#kfm-downloads=${tokens.downloads}%0A`]) {
    const saved = new Map([['kfm-downloads-session', tokens.downloads]]);
    const env = browser(hash, saved);
    assert.equal(session(env).companionSession('downloads'), '');
    assert.equal(saved.has('kfm-downloads-session'), false);
    assert.equal(env.window.location.hash, '');
  }
  const env = browser(`#kfm-intake=${tokens.intake}`, new Map(), true);
  assert.equal(session(env).companionSession('intake'), tokens.intake);
  assert.equal(env.window.location.hash, '');
});

test('every Explorer transport authenticates initial GET from the owner fragment', async () => {
  const env = browser('#' + Object.entries(tokens).map(([name, token]) => `kfm-${name}=${token}`).join('&'));
  const owner = session(env);
  const calls = [];
  const fetch = async (url, init) => { calls.push({ url, init }); return { ok: true, text: async () => JSON.stringify({ schema: 'kfm-basemap-cache/v1', limitBytes: 10_000_000_000, usedBytes: 0, destination: '/owner/basemap-cache', sessionToken: tokens.basemap, job: {} }) }; };
  const dependencies = { './local-companion-session': owner, './bounded-json': { readBoundedJson: async () => ({ test: true }) }, './intake-desk-client': { INTAKE_DESK_ORIGIN: 'http://127.0.0.1:8771' }, './public-map-catalog': {} };
  async function module(file) {
    const exports = {};
    vm.runInNewContext(compile(await readFile(`app/${file}.ts`, 'utf8')), { exports, require: name => { assert.ok(dependencies[name], name); return dependencies[name]; }, fetch, URL, Date, AbortSignal, DOMException });
    return exports;
  }
  const signal = new AbortController().signal;
  await (await module('local-download-client')).localDownloadRequest('/status', signal);
  await (await module('public-map-client')).publicMapRequest('/status', signal);
  await (await module('intake-desk-client')).intakeOverviewRequest(signal);
  await (await module('local-atlas-client')).atlasRequest('/api/status', signal, () => true);
  assert.ok(await (await module('basemap-cache')).connectBasemapCache());
  for (const [index, service] of ['downloads', 'downloads', 'intake', 'intake', 'basemap'].entries()) {
    assert.equal(calls[index].init.headers['X-KFM-Session'], tokens[service]);
    assert.equal(calls[index].init.credentials, 'omit');
    assert.equal(calls[index].init.redirect, 'error');
    assert.equal(calls[index].url.includes(tokens[service]), false);
  }
  assert.equal(env.window.location.hash, '');
});

async function deskClient(env, fetch, workspace) {
  const repositoryRoot = process.env.KFM_WEATHER_REPOSITORY_ROOT;
  if (repositoryRoot && !isAbsolute(repositoryRoot)) throw new Error('KFM_WEATHER_REPOSITORY_ROOT must be absolute');
  const deskPath = repositoryRoot ? join(repositoryRoot, 'tools/local_data/intake_desk/desk.js') : '../../../tools/local_data/intake_desk/desk.js';
  const desk = (await readFile(deskPath, 'utf8')).split('const project =')[0];
  const context = vm.createContext({ URLSearchParams, location: env.window.location, history: env.window.history, sessionStorage: env.window.sessionStorage,
    document: { body: { dataset: workspace ? { kfmWorkspace: workspace } : {} } }, fetch });
  vm.runInContext(desk, context);
  return context;
}

test('standalone Desk consumes its fragment and authenticates API reads and writes', async () => {
  const env = browser(`#kfm-intake=${tokens.intake}`);
  const calls = [];
  const context = await deskClient(env, async (path, init) => { calls.push({ path, init }); return { ok: true, json: async () => ({}) }; });
  await vm.runInContext('api("/api/status")', context);
  await vm.runInContext('api("/api/analyze", {})', context);
  assert.deepEqual(calls.map(call => call.path), ['/api/status', '/api/analyze'], 'the public shell does not bootstrap an operator session');
  for (const call of calls) {
    assert.equal(call.init.headers['X-KFM-Session'], tokens.intake);
    assert.equal(call.init.credentials, 'omit');
    assert.equal(call.init.redirect, 'error');
    assert.equal(call.path.includes(tokens.intake), false);
  }
  assert.equal(calls[0].init.method, undefined);
  assert.equal(calls[1].init.method, 'POST');
  assert.equal(calls[1].init.headers['Content-Type'], 'application/json');
  assert.equal(calls[1].init.body, '{}');
  assert.equal(env.window.location.hash, '');
});

test('operator Desk awaits its session handshake before scoped API reads and writes', async () => {
  const env = browser();
  const calls = [];
  const workspace = 'operator-fixture', token = 'o'.repeat(43);
  let completeSession;
  const pendingSession = new Promise(resolve => { completeSession = resolve; });
  const context = await deskClient(env, async (path, init) => {
    calls.push({ path, init });
    return path === '/api/session' ? pendingSession : { ok: true, json: async () => ({}) };
  }, workspace);
  const read = vm.runInContext('api("/api/status")', context);
  const write = vm.runInContext('api("/api/analyze", {requested: true})', context);
  assert.deepEqual(calls.map(call => call.path), ['/api/session'], 'API operations wait for the operator handshake');
  assert.equal(calls[0].init.headers, undefined, 'the session bootstrap does not forward a stored capability');
  completeSession({ ok: true, json: async () => ({ token }) });
  await Promise.all([read, write]);
  assert.deepEqual(calls.map(call => call.path), ['/api/session', `/api/workspace/${workspace}/status`, `/api/workspace/${workspace}/analyze`]);
  for (const call of calls) {
    assert.equal(call.init.cache, 'no-store');
    assert.equal(call.init.credentials, 'omit');
    assert.equal(call.init.redirect, 'error');
    assert.equal(call.path.includes(token), false);
  }
  for (const call of calls.slice(1)) assert.equal(call.init.headers['X-KFM-Session'], token);
  assert.equal(calls[1].init.method, undefined);
  assert.equal(calls[2].init.method, 'POST');
  assert.equal(calls[2].init.body, '{"requested":true}');
  assert.equal(env.saved.size, 0, 'the operator handshake does not persist its capability');
});
