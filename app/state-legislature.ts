import type { Feature, FeatureCollection, MultiPolygon, Polygon } from "geojson";
import type { GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";
import type { MapKey } from "./map-keys";
import { validateCivicGeometry } from "./civic-districts";

/**
 * Kansas Legislature districts: the 40 Senate and 125 House districts of the
 * 2024 plans, as the Census Bureau's January 1, 2025 generalized (1:500,000)
 * geography draws them in TIGERweb.
 */

export type Chamber = "senate" | "house";
export const LEGISLATURE_SERVICE = "https://tigerweb.geo.census.gov/arcgis/rest/services/Generalized_ACS2025/Legislative/MapServer";
export const CHAMBERS: Readonly<Record<Chamber, Readonly<{ layer: number; name: string; districts: number; title: string }>>> = Object.freeze({
  senate: { layer: 8, name: "Kansas Senate", districts: 40, title: "Senate" },
  house: { layer: 9, name: "Kansas House", districts: 125, title: "House" },
});
export const isChamber = (value: unknown): value is Chamber => value === "senate" || value === "house";
export const LEGISLATURE_OFFICIAL_MAPS = "https://www.sos.ks.gov/elections/district-maps.html";

/** Kansas's districts in one chamber, as GeoJSON in longitude and latitude, rounded to about a metre. */
export function legislatureProviderUrl(chamber: Chamber): string {
  const url = new URL(`${LEGISLATURE_SERVICE}/${CHAMBERS[chamber].layer}/query`);
  for (const [key, value] of Object.entries({ where: "STATE='20'", outFields: "GEOID,STATE,BASENAME,NAME", returnGeometry: "true", outSR: "4326", geometryPrecision: "5", f: "geojson" })) url.searchParams.set(key, value);
  return url.toString();
}
export const legislatureApiPath = (chamber: Chamber) => `/api/state-legislature?chamber=${chamber}`;

export type LegislatureDistricts = Readonly<{ chamber: Chamber; retrievedAt: string; data: FeatureCollection<Polygon | MultiPolygon> }>;
type Row = Record<string, unknown>;
const isRow = (value: unknown): value is Row => Boolean(value) && typeof value === "object" && !Array.isArray(value);

/**
 * The complete edition or nothing: every district of the chamber, each once,
 * each a valid Kansas polygon. A missing or extra district is refused rather
 * than drawn from part of a plan.
 */
export function parseLegislature(value: unknown, chamber: Chamber, retrievedAt: string): LegislatureDistricts {
  if (!isRow(value) || value.type !== "FeatureCollection" || !Array.isArray(value.features) || value.exceededTransferLimit) throw new Error("Incomplete legislative geography.");
  const expected = CHAMBERS[chamber].districts, seen = new Set<number>();
  const features: Feature<Polygon | MultiPolygon>[] = [];
  for (const row of value.features) {
    if (!isRow(row) || !isRow(row.properties)) throw new Error("Invalid district feature.");
    const p = row.properties;
    const geoid = typeof p.GEOID === "string" ? p.GEOID : "";
    // "ZZZ" marks water or land in no district; it is not a district.
    if (/^20ZZZ$/.test(geoid)) continue;
    if (p.STATE !== "20" || !/^20\d{3}$/.test(geoid)) throw new Error("District identity changed.");
    const district = Number(geoid.slice(2));
    if (district < 1 || district > expected || seen.has(district)) throw new Error("Unexpected or repeated district.");
    seen.add(district);
    const geometry = validateCivicGeometry(row.geometry, { vertices: 0 });
    features.push({ type: "Feature", id: district, geometry, properties: { district, geoid, chamber, name: `${CHAMBERS[chamber].name} District ${district}` } });
  }
  if (seen.size !== expected) throw new Error(`Expected ${expected} districts, found ${seen.size}.`);
  features.sort((a, b) => (a.properties!.district as number) - (b.properties!.district as number));
  return Object.freeze({ chamber, retrievedAt, data: { type: "FeatureCollection" as const, features } });
}

export function validLegislature(value: unknown, chamber: Chamber): value is LegislatureDistricts {
  return isRow(value) && value.chamber === chamber && isRow(value.data) && Array.isArray(value.data.features) && value.data.features.length === CHAMBERS[chamber].districts;
}

export const legislatureList = (districts: LegislatureDistricts) =>
  districts.data.features.map(feature => ({ id: String(feature.properties!.district), label: `${CHAMBERS[districts.chamber].title} District ${feature.properties!.district}` }));

/** The dock's line: the chamber, the plan and the scale, and the district picked. */
export function legislatureReading(chamber: Chamber, picked: number | null): string {
  const c = CHAMBERS[chamber];
  return `${c.name}: ${c.districts} districts · 2024 plan · Census January 2025 geography, generalized to 1:500,000${picked ? ` · ${c.title} District ${picked} picked` : ""}`;
}

export function legislatureKey(chamber: Chamber): MapKey {
  return Object.freeze({
    id: "kansas-legislature",
    title: `${CHAMBERS[chamber].name} districts · 2024 plan`,
    items: Object.freeze([
      Object.freeze({ label: "District boundary and number", color: "#2b5f5b", shape: "line" as const }),
      Object.freeze({ label: "District picked", color: "#c2410c", shape: "line" as const }),
    ]),
    note: "Census Bureau generalized geography for display: not for deciding which district an address is in. Officeholders and elections are not shown; the Kansas Secretary of State publishes the official maps.",
  });
}

// Under the site's own overlays and labels, like the congressional districts.
export const LEGISLATURE_SOURCE_ID = "kfm-kansas-legislature";
export const LEGISLATURE_FILL_LAYER_ID = "kfm-kansas-legislature-fill";
export const LEGISLATURE_LINE_LAYER_ID = "kfm-kansas-legislature-line";
export const LEGISLATURE_SELECTED_LAYER_ID = "kfm-kansas-legislature-selected";
export const LEGISLATURE_LABEL_LAYER_ID = "kfm-kansas-legislature-label";
const shown = new WeakMap<MapLibreMap, FeatureCollection>();

/** The districts of one chamber (or nothing, for null): a faint fill to click, outlines, the picked district, and district numbers. */
export function syncLegislature(map: MapLibreMap, districts: LegislatureDistricts | null, picked: number | null = null): void {
  if (!districts) {
    for (const id of [LEGISLATURE_LABEL_LAYER_ID, LEGISLATURE_SELECTED_LAYER_ID, LEGISLATURE_LINE_LAYER_ID, LEGISLATURE_FILL_LAYER_ID]) if (map.getLayer(id)) map.removeLayer(id);
    if (map.getSource(LEGISLATURE_SOURCE_ID)) map.removeSource(LEGISLATURE_SOURCE_ID);
    shown.delete(map);
    return;
  }
  const source = map.getSource(LEGISLATURE_SOURCE_ID) as GeoJSONSource | undefined;
  if (!source) map.addSource(LEGISLATURE_SOURCE_ID, { type: "geojson", data: districts.data });
  else if (shown.get(map) !== districts.data) source.setData(districts.data);
  shown.set(map, districts.data);
  const before = map.getStyle().layers?.find(layer => layer.id.startsWith("kfm-") && layer.id !== "kfm-background" && !layer.id.startsWith(LEGISLATURE_SOURCE_ID))?.id;
  if (!map.getLayer(LEGISLATURE_FILL_LAYER_ID)) map.addLayer({ id: LEGISLATURE_FILL_LAYER_ID, type: "fill", source: LEGISLATURE_SOURCE_ID,
    paint: { "fill-color": "#397f7a", "fill-opacity": ["case", ["==", ["get", "district"], picked ?? -1], 0.22, 0.06] as never } }, before);
  else map.setPaintProperty(LEGISLATURE_FILL_LAYER_ID, "fill-opacity", ["case", ["==", ["get", "district"], picked ?? -1], 0.22, 0.06] as never);
  if (!map.getLayer(LEGISLATURE_LINE_LAYER_ID)) map.addLayer({ id: LEGISLATURE_LINE_LAYER_ID, type: "line", source: LEGISLATURE_SOURCE_ID,
    layout: { "line-join": "round" }, paint: { "line-color": "#2b5f5b", "line-width": ["interpolate", ["linear"], ["zoom"], 5, 0.8, 10, 2] as never, "line-opacity": 0.9 } }, before);
  if (!map.getLayer(LEGISLATURE_SELECTED_LAYER_ID)) map.addLayer({ id: LEGISLATURE_SELECTED_LAYER_ID, type: "line", source: LEGISLATURE_SOURCE_ID,
    layout: { "line-join": "round" }, paint: { "line-color": "#c2410c", "line-width": ["interpolate", ["linear"], ["zoom"], 5, 2.4, 10, 4] as never } }, before);
  map.setFilter(LEGISLATURE_SELECTED_LAYER_ID, ["==", ["get", "district"], picked ?? -1] as never);
  if (!map.getLayer(LEGISLATURE_LABEL_LAYER_ID)) map.addLayer({ id: LEGISLATURE_LABEL_LAYER_ID, type: "symbol", source: LEGISLATURE_SOURCE_ID,
    layout: { "text-field": ["to-string", ["get", "district"]], "text-font": ["Noto Sans Regular"], "text-size": ["interpolate", ["linear"], ["zoom"], 5, 10, 10, 15] as never, "text-allow-overlap": false },
    paint: { "text-color": "#173f3c", "text-halo-color": "#f3f1ec", "text-halo-width": 1.4 } }, before);
}
