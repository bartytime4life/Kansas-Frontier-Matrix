import type { FeatureCollection, Point } from "geojson";
import type { GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";
import type { MapKey } from "./map-keys";

/**
 * Measured depth to water at the Kansas Geological Survey's monitoring wells:
 * each well's discrete measurements (USGS parameter 72019, feet below land
 * surface) from the USGS Water Data field-measurements collection, where KGS
 * and USGS measurements of these wells are kept. Most are the annual winter
 * measurements taken while irrigation pumps are off.
 */

export const USGS_FIELD_MEASUREMENTS = "https://api.waterdata.usgs.gov/ogcapi/v1/collections/field-measurements/items";
export const WELL_DEPTH_PARAMETER = "72019";
export const WELL_LEVELS_PAGE_SIZE = 1000;
export const WELL_LEVELS_MAX_PAGES = 5;
/** The static snapshot of the 2026 KGS monitoring network the map already draws. */
export const WELLS_SNAPSHOT_PATH = "/data/groundwater/kgs-monitoring-wells.geojson";

/** A USGS site number for a well: 15 digits (latitude, longitude and a sequence number). */
export const isWellSite = (value: unknown): value is string => typeof value === "string" && /^\d{15}$/.test(value);
export const wellLevelsApiPath = (site: string) => `/api/well-levels?site=${site}`;
export const wellUsgsPage = (site: string) => `https://waterdata.usgs.gov/monitoring-location/USGS-${site}/`;
export const wellKgsPage = (site: string) => `https://geohydro.kgs.ku.edu/geohydro/wizard/wizardwelldetail.cfm?usgs_id=${site}`;

export function wellLevelsProviderUrl(site: string): string {
  const url = new URL(USGS_FIELD_MEASUREMENTS);
  for (const [key, value] of Object.entries({ f: "json", monitoring_location_id: `USGS-${site}`, parameter_code: WELL_DEPTH_PARAMETER, limit: String(WELL_LEVELS_PAGE_SIZE), skipGeometry: "true" })) url.searchParams.set(key, value);
  return url.toString();
}

/** The next page of an answer, only if it is the same collection on the same host. */
export function nextPageUrl(value: unknown): string | null {
  const links = isRow(value) && Array.isArray(value.links) ? value.links : [];
  const href = links.find(link => isRow(link) && link.rel === "next" && typeof link.href === "string")?.href;
  if (typeof href !== "string") return null;
  try {
    const next = new URL(href), base = new URL(USGS_FIELD_MEASUREMENTS);
    return next.origin === base.origin && next.pathname === base.pathname ? next.toString() : null;
  } catch { return null; }
}

/**
 * One measurement. `date` is the provider's date and `precision` how much of it
 * is known: USGS writes 01 placeholders for an unknown month or day and gives
 * null `month` or `day` fields. A measurement known only to the month or year
 * is placed at the middle of that period (`time`) for plotting and trends, and
 * `span` holds the whole period it could fall in.
 */
export type WellMeasurement = Readonly<{ date: string; precision: "day" | "month" | "year"; time: number; span: readonly [number, number] | null; depth: number; provisional: boolean }>;
export type WellLevels = Readonly<{ site: string; retrievedAt: string; source: string; measurements: readonly WellMeasurement[]; truncated: boolean }>;

type Row = Record<string, unknown>;
const isRow = (value: unknown): value is Row => Boolean(value) && typeof value === "object" && !Array.isArray(value);

/** The features of one page of the collection. */
export function pageFeatures(value: unknown): unknown[] {
  if (!isRow(value) || !Array.isArray(value.features)) throw new Error("Not a USGS field-measurements answer.");
  return value.features;
}

/**
 * Depth-to-water measurements in feet, oldest first, one per date and depth.
 * A measurement without a value (a dry, obstructed or pumping well) is left
 * out, not read as zero; so is any other parameter or unit.
 */
export function parseWellLevels(features: readonly unknown[], site: string, retrievedAt: string, source: string, truncated = false): WellLevels {
  const seen = new Set<string>();
  const measurements: WellMeasurement[] = [];
  for (const feature of features) {
    const p = isRow(feature) && isRow(feature.properties) ? feature.properties : null;
    if (!p) continue;
    if (p.parameter_code !== undefined && p.parameter_code !== WELL_DEPTH_PARAMETER) continue;
    if (p.unit_of_measure !== undefined && !/^(ft|feet)$/i.test(String(p.unit_of_measure))) continue;
    const depth = typeof p.value === "number" ? p.value : typeof p.value === "string" && p.value.trim() !== "" ? Number(p.value) : Number.NaN;
    const time = typeof p.time === "string" ? Date.parse(p.time) : Number.NaN;
    // Negative depths are water above the land surface (a flowing well); deeper than 2,000 ft is not a High Plains water level.
    if (!Number.isFinite(depth) || depth < -100 || depth > 2000 || !Number.isFinite(time)) continue;
    const date = new Date(time).toISOString().slice(0, 10);
    const precision = p.month === null ? "year" as const : p.day === null ? "month" as const : "day" as const;
    const key = `${date}|${precision}|${depth}`;
    if (seen.has(key)) continue;
    seen.add(key);
    const y = Number(date.slice(0, 4)), mo = Number(date.slice(5, 7)) - 1;
    const span = precision === "year" ? [Date.UTC(y, 0, 1), Date.UTC(y + 1, 0, 1)] as const : precision === "month" ? [Date.UTC(y, mo, 1), Date.UTC(y, mo + 1, 1)] as const : null;
    measurements.push(Object.freeze({ date, precision, time: span ? (span[0] + span[1]) / 2 : time, span, depth,
      provisional: typeof p.approval_status === "string" && /provisional/i.test(p.approval_status) }));
  }
  measurements.sort((a, b) => a.time - b.time);
  return Object.freeze({ site, retrievedAt, source, measurements: Object.freeze(measurements), truncated });
}

export function validWellLevels(value: unknown, site: string): value is WellLevels {
  return isRow(value) && value.site === site && Array.isArray(value.measurements)
    && value.measurements.every(m => isRow(m) && typeof m.date === "string" && typeof m.time === "number" && typeof m.depth === "number");
}

const YEAR_MS = 365.25 * 24 * 60 * 60 * 1000;
/** Least-squares slope of depth on time, in feet per year: positive means the water level is falling. */
export function depthTrend(measurements: readonly WellMeasurement[]): number | null {
  if (measurements.length < 3) return null;
  const xs = measurements.map(m => m.time / YEAR_MS), ys = measurements.map(m => m.depth);
  const mx = xs.reduce((a, b) => a + b, 0) / xs.length, my = ys.reduce((a, b) => a + b, 0) / ys.length;
  const sxx = xs.reduce((a, x) => a + (x - mx) ** 2, 0);
  if (xs[xs.length - 1] - xs[0] < 3 || sxx === 0) return null;
  return xs.reduce((a, x, i) => a + (x - mx) * (ys[i] - my), 0) / sxx;
}
/** The record's last ten years (from the calendar year ten before the latest), if they hold at least three measurements over five years or more. */
export function recentMeasurements(measurements: readonly WellMeasurement[]): WellMeasurement[] | null {
  const last = measurements[measurements.length - 1];
  if (!last) return null;
  const from = new Date(last.time).getUTCFullYear() - 10;
  const recent = measurements.filter(m => new Date(m.time).getUTCFullYear() >= from);
  return recent.length >= 3 && last.time - recent[0].time >= 5 * YEAR_MS ? recent : null;
}

const DATE = new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: "short", day: "numeric", year: "numeric" });
const MONTH = new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: "short", year: "numeric" });
/** A measurement's date as precisely as the provider knows it: "Jan 10, 1966", "Jan 1966" or "1966". */
export const measurementDate = (m: WellMeasurement) => {
  const at = Date.parse(`${m.date}T00:00:00Z`);
  return m.precision === "year" ? m.date.slice(0, 4) : m.precision === "month" ? MONTH.format(at) : DATE.format(at);
};
const year = (m: WellMeasurement) => Number(m.date.slice(0, 4));
const rate = (slope: number) => Math.abs(slope) < 0.005 ? "level" : `${slope > 0 ? "falling" : "rising"} ${Math.abs(slope).toFixed(2)} ft/yr`;

/** The picked well's line: the latest depth, the change over the record, and the trend over it and over the last ten years. */
export function wellReading(levels: WellLevels): string {
  const m = levels.measurements;
  if (!m.length) return "USGS holds no depth-to-water measurements for this well; open its KGS record for what is known.";
  const last = m[m.length - 1], first = m[0];
  const latest = `Depth to water ${last.depth.toFixed(1)} ft ${last.precision === "day" ? "on" : "in"} ${measurementDate(last)}${last.provisional ? " (provisional)" : ""}`;
  if (m.length === 1) return `${latest} · the only measurement on record`;
  const change = last.depth - first.depth;
  const moved = Math.abs(change) < 0.05 ? `no net change since ${year(first)}` : `water level ${change > 0 ? "down" : "up"} ${Math.abs(change).toFixed(1)} ft since ${year(first)}`;
  // The last ten years are given apart only when the record reaches further back.
  const trend = depthTrend(m), recent = recentMeasurements(m), recentTrend = recent && recent.length < m.length ? depthTrend(recent) : null;
  const vague = m.filter(p => p.precision !== "day").length;
  return `${latest} · ${m.length} measurements, ${year(first)}–${year(last)} · ${moved}`
    + (trend !== null ? ` · trend ${rate(trend)} over the record` : "")
    + (recentTrend !== null && recent ? `, ${rate(recentTrend)} over ${year(recent[0])}–${year(last)}` : "")
    + (vague ? ` · ${vague} dated only to the month or year, placed mid-period in the trend` : "")
    + (levels.truncated ? " · the USGS answer was cut short" : "");
}

export type WellPlot = Readonly<{
  start: number; end: number; low: number; high: number; ticks: readonly number[];
  years: readonly Readonly<{ time: number; label: string }>[];
  points: readonly WellMeasurement[];
  /** The first and last measurements' dates, as precisely as they are known. */
  firstLabel: string; lastLabel: string;
  trend: Readonly<{ from: Readonly<{ time: number; depth: number }>; to: Readonly<{ time: number; depth: number }> }> | null;
}>;

/** A hydrograph with depth increasing downward, rounded depth ticks, year ticks, and the record's trend line. */
export function wellPlot(levels: WellLevels): WellPlot | null {
  const m = levels.measurements;
  if (m.length < 2) return null;
  const min = Math.min(...m.map(p => p.depth)), max = Math.max(...m.map(p => p.depth));
  const step = [1, 2, 5, 10, 20, 25, 50, 100, 200].find(s => (Math.ceil(max / s) - Math.floor(min / s)) <= 5) ?? 500;
  const low = Math.floor(min / step) * step, high = Math.max(Math.ceil(max / step) * step, low + step);
  const ticks = Array.from({ length: Math.round((high - low) / step) + 1 }, (_, i) => low + i * step);
  const first = year(m[0]), last = year(m[m.length - 1]) + 1;
  const span = last - first;
  const every = [1, 2, 5, 10, 20].find(s => span / s <= 6) ?? 25;
  const years = [];
  for (let y = Math.ceil(first / every) * every; y <= last; y += every) years.push({ time: Date.UTC(y, 0, 1), label: String(y) });
  const start = Date.UTC(first, 0, 1), end = Date.UTC(last, 0, 1);
  const slope = depthTrend(m);
  let trend: WellPlot["trend"] = null;
  if (slope !== null) {
    const mx = m.reduce((a, p) => a + p.time, 0) / m.length, my = m.reduce((a, p) => a + p.depth, 0) / m.length;
    const at = (time: number) => my + slope * (time - mx) / YEAR_MS;
    trend = { from: { time: m[0].time, depth: at(m[0].time) }, to: { time: m[m.length - 1].time, depth: at(m[m.length - 1].time) } };
  }
  return Object.freeze({ start, end, low, high, ticks, years, points: m, firstLabel: measurementDate(m[0]), lastLabel: measurementDate(m[m.length - 1]), trend });
}

export type WellSite = Readonly<{ site: string; name: string; lon: number; lat: number }>;
/** The monitoring wells in the snapshot that carry a USGS site number. */
export function wellSites(collection: unknown): WellSite[] {
  const features = isRow(collection) && Array.isArray(collection.features) ? collection.features : [];
  return features.flatMap(feature => {
    const p = isRow(feature) && isRow(feature.properties) ? feature.properties : null;
    const c = isRow(feature) && isRow(feature.geometry) && Array.isArray(feature.geometry.coordinates) ? feature.geometry.coordinates : null;
    if (!p || !c || !isWellSite(p.USGS_ID) || typeof c[0] !== "number" || typeof c[1] !== "number") return [];
    return [{ site: p.USGS_ID, name: String(p.LOCAL_WELL ?? p.name ?? p.USGS_ID), lon: c[0], lat: c[1] }];
  });
}

const MILES_PER_DEGREE = 69.05;
const miles = (a: { lon: number; lat: number }, b: { lon: number; lat: number }) =>
  Math.hypot((a.lon - b.lon) * Math.cos((a.lat + b.lat) / 2 * Math.PI / 180), a.lat - b.lat) * MILES_PER_DEGREE;
/** The wells nearest a point (the map's centre), nearest first, for picking by keyboard. */
export function wellsNear(wells: readonly WellSite[], centre: { lon: number; lat: number }, count = 40): { id: string; label: string }[] {
  return wells.map(well => ({ well, d: miles(well, centre) })).sort((a, b) => a.d - b.d || a.well.name.localeCompare(b.well.name)).slice(0, count)
    .map(({ well, d }) => ({ id: well.site, label: `${well.name} · ${d < 10 ? d.toFixed(1) : Math.round(d)} mi` }));
}

export function wellLevelsKey(): MapKey {
  return Object.freeze({
    id: "well-levels",
    title: "Measured depth to water at KGS monitoring wells",
    items: Object.freeze([
      Object.freeze({ label: "Monitoring well (2026 network)", color: "#f4d57d", shape: "dot" as const }),
      Object.freeze({ label: "Well picked", color: "#ffffff", shape: "ring" as const }),
    ]),
    note: "Measured depth below land surface (USGS 72019), mostly the January measurements taken with irrigation pumps off. One well is one point in the aquifer: neighbouring wells can differ by tens of feet.",
  });
}

// The picked well's ring, above the wells it marks.
export const WELL_PICK_SOURCE_ID = "kfm-well-levels-picked";
export const WELL_PICK_LAYER_ID = "kfm-well-levels-picked-ring";

/** A ring at the picked well (or nothing, for null). */
export function syncWellPick(map: MapLibreMap, well: WellSite | null): void {
  if (!well) {
    if (map.getLayer(WELL_PICK_LAYER_ID)) map.removeLayer(WELL_PICK_LAYER_ID);
    if (map.getSource(WELL_PICK_SOURCE_ID)) map.removeSource(WELL_PICK_SOURCE_ID);
    return;
  }
  const data: FeatureCollection<Point> = { type: "FeatureCollection", features: [{ type: "Feature", geometry: { type: "Point", coordinates: [well.lon, well.lat] }, properties: { site: well.site } }] };
  const source = map.getSource(WELL_PICK_SOURCE_ID) as GeoJSONSource | undefined;
  if (source) source.setData(data);
  else map.addSource(WELL_PICK_SOURCE_ID, { type: "geojson", data });
  if (!map.getLayer(WELL_PICK_LAYER_ID)) map.addLayer({ id: WELL_PICK_LAYER_ID, type: "circle", source: WELL_PICK_SOURCE_ID,
    paint: { "circle-color": "rgba(0,0,0,0)", "circle-radius": ["interpolate", ["linear"], ["zoom"], 5, 7, 10, 11] as never, "circle-stroke-color": "#ffffff", "circle-stroke-width": 2.4 } });
}
