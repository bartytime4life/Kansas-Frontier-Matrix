import type { FeatureCollection, LineString, MultiLineString } from "geojson";
import type { GeoJSONSource, Map as MapLibreMap } from "maplibre-gl";
import { buildLocalImportPreview, IMPORT_PREVIEW_MAX_BYTES } from "./import-preview";
import { ROAD_MAP_EDITIONS } from "./road-map-editions";

const SOURCE_PREFIX = "kfm-road-study-source-";
const LAYER_PREFIX = "kfm-road-study-line-";
export const ROAD_STUDY_MAX_LAYERS = 4;
export const ROAD_STUDY_COLORS = ["#ffbd69", "#60d3e8", "#e993e3", "#a8e08e"] as const;

export type RoadStudyLayer = Readonly<{
  editionId: string;
  editionLabel: string;
  fileName: string;
  featureCount: number;
  color: string;
  opacity: number;
  visible: boolean;
  data: FeatureCollection<LineString | MultiLineString>;
}>;

export function inspectRoadStudyFile(input: Readonly<{
  editionId: string;
  fileName: string;
  fileSizeBytes: number;
  text: string;
  color: string;
  supportedBounds: Readonly<{ west: number; south: number; east: number; north: number }>;
}>): RoadStudyLayer {
  const edition = ROAD_MAP_EDITIONS.find((candidate) => candidate.id === input.editionId);
  if (!edition || edition.localPdfState === "BLANK") throw new Error("Choose a usable map edition.");
  if (!/\.geojson$|\.json$/i.test(input.fileName)) throw new Error("Choose a road-only GeoJSON file, not a whole map PDF.");
  if (input.fileSizeBytes > IMPORT_PREVIEW_MAX_BYTES) throw new Error("Road study files must be no larger than 2 MB.");
  const preview = buildLocalImportPreview({
    fileName: input.fileName,
    fileSizeBytes: input.fileSizeBytes,
    text: input.text,
    inspectedAt: new Date().toISOString(),
    supportedBounds: input.supportedBounds,
  });
  if (preview.sourceFormat !== "GEOJSON" || !preview.renderAllowed || preview.coverage !== "WITHIN_KANSAS_CONTEXT") throw new Error("The road lines must be GeoJSON inside the Kansas study area.");
  if (preview.invalidFeatureCount || preview.featureCount > 2_500) throw new Error("The file has invalid features or exceeds 2,500 road lines.");
  if (preview.sensitivitySignals.length) throw new Error("The file has fields needing sensitivity review; remove them for this local line-only study.");
  if (preview.featureCollection.features.some((feature) => feature.geometry.type !== "LineString" && feature.geometry.type !== "MultiLineString")) throw new Error("Only road line geometry is allowed; full map images, points, and polygons stay out of this comparison.");
  // Strip source properties from the display carrier. This remains browser-local
  // comparison geometry, not a KFM RoadSegment, source admission, or evidence.
  const data: FeatureCollection<LineString | MultiLineString> = {
    type: "FeatureCollection",
    features: preview.featureCollection.features.map((feature) => ({
      type: "Feature" as const,
      properties: {},
      geometry: feature.geometry as LineString | MultiLineString,
    })),
  };
  return {
    editionId: edition.id,
    editionLabel: edition.label,
    fileName: input.fileName,
    featureCount: preview.featureCount,
    color: input.color,
    opacity: 0.8,
    visible: true,
    data,
  };
}

export function applyRoadStudyLayers(map: MapLibreMap, layers: readonly RoadStudyLayer[]) {
  const wanted = new Set(layers.map((layer) => `${LAYER_PREFIX}${layer.editionId}`));
  for (const layer of map.getStyle().layers ?? []) {
    if (!layer.id.startsWith(LAYER_PREFIX) || wanted.has(layer.id)) continue;
    map.removeLayer(layer.id);
    const sourceId = `${SOURCE_PREFIX}${layer.id.slice(LAYER_PREFIX.length)}`;
    if (map.getSource(sourceId)) map.removeSource(sourceId);
  }
  for (const layer of layers) {
    const sourceId = `${SOURCE_PREFIX}${layer.editionId}`;
    const layerId = `${LAYER_PREFIX}${layer.editionId}`;
    const source = map.getSource(sourceId) as GeoJSONSource | undefined;
    if (source) source.setData(layer.data);
    else map.addSource(sourceId, { type: "geojson", data: layer.data });
    if (!map.getLayer(layerId)) map.addLayer({
      id: layerId,
      source: sourceId,
      type: "line",
      layout: { visibility: layer.visible ? "visible" : "none", "line-cap": "round", "line-join": "round" },
      paint: { "line-color": layer.color, "line-width": 3, "line-opacity": layer.opacity },
    });
    else {
      map.setPaintProperty(layerId, "line-color", layer.color);
      map.setPaintProperty(layerId, "line-opacity", layer.opacity);
      map.setLayoutProperty(layerId, "visibility", layer.visible ? "visible" : "none");
    }
  }
}
