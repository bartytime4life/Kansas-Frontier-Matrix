import { connectionOptions } from './database-connection.mjs';

// Metadata for tables visible to this application's account, never table contents.
const SQL = `SELECT COUNT(*) AS tables_count,
  CASE WHEN COUNT(*) = COUNT(DATA_LENGTH) AND COUNT(*) = COUNT(INDEX_LENGTH)
    THEN COALESCE(SUM(DATA_LENGTH + INDEX_LENGTH), 0) ELSE NULL END AS allocated_bytes,
  CASE WHEN COUNT(*) = COUNT(TABLE_ROWS) THEN COALESCE(SUM(TABLE_ROWS), 0) ELSE NULL END AS estimated_rows
  FROM information_schema.TABLES WHERE TABLE_SCHEMA = DATABASE() AND TABLE_TYPE = 'BASE TABLE'`;
export const SQL_TARGET_BYTES = 85_000_000_000;
const count = value => {
  if (typeof value === 'string' && /^\d+$/.test(value)) value = Number(value);
  if (!Number.isSafeInteger(value) || value < 0) throw new Error('INVALID_METADATA');
  return value;
};
export function createCapacityCheck({ environment = () => process.env, now = Date.now,
  options = connectionOptions, connect = async config => (await import('mysql2/promise')).createConnection(config) } = {}) {
  let cached, until = 0, pending;
  return async function check() {
    if (cached && now() < until) return cached;
    if (pending) return pending;
    pending = (async () => {
      let connection, result;
      try {
        const selected = await options(environment());
        connection = await connect(selected.options);
        const [rows] = await connection.query({ sql: SQL, timeout: 2000 });
        if (rows.length !== 1) throw new Error('INVALID_METADATA');
        result = { state: 'measured', tables: count(rows[0].tables_count),
          usedBytes: rows[0].allocated_bytes === null ? null : count(rows[0].allocated_bytes),
          estimatedRows: rows[0].estimated_rows === null ? null : count(rows[0].estimated_rows) };
      } catch (error) {
        result = { state: 'unavailable', tables: null, usedBytes: null, estimatedRows: null,
          reason: error?.message === 'DATABASE_CONFIGURATION_MISSING' ? 'configuration-missing' : 'measurement-unavailable' };
      } finally { connection?.destroy(); }
      cached = { format: 'kfm-database-capacity-v1', scope: 'visible-hosted-sql-tables',
        checkedAt: new Date(now()).toISOString(), targetBytes: SQL_TARGET_BYTES, cacheSeconds: 60, ...result };
      until = now() + 60000;
      return cached;
    })();
    try { return await pending; } finally { pending = undefined; }
  };
}
export const checkDatabaseCapacity = createCapacityCheck();
