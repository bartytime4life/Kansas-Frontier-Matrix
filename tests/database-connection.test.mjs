import test from 'node:test';
import assert from 'node:assert/strict';
import { createDatabaseCheck, databaseOptions } from '../server/database-connection.mjs';

const env = { DB_HOST: 'database.example.test', DB_NAME: 'private-db', DB_USER: 'private-user', DB_PASSWORD: 'private-password' };

test('remote SQL always verifies TLS and refuses missing configuration', () => {
  const remote = databaseOptions(env);
  assert.equal(remote.transport, 'verified-tls');
  assert.equal(remote.options.ssl.rejectUnauthorized, true);
  assert.equal(remote.options.ssl.verifyIdentity, true);
  assert.equal(remote.options.multipleStatements, false);
  assert.throws(() => databaseOptions({ ...env, DB_PASSWORD: '' }), /CONFIGURATION_MISSING/);
  assert.throws(() => databaseOptions({ ...env, DB_PORT: 'invalid' }), /CONFIGURATION_MISSING/);
  const local = databaseOptions({ ...env, DB_HOST: 'localhost' });
  assert.equal(local.options.host, '127.0.0.1');
  assert.equal(local.options.ssl, undefined);
  assert.ok(databaseOptions({ ...env, DB_HOST: '192.168.1.2' }).options.ssl);
});

test('only a constant SELECT runs; credentials and database names never leave the check', async () => {
  let destroyed = 0;
  const calls = [];
  const check = createDatabaseCheck({ environment: () => env, connect: async options => {
    assert.equal(options.password, env.DB_PASSWORD);
    return { query: async query => { calls.push(query); return [[{ connection_ok: 1 }]]; }, destroy: () => destroyed++ };
  } });
  const result = await check();
  assert.equal(result.connected, true);
  assert.deepEqual(calls, [{ sql: 'SELECT 1 AS connection_ok', timeout: 2000 }]);
  assert.equal(destroyed, 1);
  assert.equal(result.uploadsEnabled, false);
  assert.equal(result.sqlWritesEnabled, false);
  assert.doesNotMatch(JSON.stringify(result), /private-db|private-user|private-password|database.example/);
});

test('concurrent requests share one connection and failures are cached without leaking driver text', async () => {
  let count = 0, time = 1792770000000;
  const check = createDatabaseCheck({ environment: () => env, now: () => time, connect: async () => {
    count++;
    throw Object.assign(new Error('private-password at database.example.test'), { code: 'CERT_HAS_EXPIRED' });
  } });
  const results = await Promise.all(Array.from({ length: 20 }, () => check()));
  assert.equal(count, 1);
  assert.ok(results.every(r => r.reason === 'verified-tls-unavailable'));
  assert.doesNotMatch(JSON.stringify(results), /private-password|database.example/);
  time += 59999; await check(); assert.equal(count, 1);
  time += 2; await check(); assert.equal(count, 2);
});

test('failed queries close the connection and missing configuration never connects', async () => {
  let destroyed = 0;
  const check = createDatabaseCheck({ environment: () => env, connect: async () => ({
    query: async () => { throw new Error('private SQL error'); }, destroy: () => destroyed++,
  }) });
  assert.equal((await check()).connected, false);
  assert.equal(destroyed, 1);
  const missing = createDatabaseCheck({ environment: () => ({}), connect: async () => assert.fail('must not connect') });
  assert.equal((await missing()).reason, 'configuration-missing');
});

test('TLS diagnosis distinguishes missing provider trust from unavailable TLS without exposing host details', async () => {
  for (const [code, message, expected] of [
    ['HANDSHAKE_NO_SSL_SUPPORT', 'Server does not support secure connection', 'server-does-not-support-tls'],
    ['HANDSHAKE_SSL_ERROR', 'self-signed certificate at private.example', 'provider-ca-required'],
    ['ERR_TLS_CERT_ALTNAME_INVALID', 'Hostname does not match private.example', 'certificate-hostname-mismatch'],
  ]) {
    const check = createDatabaseCheck({ environment: () => env, connect: async () => { throw Object.assign(new Error(message), { code }); } });
    const result = await check();
    assert.equal(result.tlsFailure, expected);
    assert.doesNotMatch(JSON.stringify(result), /private.example/);
  }
});
