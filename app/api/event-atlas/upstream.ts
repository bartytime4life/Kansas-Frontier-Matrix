const HOSTS = new Set(["mesonet.agron.iastate.edu", "satepsanone.nesdis.noaa.gov", "gibs.earthdata.nasa.gov", "api.gbif.org", "services.arcgis.com", "tigerweb.geo.census.gov", "tiles.arcgis.com", "data.raspberryshake.org", "api.waterdata.usgs.gov", "www.ncei.noaa.gov", "elevation.nationalmap.gov"]);
export async function boundedFetch(url: string, limit: number) {
  const parsed = new URL(url);
  if (parsed.protocol !== "https:" || !HOSTS.has(parsed.hostname) || parsed.username || parsed.password) throw new Error("Non-allowlisted source.");
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 18_000);
  try {
    // Workers implements manual/follow, but rejects redirect:"error" before I/O.
    // Manual keeps redirects inside the same fail-closed source boundary.
    const response = await fetch(url, { signal: controller.signal, redirect: "manual", headers: { "User-Agent": "KansasFrontierMatrixExplorer/1.0" } });
    if (response.status === 204) return { bytes: new Uint8Array(), text: () => "", headers: response.headers };
    if (!response.ok || !response.body) throw new Error(`Source unavailable (HTTP ${response.status}).`);
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
  } finally { clearTimeout(timer); }
}
export const jsonHeaders = { "Cache-Control": "public, max-age=120", "X-Content-Type-Options": "nosniff" };
