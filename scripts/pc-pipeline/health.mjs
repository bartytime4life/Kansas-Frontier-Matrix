#!/usr/bin/env node
/** Read-only private diagnostics. Never import this module into a public route. */
import { DatabaseSync } from 'node:sqlite';
import { lstat } from 'node:fs/promises';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { readConfig } from './config.mjs';
import { readRegular, directory, storageGuard } from '../../server/pipeline-files.mjs';
import { parse } from '../../server/pipeline-contract.mjs';
import { validateContext } from '../../server/pipeline-normalize.mjs';
import { sha } from '../../server/pipeline-contract.mjs';
import { PC_CAPTURE_IDS } from '../../app/pipeline-catalog.mjs';
const iso = n => typeof n === 'number' && Number.isFinite(n) && n > 0 ? new Date(n).toISOString() : null;
const code = error => /^[A-Z][A-Z_]{1,63}$/.test(error?.message ?? '') ? error.message : 'DIAGNOSTIC_UNAVAILABLE';
async function reader(path, work) {
  await directory(resolve(path, '..'));
  const info = await lstat(path);
  if (!info.isFile() || info.isSymbolicLink()) throw new Error('JOURNAL_INVALID');
  for (const suffix of ['-wal', '-shm', '-journal']) {
    try { if ((await lstat(path + suffix)).isSymbolicLink()) throw new Error('JOURNAL_INVALID'); }
    catch (error) { if (error.code !== 'ENOENT') throw error; }
  }
  const db = new DatabaseSync(path, { readOnly: true });
  try { db.exec('PRAGMA query_only=ON; PRAGMA trusted_schema=OFF; PRAGMA busy_timeout=2000'); return work(db); }
  finally { db.close(); }
}
export async function journalHealth(root, sources = PC_CAPTURE_IDS, now = Date.now()) {
  const results = await reader(resolve(root, 'pipeline-journal.sqlite'), db => {
    const columns = new Set(db.prepare('PRAGMA table_info(jobs)').all().map(c => c.name));
    const clocks = ['started_at', 'finished_at', 'captured_at'].map(name => columns.has(name) ? name : `NULL AS ${name}`).join(',');
    return sources.map(sourceId => {
      const row = db.prepare(`SELECT source,slot,state,attempts,retry_at,lease_until,release_id,reason,product_path,${clocks} FROM jobs WHERE source=? ORDER BY slot DESC LIMIT 1`).get(sourceId);
      const successful = db.prepare(`SELECT ${clocks} FROM jobs WHERE source=? AND product_path IS NOT NULL ORDER BY slot DESC LIMIT 1`).get(sourceId);
      const slot = Math.floor(now / 3600000) * 3600000;
      // Match the worker's current-slot eligibility; never promise a fourth retry.
      const sameSlot = row?.slot === slot;
      const next = !sameSlot ? slot : row.state === 'complete' || row.attempts >= 3 ? slot + 3600000 : Math.max(now, row.retry_at, row.lease_until);
      return { sourceId, productPath: row?.product_path, state: row?.state ?? 'not-started', attempts: row?.attempts ?? 0, reason: /^[A-Z][A-Z_]{1,63}$/.test(row?.reason ?? '') ? row.reason : null,
        exhausted: row?.state !== 'complete' && (row?.attempts ?? 0) >= 3,
        lastAttemptAt: iso(row?.started_at), lastFinishedAt: iso(row?.finished_at),
        lastSuccessfulCaptureAt: iso(successful?.captured_at), nextEligibleAt: iso(Math.min(next, slot + 3600000)),
        retryAt: row?.state === 'held' && row.attempts < 3 ? iso(row.retry_at) : null,
        releaseId: /^[a-f0-9]{64}$/.test(row?.release_id ?? '') ? row.release_id : null,
      };
    });
  });
  for (const job of results) {
    const productPath = job.productPath; delete job.productPath;
    job.candidateState = 'not-checked';
    if (!productPath) continue;
    try {
      if (!new RegExp('^data/processed/' + job.sourceId + '/[a-f0-9]{64}\\.json$').test(productPath)) throw new Error('PRODUCT_PATH_INVALID');
      const bytes = await readRegular(resolve(root, productPath), 8 * 1024 ** 2);
      if (sha(bytes) !== productPath.split('/').at(-1).slice(0, -5)) throw new Error('PRODUCT_INTEGRITY_FAILED');
      const product = validateContext(parse(bytes));
      if (product.sourceId !== job.sourceId) throw new Error('PRODUCT_SOURCE_INVALID');
      job.candidateState = 'valid';
    } catch (error) { job.candidateState = 'invalid'; job.candidateReason = code(error); }
  }
  return results;

}
async function receipt(path, now, maxAge) {
  try {
    const value = parse(await readRegular(path, 65536));
    const info = await lstat(path);
    const verified = ['verified-copy', 'verified'].includes(value.state);
    // Legacy backup receipts have no source timestamp: label the filesystem clock separately.
    const at = typeof value.restoredAt === 'string' && Number.isFinite(Date.parse(value.restoredAt)) ? value.restoredAt : null;
    const ageFrom = at ? Date.parse(at) : info.mtimeMs;
    return { state: verified ? now - ageFrom > maxAge ? 'overdue' : value.state : 'unverified',
      receiptTime: at, receiptFileModifiedAt: iso(info.mtimeMs), files: Number.isSafeInteger(value.files) ? value.files : null,
      matchesLatestBackup: null };
  } catch (error) { return { state: 'unavailable', reason: code(error) }; }
}
export function operatorState(report) {
  return report.storage?.state === 'qualified' && Array.isArray(report.jobs)
    && !report.jobs.some(job => job.state === 'held' || job.exhausted || job.candidateState === 'invalid') && report.intake?.state === 'indexed'
    && !['overdue', 'unavailable', 'unverified'].includes(report.backup?.state)
    && !['overdue', 'unavailable', 'unverified'].includes(report.restore?.state)
    && report.lastTick?.state !== 'held' ? 'checked' : 'degraded';
}
function tickRecord(value) {
  if (!value || !['complete', 'held'].includes(value.state) || typeof value.finishedAt !== 'string' || !Number.isFinite(Date.parse(value.finishedAt))) return null;
  return { state: value.state, finishedAt: new Date(value.finishedAt).toISOString(), reason: /^[A-Z][A-Z_]{1,63}$/.test(value.reason ?? '') ? value.reason : null };
}
export async function operatorHealth(configPath, runDirectory, { now = Date.now(), guard = storageGuard } = {}) {
  const config = await readConfig(resolve(configPath));
  let storage;
  try { storage = { state: 'qualified', ...await guard(config) }; }
  catch (error) { return { format: 'kfm-pipeline-operator-health-v1', checkedAt: iso(now), state: 'held', storage: { state: 'held', reason: code(error) } }; }
  let jobs, intake, lastTick = null;
  try { lastTick = tickRecord(parse(await readRegular(resolve(config.root, 'data/work/pipeline-health.json'), 65536)).lastTick); }
  catch { /* No earlier report is a normal first-run state. */ }
  try { jobs = await journalHealth(config.root, config.sources, now); } catch (error) { jobs = { state: 'unavailable', reason: code(error) }; }
  try {
    intake = await reader(resolve(config.root, 'data/work/intake/index.sqlite'), db => ({ state: 'indexed',
      byStatus: db.prepare('SELECT status,COUNT(*) AS files FROM items WHERE present=1 GROUP BY status').all() }));
  } catch (error) { intake = { state: 'unavailable', reason: code(error) }; }
  const backup = await receipt(resolve(runDirectory, 'backup-last.json'), now, 36 * 3600000);
  const restore = await receipt(resolve(runDirectory, 'restore-last.json'), now, 35 * 86400000);
  if ('matchesLatestBackup' in restore) {
    try {
      const a = parse(await readRegular(resolve(runDirectory, 'backup-last.json'), 65536));
      const b = parse(await readRegular(resolve(runDirectory, 'restore-last.json'), 65536));
      restore.matchesLatestBackup = typeof a.inventorySha256 === 'string' && a.inventorySha256 === b.inventorySha256;
    } catch { /* Missing receipts are already explicit. */ }
  }
  const report = { format: 'kfm-pipeline-operator-health-v1', checkedAt: iso(now), state: 'checked',
    publication: config.publish ? 'approved-profiles-required' : 'disabled', remoteMode: config.remoteMode ?? 'delegated-publication',
    storage, jobs, intake, lastTick, backup, restore, preservedArchiveBackup: { state: 'needs-independent-full-size-backup' } };
  report.state = operatorState(report);
  return report;
}
export function backfillPlan(sourceId, from, through, now = Date.now()) {
  if (!PC_CAPTURE_IDS.includes(sourceId)) throw new Error('SOURCE_NOT_ALLOWED');
  const begin = Date.parse(from), end = Date.parse(through);
  if (![begin, end].every(Number.isFinite) || begin % 3600000 || end % 3600000 || end < begin || end > now || end - begin > 31 * 86400000) throw new Error('BACKFILL_WINDOW_INVALID');
  // The upstream latest-continuous and active-alert products cannot reconstruct missed snapshots.
  return { format: 'kfm-pipeline-backfill-plan-v1', sourceId, from: new Date(begin).toISOString(), through: new Date(end).toISOString(),
    requestedSlots: (end - begin) / 3600000 + 1, executable: false, state: 'held',
    reason: 'HISTORICAL_PRODUCT_REQUIRED', networkAccess: false, originalSnapshotsPreserved: true };
}
if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const [command, ...args] = process.argv.slice(2);
    const result = command === 'backfill-plan' ? backfillPlan(...args) : command === 'status' && args.length === 2 ? await operatorHealth(...args) : null;
    if (!result) throw new Error('USE_STATUS_OR_BACKFILL_PLAN');
    console.log(JSON.stringify(result));
  } catch (error) { console.error(JSON.stringify({ state: 'held', reason: code(error) })); process.exitCode = 1; }
}
