const NDFD_WMS = "https://digital.weather.gov/ndfd/wms";
const KANSAS_BOUNDS = [-102.1, 36.9, -94.5, 40.1] as const;
const MAX_TILE_BYTES = 512_000;

export function airflowTileRequest(url: URL) {
  const params = url.searchParams;
  if ([...params.keys()].some((key) => !["z", "x", "y"].includes(key) || params.getAll(key).length !== 1)) throw new Error("Unsupported airflow tile request.");
  const values = ["z", "x", "y"].map((key) => {
    const raw = params.get(key);
    if (!raw || !/^\d{1,5}$/.test(raw)) throw new Error("Invalid airflow tile coordinate.");
    return Number(raw);
  });
  const [z, x, y] = values;
  const count = 2 ** z;
  if (z < 3 || z > 11 || x >= count || y >= count) throw new Error("Airflow tile outside supported zoom range.");
  const latitude = (row: number) => Math.atan(Math.sinh(Math.PI * (1 - 2 * row / count))) * 180 / Math.PI;
  const west = x / count * 360 - 180;
  const east = (x + 1) / count * 360 - 180;
  if (east <= KANSAS_BOUNDS[0] || west >= KANSAS_BOUNDS[2] || latitude(y) <= KANSAS_BOUNDS[1] || latitude(y + 1) >= KANSAS_BOUNDS[3]) throw new Error("Airflow tile outside the Kansas map area.");
  const extent = 20037508.342789244;
  const size = 2 * extent / count;
  const bbox = [-extent + x * size, extent - (y + 1) * size, -extent + (x + 1) * size, extent - y * size].join(",");
  const query = new URLSearchParams({
    SERVICE: "WMS", VERSION: "1.1.1", REQUEST: "GetMap",
    LAYERS: "ndfd.conus.windspd.windbarbs", STYLES: "",
    FORMAT: "image/png", TRANSPARENT: "TRUE", SRS: "EPSG:3857",
    WIDTH: "256", HEIGHT: "256", BBOX: bbox,
  });
  return `${NDFD_WMS}?${query}`;
}

export async function serveAirflowTile(request: Request, fetchUpstream: typeof fetch = fetch) {
  let upstream: string;
  try { upstream = airflowTileRequest(new URL(request.url)); }
  catch (error) { return Response.json({ error: (error as Error).message }, { status: 400, headers: { "Cache-Control": "no-store" } }); }
  try {
    const response = await fetchUpstream(upstream, { signal: AbortSignal.timeout(12_000), redirect: "manual" });
    if (!response.ok || !response.body || !(response.headers.get("content-type") ?? "").toLowerCase().startsWith("image/png")) throw new Error("NDFD did not return a PNG image.");
    if (Number(response.headers.get("content-length")) > MAX_TILE_BYTES) throw new Error("NDFD image exceeds the tile budget.");
    const reader = response.body.getReader();
    const chunks: Uint8Array[] = [];
    let total = 0;
    while (true) {
      const { value, done } = await reader.read();
      if (done) break;
      total += value.byteLength;
      if (total > MAX_TILE_BYTES) { await reader.cancel(); throw new Error("NDFD image exceeds the tile budget."); }
      chunks.push(value);
    }
    const bytes = new Uint8Array(total);
    let offset = 0;
    for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
    const signature = [137, 80, 78, 71, 13, 10, 26, 10];
    if (bytes.length < 33 || signature.some((byte, index) => bytes[index] !== byte)) throw new Error("Invalid NDFD image.");
    const header = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
    if (header.getUint32(12) !== 0x49484452 || header.getUint32(16) !== 256 || header.getUint32(20) !== 256) throw new Error("Unexpected NDFD image dimensions.");
    return new Response(bytes, { headers: {
      "Content-Type": "image/png", "Cache-Control": "public, max-age=300, s-maxage=300",
      "X-Content-Type-Options": "nosniff", "X-KFM-Source": "NWS NDFD forecast wind barbs",
      "X-KFM-Time-Boundary": "Provider-default forecast; exact valid time not resolved",
    } });
  } catch {
    return Response.json({ error: "NWS forecast wind image unavailable. No airflow substitute was drawn." }, { status: 502, headers: { "Cache-Control": "no-store", "Retry-After": "30" } });
  }
}
