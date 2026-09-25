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

// Browser diagnostics use finite check IDs. MapLibre errors may contain source
// URLs or request details, so neither exception messages nor stacks leave here.
export type MapRuntimeCheckFailure =
  | "STYLE_CHECK_FAILED" | "SOURCE_CHECK_FAILED" | "CANVAS_CHECK_FAILED"
  | "PROJECTION_CHECK_FAILED" | "INTERACTION_CHECK_FAILED"
  | "IDLE_CHECK_FAILED" | "TILE_CHECK_FAILED";

export function sampleMapRuntimeHealth(
  map: Pick<GLMap, "isStyleLoaded" | "getSource" | "getCanvas" | "getProjection" | "loaded" | "areTilesLoaded" | "dragPan" | "scrollZoom" | "keyboard" | "touchZoomRotate">,
  sourceIds: readonly string[],
  handlersBound: boolean,
  controlsBound: boolean,
) {
  const failedChecks: MapRuntimeCheckFailure[] = [];
  const read = <T>(code: MapRuntimeCheckFailure, fallback: T, operation: () => T): T => {
    try { return operation(); } catch { failedChecks.push(code); return fallback; }
  };
  const styleLoaded = read("STYLE_CHECK_FAILED", false, () => map.isStyleLoaded() === true);
  const sourceReadyById: Record<string, boolean> = {};
  for (const id of sourceIds) {
    // isSourceLoaded emits a MapLibre error event when a style swap has not yet
    // created its tile manager. The local GeoJSON source can be sampled without
    // that side effect; the separate tile check still covers visible tiles.
    sourceReadyById[id] = styleLoaded && read("SOURCE_CHECK_FAILED", false, () => map.getSource(id)?.loaded() === true);
  }
  const canvasReady = read("CANVAS_CHECK_FAILED", false, () => {
    const canvas = map.getCanvas();
    const bounds = canvas.getBoundingClientRect();
    return bounds.width > 0 && bounds.height > 0 && canvas.width > 0 && canvas.height > 0;
  });
  // A style with MapLibre's default Mercator projection has no explicit
  // projection entry, so getProjection() can return undefined at runtime.
  const projection = read("PROJECTION_CHECK_FAILED", "mercator" as "mercator" | "globe", () => map.getProjection()?.type === "globe" ? "globe" : "mercator");
  const interactionsReady = handlersBound && read("INTERACTION_CHECK_FAILED", false, () =>
    map.dragPan.isEnabled() && map.scrollZoom.isEnabled() && map.keyboard.isEnabled() && map.touchZoomRotate.isEnabled());
  return {
    sourceReadyById,
    styleLoaded,
    canvasReady,
    projection,
    interactionsReady,
    controlsReady: controlsBound,
    idle: read("IDLE_CHECK_FAILED", false, () => map.loaded()),
    tilesLoaded: read("TILE_CHECK_FAILED", false, () => map.areTilesLoaded()),
    failedChecks: [...new Set(failedChecks)],
  };
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
