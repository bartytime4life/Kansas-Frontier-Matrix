import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, settle } from './component-harness.mjs';
const compile = async path => ts.transpileModule(await readFile(path, 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const url = source => `data:text/javascript;base64,${Buffer.from(source).toString('base64')}`;
const modelUrl = url(await compile('app/public-map-catalog.ts'));
const model = await import(modelUrl);
const activity = await import(url(await compile('app/download-activity.ts')));
const polling = await import(url(await compile('app/download-polling.ts')));
const bounded = url(await compile('app/bounded-json.ts'));
const client = await import(url((await compile('app/public-map-client.ts')).replace('"./public-map-catalog"', JSON.stringify(modelUrl)).replace('"./bounded-json"', JSON.stringify(bounded))));
const seed = JSON.parse(await readFile('app/public-map-catalog.json', 'utf8'));
const asset = seed.records.flatMap(r => r.assets).find(a => a.id === 'kgs-m118-pdf');
const deferred = () => { let resolve, reject; const promise = new Promise((yes, no) => { resolve = yes; reject = no; }); return { promise, resolve, reject }; };
const job = patch => ({ id: '1'.repeat(32), assetId: asset.id, title: 'Geology map', state: 'downloading', bytes: 20, expectedBytes: 100, maxBytes: 500,
  sha256: null, destination: '/data/candidate', reason: null, mapReady: false, createdAt: '2026-10-08T12:00:00Z', updatedAt: '2026-10-08T12:00:01Z', ...patch });
const status = patch => ({ schema: 'kfm-public-map-download-control/v1', sessionToken: 'p'.repeat(43), jobs: [], active: null, limitBytes: 500_000_000_000, refresh: { state: 'idle' }, ...patch });
async function mapHarness({ origin = 'https://hosted.example', options = {} } = {}) {
  const calls = [], timers = new Map(), listeners = new Map(); let nextTimer = 0, nextId = 0, currentOptions = options;
  const document = { visibilityState: 'visible', addEventListener: (n, f) => listeners.set(n, f), removeEventListener: (n, f) => { if (listeners.get(n) === f) listeners.delete(n); } };
  const environment = { document, setTimeout: (callback, delay) => { timers.set(++nextTimer, { callback, delay }); return nextTimer; }, clearTimeout: id => timers.delete(id) };
  const h = await componentHarness('app/use-public-map-downloads.ts', {
    './public-map-catalog.json': { default: seed }, './public-map-catalog': model,
    './public-map-client': { ...client, publicMapRequest: (path, signal, payload, token) => { const d = deferred(); calls.push({ path, signal, payload, token, ...d }); return d.promise; } },
    './local-download-client': { automaticLocalConnection: origin => origin === 'http://127.0.0.1:4173' },
    './download-activity': activity, './download-polling': { startDownloadPolling: run => polling.startDownloadPolling(run, environment) },
  }, { queueMicrotask, window: { location: { origin } }, crypto: { randomUUID: () => (++nextId).toString(16).padStart(32, '0') } }, '\nexport function Probe(options){return usePublicMapDownloads(options);}');
  const render = () => { const value = h.render(h.exports.Probe, currentOptions); h.commit(); return value; };
  const respond = async (index, body, code = 200) => { calls[index].resolve({ response: { ok: code >= 200 && code < 300, status: code }, body }); await settle(); return render(); };
  const tick = async () => { assert.equal(timers.size, 1); const [id, task] = [...timers][0]; timers.delete(id); task.callback(); await settle(); return task.delay; };
  render(); await settle(); render();
  const connect = async (initial = status()) => { if (!calls.length) { render().connect(); render(); } await respond(0, initial); await respond(1, seed); return render(); };
  return { ...h, render, connect, respond, calls, timers, tick, setOptions: value => { currentOptions = value; return render(); }, visibility: value => { document.visibilityState = value; listeners.get('visibilitychange')?.(); } };
}

test('activity keeps provider identity and native progress; caps never become percentage totals', () => {
  const maps = status({ active: '1'.repeat(32), jobs: [job({ expectedBytes: null, bytes: 300, maxBytes: 500 })] });
  const ee = { active: null, jobs: [{ id: '1'.repeat(32), state: 'cancelled', createdAt: '2026-10-08T13:00:00Z', bytes: 100,
    selection: { dataset: 'ee-cdl', year: 2023, maxBytes: 1e9 }, completed: 2, total: 10 }] };
  const rows = activity.normalizeDownloadActivity(ee, maps);
  assert.equal(rows[0].kind, 'public-map'); assert.notEqual(rows[0].key, rows[1].key);
  assert.deepEqual(rows[0].progress, { unit: 'unknown', value: null, total: null });
  assert.deepEqual(rows[1].progress, { unit: 'files', value: 2, total: 10 });
  assert.equal(rows[1].bytes, 100, 'stopped captured bytes remain visible');
});

test('terminal observation ignores history and refreshes once for newly finished or between-poll jobs', () => {
  let observed = activity.observeDownloadTransitions(null, [job({ state: 'downloaded' })]);
  assert.equal(observed.terminal.length, 0);
  observed = activity.observeDownloadTransitions(observed.next, [job({ state: 'downloaded' }), job({ id: '2'.repeat(32), state: 'downloading' })]);
  assert.equal(observed.terminal.length, 0);
  observed = activity.observeDownloadTransitions(observed.next, [job({ state: 'downloaded' }), job({ id: '2'.repeat(32), state: 'cancelled' })]);
  assert.equal(observed.terminal.length, 1);
  observed = activity.observeDownloadTransitions(observed.next, [job({ id: '2'.repeat(32), state: 'interrupted' }), job({ id: '3'.repeat(32), state: 'failed' })]);
  assert.deepEqual(observed.terminal.map(j => j.id), ['3'.repeat(32)]);
});

test('public controller reads catalog once, polls active2.5s/idle15s and announces only transitions', async () => {
  let refreshes = 0;
  const h = await mapHarness({ options: { onTransferTerminal: () => refreshes++ } }); assert.equal(h.calls.length, 0);
  const running = status({ active: '1'.repeat(32), jobs: [job()] });
  await h.connect(running); assert.deepEqual(h.calls.map(c => c.path), ['/status', '/catalog']);
  const initial = h.render().announcement;
  assert.equal(await h.tick(), 2500); await h.respond(2, status({ ...running, jobs: [job({ bytes: 50 })] }));
  assert.equal(h.render().announcement, initial); assert.equal(h.calls.filter(c => c.path === '/catalog').length, 1);
  await h.tick(); const done = status({ jobs: [job({ state: 'cancelled' })] }); await h.respond(3, done);
  assert.equal(refreshes, 1); assert.match(h.render().announcement, /Cancelled/);
  assert.equal(await h.tick(), 15000); await h.respond(4, done); assert.equal(refreshes, 1);
  assert.equal(h.calls.filter(c => c.path === '/catalog').length, 1); h.dispose();
});

test('hidden requests abort, foreground return waits without overlap, disposed replies are ignored', async () => {
  const h = await mapHarness({ origin: 'http://127.0.0.1:4173' }); assert.equal(h.calls.length, 1);
  h.visibility('hidden'); assert.equal(h.calls[0].signal.aborted, true); h.visibility('visible'); assert.equal(h.calls.length, 1);
  await h.respond(0, status()); assert.equal(h.render().status, null); assert.equal(await h.tick(), 0);
  await h.respond(1, status()); await h.respond(2, seed); assert.equal(h.render().connection, 'connected');
  h.visibility('hidden'); assert.equal(h.timers.size, 0); h.visibility('visible'); assert.equal(h.calls.length, 4);
  h.dispose(); assert.equal(h.calls[3].signal.aborted, true); await h.respond(3, status({ refresh: { state: 'failed' } }));
  assert.equal(h.render().status.refresh.state, 'idle'); assert.equal(h.timers.size, 0);
});

test('completed catalog refresh causes one read; failures preserve catalog and connection truth', async () => {
  const h = await mapHarness(); await h.connect();
  const request = h.render().refreshCatalog(); assert.equal(h.calls[2].path, '/refresh'); assert.equal(h.calls[2].token, status().sessionToken);
  await h.respond(2, { state: 'running' }); await request; assert.equal(h.calls[3].path, '/status');
  await h.respond(3, status({ refresh: { state: 'running' } })); assert.equal(await h.tick(), 2500);
  await h.respond(4, status({ refresh: { state: 'complete' } })); assert.equal(h.calls[5].path, '/catalog');
  await h.respond(5, {}, 503); assert.match(h.render().catalogError, /unavailable/); assert.equal(h.render().catalog.records.length, seed.records.length);
  await h.tick(); await h.respond(6, status({ refresh: { state: 'complete' } })); assert.equal(h.calls[7].path, '/catalog', 'failed catalogs retry on the next healthy poll');
  await h.respond(7, seed); assert.equal(h.render().catalogError, null);
  await h.tick(); await h.respond(8, {}, 503); assert.equal(h.render().connection, 'unavailable'); assert.ok(h.render().status); h.dispose();
});

test('ambiguous start retains its ID, selection changes release it, external busy blocks and native cancellation uses public token', async () => {
  const h = await mapHarness(); await h.connect(); h.render().selectAsset(asset.id);
  h.setOptions({ blockedByOtherDownload: true }); await h.render().startDownload(asset, 40_000_000); assert.equal(h.calls.length, 2);
  h.setOptions({ blockedByOtherDownload: false }); const first = h.render().startDownload(asset, 40_000_000);
  assert.equal(h.calls[2].path, '/downloads'); const id = h.calls[2].payload.requestId;
  h.calls[2].reject(new Error('lost reply')); await first; await settle(); h.render();
  await h.respond(3, status());
  const retry = h.render().startDownload(asset, 40_000_000); assert.equal(h.calls[4].payload.requestId, id);
  h.render().selectAsset('another-asset'); h.render().selectAsset(asset.id);
  await h.respond(4, { id, assetId: asset.id, maxBytes: 40_000_000, mapReady: false }); await retry;
  assert.equal(h.render().notice, '', 'old selection cannot overwrite a new selection notice'); await h.respond(5, status());
  const next = h.render().startDownload(asset, 40_000_000); assert.notEqual(h.calls[6].payload.requestId, id);
  const nextId = h.calls[6].payload.requestId;
  await h.respond(6, { id: nextId, assetId: asset.id, maxBytes: 40_000_000, mapReady: false }); await next;
  await h.respond(7, status({ active: nextId, jobs: [job({ id: nextId, maxBytes: 40_000_000 })] }));
  const cancel = h.render().cancelJob(nextId); assert.equal(h.calls[8].path, '/cancel'); assert.equal(h.calls[8].payload.id, nextId); assert.equal(h.calls[8].token, status().sessionToken);
  await h.respond(8, { cancelled: true }); await cancel; assert.match(h.render().notice, /Cancellation requested/); h.dispose();
});

test('accepted public start keeps shared busy through a delayed pre-start status and waits for a fresh read', async () => {
  const h = await mapHarness(); await h.connect(); h.render().selectAsset(asset.id);
  await h.tick(); assert.equal(h.calls[2].path, '/status');
  const request = h.render().startDownload(asset, 40_000_000), id = h.calls[3].payload.requestId;
  await h.respond(3, { id, assetId: asset.id, maxBytes: 40_000_000, mapReady: false }); await request;
  assert.equal(h.render().busy, 'download');
  await h.respond(2, status()); assert.equal(h.render().busy, 'download', 'an older empty status cannot release the accepted request lock');
  assert.equal(await h.tick(), 0);
  await h.respond(4, status({ active: id, jobs: [job({ id, maxBytes: 40_000_000 })] }));
  assert.equal(h.render().busy, null); assert.equal(h.render().status.active, id); h.dispose();
});

test('default browser polling preserves the native Window timer receiver across repeat, hide, resume and disposal', async () => {
  const timers = new Map(), listeners = new Map(); let nextTimer = 0, rounds = 0, cleared = 0;
  const nativeWindow = {
    setTimeout(callback, delay) {
      assert.equal(this, nativeWindow, 'native setTimeout requires its Window receiver');
      timers.set(++nextTimer, { callback, delay }); return nextTimer;
    },
    clearTimeout(id) {
      assert.equal(this, nativeWindow, 'native clearTimeout requires its Window receiver');
      cleared++; timers.delete(id);
    },
  };
  const document = { visibilityState: 'visible', addEventListener: (name, fn) => listeners.set(name, fn), removeEventListener: name => listeners.delete(name) };
  const h = await componentHarness('app/download-polling.ts', {}, {
    window: nativeWindow, document, setTimeout: nativeWindow.setTimeout, clearTimeout: nativeWindow.clearTimeout,
  });
  const control = h.exports.startDownloadPolling(async () => ++rounds < 2); // Exercise the production default environment.
  await settle(); assert.equal(rounds, 1); assert.equal(timers.size, 1);
  let [id, task] = [...timers][0]; assert.equal(task.delay, 2500); timers.delete(id); task.callback(); await settle();
  assert.equal(rounds, 2); assert.equal(timers.size, 1); assert.equal([...timers][0][1].delay, 15000);
  document.visibilityState = 'hidden'; listeners.get('visibilitychange')(); assert.equal(timers.size, 0);
  document.visibilityState = 'visible'; listeners.get('visibilitychange')(); await settle(); assert.equal(rounds, 3); assert.equal(timers.size, 1);
  control.refresh(); await settle(); assert.equal(rounds, 4); assert.equal(timers.size, 1);
  control.dispose(); assert.equal(timers.size, 0); assert.equal(listeners.size, 0); assert.ok(cleared >= 3); h.dispose();
});

test('a Storm Events queue sends verified files under one maximum, blocks single starts and cancels the rest', async () => {
  const storm = year => ({ id: `publisher-noaa-storm-events-${year}-details`, title: `StormEvents_details-ftp_v1.0_d${year}_c20250401.csv.gz`, format: 'GZIP',
    url: `https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d${year}_c20250401.csv.gz`, expectedBytes: null, kind: 'download', availability: 'verified', checkedAt: '2026-10-09' });
  const h = await mapHarness(); await h.connect();
  const assets = [storm(2023), storm(2024)], maximum = 80 * 1_048_576;
  const queued = h.render().startQueue(assets, maximum);
  assert.equal(h.calls[2].path, '/queue'); const batch = h.calls[2].payload.requestId;
  assert.deepEqual(JSON.parse(JSON.stringify(h.calls[2].payload)), { requestId: batch, assetIds: assets.map(a => a.id), maxBytes: maximum });
  await h.respond(2, { batchId: batch, jobs: 2, queued: 1, active: '1'.repeat(32), mapReady: false }); await queued;
  assert.match(h.render().notice, /2 files queued/);
  await h.respond(3, status({ active: '1'.repeat(32), queued: 1, jobs: [job({ assetId: assets[0].id, expectedBytes: null })] }));
  assert.equal(h.render().status.queued, 1);
  await h.render().startDownload(asset, 40_000_000); assert.equal(h.calls.length, 4, 'a running queue blocks a single start');
  const cancel = h.render().cancelQueue(); assert.equal(h.calls[4].path, '/queue/cancel'); assert.equal(JSON.stringify(h.calls[4].payload), '{}'); assert.equal(h.calls[4].token, status().sessionToken);
  await h.respond(4, { cancelledQueued: 1, cancelling: '1'.repeat(32) }); await cancel; assert.match(h.render().notice, /Queued files cancelled/); h.dispose();
});

test('a queued count is valid only alongside a running job', () => {
  assert.ok(client.parsePublicMapStatus(status({ active: '1'.repeat(32), queued: 3, jobs: [job()] })));
  assert.ok(client.parsePublicMapStatus(status()), 'operators without a queue omit the count');
  for (const queued of [2, -1, 1.5, 301]) assert.equal(client.parsePublicMapStatus(status({ queued, ...(queued === 2 ? {} : { active: '1'.repeat(32), jobs: [job()] }) })), null);
});
