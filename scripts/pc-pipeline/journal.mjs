import { DatabaseSync } from 'node:sqlite';
import { randomUUID } from 'node:crypto';
import { constants } from 'node:fs';
import { open } from 'node:fs/promises';
import { directory } from '../../server/pipeline-files.mjs';
import { dirname } from 'node:path';

export class Journal {
  static async open(path) {
    await directory(dirname(path));
    const fd = await open(path, constants.O_RDWR | constants.O_CREAT | constants.O_NOFOLLOW, 0o600);
    try { if (!(await fd.stat()).isFile()) throw new Error('JOURNAL_INVALID'); } finally { await fd.close(); }
    return new Journal(new DatabaseSync(path));
  }
  constructor(db) {
    this.db = db;
    db.exec(`PRAGMA journal_mode=WAL; PRAGMA synchronous=FULL; PRAGMA busy_timeout=5000;
      CREATE TABLE IF NOT EXISTS jobs (source TEXT NOT NULL, slot INTEGER NOT NULL, state TEXT NOT NULL DEFAULT 'pending', attempts INTEGER NOT NULL DEFAULT 0,
      retry_at INTEGER NOT NULL DEFAULT 0, lease_token TEXT, lease_until INTEGER NOT NULL DEFAULT 0, product_path TEXT, transfer_path TEXT, release_id TEXT, reason TEXT,
      PRIMARY KEY(source,slot));`);
    // Additive migration: preserve old captures and leave unknown historical clocks null.
    const columns = new Set(db.prepare('PRAGMA table_info(jobs)').all().map(column => column.name));
    for (const column of ['started_at', 'finished_at', 'captured_at']) if (!columns.has(column)) db.exec(`ALTER TABLE jobs ADD COLUMN ${column} INTEGER`);
  }
  claim(source, slot, now = Date.now(), publish = false) {
    this.db.exec('BEGIN IMMEDIATE');
    try {
      this.db.prepare('INSERT OR IGNORE INTO jobs(source,slot) VALUES (?,?)').run(source, slot);
      const row = this.db.prepare('SELECT * FROM jobs WHERE source=? AND slot=?').get(source, slot);
      if ((row.state === 'complete' && !(publish && row.product_path && !row.release_id)) || row.lease_until > now || row.retry_at > now || row.attempts >= 3) { this.db.exec('COMMIT'); return null; }
      const token = randomUUID();
      this.db.prepare("UPDATE jobs SET state='running',attempts=attempts+1,lease_token=?,lease_until=?,started_at=?,finished_at=NULL WHERE source=? AND slot=?").run(token, now + 600000, now, source, slot);
      this.db.exec('COMMIT'); return { ...row, token, source, slot };
    } catch (e) { this.db.exec('ROLLBACK'); throw e; }
  }
  update(job, values, now = Date.now()) {
    const allowed = ['state','retry_at','product_path','transfer_path','release_id','reason','captured_at'];
    const entries = Object.entries(values); if (!entries.length || entries.some(([k]) => !allowed.includes(k))) throw new Error('JOURNAL_UPDATE_INVALID');
    const r = this.db.prepare('UPDATE jobs SET ' + entries.map(([k]) => k + '=?').join(',') + ' WHERE source=? AND slot=? AND lease_token=? AND lease_until>?')
      .run(...entries.map(([,v]) => v), job.source, job.slot, job.token, now);
    if (r.changes !== 1) throw new Error('LEASE_LOST');
  }
  finish(job, reason = null, now = Date.now()) {
    const r = this.db.prepare('UPDATE jobs SET state=?,reason=?,retry_at=?,lease_token=NULL,lease_until=0,finished_at=? WHERE source=? AND slot=? AND lease_token=? AND lease_until>?')
      .run(reason ? 'held' : 'complete', reason, reason ? now + 300000 * 2 ** Math.min(job.attempts, 3) : 0, now, job.source, job.slot, job.token, now);
    if (r.changes !== 1) throw new Error('LEASE_LOST');
  }
  defer(job, reason, now = Date.now()) {
    // A capacity/offline deferral does not consume a source-validation attempt.
    const r = this.db.prepare("UPDATE jobs SET state='pending',reason=?,retry_at=?,attempts=MAX(0,attempts-1),lease_token=NULL,lease_until=0,finished_at=? WHERE source=? AND slot=? AND lease_token=? AND lease_until>?")
      .run(reason, now + 300000, now, job.source, job.slot, job.token, now);
    if (r.changes !== 1) throw new Error('LEASE_LOST');
  }
  status() { return this.db.prepare('SELECT source,slot,state,attempts,retry_at,release_id,reason FROM jobs ORDER BY slot DESC LIMIT 100').all(); }
  close() { this.db.close(); }
}
