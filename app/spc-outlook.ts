import type { Map as MapLibreMap, GeoJSONSource } from "./maplibre-seam";
import type { Feature, FeatureCollection, MultiPolygon, Polygon, Position } from "geojson";
import { KANSAS_OUTLINE } from "./kansas-orientation";
import type { MapKey } from "./map-keys";

/**
 * The NOAA Storm Prediction Center's categorical convective outlook for days
 * 1–3: where SPC forecasts thunderstorms and how high the severe risk is.
 * It is a forecast, drawn on the Storm desk as outlines over radar and alerts,
 * never as an observation or a warning.
 */
export type OutlookDay = 1 | 2 | 3;
export const OUTLOOK_DAYS: readonly OutlookDay[] = Object.freeze([1, 2, 3]);
export const SPC_OUTLOOK_SOURCE_ID = "kfm-spc-outlook";
export const SPC_OUTLOOK_LAYER_ID = "kfm-spc-outlook-lines";
export const spcOutlookProviderUrl = (day: OutlookDay): string => `https://www.spc.noaa.gov/products/outlook/day${day}otlk_cat.lyr.geojson`;
export const SPC_OUTLOOK_PAGE = "https://www.spc.noaa.gov/products/outlook/";

/**
 * SPC's categories, lowest to highest, with SPC's own fill colours. On the
 * dark storm base the fills, not SPC's darker strokes, are what stays legible,
 * so the outlines are drawn in them.
 */
export const SPC_CATEGORIES = Object.freeze([
  Object.freeze({ id: "TSTM", rank: 0, name: "General thunderstorms", short: "TSTM", color: "#c1e9c1" }),
  Object.freeze({ id: "MRGL", rank: 1, name: "Marginal", short: "1 · MRGL", color: "#66a366" }),
  Object.freeze({ id: "SLGT", rank: 2, name: "Slight", short: "2 · SLGT", color: "#ffe066" }),
  Object.freeze({ id: "ENH", rank: 3, name: "Enhanced", short: "3 · ENH", color: "#ffa366" }),
  Object.freeze({ id: "MDT", rank: 4, name: "Moderate", short: "4 · MDT", color: "#e06666" }),
  Object.freeze({ id: "HIGH", rank: 5, name: "High", short: "5 · HIGH", color: "#ee99ee" }),
] as const);
export type SpcCategory = (typeof SPC_CATEGORIES)[number];
const CATEGORY = new Map<string, SpcCategory>(SPC_CATEGORIES.map(category => [category.id, category]));

export type SpcOutlook = Readonly<{
  day: OutlookDay;
  /** Category polygons, each with the category id as `category`. */
  data: FeatureCollection<Polygon | MultiPolygon, { category: SpcCategory["id"] }>;
  issuedAt: string | null; validFrom: string | null; validUntil: string | null;
  /** The highest category whose area reaches into Kansas, or null. */
  kansas: SpcCategory["id"] | null;
  retrievedAt: string; source: string;
}>;

const record = (value: unknown): Record<string, unknown> | null => value && typeof value === "object" && !Array.isArray(value) ? value as Record<string, unknown> : null;

/** SPC times: "YYYYMMDDHHMM" (UTC) in the classic fields, ISO 8601 in the *_ISO ones. */
export function spcTime(value: unknown): string | null {
  if (typeof value !== "string") return null;
  const compact = /^(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})$/.exec(value.trim());
  const date = compact ? new Date(Date.UTC(+compact[1], +compact[2] - 1, +compact[3], +compact[4], +compact[5])) : /^\d{4}-\d{2}-\d{2}T/.test(value) ? new Date(value) : null;
  return date && Number.isFinite(date.getTime()) ? date.toISOString() : null;
}

const ring = (value: unknown): Position[] | null => Array.isArray(value) && value.length >= 4 && value.every(point => Array.isArray(point) && point.length >= 2
  && typeof point[0] === "number" && typeof point[1] === "number" && Number.isFinite(point[0]) && Number.isFinite(point[1]) && Math.abs(point[0]) <= 180 && Math.abs(point[1]) <= 90)
  ? value.map(point => [Math.round(point[0] * 1e4) / 1e4, Math.round(point[1] * 1e4) / 1e4]) : null;
const polygon = (value: unknown): Position[][] | null => {
  if (!Array.isArray(value) || !value.length) return null;
  const rings = value.map(ring);
  return rings.every(Boolean) ? rings as Position[][] : null;
};

/** Point in a polygon with holes (even-odd over all its rings). */
function inPolygon(point: readonly [number, number], rings: readonly Position[][]): boolean {
  let inside = false;
  for (const r of rings) for (let i = 0, j = r.length - 1; i < r.length; j = i++) {
    const [xi, yi] = r[i], [xj, yj] = r[j];
    if ((yi > point[1]) !== (yj > point[1]) && point[0] < (xj - xi) * (point[1] - yi) / (yj - yi) + xi) inside = !inside;
  }
  return inside;
}
function inKansas([x, y]: readonly [number, number]): boolean {
  let inside = false;
  for (let i = 0, j = KANSAS_OUTLINE.length - 1; i < KANSAS_OUTLINE.length; j = i++) {
    const [xi, yi] = KANSAS_OUTLINE[i], [xj, yj] = KANSAS_OUTLINE[j];
    if ((yi > y) !== (yj > y) && x < (xj - xi) * (y - yi) / (yj - yi) + xi) inside = !inside;
  }
  return inside;
}
/** Points every 0.1° (about 10 km) inside Kansas, against which an outlook area is tested. */
const KANSAS_SAMPLES: readonly (readonly [number, number])[] = (() => {
  const points: [number, number][] = [];
  for (let x = -102.0; x <= -94.6; x += 0.1) for (let y = 37.0; y <= 40.0; y += 0.1) {
    const p: [number, number] = [Math.round(x * 100) / 100, Math.round(y * 100) / 100];
    if (inKansas(p)) points.push(p);
  }
  return points;
})();
const reachesKansas = (polygons: readonly Position[][][]) => KANSAS_SAMPLES.some(point => polygons.some(rings => inPolygon(point, rings)));

/** SPC GeoJSON to the outlook drawn: known categories only, valid polygons only, with its clock and the highest risk over Kansas. */
export function parseSpcOutlook(raw: unknown, day: OutlookDay, retrievedAt: string, source: string): SpcOutlook {
  const features = record(raw)?.features;
  if (!Array.isArray(features)) throw new Error("The SPC outlook was not a feature collection.");
  const kept: Feature<Polygon | MultiPolygon, { category: SpcCategory["id"] }>[] = [];
  let issuedAt: string | null = null, validFrom: string | null = null, validUntil: string | null = null, kansas: SpcCategory | null = null;
  for (const candidate of features) {
    const feature = record(candidate), properties = record(feature?.properties), geometry = record(feature?.geometry);
    const category = CATEGORY.get(typeof properties?.LABEL === "string" ? properties.LABEL.trim().toUpperCase() : "");
    if (!category || !geometry) continue;
    const polygons = geometry.type === "Polygon" ? [polygon(geometry.coordinates)] : geometry.type === "MultiPolygon" && Array.isArray(geometry.coordinates) ? geometry.coordinates.map(polygon) : [];
    if (!polygons.length || !polygons.every(Boolean)) continue;
    const valid = polygons as Position[][][];
    issuedAt ??= spcTime(properties?.ISSUE_ISO) ?? spcTime(properties?.ISSUE);
    validFrom ??= spcTime(properties?.VALID_ISO) ?? spcTime(properties?.VALID);
    validUntil ??= spcTime(properties?.EXPIRE_ISO) ?? spcTime(properties?.EXPIRE);
    kept.push({ type: "Feature", properties: { category: category.id },
      geometry: valid.length === 1 ? { type: "Polygon", coordinates: valid[0] } : { type: "MultiPolygon", coordinates: valid } });
    if ((!kansas || category.rank > kansas.rank) && reachesKansas(valid)) kansas = category;
  }
  kept.sort((a, b) => CATEGORY.get(a.properties.category)!.rank - CATEGORY.get(b.properties.category)!.rank);
  return Object.freeze({ day, data: { type: "FeatureCollection" as const, features: kept }, issuedAt, validFrom, validUntil, kansas: kansas?.id ?? null, retrievedAt, source });
}

export function validSpcOutlook(value: unknown): value is SpcOutlook {
  const candidate = record(value), data = record(candidate?.data);
  return Boolean(candidate && OUTLOOK_DAYS.includes(candidate.day as OutlookDay) && typeof candidate.retrievedAt === "string"
    && (candidate.kansas === null || CATEGORY.has(candidate.kansas as string))
    && data?.type === "FeatureCollection" && Array.isArray(data.features)
    && data.features.every(feature => { const f = record(feature), g = record(f?.geometry); return CATEGORY.has(record(f?.properties)?.category as string) && (g?.type === "Polygon" || g?.type === "MultiPolygon"); }));
}

export const spcCategory = (id: string | null): SpcCategory | null => id ? CATEGORY.get(id) ?? null : null;

/** The outlook key: one line per category, lowest to highest, in the colours drawn. */
export function spcOutlookKey(day: OutlookDay): MapKey {
  return Object.freeze({
    id: "spc-outlook", title: `SPC convective outlook · Day ${day}`,
    items: Object.freeze(SPC_CATEGORIES.map(category => Object.freeze({ label: `${category.short === category.id ? category.id : category.short} ${category.name}`, color: category.color, shape: "line" as const }))),
    note: "A forecast of where thunderstorms are expected and the risk of severe storms (1 Marginal to 5 High); higher categories lie inside lower ones. Not an observation or a warning.",
  });
}

const colors = ["match", ["get", "category"], ...SPC_CATEGORIES.flatMap(category => [category.id, category.color]), "#9aa5ad"];
const widths = ["match", ["get", "category"], "TSTM", 1.4, "MRGL", 1.8, 2.4];
const shown = new WeakMap<MapLibreMap, SpcOutlook["data"]>();

/** Draws the outlook's outlines (or removes them, for null). Safe to call on every style load. */
export function syncSpcOutlook(map: MapLibreMap, outlook: SpcOutlook | null): void {
  if (!outlook) {
    if (map.getLayer(SPC_OUTLOOK_LAYER_ID)) map.removeLayer(SPC_OUTLOOK_LAYER_ID);
    if (map.getSource(SPC_OUTLOOK_SOURCE_ID)) map.removeSource(SPC_OUTLOOK_SOURCE_ID);
    shown.delete(map);
    return;
  }
  const source = map.getSource(SPC_OUTLOOK_SOURCE_ID) as GeoJSONSource | undefined;
  if (!source) map.addSource(SPC_OUTLOOK_SOURCE_ID, { type: "geojson", data: outlook.data });
  else if (shown.get(map) !== outlook.data) source.setData(outlook.data);
  shown.set(map, outlook.data);
  // Above the base and the provider layers (radar, alerts), under the site's own overlays and labels.
  const before = map.getStyle().layers?.find(layer => layer.id.startsWith("kfm-") && layer.id !== "kfm-background" && !layer.id.startsWith(SPC_OUTLOOK_SOURCE_ID))?.id;
  if (!map.getLayer(SPC_OUTLOOK_LAYER_ID)) map.addLayer({ id: SPC_OUTLOOK_LAYER_ID, type: "line", source: SPC_OUTLOOK_SOURCE_ID,
    layout: { "line-join": "round", "line-cap": "round" },
    paint: { "line-color": colors as never, "line-width": widths as never, "line-opacity": 0.95 } }, before);
}

const CLOCK = new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: "short", day: "numeric", hour: "2-digit", minute: "2-digit", hourCycle: "h23" });
const clock = (iso: string) => `${CLOCK.format(new Date(iso))} UTC`;

/** What the outlook says for Kansas, and when it was issued and is valid. */
export function spcOutlookReading(outlook: SpcOutlook): string {
  const category = spcCategory(outlook.kansas);
  const risk = category ? category.rank === 0 ? "General thunderstorms forecast in Kansas, below the severe categories" : `Highest risk in Kansas: ${category.name} (${category.rank} of 5)`
    : outlook.data.features.length ? "No thunderstorm area reaches Kansas" : "No thunderstorm areas in this outlook";
  const issued = outlook.issuedAt ? ` · issued ${clock(outlook.issuedAt)}` : "";
  const valid = outlook.validFrom && outlook.validUntil ? ` · valid ${clock(outlook.validFrom)} to ${clock(outlook.validUntil)}` : "";
  return `${risk}${issued}${valid}`;
}
