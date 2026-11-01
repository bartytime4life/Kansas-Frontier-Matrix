// Owner-only, one-time additive pipeline tables, applied by the app itself because the hosting
// dashboard's SQL tools cannot reach this app. It acts only when KFM_PIPELINE_SCHEMA_APPLY_SHA256
// names this exact SQL, runs after the server listens, and never stops it. One log line carries
// counts and codes only: no table names, credentials or driver text. See docs/second-pc-pipeline.md.
import { readFile } from 'node:fs/promises';
import { sha } from './pipeline-contract.mjs';
import { pipelinePoolOptions } from './pipeline-store.mjs';

export const PIPELINE_TABLES = Object.freeze(['kfm_pipeline_control', 'kfm_pipeline_nonces', 'kfm_pipeline_releases', 'kfm_pipeline_heads', 'kfm_pipeline_events']);
const SCHEMA = new URL('./pipeline-schema.sql', import.meta.url);
const TABLES = "SELECT table_name AS name FROM information_schema.tables WHERE table_schema = DATABASE() AND table_type = 'BASE TABLE'";
const code = value => /^[A-Z][A-Z0-9_]{2,63}$/.test(value ?? '') ? value : undefined;

export const schemaStatements = sql => sql.replace(/--[^\n]*/g, '').split(';').map(v => v.trim()).filter(Boolean);

export async function applyPipelineSchema({
  environment = process.env, readSql = () => readFile(SCHEMA, 'utf8'), poolOptions = pipelinePoolOptions,
  connect = async options => (await import('mysql2/promise')).createConnection(options),
} = {}) {
  let result = { profile: 'kfm.pipeline-schema/v1' }, connection;
  try {
    const sql = await readSql(); result.schemaSha256 = sha(sql);
    if (environment.KFM_PIPELINE_SCHEMA_APPLY_SHA256 !== result.schemaSha256) return { ...result, state: 'held', reason: 'SCHEMA_DIGEST_MISMATCH' };
    // Same transport rule as pipeline writes: verified TLS, or the owner-approved private network.
    const { connectionLimit, queueLimit, ...options } = await poolOptions(environment);
    connection = await connect(options);
    const tables = async () => (await connection.query(TABLES))[0].map(row => String(row.name ?? row.NAME ?? row.TABLE_NAME));
    const before = await tables();
    const otherTables = before.filter(name => !PIPELINE_TABLES.includes(name)).length;
    const pipelineTablesBefore = before.filter(name => PIPELINE_TABLES.includes(name)).length;
    result = { ...result, otherTables, pipelineTablesBefore };
    // An empty database has nothing to back up; any other table needs the owner's backup assertion.
    if (otherTables > 0 && environment.KFM_PIPELINE_DATABASE_BACKUP_VERIFIED !== 'true') return { ...result, state: 'held', reason: 'DATABASE_BACKUP_REQUIRED' };
    for (const statement of schemaStatements(sql)) await connection.query(statement);
    const pipelineTables = (await tables()).filter(name => PIPELINE_TABLES.includes(name)).length;
    const [[control]] = await connection.query('SELECT schema_version, paused FROM kfm_pipeline_control WHERE id=1');
    const [[heads]] = await connection.query('SELECT COUNT(*) AS n FROM kfm_pipeline_heads');
    result = { ...result, pipelineTables, schemaVersion: Number(control?.schema_version), paused: Boolean(Number(control?.paused)), heads: Number(heads?.n) };
    if (pipelineTables !== PIPELINE_TABLES.length || result.schemaVersion !== 1) return { ...result, state: 'held', reason: 'SCHEMA_VERIFICATION_FAILED' };
    return { ...result, state: pipelineTablesBefore === PIPELINE_TABLES.length ? 'already-applied' : 'applied' };
  } catch (error) {
    return { ...result, state: 'held', reason: code(error?.message) ?? 'SCHEMA_APPLY_FAILED', ...(code(error?.code) ? { errorCode: error.code } : {}) };
  } finally {
    try { await connection?.end(); } catch { connection?.destroy?.(); }
  }
}

export async function applyPipelineSchemaOnStart(write = console.info, options) {
  const result = await applyPipelineSchema(options);
  write('KFM_PIPELINE_SCHEMA ' + JSON.stringify(result));
  return result;
}
