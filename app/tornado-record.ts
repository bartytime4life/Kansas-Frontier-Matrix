import type { Feature, FeatureCollection, LineString, Point } from "geojson";
import type { GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";
import type { MapKey } from "./map-keys";

/**
 * Every Kansas tornado since 1950, from the Storm Prediction Center's severe
 * weather database (the "actual tornadoes" file: one row per tornado, the
 * whole track). Each track is drawn as the straight line from touchdown to
 * lift-off, the only path the database records.
 */

export const SPC_TORNADO_FIRST_YEAR = 1950;
export const SPC_TORNADO_PAGE = "https://www.spc.noaa.gov/wcm/";
/** The database is released each spring for the year before; the newest file that answers is used. */
export const tornadoCsvCandidates = (now: Date) => Array.from({ length: 4 }, (_, i) => now.getUTCFullYear() - 1 - i)
  .map(year => `https://www.spc.noaa.gov/wcm/data/1950-${year}_actual_tornadoes.csv`);

/** F scale until February 2007, Enhanced Fujita (EF) after; one colour per rating, light to dark. */
export const TORNADO_RATINGS = Object.freeze([
  { id: 0, name: "F/EF0", color: "#d9ef8b" },
  { id: 1, name: "F/EF1", color: "#fee08b" },
  { id: 2, name: "F/EF2", color: "#fdae61" },
  { id: 3, name: "F/EF3", color: "#f46d43" },
  { id: 4, name: "F/EF4", color: "#d73027" },
  { id: 5, name: "F/EF5", color: "#7f0000" },
] as const);
export const UNRATED_COLOR = "#9e9e9e";
export const ratingColor = (rating: number | null) => rating === null ? UNRATED_COLOR : TORNADO_RATINGS[rating]?.color ?? UNRATED_COLOR;
/** "F3" or "EF3": the Enhanced Fujita scale replaced the Fujita scale on February 1, 2007. */
export const ratingName = (rating: number | null, date: string) => rating === null ? "unrated" : `${date >= "2007-02-01" ? "EF" : "F"}${rating}`;

export type Tornado = Readonly<{
  id: string;
  year: number;
  /** YYYY-MM-DD, local (Central Standard) date as the SPC records it. */
  date: string;
  time: string | null;
  rating: number | null;
  /** null where the SPC records the count as unknown (-9). */
  injuries: number | null;
  fatalities: number | null;
  start: readonly [number, number];
  end: readonly [number, number] | null;
  lengthMiles: number | null;
  widthYards: number | null;
  states: number;
}>;
export type TornadoRecord = Readonly<{ retrievedAt: string; source: string; firstYear: number; lastYear: number; tornadoes: readonly Tornado[]; skipped: number }>;

/** Kansas and a few kilometres: a track that starts or ends inside is Kansas's. */
const KANSAS = { west: -102.06, east: -94.58, south: 36.99, north: 40.01 };
const inKansas = (p: readonly [number, number]) => p[0] >= KANSAS.west && p[0] <= KANSAS.east && p[1] >= KANSAS.south && p[1] <= KANSAS.north;

/**
 * Kansas's tornadoes from the CSV, read by column name: those whose row is
 * Kansas's, and multi-state tracks that start or end in Kansas. Unknown values
 * (-9) are kept as unknown; an end point of 0,0 means none was recorded.
 */
export function parseTornadoCsv(text: string, retrievedAt: string, source: string): TornadoRecord {
  const lines = text.split(/\r?\n/).filter(line => line.trim());
  const header = (lines.shift() ?? "").split(",").map(name => name.trim().toLowerCase());
  const col = (name: string) => header.indexOf(name);
  const required = ["yr", "mo", "dy", "st", "mag", "inj", "fat", "slat", "slon", "elat", "elon", "len", "wid"];
  if (required.some(name => col(name) < 0)) throw new Error("The SPC tornado file's columns changed.");
  const tornadoes: Tornado[] = [];
  let skipped = 0;
  for (const line of lines) {
    const cell = line.split(",");
    const get = (name: string) => col(name) < 0 ? "" : (cell[col(name)] ?? "").trim();
    const num = (name: string) => { const v = Number(get(name)); return Number.isFinite(v) ? v : Number.NaN; };
    const year = num("yr"), month = num("mo"), day = num("dy");
    const start: [number, number] = [num("slon"), num("slat")];
    const endRaw: [number, number] = [num("elon"), num("elat")];
    const end = endRaw[0] !== 0 && endRaw[1] !== 0 && Number.isFinite(endRaw[0]) && Number.isFinite(endRaw[1]) ? endRaw : null;
    const states = col("ns") < 0 ? 1 : Math.max(1, num("ns") || 1);
    const kansas = get("st") === "KS" || (states > 1 && (inKansas(start) || (end !== null && inKansas(end))));
    if (!kansas) continue;
    if (!Number.isInteger(year) || year < SPC_TORNADO_FIRST_YEAR || !Number.isInteger(month) || month < 1 || month > 12 || !Number.isInteger(day) || day < 1 || day > 31
      || !Number.isFinite(start[0]) || !Number.isFinite(start[1]) || start[0] > -60 || start[1] < 20) { skipped++; continue; }
    const mag = num("mag"), len = num("len"), wid = num("wid");
    // A casualty count of -9 (or none) is unknown, not zero.
    const count = (v: number) => Number.isInteger(v) && v >= 0 ? v : null;
    const om = get("om");
    tornadoes.push(Object.freeze({
      id: `${year}-${om || tornadoes.length}`,
      year, date: `${year}-${String(month).padStart(2, "0")}-${String(day).padStart(2, "0")}`, time: /^\d{1,2}:\d\d(:\d\d)?$/.test(get("time")) ? get("time").slice(0, 5) : null,
      rating: Number.isInteger(mag) && mag >= 0 && mag <= 5 ? mag : null,
      injuries: count(num("inj")), fatalities: count(num("fat")),
      start: Object.freeze(start), end: end ? Object.freeze(end) : null,
      lengthMiles: len > 0 ? len : null, widthYards: wid > 0 ? wid : null, states,
    }));
  }
  if (!tornadoes.length) throw new Error("The SPC tornado file had no Kansas tornadoes.");
  tornadoes.sort((a, b) => a.date.localeCompare(b.date) || (a.time ?? "").localeCompare(b.time ?? ""));
  const years = tornadoes.map(t => t.year);
  return Object.freeze({ retrievedAt, source, firstYear: Math.min(SPC_TORNADO_FIRST_YEAR, ...years), lastYear: Math.max(...years), tornadoes: Object.freeze(tornadoes), skipped });
}

export function validTornadoRecord(value: unknown): value is TornadoRecord {
  const v = value as TornadoRecord;
  return Boolean(v) && typeof v === "object" && Array.isArray(v.tornadoes) && typeof v.firstYear === "number" && typeof v.lastYear === "number"
    && v.tornadoes.every(t => t && typeof t.id === "string" && typeof t.year === "number" && Array.isArray(t.start));
}

export type TornadoFilter = Readonly<{ year: number | null; minRating: number }>;
export const TORNADO_DEFAULT_FILTER: TornadoFilter = Object.freeze({ year: null, minRating: 0 });
/** The tornadoes a view shows: a year or all, at or above a rating (0 includes the unrated). */
export const tornadoSelect = (record: Pick<TornadoRecord, "tornadoes">, filter: TornadoFilter) =>
  record.tornadoes.filter(t => (filter.year === null || t.year === filter.year) && (filter.minRating === 0 || (t.rating ?? -1) >= filter.minRating));

export type TornadoYear = Readonly<{ year: number; total: number; byRating: readonly number[] }>;
/** Tornadoes per year by rating (index 0–5, then unrated), every year of the record; the year filter is not applied. */
export function tornadoYears(record: TornadoRecord, filter: TornadoFilter): TornadoYear[] {
  const chosen = tornadoSelect(record, { ...filter, year: null });
  return Array.from({ length: record.lastYear - record.firstYear + 1 }, (_, i) => {
    const year = record.firstYear + i, ofYear = chosen.filter(t => t.year === year);
    const byRating = [0, 1, 2, 3, 4, 5].map(r => ofYear.filter(t => t.rating === r).length).concat(ofYear.filter(t => t.rating === null).length);
    return { year, total: ofYear.length, byRating };
  });
}

const DATE = new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: "short", day: "numeric", year: "numeric" });
export const tornadoDate = (t: Tornado) => DATE.format(Date.parse(`${t.date}T00:00:00Z`));
/** The record's notable tornadoes: strongest first, then deadliest, then longest; at most 60. */
export function tornadoList(tornadoes: readonly Tornado[]): { id: string; label: string }[] {
  return [...tornadoes].sort((a, b) => (b.rating ?? -1) - (a.rating ?? -1) || (b.fatalities ?? 0) - (a.fatalities ?? 0) || (b.lengthMiles ?? 0) - (a.lengthMiles ?? 0) || a.date.localeCompare(b.date))
    .slice(0, 60).map(t => ({ id: t.id, label: `${ratingName(t.rating, t.date)} · ${tornadoDate(t)}${t.fatalities ? ` · ${t.fatalities} killed` : ""}${t.lengthMiles ? ` · ${t.lengthMiles.toFixed(1)} mi` : ""}` }));
}

const plural = (n: number, one: string, many: string) => `${n.toLocaleString("en-US")} ${n === 1 ? one : many}`;
/** The statewide line for the view. */
export function tornadoReading(record: TornadoRecord, filter: TornadoFilter, chosen: readonly Tornado[]): string {
  const rating = filter.minRating ? ` of F/EF${filter.minRating} or stronger` : "";
  const span = filter.year !== null ? `in ${filter.year}` : `${record.firstYear}–${record.lastYear}`;
  const killed = chosen.reduce((sum, t) => sum + (t.fatalities ?? 0), 0);
  const unknown = chosen.filter(t => t.fatalities === null).length;
  return `${plural(chosen.length, "tornado", "tornadoes")}${rating} in Kansas, ${span}${killed ? ` · ${plural(killed, "death", "deaths")}` : ""}${unknown ? ` · ${unknown} with deaths unknown` : ""}`;
}

const coordinate = (p: readonly [number, number]) => `${Math.abs(p[1]).toFixed(2)}°N, ${Math.abs(p[0]).toFixed(2)}°W`;
/** One tornado in words: rating, date and time, casualties, and the track. */
export function tornadoDetail(t: Tornado): string {
  return [`${ratingName(t.rating, t.date)} · ${tornadoDate(t)}${t.time ? ` ${t.time} CST` : ""}`,
    // "No casualties" only when both counts are a recorded zero; an unknown count is named, beside the other.
    t.fatalities === null && t.injuries === null ? "casualties unknown"
      : t.fatalities === 0 && t.injuries === 0 ? "no casualties recorded"
      : `${t.fatalities === null ? "deaths unknown" : plural(t.fatalities, "death", "deaths")}, ${t.injuries === null ? "injuries unknown" : plural(t.injuries, "injury", "injuries")}`,
    `touchdown ${coordinate(t.start)}${t.end ? ` · lift-off ${coordinate(t.end)}` : ""}`,
    [t.lengthMiles ? `${t.lengthMiles.toFixed(1)} mi long` : null, t.widthYards ? `${t.widthYards.toLocaleString("en-US")} yd wide` : null].filter(Boolean).join(", ") || null,
    t.states > 1 ? `crossed ${t.states} states` : null].filter(Boolean).join(" · ");
}

export function tornadoKey(record: TornadoRecord, filter: TornadoFilter): MapKey {
  return Object.freeze({
    id: "spc-tornadoes",
    title: `Kansas tornadoes · ${filter.year ?? `${record.firstYear}–${record.lastYear}`}`,
    items: Object.freeze([...TORNADO_RATINGS.map(r => Object.freeze({ label: r.name, color: r.color, shape: "line" as const })),
      Object.freeze({ label: "Unrated", color: UNRATED_COLOR, shape: "line" as const })]),
    note: "SPC severe weather database. Each track is the straight line from touchdown to lift-off, not the path on the ground. F scale before February 2007, EF after; ratings are from damage, so a tornado over open country may be rated low.",
  });
}

export const TORNADO_SOURCE_ID = "kfm-spc-tornadoes";
export const TORNADO_LINE_LAYER_ID = "kfm-spc-tornadoes-track";
export const TORNADO_POINT_LAYER_ID = "kfm-spc-tornadoes-touchdown";
export const TORNADO_SELECTED_LAYER_ID = "kfm-spc-tornadoes-selected";
export const TORNADO_SELECTED_POINT_LAYER_ID = "kfm-spc-tornadoes-selected-touchdown";

/** Tracks (or touchdown points where no lift-off was recorded), strongest drawn last. */
export function tornadoCollection(tornadoes: readonly Tornado[]): FeatureCollection<LineString | Point> {
  return { type: "FeatureCollection", features: [...tornadoes].sort((a, b) => (a.rating ?? -1) - (b.rating ?? -1)).map((t): Feature<LineString | Point> => ({
    type: "Feature", id: t.id,
    geometry: t.end ? { type: "LineString", coordinates: [[t.start[0], t.start[1]], [t.end[0], t.end[1]]] } : { type: "Point", coordinates: [t.start[0], t.start[1]] },
    properties: { id: t.id, rating: t.rating ?? -1, color: ratingColor(t.rating) },
  })) };
}

const shown = new WeakMap<MapLibreMap, FeatureCollection>();
/** The tornado tracks (or nothing, for null) under the site's overlays, wider for stronger ratings, with the picked one outlined. */
export function syncTornadoRecord(map: MapLibreMap, collection: FeatureCollection | null, selected: string | null = null): void {
  if (!collection) {
    for (const id of [TORNADO_SELECTED_POINT_LAYER_ID, TORNADO_SELECTED_LAYER_ID, TORNADO_POINT_LAYER_ID, TORNADO_LINE_LAYER_ID]) if (map.getLayer(id)) map.removeLayer(id);
    if (map.getSource(TORNADO_SOURCE_ID)) map.removeSource(TORNADO_SOURCE_ID);
    shown.delete(map);
    return;
  }
  const source = map.getSource(TORNADO_SOURCE_ID) as GeoJSONSource | undefined;
  if (!source) map.addSource(TORNADO_SOURCE_ID, { type: "geojson", data: collection });
  else if (shown.get(map) !== collection) source.setData(collection);
  shown.set(map, collection);
  const before = map.getStyle().layers?.find(layer => layer.id.startsWith("kfm-") && layer.id !== "kfm-background" && !layer.id.startsWith(TORNADO_SOURCE_ID))?.id;
  const width = ["interpolate", ["linear"], ["zoom"], 5, ["+", 0.8, ["*", 0.45, ["max", 0, ["get", "rating"]]]], 10, ["+", 2, ["*", 1.2, ["max", 0, ["get", "rating"]]]]];
  if (!map.getLayer(TORNADO_LINE_LAYER_ID)) map.addLayer({ id: TORNADO_LINE_LAYER_ID, type: "line", source: TORNADO_SOURCE_ID, filter: ["==", ["geometry-type"], "LineString"] as never,
    layout: { "line-cap": "round" }, paint: { "line-color": ["get", "color"] as never, "line-width": width as never, "line-opacity": 0.9 } }, before);
  if (!map.getLayer(TORNADO_POINT_LAYER_ID)) map.addLayer({ id: TORNADO_POINT_LAYER_ID, type: "circle", source: TORNADO_SOURCE_ID, filter: ["==", ["geometry-type"], "Point"] as never,
    paint: { "circle-color": ["get", "color"] as never, "circle-radius": ["interpolate", ["linear"], ["zoom"], 5, 2, 10, 4] as never, "circle-stroke-color": "#1b1b1b", "circle-stroke-width": 0.5 } }, before);
  if (!map.getLayer(TORNADO_SELECTED_LAYER_ID)) map.addLayer({ id: TORNADO_SELECTED_LAYER_ID, type: "line", source: TORNADO_SOURCE_ID,
    layout: { "line-cap": "round" }, paint: { "line-color": "#ffffff", "line-width": ["interpolate", ["linear"], ["zoom"], 5, 7, 10, 16] as never, "line-opacity": 0.95 } }, TORNADO_LINE_LAYER_ID);
  // A tornado with no lift-off point is a touchdown dot; picked, it gets a ring.
  if (!map.getLayer(TORNADO_SELECTED_POINT_LAYER_ID)) map.addLayer({ id: TORNADO_SELECTED_POINT_LAYER_ID, type: "circle", source: TORNADO_SOURCE_ID,
    paint: { "circle-color": "rgba(0,0,0,0)", "circle-radius": ["interpolate", ["linear"], ["zoom"], 5, 6, 10, 10] as never, "circle-stroke-color": "#ffffff", "circle-stroke-width": 2.2 } }, before);
  map.setFilter(TORNADO_SELECTED_LAYER_ID, ["all", ["==", ["geometry-type"], "LineString"], ["==", ["get", "id"], selected ?? ""]] as never);
  map.setFilter(TORNADO_SELECTED_POINT_LAYER_ID, ["all", ["==", ["geometry-type"], "Point"], ["==", ["get", "id"], selected ?? ""]] as never);
}
