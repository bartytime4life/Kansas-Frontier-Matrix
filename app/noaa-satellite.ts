export const NOAA_SATELLITE_SOURCE_URL = "https://www.nesdis.noaa.gov/imagery/satellite-maps/earth-real-time";
export const NOAA_SATELLITE_SERVICE_URL = "https://satellitemaps.nesdis.noaa.gov/arcgis/rest/services/MERGEDGC_Last_24hr/ImageServer";
export const NOAA_SATELLITE_FRAMES_PATH = "/api/noaa-satellite/frames";
export const NOAA_SATELLITE_MAX_FRAMES = 160;
export const NOAA_SATELLITE_FRESH_AGE_MS = 90 * 60 * 1000;

export type NoaaSatelliteFrame = Readonly<{ objectId: number; observedAt: string; validThrough: string }>;
export type NoaaSatelliteManifest = Readonly<{
  kind: "noaa-goes-geocolor-frames";
  source: typeof NOAA_SATELLITE_SERVICE_URL;
  retrievedAt: string;
  frames: readonly NoaaSatelliteFrame[];
  frameCount: number;
  freshness: "current" | "delayed";
  latestAgeSeconds: number;
  partial: boolean;
  limitation: string;
  evidenceRole: "EXTERNAL_CONTEXT_ONLY";
}>;

const record = (value: unknown): value is Record<string, unknown> => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const timestamp = (value: unknown): value is string => typeof value === "string" && /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$/.test(value) && Number.isFinite(Date.parse(value));

/** Accept only dated catalog frames from the fixed NOAA ImageServer contract. */
export const buildNoaaSatelliteManifest = (payload: unknown, retrievedAt: string): NoaaSatelliteManifest => {
  if (!record(payload) || !Array.isArray(payload.features) || !timestamp(retrievedAt)) throw new Error("NOAA satellite catalog response was invalid.");
  const now = Date.parse(retrievedAt);
  const frames: NoaaSatelliteFrame[] = [];
  let rejected = 0;
  for (const feature of payload.features) {
    const attributes = record(feature) && record(feature.attributes) ? feature.attributes : null;
    const objectId = attributes?.objectid;
    const start = attributes?.start_time;
    const end = attributes?.end_time;
    const name = attributes?.name;
    if (!Number.isSafeInteger(objectId) || (objectId as number) <= 0 || typeof start !== "number" || typeof end !== "number"
      || !Number.isFinite(start) || !Number.isFinite(end) || end <= start || end - start > 20 * 60 * 1000
      || start < now - 25 * 60 * 60 * 1000 || start > now + 5 * 60 * 1000
      || typeof name !== "string" || !/^MERGEDGC\.10-minute\.\d{8}_\d{4}\.color$/.test(name)) { rejected += 1; continue; }
    frames.push({ objectId: objectId as number, observedAt: new Date(start).toISOString(), validThrough: new Date(end).toISOString() });
  }
  frames.sort((left, right) => Date.parse(left.observedAt) - Date.parse(right.observedAt));
  const unique = frames.filter((frame, index) => index === 0 || frame.objectId !== frames[index - 1].objectId);
  if (!unique.length) throw new Error("NOAA returned no dated satellite frames in the checked window.");
  if (unique.length > NOAA_SATELLITE_MAX_FRAMES) throw new Error("NOAA satellite frame count exceeded the supported window.");
  const latest = unique.at(-1)!;
  const latestAgeSeconds = Math.max(0, Math.round((now - Date.parse(latest.validThrough)) / 1000));
  return Object.freeze({
    kind: "noaa-goes-geocolor-frames", source: NOAA_SATELLITE_SERVICE_URL, retrievedAt,
    frames: Object.freeze(unique.map((frame) => Object.freeze(frame))), frameCount: unique.length,
    freshness: latestAgeSeconds * 1000 <= NOAA_SATELLITE_FRESH_AGE_MS ? "current" : "delayed",
    latestAgeSeconds, partial: rejected > 0 || payload.exceededTransferLimit === true,
    limitation: "GOES East/West GeoColor imagery from NOAA's rolling 24-hour image catalog. Each displayed image is locked to one catalog raster ID and its provider start/end times. GeoColor is visual context, not a measured surface condition, fire confirmation, weather warning, forecast, or KFM EvidenceBundle. NOAA calls this map informational, not operational.",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
  });
};

export const isNoaaSatelliteManifest = (value: unknown): value is NoaaSatelliteManifest => {
  if (!record(value) || value.kind !== "noaa-goes-geocolor-frames" || value.source !== NOAA_SATELLITE_SERVICE_URL
    || !timestamp(value.retrievedAt) || !Array.isArray(value.frames) || value.frames.length < 1 || value.frames.length > NOAA_SATELLITE_MAX_FRAMES
    || value.frameCount !== value.frames.length || !["current", "delayed"].includes(String(value.freshness))
    || typeof value.latestAgeSeconds !== "number" || !Number.isFinite(value.latestAgeSeconds)
    || typeof value.partial !== "boolean" || typeof value.limitation !== "string" || value.evidenceRole !== "EXTERNAL_CONTEXT_ONLY") return false;
  let previous = -Infinity;
  for (const frame of value.frames) {
    if (!record(frame) || !Number.isSafeInteger(frame.objectId) || (frame.objectId as number) <= 0 || !timestamp(frame.observedAt) || !timestamp(frame.validThrough)) return false;
    const start = Date.parse(frame.observedAt);
    if (start <= previous || Date.parse(frame.validThrough) <= start) return false;
    previous = start;
  }
  return true;
};

/** ArcGIS raster ID locks one exact catalog image, avoiding ambiguous default mosaics. */
export const noaaSatelliteTileUrl = (objectId: number): string => {
  if (!Number.isSafeInteger(objectId) || objectId <= 0) throw new Error("Choose a checked NOAA satellite frame.");
  const mosaicRule = encodeURIComponent(JSON.stringify({ mosaicMethod: "esriMosaicLockRaster", lockRasterIds: [objectId] }));
  return `${NOAA_SATELLITE_SERVICE_URL}/exportImage?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&transparent=true&mosaicRule=${mosaicRule}&f=image`;
};
