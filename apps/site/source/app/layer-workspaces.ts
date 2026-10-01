import type { OfficialContextId, OfficialContextSource } from "./live-context";

export type LayerWorkspace = "all" | "disaster" | "land";

export const DISASTER_SOURCE_IDS: readonly OfficialContextId[] = Object.freeze([
  "fema-disaster-declarations",
  "usgs-streamflow", "noaa-nwps-gauges", "noaa-nwm-analysis", "noaa-nwm-short-range",
  "usgs-earthquakes", "raspberry-shake-stations", "noaa-hms-smoke",
  "nasa-firms-active-fire", "nasa-gibs-fire-points", "nifc-fire-reports",
  "nws-alerts", "nws-radar", "noaa-goes-geocolor", "nws-forecast-wind",
  "noaa-lightning-density", "nasa-lightning-climatology",
]);
export const LAND_SOURCE_IDS: readonly OfficialContextId[] = Object.freeze([
  "blm-plss-townships", "blm-plss-sections", "blm-plss-intersected",
]);

/** These families remain visible as holds until an adapter and its geometry are verified. */
export const DISASTER_COVERAGE_HOLDS = Object.freeze([
  { title: "FEMA flood hazard areas", detail: "NFHL effective dates and zone meaning require a separate regulated-map adapter.", sourceUrl: "https://www.fema.gov/flood-maps/national-flood-hazard-layer" },
  { title: "NOAA Storm Events", detail: "Historical event points, county records, and reported impacts cannot share one footprint.", sourceUrl: "https://www.ncei.noaa.gov/access/storm-events-database/" },
  { title: "Drought and harmful algal blooms", detail: "Source-specific dates, scale, and waterbody extent remain to be validated.", sourceUrl: "https://www.drought.gov/states/kansas" },
]);

export function filterOfficialSources(
  sources: readonly OfficialContextSource[], workspace: LayerWorkspace, query: string,
): OfficialContextSource[] {
  const term = query.trim().toLowerCase();
  const ids = workspace === "disaster" ? new Set(DISASTER_SOURCE_IDS)
    : workspace === "land" ? new Set(LAND_SOURCE_IDS) : null;
  return sources.filter(source => (!ids || ids.has(source.id))
    && (!term || `${source.title} ${source.shortTitle} ${source.organization} ${source.domain}`.toLowerCase().includes(term)))
    .sort((a, b) => Number(b.defaultVisibility) - Number(a.defaultVisibility));
}
