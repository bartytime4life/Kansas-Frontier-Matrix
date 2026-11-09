'use client';
import { useEffect, useState } from 'react';
import { boundedStoryText, validStoryBundle } from './story-bundle.mjs';

// Bundles are the only thing a story fetches. A small LRU shares reusable snapshots. Mounted consumers retain
// their active value until disabled/unmounted; the cache limit is not a bound on all mounted consumers.
const CACHE_BYTES = 3_000_000;
const WAITING_MS = 5 * 60_000;
const cache = new Map();   // id -> { value, bytes, at }
const inflight = new Map();   // id -> { promise, controller, users }
const known = new Map();   // id -> { state, observedTo }: what a card keeps saying once its bundle is let go

const IDLE = Object.freeze({ state: 'idle', bundle: null, known: null });
const LOADING = Object.freeze({ state: 'loading', bundle: null });
const WAITING = Object.freeze({ state: 'waiting', bundle: null });
const OFFLINE = Object.freeze({ state: 'offline', bundle: null });

function remember(id, value, bytes) {
  cache.delete(id);
  cache.set(id, { value, bytes, at: Date.now() });
  let total = 0;
  for (const entry of cache.values()) total += entry.bytes;
  for (const [key, entry] of cache) {
    if (total <= CACHE_BYTES || key === id) break;
    total -= entry.bytes; cache.delete(key);
  }
}
function cached(id) {
  const entry = cache.get(id);
  if (!entry) return null;
  if (entry.value.state === 'waiting' && Date.now() - entry.at > WAITING_MS) { cache.delete(id); return null; }
  cache.delete(id); cache.set(id, entry);
  return entry.value;
}

/** The relay wraps a stored bundle as rows[0].bundle; the dev preview serves the bundle itself. */
export function storyBundleFrom(reply, id) {
  const bundle = reply?.format === 'kfm-story-bundle-v1' ? reply : reply?.rows?.[0]?.bundle;
  return validStoryBundle(bundle, id) ? bundle : null;
}
/** What a reply means for the card. Anything short of a bundle reads as waiting, or as offline for a gateway outage. */
export function storyBundleState(status, reply, id) {
  if (status >= 200 && status < 300) {
    const bundle = storyBundleFrom(reply, id);
    return bundle ? { state: 'ready', bundle } : WAITING;
  }
  return status === 404 ? WAITING : OFFLINE;
}

function request(id) {
  const running = inflight.get(id);
  // A remount can arrive before an aborted request's finally handler removes it.
  if (running && !running.controller.signal.aborted) { running.users += 1; return running; }
  const controller = new AbortController();
  const promise = fetch(`/api/local-data/stories?story=${encodeURIComponent(id)}`, { signal: controller.signal, headers: { Accept: 'application/json' } })
    .then(async response => {
      const text = await boundedStoryText(response);
      let reply = null;
      try { reply = JSON.parse(text); } catch { reply = null; }
      const value = storyBundleState(response.status, reply, id);
      known.set(id, { state: value.state, observedTo: value.bundle?.observed?.to ?? null });
      if (value.state !== 'offline') remember(id, value, value.state === 'ready' ? text.length : 0);
      return value;
    })
    .finally(() => { if (inflight.get(id)?.promise === promise) inflight.delete(id); });
  const entry = { promise, controller, users: 1 };
  inflight.set(id, entry);
  return entry;
}

/** { state: 'idle' | 'loading' | 'ready' | 'waiting' | 'offline', bundle, known }. Pass id = null, or enabled: false, to stay idle. */
export function useStoryBundle(id, { enabled = true } = {}) {
  const key = enabled ? id : null;
  const [settled, setSettled] = useState({ key: null, value: IDLE });
  useEffect(() => {
    if (!key) return undefined;
    let live = true;
    const hit = cached(key), entry = hit ? null : request(key);
    // Keep an already-cached value in this mounted consumer too. Later LRU eviction must not strand it
    // in loading with an unchanged effect key.
    (hit ? Promise.resolve(hit) : entry.promise).then(value => { if (live) setSettled({ key, value }); }, error => {
      if (live && error?.name !== 'AbortError') setSettled({ key, value: OFFLINE });
    });
    return () => {
      live = false;
      if (!entry) return;
      entry.users -= 1;
      if (entry.users <= 0) entry.controller.abort();
    };
  }, [key]);
  if (!key) return id && known.has(id) ? { ...IDLE, known: known.get(id) } : IDLE;
  // Active consumers remain usable when other instruments evict their shared cache entry.
  return cached(key) || (settled.key === key ? settled.value : LOADING);
}
