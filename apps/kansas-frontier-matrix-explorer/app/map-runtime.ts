import type { Feature, FeatureCollection, Geometry, Position } from "geojson";
import type {
  FilterSpecification,
  GeoJSONSource,
  LayerSpecification,
  Map as MapLibreMap,
  StyleSpecification,
} from "maplibre-gl";
import { LAYER_REGISTRY } from "./explorer-data";

export type BasemapKey = "midnight" | "prairie";

export const BASEMAPS: Record<BasemapKey, { title: string; note: string; style: StyleSpecification }> = {
  midnight: {
    title: "Midnight navy",
    note: "High-contrast local style",
    style: {
      version: 8,
      name: "KFM Midnight",
      sources: {},
      layers: [{ id: "kfm-background", type: "background", paint: { "background-color": "#07171a" } }],
    },
  },
  prairie: {
    title: "Prairie dusk",
    note: "Low-glare earthen local style",
    style: {
      version: 8,
      name: "KFM Prairie Dusk",
      sources: {},
      layers: [{ id: "kfm-background", type: "background", paint: { "background-color": "#17231f" } }],
    },
  },
};

const emptyCollection = (): FeatureCollection => ({ type: "FeatureCollection", features: [] });

const SYSTEM_LAYER_IDS = [
  "kfm-measure-fill",
  "kfm-measure-line",
  "kfm-measure-points",
  "kfm-selection-fill",
  "kfm-selection-line",
  "kfm-selection-point",
];

const addSystemLayers = (map: MapLibreMap) => {
  if (!map.getSource("kfm-selection")) {
    map.addSource("kfm-selection", { type: "geojson", data: emptyCollection() });
  }
  if (!map.getLayer("kfm-selection-fill")) {
    map.addLayer({ id: "kfm-selection-fill", type: "fill", source: "kfm-selection", filter: ["==", ["geometry-type"], "Polygon"], paint: { "fill-color": "#f4dfae", "fill-opacity": 0.18, "fill-outline-color": "#fff4ce" } });
  }
  if (!map.getLayer("kfm-selection-line")) {
    map.addLayer({ id: "kfm-selection-line", type: "line", source: "kfm-selection", filter: ["==", ["geometry-type"], "LineString"], paint: { "line-color": "#fff4ce", "line-width": 6, "line-opacity": 0.95 } });
  }
  if (!map.getLayer("kfm-selection-point")) {
    map.addLayer({ id: "kfm-selection-point", type: "circle", source: "kfm-selection", filter: ["==", ["geometry-type"], "Point"], paint: { "circle-color": "#fff4ce", "circle-radius": 11, "circle-opacity": 0.95, "circle-stroke-color": "#061416", "circle-stroke-width": 4 } });
  }

  if (!map.getSource("kfm-measure")) {
    map.addSource("kfm-measure", { type: "geojson", data: emptyCollection() });
  }
  if (!map.getLayer("kfm-measure-fill")) {
    map.addLayer({ id: "kfm-measure-fill", type: "fill", source: "kfm-measure", filter: ["==", ["geometry-type"], "Polygon"], paint: { "fill-color": "#73c7d2", "fill-opacity": 0.16 } });
  }
  if (!map.getLayer("kfm-measure-line")) {
    map.addLayer({ id: "kfm-measure-line", type: "line", source: "kfm-measure", filter: ["in", ["geometry-type"], ["literal", ["LineString", "Polygon"]]], paint: { "line-color": "#8ee4ef", "line-width": 3, "line-dasharray": [2, 1] } });
  }
  if (!map.getLayer("kfm-measure-points")) {
    map.addLayer({ id: "kfm-measure-points", type: "circle", source: "kfm-measure", filter: ["==", ["geometry-type"], "Point"], paint: { "circle-color": "#f4dfae", "circle-radius": 5, "circle-stroke-color": "#07171a", "circle-stroke-width": 2 } });
  }
};

const temporalFilter = (year: number, mode: "exact" | "through"): FilterSpecification =>
  mode === "exact"
    ? (["==", ["get", "year"], year] as FilterSpecification)
    : (["<=", ["get", "year"], year] as FilterSpecification);

const mergeFilters = (base?: FilterSpecification, temporal?: FilterSpecification): FilterSpecification | undefined => {
  if (base && temporal) return ["all", base, temporal] as FilterSpecification;
  return base ?? temporal;
};

export const applyRegistryState = (
  map: MapLibreMap,
  visibility: Record<string, boolean>,
  opacity: Record<string, number>,
  year: number,
  order: string[],
) => {
  for (const record of LAYER_REGISTRY) {
    if (!map.getSource(record.sourceId)) {
      map.addSource(record.sourceId, {
        type: "geojson",
        data: record.data,
        promoteId: "fid",
        ...(record.sourceOptions ?? {}),
        attribution: record.attribution,
      });
    }

    for (const renderer of record.renderers) {
      if (!map.getLayer(renderer.id)) map.addLayer(renderer.spec as LayerSpecification);
      map.setLayerZoomRange(renderer.id, record.minZoom, record.maxZoom);

      map.setLayoutProperty(renderer.id, "visibility", visibility[record.id] ? "visible" : "none");
      const filter = mergeFilters(
        renderer.baseFilter,
        record.temporal ? temporalFilter(year, record.temporal.mode) : undefined,
      );
      if (filter) map.setFilter(renderer.id, filter);

      for (const property of renderer.opacityProperties ?? []) {
        map.setPaintProperty(renderer.id, property, opacity[record.id] ?? record.defaultOpacity);
      }
    }
  }

  addSystemLayers(map);
  reorderRegistryLayers(map, order);
};

export const reorderRegistryLayers = (map: MapLibreMap, order: string[]) => {
  for (const layerId of order) {
    const record = LAYER_REGISTRY.find((candidate) => candidate.id === layerId);
    for (const renderer of record?.renderers ?? []) {
      if (map.getLayer(renderer.id)) map.moveLayer(renderer.id);
    }
  }
  for (const id of SYSTEM_LAYER_IDS) if (map.getLayer(id)) map.moveLayer(id);
};

export const updateSelectionSource = (map: MapLibreMap, selection?: Feature<Geometry> | null) => {
  const source = map.getSource("kfm-selection") as GeoJSONSource | undefined;
  source?.setData({ type: "FeatureCollection", features: selection ? [selection] : [] });
};

export const buildMeasurementData = (coordinates: [number, number][], mode: "distance" | "area" | null): FeatureCollection => {
  if (!mode || coordinates.length === 0) return emptyCollection();
  const features: Feature[] = coordinates.map((coordinate, index) => ({
    type: "Feature",
    id: `measure-${index}`,
    properties: {},
    geometry: { type: "Point", coordinates: coordinate },
  }));
  if (mode === "distance" && coordinates.length > 1) {
    features.unshift({ type: "Feature", properties: {}, geometry: { type: "LineString", coordinates } });
  }
  if (mode === "area" && coordinates.length > 2) {
    features.unshift({ type: "Feature", properties: {}, geometry: { type: "Polygon", coordinates: [[...coordinates, coordinates[0]]] } });
  }
  return { type: "FeatureCollection", features };
};

export const updateMeasurementSource = (map: MapLibreMap, data: FeatureCollection) => {
  const source = map.getSource("kfm-measure") as GeoJSONSource | undefined;
  source?.setData(data);
};

const radians = (degrees: number) => degrees * (Math.PI / 180);

export const distanceMiles = (coordinates: [number, number][]) => {
  let miles = 0;
  for (let index = 1; index < coordinates.length; index += 1) {
    const [lng1, lat1] = coordinates[index - 1];
    const [lng2, lat2] = coordinates[index];
    const dLat = radians(lat2 - lat1);
    const dLng = radians(lng2 - lng1);
    const a = Math.sin(dLat / 2) ** 2 + Math.cos(radians(lat1)) * Math.cos(radians(lat2)) * Math.sin(dLng / 2) ** 2;
    miles += 3958.8 * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  }
  return miles;
};

export const areaSquareMiles = (coordinates: [number, number][]) => {
  if (coordinates.length < 3) return 0;
  const meanLat = coordinates.reduce((sum, coordinate) => sum + coordinate[1], 0) / coordinates.length;
  const points = coordinates.map(([lng, lat]) => [radians(lng) * Math.cos(radians(meanLat)) * 3958.8, radians(lat) * 3958.8]);
  let area = 0;
  for (let index = 0; index < points.length; index += 1) {
    const next = points[(index + 1) % points.length];
    area += points[index][0] * next[1] - next[0] * points[index][1];
  }
  return Math.abs(area) / 2;
};

export const geometryFromRendered = (geometry: Geometry): Feature<Geometry> => ({
  type: "Feature",
  properties: {},
  geometry: JSON.parse(JSON.stringify(geometry)) as Geometry,
});

export const boundsForCoordinates = (positions: Position[]): [number, number, number, number] => {
  const lngs = positions.map((position) => position[0]);
  const lats = positions.map((position) => position[1]);
  return [Math.min(...lngs), Math.min(...lats), Math.max(...lngs), Math.max(...lats)];
};
