/** Expendable, same-origin public terrain only. Never an archive or source authority. */
const DB = 'kfm-public-terrain-v1', SETTING = 'kfm-temporary-terrain-enabled';
const MIB = 1024 * 1024;
export const TERRAIN_CACHE_ENTRY_LIMIT = 2 * MIB, TERRAIN_CACHE_COUNT_LIMIT = 24;
export const TERRAIN_CACHE_RETENTION_MS = 60 * 60 * 1000, TERRAIN_CACHE_REUSE_MS = 5 * 60 * 1000;
export const TERRAIN_CACHE_EVENT = 'kfm-terrain-cache-change';
type Control = { id: 'state'; generation: number; enabled: boolean };
type Meta = { key: string; bytes: number; storedAt: number; expiresAt: number };
export type VisitorTerrainCacheStatus = { enabled: boolean; usedBytes: number; limitBytes: number; available: boolean };
export type VisitorTerrainEntry = { value: unknown | null; save(value: unknown, expiresAt: number): Promise<void>; discard(): Promise<void> };
let localGeneration = 0;
let preference: boolean | null = null;
const empty = (): VisitorTerrainEntry => ({ value: null, save: async () => {}, discard: async () => {} });
const browser = () => { try { return typeof window !== 'undefined' && typeof indexedDB !== 'undefined'; } catch { return false; } };
function enabled() { try { return localStorage.getItem(SETTING) !== 'false' && preference !== false; } catch { return preference !== false; } }
function notify() { if (typeof window !== 'undefined') window.dispatchEvent(new Event(TERRAIN_CACHE_EVENT)); }
export function terrainCacheDeviceLimit(hints: { memory?: number; cores?: number; saveData?: boolean }) {
  return !hints.saveData && Number(hints.memory) > 4 && Number(hints.cores) > 4 ? 16 * MIB : 8 * MIB;
}
function deviceLimit() {
  if (typeof navigator === 'undefined') return 8 * MIB;
  const n = navigator as Navigator & { deviceMemory?: number; connection?: { saveData?: boolean } };
  return terrainCacheDeviceLimit({ memory: n.deviceMemory, cores: n.hardwareConcurrency, saveData: n.connection?.saveData });
}
/** A browser hit cannot extend original host freshness or re-label stale data. */
export function terrainCacheExpiry(caches: { state: string; at: string }[], now = Date.now()) {
  if (!caches.length || caches.some(c => !['live', 'fresh'].includes(c.state) || !Number.isFinite(Date.parse(c.at)) || Date.parse(c.at) > now + 60_000)) return 0;
  return Math.min(now + TERRAIN_CACHE_REUSE_MS, ...caches.map(c => Date.parse(c.at) + 24 * 60 * 60 * 1000));
}
export function terrainCacheKeyValid(key: string) { return /^(ground|native):[0-9a-f]{64}$/.test(key); }
export function terrainCacheRecordValid(v: Meta, now: number) {
  return !!v && terrainCacheKeyValid(v.key) && Number.isSafeInteger(v.bytes) && v.bytes > 0 && v.bytes <= TERRAIN_CACHE_ENTRY_LIMIT &&
    Number.isSafeInteger(v.storedAt) && v.storedAt <= now && v.storedAt > now - TERRAIN_CACHE_RETENTION_MS &&
    Number.isSafeInteger(v.expiresAt) && v.expiresAt > now && v.expiresAt <= v.storedAt + TERRAIN_CACHE_REUSE_MS;
}
const state = (raw: unknown): Control => {
  const c = raw as Control | undefined;
  return c?.id === 'state' && Number.isSafeInteger(c.generation) && c.generation >= 0 && typeof c.enabled === 'boolean' ? c : { id: 'state', generation: 0, enabled: true };
};
function open(): Promise<IDBDatabase | null> {
  if (!browser()) return Promise.resolve(null);
  return new Promise(resolve => {
    let finished = false;
    const done = (db: IDBDatabase | null) => { if (finished) { db?.close(); return; } finished = true; clearTimeout(timer); resolve(db); };
    const timer = setTimeout(() => done(null), 200);
    try {
      const request = indexedDB.open(DB, 1);
      request.onupgradeneeded = () => { for (const name of ['meta', 'data', 'control']) if (!request.result.objectStoreNames.contains(name)) request.result.createObjectStore(name); };
      request.onsuccess = () => { request.result.onversionchange = () => request.result.close(); done(request.result); };
      request.onerror = () => done(null); request.onblocked = () => done(null);
    } catch { done(null); }
  });
}
/** Every trim/write shares one readwrite transaction across tabs. */
async function transaction<T>(fallback: T, work: (tx: IDBTransaction, result: (value: T) => void) => void): Promise<T> {
  const db = await open(); if (!db) return fallback;
  return new Promise(resolve => {
    let value = fallback, finished = false, tx: IDBTransaction;
    const finish = (ok: boolean) => { if (finished) return; finished = true; clearTimeout(timer); db.close(); resolve(ok ? value : fallback); };
    const timer = setTimeout(() => { try { tx?.abort(); } catch { /* Already complete. */ } finish(false); }, 250);
    try {
      tx = db.transaction(['meta', 'data', 'control'], 'readwrite');
      tx.oncomplete = () => finish(true); tx.onerror = () => finish(false); tx.onabort = () => finish(false);
      work(tx, v => { value = v; });
    } catch { finish(false); }
  });
}
function remove(tx: IDBTransaction, key: IDBValidKey) { tx.objectStore('meta').delete(key); tx.objectStore('data').delete(key); }
function trim(tx: IDBTransaction, limit: number, after: (entries: Meta[]) => void) {
  const entries: Meta[] = [], now = Date.now(), request = tx.objectStore('meta').openCursor();
  request.onsuccess = () => {
    const cursor = request.result;
    if (cursor) { const v = cursor.value as Meta; if (cursor.key !== v?.key || !terrainCacheRecordValid(v, now)) remove(tx, cursor.key); else entries.push(v); cursor.continue(); return; }
    entries.sort((a, b) => a.storedAt - b.storedAt);
    let bytes = entries.reduce((sum, e) => sum + e.bytes, 0);
    while (entries.length > TERRAIN_CACHE_COUNT_LIMIT || bytes > limit) { const e = entries.shift()!; bytes -= e.bytes; remove(tx, e.key); }
    after(entries);
  };
}
async function storageLimit() {
  const limit = deviceLimit();
  try {
    if (!navigator.storage?.estimate) return limit;
    const estimate = await Promise.race([navigator.storage.estimate(), new Promise<null>(resolve => setTimeout(() => resolve(null), 100))]);
    if (!estimate || !Number.isFinite(estimate.quota) || !Number.isFinite(estimate.usage)) return limit;
    // Never consume the last 50MiB of reported origin quota. Quotas are hints,
    // not reservations; quota errors always fall back to uncached delivery.
    return Math.max(0, Math.min(limit, Math.floor((estimate.quota! - estimate.usage! - 50 * MIB) / 4)));
  } catch { return limit; }
}
export async function visitorTerrainCacheStatus(): Promise<VisitorTerrainCacheStatus> {
  const limitBytes = deviceLimit(), fallback = { enabled: enabled(), usedBytes: 0, limitBytes, available: false };
  return transaction(fallback, (tx, result) => { const r=tx.objectStore('control').get('state'); r.onsuccess=()=>trim(tx, limitBytes, entries => result({ enabled: enabled() && state(r.result).enabled, usedBytes: entries.reduce((n, e) => n + e.bytes, 0), limitBytes, available: true })); });
}
export async function clearVisitorTerrainCache() {
  localGeneration++;
  const changed = await transaction(false, (tx, done) => {
    const request = tx.objectStore('control').get('state');
    request.onsuccess = () => { const c = state(request.result); tx.objectStore('control').put({ ...c, generation: c.generation + 1 }, 'state'); tx.objectStore('meta').clear(); tx.objectStore('data').clear(); done(true); };
  });
  notify();
  if (!changed) throw new Error('Temporary terrain storage could not be changed.');
}
export async function setVisitorTerrainCacheEnabled(value: boolean) {
  localGeneration++; preference = value;
  try { localStorage.setItem(SETTING, String(value)); } catch { /* Private mode can reject preference storage. */ }
  const changed = await transaction(false, (tx, done) => {
    const request = tx.objectStore('control').get('state');
    request.onsuccess = () => { const c = state(request.result); tx.objectStore('control').put({ ...c, generation: c.generation + 1, enabled: value }, 'state'); if (!value) { tx.objectStore('meta').clear(); tx.objectStore('data').clear(); } done(true); };
  });
  notify();
  if (!changed) throw new Error('Temporary terrain storage could not be changed.');
}
/** Capture a generation BEFORE network work, so Clear/Off cannot be undone by a late reply. */
export async function openVisitorTerrainEntry(key: string, signal: AbortSignal): Promise<VisitorTerrainEntry> {
  if (!browser() || !enabled() || !terrainCacheKeyValid(key) || signal.aborted) return empty();
  const generation = localGeneration, limit = deviceLimit();
  const found = await transaction<{ generation: number; text: string | null } | null>(null, (tx, done) => {
    const r = tx.objectStore('control').get('state');
    r.onsuccess = () => { const c = state(r.result); if (!c.enabled) return;
      trim(tx, limit, entries => { const entry=entries.find(e => e.key === key); if (!entry) { done({ generation: c.generation, text: null }); return; }
        const v = tx.objectStore('data').get(key); v.onsuccess = () => { const text = v.result; if (typeof text !== 'string' || text.length > TERRAIN_CACHE_ENTRY_LIMIT || new TextEncoder().encode(text).byteLength !== entry.bytes) { remove(tx, key); done({ generation: c.generation, text: null }); } else done({ generation: c.generation, text }); };
      });
    };
  });
  if (!found || signal.aborted || generation !== localGeneration || !enabled()) return empty();
  let value: unknown | null = null; try { if (found.text) value = JSON.parse(found.text); } catch { /* Treat corrupt copies as misses. */ }
  return {
    value,
    discard: async () => { await transaction(false, (tx, done) => { remove(tx, key); done(true); }); },
    save: async (payload, expiresAt) => {
      if (signal.aborted || generation !== localGeneration || !enabled() || !Number.isFinite(expiresAt) || expiresAt <= Date.now()) return;
      let text: string; try { text = JSON.stringify(payload); } catch { return; }
      if (typeof text !== 'string' || text.length > TERRAIN_CACHE_ENTRY_LIMIT) return;
      const bytes = new TextEncoder().encode(text).byteLength; if (bytes > TERRAIN_CACHE_ENTRY_LIMIT) return;
      const limitBytes = await storageLimit(); if (bytes > limitBytes || signal.aborted || generation !== localGeneration || !enabled()) return;
      await transaction(false, (tx, done) => {
        const r = tx.objectStore('control').get('state'); r.onsuccess = () => { const c = state(r.result);
          if (!c.enabled || c.generation !== found.generation || signal.aborted || generation !== localGeneration || !enabled()) return;
          trim(tx, limitBytes, entries => {
            if (signal.aborted || generation !== localGeneration) return;
            const others = entries.filter(e => e.key !== key); let total = others.reduce((n, e) => n + e.bytes, 0);
            while (others.length >= TERRAIN_CACHE_COUNT_LIMIT || total + bytes > limitBytes) { const e = others.shift(); if (!e) return; total -= e.bytes; remove(tx, e.key); }
            const storedAt = Date.now(), expiry = Math.min(expiresAt, storedAt + TERRAIN_CACHE_REUSE_MS); if (expiry <= storedAt) return;
            tx.objectStore('meta').put({ key, bytes, storedAt, expiresAt: expiry }, key); tx.objectStore('data').put(text, key); done(true);
          });
        };
      });
      notify();
    }
  };
}

if (typeof window !== 'undefined') window.addEventListener('storage', event => { if (event.key === SETTING || event.key === null) { preference = null; localGeneration++; notify(); } });
