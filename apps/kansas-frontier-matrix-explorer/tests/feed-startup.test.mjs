import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { stripTypeScriptTypes } from 'node:module';
const source = await readFile(new URL('../app/feed-startup.ts', import.meta.url), 'utf8');
const { resolveFeedStartup: resolve } = await import(`data:text/javascript;base64,${Buffer.from(stripTypeScriptTypes(source)).toString('base64')}`);
const fixtureBytes = await readFile(new URL('../fixtures/feed-startup.synthetic.json', import.meta.url));
const fixture = JSON.parse(fixtureBytes);
const now = '2026-09-22T12:00:00.000Z';
const artifact = (overrides = {}) => ({ id: 'live:1', sourceId: 'usgs-earthquakes', scopeKey: 'ks:quakes:30d',
  kind: 'live', dataRole: 'observation', sha256: 'a'.repeat(64), validation: 'passed', displayAllowed: true,
  dataTime: '2026-09-22T11:50:00.000Z', retrievedAt: '2026-09-22T11:55:00.000Z',
  freshnessAnchor: '2026-09-22T11:50:00.000Z', validUntil: '2026-09-22T12:10:00.000Z',
  featureCount: 2, ...overrides });
const demo = artifact({ id: fixture.properties.artifactId, sourceId: 'synthetic:starter', scopeKey: 'demo:kansas',
  kind: 'synthetic', dataRole: 'synthetic', sha256: createHash('sha256').update(fixtureBytes).digest('hex'),
  dataTime: fixture.properties.dataTime, retrievedAt: null, freshnessAnchor: null, validUntil: null });
const snapshot = (overrides = {}) => artifact({ id: 'snapshot:1', kind: 'snapshot', ...overrides });
const input = (overrides = {}) => ({ now, sourceId: 'usgs-earthquakes', scopeKey: 'ks:quakes:30d',
  direction: 'auto', enabled: true, access: 'allowed', timeSupported: true, zoomSupported: true,
  phase: 'idle', demo, ...overrides });

test('no direction starts a separately labelled synthetic demo, never a healthy live feed', () => {
  const r = resolve(input());
  assert.equal(r.display, 'SYNTHETIC_DEMO'); assert.equal(r.artifact.sourceId, 'synthetic:starter');
  assert.equal(r.liveAvailable, false); assert.equal(r.renderedLive, false); assert.match(r.disclosure, /not observations/);
});
test('loading can retain the demonstration without concealing loading', () => {
  const r = resolve(input({ phase: 'loading' })); assert.equal(r.phase, 'loading'); assert.equal(r.display, 'SYNTHETIC_DEMO');
});
test('fallback keeps the original finite connection failure', () => {
  const r = resolve(input({ phase: 'error', failureCode: 'TIMEOUT' })); assert.equal(r.connectionFailure, 'TIMEOUT'); assert.equal(r.phase, 'error');
});
test('arbitrary error text is never projected into diagnostics', () => {
  const r = resolve(input({ phase: 'error', failureCode: 'https://private.invalid/?token=secret' }));
  assert.equal(r.connectionFailure, 'UPSTREAM_ERROR'); assert.doesNotMatch(JSON.stringify(r), /token|secret|private/);
});
test('eligible real snapshot precedes demo but never becomes live', () => {
  const s = snapshot(), r = resolve(input({ snapshots: [s] }));
  assert.equal(r.display, 'SNAPSHOT'); assert.equal(r.artifact, s); assert.equal(r.liveAvailable, false);
});
test('source freshness rather than a new retrieval timestamp orders snapshots', () => {
  const old = snapshot({ id: 'snapshot:old', freshnessAnchor: '2026-09-22T10:00:00.000Z', retrievedAt: now });
  const current = snapshot(); assert.equal(resolve(input({ snapshots: [old, current] })).artifact.id, current.id);
});
test('expired snapshot is explicitly stale and not live', () => {
  const r = resolve(input({ snapshots: [snapshot({ validUntil: '2026-09-22T11:59:00.000Z' })] }));
  assert.equal(r.display, 'STALE_SNAPSHOT'); assert.equal(r.liveAvailable, false);
});
test('prefer a fresh eligible snapshot over an expired snapshot', () => {
  const stale = snapshot({ id: 'snapshot:stale', validUntil: '2026-09-22T11:59:00.000Z' });
  const fresh = snapshot({ id: 'snapshot:fresh', freshnessAnchor: '2026-09-22T11:45:00.000Z' });
  assert.equal(resolve(input({ snapshots: [stale, fresh] })).artifact.id, fresh.id);
});
for (const [label, patch] of [
  ['wrong source', { sourceId: 'nws-alerts' }], ['wrong AOI/time/product scope', { scopeKey: 'elsewhere' }],
  ['failed payload validation', { validation: 'failed' }], ['missing display permission', { displayAllowed: false }],
  ['bad digest', { sha256: 'not-a-digest' }], ['future retrieval', { retrievedAt: '2026-09-22T12:01:00.000Z' }],
  ['invalid calendar date', { dataTime: '2026-02-30T00:00:00.000Z' }],
  ['unbounded feature count', { featureCount: 100_001 }], ['negative feature count', { featureCount: -1 }],
  ['source timestamp after retrieval', { freshnessAnchor: now }],
]) test(`reject snapshot with ${label}`, () => assert.equal(resolve(input({ snapshots: [snapshot(patch)] })).display, 'SYNTHETIC_DEMO'));
for (const access of ['held', 'restricted', 'denied']) test(`${access} cannot be bypassed by fallback`, () => {
  const r = resolve(input({ access, snapshots: [snapshot()] })); assert.equal(r.display, 'NONE'); assert.equal(r.reason, 'ACCESS_BLOCKED');
});
for (const [field, reason] of [['enabled', 'DISABLED'], ['timeSupported', 'OUTSIDE_SELECTED_TIME'], ['zoomSupported', 'OUTSIDE_SUPPORTED_ZOOM']]) {
  test(`${field} remains distinct from a network failure`, () => {
    const r = resolve(input({ [field]: false })); assert.equal(r.display, 'NONE'); assert.equal(r.reason, reason);
  });
}
test('validated empty result beats prior populated snapshots and demo; never all-clear', () => {
  const r = resolve(input({ phase: 'empty', live: artifact({ featureCount: 0 }), snapshots: [snapshot()] }));
  assert.equal(r.display, 'LIVE_EMPTY'); assert.equal(r.liveAvailable, true); assert.equal(r.renderedLive, false);
  assert.match(r.disclosure, /Not an all-clear/);
});
test('current payload without matching renderer proof cannot report rendered-live', () => {
  const r = resolve(input({ phase: 'ready', live: artifact() })); assert.equal(r.display, 'LIVE'); assert.equal(r.renderedLive, false);
});
test('rendered-live requires the exact displayed artifact and scope', () => {
  const r = resolve(input({ phase: 'ready', live: artifact(), rendererState: 'rendered', renderedArtifactId: 'live:1', renderedScopeKey: 'ks:quakes:30d' }));
  assert.equal(r.renderedLive, true);
});
for (const patch of [{ renderedArtifactId: 'live:old', renderedScopeKey: 'ks:quakes:30d' },
  { renderedArtifactId: 'live:1', renderedScopeKey: 'different:time' }]) {
  test(`old renderer proof is ignored: ${JSON.stringify(patch)}`, () => {
    assert.equal(resolve(input({ phase: 'ready', live: artifact(), rendererState: 'rendered', ...patch })).renderedLive, false);
  });
}
test('partial response stays partial instead of turning into a complete demo', () => {
  const r = resolve(input({ phase: 'partial', live: artifact() })); assert.equal(r.display, 'LIVE_PARTIAL'); assert.equal(r.liveAvailable, false);
});
test('successful but stale source is not refreshed merely by retrieval', () => {
  const r = resolve(input({ phase: 'ready', live: artifact({ validUntil: '2026-09-22T11:59:00.000Z' }) }));
  assert.equal(r.display, 'LIVE_STALE'); assert.equal(r.liveAvailable, false);
});
test('explicit live request cannot silently become snapshot or demo', () => {
  const r = resolve(input({ direction: 'live', phase: 'error', snapshots: [snapshot()] })); assert.equal(r.display, 'NONE');
});
test('missing explicit historical selection never becomes present-day data', () => {
  const r = resolve(input({ direction: 'history', phase: 'ready', live: artifact() })); assert.equal(r.reason, 'SELECTED_HISTORY_UNAVAILABLE');
});
test('matching explicit history retains its original data time', () => {
  const h = artifact({ id: 'history:1', kind: 'historical', dataTime: '2010-01-01T00:00:00.000Z', freshnessAnchor: null, validUntil: null });
  const r = resolve(input({ direction: 'history', history: h })); assert.equal(r.display, 'HISTORICAL'); assert.equal(r.artifact.dataTime, h.dataTime);
});
test('explicit demo remains demo even if a live response is available', () => {
  assert.equal(resolve(input({ direction: 'demo', phase: 'ready', live: artifact() })).display, 'SYNTHETIC_DEMO');
});
test('history is not accepted as an auto snapshot', () => {
  assert.equal(resolve(input({ snapshots: [snapshot({ kind: 'historical' })] })).display, 'SYNTHETIC_DEMO');
});
test('more than 32 fallback candidates fails closed', () => {
  assert.equal(resolve(input({ snapshots: Array(33).fill(snapshot()) })).reason, 'SNAPSHOT_LIMIT');
});
for (const [phase, featureCount] of [['ready', 0], ['empty', 1]]) {
  test(`${phase} with inconsistent count becomes invalid response, not fresh-empty`, () => {
    const r = resolve(input({ phase, live: artifact({ featureCount }) }));
    assert.equal(r.phase, 'error'); assert.equal(r.connectionFailure, 'INVALID_LIVE_RESULT');
  });
}
test('invalid clock and invalid opaque scope fail closed', () => {
  assert.equal(resolve(input({ now: 'tomorrow' })).reason, 'INVALID_CLOCK');
  assert.equal(resolve(input({ scopeKey: 'https://host.invalid/private' })).reason, 'INVALID_SCOPE');
});
test('invalid or absent demo does not create fictitious data', () => {
  assert.equal(resolve(input({ demo: undefined })).display, 'NONE');
  assert.equal(resolve(input({ demo: { ...demo, validation: 'failed' } })).display, 'NONE');
});
test('recovery replaces demo with real data without mutating selection or cache', () => {
  const snapshots = Object.freeze([Object.freeze(snapshot())]);
  const initial = Object.freeze(input({ snapshots }));
  resolve(initial);
  const r = resolve({ ...initial, phase: 'ready', live: artifact() });
  assert.equal(r.display, 'LIVE'); assert.equal(initial.phase, 'idle'); assert.equal(snapshots[0].kind, 'snapshot');
});
test('bundled baseline is deterministic synthetic geometry, not measured hazards', () => {
  assert.equal(fixture.properties.synthetic, true); assert.equal(fixture.properties.retrievedAt, null);
  assert.equal(fixture.features.length, 2);
  for (const feature of fixture.features) { assert.equal(feature.properties.synthetic, true); assert.match(feature.properties.label, /SYNTHETIC/); }
  const ring = fixture.features[1].geometry.coordinates[0]; assert.deepEqual(ring[0], ring.at(-1));
  assert.doesNotMatch(fixtureBytes.toString(), /"(?:magnitude|discharge|reflectivity|elevation|smokeDensity)"/);
});

test('missing runtime adapter is preserved as API_NOT_CONFIGURED', () => {
  assert.equal(resolve(input({ phase: 'error', failureCode: 'API_NOT_CONFIGURED' })).connectionFailure, 'API_NOT_CONFIGURED');
});
test('forecast valid time can be future but its original role remains visible', () => {
  const r = resolve(input({ phase: 'ready', live: artifact({ dataRole: 'forecast', dataTime: '2026-09-23T00:00:00.000Z' }) }));
  assert.equal(r.display, 'LIVE'); assert.equal(r.artifact.dataRole, 'forecast'); assert.match(r.disclosure, /forecast/);
});
test('synthetic and real artifact roles cannot be interchanged', () => {
  assert.equal(resolve(input({ demo: { ...demo, dataRole: 'observation' } })).display, 'NONE');
  assert.equal(resolve(input({ snapshots: [snapshot({ dataRole: 'synthetic' })] })).display, 'SYNTHETIC_DEMO');
});

for (const rendererState of ['unverified', 'loading', 'error', 'unavailable']) {
  test(`retained artifact identity does not mask renderer ${rendererState}`, () => {
    const r = resolve(input({ phase: 'ready', live: artifact(), rendererState,
      renderedArtifactId: 'live:1', renderedScopeKey: 'ks:quakes:30d' }));
    assert.equal(r.liveAvailable, true); assert.equal(r.renderedLive, false); assert.equal(r.rendererState, rendererState);
  });
}
