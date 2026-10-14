import { CAPTURE_SOURCES, captureRequest, fetchCapture } from "./ingestion-sources.mjs";
import { ingestionConfig, ARCHIVE_LIMIT_BYTES } from "./ingestion-config.mjs";
import { getIngestionStore } from "./ingestion-store.mjs";
const SAFE_FAILURES = new Set(["UPSTREAM_UNAVAILABLE", "UPSTREAM_TIMEOUT", "CONTENT_TYPE_REJECTED", "RESPONSE_TOO_LARGE", "ARCHIVE_LIMIT_REACHED", "CAPTURE_INTEGRITY_FAILED", "LEASE_LOST", "PIPELINE_PAUSED"]);
export async function runIngestion({ config = ingestionConfig(), store, fetcher = fetch, at = Date.now(), signal, actor = "capture-worker" } = {}) {
  if (!config.ready) return { state: "configuration-required", captured: 0 };
  store ??= await getIngestionStore();
  const token = await store.claim(at, actor);
  if (!token) return { state: "paused-or-busy", captured: 0 };
  let captured = 0; const outcomes = [];
  try {
    for (const source of CAPTURE_SOURCES) {
      signal?.throwIfAborted();
      const request = captureRequest(source.id, at);
      if (!await store.due(request, token, at)) { outcomes.push({ sourceId: source.id, state: "already-captured-or-retry-held" }); continue; }
      let reservation = 0;
      try {
        reservation = await store.reserve(request, token);
        const result = await fetchCapture(request, { fetcher, signal, apiKey: process.env.USGS_WATER_API_KEY });
        result.receipt.capturedBy = actor;
        await store.save(request, result, token, reservation);
        captured++; outcomes.push({ sourceId: source.id, state: result.receipt.validation === "invalid" ? "quarantined-invalid" : "quarantined", captureId: request.id });
      } catch (error) {
        const code = SAFE_FAILURES.has(error?.message) ? error.message : "STORAGE_UNAVAILABLE";
        try { await store.failure(request, token, code, reservation); } catch { /* Fenced or unavailable storage: no stale write and no log of credentials. */ }
        outcomes.push({ sourceId: source.id, state: "held", code });
        if (["ARCHIVE_LIMIT_REACHED", "LEASE_LOST", "PIPELINE_PAUSED", "STORAGE_UNAVAILABLE"].includes(code)) break;
      }
    }
    return { state: outcomes.some(item => item.state === "held") ? "partial" : "complete", captured, outcomes };
  } finally { await store.release(token); }
}
let statusPromise; let statusExpires = 0;
export async function ingestionStatus() {
  if (statusPromise && statusExpires > Date.now()) return statusPromise;
  statusExpires = Date.now() + 30_000;
  statusPromise = (async () => {
    const config = ingestionConfig();
    const common = { format: "kfm-hosted-source-status-v1", limitBytes: ARCHIVE_LIMIT_BYTES, configured: config.ready,
      releaseState: "unreleased", sources: CAPTURE_SOURCES.map(source => ({ id: source.id, name: source.name, intervalMs: source.intervalMs, state: "not-configured" })) };
    if (!config.database || !config.tls) return { ...common, state: "storage-not-configured", usedBytes: null, captures: null, lastTick: null };
    try {
      const stored = await (await getIngestionStore()).status();
      const jobs = new Map(stored.sources.map(source => [source.id, source]));
      return { ...common, ...stored, state: !config.ready ? "configuration-required" : stored.paused ? "paused" : "awaiting-scheduled-tick",
        sources: common.sources.map(source => ({ ...source, state: "not-captured", ...jobs.get(source.id) })) };
    } catch { return { ...common, state: "storage-unavailable", usedBytes: null, captures: null, lastTick: null }; }
  })();
  return statusPromise;
}
export function clearIngestionStatusCache() { statusExpires = 0; }
