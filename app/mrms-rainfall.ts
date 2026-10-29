import type { Map as MapLibreMap } from "./maplibre-seam";

/**
 * Rainfall from the NWS Multi-Radar Multi-Sensor (MRMS) quantitative
 * precipitation estimate, as the NWS map service renders it: the rain of the
 * past 1 to 72 hours on a 1 km grid, in inches. It is a radar-only estimate,
 * updated shortly after each hour; the service keeps no history.
 */

export const MRMS_QPE_SERVICE = "https://mapservices.weather.noaa.gov/raster/rest/services/obs/mrms_qpe/ImageServer";
export const RAINFALL_WINDOWS = Object.freeze([1, 3, 6, 12, 24, 48, 72] as const);
export type RainfallHours = (typeof RAINFALL_WINDOWS)[number];
export const isRainfallHours = (value: unknown): value is RainfallHours => RAINFALL_WINDOWS.includes(value as RainfallHours);
/** The service's own raster function for each window. */
export const rainfallRenderingRule = (hours: RainfallHours) => JSON.stringify({ rasterFunction: `rft_${hours}hr` });
/** Tiles are asked for again every quarter hour, so a new hourly update is picked up soon after it lands. */
export const RAINFALL_REFRESH_MS = 15 * 60 * 1000;
export const rainfallStamp = (now: number) => String(Math.floor(now / RAINFALL_REFRESH_MS));

/** One 512-pixel Web Mercator tile from the service's exportImage, rendered by its raster function. */
export function rainfallTileUrl(hours: RainfallHours, stamp: string): string {
  return `${MRMS_QPE_SERVICE}/exportImage?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=512,512&format=png32&transparent=true`
    + `&renderingRule=${encodeURIComponent(rainfallRenderingRule(hours))}&f=image&_=${stamp}`;
}
export const rainfallLegendProviderUrl = (hours: RainfallHours) => `${MRMS_QPE_SERVICE}/legend?renderingRule=${encodeURIComponent(rainfallRenderingRule(hours))}&f=json`;
export const rainfallLegendApiPath = (hours: RainfallHours) => `/api/mrms-rainfall/legend?hours=${hours}`;

export type RainfallLegend = Readonly<{ hours: RainfallHours; items: readonly Readonly<{ label: string; image: string }>[]; retrievedAt: string }>;

type Row = Record<string, unknown>;
const isRow = (value: unknown): value is Row => Boolean(value) && typeof value === "object" && !Array.isArray(value);

/**
 * The service's legend for a window: each class's label and its swatch, kept
 * as the PNG the service drew, so the key shows exactly the colours on the map.
 */
export function parseRainfallLegend(value: unknown, hours: RainfallHours, retrievedAt: string): RainfallLegend {
  const layers = isRow(value) && Array.isArray(value.layers) ? value.layers : [];
  const legend = layers.find(layer => isRow(layer) && Array.isArray(layer.legend));
  const entries = isRow(legend) && Array.isArray(legend.legend) ? legend.legend : [];
  const items = entries.flatMap(entry => {
    if (!isRow(entry)) return [];
    const label = typeof entry.label === "string" ? entry.label.trim() : "";
    const data = typeof entry.imageData === "string" ? entry.imageData : "";
    const type = entry.contentType === "image/png" || entry.contentType === "image/jpeg" ? entry.contentType : null;
    return label && label.length <= 60 && type && data.length <= 20_000 && /^[A-Za-z0-9+/]+={0,2}$/.test(data) ? [{ label, image: `data:${type};base64,${data}` }] : [];
  }).slice(0, 40);
  if (!items.length) throw new Error("The MRMS legend had no classes.");
  return Object.freeze({ hours, items: Object.freeze(items), retrievedAt });
}

export function validRainfallLegend(value: unknown, hours: RainfallHours): value is RainfallLegend {
  return isRow(value) && value.hours === hours && Array.isArray(value.items) && value.items.length > 0
    && value.items.every(item => isRow(item) && typeof item.label === "string" && typeof item.image === "string" && /^data:image\/(png|jpeg);base64,/.test(item.image));
}

export const rainfallWindowLabel = (hours: RainfallHours) => hours === 1 ? "1 hour" : `${hours} hours`;
/** What the map shows, and what it is not. */
export function rainfallReading(hours: RainfallHours): string {
  return `Rain in the past ${rainfallWindowLabel(hours)}, in inches, from the NWS MRMS radar estimate on a 1 km grid · the latest hourly update · radar-only, not corrected to rain gauges`;
}

export const RAINFALL_SOURCE_ID = "kfm-mrms-rainfall";
export const RAINFALL_LAYER_ID = "kfm-mrms-rainfall-raster";
const shown = new WeakMap<MapLibreMap, string>();

/** The rendered rainfall raster (or nothing, for null), under the site's own overlays and labels. */
export function syncRainfall(map: MapLibreMap, hours: RainfallHours | null, stamp: string): void {
  const url = hours ? rainfallTileUrl(hours, stamp) : null;
  if (!url || shown.get(map) !== url) {
    if (map.getLayer(RAINFALL_LAYER_ID)) map.removeLayer(RAINFALL_LAYER_ID);
    if (map.getSource(RAINFALL_SOURCE_ID)) map.removeSource(RAINFALL_SOURCE_ID);
    shown.delete(map);
  }
  if (!url) return;
  if (!map.getSource(RAINFALL_SOURCE_ID)) {
    map.addSource(RAINFALL_SOURCE_ID, { type: "raster", tiles: [url], tileSize: 512, minzoom: 3, maxzoom: 10,
      attribution: "NWS MRMS QPE · NOAA mapservices" } as never);
    shown.set(map, url);
  }
  const before = map.getStyle().layers?.find(layer => layer.id.startsWith("kfm-") && layer.id !== "kfm-background" && !layer.id.startsWith(RAINFALL_SOURCE_ID))?.id;
  if (!map.getLayer(RAINFALL_LAYER_ID)) map.addLayer({ id: RAINFALL_LAYER_ID, type: "raster", source: RAINFALL_SOURCE_ID,
    paint: { "raster-opacity": 0.82, "raster-resampling": "nearest", "raster-fade-duration": 0 } }, before);
}
