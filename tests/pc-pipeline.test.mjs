import test from 'node:test';
import assert from 'node:assert/strict';
import { generateKeyPairSync, sign, randomBytes } from 'node:crypto';
import { mkdtemp, mkdir, writeFile, readFile, readdir, symlink, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { resolve } from 'node:path';
import { DatabaseSync } from 'node:sqlite';
import { canonical, sha, verifyProfile, recipeDigest, ORIGIN, MAX_PACKAGE, CHUNK_SIZE, PipelineError } from '../server/pipeline-contract.mjs';
import { signRequest } from '../server/pipeline-auth.mjs';
import { handlePipeline, publicContext } from '../server/pipeline-handler.mjs';
import { ArtifactFiles, immutable, readRegular, storageGuard, hashFile } from '../server/pipeline-files.mjs';
import { captureRequest, fetchCapture } from '../server/ingestion-sources.mjs';
import { normalizeCapture, providerTime, validateContext } from '../server/pipeline-normalize.mjs';
import { Journal } from '../scripts/pc-pipeline/journal.mjs';
import { tick } from '../scripts/pc-pipeline/worker.mjs';
import { publish } from '../scripts/pc-pipeline/publisher.mjs';
import { captureFile } from '../scripts/pc-pipeline/copy.mjs';
import { mirrorFtps } from '../scripts/pc-pipeline/ftps.mjs';
import { validateBackup, backupObjectPath } from '../scripts/pc-pipeline/backup-layout.mjs';
import { cli } from '../scripts/pc-pipeline/cli.mjs';
import { operatorHealth } from '../scripts/pc-pipeline/health.mjs';

const now = Date.now();
const keys = generateKeyPairSync('ed25519');
const publicKey = keys.publicKey.export({ format: 'pem', type: 'spki' });
const secret = randomBytes(32).toString('hex');
const recipe = await recipeDigest();
const env = { KFM_PIPELINE_ENABLED: 'true', KFM_RUNTIME_ROLE: 'published', KFM_PIPELINE_APPROVER_PUBLIC_KEY: publicKey, KFM_PIPELINE_WORKER_SECRET: secret };
function approval(sourceId = 'nws-alerts') {
  const profile = { format: 'kfm-pc-release-delegation-v1', id: 'test-owner-approval', sourceId, recipeSha256: recipe, approver: 'fixture-owner',
    validFrom: new Date(now - 60000).toISOString(), expiresAt: new Date(now + 86400000).toISOString(), rights: 'redistribution-allowed', sensitivity: 'public',
    sourceRef: 'kfm://source/fixture', rightsRef: 'kfm://review/fixture-rights', reviewRef: 'kfm://review/fixture', releaseProfileRef: 'kfm://release/profile/fixture',
    maxBytes: MAX_PACKAGE, maxRows: 1000, staleAfterSeconds: 7200, role: ['water','weather'].includes(sourceId) ? 'governed-package' : 'external-context' };
  return { profile, signature: sign(null, Buffer.from(canonical(profile)), keys.privateKey).toString('base64url') };
}
async function candidate(id = 'fixture-alert', geometry = null) {
  const request = captureRequest('nws-alerts', now);
  const capture = await fetchCapture(request, { fetcher: async () => Response.json({ type: 'FeatureCollection', features: [{ type: 'Feature', id, geometry, properties: {
    sent: new Date(now - 120000).toISOString(), effective: new Date(now - 120000).toISOString(), expires: new Date(now + 60000).toISOString(),
    event: 'Synthetic fixture', severity: 'Unknown', privateUnapprovedField: 'MUST_NOT_PUBLISH', description: 'Synthetic only' } }] }) });
  return normalizeCapture(request, capture);
}
class MemoryStore {
  constructor() { this.rows = new Map(); this.heads = new Map(); this.nonces = new Set(); this.paused = false; }
  async claimNonce(n) { if (this.nonces.has(n)) return false; this.nonces.add(n); return true; }
  async ready() { return { paused: this.paused }; }
  async stage(id, manifest) { if (this.paused) throw new PipelineError('PIPELINE_PAUSED'); const r = this.rows.get(id) ?? { id, sourceId: manifest.sourceId, manifest, state: 'STAGED' }; this.rows.set(id, r); return r; }
  async release(id) { return this.rows.get(id) ?? null; }
  async active(sourceId) { return this.rows.get(this.heads.get(sourceId)) ?? null; }
  async commit(id, expected, projection) {
    if (this.paused) throw new PipelineError('PIPELINE_PAUSED');
    const r = this.rows.get(id); const head = this.heads.get(r.sourceId) ?? null;
    if (r.state === 'COMMITTED') return { releaseId: id, active: head === id };
    if (head !== expected) throw new PipelineError('ACTIVATION_CONFLICT');
    r.projection = projection; r.state = 'COMMITTED'; this.heads.set(r.sourceId, id); return { releaseId: id, active: true };
  }
  async heartbeat() { return { receivedAt: now }; }
}
async function fixture() {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-pipeline-test-')); await writeFile(resolve(root, '.qualified'), 'kfm-private-artifacts-v1');
  const store = new MemoryStore(), files = new ArtifactFiles(root);
  const request = async (action, body, options = {}) => {
    const raw = canonical(body), path = '/api/pipeline/v1/' + action;
    const headers = signRequest({ secret: options.secret ?? secret, method: 'POST', path, body: raw, now });
    const req = new Request(ORIGIN + path, { method: 'POST', headers: { 'content-type': 'application/json', ...headers, ...options.headers }, body: raw });
    return handlePipeline(req, { store, files, environment: options.environment ?? env, now, ...options.dependencies });
  };
  const fetcher = async (url, options) => handlePipeline(new Request(url, options), { store, files, environment: env });
  return { store, files, request, fetcher, root };
}
function transfer(payload, sourceId = 'nws-alerts', expectedActive = null) {
  return { format: 'kfm-pc-release-transfer-v1', sourceId, recipeSha256: recipe, byteLength: payload.length, payloadSha256: sha(payload), approval: approval(sourceId), expectedActive };
}

test('owner delegation binds source, recipe, rights, expiration and exact bytes', () => {
  const a = approval(); assert.equal(verifyProfile(a, publicKey, { now, recipe, sourceId: 'nws-alerts' }).sourceId, 'nws-alerts');
  for (const changed of [{ ...a, signature: 'bad' }, { ...a, profile: { ...a.profile, rights: 'unknown' } }, { ...a, profile: { ...a.profile, recipeSha256: 'a'.repeat(64) } }]) assert.throws(() => verifyProfile(changed, publicKey, { now, recipe, sourceId: 'nws-alerts' }), /APPROVAL_INVALID/);
  assert.throws(() => verifyProfile(a, publicKey, { now: now + 2 * 86400000, recipe, sourceId: 'nws-alerts' }), /APPROVAL_INVALID/);
  assert.throws(() => verifyProfile(a, publicKey, { now, recipe, sourceId: 'water' }), /APPROVAL_INVALID/);
});
test('private capture normalizes only allowlisted fields and preserves external-context role', async () => {
  const { product, bytes } = await candidate();
  assert.equal(product.evidenceEligible, false); assert.equal(product.evidenceRole, 'EXTERNAL_CONTEXT_ONLY');
  assert.doesNotMatch(bytes.toString(), /MUST_NOT_PUBLISH|privateUnapprovedField/);
  await assert.rejects(candidate('bad-geometry', { type: 'Point', coordinates: [0, 91] }), /GEOMETRY_INVALID/);
});
test('HTTPS publisher verifies staging, every chunk and committed identity; replays are rejected', async () => {
  const f = await fixture(); const { bytes } = await candidate(); const m = transfer(bytes);
  const receipt = await publish(m, bytes, secret, { fetcher: f.fetcher }); assert.equal(receipt.state, 'COMMITTED');
  const data = await publicContext('nws-alerts', { store: f.store, environment: env, now });
  assert.equal(data.releaseId, sha(canonical(m))); assert.equal(data.data.features.length, 1); assert.equal(data.freshness, 'current');
  const repeat = await publish(m, bytes, secret, { fetcher: f.fetcher }); assert.equal(repeat.state, 'COMMITTED');
  const body = canonical({ state: 'idle' }), path = '/api/pipeline/v1/heartbeat'; const h = signRequest({ secret, method: 'POST', path, body, now });
  const req = () => new Request(ORIGIN + path, { method: 'POST', headers: h, body });
  assert.equal((await handlePipeline(req(), { store: f.store, environment: env, now })).status, 200);
  assert.equal((await handlePipeline(req(), { store: f.store, environment: env, now })).status, 401);
});
test('lost commit response recovers by immutable release lookup without double activation', async () => {
  const f = await fixture(); const { bytes } = await candidate(); const m = transfer(bytes); let dropped = false;
  const unreliable = async (url, options) => { const result = await f.fetcher(url, options); if (url.endsWith('/commit') && !dropped) { dropped = true; throw new Error('connection lost'); } return result; };
  await assert.rejects(publish(m, bytes, secret, { fetcher: unreliable }), /REMOTE_UNAVAILABLE/);
  assert.equal(f.store.heads.size, 1);
  assert.equal((await publish(m, bytes, secret, { fetcher: f.fetcher })).state, 'COMMITTED'); assert.equal(f.store.rows.size, 1);
});
test('preview, browser-origin calls, tampering and pause cannot publish', async () => {
  const f = await fixture(); const { bytes } = await candidate(); const m = transfer(bytes);
  assert.equal((await f.request('stage', m, { environment: { ...env, KFM_RUNTIME_ROLE: 'preview' } })).status, 404);
  assert.equal((await f.request('stage', m, { headers: { origin: ORIGIN } })).status, 401);
  assert.equal((await f.request('stage', m, { secret: 'f'.repeat(64) })).status, 401);
  f.store.paused = true; assert.equal((await f.request('stage', m)).status, 409); assert.equal(f.store.heads.size, 0);
});
test('incomplete artifacts and conflicting immutable chunks cannot replace active data', async () => {
  const f = await fixture(); const { bytes } = await candidate(); const m = transfer(bytes); const staged = await (await f.request('stage', m)).json();
  assert.equal((await f.request('commit', { releaseId: staged.releaseId })).status, 503); assert.equal(f.store.heads.size, 0);
  assert.equal((await f.request('chunk', { releaseId: staged.releaseId, index: 0, data: bytes.toString('base64') })).status, 200);
  const wrong = Buffer.from(bytes); wrong[0] ^= 1;
  assert.equal((await f.request('chunk', { releaseId: staged.releaseId, index: 0, data: wrong.toString('base64') })).status, 409);
  assert.equal((await f.request('commit', { releaseId: staged.releaseId })).status, 200);
});
test('CAS rejects a stale publisher and public reads reject corrupt, revoked and expired projections', async () => {
  const f = await fixture(); const a = (await candidate('a')).bytes, b = (await candidate('b')).bytes;
  const ma = transfer(a), mb = transfer(b);
  await publish(ma, a, secret, { fetcher: f.fetcher });
  await assert.rejects(publish(mb, b, secret, { fetcher: f.fetcher }), /ACTIVATION_CONFLICT/);
  await assert.rejects(publicContext('nws-alerts', { store: f.store, environment: { ...env, KFM_PIPELINE_REVOKED_PROFILES: 'test-owner-approval' }, now }), /APPROVAL_REVOKED/);
  await assert.rejects(publicContext('nws-alerts', { store: f.store, environment: env, now: now + 2 * 86400000 }), /APPROVAL_INVALID/);
  const row = await f.store.active('nws-alerts'); row.projection.data.features[0].properties.event = 'corrupt';
  await assert.rejects(publicContext('nws-alerts', { store: f.store, environment: env, now }), /PROJECTION_INTEGRITY_FAILED/);
});
test('expired alerts are labeled and do not become a fresh active-alert claim', async () => {
  const f = await fixture(); const { bytes } = await candidate(); await publish(transfer(bytes), bytes, secret, { fetcher: f.fetcher });
  const result = await publicContext('nws-alerts', { store: f.store, environment: env, now: now + 3 * 3600000 });
  assert.equal(result.freshness, 'stale'); assert.equal(result.data.features[0].properties.expired, true);
});
test('actual SQLite journal fences old workers and survives close/reopen', async () => {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-journal-test-')); const path = resolve(root, 'journal.sqlite');
  let j = await Journal.open(path); const a = j.claim('nws-alerts', 1000, now); assert.ok(a);
  assert.equal(j.claim('nws-alerts', 1000, now), null); j.close();
  j = await Journal.open(path); const b = j.claim('nws-alerts', 1000, now + 600001); assert.ok(b);
  assert.throws(() => j.update(a, { state: 'complete' }, now + 600002), /LEASE_LOST/);
  j.update(b, { product_path: 'data/processed/test.json' }, now + 600002); j.finish(b, null, now + 600002); j.close();
  j = await Journal.open(path); assert.equal(j.status()[0].state, 'complete'); assert.equal(j.claim('nws-alerts', 1000, now + 700000), null); j.close();
});
test('PC worker retains failed raw input and avoids repeating completed hourly work', async () => {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-worker-test-')); const config = { root, sources: ['nws-alerts'], publish: false };
  let calls = 0;
  const acquire = async req => { calls++; return fetchCapture(req, { fetcher: async () => Response.json({ type: 'FeatureCollection', features: [] }) }); };
  const options = { now, acquire, memory: () => 8 * 1024 ** 3, guard: async () => ({}) };
  assert.equal((await tick(config, options)).outcomes[0].state, 'candidate-only');
  await tick(config, options); assert.equal(calls, 1);
  const other = await mkdtemp(resolve(tmpdir(), 'kfm-worker-invalid-'));
  const bad = await tick({ ...config, root: other }, { ...options, acquire: req => fetchCapture(req, { fetcher: async () => Response.json({ unexpected: true }) }) });
  assert.equal(bad.outcomes[0].state, 'held'); assert.ok((await readdir(resolve(other, 'data/quarantine/nws-alerts/objects/sha256'))).length);
});
test('low memory defers only claimable work and leaves an idle tick successful', async () => {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-worker-memory-')); const config = { root, sources: ['nws-alerts'], publish: false };
  const acquire = req => fetchCapture(req, { fetcher: async () => Response.json({ type: 'FeatureCollection', features: [] }) });
  const low = { now, acquire, memory: () => 1024 ** 3, guard: async () => ({}) };
  await assert.rejects(tick(config, low), /MEMORY_RESERVE_REQUIRED/);
  let j = await Journal.open(resolve(root, 'pipeline-journal.sqlite'));
  assert.equal(j.status().length, 0, 'a memory deferral neither creates a slot nor consumes an attempt'); j.close();
  assert.equal((await tick(config, { ...low, memory: () => 8 * 1024 ** 3 })).outcomes[0].state, 'candidate-only');
  const idle = await tick(config, { ...low, acquire: () => assert.fail('a completed slot must not reacquire') });
  assert.deepEqual(idle.outcomes, [{ sourceId: 'nws-alerts', state: 'already-complete-or-held' }]);
  j = await Journal.open(resolve(root, 'pipeline-journal.sqlite'));
  assert.equal(j.status()[0].attempts, 1); assert.equal(j.claimable('nws-alerts', captureRequest('nws-alerts', now).slot, now), false); j.close();
});
test('connection-only mode blocks scheduled, package and FTPS uploads before data or credentials are read', async () => {
  await assert.rejects(tick({ remoteMode: 'connection-only', publish: true }, {
    guard: () => assert.fail('must reject before storage or network access'),
  }), /CONNECTION_ONLY_UPLOADS_DISABLED/);
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-connection-policy-'));
  const path = resolve(root, 'config.json');
  const config = { format: 'kfm-pc-pipeline-config-v1', root: '/unmounted/store', mount: '/unmounted', storeId: 'a'.repeat(32),
    device: 1, sources: [], publish: false, remoteMode: 'connection-only', approvalDirectory: '/nonexistent' };
  await writeFile(path, JSON.stringify(config));
  await assert.rejects(cli(['stage-package', path, 'water', '/nonexistent', '/nonexistent']), /CONNECTION_ONLY_UPLOADS_DISABLED/);
  await assert.rejects(cli(['ftps-mirror', path, 'a'.repeat(64), '/nonexistent']), /CONNECTION_ONLY_UPLOADS_DISABLED/);
});
test('storage guards reject the root filesystem and immutable writes reject symlinks', async () => {
  await assert.rejects(storageGuard({ root: '/tmp/test', mount: '/', device: '0', storeId: 'x' }), /DEDICATED_DATA_MOUNT_REQUIRED/);
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-files-test-')); const file = resolve(root, 'object');
  await immutable(file, Buffer.from('original')); await immutable(file, Buffer.from('original'));
  await assert.rejects(immutable(file, Buffer.from('changed!')), /IMMUTABLE_CONFLICT/);
  await symlink(file, resolve(root, 'symlink')); await assert.rejects(readRegular(resolve(root, 'symlink'), 100));
});
test('backup streams multi-megabyte originals, verifies bytes and refuses conflicting copies', async () => {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-backup-test-')); const source = resolve(root, 'source'), destination = resolve(root, 'copy');
  const content = randomBytes(CHUNK_SIZE * 13); await writeFile(source, content); const expected = await hashFile(source);
  await captureFile(source, destination, expected); assert.deepEqual(await readFile(destination), content);
  await captureFile(source, destination, expected); await writeFile(destination, 'corrupt');
  await assert.rejects(captureFile(source, destination, expected), /BACKUP_CONFLICT/);
});
test('successive backups preserve both versions of a mutable working file', async () => {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-backup-versions-'));
  const source = resolve(root, 'index.sqlite');
  const objects = resolve(root, 'store');
  await writeFile(source, 'first committed version');
  const first = { path: 'work/intake/index.sqlite', ...await hashFile(source) };
  await captureFile(source, backupObjectPath(objects, first), first);
  await writeFile(source, 'second committed version');
  const second = { path: first.path, ...await hashFile(source) };
  await captureFile(source, backupObjectPath(objects, second), second);
  await captureFile(source, backupObjectPath(objects, second), second);
  assert.equal((await readFile(backupObjectPath(objects, first))).toString(), 'first committed version');
  assert.equal((await readFile(backupObjectPath(objects, second))).toString(), 'second committed version');
  const manifest = { format: 'kfm-pc-data-backup-v2', files: [second], inventorySha256: sha(Buffer.from(canonical([second]))) };
  assert.equal(validateBackup(manifest), manifest);
  assert.equal(backupObjectPath(objects, first, 'kfm-pc-data-backup-v1'), resolve(objects, 'data', first.path));
  const invalid = { ...manifest, files: [{ ...second, path: '../escape' }] };
  invalid.inventorySha256 = sha(Buffer.from(canonical(invalid.files)));
  assert.throws(() => validateBackup(invalid), /BACKUP_PATH_INVALID/);
});
test('operator health ages a backup by its completion clock and keeps legacy receipts explicit', async () => {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-health-clock-')); const run = resolve(root, 'run'); await mkdir(run);
  const configPath = resolve(root, 'config.json');
  await writeFile(configPath, JSON.stringify({ format: 'kfm-pc-pipeline-config-v1', root: resolve(root, 'store'), mount: root, storeId: 'a'.repeat(32),
    device: 1, sources: ['nws-alerts'], publish: false, remoteMode: 'connection-only', approvalDirectory: '/nonexistent' }));
  const options = { now, guard: async () => ({}) };
  const receipt = completedAt => writeFile(resolve(run, 'backup-last.json'), JSON.stringify({ state: 'verified-copy', files: 3, inventorySha256: 'b'.repeat(64), completedAt }));
  const recent = new Date(now - 3600000).toISOString();
  await receipt(recent);
  const fresh = (await operatorHealth(configPath, run, options)).backup;
  assert.equal(fresh.state, 'verified-copy'); assert.equal(fresh.receiptTime, recent);
  await receipt(new Date(now - 40 * 3600000).toISOString());
  assert.equal((await operatorHealth(configPath, run, options)).backup.state, 'overdue', 'a fresh file time must not hide an old backup');
  await receipt(undefined);
  const legacy = (await operatorHealth(configPath, run, options)).backup;
  assert.equal(legacy.receiptTime, null); assert.equal(typeof legacy.receiptFileModifiedAt, 'string');
});
test('operator health counts its own undeclared captures apart from intake files awaiting review', async () => {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-health-intake-')); const run = resolve(root, 'run'); await mkdir(run);
  const store = resolve(root, 'store'); await mkdir(resolve(store, 'data/work/intake'), { recursive: true });
  const configPath = resolve(root, 'config.json');
  await writeFile(configPath, JSON.stringify({ format: 'kfm-pc-pipeline-config-v1', root: store, mount: root, storeId: 'a'.repeat(32),
    device: 1, sources: ['nws-alerts'], publish: false, remoteMode: 'connection-only', approvalDirectory: '/nonexistent' }));
  const db = new DatabaseSync(resolve(store, 'data/work/intake/index.sqlite'));
  db.exec('CREATE TABLE items(lane TEXT, relative_path TEXT, declared_json TEXT, status TEXT, present INTEGER)');
  const add = db.prepare('INSERT INTO items VALUES (?,?,?,?,?)');
  const payload = source => `${source}/objects/sha256/${'c'.repeat(64)}/payload`;
  add.run('quarantine', payload('usgs-streamflow'), null, 'review', 1);
  add.run('quarantine', payload('nws-alerts'), null, 'review', 1);
  add.run('quarantine', payload('usgs-streamflow'), null, 'review', 0);
  add.run('quarantine', payload('usgs-streamflow'), '{"source_id":"usgs-streamflow"}', 'ready', 1);
  add.run('quarantine', payload('kgs-wells'), null, 'review', 1);
  add.run('raw', 'usgs-streamflow/gauges.csv', null, 'review', 1);
  db.close();
  const { intake } = await operatorHealth(configPath, run, { now, guard: async () => ({}) });
  assert.deepEqual(intake.pipelineCaptures, { state: 'held-for-source-profile', byStatus: [{ status: 'review', files: 2 }] });
  // A declared capture, another source's quarantine payload and a raw file still await their own decisions.
  assert.deepEqual([...intake.byStatus].sort((a, b) => a.status.localeCompare(b.status)), [{ status: 'ready', files: 1 }, { status: 'review', files: 2 }]);
});
test('real provider formats preserve decimal source values and RFC3339 offset/subsecond clocks', async () => {
  assert.equal(providerTime('2026-10-22T20:06:29.034006+00:00'), '2026-10-22T20:06:29.034Z');
  assert.equal(providerTime('2026-10-22T15:06:29-05:00'), '2026-10-22T20:06:29.000Z');
  assert.throws(() => providerTime('2026-02-30T20:06:29+00:00'), /SOURCE_TIME_INVALID/);
  const request = captureRequest('usgs-streamflow', now);
  const acquired = await fetchCapture(request, { fetcher: async () => Response.json({ type: 'FeatureCollection', features: [{ type: 'Feature', id: 'fixture-usgs', geometry: { type: 'Point', coordinates: [-98, 38] },
    properties: { parameter_code: '00060', monitoring_location_id: 'USGS-07144486', time: new Date(request.slot).toISOString().replace('Z', '+00:00'), value: '0.09', unit_of_measure: 'ft^3/s', approval_status: 'Provisional', qualifier: null } }] }) });
  const { product } = normalizeCapture(request, acquired); assert.equal(product.data.features[0].properties.value, 0.09);
  assert.equal(product.data.features[0].properties.originalValue, '0.09'); assert.equal(validateContext(product), product);
  product.data.features[0].properties.privateContact = 'must not pass'; assert.throws(() => validateContext(product), /CONTEXT_INVALID/);
});
test('multi-chunk publication checks every chunk and reconstructs the exact bytes', async () => {
  const f = await fixture(); const c = await candidate();
  const features = Array.from({ length: 50 }, (_, i) => ({ ...c.product.data.features[0], id: 'fixture-' + i, properties: { ...c.product.data.features[0].properties, description: 'x'.repeat(10000) } }));
  const payload = Buffer.from(canonical({ ...c.product, data: { type: 'FeatureCollection', features } })); assert.ok(payload.length > CHUNK_SIZE);
  const receipt = await publish(transfer(payload), payload, secret, { fetcher: f.fetcher });
  assert.equal((await publicContext('nws-alerts', { store: f.store, environment: env, now })).data.features.length, 50);
  assert.equal(receipt.payloadSha256, sha(payload));
});
test('FTPS verifies encrypted private staging before rename and keeps credentials out of arguments', async () => {
  const payload = (await candidate()).bytes, m = transfer(payload), id = sha(canonical(m));
  const receipt = { state: 'COMMITTED', releaseId: id, payloadSha256: sha(payload) };
  const config = { format: 'kfm-qualified-ftps-v1', qualified: true, host: 'ftp.example.test', username: 'fixture-user', password: 'fixture-password', privateDirectory: '/private/staging', publicDirectory: '/public/data', httpsBase: 'https://files.example.test/data' };
  const calls = [];
  const run = async (args, input) => {
    calls.push(args); assert.ok(args.includes('--ssl-reqd')); assert.ok(args.includes('--tlsv1.2')); assert.ok(!args.join(' ').includes(config.password)); assert.ok(input.includes(config.password));
    const output = args.indexOf('--output'); if (output >= 0) await writeFile(args[output + 1], payload);
  };
  assert.equal((await mirrorFtps(config, m, payload, receipt, { run, fetcher: async () => new Response(payload) })).state, 'mirror-verified'); assert.equal(calls.length, 3);
  let renamed = false;
  await assert.rejects(mirrorFtps(config, m, payload, receipt, { run: async args => { if (args.includes('--quote')) renamed = true; const output = args.indexOf('--output'); if (output >= 0) await writeFile(args[output + 1], 'corrupt'); } }), /FTPS_READBACK_FAILED/);
  assert.equal(renamed, false);
});
test('governed packages cannot use the external-context shortcut', async () => {
  const f = await fixture(); const payload = Buffer.from(canonical({ snapshot: {}, decision: {} })); const m = transfer(payload, 'water');
  await assert.rejects(publish(m, payload, secret, { fetcher: f.fetcher }), /GOVERNED_VALIDATOR_REQUIRED/); assert.equal(f.store.heads.size, 0);
});

test('hosting outage keeps captures private and retries after recovery without reacquiring', async () => {
  const f = await fixture(); const credentials = await mkdtemp(resolve(tmpdir(), 'kfm-credentials-'));
  await writeFile(resolve(credentials, 'pipeline-worker-key'), secret);
  await writeFile(resolve(credentials, 'nws-alerts.json'), canonical(approval()));
  const previous = process.env.CREDENTIALS_DIRECTORY; process.env.CREDENTIALS_DIRECTORY = credentials;
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-outage-'));
  const config = { root, sources: ['nws-alerts'], publish: true, approvalDirectory: credentials };
  let captures = 0;
  const options = { now, memory: () => 8 * 1024 ** 3, guard: async () => ({}), acquire: req => {
    captures++; return fetchCapture(req, { fetcher: async () => Response.json({ type: 'FeatureCollection', features: [] }) });
  } };
  try {
    const down = await tick(config, { ...options, fetcher: async () => { throw Error('offline'); } });
    assert.equal(down.outcomes[0].state, 'deferred'); assert.equal(captures, 1);
    const j = await Journal.open(resolve(root, 'pipeline-journal.sqlite'));
    assert.ok(j.status()[0].retry_at > now); assert.equal(j.status()[0].attempts, 0);
    // Advance eligibility in this private fixture without depending on the wall-clock hour boundary.
    j.db.exec('UPDATE jobs SET retry_at=0'); j.close();
    const recovered = await tick(config, { ...options, fetcher: f.fetcher });
    assert.equal(recovered.outcomes[0].state, 'published');
    assert.equal(captures, 1);
  } finally { if (previous === undefined) delete process.env.CREDENTIALS_DIRECTORY; else process.env.CREDENTIALS_DIRECTORY = previous; }
});

test('priority and one-publication budget preserve the second candidate for a later tick', async () => {
  const f = await fixture(); const root = await mkdtemp(resolve(tmpdir(), 'kfm-priority-'));
  const credentials = await mkdtemp(resolve(tmpdir(), 'kfm-priority-credentials-'));
  await writeFile(resolve(credentials, 'pipeline-worker-key'), secret);
  for (const id of ['nws-alerts', 'usgs-streamflow']) await writeFile(resolve(credentials, id + '.json'), canonical(approval(id)));
  const previous = process.env.CREDENTIALS_DIRECTORY; process.env.CREDENTIALS_DIRECTORY = credentials;
  const config = { root, sources: ['usgs-streamflow', 'nws-alerts'], publish: true, approvalDirectory: credentials };
  const acquired = [];
  try {
    const result = await tick(config, { now, fetcher: f.fetcher, memory: () => 8 * 1024 ** 3, guard: async () => ({}), acquire: req => {
      acquired.push(req.sourceId); return fetchCapture(req, { fetcher: async () => Response.json({ type: 'FeatureCollection', features: [] }) });
    } });
    assert.deepEqual(result.outcomes.map(x => [x.sourceId, x.state]), [['nws-alerts', 'published'], ['usgs-streamflow', 'deferred']]);
    assert.equal(result.outcomes[1].reason, 'PUBLICATION_BUDGET'); assert.equal(acquired.length, 2);
    assert.equal(result.publication.attempted, 1); assert.equal(f.store.heads.size, 1);
    const j = await Journal.open(resolve(root, 'pipeline-journal.sqlite'));
    assert.equal(j.status().find(x => x.source === 'usgs-streamflow').attempts, 0);
    j.db.exec('UPDATE jobs SET retry_at=0'); j.close();
    const later = await tick(config, { now, fetcher: f.fetcher, memory: () => 8 * 1024 ** 3, guard: async () => ({}), acquire: async () => { throw Error('must reuse saved candidates'); } });
    assert.equal(later.outcomes.find(x => x.sourceId === 'usgs-streamflow').state, 'published');
    assert.equal(f.store.heads.size, 2);
  } finally { if (previous === undefined) delete process.env.CREDENTIALS_DIRECTORY; else process.env.CREDENTIALS_DIRECTORY = previous; }
});

test('capture-only completion can later publish and deferrals remain fenced', async () => {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-promotion-')); const j = await Journal.open(resolve(root, 'journal.sqlite'));
  try {
    const a = j.claim('nws-alerts', 1, now); j.update(a, { product_path: 'candidate.json' }, now); j.finish(a, null, now);
    assert.equal(j.claim('nws-alerts', 1, now), null);
    const b = j.claim('nws-alerts', 1, now, true); assert.ok(b);
    assert.throws(() => j.defer(a, 'PUBLICATION_BUDGET', now), /LEASE_LOST/);
    j.defer(b, 'PUBLICATION_BUDGET', now); assert.equal(j.claim('nws-alerts', 1, now + 1, true), null);
    assert.ok(j.claim('nws-alerts', 1, now + 300001, true));
  } finally { j.close(); }
});

async function workerFixture(t, workerSecret = secret) {
  const f = await fixture();
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-qualified-synthetic-'));
  const credentials = await mkdtemp(resolve(tmpdir(), 'kfm-fixture-credentials-'));
  await writeFile(resolve(credentials, 'pipeline-worker-key'), workerSecret);
  for (const sourceId of ['nws-alerts', 'usgs-streamflow']) await writeFile(resolve(credentials, sourceId + '.json'), canonical(approval(sourceId)));
  const previous = process.env.CREDENTIALS_DIRECTORY; process.env.CREDENTIALS_DIRECTORY = credentials;
  t.after(async () => {
    if (previous === undefined) delete process.env.CREDENTIALS_DIRECTORY; else process.env.CREDENTIALS_DIRECTORY = previous;
    for (const path of [root, credentials, f.root]) await rm(path, { recursive: true, force: true });
  });
  const config = { root, sources: ['nws-alerts', 'usgs-streamflow'], publish: true, approvalDirectory: credentials };
  const captured = [];
  const options = { now, fetcher: f.fetcher, memory: () => 8 * 1024 ** 3, guard: async () => ({}), acquire: req => {
    captured.push(req.sourceId); return fetchCapture(req, { fetcher: async () => Response.json({ type: 'FeatureCollection', features: [] }) });
  } };
  const journal = async work => {
    const j = await Journal.open(resolve(root, 'pipeline-journal.sqlite'));
    try { return await work(j); } finally { j.close(); }
  };
  return { ...f, root, credentials, config, options, captured, journal };
}

test('malformed, empty and mismatched heartbeat keys hold bounded jobs while preserving raw captures', async t => {
  for (const [key, code] of [['malformed', 'PIPELINE_KEY_INVALID'], ['', 'PIPELINE_KEY_INVALID'], ['0'.repeat(64), 'PIPELINE_AUTH_REQUIRED']]) {
    await t.test(code + ':' + key.length, async t => {
      const f = await workerFixture(t, key);
      for (let i = 0; i < 3; i++) {
        const result = await tick(f.config, f.options);
        assert.deepEqual(result.outcomes.map(row => [row.state, row.reason]), [['held', code], ['held', code]]);
        assert.equal(result.publication.attempted, 0);
        await f.journal(j => { assert.ok(j.status().every(row => row.attempts === i + 1)); j.db.exec('UPDATE jobs SET retry_at=0'); });
      }
      const stopped = await tick(f.config, f.options);
      assert.ok(stopped.outcomes.every(row => row.state === 'already-complete-or-held'));
      assert.equal(f.captured.length, 2); assert.equal(f.store.rows.size, 0);
      for (const id of f.config.sources) assert.equal((await readdir(resolve(f.root, 'data/quarantine', id, 'objects/sha256'))).length, 1);
    });
  }
});

test('missing local approval is held and does not prevent the other source from publishing', async t => {
  const f = await workerFixture(t);
  await rm(resolve(f.credentials, 'nws-alerts.json'));
  f.config.storagePolicy = { maxPublicationsPerTick: 2 };
  const result = await tick(f.config, f.options);
  assert.deepEqual(result.outcomes.map(row => [row.state, row.reason]), [['held', 'PIPELINE_OPERATION_FAILED'], ['published', undefined]]);
  assert.equal(result.publication.remoteAvailable, true);
  await f.journal(j => assert.equal(j.status().find(row => row.source === 'nws-alerts').attempts, 1));
  assert.equal(f.store.heads.size, 1); assert.equal(f.captured.length, 2);
});

test('byte budget defers an oversized candidate then publishes the saved bytes when budget permits', async t => {
  const f = await workerFixture(t);
  f.config.sources = ['nws-alerts']; f.config.storagePolicy = { maxBytesPerTick: CHUNK_SIZE };
  let captures = 0;
  const options = { ...f.options, acquire: req => {
    captures++;
    return fetchCapture(req, { fetcher: async () => Response.json({ type: 'FeatureCollection', features: Array.from({ length: 40 }, (_, i) => ({
      type: 'Feature', id: 'synthetic-byte-budget-' + i, geometry: null,
      properties: { sent: new Date(now - 120000).toISOString(), effective: new Date(now - 120000).toISOString(), expires: new Date(now + 60000).toISOString(),
        event: 'Synthetic fixture', severity: 'Unknown', description: 'x'.repeat(10000) }
    })) }) });
  } };
  const deferred = await tick(f.config, options);
  assert.equal(deferred.outcomes[0].reason, 'PUBLICATION_BUDGET');
  assert.equal(deferred.publication.attempted, 0); assert.equal(deferred.publication.payloadBytes, 0);
  assert.equal(f.store.rows.size, 0);
  await f.journal(j => { assert.equal(j.status()[0].attempts, 0); j.db.exec('UPDATE jobs SET retry_at=0'); });
  f.config.storagePolicy.maxBytesPerTick = 1024 ** 2;
  const recovered = await tick(f.config, options);
  assert.equal(recovered.outcomes[0].state, 'published'); assert.equal(captures, 1);
  assert.ok(recovered.publication.payloadBytes > CHUNK_SIZE && recovered.publication.payloadBytes <= 1024 ** 2);
  await tick(f.config, options); assert.equal(captures, 1); assert.equal(f.store.rows.size, 1);
});

test('receiver rejects a product beyond 8 MiB without staging any release', async () => {
  const f = await fixture(); const m = transfer((await candidate()).bytes); m.byteLength = MAX_PACKAGE + 1;
  const result = await f.request('stage', m);
  assert.equal(result.status, 400); assert.equal((await result.json()).error, 'MANIFEST_INVALID'); assert.equal(f.store.rows.size, 0);
});

test('busy hosting consumes one failed attempt and blocks further publication for the run', async t => {
  const f = await workerFixture(t); f.config.storagePolicy = { maxPublicationsPerTick: 2 };
  let stages = 0;
  const result = await tick(f.config, { ...f.options, fetcher: (url, options) => {
    if (url.endsWith('/stage')) { stages++; return Promise.resolve(new Response('busy', { status: 503 })); }
    return f.fetcher(url, options);
  } });
  assert.deepEqual(result.outcomes.map(row => [row.state, row.reason]), [['deferred', 'REMOTE_BUSY'], ['deferred', 'HOSTING_UNAVAILABLE']]);
  assert.equal(stages, 1); assert.equal(result.publication.attempted, 1); assert.ok(result.publication.payloadBytes > 0);
  await f.journal(j => assert.ok(j.status().every(row => row.attempts === 0)));
  assert.equal(f.captured.length, 2); assert.equal(f.store.rows.size, 0);
});

test('publication respects an aborted aggregate signal without retrying or leaking transport errors', async () => {
  const payload = (await candidate()).bytes; let calls = 0;
  await assert.rejects(publish(transfer(payload), payload, secret, { signal: AbortSignal.abort(), fetcher: async (url, options) => {
    calls++; options.signal.throwIfAborted(); throw Error('synthetic-private-transport-text');
  } }), /^Error: REMOTE_UNAVAILABLE$/);
  assert.equal(calls, 1);
});
