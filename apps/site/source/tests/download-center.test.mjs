import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import ts from 'typescript';
import { componentHarness, findNode, settle } from './component-harness.mjs';
const compile = async path => ts.transpileModule(await readFile(path, 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const url = value => `data:text/javascript;base64,${Buffer.from(value).toString('base64')}`;
const bounded = url(await compile('app/bounded-json.ts'));
const client = await import(url((await compile('app/local-download-client.ts')).replace('"./bounded-json"', JSON.stringify(bounded))));
const activity = await import(url(await compile('app/download-activity.ts')));
const polling = await import(url(await compile('app/download-polling.ts')));
const status = () => ({ schema: 'kfm-ee-download-control/v1', configured: false, project: null, authentication: 'idle', destination: '/local/captures', sessionToken: 'a'.repeat(43), active: null, jobs: [] });
const job = patch => ({ id: 'a'.repeat(32), selection: { dataset: 'ee-cdl', year: 2023, maxBytes: 8e9 }, state: 'downloading', bytes: 12345, completed: 0, total: 0, destination: '/local/captures/job', mapReady: false, createdAt: '2026-10-08T12:00:00Z', ...patch });
const library = patch => ({ schema: 'kfm-local-library/v1', state: 'scanning', scannedFiles: 100, generatedAt: null, entries: [], totalFiles: 0, totalBytes: 0, error: null, ...patch });
const collection = index => ({ id: index.toString(16).padStart(64, '0'), label: `Source ${index}`, lane: 'raw', files: index, bytes: index * 100, role: 'stored-candidate' });
const snapshot = () => { const entries = Array.from({ length: 40 }, (_, i) => collection(i + 1)); return library({ state: 'complete', generatedAt: '2026-10-08T12:00:00Z', entries, totalFiles: 820, totalBytes: 82000 }); };
const deferred = () => { let resolve, reject; const promise = new Promise((yes, no) => { resolve = yes; reject = no; }); return { promise, resolve, reject }; };
const css = { default: new Proxy({}, { get: (_, key) => key }) };
function nodes(tree, predicate) { if (!tree || typeof tree !== 'object') return []; return [...(predicate(tree) ? [tree] : []), ...[tree.props?.children].flat(Infinity).flatMap(child => nodes(child, predicate))]; }

test('real unconfigured backend status accepts null project and rejects false job/progress identities', () => {
  assert.ok(client.parseDownloadStatus(status()));
  const running = { ...status(), active: 'a'.repeat(32), jobs: [job()] };
  assert.ok(client.parseDownloadStatus(running));
  for (const patch of [{ selection: { dataset: 'ee-cdl', year: 2023, maxBytes: 0 } }, { total: -1 }, { total: 1, completed: 2 }, { bytes: '123' }, { mapReady: true }]) assert.equal(client.parseDownloadStatus({ ...running, jobs: [job(patch)] }), null);
  assert.equal(client.parseDownloadStatus({ ...status(), active: 'a'.repeat(32) }), null);
  assert.equal(client.automaticLocalConnection('http://127.0.0.1:4173'), true);
  for (const origin of ['http://localhost:4173', 'https://127.0.0.1:4173', 'http://127.0.0.1:4174', 'https://site.example']) assert.equal(client.automaticLocalConnection(origin), false);
});

test('library totals require complete dated identity and do not turn an unfinished scan into zero measured files', () => {
  assert.ok(client.parseLocalLibrary(library())); assert.ok(client.parseLocalLibrary(snapshot()));
  for (const value of [snapshot(), library({ state: 'complete' }), library({ entries: [collection(1)] }), snapshot()]) {
    if (value.totalBytes === 82000) value.totalBytes++;
    assert.equal(client.parseLocalLibrary(value), null);
  }
  assert.equal(client.parseLocalLibrary({ ...snapshot(), entries: [collection(1), collection(1)] }), null);
});

async function hookHarness(origin = 'https://hosted.example') {
  const calls = [], timers = new Map(), listeners = new Map(); let nextTimer = 0;
  const document = { visibilityState: 'visible', addEventListener: (name, fn) => listeners.set(name, fn), removeEventListener: (name, fn) => { if (listeners.get(name) === fn) listeners.delete(name); } };
  const environment = { document, setTimeout: (callback, delay) => { timers.set(++nextTimer, { callback, delay }); return nextTimer; }, clearTimeout: id => timers.delete(id) };
  const h = await componentHarness('app/use-local-downloads.ts', { './local-download-client': { ...client, localDownloadRequest: (path, signal, payload, token) => { const d = deferred(); calls.push({ path, signal, payload, token, ...d }); return d.promise; } },
    './download-activity': activity, './download-polling': { startDownloadPolling: run => polling.startDownloadPolling(run, environment) } },
    { window: { location: { origin } }, document, queueMicrotask, ...environment }, '\nexport function Probe(){return useLocalDownloads();}');
  const render = () => { const value = h.render(h.exports.Probe); h.commit(); return value; };
  const respond = async (index, body, code = 200) => { calls[index].resolve({ response: { ok: code >= 200 && code < 300, status: code }, body }); await settle(); };
  const tick = async () => { assert.equal(timers.size, 1, 'only one polling timer'); const [id, task] = [...timers][0]; timers.delete(id); task.callback(); await settle(); return task.delay; };
  render(); await settle(); render();
  return { ...h, render, respond, calls, timers, tick, visibility: value => { document.visibilityState = value; listeners.get('visibilitychange')?.(); }, listeners };
}

test('hosted connection is explicit, local connection is automatic, polling is bounded to one round and state announcements ignore byte changes', async () => {
  const hosted = await hookHarness(); assert.equal(hosted.calls.length, 0);
  hosted.render().connect(); hosted.render(); assert.deepEqual(hosted.calls.map(c => c.path), ['/status', '/library']);
  const running = { ...status(), active: 'a'.repeat(32), jobs: [job()] };
  await hosted.respond(0, running); await hosted.respond(1, snapshot());
  let state = hosted.render(); assert.equal(state.connection, 'connected'); const announcement = state.announcement;
  assert.equal(await hosted.tick(), 2500); assert.equal(hosted.calls.length, 4); assert.equal(hosted.timers.size, 0, 'no timer while reads are pending');
  await hosted.respond(2, { ...running, jobs: [job({ bytes: 15000 })] }); await hosted.respond(3, snapshot());
  state = hosted.render(); assert.equal(state.announcement, announcement, 'receiving bytes does not flood the live region');
  await hosted.tick(); await hosted.respond(4, { ...status(), jobs: [job({ state: 'downloaded', total: 1, completed: 1 })] }); await hosted.respond(5, snapshot());
  assert.match(hosted.render().announcement, /Downloaded · awaiting map review/); hosted.dispose(); assert.equal(hosted.timers.size, 0);
  const local = await hookHarness('http://127.0.0.1:4173'); assert.equal(local.calls.length, 2); local.dispose(); assert.ok(local.calls.every(c => c.signal.aborted));
});

test('hidden tabs cancel reads, quick return schedules immediate nonoverlapping refresh, late replies never replace current state', async () => {
  const h = await hookHarness('http://127.0.0.1:4173');
  h.visibility('hidden'); assert.ok(h.calls.every(c => c.signal.aborted)); h.visibility('visible'); assert.equal(h.calls.length, 2);
  await h.respond(0, status()); await h.respond(1, snapshot());
  assert.equal(h.render().status, null, 'aborted results are ignored'); assert.equal(await h.tick(), 0, 'foreground return refreshes immediately after retired round');
  assert.equal(h.calls.length, 4); await h.respond(2, status()); await h.respond(3, snapshot()); assert.equal(h.render().library.entries.length, 40);
  h.visibility('hidden'); assert.equal(h.timers.size, 0); h.visibility('visible'); assert.equal(h.calls.length, 6);
  h.dispose(); await h.respond(4, { ...status(), project: 'STALE' }); await h.respond(5, library()); assert.notEqual(h.render().status.project, 'STALE'); assert.equal(h.timers.size, 0);
});

test('a failed or older library service retains last completed snapshot and cancellation has a visible action message', async () => {
  const h = await hookHarness('http://127.0.0.1:4173');
  await h.respond(0, { ...status(), active: 'a'.repeat(32), jobs: [job()] }); await h.respond(1, snapshot());
  await h.tick(); await h.respond(2, { ...status(), active: 'a'.repeat(32), jobs: [job()] }); await h.respond(3, { error: 'NOT_FOUND' }, 404);
  let value = h.render(); assert.equal(value.library.entries.length, 40); assert.match(value.libraryError, /does not support library/);
  const cancellation = value.cancelJob(); assert.equal(h.calls[4].path, '/cancel'); assert.equal(h.calls[4].token, status().sessionToken); assert.equal(h.calls[4].payload.id, 'a'.repeat(32));
  await h.respond(4, { error: 'FAILED' }, 503); await cancellation; value = h.render(); assert.match(value.actionNotice, /Cancellation was not confirmed/); assert.equal(value.cancelling, false); h.dispose();
});

test('background library refresh keeps prior results, uses session write check, and status failures do not imply empty storage', async () => {
  const h = await hookHarness('http://127.0.0.1:4173'); await h.respond(0, status()); await h.respond(1, snapshot());
  const refresh = h.render().refreshLibrary(); assert.equal(h.calls[2].path, '/library/refresh'); assert.equal(JSON.stringify(h.calls[2].payload), '{}'); assert.equal(h.calls[2].token, status().sessionToken);
  await h.respond(2, { ...snapshot(), state: 'scanning', scannedFiles: 12 }); await refresh;
  let value = h.render(); assert.equal(value.library.entries.length, 40); assert.equal(value.library.state, 'scanning');
  await h.respond(3, {}, 503); await h.respond(4, { ...snapshot(), state: 'failed', error: 'LIBRARY_SCAN_CHANGED' });
  value = h.render(); assert.equal(value.connection, 'unavailable'); assert.equal(value.library.totalBytes, 82000); assert.equal(value.library.state, 'failed'); h.dispose();
});

test('Earth Engine terminal transfer refreshes the library once, without rescanning historical jobs on connection', async () => {
  const h = await hookHarness('http://127.0.0.1:4173');
  const historical = job({ state: 'cancelled' });
  await h.respond(0, { ...status(), jobs: [historical] }); await h.respond(1, snapshot());
  assert.equal(h.calls.filter(c => c.path === '/library/refresh').length, 0);
  await h.tick();
  const active = job({ id: 'b'.repeat(32) });
  await h.respond(2, { ...status(), active: active.id, jobs: [historical, active] }); await h.respond(3, snapshot());
  await h.tick();
  const terminal = { ...active, state: 'cancelled' };
  await h.respond(4, { ...status(), jobs: [historical, terminal] }); await h.respond(5, snapshot());
  assert.equal(h.calls[6].path, '/library/refresh'); assert.equal(h.calls[6].token, status().sessionToken);
  await h.respond(6, { ...snapshot(), state: 'scanning' });
  await h.respond(7, { ...status(), jobs: [historical, terminal] }); await h.respond(8, snapshot());
  await h.tick(); await h.respond(9, { ...status(), jobs: [historical, terminal] }); await h.respond(10, snapshot());
  assert.equal(h.calls.filter(c => c.path === '/library/refresh').length, 1);
  h.dispose();
});

test('accepted Earth Engine start keeps its shared lock until a status read issued after acknowledgement', async () => {
  const h = await hookHarness('http://127.0.0.1:4173'); await h.respond(0, status()); await h.respond(1, snapshot());
  await h.tick(); // This request began before the POST acknowledgement.
  h.render().setStarting(true); h.render().confirmStart(); h.render().refresh();
  await h.respond(2, status()); await h.respond(3, snapshot());
  assert.equal(h.render().starting, true, 'an old empty snapshot cannot release the global pending lock');
  assert.equal(await h.tick(), 0);
  await h.respond(4, { ...status(), active: 'a'.repeat(32), jobs: [job()] }); await h.respond(5, snapshot());
  assert.equal(h.render().starting, false); assert.equal(h.render().status.active, 'a'.repeat(32)); h.dispose();
});

test('terminal transfer during a running scan queues one trailing scan, shared by both providers', async () => {
  const h = await hookHarness('http://127.0.0.1:4173');
  await h.respond(0, { ...status(), active: 'a'.repeat(32), jobs: [job()] }); await h.respond(1, { ...snapshot(), state: 'scanning' });
  await h.tick(); const terminal = { ...status(), jobs: [job({ state: 'cancelled' })] };
  await h.respond(2, terminal); await h.respond(3, { ...snapshot(), state: 'scanning' });
  await h.render().refreshLibrary(); // The public-map terminal callback uses this same API.
  assert.equal(h.calls.filter(c => c.path === '/library/refresh').length, 0, 'avoid the backend no-op during a running scan');
  await h.tick(); await h.respond(4, terminal); await h.respond(5, snapshot());
  assert.equal(h.calls[6].path, '/library/refresh');
  await h.respond(6, { ...snapshot(), state: 'scanning' });
  await h.respond(7, terminal); await h.respond(8, snapshot());
  await h.tick(); await h.respond(9, terminal); await h.respond(10, snapshot());
  assert.equal(h.calls.filter(c => c.path === '/library/refresh').length, 1, 'the trailing scan does not queue itself again'); h.dispose();
});

test('library reads issued before refresh acknowledgement cannot overwrite scanning or consume the trailing refresh', async () => {
  const h = await hookHarness('http://127.0.0.1:4173'); await h.respond(0, status()); await h.respond(1, snapshot());
  const first = h.render().refreshLibrary(); assert.equal(h.calls[2].path, '/library/refresh');
  h.render().refresh(); assert.deepEqual(h.calls.slice(3).map(c => c.path), ['/status', '/library']);
  await h.render().refreshLibrary(); // A new terminal transfer queues behind the pending scan.
  await h.respond(2, { ...snapshot(), state: 'scanning' }); await first;
  await h.respond(3, status()); await h.respond(4, snapshot()); // This old read still says complete.
  assert.equal(h.render().library.state, 'scanning');
  assert.equal(h.calls.filter(c => c.path === '/library/refresh').length, 1, 'the old completed scan must not drain the queue');
  assert.equal(await h.tick(), 0); await h.respond(5, status()); await h.respond(6, { ...snapshot(), state: 'scanning' });
  assert.equal(h.calls.filter(c => c.path === '/library/refresh').length, 1);
  assert.equal(await h.tick(), 2500); await h.respond(7, status()); await h.respond(8, snapshot());
  assert.equal(h.calls[9].path, '/library/refresh');
  await h.respond(9, { ...snapshot(), state: 'scanning' });
  await h.respond(10, status()); await h.respond(11, snapshot());
  await h.tick(); await h.respond(12, status()); await h.respond(13, snapshot());
  assert.equal(h.calls.filter(c => c.path === '/library/refresh').length, 2, 'exactly the initial and trailing scans were requested'); h.dispose();
});

test('local transport sends no cookies, bounds streamed bytes, and cancels a stalled body', async () => {
  const previous = globalThis.fetch; let options;
  try {
    globalThis.fetch = async (_url, init) => { options = init; return Response.json(status()); };
    const controller = new AbortController(); await client.localDownloadRequest('/status', controller.signal);
    assert.equal(options.credentials, 'omit'); assert.equal(options.cache, 'no-store');
    globalThis.fetch = async (_url, init) => { options = init; return Response.json({ cancelling: true }); };
    await client.localDownloadRequest('/cancel', controller.signal, { id: 'a'.repeat(32) }, status().sessionToken);
    assert.equal(options.headers['X-KFM-Session'], status().sessionToken);
    globalThis.fetch = async () => new Response('x'.repeat(256001));
    await assert.rejects(client.localDownloadRequest('/library', controller.signal));
    let cancelled = false; globalThis.fetch = async () => new Response(new ReadableStream({ cancel() { cancelled = true; } }));
    const aborted = new AbortController(), pending = client.localDownloadRequest('/library', aborted.signal); await settle(); aborted.abort(); await assert.rejects(pending); assert.equal(cancelled, true);
  } finally { globalThis.fetch = previous; }
});

test('job progress counts files, shows the byte cap separately, and keeps unknown totals indeterminate', async () => {
  const h = await componentHarness('app/download-job.tsx', { './earth-engine-data': { EARTH_ENGINE_DATASETS: [{ id: 'ee-cdl', title: 'Cropland' }] }, './local-download-client': client, './downloads/workspace.module.css': css });
  let cancelled = 0;
  const props = { job: job(), active: true, connected: true, cancelling: false, onCancel: () => cancelled++ };
  let tree = h.render(h.exports.DownloadJob, props); const unknown = findNode(tree, node => node.type === 'progress'); assert.equal(unknown.props.value, undefined); assert.equal(unknown.props.max, undefined);
  assert.match(JSON.stringify(tree), /Selected maximum/); assert.match(JSON.stringify(tree), /8.00 GB/);
  findNode(tree, node => node.type === 'button').props.onClick(); assert.equal(cancelled, 1);
  tree = h.render(h.exports.DownloadJob, { ...props, job: job({ completed: 2, total: 9 }), cancelling: true }); const known = findNode(tree, node => node.type === 'progress'); assert.equal(known.props.max, 9); assert.equal(known.props.value, 2);
  assert.equal(findNode(tree, node => node.type === 'button').props['aria-busy'], true);
  tree = h.render(h.exports.DownloadJob, { ...props, job: job({ state: 'failed', bytes: 500 }) }); assert.match(JSON.stringify(tree), /captured files remain/); h.dispose();
});

test('library view pages stored collections and keeps unknown totals separate from map approval', async () => {
  let state = { status: status(), library: snapshot(), connection: 'connected', libraryError: null, announcement: '', actionNotice: '', lastChecked: '2026-10-08T12:00:00Z', refreshLibrary() {}, refreshingLibrary: false };
  const reviewed = { manifests: [], loading: false, error: null, reload() {} };
  const h = await componentHarness('app/download-library.tsx', {
    'next/link': { default: 'a' }, './earth-engine-context': { earthEngineSetYear: () => 2024 },
    './earth-engine-data': { EARTH_ENGINE_DATASETS: [] }, './local-download-client': client,
    './downloads/workspace.module.css': css,
  });
  const render = () => { const tree = h.render(h.exports.default, { downloads: state, reviewed }); h.commit(); return tree; };
  let tree = render(); const list = () => findNode(tree, node => node.type === 'ul' && node.props.className === 'collections');
  assert.equal(nodes(list(), node => node.type === 'li').length, 10); assert.match(JSON.stringify(tree), /No approved display periods/);
  const pages = findNode(tree, node => node.props?.['aria-label'] === 'Collection pages'); findNode(pages, node => node.type === 'button' && node.props.children === 'Next').props.onClick(); tree = render(); assert.match(JSON.stringify(list()), /Source 11/);
  findNode(tree, node => node.type === 'input' && node.props.type === 'search').props.onChange({ target: { value: 'Source 40' } }); tree = render(); assert.equal(nodes(list(), node => node.type === 'li').length, 1); assert.match(JSON.stringify(list()), /Source 40/);
  state = { ...state, library: library() }; tree = render(); assert.match(JSON.stringify(tree), /Unknown/); assert.match(JSON.stringify(tree), /first scan finishes/); const progress = findNode(tree, node => node.type === 'progress'); assert.equal(progress.props.value, undefined);
  state = { ...state, library: { ...snapshot(), state: 'failed', error: 'LIBRARY_SCAN_CHANGED' } }; tree = render(); assert.match(JSON.stringify(tree), /Previous completed scan/); assert.match(JSON.stringify(tree), /82.0 kB/); h.dispose();
});
