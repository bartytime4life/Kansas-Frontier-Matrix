// Explicit disposable localhost opt-in only. Never targets the hosting database.
import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import mysql from 'mysql2/promise';
import { PipelineStore } from '../server/pipeline-store.mjs';
import { execFileSync } from 'node:child_process';
import { sha } from '../server/pipeline-contract.mjs';

test('MySQL: additive migration, persistent replay, atomic activation/CAS and withdrawal', { skip: process.env.KFM_PIPELINE_MYSQL_TEST !== '1' }, async t => {
  const port = Number(process.env.KFM_PIPELINE_MYSQL_PORT ?? 13317); assert.ok(Number.isInteger(port) && port > 1024 && port <= 65535);
  const options = { host: '127.0.0.1', port, user: 'root', password: 'kfm-disposable-test-only', connectionLimit: 4 };
  const bootstrap = await mysql.createConnection(options); const database = 'kfm_pc_fixture_' + process.pid;
  await bootstrap.query('CREATE DATABASE ' + database); const pool = mysql.createPool({ ...options, database }); const store = new PipelineStore(pool);
  t.after(async () => { await pool.end(); await bootstrap.query('DROP DATABASE ' + database); await bootstrap.end(); });
  const queries = (await readFile(new URL('../server/pipeline-schema.sql', import.meta.url), 'utf8')).replace(/--[^\n]*/g, '').split(';').map(v => v.trim()).filter(Boolean);
  await pool.query('CREATE TABLE unrelated_sentinel (value INT)'); await pool.query('INSERT INTO unrelated_sentinel VALUES (42)');
  for (let i = 0; i < 2; i++) for (const query of queries) await pool.query(query);
  assert.equal((await pool.query('SELECT value FROM unrelated_sentinel'))[0][0].value, 42);
  const now = Date.now(); const m = { sourceId: 'nws-alerts', byteLength: 100 };
  await assert.rejects(store.stage('a'.repeat(64), m, now), /PIPELINE_PAUSED/);
  await pool.execute('UPDATE kfm_pipeline_control SET paused=FALSE WHERE id=1');
  assert.equal(await store.claimNonce('c'.repeat(64), now), true); assert.equal(await new PipelineStore(pool).claimNonce('c'.repeat(64), now), false);
  const a = 'a'.repeat(64), b = 'b'.repeat(64); await store.stage(a, m, now); await store.stage(b, m, now);
  const outcomes = await Promise.allSettled([store.commit(a, null, { value: 1 }, now), store.commit(b, null, { value: 2 }, now)]);
  assert.equal(outcomes.filter(o => o.status === 'fulfilled').length, 1, JSON.stringify(outcomes.map(o => o.status === 'rejected' ? o.reason.message : o.status)));
  const head = await store.active('nws-alerts'); assert.ok(head); assert.ok(head.projection);
  assert.equal((await pool.query('SELECT COUNT(*) AS n FROM kfm_pipeline_events'))[0][0].n, 1);
  assert.equal((await pool.query('SELECT MAX(CHAR_LENGTH(event_id)) AS n FROM kfm_pipeline_events'))[0][0].n, 64);
  await store.commit(head.id, null, null, now); assert.equal((await store.active('nws-alerts')).id, head.id);
  const next = head.id === a ? b : a;
  await store.commit(next, head.id, { value: 3 }, now);
  await store.rollback(head.id, next, 'd'.repeat(64), now);
  assert.equal((await store.active('nws-alerts')).id, head.id);
  await assert.rejects(store.withdraw(head.id, 'f'.repeat(64), now), /ACTIVATION_CONFLICT/);
  await store.withdraw(head.id, head.id, now); assert.equal(await store.active('nws-alerts'), null);
  assert.equal((await store.release(head.id)).state, 'WITHDRAWN');
});

test('MySQL: restore pre-county backup, preserve populated heads/control/history through migration, restore post-cutover backup', {
  skip: process.env.KFM_PIPELINE_MYSQL_TEST !== '1' || !process.env.KFM_PIPELINE_MYSQL_CONTAINER,
}, async t => {
  // Only the disposable CI service is accepted; never accepts an operational host/DSN.
  const container = process.env.KFM_PIPELINE_MYSQL_CONTAINER;
  assert.match(container, /^[a-f0-9]{64}$/);
  const port = Number(process.env.KFM_PIPELINE_MYSQL_PORT ?? 13317);
  assert.ok(Number.isInteger(port) && port > 1024 && port <= 65535);
  const connection = await mysql.createConnection({ host: '127.0.0.1', port, user: 'root', password: 'kfm-disposable-test-only' });
  const databases = [];
  t.after(async () => { try { for (const db of databases) await connection.query('DROP DATABASE ' + db); } finally { await connection.end(); } });
  const oldSql = await readFile(new URL('./fixtures/pipeline/pre-county-schema.sql', import.meta.url), 'utf8');
  const sql = await readFile(new URL('../server/pipeline-schema.sql', import.meta.url), 'utf8');
  assert.equal(sha(oldSql), '5c5049c2c1a9c932b928c96bdb2195114f0e7a8f2df84b6c6f38b61597c254f5');
  // This cutover only adds one source head. If a later migration changes more, review this rehearsal explicitly.
  assert.equal(sql.replace(",('newberry-county-history')", ''), oldSql);
  const tables = ['kfm_pipeline_control', 'kfm_pipeline_nonces', 'kfm_pipeline_releases', 'kfm_pipeline_heads', 'kfm_pipeline_events', 'unrelated_sentinel'];
  const create = async suffix => {
    const db = 'kfm_county_restore_' + process.pid + '_' + suffix;
    await connection.query('CREATE DATABASE ' + db); databases.push(db); return db;
  };
  // Use text-protocol queries below: prepared statements can retain the previous default database.
  const use = async db => connection.query('USE ' + db);
  const apply = async text => { for (const q of text.replace(/--[^\n]*/g, '').split(';').map(s => s.trim()).filter(Boolean)) await connection.query(q); };
  const snapshot = async () => {
    const result = {};
    for (const table of tables) {
      const [ddl] = await connection.query('SHOW CREATE TABLE ' + table);
      const [rows] = await connection.query('SELECT * FROM ' + table);
      result[table] = { ddl: ddl[0]['Create Table'], rows: rows.sort((a, b) => JSON.stringify(a).localeCompare(JSON.stringify(b))) };
    }
    return result;
  };
  const docker = (program, args, input) => execFileSync('docker', ['exec', ...(input ? ['-i'] : []), '-e', 'MYSQL_PWD=kfm-disposable-test-only',
    container, program, '--user=root', ...args], { input, encoding: 'utf8', timeout: 30000, maxBuffer: 4 * 1024 * 1024 });
  const backup = db => docker('mysqldump', ['--single-transaction', '--skip-lock-tables', '--no-tablespaces', '--set-gtid-purged=OFF', '--hex-blob', db]);
  for (const paused of [false, true]) {
    const original = await create('original_' + Number(paused)); await use(original); await apply(oldSql);
    await connection.query('UPDATE kfm_pipeline_control SET paused=?,worker_seen=?,worker_state=? WHERE id=1', [paused, 1793298600000, 'idle']);
    await connection.query('CREATE TABLE unrelated_sentinel (id INT PRIMARY KEY, value TEXT) ENGINE=InnoDB');
    await connection.query('INSERT INTO unrelated_sentinel VALUES (1,?)', ['unrelated records; quotes \' and Unicode Kansas 🌻']);
    await connection.query('INSERT INTO kfm_pipeline_nonces VALUES (?,?)', ['f'.repeat(64), 1793298720000]);
    for (const [index, source] of ['usgs-streamflow', 'nws-alerts', 'usgs-earthquakes', 'water', 'weather'].entries()) {
      const id = (index + 1).toString(16).repeat(64), prior = (index + 6).toString(16).repeat(64);
      for (const [release, state] of [[id, 'COMMITTED'], [prior, 'WITHDRAWN']]) {
        await connection.query('INSERT INTO kfm_pipeline_releases VALUES (?,?,?,?,?,?)',
          [release, source, JSON.stringify({ fixture: true, source, recipe: 'pre-county' }), state, JSON.stringify({ synthetic: source }), 1793298600000]);
      }
      await connection.query('UPDATE kfm_pipeline_heads SET release_id=?,previous_id=?,revision=? WHERE source_id=?', [id, prior, index + 10, source]);
      await connection.query('INSERT INTO kfm_pipeline_events VALUES (?,?,?,?,?,?)', [id, source, id, prior, 'ACTIVATE', 1793298600000]);
    }
    const before = await snapshot(), dump = backup(original); assert.ok(dump.includes('unrelated_sentinel'));
    const restored = await create('restored_' + Number(paused)); docker('mysql', [restored], dump); await use(restored);
    assert.deepEqual(await snapshot(), before, 'pre-cutover backup restores all fixture schema and rows');
    await apply(sql); await apply(sql);
    const after = await snapshot(), expected = structuredClone(before);
    expected.kfm_pipeline_heads.rows.push({ source_id: 'newberry-county-history', release_id: null, previous_id: null, revision: 0 });
    expected.kfm_pipeline_heads.rows.sort((a, b) => JSON.stringify(a).localeCompare(JSON.stringify(b)));
    assert.deepEqual(after, expected, 'only the empty county head is added; pause/resume state is preserved');
    const postDump = backup(restored), postRestore = await create('post_' + Number(paused));
    docker('mysql', [postRestore], postDump); await use(postRestore);
    assert.deepEqual(await snapshot(), after, 'post-cutover backup preserves additive row and all original history');
    t.diagnostic(JSON.stringify({ paused, serverVersion: (await connection.query('SELECT VERSION() AS version'))[0][0].version,
      migrationSha256: sha(sql), backupSha256: sha(dump), restoredBackupSha256: sha(postDump), oldHeadCount: 5, newHeadCount: 6 }));
  }
});
