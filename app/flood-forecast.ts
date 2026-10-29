import type { GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";
import { FLOOD_STATUS, type FloodStatus, type MapKey } from "./map-keys";

export { FLOOD_STATUS, type FloodStatus };

/**
 * NWS river flood forecasts for the River network: each NOAA NWPS gauge by
 * its flood category, and one gauge's stage hydrograph as the NWS draws it —
 * observed, then the official forecast, against the gauge's action, minor,
 * moderate and major flood stages.
 */

export type FloodCategoryId = "action" | "minor" | "moderate" | "major";

/** The NWS flood-category colours, in the order NWS hydrographs stack them. */
export const FLOOD_CATEGORIES: readonly Readonly<{ id: FloodCategoryId; name: string; stage: string; short: string; color: string }>[] = Object.freeze([
  { id: "action", name: "Action", stage: "Action stage", short: "Action", color: "#ffff00" },
  { id: "minor", name: "Minor flooding", stage: "Flood stage", short: "Flood", color: "#ff9900" },
  { id: "moderate", name: "Moderate flooding", stage: "Moderate flood stage", short: "Moderate", color: "#ff0000" },
  { id: "major", name: "Major flooding", stage: "Major flood stage", short: "Major", color: "#cc33ff" },
]);


export const FLOOD_PAGE = "https://water.noaa.gov/";
export const floodGaugePage = (lid: string) => `https://water.noaa.gov/gauges/${encodeURIComponent(lid)}`;
export const floodGaugeApiPath = (lid: string) => `/api/hydrology/noaa?mode=gauge&lid=${encodeURIComponent(lid)}`;
/** Observations arrive every 15–60 minutes and forecasts a few times a day. */
export const FLOOD_GAUGE_REFRESH_MS = 10 * 60 * 1000;
/** How much of the observed record the hydrograph shows before now. */
export const FLOOD_OBSERVED_DAYS = 7;
const DAY_MS = 86_400_000;

/** NWPS writes categories as "no_flooding", "obs_not_current" and so on; the map and dock read one form. */
export function floodStatus(raw: string | null | undefined): FloodStatus {
  const value = (raw ?? "").trim().toLowerCase().replace(/[\s-]+/g, "_");
  if (value === "major" || value === "moderate" || value === "minor" || value === "action") return value;
  if (value === "no_flooding" || value === "none" || value === "normal") return "none";
  if (value === "not_defined" || value === "flood_category_not_defined") return "not_defined";
  if (value === "low_threshold" || value === "low_water") return "low_water";
  if (value.endsWith("not_current")) return "not_current";
  if (value === "out_of_service") return "out_of_service";
  return "unknown";
}

const RANK: Readonly<Partial<Record<FloodStatus, number>>> = { major: 4, moderate: 3, minor: 2, action: 1, none: 0 };
/** Major 4 … action 1, no flooding 0; a status that says nothing about flooding ranks below. */
export const floodRank = (status: FloodStatus) => RANK[status] ?? -1;

export type FloodGaugeSummary = Readonly<{ lid: string; name: string; observed: FloodStatus; forecast: FloodStatus }>;

/** The network's gauges as the dock lists them: worst observed or forecast category first. */
export function floodGaugeSummaries(features: readonly Readonly<{ properties?: Record<string, unknown> | null }>[]): FloodGaugeSummary[] {
  return features.flatMap(feature => {
    const p = feature.properties ?? {};
    if (typeof p.lid !== "string") return [];
    return [{ lid: p.lid, name: typeof p.name === "string" ? p.name : p.lid,
      observed: floodStatus(typeof p.observedCategory === "string" ? p.observedCategory : null),
      forecast: floodStatus(typeof p.forecastCategory === "string" ? p.forecastCategory : null) }];
  });
}

const worst = (gauge: FloodGaugeSummary) => Math.max(floodRank(gauge.observed), floodRank(gauge.forecast));

export function floodGaugeList(gauges: readonly FloodGaugeSummary[]): { id: string; label: string }[] {
  return [...gauges]
    .sort((a, b) => worst(b) - worst(a) || floodRank(b.forecast) - floodRank(a.forecast) || a.name.localeCompare(b.name))
    .map(gauge => {
      const now = FLOOD_STATUS[gauge.observed].label.toLowerCase();
      const ahead = floodRank(gauge.forecast) > Math.max(0, floodRank(gauge.observed)) ? ` · forecast ${FLOOD_STATUS[gauge.forecast].label.toLowerCase()}` : "";
      return { id: gauge.lid, label: `${gauge.name} (${gauge.lid}) · ${now}${ahead}` };
    });
}

/** One line for the whole network: how many gauges flood now, sit at action stage, or are forecast to flood. */
export function floodNetworkSummary(gauges: readonly FloodGaugeSummary[]): string {
  const flooding = gauges.filter(gauge => floodRank(gauge.observed) >= 2).length;
  const action = gauges.filter(gauge => gauge.observed === "action").length;
  const ahead = gauges.filter(gauge => floodRank(gauge.observed) < 2 && floodRank(gauge.forecast) >= 2).length;
  const parts = [flooding ? `${flooding} in flood` : null, action ? `${action} near flood stage` : null, ahead ? `${ahead} forecast to flood` : null].filter(Boolean);
  const total = `${gauges.length} NWS ${gauges.length === 1 ? "gauge" : "gauges"} in Kansas`;
  return parts.length ? `${parts.join(" · ")} · ${total}` : `No Kansas gauge is above action stage or forecast to flood · ${total}`;
}

export type FloodPoint = Readonly<{ time: number; value: number }>;
export type FloodCrest = Readonly<{ time: string; value: number; oldDatum: boolean; preliminary: boolean }>;
export type FloodGauge = Readonly<{
  lid: string;
  name: string;
  usgsId: string | null;
  wfo: string | null;
  quantity: "stage" | "flow" | null;
  /** The plotted series' name and units, as NWPS gives them ("Stage", "ft"). */
  label: string;
  units: string | null;
  thresholds: Readonly<Record<FloodCategoryId, number | null>>;
  observed: readonly FloodPoint[];
  forecast: readonly FloodPoint[];
  issuedTime: string | null;
  observedStatus: FloodStatus;
  forecastStatus: FloodStatus;
  /** Highest historic crests in the plotted units, highest first. */
  crests: readonly FloodCrest[];
  retrievedAt: string;
}>;

type JsonRecord = Record<string, unknown>;
const isRecord = (value: unknown): value is JsonRecord => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const text = (value: unknown, max = 300) => typeof value === "string" && value.trim() && value.length <= max ? value.trim() : null;
const num = (value: unknown) => typeof value === "number" && Number.isFinite(value) ? value : null;
const ms = (value: unknown) => { const t = typeof value === "string" ? Date.parse(value) : Number.NaN; return Number.isFinite(t) ? t : null; };
const sameUnits = (a: string | null, b: string | null) => Boolean(a && b && a.trim().toLowerCase() === b.trim().toLowerCase());

const seriesPoints = (series: JsonRecord): FloodPoint[] => (Array.isArray(series.points) ? series.points : []).flatMap(point => {
  if (!isRecord(point)) return [];
  const time = ms(point.validTime), value = num(point.primary);
  return time === null || value === null ? [] : [{ time, value }];
}).sort((a, b) => a.time - b.time);

/**
 * One gauge from the hydrology adapter's gauge answer: its metadata, the
 * observed series and the official forecast. Thresholds and crests are kept
 * in the units of the plotted series (stage in feet at nearly every Kansas
 * gauge); when the units do not match, no flood stages are drawn.
 */
export function parseFloodGauge(value: unknown, lid: string): FloodGauge {
  if (!isRecord(value) || value.mode !== "gauge" || !Array.isArray(value.records)) throw new Error("The NOAA gauge answer was not a gauge.");
  const records: readonly unknown[] = value.records;
  const metadata = records.find(record => isRecord(record) && record.kind === "gauge-metadata");
  const series = (product: string) => records.find(record => isRecord(record) && record.kind === "stageflow-series" && record.product === product);
  const observed = series("observed"), forecast = series("forecast");
  if (!isRecord(metadata) || metadata.lid !== lid || !isRecord(observed) || !isRecord(forecast)) throw new Error("The NOAA gauge answer was incomplete.");
  const primary = (record: JsonRecord) => isRecord(record.primary) ? record.primary : {};
  const units = text(primary(observed).units, 32) ?? text(primary(forecast).units, 32);
  const label = text(primary(observed).name, 100) ?? text(primary(forecast).name, 100) ?? "Stage";
  const flood = isRecord(metadata.flood) ? metadata.flood : {};
  const quantity = sameUnits(units, text(flood.stageUnits, 32)) ? "stage" : sameUnits(units, text(flood.flowUnits, 32)) ? "flow" : null;
  const categories = isRecord(flood.categories) ? flood.categories : {};
  const threshold = (id: FloodCategoryId) => {
    const entry = categories[id];
    return quantity && isRecord(entry) ? num(entry[quantity]) : null;
  };
  const crests = (Array.isArray(flood.historicCrests) ? flood.historicCrests : []).flatMap(crest => {
    if (!isRecord(crest) || !quantity) return [];
    const time = text(crest.occurredTime, 80), crestValue = num(crest[quantity]);
    return time && crestValue !== null && ms(time) !== null ? [{ time, value: crestValue, oldDatum: crest.oldDatum === true, preliminary: Boolean(text(crest.preliminary, 32) && crest.preliminary !== "false") }] : [];
  }).sort((a, b) => b.value - a.value).slice(0, 5);
  const status = (key: "observed" | "forecast") => floodStatus(isRecord(metadata[key]) ? text((metadata[key] as JsonRecord).floodCategory, 64) : null);
  return Object.freeze({
    lid,
    name: text(metadata.name) ?? lid,
    usgsId: text(metadata.usgsId, 24),
    wfo: isRecord(metadata.wfo) ? text(metadata.wfo.abbreviation, 16) : null,
    quantity,
    label,
    units,
    thresholds: Object.freeze({ action: threshold("action"), minor: threshold("minor"), moderate: threshold("moderate"), major: threshold("major") }),
    observed: seriesPoints(observed),
    forecast: seriesPoints(forecast),
    issuedTime: text(forecast.issuedTime, 80),
    observedStatus: status("observed"),
    forecastStatus: status("forecast"),
    crests,
    retrievedAt: text(value.retrievedAt, 80) ?? new Date(0).toISOString(),
  });
}

/** The category a value falls in, by the gauge's own stages; "not_defined" when it has none. */
export function floodCategoryAt(value: number, thresholds: FloodGauge["thresholds"]): FloodStatus {
  const defined = FLOOD_CATEGORIES.filter(category => thresholds[category.id] !== null);
  if (!defined.length) return "not_defined";
  let status: FloodStatus = "none";
  for (const category of defined) if (value >= (thresholds[category.id] as number)) status = category.id;
  return status;
}

export type FloodHydrograph = Readonly<{
  start: number;
  end: number;
  now: number;
  low: number;
  high: number;
  observed: readonly FloodPoint[];
  forecast: readonly FloodPoint[];
  /** Each defined category from its stage up to the next one's, or to the top of the plot. */
  bands: readonly Readonly<{ id: FloodCategoryId; from: number; to: number; color: string; stage: string; short: string }>[];
  crest: FloodPoint | null;
  /** Central-time midnights and round stage values for the gridlines. */
  days: readonly Readonly<{ time: number; label: string }>[];
  ticks: readonly number[];
}>;

/**
 * The hydrograph's frame: the past week of observations and the whole
 * forecast, with the vertical range opened to the flood stage (or the next
 * stage above the highest value) so the distance to flooding is read off the
 * plot, as on NWS hydrographs.
 */
export function floodHydrograph(gauge: FloodGauge, now: number): FloodHydrograph | null {
  const observed = gauge.observed.filter(point => point.time >= now - FLOOD_OBSERVED_DAYS * DAY_MS && point.time <= now + DAY_MS);
  const forecast = gauge.forecast.filter(point => point.time >= (observed.at(-1)?.time ?? now - DAY_MS));
  const points = [...observed, ...forecast];
  if (points.length < 2) return null;
  const values = points.map(point => point.value);
  const highest = Math.max(...values);
  let low = Math.min(...values), high = highest;
  const stages = FLOOD_CATEGORIES.flatMap(category => gauge.thresholds[category.id] === null ? [] : [{ ...category, value: gauge.thresholds[category.id] as number }]);
  const floodStage = gauge.thresholds.minor ?? gauge.thresholds.action;
  if (floodStage !== null) high = Math.max(high, floodStage);
  const above = stages.find(stage => stage.value > high);
  // Once the water reaches flood stage, the plot opens to the next stage above it.
  if (above && floodStage !== null && highest >= floodStage) high = above.value;
  const pad = Math.max((high - low) * 0.06, 0.25);
  low -= pad; high += pad;
  const bands = stages.filter(stage => stage.value < high).map((stage, i, shown) => ({
    id: stage.id, from: Math.max(stage.value, low), to: Math.min(shown[i + 1]?.value ?? high, high), color: stage.color, stage: stage.stage, short: stage.short,
  }));
  const crest = forecast.length ? forecast.reduce((best, point) => point.value > best.value ? point : best) : null;
  const start = points[0].time, end = Math.max(points[points.length - 1].time, now);
  return Object.freeze({ start, end, now, low, high, observed, forecast, bands, crest, days: floodDayTicks(start, end), ticks: floodValueTicks(low, high) });
}

const CENTRAL = new Intl.DateTimeFormat("en-US", { timeZone: "America/Chicago", month: "short", day: "numeric", hour: "numeric", minute: "2-digit", timeZoneName: "short" });
const CENTRAL_DAY = new Intl.DateTimeFormat("en-US", { timeZone: "America/Chicago", month: "short", day: "numeric" });
const CENTRAL_YEAR = new Intl.DateTimeFormat("en-US", { timeZone: "America/Chicago", year: "numeric", month: "short", day: "numeric" });
/** Times on Kansas's Central clock, labelled CST or CDT. */
export const floodClock = (time: number) => CENTRAL.format(time);
export const floodDay = (time: number) => CENTRAL_DAY.format(time);

const amount = (value: number, units: string | null) => `${value.toLocaleString("en-US", { maximumFractionDigits: Math.abs(value) >= 100 ? 0 : 1, minimumFractionDigits: Math.abs(value) >= 100 ? 0 : 1 })}${units ? ` ${units}` : ""}`;

/** What the hydrograph says, in words: the latest observation, the forecast's crest or trend, and the record crest. */
export function floodReading(gauge: FloodGauge, now: number): string {
  const latest = gauge.observed.filter(point => point.time <= now + 60_000).at(-1) ?? null;
  const stage = gauge.thresholds.minor;
  const parts: string[] = [];
  if (latest) {
    const status = gauge.quantity ? floodCategoryAt(latest.value, gauge.thresholds) : gauge.observedStatus;
    parts.push(`Observed ${amount(latest.value, gauge.units)} at ${floodClock(latest.time)} · ${FLOOD_STATUS[status].label.toLowerCase()}`);
  } else parts.push("No recent observation");
  const ahead = gauge.forecast.filter(point => point.time > (latest?.time ?? now));
  if (!ahead.length) parts.push("no NWS forecast is issued for this gauge");
  else {
    const crest = ahead.reduce((best, point) => point.value > best.value ? point : best);
    const status = gauge.quantity ? floodCategoryAt(crest.value, gauge.thresholds) : gauge.forecastStatus;
    const issued = gauge.issuedTime && ms(gauge.issuedTime) !== null ? ` (issued ${floodClock(ms(gauge.issuedTime) as number)})` : "";
    if (latest && crest.value <= latest.value + 0.05) {
      const last = ahead[ahead.length - 1];
      parts.push(`NWS forecast: ${last.value < latest.value - 0.05 ? "falling" : "steady"} to ${amount(last.value, gauge.units)} by ${floodClock(last.time)}${issued}`);
    } else parts.push(`NWS forecast crest ${amount(crest.value, gauge.units)} at ${floodClock(crest.time)} · ${FLOOD_STATUS[status].label.toLowerCase()}${issued}`);
  }
  if (stage !== null && gauge.quantity === "stage") parts.push(`flood stage ${amount(stage, gauge.units)}`);
  const record = gauge.crests[0];
  if (record) parts.push(`record crest ${amount(record.value, gauge.units)} on ${CENTRAL_YEAR.format(Date.parse(record.time))}${record.oldDatum ? " (old datum)" : ""}`);
  return parts.join(" · ");
}

/** The key for the River network while the flood view is on: the NWS category colours on the gauges. */
export function floodKey(): MapKey {
  return Object.freeze({
    id: "nws-flood-categories",
    title: "NWS flood category · at the gauge now",
    items: Object.freeze([
      ...(["major", "moderate", "minor", "action", "none", "not_defined", "not_current"] as const).map(status => Object.freeze({ label: FLOOD_STATUS[status].label, color: FLOOD_STATUS[status].color, shape: "dot" as const })),
      Object.freeze({ label: "Official NWS forecast issued", color: "#e7d9ff", shape: "ring" as const }),
    ]),
    note: "NOAA National Water Prediction Service gauge status: the latest observation against each gauge's own flood stages. Not a flood warning; warnings come from the National Weather Service.",
  });
}

export const FLOOD_SELECTED_SOURCE_ID = "kfm-flood-gauge-selected";
export const FLOOD_SELECTED_LAYER_ID = "kfm-flood-gauge-selected-ring";

/** A ring on the gauge whose hydrograph the dock shows; removed with the selection. */
export function syncFloodSelection(map: MapLibreMap, point: readonly [number, number] | null) {
  if (!point) {
    if (map.getLayer(FLOOD_SELECTED_LAYER_ID)) map.removeLayer(FLOOD_SELECTED_LAYER_ID);
    if (map.getSource(FLOOD_SELECTED_SOURCE_ID)) map.removeSource(FLOOD_SELECTED_SOURCE_ID);
    return;
  }
  const data: GeoJSON.FeatureCollection = { type: "FeatureCollection", features: [{ type: "Feature", properties: {}, geometry: { type: "Point", coordinates: [point[0], point[1]] } }] };
  const source = map.getSource(FLOOD_SELECTED_SOURCE_ID) as GeoJSONSource | undefined;
  if (source) source.setData(data);
  else map.addSource(FLOOD_SELECTED_SOURCE_ID, { type: "geojson", data });
  if (!map.getLayer(FLOOD_SELECTED_LAYER_ID)) map.addLayer({ id: FLOOD_SELECTED_LAYER_ID, type: "circle", source: FLOOD_SELECTED_SOURCE_ID, paint: {
    "circle-color": "rgba(0,0,0,0)", "circle-radius": ["interpolate", ["linear"], ["zoom"], 4, 8, 10, 13, 14, 16], "circle-stroke-color": "#ffffff", "circle-stroke-width": 2.2,
  } });
}

/** Midnights on Kansas's Central clock between two times, for the hydrograph's day ticks. */
export function floodDayTicks(start: number, end: number): { time: number; label: string }[] {
  const ticks: { time: number; label: string }[] = [];
  const hour = 3_600_000;
  let previous = floodDay(start);
  for (let t = Math.ceil(start / hour) * hour; t <= end; t += hour) {
    const day = floodDay(t);
    if (day !== previous) ticks.push({ time: t, label: day });
    previous = day;
  }
  return ticks;
}

/** Stage gridlines at a round step (1, 2 or 5 times a power of ten), three to six across the range. */
export function floodValueTicks(low: number, high: number): number[] {
  const raw = (high - low) / 5;
  const power = 10 ** Math.floor(Math.log10(Math.max(raw, 1e-6)));
  const step = [1, 2, 5, 10].map(m => m * power).find(s => s >= raw) ?? 10 * power;
  const ticks: number[] = [];
  for (let k = Math.ceil(low / step); k <= Math.floor(high / step); k++) ticks.push(Number((k * step).toPrecision(12)));
  return ticks;
}
