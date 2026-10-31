#!/usr/bin/env node
/** Private, read-only report. Never import this module into a hosted route. */
import { DatabaseSync } from 'node:sqlite';
import { lstat, open, writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const TARGET_BYTES = 85_000_000_000;
const STATUSES = ['ready', 'reviewed', 'review', 'blocked'];
const HOLDS = new Set(['CAPTURE_REQUIRED', 'FORMAT_UNRECOGNIZED', 'DOMAIN_UNRESOLVED', 'RIGHTS_UNKNOWN',
  'RIGHTS_RESTRICTED', 'RIGHTS_DENIED', 'SENSITIVITY_UNKNOWN', 'SENSITIVITY_SENSITIVE', 'SENSITIVITY_RESTRICTED',
  'REVIEW_FLAGS', 'GITHUB_BUDGET_EXCEEDED', 'OUTSIDE_KANSAS', 'REVIEWED_LOCAL_ONLY']);
async function sqliteFile(path) {
  const info = await lstat(path);
  if (!info.isFile() || info.isSymbolicLink()) throw new Error('CATALOG_UNAVAILABLE');
  const handle = await open(path, 'r');
  try {
    const bytes = Buffer.alloc(16);
    const read = await handle.read(bytes, 0, 16, 0);
    if (read.bytesRead !== 16 || bytes.toString() !== 'SQLite format 3\0') throw new Error('CATALOG_UNAVAILABLE');
  } finally { await handle.close(); }
  return info;
}
async function sqlUsage(catalogs) {
  try {
    let usedBytes = 0, journalBytes = 0, catalogCount = 0;
    const seen = new Set();
    for (const path of catalogs) {
      const info = await sqliteFile(path), identity = `${info.dev}:${info.ino}`;
      if (seen.has(identity)) continue;
      seen.add(identity); catalogCount++; usedBytes += info.size;
      for (const suffix of ['-wal', '-journal', '-shm']) {
        try {
          const journal = await lstat(path + suffix);
          if (!journal.isFile() || journal.isSymbolicLink()) throw new Error('CATALOG_UNAVAILABLE');
          journalBytes += journal.size;
        } catch (error) { if (error.code !== 'ENOENT') throw error; }
      }
    }
    usedBytes += journalBytes;
    if (!Number.isSafeInteger(usedBytes)) throw new Error('CATALOG_UNAVAILABLE');
    return { state: 'measured', catalogCount, usedBytes, journalBytes, targetBytes: TARGET_BYTES };
  } catch { return { state: 'unavailable', catalogCount: null, usedBytes: null, journalBytes: null, targetBytes: TARGET_BYTES }; }
}
async function intakeStatus(path) {
  let db;
  try {
    await sqliteFile(path);
    for (const suffix of ['-wal', '-shm', '-journal']) {
      try { if ((await lstat(path + suffix)).isSymbolicLink()) throw new Error('INTAKE_UNAVAILABLE'); }
      catch (error) { if (error.code !== 'ENOENT') throw error; }
    }
    db = new DatabaseSync(path, { readOnly: true });
    db.exec('PRAGMA query_only=ON; PRAGMA trusted_schema=OFF; PRAGMA busy_timeout=2000; BEGIN');
    const counts = Object.fromEntries([...STATUSES, 'other'].map(key => [key, 0]));
    for (const row of db.prepare('SELECT status,COUNT(*) AS files FROM items WHERE present=1 GROUP BY status').all()) {
      counts[STATUSES.includes(row.status) ? row.status : 'other'] += Number(row.files);
    }
    const reasons = new Map();
    const rows = db.prepare(`SELECT CASE WHEN j.value IN (${[...HOLDS].map(() => '?').join(',')}) THEN j.value ELSE 'OTHER' END AS reason,COUNT(DISTINCT i.id) AS files FROM items i,
      json_each(CASE WHEN json_valid(i.decision_json) THEN i.decision_json ELSE '{}' END, '$.holds') j
      WHERE i.present=1 GROUP BY 1`).all(...HOLDS);
    for (const row of rows) {
      const code = HOLDS.has(row.reason) ? row.reason : 'OTHER';
      // Unknown reasons are grouped without returning free text, paths or source identities.
      reasons.set(code, (reasons.get(code) ?? 0) + Number(row.files));
    }
    db.exec('ROLLBACK');
    return { state: 'measured', files: Object.values(counts).reduce((a, b) => a + b, 0), counts,
      holds: [...reasons].map(([code, files]) => ({ code, files })) };
  } catch { return { state: 'unavailable', files: null, counts: null, holds: [] }; }
  finally { db?.close(); }
}
export async function localDataStatus({ catalogs, intake, now = Date.now() }) {
  if (!Array.isArray(catalogs) || !catalogs.length || catalogs.length > 32 || !catalogs.every(path => typeof path === 'string' && path.length)
    || typeof intake !== 'string' || !intake) throw new Error('EXPLICIT_CATALOGS_AND_INTAKE_REQUIRED');
  const [sql, queue] = await Promise.all([sqlUsage(catalogs.map(path => resolve(path))), intakeStatus(resolve(intake))]);
  return { format: 'kfm-local-data-status-v1', scope: 'selected-local-catalogs', checkedAt: new Date(now).toISOString(), sql, intake: queue };
}
if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const catalogs = []; let intake, output;
    for (let i = 2; i < process.argv.length; i += 2) {
      const flag = process.argv[i], value = process.argv[i + 1];
      if (!value) throw new Error('USAGE');
      if (flag === '--catalog') catalogs.push(value);
      else if (flag === '--intake' && !intake) intake = value;
      else if (flag === '--output' && !output) output = value;
      else throw new Error('USAGE');
    }
    const report = JSON.stringify(await localDataStatus({ catalogs, intake }), null, 2) + '\n';
    if (output) await writeFile(resolve(output), report, { flag: 'wx', mode: 0o600 });
    else process.stdout.write(report);
  } catch { console.error('Report could not be created. Supply --intake FILE and one or more --catalog FILE arguments; --output must be a new file.'); process.exitCode = 1; }
}
