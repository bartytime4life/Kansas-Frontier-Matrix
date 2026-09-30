import type { LayerRecord } from "./explorer-data";
import { BUILD_UTC_YEAR } from "./build-clock";

export type MapUtilityView = "report" | "inspect" | "navigate" | "scene" | "connections" | "import" | "compare" | "measure" | "export" | "diagnostics";
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
  Object.freeze({ id: "overview", title: "Kansas overview", summary: "Census county boundaries and baseline counts, USGS stream observations, and mapped hydrography.", visibleLayerIds: Object.freeze([]), year: BUILD_UTC_YEAR, basemap: "streets", projection: "mercator" }),
  Object.freeze({ id: "water", title: "Living waters", summary: "USGS observations and hydrography with WBD watersheds and NOAA context, each on its own source clock.", visibleLayerIds: Object.freeze([]), year: BUILD_UTC_YEAR, basemap: "midnight", projection: "mercator" }),
  Object.freeze({ id: "smoke", title: "Smoke context", summary: "NOAA HMS analyzed smoke footprints and observed radar frames with their source times.", visibleLayerIds: Object.freeze([]), year: BUILD_UTC_YEAR, basemap: "midnight", projection: "mercator" }),
  Object.freeze({ id: "elevation", title: "Terrain & landforms", summary: "Published elevation-derived terrain and USGS 3DEP display context with source limitations.", visibleLayerIds: Object.freeze([]), year: BUILD_UTC_YEAR, basemap: "prairie", projection: "mercator" }),
]);

export const MAPLIBRE_REPOSITORY_STATUS = Object.freeze([
  Object.freeze({ id: "architecture", label: "Renderer architecture", state: "ACCEPTED", detail: "ADR-0006 and ADR-0007 accept one packages/maplibre adapter behind a KFM runtime port." }),
  Object.freeze({ id: "port", label: "MapRuntimePort + Null runtime", state: "VERIFIED SLICE", detail: "Current main proves a strict renderer-neutral port, deterministic no-network NullMapRuntime, and governed evidence binding." }),
  Object.freeze({ id: "dependency", label: "Dependency compatibility", state: "SITE 6.9.0 / REPO 6.9.0", detail: "This Site and current repository main now pin exact maplibre-gl 6.9.0. Version alignment removes one compatibility gap; promotion remains held until the governed worker, style, interaction, performance, long-session, and rollback probes are complete." }),
  Object.freeze({ id: "runtime", label: "Concrete MapLibre adapter", state: "VERIFIED SLICE", detail: "Current main implements a bounded package-owned lifecycle and camera adapter plus the Vite worker seam; broader production activation remains held." }),
  Object.freeze({ id: "consumer", label: "Repository Sites consumer", state: "NULL RUNTIME / HOLD", detail: "Current GitHub main fail-closes its repository mirror through NullMapRuntime. This separately deployed Site retains its site-local renderer without claiming repository conformance or readiness." }),
  Object.freeze({ id: "probes", label: "Browser readiness", state: "BOUNDED FIXTURE", detail: "A bounded real-browser fixture is recorded; broader authenticated, performance, CSP, PMTiles, terrain, accessibility, and long-session evidence remains held." }),
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
