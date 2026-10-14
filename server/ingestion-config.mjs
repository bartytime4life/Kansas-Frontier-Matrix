import { isIP } from "node:net";
// Node hosting composition only. No D1/R2 or governed-release bindings.
export const ARCHIVE_LIMIT_BYTES = 80_000_000_000; // Owner chose 80 GB, decimal bytes.
export const OWNER_GITHUB_ID = "203533328";
export const INGEST_SCHEMA_VERSION = 1;
export const RECEIPT_ALLOWANCE = 16_384;
export const CHUNK_BYTES = 512 * 1024;
export function ingestionConfig(environment = process.env) {
  const database = ["DB_HOST", "DB_NAME", "DB_USER", "DB_PASSWORD"].every(key => Boolean(environment[key]));
  // mysql2's SNI identity check needs a DNS host; never silently skip it for an IP.
  const tls = environment.KFM_DB_TLS === "verified" && Boolean(environment.KFM_DB_CA_PEM) && Boolean(environment.DB_HOST) && isIP(environment.DB_HOST) === 0;
  const origin = environment.KFM_PUBLIC_ORIGIN === "https://kansasfrontiermatrix.com" ? environment.KFM_PUBLIC_ORIGIN : null;
  const authentication = Boolean(origin && environment.KFM_GITHUB_CLIENT_ID && environment.KFM_GITHUB_CLIENT_SECRET && /^[A-Za-z0-9_-]{43,}$/.test(environment.KFM_SESSION_KEY ?? ""));
  const enabled = environment.KFM_INGEST_ENABLED === "true";
  // Shared preview/live DB: only the confirmed published app may run workers.
  const production = environment.KFM_RUNTIME_ROLE === "published";
  const capacityConfirmed = environment.KFM_ARCHIVE_CAPACITY_CONFIRMED_BYTES === String(ARCHIVE_LIMIT_BYTES);
  return { database, tls, origin, authentication, enabled, production, capacityConfirmed,
    ready: database && tls && authentication && enabled && production && capacityConfirmed };
}
