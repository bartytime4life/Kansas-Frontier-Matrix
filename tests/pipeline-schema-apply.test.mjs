import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { applyPipelineSchema, applyPipelineSchemaOnStart, schemaStatements, PIPELINE_TABLES } from '../server/pipeline-schema-apply.mjs';
import { sha } from '../server/pipeline-contract.mjs';

const sql = await readFile(new URL('../server/pipeline-schema.sql', import.meta.url), 'utf8');
const digest = sha(sql);
const env = { DB_HOST: 'database.example.test', DB_NAME: 'private-db', DB_USER: 'private-user', DB_PASSWORD: 'private-password',
  KFM_DATABASE_CONNECTION_TRANSPORT: 'provider-private-network', KFM_PIPELINE_SCHEMA_APPLY_SHA256: digest };
const poolOptions = async () => ({ host: '10.0.0.5', port: 3306, user: 'private-user', password: 'private-password', database: 'private-db', connectionLimit: 3, queueLimit: 8 });

/** A fake MySQL connection: base tables before, the statements it ran, and whether it was closed. */
function database(before = [], { fail } = {}) {
  const tables = new Set(before), ran = []; let ended = 0, options;
  const connection = {
    async query(text) {
      if (fail && text.startsWith(fail)) throw Object.assign(new Error("Access denied for user 'private-user' at database.example.test"), { code: 'ER_DBACCESS_DENIED_ERROR' });
      if (text.startsWith('SELECT table_name')) return [[...tables].map(name => ({ name }))];
      if (text.startsWith('SELECT schema_version')) return [tables.has('kfm_pipeline_control') ? [{ schema_version: 1, paused: 1 }] : []];
      if (text.startsWith('SELECT COUNT(*)')) return [[{ n: '6' }]];
      ran.push(text);
      const created = /^CREATE TABLE IF NOT EXISTS (\w+)/.exec(text); if (created) tables.add(created[1]);
      return [{}];
    },
    async end() { ended++; },
  };
  return { connect: async o => { options = o; return connection; }, ran, ended: () => ended, options: () => options };
}

test('an empty database gets exactly the reviewed statements, in order, and reports paused control', async () => {
  const db = database();
  const result = await applyPipelineSchema({ environment: env, poolOptions, connect: db.connect });
  assert.deepEqual(db.ran, schemaStatements(sql));
  assert.equal(db.ran.length, 7);
  assert.deepEqual(result, { profile: 'kfm.pipeline-schema/v1', schemaSha256: digest, otherTables: 0, pipelineTablesBefore: 0,
    pipelineTables: 5, schemaVersion: 1, paused: true, heads: 6, state: 'applied' });
  assert.equal(db.ended(), 1);
  // Pool-only options are not passed to a single connection.
  assert.equal(db.options().connectionLimit, undefined); assert.equal(db.options().queueLimit, undefined);
});

test('the schema statements only create tables if missing and insert-ignore seed rows', () => {
  for (const statement of schemaStatements(sql)) assert.match(statement, /^(CREATE TABLE IF NOT EXISTS kfm_pipeline_\w+ |INSERT IGNORE INTO kfm_pipeline_\w+ )/);
  assert.doesNotMatch(sql, /\b(DROP|DELETE|UPDATE|ALTER|TRUNCATE|RENAME|GRANT)\b/i);
});

test('without the exact digest nothing connects', async () => {
  for (const value of [undefined, '', 'a'.repeat(64), digest.toUpperCase()]) {
    const result = await applyPipelineSchema({ environment: { ...env, KFM_PIPELINE_SCHEMA_APPLY_SHA256: value }, poolOptions,
      connect: async () => assert.fail('must not connect') });
    assert.deepEqual([result.state, result.reason], ['held', 'SCHEMA_DIGEST_MISMATCH']);
  }
});

test('any other table holds the change until the owner asserts a backup', async () => {
  const held = database(['site_sessions', 'kfm_pipeline_control']);
  const result = await applyPipelineSchema({ environment: env, poolOptions, connect: held.connect });
  assert.deepEqual([result.state, result.reason, result.otherTables, result.pipelineTablesBefore], ['held', 'DATABASE_BACKUP_REQUIRED', 1, 1]);
  assert.deepEqual(held.ran, []); assert.equal(held.ended(), 1);
  assert.doesNotMatch(JSON.stringify(result), /site_sessions/);
  const backed = database(['site_sessions']);
  const applied = await applyPipelineSchema({ environment: { ...env, KFM_PIPELINE_DATABASE_BACKUP_VERIFIED: 'true' }, poolOptions, connect: backed.connect });
  assert.deepEqual([applied.state, applied.otherTables, applied.pipelineTables], ['applied', 1, 5]);
});

test('a database that already has the tables reports already-applied', async () => {
  const result = await applyPipelineSchema({ environment: env, poolOptions, connect: database([...PIPELINE_TABLES]).connect });
  assert.equal(result.state, 'already-applied'); assert.equal(result.pipelineTablesBefore, 5);
});

test('driver errors and refused transports are held with codes only, and the connection closes', async () => {
  const db = database([], { fail: 'CREATE TABLE IF NOT EXISTS kfm_pipeline_nonces' });
  const result = await applyPipelineSchema({ environment: env, poolOptions, connect: db.connect });
  assert.deepEqual([result.state, result.reason, result.errorCode], ['held', 'SCHEMA_APPLY_FAILED', 'ER_DBACCESS_DENIED_ERROR']);
  assert.equal(db.ended(), 1);
  assert.doesNotMatch(JSON.stringify(result), /private|database\.example|Access denied/);
  const refused = await applyPipelineSchema({ environment: env, connect: async () => assert.fail('must not connect'),
    poolOptions: async () => { throw new Error('DATABASE_PRIVATE_NETWORK_REQUIRED'); } });
  assert.deepEqual([refused.state, refused.reason], ['held', 'DATABASE_PRIVATE_NETWORK_REQUIRED']);
  const unreadable = await applyPipelineSchema({ environment: env, readSql: async () => { throw new Error('ENOENT /app/server'); } });
  assert.deepEqual([unreadable.state, unreadable.reason], ['held', 'SCHEMA_APPLY_FAILED']);
});

test('the start hook writes one tagged JSON line and start.mjs runs it only behind the setting', async () => {
  const lines = [];
  await applyPipelineSchemaOnStart(line => lines.push(line), { environment: env, poolOptions, connect: database().connect });
  assert.equal(lines.length, 1); assert.match(lines[0], /^KFM_PIPELINE_SCHEMA \{"profile":"kfm\.pipeline-schema\/v1",/);
  const start = await readFile(new URL('../server/start.mjs', import.meta.url), 'utf8');
  assert.match(start, /if \(process\.env\.KFM_PIPELINE_SCHEMA_APPLY_SHA256\) \{\n\s+const \{ applyPipelineSchemaOnStart \} = await import\("\.\/pipeline-schema-apply\.mjs"\);\n\s+void applyPipelineSchemaOnStart\(\)\.catch/);
});
