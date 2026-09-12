export const NOAA_RADAR_PRODUCT_ID = "conus_base_reflectivity_mosaic";
export const NOAA_RADAR_PRODUCT_TITLE = "CONUS weather radar base reflectivity";
export const NOAA_RADAR_SOURCE_TITLE = "NOAA nowCOAST · NWS/OAR MRMS";
export const NOAA_RADAR_CAPABILITIES_URL = "https://nowcoast.noaa.gov/geoserver/weather_radar/wms?service=WMS&version=1.3.0&request=GetCapabilities";
export const NOAA_RADAR_SERVICE_URL = "https://nowcoast.noaa.gov/geoserver/weather_radar/wms";
export const NOAA_RADAR_LEGEND_URL = "https://nowcoast.noaa.gov/geoserver/observations/weather_radar/ows?service=WMS&version=1.3.0&request=GetLegendGraphic&format=image%2Fpng&width=272&height=21&layer=conus_base_reflectivity_mosaic";
export const NOAA_RADAR_FRAME_API_PATH = "/api/noaa-radar/frames";
export const NOAA_RADAR_EXPECTED_CADENCE_SECONDS = 240;
export const NOAA_RADAR_MAX_FRESH_AGE_SECONDS = 15 * 60;
export const NOAA_RADAR_MAX_SOURCE_FRAMES = 180;
export const NOAA_RADAR_MAX_LOOP_FRAMES = 32;

export type NoaaRadarLoopSpanMinutes = 30 | 60 | 120;
export type NoaaRadarPlaybackSpeed = 0.5 | 1 | 2;
export type NoaaRadarManifestState = "idle" | "loading" | "ready" | "error";
export type NoaaRadarFreshness = "current" | "delayed";

export type NoaaRadarManifest = Readonly<{
  productId: typeof NOAA_RADAR_PRODUCT_ID;
  productTitle: typeof NOAA_RADAR_PRODUCT_TITLE;
  sourceTitle: typeof NOAA_RADAR_SOURCE_TITLE;
  sourceUrl: typeof NOAA_RADAR_CAPABILITIES_URL;
  serviceUrl: typeof NOAA_RADAR_SERVICE_URL;
  retrievedAt: string;
  upstreamDefaultTime: string | null;
  frames: readonly string[];
  frameCount: number;
  nominalCadenceSeconds: number;
  gapCount: number;
  retentionMinutes: number;
  freshness: NoaaRadarFreshness;
  latestAgeSeconds: number;
  interpolation: false;
  evidenceRole: "EXTERNAL_CONTEXT_ONLY";
  limitation: string;
}>;

const toIsoTimestamp = (value: string): string | null => {
  const trimmed = value.trim();
  if (!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,3})?Z$/.test(trimmed)) return null;
  const milliseconds = Date.parse(trimmed);
  return Number.isFinite(milliseconds) ? new Date(milliseconds).toISOString() : null;
};

const median = (values: readonly number[]): number => {
  if (values.length === 0) return NOAA_RADAR_EXPECTED_CADENCE_SECONDS;
  const sorted = [...values].sort((left, right) => left - right);
  const middle = Math.floor(sorted.length / 2);
  return sorted.length % 2 === 0 ? (sorted[middle - 1] + sorted[middle]) / 2 : sorted[middle];
};

/**
 * Parses only the fixed nowCOAST CONUS layer and its explicit ISO8601 frame
 * list. Interval expansion and nearest-time invention are intentionally not
 * supported: a changed or ambiguous upstream contract fails closed.
 */
export const parseNoaaRadarCapabilities = (xml: string): Readonly<{
  frames: readonly string[];
  upstreamDefaultTime: string | null;
}> => {
  const layerMarker = `<Name>${NOAA_RADAR_PRODUCT_ID}</Name>`;
  const markerIndex = xml.indexOf(layerMarker);
  if (markerIndex < 0) throw new Error("The NOAA capabilities response omitted the fixed CONUS radar layer.");
  const layerEnd = xml.indexOf("</Layer>", markerIndex);
  if (layerEnd < 0) throw new Error("The NOAA CONUS radar layer description was incomplete.");
  const layerXml = xml.slice(markerIndex, layerEnd);
  const dimension = layerXml.match(/<Dimension\b([^>]*)\bname=["']time["']([^>]*)>([\s\S]*?)<\/Dimension>/i);
  if (!dimension) throw new Error("The NOAA CONUS radar layer omitted its explicit time dimension.");
  const attributes = `${dimension[1]} ${dimension[2]}`;
  const rawDefault = attributes.match(/\bdefault=["']([^"']+)["']/i)?.[1] ?? "";
  const upstreamDefaultTime = toIsoTimestamp(rawDefault);
  const rawTokens = dimension[3].split(",").map((value) => value.trim()).filter(Boolean);
  if (rawTokens.some((value) => value.includes("/"))) {
    throw new Error("The NOAA radar time dimension changed from explicit observations to an unsupported interval.");
  }
  const parsed = rawTokens.map(toIsoTimestamp);
  if (parsed.some((value) => value === null)) throw new Error("The NOAA radar time dimension contained an invalid timestamp.");
  const frames = [...new Set(parsed as string[])]
    .sort((left, right) => Date.parse(left) - Date.parse(right))
    .slice(-NOAA_RADAR_MAX_SOURCE_FRAMES);
  if (frames.length < 2) throw new Error("The NOAA radar loop exposed fewer than two usable observation frames.");
  return Object.freeze({ frames: Object.freeze(frames), upstreamDefaultTime });
};

export const buildNoaaRadarManifest = (xml: string, retrievedAt: string): NoaaRadarManifest => {
  const retrievedMilliseconds = Date.parse(retrievedAt);
  if (!Number.isFinite(retrievedMilliseconds)) throw new Error("The radar retrieval timestamp was invalid.");
  const parsed = parseNoaaRadarCapabilities(xml);
  const frameMilliseconds = parsed.frames.map(Date.parse);
  const positiveFrameDeltas = frameMilliseconds.slice(1)
    .map((value, index) => Math.round((value - frameMilliseconds[index]) / 1000))
    .filter((value) => value > 0);
  const cadenceSamples = positiveFrameDeltas.filter((value) => value < 1800);
  const nominalCadenceSeconds = Math.max(1, Math.round(median(cadenceSamples)));
  const gapCount = positiveFrameDeltas.filter((value) => value > nominalCadenceSeconds * 1.75).length;
  const latestAgeSeconds = Math.max(0, Math.round((retrievedMilliseconds - frameMilliseconds.at(-1)!) / 1000));
  const retentionMinutes = Math.max(0, Math.round((frameMilliseconds.at(-1)! - frameMilliseconds[0]) / 60000));
  const freshness: NoaaRadarFreshness = latestAgeSeconds <= NOAA_RADAR_MAX_FRESH_AGE_SECONDS
    ? "current"
    : "delayed";
  return Object.freeze({
    productId: NOAA_RADAR_PRODUCT_ID,
    productTitle: NOAA_RADAR_PRODUCT_TITLE,
    sourceTitle: NOAA_RADAR_SOURCE_TITLE,
    sourceUrl: NOAA_RADAR_CAPABILITIES_URL,
    serviceUrl: NOAA_RADAR_SERVICE_URL,
    retrievedAt: new Date(retrievedMilliseconds).toISOString(),
    upstreamDefaultTime: parsed.upstreamDefaultTime,
    frames: parsed.frames,
    frameCount: parsed.frames.length,
    nominalCadenceSeconds,
    gapCount,
    retentionMinutes,
    freshness,
    latestAgeSeconds,
    interpolation: false,
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    limitation: "Observed NOAA nowCOAST MRMS base-reflectivity mosaics only. Frames may be delayed, incomplete, revised, or unavailable and do not establish precipitation rate, storm motion, warning status, forecast, or KFM evidence support.",
  });
};

export const isNoaaRadarManifest = (value: unknown): value is NoaaRadarManifest => {
  if (!value || typeof value !== "object") return false;
  const candidate = value as Partial<NoaaRadarManifest>;
  return candidate.productId === NOAA_RADAR_PRODUCT_ID
    && candidate.interpolation === false
    && candidate.evidenceRole === "EXTERNAL_CONTEXT_ONLY"
    && typeof candidate.retrievedAt === "string"
    && typeof candidate.nominalCadenceSeconds === "number"
    && Number.isFinite(candidate.nominalCadenceSeconds)
    && Array.isArray(candidate.frames)
    && candidate.frames.length >= 2
    && candidate.frames.length <= NOAA_RADAR_MAX_SOURCE_FRAMES
    && candidate.frames.every((frame) => typeof frame === "string" && toIsoTimestamp(frame) === frame);
};

export const selectNoaaRadarLoopFrames = (
  frames: readonly string[],
  spanMinutes: NoaaRadarLoopSpanMinutes,
  maxFrames = NOAA_RADAR_MAX_LOOP_FRAMES,
): readonly string[] => {
  if (frames.length === 0) return Object.freeze([]);
  const sorted = [...new Set(frames.map(toIsoTimestamp).filter((value): value is string => Boolean(value)))]
    .sort((left, right) => Date.parse(left) - Date.parse(right));
  const latest = Date.parse(sorted.at(-1)!);
  const cutoff = latest - spanMinutes * 60_000;
  return Object.freeze(sorted.filter((frame) => Date.parse(frame) >= cutoff).slice(-Math.max(2, Math.floor(maxFrames))));
};

export const noaaRadarTileUrl = (observedAt: string): string => {
  const normalized = toIsoTimestamp(observedAt);
  if (!normalized) throw new Error("A NOAA radar tile request requires an exact advertised observation timestamp.");
  const parameters = [
    "service=WMS",
    "version=1.3.0",
    "request=GetMap",
    `layers=${NOAA_RADAR_PRODUCT_ID}`,
    "styles=weather_radar_base_reflectivity",
    "bbox={bbox-epsg-3857}",
    "width=256",
    "height=256",
    "crs=EPSG:3857",
    "format=image/png",
    "transparent=true",
  ];
  parameters.push(`time=${encodeURIComponent(normalized)}`);
  return `${NOAA_RADAR_SERVICE_URL}?${parameters.join("&")}`;
};

export const nextNoaaRadarFrameIndex = (frameCount: number, currentIndex: number, direction: "forward" | "reverse", loop: boolean): number | null => {
  if (frameCount < 1) return null;
  const safeIndex = Math.max(0, Math.min(frameCount - 1, Math.floor(currentIndex)));
  const candidate = safeIndex + (direction === "forward" ? 1 : -1);
  if (candidate >= 0 && candidate < frameCount) return candidate;
  if (!loop) return null;
  return direction === "forward" ? 0 : frameCount - 1;
};

export const noaaRadarFrameAgeMinutes = (observedAt: string, now: number): number | null => {
  const timestamp = Date.parse(observedAt);
  if (!Number.isFinite(timestamp) || !Number.isFinite(now)) return null;
  return Math.max(0, Math.round((now - timestamp) / 60000));
};

export const noaaRadarManifestIsFresh = (manifest: NoaaRadarManifest | null, now: number): boolean => {
  const latest = manifest?.frames.at(-1);
  if (!latest || !Number.isFinite(now)) return false;
  const latestMilliseconds = Date.parse(latest);
  if (!Number.isFinite(latestMilliseconds)) return false;
  const ageMilliseconds = now - latestMilliseconds;
  return ageMilliseconds >= -5 * 60_000 && ageMilliseconds <= NOAA_RADAR_MAX_FRESH_AGE_SECONDS * 1000;
};
