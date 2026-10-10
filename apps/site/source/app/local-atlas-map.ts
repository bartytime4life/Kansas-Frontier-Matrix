import type { ExpressionSpecification, Map as AtlasMap, MapMouseEvent } from "./maplibre-seam";
import type { AtlasPreview, AtlasRaster } from "./local-atlas-client";

export const LOCAL_ATLAS_PREFIX = "kfm-local-atlas-";
const SOURCE = `${LOCAL_ATLAS_PREFIX}source`;
const LAYERS = ["fill", "line", "density", "point", "raster"].map(v => `${LOCAL_ATLAS_PREFIX}${v}`);
export const ATLAS_COLORS = { low: "#1c7898", mid: "#d9e9db", high: "#e4ae58", missing: "#72818d" };
export type AtlasScale = { min: number; max: number; count: number; difference: boolean };
export function atlasScale(preview: AtlasPreview, field: string | null, difference = false): AtlasScale | null {
  if (preview.kind === "raster") { const d = preview.data as AtlasRaster; return d.min === null || d.max === null ? null : { min: d.min, max: d.max, count: preview.displayedCount, difference: false }; }
  if (!field) return null;
  const values = (preview.data as GeoJSON.FeatureCollection).features.map(f => f.properties?.[field]).filter((n): n is number => typeof n === "number" && Number.isFinite(n));
  if (!values.length) return null;
  const min = Math.min(...values), max = Math.max(...values), bound = Math.max(Math.abs(min), Math.abs(max));
  return { min: difference ? -bound : min, max: difference ? bound : max, count: values.length, difference };
}
export function atlasColor(field: string | null, scale: AtlasScale | null): string | ExpressionSpecification {
  if (!field || !scale) return ATLAS_COLORS.high;
  const value: ExpressionSpecification = ["get", field];
  const ramp: string | ExpressionSpecification = scale.min === scale.max ? ATLAS_COLORS.mid
    : ["interpolate", ["linear"], value, scale.min, ATLAS_COLORS.low, (scale.min + scale.max) / 2, ATLAS_COLORS.mid, scale.max, ATLAS_COLORS.high];
  return ["case", ["==", ["typeof", value], "number"], ramp, ATLAS_COLORS.missing];
}
export function localAtlasHit(map: AtlasMap, point: MapMouseEvent["point"]): boolean {
  try {
    const layers = LAYERS.filter(id => id !== LAYERS[4] && Boolean(map.getLayer(id)));
    if (layers.length > 0 && map.queryRenderedFeatures(point, { layers }).length > 0) return true;
    // Raster images have no rendered features. Own clicks within their displayed
    // image bounds, including nodata pixels; this does not promise pixel lookup.
    if (!map.getLayer(LAYERS[4]) || map.getLayoutProperty(LAYERS[4], "visibility") === "none"
      || Number(map.getPaintProperty(LAYERS[4], "raster-opacity")) <= 0) return false;
    const source = map.getStyle().sources[SOURCE];
    if (source?.type !== "image" || !source.coordinates.length) return false;
    const location = map.unproject(point), lng = ((location.lng + 180) % 360 + 360) % 360 - 180;
    const west = Math.min(...source.coordinates.map(c => c[0])), east = Math.max(...source.coordinates.map(c => c[0]));
    const south = Math.min(...source.coordinates.map(c => c[1])), north = Math.max(...source.coordinates.map(c => c[1]));
    return lng >= west && lng <= east && location.lat >= south && location.lat <= north;
  } catch { return false; }
}
export const atlasPointsOnly = (preview: AtlasPreview) => preview.kind === "vector" && (preview.data as GeoJSON.FeatureCollection).features.length > 0
  && (preview.data as GeoJSON.FeatureCollection).features.every(f => f.geometry?.type === "Point" || f.geometry?.type === "MultiPoint");

export function attachAtlasPreview(map: AtlasMap, preview: AtlasPreview, options: { field: string | null; difference: boolean; density: boolean; opacity: number; flatMap: boolean },
  inspect: (properties: Record<string, unknown>) => void, state: (value: "visible" | "flat-map-required" | "unavailable") => void) {
  let disposed = false, failed = false;
  const remove = () => {
    for (const id of [...LAYERS].reverse()) try { if (map.getLayer(id)) map.removeLayer(id); } catch { /* style replaced */ }
    try { if (map.getSource(SOURCE)) map.removeSource(SOURCE); } catch { /* map disposed */ }
  };
  const isFlat = () => options.flatMap && map.getPitch() === 0 && !map.getTerrain() && map.getProjection()?.type === "mercator";
  const update = () => {
    if (disposed || failed) return;
    try {
      const visible = preview.kind !== "raster" || isFlat();
      for (const id of LAYERS) if (map.getLayer(id)) map.setLayoutProperty(id, "visibility", visible ? "visible" : "none");
      state(visible ? "visible" : "flat-map-required");
    } catch { failed = true; remove(); state("unavailable"); }
  };
  const error = (event: unknown) => { if (!disposed && event && typeof event === "object" && "sourceId" in event && String(event.sourceId).startsWith(LOCAL_ATLAS_PREFIX)) { failed = true; remove(); state("unavailable"); } };
  const click = (event: MapMouseEvent) => {
    if (disposed || failed || preview.kind === "raster") return;
    try {
      const layers = LAYERS.filter(id => map.getLayer(id));
      const feature = map.queryRenderedFeatures(event.point, { layers })[0];
      if (feature?.properties) inspect(feature.properties);
    } catch { /* Style change invalidates a click. */ }
  };
  try {
    remove();
    const opacity = Math.max(0, Math.min(1, options.opacity));
    if (preview.kind === "raster") {
      const data = preview.data as AtlasRaster;
      map.addSource(SOURCE, { type: "image", url: data.imageDataUrl, coordinates: data.coordinates });
      map.addLayer({ id: LAYERS[4], type: "raster", source: SOURCE, layout: { visibility: "none" }, paint: { "raster-opacity": opacity, "raster-fade-duration": 0, "raster-resampling": "nearest" } });
    } else {
      const color = atlasColor(options.field, atlasScale(preview, options.field, options.difference));
      map.addSource(SOURCE, { type: "geojson", data: preview.data as GeoJSON.FeatureCollection, generateId: true, attribution: preview.source.attribution });
      map.addLayer({ id: LAYERS[0], type: "fill", source: SOURCE, filter: ["==", ["geometry-type"], "Polygon"], paint: { "fill-color": color, "fill-opacity": opacity * .82 } });
      map.addLayer({ id: LAYERS[1], type: "line", source: SOURCE, filter: ["!=", ["geometry-type"], "Point"], paint: { "line-color": ["case", ["==", ["geometry-type"], "LineString"], color, "#d7e6ee"], "line-width": ["case", ["==", ["geometry-type"], "LineString"], 2, .7], "line-opacity": opacity } });
      if (options.density && atlasPointsOnly(preview)) map.addLayer({ id: LAYERS[2], type: "heatmap", source: SOURCE, paint: {
        "heatmap-weight": 1, "heatmap-radius": 24, "heatmap-intensity": 1, "heatmap-opacity": opacity,
        "heatmap-color": ["interpolate", ["linear"], ["heatmap-density"], 0, "rgba(28,120,152,0)", .25, ATLAS_COLORS.low, .6, ATLAS_COLORS.mid, 1, ATLAS_COLORS.high],
      } });
      map.addLayer({ id: LAYERS[3], type: "circle", source: SOURCE, filter: ["==", ["geometry-type"], "Point"], paint: { "circle-color": color, "circle-radius": options.density ? 3 : 5,
        "circle-opacity": options.density ? .2 * opacity : opacity, "circle-stroke-color": "#edf3f8", "circle-stroke-width": options.density ? 0 : 1 } });
    }
    map.on("click", click); map.on("move", update); map.on("error", error); update();
  } catch { failed = true; remove(); state("unavailable"); }
  return { dispose() { if (disposed) return; disposed = true; map.off("click", click); map.off("move", update); map.off("error", error); remove(); } };
}
