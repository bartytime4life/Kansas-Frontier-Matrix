import type { Feature, FeatureCollection, Geometry } from "geojson";
import type { GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";
import type { MapKey } from "./map-keys";

/**
 * Kansas population change by county, 2010 to 2020: the Census Bureau's
 * decennial counts for both years (TIGERweb POP100), joined by county GEOID.
 * Kansas's 105 counties kept their boundaries through the decade, so each
 * county is compared with itself.
 */

export const POPULATION_CHANGE_FROM = 2010;
export const POPULATION_CHANGE_TO = 2020;
export const KANSAS_COUNTIES = 105;
export const populationChangeApiPath = `/api/event-atlas/counties?edition=${POPULATION_CHANGE_FROM}`;

/** Percent-change classes, losses brown and gains blue-green (ColorBrewer BrBG); each lower bound is inclusive. */
export const CHANGE_CLASSES = Object.freeze([
  Object.freeze({ min: -Infinity, label: "Lost 10% or more", color: "#8c510a" }),
  Object.freeze({ min: -10, label: "Lost 5 to 10%", color: "#d8b365" }),
  Object.freeze({ min: -5, label: "Lost under 5%", color: "#f6e8c3" }),
  Object.freeze({ min: 0, label: "Grew under 5%", color: "#c7eae5" }),
  Object.freeze({ min: 5, label: "Grew 5 to 10%", color: "#5ab4ac" }),
  Object.freeze({ min: 10, label: "Grew 10% or more", color: "#01665e" }),
] as const);
export const changeColor = (percent: number) => [...CHANGE_CLASSES].reverse().find(entry => percent >= entry.min)?.color ?? CHANGE_CLASSES[0].color;

export type CountyChange = Readonly<{ geoid: string; name: string; from: number; to: number; change: number; percent: number }>;
export type PopulationChange = Readonly<{ counties: readonly CountyChange[]; from: number; to: number; change: number; percent: number; losing: number; gaining: number }>;

type Row = Record<string, unknown>;
const isRow = (value: unknown): value is Row => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const count = (value: unknown) => typeof value === "number" && Number.isInteger(value) && value >= 0 ? value : null;

/** The 2010 county payload, as the counties route answers it: a collection of 105 Kansas counties. */
export function validCountyBaseline(value: unknown): value is { data: FeatureCollection } {
  return isRow(value) && isRow(value.data) && value.data.type === "FeatureCollection" && Array.isArray(value.data.features) && value.data.features.length === KANSAS_COUNTIES;
}

const people = (collection: FeatureCollection) => {
  const rows = new Map<string, { name: string; population: number | null }>();
  for (const feature of collection.features) {
    const geoid = String(feature.properties?.geoid ?? "");
    if (/^20\d{3}$/.test(geoid)) rows.set(geoid, { name: String(feature.properties?.name ?? geoid), population: count(feature.properties?.population) });
  }
  return rows;
};

/**
 * Each county's change, or null unless every Kansas county has a count in both
 * years: a partial join would understate the state and misplace counties.
 */
export function populationChange(now: FeatureCollection, then: FeatureCollection): PopulationChange | null {
  const a = people(then), b = people(now);
  if (a.size !== KANSAS_COUNTIES || b.size !== KANSAS_COUNTIES) return null;
  const counties: CountyChange[] = [];
  for (const [geoid, later] of b) {
    const earlier = a.get(geoid);
    if (!earlier || earlier.population === null || later.population === null || earlier.population === 0) return null;
    const change = later.population - earlier.population;
    counties.push(Object.freeze({ geoid, name: later.name, from: earlier.population, to: later.population, change, percent: change / earlier.population * 100 }));
  }
  counties.sort((x, y) => x.geoid.localeCompare(y.geoid));
  const from = counties.reduce((sum, c) => sum + c.from, 0), to = counties.reduce((sum, c) => sum + c.to, 0);
  return Object.freeze({ counties: Object.freeze(counties), from, to, change: to - from, percent: (to - from) / from * 100,
    losing: counties.filter(c => c.change < 0).length, gaining: counties.filter(c => c.change > 0).length });
}

const thousands = (n: number) => n.toLocaleString("en-US");
const signed = (n: number) => `${n > 0 ? "+" : n < 0 ? "−" : ""}${thousands(Math.abs(n))}`;
export const signedPercent = (p: number) => `${p > 0 ? "+" : p < 0 ? "−" : ""}${Math.abs(p).toFixed(1)}%`;

/** Counties from the largest gain to the largest loss, in percent. */
export const byPercent = (change: PopulationChange) => [...change.counties].sort((x, y) => y.percent - x.percent || x.name.localeCompare(y.name));

export function populationChangeList(change: PopulationChange): { id: string; label: string }[] {
  return byPercent(change).map(c => ({ id: c.geoid, label: `${c.name} · ${signedPercent(c.percent)} · ${thousands(c.from)} → ${thousands(c.to)}` }));
}

/** The statewide line: both totals, the net change, how many counties lost people, and the largest gain and loss in people. */
export function populationChangeReading(change: PopulationChange): string {
  const most = change.counties.reduce((best, c) => c.change > best.change ? c : best);
  const least = change.counties.reduce((worst, c) => c.change < worst.change ? c : worst);
  return `Kansas ${thousands(change.from)} → ${thousands(change.to)} (${signed(change.change)}, ${signedPercent(change.percent)}) · ${change.losing} of ${change.counties.length} counties lost people`
    + ` · largest gain ${most.name} (${signed(most.change)}) · largest loss ${least.name} (${signed(least.change)})`;
}

/** The picked county's line, with its rank by percent change. */
export function countyPopulationReading(change: PopulationChange, geoid: string): string | null {
  const ranked = byPercent(change);
  const index = ranked.findIndex(c => c.geoid === geoid);
  if (index < 0) return null;
  const c = ranked[index];
  return `${c.name} County: ${thousands(c.from)} in ${POPULATION_CHANGE_FROM} → ${thousands(c.to)} in ${POPULATION_CHANGE_TO} (${signed(c.change)}, ${signedPercent(c.percent)}) · ${index + 1} of ${ranked.length} by percent change`;
}

export function populationChangeKey(): MapKey {
  return Object.freeze({
    id: "population-change",
    title: `Population change by county · ${POPULATION_CHANGE_FROM}–${POPULATION_CHANGE_TO}`,
    items: Object.freeze(CHANGE_CLASSES.map(entry => Object.freeze({ label: entry.label, color: entry.color, shape: "area" as const }))),
    note: "Census Bureau decennial counts (April 1, 2010 and April 1, 2020) for the same 105 county boundaries. Percent change from 2010. Counts, not estimates; the 2020 count used disclosure-avoidance noise, which matters little at county totals.",
  });
}

export function populationChangeCollection(counties: FeatureCollection, change: PopulationChange): FeatureCollection {
  const rows = new Map(change.counties.map(c => [c.geoid, c]));
  return { type: "FeatureCollection", features: counties.features.flatMap((feature): Feature<Geometry>[] => {
    const c = rows.get(String(feature.properties?.geoid ?? ""));
    if (!feature.geometry || !c) return [];
    return [{ type: "Feature", geometry: feature.geometry, properties: { geoid: c.geoid, name: c.name, percent: Math.round(c.percent * 10) / 10, change: c.change, color: changeColor(c.percent) } }];
  }) };
}

// Under the site's own overlays and labels, like the other county maps.
export const POPULATION_CHANGE_SOURCE_ID = "kfm-population-change";
export const POPULATION_CHANGE_FILL_LAYER_ID = "kfm-population-change-fill";
export const POPULATION_CHANGE_LINE_LAYER_ID = "kfm-population-change-line";
export const POPULATION_CHANGE_SELECTED_LAYER_ID = "kfm-population-change-selected";
const shown = new WeakMap<MapLibreMap, FeatureCollection>();

/** The change choropleth (or nothing, for null), with the picked county outlined. */
export function syncPopulationChange(map: MapLibreMap, collection: FeatureCollection | null, selected: string | null = null): void {
  if (!collection) {
    for (const id of [POPULATION_CHANGE_SELECTED_LAYER_ID, POPULATION_CHANGE_LINE_LAYER_ID, POPULATION_CHANGE_FILL_LAYER_ID]) if (map.getLayer(id)) map.removeLayer(id);
    if (map.getSource(POPULATION_CHANGE_SOURCE_ID)) map.removeSource(POPULATION_CHANGE_SOURCE_ID);
    shown.delete(map);
    return;
  }
  const source = map.getSource(POPULATION_CHANGE_SOURCE_ID) as GeoJSONSource | undefined;
  if (!source) map.addSource(POPULATION_CHANGE_SOURCE_ID, { type: "geojson", data: collection });
  else if (shown.get(map) !== collection) source.setData(collection);
  shown.set(map, collection);
  const before = map.getStyle().layers?.find(layer => layer.id.startsWith("kfm-") && layer.id !== "kfm-background" && !layer.id.startsWith(POPULATION_CHANGE_SOURCE_ID))?.id;
  if (!map.getLayer(POPULATION_CHANGE_FILL_LAYER_ID)) map.addLayer({ id: POPULATION_CHANGE_FILL_LAYER_ID, type: "fill", source: POPULATION_CHANGE_SOURCE_ID,
    paint: { "fill-color": ["get", "color"] as never, "fill-opacity": 0.88 } }, before);
  if (!map.getLayer(POPULATION_CHANGE_LINE_LAYER_ID)) map.addLayer({ id: POPULATION_CHANGE_LINE_LAYER_ID, type: "line", source: POPULATION_CHANGE_SOURCE_ID,
    layout: { "line-join": "round" }, paint: { "line-color": "#3d3a33", "line-width": ["interpolate", ["linear"], ["zoom"], 5, 0.5, 9, 1.2] as never, "line-opacity": 0.6 } }, before);
  if (!map.getLayer(POPULATION_CHANGE_SELECTED_LAYER_ID)) map.addLayer({ id: POPULATION_CHANGE_SELECTED_LAYER_ID, type: "line", source: POPULATION_CHANGE_SOURCE_ID,
    layout: { "line-join": "round" }, paint: { "line-color": "#111111", "line-width": ["interpolate", ["linear"], ["zoom"], 5, 2.4, 9, 3.8] as never } }, before);
  map.setFilter(POPULATION_CHANGE_SELECTED_LAYER_ID, ["==", ["get", "geoid"], selected ?? ""] as never);
}
