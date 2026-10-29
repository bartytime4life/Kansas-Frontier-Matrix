// Fixed, synthetic authority only. Never use these fixture keys or references operationally.
import test from 'node:test';
import assert from 'node:assert/strict';
import { createPrivateKey, createPublicKey, sign } from 'node:crypto';
import { mkdtemp, writeFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { canonical, sha, recipeDigest, MAX_PACKAGE, ORIGIN, SOURCES, verifyProfile } from '../server/pipeline-contract.mjs';
import { signRequest } from '../server/pipeline-auth.mjs';
import { handlePipeline, publicContext, publicArtifact } from '../server/pipeline-handler.mjs';
import { ArtifactFiles } from '../server/pipeline-files.mjs';
import { captureRequest, fetchCapture } from '../server/ingestion-sources.mjs';
import { normalizeCapture } from '../server/pipeline-normalize.mjs';
import { publish } from '../scripts/pc-pipeline/publisher.mjs';

const now = Date.parse('2026-10-29T18:30:00.000Z');
const previous = 'e8b85ea8ff6414e9dc46030835d2102ce7439cf7811615512b422b2386d5fab3';
const recipe = await recipeDigest();
const feeds = ['usgs-streamflow', 'nws-alerts', 'usgs-earthquakes'];
const priorSources = [...feeds, 'water', 'weather'];
// A public deterministic fixture seed, never an owner key or generated operational credential.
const privateKey = createPrivateKey({ key: Buffer.concat([Buffer.from('302e020100300506032b657004220420', 'hex'), Buffer.alloc(32, 7)]), format: 'der', type: 'pkcs8' });
const environment = { KFM_PIPELINE_ENABLED: 'true', KFM_RUNTIME_ROLE: 'published',
  KFM_PIPELINE_APPROVER_PUBLIC_KEY: createPublicKey(privateKey).export({ format: 'pem', type: 'spki' }),
  KFM_PIPELINE_WORKER_SECRET: 'f'.repeat(64) };
function approval(sourceId, digest) {
  const profile = { format: 'kfm-pc-release-delegation-v1', id: 'synthetic-' + sourceId + '-' + digest.slice(0, 8),
    sourceId, recipeSha256: digest, approver: 'synthetic-only', validFrom: new Date(now - 60000).toISOString(),
    expiresAt: new Date(now + 86400000).toISOString(), rights: 'redistribution-allowed', sensitivity: 'public',
    sourceRef: 'kfm://source/synthetic', rightsRef: 'kfm://review/synthetic-rights', reviewRef: 'kfm://review/synthetic',
    releaseProfileRef: 'kfm://release/synthetic', maxBytes: MAX_PACKAGE, maxRows: 1000, staleAfterSeconds: 7200,
    role: ['water', 'weather'].includes(sourceId) ? 'governed-package' : 'external-context' };
  return { profile, signature: sign(null, Buffer.from(canonical(profile)), privateKey).toString('base64url') };
}
async function payload(sourceId) {
  const request = captureRequest(sourceId, now), at = new Date(request.slot - 60000).toISOString();
  const properties = sourceId === 'usgs-streamflow'
    ? { parameter_code: '00060', monitoring_location_id: 'USGS-07144486', time: at, value: '0.09', unit_of_measure: 'ft^3/s', approval_status: 'Provisional' }
    : sourceId === 'nws-alerts'
      ? { event: 'Synthetic only', severity: 'Unknown', sent: at, effective: at, expires: new Date(now + 7200000).toISOString() }
      : { type: 'earthquake', status: 'reviewed', mag: 2.7, magType: 'ml', place: 'Synthetic only', time: request.slot - 60000, updated: request.slot - 30000 };
  const features = [{ type: 'Feature', id: 'synthetic', geometry: sourceId === 'nws-alerts' ? null : { type: 'Point', coordinates: sourceId === 'usgs-earthquakes' ? [-98, 38, 5] : [-98, 38] }, properties }];
  const captured = await fetchCapture(request, { fetcher: async () => Response.json({ type: 'FeatureCollection', features }) });
  // The adapter records wall time; freeze only its synthetic receipt for reproducible identities.
  captured.receipt.requestedAt = captured.receipt.retrievedAt = new Date(now).toISOString();
  return normalizeCapture(request, captured);
}
async function fixture(t) {
  const root = await mkdtemp(join(tmpdir(), 'kfm-fixed-cutover-')); t.after(() => rm(root, { recursive: true, force: true }));
  await writeFile(join(root, '.qualified'), 'kfm-private-artifacts-v1');
  const files = new ArtifactFiles(root), rows = new Map(), heads = new Map(), nonces = new Set();
  const store = { rows, heads, async ready() { return { paused: false }; }, async claimNonce(n) { if (nonces.has(n)) return false; nonces.add(n); return true; },
    async release(id) { return rows.get(id) ?? null; }, async active(id) { return rows.get(heads.get(id)) ?? null; },
    async stage(id, manifest) { const row = { id, sourceId: manifest.sourceId, manifest, state: 'STAGED' }; rows.set(id, row); return row; },
    async commit(id, expected, projection) { const row = rows.get(id); assert.equal(heads.get(row.sourceId) ?? null, expected); row.projection = projection; row.state = 'COMMITTED'; heads.set(row.sourceId, id); return { releaseId: id, active: true }; } };
  const request = async (action, body) => {
    const raw = canonical(body), path = '/api/pipeline/v1/' + action;
    return handlePipeline(new Request(ORIGIN + path, { method: 'POST', body: raw,
      headers: signRequest({ secret: environment.KFM_PIPELINE_WORKER_SECRET, method: 'POST', path, body: raw, now }) }), { store, files, environment, now });
  };
  // Publisher transport is fixed to the fixture clock too; no real network call occurs.
  const fetcher = (url, options) => request(new URL(url).pathname.split('/').at(-1), JSON.parse(options.body));
  const transfer = (sourceId, bytes, digest = recipe, expectedActive = null) => ({ format: 'kfm-pc-release-transfer-v1', sourceId,
    recipeSha256: digest, byteLength: bytes.length, payloadSha256: sha(bytes), approval: approval(sourceId, digest), expectedActive });
  return { store, request, fetcher, transfer, options: { store, environment, now } };
}

test('actual pre-county recipe and stale delegations refuse all five prior transport sources without mutating heads', async t => {
  const f = await fixture(t);
  for (const sourceId of priorSources) {
    const bytes = Buffer.from(canonical({ synthetic: sourceId })), m = f.transfer(sourceId, bytes, previous), id = sha(canonical(m));
    f.store.rows.set(id, { id, sourceId, manifest: m, state: 'COMMITTED', projection: JSON.parse(bytes) }); f.store.heads.set(sourceId, id);
    const before = canonical([...f.store.rows]), beforeHeads = canonical([...f.store.heads]);
    for (const [body, code] of [[m, 'RECIPE_CHANGED'], [{ ...m, recipeSha256: recipe }, 'APPROVAL_INVALID']]) {
      const response = await f.request('stage', body); assert.equal((await response.json()).error, code);
    }
    const forged = structuredClone(m); forged.recipeSha256 = recipe; forged.approval.profile.recipeSha256 = recipe;
    assert.equal((await (await f.request('stage', forged)).json()).error, 'APPROVAL_INVALID');
    assert.equal(canonical([...f.store.rows]), before); assert.equal(canonical([...f.store.heads]), beforeHeads);
  }
});

test('each registered source requires a valid source-specific target delegation with its correct role', async t => {
  const f = await fixture(t);
  for (const sourceId of SOURCES) {
    const signed = approval(sourceId, recipe);
    assert.equal(verifyProfile(signed, environment.KFM_PIPELINE_APPROVER_PUBLIC_KEY, { now, recipe, sourceId }).role,
      ['water', 'weather'].includes(sourceId) ? 'governed-package' : 'external-context');
    const m = f.transfer(sourceId, Buffer.from('{}'));
    assert.equal((await f.request('stage', m)).status, 200); // Admission only; governed content still needs its domain validator at commit.
    assert.throws(() => verifyProfile(approval(sourceId, previous), environment.KFM_PIPELINE_APPROVER_PUBLIC_KEY, { now, recipe, sourceId }), /APPROVAL_INVALID/);
  }
});

test('three old feed releases retain download bytes; replacement delegations allow distinct new signed publications', async t => {
  const f = await fixture(t), ids = [];
  for (const sourceId of feeds) {
    const { bytes, product } = await payload(sourceId), old = f.transfer(sourceId, bytes, previous), id = sha(canonical(old));
    f.store.rows.set(id, { id, sourceId, manifest: old, state: 'COMMITTED', projection: product }); f.store.heads.set(sourceId, id);
    const before = canonical(await f.store.release(id));
    assert.equal((await publicContext(sourceId, f.options)).releaseId, id);
    assert.deepEqual(await publicArtifact(sourceId, f.options, id), bytes);
    const m = f.transfer(sourceId, bytes, recipe, id), result = await publish(m, bytes, environment.KFM_PIPELINE_WORKER_SECRET, { fetcher: f.fetcher });
    assert.equal(result.state, 'COMMITTED'); assert.equal(result.releaseId, sha(canonical(m))); assert.notEqual(result.releaseId, id);
    assert.equal((await publicContext(sourceId, f.options)).releaseId, result.releaseId);
    assert.deepEqual(await publicArtifact(sourceId, f.options, id), bytes); assert.equal(canonical(await f.store.release(id)), before);
    await assert.rejects(publicContext(sourceId, { ...f.options, environment: { ...environment, KFM_PIPELINE_REVOKED_PROFILES: old.approval.profile.id } }, id), /APPROVAL_REVOKED/);
    await assert.rejects(publicContext(sourceId, { ...f.options, now: now + 86400001 }, id), /APPROVAL_INVALID/);
    ids.push(result.releaseId);
  }
  assert.equal(new Set(ids).size, 3); assert.equal(f.store.rows.size, 6);
});
