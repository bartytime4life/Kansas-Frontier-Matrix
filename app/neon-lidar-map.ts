/** Browser-local display cells only. No dataset admission, persistence or I/O. */
import type { FeatureCollection, Polygon } from "geojson";
import type { GeoJSONSource, Map as MapLibreMap, ExpressionSpecification } from "./maplibre-seam";
import { composeMapLayers } from "./map-layer-composition";
import { neonSampleColor, type NeonLidarMode, type NeonLidarPreview } from "./neon-lidar-preview";

export const NEON_LOCAL_SOURCE = "kfm-neon-local-preview";
export const NEON_LOCAL_FILL = "external-neon-local-fill";
export const NEON_LOCAL_GROUND = "external-neon-local-ground";
export type NeonMapProperties = { row: number; column: number; dtm: number | null; dsm: number | null; chm: number | null; local_preview: true; synthetic: boolean };
export type NeonMapData = FeatureCollection<Polygon, NeonMapProperties>;
// Conservative local-display budget, not a scientific validity threshold.
// Out-of-budget columns are omitted, never clamped or written into samples.
export const NEON_3D_MAX_RENDER_HEIGHT_M = 100_000;
export type NeonMapDisplayOptions = { representation?: "flat" | "columns"; verticalExaggeration?: number };
export type Neon3DMapProperties = NeonMapProperties & { display_base_m: number; display_top_m: number };
export type Neon3DMapData = FeatureCollection<Polygon, Neon3DMapProperties>;
export type Neon3DMetadata = {
  baseline_m: number | null; eligible_cells: number; omitted_cells: number;
  input_cells: number; vertical_exaggeration: number; render_height_limit_m: number;
};
const finite = (value: unknown): value is number => typeof value === "number" && Number.isFinite(value);

export function buildNeonMapData(preview: NeonLidarPreview): NeonMapData | null {
  const geo = preview.georeferencing;
  if (!geo || geo.corner_width !== preview.grid.width + 1 || geo.corners.length !== geo.corner_width ** 2) return null;
  const { width, height, dtm, dsm, chm } = preview.grid;
  const features: NeonMapData["features"] = [];
  for (let row = 0; row < height; row++) for (let column = 0; column < width; column++) {
    const index = row * width + column;
    if (dtm[index] === null && dsm[index] === null && chm[index] === null) continue;
    const nw = row * geo.corner_width + column;
    // Shared transformed corners prevent independently rounded cell seams.
    // These straight display edges approximate native projected grid edges;
    // they are not new ground observations or surveyed vegetation footprints.
    const ring = [geo.corners[nw], geo.corners[nw + geo.corner_width],
      geo.corners[nw + geo.corner_width + 1], geo.corners[nw + 1], geo.corners[nw]];
    features.push({ type: "Feature", id: index, geometry: { type: "Polygon", coordinates: [ring] },
      properties: { row, column, dtm: dtm[index], dsm: dsm[index], chm: chm[index], local_preview: true,
        synthetic: preview.data_kind === "synthetic-test" } });
  }
  return { type: "FeatureCollection", features };
}

/**
 * Local relative columns, not absolute terrain or a reconstructed vegetation mesh.
 * Ground and surface share the minimum finite DTM/DSM sample as their baseline.
 * Provider CHM is independent: its column starts at that cell's actual DTM and
 * ends CHM metres above it. The same display scale applies to both ends.
 * Missing/negative CHM and numerically unrepresentable columns are omitted;
 * original source properties and the caller's flat data are never changed.
 */
export function buildNeon3DMapData(data: NeonMapData, mode: NeonLidarMode, verticalExaggeration = 1): { data: Neon3DMapData; metadata: Neon3DMetadata } {
  validateDisplayRequest(data, mode, 1, { representation: "columns", verticalExaggeration });
  let baseline = Infinity;
  for (const { properties } of data.features) for (const value of [properties.dtm, properties.dsm]) {
    if (finite(value)) baseline = Math.min(baseline, value);
  }
  const features: Neon3DMapData["features"] = [];
  if (finite(baseline)) for (const feature of data.features) {
    const p = feature.properties, value = p[mode];
    if (!finite(value) || (mode === "chm" && (!finite(p.dtm) || value < 0))) continue;
    const base = mode === "chm" ? (p.dtm! - baseline) * verticalExaggeration : 0;
    const top = mode === "chm" ? ((p.dtm! - baseline) + value) * verticalExaggeration : (value - baseline) * verticalExaggeration;
    // MapLibre stores render attributes as floats. Do not pass finite JS values
    // that overflow those attributes, or clamp them into plausible heights.
    if (!finite(base) || !finite(top) || !Number.isFinite(Math.fround(base)) || !Number.isFinite(Math.fround(top)) || base < 0 || top < base || top > NEON_3D_MAX_RENDER_HEIGHT_M) continue;
    features.push({ ...feature, properties: { ...p, display_base_m: base, display_top_m: top } });
  }
  return { data: { type: "FeatureCollection", features }, metadata: {
    baseline_m: finite(baseline) ? baseline : null, eligible_cells: features.length,
    omitted_cells: data.features.length - features.length, input_cells: data.features.length, vertical_exaggeration: verticalExaggeration, render_height_limit_m: NEON_3D_MAX_RENDER_HEIGHT_M,
  } };
}

export function neonMapBounds(preview: NeonLidarPreview): [[number, number], [number, number]] | null {
  const geo = preview.georeferencing;
  if (!geo?.corners.length) return null;
  let west = Infinity, east = -Infinity, south = Infinity, north = -Infinity;
  for (const [longitude, latitude] of geo.corners) {
    west = Math.min(west, longitude); east = Math.max(east, longitude);
    south = Math.min(south, latitude); north = Math.max(north, latitude);
  }
  return [[west, south], [east, north]];
}

export function hasNeonLocalHit(hits: readonly { source?: string }[]): boolean {
  return hits.some(hit => hit.source === NEON_LOCAL_SOURCE);
}

function colorExpression(data: NeonMapData, mode: NeonLidarMode): string | ExpressionSpecification {
  let min = mode === "chm" ? 0 : Infinity, max = mode === "chm" ? 30 : -Infinity;
  if (mode !== "chm") for (const { properties } of data.features) for (const value of [properties.dtm, properties.dsm]) {
    if (finite(value)) { min = Math.min(min, value); max = Math.max(max, value); }
  }
  if (min === Infinity || min === max) return neonSampleColor(min === Infinity ? 0 : min, [min === Infinity ? 0 : min, min === Infinity ? 0 : min]);
  const expression: unknown[] = ["interpolate", ["linear"], ["to-number", ["get", mode], 0]];
  // Weighted arithmetic also avoids overflow for extreme but finite inputs.
  let previous = -Infinity;
  for (const fraction of [0, 1 / 3, 2 / 3, 1]) {
    const stop = min * (1 - fraction) + max * fraction;
    if (stop <= previous) continue;
    expression.push(stop, neonSampleColor(stop, [min, max]));
    previous = stop;
  }
  return expression as ExpressionSpecification;
}

function validateDisplayRequest(data: NeonMapData, mode: NeonLidarMode, opacity: number, options: NeonMapDisplayOptions): void {
  if (!["dtm", "dsm", "chm"].includes(mode) || !Number.isFinite(opacity) || opacity < 0 || opacity > 1
    || data.type !== "FeatureCollection" || data.features.length > 128 ** 2
    || (options.representation !== undefined && options.representation !== "flat" && options.representation !== "columns")
    || (options.verticalExaggeration !== undefined && (!Number.isFinite(options.verticalExaggeration) || options.verticalExaggeration < 1 || options.verticalExaggeration > 5)))
    throw new Error("Invalid local NEON display request");
}

type Owner = {
  source: GeoJSONSource; data: NeonMapData; renderedData: NeonMapData | Neon3DMapData;
  representation: "flat" | "columns"; mode: NeonLidarMode; verticalExaggeration: number;
  layers: Map<string, unknown>;
};
const owners = new WeakMap<MapLibreMap, Owner>();

export function applyNeonMapOverlay(map: MapLibreMap, data: NeonMapData, mode: NeonLidarMode, opacity: number, options: NeonMapDisplayOptions = {}): void {
  validateDisplayRequest(data, mode, opacity, options);
  if (opacity === 0) { clearNeonMapOverlay(map); return; }
  const representation = options.representation ?? "flat", verticalExaggeration = options.verticalExaggeration ?? 1;
  // Relative columns must not inherit an unrelated DEM or globe transform.
  // The caller may pitch the existing Mercator camera without enabling terrain.
  if (representation === "columns" && (map.getProjection?.()?.type !== "mercator" || map.getTerrain?.()))
    throw new Error("Local NEON columns require Mercator without an active terrain surface");
  const current = map.getSource(NEON_LOCAL_SOURCE);
  let owner = owners.get(map);
  if (current && current !== owner?.source) throw new Error("Local NEON source ID is already owned");
  const existingLayer = map.getLayer(NEON_LOCAL_FILL);
  for (const id of [NEON_LOCAL_FILL, NEON_LOCAL_GROUND]) {
    const layer = map.getLayer(id);
    if (layer && ((layer as { source?: string }).source !== NEON_LOCAL_SOURCE || !current || current !== owner?.source || layer !== owner?.layers.get(id)))
      throw new Error("Local NEON layer ID is already owned");
  }
  const matches = owner?.data === data && owner.representation === representation
    && (representation === "flat" || (owner.mode === mode && owner.verticalExaggeration === verticalExaggeration));
  const renderedData = matches ? owner!.renderedData : representation === "columns" ? buildNeon3DMapData(data, mode, verticalExaggeration).data : data;
  if (!current) {
    const attribution = data.features.some(feature => feature.properties.synthetic)
      ? "Synthetic local raster grid · no NEON observations" : "NSF NEON, operated by Battelle · local candidate preview";
    map.addSource(NEON_LOCAL_SOURCE, { type: "geojson", data: renderedData, attribution });
    owner = { source: map.getSource(NEON_LOCAL_SOURCE) as GeoJSONSource, data, renderedData, representation, mode, verticalExaggeration, layers: new Map() };
    owners.set(map, owner);
  } else if (owner) {
    if (owner.renderedData !== renderedData) owner.source.setData(renderedData);
    Object.assign(owner, { data, renderedData, representation, mode, verticalExaggeration });
  }
  const layerType = representation === "columns" ? "fill-extrusion" : "fill";
  if (existingLayer && existingLayer.type !== layerType) { map.removeLayer(NEON_LOCAL_FILL); owner?.layers.delete(NEON_LOCAL_FILL); }
  const ground = map.getLayer(NEON_LOCAL_GROUND), pedestal = representation === "columns" && mode === "chm";
  if (ground && !pedestal) { map.removeLayer(NEON_LOCAL_GROUND); owner?.layers.delete(NEON_LOCAL_GROUND); }
  if (pedestal && !ground) {
    // A neutral pedestal makes each canopy column visibly sit on its own DTM
    // sample. These are the same discrete footprints, never an invented mesh.
    map.addLayer({ id: NEON_LOCAL_GROUND, type: "fill-extrusion", source: NEON_LOCAL_SOURCE,
      metadata: { role: "LOCAL_PREVIEW_ONLY", evidence: false, representation: "sampled-ground-pedestal",
        same_sampled_cells: true, heights: "relative-to-shared-sampled-baseline" },
      paint: { "fill-extrusion-color": "#496459", "fill-extrusion-opacity": opacity,
        "fill-extrusion-base": 0, "fill-extrusion-height": ["get", "display_base_m"], "fill-extrusion-vertical-gradient": true }
    }, map.getLayer(NEON_LOCAL_FILL) ? NEON_LOCAL_FILL : undefined);
    owner?.layers.set(NEON_LOCAL_GROUND, map.getLayer(NEON_LOCAL_GROUND));
  } else if (pedestal) map.setPaintProperty(NEON_LOCAL_GROUND, "fill-extrusion-opacity", opacity);
  const color = colorExpression(data, mode), filter: ExpressionSpecification = ["!=", ["get", mode], null];
  if (!map.getLayer(NEON_LOCAL_FILL)) {
    const metadata = { role: "LOCAL_PREVIEW_ONLY", evidence: false, representation,
      ...(representation === "columns" ? { heights: "relative-to-shared-sampled-baseline" } : {}) };
    if (representation === "columns") map.addLayer({ id: NEON_LOCAL_FILL, type: "fill-extrusion", source: NEON_LOCAL_SOURCE, metadata,
      paint: { "fill-extrusion-color": color, "fill-extrusion-opacity": opacity,
        "fill-extrusion-base": ["get", "display_base_m"], "fill-extrusion-height": ["get", "display_top_m"],
        "fill-extrusion-vertical-gradient": true }, filter });
    else map.addLayer({ id: NEON_LOCAL_FILL, type: "fill", source: NEON_LOCAL_SOURCE, metadata,
      paint: { "fill-antialias": false, "fill-opacity": opacity, "fill-color": color }, filter });
    owner?.layers.set(NEON_LOCAL_FILL, map.getLayer(NEON_LOCAL_FILL));
  } else {
    map.setFilter(NEON_LOCAL_FILL, filter);
    map.setPaintProperty(NEON_LOCAL_FILL, representation === "columns" ? "fill-extrusion-color" : "fill-color", color);
    map.setPaintProperty(NEON_LOCAL_FILL, representation === "columns" ? "fill-extrusion-opacity" : "fill-opacity", opacity);
  }
  composeMapLayers(map);
}

export function clearNeonMapOverlay(map: MapLibreMap): void {
  const owner = owners.get(map);
  if (!owner) return;
  if (map.getSource(NEON_LOCAL_SOURCE) === owner.source) {
    let foreign = false;
    for (const id of [NEON_LOCAL_FILL, NEON_LOCAL_GROUND]) {
      const layer = map.getLayer(id);
      if (!layer) continue;
      if (layer === owner.layers.get(id) && (layer as { source?: string }).source === NEON_LOCAL_SOURCE) map.removeLayer(id);
      else foreign = true;
    }
    // An unexpected replacement layer must keep its referenced source intact.
    if (!foreign) map.removeSource(NEON_LOCAL_SOURCE);
  }
  owners.delete(map);
}
