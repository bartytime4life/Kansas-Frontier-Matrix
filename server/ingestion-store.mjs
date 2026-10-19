import { createHash, randomBytes } from "node:crypto";
import { ARCHIVE_LIMIT_BYTES, CHUNK_BYTES, INGEST_SCHEMA_VERSION, RECEIPT_ALLOWANCE, ingestionConfig } from "./ingestion-config.mjs";
let pool;
export async function getIngestionStore() {
  const config = ingestionConfig();
  if (!config.database || !config.tls) throw new Error("STORAGE_NOT_CONFIGURED");
  if (!pool) {
    const mysql = await import("mysql2/promise");
    const port = Number(process.env.DB_PORT ?? "3306");
    if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error("STORAGE_NOT_CONFIGURED");
    pool = mysql.createPool({ host: process.env.DB_HOST, port, database: process.env.DB_NAME, user: process.env.DB_USER, password: process.env.DB_PASSWORD,
      ssl: { ca: process.env.KFM_DB_CA_PEM, rejectUnauthorized: true, verifyIdentity: true }, connectionLimit: 3, queueLimit: 8, connectTimeout: 8_000,
      multipleStatements: false, enableKeepAlive: true, supportBigNumbers: true, bigNumberStrings: true });
  }
  return new MySqlIngestionStore(pool);
}
export class MySqlIngestionStore {
  constructor(database) { this.database = database; }
  async transaction(work) {
    const connection = await this.database.getConnection();
    try { await connection.beginTransaction(); const value = await work(connection); await connection.commit(); return value; }
    catch (error) { await connection.rollback(); throw error; }
    finally { connection.release(); }
  }
  async control(connection = this.database, lock = false) {
    const [rows] = await connection.execute(`SELECT * FROM kfm_ingest_control WHERE id=1${lock ? " FOR UPDATE" : ""}`);
    const row = rows[0];
    if (!row || Number(row.schema_version) !== INGEST_SCHEMA_VERSION || Number(row.limit_bytes) !== ARCHIVE_LIMIT_BYTES) throw new Error("SCHEMA_NOT_READY");
    return row;
  }
  async status() {
    const row = await this.control();
    const [jobs] = await this.database.execute("SELECT source_id,state,last_error,checked_at,retry_at,attempts FROM kfm_ingest_jobs");
    const [totals] = await this.database.execute("SELECT COUNT(*) AS capture_count FROM kfm_ingest_captures");
    return { paused: Boolean(row.paused), limitBytes: ARCHIVE_LIMIT_BYTES, usedBytes: Number(row.used_bytes), reservedBytes: Number(row.reserved_bytes),
      captures: Number(totals[0].capture_count), lastTick: row.last_tick ? Number(row.last_tick) : null,
      sources: jobs.map(job => ({ id: job.source_id, state: job.state, lastError: job.last_error, checkedAt: job.checked_at ? Number(job.checked_at) : null, retryAt: Number(job.retry_at), attempts: Number(job.attempts) })) };
  }
  async setPaused(paused, actor) {
    await this.transaction(async connection => { await this.control(connection, true);
      await connection.execute("UPDATE kfm_ingest_control SET paused=?,last_actor=? WHERE id=1", [Boolean(paused), actor]); });
  }
  async claim(at = Date.now(), actor = "capture-worker") {
    return this.transaction(async connection => {
      const control = await this.control(connection, true);
      if (control.paused || Number(control.lease_until) > at) return null;
      const token = randomBytes(32).toString("hex");
      // Bounded tick: 3 x 20-second upstream timeout; 3-minute fencing lease.
      // An expired worker cannot commit after a newer claim. Interrupted reservations clear here.
      await connection.execute("UPDATE kfm_ingest_control SET lease_token=?,lease_until=?,reserved_bytes=0,last_tick=?,last_actor=? WHERE id=1", [token, at + 180_000, at, actor]);
      return token;
    });
  }
  async fenced(connection, token) {
    const control = await this.control(connection, true);
    if (control.lease_token !== token || Number(control.lease_until) <= Date.now()) throw new Error("LEASE_LOST");
    if (control.paused) throw new Error("PIPELINE_PAUSED");
    return control;
  }
  async due(request, token, at = Date.now()) {
    return this.transaction(async connection => {
      await this.fenced(connection, token);
      const [captured] = await connection.execute("SELECT capture_id FROM kfm_ingest_captures WHERE capture_id=?", [request.id]);
      if (captured.length) return false;
      const [jobs] = await connection.execute("SELECT * FROM kfm_ingest_jobs WHERE source_id=?", [request.sourceId]);
      if (jobs[0]?.capture_id === request.id && (Number(jobs[0].retry_at) > at || Number(jobs[0].attempts) >= 3)) return false;
      return true;
    });
  }
  async reserve(request, token) {
    const amount = request.limitBytes + RECEIPT_ALLOWANCE;
    await this.transaction(async connection => {
      const control = await this.fenced(connection, token);
      if (Number(control.used_bytes) + Number(control.reserved_bytes) + amount > ARCHIVE_LIMIT_BYTES) throw new Error("ARCHIVE_LIMIT_REACHED");
      await connection.execute("UPDATE kfm_ingest_control SET reserved_bytes=reserved_bytes+? WHERE id=1", [amount]);
    });
    return amount;
  }
  async save(request, capture, token, reservation) {
    const receipt = JSON.stringify(capture.receipt);
    const accounted = capture.bytes.length + Buffer.byteLength(receipt) + 8192;
    if (accounted > reservation || capture.bytes.length > request.limitBytes || capture.receipt.captureId !== request.id || capture.receipt.sha256 !== createHash("sha256").update(capture.bytes).digest("hex")) throw new Error("CAPTURE_INTEGRITY_FAILED");
    await this.transaction(async connection => {
      const control = await this.fenced(connection, token);
      if (Number(control.reserved_bytes) < reservation || Number(control.used_bytes) + accounted > ARCHIVE_LIMIT_BYTES) throw new Error("ARCHIVE_LIMIT_REACHED");
      await connection.execute("INSERT INTO kfm_ingest_captures (capture_id,source_id,slot,sha256,byte_length,accounted_bytes,receipt,validation,retrieved_at) VALUES (?,?,?,?,?,?,?,?,?)",
        [request.id, request.sourceId, request.slot, capture.receipt.sha256, capture.bytes.length, accounted, receipt, capture.receipt.validation, capture.receipt.retrievedAt]);
      for (let offset = 0, index = 0; offset < capture.bytes.length; offset += CHUNK_BYTES, index++) {
        await connection.execute("INSERT INTO kfm_ingest_chunks (capture_id,chunk_index,entity_bytes) VALUES (?,?,?)", [request.id, index, capture.bytes.subarray(offset, offset + CHUNK_BYTES)]);
      }
      await connection.execute("UPDATE kfm_ingest_control SET used_bytes=used_bytes+?,reserved_bytes=reserved_bytes-? WHERE id=1", [accounted, reservation]);
      await connection.execute("INSERT INTO kfm_ingest_jobs (source_id,capture_id,slot,state,checked_at) VALUES (?,?,?,?,?) ON DUPLICATE KEY UPDATE capture_id=VALUES(capture_id),slot=VALUES(slot),state=VALUES(state),checked_at=VALUES(checked_at),attempts=0,retry_at=0,last_error=NULL",
        [request.sourceId, request.id, request.slot, capture.receipt.validation === "invalid" ? "quarantined-invalid" : "quarantined", Date.now()]);
    });
  }
  async failure(request, token, code, reservation = 0) {
    await this.transaction(async connection => {
      const control = await this.fenced(connection, token);
      const [rows] = await connection.execute("SELECT capture_id,attempts FROM kfm_ingest_jobs WHERE source_id=?", [request.sourceId]);
      const attempts = rows[0]?.capture_id === request.id ? Number(rows[0].attempts) + 1 : 1;
      await connection.execute("UPDATE kfm_ingest_control SET reserved_bytes=? WHERE id=1", [Math.max(0, Number(control.reserved_bytes) - reservation)]);
      await connection.execute("INSERT INTO kfm_ingest_jobs (source_id,capture_id,slot,attempts,retry_at,state,last_error,checked_at) VALUES (?,?,?,?,?,?,?,?) ON DUPLICATE KEY UPDATE capture_id=VALUES(capture_id),slot=VALUES(slot),attempts=VALUES(attempts),retry_at=VALUES(retry_at),state=VALUES(state),last_error=VALUES(last_error),checked_at=VALUES(checked_at)",
        [request.sourceId, request.id, request.slot, attempts, Date.now() + Math.min(3_600_000, 300_000 * 2 ** Math.min(attempts - 1, 3)), "retry-held", code, Date.now()]);
    });
  }
  async release(token) { await this.database.execute("UPDATE kfm_ingest_control SET lease_token=NULL,lease_until=0,reserved_bytes=0 WHERE id=1 AND lease_token=?", [token]); }
  async list() {
    const [rows] = await this.database.execute("SELECT receipt FROM kfm_ingest_captures ORDER BY slot DESC,capture_id LIMIT 50");
    return rows.map(row => JSON.parse(row.receipt));
  }
  async read(id) {
    if (!/^[a-f0-9]{64}$/.test(id)) throw new Error("CAPTURE_NOT_FOUND");
    const [rows] = await this.database.execute("SELECT receipt,byte_length,sha256 FROM kfm_ingest_captures WHERE capture_id=?", [id]);
    const row = rows[0]; if (!row) throw new Error("CAPTURE_NOT_FOUND");
    if (Number(row.byte_length) > 8 * 1024 * 1024) throw new Error("CAPTURE_INTEGRITY_FAILED");
    const [chunks] = await this.database.execute("SELECT chunk_index,entity_bytes FROM kfm_ingest_chunks WHERE capture_id=? ORDER BY chunk_index", [id]);
    const bytes = Buffer.concat(chunks.map((chunk, index) => { if (Number(chunk.chunk_index) !== index) throw new Error("CAPTURE_INTEGRITY_FAILED"); return chunk.entity_bytes; }));
    if (bytes.length !== Number(row.byte_length) || createHash("sha256").update(bytes).digest("hex") !== row.sha256) throw new Error("CAPTURE_INTEGRITY_FAILED");
    return { bytes, receipt: JSON.parse(row.receipt) };
  }
}
