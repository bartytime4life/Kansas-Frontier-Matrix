import type { Feature, FeatureCollection, Geometry, Position } from "geojson";
import type {
  FilterSpecification,
  GeoJSONSource,
  LayerSpecification,
  Map as MapLibreMap,
  StyleSpecification,
} from "maplibre-gl";
import { externalContextSource } from "./external-context-sources";
import { LAYER_REGISTRY, type EvidenceState } from "./explorer-data";
import { ACTIVE_TERRAIN_SOURCE } from "./terrain-sources";
import type { TemporalSweepQuery } from "./temporal-sweep";

export type BasemapKey = "standard" | "imagery" | "midnight" | "prairie" | "streets" | "topo";
export type AtmospherePreset = "night" | "dusk" | "clear";

const openFreeMapContext = externalContextSource("openfreemap-liberty");
const esriImageryContext = externalContextSource("esri-world-imagery");
const openStreetMapContext = externalContextSource("openstreetmap-standard");
const usgsTopoContext = externalContextSource("usgs-national-map-topo");

export const BASEMAPS: Record<BasemapKey, { title: string; note: string; style: StyleSpecification | string }> = {
  standard: {
    title: "Standard vector context",
    note: "OpenFreeMap · OpenMapTiles · OpenStreetMap · display context · not evidence",
    style: openFreeMapContext.requestUrl,
  },
  imagery: {
    title: "Satellite imagery",
    note: "Esri World Imagery · display context · not evidence",
    style: {
      version: 8,
      name: "KFM Satellite Imagery Context",
      sources: {
        "esri-imagery": {
          type: "raster",
          tiles: [esriImageryContext.requestUrl],
          tileSize: 256,
          attribution: esriImageryContext.attribution,
          bounds: [-104.8, 34.8, -92, 42.2],
          minzoom: 4,
          maxzoom: 19,
        },
      },
      layers: [{
        id: "esri-imagery-raster",
        type: "raster",
        source: "esri-imagery",
        paint: {
          "raster-opacity": 0.94,
          "raster-saturation": -0.08,
          "raster-contrast": 0.06,
          "raster-fade-duration": 180,
        },
      }],
    },
  },
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
  streets: {
    title: "OpenStreetMap context",
    note: "Attributed online context · not evidence",
    style: {
      version: 8,
      name: "KFM OpenStreetMap Context",
      sources: {
        "osm-context": {
          type: "raster",
          tiles: [openStreetMapContext.requestUrl],
          tileSize: 256,
          attribution: openStreetMapContext.attribution,
          bounds: [-104.8, 34.8, -92, 42.2],
          minzoom: 4,
          maxzoom: 19,
        },
      },
      layers: [{
        id: "osm-context-raster",
        type: "raster",
        source: "osm-context",
        paint: {
          "raster-opacity": 0.9,
          "raster-saturation": -0.12,
          "raster-contrast": 0.04,
          "raster-fade-duration": 180,
        },
      }],
    },
  },
  topo: {
    title: "USGS topographic map",
    note: "The National Map · display context · not evidence",
    style: {
      version: 8,
      name: "KFM USGS Topographic Context",
      sources: {
        "usgs-topo-context": {
          type: "raster",
          tiles: [usgsTopoContext.requestUrl],
          tileSize: 256,
          attribution: usgsTopoContext.attribution,
          bounds: [-104.8, 34.8, -92, 42.2],
          minzoom: 4,
          maxzoom: 16,
        },
      },
      layers: [{
        id: "usgs-topo-context-raster",
        type: "raster",
        source: "usgs-topo-context",
        paint: { "raster-opacity": 0.94, "raster-fade-duration": 120 },
      }],
    },
  },
};

const emptyCollection = (): FeatureCollection => ({ type: "FeatureCollection", features: [] });

const SYSTEM_LAYER_IDS = [
  "kfm-import-preview-fill",
  "kfm-import-preview-line",
  "kfm-import-preview-point",
  "kfm-analysis-area-fill",
  "kfm-analysis-area-line",
  "kfm-measure-fill",
  "kfm-measure-line",
  "kfm-measure-points",
  "kfm-selection-fill",
  "kfm-selection-line",
  "kfm-selection-point",
];

const addSystemLayers = (map: MapLibreMap) => {
  if (!map.getSource("kfm-import-preview")) {
    map.addSource("kfm-import-preview", { type: "geojson", data: emptyCollection() });
  }
  if (!map.getLayer("kfm-import-preview-fill")) {
    map.addLayer({ id: "kfm-import-preview-fill", type: "fill", source: "kfm-import-preview", filter: ["==", ["geometry-type"], "Polygon"], paint: { "fill-color": "#e58bf0", "fill-opacity": 0.16 } });
  }
  if (!map.getLayer("kfm-import-preview-line")) {
    map.addLayer({ id: "kfm-import-preview-line", type: "line", source: "kfm-import-preview", filter: ["in", ["geometry-type"], ["literal", ["LineString", "Polygon"]]], paint: { "line-color": "#f0a8f6", "line-width": 3, "line-dasharray": [1.5, 1] } });
  }
  if (!map.getLayer("kfm-import-preview-point")) {
    map.addLayer({ id: "kfm-import-preview-point", type: "circle", source: "kfm-import-preview", filter: ["==", ["geometry-type"], "Point"], paint: { "circle-color": "#f4dfae", "circle-radius": 6, "circle-stroke-color": "#e58bf0", "circle-stroke-width": 3 } });
  }

  if (!map.getSource("kfm-analysis-area")) {
    map.addSource("kfm-analysis-area", { type: "geojson", data: emptyCollection() });
  }
  if (!map.getLayer("kfm-analysis-area-fill")) {
    map.addLayer({ id: "kfm-analysis-area-fill", type: "fill", source: "kfm-analysis-area", paint: { "fill-color": "#69d4bb", "fill-opacity": 0.08 } });
  }
  if (!map.getLayer("kfm-analysis-area-line")) {
    map.addLayer({ id: "kfm-analysis-area-line", type: "line", source: "kfm-analysis-area", paint: { "line-color": "#9debd8", "line-width": 2.5, "line-dasharray": [2, 1.5] } });
  }

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

const temporalFilter = (
  year: number,
  mode: "exact" | "through",
  query?: TemporalSweepQuery,
): FilterSpecification => {
  const frame = query?.frame ?? year;
  if (query?.mode === "moving-window" && mode === "exact") {
    return ["all", [">=", ["get", "year"], query.windowStart], ["<=", ["get", "year"], frame]] as FilterSpecification;
  }
  if (query?.mode === "accumulation") {
    return ["all", [">=", ["get", "year"], query.rangeStart], ["<=", ["get", "year"], frame]] as FilterSpecification;
  }
  return mode === "exact"
    ? (["==", ["get", "year"], frame] as FilterSpecification)
    : (["<=", ["get", "year"], frame] as FilterSpecification);
};

const mergeFilters = (...filters: Array<FilterSpecification | undefined>): FilterSpecification | undefined => {
  const activeFilters = filters.filter((filter): filter is FilterSpecification => Boolean(filter));
  if (activeFilters.length > 1) return ["all", ...activeFilters] as FilterSpecification;
  return activeFilters[0];
};

export type RegistryEvidenceFilter = EvidenceState | "ALL";

export const TERRAIN_SOURCE_ID = "kfm-terrain-dem";
export const TERRAIN_HILLSHADE_LAYER_ID = "kfm-terrain-hillshade";
export const TERRAIN_COLOR_SOURCE_ID = "kfm-terrain-color-dem";
export const TERRAIN_COLOR_RELIEF_LAYER_ID = "kfm-terrain-color-relief";
export type TerrainPresentationState = "OFF" | "LOADING" | "READY" | "ERROR";
export const LIBERTY_STRUCTURES_3D_LAYER_ID = "building-3d";
export type Structures3DState = "OFF" | "READY" | "UNAVAILABLE" | "ERROR";

/**
 * Real elevation presentation is opt-in and remains a display carrier. The
 * active terrain carrier is not a KFM release and never changes evidence,
 * feature identity, or reported numeric source values.
 */
export const setTerrainPresentation = (
  map: MapLibreMap,
  enabled: boolean,
  exaggeration: number,
): TerrainPresentationState => {
  if (!enabled) {
    if (map.getLayer(TERRAIN_HILLSHADE_LAYER_ID)) {
      map.setLayoutProperty(TERRAIN_HILLSHADE_LAYER_ID, "visibility", "none");
    }
    map.setTerrain(null);
    return "OFF";
  }

  try {
    if (!map.getSource(TERRAIN_SOURCE_ID)) {
      map.addSource(TERRAIN_SOURCE_ID, {
        type: "raster-dem",
        tiles: [ACTIVE_TERRAIN_SOURCE.tileTemplate!],
        tileSize: ACTIVE_TERRAIN_SOURCE.tileSize!,
        maxzoom: ACTIVE_TERRAIN_SOURCE.maxZoom!,
        encoding: ACTIVE_TERRAIN_SOURCE.encoding,
        attribution: ACTIVE_TERRAIN_SOURCE.attribution,
      });
    }
    if (!map.getLayer(TERRAIN_HILLSHADE_LAYER_ID)) {
      map.addLayer({
        id: TERRAIN_HILLSHADE_LAYER_ID,
        type: "hillshade",
        source: TERRAIN_SOURCE_ID,
        layout: { visibility: "visible" },
        paint: {
          "hillshade-shadow-color": "#163337",
          "hillshade-highlight-color": "#d9d5bd",
          "hillshade-accent-color": "#6d8175",
          "hillshade-illumination-direction": 235,
        },
      });
    } else {
      map.setLayoutProperty(TERRAIN_HILLSHADE_LAYER_ID, "visibility", "visible");
    }
    const safeExaggeration = Math.max(0.1, Math.min(3, Number.isFinite(exaggeration) ? exaggeration : 1));
    map.setTerrain({ source: TERRAIN_SOURCE_ID, exaggeration: safeExaggeration });
    return "LOADING";
  } catch {
    return "ERROR";
  }
};

/** Adds a quantitative color ramp over the active terrain using unexaggerated
 * DEM elevations. The ramp is a visual reading aid, not analytical evidence. */
export const setTerrainHeightOverlay = (map: MapLibreMap, enabled: boolean): boolean => {
  try {
    if (!enabled) {
      if (map.getLayer(TERRAIN_COLOR_RELIEF_LAYER_ID)) {
        map.setLayoutProperty(TERRAIN_COLOR_RELIEF_LAYER_ID, "visibility", "none");
      }
      return false;
    }
    if (!map.getSource(TERRAIN_COLOR_SOURCE_ID)) {
      map.addSource(TERRAIN_COLOR_SOURCE_ID, {
        type: "raster-dem",
        tiles: [ACTIVE_TERRAIN_SOURCE.tileTemplate!],
        tileSize: ACTIVE_TERRAIN_SOURCE.tileSize!,
        maxzoom: ACTIVE_TERRAIN_SOURCE.maxZoom!,
        encoding: ACTIVE_TERRAIN_SOURCE.encoding,
        attribution: ACTIVE_TERRAIN_SOURCE.attribution,
      });
    }
    if (!map.getLayer(TERRAIN_COLOR_RELIEF_LAYER_ID)) {
      const firstSymbolLayerId = map.getStyle().layers?.find((layer) => layer.type === "symbol")?.id;
      map.addLayer({
        id: TERRAIN_COLOR_RELIEF_LAYER_ID,
        type: "color-relief",
        source: TERRAIN_COLOR_SOURCE_ID,
        layout: { visibility: "visible" },
        paint: {
          "color-relief-opacity": 0.58,
          "color-relief-color": [
            "interpolate", ["linear"], ["elevation"],
            200, "#163d59",
            300, "#1f6f78",
            400, "#5a916a",
            500, "#a5a95d",
            650, "#d0a957",
            800, "#c87945",
            1000, "#9e5145",
            1250, "#f1e5cf",
          ],
        },
      }, firstSymbolLayerId);
    } else {
      map.setLayoutProperty(TERRAIN_COLOR_RELIEF_LAYER_ID, "visibility", "visible");
    }
    return true;
  } catch {
    return false;
  }
};

/**
 * Controls the height-backed building extrusion already carried by OpenFreeMap
 * Liberty. That style reads render_height/render_min_height directly, so the
 * Site neither duplicates the layer nor invents a client-side height.
 */
export const setStructureExtrusions = (
  map: MapLibreMap,
  enabled: boolean,
): Structures3DState => {
  try {
    const layer = map.getLayer(LIBERTY_STRUCTURES_3D_LAYER_ID);
    if (!map.getSource("openmaptiles") || layer?.type !== "fill-extrusion") return enabled ? "UNAVAILABLE" : "OFF";
    map.setLayoutProperty(LIBERTY_STRUCTURES_3D_LAYER_ID, "visibility", enabled ? "visible" : "none");
    return enabled ? "READY" : "OFF";
  } catch {
    return "ERROR";
  }
};

const evidenceFilterForRecord = (record: (typeof LAYER_REGISTRY)[number], evidenceFilter: RegistryEvidenceFilter): FilterSpecification | undefined => {
  if (evidenceFilter === "ALL") return undefined;
  if (!record.sourceOptions?.cluster) return ["==", ["get", "evidenceState"], evidenceFilter] as FilterSpecification;
  const clusteredRecordMatches = record.data.features.some((feature) => feature.properties.evidenceState === evidenceFilter);
  return clusteredRecordMatches ? undefined : ["==", ["get", "fid"], "__no_matching_feature__"] as FilterSpecification;
};

/** Update only renderer filters during time playback. Sources, paint, zoom
 * ranges, and draw order remain untouched so large registries do not churn on
 * every frame. */
export const applyTemporalRegistryFilters = (
  map: MapLibreMap,
  year: number,
  evidenceFilter: RegistryEvidenceFilter = "ALL",
  temporalQuery?: TemporalSweepQuery,
) => {
  for (const record of LAYER_REGISTRY) {
    for (const renderer of record.renderers) {
      if (!map.getLayer(renderer.id)) continue;
      const filter = mergeFilters(
        renderer.baseFilter,
        record.temporal ? temporalFilter(year, record.temporal.mode, temporalQuery) : undefined,
        evidenceFilterForRecord(record, evidenceFilter),
      );
      map.setFilter(renderer.id, filter ?? null);
    }
  }
};

export const applyRegistryState = (
  map: MapLibreMap,
  visibility: Record<string, boolean>,
  opacity: Record<string, number>,
  year: number,
  order: string[],
  evidenceFilter: RegistryEvidenceFilter = "ALL",
  temporalQuery?: TemporalSweepQuery,
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
        record.temporal ? temporalFilter(year, record.temporal.mode, temporalQuery) : undefined,
        evidenceFilterForRecord(record, evidenceFilter),
      );
      map.setFilter(renderer.id, filter ?? null);

      for (const property of renderer.opacityProperties ?? []) {
        map.setPaintProperty(renderer.id, property, opacity[record.id] ?? record.defaultOpacity);
      }
    }
  }

  addSystemLayers(map);
  reorderRegistryLayers(map, order);
};

export const setElevationExaggeration = (map: MapLibreMap, scale: number) => {
  if (!map.getLayer("elevation-concept-extrusion")) return;
  const safeScale = Math.max(0, Math.min(2, Number.isFinite(scale) ? scale : 1));
  map.setPaintProperty(
    "elevation-concept-extrusion",
    "fill-extrusion-height",
    ["*", ["get", "relativeHeightM"], safeScale],
  );
};

const setPaintIfPresent = (
  map: MapLibreMap,
  layerId: string,
  property: Parameters<MapLibreMap["setPaintProperty"]>[1],
  value: Parameters<MapLibreMap["setPaintProperty"]>[2],
) => {
  if (map.getLayer(layerId)) map.setPaintProperty(layerId, property, value);
};

/**
 * Decorative, reversible MapLibre effects. These values change presentation only:
 * feature geometry, evidence state, time, source data, and report semantics remain fixed.
 */
export const applyDynamicMapEffects = (
  map: MapLibreMap,
  elapsedMs: number,
  opacity: Record<string, number>,
  active: boolean,
) => {
  const phase = active ? elapsedMs / 1000 : 0;
  const wave = active ? (Math.sin(phase * 2.1) + 1) / 2 : 0.5;
  const slowWave = active ? (Math.sin(phase * 0.82) + 1) / 2 : 0.5;
  const travelStep = active ? Math.floor(phase * 5) % 4 : 0;
  const waterWidth = active ? 1.8 + wave * 1.05 : 2.2;
  const fireWidth = active ? 1.25 + wave * 1.15 : 1.6;
  const roadWidth = active ? 2 + wave * 0.55 : 2.2;
  const metroRadius = active ? 6.6 + wave * 1.2 : 7;
  const regionalRadius = active ? 5.1 + wave * 0.7 : 5.5;
  const localRadius = active ? 4.2 + wave * 0.5 : 4.5;

  setPaintIfPresent(map, "water-context-flow", "line-opacity", (opacity["water-context"] ?? 0.9) * (active ? 0.68 + wave * 0.3 : 1));
  setPaintIfPresent(map, "water-context-flow", "line-width", waterWidth);
  setPaintIfPresent(map, "smoke-context-fill", "fill-opacity", (opacity["smoke-context"] ?? 0.28) * (active ? 0.72 + slowWave * 0.28 : 1));
  setPaintIfPresent(map, "smoke-context-outline", "line-dasharray", travelStep % 2 === 0 ? [2, 2] : [1.5, 2.5]);
  setPaintIfPresent(map, "fire-context-fill", "fill-opacity", (opacity["fire-context"] ?? 0.24) * (active ? 0.68 + wave * 0.32 : 1));
  setPaintIfPresent(map, "fire-context-outline", "line-width", ["case", ["boolean", ["feature-state", "hover"], false], fireWidth + 2, fireWidth]);
  setPaintIfPresent(map, "hazards-context-fill", "fill-opacity", (opacity["hazards-context"] ?? 0.12) * (active ? 0.72 + slowWave * 0.28 : 1));
  setPaintIfPresent(map, "habitat-connectivity-fill", "fill-opacity", (opacity["habitat-connectivity"] ?? 0.22) * (active ? 0.84 + slowWave * 0.16 : 1));
  setPaintIfPresent(map, "transport-context-road", "line-width", ["case", ["boolean", ["feature-state", "hover"], false], roadWidth + 2, roadWidth]);
  setPaintIfPresent(map, "transport-context-rail", "line-dasharray", active ? [3 + travelStep, 2, 1, 2] : [4, 2]);
  setPaintIfPresent(map, "communities-points", "circle-radius", [
    "+",
    ["match", ["get", "settlementClass"], "METRO", metroRadius, "REGIONAL", regionalRadius, "LOCAL", localRadius, 5],
    ["case", ["boolean", ["feature-state", "hover"], false], 3, 0],
  ]);
};

const SCENE_SKIES = Object.freeze({
  night: Object.freeze({
    "sky-color": "#07171a",
    "horizon-color": "#173438",
    "fog-color": "#0d2427",
    "fog-ground-blend": 0.35,
    "horizon-fog-blend": 0.7,
    "sky-horizon-blend": 0.82,
    "atmosphere-blend": 0.68,
  }),
  dusk: Object.freeze({
    "sky-color": "#263744",
    "horizon-color": "#d49c78",
    "fog-color": "#5f6867",
    "fog-ground-blend": 0.28,
    "horizon-fog-blend": 0.62,
    "sky-horizon-blend": 0.9,
    "atmosphere-blend": 0.82,
  }),
  clear: Object.freeze({
    "sky-color": "#6d9dac",
    "horizon-color": "#d4e5df",
    "fog-color": "#afc9c3",
    "fog-ground-blend": 0.22,
    "horizon-fog-blend": 0.48,
    "sky-horizon-blend": 0.78,
    "atmosphere-blend": 0.88,
  }),
}) satisfies Record<AtmospherePreset, Parameters<MapLibreMap["setSky"]>[0]>;

export const applySceneEnvironment = (map: MapLibreMap, preset: AtmospherePreset, lightAzimuth: number) => {
  const safeAzimuth = ((Number.isFinite(lightAzimuth) ? lightAzimuth : 210) % 360 + 360) % 360;
  map.setSky(SCENE_SKIES[preset]);
  map.setLight({
    anchor: "map",
    position: [1.45, safeAzimuth, preset === "night" ? 50 : 38],
    color: preset === "night" ? "#b9d5d8" : preset === "dusk" ? "#ffd2a2" : "#fff8df",
    intensity: preset === "night" ? 0.42 : preset === "dusk" ? 0.68 : 0.58,
  });
};

export type TileCoordinate = Readonly<{ z: number; x: number; y: number; label: string }>;

export const lngLatToTile = (longitude: number, latitude: number, zoom: number): TileCoordinate => {
  const z = Math.max(0, Math.min(22, Math.floor(Number.isFinite(zoom) ? zoom : 0)));
  const lng = Math.max(-180, Math.min(180, Number.isFinite(longitude) ? longitude : 0));
  const lat = Math.max(-85.051129, Math.min(85.051129, Number.isFinite(latitude) ? latitude : 0));
  const tileCount = 2 ** z;
  const x = Math.max(0, Math.min(tileCount - 1, Math.floor(((lng + 180) / 360) * tileCount)));
  const latitudeRadians = radians(lat);
  const y = Math.max(0, Math.min(tileCount - 1, Math.floor(
    ((1 - Math.log(Math.tan(latitudeRadians) + (1 / Math.cos(latitudeRadians))) / Math.PI) / 2) * tileCount,
  )));
  return Object.freeze({ z, x, y, label: `${z}/${x}/${y}` });
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

export const buildMeasurementData = (coordinates: [number, number][], mode: "point" | "distance" | "area" | null): FeatureCollection => {
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

export type AnalysisAreaBounds = Readonly<{ west: number; south: number; east: number; north: number }>;

export const buildAnalysisAreaData = (bounds?: AnalysisAreaBounds | null): FeatureCollection => {
  if (!bounds) return emptyCollection();
  return {
    type: "FeatureCollection",
    features: [{
      type: "Feature",
      id: "analysis-area",
      properties: { role: "site-local-analysis-area" },
      geometry: {
        type: "Polygon",
        coordinates: [[
          [bounds.west, bounds.south],
          [bounds.east, bounds.south],
          [bounds.east, bounds.north],
          [bounds.west, bounds.north],
          [bounds.west, bounds.south],
        ]],
      },
    }],
  };
};

export const updateAnalysisAreaSource = (map: MapLibreMap, bounds?: AnalysisAreaBounds | null) => {
  const source = map.getSource("kfm-analysis-area") as GeoJSONSource | undefined;
  source?.setData(buildAnalysisAreaData(bounds));
};

export const updateImportPreviewSource = (map: MapLibreMap, data?: FeatureCollection | null) => {
  const source = map.getSource("kfm-import-preview") as GeoJSONSource | undefined;
  source?.setData(data ?? emptyCollection());
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
