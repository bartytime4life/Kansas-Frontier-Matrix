import type { Map as GLMap, StyleSpecification, LayerSpecification } from "./maplibre-seam";

export type SurfaceBounds = [number, number, number, number];
export type SurfaceCapture = {
  bounds: SurfaceBounds; style: StyleSpecification; copiedAt: string; omitted: number;
  images: { id: string; data: { width: number; height: number; data: Uint8Array }; pixelRatio: number; sdf: boolean }[];
};
const clone = <T,>(value: T): T => JSON.parse(JSON.stringify(value));

export function surfaceBoundsMatch(map: Pick<GLMap, "getBounds">, bounds: SurfaceBounds) {
  try {
    const b = map.getBounds(), actual = [b.getWest(), b.getSouth(), b.getEast(), b.getNorth()];
    return bounds.every((value, i) => Math.abs(value - actual[i]) < 1e-6);
  } catch { return false; }
}

/** Freeze the selected layers and their source clocks, independently of locator preview movement. */
export function captureSelectedSurface(map: GLMap, bounds: SurfaceBounds): SurfaceCapture | null {
  if (!surfaceBoundsMatch(map, bounds)) return null;
  const current = map.getStyle();
  if (!current) return null;
  const sources: StyleSpecification["sources"] = {}, layers: LayerSpecification[] = [];
  let omitted = 0;
  for (const layer of current.layers) {
    if (layer.layout?.visibility === "none") continue;
    const source = "source" in layer ? current.sources[layer.source as string] : undefined;
    // Custom renderers and live canvas/video sources cannot be copied as a stable map layer.
    if ((layer as { type: string }).type === "custom" || source && !["vector", "raster", "raster-dem", "geojson", "image"].includes(source.type)) { omitted++; continue; }
    if ("source" in layer && !source) { omitted++; continue; }
    if (source && "source" in layer) sources[layer.source as string] = clone(source);
    layers.push(clone(layer));
  }
  const style: StyleSpecification = { version: 8, sources, layers, projection: { type: "mercator" } };
  if (current.glyphs) style.glyphs = current.glyphs;
  if (current.sprite) style.sprite = clone(current.sprite);
  const images: SurfaceCapture["images"] = [];
  for (const id of map.listImages()) {
    const image = map.getImage(id);
    if (image?.data) images.push({ id, data: { width: image.data.width, height: image.data.height, data: new Uint8Array(image.data.data) }, pixelRatio: image.pixelRatio, sdf: image.sdf });
  }
  return { bounds: [...bounds], style, images, omitted, copiedAt: new Date().toISOString() };
}

/** Opaque outside mask keeps the original selected slice visible at every camera position. */
export function surfaceSliceStyle(capture: SurfaceCapture): StyleSpecification {
  const [w, s, e, n] = capture.bounds, style = clone(capture.style);
  const ring = [[w,s],[e,s],[e,n],[w,n],[w,s]];
  style.sources["kfm-selected-surface-mask"] = { type: "geojson", data: { type: "FeatureCollection", features: [
    { type: "Feature", properties: { outside: true }, geometry: { type: "Polygon", coordinates: [[[-180,-85],[-180,85],[180,85],[180,-85],[-180,-85]], ring] } },
    { type: "Feature", properties: { outside: false }, geometry: { type: "LineString", coordinates: ring } },
  ] } };
  style.layers.push(
    { id: "kfm-selected-surface-outside", source: "kfm-selected-surface-mask", type: "fill", filter: ["==", "outside", true], paint: { "fill-color": "#101b20", "fill-opacity": 1 } },
    { id: "kfm-selected-surface-boundary", source: "kfm-selected-surface-mask", type: "line", filter: ["==", "outside", false], paint: { "line-color": "#e0b46f", "line-width": 2 } },
  );
  return style;
}

export function surfaceCameraBounds(bounds: SurfaceBounds): [[number, number], [number, number]] {
  return [[bounds[0], bounds[1]], [bounds[2], bounds[3]]];
}

export function constrainSurfaceCenter(bounds: SurfaceBounds, center: {lng: number; lat: number}): [number, number] {
  return [Math.max(bounds[0], Math.min(bounds[2], center.lng)), Math.max(bounds[1], Math.min(bounds[3], center.lat))];
}

/** Retain categorical nearest-neighbor rendering when the user restores normal imagery. */
export function surfaceRasterSampling(style: StyleSpecification, smooth: boolean) {
  return style.layers.filter(layer => layer.type === "raster").map(layer => ({ id: layer.id,
    value: smooth ? (layer as Extract<LayerSpecification, {type:"raster"}>).paint?.["raster-resampling"] ?? "linear" : "nearest" }));
}
