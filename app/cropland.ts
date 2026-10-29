import type { Map as MapLibreMap } from "./maplibre-seam";
import type { MapKey } from "./map-keys";

/**
 * The USDA NASS Cropland Data Layer (CDL): what was planted in each 30 m cell
 * each year, classified from satellite imagery and checked against USDA farm
 * records, served by CropScape (George Mason University for NASS).
 */

export const CDL_WMS = "https://nassgeodata.gmu.edu/CropScapeService/wms_cdlall.cgi";
export const CDL_VALUE_SERVICE = "https://nassgeodata.gmu.edu/axis2/services/CDLService/GetCDLValue";
export const CDL_PAGE = "https://nassgeodata.gmu.edu/CropScape/";
export const CDL_FIRST_YEAR = 2008;
/** The newest year offered; a new year is added here once NASS releases it (about February). */
export const CDL_LATEST_YEAR = 2024;
export const CDL_YEARS = Object.freeze(Array.from({ length: CDL_LATEST_YEAR - CDL_FIRST_YEAR + 1 }, (_, i) => CDL_LATEST_YEAR - i));
export const isCdlYear = (value: unknown): value is number => typeof value === "number" && Number.isInteger(value) && value >= CDL_FIRST_YEAR && value <= CDL_LATEST_YEAR;

/** Kansas's main CDL classes in CropScape's colours; the CDL has more than a hundred. */
export const CDL_MAIN_CLASSES = Object.freeze([
  { value: 1, name: "Corn", color: "#ffd300" },
  { value: 4, name: "Sorghum", color: "#ff9e0b" },
  { value: 5, name: "Soybeans", color: "#267000" },
  { value: 6, name: "Sunflower", color: "#ffff00" },
  { value: 24, name: "Winter wheat", color: "#a87000" },
  { value: 26, name: "Double crop winter wheat/soybeans", color: "#707000" },
  { value: 36, name: "Alfalfa", color: "#ffa5e2" },
  { value: 61, name: "Fallow/idle cropland", color: "#bfbf77" },
  { value: 176, name: "Grassland/pasture", color: "#e8ffbf" },
] as const);

/** Tiles are asked for at field scale only: the service draws in longitude and latitude, and from zoom 8 a tile is near enough to Web Mercator (under a pixel). */
export const CDL_MIN_ZOOM = 8;
export const CDL_MAX_ZOOM = 13;
export const cdlTileTemplate = (year: number) => `/api/cropland/tile?year=${year}&z={z}&x={x}&y={y}`;

/** A Web Mercator tile's corners in longitude and latitude. */
export function tileBounds(z: number, x: number, y: number): { west: number; south: number; east: number; north: number } {
  const n = 2 ** z;
  const lat = (row: number) => Math.atan(Math.sinh(Math.PI * (1 - 2 * row / n))) * 180 / Math.PI;
  return { west: x / n * 360 - 180, east: (x + 1) / n * 360 - 180, north: lat(y), south: lat(y + 1) };
}
/** Kansas and a margin: tiles and points outside are not asked for. */
const REGION = { west: -103.5, east: -93.5, south: 36.5, north: 40.5 };
export const inCdlRegion = (lon: number, lat: number) => Number.isFinite(lon) && Number.isFinite(lat) && lon >= REGION.west && lon <= REGION.east && lat >= REGION.south && lat <= REGION.north;
export const tileInRegion = (b: ReturnType<typeof tileBounds>) => b.east >= REGION.west && b.west <= REGION.east && b.north >= REGION.south && b.south <= REGION.north;

export function cdlTileProviderUrl(year: number, z: number, x: number, y: number): string {
  const b = tileBounds(z, x, y);
  const url = new URL(CDL_WMS);
  for (const [key, value] of Object.entries({ SERVICE: "WMS", VERSION: "1.1.1", REQUEST: "GetMap", LAYERS: `cdl_${year}`, STYLES: "", SRS: "EPSG:4326",
    BBOX: [b.west, b.south, b.east, b.north].map(v => v.toFixed(7)).join(","), WIDTH: "512", HEIGHT: "512", FORMAT: "image/png", TRANSPARENT: "true" })) url.searchParams.set(key, value);
  return url.toString();
}

// NAD83 / Conus Albers (EPSG:5070) on GRS80, the CDL's own projection, which GetCDLValue takes.
const A = 6378137, F = 1 / 298.257222101, E2 = 2 * F - F * F, E = Math.sqrt(E2);
const RAD = Math.PI / 180;
const q = (phi: number) => { const s = Math.sin(phi); return (1 - E2) * (s / (1 - E2 * s * s) - Math.log((1 - E * s) / (1 + E * s)) / (2 * E)); };
const m = (phi: number) => Math.cos(phi) / Math.sqrt(1 - E2 * Math.sin(phi) ** 2);
const PHI1 = 29.5 * RAD, PHI2 = 45.5 * RAD, PHI0 = 23 * RAD, LAMBDA0 = -96 * RAD;
const N = (m(PHI1) ** 2 - m(PHI2) ** 2) / (q(PHI2) - q(PHI1));
const C = m(PHI1) ** 2 + N * q(PHI1);
const rho = (phi: number) => A * Math.sqrt(C - N * q(phi)) / N;
const RHO0 = rho(PHI0);
/** Longitude and latitude to EPSG:5070 metres (Snyder's ellipsoidal Albers equal-area conic). */
export function toConusAlbers(lon: number, lat: number): [number, number] {
  const r = rho(lat * RAD), theta = N * (lon * RAD - LAMBDA0);
  return [r * Math.sin(theta), RHO0 - r * Math.cos(theta)];
}

export function cdlValueProviderUrl(year: number, lon: number, lat: number): string {
  const [x, y] = toConusAlbers(lon, lat);
  return `${CDL_VALUE_SERVICE}?year=${year}&x=${x.toFixed(3)}&y=${y.toFixed(3)}`;
}
export const cdlPointApiPath = (year: number, lon: number, lat: number) => `/api/cropland/point?year=${year}&lon=${lon.toFixed(5)}&lat=${lat.toFixed(5)}`;

export type CdlValue = Readonly<{ value: number; category: string; color: string | null }>;
/** GetCDLValue answers a Result such as {x: …, y: …, value: "24", category: "Winter Wheat", color: "#A87000"}; the fields are read where they are. */
export function parseCdlValue(text: string): CdlValue | null {
  const value = /\bvalue\s*:\s*"?(\d{1,3})"?/i.exec(text)?.[1];
  const category = /\bcategory\s*:\s*"([^"<>]{1,80})"/i.exec(text)?.[1]?.trim();
  const color = /\bcolor\s*:\s*"(#[0-9a-f]{6})"/i.exec(text)?.[1]?.toLowerCase() ?? null;
  if (value === undefined || !category || Number(value) === 0) return null;
  return Object.freeze({ value: Number(value), category, color });
}

export type CdlPoint = Readonly<{ lon: number; lat: number; year: number; state: "loading" | "ready" | "none" | "failed"; crop: CdlValue | null }>;
const coordinate = (lon: number, lat: number) => `${Math.abs(lat).toFixed(3)}°${lat >= 0 ? "N" : "S"}, ${Math.abs(lon).toFixed(3)}°${lon >= 0 ? "E" : "W"}`;
/** The dock's line: the year drawn, then the class at the point clicked. */
export function cdlReading(year: number, point: CdlPoint | null, zoom: number): string {
  const scale = zoom < CDL_MIN_ZOOM ? " · zoom in to field scale to draw it" : "";
  if (!point) return `USDA Cropland Data Layer ${year}: what was planted in each 30 m cell · click a field for its crop${scale}`;
  const at = `At ${coordinate(point.lon, point.lat)}, ${point.year}`;
  if (point.state === "loading") return `${at}: reading CropScape…`;
  if (point.state === "failed") return `${at}: CropScape did not answer`;
  return point.crop ? `${at}: ${point.crop.category} (${point.crop.value})` : `${at}: no CDL class here`;
}

export function cdlKey(year: number): MapKey {
  return Object.freeze({
    id: "usda-cdl",
    title: `USDA Cropland Data Layer ${year} · 30 m`,
    items: Object.freeze(CDL_MAIN_CLASSES.map(entry => Object.freeze({ label: entry.name, color: entry.color, shape: "area" as const }))),
    note: "Kansas's main classes in CropScape's colours; the CDL has over a hundred. Classified from satellite imagery each season and checked against USDA farm records: accurate for the main crops, less so for minor ones. Click a field for its class.",
  });
}

// Not "kfm-": other overlays insert themselves under the first kfm- layer, and must stay above this raster.
export const CDL_SOURCE_ID = "tool-usda-cdl";
export const CDL_LAYER_ID = "tool-usda-cdl-raster";
const shown = new WeakMap<MapLibreMap, number>();

/** The CDL raster for a year (or nothing, for null): over the base and other rasters, under every overlay; cells drawn sharp. */
export function syncCropland(map: MapLibreMap, year: number | null): void {
  if (year === null || shown.get(map) !== year) {
    if (map.getLayer(CDL_LAYER_ID)) map.removeLayer(CDL_LAYER_ID);
    if (map.getSource(CDL_SOURCE_ID)) map.removeSource(CDL_SOURCE_ID);
    shown.delete(map);
  }
  if (year === null) return;
  if (!map.getSource(CDL_SOURCE_ID)) {
    map.addSource(CDL_SOURCE_ID, { type: "raster", tiles: [cdlTileTemplate(year)], tileSize: 512, minzoom: CDL_MIN_ZOOM, maxzoom: CDL_MAX_ZOOM,
      bounds: [REGION.west, REGION.south, REGION.east, REGION.north], attribution: "USDA NASS Cropland Data Layer · CropScape" } as never);
    shown.set(map, year);
  }
  const before = map.getStyle().layers?.find(layer => (layer.id.startsWith("kfm-") || layer.id.startsWith("external-")) && layer.id !== "kfm-background"
    && !layer.id.startsWith(CDL_SOURCE_ID) && layer.type !== "raster" && layer.type !== "hillshade" && layer.type !== "background")?.id;
  if (!map.getLayer(CDL_LAYER_ID)) map.addLayer({ id: CDL_LAYER_ID, type: "raster", source: CDL_SOURCE_ID, minzoom: CDL_MIN_ZOOM,
    paint: { "raster-opacity": 0.88, "raster-resampling": "nearest", "raster-fade-duration": 0 } }, before);
}
