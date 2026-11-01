import test from 'node:test';
import assert from 'node:assert/strict';
import { pipelinePoolOptions, getPipelineStore } from '../server/pipeline-store.mjs';

const env = { DB_HOST: 'database.example.test', DB_NAME: 'private-db', DB_USER: 'private-user', DB_PASSWORD: 'private-password' };
const tls = { ...env, KFM_DB_TLS: 'verified', KFM_DB_CA_PEM: 'fixture-ca' };
const privateNetwork = { ...env, KFM_DATABASE_CONNECTION_TRANSPORT: 'provider-private-network' };
const never = async () => assert.fail('must not resolve DNS');

test('without the opt-in, pipeline writes still require certificate-verified TLS to a DNS host', async () => {
  const options = await pipelinePoolOptions(tls, never);
  assert.equal(options.host, 'database.example.test'); assert.equal(options.port, 3306);
  assert.deepEqual(options.ssl, { ca: 'fixture-ca', rejectUnauthorized: true, verifyIdentity: true });
  assert.equal(options.multipleStatements, false);
  for (const change of [{ KFM_DB_TLS: undefined }, { KFM_DB_CA_PEM: '' }, { DB_HOST: '10.1.2.3' }, { DB_PASSWORD: '' }]) {
    await assert.rejects(pipelinePoolOptions({ ...tls, ...change }, never), /DATABASE_TLS_REQUIRED/);
  }
  await assert.rejects(pipelinePoolOptions({ ...tls, DB_PORT: '70000' }, never), /DATABASE_PORT_INVALID/);
  // The health check's opt-in value is required exactly; anything else keeps the TLS rule.
  await assert.rejects(pipelinePoolOptions({ ...env, KFM_DATABASE_CONNECTION_TRANSPORT: 'private' }, never), /DATABASE_TLS_REQUIRED/);
});

test('the owner-approved private network pins a validated private address, without TLS or a CA', async () => {
  const calls = [];
  const options = await pipelinePoolOptions({ ...privateNetwork, DB_PORT: '3307' }, async (host, opts) => {
    calls.push([host, opts]); return [{ address: '10.20.30.40', family: 4 }];
  });
  assert.deepEqual(calls, [['database.example.test', { all: true, family: 4 }]]);
  assert.equal(options.host, '10.20.30.40'); assert.equal(options.port, 3307);
  assert.equal(options.ssl, undefined);
  assert.deepEqual([options.database, options.user, options.password], ['private-db', 'private-user', 'private-password']);
  assert.equal(options.multipleStatements, false); assert.equal(options.connectionLimit, 3);
});

test('the private network refuses public, mixed, empty, IPv6 and loopback answers before any credential is used', async () => {
  for (const addresses of [[], [{ address: '8.8.8.8' }], [{ address: '10.1.2.3' }, { address: '8.8.8.8' }], [{ address: '::1' }]]) {
    await assert.rejects(pipelinePoolOptions(privateNetwork, async () => addresses), /DATABASE_PRIVATE_NETWORK_REQUIRED/);
  }
  await assert.rejects(pipelinePoolOptions(privateNetwork, async () => { throw new Error('ENOTFOUND database.example.test'); }),
    error => error.message === 'DATABASE_PRIVATE_NETWORK_REQUIRED');
  await assert.rejects(pipelinePoolOptions({ ...privateNetwork, DB_HOST: 'localhost' }, never), /DATABASE_PRIVATE_NETWORK_REQUIRED/);
  await assert.rejects(pipelinePoolOptions({ ...privateNetwork, DB_PASSWORD: '' }, never), /DATABASE_CONFIGURATION_MISSING/);
});

test('a stalled DNS lookup fails closed at its deadline', async t => {
  t.mock.timers.enable({ apis: ['setTimeout'] });
  const pending = pipelinePoolOptions(privateNetwork, () => new Promise(() => {}));
  const outcome = assert.rejects(pending, /DATABASE_PRIVATE_NETWORK_REQUIRED/);
  await new Promise(resolve => setImmediate(resolve));
  t.mock.timers.tick(5000);
  await outcome;
});

test('a disabled pipeline never builds a pool', async () => {
  await assert.rejects(getPipelineStore({ ...privateNetwork }), /PIPELINE_DISABLED/);
});
