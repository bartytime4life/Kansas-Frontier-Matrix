import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, readFile, rm, lstat, symlink } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { resolve } from 'node:path';
import { DatabaseSync } from 'node:sqlite';
import { modelUrl } from '../scripts/lib/typescript-model.mjs';
import { PC_CAPTURE_IDS } from '../app/pipeline-catalog.mjs';
import { publicSourceHealth, cardSnapshot } from '../server/card-pipeline-health.mjs';
import { validateConfig } from '../scripts/pc-pipeline/config.mjs';
import { writeOperatorReport } from '../scripts/pc-pipeline/capture.mjs';
import { Journal } from '../scripts/pc-pipeline/journal.mjs';
import { journalHealth, backfillPlan } from '../scripts/pc-pipeline/health.mjs';
const model = await import(await modelUrl('app/card-pipelines.ts'));
const server = await import(await modelUrl('app/card-pipeline-server.ts'));
const now = Date.parse('2026-10-30T00:30:00Z');
const config = { format: 'kfm-pc-pipeline-config-v1', root: '/private/store', mount: '/private', storeId: 'a'.repeat(32), device: 10,
  approvalDirectory: '/private/approvals', sources: [...PC_CAPTURE_IDS], publish: false, remoteMode: 'connection-only' };

test('every real question, recipe and welcome topic has valid distinct registry bindings', () => {
  assert.equal(model.validateCardPipelines(), true);
  for (const [kind, count] of [['recipe', 6], ['topic', 22]]) assert.equal(model.CARD_PIPELINE_BINDINGS.filter(card => card.kind === kind).length, count);
  assert.deepEqual(model.PIPELINE_DEFINITIONS.filter(p => p.mode === 'pc-capture').map(p => p.id).sort(), [...PC_CAPTURE_IDS].sort());
  const ids = new Set(model.CARD_PIPELINE_BINDINGS.flatMap(card => [...card.required, ...card.optional, ...card.gaps]));
  for (const candidate of model.PIPELINE_DEFINITIONS.filter(p => p.mode === 'candidate')) assert.ok(ids.has(candidate.id), candidate.id);
  assert.ok(model.CARD_PIPELINE_BINDINGS.find(c => c.id === 'topic:sky').optional.includes('specialty:daylight'));
  assert.ok(model.CARD_PIPELINE_BINDINGS.find(c => c.id === 'topic:evidence').optional.includes('knowledge-index'));
  assert.ok(model.CARD_PIPELINE_BINDINGS.find(c => c.id === 'topic:agriculture').optional.includes('specialty:soil'));
  for (const id of ['fauna', 'flora', 'people', 'aviation', 'government', 'public-safety']) assert.ok(model.CARD_PIPELINE_BINDINGS.find(c => c.id === 'topic:' + id).gaps.length);
});
test('current category controls and earthquake support survive reconciliation', () => {
  for (const id of ['map-tool:landcover', 'map-tool:plants', 'map-tool:crops']) {
    assert.ok(model.CARD_PIPELINE_BINDINGS.find(card => card.id === 'topic:flora').optional.includes(id));
    assert.equal(model.PIPELINE_DEFINITIONS.find(source => source.id === id).mode, 'display');
  }
  assert.ok(PC_CAPTURE_IDS.includes('usgs-earthquakes'));
  assert.deepEqual(validateConfig({ ...config, sources: ['usgs-earthquakes'] }).sources, ['usgs-earthquakes']);
  assert.throws(() => validateConfig({ ...config, storagePolicy: { maxPublicationsPerTick: 99 } }), /STORAGE_POLICY_INVALID/);
});
test('v2 config selects implemented adapters and preserves v1 safety', () => {
  assert.deepEqual(validateConfig(config), config);
  const rest = { ...config }; delete rest.sources;
  const v2 = { ...rest, format: 'kfm-pc-pipeline-config-v2', pipelines: [{ sourceId: 'nws-alerts', enabled: true }, { sourceId: 'usgs-streamflow', enabled: false }] };
  assert.deepEqual(validateConfig(v2).sources, ['nws-alerts']);
  assert.deepEqual(validateConfig(validateConfig(v2)), validateConfig(v2), 'normalized v2 config must be safe to pass through existing worker interfaces');
  for (const pipelines of [[{ sourceId: 'fauna-occurrences', enabled: true }], [{ sourceId: 'nws-alerts', enabled: true, url: 'http://internal' }], [{ sourceId: 'nws-alerts', enabled: 1 }]]) assert.throws(() => validateConfig({ ...v2, pipelines }), /CONFIG_INVALID/);
  assert.throws(() => validateConfig({ ...v2, pipelines: [...v2.pipelines, v2.pipelines[0]] }), /CONFIG_INVALID/);
  assert.throws(() => validateConfig({ ...config, publish: true }), /CONNECTION_ONLY_UPLOADS_DISABLED/);
});
const product = (state = 'available') => ({ state, releaseId: 'a'.repeat(64), retrievedAt: '2026-10-30T00:20:00Z',
  approvalExpiresAt: '2026-10-31T00:00:00Z', freshness: 'current',
  privatePath: '/private/SECRET', workerSecret: 'SECRET', data: { features: [{ geometry: { coordinates: [1, 2] }, properties: { observedAt: '2026-10-29T20:00:00Z', secret: 'SECRET' } }] } });
test('public health drops payloads and keeps retrieval and measurement clocks distinct', () => {
  const health = publicSourceHealth('nws-alerts', product());
  assert.equal(health.retrievedAt, '2026-10-30T00:20:00.000Z'); assert.equal(health.observedThrough, '2026-10-29T20:00:00.000Z');
  assert.doesNotMatch(JSON.stringify(health), /SECRET|coordinates|geometry/);
  assert.equal(publicSourceHealth('nws-alerts', { ...product(), freshness: 'stale' }).state, 'stale');
  for (const state of ['withheld', 'WITHDRAWN', 'error']) assert.equal(publicSourceHealth('nws-alerts', product(state)).releaseId, null);
});
test('required failures show partial, empty differs from gaps, optional context does not promise coverage', () => {
  const card = { id: 'test', required: ['a', 'b'], optional: [], gaps: ['candidate'], demo: false };
  const snapshot = health => cardSnapshot([card], [{ id: 'a' }, { id: 'b' }], health).cards[0];
  assert.equal(snapshot([{ sourceId: 'a', state: 'available' }, { sourceId: 'b', state: 'held' }]).state, 'partial');
  assert.equal(snapshot(['a', 'b'].map(sourceId => ({ sourceId, state: 'empty' }))).state, 'empty');
  assert.equal(snapshot(['a', 'b'].map(sourceId => ({ sourceId, state: 'stale' }))).state, 'stale');
  assert.equal(cardSnapshot([{ ...card, required: [], optional: ['a'] }], [], [{ sourceId: 'a', state: 'available' }]).cards[0].state, 'coverage-gap');
  assert.equal(cardSnapshot([{ ...card, demo: true }], []).cards[0].state, 'demo');
});
test('disabled and preview environments never touch storage or announce local capture health', async () => {
  for (const environment of [{}, { KFM_PIPELINE_ENABLED: 'true', KFM_RUNTIME_ROLE: 'preview' }]) {
    const snapshot = await server.getCardPipelineSnapshot({ environment, storeFactory: () => assert.fail('no storage'), now });
    assert.equal(snapshot.cards.length, 28); assert.equal(snapshot.state, 'setup-pending');
    assert.ok(snapshot.sources.every(source => source.health.releaseId === null));
    assert.doesNotMatch(JSON.stringify(snapshot), /privatePath|workerSecret|pipeline-journal|\/run\/media/);
  }
});
test('each hosted source goes through the serving gate; failures are isolated and redacted', async () => {
  const checked = [];
  const snapshot = await server.getCardPipelineSnapshot({ environment: { KFM_PIPELINE_ENABLED: 'true', KFM_RUNTIME_ROLE: 'published' }, now,
    storeFactory: async () => ({}), readContext: async id => { checked.push(id); if (id === 'nws-alerts') throw new Error('SECRET DATABASE SETTINGS'); return product(); } });
  assert.deepEqual(checked.sort(), [...PC_CAPTURE_IDS].sort()); assert.equal(snapshot.state, 'degraded');
  assert.equal(snapshot.sources.find(p => p.id === 'nws-alerts').health.state, 'unavailable');
  assert.equal(snapshot.sources.find(p => p.id === 'usgs-streamflow').health.releaseId, 'a'.repeat(64));
  assert.doesNotMatch(JSON.stringify(snapshot), /SECRET|DATABASE SETTINGS/);
});
test('journal upgrade preserves old rows and records real new attempt and completion clocks', async t => {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-card-journal-')); t.after(() => rm(root, { recursive: true, force: true }));
  const path = resolve(root, 'pipeline-journal.sqlite');
  let db = new DatabaseSync(path);
  db.exec("CREATE TABLE jobs(source TEXT,slot INTEGER,state TEXT,attempts INTEGER,retry_at INTEGER,lease_token TEXT,lease_until INTEGER,product_path TEXT,transfer_path TEXT,release_id TEXT,reason TEXT,PRIMARY KEY(source,slot)); INSERT INTO jobs VALUES('usgs-streamflow',1,'complete',1,0,NULL,0,'kept',NULL,NULL,NULL)"); db.close();
  let before = await journalHealth(root, ['usgs-streamflow'], now);
  assert.equal(before[0].lastAttemptAt, null); assert.equal(before[0].lastSuccessfulCaptureAt, null);
  const journal = await Journal.open(path), job = journal.claim('nws-alerts', Math.floor(now / 3600000) * 3600000, now);
  journal.update(job, { product_path: 'data/processed/test.json', captured_at: now + 1 }, now + 2); journal.finish(job, null, now + 3); journal.close();
  const result = await journalHealth(root, PC_CAPTURE_IDS, now + 4), alert = result.find(p => p.sourceId === 'nws-alerts');
  assert.equal(alert.lastAttemptAt, new Date(now).toISOString()); assert.equal(alert.lastSuccessfulCaptureAt, new Date(now + 1).toISOString());
  assert.equal(alert.lastFinishedAt, new Date(now + 3).toISOString()); assert.equal(alert.nextEligibleAt, '2026-10-30T01:00:00.000Z');
  db = new DatabaseSync(path, { readOnly: true }); assert.equal(db.prepare("SELECT product_path FROM jobs WHERE source='usgs-streamflow'").get().product_path, 'kept'); db.close();
});
test('read-only diagnostics do not initialize missing journals or expose arbitrary failure text', async t => {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-card-readonly-')); t.after(() => rm(root, { recursive: true, force: true }));
  await assert.rejects(journalHealth(root)); await assert.rejects(readFile(resolve(root, 'pipeline-journal.sqlite')), { code: 'ENOENT' });
  const journal = await Journal.open(resolve(root, 'pipeline-journal.sqlite'));
  for (let attempt = 0; attempt < 3; attempt++) {
    const job = journal.claim('nws-alerts', Math.floor(now / 3600000) * 3600000, now + attempt * 700000);
    journal.finish(job, 'PRIVATE data /path SECRET', now + attempt * 700000 + 1);
  }
  journal.close(); const [health] = await journalHealth(root, ['nws-alerts'], now + 1500000);
  assert.equal(health.exhausted, true); assert.equal(health.retryAt, null); assert.equal(health.reason, null);
});
test('bounded backfill planning cannot manufacture historical active-alert or latest-water snapshots', () => {
  const plan = backfillPlan('nws-alerts', '2026-10-28T00:00:00Z', '2026-10-29T00:00:00Z', now);
  assert.equal(plan.requestedSlots, 25); assert.equal(plan.executable, false); assert.equal(plan.networkAccess, false);
  assert.throws(() => backfillPlan('nws-alerts', '2020-01-01', '2026-10-29', now), /BACKFILL_WINDOW_INVALID/);
  assert.throws(() => backfillPlan('fauna-occurrences', '2026-10-28', '2026-10-29', now), /SOURCE_NOT_ALLOWED/);
});

test('built cards endpoint is bounded, read-only and useful before publication setup', { skip: !process.env.KFM_NODE_TEST_ORIGIN }, async () => {
  const origin = new URL(process.env.KFM_NODE_TEST_ORIGIN); assert.equal(origin.hostname, '127.0.0.1');
  const response = await fetch(new URL('/api/pipeline/v1/cards', origin));
  assert.equal(response.status, 200); assert.match(response.headers.get('cache-control'), /no-store/);
  const text = await response.text(); assert.ok(Buffer.byteLength(text) < 256 * 1024);
  const snapshot = JSON.parse(text); assert.equal(snapshot.cards.length, 28); assert.equal(snapshot.authority, 'COVERAGE_METADATA_ONLY');
  const metadata = sources => sources.map(({ id, cadence, owner }) => ({ id, cadence, owner }));
  assert.deepEqual(metadata(snapshot.sources), metadata(model.PIPELINE_DEFINITIONS), 'built metadata must match current source');
  assert.doesNotMatch(text, /workerSecret|DB_PASSWORD|\/run\/media|pipeline-journal\.sqlite/);
  assert.equal((await fetch(new URL('/api/pipeline/v1/cards?path=private', origin))).status, 400);
  assert.equal((await fetch(new URL('/api/pipeline/v1/cards', origin), { method: 'POST' })).status, 405);
});


test('diagnostic report requires the qualified mount and atomically replaces only its own regular file', async t => {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-card-report-')); t.after(() => rm(root, { recursive: true, force: true }));
  const target = resolve(root, 'data/work/pipeline-health.json');
  await assert.rejects(writeOperatorReport({ root }, 'config', 'run', { guard: async () => { throw new Error('STORAGE_IDENTITY_CHANGED'); } }), /STORAGE_IDENTITY_CHANGED/);
  await assert.rejects(lstat(resolve(root, 'data')), { code: 'ENOENT' });
  const report = { format: 'kfm-pipeline-operator-health-v1', state: 'checked' };
  const options = { guard: async () => ({}), readHealth: async () => report };
  await writeOperatorReport({ root }, 'config', 'run', options);
  assert.deepEqual(JSON.parse(await readFile(target)), report);
  await writeOperatorReport({ root }, 'config', 'run', { ...options, lastTick: { state: 'held', reason: 'MEMORY_RESERVE_REQUIRED' } });
  const held = JSON.parse(await readFile(target)); assert.equal(held.state, 'degraded'); assert.equal(held.lastTick.reason, 'MEMORY_RESERVE_REQUIRED');
  assert.equal((await lstat(target)).mode & 0o777, 0o600);
  await rm(target); await symlink(resolve(root, 'outside'), target);
  await assert.rejects(writeOperatorReport({ root }, 'config', 'run', options), /HEALTH_TARGET_UNSAFE/);
  await assert.rejects(lstat(resolve(root, 'outside')), { code: 'ENOENT' });
});
