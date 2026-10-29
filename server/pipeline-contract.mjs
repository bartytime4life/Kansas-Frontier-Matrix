// Transport projections only. Existing source/evidence/release contracts retain authority.
import { createHash, createPublicKey, verify } from 'node:crypto';
import { readFile } from 'node:fs/promises';

export const ORIGIN = 'https://kansasfrontiermatrix.com';
export const MAX_PACKAGE = 8 * 1024 * 1024;
export const CHUNK_SIZE = 256 * 1024;
export const SOURCES = ['usgs-streamflow', 'nws-alerts', 'usgs-earthquakes', 'water', 'weather'];
export const HASH = /^[a-f0-9]{64}$/;
export class PipelineError extends Error { constructor(code, status = 409) { super(code); this.status = status; } }
export const fail = (code, status) => { throw new PipelineError(code, status); };
export const sha = bytes => createHash('sha256').update(bytes).digest('hex');
export function canonical(value) {
  if (value === null || typeof value !== 'object') return JSON.stringify(value);
  if (Array.isArray(value)) return '[' + value.map(canonical).join(',') + ']';
  return '{' + Object.keys(value).sort().map(key => JSON.stringify(key) + ':' + canonical(value[key])).join(',') + '}';
}
export function parse(bytes, limit = MAX_PACKAGE) {
  if (Buffer.byteLength(bytes) > limit) fail('BYTE_LIMIT', 413);
  try { return JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(Buffer.from(bytes))); }
  catch { fail('JSON_INVALID', 400); }
}
export function timestamp(value) {
  if (typeof value !== 'string' || !/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(?:\.\d{3})?Z$/.test(value) || !Number.isFinite(Date.parse(value)) || new Date(value).toISOString().replace('.000Z', 'Z') !== value.replace('.000Z', 'Z')) fail('TIME_INVALID', 400);
  return Date.parse(value);
}
export function source(value) { if (!SOURCES.includes(value)) fail('SOURCE_NOT_ALLOWED', 400); return value; }
export function digest(value) { if (!HASH.test(value ?? '')) fail('DIGEST_INVALID', 400); return value; }
export function verifyProfile(signed, publicKey, { now = Date.now(), recipe = '', sourceId = '' } = {}) {
  try {
    const { profile: p, signature } = signed;
    if (p?.format !== 'kfm-pc-release-delegation-v1' || !/^[a-zA-Z0-9._-]{1,64}$/.test(p.id ?? '') || p.sourceId !== source(sourceId)
      || p.recipeSha256 !== digest(recipe) || p.rights !== 'redistribution-allowed' || p.sensitivity !== 'public'
      || typeof p.approver !== 'string' || !p.approver.length || p.approver.length > 128
      || !['sourceRef', 'rightsRef', 'reviewRef', 'releaseProfileRef'].every(key => typeof p[key] === 'string' && /^kfm:\/\//.test(p[key]) && p[key].length < 512)
      || timestamp(p.validFrom) > now || timestamp(p.expiresAt) <= now || timestamp(p.expiresAt) - timestamp(p.validFrom) > 30 * 86400_000
      || p.maxBytes !== MAX_PACKAGE || p.maxRows !== 1000 || p.staleAfterSeconds !== 7200
      || p.role !== (['water', 'weather'].includes(sourceId) ? 'governed-package' : 'external-context')) fail('APPROVAL_INVALID', 403);
    const key = createPublicKey(publicKey);
    if (key.asymmetricKeyType !== 'ed25519' || typeof signature !== 'string' || Buffer.from(signature, 'base64url').length !== 64
      || !verify(null, Buffer.from(canonical(p)), key, Buffer.from(signature, 'base64url'))) fail('APPROVAL_INVALID', 403);
    return p;
  } catch { fail('APPROVAL_INVALID', 403); }
}
export async function recipeDigest() {
  const files = ['pipeline-contract.mjs', 'pipeline-normalize.mjs', 'ingestion-sources.mjs'];
  const entries = await Promise.all(files.map(async name => [name, sha(await readFile(new URL(name, import.meta.url)))]));
  return sha(canonical(entries));
}
export async function boundedBody(request, limit) {
  const length = request.headers.get('content-length');
  if (length && (!/^\d+$/.test(length) || Number(length) > limit)) fail('BYTE_LIMIT', 413);
  if (!request.body) return Buffer.alloc(0);
  const reader = request.body.getReader(); const pieces = []; let count = 0;
  let timedOut = false;
  const timer = setTimeout(() => { timedOut = true; void reader.cancel(); }, 15000);
  try {
    while (true) {
      const { value, done } = await reader.read(); if (done) break;
      count += value.length; if (count > limit) { await reader.cancel(); fail('BYTE_LIMIT', 413); }
      pieces.push(Buffer.from(value));
    }
    if (timedOut) fail('BODY_TIMEOUT', 408);
    if (length && count !== Number(length)) fail('BODY_INCOMPLETE', 400);
    return Buffer.concat(pieces, count);
  } finally { clearTimeout(timer); reader.releaseLock(); }
}
