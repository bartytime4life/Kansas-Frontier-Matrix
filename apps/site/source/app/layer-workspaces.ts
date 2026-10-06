import type { OfficialContextId, OfficialContextSource } from "./live-context";

export type LayerWorkspace = "groundwater" | "all" | "disaster" | "land" | "transport";
export type CatalogFilter = "all" | "selected" | "attention";
export type CatalogStatus = Readonly<{ selected: boolean; held: boolean; state: string; canDisplay: boolean }>;

export function catalogDisplayStatus(status: CatalogStatus): string {
  if (!status.selected) return "Not selected";
  if (status.held) return "Held";
  if (status.state === "error") return "Unavailable";
  if (status.state === "loading") return "Loading";
  if (status.state === "empty") return "Selected · no features in response";
  if (!status.canDisplay) return "Selected · not displayed";
  if (status.state === "partial") return "Displayed · partial response";
  return status.state === "ready" ? "Displayed" : "Selected";
}

/** Catalog filtering is a projection; it never writes visibility. */
export function catalogFilterMatches(filter: CatalogFilter, status: CatalogStatus): boolean {
  return filter === "all" || filter === "selected" && status.selected
    || filter === "attention" && status.selected && (status.held || !status.canDisplay || ["error", "partial", "empty"].includes(status.state));
}

export const DISASTER_SOURCE_IDS: readonly OfficialContextId[] = Object.freeze([
  "fema-disaster-declarations", "fema-flood-zones",
  "usgs-streamflow", "noaa-nwps-gauges", "noaa-nwm-analysis", "noaa-nwm-short-range",
  "usgs-earthquakes", "raspberry-shake-stations", "noaa-hms-smoke",
  "nasa-firms-active-fire", "nasa-gibs-fire-points", "nifc-fire-reports",
  "nws-alerts", "nws-radar", "noaa-goes-geocolor", "nws-forecast-wind",
  "noaa-lightning-density", "nasa-lightning-climatology",
]);
export const LAND_SOURCE_IDS: readonly OfficialContextId[] = Object.freeze([
  "blm-mlrs-leases-authorized", "blm-mlrs-leases-closed",
  "blm-plss-townships", "blm-plss-sections", "blm-plss-intersected",
]);

export const TRANSPORT_SOURCE_IDS: readonly OfficialContextId[] = Object.freeze(["kdot-bridges-state", "kdot-bridges-local", "kdot-bridges-historic", "kdot-bridges-old", "kdot-bridges-closed", "kdot-roads-1918", "kdot-roads", "kdot-rail-active", "kdot-rail-abandoned"]);

export const LAYER_WORKSPACES: readonly (readonly [LayerWorkspace, string])[] = Object.freeze([
  ["all", "All sources"], ["groundwater", "Aquifers & groundwater"], ["land", "BLM land records"], ["transport", "Roads, rail & bridges"], ["disaster", "Hazards"],
]);

export function sourceMinimumZoom(source: OfficialContextSource): number {
  return source.minDisplayZoom ?? (source.id === "usgs-3dep-hillshade" || source.id === "usgs-3dep-slope" ? 7 : 0);
}

export function sourceNeedsCloserView(source: OfficialContextSource, selected: boolean, held: boolean, state: string, zoom: number): boolean {
  return selected && !held && state !== "error" && zoom < sourceMinimumZoom(source);
}

/** These families remain visible as holds until an adapter and its geometry are verified. */
export const DISASTER_COVERAGE_HOLDS = Object.freeze([
  { title: "NOAA Storm Events", detail: "Historical event points, county records, and reported impacts cannot share one footprint.", sourceUrl: "https://www.ncei.noaa.gov/access/storm-events-database/" },
  { title: "Drought and harmful algal blooms", detail: "Source-specific dates, scale, and waterbody extent remain to be validated.", sourceUrl: "https://www.drought.gov/states/kansas" },
]);

export function filterOfficialSources(
  sources: readonly OfficialContextSource[], workspace: LayerWorkspace, query: string,
): OfficialContextSource[] {
  const term = query.trim().toLowerCase();
  const ids = workspace === "groundwater" ? new Set(sources.filter(source => source.id.startsWith("kgs-")).map(source => source.id)) : workspace === "disaster" ? new Set(DISASTER_SOURCE_IDS)
    : workspace === "land" ? new Set(LAND_SOURCE_IDS) : workspace === "transport" ? new Set(TRANSPORT_SOURCE_IDS) : null;
  return sources.filter(source => (!ids || ids.has(source.id))
    && (!term || `${source.id} ${source.title} ${source.shortTitle} ${source.organization} ${source.domain}`.toLowerCase().includes(term)))
    .sort((a, b) => Number(b.defaultVisibility) - Number(a.defaultVisibility));
}
