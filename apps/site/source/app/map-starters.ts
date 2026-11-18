import type { OfficialContextId, OfficialContextSource } from "./live-context";
import { newMarkersActive } from "./kansas-discovery-layers";

/** Display grouping for the starter menu; a theme is navigation, never a source category. */
export const STARTER_THEMES = ["Water & ground", "Weather & hazards", "History & routes", "Outdoors & ecology", "Earth & survey", "Built & planning"] as const;
export type StarterTheme = typeof STARTER_THEMES[number];

/** UI recipes over the existing public-context allowlist, never an admission registry. */
export const MAP_STARTERS = [
  { id: "land-water", title: "Land & water", theme: "Water & ground", description: "For growers and land stewards: locate rivers, gauge observations and mapped High Plains aquifer extent.",
    ids: ["usgs-3dhp-hydrography", "usgs-streamflow", "kgs-aquifer-high-plains"],
    limitation: "Aquifer extent is not well yield or irrigation advice. Crop, soil and private land records require their own selection and review." },
  { id: "field-science", title: "Field science", theme: "Earth & survey", description: "Compare river observations, earthquake reports and watershed reference geography.",
    ids: ["usgs-streamflow", "usgs-earthquakes", "usgs-wbd-watersheds"],
    limitation: "Each observation has its own time, units and coverage. A watershed is not a measurement; missing observations remain unknown." },
  { id: "learning-kansas", title: "Learning Kansas", theme: "Earth & survey", description: "For classrooms and first visits: explore counties, river networks and shaded landforms.",
    ids: ["census-counties", "usgs-3dhp-hydrography", "usgs-3dep-hillshade"],
    limitation: "Population belongs to the Census edition; hillshade is a terrain display, not a survey. Sources may appear only at closer zoom." },
  { id: "historical-landscape", title: "Historical landscape", theme: "History & routes", description: "For historians and archaeological background research: compare the 1918 road map, abandoned rail references and county context.",
    ids: ["kdot-roads-1918", "kdot-rail-abandoned", "census-counties"],
    limitation: "Source editions differ. These references do not locate archaeological sites, establish past ownership or grant access to land." },
  { id: "infrastructure", title: "Infrastructure", theme: "Built & planning", guide: "kansas-bridges", description: "For infrastructure professionals: inspect road and state bridge references alongside mapped flood zones.",
    ids: ["kdot-roads", "kdot-bridges-state", "fema-flood-zones"],
    limitation: "Mapped records do not establish structural safety, current road conditions or design suitability. Flood zones are not a live warning." },
  { id: "community-planning", title: "Community planning", theme: "Built & planning", description: "For public agencies and communities: orient by county population, roads, watersheds and flood-zone context.",
    ids: ["census-counties", "kdot-roads", "usgs-wbd-watersheds", "fema-flood-zones"],
    limitation: "Reference boundaries have different purposes and dates. Area population does not identify individuals or establish property rights." },
  { id: "storm-watch", title: "Storm watch", theme: "Weather & hazards", guide: "storms-and-severe-weather", isNew: true, description: "For weather watchers: today's SPC severe-storm outlook, preliminary storm reports, active NWS alerts and past-24-hour radar rainfall.",
    ids: ["noaa-spc-convective-outlook", "nws-storm-reports", "nws-alerts", "noaa-mrms-qpe-24h"],
    limitation: "Outlooks are forecasts, reports are preliminary and rainfall is a radar estimate. This is not a warning service; follow NWS warnings and local officials." },
  { id: "rain-and-drought", title: "Rain & drought", theme: "Water & ground", guide: "drought-and-water", isNew: true, description: "For growers and water planners: compare recent radar rainfall, the 5-day rain forecast, the seasonal drought outlook and river observations.",
    ids: ["noaa-mrms-qpe-24h", "noaa-wpc-qpf-5day", "noaa-cpc-drought-outlook", "usgs-streamflow"],
    limitation: "Estimates, forecasts and outlooks run on different clocks. None is a gauge measurement, crop advice or a drought designation." },
  { id: "fire-season", title: "Fire season", theme: "Weather & hazards", guide: "fire-and-smoke", isNew: true, description: "For land managers and burn planners: the SPC fire-weather outlook beside satellite heat detections, interagency fire reports and smoke footprints.",
    ids: ["noaa-spc-fire-weather", "nasa-firms-active-fire", "nifc-fire-reports", "noaa-hms-smoke"],
    limitation: "Fire-weather outlooks are forecasts; heat detections and reports do not confirm the same incident. Check county burn restrictions and red-flag warnings." },
  { id: "heritage-trail", title: "Heritage trail", theme: "History & routes", guide: "historic-places", isNew: true, description: "For history explorers: click National Register places and historic bridges, then follow 1918 roads and abandoned railroads across Kansas.",
    ids: ["nps-nrhp-places", "kdot-roads-1918", "kdot-bridges-historic", "kdot-rail-abandoned"],
    limitation: "Listed places are representative public points; sensitive sites are withheld by NPS. Listing does not grant access or confirm a property still stands." },
  { id: "trails-west", title: "Trails west", theme: "History & routes", guide: "frontier-trails", isNew: true, description: "For history explorers and travelers: follow the Santa Fe, Oregon and Pony Express trails and the cattle trails across Kansas, with forts, crossings and ruts along the way and the rivers and terrain they crossed.",
    ids: ["nps-historic-trails", "nps-trail-places", "usgs-3dhp-hydrography", "usgs-3dep-hillshade"],
    limitation: "Trail lines are approximate NPS alignments and mostly cross private land; a line is not public access. Cattle-trail routes are study routes, not designated trails." },
  { id: "open-lands", title: "Land cover & open lands", theme: "Outdoors & ecology", guide: "land-cover-and-public-lands", isNew: true, description: "For naturalists and outdoor planners: read 2021 land cover, public and protected lands, and watershed boundaries together.",
    ids: ["mrlc-nlcd-land-cover", "usgs-padus-lands", "usgs-wbd-watersheds"],
    limitation: "Land-cover classes have mapping error and PAD-US does not grant access, hunting permission or title. Check each managing agency's rules." },
  { id: "beneath-the-plains", title: "Beneath the plains", theme: "Water & ground", guide: "aquifers-and-groundwater", isNew: true, description: "For water planners and students: read the High Plains aquifer extent with KGS saturated thickness, depth to water and the wells that are measured.",
    ids: ["kgs-aquifer-high-plains", "kgs-saturated-thickness", "kgs-depth-to-water", "kgs-monitoring-wells"],
    limitation: "Thickness and depth classes are regional 2022–2024 estimates from measured wells, not parcel measurements, current well levels or pumping advice." },
  { id: "shaking-ground", title: "Shaking ground", theme: "Earth & survey", guide: "earthquakes-in-kansas", isNew: true, description: "For curious neighbours and teachers: recent USGS earthquake reports beside community seismometers and shaded terrain.",
    ids: ["usgs-earthquakes", "raspberry-shake-stations", "usgs-3dep-hillshade"],
    limitation: "Earthquake locations and magnitudes are revised by USGS. A station marker is not a measurement, and terrain does not show faults or explain a cause." },
  { id: "river-flood-watch", title: "River & flood watch", theme: "Water & ground", guide: "rivers-and-floods", isNew: true, description: "For river towns and emergency planners: forecast gauges, modeled 18-hour river flow, radar rainfall and the mapped stream network.",
    ids: ["noaa-nwps-gauges", "noaa-nwm-short-range", "noaa-mrms-qpe-24h", "usgs-3dhp-hydrography"],
    limitation: "Gauge forecasts, model guidance and radar estimates are separate products on their own clocks. This is not a flood warning; follow NWS warnings and local officials." },
  { id: "survey-and-soil", title: "Survey lines & soils", theme: "Earth & survey", guide: "land-survey-and-soils", isNew: true, description: "For land professionals and researchers: PLSS townships and sections over NRCS soil map units, with county and population context.",
    ids: ["blm-plss-townships", "blm-plss-sections", "nrcs-ssurgo-soils", "census-counties"],
    limitation: "Survey divisions and soil map units are references, not parcel boundaries, ownership, deeds or field soil tests. Sections and soils appear only at closer zoom." },
  { id: "roads-and-rails", title: "Roads & rails through time", theme: "History & routes", guide: "roads-and-railroads", isNew: true, description: "For history explorers: set the 1918 road map and abandoned railroads against today's highways and active rail lines.",
    ids: ["kdot-roads-1918", "kdot-rail-abandoned", "kdot-rail-active", "kdot-roads"],
    limitation: "Map editions differ in date, scale and accuracy. An abandoned line is not a public trail and a mapped road is not a current condition report." },
  { id: "lightning-and-sky", title: "Lightning & the sky", theme: "Weather & hazards", guide: "lightning-and-the-sky", isNew: true, description: "For weather watchers: the latest 15-minute lightning density, the long-term flash average, the radar loop and satellite imagery.",
    ids: ["noaa-lightning-density", "nasa-lightning-climatology", "nws-radar", "noaa-goes-geocolor"],
    limitation: "The 1995–2014 flash average is a historical composite, not today's storms. Radar and satellite frames are display context, not a lightning-safety service." },
  { id: "wild-kansas", title: "Wildlife & open country", theme: "Outdoors & ecology", guide: "hunting-and-wildlife-areas", isNew: true, description: "For naturalists and hunters: KDWP public wildlife areas with 2021 land cover, public and protected lands and the stream network.",
    ids: ["kdwp-wildlife-areas", "mrlc-nlcd-land-cover", "usgs-padus-lands", "usgs-3dhp-hydrography"],
    limitation: "Boundaries are simplified for display and land-cover classes are not species records. Check KDWP rules, seasons and closures before entering any area." },
  { id: "bridges-and-crossings", title: "Bridges & crossings", theme: "Built & planning", guide: "kansas-bridges", isNew: true, description: "For road users and engineers: state highway bridges and recorded closures as counted circles, with highways and the stream network they cross.",
    ids: ["kdot-bridges-state", "kdot-bridges-closed", "kdot-roads", "usgs-3dhp-hydrography"],
    limitation: "Bridge records are KDOT's inventory and may lag. A recorded status is not a live closure notice or a safety determination; follow posted signs and KDOT notices." },
  { id: "kansas-aquifers", title: "Aquifers beyond the High Plains", theme: "Water & ground", guide: "kansas-aquifers", isNew: true, description: "For water users and students: the river-valley alluvial, Dakota, Glacial Drift and Ozark aquifer extents mapped by the Kansas Geological Survey.",
    ids: ["kgs-aquifer-alluvial", "kgs-aquifer-dakota", "kgs-aquifer-glacial-drift", "kgs-aquifer-ozark"],
    limitation: "Extents are regional reference boundaries without a stated vintage. They can overlap at different depths and are not well yield, water rights or drilling advice." },
  { id: "old-bridges", title: "Bridges before 1950", theme: "History & routes", guide: "kansas-bridges", isNew: true, description: "For history explorers: local bridges with a recorded build year before 1950 and historic-designated bridges, beside the 1918 road map.",
    ids: ["kdot-bridges-old", "kdot-bridges-historic", "kdot-roads-1918"],
    limitation: "An age filter is not a historic designation, and a later rebuild may have changed a structure. Records may lag; a point is not public access or a safety finding." },
  { id: "declared-disasters", title: "Declared disasters & alerts", theme: "Weather & hazards", isNew: true, description: "For emergency planners: recent FEMA declaration counties beside active NWS alerts, today's severe-storm outlook and the National Water Model's high-flow analysis.",
    ids: ["fema-disaster-declarations", "nws-alerts", "noaa-spc-convective-outlook", "noaa-nwm-analysis"],
    limitation: "A declaration names counties, not a disaster footprint or current danger. Alerts, outlooks and model analyses are separate products; follow NWS warnings and local officials." },
  { id: "minerals-and-survey", title: "Federal mineral leases", theme: "Built & planning", isNew: true, description: "For land and energy researchers: BLM authorized and closed oil and gas lease cases on PLSS townships, with counties for orientation.",
    ids: ["blm-mlrs-leases-authorized", "blm-mlrs-leases-closed", "blm-plss-townships", "census-counties"],
    limitation: "Lease cases are geocoded from legal descriptions and are not exact lease or mineral-rights footprints, drilling activity, title or access. Leases appear only at closer zoom." },
  { id: "water-table-and-wells", title: "Water table & wells", theme: "Water & ground", guide: "aquifers-and-groundwater", isNew: true, description: "For water planners and students: the High Plains water-table elevation with the measured monitoring wells, the aquifer extent and watershed boundaries.",
    ids: ["kgs-aquifer-high-plains", "kgs-water-table", "kgs-monitoring-wells", "usgs-wbd-watersheds"],
    limitation: "Water-table classes are regional 2022–2024 estimates in feet above sea level, not current water levels, a precise head surface or pumping advice." },
  { id: "eastern-aquifers", title: "Eastern Kansas aquifers", theme: "Water & ground", guide: "kansas-aquifers", isNew: true, description: "For water users in eastern Kansas: the Osage, Flint Hills, Glacial Drift and Ozark aquifer extents mapped by the Kansas Geological Survey.",
    ids: ["kgs-aquifer-osage", "kgs-aquifer-flint-hills", "kgs-aquifer-glacial-drift", "kgs-aquifer-ozark"],
    limitation: "Extents are regional reference boundaries without a stated vintage. They can overlap at different depths and are not well yield, water rights or drilling advice." },
  { id: "slopes-and-landforms", title: "Slopes & landforms", theme: "Earth & survey", guide: "terrain-and-slope", isNew: true, description: "For hikers, teachers and land stewards: USGS 3DEP slope over shaded relief, with watersheds and counties for orientation.",
    ids: ["usgs-3dep-hillshade", "usgs-3dep-slope", "usgs-wbd-watersheds", "census-counties"],
    limitation: "Slope and shading are drawn from elevation data for display. They are not a site survey, an erosion or stability finding, or a trail rating. Slope appears from zoom 7." },
  { id: "fire-detections-up-close", title: "Fire detections up close", theme: "Weather & hazards", guide: "fire-and-smoke", isNew: true, description: "For land managers: clickable NOAA-20 heat detections over the daily thermal-anomaly image, smoke footprints and 2021 land cover.",
    ids: ["nasa-gibs-fire-points", "nasa-firms-active-fire", "noaa-hms-smoke", "mrlc-nlcd-land-cover"],
    limitation: "A heat detection is a satellite signal, not a confirmed wildfire; prescribed burns and flares also appear. Smoke outlines are not air-quality readings." },
  { id: "survey-divisions", title: "Survey divisions up close", theme: "Earth & survey", guide: "land-survey-and-soils", isNew: true, description: "For land professionals: PLSS sections and their intersected divisions, such as quarters and government lots, over soil map units and counties.",
    ids: ["blm-plss-sections", "blm-plss-intersected", "nrcs-ssurgo-soils", "census-counties"],
    limitation: "Divisions appear only from zoom 12 and are survey references, not parcels, deeds, ownership or access. Soil map units are not a field soil test." },
] as const satisfies readonly { id: string; title: string; theme: StarterTheme; guide?: string; description: string; ids: readonly OfficialContextId[]; limitation: string; isNew?: boolean }[];

export const DEFAULT_STARTER_ID = "learning-kansas";

/** A starter's "new" label follows the shared NEW-marker expiry. */
export const starterIsNew = (starter: object, now?: number) => "isNew" in starter && starter.isNew === true && newMarkersActive(now);

/** Starters grouped by theme in menu order; empty themes are omitted. */
export function startersByTheme() {
  return STARTER_THEMES.map(theme => ({ theme, starters: MAP_STARTERS.filter(starter => starter.theme === theme) }))
    .filter(group => group.starters.length > 0);
}

/** Pick a different starter for "Surprise me"; deterministic when a random source is injected. */
export function surpriseStarterId(current: string, random: () => number = Math.random): string {
  const choices = MAP_STARTERS.filter(starter => starter.id !== current);
  const index = Math.min(choices.length - 1, Math.max(0, Math.floor(random() * choices.length)));
  return choices[index]?.id ?? current;
}

export type StarterAccess = Readonly<{ held: boolean; unavailable: boolean; guidance?: string }>;
export type StarterAccessMap = Readonly<Partial<Record<OfficialContextId, StarterAccess>>>;
export type ContextSelection = Readonly<Partial<Record<OfficialContextId, boolean>>>;
const publicSources = (sources: readonly OfficialContextSource[]) => sources.filter(source => source.evidenceRole === "EXTERNAL_CONTEXT_ONLY" && source.layerIds.length > 0);

export function starterPlan(ids: readonly string[], sources: readonly OfficialContextSource[], access: StarterAccessMap) {
  const allowed = new Map(publicSources(sources).map(source => [source.id as string, source]));
  const selected: OfficialContextId[] = [];
  const skipped: { id: string; reason: string }[] = [];
  for (const id of new Set(ids)) {
    const source = allowed.get(id), status = source && access[source.id];
    if (!source || !status) skipped.push({ id, reason: "Unavailable in this Explorer" });
    else if (status.held) skipped.push({ id, reason: status.guidance ?? "Held by the current map time or representation" });
    else if (status.unavailable) skipped.push({ id, reason: "Unavailable · check the source card to retry" });
    else selected.push(source.id);
  }
  return { selected, skipped };
}

/** Deselect first; unchanged owners receive no calls and keep their request/cache state. */
export function contextSelectionChanges(ids: readonly OfficialContextId[], sources: readonly OfficialContextSource[], current: ContextSelection) {
  const wanted = new Set(ids);
  return publicSources(sources).flatMap(source => Boolean(current[source.id]) === wanted.has(source.id) ? [] : [{ id: source.id, visible: wanted.has(source.id) }])
    .sort((a, b) => Number(a.visible) - Number(b.visible));
}

export const CONTEXT_PREFERENCE_KEY = "kfm.public-context-selection.v1";
export function parseContextPreference(raw: string | null, sources: readonly OfficialContextSource[]): OfficialContextId[] | null {
  if (!raw || raw.length > 8000) return null;
  try {
    const value: unknown = JSON.parse(raw);
    if (!value || typeof value !== "object" || Array.isArray(value)) return null;
    const record = value as Record<string, unknown>;
    if (Object.keys(record).sort().join(",") !== "ids,version" || record.version !== 1 || !Array.isArray(record.ids)
      || record.ids.length > 100 || !record.ids.every(id => typeof id === "string" && id.length <= 100)
      || new Set(record.ids).size !== record.ids.length) return null;
    const allowed = new Set(publicSources(sources).map(source => source.id));
    return record.ids.filter((id): id is OfficialContextId => allowed.has(id as OfficialContextId));
  } catch { return null; }
}

export function readContextPreference(sources: readonly OfficialContextSource[]): OfficialContextId[] | null {
  try { return parseContextPreference(window.localStorage.getItem(CONTEXT_PREFERENCE_KEY), sources); } catch { return null; }
}

/** Explicit URL/tab-history selections, including an empty stack, take precedence. */
export function preferredContextIds(params: URLSearchParams, saved: readonly OfficialContextId[] | null): readonly string[] | null {
  return params.has("ctx") ? params.get("ctx")!.split(",") : saved;
}

export function writeContextPreference(ids: readonly string[] | null, sources: readonly OfficialContextSource[]): boolean {
  try {
    if (ids === null) window.localStorage.removeItem(CONTEXT_PREFERENCE_KEY);
    else {
      const allowed = new Set(publicSources(sources).map(source => source.id as string));
      const safeIds = [...new Set(ids)].filter(id => allowed.has(id));
      window.localStorage.setItem(CONTEXT_PREFERENCE_KEY, JSON.stringify({ version: 1, ids: safeIds }));
    }
    return true;
  } catch { return false; }
}
