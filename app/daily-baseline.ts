export const currentUtcDay = (now = new Date()) => now.toISOString().slice(0, 10);
export const currentDayStart = (now = new Date()) => `${currentUtcDay(now)}T00:00`;
export const latestSafeCursor = (now = new Date()) => new Date(now.getTime() - 60_000).toISOString();

// Real provider-backed starting stacks. Unsupported domains remain available
// for historical/source exploration, never filled with synthetic measurements.
export const BASELINE_STACKS: Record<string, readonly string[]> = {
  overview: ["census-counties", "usgs-streamflow", "usgs-3dhp-hydrography"],
  water: ["census-counties", "usgs-streamflow", "usgs-3dhp-hydrography", "usgs-wbd-watersheds", "noaa-nwps-gauges"],
  hazards: ["census-counties", "usgs-earthquakes", "noaa-hms-smoke", "nws-alerts"],
  smoke: ["census-counties", "noaa-hms-smoke", "nws-radar"],
  elevation: ["census-counties", "usgs-3dep-hillshade"],
  ecosystems: ["census-counties", "usgs-wbd-watersheds"],
  "people-movement": ["census-counties"],
};
