import type { Map as MapLibreMap, GeoJSONSource } from "./maplibre-seam";
import type { Feature, FeatureCollection, MultiPolygon, Polygon, Position } from "geojson";
import { KANSAS_OUTLINE } from "./kansas-orientation";
import type { MapKey } from "./map-keys";

/**
 * The NOAA Storm Prediction Center's convective outlooks for days 1–3: the
 * categorical outlook (where SPC forecasts thunderstorms and how high the
 * severe risk is) and, for days 1 and 2, its tornado, damaging-wind and hail
 * probabilities with their conditional-intensity areas. They are forecasts,
 * drawn on the Storm desk as outlines over radar and alerts, never as an
 * observation or a warning.
 */
export type OutlookDay = 1 | 2 | 3;
export const OUTLOOK_DAYS: readonly OutlookDay[] = Object.freeze([1, 2, 3]);
/** "cat" is the categorical outlook; the others are SPC's per-hazard probability outlooks. */
export type OutlookProduct = "cat" | "torn" | "wind" | "hail";
export type OutlookHazard = Exclude<OutlookProduct, "cat">;
export const OUTLOOK_PRODUCTS: readonly OutlookProduct[] = Object.freeze(["cat", "torn", "wind", "hail"]);
const HAZARD_NAMES: Readonly<Record<OutlookProduct, string>> = Object.freeze({ cat: "Categorical", torn: "Tornado", wind: "Wind", hail: "Hail" });
export const outlookProductName = (product: OutlookProduct): string => HAZARD_NAMES[product];
/** SPC issues per-hazard probabilities for days 1 and 2; day 3 is categorical here. */
export const outlookProducts = (day: OutlookDay): readonly OutlookProduct[] => day === 3 ? OUTLOOK_PRODUCTS.slice(0, 1) : OUTLOOK_PRODUCTS;
export const isOutlookProduct = (value: unknown): value is OutlookProduct => OUTLOOK_PRODUCTS.includes(value as OutlookProduct);
export const SPC_OUTLOOK_SOURCE_ID = "kfm-spc-outlook";
export const SPC_OUTLOOK_LAYER_ID = "kfm-spc-outlook-lines";
export const SPC_INTENSITY_LAYER_ID = "kfm-spc-outlook-intensity";
export const spcOutlookProviderUrl = (day: OutlookDay, product: OutlookProduct = "cat"): string => `https://www.spc.noaa.gov/products/outlook/day${day}otlk_${product}.lyr.geojson`;
/** The conditional-intensity areas that, since March 2026, replace the hatched "significant" areas of each hazard. */
export const spcIntensityProviderUrl = (day: OutlookDay, hazard: OutlookHazard): string => `https://www.spc.noaa.gov/products/outlook/day${day}otlk_cig${hazard}.lyr.geojson`;
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

/** A band of an outlook's scale: an SPC category, a probability, or an intensity level. */
export type SpcBand = Readonly<{ id: string; rank: number; name: string; short: string; color: string }>;
/**
 * SPC's probability ladders: the chance of the hazard within 25 miles of a
 * point. The colours follow SPC's hazard maps (tornado 2% green through 60%
 * blue; wind and hail 5% brown through 60% purple), lightened to stay legible
 * on the dark storm base. Since March 2026 the wind ladder runs on to 75% and
 * 90%, drawn in blue and cyan past its purple.
 */
const P = { 2: "#4fbf4f", 5: "#c08a5e", 10: "#ffd84d", 15: "#ff5c5c", 30: "#ff66ff", 45: "#b77cf2", 60: "#5f9fe0", 90: "#4fe3e3" } as const;
const ladder = (steps: readonly (readonly [number, string])[]): readonly SpcBand[] => Object.freeze(steps.map(([percent, color], rank) =>
  Object.freeze({ id: String(percent), rank: rank + 1, name: `${percent}%`, short: `${percent}%`, color })));
export const SPC_PROBABILITIES: Readonly<Record<OutlookHazard, readonly SpcBand[]>> = Object.freeze({
  torn: ladder([[2, P[2]], [5, P[5]], [10, P[10]], [15, P[15]], [30, P[30]], [45, P[45]], [60, P[60]]]),
  wind: ladder([[5, P[5]], [15, P[10]], [30, P[15]], [45, P[30]], [60, P[45]], [75, P[60]], [90, P[90]]]),
  hail: ladder([[5, P[5]], [15, P[10]], [30, P[15]], [45, P[30]], [60, P[45]]]),
});
/** SPC's conditional-intensity groups: how intense the hazard could be where it occurs. Hail has two. */
export const SPC_INTENSITY_COLOR = "#f4f4f4";
const INTENSITY: Readonly<Record<OutlookHazard, number>> = Object.freeze({ torn: 3, wind: 3, hail: 2 });
export const spcIntensityLevels = (hazard: OutlookHazard): readonly SpcBand[] => Object.freeze(Array.from({ length: INTENSITY[hazard] }, (_, i) =>
  Object.freeze({ id: `CIG${i + 1}`, rank: i + 1, name: `Intensity level ${i + 1}`, short: `CIG${i + 1}`, color: SPC_INTENSITY_COLOR })));
/** The scale an outlook's polygons are drawn on. */
export const spcScale = (product: OutlookProduct): readonly SpcBand[] => product === "cat" ? SPC_CATEGORIES : SPC_PROBABILITIES[product];
const band = (product: OutlookProduct, id: unknown): SpcBand | undefined => typeof id === "string" ? spcScale(product).find(b => b.id === id) : undefined;

export type SpcOutlook = Readonly<{
  day: OutlookDay;
  product: OutlookProduct;
  /** Band polygons, each with its band id as `category`: an SPC category, a probability percent, or an intensity group (CIG1–CIG3). */
  data: FeatureCollection<Polygon | MultiPolygon, { category: string }>;
  issuedAt: string | null; validFrom: string | null; validUntil: string | null;
  /** The highest category or probability whose area reaches into Kansas, or null. */
  kansas: string | null;
  /** The highest conditional-intensity group reaching into Kansas, or null. */
  intensity: string | null;
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

const INTENSITY_LABEL = /^CIG([1-3])$/;
/** A feature's intensity group: CIG1–CIG3, or the hatched "SIGN" area SPC drew before March 2026, which CIG1 replaces. */
function intensityOf(properties: Record<string, unknown> | null, hazard: OutlookHazard): SpcBand | undefined {
  const label = typeof properties?.LABEL === "string" ? properties.LABEL.trim().toUpperCase() : "";
  const level = label === "SIGN" ? 1 : Number(INTENSITY_LABEL.exec(label)?.[1] ?? 0);
  return spcIntensityLevels(hazard)[level - 1];
}
/** A hazard feature's probability: SPC's DN is the percent; its LABEL is the same chance as a fraction. */
function probabilityOf(properties: Record<string, unknown> | null, hazard: OutlookHazard): SpcBand | undefined {
  const label = typeof properties?.LABEL === "string" ? Number(properties.LABEL.trim()) : NaN;
  const percent = typeof properties?.DN === "number" ? properties.DN : Number.isFinite(label) ? label < 1 ? Math.round(label * 100) : label : NaN;
  return band(hazard, String(percent));
}

/**
 * SPC GeoJSON to the outlook drawn: known bands only, valid polygons only,
 * with its clock and the highest band over Kansas. For a hazard, the
 * conditional-intensity collection (SPC publishes it separately) is read with
 * it; an intensity area in the hazard file itself is taken as well.
 */
export function parseSpcOutlook(raw: unknown, day: OutlookDay, retrievedAt: string, source: string, product: OutlookProduct = "cat", intensityRaw?: unknown): SpcOutlook {
  const collection = record(raw);
  // SPC answers an empty outlook with a bare GeometryCollection.
  const features = collection?.type === "GeometryCollection" ? [] : collection?.features;
  if (!Array.isArray(features)) throw new Error("The SPC outlook was not a feature collection.");
  const intensityCollection = record(intensityRaw), extra = Array.isArray(intensityCollection?.features) ? intensityCollection.features : [];
  const kept: Feature<Polygon | MultiPolygon, { category: string }>[] = [];
  let issuedAt: string | null = null, validFrom: string | null = null, validUntil: string | null = null;
  let kansas: SpcBand | null = null, intensity: SpcBand | null = null;
  for (const candidate of [...features, ...extra]) {
    const feature = record(candidate), properties = record(feature?.properties), geometry = record(feature?.geometry);
    const level = product === "cat" ? undefined : intensityOf(properties, product);
    const found = level ?? (product === "cat" ? CATEGORY.get(typeof properties?.LABEL === "string" ? properties.LABEL.trim().toUpperCase() : "") : probabilityOf(properties, product));
    if (!found || !geometry) continue;
    const polygons = geometry.type === "Polygon" ? [polygon(geometry.coordinates)] : geometry.type === "MultiPolygon" && Array.isArray(geometry.coordinates) ? geometry.coordinates.map(polygon) : [];
    if (!polygons.length || !polygons.every(Boolean)) continue;
    const valid = polygons as Position[][][];
    if (!level) {
      issuedAt ??= spcTime(properties?.ISSUE_ISO) ?? spcTime(properties?.ISSUE);
      validFrom ??= spcTime(properties?.VALID_ISO) ?? spcTime(properties?.VALID);
      validUntil ??= spcTime(properties?.EXPIRE_ISO) ?? spcTime(properties?.EXPIRE);
    }
    kept.push({ type: "Feature", properties: { category: found.id },
      geometry: valid.length === 1 ? { type: "Polygon", coordinates: valid[0] } : { type: "MultiPolygon", coordinates: valid } });
    if (level) { if ((!intensity || level.rank > intensity.rank) && reachesKansas(valid)) intensity = level; }
    else if ((!kansas || found.rank > kansas.rank) && reachesKansas(valid)) kansas = found;
  }
  // Bands lowest to highest, intensity areas over them.
  const order = (id: string) => INTENSITY_LABEL.test(id) ? 100 + Number(id.slice(3)) : band(product, id)!.rank;
  kept.sort((a, b) => order(a.properties.category) - order(b.properties.category));
  return Object.freeze({ day, product, data: { type: "FeatureCollection" as const, features: kept }, issuedAt, validFrom, validUntil,
    kansas: kansas?.id ?? null, intensity: intensity?.id ?? null, retrievedAt, source });
}

export function validSpcOutlook(value: unknown): value is SpcOutlook {
  const candidate = record(value), data = record(candidate?.data);
  const day = candidate?.day as OutlookDay, product = candidate?.product as OutlookProduct;
  if (!candidate || !OUTLOOK_DAYS.includes(day) || !isOutlookProduct(product) || !outlookProducts(day).includes(product) || typeof candidate.retrievedAt !== "string") return false;
  const levels = product === "cat" ? [] : spcIntensityLevels(product).map(level => level.id);
  return (candidate.kansas === null || Boolean(band(product, candidate.kansas)))
    && (candidate.intensity === null || levels.includes(candidate.intensity as string))
    && data?.type === "FeatureCollection" && Array.isArray(data.features)
    && data.features.every(feature => {
      const f = record(feature), g = record(f?.geometry), id = record(f?.properties)?.category;
      return (Boolean(band(product, id)) || levels.includes(id as string)) && (g?.type === "Polygon" || g?.type === "MultiPolygon");
    });
}

export const spcCategory = (id: string | null): SpcCategory | null => id ? CATEGORY.get(id) ?? null : null;

/** The highest band (category or probability) whose area holds a point, or null; intensity areas are not bands. */
export function outlookBandAt(outlook: SpcOutlook, longitude: number, latitude: number): SpcBand | null {
  const product = outlook.product ?? "cat";
  let best: SpcBand | null = null;
  for (const feature of outlook.data.features) {
    const found = band(product, feature.properties.category);
    if (!found || (best && found.rank <= best.rank)) continue;
    const polygons = feature.geometry.type === "Polygon" ? [feature.geometry.coordinates] : feature.geometry.coordinates;
    if (polygons.some(rings => inPolygon([longitude, latitude], rings))) best = found;
  }
  return best;
}

const HAZARD_PHRASE: Readonly<Record<OutlookHazard, string>> = Object.freeze({ torn: "a tornado", wind: "damaging wind gusts (50 kt+)", hail: "hail 1 inch or larger" });
const INTENSITY_NOTE = "Dashed white lines are SPC's conditional-intensity areas: level 1 where significant severe weather is possible (EF2+ tornadoes, 65 kt+ gusts, 2 in+ hail), higher levels where storms that form could be more intense.";

/** The outlook key: one line per band, lowest to highest, in the colours drawn. */
export function spcOutlookKey(day: OutlookDay, product: OutlookProduct = "cat"): MapKey {
  if (product === "cat") return Object.freeze({
    id: "spc-outlook", title: `SPC convective outlook · Day ${day}`,
    items: Object.freeze(SPC_CATEGORIES.map(category => Object.freeze({ label: `${category.short === category.id ? category.id : category.short} ${category.name}`, color: category.color, shape: "line" as const }))),
    note: "A forecast of where thunderstorms are expected and the risk of severe storms (1 Marginal to 5 High); higher categories lie inside lower ones. Not an observation or a warning.",
  });
  return Object.freeze({
    id: "spc-outlook", title: `SPC ${HAZARD_NAMES[product].toLowerCase()} outlook · Day ${day}`,
    items: Object.freeze([
      ...SPC_PROBABILITIES[product].map(step => Object.freeze({ label: step.name, color: step.color, shape: "line" as const })),
      ...spcIntensityLevels(product).map(level => Object.freeze({ label: `${level.short} ${level.name}`, color: level.color, shape: "line" as const, dashed: true })),
    ]),
    note: `The forecast probability of ${HAZARD_PHRASE[product]} within 25 miles of a point; higher probabilities lie inside lower ones. ${INTENSITY_NOTE} Not an observation or a warning.`,
  });
}

const notIntensity = ["!", ["in", ["get", "category"], ["literal", ["CIG1", "CIG2", "CIG3"]]]];
const isIntensity = ["in", ["get", "category"], ["literal", ["CIG1", "CIG2", "CIG3"]]];
const colors = (product: OutlookProduct) => ["match", ["get", "category"], ...spcScale(product).flatMap(step => [step.id, step.color]), "#9aa5ad"];
const widths = (product: OutlookProduct) => product === "cat" ? ["match", ["get", "category"], "TSTM", 1.4, "MRGL", 1.8, 2.4]
  : ["match", ["get", "category"], spcScale(product)[0].id, 1.8, 2.4];
const shown = new WeakMap<MapLibreMap, { data: SpcOutlook["data"]; product: OutlookProduct }>();
const removeLayers = (map: MapLibreMap) => { for (const id of [SPC_INTENSITY_LAYER_ID, SPC_OUTLOOK_LAYER_ID]) if (map.getLayer(id)) map.removeLayer(id); };

/** Draws the outlook's outlines (or removes them, for null). Safe to call on every style load. */
export function syncSpcOutlook(map: MapLibreMap, outlook: SpcOutlook | null): void {
  if (!outlook) {
    removeLayers(map);
    if (map.getSource(SPC_OUTLOOK_SOURCE_ID)) map.removeSource(SPC_OUTLOOK_SOURCE_ID);
    shown.delete(map);
    return;
  }
  const product = outlook.product ?? "cat";
  const source = map.getSource(SPC_OUTLOOK_SOURCE_ID) as GeoJSONSource | undefined, last = shown.get(map);
  if (!source) map.addSource(SPC_OUTLOOK_SOURCE_ID, { type: "geojson", data: outlook.data });
  else if (last?.data !== outlook.data) source.setData(outlook.data);
  // Each product draws on its own scale: a new product brings new paint.
  if (last && last.product !== product) removeLayers(map);
  shown.set(map, { data: outlook.data, product });
  // Above the base and the provider layers (radar, alerts), under the site's own overlays and labels.
  const before = map.getStyle().layers?.find(layer => layer.id.startsWith("kfm-") && layer.id !== "kfm-background" && !layer.id.startsWith(SPC_OUTLOOK_SOURCE_ID))?.id;
  if (!map.getLayer(SPC_OUTLOOK_LAYER_ID)) map.addLayer({ id: SPC_OUTLOOK_LAYER_ID, type: "line", source: SPC_OUTLOOK_SOURCE_ID,
    ...(product === "cat" ? {} : { filter: notIntensity as never }),
    layout: { "line-join": "round", "line-cap": "round" },
    paint: { "line-color": colors(product) as never, "line-width": widths(product) as never, "line-opacity": 0.95 } }, before);
  if (product !== "cat" && !map.getLayer(SPC_INTENSITY_LAYER_ID)) map.addLayer({ id: SPC_INTENSITY_LAYER_ID, type: "line", source: SPC_OUTLOOK_SOURCE_ID,
    filter: isIntensity as never, layout: { "line-join": "round" },
    paint: { "line-color": SPC_INTENSITY_COLOR, "line-width": ["match", ["get", "category"], "CIG1", 1.4, "CIG2", 2, 2.6] as never, "line-dasharray": [2.5, 1.8], "line-opacity": 0.9 } }, before);
}

const CLOCK = new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: "short", day: "numeric", hour: "2-digit", minute: "2-digit", hourCycle: "h23" });
const clock = (iso: string) => `${CLOCK.format(new Date(iso))} UTC`;

/** What the outlook says for Kansas, and when it was issued and is valid. */
export function spcOutlookReading(outlook: SpcOutlook): string {
  const product = outlook.product ?? "cat";
  let risk: string;
  if (product === "cat") {
    const category = spcCategory(outlook.kansas);
    risk = category ? category.rank === 0 ? "General thunderstorms forecast in Kansas, below the severe categories" : `Highest risk in Kansas: ${category.name} (${category.rank} of 5)`
      : outlook.data.features.length ? "No thunderstorm area reaches Kansas" : "No thunderstorm areas in this outlook";
  } else {
    const step = band(product, outlook.kansas), lowest = SPC_PROBABILITIES[product][0].name, levels = spcIntensityLevels(product);
    const any = outlook.data.features.some(feature => !INTENSITY_LABEL.test(feature.properties.category));
    risk = `${HAZARD_NAMES[product]}: ${step ? `${step.name} chance within 25 miles of a point, highest in Kansas` : any ? `below ${lowest} across Kansas` : `below ${lowest} everywhere in this outlook`}`;
    const level = levels.find(l => l.id === outlook.intensity);
    if (level) risk += ` · intensity level ${level.rank} of ${levels.length} reaches Kansas`;
  }
  const issued = outlook.issuedAt ? ` · issued ${clock(outlook.issuedAt)}` : "";
  const valid = outlook.validFrom && outlook.validUntil ? ` · valid ${clock(outlook.validFrom)} to ${clock(outlook.validUntil)}` : "";
  return `${risk}${issued}${valid}`;
}
