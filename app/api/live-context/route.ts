import { NextRequest, NextResponse } from "next/server";
import type { Feature, FeatureCollection, Geometry, GeoJsonProperties } from "geojson";
import { EVENT_BOUNDS, eventDay, advanceEventDay, intervalDays, parseSmokeKml, smokeUrl } from "../../event-atlas";
import { boundedFetch } from "../event-atlas/upstream";
import { countyBaseline } from "../../county-baseline";

export const dynamic = "force-dynamic";

const USGS_URL = "https://api.waterdata.usgs.gov/ogcapi/v1/collections/latest-continuous/items";
const USGS_EARTHQUAKE_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query";
const NWS_ALERTS_URL = "https://api.weather.gov/alerts/active?area=KS";
const RASPBERRY_SHAKE_STATION_URL = "https://data.raspberryshake.org/fdsnws/station/1/query";
const NWS_USER_AGENT = "KansasFrontierMatrixExplorer/1.0 (https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site)";
const MAX_RESPONSE_BYTES = 8 * 1024 * 1024;
const MAX_NWS_ZONE_REQUESTS = 36;
const MAX_NWS_FEATURES = 160;
const MAX_EARTHQUAKE_FEATURES = 250;
const MAX_RASPBERRY_SHAKE_STATIONS = 250;

type Feed = "census-counties" | "usgs-streamflow" | "usgs-earthquakes" | "nws-alerts" | "noaa-hms-smoke" | "raspberry-shake-stations";
type JsonRecord = Record<string, unknown>;

class UpstreamError extends Error {
  constructor(message: string, readonly timeout = false) {
    super(message);
  }
}

const isRecord = (value: unknown): value is JsonRecord => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const asString = (value: unknown) => typeof value === "string" ? value : null;
const asNumber = (value: unknown) => typeof value === "number" && Number.isFinite(value) ? value : null;
const asNumeric = (value: unknown) => {
  const parsed = typeof value === "number" ? value : typeof value === "string" && value.trim() !== "" ? Number(value) : Number.NaN;
  return Number.isFinite(parsed) ? parsed : null;
};

const fetchBoundedJsonValue = async (url: string, timeoutMs: number, init?: RequestInit): Promise<unknown> => {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const response = await fetch(url, { ...init, cache: "no-store", redirect: "manual", signal: controller.signal });
    if (!response.ok) throw new UpstreamError(`Official upstream returned HTTP ${response.status}.`);
    const declaredLength = Number(response.headers.get("content-length") ?? "0");
    if (declaredLength > MAX_RESPONSE_BYTES) throw new UpstreamError("Official upstream response exceeded the bounded adapter limit.");
    const body = await response.arrayBuffer();
    if (body.byteLength > MAX_RESPONSE_BYTES) throw new UpstreamError("Official upstream response exceeded the bounded adapter limit.");
    return JSON.parse(new TextDecoder().decode(body)) as unknown;
  } catch (error) {
    if (error instanceof UpstreamError) throw error;
    if (error instanceof Error && error.name === "AbortError") throw new UpstreamError("Official upstream request timed out.", true);
    throw new UpstreamError(error instanceof Error ? error.message : "Official upstream request failed.");
  } finally {
    clearTimeout(timeout);
  }
};

const fetchBoundedJson = async (url: string, timeoutMs: number, init?: RequestInit): Promise<JsonRecord> => {
  const parsed = await fetchBoundedJsonValue(url, timeoutMs, init);
  if (!isRecord(parsed)) throw new UpstreamError("Official upstream response was not a JSON object.");
  return parsed;
};

const fetchBoundedJsonArray = async (url: string, timeoutMs: number, init?: RequestInit): Promise<unknown[]> => {
  const parsed = await fetchBoundedJsonValue(url, timeoutMs, init);
  if (!Array.isArray(parsed)) throw new UpstreamError("Official upstream response was not a JSON array.");
  return parsed;
};

const collectionFeatures = (payload: JsonRecord): JsonRecord[] => Array.isArray(payload.features)
  ? payload.features.filter(isRecord)
  : [];

const envelope = (
  feed: Feed,
  data: FeatureCollection,
  source: string,
  limitation: string,
  retrievedAt: string,
  upstreamUpdatedAt: string | null,
  partial = false,
  truncated = false,
) => ({
  feed,
  state: partial ? "partial" : data.features.length === 0 ? "empty" : "ready",
  retrievedAt,
  upstreamUpdatedAt,
  featureCount: data.features.length,
  data,
  source,
  limitation,
  truncated,
});

const censusCounties = async () => {
  const baseline = await countyBaseline("2020");
  return envelope("census-counties", baseline.data, baseline.source, baseline.limitation, baseline.retrievedAt, null, false);
};

const latestStreamflow = async () => {
  const retrievedAt = new Date().toISOString();
  const start = new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString();
  const url = new URL(USGS_URL);
  url.searchParams.set("f", "json");
  url.searchParams.set("limit", "1000");
  url.searchParams.set("state_code", "20");
  url.searchParams.set("agency_code", "USGS");
  url.searchParams.set("site_type_code", "ST");
  url.searchParams.set("parameter_code", "00060");
  url.searchParams.set("datetime", `${start}/..`);
  const payload = await fetchBoundedJson(url.toString(), 15_000);
  const newest = new Map<string, Feature<Geometry, GeoJsonProperties>>();
  let newestTimestamp: string | null = null;

  for (const candidate of collectionFeatures(payload)) {
    if (!isRecord(candidate.geometry) || candidate.geometry.type !== "Point") continue;
    const properties = isRecord(candidate.properties) ? candidate.properties : {};
    const monitoringLocationId = asString(properties.monitoring_location_id);
    const observedAt = asString(properties.time);
    if (!monitoringLocationId || !observedAt) continue;
    const value = asNumber(properties.value);
    const unit = asString(properties.unit_of_measure) ?? "unknown unit";
    const current = newest.get(monitoringLocationId);
    if (current && String(current.properties?.observedAt ?? "") >= observedAt) continue;
    const feature: Feature<Geometry, GeoJsonProperties> = {
      type: "Feature",
      id: monitoringLocationId,
      geometry: candidate.geometry as unknown as Geometry,
      properties: {
        featureId: `usgs-streamflow-${monitoringLocationId}`,
        name: monitoringLocationId,
        monitoringLocationId,
        observedAt,
        value,
        displayValue: value === null ? "not reported" : `${value.toLocaleString("en-US")} ${unit}`,
        unit,
        parameterCode: asString(properties.parameter_code),
        statisticId: asString(properties.statistic_id),
        approvalStatus: asString(properties.approval_status),
        qualifier: asString(properties.qualifier),
        lastModified: asString(properties.last_modified),
        sourceOrganization: "U.S. Geological Survey",
        evidenceRole: "EXTERNAL_CONTEXT_ONLY",
        retrievedAt,
      },
    };
    newest.set(monitoringLocationId, feature);
    if (!newestTimestamp || observedAt > newestTimestamp) newestTimestamp = observedAt;
  }

  const links = Array.isArray(payload.links) ? payload.links.filter(isRecord) : [];
  const truncated = links.some((link) => asString(link.rel) === "next");
  const features = [...newest.values()];
  return envelope(
    "usgs-streamflow",
    { type: "FeatureCollection", features },
    url.toString(),
    `${truncated ? "The OGC API advertised another page; this bounded view is partial. " : ""}Latest Kansas USGS streamflow values within a rolling 24-hour request window; provisional, delayed, revised, or incomplete values remain possible. Not flood guidance or KFM evidence.`,
    retrievedAt,
    newestTimestamp,
    truncated,
    truncated,
  );
};

const recentEarthquakes = async (day: string | null = null) => {
  const retrievedAt = new Date().toISOString();
  const start = day ? `${day}T00:00:00.000Z` : new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString();
  const end = day ? `${advanceEventDay(day, 1)}T00:00:00.000Z` : retrievedAt;
  const url = new URL(USGS_EARTHQUAKE_URL);
  url.searchParams.set("format", "geojson");
  url.searchParams.set("eventtype", "earthquake");
  url.searchParams.set("starttime", start);
  url.searchParams.set("endtime", end);
  url.searchParams.set("minlatitude", "36.9");
  url.searchParams.set("maxlatitude", "40.1");
  url.searchParams.set("minlongitude", "-102.1");
  url.searchParams.set("maxlongitude", "-94.5");
  url.searchParams.set("orderby", "time");
  url.searchParams.set("limit", String(MAX_EARTHQUAKE_FEATURES));
  const payload = await fetchBoundedJson(url.toString(), 15_000);
  let newestTimestamp: string | null = null;
  const catalogFeatures = collectionFeatures(payload);
  const features: Feature<Geometry, GeoJsonProperties>[] = catalogFeatures.slice(0, MAX_EARTHQUAKE_FEATURES).flatMap((candidate) => {
    if (!isRecord(candidate.geometry) || candidate.geometry.type !== "Point" || !Array.isArray(candidate.geometry.coordinates)) return [];
    const coordinates = candidate.geometry.coordinates;
    const longitude = asNumeric(coordinates[0]);
    const latitude = asNumeric(coordinates[1]);
    const depthKilometers = asNumeric(coordinates[2]);
    if (longitude === null || latitude === null || longitude < -102.1 || longitude > -94.5 || latitude < 36.9 || latitude > 40.1) return [];
    const properties = isRecord(candidate.properties) ? candidate.properties : {};
    const eventId = asString(candidate.id) ?? asString(properties.code);
    const observedMilliseconds = asNumeric(properties.time);
    if (!eventId || observedMilliseconds === null) return [];
    const observedAt = new Date(observedMilliseconds).toISOString();
    if (observedAt < start || observedAt >= end) return [];
    if (!newestTimestamp || observedAt > newestTimestamp) newestTimestamp = observedAt;
    const magnitude = asNumeric(properties.mag);
    return [{
      type: "Feature" as const,
      id: eventId,
      geometry: { type: "Point" as const, coordinates: [longitude, latitude] },
      properties: {
        featureId: `usgs-earthquake-${eventId}`,
        name: asString(properties.title) ?? asString(properties.place) ?? `USGS event ${eventId}`,
        place: asString(properties.place),
        magnitude,
        magnitudeType: asString(properties.magType),
        depthKilometers,
        observedAt,
        updatedAt: asNumeric(properties.updated) === null ? null : new Date(asNumeric(properties.updated)!).toISOString(),
        reviewStatus: asString(properties.status),
        eventType: asString(properties.type),
        detailUrl: asString(properties.url),
        tsunamiFlag: asNumeric(properties.tsunami),
        sourceOrganization: "U.S. Geological Survey",
        evidenceRole: "EXTERNAL_CONTEXT_ONLY",
        retrievedAt,
      },
    }];
  });
  const metadata = isRecord(payload.metadata) ? payload.metadata : {};
  const totalCount = asNumeric(metadata.count);
  const truncated = (totalCount ?? catalogFeatures.length) > features.length;
  return envelope(
    "usgs-earthquakes",
    { type: "FeatureCollection", features },
    url.toString(),
    `${features.length} USGS catalog event${features.length === 1 ? "" : "s"} returned for the Kansas bounding window for ${start} through ${end} (end excluded). Locations, depths, magnitudes, and review status may change. This is not an earthquake alert, hazard forecast, or KFM evidence.`,
    retrievedAt,
    newestTimestamp,
    false,
    truncated,
  );
};

const allowedZoneUrl = (value: unknown): string | null => {
  if (typeof value !== "string") return null;
  try {
    const url = new URL(value);
    if (url.protocol !== "https:" || url.hostname !== "api.weather.gov") return null;
    return /^\/zones\/(forecast|county|fire)\/(KSZ|KSC)\d{3}$/.test(url.pathname) ? url.toString() : null;
  } catch {
    return null;
  }
};

const activeNwsAlerts = async () => {
  const retrievedAt = new Date().toISOString();
  const headers = { Accept: "application/geo+json, application/json", "User-Agent": NWS_USER_AGENT };
  const payload = await fetchBoundedJson(NWS_ALERTS_URL, 15_000, { headers });
  const alerts = collectionFeatures(payload);
  const zoneUrls = [...new Set(alerts.flatMap((alert) => {
    const properties = isRecord(alert.properties) ? alert.properties : {};
    return Array.isArray(properties.affectedZones) ? properties.affectedZones.map(allowedZoneUrl).filter((value): value is string => Boolean(value)) : [];
  }))];
  const selectedZoneUrls = zoneUrls.slice(0, MAX_NWS_ZONE_REQUESTS);
  const zoneResults = await Promise.allSettled(selectedZoneUrls.map(async (url) => ({ url, payload: await fetchBoundedJson(url, 18_000, { headers }) })));
  const zones = new Map<string, JsonRecord>();
  let failedZoneCount = 0;
  for (const result of zoneResults) {
    if (result.status === "rejected") {
      failedZoneCount += 1;
      continue;
    }
    zones.set(result.value.url, result.value.payload);
  }

  const features: Feature<Geometry, GeoJsonProperties>[] = [];
  let newestTimestamp: string | null = null;
  for (const [alertIndex, alert] of alerts.entries()) {
    const properties = isRecord(alert.properties) ? alert.properties : {};
    const alertId = asString(properties.id) ?? asString(alert.id) ?? `alert-${alertIndex}`;
    const safe = {
      event: asString(properties.event), severity: asString(properties.severity), urgency: asString(properties.urgency), certainty: asString(properties.certainty),
      headline: asString(properties.headline), areaDesc: asString(properties.areaDesc), effective: asString(properties.effective), expires: asString(properties.expires), senderName: asString(properties.senderName),
    };
    if (safe.effective && (!newestTimestamp || safe.effective > newestTimestamp)) newestTimestamp = safe.effective;
    if (isRecord(alert.geometry) && (alert.geometry.type === "Polygon" || alert.geometry.type === "MultiPolygon")) {
      features.push({ type: "Feature", id: `${alertId}-geometry`, geometry: alert.geometry as unknown as Geometry, properties: { featureId: `nws-alert-${alertId}-geometry`, ...safe, zoneName: null, zoneExpirationDate: null, sourceOrganization: "NOAA National Weather Service", evidenceRole: "EXTERNAL_CONTEXT_ONLY", retrievedAt } });
    }
    const affected = Array.isArray(properties.affectedZones) ? properties.affectedZones.map(allowedZoneUrl).filter((value): value is string => Boolean(value)) : [];
    for (const zoneUrl of affected) {
      const zone = zones.get(zoneUrl);
      const geometry = zone && isRecord(zone.geometry) && (zone.geometry.type === "Polygon" || zone.geometry.type === "MultiPolygon") ? zone.geometry as unknown as Geometry : null;
      if (!geometry) continue;
      const zoneProperties = isRecord(zone?.properties) ? zone.properties : {};
      const zoneCode = new URL(zoneUrl).pathname.split("/").at(-1) ?? "zone";
      features.push({ type: "Feature", id: `${alertId}-${zoneCode}`, geometry, properties: { featureId: `nws-alert-${alertId}-${zoneCode}`, ...safe, zoneName: asString(zoneProperties.name), zoneExpirationDate: asString(zoneProperties.expirationDate), sourceOrganization: "NOAA National Weather Service", evidenceRole: "EXTERNAL_CONTEXT_ONLY", retrievedAt } });
    }
  }

  const capped = features.length > MAX_NWS_FEATURES;
  const data = { type: "FeatureCollection" as const, features: features.slice(0, MAX_NWS_FEATURES) };
  const partial = failedZoneCount > 0 || zoneUrls.length > MAX_NWS_ZONE_REQUESTS || capped;
  return envelope(
    "nws-alerts",
    data,
    NWS_ALERTS_URL,
    `${alerts.length} active Kansas alert record${alerts.length === 1 ? "" : "s"} returned at retrieval; ${failedZoneCount} selected zone lookup${failedZoneCount === 1 ? "" : "s"} failed. Zero mapped features is never an all-clear. This bounded display is not a warning-delivery service or KFM evidence.`,
    retrievedAt,
    newestTimestamp,
    partial,
    capped || zoneUrls.length > MAX_NWS_ZONE_REQUESTS,
  );
};

const currentHmsSmoke = async (day: string | null = null) => {
  const retrievedAt = new Date().toISOString();
  const endMs = day ? Date.parse(`${advanceEventDay(day, 1)}T00:00:00Z`) : Date.now();
  const startMs = endMs - 24 * 60 * 60 * 1000;
  const start = new Date(startMs).toISOString();
  const end = new Date(endMs).toISOString();
  const days = intervalDays(start, end);
  const results = await Promise.all(days.map(async (day) => {
    const artifact = smokeUrl(day);
    try {
      const response = await boundedFetch(artifact, 2 * 1024 * 1024);
      return { day, artifact, collection: parseSmokeKml(response.text(), artifact), error: null };
    } catch (error) {
      return { day, artifact, collection: null, error: error instanceof Error ? error.message : "NOAA HMS publication unavailable." };
    }
  }));
  const failures = results.filter((result) => result.error).map((result) => `${result.day}: ${result.error}`);
  if (failures.length === results.length) throw new UpstreamError(`NOAA HMS smoke publications were unavailable for the bounded window (${failures.join("; ")}).`);
  const seen = new Set<string>();
  const features: Feature<Geometry, GeoJsonProperties>[] = [];
  let newestTimestamp: string | null = null;
  for (const result of results) {
    for (const feature of result.collection?.features ?? []) {
      if (feature.properties.endMs <= startMs || feature.properties.startMs >= endMs) continue;
      const key = JSON.stringify([feature.properties.start, feature.properties.end, feature.properties.density, feature.geometry]);
      if (seen.has(key)) continue;
      seen.add(key);
      const featureId = `noaa-hms-smoke-${feature.properties.startMs}-${features.length}`;
      features.push({
        ...feature,
        id: featureId,
        properties: { ...feature.properties, featureId },
      });
      if (!newestTimestamp || feature.properties.end > newestTimestamp) newestTimestamp = feature.properties.end;
    }
  }
  const data: FeatureCollection = { type: "FeatureCollection", features };
  return envelope(
    "noaa-hms-smoke",
    data,
    "NOAA HMS Smoke Polygons KML (daily publications)",
    `NOAA HMS satellite-analyzed smoke polygons intersecting Kansas during the rolling 24-hour window ${start} through ${end}. ${failures.length ? `Unavailable daily publication${failures.length === 1 ? "" : "s"}: ${failures.join("; ")}. ` : ""}Density and Start/End are provider fields. A polygon is not a fire perimeter, plume altitude, surface PM2.5, exposure, measured transport, health guidance, warning, or all-clear; missing polygons do not prove clear air.`,
    retrievedAt,
    newestTimestamp,
    failures.length > 0,
  );
};

const normalizedFdsnHeader = (line: string) => line.replace(/^\s*#\s*/, "").split("|").map((value) => value.trim().toLowerCase().replace(/[^a-z0-9]/g, ""));

const raspberryShakeStations = async (day: string | null = null) => {
  const retrievedAt = new Date().toISOString();
  const url = new URL(RASPBERRY_SHAKE_STATION_URL);
  url.searchParams.set("net", "AM");
  url.searchParams.set("level", "station");
  url.searchParams.set("minlat", String(EVENT_BOUNDS[1]));
  url.searchParams.set("maxlat", String(EVENT_BOUNDS[3]));
  url.searchParams.set("minlon", String(EVENT_BOUNDS[0]));
  url.searchParams.set("maxlon", String(EVENT_BOUNDS[2]));
  url.searchParams.set("format", "text");
  url.searchParams.set("startbefore", day ? `${advanceEventDay(day, 1)}T00:00:00` : retrievedAt.replace("Z", ""));
  url.searchParams.set("endafter", day ? `${day}T00:00:00` : retrievedAt.replace("Z", ""));
  const response = await boundedFetch(url.toString(), 2 * 1024 * 1024);
  const lines = response.text().split(/\r?\n/).filter((line) => line.trim() !== "");
  const headerIndex = lines.findIndex((line) => {
    const header = normalizedFdsnHeader(line);
    return header.includes("network") && header.includes("station") && header.includes("latitude") && header.includes("longitude");
  });
  if (headerIndex < 0) throw new UpstreamError("Raspberry Shake FDSN station response omitted its required text header.");
  const header = normalizedFdsnHeader(lines[headerIndex]);
  const fieldIndex = (...names: string[]) => names.map((name) => header.indexOf(name)).find((index) => index >= 0) ?? -1;
  const networkIndex = fieldIndex("network");
  const stationIndex = fieldIndex("station");
  const latitudeIndex = fieldIndex("latitude");
  const longitudeIndex = fieldIndex("longitude");
  const elevationIndex = fieldIndex("elevation", "elevationm");
  const siteNameIndex = fieldIndex("sitename", "stationname", "name");
  const startIndex = fieldIndex("starttime");
  const endIndex = fieldIndex("endtime");
  const features: Feature<Geometry, GeoJsonProperties>[] = [];
  let skipped = 0;
  let validRows = 0;
  for (const line of lines.slice(headerIndex + 1)) {
    if (line.trimStart().startsWith("#")) continue;
    const values = line.split("|").map((value) => value.trim());
    const network = networkIndex >= 0 ? values[networkIndex] : "";
    const station = stationIndex >= 0 ? values[stationIndex] : "";
    const latitude = latitudeIndex >= 0 ? asNumeric(values[latitudeIndex]) : null;
    const longitude = longitudeIndex >= 0 ? asNumeric(values[longitudeIndex]) : null;
    if (!network || !station || latitude === null || longitude === null || latitude < EVENT_BOUNDS[1] || latitude > EVENT_BOUNDS[3] || longitude < EVENT_BOUNDS[0] || longitude > EVENT_BOUNDS[2]) {
      skipped += 1;
      continue;
    }
    validRows += 1;
    if (features.length >= MAX_RASPBERRY_SHAKE_STATIONS) continue;
    const featureId = `raspberry-shake-${network}-${station}-${startIndex >= 0 ? values[startIndex] : features.length}`;
    const elevation = elevationIndex >= 0 ? asNumeric(values[elevationIndex]) : null;
    const startTime = startIndex >= 0 && values[startIndex] ? values[startIndex] : null;
    const endTime = endIndex >= 0 && values[endIndex] ? values[endIndex] : null;
    const siteName = siteNameIndex >= 0 && values[siteNameIndex] ? values[siteNameIndex] : `${network}.${station}`;
    features.push({
      type: "Feature",
      id: featureId,
      geometry: { type: "Point", coordinates: [longitude, latitude] },
      properties: {
        featureId,
        name: siteName,
        network,
        station,
        latitude,
        longitude,
        elevationMeters: elevation,
        startTime,
        endTime,
        dataRole: "FDSN station metadata",
        waveformAvailability: "FDSN archive is delayed by at least 30 minutes; this map does not stream waveform samples.",
        stationViewUrl: "https://stationview.raspberryshake.org/",
        sourceOrganization: "Raspberry Shake · FDSN AM network",
        evidenceRole: "EXTERNAL_CONTEXT_ONLY",
        retrievedAt,
      },
    });
  }
  const truncated = validRows > features.length;
  return envelope(
    "raspberry-shake-stations",
    { type: "FeatureCollection", features },
    url.toString(),
    `Raspberry Shake AM station metadata inside the Kansas bounding window. ${validRows} valid station row${validRows === 1 ? "" : "s"} were found; ${skipped} malformed or out-of-bounds row${skipped === 1 ? "" : "s"} were withheld${truncated ? ` and the ${MAX_RASPBERRY_SHAKE_STATIONS}-station cap was reached` : ""}. FDSN station metadata and archived miniSEED are not a realtime waveform stream; the provider documents a separate realtime service, a delay boundary, rate limits, raw-count response handling, and no fdsnws-event service. This layer is station context only, not an earthquake alert, measurement, warning, or KFM evidence.`,
    retrievedAt,
    null,
    skipped > 0 || truncated,
    truncated,
  );
};

const cacheSeconds: Record<Feed, number> = { "census-counties": 86_400, "usgs-streamflow": 120, "usgs-earthquakes": 300, "nws-alerts": 30, "noaa-hms-smoke": 900, "raspberry-shake-stations": 900 };

export async function GET(request: NextRequest) {
  const feed = request.nextUrl.searchParams.get("feed");
  const day = request.nextUrl.searchParams.get("day");
  if (request.nextUrl.searchParams.has("day") && (!day || !eventDay(day) || day < "1800-01-01" || day > new Date().toISOString().slice(0, 10) || !["usgs-earthquakes", "noaa-hms-smoke", "raspberry-shake-stations"].includes(feed ?? "")) || [...request.nextUrl.searchParams.keys()].some((key) => !["feed", "day"].includes(key) || request.nextUrl.searchParams.getAll(key).length !== 1)) return NextResponse.json({ error: "Choose an exact supported calendar date and source." }, { status: 400 });
  if (feed !== "census-counties" && feed !== "usgs-streamflow" && feed !== "usgs-earthquakes" && feed !== "nws-alerts" && feed !== "noaa-hms-smoke" && feed !== "raspberry-shake-stations") {
    return NextResponse.json({ error: "Unknown live-context feed. The adapter accepts only its fixed allowlist." }, { status: 400, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
  try {
    const result = feed === "census-counties" ? await censusCounties() : feed === "usgs-streamflow" ? await latestStreamflow() : feed === "usgs-earthquakes" ? await recentEarthquakes(day) : feed === "nws-alerts" ? await activeNwsAlerts() : feed === "noaa-hms-smoke" ? await currentHmsSmoke(day) : await raspberryShakeStations(day);
    return NextResponse.json(result, { headers: { "Cache-Control": `public, max-age=0, s-maxage=${cacheSeconds[feed]}, stale-while-revalidate=${cacheSeconds[feed]}`, "X-KFM-Context-State": result.state, "X-Content-Type-Options": "nosniff" } });
  } catch (error) {
    const timeout = error instanceof UpstreamError && error.timeout;
    return NextResponse.json({ error: error instanceof Error ? error.message : "Official upstream request failed.", state: "error", fallback: "No fallback inference or substitute dataset was produced." }, { status: timeout ? 504 : 502, headers: { "Cache-Control": "no-store", "X-KFM-Context-State": "error", "X-Content-Type-Options": "nosniff" } });
  }
}
