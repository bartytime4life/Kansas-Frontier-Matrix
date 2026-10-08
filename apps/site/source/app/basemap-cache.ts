import type { MapOptions, RequestParameters } from "./maplibre-seam";

export const BASEMAP_CACHE_ORIGIN = "http://127.0.0.1:8770";
export type BasemapCacheStatus = { schema: "kfm-basemap-cache/v1"; destination: string; limitBytes: number; usedBytes: number; reservedBytes: number; tiles: number; hits: number; misses: number; sessionToken: string; job: { state: string; completed: number; total: number; bytes: number; failed?: number } };
let status: BasemapCacheStatus | null = null;
let enabled = true;
let retryAt = 0;
let connecting: Promise<BasemapCacheStatus | null> | null = null;

export function cacheableBasemap(url: string): boolean {
  try {
    const u = new URL(url);
    if (u.protocol !== "https:" || u.username || u.password || u.port || u.hash) return false;
    if (u.hostname === "tiles.openfreemap.org" && !u.search) return /^\/planet\/(?:\d{8}_\d{6}_pt|latest)\/\d{1,2}\/\d+\/\d+\.pbf$/.test(u.pathname) || /^\/natural_earth\/ne2sr\/\d\/\d+\/\d+\.png$/.test(u.pathname);
    if (u.hostname === "basemap.nationalmap.gov" && !u.search) return /^\/arcgis\/rest\/services\/USGSTopo\/MapServer\/tile\/\d{1,2}\/\d+\/\d+$/.test(u.pathname);
    if (u.hostname === "dascservices.kansasgis.org" && u.pathname === "/arcgis/rest/services/IMAGERY_STATEWIDE/NG911_2024_1ft_Natural_Color/ImageServer/exportImage") {
      const fixed = { bboxSR: "3857", imageSR: "3857", size: "512,512", format: "png32", interpolation: "RSP_NearestNeighbor", f: "image" };
      return [...u.searchParams.keys()].length === 7 && Object.entries(fixed).every(([k, v]) => u.searchParams.get(k) === v) && u.searchParams.has("bbox");
    }
  } catch { /* Invalid or local URLs stay on their existing path. */ }
  return false;
}

export function setBasemapCacheEnabled(value: boolean): void {
  enabled = value;
  try { localStorage.setItem("kfm-basemap-cache-enabled", String(value)); } catch { /* Device storage can be disabled. */ }
}
export function basemapCacheEnabled(): boolean {
  try { enabled = localStorage.getItem("kfm-basemap-cache-enabled") !== "false"; } catch { /* Use owner-requested default. */ }
  return enabled;
}

export async function connectBasemapCache(force = false): Promise<BasemapCacheStatus | null> {
  if (!force && retryAt > Date.now()) return status;
  if (connecting) return connecting;
  connecting = (async () => {
    try {
      const r = await fetch(`${BASEMAP_CACHE_ORIGIN}/status`, { cache: "no-store", credentials: "omit", signal: AbortSignal.timeout(1500) });
      if (!r.ok) throw new Error("Unavailable");
      const text = await r.text();
      if (text.length > 8192) throw new Error("Invalid status");
      const s = JSON.parse(text) as BasemapCacheStatus;
      if (s.schema !== "kfm-basemap-cache/v1" || s.limitBytes !== 10_000_000_000 || !/^[A-Za-z0-9_-]{43}$/.test(s.sessionToken) || typeof s.destination !== "string" || !s.destination.endsWith("/data/work/basemap-cache") || !Number.isFinite(s.usedBytes) || s.usedBytes < 0 || s.usedBytes > s.limitBytes || !s.job) throw new Error("Invalid cache");
      status = s; retryAt = Date.now() + 30_000;
    } catch { status = null; retryAt = Date.now() + 30_000; }
    finally { connecting = null; }
    return status;
  })();
  return connecting;
}

export async function basemapCacheAction(action: "overview" | "cancel"): Promise<BasemapCacheStatus | null> {
  const s = await connectBasemapCache(true);
  if (!s) throw new Error("Local cache is unavailable. Start the PC service, then reconnect.");
  const r = await fetch(`${BASEMAP_CACHE_ORIGIN}/${action}`, { method: "POST", headers: { "X-KFM-Session": s.sessionToken }, credentials: "omit", signal: AbortSignal.timeout(5000) });
  if (!r.ok) throw new Error("Local cache action failed.");
  return connectBasemapCache(true);
}

// A transport hook leaves source URLs, imagery dates, attribution and copied styles intact.
export const basemapCacheRequest: NonNullable<MapOptions["transformRequest"]> = (url, kind) => ({ url: kind === "Tile" && cacheableBasemap(url) ? `kfm-basemap://${encodeURIComponent(url)}` : url });

export async function basemapCacheProtocol(request: RequestParameters, controller: AbortController): Promise<{ data: ArrayBuffer }> {
  const url = decodeURIComponent(request.url.slice("kfm-basemap://".length));
  if (!cacheableBasemap(url)) throw new Error("Unsupported basemap resource");
  const signal = controller.signal;
  if (basemapCacheEnabled()) {
    const s = await connectBasemapCache();
    if (signal.aborted) throw new DOMException("Aborted", "AbortError");
    if (s) {
      try {
        const r = await fetch(`${BASEMAP_CACHE_ORIGIN}/resource?url=${encodeURIComponent(url)}`, { headers: { "X-KFM-Session": s.sessionToken }, credentials: "omit", cache: "no-store", signal: AbortSignal.any([signal, AbortSignal.timeout(25_000)]) });
        if (!r.ok) throw new Error("Cache unavailable");
        return { data: await r.arrayBuffer() };
      } catch { if (signal.aborted) throw new DOMException("Aborted", "AbortError"); }
    }
  }
  const r = await fetch(url, { signal, credentials: "omit" });
  if (!r.ok) throw new Error(`Basemap unavailable (${r.status})`);
  return { data: await r.arrayBuffer() };
}
