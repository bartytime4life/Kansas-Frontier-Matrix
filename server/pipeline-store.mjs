import { fail, parse, canonical, sha } from './pipeline-contract.mjs';

export class PipelineStore {
  constructor(pool) { this.pool = pool; }
  async transaction(work) {
    const c = await this.pool.getConnection();
    try { await c.beginTransaction(); const value = await work(c); await c.commit(); return value; }
    catch (e) { await c.rollback(); throw e; } finally { c.release(); }
  }
  async ready(c = this.pool, lock = false) {
    const [rows] = await c.execute('SELECT schema_version,paused FROM kfm_pipeline_control WHERE id=1' + (lock ? ' FOR UPDATE' : ''));
    if (rows[0]?.schema_version !== 1) fail('PIPELINE_SCHEMA_REQUIRED');
    return rows[0];
  }
  async claimNonce(nonce, now) {
    return this.transaction(async c => {
      // Serialize the bounded nonce ledger and admissions under one small control row.
      await this.ready(c, true);
      await c.execute('DELETE FROM kfm_pipeline_nonces WHERE expires < ?', [now]);
      const [count] = await c.execute('SELECT COUNT(*) AS n FROM kfm_pipeline_nonces');
      if (Number(count[0].n) >= 4096) return false;
      const [r] = await c.execute('INSERT IGNORE INTO kfm_pipeline_nonces (nonce,expires) VALUES (?,?)', [nonce, now + 120000]);
      return r.affectedRows === 1;
    });
  }
  async heartbeat(state, now) { await this.pool.execute('UPDATE kfm_pipeline_control SET worker_seen=?,worker_state=? WHERE id=1', [now, state]); return { receivedAt: now }; }
  async release(id, c = this.pool) {
    const [rows] = await c.execute('SELECT release_id,source_id,manifest_json,state,projection_json,created_at FROM kfm_pipeline_releases WHERE release_id=?', [id]);
    const r = rows[0]; return r ? { id: r.release_id, sourceId: r.source_id, manifest: parse(r.manifest_json), state: r.state, projection: r.projection_json ? parse(r.projection_json) : null, createdAt: Number(r.created_at) } : null;
  }
  async stage(id, manifest, now) {
    return this.transaction(async c => {
      const control = await this.ready(c, true); if (control.paused) fail('PIPELINE_PAUSED');
      const existing = await this.release(id, c);
      if (existing) { if (canonical(existing.manifest) !== canonical(manifest)) fail('RELEASE_CONFLICT'); return existing; }
      const [counts] = await c.execute("SELECT COUNT(*) AS n,COALESCE(SUM(CAST(JSON_UNQUOTE(JSON_EXTRACT(manifest_json,'$.byteLength')) AS UNSIGNED)),0) AS used_bytes FROM kfm_pipeline_releases");
      // Explicit initial projection budget; it is not a provider capacity declaration.
      if (Number(counts[0].n) >= 10000 || Number(counts[0].used_bytes) + manifest.byteLength > 1024 ** 3) fail('PROJECTION_BUDGET_REACHED');
      await c.execute('INSERT INTO kfm_pipeline_releases (release_id,source_id,manifest_json,created_at) VALUES (?,?,?,?)', [id, manifest.sourceId, canonical(manifest), now]);
      return this.release(id, c);
    });
  }
  async commit(id, expected, projection, now) {
    return this.transaction(async c => {
      const control = await this.ready(c, true); if (control.paused) fail('PIPELINE_PAUSED');
      const r = await this.release(id, c); if (!r || r.state === 'WITHDRAWN') fail('RELEASE_NOT_STAGED');
      const [heads] = await c.execute('SELECT release_id,revision FROM kfm_pipeline_heads WHERE source_id=? FOR UPDATE', [r.sourceId]);
      const head = heads[0]; if (!head) fail('PIPELINE_SCHEMA_REQUIRED');
      // A committed retry never silently reactivates a superseded release.
      if (r.state === 'COMMITTED') return { releaseId: id, active: head.release_id === id, revision: Number(head.revision) };
      if ((head.release_id ?? null) !== expected) fail('ACTIVATION_CONFLICT');
      await c.execute("UPDATE kfm_pipeline_releases SET projection_json=?,state='COMMITTED' WHERE release_id=?", [canonical(projection), id]);
      await c.execute('UPDATE kfm_pipeline_heads SET previous_id=release_id,release_id=?,revision=revision+1 WHERE source_id=?', [id, r.sourceId]);
      await c.execute('INSERT INTO kfm_pipeline_events (event_id,source_id,release_id,previous_id,action,occurred_at) VALUES (?,?,?,?,?,?)', [sha('activate:' + id), r.sourceId, id, expected, 'ACTIVATE', now]);
      return { releaseId: id, active: true, revision: Number(head.revision) + 1 };
    });
  }
  async active(sourceId) {
    const [rows] = await this.pool.execute('SELECT r.release_id,r.source_id,r.manifest_json,r.state,r.projection_json,r.created_at FROM kfm_pipeline_heads h JOIN kfm_pipeline_releases r ON r.release_id=h.release_id WHERE h.source_id=?', [sourceId]);
    const r = rows[0]; return r ? { id: r.release_id, sourceId: r.source_id, manifest: parse(r.manifest_json), state: r.state, projection: r.projection_json ? parse(r.projection_json) : null } : null;
  }
  async withdraw(id, expected, now) {
    return this.transaction(async c => {
      await this.ready(c, true); const r = await this.release(id, c); if (!r) fail('RELEASE_NOT_FOUND', 404);
      const [heads] = await c.execute('SELECT release_id FROM kfm_pipeline_heads WHERE source_id=? FOR UPDATE', [r.sourceId]);
      if ((heads[0]?.release_id ?? null) !== expected) fail('ACTIVATION_CONFLICT');
      await c.execute("UPDATE kfm_pipeline_releases SET state='WITHDRAWN' WHERE release_id=?", [id]);
      await c.execute('UPDATE kfm_pipeline_heads SET previous_id=release_id,release_id=NULL,revision=revision+1 WHERE source_id=? AND release_id=?', [r.sourceId, id]);
      await c.execute('INSERT IGNORE INTO kfm_pipeline_events (event_id,source_id,release_id,previous_id,action,occurred_at) VALUES (?,?,?,?,?,?)', [sha('withdraw:' + id), r.sourceId, id, expected, 'WITHDRAW', now]);
      return { releaseId: id, state: 'WITHDRAWN' };
    });
  }
  async rollback(id, expected, eventId, now) {
    return this.transaction(async c => {
      await this.ready(c, true); const r = await this.release(id, c);
      if (!r || r.state !== 'COMMITTED') fail('ROLLBACK_TARGET_UNAVAILABLE');
      const [heads] = await c.execute('SELECT release_id,previous_id FROM kfm_pipeline_heads WHERE source_id=? FOR UPDATE', [r.sourceId]);
      if (heads[0]?.release_id !== expected || heads[0]?.previous_id !== id) fail('ROLLBACK_TARGET_MISMATCH');
      await c.execute('UPDATE kfm_pipeline_heads SET previous_id=release_id,release_id=?,revision=revision+1 WHERE source_id=?', [id, r.sourceId]);
      await c.execute('INSERT INTO kfm_pipeline_events (event_id,source_id,release_id,previous_id,action,occurred_at) VALUES (?,?,?,?,?,?)', [eventId, r.sourceId, id, expected, 'ROLLBACK', now]);
      return { releaseId: id, state: 'ROLLED_BACK' };
    });
  }
  async history(sourceId) {
    const [rows] = await this.pool.execute("SELECT release_id,manifest_json,created_at FROM kfm_pipeline_releases WHERE source_id=? AND state='COMMITTED' ORDER BY created_at DESC,release_id LIMIT 20", [sourceId]);
    return rows.map(r => ({ releaseId: r.release_id, manifest: parse(r.manifest_json, 65536), publishedAt: Number(r.created_at) }));
  }
  async status() {
    const [rows] = await this.pool.execute('SELECT worker_seen,worker_state,paused,schema_version FROM kfm_pipeline_control WHERE id=1');
    const [heads] = await this.pool.execute('SELECT source_id,release_id,revision FROM kfm_pipeline_heads');
    return { configured: true, paused: Boolean(rows[0]?.paused), workerSeen: rows[0]?.worker_seen ? Number(rows[0].worker_seen) : null, sources: heads.map(r => ({ sourceId: r.source_id, releaseId: r.release_id, revision: Number(r.revision) })) };
  }
}
const LOOKUP_TIMEOUT_MS = 5000;
/** Pool options: certificate-verified TLS, or the owner-approved provider private network. */
export async function pipelinePoolOptions(environment = process.env, lookup) {
  const shared = { database: environment.DB_NAME, user: environment.DB_USER, password: environment.DB_PASSWORD,
    connectionLimit: 3, queueLimit: 8, connectTimeout: 8000, multipleStatements: false, supportBigNumbers: true, bigNumberStrings: true };
  if (environment.KFM_DATABASE_CONNECTION_TRANSPORT === 'provider-private-network') {
    // On 2026-11-01 the owner extended the health check's approved private-network leg to pipeline
    // writes (the provider's certificate fails hostname verification). Same guard as that check: every
    // DNS answer must be private IPv4, the pool is pinned to the validated address, and there is no TLS
    // fallback. A changed provider address takes effect at the next process start.
    const { connectionOptions } = await import('./database-connection.mjs');
    const resolve = lookup ?? (await import('node:dns/promises')).lookup;
    const bounded = (host, options) => Promise.race([resolve(host, options), new Promise((_, reject) => setTimeout(() => reject(new Error('DNS_TIMEOUT')), LOOKUP_TIMEOUT_MS).unref())]);
    let selected;
    try { selected = await connectionOptions(environment, bounded); }
    catch (e) { fail(e?.message === 'DATABASE_CONFIGURATION_MISSING' ? e.message : 'DATABASE_PRIVATE_NETWORK_REQUIRED'); }
    if (selected.transport !== 'provider-private-network') fail('DATABASE_PRIVATE_NETWORK_REQUIRED');
    return { ...shared, host: selected.options.host, port: selected.options.port };
  }
  const { isIP } = await import('node:net');
  if (!['DB_HOST','DB_NAME','DB_USER','DB_PASSWORD','KFM_DB_CA_PEM'].every(k => environment[k]) || isIP(environment.DB_HOST) || environment.KFM_DB_TLS !== 'verified') fail('DATABASE_TLS_REQUIRED');
  const port = Number(environment.DB_PORT ?? 3306); if (!Number.isInteger(port) || port < 1 || port > 65535) fail('DATABASE_PORT_INVALID');
  return { ...shared, host: environment.DB_HOST, port, ssl: { ca: environment.KFM_DB_CA_PEM, rejectUnauthorized: true, verifyIdentity: true } };
}
let pool;
export async function getPipelineStore(environment = process.env) {
  if (environment.KFM_PIPELINE_ENABLED !== 'true') fail('PIPELINE_DISABLED', 404);
  if (!pool) {
    const options = await pipelinePoolOptions(environment);
    const mysql = await import('mysql2/promise');
    pool ??= mysql.createPool(options);
  }
  return new PipelineStore(pool);
}
