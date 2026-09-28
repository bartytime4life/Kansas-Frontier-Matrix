/** Bounded display-only 10 m GFS wind samples for animated map arrows. */
export type WindArrowSample = Readonly<{
  latitude: number;
  longitude: number;
  speedMetersPerSecond: number;
  windFromDegrees: number;
  windToDegrees: number;
}>;
export type WindArrowFrame = Readonly<{
  model: "Open-Meteo NCEP GFS · 10 m forecast";
  validTimeUtc: string;
  retrievedAtUtc: string;
  samples: readonly WindArrowSample[];
}>;

const ORIGIN = "https://api.open-meteo.com/v1/gfs";
const KANSAS = { west: -102.1, south: 36.9, east: -94.5, north: 40.1 } as const;
const MAX_BYTES = 160_000;
const CACHE_MS = 5 * 60_000;
const cacheSeconds = (frame: WindArrowFrame, at: number) => Math.max(0, Math.min(300, Math.floor((Date.parse(frame.validTimeUtc) + 35 * 60_000 - at) / 1000)));
const frameHeaders = (frame: WindArrowFrame, at: number) => ({
  "Cache-Control": `public, max-age=${cacheSeconds(frame, at)}`,
  "X-KFM-Wind-Source": "Open-Meteo NCEP GFS 10 m model",
  "X-KFM-Wind-Valid-Time": frame.validTimeUtc,
  "X-KFM-Wind-Retrieved-At": frame.retrievedAtUtc,
});

type GridRequest = Readonly<{ key: string; url: string; coordinates: readonly (readonly [number, number])[] }>;
export function windArrowRequest(requestUrl: URL): GridRequest {
  const params = requestUrl.searchParams;
  if ([...params.keys()].some((key) => key !== "bbox") || params.getAll("bbox").length !== 1) throw new Error("A single map extent is required.");
  const raw = params.get("bbox")?.split(",");
  if (!raw || raw.length !== 4 || raw.some((part) => !/^-?\d{1,3}(?:\.\d{1,5})?$/.test(part))) throw new Error("Invalid map extent.");
  const [west, south, east, north] = raw.map(Number);
  if (west >= east || south >= north || east - west > 15 || north - south > 8) throw new Error("Map extent outside the supported range.");
  const clipped = {
    west: Math.max(west, KANSAS.west), south: Math.max(south, KANSAS.south),
    east: Math.min(east, KANSAS.east), north: Math.min(north, KANSAS.north),
  };
  if (clipped.east - clipped.west < 0.02 || clipped.north - clipped.south < 0.02) throw new Error("No Kansas wind coverage in view.");
  const coordinates: [number, number][] = [];
  for (let row = 0; row < 4; row += 1) for (let column = 0; column < 4; column += 1) {
    coordinates.push([
      Number((clipped.south + (row + 0.5) * (clipped.north - clipped.south) / 4).toFixed(4)),
      Number((clipped.west + (column + 0.5) * (clipped.east - clipped.west) / 4).toFixed(4)),
    ]);
  }
  const query = new URLSearchParams({
    latitude: coordinates.map(([latitude]) => latitude).join(","),
    longitude: coordinates.map(([, longitude]) => longitude).join(","),
    hourly: "wind_speed_10m,wind_direction_10m", models: "ncep_gfs_seamless",
    forecast_hours: "4", timezone: "GMT", wind_speed_unit: "ms",
  });
  // Cache by the actual sampled points. Nearby high-zoom views can otherwise
  // receive a different view's arrows after extent rounding.
  return { key: coordinates.map(([latitude, longitude]) => `${latitude},${longitude}`).join(";"), url: `${ORIGIN}?${query}`, coordinates };
}

function validForecastTime(value: unknown, now: number): string | null {
  if (typeof value !== "string" || !/^\d{4}-\d\d-\d\dT\d\d:\d\d$/.test(value)) return null;
  const parsed = Date.parse(`${value}:00Z`);
  return Number.isFinite(parsed) && parsed >= now - 35 * 60_000 && parsed <= now + 3 * 60 * 60_000
    ? new Date(parsed).toISOString() : null;
}

export function parseWindArrowResponse(body: unknown, coordinates: GridRequest["coordinates"], now: number): WindArrowFrame {
  if (!Array.isArray(body) || body.length !== coordinates.length) throw new Error("Incomplete wind grid.");
  let sharedTime: string | null = null;
  const samples: WindArrowSample[] = body.map((record, index) => {
    const forecast = record?.hourly;
    if (!forecast || !Array.isArray(forecast.time) || !Array.isArray(forecast.wind_speed_10m) || !Array.isArray(forecast.wind_direction_10m)) throw new Error("Incomplete wind forecast.");
    const timeIndex = forecast.time.findIndex((value: unknown) => validForecastTime(value, now) !== null);
    if (timeIndex < 0) throw new Error("No current forecast hour.");
    const time = validForecastTime(forecast.time[timeIndex], now)!;
    if (sharedTime && time !== sharedTime) throw new Error("Wind samples have different valid times.");
    sharedTime = time;
    const speed = forecast.wind_speed_10m[timeIndex];
    const from = forecast.wind_direction_10m[timeIndex];
    const latitude = record.latitude;
    const longitude = record.longitude;
    if (typeof speed !== "number" || !Number.isFinite(speed) || speed < 0 || speed > 75
      || typeof from !== "number" || !Number.isFinite(from) || from < 0 || from > 360
      || typeof latitude !== "number" || typeof longitude !== "number" || !Number.isFinite(latitude) || !Number.isFinite(longitude)
      || Math.abs(latitude - coordinates[index][0]) > 0.15 || Math.abs(longitude - coordinates[index][1]) > 0.15) throw new Error("Invalid wind sample.");
    return { latitude, longitude, speedMetersPerSecond: speed, windFromDegrees: from, windToDegrees: (from + 180) % 360 };
  });
  return { model: "Open-Meteo NCEP GFS · 10 m forecast", validTimeUtc: sharedTime!, retrievedAtUtc: new Date(now).toISOString(), samples };
}

export function createWindArrowService(options: { fetchUpstream?: typeof fetch; now?: () => number } = {}) {
  const fetchUpstream = options.fetchUpstream ?? fetch;
  const now = options.now ?? Date.now;
  const cache = new Map<string, { expires: number; frame: WindArrowFrame }>();
  return async (request: Request): Promise<Response> => {
    let grid: GridRequest;
    try { grid = windArrowRequest(new URL(request.url)); }
    catch (error) { return Response.json({ error: (error as Error).message }, { status: 400, headers: { "Cache-Control": "no-store" } }); }
    const cached = cache.get(grid.key);
    const requestTime = now();
    if (cached && cached.expires > requestTime && Date.parse(cached.frame.validTimeUtc) >= requestTime - 35 * 60_000) {
      return Response.json(cached.frame, { headers: { ...frameHeaders(cached.frame, requestTime), "X-KFM-Wind-Cache": "HIT" } });
    }
    if (cached) cache.delete(grid.key);
    try {
      const response = await fetchUpstream(grid.url, { signal: AbortSignal.timeout(12_000), redirect: "manual" });
      if (!response.ok || !response.body || !(response.headers.get("content-type") ?? "").toLowerCase().includes("application/json")) throw new Error("Model response unavailable.");
      if (Number(response.headers.get("content-length")) > MAX_BYTES) throw new Error("Model response too large.");
      const reader = response.body.getReader();
      const chunks: Uint8Array[] = [];
      let total = 0;
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        total += value.byteLength;
        if (total > MAX_BYTES) { await reader.cancel(); throw new Error("Model response too large."); }
        chunks.push(value);
      }
      const bytes = new Uint8Array(total);
      let offset = 0;
      for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
      const frame = parseWindArrowResponse(JSON.parse(new TextDecoder().decode(bytes)), grid.coordinates, now());
      if (cache.size >= 12) cache.delete(cache.keys().next().value!);
      cache.set(grid.key, { expires: now() + CACHE_MS, frame });
      return Response.json(frame, { headers: frameHeaders(frame, now()) });
    } catch {
      return Response.json({ error: "Directional wind forecast unavailable; no arrows drawn." }, { status: 502, headers: { "Cache-Control": "no-store", "Retry-After": "60" } });
    }
  };
}

export const serveWindArrows = createWindArrowService();
