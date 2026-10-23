// Connection health only. No datasets, schema changes or SQL supplied by callers.
import { isIP } from 'node:net';
import { lookup as systemLookup } from 'node:dns/promises';
const SQL = 'SELECT 1 AS connection_ok';
export function databaseOptions(env) {
  if (!['DB_HOST', 'DB_NAME', 'DB_USER', 'DB_PASSWORD'].every(k => typeof env[k] === 'string' && env[k].length)) {
    throw new Error('DATABASE_CONFIGURATION_MISSING');
  }
  const port = Number(env.DB_PORT ?? 3306);
  if (!Number.isInteger(port) || port < 1 || port > 65535) throw new Error('DATABASE_CONFIGURATION_MISSING');
  const local = ['localhost', '127.0.0.1', '::1'].includes(env.DB_HOST);
  const options = {
    host: env.DB_HOST === 'localhost' ? '127.0.0.1' : env.DB_HOST,
    port, database: env.DB_NAME, user: env.DB_USER, password: env.DB_PASSWORD,
    connectTimeout: 5000, multipleStatements: false,
  };
  if (!local) options.ssl = {
    ...(env.KFM_DB_CA_PEM ? { ca: env.KFM_DB_CA_PEM } : {}),
    rejectUnauthorized: true, verifyIdentity: true, minVersion: 'TLSv1.2',
  };
  return { options, transport: local ? 'host-loopback' : 'verified-tls' };
}

function providerPrivateAddress(address) {
  if (isIP(address) !== 4) return false;
  const [a, b] = address.split('.').map(Number);
  return a === 10 || (a === 172 && b >= 16 && b <= 31) || (a === 192 && b === 168);
}

export async function connectionOptions(env, lookup = systemLookup) {
  const result = databaseOptions(env);
  if (env.KFM_DATABASE_CONNECTION_TRANSPORT !== 'provider-private-network' || result.transport === 'host-loopback') return result;
  // Explicit owner opt-in only. No fallback after a TLS failure, public address,
  // mixed DNS result or unknown network. Pin the validated IP to avoid rebinding.
  const addresses = await lookup(env.DB_HOST, { all: true, family: 4 });
  if (!addresses.length || !addresses.every(item => providerPrivateAddress(item.address))) throw new Error('DATABASE_PRIVATE_NETWORK_REQUIRED');
  const options = { ...result.options, host: addresses[0].address };
  delete options.ssl;
  return { options, transport: 'provider-private-network' };
}

function reason(error) {
  if (error?.message === 'DATABASE_CONFIGURATION_MISSING') return 'configuration-missing';
  if (error?.message === 'DATABASE_PRIVATE_NETWORK_REQUIRED') return 'private-provider-network-required';
  if (/CERT|TLS|SSL|SELF_SIGNED|UNABLE_TO_VERIFY/.test(error?.code ?? '')) return 'verified-tls-unavailable';
  if (error?.code === 'ER_ACCESS_DENIED_ERROR') return 'authentication-failed';
  return 'connection-unavailable';
}

function tlsFailure(error) {
  if (error?.code === 'HANDSHAKE_NO_SSL_SUPPORT') return 'server-does-not-support-tls';
  const message = String(error?.message ?? '');
  if (/self.signed|unable to verify|issuer certificate|certificate.*expired/i.test(message)) return 'provider-ca-required';
  if (/altname|hostname.*match|certificate.*name/i.test(message)) return 'certificate-hostname-mismatch';
  return 'provider-tls-configuration-required';
}

export function createDatabaseCheck({
  environment = () => process.env, now = Date.now,
  lookup = systemLookup,
  connect = async options => (await import('mysql2/promise')).createConnection(options),
} = {}) {
  let cached, until = 0, pending;
  return async function check() {
    if (cached && now() < until) return cached;
    if (pending) return pending;
    pending = (async () => {
      let connection;
      let result;
      try {
        const { options, transport } = await connectionOptions(environment(), lookup);
        connection = await connect(options);
        const [rows] = await connection.query({ sql: SQL, timeout: 2000 });
        if (Number(rows[0]?.connection_ok) !== 1) throw new Error('DATABASE_CHECK_FAILED');
        result = { connected: true, state: 'connected', transport };
      } catch (error) {
        result = { connected: false, state: 'unavailable', reason: reason(error) };
        if (result.reason === 'verified-tls-unavailable') result.tlsFailure = tlsFailure(error);
      } finally {
        // No idle pool, retry loop or unattended database workload.
        if (connection) connection.destroy();
      }
      cached = {
        format: 'kfm-database-connection-v1', mode: 'connection-only',
        checkedAt: new Date(now()).toISOString(), cacheSeconds: 60,
        uploadsEnabled: false, sqlWritesEnabled: false, ...result,
      };
      until = now() + 60000;
      return cached;
    })();
    try { return await pending; } finally { pending = undefined; }
  };
}

export const checkDatabaseConnection = createDatabaseCheck();
