import type { Map as MapLibreMap, GeoJSONSource } from "./maplibre-seam";
import type { Feature, FeatureCollection, MultiPolygon, Polygon, Position } from "geojson";
import { KANSAS_OUTLINE } from "./kansas-orientation";
import type { MapKey } from "./map-keys";

/**
 * The U.S. Drought Monitor (USDM): the weekly map of drought intensity that the
 * National Drought Mitigation Center, USDA and NOAA authors draw from many
 * indicators and local reports. Each map is valid for a Tuesday (8 a.m.
 * Eastern) and released that Thursday. D0 is abnormally dry, not drought;
 * D1–D4 are moderate to exceptional drought.
 */
export const USDM_CATEGORIES = Object.freeze([
  Object.freeze({ dm: 0, id: "D0", name: "Abnormally dry", color: "#ffff00" }),
  Object.freeze({ dm: 1, id: "D1", name: "Moderate drought", color: "#fcd37f" }),
  Object.freeze({ dm: 2, id: "D2", name: "Severe drought", color: "#ffaa00" }),
  Object.freeze({ dm: 3, id: "D3", name: "Extreme drought", color: "#e60000" }),
  Object.freeze({ dm: 4, id: "D4", name: "Exceptional drought", color: "#730000" }),
] as const);
export const USDM_PAGE = "https://droughtmonitor.unl.edu/";
export const DROUGHT_SOURCE_ID = "kfm-drought-monitor";
export const DROUGHT_FILL_LAYER_ID = "kfm-drought-monitor-fill";
export const DROUGHT_LINE_LAYER_ID = "kfm-drought-monitor-lines";
/** The state line, drawn over the categories as the USDM's state maps draw it; the base's own outline lies beneath them. */
export const DROUGHT_STATE_SOURCE_ID = "kfm-drought-monitor-state";
export const DROUGHT_STATE_LAYER_ID = "kfm-drought-monitor-state-line";
/** County lines over the categories, as on the USDM's state maps, and the county picked in the dock. */
export const DROUGHT_COUNTY_SOURCE_ID = "kfm-drought-monitor-counties";
export const DROUGHT_COUNTY_LAYER_ID = "kfm-drought-monitor-county-lines";
export const DROUGHT_COUNTY_SELECTED_LAYER_ID = "kfm-drought-monitor-county-selected";
/** The first USDM map, valid Tuesday 4 January 2000. */
export const USDM_FIRST_DATE = "20000104";

const DAY_MS = 86_400_000;
const record = (value: unknown): Record<string, unknown> | null => value && typeof value === "object" && !Array.isArray(value) ? value as Record<string, unknown> : null;
const compactMs = (value: string): number | null => {
  const match = /^(\d{4})(\d{2})(\d{2})$/.exec(value);
  if (!match) return null;
  const ms = Date.UTC(+match[1], +match[2] - 1, +match[3]);
  return new Date(ms).toISOString().slice(0, 10).replaceAll("-", "") === value ? ms : null;
};
const compact = (ms: number): string => new Date(ms).toISOString().slice(0, 10).replaceAll("-", "");

/** A USDM map date: "YYYYMMDD", a Tuesday, from the first map on. */
export function isUsdmDate(value: unknown): value is string {
  const ms = typeof value === "string" ? compactMs(value) : null;
  return ms !== null && new Date(ms).getUTCDay() === 2 && value as string >= USDM_FIRST_DATE;
}
/**
 * The newest map released by `now`: maps come out Thursdays at 8:30 a.m.
 * Eastern (13:30 UTC in winter, 12:30 in summer; the later is taken) and are
 * valid for the Tuesday before. A holiday can delay a release; the route then
 * falls back a week.
 */
export function latestUsdmDate(now: Date): string {
  const midnight = Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate());
  let thursday = midnight - ((now.getUTCDay() - 4 + 7) % 7) * DAY_MS;
  if (now.getTime() < thursday + 13.5 * 3_600_000) thursday -= 7 * DAY_MS;
  return compact(thursday - 2 * DAY_MS);
}
export const previousUsdmDate = (date: string): string => compact((compactMs(date) ?? 0) - 7 * DAY_MS);
export const nextUsdmDate = (date: string): string => compact((compactMs(date) ?? 0) + 7 * DAY_MS);
/** The week `weeks` before `date`, no earlier than the first map. */
export const usdmWeeksBefore = (date: string, weeks: number): string => {
  const back = compact((compactMs(date) ?? 0) - weeks * 7 * DAY_MS);
  return back < USDM_FIRST_DATE ? USDM_FIRST_DATE : back;
};
/** Play holds each week this long once it is drawn; from the newest it starts a year back. */
export const DROUGHT_PLAY_STEP_MS = 1200;
export const DROUGHT_PLAY_WEEKS = 52;
const LONG = new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: "short", day: "numeric", year: "numeric" });
/** "Oct 20, 2026" for "20261020". */
export const usdmDateLabel = (date: string): string => { const ms = compactMs(date); return ms === null ? date : LONG.format(new Date(ms)); };

export const usdmMapProviderUrl = (date: string): string => `https://droughtmonitor.unl.edu/data/json/usdm_${date}.json`;
/** Kansas's weekly share of area in each category since the first map, from the USDM data services. */
export const usdmSeriesProviderUrl = (now: Date): string =>
  `https://usdmdataservices.unl.edu/api/StateStatistics/GetDroughtSeverityStatisticsByAreaPercent?aoi=KS&startdate=1/1/2000&enddate=${now.getUTCMonth() + 1}/${now.getUTCDate()}/${now.getUTCFullYear()}&statisticsType=1`;

/** Kansas with a degree or so around it: the national map is cut to this before it is sent. */
export const DROUGHT_REGION = Object.freeze([-103.2, 36.2, -93.6, 40.8] as const);

type Ring = Position[];
const round = (value: number) => Math.round(value * 1e4) / 1e4;
const finiteRing = (value: unknown): Ring | null => Array.isArray(value) && value.length >= 4 && value.every(point => Array.isArray(point) && point.length >= 2
  && typeof point[0] === "number" && typeof point[1] === "number" && Number.isFinite(point[0]) && Number.isFinite(point[1]) && Math.abs(point[0]) <= 180 && Math.abs(point[1]) <= 90)
  ? value as Ring : null;

/**
 * A ring cut to the region (Sutherland–Hodgman against each side of the box).
 * Where a concave ring leaves and re-enters, the cut runs along the box edge,
 * outside Kansas; filled, it adds nothing.
 */
export function clipRing(ring: Ring, [west, south, east, north]: readonly [number, number, number, number] = DROUGHT_REGION): Ring | null {
  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
  for (const [x, y] of ring) { if (x < minX) minX = x; if (x > maxX) maxX = x; if (y < minY) minY = y; if (y > maxY) maxY = y; }
  if (maxX < west || minX > east || maxY < south || minY > north) return null;
  let points = ring.slice(0, ring.length - (ring[0][0] === ring[ring.length - 1][0] && ring[0][1] === ring[ring.length - 1][1] ? 1 : 0)).map(([x, y]) => [x, y]);
  if (minX < west || maxX > east || minY < south || maxY > north) {
    const sides: readonly [(p: Position) => boolean, (a: Position, b: Position) => Position][] = [
      [p => p[0] >= west, (a, b) => [west, a[1] + (b[1] - a[1]) * (west - a[0]) / (b[0] - a[0])]],
      [p => p[0] <= east, (a, b) => [east, a[1] + (b[1] - a[1]) * (east - a[0]) / (b[0] - a[0])]],
      [p => p[1] >= south, (a, b) => [a[0] + (b[0] - a[0]) * (south - a[1]) / (b[1] - a[1]), south]],
      [p => p[1] <= north, (a, b) => [a[0] + (b[0] - a[0]) * (north - a[1]) / (b[1] - a[1]), north]],
    ];
    for (const [inside, cross] of sides) {
      const out: Position[] = [];
      for (let i = 0; i < points.length; i++) {
        const current = points[i], previous = points[(i + points.length - 1) % points.length];
        if (inside(current)) { if (!inside(previous)) out.push(cross(previous, current)); out.push(current); }
        else if (inside(previous)) out.push(cross(previous, current));
      }
      points = out;
      if (!points.length) return null;
    }
  }
  const kept: Position[] = [];
  for (const [x, y] of points) {
    const p = [round(x), round(y)];
    const last = kept[kept.length - 1];
    if (!last || last[0] !== p[0] || last[1] !== p[1]) kept.push(p);
  }
  if (kept.length > 1 && kept[0][0] === kept[kept.length - 1][0] && kept[0][1] === kept[kept.length - 1][1]) kept.pop();
  return kept.length >= 3 ? [...kept, [...kept[0]]] : null;
}

const category = (properties: Record<string, unknown> | null): number | null => {
  const raw = properties?.DM ?? properties?.dm;
  const value = typeof raw === "number" ? raw : typeof raw === "string" && raw.trim() ? Number(raw) : NaN;
  return Number.isInteger(value) && value >= 0 && value <= 4 ? value : null;
};

export type DroughtFeature = Feature<Polygon | MultiPolygon, { dm: number }>;
export type DroughtMap = Readonly<{
  /** The map's valid Tuesday, "YYYYMMDD". */
  date: string;
  /** The categories' areas around Kansas, lowest category first. */
  data: FeatureCollection<Polygon | MultiPolygon, { dm: number }>;
  /** Share of Kansas (percent) in D0 or worse, D1 or worse … D4, measured on this map at 0.05° (about 5 km). */
  kansas: readonly number[];
  retrievedAt: string; source: string;
}>;

/**
 * The national USDM GeoJSON to the map drawn here: valid category areas only
 * (the category is `DM`, 0–4), cut to the region around Kansas, with the
 * share of Kansas in each category measured on it.
 */
export function parseUsdmMap(raw: unknown, date: string, retrievedAt: string, source: string): DroughtMap {
  const features = record(raw)?.features;
  if (!Array.isArray(features)) throw new Error("The Drought Monitor map was not a feature collection.");
  const kept: DroughtFeature[] = [];
  for (const candidate of features) {
    const feature = record(candidate), geometry = record(feature?.geometry), dm = category(record(feature?.properties));
    if (dm === null || !geometry) continue;
    const polygons = geometry.type === "Polygon" ? [geometry.coordinates] : geometry.type === "MultiPolygon" && Array.isArray(geometry.coordinates) ? geometry.coordinates : [];
    const clipped: Position[][][] = [];
    for (const polygon of polygons as unknown[]) {
      if (!Array.isArray(polygon) || !polygon.length) continue;
      const rings = polygon.map(finiteRing);
      if (!rings.every(Boolean)) continue;
      const outer = clipRing(rings[0]!);
      if (!outer) continue;
      clipped.push([outer, ...rings.slice(1).map(ring => clipRing(ring!)).filter((ring): ring is Ring => Boolean(ring))]);
    }
    if (!clipped.length) continue;
    kept.push({ type: "Feature", properties: { dm }, geometry: clipped.length === 1 ? { type: "Polygon", coordinates: clipped[0] } : { type: "MultiPolygon", coordinates: clipped } });
  }
  kept.sort((a, b) => a.properties.dm - b.properties.dm);
  const data = { type: "FeatureCollection" as const, features: kept };
  return Object.freeze({ date, data, kansas: Object.freeze(kansasShares(data)), retrievedAt, source });
}

/** The x positions where a horizontal line at `y` crosses a set of rings, sorted. */
function crossings(rings: readonly (readonly Position[])[], y: number): number[] {
  const xs: number[] = [];
  for (const ring of rings) for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
    const [xi, yi] = ring[i], [xj, yj] = ring[j];
    if ((yi > y) !== (yj > y)) xs.push(xi + (y - yi) * (xj - xi) / (yj - yi));
  }
  return xs.sort((a, b) => a - b);
}
const STEP = 0.05;
/**
 * The share of Kansas in each category or worse, measured at the centres of a
 * 0.05° grid (about 5.5 by 4.4 km) inside the state outline, each weighted by
 * its area (the cosine of its latitude). A point takes the highest category
 * whose area holds it, so nested and separate category areas read alike.
 */
export function kansasShares(data: DroughtMap["data"]): number[] {
  const features = data.features.map(feature => ({ dm: feature.properties.dm,
    rings: feature.geometry.type === "Polygon" ? feature.geometry.coordinates : feature.geometry.coordinates.flat() }));
  const totals = [0, 0, 0, 0, 0];
  let all = 0;
  for (let y = 37 + STEP / 2; y < 40.0; y += STEP) {
    const weight = Math.cos(y * Math.PI / 180);
    const state = crossings([KANSAS_OUTLINE as unknown as Position[]], y);
    const rows = features.map(feature => ({ dm: feature.dm, xs: crossings(feature.rings, y) }));
    for (let x = -102.05 + STEP / 2; x < -94.58; x += STEP) {
      if (state.filter(cross => cross < x).length % 2 === 0) continue;
      all += weight;
      let worst = -1;
      for (const row of rows) if (row.dm > worst && row.xs.filter(cross => cross < x).length % 2 === 1) worst = row.dm;
      for (let k = 0; k <= worst; k++) totals[k] += weight;
    }
  }
  return totals.map(total => all ? Math.round(total / all * 1000) / 10 : 0);
}

export type CountyDrought = Readonly<{
  geoid: string; name: string;
  /** Percent of the county in D0 or worse, D1 or worse … D4. */
  shares: readonly number[];
  /** The highest category reaching any part of the county, 0–4, or -1 for none. */
  worst: number;
}>;
const COUNTY_STEP = 0.02;
type CountyShape = { geoid: string; name: string; rings: Position[][]; south: number; north: number; weights: number[]; total: number };
/**
 * Each Kansas county's share in each category or worse, measured on the map
 * at the centres of a 0.02° grid (about 2.2 by 1.8 km, some 200 points a
 * county), weighted by area. Counties are the Census 2020 polygons the site
 * already reads; a county without a GEOID or polygon geometry is left out.
 */
export function countyDroughtShares(data: DroughtMap["data"], counties: FeatureCollection): CountyDrought[] {
  const shapes: CountyShape[] = [];
  for (const feature of counties.features) {
    const p = record(feature.properties), g = feature.geometry;
    const geoid = typeof p?.geoid === "string" ? p.geoid : null;
    if (!geoid || !g || (g.type !== "Polygon" && g.type !== "MultiPolygon")) continue;
    const rings = (g.type === "Polygon" ? g.coordinates : g.coordinates.flat()) as Position[][];
    const ys = rings.flat().map(point => point[1]);
    shapes.push({ geoid, name: typeof p?.name === "string" && p.name.trim() ? p.name.trim() : geoid, rings, south: Math.min(...ys), north: Math.max(...ys), weights: [0, 0, 0, 0, 0], total: 0 });
  }
  if (!shapes.length) return [];
  const categories = data.features.map(feature => ({ dm: feature.properties.dm,
    rings: feature.geometry.type === "Polygon" ? feature.geometry.coordinates : feature.geometry.coordinates.flat() }));
  const south = Math.min(...shapes.map(s => s.south)), north = Math.max(...shapes.map(s => s.north));
  const x0 = -103;
  for (let y = Math.floor(south / COUNTY_STEP) * COUNTY_STEP + COUNTY_STEP / 2; y < north; y += COUNTY_STEP) {
    const weight = Math.cos(y * Math.PI / 180);
    const rows = categories.map(category => ({ dm: category.dm, xs: crossings(category.rings, y) }));
    for (const shape of shapes) {
      if (y < shape.south || y > shape.north) continue;
      const xs = crossings(shape.rings, y);
      for (let i = 0; i + 1 < xs.length; i += 2) {
        for (let k = Math.ceil((xs[i] - x0) / COUNTY_STEP - 0.5); x0 + (k + 0.5) * COUNTY_STEP < xs[i + 1]; k++) {
          const x = x0 + (k + 0.5) * COUNTY_STEP;
          shape.total += weight;
          let worst = -1;
          for (const row of rows) if (row.dm > worst && row.xs.filter(cross => cross < x).length % 2 === 1) worst = row.dm;
          for (let c = 0; c <= worst; c++) shape.weights[c] += weight;
        }
      }
    }
  }
  return shapes.filter(shape => shape.total > 0).map(shape => {
    const shares = shape.weights.map(w => Math.round(w / shape.total * 1000) / 10);
    let worst = -1;
    for (let c = 0; c < 5; c++) if (shape.weights[c] > 0) worst = c;
    return Object.freeze({ geoid: shape.geoid, name: shape.name, shares: Object.freeze(shares), worst });
  });
}
const percentOf = (value: number) => value >= 99.95 ? "all" : value < 0.05 ? "none" : `${value < 10 ? value.toFixed(1) : Math.round(value)}%`;
/** Counties for a keyboard list: the most severe first (highest category, then the most of the county in it), each with its worst category and its share in drought. */
export function countyDroughtList(counties: readonly CountyDrought[]): readonly Readonly<{ id: string; label: string }>[] {
  return [...counties].sort((a, b) => b.worst - a.worst || (b.worst >= 0 ? b.shares[b.worst] - a.shares[a.worst] : 0) || b.shares[1] - a.shares[1] || a.name.localeCompare(b.name))
    .map(county => ({ id: county.geoid, label: county.worst < 0 ? `${county.name} · none` : `${county.name} · ${USDM_CATEGORIES[county.worst].id} on ${percentOf(county.shares[county.worst])}${county.worst >= 1 ? ` · drought on ${percentOf(county.shares[1])}` : ""}` }));
}
/** How many counties each category reaches (any part of the county). */
export function countyDroughtSummary(counties: readonly CountyDrought[]): string {
  const reach = (c: number) => counties.filter(county => county.worst >= c).length;
  return `Counties reached: D1–D4 ${reach(1)} · D2+ ${reach(2)} · D3+ ${reach(3)} · D4 ${reach(4)} of ${counties.length} · measured on the map`;
}
/** One county's shares, in the order of the key. */
export function countyDroughtReading(county: CountyDrought, date: string): string {
  return `${county.name} County · valid ${usdmDateLabel(date)} · ${USDM_CATEGORIES.map((c, i) => `${i === 4 ? c.id : `${c.id}+`} ${percentOf(county.shares[i])}`).join(" · ")} · measured on the map`;
}

export type DroughtWeek = Readonly<{ date: string; /** Percent of Kansas in D0 or worse … D4. */ shares: readonly number[] }>;
export type DroughtSeries = Readonly<{ weeks: readonly DroughtWeek[]; retrievedAt: string; source: string }>;

const toCompact = (value: unknown): string | null => {
  if (typeof value !== "string" && typeof value !== "number") return null;
  const text = String(value).trim();
  const iso = /^(\d{4})-(\d{2})-(\d{2})/.exec(text), us = /^(\d{1,2})\/(\d{1,2})\/(\d{4})/.exec(text);
  const candidate = /^\d{8}$/.test(text) ? text : iso ? `${iso[1]}${iso[2]}${iso[3]}` : us ? `${us[3]}${us[1].padStart(2, "0")}${us[2].padStart(2, "0")}` : null;
  return candidate && compactMs(candidate) !== null ? candidate : null;
};
const percent = (value: unknown): number | null => {
  const n = typeof value === "number" ? value : typeof value === "string" && value.trim() ? Number(value.trim()) : NaN;
  return Number.isFinite(n) && n >= -0.01 && n <= 100.01 ? Math.min(100, Math.max(0, n)) : null;
};
/** CSV text to rows keyed by its header. */
function csvRows(text: string): Record<string, string>[] {
  const lines = text.split(/\r?\n/).filter(line => line.trim());
  const cells = (line: string) => line.split(",").map(cell => cell.trim().replace(/^"|"$/g, ""));
  const header = cells(lines[0] ?? "");
  return lines.slice(1).map(line => Object.fromEntries(cells(line).map((cell, i) => [header[i], cell])));
}

/**
 * The USDM state statistics (percent of area) to Kansas's weekly series. The
 * service answers JSON or CSV; field names are matched without regard to
 * case. Cumulative statistics (D0 = D0 or worse) are what is asked for; a
 * categorical answer, recognised by its shares summing to 100 with None, is
 * accumulated so the series always reads "this category or worse".
 */
export function parseUsdmSeries(text: string, retrievedAt: string, source: string): DroughtSeries {
  let rows: unknown[];
  try {
    const value = JSON.parse(text) as unknown;
    rows = Array.isArray(value) ? value : Array.isArray(record(value)?.data) ? record(value)!.data as unknown[] : [];
  } catch { rows = csvRows(text); }
  const weeks = new Map<string, DroughtWeek>();
  for (const candidate of rows) {
    const row = record(candidate);
    if (!row) continue;
    const field = (name: string) => { const key = Object.keys(row).find(k => k.toLowerCase() === name.toLowerCase()); return key === undefined ? undefined : row[key]; };
    const date = toCompact(field("MapDate")) ?? toCompact(field("ValidStart"));
    const values = ["D0", "D1", "D2", "D3", "D4"].map(name => percent(field(name)));
    if (!date || !isUsdmDate(date) || values.some(value => value === null)) continue;
    const d = values as number[], none = percent(field("None"));
    const categorical = none !== null ? Math.abs(none + d[0] - 100) > 0.6 && Math.abs(none + d.reduce((a, b) => a + b, 0) - 100) <= 0.6
      : d.some((value, i) => i > 0 && value > d[i - 1] + 0.01);
    const shares = categorical ? d.map((_, i) => Math.min(100, d.slice(i).reduce((a, b) => a + b, 0))) : d;
    weeks.set(date, Object.freeze({ date, shares: Object.freeze(shares.map(value => Math.round(value * 100) / 100)) }));
  }
  if (!weeks.size) throw new Error("The Drought Monitor statistics held no Kansas weeks.");
  return Object.freeze({ weeks: Object.freeze([...weeks.values()].sort((a, b) => a.date.localeCompare(b.date))), retrievedAt, source });
}

const shareList = (value: unknown): boolean => Array.isArray(value) && value.length === 5 && value.every(v => typeof v === "number" && v >= 0 && v <= 100);
export function validDroughtMap(value: unknown): value is DroughtMap {
  const candidate = record(value), data = record(candidate?.data);
  return Boolean(candidate) && isUsdmDate(candidate!.date) && typeof candidate!.retrievedAt === "string" && shareList(candidate!.kansas)
    && data?.type === "FeatureCollection" && Array.isArray(data.features) && data.features.every(feature => {
      const f = record(feature), g = record(f?.geometry);
      return category(record(f?.properties)) !== null && (g?.type === "Polygon" || g?.type === "MultiPolygon");
    });
}
export function validDroughtSeries(value: unknown): value is DroughtSeries {
  const candidate = record(value);
  return Boolean(candidate) && typeof candidate!.retrievedAt === "string" && Array.isArray(candidate!.weeks) && candidate!.weeks.length > 0
    && candidate!.weeks.every(week => { const w = record(week); return isUsdmDate(w?.date) && shareList(w?.shares); });
}

/** While shown, the newest map is read again once it is an hour old, and the Kansas series once it is six hours old; past weeks are kept as published. */
export const DROUGHT_NEWEST_REFRESH_MS = 60 * 60 * 1000;
export const DROUGHT_SERIES_REFRESH_MS = 6 * 60 * 60 * 1000;
/**
 * The maps kept in the page after `id` is read: the newest, and the `limit`
 * dated weeks read most recently, `id` among them. A Map keeps the order the
 * weeks were read in (an object would list "YYYYMMDD" keys numerically).
 */
export function rememberDroughtMap(current: ReadonlyMap<string, DroughtMap>, id: string, map: DroughtMap, limit = 12): Map<string, DroughtMap> {
  const next = new Map(current);
  next.delete(id);
  next.set(id, map);
  const older = [...next.keys()].filter(key => key !== "newest" && key !== id);
  for (const key of older.slice(0, Math.max(0, older.length - (id === "newest" ? limit : limit - 1)))) next.delete(key);
  return next;
}

const weekOf = (series: DroughtSeries | null, date: string) => series?.weeks.find(week => week.date === date) ?? null;
const pct = (value: number) => value < 0.05 ? "none" : `${value < 10 ? value.toFixed(1) : Math.round(value)}%`;

/**
 * What the shown map says for Kansas: the share in drought (D1–D4) and in
 * each worse category. The USDM's own statistics are used for the week when
 * they are in hand; otherwise the share measured on the map, marked as such.
 */
export function droughtReading(map: DroughtMap, series: DroughtSeries | null): string {
  const official = weekOf(series, map.date);
  const s = official?.shares ?? map.kansas, about = official ? "" : "≈ ";
  const parts = [`Valid ${usdmDateLabel(map.date)}`,
    s[1] < 0.05 ? (s[0] < 0.05 ? "no part of Kansas abnormally dry or in drought" : `no drought in Kansas; ${about}${pct(s[0])} abnormally dry`)
      : `${about}${pct(s[1])} of Kansas in drought (D1–D4)`];
  if (s[1] >= 0.05) parts.push(`D2+ ${about}${pct(s[2])}`, `D3+ ${about}${pct(s[3])}`, `D4 ${about}${pct(s[4])}`);
  if (!official) parts.push("shares measured on the map");
  return parts.join(" · ");
}

/** The key: the five categories in the colours drawn. */
export function droughtKey(date: string): MapKey {
  return Object.freeze({
    id: "usdm", title: `U.S. Drought Monitor · ${usdmDateLabel(date)}`,
    items: Object.freeze(USDM_CATEGORIES.map(c => Object.freeze({ label: `${c.id} ${c.name}`, color: c.color, shape: "area" as const }))),
    note: "Drought intensity as the USDM authors assess it each week from many indicators and local reports, valid Tuesday 8 a.m. Eastern and released Thursday. D0 is abnormally dry, not drought. A weekly assessment, not a forecast or a measurement at a point.",
  });
}

const fillColor = ["match", ["get", "dm"], ...USDM_CATEGORIES.flatMap(c => [c.dm, c.color]), "#9aa5ad"];
const shown = new WeakMap<MapLibreMap, DroughtMap["data"]>();
/** Draws the map's category areas (or removes them, for null). Safe to call on every style load. */
const shownCounties = new WeakMap<MapLibreMap, FeatureCollection>();
/**
 * Draws the map's category areas (or removes them, for null), with the
 * county lines over them once the counties are in hand and the picked
 * county outlined. Safe to call on every style load.
 */
export function syncDroughtMonitor(map: MapLibreMap, drought: DroughtMap | null, counties: FeatureCollection | null = null, selected: string | null = null): void {
  if (!drought) {
    for (const id of [DROUGHT_STATE_LAYER_ID, DROUGHT_COUNTY_SELECTED_LAYER_ID, DROUGHT_COUNTY_LAYER_ID, DROUGHT_LINE_LAYER_ID, DROUGHT_FILL_LAYER_ID]) if (map.getLayer(id)) map.removeLayer(id);
    for (const id of [DROUGHT_STATE_SOURCE_ID, DROUGHT_COUNTY_SOURCE_ID, DROUGHT_SOURCE_ID]) if (map.getSource(id)) map.removeSource(id);
    shown.delete(map);
    shownCounties.delete(map);
    return;
  }
  const source = map.getSource(DROUGHT_SOURCE_ID) as GeoJSONSource | undefined;
  if (!source) map.addSource(DROUGHT_SOURCE_ID, { type: "geojson", data: drought.data });
  else if (shown.get(map) !== drought.data) source.setData(drought.data);
  shown.set(map, drought.data);
  // Above the base and the provider layers, under the site's own overlays and labels.
  const before = map.getStyle().layers?.find(layer => layer.id.startsWith("kfm-") && layer.id !== "kfm-background" && !layer.id.startsWith(DROUGHT_SOURCE_ID))?.id;
  // Nearly opaque, as the USDM draws its map: worse categories are drawn last, over the milder ones.
  if (!map.getLayer(DROUGHT_FILL_LAYER_ID)) map.addLayer({ id: DROUGHT_FILL_LAYER_ID, type: "fill", source: DROUGHT_SOURCE_ID,
    layout: { "fill-sort-key": ["get", "dm"] as never }, paint: { "fill-color": fillColor as never, "fill-opacity": 0.82, "fill-antialias": true } }, before);
  if (!map.getLayer(DROUGHT_LINE_LAYER_ID)) map.addLayer({ id: DROUGHT_LINE_LAYER_ID, type: "line", source: DROUGHT_SOURCE_ID,
    layout: { "line-join": "round" }, paint: { "line-color": "#3b2d14", "line-width": ["interpolate", ["linear"], ["zoom"], 5, 0.5, 9, 1.1] as never, "line-opacity": 0.55 } }, before);
  if (!map.getSource(DROUGHT_STATE_SOURCE_ID)) map.addSource(DROUGHT_STATE_SOURCE_ID, { type: "geojson",
    data: { type: "Feature", properties: {}, geometry: { type: "Polygon", coordinates: [[...KANSAS_OUTLINE, KANSAS_OUTLINE[0]] as Position[]] } } });
  if (!map.getLayer(DROUGHT_STATE_LAYER_ID)) map.addLayer({ id: DROUGHT_STATE_LAYER_ID, type: "line", source: DROUGHT_STATE_SOURCE_ID,
    layout: { "line-join": "round" }, paint: { "line-color": "#1d1a14", "line-width": ["interpolate", ["linear"], ["zoom"], 4, 1.4, 9, 2.6] as never, "line-opacity": 0.9 } }, before);
  if (!counties) return;
  const countySource = map.getSource(DROUGHT_COUNTY_SOURCE_ID) as GeoJSONSource | undefined;
  if (!countySource) map.addSource(DROUGHT_COUNTY_SOURCE_ID, { type: "geojson", data: counties });
  else if (shownCounties.get(map) !== counties) countySource.setData(counties);
  shownCounties.set(map, counties);
  // Under the state line, over the categories.
  if (!map.getLayer(DROUGHT_COUNTY_LAYER_ID)) map.addLayer({ id: DROUGHT_COUNTY_LAYER_ID, type: "line", source: DROUGHT_COUNTY_SOURCE_ID,
    layout: { "line-join": "round" }, paint: { "line-color": "#2a2418", "line-width": ["interpolate", ["linear"], ["zoom"], 5, 0.5, 9, 1.2] as never, "line-opacity": 0.6 } }, DROUGHT_STATE_LAYER_ID);
  if (!map.getLayer(DROUGHT_COUNTY_SELECTED_LAYER_ID)) map.addLayer({ id: DROUGHT_COUNTY_SELECTED_LAYER_ID, type: "line", source: DROUGHT_COUNTY_SOURCE_ID,
    layout: { "line-join": "round" }, paint: { "line-color": "#f7f4ea", "line-width": ["interpolate", ["linear"], ["zoom"], 5, 2.2, 9, 3.6] as never, "line-opacity": 1 } }, DROUGHT_STATE_LAYER_ID);
  map.setFilter(DROUGHT_COUNTY_SELECTED_LAYER_ID, ["==", ["get", "geoid"], selected ?? ""] as never);
}
