// Synthetic cutover qualification only: no network, production keys, services or SQL.
import test from 'node:test';
import assert from 'node:assert/strict';
import { generateKeyPairSync, randomBytes, sign } from 'node:crypto';
import { mkdtemp, readFile, writeFile, mkdir, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { canonical, sha, recipeDigest, MAX_PACKAGE, ORIGIN, PipelineError } from '../server/pipeline-contract.mjs';
import { captureRequest, fetchCapture } from '../server/ingestion-sources.mjs';
import { normalizeCapture } from '../server/pipeline-normalize.mjs';
import { signRequest } from '../server/pipeline-auth.mjs';
import { handlePipeline, publicContext } from '../server/pipeline-handler.mjs';
import { ArtifactFiles } from '../server/pipeline-files.mjs';
import { publish } from '../scripts/pc-pipeline/publisher.mjs';
import { tick, loadConfig } from '../scripts/pc-pipeline/worker.mjs';
import { Journal } from '../scripts/pc-pipeline/journal.mjs';
import { copyKit } from '../scripts/pc-pipeline/bundle.mjs';

const sources = ['usgs-streamflow', 'nws-alerts', 'usgs-earthquakes'];
const recipe = await recipeDigest();
const oldRecipe = sha('synthetic-previous-recipe');

class FixtureStore {
  rows = new Map(); heads = new Map(); nonces = new Set();
  async claimNonce(nonce) { if (this.nonces.has(nonce)) return false; this.nonces.add(nonce); return true; }
  async ready() { return { paused: false }; }
  async heartbeat() { return {}; }
  async release(id) { return this.rows.get(id) ?? null; }
  async active(sourceId) { return this.release(this.heads.get(sourceId)); }
  async stage(id, manifest) {
    const row = this.rows.get(id) ?? { id, sourceId: manifest.sourceId, manifest, state: 'STAGED' };
    this.rows.set(id, row); return row;
  }
  async commit(id, expectedActive, projection) {
    const row = this.rows.get(id), head = this.heads.get(row.sourceId) ?? null;
    if (row.state === 'COMMITTED') return { releaseId: id, active: head === id };
    if (head !== expectedActive) throw new PipelineError('ACTIVATION_CONFLICT');
    row.projection = projection; row.state = 'COMMITTED'; this.heads.set(row.sourceId, id);
    return { releaseId: id, active: true };
  }
}

async function fixture(t) {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-cutover-fixture-'));
  t.after(() => rm(root, { recursive: true, force: true }));
  const artifactRoot = resolve(root, 'artifacts'); await mkdir(artifactRoot);
  await writeFile(resolve(artifactRoot, '.qualified'), 'kfm-private-artifacts-v1');
  const pair = generateKeyPairSync('ed25519'); // Private key stays in this test process, never on the worker.
  const secret = randomBytes(32).toString('hex');
  const environment = { KFM_PIPELINE_ENABLED: 'true', KFM_RUNTIME_ROLE: 'published',
    KFM_PIPELINE_APPROVER_PUBLIC_KEY: pair.publicKey.export({ format: 'pem', type: 'spki' }), KFM_PIPELINE_WORKER_SECRET: secret };
  const store = new FixtureStore(), files = new ArtifactFiles(artifactRoot);
  const fetcher = (url, options) => handlePipeline(new Request(url, options), { store, files, environment });
  function approval(sourceId, digest = recipe) {
    const now = Date.now();
    const profile = { format: 'kfm-pc-release-delegation-v1', id: 'fixture-' + sourceId + '-' + digest.slice(0, 8), sourceId, recipeSha256: digest,
      approver: 'synthetic-owner', validFrom: new Date(now - 60000).toISOString(), expiresAt: new Date(now + 86400000).toISOString(),
      rights: 'redistribution-allowed', sensitivity: 'public', sourceRef: 'kfm://source/fixture/' + sourceId,
      rightsRef: 'kfm://review/fixture-rights', reviewRef: 'kfm://review/fixture', releaseProfileRef: 'kfm://release/fixture/' + sourceId,
      maxBytes: MAX_PACKAGE, maxRows: 1000, staleAfterSeconds: 7200, role: 'external-context' };
    return { profile, signature: sign(null, Buffer.from(canonical(profile)), pair.privateKey).toString('base64url') };
  }
  function transfer(sourceId, bytes, digest = recipe, expectedActive = null) {
    return { format: 'kfm-pc-release-transfer-v1', sourceId, recipeSha256: digest, byteLength: bytes.length,
      payloadSha256: sha(bytes), approval: approval(sourceId, digest), expectedActive };
  }
  async function request(action, body) {
    const raw = canonical(body), path = '/api/pipeline/v1/' + action;
    return handlePipeline(new Request(ORIGIN + path, { method: 'POST', body: raw,
      headers: signRequest({ secret, method: 'POST', path, body: raw }) }), { store, files, environment });
  }
  return { root, secret, environment, store, fetcher, approval, transfer, request };
}

async function acquire(request) {
  const slot = request.slot;
  const common = { type: 'Feature', id: 'synthetic-' + request.sourceId, geometry: { type: 'Point', coordinates: [-98, 38] } };
  let features;
  if (request.sourceId === 'usgs-streamflow') features = [{ ...common, properties: { parameter_code: '00060', monitoring_location_id: 'USGS-07144486',
    time: new Date(slot - 60000).toISOString(), value: '0.09', unit_of_measure: 'ft^3/s', approval_status: 'Provisional', privateField: 'KEEP_PRIVATE' } }];
  else if (request.sourceId === 'nws-alerts') features = [{ ...common, geometry: null, properties: { event: 'Synthetic only', severity: 'Unknown',
    sent: new Date(slot - 60000).toISOString(), effective: new Date(slot - 60000).toISOString(), expires: new Date(slot + 7200000).toISOString(), privateField: 'KEEP_PRIVATE' } }];
  else features = ['automatic', 'reviewed'].map((status, i) => ({ ...common, id: 'usfixture' + i,
    geometry: { type: 'Point', coordinates: [-98, 38, 5] }, properties: { type: 'earthquake', status, mag: 2.7, magType: 'ml', place: 'Synthetic only',
      time: slot - 60000, updated: slot - 30000, privateField: 'KEEP_PRIVATE' } }));
  return fetchCapture(request, { fetcher: async () => Response.json({ type: 'FeatureCollection', features }) });
}

test('old approvals refuse both old and new recipe transfers without replacing existing feed heads', async t => {
  const f = await fixture(t);
  for (const sourceId of sources.slice(0, 2)) {
    const req = captureRequest(sourceId), { product, bytes } = normalizeCapture(req, await acquire(req));
    const oldManifest = f.transfer(sourceId, bytes, oldRecipe);
    const id = sha(canonical(oldManifest));
    // An already committed historical release from the earlier recipe.
    f.store.rows.set(id, { id, sourceId, manifest: oldManifest, state: 'COMMITTED', projection: product }); f.store.heads.set(sourceId, id);
    assert.equal((await publicContext(sourceId, { store: f.store, environment: f.environment })).releaseId, id);
    const oldTransfer = { ...oldManifest, expectedActive: id };
    const oldResponse = await f.request('stage', oldTransfer);
    assert.equal(oldResponse.status, 409); assert.deepEqual(await oldResponse.json(), { error: 'RECIPE_CHANGED' });
    const newResponse = await f.request('stage', { ...oldTransfer, recipeSha256: recipe });
    assert.equal(newResponse.status, 403); assert.deepEqual(await newResponse.json(), { error: 'APPROVAL_INVALID' });
    const edited = structuredClone(oldTransfer); edited.recipeSha256 = recipe; edited.approval.profile.recipeSha256 = recipe;
    assert.equal((await (await f.request('stage', edited)).json()).error, 'APPROVAL_INVALID');
    assert.equal(f.store.heads.get(sourceId), id); assert.equal(f.store.rows.size, sources.slice(0, 2).indexOf(sourceId) + 1);
    await assert.rejects(publicContext(sourceId, { store: f.store, environment: { ...f.environment,
      KFM_PIPELINE_REVOKED_PROFILES: oldManifest.approval.profile.id } }), /APPROVAL_REVOKED/);
    await assert.rejects(publicContext(sourceId, { store: f.store, environment: f.environment, now: Date.now() + 2 * 86400000 }), /APPROVAL_INVALID/);
  }
});

test('all three sources round-trip real normalization, signed staging, chunks, commit and public read with distinct identities', async t => {
  const f = await fixture(t), releases = [], payloads = [];
  for (const sourceId of sources) {
    const req = captureRequest(sourceId), { bytes } = normalizeCapture(req, await acquire(req));
    assert.doesNotMatch(bytes.toString(), /KEEP_PRIVATE|privateField/);
    const m = f.transfer(sourceId, bytes), receipt = await publish(m, bytes, f.secret, { fetcher: f.fetcher });
    assert.equal(receipt.state, 'COMMITTED'); assert.equal(receipt.releaseId, sha(canonical(m))); assert.equal(receipt.payloadSha256, sha(bytes));
    const view = await publicContext(sourceId, { store: f.store, environment: f.environment });
    assert.equal(view.sourceId, sourceId); assert.equal(view.releaseId, receipt.releaseId); assert.equal(view.evidenceEligible, false);
    assert.equal(view.evidenceRole, 'EXTERNAL_CONTEXT_ONLY'); assert.equal(view.data.features.length, sourceId === 'usgs-earthquakes' ? 2 : 1);
    if (sourceId === 'usgs-earthquakes') assert.deepEqual(view.data.features.map(x => x.properties.status), ['automatic', 'reviewed']);
    releases.push(receipt.releaseId); payloads.push(receipt.payloadSha256);
  }
  assert.equal(new Set(releases).size, 3); assert.equal(new Set(payloads).size, 3); assert.equal(f.store.heads.size, 3);
});

test('three-source worker uses the default one-attempt budget across ticks and preserves deferred captures', async t => {
  const f = await fixture(t), credentials = resolve(f.root, 'credentials'), data = resolve(f.root, 'data');
  await mkdir(credentials); await mkdir(data);
  await writeFile(resolve(credentials, 'pipeline-worker-key'), f.secret, { mode: 0o600 });
  for (const id of sources) await writeFile(resolve(credentials, id + '.json'), canonical(f.approval(id)));
  const configPath = resolve(f.root, 'config.json');
  await writeFile(configPath, canonical({ format: 'kfm-pc-pipeline-config-v1', root: data, mount: f.root, device: 123, storeId: 'a'.repeat(32),
    sources, publish: true, approvalDirectory: credentials }));
  const config = await loadConfig(configPath), captured = [];
  const previous = process.env.CREDENTIALS_DIRECTORY; process.env.CREDENTIALS_DIRECTORY = credentials;
  t.after(() => { if (previous === undefined) delete process.env.CREDENTIALS_DIRECTORY; else process.env.CREDENTIALS_DIRECTORY = previous; });
  const now = Date.now();
  const options = { now, fetcher: f.fetcher, acquire: req => { captured.push(req.sourceId); return acquire(req); },
    memory: () => 8 * 1024 ** 3, guard: async () => ({}) }; // No physical storage qualification is claimed.
  for (let i = 0; i < 3; i++) {
    const result = await tick(config, options);
    assert.equal(result.publication.attempted, 1); assert.equal(result.outcomes.filter(x => x.state === 'published').length, 1);
    assert.equal(f.store.heads.size, i + 1);
    const journal = await Journal.open(resolve(data, 'pipeline-journal.sqlite'));
    try { journal.db.exec('UPDATE jobs SET retry_at=0'); } finally { journal.close(); } // Private fixture eligibility only.
  }
  assert.deepEqual(captured, ['nws-alerts', 'usgs-streamflow', 'usgs-earthquakes']);
  for (const id of sources) assert.ok(await publicContext(id, { store: f.store, environment: f.environment }));
});

test('an incomplete explicit priority list holds a three-source tick before acquisition', async () => {
  let acquired = false, guarded = false;
  await assert.rejects(tick({ sources, publish: false, storagePolicy: { priority: ['nws-alerts', 'usgs-streamflow'] } },
    { acquire: async () => { acquired = true; }, guard: async () => { guarded = true; } }), /SOURCE_NOT_ALLOWED/);
  assert.equal(acquired, false); assert.equal(guarded, false);
});

test('renewing a profile does not rewrite an immutable failed transfer in the same hourly job', async t => {
  const f = await fixture(t), credentials = resolve(f.root, 'credentials'), data = resolve(f.root, 'data');
  await mkdir(credentials); await mkdir(data); await writeFile(resolve(credentials, 'pipeline-worker-key'), f.secret, { mode: 0o600 });
  await writeFile(resolve(credentials, 'nws-alerts.json'), canonical(f.approval('nws-alerts', oldRecipe)));
  const previous = process.env.CREDENTIALS_DIRECTORY; process.env.CREDENTIALS_DIRECTORY = credentials;
  t.after(() => { if (previous === undefined) delete process.env.CREDENTIALS_DIRECTORY; else process.env.CREDENTIALS_DIRECTORY = previous; });
  const config = { root: data, sources: ['nws-alerts'], publish: true, approvalDirectory: credentials };
  let captures = 0;
  const options = { now: Date.now(), fetcher: f.fetcher, acquire: req => { captures++; return acquire(req); }, memory: () => 8 * 1024 ** 3, guard: async () => ({}) };
  const first = await tick(config, options); assert.equal(first.outcomes[0].reason, 'APPROVAL_INVALID');
  const journal = await Journal.open(resolve(data, 'pipeline-journal.sqlite'));
  let frozen;
  try { frozen = journal.db.prepare('SELECT transfer_path FROM jobs').get().transfer_path; journal.db.exec('UPDATE jobs SET retry_at=0'); } finally { journal.close(); }
  const before = await readFile(resolve(data, frozen));
  await writeFile(resolve(credentials, 'nws-alerts.json'), canonical(f.approval('nws-alerts')));
  const retry = await tick(config, options); assert.equal(retry.outcomes[0].reason, 'APPROVAL_INVALID');
  assert.deepEqual(await readFile(resolve(data, frozen)), before); assert.equal(captures, 1); assert.equal(f.store.heads.size, 0);
});

test('installed kit preserves the recipe and admits the three-source configuration without checkout dependencies', async t => {
  const f = await fixture(t), installed = resolve(f.root, 'installed'); await copyKit(installed);
  const { recipeDigest: installedRecipe } = await import(pathToFileURL(resolve(installed, 'server/pipeline-contract.mjs')));
  const { loadConfig: installedConfig } = await import(pathToFileURL(resolve(installed, 'scripts/pc-pipeline/worker.mjs')));
  assert.equal(await installedRecipe(), recipe);
  const configPath = resolve(f.root, 'capture-only.json');
  await writeFile(configPath, canonical({ format: 'kfm-pc-pipeline-config-v1', root: '/srv/kfm-data/store', mount: '/srv/kfm-data', device: 123,
    storeId: 'a'.repeat(32), sources, publish: false, approvalDirectory: '/etc/kfm-pipeline/approvals' }));
  assert.deepEqual((await installedConfig(configPath)).sources, sources);
});

test('migration refuses missing backup assertion or wrong digest before opening the database', async t => {
  const names = ['KFM_MIGRATION_SHA256', 'KFM_PIPELINE_DATABASE_BACKUP_VERIFIED', 'KFM_PIPELINE_ENABLED'];
  const saved = Object.fromEntries(names.map(k => [k, process.env[k]])), argv = process.argv;
  t.after(() => { process.argv = argv; for (const k of names) { if (saved[k] === undefined) delete process.env[k]; else process.env[k] = saved[k]; } });
  // Even if a developer has DB credentials, the final valid-assertion case stops before creating a pool.
  process.env.KFM_PIPELINE_ENABLED = 'false'; process.argv = ['node', 'migrate-pipeline.mjs', '--apply'];
  const sqlDigest = sha(await readFile(new URL('../server/pipeline-schema.sql', import.meta.url)));
  for (const [digest, backup] of [['', 'true'], [sqlDigest, ''], [sha('wrong SQL'), 'true']]) {
    process.env.KFM_MIGRATION_SHA256 = digest; process.env.KFM_PIPELINE_DATABASE_BACKUP_VERIFIED = backup;
    await assert.rejects(import('../scripts/migrate-pipeline.mjs?fixture=' + randomBytes(8).toString('hex')), /Exact SQL digest and verified shared-database backup required/);
  }
  process.env.KFM_MIGRATION_SHA256 = sqlDigest; process.env.KFM_PIPELINE_DATABASE_BACKUP_VERIFIED = 'true';
  await assert.rejects(import('../scripts/migrate-pipeline.mjs?fixture=' + randomBytes(8).toString('hex')), /PIPELINE_DISABLED/);
});
