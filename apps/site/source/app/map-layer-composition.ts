import type { Map as MapLibreMap } from "./maplibre-seam";
import { LAYER_REGISTRY } from "./explorer-data";

const registryIds = new Set(LAYER_REGISTRY.flatMap((record) => record.renderers.map((renderer) => renderer.id)));
const daylightLayerId = "kfm-daylight-context-fill";
const systemIds = new Set([
  "kfm-import-preview-fill", "kfm-import-preview-line", "kfm-import-preview-point",
  "kfm-analysis-area-fill", "kfm-analysis-area-line", "kfm-selection-glow",
  "kfm-selection-halo", "kfm-selection-fill", "kfm-selection-line",
  "kfm-selection-point", "kfm-selection-pulse", "kfm-measure-fill",
  "kfm-measure-line", "kfm-measure-points",
]);

type LayerLike = { id: string; type: string };
const isOverlay = (layer: LayerLike) => registryIds.has(layer.id) || systemIds.has(layer.id)
  || layer.id === daylightLayerId || layer.id.startsWith("external-") || layer.id.startsWith("kfm-ee-context-layer-");

type RasterFamily = "surface" | "water" | "fire" | "air" | "radar" | "reference" | "other";
const rasterFamily = (id: string): RasterFamily => {
  if (id.startsWith("external-blm-plss-") || id.startsWith("external-blm-mlrs-") || id.startsWith("external-kdot-")) return "reference";
  if (id.includes("3dep-") || id.includes("goes-geocolor") || id.startsWith("kfm-ee-context-layer-")) return "surface";
  if (id.includes("3dhp-") || id.includes("wbd-") || id.includes("nwm-")) return "water";
  if (id.includes("firms-active-fire")) return "fire";
  if (id.includes("lightning")) return "air";
  if (id.includes("forecast-wind")) return "air";
  if (id.includes("nws-radar")) return "radar";
  return "other";
};
const rasterFamilyOrder: Record<RasterFamily, number> = { surface: 0, water: 1, other: 2, reference: 6, fire: 3, air: 4, radar: 5 };
// These are display budgets within one visual family. Transparent provider pixels
// still allow unrelated observations to be seen without dividing all layers by 14.
const rasterFamilyLimit: Record<RasterFamily, number> = { surface: 0.68, water: 0.82, fire: 0.72, air: 0.78, radar: 0.76, other: 0.9, reference: 1 };

export const orderedOverlayIds = (layers: readonly LayerLike[]): string[] => layers
  .filter(isOverlay)
  .map((layer, index) => ({ layer, index }))
  .sort((left, right) => {
    const tier = (layer: LayerLike) => systemIds.has(layer.id) ? 5
      : layer.id === daylightLayerId ? 0.5
      : layer.type === "raster" || layer.type === "hillshade" ? 0
      : layer.type === "fill" || layer.type === "fill-extrusion" ? 1
      : layer.type === "line" ? 2
      : layer.type === "circle" ? 3 : 4;
    return tier(left.layer) - tier(right.layer)
      || (tier(left.layer) === 0 ? rasterFamilyOrder[rasterFamily(left.layer.id)] - rasterFamilyOrder[rasterFamily(right.layer.id)] : 0)
      || left.index - right.index;
  })
  .map(({ layer }) => layer.id);

export const composeMapLayers = (map: MapLibreMap): void => {
  const layers = map.getStyle().layers ?? [];
  const desired = orderedOverlayIds(layers);
  if (!desired.length || desired.every((id, index) => layers[layers.length - desired.length + index]?.id === id)) return;
  for (const id of desired) map.moveLayer(id);
};

// Keep the user's slider values as requests so hiding a raster restores the others.
const rasterRequests = new WeakMap<MapLibreMap, Map<string, number>>();
const fillRequests = new WeakMap<MapLibreMap, Map<string, number>>();
export const requestRasterOpacity = (map: MapLibreMap, id: string, opacity: number): void => {
  let requests = rasterRequests.get(map);
  if (!requests) { requests = new Map(); rasterRequests.set(map, requests); }
  requests.set(id, Math.max(0, Math.min(1, opacity)));
};

export const balancedRasterOpacities = (requests: readonly number[]): number[] => {
  const total = requests.reduce((sum, value) => sum + value, 0);
  const scale = requests.length > 1 && total > 0.9 ? 0.9 / total : 1;
  return requests.map((value) => value * scale);
};

export const balanceMapRasters = (map: MapLibreMap): void => {
  const requests = rasterRequests.get(map);
  if (!requests) return;
  const visible = [...requests].filter(([id]) => map.getLayer(id) && map.getLayoutProperty(id, "visibility") !== "none");
  const families = new Map<RasterFamily, [string, number][]>();
  for (const [id, opacity] of visible) {
    const family = rasterFamily(id);
    const group = families.get(family) ?? [];
    group.push([id, opacity]);
    families.set(family, group);
  }
  for (const [family, group] of families) {
    const total = group.reduce((sum, [, opacity]) => sum + opacity, 0);
    const scale = family !== "reference" && group.length > 1 && total > rasterFamilyLimit[family] ? rasterFamilyLimit[family] / total : 1;
    for (const [id, opacity] of group) {
      const effective = opacity * scale;
      if (map.getPaintProperty(id, "raster-opacity") !== effective) map.setPaintProperty(id, "raster-opacity", effective);
    }
  }
};

// Regional Web Mercator tiles cannot be displayed as trustworthy globe imagery.
export const syncMercatorRaster = (map: MapLibreMap, id: string, opacity: number, requestedProjection: "mercator" | "globe" = "mercator"): void => {
  if (!map.getLayer(id)) { balanceMapRasters(map); return; }
  const visible = requestedProjection === "mercator" && map.getProjection()?.type === "mercator";
  if (map.getLayoutProperty(id, "visibility") !== (visible ? "visible" : "none"))
    map.setLayoutProperty(id, "visibility", visible ? "visible" : "none");
  requestRasterOpacity(map, id, opacity);
  balanceMapRasters(map);
  composeMapLayers(map);
};

export const requestFillOpacity = (map: MapLibreMap, id: string, opacity: number): void => {
  let requests = fillRequests.get(map);
  if (!requests) { requests = new Map(); fillRequests.set(map, requests); }
  requests.set(id, Math.max(0, Math.min(1, opacity)));
};

export const balanceMapFills = (map: MapLibreMap): void => {
  const requests = fillRequests.get(map);
  if (!requests) return;
  const visible = [...requests].filter(([id]) => map.getLayer(id) && map.getLayoutProperty(id, "visibility") !== "none");
  const total = visible.reduce((sum, [, opacity]) => sum + opacity, 0);
  const scale = visible.length > 1 && total > 0.65 ? 0.65 / total : 1;
  visible.forEach(([id, opacity]) => {
    const effective = opacity * scale;
    if (map.getPaintProperty(id, "fill-opacity") !== effective) map.setPaintProperty(id, "fill-opacity", effective);
  });
};
