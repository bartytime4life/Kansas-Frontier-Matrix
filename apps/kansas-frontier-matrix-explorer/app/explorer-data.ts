import type { FeatureCollection, Geometry } from "geojson";
import type { FilterSpecification, LayerSpecification } from "maplibre-gl";

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
  spec: LayerSpecification;
  interactive?: boolean;
  opacityProperties?: ("fill-opacity" | "line-opacity" | "circle-opacity" | "text-opacity")[];
  baseFilter?: FilterSpecification;
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
  sourceOptions?: { cluster?: boolean; clusterRadius?: number; clusterMaxZoom?: number };
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
    ["place-kansas-city", "Kansas City", -94.63, 39.11],
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

const point = (id: string, sourceId: string, color: string, radius: number, opacity = 0.95, filter?: FilterSpecification): RendererDefinition => ({
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
    id: "water-context", title: "Hydrology context", description: "Simplified Kansas river corridors with explicit evidence states.", domain: "Hydrology", category: "Hydrology & water", sourceType: "GeoJSON", sourceId: "kfm-water", datasetName: "KFM synthetic hydrology interaction fixture", geometryType: "LineString", minZoom: 5, maxZoom: 14, defaultVisibility: true, defaultOpacity: 0.9,
    legend: [{ label: "Demonstration water corridor", color: "#63c8db", shape: "line" }], units: "not applicable", scaleNote: "Generalized statewide corridor", validTimeExtent: "2022–2026 demonstration context", sourceTime: "Mixed synthetic source time", releaseTime: "Demonstration build", freshnessState: "MIXED", attribution: "KFM site-local synthetic fixture", evidenceReference: "Per-feature EvidenceRef", publicStatus: "GENERALIZED", sensitivityNote: "No monitoring location, measurement, or operational status is asserted.", releaseState: "DEMONSTRATION", correctionNote: "Stale and missing evidence remain visible.", relatedLayers: ["Atmosphere observations", "Communities"], interactions: ["hover", "select", "zoom", "evidence"], filters: ["time context"], viewingModes: ["2D", "globe"], bounds: [-102.05, 37.0, -94.6, 39.2], data: waterDemo,
    renderers: [line("water-context-line", "kfm-water", "#63c8db", 3, 0.9)],
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
    id: "agriculture-context", title: "Agricultural context", description: "Coarse, public-safe regional fixture without farm-level attributes.", domain: "Agriculture", category: "Agriculture", sourceType: "GeoJSON", sourceId: "kfm-agriculture", datasetName: "KFM public-safe agriculture fixture", geometryType: "Polygon", minZoom: 5, maxZoom: 12, defaultVisibility: false, defaultOpacity: 0.24,
    legend: [{ label: "Generalized agricultural context", color: "#b4a45f", shape: "fill" }], units: "regional context", scaleNote: "Coarse public-safe envelope", validTimeExtent: "Demonstration snapshot", sourceTime: "Site build", releaseTime: "Demonstration build", freshnessState: "NOT_APPLICABLE", attribution: "KFM site-local synthetic fixture", evidenceReference: "No claim-bearing evidence", publicStatus: "GENERALIZED", sensitivityNote: "No parcel, operator, yield, or private-land detail.", releaseState: "GENERALIZED", correctionNote: "No operational agriculture claim is made.", relatedLayers: ["Prairie & ecological regions"], interactions: ["hover", "select", "zoom"], filters: [], viewingModes: ["2D"], bounds: [-101.8, 37.35, -99.75, 39.35], data: agricultureDemo,
    renderers: [fill("agriculture-context-fill", "kfm-agriculture", "#b4a45f", 0.24, "#d8c97c")],
  },
  {
    id: "atmosphere-observations", title: "Atmosphere observations", description: "Three year-specific synthetic observations for temporal and correction-state testing.", domain: "Atmosphere", category: "Weather & hazards", sourceType: "GeoJSON", sourceId: "kfm-atmosphere", datasetName: "KFM temporal observation fixture", geometryType: "Point", minZoom: 5, maxZoom: 15, defaultVisibility: true, defaultOpacity: 0.95,
    legend: [{ label: "Synthetic observation", color: "#efc86e", shape: "point" }], units: "no measured variable", scaleNote: "Generalized place points", validTimeExtent: "Observation years 2022, 2024, 2026", sourceTime: "Per-feature observation year", releaseTime: "Demonstration build", freshnessState: "MIXED", attribution: "KFM site-local synthetic fixture", evidenceReference: "Per-feature EvidenceRef", publicStatus: "GENERALIZED", sensitivityNote: "No real weather measurement or hazard advisory.", releaseState: "DEMONSTRATION", correctionNote: "Corrected and stale states are explicit.", relatedLayers: ["Hydrology context"], interactions: ["hover", "select", "zoom", "evidence"], filters: ["observation year"], viewingModes: ["2D", "globe"], bounds: [-101.75, 38.8, -95.6, 39.4], temporal: { field: "year", mode: "exact", years: [2022, 2024, 2026], label: "Observation time" }, data: atmosphereDemo,
    renderers: [point("atmosphere-observations-circle", "kfm-atmosphere", "#efc86e", 7)],
  },
  {
    id: "communities", title: "Communities", description: "Public place-name points with stable identifiers and clustering.", domain: "Settlements", category: "Boundaries & places", sourceType: "GeoJSON", sourceId: "kfm-communities", datasetName: "KFM place search fixture", geometryType: "Point", minZoom: 4, maxZoom: 16, defaultVisibility: true, defaultOpacity: 0.95,
    legend: [{ label: "Place context", color: "#f0f4e9", shape: "point" }], units: "place point", scaleNote: "Generalized place center", validTimeExtent: "Current demonstration context", sourceTime: "Site build", releaseTime: "Demonstration build", freshnessState: "NOT_APPLICABLE", attribution: "KFM site-local place fixture", evidenceReference: "kfm:demo:site-local:v1", publicStatus: "PUBLIC_SAFE", sensitivityNote: "Public place names only.", releaseState: "DEMONSTRATION", correctionNote: "Not a gazetteer or municipal boundary source.", relatedLayers: ["Hydrology context", "Transportation"], interactions: ["cluster", "hover", "select", "search", "zoom"], filters: [], viewingModes: ["2D", "globe"], bounds: [-101.8, 37.6, -94.55, 39.45], sourceOptions: { cluster: true, clusterRadius: 54, clusterMaxZoom: 7 }, data: communitiesDemo,
    renderers: [
      point("communities-clusters", "kfm-communities", "#8fc8b0", 12, 0.9, ["has", "point_count"] as FilterSpecification),
      { id: "communities-count", baseFilter: ["has", "point_count"] as FilterSpecification, spec: { id: "communities-count", type: "symbol", source: "kfm-communities", filter: ["has", "point_count"], layout: { "text-field": ["get", "point_count_abbreviated"], "text-size": 11 }, paint: { "text-color": "#071719" } } },
      point("communities-points", "kfm-communities", "#f0f4e9", 5.5, 0.95, ["!", ["has", "point_count"]] as FilterSpecification),
    ],
  },
  {
    id: "transport-context", title: "Roads, rail & movement", description: "Generalized route context for system relationships, not navigation.", domain: "Transport", category: "Roads, rail & movement", sourceType: "GeoJSON", sourceId: "kfm-transport", datasetName: "KFM movement corridor fixture", geometryType: "LineString", minZoom: 5, maxZoom: 14, defaultVisibility: false, defaultOpacity: 0.75,
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

export const findLayerByRenderer = (rendererId: string) =>
  LAYER_REGISTRY.find((layer) => layer.renderers.some((renderer) => renderer.id === rendererId));
