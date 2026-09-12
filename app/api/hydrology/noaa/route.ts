import { NextRequest, NextResponse } from "next/server";

export const dynamic = "force-dynamic";

const NOAA_ORIGIN = "https://api.water.noaa.gov";
const NWPS_BASE = `${NOAA_ORIGIN}/nwps/v1`;
const NWPS_DOCS_URL = `${NWPS_BASE}/docs/`;
const NWPS_API_INFO_URL = "https://water.noaa.gov/about/api";
const NWM_INFO_URL = "https://water.noaa.gov/about/nwm";
const KANSAS_GAUGES_URL = `${NWPS_BASE}/gauges?bbox.xmin=-102.0517&bbox.ymin=36.993&bbox.xmax=-94.588&bbox.ymax=40.003&srid=EPSG_4326`;
const NOAA_USER_AGENT = "KansasFrontierMatrixExplorer/1.0 (https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site)";

const REQUEST_TIMEOUT_MS = 15_000;
const MAX_NETWORK_BYTES = 1024 * 1024;
const MAX_METADATA_BYTES = 512 * 1024;
const MAX_STAGEFLOW_BYTES = 2 * 1024 * 1024;
const MAX_REACH_BYTES = 2 * 1024 * 1024;
const MAX_NETWORK_RECORDS = 400;
const MAX_STAGEFLOW_POINTS = 5_000;
const MAX_REACH_POINTS = 1_000;
const MAX_HISTORY_EVENTS = 250;
const MAX_IMPACTS = 250;
const LID_PATTERN = /^[A-Z0-9]{3,8}$/;
const REACH_PATTERN = /^\d{1,12}$/;

type HydrologyMode = "network" | "gauge" | "reach";
type JsonRecord = Record<string, unknown>;
type SourceLink = {
  rel: "upstream" | "documentation" | "service";
  title: string;
  href: string;
};

class AdapterError extends Error {
  constructor(
    message: string,
    readonly code: string,
    readonly timeout = false,
  ) {
    super(message);
  }
}

const isRecord = (value: unknown): value is JsonRecord => Boolean(value) && typeof value === "object" && !Array.isArray(value);

const asString = (value: unknown, maxLength = 2_000) => {
  if (typeof value !== "string") return null;
  const trimmed = value.trim();
  return trimmed ? trimmed.slice(0, maxLength) : null;
};

const asBoolean = (value: unknown) => typeof value === "boolean" ? value : null;

const asNumber = (value: unknown) => {
  const candidate = typeof value === "number"
    ? value
    : typeof value === "string" && value.trim() !== ""
      ? Number(value)
      : Number.NaN;
  if (!Number.isFinite(candidate) || candidate === -999 || candidate === -9999) return null;
  return candidate;
};

const asTimestamp = (value: unknown) => {
  const candidate = asString(value, 64);
  if (!candidate || /^0001-01-01T/i.test(candidate) || !Number.isFinite(Date.parse(candidate))) return null;
  return candidate;
};

const recordAt = (value: unknown, key: string) => isRecord(value) && isRecord(value[key]) ? value[key] as JsonRecord : null;

const arrayAt = (value: unknown, key: string) => isRecord(value) && Array.isArray(value[key]) ? value[key] as unknown[] : [];

const readBoundedBody = async (response: Response, maxBytes: number) => {
  const declaredLength = Number(response.headers.get("content-length") ?? "0");
  if (Number.isFinite(declaredLength) && declaredLength > maxBytes) {
    throw new AdapterError("NOAA response exceeded the adapter byte limit.", "NOAA_RESPONSE_TOO_LARGE");
  }
  if (!response.body) throw new AdapterError("NOAA response did not include a body.", "NOAA_EMPTY_RESPONSE");

  const reader = response.body.getReader();
  const chunks: Uint8Array[] = [];
  let total = 0;
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    if (!value) continue;
    total += value.byteLength;
    if (total > maxBytes) {
      await reader.cancel();
      throw new AdapterError("NOAA response exceeded the adapter byte limit.", "NOAA_RESPONSE_TOO_LARGE");
    }
    chunks.push(value);
  }

  const body = new Uint8Array(total);
  let offset = 0;
  for (const chunk of chunks) {
    body.set(chunk, offset);
    offset += chunk.byteLength;
  }
  return new TextDecoder().decode(body);
};

const fetchFixedJson = async (url: string, maxBytes: number): Promise<JsonRecord> => {
  const parsedUrl = new URL(url);
  if (parsedUrl.origin !== NOAA_ORIGIN || !parsedUrl.pathname.startsWith("/nwps/v1/")) {
    throw new AdapterError("The requested upstream is outside the fixed NOAA allowlist.", "NOAA_UPSTREAM_DENIED");
  }

  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);
  try {
    const response = await fetch(parsedUrl, {
      cache: "no-store",
      signal: controller.signal,
      headers: {
        Accept: "application/json",
        "User-Agent": NOAA_USER_AGENT,
      },
    });
    if (!response.ok) {
      throw new AdapterError(`NOAA returned HTTP ${response.status}.`, "NOAA_UPSTREAM_STATUS");
    }
    const contentType = response.headers.get("content-type")?.toLowerCase() ?? "";
    if (!contentType.includes("json")) {
      throw new AdapterError("NOAA returned an unexpected media type.", "NOAA_MEDIA_TYPE");
    }
    const text = await readBoundedBody(response, maxBytes);
    let parsed: unknown;
    try {
      parsed = JSON.parse(text) as unknown;
    } catch {
      throw new AdapterError("NOAA returned malformed JSON.", "NOAA_INVALID_JSON");
    }
    if (!isRecord(parsed)) {
      throw new AdapterError("NOAA response did not match the expected object contract.", "NOAA_CONTRACT_MISMATCH");
    }
    return parsed;
  } catch (error) {
    if (error instanceof AdapterError) throw error;
    if (error instanceof Error && error.name === "AbortError") {
      throw new AdapterError("NOAA request timed out.", "NOAA_TIMEOUT", true);
    }
    throw new AdapterError("NOAA request failed.", "NOAA_UNAVAILABLE");
  } finally {
    clearTimeout(timeout);
  }
};

const normalizeStatus = (value: unknown, sourceRole: "OFFICIAL_NWS_OBSERVATION" | "OFFICIAL_NWS_FORECAST") => {
  const status = isRecord(value) ? value : {};
  return {
    sourceRole,
    validTime: asTimestamp(status.validTime),
    primary: {
      value: asNumber(status.primary),
      unit: asString(status.primaryUnit, 32),
    },
    secondary: {
      value: asNumber(status.secondary),
      unit: asString(status.secondaryUnit, 32),
    },
    floodCategory: asString(status.floodCategory, 64),
  };
};

const normalizeNetworkGauge = (candidate: unknown) => {
  if (!isRecord(candidate)) return null;
  const state = recordAt(candidate, "state");
  const lid = asString(candidate.lid, 8);
  const latitude = asNumber(candidate.latitude);
  const longitude = asNumber(candidate.longitude);
  if (
    !lid
    || !LID_PATTERN.test(lid)
    || state?.abbreviation !== "KS"
    || latitude === null
    || longitude === null
    || latitude < 36.993
    || latitude > 40.003
    || longitude < -102.0517
    || longitude > -94.588
  ) return null;

  const rfc = recordAt(candidate, "rfc");
  const wfo = recordAt(candidate, "wfo");
  const pedts = recordAt(candidate, "pedts");
  const status = recordAt(candidate, "status");
  return {
    kind: "gauge",
    sourceRole: "OFFICIAL_NWS_GAUGE_STATUS",
    lid,
    name: asString(candidate.name, 300),
    location: { latitude, longitude },
    state: { abbreviation: "KS", name: asString(state.name, 100) },
    rfc: {
      abbreviation: asString(rfc?.abbreviation, 16),
      name: asString(rfc?.name, 200),
    },
    wfo: {
      abbreviation: asString(wfo?.abbreviation, 16),
      name: asString(wfo?.name, 200),
    },
    pedts: {
      observed: asString(pedts?.observed, 16),
      forecast: asString(pedts?.forecast, 16),
    },
    observed: normalizeStatus(status?.observed, "OFFICIAL_NWS_OBSERVATION"),
    forecast: normalizeStatus(status?.forecast, "OFFICIAL_NWS_FORECAST"),
  };
};

const normalizeThreshold = (value: unknown) => {
  if (!isRecord(value)) return null;
  return {
    stage: asNumber(value.stage),
    flow: asNumber(value.flow),
  };
};

const normalizeHistoryEvent = (value: unknown, kind: "crest" | "low-water") => {
  if (!isRecord(value)) return null;
  const occurredTime = asTimestamp(value.occurredTime);
  if (!occurredTime) return null;
  return {
    kind,
    sourceRole: "OFFICIAL_NWS_HISTORICAL_EVENT",
    occurredTime,
    stage: asNumber(value.stage),
    flow: asNumber(value.flow),
    preliminary: asString(value.preliminary, 32),
    oldDatum: asBoolean(value.olddatum),
    statement: asString(value.statement, 2_000),
  };
};

const normalizeGaugeMetadata = (payload: JsonRecord) => {
  const lid = asString(payload.lid, 8);
  if (!lid || !LID_PATTERN.test(lid)) {
    throw new AdapterError("NOAA gauge metadata omitted a valid LID.", "NOAA_CONTRACT_MISMATCH");
  }
  const rfc = recordAt(payload, "rfc");
  const wfo = recordAt(payload, "wfo");
  const state = recordAt(payload, "state");
  const pedts = recordAt(payload, "pedts");
  const status = recordAt(payload, "status");
  const flood = recordAt(payload, "flood");
  const categories = recordAt(flood, "categories");
  const crests = recordAt(flood, "crests");
  const lowWaters = recordAt(flood, "lowWaters");
  const historicCrestsRaw = arrayAt(crests, "historic");
  const historicLowWatersRaw = arrayAt(lowWaters, "historic");
  const impactsRaw = arrayAt(flood, "impacts");
  const verticalDatums = arrayAt(recordAt(payload, "datums")?.vertical, "value")
    .slice(0, 20)
    .flatMap((entry) => isRecord(entry) ? [{
      label: asString(entry.label, 200),
      abbreviation: asString(entry.abbrev, 32),
      description: asString(entry.description, 2_000),
      value: asNumber(entry.value),
    }] : []);

  const historicCrests = historicCrestsRaw
    .slice(0, MAX_HISTORY_EVENTS)
    .map((entry) => normalizeHistoryEvent(entry, "crest"))
    .filter((entry) => entry !== null);
  const historicLowWaters = historicLowWatersRaw
    .slice(0, MAX_HISTORY_EVENTS)
    .map((entry) => normalizeHistoryEvent(entry, "low-water"))
    .filter((entry) => entry !== null);
  const impacts = impactsRaw.slice(0, MAX_IMPACTS).flatMap((entry) => isRecord(entry) ? [{
    stage: asNumber(entry.stage),
    statement: asString(entry.statement, 2_000),
  }] : []);

  return {
    record: {
      kind: "gauge-metadata",
      sourceRole: "OFFICIAL_NWS_GAUGE_METADATA",
      lid,
      usgsId: asString(payload.usgsId, 24),
      reachId: asString(payload.reachId, 24),
      name: asString(payload.name, 300),
      description: asString(payload.description, 500),
      county: asString(payload.county, 200),
      timeZone: asString(payload.timeZone, 100),
      location: {
        latitude: asNumber(payload.latitude),
        longitude: asNumber(payload.longitude),
      },
      state: {
        abbreviation: asString(state?.abbreviation, 16),
        name: asString(state?.name, 100),
      },
      rfc: {
        abbreviation: asString(rfc?.abbreviation, 16),
        name: asString(rfc?.name, 200),
      },
      wfo: {
        abbreviation: asString(wfo?.abbreviation, 16),
        name: asString(wfo?.name, 200),
      },
      pedts: {
        observed: asString(pedts?.observed, 16),
        forecast: asString(pedts?.forecast, 16),
      },
      observed: normalizeStatus(status?.observed, "OFFICIAL_NWS_OBSERVATION"),
      forecast: normalizeStatus(status?.forecast, "OFFICIAL_NWS_FORECAST"),
      flood: {
        stageUnits: asString(flood?.stageUnits, 32),
        flowUnits: asString(flood?.flowUnits, 32),
        categories: {
          action: normalizeThreshold(categories?.action),
          minor: normalizeThreshold(categories?.minor),
          moderate: normalizeThreshold(categories?.moderate),
          major: normalizeThreshold(categories?.major),
        },
        historicCrests,
        historicLowWaters,
        impacts,
      },
      verticalDatums,
      normalThreshold: isRecord(payload.normalThreshold) ? {
        value: asNumber(payload.normalThreshold.value),
        units: asString(payload.normalThreshold.units, 32),
      } : null,
      lowThreshold: isRecord(payload.lowThreshold) ? {
        value: asNumber(payload.lowThreshold.value),
        units: asString(payload.lowThreshold.units, 32),
      } : null,
      inService: isRecord(payload.inService) ? {
        enabled: asBoolean(payload.inService.enabled),
        message: asString(payload.inService.message, 500),
      } : null,
      forecastReliability: asString(payload.forecastReliability, 500),
    },
    partial: historicCrests.length < Math.min(historicCrestsRaw.length, MAX_HISTORY_EVENTS)
      || historicLowWaters.length < Math.min(historicLowWatersRaw.length, MAX_HISTORY_EVENTS)
      || impacts.length < Math.min(impactsRaw.length, MAX_IMPACTS),
    truncated: historicCrestsRaw.length > MAX_HISTORY_EVENTS
      || historicLowWatersRaw.length > MAX_HISTORY_EVENTS
      || impactsRaw.length > MAX_IMPACTS,
  };
};

const normalizeStageFlow = (payload: JsonRecord, product: "observed" | "forecast") => {
  if (!Array.isArray(payload.data)) {
    throw new AdapterError("NOAA stage/flow response omitted its data array.", "NOAA_CONTRACT_MISMATCH");
  }
  const normalized = payload.data.flatMap((entry) => {
    if (!isRecord(entry)) return [];
    const validTime = asTimestamp(entry.validTime);
    if (!validTime) return [];
    return [{
      validTime,
      generatedTime: asTimestamp(entry.generatedTime),
      primary: asNumber(entry.primary),
      secondary: asNumber(entry.secondary),
    }];
  }).sort((left, right) => Date.parse(left.validTime) - Date.parse(right.validTime)
    || Date.parse(left.generatedTime ?? left.validTime) - Date.parse(right.generatedTime ?? right.validTime));
  const truncated = normalized.length > MAX_STAGEFLOW_POINTS;
  const points = truncated
    ? product === "observed"
      ? normalized.slice(-MAX_STAGEFLOW_POINTS)
      : normalized.slice(0, MAX_STAGEFLOW_POINTS)
    : normalized;
  return {
    record: {
      kind: "stageflow-series",
      sourceRole: product === "observed" ? "OFFICIAL_NWS_OBSERVATION" : "OFFICIAL_NWS_FORECAST",
      product,
      pedts: asString(payload.pedts, 16),
      issuedTime: asTimestamp(payload.issuedTime),
      wfo: asString(payload.wfo, 16),
      timeZone: asString(payload.timeZone, 100),
      primary: {
        name: asString(payload.primaryName, 100),
        units: asString(payload.primaryUnits, 32),
      },
      secondary: {
        name: asString(payload.secondaryName, 100),
        units: asString(payload.secondaryUnits, 32),
      },
      points,
    },
    partial: normalized.length !== payload.data.length || truncated,
    truncated,
  };
};

const normalizeReachHeader = (payload: JsonRecord, expectedReachId: string) => {
  const reach = recordAt(payload, "reach");
  const reachId = asString(reach?.reachId, 24);
  if (!reach || reachId !== expectedReachId) {
    throw new AdapterError("NOAA reach response did not match the requested reach.", "NOAA_CONTRACT_MISMATCH");
  }
  const route = recordAt(reach, "route");
  const normalizeRoute = (value: unknown) => Array.isArray(value) ? value.slice(0, 250).flatMap((entry) => {
    if (!isRecord(entry)) return [];
    const relatedReachId = asString(entry.reachId, 24);
    return relatedReachId ? [{ reachId: relatedReachId, streamOrder: asNumber(entry.streamOrder) }] : [];
  }) : [];
  return {
    kind: "reach-metadata",
    sourceRole: "NWM_REACH_METADATA",
    reachId,
    name: asString(reach.name, 300),
    location: {
      latitude: asNumber(reach.latitude),
      longitude: asNumber(reach.longitude),
    },
    route: {
      upstream: normalizeRoute(route?.upstream),
      downstream: normalizeRoute(route?.downstream),
    },
  };
};

const normalizeReachSeries = (
  payload: JsonRecord,
  containerKey: "analysisAssimilation" | "shortRange",
  series: "analysis_assimilation" | "short_range",
) => {
  const container = payload[containerKey];
  if (!isRecord(container)) {
    throw new AdapterError("NOAA reach response omitted the requested model series.", "NOAA_CONTRACT_MISMATCH");
  }
  const variants = Object.entries(container).sort(([left], [right]) => left.localeCompare(right));
  if (variants.length === 0) {
    return {
      records: [{
        kind: "nwm-streamflow-series",
        sourceRole: series === "analysis_assimilation" ? "NWM_MODELED_ANALYSIS_GUIDANCE" : "NWM_MODELED_FORECAST_GUIDANCE",
        series,
        variant: null,
        available: false,
        referenceTime: null,
        units: null,
        points: [],
      }],
      partial: false,
      truncated: false,
    };
  }

  let partial = false;
  let truncated = false;
  const records = variants.map(([variant, rawSeries]) => {
    if (!isRecord(rawSeries) || !Array.isArray(rawSeries.data)) {
      throw new AdapterError("NOAA model series did not match the expected contract.", "NOAA_CONTRACT_MISMATCH");
    }
    const normalized = rawSeries.data.flatMap((entry) => {
      if (!isRecord(entry)) return [];
      const validTime = asTimestamp(entry.validTime);
      if (!validTime) return [];
      return [{ validTime, flow: asNumber(entry.flow) }];
    }).sort((left, right) => Date.parse(left.validTime) - Date.parse(right.validTime));
    if (normalized.length !== rawSeries.data.length) partial = true;
    const seriesTruncated = normalized.length > MAX_REACH_POINTS;
    if (seriesTruncated) {
      partial = true;
      truncated = true;
    }
    return {
      kind: "nwm-streamflow-series",
      sourceRole: series === "analysis_assimilation" ? "NWM_MODELED_ANALYSIS_GUIDANCE" : "NWM_MODELED_FORECAST_GUIDANCE",
      series,
      variant: variant.slice(0, 100),
      available: true,
      referenceTime: asTimestamp(rawSeries.referenceTime),
      units: asString(rawSeries.units, 32),
      points: seriesTruncated
        ? series === "analysis_assimilation"
          ? normalized.slice(-MAX_REACH_POINTS)
          : normalized.slice(0, MAX_REACH_POINTS)
        : normalized,
    };
  });
  return { records, partial, truncated };
};

const networkLinks: SourceLink[] = [
  { rel: "upstream", title: "NOAA NWPS Kansas gauge query", href: KANSAS_GAUGES_URL },
  { rel: "documentation", title: "NOAA NWPS API documentation", href: NWPS_DOCS_URL },
  { rel: "service", title: "NOAA Office of Water Prediction API information", href: NWPS_API_INFO_URL },
];

const gaugeLinks = (lid: string): SourceLink[] => [
  { rel: "upstream", title: "NOAA NWPS gauge metadata", href: `${NWPS_BASE}/gauges/${lid}` },
  { rel: "upstream", title: "NOAA NWPS observed stage/flow", href: `${NWPS_BASE}/gauges/${lid}/stageflow/observed` },
  { rel: "upstream", title: "NOAA NWPS forecast stage/flow", href: `${NWPS_BASE}/gauges/${lid}/stageflow/forecast` },
  { rel: "documentation", title: "NOAA NWPS API documentation", href: NWPS_DOCS_URL },
  { rel: "service", title: "NOAA NWPS gauge page", href: `https://water.noaa.gov/gauges/${lid}` },
];

const reachLinks = (reachId: string): SourceLink[] => [
  { rel: "upstream", title: "NOAA NWM analysis and assimilation streamflow", href: `${NWPS_BASE}/reaches/${reachId}/streamflow?series=analysis_assimilation` },
  { rel: "upstream", title: "NOAA NWM short-range streamflow guidance", href: `${NWPS_BASE}/reaches/${reachId}/streamflow?series=short_range` },
  { rel: "documentation", title: "NOAA NWPS API documentation", href: NWPS_DOCS_URL },
  { rel: "service", title: "NOAA National Water Model information", href: NWM_INFO_URL },
];

const responseHeaders = (maxAgeSeconds: number) => ({
  "Cache-Control": `public, max-age=${maxAgeSeconds}`,
  "X-Content-Type-Options": "nosniff",
});

const result = (
  mode: HydrologyMode,
  retrievedAt: string,
  records: unknown[],
  partial: boolean,
  truncated: boolean,
  limitation: string,
  sourceLinks: SourceLink[],
) => ({
  mode,
  state: partial || truncated ? "partial" : records.length === 0 ? "empty" : "ready",
  retrievedAt,
  recordCount: records.length,
  records,
  partial: partial || truncated,
  truncated,
  limitation,
  sourceLinks,
});

const networkResponse = async (retrievedAt: string) => {
  const payload = await fetchFixedJson(KANSAS_GAUGES_URL, MAX_NETWORK_BYTES);
  if (!Array.isArray(payload.gauges)) {
    throw new AdapterError("NOAA gauge network response omitted its gauges array.", "NOAA_CONTRACT_MISMATCH");
  }
  const kansasCandidates = payload.gauges.filter((candidate) => recordAt(candidate, "state")?.abbreviation === "KS");
  const normalized = kansasCandidates
    .map(normalizeNetworkGauge)
    .filter((record) => record !== null)
    .sort((left, right) => left.lid.localeCompare(right.lid));
  const truncated = normalized.length > MAX_NETWORK_RECORDS;
  const records = normalized.slice(0, MAX_NETWORK_RECORDS);
  const partial = records.length < kansasCandidates.length;
  return result(
    "network",
    retrievedAt,
    records,
    partial,
    truncated,
    "Latest operational NWPS gauge-status snapshot for the fixed Kansas bounding box, filtered to state=KS. Each observation and forecast keeps its own valid time and units. Missing, not-current, or out-of-service values remain null/status-coded; no values are interpolated. This endpoint is not a historical archive, flood warning, or emergency service.",
    networkLinks,
  );
};

const gaugeResponse = async (lid: string, retrievedAt: string) => {
  const links = gaugeLinks(lid);
  const [metadataPayload, observedPayload, forecastPayload] = await Promise.all([
    fetchFixedJson(links[0].href, MAX_METADATA_BYTES),
    fetchFixedJson(links[1].href, MAX_STAGEFLOW_BYTES),
    fetchFixedJson(links[2].href, MAX_STAGEFLOW_BYTES),
  ]);
  const metadata = normalizeGaugeMetadata(metadataPayload);
  const observed = normalizeStageFlow(observedPayload, "observed");
  const forecast = normalizeStageFlow(forecastPayload, "forecast");
  return result(
    "gauge",
    retrievedAt,
    [metadata.record, observed.record, forecast.record],
    metadata.partial || observed.partial || forecast.partial,
    metadata.truncated || observed.truncated || forecast.truncated,
    "Operational NWPS gauge metadata, observations, and official NWS forecast series for one validated gauge. NOAA states that this API is not a historical archive except for crest and low-water history; any rolling observed series is availability-limited and may be revised. Datum flags, product names, units, issue times, generated times, and valid times must remain visible. No temporal interpolation is performed.",
    links,
  );
};

const reachResponse = async (reachId: string, retrievedAt: string) => {
  const links = reachLinks(reachId);
  const [analysisPayload, shortRangePayload] = await Promise.all([
    fetchFixedJson(links[0].href, MAX_REACH_BYTES),
    fetchFixedJson(links[1].href, MAX_REACH_BYTES),
  ]);
  const reach = normalizeReachHeader(analysisPayload, reachId);
  normalizeReachHeader(shortRangePayload, reachId);
  const analysis = normalizeReachSeries(analysisPayload, "analysisAssimilation", "analysis_assimilation");
  const shortRange = normalizeReachSeries(shortRangePayload, "shortRange", "short_range");
  return result(
    "reach",
    retrievedAt,
    [reach, ...analysis.records, ...shortRange.records],
    analysis.partial || shortRange.partial,
    analysis.truncated || shortRange.truncated,
    "National Water Model analysis/assimilation and short-range streamflow for one validated reach. These are modeled hydrologic guidance: analysis/assimilation is not a gauge observation, and short-range NWM output is not an official River Forecast Center forecast. The service is not a durable historical archive; exact reference and valid times are preserved and no values are interpolated.",
    links,
  );
};

const errorPayload = (
  mode: HydrologyMode | null,
  retrievedAt: string,
  code: string,
  message: string,
  sourceLinks: SourceLink[],
) => ({
  mode,
  state: "error",
  retrievedAt,
  recordCount: 0,
  records: [],
  partial: false,
  truncated: false,
  limitation: "No synthetic, cached-stale, cross-source, or untimed fallback was used.",
  sourceLinks,
  error: { code, message },
});

export async function GET(request: NextRequest) {
  const retrievedAt = new Date().toISOString();
  const requestedMode = request.nextUrl.searchParams.get("mode") ?? "network";
  const mode: HydrologyMode | null = requestedMode === "network" || requestedMode === "gauge" || requestedMode === "reach"
    ? requestedMode
    : null;

  if (!mode) {
    return NextResponse.json(
      errorPayload(null, retrievedAt, "INVALID_MODE", "mode must be network, gauge, or reach.", networkLinks.slice(1)),
      { status: 400, headers: responseHeaders(0) },
    );
  }

  const lid = request.nextUrl.searchParams.get("lid");
  const reachId = request.nextUrl.searchParams.get("reach");
  if (mode === "gauge" && (!lid || !LID_PATTERN.test(lid))) {
    return NextResponse.json(
      errorPayload(mode, retrievedAt, "INVALID_LID", "gauge mode requires a 3-8 character uppercase alphanumeric lid.", networkLinks.slice(1)),
      { status: 400, headers: responseHeaders(0) },
    );
  }
  if (mode === "reach" && (!reachId || !REACH_PATTERN.test(reachId))) {
    return NextResponse.json(
      errorPayload(mode, retrievedAt, "INVALID_REACH", "reach mode requires a 1-12 digit reach identifier.", networkLinks.slice(1)),
      { status: 400, headers: responseHeaders(0) },
    );
  }

  const sourceLinks = mode === "gauge" && lid
    ? gaugeLinks(lid)
    : mode === "reach" && reachId
      ? reachLinks(reachId)
      : networkLinks;
  try {
    const payload = mode === "network"
      ? await networkResponse(retrievedAt)
      : mode === "gauge"
        ? await gaugeResponse(lid!, retrievedAt)
        : await reachResponse(reachId!, retrievedAt);
    return NextResponse.json(payload, {
      status: 200,
      headers: responseHeaders(mode === "reach" ? 300 : 120),
    });
  } catch (error) {
    const adapterError = error instanceof AdapterError
      ? error
      : new AdapterError("NOAA hydrology request failed.", "NOAA_UNAVAILABLE");
    return NextResponse.json(
      errorPayload(
        mode,
        retrievedAt,
        adapterError.code,
        "NOAA hydrology data are temporarily unavailable for this bounded request.",
        sourceLinks,
      ),
      {
        status: adapterError.timeout ? 504 : 502,
        headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" },
      },
    );
  }
}
