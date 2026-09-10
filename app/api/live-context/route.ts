import { NextRequest, NextResponse } from "next/server";
import type { Feature, FeatureCollection, Geometry, GeoJsonProperties } from "geojson";

export const dynamic = "force-dynamic";

const CENSUS_URL = "https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/MapServer/1/query?where=STATE%3D%2720%27&outFields=GEOID%2CNAME%2CBASENAME%2CSTATE%2CCOUNTY&returnGeometry=true&outSR=4326&geometryPrecision=5&maxAllowableOffset=0.001&f=geojson";
const CENSUS_ACS_URL = "https://api.census.gov/data/2024/acs/acs5/profile?get=NAME%2CDP05_0001E&for=county%3A%2A&in=state%3A20";
const USGS_URL = "https://api.waterdata.usgs.gov/ogcapi/v0/collections/latest-continuous/items";
const USGS_EARTHQUAKE_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query";
const NWS_ALERTS_URL = "https://api.weather.gov/alerts/active?area=KS";
const NWS_USER_AGENT = "KansasFrontierMatrixExplorer/1.0 (https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site)";
const MAX_RESPONSE_BYTES = 8 * 1024 * 1024;
const MAX_NWS_ZONE_REQUESTS = 36;
const MAX_NWS_FEATURES = 160;
const MAX_EARTHQUAKE_FEATURES = 250;

type Feed = "census-counties" | "usgs-streamflow" | "usgs-earthquakes" | "nws-alerts";
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
    const response = await fetch(url, { ...init, cache: "no-store", signal: controller.signal });
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
  const retrievedAt = new Date().toISOString();
  const payload = await fetchBoundedJson(CENSUS_URL, 25_000);
  let populationByGeoid = new Map<string, number>();
  let populationUnavailable = false;
  try {
    const rows = await fetchBoundedJsonArray(CENSUS_ACS_URL, 15_000);
    const header = Array.isArray(rows[0]) ? rows[0].map((value) => String(value)) : [];
    const populationIndex = header.indexOf("DP05_0001E");
    const stateIndex = header.indexOf("state");
    const countyIndex = header.indexOf("county");
    if (populationIndex < 0 || stateIndex < 0 || countyIndex < 0) throw new UpstreamError("Census ACS response omitted required population join fields.");
    populationByGeoid = new Map(rows.slice(1).flatMap((candidate) => {
      if (!Array.isArray(candidate)) return [];
      const state = asString(candidate[stateIndex]);
      const county = asString(candidate[countyIndex]);
      const population = asNumeric(candidate[populationIndex]);
      return state && county && population !== null && population >= 0 ? [[`${state}${county}`, Math.round(population)] as const] : [];
    }));
  } catch {
    populationUnavailable = true;
  }
  const features: Feature<Geometry, GeoJsonProperties>[] = collectionFeatures(payload).flatMap((candidate) => {
    if (!isRecord(candidate.geometry) || candidate.geometry.type !== "Polygon" && candidate.geometry.type !== "MultiPolygon") return [];
    const properties = isRecord(candidate.properties) ? candidate.properties : {};
    const geoid = asString(properties.GEOID);
    const name = asString(properties.BASENAME) ?? asString(properties.NAME);
    if (!geoid || !name) return [];
    const populationEstimate = populationByGeoid.get(geoid) ?? null;
    return [{
      type: "Feature" as const,
      id: geoid,
      geometry: candidate.geometry as unknown as Geometry,
      properties: {
        featureId: `us-census-county-${geoid}`,
        name,
        geoid,
        stateFips: asString(properties.STATE) ?? geoid.slice(0, 2),
        countyFips: asString(properties.COUNTY) ?? geoid.slice(2),
        populationEstimate,
        populationEstimateYear: populationEstimate === null ? null : 2024,
        populationEstimateProduct: populationEstimate === null ? null : "ACS 5-year DP05_0001E",
        sourceOrganization: "U.S. Census Bureau",
        evidenceRole: "EXTERNAL_CONTEXT_ONLY",
        vintage: "2026",
        retrievedAt,
      },
    }];
  });
  return envelope(
    "census-counties",
    { type: "FeatureCollection", features },
    CENSUS_URL,
    `Kansas-only Census TIGERweb State_County geometry, generalized by the adapter to approximately 0.001 degrees. ${populationUnavailable ? "The ACS population request was unavailable; no population values were inferred. " : `${populationByGeoid.size} county GEOIDs were joined to the 2024 ACS 5-year DP05_0001E population estimate. `}Boundary vintage and population estimate year remain distinct. Current context is not historical boundary authority, a current population count, or KFM evidence.`,
    retrievedAt,
    null,
    populationUnavailable || populationByGeoid.size < features.length,
  );
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

const recentEarthquakes = async () => {
  const retrievedAt = new Date().toISOString();
  const start = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString();
  const url = new URL(USGS_EARTHQUAKE_URL);
  url.searchParams.set("format", "geojson");
  url.searchParams.set("eventtype", "earthquake");
  url.searchParams.set("starttime", start);
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
    `${features.length} USGS catalog event${features.length === 1 ? "" : "s"} returned for the Kansas bounding window over the past 30 days. Locations, depths, magnitudes, and review status may change. This is not an earthquake alert, hazard forecast, or KFM evidence.`,
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

const cacheSeconds: Record<Feed, number> = { "census-counties": 86_400, "usgs-streamflow": 120, "usgs-earthquakes": 300, "nws-alerts": 30 };

export async function GET(request: NextRequest) {
  const feed = request.nextUrl.searchParams.get("feed");
  if (feed !== "census-counties" && feed !== "usgs-streamflow" && feed !== "usgs-earthquakes" && feed !== "nws-alerts") {
    return NextResponse.json({ error: "Unknown live-context feed. The adapter accepts only its fixed allowlist." }, { status: 400, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
  try {
    const result = feed === "census-counties" ? await censusCounties() : feed === "usgs-streamflow" ? await latestStreamflow() : feed === "usgs-earthquakes" ? await recentEarthquakes() : await activeNwsAlerts();
    return NextResponse.json(result, { headers: { "Cache-Control": `public, max-age=0, s-maxage=${cacheSeconds[feed]}, stale-while-revalidate=${cacheSeconds[feed]}`, "X-KFM-Context-State": result.state, "X-Content-Type-Options": "nosniff" } });
  } catch (error) {
    const timeout = error instanceof UpstreamError && error.timeout;
    return NextResponse.json({ error: error instanceof Error ? error.message : "Official upstream request failed.", state: "error", fallback: "No fallback inference or substitute dataset was produced." }, { status: timeout ? 504 : 502, headers: { "Cache-Control": "no-store", "X-KFM-Context-State": "error", "X-Content-Type-Options": "nosniff" } });
  }
}
