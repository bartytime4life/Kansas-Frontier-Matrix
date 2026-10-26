import type { ExpressionSpecification, GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";
import type { Feature, FeatureCollection, Point } from "geojson";
import { KANSAS_OUTLINE } from "./kansas-orientation";
import type { MapKey } from "./map-keys";

/**
 * The instrumental earthquake record for Kansas: every USGS ComCat event of
 * magnitude 2.5 or more since 1973 whose epicentre lies inside the state. It
 * is drawn on the Landform relief map beside the rolling 30-day catalog, and
 * coloured by year, so the 2014–2016 rise in south-central Kansas reads
 * against the decades before it.
 */
export const EARTHQUAKE_RECORD_START_YEAR = 1973;
export const EARTHQUAKE_RECORD_MIN_MAGNITUDE = 2.5;
/** The provider query asks for one more than this, so a full answer is known to be cut short. */
export const EARTHQUAKE_RECORD_LIMIT = 6000;
export const EARTHQUAKE_RECORD_PROVIDER = "https://earthquake.usgs.gov/fdsnws/event/1/query";
export const EARTHQUAKE_RECORD_SOURCE_ID = "kfm-earthquake-record";
export const EARTHQUAKE_RECORD_LAYER_ID = "kfm-earthquake-record-points";
export const EARTHQUAKE_RECORD_SELECTED_LAYER_ID = "kfm-earthquake-record-selected";

/** The USGS query: the state's bounding box, all of it, from 1 January 1973 to now. */
export const earthquakeRecordProviderUrl = (now: Date): string => {
  const url = new URL(EARTHQUAKE_RECORD_PROVIDER);
  for (const [key, value] of Object.entries({
    format: "geojson", eventtype: "earthquake", starttime: `${EARTHQUAKE_RECORD_START_YEAR}-01-01T00:00:00Z`, endtime: now.toISOString(),
    minmagnitude: String(EARTHQUAKE_RECORD_MIN_MAGNITUDE), minlatitude: "36.99", maxlatitude: "40.01", minlongitude: "-102.06", maxlongitude: "-94.58",
    orderby: "time-asc", limit: String(EARTHQUAKE_RECORD_LIMIT + 1),
  })) url.searchParams.set(key, value);
  return url.href;
};

/** Ray casting against the Census state outline (a few hundred metres at the border; epicentres are uncertain by more). */
export function insideKansas(longitude: number, latitude: number): boolean {
  let inside = false;
  for (let i = 0, j = KANSAS_OUTLINE.length - 1; i < KANSAS_OUTLINE.length; j = i++) {
    const [xi, yi] = KANSAS_OUTLINE[i], [xj, yj] = KANSAS_OUTLINE[j];
    if ((yi > latitude) !== (yj > latitude) && longitude < (xj - xi) * (latitude - yi) / (yj - yi) + xi) inside = !inside;
  }
  return inside;
}

export type EarthquakeRecordEvent = Readonly<{
  id: string; time: string; year: number; magnitude: number; magnitudeType: string | null;
  depthKilometers: number | null; place: string | null; status: string | null; longitude: number; latitude: number;
}>;
export type EarthquakeRecord = Readonly<{
  events: readonly EarthquakeRecordEvent[]; startYear: number; endYear: number; minMagnitude: number;
  /** Events the bounding box returned whose epicentres are outside Kansas. */
  outsideKansas: number; truncated: boolean; retrievedAt: string; source: string;
}>;

const finite = (value: unknown): number | null => typeof value === "number" && Number.isFinite(value) ? value : null;
const text = (value: unknown): string | null => typeof value === "string" && value.trim() ? value.trim() : null;
const record = (value: unknown): Record<string, unknown> | null => value && typeof value === "object" && !Array.isArray(value) ? value as Record<string, unknown> : null;

/** USGS GeoJSON to the Kansas record. Events without an id, time, magnitude or position are left out. */
export function parseEarthquakeRecord(raw: unknown, retrievedAt: string, source: string): EarthquakeRecord {
  const features = record(raw)?.features;
  if (!Array.isArray(features)) throw new Error("The USGS catalog answer was not a feature collection.");
  const endYear = new Date(retrievedAt).getUTCFullYear();
  const events: EarthquakeRecordEvent[] = [];
  let outsideKansas = 0;
  for (const candidate of features.slice(0, EARTHQUAKE_RECORD_LIMIT)) {
    const feature = record(candidate), properties = record(feature?.properties), geometry = record(feature?.geometry);
    const coordinates = geometry?.type === "Point" && Array.isArray(geometry.coordinates) ? geometry.coordinates : null;
    const id = text(feature?.id), at = finite(properties?.time), magnitude = finite(properties?.mag);
    const longitude = finite(coordinates?.[0]), latitude = finite(coordinates?.[1]);
    if (!id || !/^[a-z0-9]{2,32}$/i.test(id) || at === null || magnitude === null || magnitude < EARTHQUAKE_RECORD_MIN_MAGNITUDE || longitude === null || latitude === null) continue;
    if (text(properties?.type) && properties?.type !== "earthquake") continue;
    if (!insideKansas(longitude, latitude)) { outsideKansas++; continue; }
    const time = new Date(at);
    const year = time.getUTCFullYear();
    if (year < EARTHQUAKE_RECORD_START_YEAR || year > endYear) continue;
    events.push(Object.freeze({
      id, time: time.toISOString(), year, magnitude: Math.round(magnitude * 10) / 10, magnitudeType: text(properties?.magType),
      depthKilometers: finite(coordinates?.[2]) === null ? null : Math.round(finite(coordinates?.[2])! * 10) / 10,
      place: text(properties?.place), status: text(properties?.status),
      longitude: Math.round(longitude * 10_000) / 10_000, latitude: Math.round(latitude * 10_000) / 10_000,
    }));
  }
  events.sort((a, b) => a.time.localeCompare(b.time));
  return Object.freeze({ events: Object.freeze(events), startYear: EARTHQUAKE_RECORD_START_YEAR, endYear, minMagnitude: EARTHQUAKE_RECORD_MIN_MAGNITUDE,
    outsideKansas, truncated: features.length > EARTHQUAKE_RECORD_LIMIT, retrievedAt, source });
}

/** A served record, checked again in the browser before it reaches the map. */
export function validEarthquakeRecord(value: unknown): value is EarthquakeRecord {
  const candidate = record(value);
  return Boolean(candidate && Array.isArray(candidate.events) && finite(candidate.startYear) !== null && finite(candidate.endYear) !== null
    && finite(candidate.minMagnitude) !== null && typeof candidate.truncated === "boolean" && typeof candidate.retrievedAt === "string"
    && candidate.events.every(event => { const e = record(event); return e && typeof e.id === "string" && typeof e.time === "string" && finite(e.year) !== null
      && finite(e.magnitude) !== null && finite(e.longitude) !== null && finite(e.latitude) !== null; }));
}

export type YearCount = Readonly<{ year: number; count: number }>;
/** Events per calendar year (UTC), every year of the record, empty years included. */
export function annualCounts(record: Pick<EarthquakeRecord, "events" | "startYear" | "endYear">): readonly YearCount[] {
  const counts = new Map<number, number>();
  for (const event of record.events) counts.set(event.year, (counts.get(event.year) ?? 0) + 1);
  return Array.from({ length: record.endYear - record.startYear + 1 }, (_, i) => ({ year: record.startYear + i, count: counts.get(record.startYear + i) ?? 0 }));
}

// ---------------------------------------------------------------------------
// Symbols. Colour is the year: one colour for 1973–2009, when Kansas had few
// seismometers and few M2.5+ events, then a perceptually ordered ramp (the
// matplotlib "plasma" colour map, dark violet to yellow) across the years since.
// Size is magnitude, on its own scale: the record holds thousands of events.
// ---------------------------------------------------------------------------

export const RECORD_RAMP_START_YEAR = 2010;
export const RECORD_RAMP = Object.freeze(["#0d0887", "#7e03a8", "#cc4778", "#f89540", "#f0f921"] as const);
export const RECORD_RADIUS_Z5 = Object.freeze([[2.5, 2.2], [4, 4.5], [5, 7]] as const);
export const RECORD_RADIUS_Z10 = Object.freeze([[2.5, 4], [4, 8], [5, 12]] as const);
const RECORD_STROKE = "#140a1c";

const rampStops = (endYear: number): (readonly [number, string])[] => {
  const span = Math.max(1, endYear - RECORD_RAMP_START_YEAR);
  return RECORD_RAMP.map((color, i) => [RECORD_RAMP_START_YEAR + span * i / (RECORD_RAMP.length - 1), color] as const);
};

const hex = (color: string) => [1, 3, 5].map(i => parseInt(color.slice(i, i + 2), 16));
/** The year's colour as MapLibre draws it ("interpolate" mixes in RGB), for the histogram and the key. */
export function recordYearColor(year: number, endYear: number): string {
  const stops = rampStops(endYear);
  if (year <= stops[0][0]) return stops[0][1];
  const upper = stops.findIndex(([at]) => year <= at);
  if (upper < 0) return stops[stops.length - 1][1];
  const [a, ca] = stops[upper - 1], [b, cb] = stops[upper];
  const t = (year - a) / (b - a), from = hex(ca), to = hex(cb);
  return `#${from.map((v, i) => Math.round(v + (to[i] - v) * t).toString(16).padStart(2, "0")).join("")}`;
}

const magnitude: ExpressionSpecification = ["get", "magnitude"];
export const recordColor = (endYear: number): ExpressionSpecification =>
  ["interpolate", ["linear"], ["get", "year"], ...rampStops(endYear).flat()] as unknown as ExpressionSpecification;
export const recordRadius = (): ExpressionSpecification =>
  ["interpolate", ["linear"], ["zoom"], 5, ["interpolate", ["linear"], magnitude, ...RECORD_RADIUS_Z5.flat()], 10, ["interpolate", ["linear"], magnitude, ...RECORD_RADIUS_Z10.flat()]] as unknown as ExpressionSpecification;

const along = (stops: readonly (readonly [number, number])[], x: number) => {
  if (x <= stops[0][0]) return stops[0][1];
  const i = stops.findIndex(([at]) => x <= at);
  if (i < 0) return stops[stops.length - 1][1];
  const [a, va] = stops[i - 1], [b, vb] = stops[i];
  return va + (vb - va) * (x - a) / (b - a);
};

/** The record's key: the year ramp as a bar (1973–2009 as one block), and circle size by magnitude at statewide zoom. */
export function earthquakeRecordKey(endYear: number): MapKey {
  const block = 20; // per cent of the bar for 1973–2009
  const at = (year: number) => Math.round((block + (100 - block) * (year - RECORD_RAMP_START_YEAR) / Math.max(1, endYear - RECORD_RAMP_START_YEAR)) * 10) / 10;
  const css = `linear-gradient(to right, ${RECORD_RAMP[0]} 0% ${block}%, ${rampStops(endYear).map(([year, color]) => `${color} ${at(year)}%`).join(", ")})`;
  const tickYears = [2015, 2020, 2025].filter(year => year <= endYear);
  return Object.freeze({
    id: "earthquake-record", title: `Earthquakes M${EARTHQUAKE_RECORD_MIN_MAGNITUDE}+ by year`,
    ramp: Object.freeze({ css, ticks: Object.freeze([{ label: "≤2009", at: block / 2 }, ...tickYears.map(year => ({ label: String(year), at: at(year) }))]) }),
    items: Object.freeze([2.5, 3, 4, 5].map(m => Object.freeze({ label: `M ${m}`, color: "#cc4778", shape: "dot" as const, stroke: RECORD_STROKE, size: Math.round(2 * along(RECORD_RADIUS_Z5, m)) }))),
    note: "USGS ComCat epicentres inside Kansas. Size is magnitude; circles grow as you zoom in. Detection improved as seismometers were added after 2013, so early decades miss some small events.",
  });
}

const geojson = (events: readonly EarthquakeRecordEvent[]): FeatureCollection<Point> => ({
  type: "FeatureCollection",
  features: events.map((event): Feature<Point> => ({ type: "Feature", id: event.id, geometry: { type: "Point", coordinates: [event.longitude, event.latitude] },
    properties: { id: event.id, year: event.year, magnitude: event.magnitude } })),
});
const shown = new WeakMap<MapLibreMap, readonly EarthquakeRecordEvent[]>();

/**
 * Draws the record (or removes it, for null), showing one year or every year,
 * and rings the selected event. Safe to call on every style load.
 */
export function syncEarthquakeRecord(map: MapLibreMap, record: EarthquakeRecord | null, year: number | null, selectedId: string | null): void {
  if (!record) {
    for (const id of [EARTHQUAKE_RECORD_SELECTED_LAYER_ID, EARTHQUAKE_RECORD_LAYER_ID]) if (map.getLayer(id)) map.removeLayer(id);
    if (map.getSource(EARTHQUAKE_RECORD_SOURCE_ID)) map.removeSource(EARTHQUAKE_RECORD_SOURCE_ID);
    shown.delete(map);
    return;
  }
  const source = map.getSource(EARTHQUAKE_RECORD_SOURCE_ID) as GeoJSONSource | undefined;
  if (!source) map.addSource(EARTHQUAKE_RECORD_SOURCE_ID, { type: "geojson", data: geojson(record.events) });
  else if (shown.get(map) !== record.events) source.setData(geojson(record.events));
  shown.set(map, record.events);
  // Under the site's own overlays and labels, above the basemap and the provider context layers.
  const before = map.getStyle().layers?.find(layer => layer.id.startsWith("kfm-") && layer.id !== "kfm-background" && !layer.id.startsWith(EARTHQUAKE_RECORD_SOURCE_ID))?.id;
  if (!map.getLayer(EARTHQUAKE_RECORD_LAYER_ID)) map.addLayer({ id: EARTHQUAKE_RECORD_LAYER_ID, type: "circle", source: EARTHQUAKE_RECORD_SOURCE_ID,
    layout: { "circle-sort-key": magnitude },
    paint: { "circle-color": recordColor(record.endYear), "circle-radius": recordRadius(), "circle-opacity": 0.88, "circle-stroke-color": RECORD_STROKE, "circle-stroke-width": 0.8, "circle-stroke-opacity": 0.9 } }, before);
  if (!map.getLayer(EARTHQUAKE_RECORD_SELECTED_LAYER_ID)) map.addLayer({ id: EARTHQUAKE_RECORD_SELECTED_LAYER_ID, type: "circle", source: EARTHQUAKE_RECORD_SOURCE_ID,
    paint: { "circle-color": "rgba(0,0,0,0)", "circle-radius": ["+", recordRadius(), 3.5], "circle-stroke-color": "#ffffff", "circle-stroke-width": 2 } }, before);
  map.setFilter(EARTHQUAKE_RECORD_LAYER_ID, year === null ? null : ["==", ["get", "year"], year]);
  map.setFilter(EARTHQUAKE_RECORD_SELECTED_LAYER_ID, ["==", ["get", "id"], selectedId ?? ""]);
}

/** The USGS event page for a record event id (ids are checked when the record is parsed). */
export const earthquakeEventUrl = (id: string): string => `https://earthquake.usgs.gov/earthquakes/eventpage/${encodeURIComponent(id)}`;
