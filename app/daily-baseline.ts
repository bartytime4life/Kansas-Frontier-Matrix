export const currentUtcDay = (now = new Date()) => now.toISOString().slice(0, 10);
export const currentDayStart = (now = new Date()) => `${currentUtcDay(now)}T00:00`;
export const latestSafeCursor = (now = new Date()) => new Date(now.getTime() - 60_000).toISOString();

// Real provider-backed starting stacks. Unsupported domains remain available
// for historical/source exploration, never filled with synthetic measurements.
// Counties are a subject (people), not a backdrop for every view, and the
// overview adds nothing: it is the Explorer's own uncluttered start.
export const BASELINE_STACKS: Record<string, readonly string[]> = {
  overview: [],
  water: ["usgs-streamflow", "usgs-3dhp-hydrography", "usgs-wbd-watersheds", "noaa-nwps-gauges"],
  hazards: ["usgs-earthquakes", "noaa-hms-smoke", "nws-alerts"],
  smoke: ["noaa-hms-smoke", "nws-radar"],
  elevation: ["usgs-3dep-hillshade"],
  ecosystems: ["usgs-wbd-watersheds"],
  "people-movement": ["census-counties"],
};
