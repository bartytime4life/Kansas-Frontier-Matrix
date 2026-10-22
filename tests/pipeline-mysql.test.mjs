// Explicit disposable localhost opt-in only. Never targets the hosting database.
import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import mysql from 'mysql2/promise';
import { PipelineStore } from '../server/pipeline-store.mjs';

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
