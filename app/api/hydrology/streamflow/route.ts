import { NextRequest, NextResponse } from "next/server";

export const dynamic = "force-dynamic";

const USGS_API_ORIGIN = "https://api.waterdata.usgs.gov";
const USGS_SITE_ORIGIN = "https://waterdata.usgs.gov";
const OGC_ROOT = "/ogcapi/v1/collections";
const COLLECTION_PATHS = Object.freeze({
  latest: `${OGC_ROOT}/latest-continuous/items`,
  continuous: `${OGC_ROOT}/continuous/items`,
  daily: `${OGC_ROOT}/daily/items`,
  stations: `${OGC_ROOT}/monitoring-locations/items`,
});
const ALLOWED_UPSTREAM_PATHS: ReadonlySet<string> = new Set(Object.values(COLLECTION_PATHS));
const USER_AGENT = "KansasFrontierMatrixExplorer/1.0 (https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site)";
const RESPONSE_BYTE_LIMIT = 12 * 1024 * 1024;
const REQUEST_TIMEOUT_MS = 25_000;
const NETWORK_STATION_CAP = 72;
const OBSERVATION_CAP = 20_000;
const STATION_ID_PATTERN = /^USGS-(\d{8,15})$/;
const PARAMETER_PATTERN = /^0006[05]$/;
const STATISTIC_PATTERN = /^\d{5}$/;
const DATE_ONLY_PATTERN = /^\d{4}-\d{2}-\d{2}$/;
const ISO_TIMESTAMP_PATTERN = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$/;

type JsonRecord = Record<string, unknown>;
type Mode = "network" | "station";
type Range = "24h" | "7d" | "30d" | "1y";
type ParameterCode = "00060" | "00065";
type CollectionName = keyof typeof COLLECTION_PATHS;

type ParsedQuery = Readonly<{
  mode: Mode;
  range: Range;
  parameterCode: ParameterCode;
  stationId: string | null;
  stationNumber: string | null;
  archiveEnd: string | null;
  resolution: "continuous" | "daily";
}>;

type Collection = Readonly<{
  features: readonly JsonRecord[];
  hasNextPage: boolean;
  responseTimestamp: string;
}>;

type Station = Readonly<{
  id: string;
  stationId: string;
  number: string;
  name: string;
  coordinates: readonly [number, number];
  longitude: number;
  latitude: number;
  huc: string | null;
  county: string | null;
  drainageArea: number | null;
  contributingDrainageArea: number | null;
  sourceUrl: string;
  agencyCode: "USGS";
  siteTypeCode: string | null;
}>;

type Observation = Readonly<{
  stationId: string;
  observedAt: string;
  value: number | null;
  unit: string;
  parameterCode: ParameterCode;
  statisticId: string | null;
  approvalStatus: string | null;
  qualifier: string | readonly string[] | null;
  qualifiers: readonly string[];
  lastModified: string | null;
}>;

type ParsedObservation = Readonly<{
  observation: Observation;
  revisionTime: number;
  revisionSource: string;
  coordinates: readonly [number, number];
}>;

type LatestCandidate = Readonly<{
  stationId: string;
  stationNumber: string;
  coordinates: readonly [number, number];
  observedAt: string;
  lastModified: string | null;
}>;

class QueryError extends Error {}

class UsgsUpstreamError extends Error {
  constructor(message: string, readonly timeout = false) {
    super(message);
  }
}

class StationNotFoundError extends Error {}

const isRecord = (value: unknown): value is JsonRecord => (
  Boolean(value) && typeof value === "object" && !Array.isArray(value)
);

const requiredString = (value: unknown, label: string, maximum = 512): string => {
  if (typeof value !== "string" || value.trim() === "" || value.length > maximum) {
    throw new UsgsUpstreamError(`USGS response field ${label} was invalid.`);
  }
  return value;
};

const nullableString = (record: JsonRecord, key: string, maximum = 512): string | null => {
  if (!Object.hasOwn(record, key)) throw new UsgsUpstreamError(`USGS response omitted ${key}.`);
  const value = record[key];
  if (value === null) return null;
  return requiredString(value, key, maximum);
};

const nullableNumber = (record: JsonRecord, key: string): number | null => {
  if (!Object.hasOwn(record, key)) throw new UsgsUpstreamError(`USGS response omitted ${key}.`);
  const value = record[key];
  if (value === null) return null;
  const parsed = typeof value === "number"
    ? value
    : typeof value === "string" && value.trim() !== ""
      ? Number(value)
      : Number.NaN;
  if (!Number.isFinite(parsed)) throw new UsgsUpstreamError(`USGS response field ${key} was not numeric or null.`);
  return parsed;
};

const canonicalTimestamp = (value: unknown, label: string, allowDateOnly = false): string => {
  const text = requiredString(value, label, 80);
  if (allowDateOnly && DATE_ONLY_PATTERN.test(text)) {
    const parsed = new Date(`${text}T00:00:00.000Z`);
    if (!Number.isFinite(parsed.getTime()) || parsed.toISOString().slice(0, 10) !== text) {
      throw new UsgsUpstreamError(`USGS response field ${label} was not a valid calendar date.`);
    }
    return parsed.toISOString();
  }
  if (!ISO_TIMESTAMP_PATTERN.test(text)) {
    throw new UsgsUpstreamError(`USGS response field ${label} was not an ISO timestamp.`);
  }
  const milliseconds = Date.parse(text);
  if (!Number.isFinite(milliseconds)) throw new UsgsUpstreamError(`USGS response field ${label} was not a valid timestamp.`);
  return new Date(milliseconds).toISOString();
};

const nullableTimestamp = (record: JsonRecord, key: string): Readonly<{
  normalized: string | null;
  milliseconds: number;
  source: string;
}> => {
  if (!Object.hasOwn(record, key)) throw new UsgsUpstreamError(`USGS response omitted ${key}.`);
  const value = record[key];
  if (value === null) return { normalized: null, milliseconds: Number.NEGATIVE_INFINITY, source: "" };
  const source = requiredString(value, key, 80);
  const normalized = canonicalTimestamp(source, key);
  return { normalized, milliseconds: Date.parse(normalized), source };
};

const qualifierValues = (record: JsonRecord): Readonly<{
  source: string | readonly string[] | null;
  normalized: readonly string[];
}> => {
  if (!Object.hasOwn(record, "qualifier")) throw new UsgsUpstreamError("USGS response omitted qualifier.");
  const value = record.qualifier;
  if (value === null) return { source: null, normalized: [] };
  if (typeof value === "string") {
    const qualifier = requiredString(value, "qualifier", 80);
    return { source: qualifier, normalized: [qualifier] };
  }
  if (!Array.isArray(value) || value.length > 16) {
    throw new UsgsUpstreamError("USGS response field qualifier was not a bounded string array or null.");
  }
  const qualifiers = value.map((qualifier) => requiredString(qualifier, "qualifier", 80));
  return { source: qualifiers, normalized: qualifiers };
};

const pointCoordinates = (feature: JsonRecord): readonly [number, number] => {
  if (!isRecord(feature.geometry) || feature.geometry.type !== "Point" || !Array.isArray(feature.geometry.coordinates)) {
    throw new UsgsUpstreamError("USGS feature geometry was not a GeoJSON Point.");
  }
  const [longitude, latitude] = feature.geometry.coordinates;
  if (typeof longitude !== "number" || !Number.isFinite(longitude) || longitude < -180 || longitude > 180
    || typeof latitude !== "number" || !Number.isFinite(latitude) || latitude < -90 || latitude > 90) {
    throw new UsgsUpstreamError("USGS feature coordinates were outside the valid longitude/latitude domain.");
  }
  return [longitude, latitude];
};

const featureProperties = (feature: JsonRecord): JsonRecord => {
  if (feature.type !== "Feature" || typeof feature.id !== "string" || !isRecord(feature.properties)) {
    throw new UsgsUpstreamError("USGS response contained a malformed GeoJSON feature.");
  }
  return feature.properties;
};

const collectionUrl = (collection: CollectionName, parameters: Readonly<Record<string, string>>): URL => {
  const url = new URL(COLLECTION_PATHS[collection], USGS_API_ORIGIN);
  url.searchParams.set("f", "json");
  for (const [key, value] of Object.entries(parameters)) url.searchParams.set(key, value);
  return url;
};

const assertFixedUpstream = (url: URL) => {
  if (url.origin !== USGS_API_ORIGIN || !ALLOWED_UPSTREAM_PATHS.has(url.pathname)
    || url.username !== "" || url.password !== "" || url.hash !== "") {
    throw new UsgsUpstreamError("The hydrology adapter refused a non-allowlisted upstream URL.");
  }
};

const readBoundedBody = async (response: Response, controller: AbortController): Promise<string> => {
  const declaredLength = response.headers.get("content-length")?.trim();
  if (declaredLength) {
    if (!/^\d+$/.test(declaredLength)) throw new UsgsUpstreamError("USGS returned an invalid Content-Length header.");
    if (Number(declaredLength) > RESPONSE_BYTE_LIMIT) {
      controller.abort();
      throw new UsgsUpstreamError("USGS response exceeded the 12 MB adapter limit.");
    }
  }
  if (!response.body) throw new UsgsUpstreamError("USGS response did not contain a body.");

  const reader = response.body.getReader();
  const chunks: Uint8Array[] = [];
  let total = 0;
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    total += value.byteLength;
    if (total > RESPONSE_BYTE_LIMIT) {
      controller.abort();
      await reader.cancel().catch(() => undefined);
      throw new UsgsUpstreamError("USGS response exceeded the 12 MB adapter limit.");
    }
    chunks.push(value);
  }

  const bytes = new Uint8Array(total);
  let offset = 0;
  for (const chunk of chunks) {
    bytes.set(chunk, offset);
    offset += chunk.byteLength;
  }
  return new TextDecoder("utf-8", { fatal: true }).decode(bytes);
};

const parseCollection = (value: unknown): Collection => {
  if (!isRecord(value) || value.type !== "FeatureCollection" || !Array.isArray(value.features)
    || !Number.isInteger(value.numberReturned) || value.numberReturned !== value.features.length
    || !Array.isArray(value.links)) {
    throw new UsgsUpstreamError("USGS response did not match the required OGC FeatureCollection schema.");
  }
  const responseTimestamp = canonicalTimestamp(value.timeStamp, "timeStamp");
  const features = value.features.map((feature) => {
    if (!isRecord(feature)) throw new UsgsUpstreamError("USGS FeatureCollection contained a non-object feature.");
    return feature;
  });
  let hasNextPage = false;
  for (const link of value.links) {
    if (!isRecord(link) || typeof link.rel !== "string" || typeof link.href !== "string") {
      throw new UsgsUpstreamError("USGS FeatureCollection contained a malformed link.");
    }
    if (link.rel === "next") hasNextPage = true;
  }
  return { features, hasNextPage, responseTimestamp };
};

const fetchCollection = async (url: URL): Promise<Collection> => {
  assertFixedUpstream(url);
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);
  try {
    const response = await fetch(url, {
      cache: "no-store",
      redirect: "manual",
      signal: controller.signal,
      headers: {
        Accept: "application/geo+json,application/json;q=0.9",
        "User-Agent": USER_AGENT,
      },
    });
    if (!response.ok) throw new UsgsUpstreamError(`USGS Water Data returned HTTP ${response.status}.`);
    const contentType = response.headers.get("content-type")?.toLowerCase() ?? "";
    if (!contentType.includes("json")) throw new UsgsUpstreamError("USGS Water Data returned an unexpected media type.");
    const body = await readBoundedBody(response, controller);
    let parsed: unknown;
    try {
      parsed = JSON.parse(body) as unknown;
    } catch {
      throw new UsgsUpstreamError("USGS Water Data returned malformed JSON.");
    }
    return parseCollection(parsed);
  } catch (error) {
    if (error instanceof UsgsUpstreamError) throw error;
    if (error instanceof Error && error.name === "AbortError") {
      throw new UsgsUpstreamError("USGS Water Data request exceeded the 25 second timeout.", true);
    }
    throw new UsgsUpstreamError(error instanceof Error ? error.message : "USGS Water Data request failed.");
  } finally {
    clearTimeout(timeout);
  }
};

const parseStationFeature = (feature: JsonRecord, expectedIds: ReadonlySet<string>): Station => {
  const properties = featureProperties(feature);
  const id = requiredString(properties.id, "monitoring location id", 32);
  const match = id.match(STATION_ID_PATTERN);
  if (!match || !expectedIds.has(id) || properties.agency_code !== "USGS") {
    throw new UsgsUpstreamError("USGS monitoring-location response contained an unexpected station.");
  }
  const number = requiredString(properties.monitoring_location_number, "monitoring_location_number", 15);
  if (number !== match[1]) throw new UsgsUpstreamError("USGS monitoring-location number did not match its canonical identifier.");
  const name = requiredString(properties.monitoring_location_name, "monitoring_location_name", 240).trim();
  const coordinates = pointCoordinates(feature);
  const siteTypeCode = nullableString(properties, "site_type_code", 40);
  const huc = nullableString(properties, "hydrologic_unit_code", 40);
  const county = nullableString(properties, "county_name", 160);
  const drainageArea = nullableNumber(properties, "drainage_area");
  const contributingDrainageArea = nullableNumber(properties, "contributing_drainage_area");
  return {
    id,
    stationId: id,
    number,
    name,
    coordinates,
    longitude: coordinates[0],
    latitude: coordinates[1],
    huc,
    county,
    drainageArea,
    contributingDrainageArea,
    sourceUrl: `${USGS_SITE_ORIGIN}/monitoring-location/${number}/`,
    agencyCode: "USGS",
    siteTypeCode,
  };
};

const parseObservationFeature = (
  feature: JsonRecord,
  expectedIds: ReadonlySet<string> | null,
  expectedParameter: ParameterCode,
  expectedStatistic: string | null,
): ParsedObservation => {
  const properties = featureProperties(feature);
  requiredString(properties.time_series_id, "time_series_id", 80);
  const stationId = requiredString(properties.monitoring_location_id, "monitoring_location_id", 32);
  if (!STATION_ID_PATTERN.test(stationId) || expectedIds && !expectedIds.has(stationId)) {
    throw new UsgsUpstreamError("USGS observation response contained an unexpected station identifier.");
  }
  if (properties.parameter_code !== expectedParameter) {
    throw new UsgsUpstreamError("USGS observation response contained an unexpected parameter code.");
  }
  const statisticId = nullableString(properties, "statistic_id", 20);
  if (statisticId !== null && !STATISTIC_PATTERN.test(statisticId)) {
    throw new UsgsUpstreamError("USGS observation response contained an invalid statistic identifier.");
  }
  if (expectedStatistic && statisticId !== expectedStatistic) {
    throw new UsgsUpstreamError("USGS daily response did not contain the requested statistic.");
  }
  const observedAt = canonicalTimestamp(properties.time, "time", true);
  const value = nullableNumber(properties, "value");
  const unit = requiredString(properties.unit_of_measure, "unit_of_measure", 64).trim();
  const approvalStatus = nullableString(properties, "approval_status", 80);
  if (approvalStatus !== null && approvalStatus !== "Provisional" && approvalStatus !== "Approved") {
    throw new UsgsUpstreamError("USGS observation response contained an unknown approval status.");
  }
  const qualifier = qualifierValues(properties);
  const revision = nullableTimestamp(properties, "last_modified");
  return {
    observation: {
      stationId,
      observedAt,
      value,
      unit,
      parameterCode: expectedParameter,
      statisticId,
      approvalStatus,
      qualifier: qualifier.source,
      qualifiers: qualifier.normalized,
      lastModified: revision.normalized,
    },
    revisionTime: revision.milliseconds,
    revisionSource: revision.source,
    coordinates: pointCoordinates(feature),
  };
};

const newerObservation = (candidate: ParsedObservation, current: ParsedObservation): boolean => (
  candidate.revisionTime > current.revisionTime
  || candidate.revisionTime === current.revisionTime && candidate.revisionSource > current.revisionSource
);

const dedupeObservations = (observations: readonly ParsedObservation[]): Observation[] => {
  const deduped = new Map<string, ParsedObservation>();
  for (const candidate of observations) {
    const key = `${candidate.observation.stationId}\u0000${candidate.observation.observedAt}`;
    const current = deduped.get(key);
    if (!current || newerObservation(candidate, current)) deduped.set(key, candidate);
  }
  return [...deduped.values()]
    .map(({ observation }) => observation)
    .sort((left, right) => (
      Date.parse(left.observedAt) - Date.parse(right.observedAt)
      || left.stationId.localeCompare(right.stationId)
    ))
    .slice(0, OBSERVATION_CAP);
};

const latestCandidates = (features: readonly JsonRecord[]): LatestCandidate[] => {
  const newest = new Map<string, ParsedObservation>();
  for (const feature of features) {
    const candidate = parseObservationFeature(feature, null, "00060", null);
    const current = newest.get(candidate.observation.stationId);
    const candidateTime = Date.parse(candidate.observation.observedAt);
    const currentTime = current ? Date.parse(current.observation.observedAt) : Number.NEGATIVE_INFINITY;
    if (!current || candidateTime > currentTime || candidateTime === currentTime && newerObservation(candidate, current)) {
      newest.set(candidate.observation.stationId, candidate);
    }
  }
  return [...newest.values()].map((candidate) => ({
    stationId: candidate.observation.stationId,
    stationNumber: candidate.observation.stationId.slice("USGS-".length),
    coordinates: candidate.coordinates,
    observedAt: candidate.observation.observedAt,
    lastModified: candidate.observation.lastModified,
  })).sort((left, right) => left.stationId.localeCompare(right.stationId));
};

/**
 * Deliberately caps the statewide animation at 72 gauges. Starting at the
 * westernmost gauge, deterministic farthest-point sampling in normalized
 * lon/lat space retains geographic coverage instead of selecting API order.
 */
const geographicallySpread = (candidates: readonly LatestCandidate[]): LatestCandidate[] => {
  if (candidates.length <= NETWORK_STATION_CAP) return [...candidates];
  const minimumLongitude = Math.min(...candidates.map((candidate) => candidate.coordinates[0]));
  const maximumLongitude = Math.max(...candidates.map((candidate) => candidate.coordinates[0]));
  const minimumLatitude = Math.min(...candidates.map((candidate) => candidate.coordinates[1]));
  const maximumLatitude = Math.max(...candidates.map((candidate) => candidate.coordinates[1]));
  const longitudeSpan = Math.max(maximumLongitude - minimumLongitude, Number.EPSILON);
  const latitudeSpan = Math.max(maximumLatitude - minimumLatitude, Number.EPSILON);
  const normalized = candidates.map((candidate) => ({
    candidate,
    x: (candidate.coordinates[0] - minimumLongitude) / longitudeSpan,
    y: (candidate.coordinates[1] - minimumLatitude) / latitudeSpan,
  }));
  const first = [...normalized].sort((left, right) => (
    left.x - right.x || left.y - right.y || left.candidate.stationId.localeCompare(right.candidate.stationId)
  ))[0];
  const selected = [first];
  const selectedIds = new Set([first.candidate.stationId]);

  while (selected.length < NETWORK_STATION_CAP) {
    let best: (typeof normalized)[number] | null = null;
    let bestDistance = Number.NEGATIVE_INFINITY;
    for (const point of normalized) {
      if (selectedIds.has(point.candidate.stationId)) continue;
      const minimumSquaredDistance = Math.min(...selected.map((chosen) => (
        (point.x - chosen.x) ** 2 + (point.y - chosen.y) ** 2
      )));
      if (minimumSquaredDistance > bestDistance
        || minimumSquaredDistance === bestDistance && best
          && point.candidate.stationId.localeCompare(best.candidate.stationId) < 0) {
        best = point;
        bestDistance = minimumSquaredDistance;
      }
    }
    if (!best) break;
    selected.push(best);
    selectedIds.add(best.candidate.stationId);
  }
  return selected.map(({ candidate }) => candidate).sort((left, right) => left.stationId.localeCompare(right.stationId));
};

const parseStations = (collection: Collection, expectedIds: ReadonlySet<string>): Station[] => {
  const stations = new Map<string, Station>();
  for (const feature of collection.features) {
    const station = parseStationFeature(feature, expectedIds);
    const existing = stations.get(station.stationId);
    if (existing && JSON.stringify(existing) !== JSON.stringify(station)) {
      throw new UsgsUpstreamError("USGS returned conflicting metadata for one monitoring location.");
    }
    stations.set(station.stationId, station);
  }
  return [...stations.values()].sort((left, right) => left.stationId.localeCompare(right.stationId));
};

const parseObservations = (
  collection: Collection,
  expectedIds: ReadonlySet<string>,
  parameterCode: ParameterCode,
  statisticId: string | null,
): Observation[] => dedupeObservations(collection.features.map((feature) => (
  parseObservationFeature(feature, expectedIds, parameterCode, statisticId)
)));

const responseHasMoreThanObservationCap = (collection: Collection) => (
  collection.hasNextPage || collection.features.length > OBSERVATION_CAP
);

const sourceUpdatedAt = (
  observations: readonly Observation[],
  additional: readonly (string | null)[] = [],
): string | null => {
  const timestamps = [
    ...observations.map((observation) => observation.lastModified),
    ...additional,
  ].filter((value): value is string => value !== null);
  return timestamps.sort((left, right) => Date.parse(right) - Date.parse(left))[0] ?? null;
};

const subtractRange = (end: Date, range: Range): Date => {
  const durations: Record<Range, number> = {
    "24h": 24 * 60 * 60 * 1_000,
    "7d": 7 * 24 * 60 * 60 * 1_000,
    "30d": 30 * 24 * 60 * 60 * 1_000,
    "1y": 365 * 24 * 60 * 60 * 1_000,
  };
  return new Date(end.getTime() - durations[range]);
};

const singleQueryValue = (request: NextRequest, name: string, required: boolean): string | null => {
  const values = request.nextUrl.searchParams.getAll(name);
  if (values.length > 1) throw new QueryError(`Query parameter ${name} must appear at most once.`);
  if (required && values.length !== 1) throw new QueryError(`Query parameter ${name} is required.`);
  return values[0] ?? null;
};

const parseQuery = (request: NextRequest): ParsedQuery => {
  const allowed = new Set(["mode", "range", "station", "parameter", "end", "resolution"]);
  for (const key of request.nextUrl.searchParams.keys()) {
    if (!allowed.has(key)) throw new QueryError("The request contained an unsupported query parameter.");
  }
  const mode = singleQueryValue(request, "mode", true);
  const range = singleQueryValue(request, "range", true);
  const archiveEnd = singleQueryValue(request, "end", false);
  const resolution = singleQueryValue(request, "resolution", false) ?? (range === "1y" ? "daily" : "continuous");
  if (resolution !== "continuous" && resolution !== "daily") throw new QueryError("resolution must be continuous or daily.");
  if (archiveEnd && (!ISO_TIMESTAMP_PATTERN.test(archiveEnd) || !archiveEnd.endsWith("Z") || !Number.isFinite(Date.parse(archiveEnd)) || new Date(archiveEnd).toISOString().replace(".000Z", "Z") !== archiveEnd.replace(".000Z", "Z") || Date.parse(archiveEnd) > Date.now() || Date.parse(archiveEnd) < Date.parse("1800-01-01T00:00:00Z"))) throw new QueryError("end must be an exact past UTC timestamp since 1800.");
  if (mode !== "network" && mode !== "station") throw new QueryError("mode must be network or station.");
  if (range !== "24h" && range !== "7d" && range !== "30d" && range !== "1y") {
    throw new QueryError("range must be 24h, 7d, 30d, or 1y.");
  }

  if (mode === "network") {
    const parameter = singleQueryValue(request, "parameter", false);
    const station = singleQueryValue(request, "station", false);
    if (range !== "24h" || parameter && parameter !== "00060" || station !== null || archiveEnd !== null) {
      throw new QueryError("Network mode supports only range=24h and parameter 00060, without a station.");
    }
    if (resolution !== "continuous") throw new QueryError("Network mode uses continuous observations.");
    return { mode, range, parameterCode: "00060", stationId: null, stationNumber: null, archiveEnd: null, resolution };
  }

  const stationId = singleQueryValue(request, "station", true);
  const parameter = singleQueryValue(request, "parameter", true);
  const match = stationId?.match(STATION_ID_PATTERN);
  if (!match) throw new QueryError("station must match USGS- followed by 8 to 15 digits.");
  if (!parameter || !PARAMETER_PATTERN.test(parameter)) throw new QueryError("parameter must be 00060 or 00065.");
  return {
    mode,
    range,
    parameterCode: parameter as ParameterCode,
    stationId,
    stationNumber: match[1],
    archiveEnd,
    resolution,
  };
};

const cacheSeconds = (query: ParsedQuery): number => (
  query.mode === "network" ? 120 : query.range === "1y" ? 3_600 : 300
);

const successfulHeaders = (seconds: number) => ({
  "Cache-Control": `public, max-age=${seconds}, stale-while-revalidate=${seconds}`,
  "X-Content-Type-Options": "nosniff",
});

const sourceLinks = (series: "continuous" | "daily") => [
  `${USGS_API_ORIGIN}${OGC_ROOT}/monitoring-locations`,
  `${USGS_API_ORIGIN}${OGC_ROOT}/${series}`,
  ...(series === "continuous" ? [`${USGS_API_ORIGIN}${OGC_ROOT}/latest-continuous`] : []),
];

const parserContract = (
  query: ParsedQuery,
  queryStart: string,
  queryEnd: string,
  partial: boolean,
  observations: readonly Observation[],
  source: string,
) => query.parameterCode === "00060" ? {
  format: "kfm-usgs-streamflow-v1" as const,
  feed: "usgs-streamflow" as const,
  state: partial ? "partial" as const : observations.length === 0 ? "empty" as const : "ready" as const,
  query: {
    mode: query.range === "1y" || query.archiveEnd ? "historical-series" as const : "recent-series" as const,
    start: queryStart,
    end: queryEnd,
    parameterCode: "00060" as const,
  },
  source,
  interpolation: false as const,
  evidenceRole: "EXTERNAL_CONTEXT_ONLY" as const,
} : {};

const networkBundle = async (query: ParsedQuery, queryStart: string, queryEnd: string) => {
  const latestUrl = collectionUrl("latest", {
    limit: String(OBSERVATION_CAP),
    state_code: "20",
    agency_code: "USGS",
    site_type_code: "ST",
    parameter_code: "00060",
    datetime: `${queryStart}/${queryEnd}`,
  });
  const latest = await fetchCollection(latestUrl);
  const candidates = geographicallySpread(latestCandidates(latest.features));
  const expectedIds = new Set(candidates.map((candidate) => candidate.stationId));
  const retrievedAt = new Date().toISOString();

  if (candidates.length === 0) {
    const limitation = "No qualifying Kansas USGS stream-gauge observation was returned in the requested 24-hour window. No synthetic, interpolated, or stale fallback was substituted.";
    const source = `${USGS_API_ORIGIN}${OGC_ROOT}/continuous`;
    return {
      kind: "usgs-streamflow-bundle" as const,
      mode: query.mode,
      range: query.range,
      parameterCode: query.parameterCode,
      statisticId: null,
      queryStart,
      queryEnd,
      retrievedAt,
      sourceUpdatedAt: null,
      stations: [] as Station[],
      observations: [] as Observation[],
      partial: latest.hasNextPage,
      truncated: latest.hasNextPage,
      limitation,
      sourceLinks: sourceLinks("continuous"),
      ...parserContract(query, queryStart, queryEnd, latest.hasNextPage, [], source),
    };
  }

  const stationNumbers = candidates.map((candidate) => candidate.stationNumber).join(",");
  const stationIds = candidates.map((candidate) => candidate.stationId).join(",");
  const metadataUrl = collectionUrl("stations", {
    limit: String(NETWORK_STATION_CAP),
    agency_code: "USGS",
    monitoring_location_number: stationNumbers,
  });
  const observationsUrl = collectionUrl("continuous", {
    limit: String(OBSERVATION_CAP),
    monitoring_location_id: stationIds,
    parameter_code: "00060",
    datetime: `${queryStart}/${queryEnd}`,
  });
  const [metadata, series] = await Promise.all([
    fetchCollection(metadataUrl),
    fetchCollection(observationsUrl),
  ]);
  const stations = parseStations(metadata, expectedIds);
  const stationIdsWithMetadata = new Set(stations.map((station) => station.stationId));
  const parsedObservations = parseObservations(series, expectedIds, "00060", null);
  const observations = parsedObservations.filter((observation) => stationIdsWithMetadata.has(observation.stationId));
  const observationStationIds = new Set(observations.map((observation) => observation.stationId));
  const metadataIncomplete = stationIdsWithMetadata.size !== expectedIds.size;
  const seriesIncomplete = stations.some((station) => !observationStationIds.has(station.stationId));
  const truncated = latest.hasNextPage || metadata.hasNextPage || responseHasMoreThanObservationCap(series);
  const partial = truncated || metadataIncomplete || seriesIncomplete;
  const statisticIds = [...new Set(observations.map((observation) => observation.statisticId).filter((value): value is string => value !== null))];
  const limitation = [
    "Kansas network mode is deliberately capped at 72 stream gauges, selected by deterministic farthest-point geographic sampling rather than API order; it is not an all-stations inventory.",
    "The animation uses exact USGS samples without spatial or temporal interpolation. Values may be provisional, qualified, delayed, revised, missing, or incomparable across differently sized basins; this is not flood guidance.",
    truncated ? "At least one OGC collection advertised additional records beyond the fixed 20,000-observation page cap, so this bundle is truncated." : null,
    metadataIncomplete ? "Metadata was unavailable for one or more sampled gauges; their observations were omitted rather than shown without provenance." : null,
    seriesIncomplete ? "One or more sampled gauges had no continuous-series observation in the query window." : null,
  ].filter((value): value is string => value !== null).join(" ");
  const source = `${USGS_API_ORIGIN}${OGC_ROOT}/continuous`;
  return {
    kind: "usgs-streamflow-bundle" as const,
    mode: query.mode,
    range: query.range,
    parameterCode: query.parameterCode,
    statisticId: statisticIds.length === 1 ? statisticIds[0] : null,
    queryStart,
    queryEnd,
    retrievedAt,
    sourceUpdatedAt: sourceUpdatedAt(observations, candidates.map((candidate) => candidate.lastModified)),
    stations,
    observations,
    partial,
    truncated,
    limitation,
    sourceLinks: sourceLinks("continuous"),
    ...parserContract(query, queryStart, queryEnd, partial, observations, source),
  };
};

const stationBundle = async (query: ParsedQuery, queryStart: string, queryEnd: string) => {
  const stationId = query.stationId as string;
  const stationNumber = query.stationNumber as string;
  const expectedIds = new Set([stationId]);
  const daily = query.resolution === "daily";
  const statisticId = daily ? "00003" : null;
  const metadataUrl = collectionUrl("stations", {
    limit: "2",
    agency_code: "USGS",
    monitoring_location_number: stationNumber,
  });
  const observationsUrl = collectionUrl(daily ? "daily" : "continuous", {
    limit: String(OBSERVATION_CAP),
    monitoring_location_id: stationId,
    parameter_code: query.parameterCode,
    ...(statisticId ? { statistic_id: statisticId } : {}),
    datetime: `${queryStart}/${queryEnd}`,
  });
  const [metadata, series] = await Promise.all([
    fetchCollection(metadataUrl),
    fetchCollection(observationsUrl),
  ]);
  const stations = parseStations(metadata, expectedIds);
  if (stations.length === 0) throw new StationNotFoundError(`USGS monitoring location ${stationId} was not found.`);
  if (stations.length !== 1 || metadata.hasNextPage) {
    throw new UsgsUpstreamError("USGS returned ambiguous monitoring-location metadata.");
  }
  const observations = parseObservations(series, expectedIds, query.parameterCode, statisticId);
  const observedStatisticIds = [...new Set(observations
    .map((observation) => observation.statisticId)
    .filter((value): value is string => value !== null))];
  const bundleStatisticId = statisticId ?? (observedStatisticIds.length === 1 ? observedStatisticIds[0] : null);
  const truncated = responseHasMoreThanObservationCap(series);
  const partial = truncated;
  const retrievedAt = new Date().toISOString();
  const limitation = [
    daily
      ? "This view uses USGS daily values with statistic 00003 (daily mean); it does not supply hourly or instantaneous observations."
      : "The selected-station view uses exact USGS continuous samples without interpolation.",
    "Values may be provisional, qualified, delayed, revised, or missing. Stage and discharge are distinct parameters, and this product is not flood guidance.",
    observations.length === 0 ? "No observation was returned for the station and interval; no zero, stale value, or synthetic fallback was substituted." : null,
    truncated ? "The OGC collection advertised additional records beyond the fixed 20,000-observation page cap, so this bundle is truncated." : null,
  ].filter((value): value is string => value !== null).join(" ");
  const source = `${USGS_API_ORIGIN}${OGC_ROOT}/${daily ? "daily" : "continuous"}`;
  return {
    kind: "usgs-streamflow-bundle" as const,
    mode: query.mode,
    range: query.range,
    parameterCode: query.parameterCode,
    statisticId: bundleStatisticId,
    queryStart,
    queryEnd,
    retrievedAt,
    sourceUpdatedAt: sourceUpdatedAt(observations),
    stations,
    observations,
    partial,
    truncated,
    limitation,
    sourceLinks: sourceLinks(daily ? "daily" : "continuous"),
    ...parserContract(query, queryStart, queryEnd, partial, observations, source),
  };
};

const errorResponse = (status: number, code: string, message: string) => NextResponse.json({
  kind: "usgs-streamflow-error",
  state: "error",
  code,
  message,
  interpolation: false,
  evidenceRole: "EXTERNAL_CONTEXT_ONLY",
}, {
  status,
  headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" },
});

export async function GET(request: NextRequest) {
  try {
    const query = parseQuery(request);
    const queryEndDate = query.archiveEnd ? new Date(query.archiveEnd) : new Date();
    const queryEnd = queryEndDate.toISOString();
    const queryStart = subtractRange(queryEndDate, query.range).toISOString();
    const bundle = query.mode === "network"
      ? await networkBundle(query, queryStart, queryEnd)
      : await stationBundle(query, queryStart, queryEnd);
    return NextResponse.json(bundle, {
      status: 200,
      headers: successfulHeaders(cacheSeconds(query)),
    });
  } catch (error) {
    if (error instanceof QueryError) {
      return errorResponse(400, "USGS_STREAMFLOW_INVALID_QUERY", error.message);
    }
    if (error instanceof StationNotFoundError) {
      return errorResponse(404, "USGS_STREAMFLOW_STATION_NOT_FOUND", error.message);
    }
    const timeout = error instanceof UsgsUpstreamError && error.timeout;
    console.error("KFM_STREAMFLOW_SOURCE_FAILED", error instanceof Error ? error.message : "Unknown provider failure");
    return errorResponse(
      timeout ? 504 : 502,
      timeout ? "USGS_STREAMFLOW_TIMEOUT" : "USGS_STREAMFLOW_UNAVAILABLE",
      timeout
        ? "USGS Water Data did not respond within 25 seconds. No fallback observations were used."
        : "USGS Water Data was unavailable or failed the fixed response schema. No fallback observations were used.",
    );
  }
}
