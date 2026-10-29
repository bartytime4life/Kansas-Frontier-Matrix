import type { Map as MapLibreMap } from "./maplibre-seam";
import type { MapKey } from "./map-keys";

/**
 * USGS National Land Cover Database (NLCD) 2021: land cover classified from
 * Landsat at 30 m for the conterminous United States, served by the MRLC
 * consortium's GeoServer and drawn in NLCD's own colours.
 */

export const MRLC_WMS = "https://www.mrlc.gov/geoserver/wms";
export const NLCD_LAYER = "mrlc_display:NLCD_2021_Land_Cover_L48";
export const NLCD_PAGE = "https://www.mrlc.gov/data/nlcd-2021-land-cover-conus";

/** The NLCD legend: each class code, its name, its group and its official colour. Perennial ice/snow (12) does not occur in Kansas. */
export const NLCD_CLASSES = Object.freeze([
  { code: 11, name: "Open water", group: "Water", color: "#466b9f" },
  { code: 21, name: "Developed, open space", group: "Developed", color: "#dec5c5" },
  { code: 22, name: "Developed, low intensity", group: "Developed", color: "#d99282" },
  { code: 23, name: "Developed, medium intensity", group: "Developed", color: "#eb0000" },
  { code: 24, name: "Developed, high intensity", group: "Developed", color: "#ab0000" },
  { code: 31, name: "Barren land", group: "Barren", color: "#b3ac9f" },
  { code: 41, name: "Deciduous forest", group: "Forest", color: "#68ab5f" },
  { code: 42, name: "Evergreen forest", group: "Forest", color: "#1c5f2c" },
  { code: 43, name: "Mixed forest", group: "Forest", color: "#b5c58f" },
  { code: 52, name: "Shrub/scrub", group: "Shrubland", color: "#ccb879" },
  { code: 71, name: "Grassland/herbaceous", group: "Herbaceous", color: "#dfdfc2" },
  { code: 81, name: "Pasture/hay", group: "Planted/cultivated", color: "#dcd939" },
  { code: 82, name: "Cultivated crops", group: "Planted/cultivated", color: "#ab6c28" },
  { code: 90, name: "Woody wetlands", group: "Wetlands", color: "#b8d9eb" },
  { code: 95, name: "Emergent herbaceous wetlands", group: "Wetlands", color: "#6c9fb8" },
] as const);
export type NlcdCode = (typeof NLCD_CLASSES)[number]["code"];
export const nlcdClass = (code: number) => NLCD_CLASSES.find(entry => entry.code === code) ?? null;

/** One 512-pixel Web Mercator tile of the NLCD layer, drawn by MRLC in NLCD's colours. */
export const LAND_COVER_TILE_URL = `${MRLC_WMS}?service=WMS&version=1.1.1&request=GetMap&layers=${encodeURIComponent(NLCD_LAYER)}&styles=&format=image%2Fpng&transparent=true`
  + "&srs=EPSG%3A3857&bbox={bbox-epsg-3857}&width=512&height=512";

/** Kansas and a margin: the only places the point lookup answers for. */
const REGION = { west: -103.5, east: -93.5, south: 36.5, north: 40.5 };
export const inLandCoverRegion = (lon: number, lat: number) => Number.isFinite(lon) && Number.isFinite(lat) && lon >= REGION.west && lon <= REGION.east && lat >= REGION.south && lat <= REGION.north;

/** The class of the one 30 m cell at a point, from MRLC's GetFeatureInfo on a 3-pixel window centred on it. */
export function landCoverPointProviderUrl(lon: number, lat: number): string {
  const d = 0.0002;
  const url = new URL(MRLC_WMS);
  for (const [key, value] of Object.entries({ service: "WMS", version: "1.1.1", request: "GetFeatureInfo", layers: NLCD_LAYER, query_layers: NLCD_LAYER, styles: "",
    srs: "EPSG:4326", bbox: [lon - d, lat - d, lon + d, lat + d].map(v => v.toFixed(6)).join(","), width: "3", height: "3", x: "1", y: "1", info_format: "application/json", feature_count: "1" })) url.searchParams.set(key, value);
  return url.toString();
}
export const landCoverPointApiPath = (lon: number, lat: number) => `/api/land-cover/point?lon=${lon.toFixed(5)}&lat=${lat.toFixed(5)}`;

/** The NLCD code in a GetFeatureInfo answer: the first property that is a known class (GeoServer names it PALETTE_INDEX or GRAY_INDEX). */
export function parseLandCoverPoint(value: unknown): NlcdCode | null {
  const features = value && typeof value === "object" && Array.isArray((value as { features?: unknown }).features) ? (value as { features: unknown[] }).features : [];
  for (const feature of features) {
    const properties = feature && typeof feature === "object" ? (feature as { properties?: unknown }).properties : null;
    if (!properties || typeof properties !== "object") continue;
    for (const raw of Object.values(properties as Record<string, unknown>)) {
      const code = typeof raw === "number" ? raw : typeof raw === "string" && /^\d+$/.test(raw) ? Number(raw) : Number.NaN;
      const entry = nlcdClass(code);
      if (entry) return entry.code;
    }
  }
  return null;
}

export type LandCoverPoint = Readonly<{ lon: number; lat: number; state: "loading" | "ready" | "none" | "failed"; code: NlcdCode | null }>;
const coordinate = (lon: number, lat: number) => `${Math.abs(lat).toFixed(3)}°${lat >= 0 ? "N" : "S"}, ${Math.abs(lon).toFixed(3)}°${lon >= 0 ? "E" : "W"}`;
/** The dock's line: what the map is, and the class at the point clicked. */
export function landCoverReading(point: LandCoverPoint | null): string {
  if (!point) return "USGS NLCD 2021: land cover classified from Landsat at 30 m · click the map for the class at a point";
  const at = `At ${coordinate(point.lon, point.lat)}`;
  if (point.state === "loading") return `${at}: reading NLCD…`;
  if (point.state === "failed") return `${at}: MRLC did not answer; the map's colours are NLCD's own`;
  const entry = point.code === null ? null : nlcdClass(point.code);
  return entry ? `${at}: ${entry.name} (${entry.code}) · ${entry.group.toLowerCase()}` : `${at}: no NLCD class (outside the mapped area)`;
}

export function landCoverKey(): MapKey {
  return Object.freeze({
    id: "nlcd-2021",
    title: "NLCD 2021 land cover · 30 m",
    items: Object.freeze(NLCD_CLASSES.map(entry => Object.freeze({ label: `${entry.code} ${entry.name}`, color: entry.color, shape: "area" as const }))),
    note: "USGS National Land Cover Database, classified from 2021 Landsat imagery. A mapped class for each 30 m cell, not a field survey: single cells can be wrong, and field edges blur across cells.",
  });
}

// Not "kfm-": other overlays (the Drought Monitor, storm reports) insert themselves under the first kfm- layer, and must stay above this raster.
export const LAND_COVER_SOURCE_ID = "tool-nlcd-land-cover";
export const LAND_COVER_LAYER_ID = "tool-nlcd-land-cover-raster";

/** The NLCD raster (or nothing, for false): over the base and other rasters, under every overlay; cells drawn sharp. */
export function syncLandCover(map: MapLibreMap, on: boolean): void {
  if (!on) {
    if (map.getLayer(LAND_COVER_LAYER_ID)) map.removeLayer(LAND_COVER_LAYER_ID);
    if (map.getSource(LAND_COVER_SOURCE_ID)) map.removeSource(LAND_COVER_SOURCE_ID);
    return;
  }
  if (!map.getSource(LAND_COVER_SOURCE_ID)) map.addSource(LAND_COVER_SOURCE_ID, { type: "raster", tiles: [LAND_COVER_TILE_URL], tileSize: 512, minzoom: 4, maxzoom: 13,
    attribution: "USGS NLCD 2021 · MRLC" } as never);
  const before = map.getStyle().layers?.find(layer => (layer.id.startsWith("kfm-") || layer.id.startsWith("external-")) && layer.id !== "kfm-background"
    && !layer.id.startsWith(LAND_COVER_SOURCE_ID) && layer.type !== "raster" && layer.type !== "hillshade" && layer.type !== "background")?.id;
  if (!map.getLayer(LAND_COVER_LAYER_ID)) map.addLayer({ id: LAND_COVER_LAYER_ID, type: "raster", source: LAND_COVER_SOURCE_ID,
    paint: { "raster-opacity": 0.85, "raster-resampling": "nearest", "raster-fade-duration": 0 } }, before);
}
