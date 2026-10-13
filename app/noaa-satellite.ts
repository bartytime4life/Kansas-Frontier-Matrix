export const NOAA_SATELLITE_SOURCE_URL = "https://www.nesdis.noaa.gov/imagery/satellite-maps/earth-real-time";
export const NOAA_SATELLITE_SERVICE_URL = "https://satellitemaps.nesdis.noaa.gov/arcgis/rest/services/MERGEDGC_Last_24hr/ImageServer";
export const NOAA_SATELLITE_VISIBLE_URL = "https://nowcoast.noaa.gov/geoserver/observations/satellite/ows";
export const NOAA_SATELLITE_VISIBLE_CAPABILITIES_URL = `${NOAA_SATELLITE_VISIBLE_URL}?service=WMS&version=1.3.0&request=GetCapabilities`;
export const NOAA_SATELLITE_VISIBLE_LAYER = "goes_visible_imagery";
export const NOAA_SATELLITE_FRAMES_PATH = "/api/noaa-satellite/frames";
export const NOAA_SATELLITE_MAX_FRAMES = 160;
export const NOAA_SATELLITE_FRESH_AGE_MS = 90 * 60 * 1000;

export type NoaaSatelliteFrame = Readonly<
  | { kind: "geocolor"; objectId: number; observedAt: string; validThrough: string }
  | { kind: "visible"; observedAt: string; validThrough: null }
>;
export type NoaaSatelliteManifest = Readonly<{
  kind: "noaa-goes-geocolor-frames" | "noaa-goes-visible-frames";
  product: "geocolor" | "visible";
  source: typeof NOAA_SATELLITE_SERVICE_URL | typeof NOAA_SATELLITE_VISIBLE_CAPABILITIES_URL;
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
    frames.push({ kind: "geocolor", objectId: objectId as number, observedAt: new Date(start).toISOString(), validThrough: new Date(end).toISOString() });
  }
  frames.sort((left, right) => Date.parse(left.observedAt) - Date.parse(right.observedAt));
  const unique = frames.filter((frame, index) => index === 0 || frame.observedAt !== frames[index - 1].observedAt);
  if (!unique.length) throw new Error("NOAA returned no dated satellite frames in the checked window.");
  if (unique.length > NOAA_SATELLITE_MAX_FRAMES) throw new Error("NOAA satellite frame count exceeded the supported window.");
  const latest = unique.at(-1)!;
  const latestAgeSeconds = Math.max(0, Math.round((now - Date.parse(latest.validThrough!)) / 1000));
  return Object.freeze({
    kind: "noaa-goes-geocolor-frames", product: "geocolor", source: NOAA_SATELLITE_SERVICE_URL, retrievedAt,
    frames: Object.freeze(unique.map((frame) => Object.freeze(frame))), frameCount: unique.length,
    freshness: latestAgeSeconds * 1000 <= NOAA_SATELLITE_FRESH_AGE_MS ? "current" : "delayed",
    latestAgeSeconds, partial: rejected > 0 || payload.exceededTransferLimit === true,
    limitation: "GOES East/West GeoColor imagery from NOAA's rolling 24-hour image catalog. Each displayed image is locked to one catalog raster ID and its provider start/end times. GeoColor is visual context, not a measured surface condition, fire confirmation, weather warning, forecast, or KFM EvidenceBundle. NOAA calls this map informational, not operational.",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
  });
};

/** Use NOAA's separately dated GOES visible WMS only while GeoColor is unavailable. */
export const buildNoaaVisibleManifest = (xml: string, retrievedAt: string): NoaaSatelliteManifest => {
  if (!timestamp(retrievedAt) || !xml.includes("WMS_Capabilities")) throw new Error("NOAA visible capabilities response was invalid.");
  const marker = `<Name>${NOAA_SATELLITE_VISIBLE_LAYER}</Name>`;
  const start = xml.indexOf(marker);
  const end = xml.indexOf("</Layer>", start);
  if (start < 0 || end < 0) throw new Error("NOAA visible imagery was absent from the fixed WMS service.");
  const dimension = xml.slice(start, end).match(/<Dimension\b[^>]*\bname=["']time["'][^>]*>([\s\S]*?)<\/Dimension>/i);
  if (!dimension) throw new Error("NOAA visible imagery had no dated frames.");
  const raw = dimension[1].split(",").map((value) => value.trim()).filter(Boolean);
  if (raw.length > 1000 || raw.some((value) => value.includes("/") || !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,3})?Z$/.test(value) || !Number.isFinite(Date.parse(value)))) {
    throw new Error("NOAA visible imagery times did not match the fixed WMS contract.");
  }
  const now = Date.parse(retrievedAt);
  const times = [...new Set(raw.map((value) => new Date(Date.parse(value)).toISOString()))]
    .filter((value) => Date.parse(value) >= now - 25 * 60 * 60 * 1000 && Date.parse(value) <= now + 5 * 60 * 1000)
    .sort()
    .slice(-NOAA_SATELLITE_MAX_FRAMES);
  if (!times.length) throw new Error("NOAA visible imagery had no recent dated frames.");
  const frames = Object.freeze(times.map((observedAt): NoaaSatelliteFrame => Object.freeze({ kind: "visible", observedAt, validThrough: null })));
  const latestAgeSeconds = Math.max(0, Math.round((now - Date.parse(times.at(-1)!)) / 1000));
  return Object.freeze({
    kind: "noaa-goes-visible-frames", product: "visible", source: NOAA_SATELLITE_VISIBLE_CAPABILITIES_URL, retrievedAt,
    frames, frameCount: frames.length,
    freshness: latestAgeSeconds * 1000 <= NOAA_SATELLITE_FRESH_AGE_MS ? "current" : "delayed",
    latestAgeSeconds, partial: false,
    limitation: "NOAA NESDIS GeoColor is unavailable. This fallback is NOAA nowCOAST GOES East/West visible Band 2 imagery, not GeoColor. Visible imagery is daylight-dependent and its exact selected observation time is shown. It is external visual context, not fire or smoke confirmation, a forecast, warning, or KFM EvidenceBundle.",
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
  });
};

export const isNoaaSatelliteManifest = (value: unknown): value is NoaaSatelliteManifest => {
  if (!record(value)
    || (value.product !== "geocolor" && value.product !== "visible")
    || value.kind !== (value.product === "geocolor" ? "noaa-goes-geocolor-frames" : "noaa-goes-visible-frames")
    || value.source !== (value.product === "geocolor" ? NOAA_SATELLITE_SERVICE_URL : NOAA_SATELLITE_VISIBLE_CAPABILITIES_URL)
    || !timestamp(value.retrievedAt) || !Array.isArray(value.frames) || value.frames.length < 1 || value.frames.length > NOAA_SATELLITE_MAX_FRAMES
    || value.frameCount !== value.frames.length || !["current", "delayed"].includes(String(value.freshness))
    || typeof value.latestAgeSeconds !== "number" || !Number.isFinite(value.latestAgeSeconds)
    || typeof value.partial !== "boolean" || typeof value.limitation !== "string" || value.evidenceRole !== "EXTERNAL_CONTEXT_ONLY") return false;
  let previous = -Infinity;
  for (const frame of value.frames) {
    if (!record(frame) || frame.kind !== value.product || !timestamp(frame.observedAt)) return false;
    const start = Date.parse(frame.observedAt);
    if (start <= previous) return false;
    if (value.product === "geocolor") {
      if (!Number.isSafeInteger(frame.objectId) || (frame.objectId as number) <= 0 || !timestamp(frame.validThrough) || Date.parse(frame.validThrough) <= start) return false;
    } else if (frame.validThrough !== null || "objectId" in frame) return false;
    previous = start;
  }
  return true;
};

/** ArcGIS raster ID locks one exact catalog image, avoiding ambiguous default mosaics. */
export const noaaSatelliteTileUrl = (frame: NoaaSatelliteFrame): string => {
  if (frame.kind === "visible") {
    if (!timestamp(frame.observedAt) || frame.validThrough !== null) throw new Error("Choose a checked NOAA visible frame.");
    return `${NOAA_SATELLITE_VISIBLE_URL}?service=WMS&version=1.3.0&request=GetMap&layers=${NOAA_SATELLITE_VISIBLE_LAYER}&styles=&bbox={bbox-epsg-3857}&width=256&height=256&crs=EPSG:3857&format=image/png&transparent=true&time=${encodeURIComponent(frame.observedAt)}`;
  }
  if (!Number.isSafeInteger(frame.objectId) || frame.objectId <= 0 || !timestamp(frame.observedAt) || !timestamp(frame.validThrough)) throw new Error("Choose a checked NOAA GeoColor frame.");
  const mosaicRule = encodeURIComponent(JSON.stringify({ mosaicMethod: "esriMosaicLockRaster", lockRasterIds: [frame.objectId] }));
  return `${NOAA_SATELLITE_SERVICE_URL}/exportImage?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=256%2C256&format=png32&transparent=true&mosaicRule=${mosaicRule}&f=image`;
};
