// Offline research intake for the hosted-composition PC tooling. This module
// neither creates release EvidenceBundles nor publishes records or opens URLs.
import { DatabaseSync } from 'node:sqlite';
import { createHash } from 'node:crypto';
import { isIP } from 'node:net';
import { isAbsolute } from 'node:path';
import { readRegular } from '../../server/pipeline-files.mjs';

export const CIVIC_INTAKE_LIMITS = Object.freeze({ bytes: 512 * 1024, observations: 500, countyReferencePoints: 200, countyDirectoryCandidates: 500 });
const own = (value, key) => Object.hasOwn(value, key);
function fail(code) { throw new Error('CIVIC_' + code); }
function object(value, required, optional = []) {
  if (!value || typeof value !== 'object' || Array.isArray(value) || ![Object.prototype, null].includes(Object.getPrototypeOf(value))) fail('SCHEMA_INVALID');
  const descriptors = Object.getOwnPropertyDescriptors(value);
  if (Reflect.ownKeys(value).some(key => typeof key !== 'string' || ![...required, ...optional].includes(key) || !own(descriptors[key], 'value')) || required.some(key => !own(value, key))) fail('SCHEMA_INVALID');
}
function string(value, max = 200) {
  if (typeof value !== 'string' || value.length === 0 || value.length > max || value !== value.trim() || /[\u0000-\u001f\u007f]/u.test(value)) fail('TEXT_INVALID');
  return value;
}
function id(value) {
  if (typeof value !== 'string' || !/^[a-z0-9][a-z0-9._:-]{0,95}$/.test(value)) fail('ID_INVALID');
  return value;
}
function geoid(value) {
  if (typeof value !== 'string' || !/^20\d{3}$/.test(value) || value === '20000') fail('GEOID_INVALID');
  return value; // Format validation only: not proof a boundary or county exists.
}
function url(value) {
  string(value, 2048);
  if (!value.startsWith('https://') || /[\\\s]/u.test(value)) fail('URL_INVALID');
  let parsed;
  try { parsed = new URL(value); } catch { fail('URL_INVALID'); }
  const host = parsed.hostname;
  if (parsed.protocol !== 'https:' || parsed.username || parsed.password || (parsed.port && parsed.port !== '443') || !host.includes('.') || isIP(host.replace(/^\[|\]$/g, '')) || /(?:^|\.)(?:localhost|local|internal|test|invalid|example)$/.test(host) || host.endsWith('.')) fail('URL_INVALID');
  for (const [key] of parsed.searchParams) if (/(?:token|secret|password|passwd|credential|authorization|api[_-]?key|access[_-]?key|signature|^auth$|^key$|^jwt$)/i.test(key)) fail('URL_CREDENTIALS');
  if (/(?:token|secret|password|credential|authorization|api[_-]?key|signature)=/i.test(parsed.hash)) fail('URL_CREDENTIALS');
  return parsed.href;
}
function observedAt(value) {
  if (typeof value !== 'string' || !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$/.test(value) || !Number.isFinite(Date.parse(value)) || new Date(value).toISOString() !== value) fail('DATE_INVALID');
  return value;
}
function coordinate(value, max) {
  if (typeof value !== 'number' || !Number.isFinite(value) || Math.abs(value) > max) fail('COORDINATE_INVALID');
  return Object.is(value, -0) ? 0 : value;
}
function canonical(value) {
  if (Array.isArray(value)) return '[' + value.map(canonical).join(',') + ']';
  if (value && typeof value === 'object') return '{' + Object.keys(value).sort().map(key => JSON.stringify(key) + ':' + canonical(value[key])).join(',') + '}';
  return JSON.stringify(value);
}
function sha(value) { return createHash('sha256').update(value).digest('hex'); }
function list(value, max, normalize) {
  if (!Array.isArray(value) || value.length > max) fail('LIMIT');
  const results = [];
  for (let index = 0; index < value.length; index++) {
    // Sparse arrays and accessor entries are not JSON research records.
    const descriptor = Object.getOwnPropertyDescriptor(value, String(index));
    if (!descriptor || !own(descriptor, 'value')) fail('SCHEMA_INVALID');
    results.push(normalize(descriptor.value));
  }
  return results;
}
function observation(value) {
  object(value, ['id', 'sourceId', 'title', 'url', 'observedAt', 'evidence'], ['notes']);
  const evidence = list(value.evidence, 8, item => {
    object(item, ['url', 'locator']);
    return { url: url(item.url), locator: string(item.locator, 500) };
  });
  if (!evidence.length) fail('EVIDENCE_REQUIRED');
  evidence.sort((a, b) => canonical(a) < canonical(b) ? -1 : canonical(a) > canonical(b) ? 1 : 0);
  if (new Set(evidence.map(canonical)).size !== evidence.length) fail('EVIDENCE_DUPLICATE');
  return { id: id(value.id), sourceId: id(value.sourceId), title: string(value.title), url: url(value.url), observedAt: observedAt(value.observedAt), evidence, ...(own(value, 'notes') ? { notes: string(value.notes, 2000) } : {}) };
}
function point(value) {
  object(value, ['id', 'geoid', 'name', 'longitude', 'latitude', 'observationId']);
  return { id: id(value.id), geoid: geoid(value.geoid), name: string(value.name), longitude: coordinate(value.longitude, 180), latitude: coordinate(value.latitude, 90), observationId: id(value.observationId) };
}
function directory(value) {
  object(value, ['id', 'geoid', 'name', 'url', 'observationId']);
  return { id: id(value.id), geoid: geoid(value.geoid), name: string(value.name), url: url(value.url), observationId: id(value.observationId) };
}

/** Validate the v1 local research packet; returned records remain unapproved. */
export function normalizeCivicResearch(packet) {
  object(packet, ['schemaVersion', 'observations', 'countyReferencePoints', 'countyDirectoryCandidates']);
  if (packet.schemaVersion !== 1) fail('SCHEMA_VERSION');
  const normalized = {
    schemaVersion: 1,
    observations: list(packet.observations, CIVIC_INTAKE_LIMITS.observations, observation),
    countyReferencePoints: list(packet.countyReferencePoints, CIVIC_INTAKE_LIMITS.countyReferencePoints, point),
    countyDirectoryCandidates: list(packet.countyDirectoryCandidates, CIVIC_INTAKE_LIMITS.countyDirectoryCandidates, directory),
  };
  if (Buffer.byteLength(canonical(normalized)) > CIVIC_INTAKE_LIMITS.bytes) fail('LIMIT');
  return normalized;
}

/** Read one explicit absolute regular-file path, with no symlink traversal. */
export async function readCivicResearchFile(path) {
  if (typeof path !== 'string' || !isAbsolute(path) || path.split('/').includes('..')) fail('PATH_INVALID');
  const bytes = await readRegular(path, CIVIC_INTAKE_LIMITS.bytes);
  if (bytes.length > CIVIC_INTAKE_LIMITS.bytes) fail('LIMIT');
  let packet;
  try { packet = JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(bytes)); } catch { fail('JSON_INVALID'); }
  return normalizeCivicResearch(packet);
}

/**
 * createCivicIntake() -> { ingest(packet), snapshot(), close() }.
 * Always uses a new private in-memory SQLite DB. No path/connection arguments,
 * persistence, network, public projection or release transition are supported.
 * IDs are caller-assigned stable identities. A normalized SHA-256 digest binds
 * their content; same ID+content is idempotent and changed content is a conflict.
 */
export function createCivicIntake(...args) {
  if (args.length) fail('OPTIONS_UNSUPPORTED');
  const db = new DatabaseSync(':memory:');
  db.exec(`PRAGMA foreign_keys=ON;
    CREATE TABLE civic_source_observations (
      id TEXT PRIMARY KEY, source_id TEXT NOT NULL, observed_at TEXT NOT NULL,
      content_sha256 TEXT NOT NULL, payload TEXT NOT NULL,
      state TEXT NOT NULL DEFAULT 'held' CHECK(state='held'),
      evidence_status TEXT NOT NULL DEFAULT 'research_only' CHECK(evidence_status='research_only')
    ) STRICT;
    CREATE TABLE civic_county_reference_points (
      id TEXT PRIMARY KEY, geoid TEXT NOT NULL,
      observation_id TEXT NOT NULL REFERENCES civic_source_observations(id),
      content_sha256 TEXT NOT NULL, payload TEXT NOT NULL,
      state TEXT NOT NULL DEFAULT 'held' CHECK(state='held'),
      evidence_status TEXT NOT NULL DEFAULT 'research_only' CHECK(evidence_status='research_only')
    ) STRICT;
    CREATE TABLE civic_county_directory_candidates (
      id TEXT PRIMARY KEY, geoid TEXT NOT NULL,
      observation_id TEXT NOT NULL REFERENCES civic_source_observations(id),
      content_sha256 TEXT NOT NULL, payload TEXT NOT NULL,
      state TEXT NOT NULL DEFAULT 'held' CHECK(state='held'),
      evidence_status TEXT NOT NULL DEFAULT 'research_only' CHECK(evidence_status='research_only')
    ) STRICT;`);
  // Table names and SQL are static. Only values from validated records are bound.
  const collections = [
    { key: 'observations', table: 'civic_source_observations', values: item => [item.sourceId, item.observedAt], columns: 'source_id,observed_at' },
    { key: 'countyReferencePoints', table: 'civic_county_reference_points', values: item => [item.geoid, item.observationId], columns: 'geoid,observation_id' },
    { key: 'countyDirectoryCandidates', table: 'civic_county_directory_candidates', values: item => [item.geoid, item.observationId], columns: 'geoid,observation_id' },
  ].map(entry => ({ ...entry,
    find: db.prepare(`SELECT content_sha256 FROM ${entry.table} WHERE id=?`),
    insert: db.prepare(`INSERT INTO ${entry.table}(id,${entry.columns},content_sha256,payload) VALUES(?,?,?,?,?)`),
    all: db.prepare(`SELECT payload,content_sha256,state,evidence_status FROM ${entry.table} ORDER BY id`),
  }));
  const findObservation = db.prepare('SELECT id FROM civic_source_observations WHERE id=?');
  let closed = false;
  function requireOpen() { if (closed) fail('CLOSED'); }
  return Object.freeze({
    ingest(packet) {
      requireOpen();
      const normalized = normalizeCivicResearch(packet);
      let inserted = 0, unchanged = 0;
      db.exec('BEGIN IMMEDIATE');
      try {
        for (const entry of collections) for (const item of normalized[entry.key]) {
          const payload = canonical(item), digest = sha(payload);
          const prior = entry.find.get(item.id);
          if (prior) {
            if (prior.content_sha256 !== digest) fail('IDENTITY_CONFLICT');
            unchanged++;
            continue;
          }
          if (item.observationId && !findObservation.get(item.observationId)) fail('EVIDENCE_MISSING');
          entry.insert.run(item.id, ...entry.values(item), digest, payload);
          inserted++;
        }
        db.exec('COMMIT');
        return { inserted, unchanged, state: 'held', evidenceStatus: 'research_only', releaseEligible: false };
      } catch (error) {
        db.exec('ROLLBACK');
        throw error;
      }
    },
    snapshot() {
      requireOpen();
      const result = { schemaVersion: 1, state: 'held', evidenceStatus: 'research_only', releaseEligible: false, coverage: 'not_assessed', counts: {} };
      for (const entry of collections) {
        result[entry.key] = entry.all.all().map(row => ({ ...JSON.parse(row.payload), contentSha256: row.content_sha256, state: row.state, evidenceStatus: row.evidence_status, releaseEligible: false }));
        result.counts[entry.key] = result[entry.key].length;
      }
      return result;
    },
    close() { if (!closed) { db.close(); closed = true; } },
  });
}
