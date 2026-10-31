import { CATEGORY_MAPS, type CategoryTool } from "./category-maps";
import { TOPIC_STRUCTURE, type LayerWorkspace, type TopicId } from "./layer-workspaces";

/** Discovery only: these entries navigate to existing owners, never fetch or enable data. */
export const CATEGORY_TOOL_DETAILS: Readonly<Record<CategoryTool, readonly [string, string]>> = {
  transect: ["Terrain cross-section", "Draw a line through elevation; display DEM, not a borehole survey."],
  flow: ["River flow effect", "Animate provider-directed reaches; display speed is not measured velocity."],
  underground: ["Underground · cores & wells", "Recorded columns and aquifer context; unobserved space stays unknown."],
  daylight: ["Daylight & twilight", "Calculated sun geometry and time playback, not cloud observations."],
  area: ["Measure a field or area", "Outline a polygon; a map measurement does not establish a legal boundary."],
  radar: ["Radar playback", "Step through timestamped NOAA scans with coverage gaps intact."],
  population: ["Population & change", "County Census counts, density columns and 2010–2020 change."],
  soil: ["Soil moisture · NASA SMAP", "Surface/root-zone model context at 9 km, not a field sample."],
  aquifer: ["Aquifer thickness & water depth", "Compare dated KGS High Plains classes, extents and legends."],
  reviewed: ["Reviewed snapshot history", "Browse eligible snapshots only when this site's store supplies them."],
  photoreal: ["Aerial terrain", "Kansas 2024 aerial imagery draped on the display DEM at true vertical scale."],
  quakes: ["Earthquake history", "Magnitude, depth and origin time from the USGS event catalogue."],
  outlook: ["Severe-weather outlook", "SPC forecast risk and probabilities, separate from observations."],
  reports: ["Storm reports", "Dated reported wind, hail and tornado events; reports are not warnings."],
  drought: ["Drought history & change", "Weekly U.S. Drought Monitor classes and county comparison since 2000."],
  flood: ["River flood forecasts", "NWS gauge-stage hydrographs; stage is not a mapped inundation extent."],
  fema: ["Disaster declaration history", "Kansas FEMA declarations since 1953, by county and hazard family."],
  rainfall: ["Rainfall estimates", "MRMS accumulations with product and duration controls; not field measurements."],
  landcover: ["Land-cover classes", "USGS NLCD 2021 classification at 30 m; inspect a point's class."],
  plants: ["Plant-record density", "GBIF annual coarse hexagons; records are not abundance or absence."],
  crops: ["Crops, soils & growing season", "USDA crop history, SSURGO soil, growing degree days, frost dates and season rain at a chosen point."],
  legislature: ["District plans", "Kansas Senate/House and U.S. congressional plans with separate dates."],
  tornadoes: ["Tornado record", "Filter reported paths by year and rating; historical reports are incomplete."],
  wells: ["Measured well levels", "Dated station readings; no continuous underground surface is inferred."],
  surface: ["Weather stations", "Temperature, wind and pressure at observing stations, not between them."],
  sunyear: ["Sun & Moon through the year", "Calculated daylight, twilight, lunar phases and a chosen Kansas location."],
};

export type CategoryWorkbench = Readonly<{ title: string; detail: string; href: string }>;
const lab = (title: string, detail: string, query = ""): CategoryWorkbench => ({ title, detail, href: `/observatory?panel=science${query ? `&q=${encodeURIComponent(query)}` : ""}` });
const imagery: CategoryWorkbench = { title: "Imagery recipes & availability", detail: "Satellite, climate and crop recipes; display requires an eligible installed package.", href: "/earth-engine" };
const sources: CategoryWorkbench = { title: "Source catalogue & methods", detail: "Check dates, units, coverage and limitations before combining products.", href: "/observatory/sources" };
const knowledge: CategoryWorkbench = { title: "Released knowledge search", detail: "Search only what the existing knowledge service makes available.", href: "/knowledge" };
export const CATEGORY_WORKBENCHES: Readonly<Record<TopicId, readonly CategoryWorkbench[]>> = {
  engineering: [lab("Elevation methods", "Relief, distance and bearing; paired surveys are needed for measured change.", "elevation")],
  transport: [lab("Roads & historical routes", "Present roads and historical route references have different evidence.", "roads")],
  aviation: [sources],
  weather: [lab("Science Lab · snow, storms & ice", "Station snow, storm context and archive-only ice records stay distinct."), imagery],
  disaster: [lab("Science Lab · hazard evidence", "Explore supported event clocks and unconnected hazard archives."), sources],
  water: [lab("Science Lab · water levels", "Discharge samples, intervals and gaps; not continuous basin flow.", "water-levels"), imagery],
  groundwater: [sources],
  geology: [lab("Surface geology & its legend", "Existing KGS surface map in the Observatory; edition/rights limits remain visible.", "geology"), lab("Resource-map symbols", "County aggregates of mapped symbols, not reserves or exact mine locations.", "resources")],
  terrain: [lab("Elevation & change methods", "No erosion surface is supplied without paired surveys and a method.", "elevation"), imagery],
  ecology: [lab("Vegetation occurrence context", "Dated coarse plant records are separate from land cover.", "foliage"), imagery],
  agriculture: [lab("Daily weather & snow records", "Station observations complement crop and soil context without becoming field measurements.", "snow"), imagery],
  flora: [lab("Science Lab · plant records", "Generalized occurrence context with source and sampling limits.", "foliage"), imagery],
  fauna: [lab("Generalized animal records", "The Observatory's existing coarse occurrence display; no exact sites or movement tracks.", "fauna"), sources],
  history: [{ title: "Historical accounts & availability", detail: "Research remains distinct from released people/event records.", href: "/history/people-events" }, { title: "Kansas history · 1909", detail: "Attributed original text and existing download choices.", href: "/history/prentis-1909" }],
  land: [knowledge, imagery],
  people: [{ title: "Civic atlas", detail: "Aggregate community context, not individual profiles.", href: "/civic" }, knowledge],
  government: [{ title: "Civic atlas & records", detail: "Jurisdictions, offices and official references; not endorsements.", href: "/civic" }],
  places: [knowledge],
  "public-safety": [sources],
  science: [lab("Science Lab · 18 phenomena", "Snow, ice, geology, resources, vegetation, wildlife and more, with availability by source."), imagery, sources],
  sky: [sources],
  evidence: [knowledge, sources, imagery],
};

export function categoryCapabilityMatches(title: string, detail: string, topic: TopicId, query: string): boolean {
  const definition = TOPIC_STRUCTURE.find(item => item.id === topic);
  const text = `${title} ${detail} ${definition?.title ?? ""}`.toLowerCase();
  return query.trim().toLowerCase().split(/\s+/).filter(Boolean).every(term => text.includes(term));
}

export function categoryCapabilityGroups(topic: LayerWorkspace, query: string) {
  return TOPIC_STRUCTURE.filter(item => topic === "all" || item.id === topic).map(item => ({
    topic: item.id, title: item.title,
    tools: (CATEGORY_MAPS[item.id].tools ?? []).filter(id => categoryCapabilityMatches(...CATEGORY_TOOL_DETAILS[id], item.id, query)),
    workbenches: CATEGORY_WORKBENCHES[item.id].filter(link => categoryCapabilityMatches(link.title, link.detail, item.id, query)),
  })).filter(group => group.tools.length || group.workbenches.length);
}
