import { readBoundedJson } from "./bounded-json";
import { archiveInterval, GLM_ARCHIVE_BATCH, GLM_ARCHIVE_FLASH_LIMIT, type GlmArchiveManifest, type GlmArchiveQuery } from "./lightning-archive";
import { decodeArchiveFlashes, type HdfReader } from "./lightning-archive-decode";
import type { GlmFlash, GlmFlashSnapshot } from "./lightning-flashes";

type Decoder = typeof decodeArchiveFlashes;
let reader: Promise<HdfReader> | null = null;
async function browserReader() {
  if (!reader) {
    // Pinned, same-origin browser bundle, loaded only when an archive is requested.
    reader = new Promise<HdfReader>((resolve, reject) => {
      const script = document.createElement("script");
      script.src = "/vendor/h5wasm/h5wasm.js";
      script.async = true;
      script.onload = () => {
        const decoder = (window as typeof window & { h5wasm?: HdfReader }).h5wasm;
        if (!decoder) { script.remove(); reject(new Error("Archive reader could not initialize.")); return; }
        void decoder.ready.then(() => resolve(decoder)).catch(error => { script.remove(); reject(error); });
      };
      script.onerror = () => { script.remove(); reject(new Error("Archive reader could not load. Retry the interval.")); };
      document.head.appendChild(script);
    }).catch(error => { reader = null; throw error; });
  }
  return reader;
}
async function readArchiveBytes(response: Response, limit: number, signal: AbortSignal) {
  if (!response.body || Number(response.headers.get("content-length")) > limit) throw new Error("Archive file too large.");
  const stream = response.body.getReader(), chunks: Uint8Array[] = []; let length = 0;
  try {
    while (true) {
      signal.throwIfAborted(); const { done, value } = await stream.read(); signal.throwIfAborted(); if (done) break;
      length += value.length; if (length > limit) throw new Error("Archive file too large."); chunks.push(value);
    }
  } catch (error) { await stream.cancel().catch(() => {}); throw error; }
  finally { stream.releaseLock(); }
  const bytes = new Uint8Array(length); let offset = 0;
  for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.length; }
  return bytes.buffer;
}

export async function loadLightningArchive(query: GlmArchiveQuery, signal: AbortSignal, progress: (done: number, total: number) => void, fetcher: typeof fetch = fetch, suppliedReader?: HdfReader, decoder: Decoder = decodeArchiveFlashes): Promise<GlmFlashSnapshot> {
  const interval = archiveInterval(query);
  const params = new URLSearchParams({ day: query.day, hour: String(query.hour), minute: String(query.minute), duration: String(query.duration) });
  const read = async (suffix = "") => {
    signal.throwIfAborted();
    const response = await fetcher(`/api/lightning/archive?${params}${suffix}`, { signal, cache: "no-store" });
    const data = await readBoundedJson(response, 4 * 1024 * 1024, signal);
    signal.throwIfAborted();
    if (!response.ok) throw new Error("Archive interval unavailable. Try another date or retry.");
    return data;
  };
  const manifest = await read() as GlmArchiveManifest;
  if (!/^[a-f0-9]{64}$/.test(manifest.id) || Date.parse(manifest.start) !== interval.start || Date.parse(manifest.end) !== interval.end
    || !Array.isArray(manifest.files) || !manifest.files.length || manifest.files.length > 181
    || manifest.expectedFiles !== query.duration * 3 + 1 || manifest.missingFiles !== manifest.expectedFiles - manifest.files.length || manifest.missingFiles < 0
    || manifest.parts !== Math.ceil(manifest.files.length / GLM_ARCHIVE_BATCH)) throw new Error("Archive coverage response is invalid.");
  const hdf = suppliedReader ?? await browserReader();
  signal.throwIfAborted();
  const unique = new Map<string, GlmFlash>(); let omittedQuality = 0, done = 0;
  progress(0, manifest.files.length);
  // Two bounded files at a time. Nothing reaches the map until the entire selection is checked.
  for (let index = 0; index < manifest.files.length; index += 2) {
    const results = await Promise.allSettled(manifest.files.slice(index, index + 2).map(async (file, offset) => {
      const part = index + offset;
      const response = await fetcher(`/api/lightning/archive?${params}&part=${part}&manifest=${manifest.id}`, { signal, cache: "default" });
      if (!response.ok || response.headers.get("X-GLM-Manifest") !== manifest.id) throw new Error("Archive file unavailable or changed. Reload the interval.");
      const bytes = await readArchiveBytes(response, 4 * 1024 * 1024, signal);
      signal.throwIfAborted();
      const data = decoder(bytes, file, interval.start, interval.end, hdf);
      omittedQuality += data.omittedQuality;
      for (const flash of data.flashes) {
        unique.set(flash.id, flash);
        if (unique.size > GLM_ARCHIVE_FLASH_LIMIT) throw new Error("Too many flashes for one view. Select a shorter interval.");
      }
      progress(++done, manifest.files.length);
    }));
    const failed = results.find(result => result.status === "rejected");
    if (failed?.status === "rejected") throw failed.reason;
  }
  signal.throwIfAborted();
  const flashes = [...unique.values()].sort((a, b) => a.timeMs - b.timeMs || a.id.localeCompare(b.id));
  return {
    source: "NOAA_GOES_GLM_ARCHIVE", evidenceRole: "EXTERNAL_CONTEXT_ONLY", windowMinutes: query.duration,
    requestedAt: new Date().toISOString(), providerGeneratedAt: manifest.end,
    oldestFlashAt: flashes.at(0)?.observedAt ?? null, latestFlashAt: flashes.at(-1)?.observedAt ?? null,
    state: manifest.missingFiles ? "partial" : flashes.length ? "ready" : "empty",
    partialReason: manifest.missingFiles ? `${manifest.missingFiles} of ${manifest.expectedFiles} expected 20-second files are missing. Gaps remain unknown.` : null,
    providerCount: flashes.length,
    nearBorderCount: flashes.filter(f => f.longitude < -102.052 || f.longitude > -94.588 || f.latitude < 36.993 || f.latitude > 40.004).length,
    flashes, archive: { start: manifest.start, end: manifest.end, files: manifest.files.length, expectedFiles: manifest.expectedFiles, missingFiles: manifest.missingFiles, omittedQuality },
  };
}
