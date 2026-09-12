import type { LayerRecord } from "./explorer-data";

export type MapUtilityView = "report" | "inspect" | "navigate" | "places" | "scene" | "connections" | "import" | "compare" | "display" | "measure" | "export" | "diagnostics";
export type MeasureUnit = "imperial" | "metric";

export type MapViewProfile = Readonly<{
  id: "overview" | "water" | "ecosystems" | "hazards" | "people-movement" | "smoke" | "elevation" | "time" | "history" | "trust";
  title: string;
  summary: string;
  visibleLayerIds: readonly string[];
  year: number;
  basemap: "standard" | "imagery" | "midnight" | "prairie" | "streets" | "topo";
  projection: "mercator" | "globe";
}>;

export const MAP_VIEW_PROFILES: readonly MapViewProfile[] = Object.freeze([
  Object.freeze({
    id: "overview",
    title: "Kansas overview",
    summary: "Real Census county boundaries and baseline counts, USGS stream observations, and mapped hydrography. Current sources refresh when you open the map.",
    visibleLayerIds: Object.freeze([]),
    year: new Date().getUTCFullYear(),
    basemap: "streets",
    projection: "mercator",
  }),
  Object.freeze({
    id: "water",
    title: "Water + places",
    summary: "Generalized local water context plus optional official USGS observations, 3DHP hydrography, WBD watersheds, and NOAA forecast/model context—each with its own role and clock.",
    visibleLayerIds: Object.freeze(["kansas-extent", "county-starter-points", "watershed-context", "water-context", "communities"]),
    year: 2026,
    basemap: "midnight",
    projection: "mercator",
  }),
  Object.freeze({
    id: "ecosystems",
    title: "Habitat + living systems",
    summary: "Habitat, fauna guild, flora community, prairie, and water concepts with sensitive occurrence detail excluded.",
    visibleLayerIds: Object.freeze(["kansas-extent", "county-starter-points", "watershed-context", "water-context", "prairie-context", "habitat-connectivity", "fauna-range-context", "flora-communities", "communities"]),
    year: 2026,
    basemap: "prairie",
    projection: "mercator",
  }),
  Object.freeze({
    id: "hazards",
    title: "Fire, smoke + hazards",
    summary: "Synthetic fire, smoke, and multi-hazard context beside water and settlements—never current conditions or life-safety guidance.",
    visibleLayerIds: Object.freeze(["kansas-extent", "county-starter-points", "watershed-context", "water-context", "smoke-context", "fire-context", "hazards-context", "communities"]),
    year: 2026,
    basemap: "midnight",
    projection: "mercator",
  }),
  Object.freeze({
    id: "people-movement",
    title: "People, movement + places",
    summary: "Aggregate-only people governance beside labeled settlements and distinct road and rail context; no person-level or genomic data.",
    visibleLayerIds: Object.freeze(["kansas-extent", "county-starter-points", "people-dna-context", "transport-context", "communities"]),
    year: 2026,
    basemap: "prairie",
    projection: "mercator",
  }),
  Object.freeze({
    id: "smoke",
    title: "Smoke context timeline",
    summary: "Synthetic, time-specific plume envelopes beside county, atmosphere, basin, and community context—not current conditions.",
    visibleLayerIds: Object.freeze(["kansas-extent", "county-starter-points", "watershed-context", "smoke-context", "atmosphere-observations", "communities"]),
    year: 2026,
    basemap: "midnight",
    projection: "mercator",
  }),
  Object.freeze({
    id: "elevation",
    title: "Elevation concept",
    summary: "Reversible relative-height extrusions with county, water, and watershed context; no DEM, terrain, or topographic claim.",
    visibleLayerIds: Object.freeze(["kansas-extent", "county-starter-points", "watershed-context", "water-context", "elevation-concept", "communities"]),
    year: 2026,
    basemap: "prairie",
    projection: "mercator",
  }),
  Object.freeze({
    id: "time",
    title: "Temporal lab",
    summary: "Exact-time atmosphere fixtures with county, place, and water context at the 2024 step.",
    visibleLayerIds: Object.freeze(["kansas-extent", "county-starter-points", "watershed-context", "water-context", "atmosphere-observations", "communities"]),
    year: 2024,
    basemap: "midnight",
    projection: "mercator",
  }),
  Object.freeze({
    id: "history",
    title: "Historical vintage",
    summary: "Through-time historical study lines beside county locators, generalized movement, and place context.",
    visibleLayerIds: Object.freeze(["kansas-extent", "county-starter-points", "historical-context", "transport-context", "communities"]),
    year: 1910,
    basemap: "prairie",
    projection: "mercator",
  }),
  Object.freeze({
    id: "trust",
    title: "Trust-state lab",
    summary: "Public-safe denial, restriction, error, correction, and county-locator demonstrations.",
    visibleLayerIds: Object.freeze(["kansas-extent", "county-starter-points", "public-safe-planning", "review-diagnostics", "atmosphere-observations"]),
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
  Object.freeze({ id: "consumer", label: "Repository Sites consumer", state: "NULL RUNTIME / HOLD", detail: "Current GitHub main fail-closes its repository mirror through NullMapRuntime. This separately deployed demonstration retains its site-local renderer without claiming repository conformance or readiness." }),
  Object.freeze({ id: "probes", label: "Browser readiness", state: "BOUNDED FIXTURE", detail: "A bounded real-browser fixture is recorded; broader authenticated, performance, CSP, PMTiles, terrain, accessibility, and long-session evidence remains held." }),
  Object.freeze({ id: "county-starters", label: "County starter coverage", state: "105 / 105", detail: "Every Kansas county has one source-referenced Census Gazetteer internal point for map entry, search, selection, Evidence Drawer inspection, and report scoping; these are locators, not boundaries or county claims." }),
]);

export const MAP_CAPABILITY_GATES = Object.freeze([
  Object.freeze({ id: "import", title: "External data admission", state: "HOLD", reason: "A browser preview cannot establish rights, provenance, sensitivity clearance, evidence binding, policy approval, or release state.", safeInterface: "No-upload KML / GeoJSON structure and geometry preview only" }),
  Object.freeze({ id: "terrain", title: "Terrain + hillshade", state: "CONTEXT ONLY", reason: "An attributed external Terrarium carrier supports reversible display; USGS 3DEP is cataloged separately and remains unadmitted.", safeInterface: "3D terrain and hillshade with explicit source links, 2D parity, and no reportable elevation claims" }),
  Object.freeze({ id: "compare", title: "Swipe compare", state: "HOLD", reason: "No aligned, independently supported, rights-cleared comparison pair is admitted.", safeInterface: "Separate A/B context requirements remain visible" }),
  Object.freeze({ id: "offline", title: "Offline / PMTiles", state: "HOLD", reason: "No admitted archive, ETag/range proof, release-scoped cache manifest, expiry, or correction path.", safeInterface: "Display-only readiness and source diagnostics" }),
  Object.freeze({ id: "live", title: "Governed live sources", state: "EXTERNAL CONTEXT", reason: "Fixed read-only USGS and NOAA adapters now expose bounded operational context, but that context is not admitted KFM evidence, a durable archive, or a warning service.", safeInterface: "Exact observations, provider forecasts, modeled guidance, retrieval times, provisional states, and visible gaps remain distinct" }),
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
