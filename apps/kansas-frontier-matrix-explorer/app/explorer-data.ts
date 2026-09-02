import type { FeatureCollection, Geometry } from "geojson";

export type RendererFilterDescriptor = readonly unknown[];
export type RendererLayerDescriptor = Readonly<Record<string, unknown> & {
  id: string;
  type: string;
  source?: string;
  filter?: RendererFilterDescriptor;
}>;

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
  | "Boundaries & places"
  | "Hydrology & water"
  | "Geology & landforms"
  | "Land cover & ecology"
  | "Agriculture"
  | "Weather & hazards"
  | "Roads, rail & movement"
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
  spec: RendererLayerDescriptor;
  interactive?: boolean;
  opacityProperties?: ("fill-opacity" | "line-opacity" | "circle-opacity" | "text-opacity" | "fill-extrusion-opacity")[];
  baseFilter?: RendererFilterDescriptor;
};

export type LayerRecord = {
  id: string;
  title: string;
  description: string;
  domain: string;
  category: LayerCategory;
  sourceType: "GeoJSON";
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
};

const feature = (
  id: string,
  geometry: Geometry,
  properties: Omit<FeatureProperties, "fid">,
) => ({ type: "Feature" as const, id, geometry, properties: { ...properties, fid: id } });

const baseProps = {
  sourceRole: "synthetic",
  sourceOrganization: "Kansas Frontier Matrix site-local demonstration",
  citation: "kfm:demo:site-local:v1",
  freshnessState: "NOT_APPLICABLE",
  reviewState: "DEMONSTRATION",
  releaseState: "DEMONSTRATION" as const,
  rights: "Public-safe site demonstration; not a released KFM dataset.",
  generalizationNote: "Geometry is simplified and must not be used for boundary, parcel, engineering, or navigation decisions.",
  uncertainty: "Illustrative placement and simplified geometry.",
  correctionState: "NONE",
  relatedLayers: "",
  year: 2026,
};

const kansasBoundary: FeatureCollection<Geometry, FeatureProperties> = {
  type: "FeatureCollection",
  features: [
    feature(
      "ks-demo-boundary",
      {
        type: "Polygon",
        coordinates: [[
          [-102.05, 40.0], [-95.31, 40.0], [-95.12, 39.78], [-94.95, 39.56],
          [-95.03, 39.32], [-94.62, 39.12], [-94.62, 37.0], [-102.05, 37.0],
          [-102.05, 40.0],
        ]],
      },
      {
        ...baseProps,
        title: "Kansas demonstration extent",
        summary: "A simplified statewide operating extent used to frame the Explorer.",
        sourceRole: "aggregate",
        spatialScope: "Kansas, generalized statewide outline",
        temporalScope: "Not time-varying",
        lastUpdate: "2026-08-20",
        evidenceState: "GENERALIZED_GEOMETRY",
        releaseState: "GENERALIZED",
        generalizationNote: "This deliberately simplified outline is not an authoritative state boundary.",
        focusLng: -98.4,
        focusLat: 38.5,
      },
    ),
  ],
};

const waterDemo: FeatureCollection<Geometry, FeatureProperties> = {
  type: "FeatureCollection",
  features: [
    feature("water-smoky-hill", { type: "LineString", coordinates: [[-101.65, 38.71], [-100.62, 38.86], [-99.33, 38.87], [-98.23, 38.73], [-97.62, 38.82], [-96.83, 39.03]] }, {
      ...baseProps,
      title: "Smoky Hill hydrology context",
      summary: "A simplified demonstration line used to exercise the feature-to-evidence bridge.",
      sourceRole: "synthetic",
      spatialScope: "Smoky Hills corridor, generalized",
      temporalScope: "Valid for the 2026 demonstration snapshot",
      lastUpdate: "2026-08-20",
      evidenceState: "ANSWER",
      citation: "kfm:evidence:synthetic:flow-001",
      relatedLayers: "Kansas demonstration extent; Communities",
      focusLng: -98.23,
      focusLat: 38.73,
    }),
    feature("water-kansas-river", { type: "LineString", coordinates: [[-96.83, 39.03], [-96.31, 39.06], [-95.68, 39.03], [-95.23, 39.08], [-94.62, 39.11]] }, {
      ...baseProps,
      title: "Kansas River demonstration context",
      summary: "Generalized river geometry with no resolved claim evidence attached in this site.",
      sourceRole: "synthetic",
      spatialScope: "Northeast Kansas corridor, generalized",
      temporalScope: "Valid for the 2026 demonstration snapshot",
      lastUpdate: "2026-08-20",
      evidenceState: "MISSING_EVIDENCE",
      citation: "No released evidence reference available",
      relatedLayers: "Communities",
      focusLng: -95.55,
      focusLat: 39.06,
    }),
    feature("water-arkansas", { type: "LineString", coordinates: [[-102.05, 37.64], [-100.02, 37.75], [-98.86, 38.05], [-97.93, 38.06], [-97.34, 37.69], [-96.53, 37.06]] }, {
      ...baseProps,
      title: "Arkansas River demonstration context",
      summary: "A generalized line retained to demonstrate explicit stale-source handling.",
      sourceRole: "synthetic",
      spatialScope: "South-central Kansas corridor, generalized",
      temporalScope: "Source time 2022; viewed in the 2026 demonstration",
      lastUpdate: "2022-06-01",
      freshnessState: "STALE",
      evidenceState: "SOURCE_STALE",
      citation: "kfm:evidence:synthetic:stale-001",
      relatedLayers: "Atmosphere observations",
      year: 2022,
      focusLng: -97.93,
      focusLat: 38.06,
    }),
    feature("water-cimarron-context", { type: "LineString", coordinates: [[-101.95, 37.12], [-100.72, 37.05], [-99.55, 37.2], [-98.47, 37.13], [-97.26, 37.05]] }, {
      ...baseProps,
      title: "Cimarron basin demonstration context",
      summary: "A simplified southern-basin line for multi-layer report and regional-scope testing.",
      sourceRole: "synthetic",
      spatialScope: "Southern Kansas corridor, generalized",
      temporalScope: "Valid for the 2026 demonstration snapshot",
      lastUpdate: "2026-08-29",
      evidenceState: "GENERALIZED_GEOMETRY",
      citation: "kfm:evidence:synthetic:cimarron-context-v1",
      generalizationNote: "Illustrative corridor only; no flow, allocation, monitoring, or legal-water claim.",
      relatedLayers: "Agricultural context; Communities",
      focusLng: -99.55,
      focusLat: 37.16,
    }),
  ],
};

const prairieDemo: FeatureCollection<Geometry, FeatureProperties> = {
  type: "FeatureCollection",
  features: [
    feature("prairie-high-plains", { type: "Polygon", coordinates: [[[-102.03, 39.96], [-100.55, 39.96], [-100.55, 37.04], [-102.03, 37.04], [-102.03, 39.96]]] }, {
      ...baseProps,
      title: "High Plains demonstration region",
      summary: "A coarse ecological context polygon used for layer comparison and transparency testing.",
      sourceRole: "modeled",
      spatialScope: "Western Kansas, generalized regional envelope",
      temporalScope: "Illustrative 2026 snapshot",
      lastUpdate: "2026-08-20",
      evidenceState: "GENERALIZED_GEOMETRY",
      focusLng: -101.25,
      focusLat: 38.5,
    }),
    feature("prairie-flint-hills", { type: "Polygon", coordinates: [[[-97.15, 39.65], [-96.05, 39.55], [-96.2, 37.05], [-97.15, 37.05], [-97.15, 39.65]]] }, {
      ...baseProps,
      title: "Flint Hills demonstration region",
      summary: "A generalized ecological corridor. Rendered geometry is context, not habitat evidence.",
      sourceRole: "modeled",
      spatialScope: "East-central Kansas, generalized",
      temporalScope: "Illustrative 2026 snapshot",
      lastUpdate: "2026-08-20",
      evidenceState: "MISSING_EVIDENCE",
      citation: "No claim-bearing EvidenceBundle attached",
      relatedLayers: "Geology & landforms",
      focusLng: -96.6,
      focusLat: 38.45,
    }),
  ],
};

const geologyDemo: FeatureCollection<Geometry, FeatureProperties> = {
  type: "FeatureCollection",
  features: [
    feature("geology-smoky-hills", { type: "Polygon", coordinates: [[[-100.55, 39.65], [-97.35, 39.65], [-97.15, 38.0], [-100.4, 38.0], [-100.55, 39.65]]] }, {
      ...baseProps,
      title: "Smoky Hills landform context",
      summary: "Illustrative landform extent with an intentionally stale metadata state.",
      sourceRole: "historical",
      spatialScope: "Central Kansas, generalized",
      temporalScope: "Demonstration source vintage 2019",
      lastUpdate: "2019-01-01",
      freshnessState: "STALE",
      evidenceState: "SOURCE_STALE",
      citation: "kfm:evidence:synthetic:geology-stale",
      year: 2019,
      focusLng: -98.8,
      focusLat: 38.8,
    }),
  ],
};

const agricultureDemo: FeatureCollection<Geometry, FeatureProperties> = {
  type: "FeatureCollection",
  features: [
    feature("ag-generalized-west", { type: "Polygon", coordinates: [[[-101.8, 39.35], [-99.75, 39.35], [-99.75, 37.35], [-101.8, 37.35], [-101.8, 39.35]]] }, {
      ...baseProps,
      title: "Generalized agricultural context",
      summary: "A coarse regional fixture that intentionally carries no farm-, parcel-, or production-level claim.",
      sourceRole: "aggregate",
      spatialScope: "Western Kansas regional envelope",
      temporalScope: "Demonstration snapshot only",
      lastUpdate: "2026-08-20",
      evidenceState: "MISSING_EVIDENCE",
      citation: "No claim-bearing evidence attached",
      generalizationNote: "No parcel, owner, operator, yield, or private-land attribute is present.",
      focusLng: -100.8,
      focusLat: 38.35,
    }),
    feature("ag-generalized-central", { type: "Polygon", coordinates: [[[-99.72, 39.35], [-97.35, 39.35], [-97.35, 37.45], [-99.72, 37.45], [-99.72, 39.35]]] }, {
      ...baseProps,
      title: "Central agriculture demonstration region",
      summary: "A coarse regional fixture for comparing agriculture, water, transport, and community context without farm-level claims.",
      sourceRole: "aggregate",
      spatialScope: "Central Kansas regional envelope",
      temporalScope: "Demonstration snapshot only",
      lastUpdate: "2026-08-29",
      evidenceState: "CORRECTED",
      citation: "kfm:evidence:synthetic:ag-central-r2",
      correctionState: "CORRECTED · eastern edge generalized in revision 2",
      generalizationNote: "No parcel, owner, operator, crop, yield, livestock, or production attribute is present.",
      relatedLayers: "Hydrology context; Communities; Roads, rail & movement",
      focusLng: -98.55,
      focusLat: 38.4,
    }),
    feature("ag-generalized-east", { type: "Polygon", coordinates: [[[-97.32, 39.45], [-95.15, 39.45], [-95.15, 37.25], [-97.32, 37.25], [-97.32, 39.45]]] }, {
      ...baseProps,
      title: "Eastern agriculture demonstration region",
      summary: "A generalized regional fixture designed for habitat and community-context report recipes.",
      sourceRole: "aggregate",
      spatialScope: "Eastern Kansas regional envelope",
      temporalScope: "Demonstration snapshot only",
      lastUpdate: "2026-08-29",
      evidenceState: "GENERALIZED_GEOMETRY",
      citation: "kfm:evidence:synthetic:ag-east-context-v1",
      generalizationNote: "Regional context only; no field, ownership, operation, production, or private-land detail.",
      relatedLayers: "Prairie & ecological regions; Communities",
      focusLng: -96.25,
      focusLat: 38.35,
    }),
  ],
};

const atmosphereDemo: FeatureCollection<Geometry, FeatureProperties> = {
  type: "FeatureCollection",
  features: [
    feature("atmo-goodland-2022", { type: "Point", coordinates: [-101.71, 39.35] }, {
      ...baseProps,
      title: "Goodland 2022 source-time fixture",
      summary: "A stale synthetic observation used to test exact-year temporal filtering.",
      sourceRole: "observed",
      spatialScope: "Generalized place point",
      temporalScope: "Observation year 2022",
      lastUpdate: "2022-08-01",
      freshnessState: "STALE",
      evidenceState: "SOURCE_STALE",
      citation: "kfm:evidence:synthetic:atmo-2022",
      year: 2022,
      focusLng: -101.71,
      focusLat: 39.35,
    }),
    feature("atmo-hays-2024", { type: "Point", coordinates: [-99.33, 38.88] }, {
      ...baseProps,
      title: "Hays 2024 corrected fixture",
      summary: "A synthetic observation whose earlier value is visibly marked corrected.",
      sourceRole: "observed",
      spatialScope: "Generalized place point",
      temporalScope: "Observation year 2024",
      lastUpdate: "2025-01-12",
      evidenceState: "CORRECTED",
      citation: "kfm:evidence:synthetic:atmo-2024-r2",
      correctionState: "CORRECTED · supersedes revision 1",
      year: 2024,
      focusLng: -99.33,
      focusLat: 38.88,
    }),
    feature("atmo-topeka-2026", { type: "Point", coordinates: [-95.68, 39.05] }, {
      ...baseProps,
      title: "Topeka 2026 supported fixture",
      summary: "A synthetic current-year observation with a matching demonstration evidence reference.",
      sourceRole: "observed",
      spatialScope: "Generalized place point",
      temporalScope: "Observation year 2026",
      lastUpdate: "2026-08-20",
      freshnessState: "CURRENT",
      evidenceState: "ANSWER",
      citation: "kfm:evidence:synthetic:atmo-2026",
      year: 2026,
      focusLng: -95.68,
      focusLat: 39.05,
    }),
  ],
};

const communitiesDemo: FeatureCollection<Geometry, FeatureProperties> = {
  type: "FeatureCollection",
  features: [
    ["place-goodland", "Goodland", -101.71, 39.35], ["place-hays", "Hays", -99.33, 38.88],
    ["place-ellsworth", "Ellsworth", -98.23, 38.73], ["place-wichita", "Wichita", -97.34, 37.69],
    ["place-manhattan", "Manhattan", -96.58, 39.18], ["place-topeka", "Topeka", -95.68, 39.05],
    ["place-kansas-city", "Kansas City", -94.63, 39.11], ["place-garden-city", "Garden City", -100.87, 37.97],
    ["place-dodge-city", "Dodge City", -100.02, 37.75], ["place-salina", "Salina", -97.61, 38.84],
    ["place-emporia", "Emporia", -96.18, 38.4], ["place-pittsburg", "Pittsburg", -94.7, 37.41],
  ].map(([id, name, lng, lat]) => feature(String(id), { type: "Point", coordinates: [Number(lng), Number(lat)] }, {
    ...baseProps,
    title: `${name} place context`,
    summary: "A public place-name fixture for search, clustering, and map navigation.",
    sourceRole: "aggregate",
    spatialScope: `${name}, Kansas; generalized point`,
    temporalScope: "Current demonstration context",
    lastUpdate: "2026-08-20",
    evidenceState: "GENERALIZED_GEOMETRY",
    focusLng: Number(lng),
    focusLat: Number(lat),
  })),
};

const transportDemo: FeatureCollection<Geometry, FeatureProperties> = {
  type: "FeatureCollection",
  features: [
    feature("transport-i70-context", { type: "LineString", coordinates: [[-102.0, 39.31], [-101.1, 39.34], [-99.33, 38.88], [-98.23, 38.73], [-96.58, 39.18], [-95.68, 39.05], [-94.64, 39.1]] }, {
      ...baseProps,
      title: "East–west movement corridor",
      summary: "A generalized route centerline for interaction testing, not navigation.",
      sourceRole: "aggregate",
      spatialScope: "Statewide public route context",
      temporalScope: "Current demonstration context",
      lastUpdate: "2026-08-20",
      evidenceState: "GENERALIZED_GEOMETRY",
      generalizationNote: "Approximate corridor only; no routing, lane, bridge, or operational detail.",
      focusLng: -98.2,
      focusLat: 38.9,
    }),
    feature("transport-north-south-context", { type: "LineString", coordinates: [[-97.62, 39.95], [-97.61, 38.84], [-97.34, 37.69], [-97.33, 37.05]] }, {
      ...baseProps,
      title: "North–south movement corridor",
      summary: "A generalized corridor fixture for comparing community access, report coverage, and map extent.",
      sourceRole: "aggregate",
      spatialScope: "Central Kansas public route context",
      temporalScope: "Current demonstration context",
      lastUpdate: "2026-08-29",
      evidenceState: "GENERALIZED_GEOMETRY",
      citation: "kfm:evidence:synthetic:transport-ns-v1",
      generalizationNote: "Approximate corridor only; no routing, traffic, lane, bridge, schedule, or operational detail.",
      relatedLayers: "Communities; Agricultural context",
      focusLng: -97.5,
      focusLat: 38.5,
    }),
  ],
};

const historyDemo: FeatureCollection<Geometry, FeatureProperties> = {
  type: "FeatureCollection",
  features: [
    feature("history-route-1885", { type: "LineString", coordinates: [[-101.55, 38.55], [-100.25, 38.65], [-99.15, 38.72], [-97.75, 38.82], [-96.4, 39.0]] }, {
      ...baseProps,
      title: "1885 historical-vintage study line",
      summary: "An illustrative line for vintage filtering; it does not assert a historical route.",
      sourceRole: "synthetic",
      spatialScope: "Central Kansas demonstration corridor",
      temporalScope: "Historical-vintage selector: 1885",
      lastUpdate: "2026-08-20",
      evidenceState: "MISSING_EVIDENCE",
      citation: "No historical claim attached",
      year: 1885,
      focusLng: -98.8,
      focusLat: 38.75,
    }),
    feature("history-route-1910", { type: "LineString", coordinates: [[-101.7, 37.85], [-100.3, 37.9], [-98.8, 38.0], [-97.3, 37.75], [-95.75, 37.45]] }, {
      ...baseProps,
      title: "1910 historical-vintage study line",
      summary: "A second illustrative vintage used to demonstrate cumulative time visibility.",
      sourceRole: "synthetic",
      spatialScope: "Southern Kansas demonstration corridor",
      temporalScope: "Historical-vintage selector: 1910",
      lastUpdate: "2026-08-20",
      evidenceState: "SUPERSEDED",
      citation: "kfm:evidence:synthetic:history-1910",
      correctionState: "SUPERSEDED by a later demonstration interpretation",
      year: 1910,
      focusLng: -98.7,
      focusLat: 37.85,
    }),
  ],
};

const restrictedDemo: FeatureCollection<Geometry, FeatureProperties> = {
  type: "FeatureCollection",
  features: [
    feature("planning-generalized-envelope", { type: "Polygon", coordinates: [[[-96.2, 39.55], [-95.15, 39.55], [-95.15, 38.65], [-96.2, 38.65], [-96.2, 39.55]]] }, {
      ...baseProps,
      title: "Generalized protected-context envelope",
      summary: "A deliberately coarse envelope that demonstrates policy denial without exposing a sensitive subject or site.",
      sourceRole: "synthetic",
      spatialScope: "Coarse regional envelope only",
      temporalScope: "Not disclosed",
      lastUpdate: "2026-08-20",
      evidenceState: "DENIED_BY_POLICY",
      releaseState: "RESTRICTED",
      citation: "kfm:policy:public-safe:deny-demo",
      rights: "Exact subject, attributes, and location are not available to this public client.",
      generalizationNote: "The displayed envelope is intentionally unrelated to any exact protected location.",
      uncertainty: "No precise inference is permitted from this demonstration envelope.",
      focusLng: -95.65,
      focusLat: 39.1,
    }),
  ],
};

const diagnosticsDemo: FeatureCollection<Geometry, FeatureProperties> = {
  type: "FeatureCollection",
  features: [
    feature("diagnostic-resolver-error", { type: "Point", coordinates: [-97.34, 37.69] }, {
      ...baseProps,
      title: "Resolver error fixture",
      summary: "A deterministic negative fixture that verifies operational errors do not become unsupported answers.",
      sourceRole: "synthetic",
      spatialScope: "Site-local diagnostic point",
      temporalScope: "2026 test snapshot",
      lastUpdate: "2026-08-20",
      evidenceState: "ERROR",
      citation: "kfm:demo:resolver-error",
      focusLng: -97.34,
      focusLat: 37.69,
    }),
    feature("diagnostic-restricted", { type: "Point", coordinates: [-96.1, 38.25] }, {
      ...baseProps,
      title: "Restricted-access fixture",
      summary: "A deterministic fixture showing that an authenticated or restricted source is unavailable in the public Explorer.",
      sourceRole: "synthetic",
      spatialScope: "Generalized diagnostic point",
      temporalScope: "2026 test snapshot",
      lastUpdate: "2026-08-20",
      evidenceState: "RESTRICTED_ACCESS",
      releaseState: "RESTRICTED",
      citation: "kfm:policy:restricted-access-demo",
      rights: "Public access is not authorized.",
      focusLng: -96.1,
      focusLat: 38.25,
    }),
  ],
};

const watershedDemo: FeatureCollection<Geometry, FeatureProperties> = {
  type: "FeatureCollection",
  features: [
    feature("watershed-upper-arkansas", { type: "Polygon", coordinates: [[[-102.0, 37.25], [-99.65, 37.25], [-99.65, 38.35], [-102.0, 38.35], [-102.0, 37.25]]] }, {
      ...baseProps,
      title: "Upper Arkansas watershed concept",
      summary: "A coarse synthetic basin envelope for inspecting water relationships without hydrologic or regulatory claims.",
      sourceRole: "synthetic context",
      spatialScope: "Western Kansas, deliberately generalized",
      temporalScope: "Static 2026 demonstration context",
      lastUpdate: "2026-08-29",
      evidenceState: "GENERALIZED_GEOMETRY",
      citation: "kfm:evidence:synthetic:watershed-upper-arkansas-v1",
      watershedClass: "WESTERN",
      generalizationNote: "This polygon is not a HUC, drainage divide, flood zone, allocation area, or legal boundary.",
      uncertainty: "Synthetic basin shape created only for interface and report testing.",
      relatedLayers: "Hydrology context; Elevation concept",
      focusLng: -100.82,
      focusLat: 37.8,
    }),
    feature("watershed-smoky-hill", { type: "Polygon", coordinates: [[[-101.15, 38.35], [-97.05, 38.35], [-97.05, 39.45], [-101.15, 39.45], [-101.15, 38.35]]] }, {
      ...baseProps,
      title: "Smoky Hill watershed concept",
      summary: "A generalized synthetic planning envelope aligned only loosely with the demonstration river corridor.",
      sourceRole: "synthetic context",
      spatialScope: "North-central Kansas, deliberately generalized",
      temporalScope: "Static 2026 demonstration context",
      lastUpdate: "2026-08-29",
      evidenceState: "ANSWER",
      citation: "kfm:evidence:synthetic:watershed-smoky-hill-v1",
      watershedClass: "CENTRAL",
      generalizationNote: "No gauge, flow, storage, water-quality, flood, or legal-water conclusion is supported.",
      uncertainty: "Synthetic basin shape and attributes; not derived from a watershed product.",
      relatedLayers: "Hydrology context; Communities",
      focusLng: -99.1,
      focusLat: 38.9,
    }),
    feature("watershed-kansas-lower", { type: "Polygon", coordinates: [[[-97.25, 38.35], [-94.68, 38.35], [-94.68, 40.0], [-97.25, 40.0], [-97.25, 38.35]]] }, {
      ...baseProps,
      title: "Lower Kansas watershed concept",
      summary: "A coarse eastern envelope for testing watershed, community, and smoke-context reports.",
      sourceRole: "synthetic context",
      spatialScope: "Eastern Kansas, deliberately generalized",
      temporalScope: "Static 2026 demonstration context",
      lastUpdate: "2026-08-29",
      evidenceState: "MISSING_EVIDENCE",
      citation: "No released evidence reference available",
      watershedClass: "EASTERN",
      generalizationNote: "This geometry is not an admitted watershed, regulatory, flood, or water-quality layer.",
      uncertainty: "Synthetic basin shape created only for interface and report testing.",
      relatedLayers: "Hydrology context; Smoke context",
      focusLng: -95.95,
      focusLat: 39.15,
    }),
  ],
};

const elevationBands = [
  { west: -102.02, east: -100.8, feet: 3400, height: 780, label: "Western high concept" },
  { west: -100.8, east: -99.55, feet: 2600, height: 590, label: "West-central rise concept" },
  { west: -99.55, east: -98.3, feet: 2100, height: 470, label: "Central upland concept" },
  { west: -98.3, east: -97.05, feet: 1650, height: 350, label: "Central transition concept" },
  { west: -97.05, east: -95.8, feet: 1250, height: 250, label: "Eastern transition concept" },
  { west: -95.8, east: -94.65, feet: 850, height: 150, label: "Eastern low concept" },
] as const;

const elevationDemo: FeatureCollection<Geometry, FeatureProperties> = {
  type: "FeatureCollection",
  features: elevationBands.map((band, index) => feature(`elevation-band-${index + 1}`, {
    type: "Polygon",
    coordinates: [[[band.west, 37.05], [band.east, 37.05], [band.east, 39.95], [band.west, 39.95], [band.west, 37.05]]],
  }, {
    ...baseProps,
    title: band.label,
    summary: `A synthetic relative-elevation band rendered at ${band.feet.toLocaleString()} display feet for reversible 3D interface testing.`,
    sourceRole: "synthetic display context",
    spatialScope: "Statewide longitudinal band, deliberately generalized",
    temporalScope: "Static 2026 display concept",
    lastUpdate: "2026-08-29",
    evidenceState: "GENERALIZED_GEOMETRY",
    citation: `kfm:evidence:synthetic:elevation-band-${index + 1}`,
    displayElevationFt: band.feet,
    relativeHeightM: band.height,
    generalizationNote: "Display heights are invented relative bins, not DEM samples, contours, survey elevations, terrain, hillshade, or topographic evidence.",
    uncertainty: "Synthetic east-west gradient used only to prove extrusion, camera, selection, and 2D evidence parity.",
    relatedLayers: "Geology & landforms; Watershed context",
    focusLng: (band.west + band.east) / 2,
    focusLat: 38.5,
  })),
};

const smokeDemo: FeatureCollection<Geometry, FeatureProperties> = {
  type: "FeatureCollection",
  features: [
    feature("smoke-west-2022", { type: "Polygon", coordinates: [[[-102.0, 38.2], [-100.3, 37.65], [-98.9, 38.15], [-99.55, 39.0], [-101.4, 39.35], [-102.0, 38.2]]] }, {
      ...baseProps,
      title: "Western smoke-context fixture · 2022",
      summary: "A synthetic stale plume envelope for testing time filters and negative freshness states.",
      sourceRole: "synthetic model context",
      spatialScope: "Western Kansas generalized envelope",
      temporalScope: "Synthetic 2022 snapshot",
      lastUpdate: "2022-08-01",
      freshnessState: "STALE",
      evidenceState: "SOURCE_STALE",
      citation: "kfm:evidence:synthetic:smoke-2022",
      smokeDensity: "LOW",
      year: 2022,
      generalizationNote: "Not observed smoke, a forecast, an advisory, an exposure surface, or a fire perimeter.",
      uncertainty: "Shape, timing, and density are invented for temporal interface testing.",
      relatedLayers: "Atmosphere observations; Watershed context",
      focusLng: -100.45,
      focusLat: 38.45,
    }),
    feature("smoke-central-2024", { type: "Polygon", coordinates: [[[-100.1, 38.95], [-98.4, 38.25], [-96.75, 38.5], [-97.35, 39.45], [-99.15, 39.65], [-100.1, 38.95]]] }, {
      ...baseProps,
      title: "Central smoke-context fixture · 2024",
      summary: "A corrected synthetic plume retained to keep correction state visible in a time-aware map layer.",
      sourceRole: "synthetic model context",
      spatialScope: "Central Kansas generalized envelope",
      temporalScope: "Synthetic 2024 snapshot",
      lastUpdate: "2024-09-15",
      evidenceState: "CORRECTED",
      citation: "kfm:evidence:synthetic:smoke-2024-corrected",
      smokeDensity: "HIGH",
      year: 2024,
      correctionState: "CORRECTED_FIXTURE",
      generalizationNote: "Not observed smoke, a forecast, an advisory, an exposure surface, or a fire perimeter.",
      uncertainty: "Shape, timing, and density are invented for correction and timeline testing.",
      relatedLayers: "Atmosphere observations; Communities",
      focusLng: -98.45,
      focusLat: 39.0,
    }),
    feature("smoke-east-2026", { type: "Polygon", coordinates: [[[-98.35, 38.1], [-96.45, 37.65], [-94.7, 38.15], [-95.15, 39.2], [-96.95, 39.55], [-98.35, 38.1]]] }, {
      ...baseProps,
      title: "Eastern smoke-context fixture · 2026",
      summary: "A generalized synthetic plume demonstrating map, report, and Evidence Drawer parity without current-condition claims.",
      sourceRole: "synthetic model context",
      spatialScope: "Eastern Kansas generalized envelope",
      temporalScope: "Synthetic 2026 snapshot",
      lastUpdate: "2026-08-29",
      evidenceState: "GENERALIZED_GEOMETRY",
      citation: "kfm:evidence:synthetic:smoke-2026",
      smokeDensity: "MODERATE",
      generalizationNote: "Not observed smoke, a forecast, an advisory, an exposure surface, or a fire perimeter.",
      uncertainty: "Shape, timing, and density are invented for public-safe UI testing.",
      relatedLayers: "Atmosphere observations; Watershed context",
      focusLng: -96.35,
      focusLat: 38.65,
    }),
  ],
};

const tileGridDemo: FeatureCollection<Geometry, FeatureProperties> = {
  type: "FeatureCollection",
  features: Array.from({ length: 24 }, (_, index) => {
    const column = index % 6;
    const row = Math.floor(index / 6);
    const west = -102 + column * 1.22;
    const east = Math.min(-94.68, west + 1.22);
    const south = 37.05 + row * 0.72;
    const north = Math.min(39.95, south + 0.72);
    return feature(`tile-cell-${column}-${row}`, { type: "Polygon", coordinates: [[[west, south], [east, south], [east, north], [west, north], [west, south]]] }, {
      ...baseProps,
      title: `Diagnostic tile cell ${column + 1}.${row + 1}`,
      summary: "A site-local GeoJSON grid cell labeled like a tile matrix for viewport and selection diagnostics.",
      sourceRole: "synthetic diagnostics",
      spatialScope: "Kansas diagnostic grid",
      temporalScope: "Not time-varying",
      lastUpdate: "2026-08-29",
      evidenceState: "GENERALIZED_GEOMETRY",
      citation: `kfm:demo:tile-grid:${column}:${row}`,
      tileLabel: `SIM/${column}/${row}`,
      generalizationNote: "This is not a fetched vector tile, PMTiles archive, cache entry, source-layer, or release artifact.",
      uncertainty: "Grid boundaries are arbitrary and exist only to exercise tile-style navigation and diagnostics.",
      relatedLayers: "All local layers",
      focusLng: (west + east) / 2,
      focusLat: (south + north) / 2,
    });
  }),
};

const fill = (id: string, sourceId: string, color: string, opacity: number, outline: string): RendererDefinition => ({
  id,
  interactive: true,
  opacityProperties: ["fill-opacity"],
  spec: { id, type: "fill", source: sourceId, paint: { "fill-color": color, "fill-opacity": opacity, "fill-outline-color": ["case", ["boolean", ["feature-state", "hover"], false], "#fff4ce", outline] } },
});

const line = (id: string, sourceId: string, color: string, width: number, opacity = 0.9, dash?: number[]): RendererDefinition => ({
  id,
  interactive: true,
  opacityProperties: ["line-opacity"],
  spec: {
    id,
    type: "line",
    source: sourceId,
    paint: {
      "line-color": color,
      "line-width": ["case", ["boolean", ["feature-state", "hover"], false], width + 2, width],
      "line-opacity": opacity,
      ...(dash ? { "line-dasharray": dash } : {}),
    },
  },
});

const point = (id: string, sourceId: string, color: string, radius: number, opacity = 0.95, filter?: RendererFilterDescriptor): RendererDefinition => ({
  id,
  interactive: true,
  opacityProperties: ["circle-opacity"],
  baseFilter: filter,
  spec: {
    id,
    type: "circle",
    source: sourceId,
    ...(filter ? { filter } : {}),
    paint: {
      "circle-color": color,
      "circle-radius": ["case", ["boolean", ["feature-state", "hover"], false], radius + 3, radius],
      "circle-opacity": opacity,
      "circle-stroke-color": "#f6e3b4",
      "circle-stroke-width": 1.5,
    },
  },
});

export const LAYER_REGISTRY: LayerRecord[] = [
  {
    id: "kansas-extent", title: "Kansas demonstration extent", description: "Simplified statewide frame and public-safe selection scope.", domain: "Boundaries", category: "Boundaries & places", sourceType: "GeoJSON", sourceId: "kfm-kansas-extent", datasetName: "KFM site-local Kansas extent fixture", geometryType: "Polygon", minZoom: 4, maxZoom: 12, defaultVisibility: true, defaultOpacity: 0.42,
    legend: [{ label: "Generalized extent", color: "#c8a963", shape: "fill" }], units: "degrees", scaleNote: "Statewide generalized context", validTimeExtent: "Not time-varying", sourceTime: "Site build 2026-08-20", releaseTime: "Demonstration build", freshnessState: "NOT_APPLICABLE", attribution: "KFM site-local demonstration geometry", evidenceReference: "kfm:demo:site-local:v1", publicStatus: "GENERALIZED", sensitivityNote: "Not an authoritative boundary.", releaseState: "GENERALIZED", correctionNote: "Replace only through a released public-safe boundary adapter.", relatedLayers: ["Communities"], interactions: ["hover", "select", "zoom"], filters: [], viewingModes: ["2D", "globe"], bounds: [-102.1, 36.95, -94.55, 40.05], data: kansasBoundary,
    renderers: [fill("kansas-extent-fill", "kfm-kansas-extent", "#244f45", 0.42, "#d9bc77"), line("kansas-extent-line", "kfm-kansas-extent", "#d9bc77", 1.8, 0.9)],
  },
  {
    id: "water-context", title: "Hydrology context", description: "Simplified Kansas river and basin corridors with explicit evidence states.", domain: "Hydrology", category: "Hydrology & water", sourceType: "GeoJSON", sourceId: "kfm-water", datasetName: "KFM synthetic hydrology interaction fixtures", geometryType: "LineString", minZoom: 5, maxZoom: 14, defaultVisibility: true, defaultOpacity: 0.9,
    legend: [{ label: "Demonstration water corridor", color: "#63c8db", shape: "line" }], units: "not applicable", scaleNote: "Generalized statewide corridor", validTimeExtent: "2022–2026 demonstration context", sourceTime: "Mixed synthetic source time", releaseTime: "Demonstration build", freshnessState: "MIXED", attribution: "KFM site-local synthetic fixture", evidenceReference: "Per-feature EvidenceRef", publicStatus: "GENERALIZED", sensitivityNote: "No monitoring location, measurement, or operational status is asserted.", releaseState: "DEMONSTRATION", correctionNote: "Stale and missing evidence remain visible.", relatedLayers: ["Watershed context", "Atmosphere observations", "Communities"], interactions: ["hover", "select", "zoom", "evidence", "flow-direction display"], filters: ["time context"], viewingModes: ["2D", "globe", "pitched"], bounds: [-102.05, 37.0, -94.6, 39.2], sourceOptions: { lineMetrics: true }, data: waterDemo,
    renderers: [
      line("water-context-line", "kfm-water", "#2d7d9a", 5, 0.72),
      { id: "water-context-flow", spec: { id: "water-context-flow", type: "line", source: "kfm-water", paint: { "line-color": "#7fe8f5", "line-width": 2.2, "line-opacity": 0.96, "line-gradient": ["interpolate", ["linear"], ["line-progress"], 0, "#9af2ff", 0.5, "#4cb6d3", 1, "#e6fbff"] } } },
    ],
  },
  {
    id: "watershed-context", title: "Watershed & storage context", description: "Three coarse synthetic basin envelopes for water-system navigation and reporting.", domain: "Hydrology", category: "Hydrology & water", sourceType: "GeoJSON", sourceId: "kfm-watersheds", datasetName: "KFM synthetic watershed concept fixtures", geometryType: "Polygon", minZoom: 4, maxZoom: 12, defaultVisibility: true, defaultOpacity: 0.18,
    legend: [{ label: "Synthetic basin envelope", color: "#2b7f91", shape: "fill" }], units: "not applicable", scaleNote: "Coarse statewide concept only", validTimeExtent: "Static 2026 demonstration context", sourceTime: "Site build", releaseTime: "Demonstration build", freshnessState: "NOT_APPLICABLE", attribution: "KFM site-local synthetic fixture", evidenceReference: "Per-feature demonstration reference", publicStatus: "GENERALIZED", sensitivityNote: "No HUC, flow, storage, allocation, flood, monitoring, or regulatory claim.", releaseState: "DEMONSTRATION", correctionNote: "Replace only through an admitted public-safe watershed adapter.", relatedLayers: ["Hydrology context", "Elevation concept"], interactions: ["hover", "select", "zoom", "evidence", "report"], filters: [], viewingModes: ["2D", "globe", "pitched"], bounds: [-102.0, 37.2, -94.65, 40.0], data: watershedDemo,
    renderers: [{ id: "watershed-context-fill", interactive: true, opacityProperties: ["fill-opacity"], spec: { id: "watershed-context-fill", type: "fill", source: "kfm-watersheds", paint: { "fill-color": ["match", ["get", "watershedClass"], "WESTERN", "#245f71", "CENTRAL", "#287f8a", "EASTERN", "#2f9fb2", "#2b7f91"], "fill-opacity": 0.18, "fill-outline-color": "#76d5df" } } }],
  },
  {
    id: "prairie-context", title: "Prairie & ecological regions", description: "Generalized regional ecology fixtures with no protected-species coordinates.", domain: "Habitat", category: "Land cover & ecology", sourceType: "GeoJSON", sourceId: "kfm-prairie", datasetName: "KFM generalized ecological region fixture", geometryType: "Polygon", minZoom: 4, maxZoom: 12, defaultVisibility: true, defaultOpacity: 0.25,
    legend: [{ label: "Generalized ecology region", color: "#78a86f", shape: "fill" }], units: "regional context", scaleNote: "Coarse statewide envelope", validTimeExtent: "Illustrative 2026 snapshot", sourceTime: "Site build", releaseTime: "Demonstration build", freshnessState: "NOT_APPLICABLE", attribution: "KFM site-local synthetic fixture", evidenceReference: "Per-feature state", publicStatus: "GENERALIZED", sensitivityNote: "No rare-species, habitat-site, or private-property detail.", releaseState: "GENERALIZED", correctionNote: "Rendered region is context, not ecological proof.", relatedLayers: ["Geology & landforms"], interactions: ["hover", "select", "zoom"], filters: [], viewingModes: ["2D", "globe"], bounds: [-102.03, 37.04, -96.05, 39.96], data: prairieDemo,
    renderers: [fill("prairie-context-fill", "kfm-prairie", "#78a86f", 0.25, "#a8ce8c")],
  },
  {
    id: "geology-context", title: "Geology & landforms", description: "Generalized landform context with a visible stale-source posture.", domain: "Geology", category: "Geology & landforms", sourceType: "GeoJSON", sourceId: "kfm-geology", datasetName: "KFM landform context fixture", geometryType: "Polygon", minZoom: 5, maxZoom: 13, defaultVisibility: false, defaultOpacity: 0.34,
    legend: [{ label: "Landform context", color: "#b98962", shape: "fill" }], units: "regional context", scaleNote: "Generalized regional envelope", validTimeExtent: "Demonstration source vintage 2019", sourceTime: "2019", releaseTime: "Demonstration build", freshnessState: "STALE", attribution: "KFM site-local synthetic fixture", evidenceReference: "kfm:evidence:synthetic:geology-stale", publicStatus: "GENERALIZED", sensitivityNote: "Not suitable for engineering or mineral-resource claims.", releaseState: "DEMONSTRATION", correctionNote: "Stale status is intentionally preserved.", relatedLayers: ["Prairie & ecological regions"], interactions: ["hover", "select", "zoom", "evidence"], filters: [], viewingModes: ["2D", "globe"], bounds: [-100.55, 38.0, -97.15, 39.65], data: geologyDemo,
    renderers: [fill("geology-context-fill", "kfm-geology", "#b98962", 0.34, "#e0b98d")],
  },
  {
    id: "elevation-concept", title: "Elevation extrusion concept", description: "Six invented relative-height bands for 3D camera, extrusion, selection, and 2D evidence-parity testing.", domain: "Geology", category: "Geology & landforms", sourceType: "GeoJSON", sourceId: "kfm-elevation-concept", datasetName: "KFM synthetic relative-elevation display fixture", geometryType: "Polygon", minZoom: 4, maxZoom: 12, defaultVisibility: false, defaultOpacity: 0.72,
    legend: [{ label: "Relative display height · synthetic", color: "#c59058", shape: "fill" }], units: "invented relative display feet", scaleNote: "Six statewide longitudinal bands", validTimeExtent: "Static 2026 display concept", sourceTime: "Site build", releaseTime: "Demonstration build", freshnessState: "NOT_APPLICABLE", attribution: "KFM site-local synthetic fixture", evidenceReference: "Per-band demonstration reference", publicStatus: "GENERALIZED", sensitivityNote: "No DEM, contour, survey elevation, hillshade, terrain source, or protected vertical detail.", releaseState: "DEMONSTRATION", correctionNote: "A real elevation carrier remains held pending source, rights, manifest, performance, evidence-parity, and rollback proof.", relatedLayers: ["Geology & landforms", "Watershed context"], interactions: ["hover", "select", "zoom", "pitch", "extrusion"], filters: [], viewingModes: ["2D fallback", "pitched extrusion"], bounds: [-102.02, 37.05, -94.65, 39.95], data: elevationDemo,
    renderers: [
      { id: "elevation-concept-underlay", spec: { id: "elevation-concept-underlay", type: "fill", source: "kfm-elevation-concept", paint: { "fill-color": ["interpolate", ["linear"], ["get", "displayElevationFt"], 800, "#294f4e", 1800, "#777348", 2600, "#ad7448", 3500, "#dfad68"], "fill-opacity": 0.08, "fill-outline-color": "#d9b978" } } },
      { id: "elevation-concept-extrusion", interactive: true, opacityProperties: ["fill-extrusion-opacity"], spec: { id: "elevation-concept-extrusion", type: "fill-extrusion", source: "kfm-elevation-concept", paint: { "fill-extrusion-color": ["interpolate", ["linear"], ["get", "displayElevationFt"], 800, "#315b57", 1800, "#8b7c4a", 2600, "#b9794b", 3500, "#e2ae6a"], "fill-extrusion-height": ["get", "relativeHeightM"], "fill-extrusion-base": 0, "fill-extrusion-opacity": 0.72, "fill-extrusion-vertical-gradient": true } } },
    ],
  },
  {
    id: "agriculture-context", title: "Agricultural context", description: "Coarse, public-safe regional fixtures without farm-level attributes.", domain: "Agriculture", category: "Agriculture", sourceType: "GeoJSON", sourceId: "kfm-agriculture", datasetName: "KFM public-safe agriculture fixtures", geometryType: "Polygon", minZoom: 5, maxZoom: 12, defaultVisibility: false, defaultOpacity: 0.24,
    legend: [{ label: "Generalized agricultural context", color: "#b4a45f", shape: "fill" }], units: "regional context", scaleNote: "Coarse public-safe envelope", validTimeExtent: "Demonstration snapshot", sourceTime: "Site build", releaseTime: "Demonstration build", freshnessState: "NOT_APPLICABLE", attribution: "KFM site-local synthetic fixture", evidenceReference: "No claim-bearing evidence", publicStatus: "GENERALIZED", sensitivityNote: "No parcel, operator, yield, or private-land detail.", releaseState: "GENERALIZED", correctionNote: "No operational agriculture claim is made.", relatedLayers: ["Prairie & ecological regions"], interactions: ["hover", "select", "zoom"], filters: [], viewingModes: ["2D"], bounds: [-101.8, 37.35, -99.75, 39.35], data: agricultureDemo,
    renderers: [fill("agriculture-context-fill", "kfm-agriculture", "#b4a45f", 0.24, "#d8c97c")],
  },
  {
    id: "atmosphere-observations", title: "Atmosphere observations", description: "Three year-specific synthetic observations for temporal and correction-state testing.", domain: "Atmosphere", category: "Weather & hazards", sourceType: "GeoJSON", sourceId: "kfm-atmosphere", datasetName: "KFM temporal observation fixture", geometryType: "Point", minZoom: 5, maxZoom: 15, defaultVisibility: true, defaultOpacity: 0.95,
    legend: [{ label: "Synthetic observation", color: "#efc86e", shape: "point" }], units: "no measured variable", scaleNote: "Generalized place points", validTimeExtent: "Observation years 2022, 2024, 2026", sourceTime: "Per-feature observation year", releaseTime: "Demonstration build", freshnessState: "MIXED", attribution: "KFM site-local synthetic fixture", evidenceReference: "Per-feature EvidenceRef", publicStatus: "GENERALIZED", sensitivityNote: "No real weather measurement or hazard advisory.", releaseState: "DEMONSTRATION", correctionNote: "Corrected and stale states are explicit.", relatedLayers: ["Hydrology context"], interactions: ["hover", "select", "zoom", "evidence"], filters: ["observation year"], viewingModes: ["2D", "globe"], bounds: [-101.75, 38.8, -95.6, 39.4], temporal: { field: "year", mode: "exact", years: [2022, 2024, 2026], label: "Observation time" }, data: atmosphereDemo,
    renderers: [point("atmosphere-observations-circle", "kfm-atmosphere", "#efc86e", 7)],
  },
  {
    id: "smoke-context", title: "Smoke-context timeline", description: "Three year-specific synthetic plume envelopes for time, correction, reporting, and not-for-life-safety testing.", domain: "Atmosphere", category: "Weather & hazards", sourceType: "GeoJSON", sourceId: "kfm-smoke-context", datasetName: "KFM synthetic smoke-context fixture", geometryType: "Polygon", minZoom: 4, maxZoom: 12, defaultVisibility: false, defaultOpacity: 0.28,
    legend: [{ label: "Synthetic smoke-context envelope", color: "#b99ab8", shape: "fill" }], units: "qualitative synthetic density", scaleNote: "Generalized statewide envelopes", validTimeExtent: "Synthetic snapshots for 2022, 2024, and 2026", sourceTime: "Per-feature synthetic year", releaseTime: "Demonstration build", freshnessState: "MIXED", attribution: "KFM site-local synthetic fixture", evidenceReference: "Per-feature demonstration reference", publicStatus: "GENERALIZED", sensitivityNote: "Not observed smoke, a forecast, an AQI product, a fire perimeter, an exposure estimate, or an emergency advisory.", releaseState: "DEMONSTRATION", correctionNote: "The 2024 fixture preserves a visible correction state.", relatedLayers: ["Atmosphere observations", "Watershed context", "Communities"], interactions: ["hover", "select", "zoom", "time", "evidence", "report"], filters: ["synthetic year"], viewingModes: ["2D", "globe", "pitched"], bounds: [-102.0, 37.6, -94.7, 39.65], temporal: { field: "year", mode: "exact", years: [2022, 2024, 2026], label: "Synthetic smoke context" }, data: smokeDemo,
    renderers: [{ id: "smoke-context-fill", interactive: true, opacityProperties: ["fill-opacity"], spec: { id: "smoke-context-fill", type: "fill", source: "kfm-smoke-context", paint: { "fill-color": ["match", ["get", "smokeDensity"], "LOW", "#8ba0aa", "MODERATE", "#b29aa8", "HIGH", "#d18787", "#a99aa8"], "fill-opacity": 0.28, "fill-outline-color": "#e4c5cf" } } }],
  },
  {
    id: "communities", title: "Communities", description: "Public place-name points with stable identifiers and clustering.", domain: "Settlements", category: "Boundaries & places", sourceType: "GeoJSON", sourceId: "kfm-communities", datasetName: "KFM place search fixture", geometryType: "Point", minZoom: 4, maxZoom: 16, defaultVisibility: true, defaultOpacity: 0.95,
    legend: [{ label: "Place context", color: "#f0f4e9", shape: "point" }], units: "place point", scaleNote: "Generalized place center", validTimeExtent: "Current demonstration context", sourceTime: "Site build", releaseTime: "Demonstration build", freshnessState: "NOT_APPLICABLE", attribution: "KFM site-local place fixture", evidenceReference: "kfm:demo:site-local:v1", publicStatus: "PUBLIC_SAFE", sensitivityNote: "Public place names only.", releaseState: "DEMONSTRATION", correctionNote: "Not a gazetteer or municipal boundary source.", relatedLayers: ["Hydrology context", "Transportation"], interactions: ["cluster", "hover", "select", "search", "zoom"], filters: [], viewingModes: ["2D", "globe"], bounds: [-101.8, 37.6, -94.55, 39.45], sourceOptions: { cluster: true, clusterRadius: 54, clusterMaxZoom: 7 }, data: communitiesDemo,
    renderers: [
      point("communities-clusters", "kfm-communities", "#8fc8b0", 12, 0.9, ["has", "point_count"]),
      { id: "communities-count", baseFilter: ["has", "point_count"], spec: { id: "communities-count", type: "symbol", source: "kfm-communities", filter: ["has", "point_count"], layout: { "text-field": ["get", "point_count_abbreviated"], "text-size": 11 }, paint: { "text-color": "#071719" } } },
      point("communities-points", "kfm-communities", "#f0f4e9", 5.5, 0.95, ["!", ["has", "point_count"]]),
    ],
  },
  {
    id: "transport-context", title: "Roads, rail & movement", description: "Generalized corridor context for system relationships, not navigation.", domain: "Transport", category: "Roads, rail & movement", sourceType: "GeoJSON", sourceId: "kfm-transport", datasetName: "KFM movement corridor fixtures", geometryType: "LineString", minZoom: 5, maxZoom: 14, defaultVisibility: false, defaultOpacity: 0.75,
    legend: [{ label: "Generalized movement corridor", color: "#dc9d72", shape: "line" }], units: "not navigable", scaleNote: "Statewide generalized corridor", validTimeExtent: "Current demonstration context", sourceTime: "Site build", releaseTime: "Demonstration build", freshnessState: "NOT_APPLICABLE", attribution: "KFM site-local synthetic fixture", evidenceReference: "kfm:demo:site-local:v1", publicStatus: "GENERALIZED", sensitivityNote: "No operational infrastructure detail.", releaseState: "GENERALIZED", correctionNote: "Not suitable for routing or asset inspection.", relatedLayers: ["Communities"], interactions: ["hover", "select", "zoom"], filters: [], viewingModes: ["2D", "globe"], bounds: [-102.0, 38.7, -94.6, 39.35], data: transportDemo,
    renderers: [line("transport-context-line", "kfm-transport", "#dc9d72", 2.2, 0.75, [3, 2])],
  },
  {
    id: "historical-context", title: "Historical-vintage study lines", description: "Illustrative lines for time-vintage controls; no historical route claim.", domain: "History", category: "Historical geography", sourceType: "GeoJSON", sourceId: "kfm-history", datasetName: "KFM historical-vintage interaction fixture", geometryType: "LineString", minZoom: 5, maxZoom: 13, defaultVisibility: false, defaultOpacity: 0.72,
    legend: [{ label: "Available by selected vintage", color: "#d8b77a", shape: "line" }], units: "illustrative", scaleNote: "Statewide study line", validTimeExtent: "1885 and 1910 vintages", sourceTime: "Per-feature historical vintage", releaseTime: "Demonstration build", freshnessState: "NOT_APPLICABLE", attribution: "KFM site-local synthetic fixture", evidenceReference: "Per-feature negative state", publicStatus: "GENERALIZED", sensitivityNote: "No archaeological or protected-site coordinate.", releaseState: "DEMONSTRATION", correctionNote: "1910 fixture carries a visible supersession state.", relatedLayers: ["Transportation"], interactions: ["hover", "select", "zoom", "time"], filters: ["historical vintage"], viewingModes: ["2D"], bounds: [-101.8, 37.4, -95.7, 39.05], temporal: { field: "year", mode: "through", years: [1885, 1910], label: "Historical vintage" }, data: historyDemo,
    renderers: [line("historical-context-line", "kfm-history", "#d8b77a", 2.4, 0.72, [4, 3])],
  },
  {
    id: "public-safe-planning", title: "Generalized protected context", description: "Coarse envelope demonstrating policy denial without revealing a protected subject.", domain: "Planning", category: "Public-safe planning", sourceType: "GeoJSON", sourceId: "kfm-planning", datasetName: "KFM denied-context fixture", geometryType: "Polygon", minZoom: 5, maxZoom: 11, defaultVisibility: false, defaultOpacity: 0.18,
    legend: [{ label: "Policy-generalized envelope", color: "#ee8f7c", shape: "fill" }], units: "withheld", scaleNote: "Coarse regional envelope", validTimeExtent: "Not disclosed", sourceTime: "Withheld", releaseTime: "Demonstration build", freshnessState: "NOT_APPLICABLE", attribution: "KFM public-safe policy fixture", evidenceReference: "kfm:policy:public-safe:deny-demo", publicStatus: "RESTRICTED", sensitivityNote: "Exact subject, attributes, and coordinates are absent.", releaseState: "RESTRICTED", correctionNote: "No client-side style can reveal withheld detail.", relatedLayers: [], interactions: ["hover", "select", "policy explanation"], filters: [], viewingModes: ["2D"], bounds: [-96.2, 38.65, -95.15, 39.55], data: restrictedDemo,
    renderers: [fill("public-safe-planning-fill", "kfm-planning", "#ee8f7c", 0.18, "#ee8f7c")],
  },
  {
    id: "tile-matrix-grid", title: "Tile matrix diagnostic grid", description: "A labeled site-local GeoJSON grid for tile-style viewport navigation and source-boundary inspection.", domain: "Diagnostics", category: "Review & diagnostics", sourceType: "GeoJSON", sourceId: "kfm-tile-grid", datasetName: "KFM synthetic tile matrix diagnostics fixture", geometryType: "Polygon", minZoom: 4, maxZoom: 11, defaultVisibility: false, defaultOpacity: 0.72,
    legend: [{ label: "Simulated tile cell", color: "#d5bd75", shape: "line" }], units: "SIM/column/row", scaleNote: "24 arbitrary statewide cells", validTimeExtent: "Not time-varying", sourceTime: "Site build", releaseTime: "Demonstration build", freshnessState: "NOT_APPLICABLE", attribution: "KFM site-local diagnostic fixture", evidenceReference: "kfm:demo:tile-grid", publicStatus: "PUBLIC_SAFE", sensitivityNote: "No tile archive, source layer, cache key, range response, protected property, or released geometry is present.", releaseState: "DEMONSTRATION", correctionNote: "PMTiles, MVT, COG, DEM, and offline delivery remain separate held capabilities.", relatedLayers: ["All site-local layers"], interactions: ["hover", "select", "zoom", "tile-coordinate inspection"], filters: [], viewingModes: ["2D", "globe", "pitched"], bounds: [-102.0, 37.05, -94.68, 39.95], data: tileGridDemo,
    renderers: [
      { id: "tile-matrix-grid-fill", interactive: true, spec: { id: "tile-matrix-grid-fill", type: "fill", source: "kfm-tile-grid", paint: { "fill-color": "#d5bd75", "fill-opacity": 0.025 } } },
      line("tile-matrix-grid-line", "kfm-tile-grid", "#d5bd75", 1.1, 0.72, [2, 2]),
      { id: "tile-matrix-grid-label", opacityProperties: ["text-opacity"], spec: { id: "tile-matrix-grid-label", type: "symbol", source: "kfm-tile-grid", layout: { "text-field": ["get", "tileLabel"], "text-size": 9, "text-allow-overlap": false }, paint: { "text-color": "#ead79c", "text-halo-color": "#07171a", "text-halo-width": 1.5, "text-opacity": 0.72 } } },
    ],
  },
  {
    id: "review-diagnostics", title: "Finite-state diagnostics", description: "Clearly separated test fixtures for ERROR and RESTRICTED_ACCESS paths.", domain: "Diagnostics", category: "Review & diagnostics", sourceType: "GeoJSON", sourceId: "kfm-diagnostics", datasetName: "KFM deterministic UI negative fixtures", geometryType: "Point", minZoom: 5, maxZoom: 15, defaultVisibility: false, defaultOpacity: 0.95,
    legend: [{ label: "Diagnostic fixture", color: "#ee8f7c", shape: "point" }], units: "not applicable", scaleNote: "Site-local diagnostic points", validTimeExtent: "2026 test snapshot", sourceTime: "Site build", releaseTime: "Demonstration build", freshnessState: "NOT_APPLICABLE", attribution: "KFM site-local deterministic fixtures", evidenceReference: "Per-feature finite negative", publicStatus: "PUBLIC_SAFE", sensitivityNote: "Contains no real protected subject.", releaseState: "DEMONSTRATION", correctionNote: "Review-only layer; separated from knowledge layers.", relatedLayers: [], interactions: ["hover", "select", "focus outcome"], filters: [], viewingModes: ["2D"], bounds: [-97.4, 37.6, -96.0, 38.35], data: diagnosticsDemo,
    renderers: [point("review-diagnostics-circle", "kfm-diagnostics", "#ee8f7c", 7)],
  },
];

export const CATEGORY_ORDER: LayerCategory[] = [
  "Boundaries & places", "Hydrology & water", "Geology & landforms", "Land cover & ecology", "Agriculture", "Weather & hazards", "Roads, rail & movement", "Historical geography", "Public-safe planning", "Review & diagnostics",
];

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
  1800,
  1854,
  1885,
  1910,
  1950,
  2000,
  2019,
  2022,
  2024,
  2026,
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
