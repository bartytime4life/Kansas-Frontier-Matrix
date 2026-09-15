import type { FeatureCollection } from "geojson";
import type { GeoJSONSource, Map as GLMap } from "maplibre-gl";

export type RenderQuality = "auto" | "efficient" | "detail";
export const QUALITY_LABELS = { auto: "Balanced", efficient: "Battery saver", detail: "High detail" } as const;
export const QUALITY_STORAGE_KEY = "kfm-render-quality-v1";
export function renderBudget(quality: RenderQuality, deviceRatio = 1, saveData = false, coarsePointer = false, embedded = false) {
  const efficient = quality === "efficient" || quality === "auto" && (saveData || embedded);
  // "Balanced" is intentionally adaptive: touch-first devices get a smaller
  // default GPU/tile budget, while an explicit High detail choice is never
  // silently downgraded.
  const touchBalanced = quality === "auto" && coarsePointer && !efficient;
  return {
    efficient,
    pixelRatio: Math.max(1, Math.min(Number.isFinite(deviceRatio) ? deviceRatio : 1, efficient ? 1 : quality === "detail" ? 2 : touchBalanced ? 1.25 : 1.5)),
    imageRequests: efficient ? 6 : quality === "detail" ? 12 : touchBalanced ? 7 : 10,
    tileCache: efficient ? 48 : quality === "detail" ? 112 : touchBalanced ? 64 : 96,
    workerCount: efficient ? 1 : quality === "detail" ? 4 : 2,
    coarsePointer,
    embedded,
  };
}
export function readRenderQuality(): RenderQuality {
  try { const value = localStorage.getItem(QUALITY_STORAGE_KEY); return value === "efficient" || value === "detail" ? value : "auto"; } catch { return "auto"; }
}
export function browserRenderBudget(quality = readRenderQuality()) {
  const connection = typeof navigator === "undefined" ? undefined : (navigator as Navigator & { connection?: { saveData?: boolean } }).connection;
  const coarsePointer = typeof window !== "undefined" && (
    window.matchMedia?.("(pointer: coarse)").matches || Math.min(window.innerWidth, window.innerHeight) <= 760
  );
  let embedded = false;
  if (typeof window !== "undefined") {
    try { embedded = window.self !== window.top; } catch { embedded = true; }
  }
  return renderBudget(quality, typeof window === "undefined" ? 1 : window.devicePixelRatio, Boolean(connection?.saveData), coarsePointer, embedded);
}

// Source identity changes on style replacement. Weak keys cannot retain an old
// map or a discarded payload. Feature-reference comparison also skips identical
// filtered smoke/station frames without dropping changed observation values.
const uploaded = new WeakMap<GeoJSONSource, FeatureCollection>();
export function rememberGeoJSON(source: GeoJSONSource, data: FeatureCollection) { uploaded.set(source, data); }
export function updateGeoJSON(source: GeoJSONSource | undefined, data: FeatureCollection): boolean {
  if (!source) return false;
  const prior = uploaded.get(source);
  if (prior === data || prior && prior.features.length === data.features.length && prior.features.every((feature, index) => feature === data.features[index])) return false;
  source.setData(data); uploaded.set(source, data); return true;
}
export function setVisibleIfChanged(map: GLMap, id: string, visible: boolean) {
  const next = visible ? "visible" : "none";
  if ((map.getLayoutProperty(id, "visibility") ?? "visible") !== next) map.setLayoutProperty(id, "visibility", next);
}
export function setPaintIfChanged(map: GLMap, id: string, property: Parameters<GLMap["setPaintProperty"]>[1], value: number) {
  if (map.getPaintProperty(id, property) !== value) map.setPaintProperty(id, property, value);
}
