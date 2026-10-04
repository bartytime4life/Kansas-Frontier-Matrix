const ORIGINS = new Set(["https://kanplan.ksdot.gov", "https://gis.blm.gov", "https://mesonet.agron.iastate.edu", "https://satepsanone.nesdis.noaa.gov", "https://gibs.earthdata.nasa.gov", "https://api.gbif.org", "https://services.arcgis.com", "https://tigerweb.geo.census.gov", "https://tiles.arcgis.com", "https://data.raspberryshake.org", "https://api.waterdata.usgs.gov", "https://ngmdb.usgs.gov", "https://www.ncei.noaa.gov", "https://elevation.nationalmap.gov"]);
export async function boundedFetch(url: string, limit: number, options: { timeoutMs?: number; cache?: RequestCache; signal?: AbortSignal } = {}) {
  const parsed = new URL(url);
  if (!ORIGINS.has(parsed.origin) || parsed.username || parsed.password || parsed.hash) throw new Error("Non-allowlisted source.");
  const controller = new AbortController();
  const abort = () => controller.abort();
  options.signal?.throwIfAborted();
  options.signal?.addEventListener("abort", abort, { once: true });
  const timer = setTimeout(() => controller.abort(), options.timeoutMs ?? 18_000);
  try {
    // Workers implements manual/follow, but rejects redirect:"error" before I/O.
    // Manual keeps redirects inside the same fail-closed source boundary.
    const response = await fetch(parsed, { signal: controller.signal, redirect: "manual", cache: options.cache, headers: { "User-Agent": "KansasFrontierMatrixExplorer/1.0" } });
    if (response.status === 204) return { bytes: new Uint8Array(), text: () => "", headers: response.headers };
    if (!response.ok) throw new Error(`Source unavailable (HTTP ${response.status}).`);
    if (!response.body) throw new Error("Source response body was missing.");
    if (Number(response.headers.get("content-length")) > limit) throw new Error("Source exceeded the response budget.");
    const reader = response.body.getReader();
    const chunks: Uint8Array[] = []; let total = 0;
    while (true) {
      const { value, done } = await reader.read(); if (done) break;
      total += value.byteLength;
      if (total > limit) { controller.abort(); await reader.cancel(); throw new Error("Source exceeded the response budget."); }
      chunks.push(value);
    }
    const bytes = new Uint8Array(total); let offset = 0;
    for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
    return { bytes, text: () => new TextDecoder().decode(bytes), headers: response.headers };
  } finally { clearTimeout(timer); options.signal?.removeEventListener("abort", abort); }
}
export const jsonHeaders = { "Cache-Control": "public, max-age=120", "X-Content-Type-Options": "nosniff" };
