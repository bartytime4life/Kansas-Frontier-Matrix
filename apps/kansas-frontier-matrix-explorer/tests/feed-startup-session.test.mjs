import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { stripTypeScriptTypes } from 'node:module';
const selectorSource = await readFile(new URL('../app/feed-startup.ts', import.meta.url), 'utf8');
const selectorUrl = `data:text/javascript;base64,${Buffer.from(stripTypeScriptTypes(selectorSource)).toString('base64')}`;
const sessionSource = (await readFile(new URL('../app/feed-startup-session.mjs', import.meta.url), 'utf8'))
  .replace("'./feed-startup.ts'", JSON.stringify(selectorUrl));
const { createFeedStartupSession } = await import(`data:text/javascript;base64,${Buffer.from(sessionSource).toString('base64')}`);
import { readBundledStartupDemo } from '../app/feed-startup-demo.mjs';
import { probeContextConnections } from '../app/context-connection-probe.mjs';

const raw = await readFile(new URL('../fixtures/feed-startup.synthetic.json', import.meta.url), 'utf8');
const demo = await readBundledStartupDemo(raw);
const now = '2026-09-22T12:00:00.000Z';
const artifact = (overrides = {}) => ({ id: 'live:one', sourceId: 'usgs-earthquakes', scopeKey: 'ks:30d', kind: 'live',
  dataRole: 'observation', sha256: 'a'.repeat(64), validation: 'passed', displayAllowed: true, featureCount: 1,
  dataTime: '2026-09-22T11:00:00.000Z', retrievedAt: '2026-09-22T11:50:00.000Z',
  freshnessAnchor: '2026-09-22T11:50:00.000Z', validUntil: '2026-09-22T12:10:00.000Z', ...overrides });
const setup = (patch = {}, onChange = () => {}) => createFeedStartupSession({ now, sourceId: 'usgs-earthquakes',
  scopeKey: 'ks:30d', direction: 'auto', enabled: true, access: 'allowed', timeSupported: true, zoomSupported: true,
  phase: 'idle', demo: demo.artifact, ...patch }, { now: () => now, onChange });
const deferred = () => { let resolve; const promise = new Promise((r) => { resolve = r; }); return { promise, resolve }; };

test('construction is no-I/O and uses the verified bundled synthetic artifact', () => {
  const session = setup(); assert.equal(session.snapshot().decision.display, 'SYNTHETIC_DEMO');
  assert.equal(session.snapshot().decision.liveAvailable, false); session.dispose();
});
test('all bundled metadata and geometry are immutable', () => {
  assert.ok(Object.isFrozen(demo.artifact)); assert.ok(Object.isFrozen(demo.data.features[0].geometry.coordinates));
  assert.throws(() => { demo.artifact.sourceId = 'usgs'; }, TypeError);
});
for (const [name, value] of [['whitespace drift', `${raw} `], ['identity drift', raw.replace('demo:kansas', 'live:kansas')],
  ['invalid JSON', '{'], ['oversized', 'x'.repeat(16_385)], ['not text', null]]) {
  test(`demo refuses ${name}`, async () => { await assert.rejects(readBundledStartupDemo(value), /DEMO_/); });
}
test('validated fresh result can replace demo but does not invent renderer proof', async () => {
  const session = setup(); await session.load(async () => ({ phase: 'ready', artifact: artifact() }));
  assert.equal(session.snapshot().decision.display, 'LIVE'); assert.equal(session.snapshot().decision.renderedLive, false);
  session.dispose();
});
test('valid empty stays empty instead of substituting populated geometry', async () => {
  const session = setup(); await session.load(async () => ({ phase: 'empty', artifact: artifact({ featureCount: 0 }) }));
  assert.equal(session.snapshot().decision.display, 'LIVE_EMPTY'); session.dispose();
});
test('refresh immediately invalidates any previously supplied renderer claim', async () => {
  const wait = deferred(), session = setup({ phase: 'ready', live: artifact(), rendererState: 'rendered',
    renderedArtifactId: 'live:one', renderedScopeKey: 'ks:30d' });
  assert.equal(session.snapshot().decision.renderedLive, true);
  const pending = session.load(() => wait.promise);
  assert.equal(session.snapshot().decision.renderedLive, false); session.cancel();
  assert.equal((await pending).outcome, 'SUPERSEDED'); session.dispose();
});
test('superseded same-scope response cannot overwrite a newer result', async () => {
  const old = deferred(), session = setup();
  const first = session.load(() => old.promise); await Promise.resolve();
  await session.load(async () => ({ phase: 'ready', artifact: artifact({ id: 'live:new' }) }));
  old.resolve({ phase: 'ready', artifact: artifact({ id: 'live:old' }) });
  assert.equal((await first).outcome, 'SUPERSEDED');
  assert.equal(session.snapshot().decision.artifact.id, 'live:new'); session.dispose();
});
test('A-to-B-to-A scope changes still reject the old A generation', async () => {
  const old = deferred(), session = setup(); const first = session.load(() => old.promise); await Promise.resolve();
  session.select({ scopeKey: 'ks:one-day' }); session.select({ scopeKey: 'ks:30d' });
  old.resolve({ phase: 'ready', artifact: artifact() });
  assert.equal((await first).outcome, 'SUPERSEDED'); assert.equal(session.snapshot().decision.display, 'SYNTHETIC_DEMO');
  session.dispose();
});
test('a queued reader is not invoked after an immediate change to denied', async () => {
  let calls = 0; const session = setup();
  const pending = session.load(async () => { calls++; return { phase: 'ready', artifact: artifact() }; });
  session.select({ access: 'denied' });
  assert.equal((await pending).outcome, 'SUPERSEDED'); assert.equal(calls, 0); assert.equal(session.snapshot().decision.display, 'NONE');
  session.dispose();
});
test('reader receives the original frozen scope, not a later mutable selection', async () => {
  let context; const old = deferred(), session = setup();
  const pending = session.load((c) => { context = c; return old.promise; }); await Promise.resolve();
  session.select({ scopeKey: 'changed' });
  assert.equal(context.scopeKey, 'ks:30d'); assert.ok(Object.isFrozen(context)); assert.equal(context.signal.aborted, true);
  assert.equal((await pending).outcome, 'SUPERSEDED'); session.dispose();
});
test('timeout settles even a non-cooperating injected reader', async () => {
  const session = setup(); const r = await session.load(() => new Promise(() => {}), { timeoutMs: 10 });
  assert.equal(r.outcome, 'SETTLED'); assert.equal(session.snapshot().decision.connectionFailure, 'TIMEOUT');
  assert.equal(session.snapshot().decision.display, 'SYNTHETIC_DEMO'); session.dispose();
});
test('cancel releases a pending operation and retains no accepted live payload', async () => {
  const session = setup(); const pending = session.load(() => new Promise(() => {})); await Promise.resolve(); session.cancel();
  assert.equal((await pending).outcome, 'SUPERSEDED'); assert.equal(session.snapshot().workState, 'cancelled');
  assert.equal(session.snapshot().decision.liveAvailable, false); session.dispose();
});
test('dispose suppresses all subsequent callbacks and reads', async () => {
  const changes = [], session = setup({}, (s) => changes.push(s));
  const pending = session.load(() => new Promise(() => {})); session.dispose(); const count = changes.length;
  assert.equal((await pending).outcome, 'SUPERSEDED'); assert.equal(session.select({ direction: 'live' }), false);
  assert.equal((await session.load(async () => { throw Error('must not invoke'); })).outcome, 'DISPOSED');
  assert.equal(changes.length, count);
});
for (const patch of [{ enabled: false }, { access: 'denied' }, { access: 'held' }, { access: 'restricted' },
  { timeSupported: false }, { zoomSupported: false }, { direction: 'demo' }]) {
  test(`no reader is started through blocked selection ${JSON.stringify(patch)}`, async () => {
    const session = setup(patch); let calls = 0;
    assert.equal((await session.load(async () => { calls++; })).outcome, 'NOT_REQUESTED'); assert.equal(calls, 0); session.dispose();
  });
}
test('explicit history retains original artifact time and source role', async () => {
  const session = setup({ direction: 'history' });
  await session.load(async () => ({ phase: 'ready', artifact: artifact({ kind: 'historical', id: 'history:1',
    dataTime: '2010-01-01T00:00:00.000Z', freshnessAnchor: null, validUntil: null }) }));
  assert.equal(session.snapshot().decision.display, 'HISTORICAL'); session.dispose();
});
test('history reader returning present data cannot populate selected history', async () => {
  const session = setup({ direction: 'history' }); await session.load(async () => ({ phase: 'ready', artifact: artifact() }));
  assert.equal(session.snapshot().decision.display, 'NONE'); session.dispose();
});
test('observations after retrieval are rejected; forecast roles remain explicit', async () => {
  for (const dataRole of ['observation', 'reference', 'forecast']) {
    const session = setup(); await session.load(async () => ({ phase: 'ready', artifact: artifact({ dataRole, dataTime: '2026-09-23T00:00:00.000Z' }) }));
    assert.equal(session.snapshot().decision.display, dataRole === 'forecast' ? 'LIVE' : 'SYNTHETIC_DEMO'); session.dispose();
  }
});
test('transport success without provider validation is visibly unverified, never live', async () => {
  const session = setup(); await session.load(async () => ({ phase: 'error', failureCode: 'PAYLOAD_UNVERIFIED' }));
  assert.equal(session.snapshot().decision.connectionFailure, 'PAYLOAD_UNVERIFIED'); assert.equal(session.snapshot().decision.liveAvailable, false);
  session.dispose();
});
test('raw thrown messages do not leak to observer state', async () => {
  const session = setup(); await session.load(async () => { throw Error('PRIVATE_TOKEN'); });
  assert.doesNotMatch(JSON.stringify(session.snapshot()), /PRIVATE_TOKEN/); session.dispose();
});
test('caller mutation cannot change accepted snapshot metadata', async () => {
  const a = artifact(), session = setup(); await session.load(async () => ({ phase: 'ready', artifact: a }));
  a.id = 'live:changed'; assert.equal(session.snapshot().decision.artifact.id, 'live:one'); session.dispose();
});
for (const timeoutMs of [0, 9, 60_001, NaN, 11.5]) {
  test(`invalid overall deadline ${timeoutMs} is refused`, async () => {
    const session = setup(); await assert.rejects(session.load(async () => {}, { timeoutMs }), /deadline/); session.dispose();
  });
}
test('pre-aborted probe sends no request, preserving unprobed raster distinctions', async () => {
  const controller = new AbortController(); controller.abort(); let calls = 0;
  const r = await probeContextConnections({ origin: 'http://127.0.0.1:5173', signal: controller.signal, fetchImpl: () => { calls++; } });
  assert.equal(calls, 0); assert.equal(r.results.filter((x) => x.status === 'CANCELLED').length, 10);
  assert.equal(r.results.filter((x) => x.status === 'NOT_PROBED_RENDERER').length, 5);
});
test('probe cancellation settles pending requests without continuing the queue', async () => {
  const controller = new AbortController(); let calls = 0;
  const pending = probeContextConnections({ origin: 'http://127.0.0.1:5173', signal: controller.signal,
    fetchImpl: () => { calls++; return new Promise(() => {}); } });
  await Promise.resolve(); controller.abort(); const r = await pending;
  assert.equal(calls, 2); assert.equal(r.results.filter((x) => x.status === 'CANCELLED').length, 10);
});
test('invalid probe signal is rejected without a network request', async () => {
  await assert.rejects(probeContextConnections({ origin: 'http://127.0.0.1:5173', signal: {}, fetchImpl: () => { throw Error('network'); } }), /signal/);
});
test('React composition mounts an isolated inspector without touching existing map state', async () => {
  const main = await readFile(new URL('../main.tsx', import.meta.url), 'utf8');
  const wrapper = await readFile(new URL('../app/feed-startup-panel.tsx', import.meta.url), 'utf8');
  const surface = await readFile(new URL('../app/feed-startup-surface.mjs', import.meta.url), 'utf8');
  assert.match(main, /!isAbout && <FeedStartupPanel \/>/);
  assert.match(wrapper, /mountFeedStartupSurface\(host, \{ fixtureText \}\)/);
  assert.match(wrapper, /surface\.dispose\(\); host\.remove\(\)/);
  assert.doesNotMatch(surface, /innerHTML|localStorage|sessionStorage|navigator\.geolocation|pushState|replaceState|setInterval|addSource|setStyle/);
});


test('uncloneable reader output fails finitely without leaking its value', async () => {
  const session = setup(); await session.load(async () => ({ phase: 'ready', artifact: () => 'SECRET' }));
  assert.equal(session.snapshot().decision.connectionFailure, 'INVALID_RESPONSE');
  assert.doesNotMatch(JSON.stringify(session.snapshot()), /SECRET/); session.dispose();
});
test('disposed snapshot exposes no live or synthetic artifact', async () => {
  const session = setup(); await session.load(async () => ({ phase: 'ready', artifact: artifact() }));
  session.dispose(); assert.equal(session.snapshot().decision.display, 'NONE');
  assert.equal(session.snapshot().decision.artifact, null); assert.equal(session.snapshot().decision.liveAvailable, false);
});
