/** Browser-local display cells only. No dataset admission, persistence or I/O. */
import type { FeatureCollection, Polygon } from "geojson";
import type { GeoJSONSource, Map as MapLibreMap, ExpressionSpecification } from "./maplibre-seam";
import { composeMapLayers } from "./map-layer-composition";
import { neonSampleColor, type NeonLidarMode, type NeonLidarPreview } from "./neon-lidar-preview";

export const NEON_LOCAL_SOURCE = "kfm-neon-local-preview";
export const NEON_LOCAL_FILL = "external-neon-local-fill";
export type NeonMapProperties = { row: number; column: number; dtm: number | null; dsm: number | null; chm: number | null; local_preview: true; synthetic: boolean };
export type NeonMapData = FeatureCollection<Polygon, NeonMapProperties>;

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
    if (value !== null) { min = Math.min(min, value); max = Math.max(max, value); }
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

const owners = new WeakMap<MapLibreMap, { source: GeoJSONSource; data: NeonMapData }>();

export function applyNeonMapOverlay(map: MapLibreMap, data: NeonMapData, mode: NeonLidarMode, opacity: number): void {
  if (!["dtm", "dsm", "chm"].includes(mode) || !Number.isFinite(opacity) || opacity < 0 || opacity > 1
    || data.type !== "FeatureCollection" || data.features.length > 128 ** 2) throw new Error("Invalid local NEON display request");
  if (opacity === 0) { clearNeonMapOverlay(map); return; }
  const current = map.getSource(NEON_LOCAL_SOURCE);
  let owner = owners.get(map);
  if (current && current !== owner?.source) throw new Error("Local NEON source ID is already owned");
  const existingLayer = map.getLayer(NEON_LOCAL_FILL);
  if (existingLayer && (existingLayer as { source?: string }).source !== NEON_LOCAL_SOURCE) throw new Error("Local NEON layer ID is already owned");
  if (!current) {
    const attribution = data.features.some(feature => feature.properties.synthetic)
      ? "Synthetic local raster grid · no NEON observations" : "NSF NEON, operated by Battelle · local candidate preview";
    map.addSource(NEON_LOCAL_SOURCE, { type: "geojson", data, attribution });
    owner = { source: map.getSource(NEON_LOCAL_SOURCE) as GeoJSONSource, data };
    owners.set(map, owner);
  } else if (owner && owner.data !== data) {
    owner.source.setData(data); owner.data = data;
  }
  if (!existingLayer) map.addLayer({ id: NEON_LOCAL_FILL, type: "fill", source: NEON_LOCAL_SOURCE,
    metadata: { role: "LOCAL_PREVIEW_ONLY", evidence: false }, paint: { "fill-antialias": false, "fill-opacity": opacity, "fill-color": colorExpression(data, mode) },
    filter: ["!=", ["get", mode], null] });
  else {
    map.setFilter(NEON_LOCAL_FILL, ["!=", ["get", mode], null]);
    map.setPaintProperty(NEON_LOCAL_FILL, "fill-color", colorExpression(data, mode));
    map.setPaintProperty(NEON_LOCAL_FILL, "fill-opacity", opacity);
  }
  composeMapLayers(map);
}

export function clearNeonMapOverlay(map: MapLibreMap): void {
  const owner = owners.get(map);
  if (!owner) return;
  if (map.getSource(NEON_LOCAL_SOURCE) === owner.source) {
    if (map.getLayer(NEON_LOCAL_FILL) && (map.getLayer(NEON_LOCAL_FILL) as { source?: string }).source === NEON_LOCAL_SOURCE)
      map.removeLayer(NEON_LOCAL_FILL);
    map.removeSource(NEON_LOCAL_SOURCE);
  }
  owners.delete(map);
}
