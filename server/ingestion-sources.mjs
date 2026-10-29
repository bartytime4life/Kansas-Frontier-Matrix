import { createHash } from "node:crypto";
// Versioned, fixed Kansas requests. No caller-supplied URLs or pagination walks.
export const CAPTURE_SOURCES = Object.freeze([
  { id: "usgs-streamflow", name: "USGS streamflow", intervalMs: 3_600_000, limitBytes: 8 * 1024 * 1024,
    rightsUrl: "https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits",
    limitation: "Rolling 24-hour Kansas streamflow query, at most 1,000 rows. Provisional values, original units, missing values and paging remain in the source. No automatic flood or evidence interpretation." },
  { id: "nws-alerts", name: "NWS Kansas alerts", intervalMs: 3_600_000, limitBytes: 8 * 1024 * 1024,
    rightsUrl: "https://www.weather.gov/disclaimer",
    limitation: "Active Kansas alert payload at retrieval time; no zone geometry expansion. Expired or missing alerts are not an all-clear. Not an emergency notification service." },
  // Hourly, like the other sources, so a published snapshot stays inside the release profiles' two-hour freshness.
  { id: "usgs-earthquakes", name: "USGS earthquake catalog", intervalMs: 3_600_000, limitBytes: 8 * 1024 * 1024,
    rightsUrl: "https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits",
    limitation: "Kansas bounding window, rolling 30 days, at most 250 events. Catalog locations, magnitude, depth and review state can be revised. At the row cap the capture is partial." },
]);
export function captureRequest(sourceId, at = Date.now()) {
  const source = CAPTURE_SOURCES.find(item => item.id === sourceId);
  if (!source || !Number.isFinite(at)) throw new Error("SOURCE_NOT_ALLOWED");
  // Stable time bucket gives replicas, cron, retries and restarts the same identity.
  const slot = Math.floor(at / source.intervalMs) * source.intervalMs;
  const end = new Date(slot).toISOString();
  let url;
  if (sourceId === "usgs-streamflow") {
    url = new URL("https://api.waterdata.usgs.gov/ogcapi/v1/collections/latest-continuous/items");
    for (const [key, value] of Object.entries({ f: "json", limit: "1000", state_code: "20", agency_code: "USGS", site_type_code: "ST", parameter_code: "00060", datetime: `${new Date(slot - 86_400_000).toISOString()}/${end}` })) url.searchParams.set(key, value);
  } else if (sourceId === "nws-alerts") {
    url = new URL("https://api.weather.gov/alerts/active?area=KS");
  } else {
    url = new URL("https://earthquake.usgs.gov/fdsnws/event/1/query");
    for (const [key, value] of Object.entries({ format: "geojson", eventtype: "earthquake", starttime: new Date(slot - 30 * 86_400_000).toISOString(), endtime: end, minlatitude: "36.9", maxlatitude: "40.1", minlongitude: "-102.1", maxlongitude: "-94.5", orderby: "time", limit: "250" })) url.searchParams.set(key, value);
  }
  const id = createHash("sha256").update(`kfm-hosted-capture-v1\n${sourceId}\n${slot}\n${url}`).digest("hex");
  return { ...source, sourceId: source.id, slot, id, url: url.toString(), requestedAt: end, adapterVersion: "kfm-hosted-capture-v1" };
}
export async function fetchCapture(request, { fetcher = fetch, signal, apiKey } = {}) {
  // Rebuild from admitted source/bucket; never trust a caller's mutated URL/budget.
  const canonical = captureRequest(request.sourceId, request.slot);
  if (request.url !== canonical.url || request.id !== canonical.id || request.limitBytes !== canonical.limitBytes) throw new Error("SOURCE_NOT_ALLOWED");
  const controller = new AbortController();
  const requestedAt = new Date().toISOString();
  const abort = () => controller.abort();
  signal?.throwIfAborted(); signal?.addEventListener("abort", abort, { once: true });
  const timer = setTimeout(abort, 20_000);
  try {
    const response = await fetcher(request.url, { redirect: "manual", cache: "no-store", signal: controller.signal,
      headers: { Accept: "application/geo+json, application/json", "User-Agent": "KansasFrontierMatrix/1.0 (https://kansasfrontiermatrix.com)", ...(request.sourceId === "usgs-streamflow" && apiKey ? { "X-Api-Key": apiKey } : {}) } });
    if (response.status !== 200 || !response.body) { await response.body?.cancel(); throw new Error("UPSTREAM_UNAVAILABLE"); }
    const contentType = response.headers.get("content-type") ?? "";
    if (!/^(application\/(?:geo\+)?json)(?:;|$)/i.test(contentType)) { await response.body.cancel(); throw new Error("CONTENT_TYPE_REJECTED"); }
    if (Number(response.headers.get("content-length")) > request.limitBytes) { await response.body.cancel(); throw new Error("RESPONSE_TOO_LARGE"); }
    const reader = response.body.getReader(); const chunks = []; let length = 0;
    try {
      while (true) {
        const { value, done } = await reader.read(); if (done) break;
        length += value.byteLength;
        if (length > request.limitBytes) { controller.abort(); await reader.cancel(); throw new Error("RESPONSE_TOO_LARGE"); }
        chunks.push(Buffer.from(value));
      }
    } finally { reader.releaseLock(); }
    const bytes = Buffer.concat(chunks, length);
    // Bytes are the unmodified decoded HTTP entity, not the compressed wire stream.
    let validation = "invalid"; let featureCount = null; let partial = false; let sourceTimeStart = null; let sourceTimeEnd = null;
    try {
      const value = JSON.parse(new TextDecoder("utf-8", { fatal: true }).decode(bytes));
      if (value?.type === "FeatureCollection" && Array.isArray(value.features) && value.features.every(feature => feature?.type === "Feature" && feature.properties && typeof feature.properties === "object" && !Array.isArray(feature.properties) && (feature.geometry === null || typeof feature.geometry === "object"))) {
        validation = "structure-valid"; featureCount = value.features.length;
        partial = Boolean(value.links?.some?.(link => link.rel === "next") || (request.sourceId === "usgs-earthquakes" && featureCount >= 250) || (request.sourceId === "usgs-streamflow" && featureCount >= 1000));
        for (const feature of value.features) {
          const candidate = feature.properties.time ?? feature.properties.sent;
          const timestamp = typeof candidate === "number" || typeof candidate === "string" ? new Date(candidate).getTime() : NaN;
          if (Number.isFinite(timestamp)) { const iso = new Date(timestamp).toISOString(); if (!sourceTimeStart || iso < sourceTimeStart) sourceTimeStart = iso; if (!sourceTimeEnd || iso > sourceTimeEnd) sourceTimeEnd = iso; }
        }
      }
    } catch { /* Preserve malformed entity privately for correction, never publish it. */ }
    return { bytes, receipt: { format: "kfm-hosted-capture-receipt-v1", captureId: request.id, sourceId: request.sourceId,
      sourceUrl: request.url, captureBucketAt: request.requestedAt, requestedAt, retrievedAt: new Date().toISOString(), adapterVersion: request.adapterVersion,
      sha256: createHash("sha256").update(bytes).digest("hex"), byteLength: length, contentType: contentType.slice(0, 160),
      etag: (response.headers.get("etag") ?? "").slice(0, 256) || null, lastModified: (response.headers.get("last-modified") ?? "").slice(0, 128) || null,
      validation, featureCount, partial, sourceTimeStart, sourceTimeEnd, lifecycle: "WORK/QUARANTINE", evidenceRole: "EXTERNAL_CONTEXT_ONLY", rightsReview: "pending", sensitivityReview: "pending", releaseState: "unreleased",
      rightsUrl: request.rightsUrl, limitation: request.limitation, transforms: ["HTTP content decoding only; original entity preserved; original units/properties retained."] } };
  } catch (error) {
    if (["SOURCE_NOT_ALLOWED", "UPSTREAM_UNAVAILABLE", "CONTENT_TYPE_REJECTED", "RESPONSE_TOO_LARGE"].includes(error?.message)) throw error;
    throw new Error(controller.signal.aborted ? "UPSTREAM_TIMEOUT" : "UPSTREAM_UNAVAILABLE");
  } finally { clearTimeout(timer); signal?.removeEventListener("abort", abort); }
}
