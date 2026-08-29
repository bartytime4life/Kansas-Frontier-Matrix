import type { LayerRecord } from "./explorer-data";

export type MapUtilityView = "report" | "inspect" | "navigate" | "scene" | "compare" | "display" | "measure" | "export" | "diagnostics";
export type MeasureUnit = "imperial" | "metric";

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
    summary: "Generalized extent, hydrology, ecology, current temporal fixture, and places.",
    visibleLayerIds: Object.freeze(["kansas-extent", "watershed-context", "water-context", "prairie-context", "atmosphere-observations", "communities"]),
    year: 2026,
    basemap: "midnight",
    projection: "mercator",
  }),
  Object.freeze({
    id: "water",
    title: "Water + places",
    summary: "Hydrology and community context without implying monitoring or current conditions.",
    visibleLayerIds: Object.freeze(["kansas-extent", "watershed-context", "water-context", "communities"]),
    year: 2026,
    basemap: "midnight",
    projection: "mercator",
  }),
  Object.freeze({
    id: "smoke",
    title: "Smoke context timeline",
    summary: "Synthetic, time-specific plume envelopes beside atmosphere, basin, and community context—not current conditions.",
    visibleLayerIds: Object.freeze(["kansas-extent", "watershed-context", "smoke-context", "atmosphere-observations", "communities"]),
    year: 2026,
    basemap: "midnight",
    projection: "mercator",
  }),
  Object.freeze({
    id: "elevation",
    title: "Elevation concept",
    summary: "Reversible relative-height extrusions with water and watershed context; no DEM, terrain, or topographic claim.",
    visibleLayerIds: Object.freeze(["kansas-extent", "watershed-context", "water-context", "elevation-concept", "communities"]),
    year: 2026,
    basemap: "prairie",
    projection: "mercator",
  }),
  Object.freeze({
    id: "time",
    title: "Temporal lab",
    summary: "Exact-time atmosphere fixtures with place and water context at the 2024 step.",
    visibleLayerIds: Object.freeze(["kansas-extent", "watershed-context", "water-context", "atmosphere-observations", "communities"]),
    year: 2024,
    basemap: "midnight",
    projection: "mercator",
  }),
  Object.freeze({
    id: "history",
    title: "Historical vintage",
    summary: "Through-time historical study lines beside generalized movement and place context.",
    visibleLayerIds: Object.freeze(["kansas-extent", "historical-context", "transport-context", "communities"]),
    year: 1910,
    basemap: "prairie",
    projection: "mercator",
  }),
  Object.freeze({
    id: "trust",
    title: "Trust-state lab",
    summary: "Public-safe denial, restriction, error, and correction demonstrations.",
    visibleLayerIds: Object.freeze(["kansas-extent", "public-safe-planning", "review-diagnostics", "atmosphere-observations"]),
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
]);

export const MAP_CAPABILITY_GATES = Object.freeze([
  Object.freeze({ id: "terrain", title: "Terrain + hillshade", state: "HOLD", reason: "No audited DEM, release-linked terrain manifest, rights closure, or evidence-parity 2D fallback.", safeInterface: "Synthetic extrusion concept only; real elevation carriers remain held" }),
  Object.freeze({ id: "compare", title: "Swipe compare", state: "HOLD", reason: "No aligned, independently supported, rights-cleared comparison pair is admitted.", safeInterface: "Separate A/B context requirements remain visible" }),
  Object.freeze({ id: "offline", title: "Offline / PMTiles", state: "HOLD", reason: "No admitted archive, ETag/range proof, release-scoped cache manifest, expiry, or correction path.", safeInterface: "Display-only readiness and source diagnostics" }),
  Object.freeze({ id: "live", title: "Governed live sources", state: "HOLD", reason: "No authenticated source adapter, freshness envelope, policy execution, or released public transport is proven.", safeInterface: "Site-local GeoJSON fixtures remain explicit" }),
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

