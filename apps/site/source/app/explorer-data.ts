import type { FeatureCollection, Geometry } from "geojson";
import type { FilterSpecification, LayerSpecification } from "./maplibre-seam";
import { BUILD_UTC_YEAR } from "./build-clock";

export type EvidenceState =
  | "ANSWER"
  | "MISSING_EVIDENCE"
  | "SOURCE_STALE"
  | "GENERALIZED_GEOMETRY"
  | "RESTRICTED_ACCESS"
  | "DENIED_BY_POLICY"
  | "CORRECTED"
  | "SUPERSEDED"
  | "ERROR";

export type ReleaseState = "RELEASED" | "DEMONSTRATION" | "GENERALIZED" | "RESTRICTED";
export type LayerCategory =
  | "Reference boundaries & locators"
  | "Hydrology & water"
  | "Geology & landforms"
  | "Habitat, fauna & flora"
  | "Agriculture"
  | "Weather & hazards"
  | "Fire, smoke & hazards"
  | "People & DNA"
  | "Roads, rail & movement"
  | "Settlements & cities"
  | "Historical geography"
  | "Public-safe planning"
  | "Review & diagnostics";

export type TemporalDefinition = {
  field: "year";
  mode: "exact" | "through";
  years: number[];
  label: string;
};

export type RendererDefinition = {
  id: string;
  spec: LayerSpecification;
  interactive?: boolean;
  opacityProperties?: ("fill-opacity" | "line-opacity" | "circle-opacity" | "text-opacity" | "fill-extrusion-opacity")[];
  baseFilter?: FilterSpecification;
};

export type LayerRecord = {
  id: string;
  title: string;
  description: string;
  domain: string;
  category: LayerCategory;
  sourceType: "GeoJSON" | "Vector tiles" | "Raster" | "Raster DEM";
  sourceId: string;
  datasetName: string;
  geometryType: "Point" | "LineString" | "Polygon" | "Mixed";
  minZoom: number;
  maxZoom: number;
  defaultVisibility: boolean;
  defaultOpacity: number;
  legend: { label: string; color: string; shape: "line" | "fill" | "point" }[];
  units: string;
  scaleNote: string;
  validTimeExtent: string;
  sourceTime: string;
  releaseTime: string;
  freshnessState: "CURRENT" | "STALE" | "MIXED" | "NOT_APPLICABLE";
  attribution: string;
  evidenceReference: string;
  publicStatus: "PUBLIC_SAFE" | "GENERALIZED" | "RESTRICTED";
  sensitivityNote: string;
  releaseState: ReleaseState;
  correctionNote: string;
  relatedLayers: string[];
  interactions: string[];
  filters: string[];
  viewingModes: string[];
  bounds: [number, number, number, number];
  temporal?: TemporalDefinition;
  sourceOptions?: { cluster?: boolean; clusterRadius?: number; clusterMaxZoom?: number; lineMetrics?: boolean };
  data: FeatureCollection<Geometry, FeatureProperties>;
  renderers: RendererDefinition[];
};

export type FeatureProperties = {
  fid: string;
  title: string;
  summary: string;
  sourceRole: string;
  sourceOrganization: string;
  citation: string;
  spatialScope: string;
  temporalScope: string;
  lastUpdate: string;
  freshnessState: string;
  evidenceState: EvidenceState;
  reviewState: string;
  releaseState: ReleaseState;
  rights: string;
  generalizationNote: string;
  uncertainty: string;
  correctionState: string;
  relatedLayers: string;
  year: number;
  focusLng: number;
  focusLat: number;
  displayElevationFt?: number;
  relativeHeightM?: number;
  smokeDensity?: "LOW" | "MODERATE" | "HIGH";
  watershedClass?: string;
  tileLabel?: string;
  displayLabel?: string;
  settlementClass?: "METRO" | "REGIONAL" | "LOCAL";
  transportMode?: "ROAD" | "RAIL";
  habitatClass?: "CORE" | "CORRIDOR" | "RESTORATION";
  faunaClass?: "GRASSLAND" | "WETLAND" | "MIGRATION";
  floraClass?: "SHORTGRASS" | "MIXED_GRASS" | "TALLGRASS";
  fireClass?: "WATCH" | "RECOVERY" | "TRAINING";
  hazardClass?: "FLOOD" | "WIND" | "DROUGHT";
  consentPosture?: "AGGREGATE_ONLY" | "CONSENT_REQUIRED" | "DENIED";
};

// The site has no released, source-backed domain GeoJSON layers. Provider-backed
// map context is registered separately in live-context.ts and related adapters.
// Keep this registry empty until a governed, public-safe layer is admitted.
export const LAYER_REGISTRY: LayerRecord[] = [];
export const CATEGORY_ORDER: LayerCategory[] = [];

export const TIME_STEPS = [
  -4_540_000_000,
  -2_500_000_000,
  -541_000_000,
  -299_000_000,
  -66_000_000,
  -2_580_000,
  -11_700,
  -8_000,
  -3_000,
  1,
  1000,
  1541,
  // Annual selection is a time capacity, not a claim of data in every year.
  ...Array.from({ length: BUILD_UTC_YEAR - 1800 + 1 }, (_, index) => 1800 + index),
] as const;

export type SearchItem = {
  id: string;
  kind: "layer" | "feature";
  title: string;
  subtitle: string;
  layerId: string;
  featureId?: string;
  focus?: [number, number];
};

export const SEARCH_INDEX: SearchItem[] = LAYER_REGISTRY.flatMap((layer) => [
  { id: `layer:${layer.id}`, kind: "layer" as const, title: layer.title, subtitle: `${layer.category} · ${layer.datasetName}`, layerId: layer.id },
  ...layer.data.features.map((item) => ({
    id: `feature:${item.properties.fid}`,
    kind: "feature" as const,
    title: item.properties.title,
    subtitle: `${layer.title} · ${item.properties.fid}`,
    layerId: layer.id,
    featureId: item.properties.fid,
    focus: [item.properties.focusLng, item.properties.focusLat] as [number, number],
  })),
]);

export const findFeature = (featureId: string) => {
  for (const layer of LAYER_REGISTRY) {
    const found = layer.data.features.find((item) => item.properties.fid === featureId);
    if (found) return { layer, feature: found };
  }
  return null;
};

export const findLayerByRenderer = (rendererId: string) =>
  LAYER_REGISTRY.find((layer) => layer.renderers.some((renderer) => renderer.id === rendererId));
