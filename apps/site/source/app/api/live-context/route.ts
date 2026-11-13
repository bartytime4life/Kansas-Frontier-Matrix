import { env } from "cloudflare:workers";
import { readBoundedJson } from "../../bounded-json";
import { NextRequest, NextResponse } from "next/server";
import type { Feature, FeatureCollection, Geometry, GeoJsonProperties } from "geojson";
import { EVENT_BOUNDS, eventDay, advanceEventDay, intervalDays, parseSmokeKml, smokeOverlaps, smokeUrl } from "../../event-atlas";
import { boundedFetch } from "../event-atlas/upstream";
import { countyBaseline } from "../../county-baseline";
import { FEMA_DECLARATION_LIMIT, parseFemaDeclarations } from "../../fema-declarations";
import { VectorTile } from "@mapbox/vector-tile";
import Pbf from "pbf";

export const dynamic = "force-dynamic";

const USGS_URL = "https://api.waterdata.usgs.gov/ogcapi/v1/collections/latest-continuous/items";
const USGS_EARTHQUAKE_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query";
const NWS_ALERTS_URL = "https://api.weather.gov/alerts/active?area=KS";
const RASPBERRY_SHAKE_STATION_URL = "https://data.raspberryshake.org/fdsnws/station/1/query";
const NIFC_INCIDENT_URL = "https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/WFIGS_Incident_Locations_YearToDate/FeatureServer/0/query";
const FEMA_DECLARATIONS_URL = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries";
const NPS_NRHP_POINTS_URL = "https://mapservices.nps.gov/arcgis/rest/services/cultural_resources/nrhp_locations/MapServer/0/query";
const NWS_STORM_REPORTS_URL = "https://mapservices.weather.noaa.gov/vector/rest/services/obs/nws_local_storm_reports/MapServer/2/query";
const MAX_NRHP_PLACES = 2000;
const MAX_STORM_REPORTS = 500;
const KDWP_SERVICES = "https://services1.arcgis.com/q2CglofYX6ACNEeu/arcgis/rest/services";
const KDWP_WILDLIFE_AREAS_URL = `${KDWP_SERVICES}/KDWPT_Wildlife_Areas_view/FeatureServer/0/query`;
const KDWP_WIHA_URL = `${KDWP_SERVICES}/24_25_7_29/FeatureServer/0/query`;
const MAX_KDWP_AREAS = 6000;
const KDWP_PAGE_SIZE = 2000;
const NWS_USER_AGENT = "KansasFrontierMatrixExplorer/1.0 (https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site)";
const MAX_RESPONSE_BYTES = 8 * 1024 * 1024;
const MAX_STREAMFLOW_RECORDS = 1000;
const MAX_NWS_ZONE_REQUESTS = 36;
const MAX_NWS_FEATURES = 160;
const MAX_EARTHQUAKE_FEATURES = 250;
const MAX_RASPBERRY_SHAKE_STATIONS = 250;
const MAX_NIFC_INCIDENTS = 250;
const GIBS_FIRE_LAYER = "VIIRS_NOAA20_Thermal_Anomalies_375m_All";
const GIBS_FIRE_SOURCE_LAYER = `${GIBS_FIRE_LAYER}_v2_NRT`;
const GIBS_FIRE_TILE_COLUMNS = [8, 9] as const; // EPSG:4326 500m matrix 5; Kansas lies in row 5.
const GIBS_FIRE_TILE_ROW = 5;
const MAX_GIBS_FIRE_TILE_BYTES = 1024 * 1024;
const MAX_GIBS_FIRE_FEATURES = 5000;

type Feed = "census-counties" | "usgs-streamflow" | "usgs-earthquakes" | "nws-alerts" | "noaa-hms-smoke" | "nasa-gibs-fire-points" | "nifc-fire-reports" | "raspberry-shake-stations" | "fema-disaster-declarations" | "nps-nrhp-places" | "nws-storm-reports" | "kdwp-wildlife-areas" | "kdwp-wiha-access";
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
    return await readBoundedJson(response, MAX_RESPONSE_BYTES);
  } catch (error) {
    if (error instanceof UpstreamError) throw error;
    if (error instanceof Error && error.name === "AbortError") throw new UpstreamError("Official upstream request timed out.", true);
    // Native fetch failures can include the full provider URL and query string.
    throw new UpstreamError("Official upstream request failed.");
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

const collectionFeatures = (payload: JsonRecord): JsonRecord[] => {
  if (!Array.isArray(payload.features) || !payload.features.every(isRecord)) throw new UpstreamError("Official upstream response had an invalid feature collection.");
  return payload.features;
};

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

const recentFemaDeclarations = async () => {
  const retrievedAt = new Date().toISOString();
  const url = new URL(FEMA_DECLARATIONS_URL);
  url.searchParams.set("$filter", "state eq 'KS'");
  url.searchParams.set("$orderby", "declarationDate desc");
  url.searchParams.set("$top", String(FEMA_DECLARATION_LIMIT + 1));
  const [payload, counties] = await Promise.all([fetchBoundedJson(url.toString(), 12_000), countyBaseline("2020")]);
  const result = parseFemaDeclarations(payload, counties.data, retrievedAt);
  return envelope("fema-disaster-declarations", result.data,
    "FEMA OpenFEMA DisasterDeclarationsSummaries v2 · U.S. Census Bureau 2020 county geography",
    `Latest ${FEMA_DECLARATION_LIMIT} Kansas declaration designations at most; ${result.skipped} unmatched or invalid rows withheld${result.truncated ? "; older records exist beyond this bounded view" : ""}. The 2020 county outlines locate designated areas, not observed impact footprints or current danger. A missing declaration is not an all-clear.`,
    retrievedAt, result.upstreamUpdatedAt, result.partial, result.truncated);
};

const latestStreamflow = async () => {
  const endMs = Date.now();
  const retrievedAt = new Date(endMs).toISOString();
  const startMs = endMs - 24 * 60 * 60 * 1000;
  const start = new Date(startMs).toISOString();
  // Require a complete RFC3339 clock, validate its calendar before applying
  // the explicit offset, then compare observations as instants rather than text.
  const observationTime = (value: unknown): string | null => {
    if (typeof value !== "string") return null;
    const match = /^(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2})(?:\.(\d{1,9}))?(Z|([+-])(\d{2}):(\d{2}))$/i.exec(value);
    if (!match) return null;
    const local = `${match[1]}T${match[2]}.${(match[3] ?? "").padEnd(3, "0").slice(0, 3)}Z`;
    const localMs = Date.parse(local);
    if (!Number.isFinite(localMs) || new Date(localMs).toISOString() !== local) return null;
    const hours = Number(match[6] ?? 0), minutes = Number(match[7] ?? 0);
    if (hours > 23 || minutes > 59) return null;
    const offsetMs = (match[5] === "-" ? -1 : 1) * (hours * 60 + minutes) * 60_000;
    const utc = new Date(localMs - offsetMs).toISOString();
    // Offsets are whole minutes, so the finer-than-millisecond remainder is
    // unchanged. Retain it instead of letting Date discard source precision.
    return (match[3]?.length ?? 0) > 3 ? utc.replace(/Z$/, `${match[3].slice(3)}Z`) : utc;
  };
  const instantKey = (time: string): string => time.replace(/\.(\d+)Z$/, (_match, fraction: string) => `.${fraction.padEnd(9, "0")}Z`);
  const startKey = instantKey(start), endKey = instantKey(retrievedAt);
  const url = new URL(USGS_URL);
  url.searchParams.set("f", "json");
  url.searchParams.set("limit", String(MAX_STREAMFLOW_RECORDS));
  url.searchParams.set("state_code", "20");
  url.searchParams.set("agency_code", "USGS");
  url.searchParams.set("site_type_code", "ST");
  url.searchParams.set("parameter_code", "00060");
  url.searchParams.set("datetime", `${start}/${retrievedAt}`);
  const payload = await fetchBoundedJson(url.toString(), 15_000, { headers: { ...((env as { USGS_WATER_API_KEY?: string }).USGS_WATER_API_KEY ? { "X-Api-Key": String(env.USGS_WATER_API_KEY) } : {}) } });
  if (!Array.isArray(payload.features)) throw new UpstreamError("USGS latest response had no feature array.");
  const capped = payload.features.length > MAX_STREAMFLOW_RECORDS;
  const candidates = payload.features.slice(0, MAX_STREAMFLOW_RECORDS);
  const newest = new Map<string, Feature<Geometry, GeoJsonProperties>>();
  let newestTimestamp: string | null = null;
  let newestKey: string | null = null;
  let skipped = 0;

  for (const candidate of candidates) {
    if (!isRecord(candidate) || !isRecord(candidate.geometry) || candidate.geometry.type !== "Point") { skipped += 1; continue; }
    const properties = isRecord(candidate.properties) ? candidate.properties : {};
    const monitoringLocationId = asString(properties.monitoring_location_id);
    const observedAt = observationTime(properties.time);
    const observedKey = observedAt === null ? "" : instantKey(observedAt);
    if (!monitoringLocationId || observedAt === null || observedKey < startKey || observedKey > endKey) { skipped += 1; continue; }
    const value = asNumber(properties.value);
    const unit = asString(properties.unit_of_measure) ?? "unknown unit";
    const current = newest.get(monitoringLocationId);
    if (current && instantKey(String(current.properties?.observedAt)) >= observedKey) continue;
    const feature: Feature<Geometry, GeoJsonProperties> = {
      type: "Feature",
      id: monitoringLocationId,
      geometry: candidate.geometry as unknown as Geometry,
      properties: {
        featureId: `usgs-streamflow-${monitoringLocationId}`,
        name: monitoringLocationId,
        monitoringLocationId,
        observedAt,
        sourceObservedAt: asString(properties.time),
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
    if (newestKey === null || observedKey > newestKey) { newestKey = observedKey; newestTimestamp = observedAt; }
  }

  const links = Array.isArray(payload.links) ? payload.links.filter(isRecord) : [];
  const nextPage = links.some((link) => asString(link.rel) === "next");
  const truncated = capped || nextPage;
  const features = [...newest.values()];
  return envelope(
    "usgs-streamflow",
    { type: "FeatureCollection", features },
    url.toString(),
    `${nextPage ? "The OGC API advertised another page; this bounded view is partial. " : ""}${capped ? `The provider returned more than ${MAX_STREAMFLOW_RECORDS} records; only the first ${MAX_STREAMFLOW_RECORDS} were considered, so this view is partial. ` : ""}Latest Kansas USGS streamflow values within the rolling 24-hour request window ${start} through ${retrievedAt} (inclusive). ${skipped} invalid or outside-window returned observation${skipped === 1 ? "" : "s"} withheld. Provisional, delayed, revised, or incomplete values remain possible. Not flood guidance or KFM evidence.`,
    retrievedAt,
    newestTimestamp,
    skipped > 0 || truncated,
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
  // One lookahead record distinguishes an exact 250-event response from a
  // capped response without claiming the provider's count is a total inventory.
  url.searchParams.set("limit", String(MAX_EARTHQUAKE_FEATURES + 1));
  const payload = await fetchBoundedJson(url.toString(), 15_000);
  let newestTimestamp: string | null = null;
  const catalogFeatures = collectionFeatures(payload);
  const candidates = catalogFeatures.slice(0, MAX_EARTHQUAKE_FEATURES);
  const sourceTimestamp = (value: unknown): string | null => {
    const milliseconds = asNumeric(value);
    if (milliseconds === null) return null;
    const date = new Date(milliseconds);
    return Number.isFinite(date.getTime()) ? date.toISOString() : null;
  };
  const features: Feature<Geometry, GeoJsonProperties>[] = candidates.flatMap((candidate) => {
    if (!isRecord(candidate.geometry) || candidate.geometry.type !== "Point" || !Array.isArray(candidate.geometry.coordinates)) return [];
    const coordinates = candidate.geometry.coordinates;
    const longitude = asNumeric(coordinates[0]);
    const latitude = asNumeric(coordinates[1]);
    const depthKilometers = asNumeric(coordinates[2]);
    if (longitude === null || latitude === null || longitude < -102.1 || longitude > -94.5 || latitude < 36.9 || latitude > 40.1) return [];
    const properties = isRecord(candidate.properties) ? candidate.properties : {};
    const eventId = asString(candidate.id) ?? asString(properties.code);
    const observedAt = sourceTimestamp(properties.time);
    if (!eventId || observedAt === null) return [];
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
        updatedAt: sourceTimestamp(properties.updated),
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
  const skipped = candidates.length - features.length;
  const truncated = catalogFeatures.length > MAX_EARTHQUAKE_FEATURES || (totalCount !== null && totalCount > catalogFeatures.length);
  return envelope(
    "usgs-earthquakes",
    { type: "FeatureCollection", features },
    url.toString(),
    `${features.length} USGS catalog event${features.length === 1 ? "" : "s"} returned for the Kansas bounding window for ${start} through ${end} (end excluded). ${skipped} invalid or outside-window returned record${skipped === 1 ? "" : "s"} withheld.${truncated ? ` This bounded view considers at most ${MAX_EARTHQUAKE_FEATURES} returned records; additional catalog records were omitted, so the view is partial.` : ""} Locations, depths, magnitudes, and review status may change. This is not an earthquake alert, hazard forecast, or KFM evidence.`,
    retrievedAt,
    newestTimestamp,
    skipped > 0 || truncated,
    truncated,
  );
};

const allowedZoneUrl = (value: unknown): string | null => {
  if (typeof value !== "string") return null;
  try {
    const url = new URL(value);
    if (url.origin !== "https://api.weather.gov" || url.username || url.password || url.search || url.hash) return null;
    return /^\/zones\/(forecast|county|fire)\/(KSZ|KSC)\d{3}$/.test(url.pathname) ? url.toString() : null;
  } catch {
    return null;
  }
};

/** Keep unusable source polygons out of the map and out of complete-coverage claims. */
const alertGeometry = (value: unknown): Geometry | null => {
  if (!isRecord(value) || !Array.isArray(value.coordinates)) return null;
  const position = (point: unknown): point is number[] => Array.isArray(point) && point.length >= 2 && point.length <= 3
    && point.every(coordinate => typeof coordinate === "number" && Number.isFinite(coordinate))
    && Math.abs(point[0]) <= 180 && Math.abs(point[1]) <= 90;
  const ring = (value: unknown): boolean => Array.isArray(value) && value.length >= 4 && value.every(position)
    && value[0].length === value[value.length - 1].length && value[0].every((coordinate: number, index: number) => coordinate === value[value.length - 1][index]);
  const polygon = (value: unknown): boolean => Array.isArray(value) && value.length > 0 && value.every(ring);
  if (value.type === "Polygon" && polygon(value.coordinates)
      || value.type === "MultiPolygon" && value.coordinates.length > 0 && value.coordinates.every(polygon)) return value as unknown as Geometry;
  return null;
};

const activeNwsAlerts = async () => {
  const retrievedAt = new Date().toISOString();
  const headers = { Accept: "application/geo+json, application/json", "User-Agent": NWS_USER_AGENT };
  const payload = await fetchBoundedJson(NWS_ALERTS_URL, 15_000, { headers });
  const alerts = collectionFeatures(payload);
  // Only inspect pagination metadata. The bounded adapter never follows a
  // provider-supplied continuation URL or spends another page's request budget.
  let nextPage = false, paginationUnverified = false;
  if (payload.pagination !== undefined) {
    if (!isRecord(payload.pagination)) paginationUnverified = true;
    else if (payload.pagination.next !== undefined && payload.pagination.next !== null) {
      try {
        if (typeof payload.pagination.next !== "string") throw new Error();
        const next = new URL(payload.pagination.next);
        if (next.origin !== "https://api.weather.gov" || next.username || next.password || next.hash || !/^\/alerts(?:\/active)?$/.test(next.pathname)) throw new Error();
        nextPage = true;
      } catch { paginationUnverified = true; }
    }
  }
  const zoneUrls = [...new Set(alerts.flatMap((alert) => {
    const properties = isRecord(alert.properties) ? alert.properties : {};
    return Array.isArray(properties.affectedZones) ? properties.affectedZones.map(allowedZoneUrl).filter((value): value is string => Boolean(value)) : [];
  }))];
  const selectedZoneUrls = zoneUrls.slice(0, MAX_NWS_ZONE_REQUESTS);
  const zoneResults = await Promise.allSettled(selectedZoneUrls.map(async (url) => ({ url, payload: await fetchBoundedJson(url, 18_000, { headers }) })));
  const zones = new Map<string, JsonRecord>();
  let failedZoneCount = 0;
  for (const result of zoneResults) {
    if (result.status === "rejected" || !alertGeometry(result.value.payload.geometry)) {
      failedZoneCount += 1;
      continue;
    }
    zones.set(result.value.url, result.value.payload);
  }

  const features: Feature<Geometry, GeoJsonProperties>[] = [];
  let newestTimestamp: string | null = null;
  let unmappedAlerts = 0, invalidAlertPolygons = 0;
  for (const [alertIndex, alert] of alerts.entries()) {
    const before = features.length;
    const properties = isRecord(alert.properties) ? alert.properties : {};
    const alertId = asString(properties.id) ?? asString(alert.id) ?? `alert-${alertIndex}`;
    const safe = {
      event: asString(properties.event), severity: asString(properties.severity), urgency: asString(properties.urgency), certainty: asString(properties.certainty),
      headline: asString(properties.headline), areaDesc: asString(properties.areaDesc), effective: asString(properties.effective), expires: asString(properties.expires), senderName: asString(properties.senderName),
    };
    if (safe.effective && (!newestTimestamp || safe.effective > newestTimestamp)) newestTimestamp = safe.effective;
    const ownGeometry = alertGeometry(alert.geometry);
    if (ownGeometry) {
      features.push({ type: "Feature", id: `${alertId}-geometry`, geometry: ownGeometry, properties: { featureId: `nws-alert-${alertId}-geometry`, ...safe, zoneName: null, zoneExpirationDate: null, sourceOrganization: "NOAA National Weather Service", evidenceRole: "EXTERNAL_CONTEXT_ONLY", retrievedAt } });
    } else if (alert.geometry !== undefined && alert.geometry !== null) {
      invalidAlertPolygons += 1;
    }
    const affected = Array.isArray(properties.affectedZones) ? properties.affectedZones.map(allowedZoneUrl).filter((value): value is string => Boolean(value)) : [];
    for (const zoneUrl of affected) {
      const zone = zones.get(zoneUrl);
      const geometry = zone ? alertGeometry(zone.geometry) : null;
      if (!geometry) continue;
      const zoneProperties = isRecord(zone?.properties) ? zone.properties : {};
      const zoneCode = new URL(zoneUrl).pathname.split("/").at(-1) ?? "zone";
      features.push({ type: "Feature", id: `${alertId}-${zoneCode}`, geometry, properties: { featureId: `nws-alert-${alertId}-${zoneCode}`, ...safe, zoneName: asString(zoneProperties.name), zoneExpirationDate: asString(zoneProperties.expirationDate), sourceOrganization: "NOAA National Weather Service", evidenceRole: "EXTERNAL_CONTEXT_ONLY", retrievedAt } });
    }
    if (features.length === before) unmappedAlerts += 1;
  }

  const capped = features.length > MAX_NWS_FEATURES;
  const data = { type: "FeatureCollection" as const, features: features.slice(0, MAX_NWS_FEATURES) };
  const truncated = zoneUrls.length > MAX_NWS_ZONE_REQUESTS || capped || nextPage || paginationUnverified;
  const partial = failedZoneCount > 0 || unmappedAlerts > 0 || invalidAlertPolygons > 0 || truncated;
  return envelope(
    "nws-alerts",
    data,
    NWS_ALERTS_URL,
    `${alerts.length} active Kansas alert record${alerts.length === 1 ? "" : "s"} returned at retrieval; ${failedZoneCount} selected zone lookup${failedZoneCount === 1 ? "" : "s"} failed or returned unusable geometry; ${unmappedAlerts} returned alert${unmappedAlerts === 1 ? "" : "s"} could not be mapped; ${invalidAlertPolygons} supplied alert polygon${invalidAlertPolygons === 1 ? "" : "s"} withheld as unusable.${nextPage ? " Another alert page was advertised; only this first page was checked." : ""}${paginationUnverified ? " Pagination metadata could not be verified; additional alerts may be missing." : ""}${zoneUrls.length > MAX_NWS_ZONE_REQUESTS ? ` Zone lookups were bounded to ${MAX_NWS_ZONE_REQUESTS}.` : ""}${capped ? ` Mapped features were capped at ${MAX_NWS_FEATURES}.` : ""} Zero mapped features is never an all-clear. This bounded display is not a warning-delivery service or KFM evidence.`,
    retrievedAt,
    newestTimestamp,
    partial,
    truncated,
  );
};

const currentHmsSmoke = async (day: string | null = null, signal?: AbortSignal) => {
  const retrievedAt = new Date().toISOString();
  const endMs = day ? Date.parse(`${advanceEventDay(day, 1)}T00:00:00Z`) : Date.now();
  const startMs = endMs - 24 * 60 * 60 * 1000;
  const start = new Date(startMs).toISOString();
  const end = new Date(endMs).toISOString();
  // A polygon valid after midnight can originate in the prior day's KML.
  // Keep the rolling-current window unchanged; dated requests check both publications.
  const priorDay = day ? advanceEventDay(day, -1) : null;
  const priorOutsideConnectedArchive = Boolean(priorDay && priorDay < "2005-08-05");
  const days = day ? [...(priorDay && !priorOutsideConnectedArchive ? [priorDay] : []), day] : intervalDays(start, end);
  const results = await Promise.all(days.map(async (day) => {
    const artifact = smokeUrl(day);
    try {
      const response = await boundedFetch(artifact, 2 * 1024 * 1024, { signal });
      return { day, artifact, collection: parseSmokeKml(response.text(), artifact), error: null };
    } catch {
      return { day, artifact, collection: null, error: "NOAA HMS publication unavailable." };
    }
  }));
  const failures = results.filter((result) => result.error).map((result) => `${result.day}: ${result.error}`);
  if (failures.length === results.length) throw new UpstreamError(`NOAA HMS smoke publications were unavailable for the bounded window (${failures.join("; ")}).`);
  const seen = new Set<string>();
  const features: Feature<Geometry, GeoJsonProperties>[] = [];
  let newestTimestamp: string | null = null;
  for (const result of results) {
    for (const feature of result.collection?.features ?? []) {
      if (!smokeOverlaps(feature.properties, startMs, endMs)) continue;
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
  return { ...envelope(
    "noaa-hms-smoke",
    data,
    "NOAA HMS Smoke Polygons KML (daily publications)",
    `NOAA HMS satellite-analyzed smoke polygons intersecting Kansas during the ${day ? "selected UTC day" : "rolling 24-hour window"} ${start} through ${end}. ${failures.length ? `Unavailable daily publication${failures.length === 1 ? "" : "s"}: ${failures.join("; ")}. ` : ""}${priorOutsideConnectedArchive ? "A prior-day publication falls before the connected archive start, so midnight overlap cannot be fully checked. " : ""}Density and Start/End are provider fields. Equal Start/End denotes timestamp-only support, with no duration inferred. A polygon is not a fire perimeter, plume altitude, surface PM2.5, exposure, measured transport, health guidance, warning, or all-clear; missing polygons do not prove clear air.`,
    retrievedAt,
    newestTimestamp,
    failures.length > 0 || priorOutsideConnectedArchive,
  ), smokeCoverage: { day, availableDays: results.filter(result => !result.error).map(result => result.day), missingDays: results.filter(result => result.error).map(result => result.day), firstDay: "2005-08-05" } };
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

/** Two official geographic WMTS tiles cover the Kansas window at matrix 5.
 * MVT coordinates are geographic, so use NASA's explicit LATITUDE/LONGITUDE
 * properties rather than a Web Mercator toGeoJSON projection. */
const nasaGibsFirePointsForDay = async (day: string, unavailableCurrentDay: string | null = null) => {
  const safeDay = encodeURIComponent(day);
  const retrievedAt = new Date().toISOString();
  const tiles = await Promise.all(GIBS_FIRE_TILE_COLUMNS.map(async (column) => {
    const url = `https://gibs.earthdata.nasa.gov/wmts/epsg4326/best/${GIBS_FIRE_LAYER}/default/${safeDay}/500m/5/${GIBS_FIRE_TILE_ROW}/${column}.mvt`;
    try {
      const response = await boundedFetch(url, MAX_GIBS_FIRE_TILE_BYTES, { timeoutMs: 8000, cache: "no-store" });
      if (response.bytes.length === 0) throw new UpstreamError("NASA GIBS tile body was missing.");
      const tile = new VectorTile(new Pbf(response.bytes));
      const layer = tile.layers[GIBS_FIRE_SOURCE_LAYER];
      if (!layer && Object.keys(tile.layers).length > 0) throw new UpstreamError("NASA GIBS returned an unexpected fire tile layer.");
      return { column, layer };
    } catch (error) {
      if (error instanceof UpstreamError) throw error;
      if (error instanceof Error && error.message === "Source response body was missing.") throw new UpstreamError("NASA GIBS tile body was missing.");
      if (error instanceof Error && error.message === "Source exceeded the response budget.") throw new UpstreamError("NASA GIBS tile exceeded the response limit.");
      const status = error instanceof Error ? /^Source unavailable \(HTTP (\d{3})\)\.$/.exec(error.message)?.[1] : null;
      if (status) throw new UpstreamError(`NASA GIBS tile ${column} returned HTTP ${status}.`);
      throw new UpstreamError(`NASA GIBS tile ${column} was unavailable or malformed.`, error instanceof Error && error.name === "AbortError");
    }
  }));
  const features: Feature<Geometry, GeoJsonProperties>[] = [];
  const seen = new Set<string>();
  let skipped = 0;
  let newestTimestamp: string | null = null;
  for (const { column, layer } of tiles) {
    if (!layer) continue;
    for (let index = 0; index < layer.length; index += 1) {
      const row = layer.feature(index).properties;
      const latitude = asNumber(row.LATITUDE);
      const longitude = asNumber(row.LONGITUDE);
      if (latitude === null || longitude === null || latitude < EVENT_BOUNDS[1] || latitude > EVENT_BOUNDS[3] || longitude < EVENT_BOUNDS[0] || longitude > EVENT_BOUNDS[2]) continue;
      const acquiredDate = asString(row.ACQ_DATE);
      const acquiredTime = asString(row.ACQ_TIME);
      const acquiredAt = acquiredDate === day && acquiredTime && /^\d{2}:\d{2}$/.test(acquiredTime)
        ? `${acquiredDate}T${acquiredTime}:00Z` : null;
      if (!acquiredAt || !Number.isFinite(Date.parse(acquiredAt))) { skipped += 1; continue; }
      const satellite = asString(row.SATELLITE);
      if (satellite !== "N20") { skipped += 1; continue; }
      const uid = asNumber(row.UID);
      const featureId = `nasa-gibs-${day}-${uid ?? `${column}-${index}`}`;
      if (seen.has(featureId)) continue;
      seen.add(featureId);
      if (features.length >= MAX_GIBS_FIRE_FEATURES) { skipped += 1; continue; }
      const frpMw = asNumber(row.FRP);
      const confidence = asString(row.CONFIDENCE)?.toLowerCase() ?? null;
      const dayNight = row.DAYNIGHT === "D" ? "Day" : row.DAYNIGHT === "N" ? "Night" : null;
      const typeCode = asString(row.TYPE) ?? (asNumber(row.TYPE) === null ? null : String(row.TYPE));
      const hotSpotType = typeCode === "0" ? "Presumed vegetation fire" : typeCode === "1" ? "Active volcano" : typeCode === "2" ? "Other static land source" : typeCode === "3" ? "Offshore detection" : null;
      features.push({
        type: "Feature", id: featureId,
        geometry: { type: "Point", coordinates: [longitude, latitude] },
        properties: {
          featureId,
          name: `Thermal detection${frpMw === null ? "" : ` · ${frpMw.toFixed(1)} MW`}`,
          acquiredAt, sourceDay: day, latitude, longitude,
          satellite: "NOAA-20", instrument: "VIIRS 375 m", confidence,
          frpMw, brightnessI4Kelvin: asNumber(row.BRIGHT_TI4), brightnessI5Kelvin: asNumber(row.BRIGHT_TI5),
          scanKm: asNumber(row.SCAN), trackKm: asNumber(row.TRACK), dayNight,
          hotSpotType: hotSpotType ?? "Not supplied", typeCode, providerUid: uid,
          processingVersion: asString(row.VERSION), retrievedAt,
          evidenceRole: "EXTERNAL_CONTEXT_ONLY",
        },
      });
      if (!newestTimestamp || acquiredAt > newestTimestamp) newestTimestamp = acquiredAt;
    }
  }
  return { ...envelope(
    "nasa-gibs-fire-points",
    { type: "FeatureCollection", features },
    `NASA GIBS WMTS ${GIBS_FIRE_LAYER}, EPSG:4326 500m matrix 5, UTC ${day}`,
    `NOAA-20 VIIRS thermal detections within the bounded Kansas window for ${day} UTC. ${unavailableCurrentDay ? `The current UTC day ${unavailableCurrentDay} returned a missing tile when checked; this is the previous day's snapshot, not current-day coverage. ` : ""}${skipped ? `${skipped} malformed, mismatched, or over-cap records were withheld; this response is partial. ` : ""}Each point is a satellite thermal-anomaly pixel, not a confirmed wildfire, incident, ignition point, perimeter, burn area, or safety guidance. Missing detections do not establish no fire or full coverage.`,
    retrievedAt,
    newestTimestamp,
    skipped > 0 || unavailableCurrentDay !== null,
    features.length >= MAX_GIBS_FIRE_FEATURES,
  ), sourceDay: day };
};

const nasaGibsFirePoints = async (requestedDay: string | null = null) => {
  const dayPattern = /^\d{4}-\d{2}-\d{2}$/;
  if (requestedDay !== null && !dayPattern.test(requestedDay)) throw new UpstreamError("NASA GIBS day must be an exact calendar date.");
  const day = requestedDay ?? new Date().toISOString().slice(0, 10);
  if (!dayPattern.test(day)) throw new UpstreamError("NASA GIBS day must be an exact calendar date.");
  try {
    return await nasaGibsFirePointsForDay(day);
  } catch (error) {
    // New UTC days can precede the provider's first published tile. Only the
    // implicit current-day view may use one dated previous-day snapshot.
    if (requestedDay !== null || !(error instanceof UpstreamError) || !/^NASA GIBS tile (8|9) returned HTTP 404\.$/.test(error.message)) throw error;
    const previousDay = new Date(Date.parse(`${day}T00:00:00.000Z`) - 86_400_000).toISOString().slice(0, 10);
    return nasaGibsFirePointsForDay(previousDay, day);
  }
};

/** Recent interagency incident reports. The IRWIN working record is an official
 * report of an incident; it is not a certified fire occurrence or news article. */
const nifcFireReports = async () => {
  const retrievedAt = new Date().toISOString();
  const windowStart = new Date(Date.now() - 30 * 86_400_000).toISOString();
  const url = new URL(NIFC_INCIDENT_URL);
  url.searchParams.set("where", `POOState='US-KS' AND IncidentTypeCategory IN ('WF','RX','CX') AND FireDiscoveryDateTime >= TIMESTAMP '${windowStart.slice(0, 10)} 00:00:00'`);
  url.searchParams.set("outFields", "IncidentName,IncidentTypeCategory,IncidentSize,FireDiscoveryDateTime,ModifiedOnDateTime_dt,FireOutDateTime,PercentContained,FireCause,POOCounty,POOState,UniqueFireIdentifier,IrwinID,ActiveFireCandidate,POOJurisdictionalAgency,POOProtectingAgency");
  url.searchParams.set("returnGeometry", "true");
  url.searchParams.set("outSR", "4326");
  url.searchParams.set("orderByFields", "FireDiscoveryDateTime DESC");
  url.searchParams.set("resultRecordCount", String(MAX_NIFC_INCIDENTS + 1));
  url.searchParams.set("f", "geojson");
  const payload = await fetchBoundedJson(url.toString(), 12_000);
  if (!Array.isArray(payload.features)) throw new UpstreamError("NIFC incident response had no feature array.");
  // ArcGIS GeoJSON can report a provider-side limit independently of this
  // adapter's display cap, including when fewer than 250 records are returned.
  const transferFlags = [payload.exceededTransferLimit, isRecord(payload.properties) ? payload.properties.exceededTransferLimit : undefined];
  if (transferFlags.some(flag => flag !== undefined && typeof flag !== "boolean")) throw new UpstreamError("NIFC incident response had invalid transfer-limit metadata.");
  const providerLimited = transferFlags.includes(true);
  const features: Feature<Geometry, GeoJsonProperties>[] = [];
  let skipped = 0;
  let invalidOptionalDates = 0;
  const optionalDate = (value: unknown): string | null => {
    if (value === undefined || value === null) return null;
    const milliseconds = asNumber(value);
    const date = milliseconds === null ? null : new Date(milliseconds);
    if (!date || !Number.isFinite(date.getTime())) { invalidOptionalDates += 1; return null; }
    return date.toISOString();
  };
  let newestTimestamp: string | null = null;
  for (const candidate of payload.features) {
    if (features.length >= MAX_NIFC_INCIDENTS) break;
    if (!isRecord(candidate) || !isRecord(candidate.geometry) || candidate.geometry.type !== "Point" || !Array.isArray(candidate.geometry.coordinates)) { skipped += 1; continue; }
    const properties = isRecord(candidate.properties) ? candidate.properties : {};
    const longitude = asNumber(candidate.geometry.coordinates[0]);
    const latitude = asNumber(candidate.geometry.coordinates[1]);
    const identifier = asString(properties.UniqueFireIdentifier);
    const category = asString(properties.IncidentTypeCategory);
    const discoveryMs = asNumber(properties.FireDiscoveryDateTime);
    if (longitude === null || latitude === null || longitude < EVENT_BOUNDS[0] || longitude > EVENT_BOUNDS[2] || latitude < EVENT_BOUNDS[1] || latitude > EVENT_BOUNDS[3]
      || asString(properties.POOState) !== "US-KS" || !identifier || !["WF", "RX", "CX"].includes(category ?? "") || discoveryMs === null || discoveryMs < Date.parse(windowStart) - 86_400_000 || discoveryMs > Date.now()) { skipped += 1; continue; }
    const discoveryAt = new Date(discoveryMs).toISOString();
    const modifiedAt = optionalDate(properties.ModifiedOnDateTime_dt);
    const reportedOutAt = optionalDate(properties.FireOutDateTime);
    const featureId = `nifc-${identifier}`;
    const name = asString(properties.IncidentName)?.trim().slice(0, 120) || "Unnamed incident";
    features.push({ type: "Feature", id: featureId, geometry: { type: "Point", coordinates: [longitude, latitude] }, properties: {
      featureId, name, incidentType: category === "WF" ? "Wildfire" : category === "RX" ? "Prescribed fire" : "Incident complex",
      reportState: reportedOutAt ? "Out date reported" : "No out date in record; current activity unverified",
      discoveryAt, modifiedAt, reportedOutAt, county: asString(properties.POOCounty), state: "Kansas",
      reportedAcres: asNumber(properties.IncidentSize), percentContained: asNumber(properties.PercentContained),
      reportedCause: asString(properties.FireCause), jurisdiction: asString(properties.POOJurisdictionalAgency),
      protectingAgency: asString(properties.POOProtectingAgency), uniqueFireIdentifier: identifier,
      irwinId: asString(properties.IrwinID), latitude, longitude, retrievedAt,
      dataRole: "NIFC WFIGS/IRWIN working incident report", evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    } });
    if (modifiedAt && (!newestTimestamp || modifiedAt > newestTimestamp)) newestTimestamp = modifiedAt;
  }
  const capped = payload.features.length > MAX_NIFC_INCIDENTS;
  const truncated = capped || providerLimited;
  return envelope("nifc-fire-reports", { type: "FeatureCollection", features },
    "NIFC WFIGS Wildland Fire Incident Locations Year to Date · IRWIN working records",
    `Interagency reports discovered in the last 30 days in Kansas; ${skipped} record${skipped === 1 ? "" : "s"} withheld because required fields, Kansas scope or discovery times did not match; ${invalidOptionalDates} invalid optional date value${invalidOptionalDates === 1 ? "" : "s"} withheld${capped ? `; capped at ${MAX_NIFC_INCIDENTS}` : ""}${providerLimited ? "; the provider reported a transfer limit, so additional records may be missing" : ""}. A report establishes that an incident was recorded by the provider, not its current activity, exact perimeter, location precision, independent satellite confirmation, or KFM evidence. The absence of a report is not an all-clear. IRWIN working records may change; certified occurrence data are separate.`,
    retrievedAt, newestTimestamp, skipped > 0 || invalidOptionalDates > 0 || truncated, truncated);
};

/** Public, non-restricted National Register listing points in Kansas. NPS withholds
 * sensitive locations at the source; this adapter never requests or infers them. */
const nationalRegisterPlaces = async () => {
  const retrievedAt = new Date().toISOString();
  const url = new URL(NPS_NRHP_POINTS_URL);
  url.searchParams.set("where", "State='KANSAS'");
  url.searchParams.set("outFields", "NRIS_Refnum,RESNAME,ResType,City,County,CertDate,Is_NHL,NARA_URL,STATUS,Vicinity");
  url.searchParams.set("returnGeometry", "true");
  url.searchParams.set("outSR", "4326");
  url.searchParams.set("orderByFields", "RESNAME ASC");
  url.searchParams.set("resultRecordCount", String(MAX_NRHP_PLACES));
  url.searchParams.set("f", "geojson");
  const payload = await fetchBoundedJson(url.toString(), 15_000);
  if (!Array.isArray(payload.features)) throw new UpstreamError("NPS National Register response had no feature array.");
  const transferFlags = [payload.exceededTransferLimit, isRecord(payload.properties) ? payload.properties.exceededTransferLimit : undefined];
  const providerLimited = transferFlags.includes(true);
  const features: Feature<Geometry, GeoJsonProperties>[] = [];
  const pointsPerListing = new Map<string, number>();
  let skipped = 0, removed = 0, landmarks = 0;
  for (const candidate of payload.features) {
    if (features.length >= MAX_NRHP_PLACES) break;
    if (!isRecord(candidate) || !isRecord(candidate.geometry) || candidate.geometry.type !== "Point" || !Array.isArray(candidate.geometry.coordinates)) { skipped += 1; continue; }
    const properties = isRecord(candidate.properties) ? candidate.properties : {};
    const longitude = asNumber(candidate.geometry.coordinates[0]);
    const latitude = asNumber(candidate.geometry.coordinates[1]);
    const refnum = asString(properties.NRIS_Refnum)?.trim() ?? "";
    const name = asString(properties.RESNAME)?.trim().slice(0, 160) ?? "";
    if (longitude === null || latitude === null || longitude < EVENT_BOUNDS[0] || longitude > EVENT_BOUNDS[2] || latitude < EVENT_BOUNDS[1] || latitude > EVENT_BOUNDS[3]
      || !/^[0-9A-Z]{6,12}$/.test(refnum) || !name) { skipped += 1; continue; }
    const status = asString(properties.STATUS)?.trim() || null;
    if (status && status !== "Listed") { removed += 1; continue; }
    // Some listings (districts, multiple-part properties) publish several points under one reference number.
    const part = (pointsPerListing.get(refnum) ?? 0) + 1;
    pointsPerListing.set(refnum, part);
    const featureId = part === 1 ? `nrhp-${refnum}` : `nrhp-${refnum}-${part}`;
    const landmark = asString(properties.Is_NHL)?.trim().toUpperCase() === "X";
    if (landmark && part === 1) landmarks += 1;
    const resourceType = (asString(properties.ResType)?.trim().toLowerCase() ?? "").replace(/[^a-z ]/g, "").slice(0, 24) || "not recorded";
    const certified = (asString(properties.CertDate)?.trim() ?? "").replace(/-+$/, "");
    const nara = asString(properties.NARA_URL)?.trim() ?? "";
    features.push({ type: "Feature", id: featureId, geometry: { type: "Point", coordinates: [longitude, latitude] }, properties: {
      featureId, name, resourceType, landmark, landmarkLabel: landmark ? "National Historic Landmark" : null,
      city: asString(properties.City)?.trim().slice(0, 80) || null, county: asString(properties.County)?.trim().slice(0, 80) || null,
      certified: /^\d{4}(-\d{2}(-\d{2})?)?$/.test(certified) ? certified : null, refnum,
      vicinity: asString(properties.Vicinity) === "True" ? "Approximate (vicinity) location" : "Listed address location",
      recordUrl: /^https:\/\/catalog\.archives\.gov\/[\w/?=&%.:-]+$/.test(nara) ? nara.slice(0, 240) : null,
      latitude, longitude, retrievedAt, dataRole: "NPS public National Register point", evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    } });
  }
  const capped = payload.features.length > MAX_NRHP_PLACES;
  const truncated = capped || providerLimited;
  return envelope("nps-nrhp-places", { type: "FeatureCollection", features },
    "National Park Service · National Register of Historic Places public point locations",
    `${pointsPerListing.size.toLocaleString("en-US")} listed Kansas properties shown at ${features.length.toLocaleString("en-US")} public points (${landmarks} flagged as National Historic Landmarks in this service). ${removed} record${removed === 1 ? "" : "s"} marked removed from the Register ${removed === 1 ? "is" : "are"} omitted; ${skipped} record${skipped === 1 ? "" : "s"} withheld for an invalid location or identifier${truncated ? "; the response was capped, so additional listings may be missing" : ""}. NPS withholds restricted and sensitive locations. Points are representative locations, not boundaries, access permission, ownership or current condition.`,
    retrievedAt, null, skipped > 0 || truncated, truncated);
};

const stormReportCategory = (description: string) => {
  if (/tornado|funnel|landspout|waterspout/i.test(description)) return "Tornado";
  if (/hail/i.test(description)) return "Hail";
  if (/flood/i.test(description)) return "Flood";
  if (/snow|sleet|freez|blizzard|ice|chill|cold/i.test(description)) return "Winter";
  if (/wind|wnd|gust|downburst/i.test(description)) return "Wind";
  return "Other";
};
const stormReportRank = (category: string, magnitude: number | null) => {
  if (category === "Tornado") return 3;
  if (magnitude === null) return 0;
  if (category === "Hail") return magnitude >= 2 ? 4 : magnitude >= 1.5 ? 3 : magnitude >= 1 ? 2 : 1;
  if (category === "Wind") return magnitude >= 80 ? 4 : magnitude >= 70 ? 3 : magnitude >= 58 ? 2 : 1;
  if (category === "Winter") return magnitude >= 12 ? 3 : magnitude >= 6 ? 2 : 1;
  return 1;
};

/** Preliminary NWS local storm reports for Kansas in the provider's rolling 72-hour layer. */
const recentStormReports = async () => {
  const retrievedAt = new Date().toISOString();
  const url = new URL(NWS_STORM_REPORTS_URL);
  url.searchParams.set("where", "state='KS'");
  url.searchParams.set("outFields", "objectid,wfo,lsr_validtime,descript,loc_desc,magnitude,units,remarks,state");
  url.searchParams.set("returnGeometry", "true");
  url.searchParams.set("outSR", "4326");
  url.searchParams.set("orderByFields", "lsr_validtime DESC");
  url.searchParams.set("resultRecordCount", String(MAX_STORM_REPORTS + 1));
  url.searchParams.set("f", "geojson");
  const payload = await fetchBoundedJson(url.toString(), 12_000);
  if (!Array.isArray(payload.features)) throw new UpstreamError("NWS storm-report response had no feature array.");
  const providerLimited = [payload.exceededTransferLimit, isRecord(payload.properties) ? payload.properties.exceededTransferLimit : undefined].includes(true);
  const features: Feature<Geometry, GeoJsonProperties>[] = [];
  let skipped = 0;
  let newestTimestamp: string | null = null;
  const earliest = Date.now() - 4 * 86_400_000;
  for (const candidate of payload.features) {
    if (features.length >= MAX_STORM_REPORTS) break;
    if (!isRecord(candidate) || !isRecord(candidate.geometry) || candidate.geometry.type !== "Point" || !Array.isArray(candidate.geometry.coordinates)) { skipped += 1; continue; }
    const properties = isRecord(candidate.properties) ? candidate.properties : {};
    const longitude = asNumber(candidate.geometry.coordinates[0]);
    const latitude = asNumber(candidate.geometry.coordinates[1]);
    const validMs = asNumber(properties.lsr_validtime);
    const objectId = asNumber(properties.objectid);
    const description = asString(properties.descript)?.trim().slice(0, 60) ?? "";
    if (longitude === null || latitude === null || longitude < EVENT_BOUNDS[0] || longitude > EVENT_BOUNDS[2] || latitude < EVENT_BOUNDS[1] || latitude > EVENT_BOUNDS[3]
      || asString(properties.state) !== "KS" || validMs === null || validMs < earliest || validMs > Date.now() + 3_600_000 || objectId === null || !description) { skipped += 1; continue; }
    const reportedAt = new Date(validMs).toISOString();
    const magnitude = asNumeric(properties.magnitude);
    const units = asString(properties.units)?.trim().slice(0, 20) || null;
    const category = stormReportCategory(description);
    const featureId = `lsr-${objectId}-${validMs}`;
    features.push({ type: "Feature", id: featureId, geometry: { type: "Point", coordinates: [longitude, latitude] }, properties: {
      featureId, name: `${description}${asString(properties.loc_desc) ? ` · ${asString(properties.loc_desc)!.trim().slice(0, 80)}` : ""}`,
      reportType: description, category, reportedAt, magnitude: magnitude === null ? null : magnitude, units,
      magnitudeLabel: magnitude === null ? "Not reported" : `${magnitude.toLocaleString("en-US")}${units ? ` ${units}` : ""}`,
      sizeRank: stormReportRank(category, magnitude), location: asString(properties.loc_desc)?.trim().slice(0, 120) || null,
      office: asString(properties.wfo)?.trim().slice(0, 60) || null, remarks: asString(properties.remarks)?.trim().slice(0, 400) || null,
      latitude, longitude, retrievedAt, dataRole: "Preliminary NWS local storm report", evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    } });
    if (!newestTimestamp || reportedAt > newestTimestamp) newestTimestamp = reportedAt;
  }
  const capped = payload.features.length > MAX_STORM_REPORTS;
  const truncated = capped || providerLimited;
  return envelope("nws-storm-reports", { type: "FeatureCollection", features },
    "NOAA NWS local storm reports · Last_72_Hours service layer",
    `Preliminary Kansas reports in the provider's rolling 72-hour window; ${skipped} record${skipped === 1 ? "" : "s"} withheld for missing time, location, type or Kansas scope${truncated ? "; capped, so additional reports may be missing" : ""}. Reports are relayed observations with approximate locations; they can be duplicated, revised or incomplete and are not warnings, damage surveys or KFM evidence. No reports is not an all-clear.`,
    retrievedAt, newestTimestamp, skipped > 0 || truncated, truncated);
};

type KdwpLayer = Readonly<{ feed: "kdwp-wildlife-areas" | "kdwp-wiha-access"; url: string; outFields: string; source: string;
  properties: (record: JsonRecord) => Record<string, unknown> | null; limitation: (shown: number, skipped: number, truncated: boolean) => string }>;

const finitePolygon = (geometry: unknown): Geometry | null => {
  if (!isRecord(geometry) || (geometry.type !== "Polygon" && geometry.type !== "MultiPolygon") || !Array.isArray(geometry.coordinates)) return null;
  const polygons = (geometry.type === "Polygon" ? [geometry.coordinates] : geometry.coordinates) as unknown[];
  let west = Infinity, east = -Infinity, south = Infinity, north = -Infinity, points = 0;
  for (const polygon of polygons) {
    if (!Array.isArray(polygon) || polygon.length === 0) return null;
    for (const ring of polygon) {
      if (!Array.isArray(ring) || ring.length < 4) return null;
      for (const position of ring) {
        const lon = Array.isArray(position) ? asNumber(position[0]) : null, lat = Array.isArray(position) ? asNumber(position[1]) : null;
        if (lon === null || lat === null) return null;
        west = Math.min(west, lon); east = Math.max(east, lon); south = Math.min(south, lat); north = Math.max(north, lat); points++;
      }
    }
  }
  if (points === 0 || east < EVENT_BOUNDS[0] || west > EVENT_BOUNDS[2] || north < EVENT_BOUNDS[1] || south > EVENT_BOUNDS[3]) return null;
  return geometry as unknown as Geometry;
};
const cleanText = (value: unknown, max = 120) => {
  const text = asString(value)?.replace(/\s+/g, " ").trim().slice(0, max);
  return text ? text : null;
};
const kdwpLink = (value: unknown) => {
  // KDWP stores the link as an HTML snippet; keep only an https ksoutdoors href.
  const raw = asString(value)?.trim() ?? "", href = raw.match(/href="([^"]+)"/i)?.[1] ?? raw;
  const url = href.trim();
  return /^https:\/\/(?:www\.)?ksoutdoors\.(?:com|gov)\/[\w/?=&%.:#-]*$/i.test(url) ? url.slice(0, 240) : null;
};

/** KDWP public outdoor-access polygons from fixed FeatureServer layers. Paged,
 * simplified at the provider, bounded to Kansas, and reduced to access fields. */
const kdwpAreas = async (layer: KdwpLayer) => {
  const retrievedAt = new Date().toISOString();
  const features: Feature<Geometry, GeoJsonProperties>[] = [];
  let skipped = 0, providerLimited = false, received = 0;
  for (let offset = 0; offset < MAX_KDWP_AREAS; offset += KDWP_PAGE_SIZE) {
    const url = new URL(layer.url);
    url.searchParams.set("where", "1=1");
    url.searchParams.set("outFields", layer.outFields);
    url.searchParams.set("returnGeometry", "true");
    url.searchParams.set("outSR", "4326");
    url.searchParams.set("maxAllowableOffset", "0.0005");
    url.searchParams.set("geometryPrecision", "5");
    url.searchParams.set("orderByFields", "FID ASC");
    url.searchParams.set("resultOffset", String(offset));
    url.searchParams.set("resultRecordCount", String(KDWP_PAGE_SIZE));
    url.searchParams.set("f", "geojson");
    const payload = await fetchBoundedJson(url.toString(), 20_000);
    if (!Array.isArray(payload.features)) throw new UpstreamError("KDWP response had no feature array.");
    received += payload.features.length;
    for (const candidate of payload.features) {
      if (!isRecord(candidate)) { skipped++; continue; }
      const geometry = finitePolygon(candidate.geometry);
      const properties = layer.properties(isRecord(candidate.properties) ? candidate.properties : {});
      if (!geometry || !properties) { skipped++; continue; }
      features.push({ type: "Feature", id: String(properties.featureId), geometry, properties: { ...properties, retrievedAt, evidenceRole: "EXTERNAL_CONTEXT_ONLY" } });
    }
    const more = [payload.exceededTransferLimit, isRecord(payload.properties) ? payload.properties.exceededTransferLimit : undefined].includes(true);
    if (!more || payload.features.length === 0) break;
    if (offset + KDWP_PAGE_SIZE >= MAX_KDWP_AREAS) providerLimited = true;
  }
  return envelope(layer.feed, { type: "FeatureCollection", features }, layer.source,
    layer.limitation(features.length, skipped, providerLimited), retrievedAt, null, skipped > 0 || providerLimited, providerLimited || received > MAX_KDWP_AREAS);
};

const KDWP_WILDLIFE_AREAS: KdwpLayer = {
  feed: "kdwp-wildlife-areas", url: KDWP_WILDLIFE_AREAS_URL, source: "Kansas Department of Wildlife and Parks · Wildlife Areas (public web map layer)",
  outFields: "FID,NAME,OTHER_NAME,Label_Name,Access_Res,Hunt_Acc,Hyperlink,Area_Site",
  properties: record => {
    const fid = asNumber(record.FID);
    if (fid === null || !Number.isInteger(fid)) return null;
    const name = cleanText(record.Label_Name) ?? cleanText(record.NAME) ?? "KDWP wildlife area (unnamed in source)";
    return { featureId: `kdwp-area-${fid}`, name, otherName: cleanText(record.OTHER_NAME),
      accessRestrictions: cleanText(record.Access_Res, 240), huntingAccess: cleanText(record.Hunt_Acc, 120), areaType: cleanText(record.Area_Site, 60),
      recordUrl: kdwpLink(record.Hyperlink), dataRole: "KDWP public wildlife area polygon" };
  },
  limitation: (shown, skipped, truncated) => `${shown.toLocaleString("en-US")} KDWP-managed public wildlife area polygons; ${skipped} withheld for invalid geometry, identifier or Kansas scope${truncated ? "; capped" : ""}. Boundaries are simplified display geometry. Regulations, closures, refuges and seasons change; check KDWP before entering or hunting. Not a legal boundary, regulation or KFM evidence.`,
};
const KDWP_WIHA: KdwpLayer = {
  feed: "kdwp-wiha-access", url: KDWP_WIHA_URL, source: "Kansas Department of Wildlife and Parks · Walk-In Hunting Access (2026–2027 public web map layer)",
  // Contract identifiers and the free-text NOTES field are not requested: NOTES holds KDWP
  // administrative text such as landowner contract numbers, payment rates and CRP expiries.
  outFields: "FID,AREAID,ACRES,SPECIES1,SPECIES2,SPECIES3,SPECIES4,SPECIES5,ISARCHERYS,COUNTY",
  properties: record => {
    const fid = asNumber(record.FID);
    if (fid === null || !Number.isInteger(fid)) return null;
    const species = [record.SPECIES1, record.SPECIES2, record.SPECIES3, record.SPECIES4, record.SPECIES5].map(value => cleanText(value, 40)).filter(Boolean);
    const archery = asNumeric(record.ISARCHERYS);
    const area = asNumeric(record.AREAID), acres = asNumeric(record.ACRES);
    return { featureId: `kdwp-wiha-${fid}`, name: `WIHA tract${area === null ? "" : ` ${area}`}${cleanText(record.COUNTY, 40) ? ` · ${cleanText(record.COUNTY, 40)} County` : ""}`,
      areaId: area, acres: acres === null ? null : Math.round(acres), county: cleanText(record.COUNTY, 40),
      species: species.length ? species.join(", ") : null, archeryOnly: archery === 1 ? "Archery only" : archery === 0 ? "Not archery-only" : null,
      dataRole: "KDWP walk-in hunting access tract" };
  },
  limitation: (shown, skipped, truncated) => `${shown.toLocaleString("en-US")} walk-in hunting access tracts from KDWP's public season layer; ${skipped} withheld for invalid geometry, identifier or Kansas scope${truncated ? "; capped" : ""}. WIHA is private land enrolled for public hunting only during posted seasons and rules; landowner contract identifiers are not requested. Check the current KDWP atlas and regulations before going. Not legal access, trespass permission or KFM evidence.`,
};

const cacheSeconds: Record<Feed, number> = { "census-counties": 86_400, "usgs-streamflow": 120, "usgs-earthquakes": 300, "nws-alerts": 30, "noaa-hms-smoke": 900, "nasa-gibs-fire-points": 900, "nifc-fire-reports": 900, "raspberry-shake-stations": 900, "fema-disaster-declarations": 3600, "nps-nrhp-places": 86_400, "nws-storm-reports": 300, "kdwp-wildlife-areas": 86_400, "kdwp-wiha-access": 86_400 };

export async function GET(request: NextRequest) {
  const feed = request.nextUrl.searchParams.get("feed");
  const day = request.nextUrl.searchParams.get("day");
  if (request.nextUrl.searchParams.has("day") && (!day || !eventDay(day) || day < (feed === "nasa-gibs-fire-points" ? "2018-01-01" : feed === "noaa-hms-smoke" ? "2005-08-05" : "1800-01-01") || day > new Date().toISOString().slice(0, 10) || !["usgs-earthquakes", "noaa-hms-smoke", "nasa-gibs-fire-points", "raspberry-shake-stations"].includes(feed ?? "")) || [...request.nextUrl.searchParams.keys()].some((key) => !["feed", "day"].includes(key) || request.nextUrl.searchParams.getAll(key).length !== 1)) return NextResponse.json({ error: "Choose an exact supported calendar date and source." }, { status: 400 });
  if (feed !== "census-counties" && feed !== "usgs-streamflow" && feed !== "usgs-earthquakes" && feed !== "nws-alerts" && feed !== "noaa-hms-smoke" && feed !== "nasa-gibs-fire-points" && feed !== "nifc-fire-reports" && feed !== "raspberry-shake-stations" && feed !== "fema-disaster-declarations" && feed !== "nps-nrhp-places" && feed !== "nws-storm-reports" && feed !== "kdwp-wildlife-areas" && feed !== "kdwp-wiha-access") {
    return NextResponse.json({ error: "Unknown live-context feed. The adapter accepts only its fixed allowlist." }, { status: 400, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
  }
  try {
    const result = feed === "census-counties" ? await censusCounties() : feed === "usgs-streamflow" ? await latestStreamflow() : feed === "usgs-earthquakes" ? await recentEarthquakes(day) : feed === "nws-alerts" ? await activeNwsAlerts() : feed === "noaa-hms-smoke" ? await currentHmsSmoke(day, request.signal) : feed === "nasa-gibs-fire-points" ? await nasaGibsFirePoints(day) : feed === "nifc-fire-reports" ? await nifcFireReports() : feed === "fema-disaster-declarations" ? await recentFemaDeclarations() : feed === "nps-nrhp-places" ? await nationalRegisterPlaces() : feed === "nws-storm-reports" ? await recentStormReports() : feed === "kdwp-wildlife-areas" ? await kdwpAreas(KDWP_WILDLIFE_AREAS) : feed === "kdwp-wiha-access" ? await kdwpAreas(KDWP_WIHA) : await raspberryShakeStations(day);
    return NextResponse.json(result, { headers: { "Cache-Control": `public, max-age=0, s-maxage=${cacheSeconds[feed]}, stale-while-revalidate=${cacheSeconds[feed]}`, "X-KFM-Context-State": result.state, "X-Content-Type-Options": "nosniff" } });
  } catch (error) {
    const timeout = error instanceof UpstreamError && error.timeout;
    return NextResponse.json({ error: error instanceof Error ? error.message : "Official upstream request failed.", state: "error", fallback: "No fallback inference or substitute dataset was produced." }, { status: timeout ? 504 : 502, headers: { "Cache-Control": "no-store", "X-KFM-Context-State": "error", "X-Content-Type-Options": "nosniff" } });
  }
}
