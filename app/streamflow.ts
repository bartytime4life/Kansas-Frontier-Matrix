import type { Feature, FeatureCollection, Point } from "geojson";

export const STREAMFLOW_BUNDLE_FORMAT = "kfm-usgs-streamflow-v1";
export const STREAMFLOW_FEED = "usgs-streamflow";
export const STREAMFLOW_PARAMETER_CODE = "00060";
export const STREAMFLOW_MAX_DISPLAY_FRAMES = 96;
export const STREAMFLOW_MAX_STATIONS = 2_000;
export const STREAMFLOW_MAX_OBSERVATIONS = 100_000;

export type StreamflowQueryMode = "latest" | "recent-series" | "historical-series";
export type StreamflowBundleState = "ready" | "empty" | "partial";
export type StreamflowTrend = "rising" | "falling" | "steady" | "unknown" | "missing";

export type StreamflowStation = Readonly<{
  stationId: string;
  name: string;
  longitude: number;
  latitude: number;
  agencyCode: "USGS";
  siteTypeCode: string | null;
}>;

export type StreamflowObservation = Readonly<{
  stationId: string;
  observedAt: string;
  value: number | null;
  unit: string;
  parameterCode: typeof STREAMFLOW_PARAMETER_CODE;
  statisticId: string | null;
  approvalStatus: string | null;
  qualifiers: readonly string[];
  lastModified: string | null;
}>;

export type StreamflowBundle = Readonly<{
  format: typeof STREAMFLOW_BUNDLE_FORMAT;
  feed: typeof STREAMFLOW_FEED;
  state: StreamflowBundleState;
  retrievedAt: string;
  query: Readonly<{
    mode: StreamflowQueryMode;
    start: string;
    end: string;
    parameterCode: typeof STREAMFLOW_PARAMETER_CODE;
  }>;
  stations: readonly StreamflowStation[];
  observations: readonly StreamflowObservation[];
  source: string;
  limitation: string;
  truncated: boolean;
  interpolation: false;
  evidenceRole: "EXTERNAL_CONTEXT_ONLY";
}>;

type NumericInput = number | string;

export type StreamflowBundlePayload = Readonly<{
  format: typeof STREAMFLOW_BUNDLE_FORMAT;
  feed: typeof STREAMFLOW_FEED;
  state: StreamflowBundleState;
  retrievedAt: string;
  query: Readonly<{
    mode: StreamflowQueryMode;
    start: string;
    end: string;
    parameterCode: typeof STREAMFLOW_PARAMETER_CODE;
  }>;
  stations: readonly Readonly<{
    stationId: string;
    name: string;
    longitude: NumericInput;
    latitude: NumericInput;
    agencyCode: "USGS";
    siteTypeCode: string | null;
  }>[];
  observations: readonly Readonly<{
    stationId: string;
    observedAt: string;
    value: NumericInput | null;
    unit: string;
    parameterCode: typeof STREAMFLOW_PARAMETER_CODE;
    statisticId: string | null;
    approvalStatus: string | null;
    qualifiers: readonly string[];
    lastModified: string | null;
  }>[];
  source: string;
  limitation: string;
  truncated: boolean;
  interpolation: false;
  evidenceRole: "EXTERNAL_CONTEXT_ONLY";
}>;

export type StreamflowFrameProperties = Readonly<{
  featureId: string;
  stationId: string;
  monitoringLocationId: string;
  name: string;
  stationName: string;
  frameCursor: string;
  observedAt: string | null;
  value: number | null;
  visualMagnitude: number;
  displayValue: string;
  unit: string | null;
  parameterCode: typeof STREAMFLOW_PARAMETER_CODE;
  statisticId: string | null;
  approvalStatus: string | null;
  qualifiers: readonly string[];
  lastModified: string | null;
  previousObservedAt: string | null;
  previousValue: number | null;
  changePercent: number | null;
  trend: StreamflowTrend;
  ageMinutes: number | null;
  missing: boolean;
  interpolation: false;
  evidenceRole: "EXTERNAL_CONTEXT_ONLY";
}>;

export type StreamflowFrame = FeatureCollection<Point, StreamflowFrameProperties>;

export type HydrographSegment = Readonly<{
  path: string;
  startTime: string;
  endTime: string;
  pointCount: number;
}>;

export type HydrographOptions = Readonly<{
  width: number;
  height: number;
  gapMinutes: number;
  padding?: number;
}>;

const record = (value: unknown): value is Record<string, unknown> => (
  Boolean(value) && typeof value === "object" && !Array.isArray(value)
);

const boundedText = (value: unknown, maximum: number, allowEmpty = false): value is string => (
  typeof value === "string"
  && value.length <= maximum
  && (allowEmpty || value.trim().length > 0)
);

const numericInput = (value: unknown): value is NumericInput => {
  if (typeof value === "number") return Number.isFinite(value);
  if (typeof value !== "string" || value.trim() === "") return false;
  return Number.isFinite(Number(value));
};

const normalizedNumber = (value: NumericInput) => typeof value === "number" ? value : Number(value.trim());

/** Accepts the canonical OGC identifier and the bare NWIS site number. */
export const normalizeUsgsStationId = (value: string): string | null => {
  const match = value.trim().toUpperCase().match(/^(?:USGS-)?(\d{8,15})$/);
  return match ? `USGS-${match[1]}` : null;
};

export const isUsgsStationId = (value: unknown): value is string => (
  typeof value === "string" && normalizeUsgsStationId(value) !== null
);

/** Normalizes only explicit UTC timestamps and rejects calendar rollover. */
export const normalizeStreamflowIsoTime = (value: string): string | null => {
  const match = value.trim().match(/^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})(?:\.(\d{1,3}))?Z$/);
  if (!match) return null;
  const canonical = `${match[1]}.${(match[2] ?? "").padEnd(3, "0")}Z`;
  const milliseconds = Date.parse(canonical);
  if (!Number.isFinite(milliseconds)) return null;
  return new Date(milliseconds).toISOString() === canonical ? canonical : null;
};

export const isStreamflowIsoTime = (value: unknown): value is string => (
  typeof value === "string" && normalizeStreamflowIsoTime(value) !== null
);

const nullableBoundedText = (value: unknown, maximum: number) => (
  value === null || boundedText(value, maximum)
);

const validHttpsUrl = (value: unknown) => {
  if (!boundedText(value, 2_000)) return false;
  try {
    return new URL(value).protocol === "https:";
  } catch {
    return false;
  }
};

/** Strictly checks the serialized contract accepted from the Site's fixed backend adapter. */
export const isStreamflowBundlePayload = (value: unknown): value is StreamflowBundlePayload => {
  if (!record(value)
    || value.format !== STREAMFLOW_BUNDLE_FORMAT
    || value.feed !== STREAMFLOW_FEED
    || !["ready", "empty", "partial"].includes(String(value.state))
    || !isStreamflowIsoTime(value.retrievedAt)
    || !record(value.query)
    || !["latest", "recent-series", "historical-series"].includes(String(value.query.mode))
    || !isStreamflowIsoTime(value.query.start)
    || !isStreamflowIsoTime(value.query.end)
    || value.query.parameterCode !== STREAMFLOW_PARAMETER_CODE
    || Date.parse(value.query.start as string) > Date.parse(value.query.end as string)
    || !Array.isArray(value.stations)
    || value.stations.length > STREAMFLOW_MAX_STATIONS
    || !Array.isArray(value.observations)
    || value.observations.length > STREAMFLOW_MAX_OBSERVATIONS
    || !validHttpsUrl(value.source)
    || !boundedText(value.limitation, 4_000)
    || typeof value.truncated !== "boolean"
    || value.interpolation !== false
    || value.evidenceRole !== "EXTERNAL_CONTEXT_ONLY") return false;

  const stationIds = new Set<string>();
  for (const station of value.stations) {
    if (!record(station)
      || !isUsgsStationId(station.stationId)
      || !boundedText(station.name, 240)
      || !numericInput(station.longitude)
      || !numericInput(station.latitude)
      || station.agencyCode !== "USGS"
      || !nullableBoundedText(station.siteTypeCode, 40)) return false;
    const longitude = normalizedNumber(station.longitude as NumericInput);
    const latitude = normalizedNumber(station.latitude as NumericInput);
    const stationId = normalizeUsgsStationId(station.stationId as string)!;
    if (longitude < -180 || longitude > 180 || latitude < -90 || latitude > 90 || stationIds.has(stationId)) return false;
    stationIds.add(stationId);
  }

  for (const observation of value.observations) {
    if (!record(observation)
      || !isUsgsStationId(observation.stationId)
      || !stationIds.has(normalizeUsgsStationId(observation.stationId as string)!)
      || !isStreamflowIsoTime(observation.observedAt)
      || observation.value !== null && !numericInput(observation.value)
      || !boundedText(observation.unit, 64)
      || observation.parameterCode !== STREAMFLOW_PARAMETER_CODE
      || !nullableBoundedText(observation.statisticId, 80)
      || !nullableBoundedText(observation.approvalStatus, 80)
      || !Array.isArray(observation.qualifiers)
      || observation.qualifiers.length > 16
      || !observation.qualifiers.every((qualifier) => boundedText(qualifier, 80))
      || observation.lastModified !== null && !isStreamflowIsoTime(observation.lastModified)) return false;
  }

  return !(value.state === "empty" && value.observations.length > 0)
    && !(value.state === "ready" && value.observations.length === 0);
};

const revisionTime = (observation: Pick<StreamflowObservation, "lastModified">) => (
  observation.lastModified ? Date.parse(observation.lastModified) : Number.NEGATIVE_INFINITY
);

/** Keeps one revision per station and observation time, preferring the later explicit revision time. */
export const dedupeStreamflowObservations = (
  observations: readonly StreamflowObservation[],
): readonly StreamflowObservation[] => {
  const deduped = new Map<string, StreamflowObservation>();
  for (const observation of observations) {
    const key = `${observation.stationId}\u0000${observation.observedAt}`;
    const current = deduped.get(key);
    if (!current || revisionTime(observation) > revisionTime(current)) deduped.set(key, observation);
  }
  return Object.freeze([...deduped.values()].sort((left, right) => (
    Date.parse(left.observedAt) - Date.parse(right.observedAt)
    || left.stationId.localeCompare(right.stationId)
  )));
};

/** Parses and freezes the backend payload into canonical IDs, ISO timestamps, and numeric values. */
export const parseStreamflowBundle = (value: unknown): StreamflowBundle => {
  if (!isStreamflowBundlePayload(value)) throw new Error("The streamflow adapter returned an invalid bundle contract.");

  const stations = Object.freeze(value.stations.map((station) => Object.freeze({
    stationId: normalizeUsgsStationId(station.stationId)!,
    name: station.name.trim(),
    longitude: normalizedNumber(station.longitude),
    latitude: normalizedNumber(station.latitude),
    agencyCode: "USGS" as const,
    siteTypeCode: station.siteTypeCode?.trim() ?? null,
  })).sort((left, right) => left.stationId.localeCompare(right.stationId)));

  const observations = dedupeStreamflowObservations(value.observations.map((observation) => Object.freeze({
    stationId: normalizeUsgsStationId(observation.stationId)!,
    observedAt: normalizeStreamflowIsoTime(observation.observedAt)!,
    value: observation.value === null ? null : normalizedNumber(observation.value),
    unit: observation.unit.trim(),
    parameterCode: STREAMFLOW_PARAMETER_CODE,
    statisticId: observation.statisticId?.trim() ?? null,
    approvalStatus: observation.approvalStatus?.trim() ?? null,
    qualifiers: Object.freeze(observation.qualifiers.map((qualifier) => qualifier.trim())),
    lastModified: observation.lastModified ? normalizeStreamflowIsoTime(observation.lastModified) : null,
  })));

  return Object.freeze({
    format: STREAMFLOW_BUNDLE_FORMAT,
    feed: STREAMFLOW_FEED,
    state: value.state,
    retrievedAt: normalizeStreamflowIsoTime(value.retrievedAt)!,
    query: Object.freeze({
      mode: value.query.mode,
      start: normalizeStreamflowIsoTime(value.query.start)!,
      end: normalizeStreamflowIsoTime(value.query.end)!,
      parameterCode: STREAMFLOW_PARAMETER_CODE,
    }),
    stations,
    observations,
    source: value.source,
    limitation: value.limitation.trim(),
    truncated: value.truncated,
    interpolation: false,
    evidenceRole: "EXTERNAL_CONTEXT_ONLY",
  });
};

/** Type guard for the already normalized in-memory representation. */
export const isStreamflowBundle = (value: unknown): value is StreamflowBundle => {
  if (!isStreamflowBundlePayload(value)) return false;
  return value.stations.every((station) => (
    typeof station.longitude === "number"
    && typeof station.latitude === "number"
    && normalizeUsgsStationId(station.stationId) === station.stationId
  )) && value.observations.every((observation) => (
    (observation.value === null || typeof observation.value === "number")
    && normalizeUsgsStationId(observation.stationId) === observation.stationId
    && normalizeStreamflowIsoTime(observation.observedAt) === observation.observedAt
    && (observation.lastModified === null || normalizeStreamflowIsoTime(observation.lastModified) === observation.lastModified)
  ));
};

export const stationObservations = (
  bundle: Pick<StreamflowBundle, "observations">,
  stationId: string,
): readonly StreamflowObservation[] => {
  const normalized = normalizeUsgsStationId(stationId);
  if (!normalized) throw new Error("A selected streamflow station requires a valid USGS monitoring-location ID.");
  return Object.freeze(bundle.observations
    .filter((observation) => observation.stationId === normalized)
    .sort((left, right) => Date.parse(left.observedAt) - Date.parse(right.observedAt)));
};

/** Returns a bounded sample of actual observation times; no synthetic timestamps are inserted. */
export const streamflowDisplayFrames = (
  bundle: Pick<StreamflowBundle, "observations">,
  requestedMaximum = STREAMFLOW_MAX_DISPLAY_FRAMES,
): readonly string[] => {
  const maximum = Number.isFinite(requestedMaximum)
    ? Math.max(1, Math.min(STREAMFLOW_MAX_DISPLAY_FRAMES, Math.floor(requestedMaximum)))
    : STREAMFLOW_MAX_DISPLAY_FRAMES;
  const exactFrames = [...new Set(bundle.observations.map((observation) => observation.observedAt))]
    .sort((left, right) => Date.parse(left) - Date.parse(right));
  if (exactFrames.length <= maximum) return Object.freeze(exactFrames);
  if (maximum === 1) return Object.freeze([exactFrames.at(-1)!]);
  return Object.freeze(Array.from({ length: maximum }, (_, index) => (
    exactFrames[Math.round(index * (exactFrames.length - 1) / (maximum - 1))]
  )));
};

export const buildStreamflowDisplayFrames = streamflowDisplayFrames;

const rounded = (value: number, digits = 2) => {
  const scale = 10 ** digits;
  const result = Math.round(value * scale) / scale;
  return Object.is(result, -0) ? 0 : result;
};

const trendFor = (current: number, previous: number): Exclude<StreamflowTrend, "unknown" | "missing"> => (
  current > previous ? "rising" : current < previous ? "falling" : "steady"
);

const observationAtOrBefore = (series: readonly StreamflowObservation[], cursorMilliseconds: number) => {
  let low = 0;
  let high = series.length - 1;
  let result = -1;
  while (low <= high) {
    const middle = Math.floor((low + high) / 2);
    if (Date.parse(series[middle].observedAt) <= cursorMilliseconds) {
      result = middle;
      low = middle + 1;
    } else {
      high = middle - 1;
    }
  }
  return result;
};

/** Builds one station point per known station at an exact cursor. Values are
 * held only within the caller-declared tolerance and are never interpolated. */
export const buildStreamflowFrame = (
  bundle: Pick<StreamflowBundle, "stations" | "observations">,
  cursor: string,
  toleranceMinutes: number,
): StreamflowFrame => {
  const normalizedCursor = normalizeStreamflowIsoTime(cursor);
  if (!normalizedCursor) throw new Error("A streamflow frame requires an explicit UTC ISO cursor.");
  if (!Number.isFinite(toleranceMinutes) || toleranceMinutes < 0) {
    throw new Error("A streamflow frame requires a finite, non-negative tolerance in minutes.");
  }
  const cursorMilliseconds = Date.parse(normalizedCursor);
  const toleranceMilliseconds = toleranceMinutes * 60_000;
  const seriesByStation = new Map<string, StreamflowObservation[]>();
  for (const observation of bundle.observations) {
    const series = seriesByStation.get(observation.stationId) ?? [];
    series.push(observation);
    seriesByStation.set(observation.stationId, series);
  }
  for (const series of seriesByStation.values()) {
    series.sort((left, right) => Date.parse(left.observedAt) - Date.parse(right.observedAt));
  }

  const features: Feature<Point, StreamflowFrameProperties>[] = bundle.stations.map((station) => {
    const series = seriesByStation.get(station.stationId) ?? [];
    const selectedIndex = observationAtOrBefore(series, cursorMilliseconds);
    const selected = selectedIndex >= 0 ? series[selectedIndex] : null;
    const selectedMilliseconds = selected ? Date.parse(selected.observedAt) : null;
    const ageMilliseconds = selectedMilliseconds === null ? null : cursorMilliseconds - selectedMilliseconds;
    const ageMinutes = ageMilliseconds === null ? null : rounded(ageMilliseconds / 60_000);
    const withinTolerance = selected !== null && ageMilliseconds !== null && ageMilliseconds >= 0 && ageMilliseconds <= toleranceMilliseconds;
    const missing = !withinTolerance || selected.value === null;
    const previous = selectedIndex > 0 ? series[selectedIndex - 1] : null;
    const previousGap = selected && previous ? Date.parse(selected.observedAt) - Date.parse(previous.observedAt) : null;
    const comparable = !missing
      && previous?.value !== null
      && previous?.value !== undefined
      && previousGap !== null
      && previousGap <= toleranceMilliseconds;
    const changePercent = comparable && previous!.value !== 0
      ? rounded(((selected!.value! - previous!.value!) / Math.abs(previous!.value!)) * 100)
      : comparable && selected!.value === 0
        ? 0
        : null;
    const trend: StreamflowTrend = missing
      ? "missing"
      : comparable
        ? trendFor(selected!.value!, previous!.value!)
        : "unknown";
    const value = missing ? null : selected!.value;
    const unit = selected?.unit ?? null;
    return {
      type: "Feature",
      id: station.stationId,
      geometry: { type: "Point", coordinates: [station.longitude, station.latitude] },
      properties: Object.freeze({
        featureId: `usgs-streamflow-${station.stationId.slice(5)}`,
        stationId: station.stationId,
        monitoringLocationId: station.stationId,
        name: station.name,
        stationName: station.name,
        frameCursor: normalizedCursor,
        observedAt: selected?.observedAt ?? null,
        value,
        visualMagnitude: value === null ? 0 : rounded(Math.min(5, Math.log10(Math.max(0, value) + 1)), 3),
        displayValue: value !== null && unit
          ? `${value.toLocaleString("en-US", { maximumFractionDigits: 3 })} ${unit}`
          : withinTolerance && selected?.value === null
            ? "Value not reported"
            : "No observation in tolerance",
        unit,
        parameterCode: STREAMFLOW_PARAMETER_CODE,
        statisticId: selected?.statisticId ?? null,
        approvalStatus: selected?.approvalStatus ?? null,
        qualifiers: selected?.qualifiers ?? Object.freeze([]),
        lastModified: selected?.lastModified ?? null,
        previousObservedAt: comparable ? previous!.observedAt : null,
        previousValue: comparable ? previous!.value : null,
        changePercent,
        trend,
        ageMinutes,
        missing,
        interpolation: false,
        evidenceRole: "EXTERNAL_CONTEXT_ONLY",
      }),
    };
  });

  return Object.freeze({ type: "FeatureCollection", features: Object.freeze(features) }) as StreamflowFrame;
};

const coordinateText = (value: number) => {
  const fixed = rounded(value).toFixed(2);
  return fixed === "-0.00" ? "0.00" : fixed;
};

/** Builds independent SVG path fragments. Null values and time deltas larger
 * than gapMinutes terminate a fragment instead of visually bridging missing data. */
export const buildHydrographSegments = (
  observations: readonly StreamflowObservation[],
  options: HydrographOptions,
): readonly HydrographSegment[] => {
  const padding = options.padding ?? 0;
  if (!Number.isFinite(options.width) || !Number.isFinite(options.height) || options.width <= 0 || options.height <= 0
    || !Number.isFinite(padding) || padding < 0 || padding * 2 >= options.width || padding * 2 >= options.height) {
    throw new Error("Hydrograph dimensions and padding must define a positive plotting area.");
  }
  if (!Number.isFinite(options.gapMinutes) || options.gapMinutes <= 0) {
    throw new Error("Hydrograph gapMinutes must be a positive finite duration.");
  }
  const stationIds = new Set(observations.map((observation) => observation.stationId));
  if (stationIds.size > 1) throw new Error("Hydrograph segments require observations for one selected station.");

  const series = dedupeStreamflowObservations(observations);
  const numeric = series.filter((observation) => observation.value !== null);
  if (numeric.length === 0) return Object.freeze([]);
  const timeMinimum = Date.parse(series[0].observedAt);
  const timeMaximum = Date.parse(series.at(-1)!.observedAt);
  const values = numeric.map((observation) => observation.value!);
  const valueMinimum = Math.min(...values);
  const valueMaximum = Math.max(...values);
  const plotWidth = options.width - padding * 2;
  const plotHeight = options.height - padding * 2;
  const x = (observedAt: string) => timeMaximum === timeMinimum
    ? padding + plotWidth / 2
    : padding + ((Date.parse(observedAt) - timeMinimum) / (timeMaximum - timeMinimum)) * plotWidth;
  const y = (value: number) => valueMaximum === valueMinimum
    ? padding + plotHeight / 2
    : padding + (1 - (value - valueMinimum) / (valueMaximum - valueMinimum)) * plotHeight;

  const segments: HydrographSegment[] = [];
  let current: StreamflowObservation[] = [];
  const flush = () => {
    if (current.length === 0) return;
    const path = current.map((observation, index) => (
      `${index === 0 ? "M" : "L"}${coordinateText(x(observation.observedAt))},${coordinateText(y(observation.value!))}`
    )).join(" ");
    segments.push(Object.freeze({
      path,
      startTime: current[0].observedAt,
      endTime: current.at(-1)!.observedAt,
      pointCount: current.length,
    }));
    current = [];
  };

  for (const observation of series) {
    if (observation.value === null) {
      flush();
      continue;
    }
    const previous = current.at(-1);
    if (previous && Date.parse(observation.observedAt) - Date.parse(previous.observedAt) > options.gapMinutes * 60_000) flush();
    current.push(observation);
  }
  flush();
  return Object.freeze(segments);
};
