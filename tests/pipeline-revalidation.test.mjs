import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, readFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { resolve } from 'node:path';
import { DatabaseSync } from 'node:sqlite';
import { Journal } from '../scripts/pc-pipeline/journal.mjs';
import { revalidateCandidates } from '../scripts/pc-pipeline/revalidate.mjs';
import { captureRequest, fetchCapture } from '../server/ingestion-sources.mjs';
import { normalizeCapture, validateContext } from '../server/pipeline-normalize.mjs';
import { immutable } from '../server/pipeline-files.mjs';
import { canonical, sha } from '../server/pipeline-contract.mjs';
const now = Date.now(), request = captureRequest('usgs-streamflow', now);
async function capture(qualifier) {
  return fetchCapture(request, { fetcher: async () => Response.json({ type: 'FeatureCollection', features: [{ type: 'Feature', id: 'fixture-gauge',
    geometry: { type: 'Point', coordinates: [-98, 38] }, properties: { parameter_code: '00060', monitoring_location_id: 'USGS-fixture',
      time: new Date(request.slot).toISOString(), value: '1.5', unit_of_measure: 'ft^3/s', approval_status: 'Provisional', qualifier } }] }) });
}
test('source-shaped USGS qualifier arrays are preserved and invalid qualifiers cannot complete normalization', async () => {
  for (const [input, expected] of [[null, []], ['Ice', ['Ice']], [['Ice'], ['Ice']], [[], []], [Array(16).fill('A'), Array(16).fill('A')]]) {
    const result = normalizeCapture(request, await capture(input));
    assert.deepEqual(result.product.data.features[0].properties.qualifiers, expected); validateContext(result.product);
  }
  for (const input of [Array(17).fill('A'), [null], { unexpected: 'value' }]) {
    const raw = await capture(input); assert.throws(() => normalizeCapture(request, raw), /STREAMFLOW_SCHEMA_CHANGED/);
  }
});
test('offline repair preserves raw bytes and old candidates, binds receipts, and changes only the private job pointer', async t => {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-revalidate-')); t.after(() => rm(root, { recursive: true, force: true }));
  const raw = await capture(['Ice']); const normalized = normalizeCapture(request, raw);
  const old = structuredClone(normalized.product); old.data.features[0].properties.qualifiers = [null];
  const bytes = Buffer.from(canonical(old)), path = 'data/processed/usgs-streamflow/' + sha(bytes) + '.json';
  await immutable(resolve(root, path), bytes);
  const rawPath = resolve(root, 'data/quarantine/usgs-streamflow/objects/sha256', sha(raw.bytes), 'payload');
  await immutable(rawPath, raw.bytes);
  const receipt = Buffer.from(canonical(raw.receipt)); await immutable(resolve(root, 'data/receipts/ingest/pc-pipeline', sha(receipt) + '.json'), receipt);
  let journal = await Journal.open(resolve(root, 'pipeline-journal.sqlite'));
  const transferPath = 'data/receipts/pipeline/transfers/' + 'a'.repeat(64) + '.json';
  const transferBytes = Buffer.from(canonical({ payloadSha256: sha(bytes), byteLength: bytes.length }));
  await immutable(resolve(root, transferPath), transferBytes);
  const job = journal.claim(request.sourceId, request.slot); journal.update(job, { product_path: path, transfer_path: transferPath }); journal.finish(job); journal.close();
  const config = { root, publish: false, remoteMode: 'connection-only' }, guard = async () => ({});
  const audit = await revalidateCandidates(config, { guard }); assert.equal(audit.invalid, 1); assert.equal(audit.repaired, 0);
  assert.equal(audit.items[0].state, 'repairable-candidate');
  const repaired = await revalidateCandidates(config, { repair: true, guard }); assert.equal(repaired.repaired, 1); assert.equal(repaired.state, 'checked');
  assert.deepEqual(await readFile(resolve(root, path)), bytes); assert.deepEqual(await readFile(rawPath), raw.bytes);
  assert.deepEqual(await readFile(resolve(root, transferPath)), transferBytes, 'old transfer bytes remain immutable');
  const db = new DatabaseSync(resolve(root, 'pipeline-journal.sqlite'), { readOnly: true });
  try { const row = db.prepare('SELECT product_path,transfer_path FROM jobs').get();
    assert.notEqual(row.product_path, path); assert.equal(row.transfer_path, null, 'a future authorized attempt must create a matching manifest');
  } finally { db.close(); }
  const replay = await revalidateCandidates(config, { repair: true, guard }); assert.equal(replay.repaired, 0); assert.equal(replay.valid, 1);
  await assert.rejects(revalidateCandidates({ ...config, publish: true }, { repair: true, guard }), /PRIVATE_CANDIDATE_REPAIR_ONLY/);
});


test('a valid empty earthquake candidate passes the same offline audit without changing pointers', async t => {
  const root = await mkdtemp(resolve(tmpdir(), 'kfm-quake-revalidate-'));
  t.after(() => rm(root, { recursive: true, force: true }));
  const req = captureRequest('usgs-earthquakes', now);
  const raw = await fetchCapture(req, { fetcher: async () => Response.json({ type: 'FeatureCollection', features: [] }) });
  const normalized = normalizeCapture(req, raw);
  const path = 'data/processed/usgs-earthquakes/' + sha(normalized.bytes) + '.json';
  await immutable(resolve(root, path), normalized.bytes);
  const journal = await Journal.open(resolve(root, 'pipeline-journal.sqlite'));
  const job = journal.claim(req.sourceId, req.slot); journal.update(job, { product_path: path }); journal.finish(job); journal.close();
  const result = await revalidateCandidates({ root, publish: false, remoteMode: 'connection-only' }, { guard: async () => ({}) });
  assert.equal(result.state, 'checked'); assert.equal(result.valid, 1); assert.equal(result.held, 0);
  assert.deepEqual(await readFile(resolve(root, path)), normalized.bytes);
});
