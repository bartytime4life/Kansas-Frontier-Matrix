#!/usr/bin/env node
/** Bounded offline candidate repair. Run repairs under the shared operation lock. */
import { DatabaseSync } from 'node:sqlite';
import { readdir, lstat } from 'node:fs/promises';
import { resolve, basename } from 'node:path';
import { fileURLToPath } from 'node:url';
import { PC_CAPTURE_IDS } from '../../app/pipeline-catalog.mjs';
import { readConfig } from './config.mjs';
import { captureRequest } from '../../server/ingestion-sources.mjs';
import { normalizeCapture, validateContext } from '../../server/pipeline-normalize.mjs';
import { canonical, sha, parse, fail, recipeDigest } from '../../server/pipeline-contract.mjs';
import { readRegular, immutable, directory, storageGuard } from '../../server/pipeline-files.mjs';
const safe = error => /^[A-Z][A-Z_]{1,63}$/.test(error?.message ?? '') ? error.message : 'REVALIDATION_FAILED';
export async function revalidateCandidates(config, { repair = false, guard = storageGuard } = {}) {
  if (repair && (config.publish !== false || config.remoteMode !== 'connection-only')) fail('PRIVATE_CANDIDATE_REPAIR_ONLY');
  await guard(config, { reserve: 64 * 1024 ** 2 });
  const path = resolve(config.root, 'pipeline-journal.sqlite'); await directory(config.root);
  const info = await lstat(path); if (!info.isFile() || info.isSymbolicLink()) fail('JOURNAL_INVALID');
  for (const suffix of ['-wal','-shm','-journal']) {
    try { if ((await lstat(path + suffix)).isSymbolicLink()) fail('JOURNAL_INVALID'); }
    catch (error) { if (error.code !== 'ENOENT') throw error; }
  }
  const db = new DatabaseSync(path, { readOnly: !repair });
  db.exec('PRAGMA trusted_schema=OFF; PRAGMA busy_timeout=5000');
  let receipts, totalBytes = 0;
  async function matchingReceipt(product) {
    if (!receipts) {
      receipts = new Map();
      const parent = resolve(config.root, 'data/receipts/ingest/pc-pipeline');
      const entries = await readdir(parent); if (entries.length > 10000) fail('REVALIDATION_RECEIPT_LIMIT');
      let receiptBytes = 0;
      for (const name of entries) {
        if (!/^[a-f0-9]{64}\.json$/.test(name)) continue;
        const bytes = await readRegular(resolve(parent, name), 65536);
        receiptBytes += bytes.length; if (receiptBytes > 64 * 1024 ** 2) fail('REVALIDATION_RECEIPT_LIMIT');
        if (sha(bytes) !== basename(name, '.json')) fail('RECEIPT_INTEGRITY_FAILED');
        const receipt = parse(bytes, 65536);
        const key = [receipt.captureId, receipt.sha256, receipt.retrievedAt].join(':');
        if (receipts.has(key)) fail('CAPTURE_RECEIPT_AMBIGUOUS');
        receipts.set(key, receipt);
      }
    }
    const receipt = receipts.get([product.captureId, product.captureSha256, product.retrievedAt].join(':'));
    if (!receipt) fail('CAPTURE_RECEIPT_REQUIRED');
    return receipt;
  }
  const result = { format: 'kfm-candidate-revalidation-v1', state: 'checked', repair, valid: 0, invalid: 0, repaired: 0, held: 0, items: [] };
  try {
    const rows = db.prepare("SELECT source,slot,state,product_path,transfer_path FROM jobs WHERE product_path IS NOT NULL AND release_id IS NULL AND lease_token IS NULL AND state IN ('complete','held') ORDER BY source,slot LIMIT 1001").all();
    if (rows.length > 1000) fail('REVALIDATION_JOB_LIMIT');
    for (const row of rows) {
      try {
        if (!PC_CAPTURE_IDS.includes(row.source) || !new RegExp('^data/processed/' + row.source + '/[a-f0-9]{64}\\.json$').test(row.product_path)) fail('PRODUCT_PATH_INVALID');
        const bytes = await readRegular(resolve(config.root, row.product_path), 8 * 1024 ** 2);
        totalBytes += bytes.length; if (totalBytes > 512 * 1024 ** 2) fail('REVALIDATION_BYTE_LIMIT');
        if (sha(bytes) !== basename(row.product_path, '.json')) fail('PRODUCT_INTEGRITY_FAILED');
        const product = parse(bytes);
        if (product.sourceId !== row.source || Date.parse(product.bucketAt) !== row.slot) fail('PRODUCT_SOURCE_INVALID');
        try { validateContext(product); result.valid++; continue; } catch { result.invalid++; }
        if (product.sourceId !== row.source || !/^[a-f0-9]{64}$/.test(product.captureSha256 ?? '')) fail('PRODUCT_SOURCE_INVALID');
        const receipt = await matchingReceipt(product);
        const raw = await readRegular(resolve(config.root, 'data/quarantine', row.source, 'objects/sha256', product.captureSha256, 'payload'), 8 * 1024 ** 2);
        totalBytes += raw.length; if (totalBytes > 512 * 1024 ** 2) fail('REVALIDATION_BYTE_LIMIT');
        const normalized = normalizeCapture(captureRequest(row.source, row.slot), { bytes: raw, receipt });
        const newDigest = sha(normalized.bytes);
        const item = { sourceId: row.source, slot: row.slot, oldSha256: sha(bytes), newSha256: newDigest, state: repair ? 'repaired-candidate' : 'repairable-candidate' };
        if (repair) {
          await guard(config, { reserve: normalized.bytes.length + 64 * 1024 ** 2 });
          const productPath = 'data/processed/' + row.source + '/' + newDigest + '.json';
          await immutable(resolve(config.root, productPath), normalized.bytes);
          const record = Buffer.from(canonical({ format: 'kfm-candidate-revalidation-receipt-v1', ...item,
            captureSha256: product.captureSha256, originalRetrievedAt: product.retrievedAt, recipeSha256: await recipeDigest(),
            revalidatedAt: new Date().toISOString(), authority: 'PRIVATE_CANDIDATE_ONLY' }));
          await immutable(resolve(config.root, 'data/receipts/pipeline/revalidated', sha(record) + '.json'), record);
          const updated = db.prepare("UPDATE jobs SET product_path=?,transfer_path=NULL WHERE source=? AND slot=? AND product_path=? AND state=? AND transfer_path IS ? AND release_id IS NULL AND lease_token IS NULL")
            .run(productPath, row.source, row.slot, row.product_path, row.state, row.transfer_path);
          if (updated.changes !== 1) fail('REVALIDATION_JOB_CHANGED');
          result.repaired++;
        }
        result.items.push(item);
      } catch (error) { result.held++; result.items.push({ sourceId: row.source, slot: row.slot, state: 'held', reason: safe(error) }); }
      if (totalBytes > 512 * 1024 ** 2) break;
    }
    if (result.held || result.invalid > result.repaired) result.state = 'held';
    return result;
  } finally { db.close(); }
}
if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const [mode, path] = process.argv.slice(2); if (!['audit','repair'].includes(mode) || !path) fail('USE_AUDIT_OR_REPAIR_CONFIG');
    const result = await revalidateCandidates(await readConfig(resolve(path)), { repair: mode === 'repair' });
    console.log(JSON.stringify(result)); if (result.state === 'held') process.exitCode = 1;
  } catch (error) { console.error(JSON.stringify({ state: 'held', reason: safe(error) })); process.exitCode = 1; }
}
