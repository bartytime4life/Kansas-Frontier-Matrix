import {
  LAYER_REGISTRY,
  SEARCH_INDEX,
  type LayerRecord,
  type SearchItem,
} from "./explorer-data";
import {
  COUNTY_STARTER_LAYER,
  COUNTY_STARTER_LAYER_ID,
} from "./county-starter-slice";
import { MAPLIBRE_PLUGIN_CONNECTIONS } from "./maplibre-plugin-connections";

export type MapUtilityView = "report" | "inspect" | "navigate" | "scene" | "connections" | "import" | "compare" | "display" | "measure" | "export" | "diagnostics";
export type MeasureUnit = "imperial" | "metric";

const countyStarterSearchItems: readonly SearchItem[] = Object.freeze([
  {
    id: `layer:${COUNTY_STARTER_LAYER.id}`,
    kind: "layer",
    title: COUNTY_STARTER_LAYER.title,
    subtitle: `${COUNTY_STARTER_LAYER.category} · ${COUNTY_STARTER_LAYER.datasetName}`,
    layerId: COUNTY_STARTER_LAYER.id,
  },
  ...COUNTY_STARTER_LAYER.data.features.map((item) => ({
    id: `feature:${item.properties.fid}`,
    kind: "feature" as const,
    title: item.properties.title,
    subtitle: `${COUNTY_STARTER_LAYER.title} · ${item.properties.fid}`,
    layerId: COUNTY_STARTER_LAYER.id,
    featureId: item.properties.fid,
    focus: [item.properties.focusLng, item.properties.focusLat] as [number, number],
  })),
]);

const registerCountyStarterSlice = () => {
  if (!LAYER_REGISTRY.some((layer) => layer.id === COUNTY_STARTER_LAYER.id)) {
    const extentIndex = LAYER_REGISTRY.findIndex((layer) => layer.id === "kansas-extent");
    LAYER_REGISTRY.splice(extentIndex >= 0 ? extentIndex + 1 : 0, 0, COUNTY_STARTER_LAYER);
  }

  if (!SEARCH_INDEX.some((item) => item.id === `layer:${COUNTY_STARTER_LAYER.id}`)) {
    SEARCH_INDEX.push(...countyStarterSearchItems);
  }
};

registerCountyStarterSlice();

export type MapViewProfile = Readonly<{
  id: "overview" | "water" | "smoke" | "elevation" | "time" | "history" | "trust";
  title: string;
  summary: string;
  visibleLayerIds: readonly string[];
  year: number;
  basemap: "midnight" | "prairie";
  projection: "mercator" | "globe";
}>;

export const MAP_VIEW_PROFILES: readonly MapViewProfile[] = Object.freeze([
  Object.freeze({
    id: "overview",
    title: "Kansas overview",
    summary: "County starter locators, generalized extent, hydrology, ecology, current temporal fixture, and places.",
    visibleLayerIds: Object.freeze(["kansas-extent", COUNTY_STARTER_LAYER_ID, "watershed-context", "water-context", "prairie-context", "atmosphere-observations", "communities"]),
    year: 2026,
    basemap: "midnight",
    projection: "mercator",
  }),
  Object.freeze({
    id: "water",
    title: "Water + places",
    summary: "Hydrology, county starter locators, and community context without implying monitoring or current conditions.",
    visibleLayerIds: Object.freeze(["kansas-extent", COUNTY_STARTER_LAYER_ID, "watershed-context", "water-context", "communities"]),
    year: 2026,
    basemap: "midnight",
    projection: "mercator",
  }),
  Object.freeze({
    id: "smoke",
    title: "Smoke context timeline",
    summary: "Synthetic, time-specific plume envelopes beside county, atmosphere, basin, and community context—not current conditions.",
    visibleLayerIds: Object.freeze(["kansas-extent", COUNTY_STARTER_LAYER_ID, "watershed-context", "smoke-context", "atmosphere-observations", "communities"]),
    year: 2026,
    basemap: "midnight",
    projection: "mercator",
  }),
  Object.freeze({
    id: "elevation",
    title: "Elevation concept",
    summary: "Reversible relative-height extrusions with county, water, and watershed context; no DEM, terrain, or topographic claim.",
    visibleLayerIds: Object.freeze(["kansas-extent", COUNTY_STARTER_LAYER_ID, "watershed-context", "water-context", "elevation-concept", "communities"]),
    year: 2026,
    basemap: "prairie",
    projection: "mercator",
  }),
  Object.freeze({
    id: "time",
    title: "Temporal lab",
    summary: "Exact-time atmosphere fixtures with county, place, and water context at the 2024 step.",
    visibleLayerIds: Object.freeze(["kansas-extent", COUNTY_STARTER_LAYER_ID, "watershed-context", "water-context", "atmosphere-observations", "communities"]),
    year: 2024,
    basemap: "midnight",
    projection: "mercator",
  }),
  Object.freeze({
    id: "history",
    title: "Historical vintage",
    summary: "Through-time historical study lines beside county locators, generalized movement, and place context.",
    visibleLayerIds: Object.freeze(["kansas-extent", COUNTY_STARTER_LAYER_ID, "historical-context", "transport-context", "communities"]),
    year: 1910,
    basemap: "prairie",
    projection: "mercator",
  }),
  Object.freeze({
    id: "trust",
    title: "Trust-state lab",
    summary: "Public-safe denial, restriction, error, correction, and county-locator demonstrations.",
    visibleLayerIds: Object.freeze(["kansas-extent", COUNTY_STARTER_LAYER_ID, "public-safe-planning", "review-diagnostics", "atmosphere-observations"]),
    year: 2026,
    basemap: "prairie",
    projection: "mercator",
  }),
]);

export const MAPLIBRE_REPOSITORY_STATUS = Object.freeze([
  Object.freeze({ id: "architecture", label: "Renderer architecture", state: "ACCEPTED", detail: "ADR-0006 and ADR-0007 accept one packages/maplibre adapter behind a KFM runtime port." }),
  Object.freeze({ id: "port", label: "MapRuntimePort + Null runtime", state: "VERIFIED SLICE", detail: "Current main proves a strict renderer-neutral port, deterministic no-network NullMapRuntime, and governed evidence binding." }),
  Object.freeze({ id: "dependency", label: "Dependency admission", state: "EXACT 6.6.0", detail: "The private @kfm/maplibre workspace package and pnpm lock admit exact maplibre-gl 6.6.0." }),
  Object.freeze({ id: "runtime", label: "Concrete MapLibre adapter", state: "VERIFIED SLICE", detail: "Current main implements a bounded package-owned lifecycle and camera adapter plus the Vite worker seam; broader production activation remains held." }),
  Object.freeze({ id: "consumer", label: "Sites renderer consumer", state: "NULL RUNTIME / HOLD", detail: "The Explorer imports the package-owned renderer-neutral surface and fail-closes through NullMapRuntime; full style, source, layer, interaction, and measurement migration remains held." }),
  Object.freeze({ id: "probes", label: "Browser readiness", state: "HOLD", detail: "The package retains a bounded historical fixture, but this fail-closed Sites consumer does not run renderer probes; authenticated, performance, CSP, PMTiles, terrain, accessibility, and long-session evidence remains held." }),
  Object.freeze({ id: "county-starters", label: "County starter coverage", state: "105 / 105", detail: "Every Kansas county has one source-referenced Census Gazetteer internal point for map entry, search, selection, evidence inspection, and report scoping; these points are locators, not boundaries or county claims." }),
  Object.freeze({ id: "plugin-registry", label: "MapLibre connection registry", state: `${MAPLIBRE_PLUGIN_CONNECTIONS.length} CANDIDATES`, detail: "Official MapLibre ecosystem candidates are ranked behind explicit KFM gates. The registry installs no runtime package, activates no live source, and creates no release or publication authority." }),
]);

const pluginCapabilityGates = MAPLIBRE_PLUGIN_CONNECTIONS.map((connection) => Object.freeze({
  id: `plugin-${connection.id}`,
  title: connection.title,
  state: connection.status.replaceAll("_", " "),
  reason: `${connection.reason} Gate: ${connection.gate}`,
  safeInterface: `${connection.connection}. Fallback: ${connection.fallback}`,
}));

export const MAP_CAPABILITY_GATES = Object.freeze([
  Object.freeze({ id: "import", title: "External data admission", state: "HOLD", reason: "A browser-local inspection cannot establish rights, provenance, sensitivity clearance, evidence binding, policy approval, or release state.", safeInterface: "No-upload KML / GeoJSON structure and geometry inspection only" }),
  Object.freeze({ id: "terrain", title: "Terrain + hillshade", state: "HOLD", reason: "No audited DEM, release-linked terrain manifest, rights closure, or evidence-parity 2D fallback.", safeInterface: "Synthetic extrusion concept only; real elevation carriers remain held" }),
  Object.freeze({ id: "compare", title: "Swipe compare", state: "HOLD", reason: "No aligned, independently supported, rights-cleared comparison pair is admitted.", safeInterface: "Separate A/B context requirements remain visible" }),
  Object.freeze({ id: "offline", title: "Offline / PMTiles", state: "HOLD", reason: "No admitted archive, ETag/range proof, release-scoped cache manifest, expiry, or correction path.", safeInterface: "Display-only readiness and source diagnostics" }),
  Object.freeze({ id: "live", title: "Governed live sources", state: "HOLD", reason: "No authenticated source adapter, freshness envelope, policy execution, or released public transport is proven.", safeInterface: "Site-local GeoJSON fixtures remain explicit" }),
  ...pluginCapabilityGates,
]);

export const isFeatureAvailableAtTime = (layer: Pick<LayerRecord, "temporal">, featureYear: number, activeYear: number) => {
  if (!layer.temporal) return true;
  if (layer.temporal.mode === "exact") return featureYear === activeYear;
  return featureYear <= activeYear;
};

export const isLayerAvailableAtTime = (layer: Pick<LayerRecord, "temporal">, activeYear: number) => {
  if (!layer.temporal) return true;
  if (layer.temporal.mode === "exact") return layer.temporal.years.includes(activeYear);
  return layer.temporal.years.some((candidateYear) => candidateYear <= activeYear);
};

export const inspectableFeatureId = (layer: LayerRecord, activeYear: number) => {
  const available = layer.data.features.filter((candidate) => isFeatureAvailableAtTime(layer, candidate.properties.year, activeYear));
  if (!available.length) return null;
  if (layer.temporal?.mode === "through") {
    return [...available].sort((left, right) => right.properties.year - left.properties.year)[0].properties.fid;
  }
  return available[0].properties.fid;
};
