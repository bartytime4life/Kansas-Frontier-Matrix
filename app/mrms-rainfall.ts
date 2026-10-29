import type { Map as MapLibreMap } from "./maplibre-seam";

/**
 * Rainfall, observed and forecast, as the NWS map services render it. Observed:
 * the Multi-Radar Multi-Sensor (MRMS) quantitative precipitation estimate, the
 * rain of the past 1 to 72 hours on a 1 km grid, in inches, a radar-only
 * estimate updated shortly after each hour. Forecast: the Weather Prediction
 * Center's quantitative precipitation forecast (QPF), the liquid precipitation
 * expected over the next 6 hours to 7 days, issued twice a day. Neither
 * service keeps history.
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
export const WPC_QPF_SERVICE = "https://mapservices.weather.noaa.gov/vector/rest/services/precip/wpc_qpf/MapServer";
export const QPF_WINDOWS = Object.freeze([6, 24, 48, 72, 120, 168] as const);
export type QpfHours = (typeof QPF_WINDOWS)[number];
export const isQpfHours = (value: unknown): value is QpfHours => QPF_WINDOWS.includes(value as QpfHours);
/** The WPC service's layer for each window: the 6-hour and Day 1 forecasts, and the cumulative forecasts from Day 1. */
export const QPF_LAYERS: Readonly<Record<QpfHours, number>> = Object.freeze({ 6: 7, 24: 1, 48: 8, 72: 9, 120: 10, 168: 11 });
/** One 512-pixel Web Mercator tile from the WPC service's export, drawn with the service's own symbols. */
export function qpfTileUrl(hours: QpfHours, stamp: string): string {
  return `${WPC_QPF_SERVICE}/export?bbox={bbox-epsg-3857}&bboxSR=3857&imageSR=3857&size=512,512&dpi=96&format=png32&transparent=true`
    + `&layers=show:${QPF_LAYERS[hours]}&f=image&_=${stamp}`;
}
export const QPF_LEGEND_PROVIDER_URL = `${WPC_QPF_SERVICE}/legend?f=json`;

export type RainfallKind = "observed" | "forecast";
export type RainfallView = Readonly<{ kind: "observed"; hours: RainfallHours } | { kind: "forecast"; hours: QpfHours }>;
export const rainfallViewTileUrl = (view: RainfallView, stamp: string) => view.kind === "observed" ? rainfallTileUrl(view.hours, stamp) : qpfTileUrl(view.hours, stamp);
export const rainfallLegendApiPath = (view: RainfallView) => `/api/mrms-rainfall/legend?kind=${view.kind}&hours=${view.hours}`;

export type RainfallLegend = Readonly<{ kind: RainfallKind; hours: number; items: readonly Readonly<{ label: string; image: string }>[]; retrievedAt: string }>;

type Row = Record<string, unknown>;
const isRow = (value: unknown): value is Row => Boolean(value) && typeof value === "object" && !Array.isArray(value);

/**
 * The service's legend for a window: each class's label and its swatch, kept
 * as the PNG the service drew, so the key shows exactly the colours on the map.
 */
export function parseRainfallLegend(value: unknown, view: RainfallView, retrievedAt: string): RainfallLegend {
  const layers = isRow(value) && Array.isArray(value.layers) ? value.layers : [];
  // The MRMS legend is the one layer the raster function draws; the WPC legend lists every layer, and the window's is taken.
  const legend = layers.find(layer => isRow(layer) && Array.isArray(layer.legend) && (view.kind === "observed" || layer.layerId === QPF_LAYERS[view.hours]));
  const entries = isRow(legend) && Array.isArray(legend.legend) ? legend.legend : [];
  const items = entries.flatMap(entry => {
    if (!isRow(entry)) return [];
    const label = typeof entry.label === "string" ? entry.label.trim() : "";
    const data = typeof entry.imageData === "string" ? entry.imageData : "";
    const type = entry.contentType === "image/png" || entry.contentType === "image/jpeg" ? entry.contentType : null;
    return label && label.length <= 60 && type && data.length <= 20_000 && /^[A-Za-z0-9+/]+={0,2}$/.test(data) ? [{ label, image: `data:${type};base64,${data}` }] : [];
  }).slice(0, 40);
  if (!items.length) throw new Error("The rainfall legend had no classes.");
  return Object.freeze({ kind: view.kind, hours: view.hours, items: Object.freeze(items), retrievedAt });
}

export function validRainfallLegend(value: unknown, view: RainfallView): value is RainfallLegend {
  return isRow(value) && value.kind === view.kind && value.hours === view.hours && Array.isArray(value.items) && value.items.length > 0
    && value.items.every(item => isRow(item) && typeof item.label === "string" && typeof item.image === "string" && /^data:image\/(png|jpeg);base64,/.test(item.image));
}

export const rainfallWindowLabel = (hours: RainfallHours) => hours === 1 ? "1 hour" : `${hours} hours`;
export const qpfWindowLabel = (hours: QpfHours) => hours === 6 ? "the next 6 hours" : hours === 24 ? "Day 1 (24 hours)" : `${hours / 24} days from Day 1`;
/** The dock's short label for a forecast window. */
export const qpfWindowButton = (hours: QpfHours) => hours === 6 ? "6 h" : hours === 24 ? "Day 1" : `${hours / 24} d`;
/** What the map shows, and what it is not. */
export function rainfallReading(view: RainfallView): string {
  if (view.kind === "forecast") return `Forecast precipitation for ${qpfWindowLabel(view.hours)}, in inches of liquid, from the NWS Weather Prediction Center · issued twice a day · a forecast, not a measurement`;
  return `Rain in the past ${rainfallWindowLabel(view.hours)}, in inches, from the NWS MRMS radar estimate on a 1 km grid · the latest hourly update · radar-only, not corrected to rain gauges`;
}

// Not "kfm-": other overlays insert themselves under the first kfm- layer, and must stay above this raster.
export const RAINFALL_SOURCE_ID = "tool-mrms-rainfall";
export const RAINFALL_LAYER_ID = "tool-mrms-rainfall-raster";
const shown = new WeakMap<MapLibreMap, string>();

/** The rendered rainfall raster (or nothing, for null), over the base and other rasters, under every overlay. */
export function syncRainfall(map: MapLibreMap, view: RainfallView | null, stamp: string): void {
  const url = view ? rainfallViewTileUrl(view, stamp) : null;
  if (!url || shown.get(map) !== url) {
    if (map.getLayer(RAINFALL_LAYER_ID)) map.removeLayer(RAINFALL_LAYER_ID);
    if (map.getSource(RAINFALL_SOURCE_ID)) map.removeSource(RAINFALL_SOURCE_ID);
    shown.delete(map);
  }
  if (!url) return;
  if (!map.getSource(RAINFALL_SOURCE_ID)) {
    map.addSource(RAINFALL_SOURCE_ID, { type: "raster", tiles: [url], tileSize: 512, minzoom: 3, maxzoom: 10,
      attribution: view?.kind === "forecast" ? "NWS WPC QPF · NOAA mapservices" : "NWS MRMS QPE · NOAA mapservices" } as never);
    shown.set(map, url);
  }
  // Over the base and other rasters, under every overlay drawn on top of them (gauges, alerts, the site's own lines and labels).
  const before = map.getStyle().layers?.find(layer => (layer.id.startsWith("kfm-") || layer.id.startsWith("external-")) && layer.id !== "kfm-background"
    && !layer.id.startsWith(RAINFALL_SOURCE_ID) && layer.type !== "raster" && layer.type !== "hillshade" && layer.type !== "background")?.id;
  // The MRMS 1 km cells stay sharp; the WPC forecast areas are smooth polygons.
  if (!map.getLayer(RAINFALL_LAYER_ID)) map.addLayer({ id: RAINFALL_LAYER_ID, type: "raster", source: RAINFALL_SOURCE_ID,
    paint: { "raster-opacity": 0.82, "raster-resampling": view?.kind === "forecast" ? "linear" : "nearest", "raster-fade-duration": 0 } }, before);
}
