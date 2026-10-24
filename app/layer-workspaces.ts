import type { OfficialContextId, OfficialContextSource } from "./live-context";

export type LayerWorkspace = "groundwater" | "all" | "disaster" | "land" | "transport" | "water" | "terrain" | "places"
  | "engineering" | "science" | "weather" | "history" | "people" | "geology" | "ecology" | "agriculture" | "sky" | "evidence";
export type TopicId = Exclude<LayerWorkspace, "all">;
export type TopicGroup = "Built systems" | "Earth & environment" | "People & place" | "Research & reference";
export type TopicDefinition = Readonly<{
  id: TopicId; title: string; group: TopicGroup; description: string;
  facets: readonly string[]; limitation: string;
  resources: readonly Readonly<{ title: string; href: string }>[];
}>;

/** Application navigation only: subjects do not admit data or activate a domain lane. */
export const TOPIC_GROUPS: readonly TopicGroup[] = ["Built systems", "Earth & environment", "People & place", "Research & reference"];
export const TOPIC_STRUCTURE: readonly TopicDefinition[] = Object.freeze(([
  { id: "engineering", title: "Engineering & infrastructure", group: "Built systems", description: "Inspect the built landscape and the terrain and water context around it.", facets: ["Bridges & structures", "Survey & measurement", "Terrain & drainage"], limitation: "Recorded bridge status, map measurements and terrain context do not establish structural safety, design suitability or permission to access an asset.", resources: [{ title: "Measure on the map", href: "/?maptab=measure&mapui=open" }] },
  { id: "transport", title: "Transportation & movement", group: "Built systems", description: "Follow Kansas roads, rail corridors and bridge references across source editions.", facets: ["Roads & bridges", "Active & abandoned rail", "Historic networks"], limitation: "Source designations are not live traffic, train movement or proof of access. Missing routes are not inferred closed.", resources: [{ title: "Compare maps", href: "/?maptab=compare&mapui=open" }] },
  { id: "weather", title: "Weather & climate", group: "Earth & environment", description: "Compare observed weather, forecast guidance and climate summaries on their own clocks.", facets: ["Radar & satellite", "Wind & lightning", "Rainfall & climate"], limitation: "Observations, forecasts and historical composites are different products. A missing frame is not clear weather; these displays are not a warning service.", resources: [{ title: "Event Observatory", href: "/observatory" }] },
  { id: "disaster", title: "Hazards & disasters", group: "Earth & environment", description: "Inspect flood, fire, smoke, seismic and disaster-declaration context.", facets: ["Flooding", "Fire & smoke", "Seismic events", "Declared disasters"], limitation: "Declaration areas, hazard zones, detections and observations do not share one footprint and do not establish current safety.", resources: [{ title: "Event Observatory", href: "/observatory" }] },
  { id: "water", title: "Water & watersheds", group: "Earth & environment", description: "Connect station observations, rivers, watershed boundaries and modeled water guidance.", facets: ["River observations", "Hydrography & basins", "Water forecasts"], limitation: "A gauge reading does not establish flow across a river or basin. Modeled guidance remains separate from observations.", resources: [{ title: "Water observations in the Observatory", href: "/observatory" }] },
  { id: "groundwater", title: "Aquifers & groundwater", group: "Earth & environment", description: "Explore aquifer extents, High Plains maps and groundwater monitoring references.", facets: ["Aquifer extents", "Depth & thickness", "Monitoring wells"], limitation: "Overlays have different vintages and depth meanings. Well locations and aquifer extents do not establish underground flow or a continuous geological model.", resources: [{ title: "Inspect mapped records", href: "/?maptab=inspect&mapui=open" }] },
  { id: "geology", title: "Geology & subsurface", group: "Earth & environment", description: "Inspect source-bounded aquifers, seismic observations and elevation context.", facets: ["Subsurface context", "Seismic monitoring", "Landforms"], limitation: "These sources do not supply a continuous rock, cave or resource model. Unobserved subsurface space remains unknown.", resources: [{ title: "Inspect mapped records", href: "/?maptab=inspect&mapui=open" }] },
  { id: "terrain", title: "Terrain & elevation", group: "Earth & environment", description: "Read elevation mosaics, hillshade, slope and calculated daylight together.", facets: ["Elevation", "Slope & hillshade", "Light & shadow"], limitation: "Mixed acquisition dates and display exaggeration must remain visible. Hillshade and slope colors are not survey measurements.", resources: [{ title: "Terrain appearance", href: "/?maptab=scene&mapui=open" }] },
  { id: "ecology", title: "Ecology & land cover", group: "Earth & environment", description: "Use land-cover imagery and water networks as context for ecological questions.", facets: ["Vegetation & land cover", "Water corridors", "Landscape change"], limitation: "Land-cover classes and satellite composites do not prove species presence, habitat condition or critical-habitat status. No species inventory is connected here.", resources: [{ title: "Imagery catalogue", href: "/earth-engine" }] },
  { id: "agriculture", title: "Agriculture & soils", group: "Earth & environment", description: "Compare crop classes, soil-moisture context and rainfall products.", facets: ["Crops & land use", "Soil moisture", "Rainfall & drought"], limitation: "Crop classes do not establish ownership or current farming activity. Modeled soil moisture is separate from sampled soil and agronomic advice.", resources: [{ title: "Imagery catalogue", href: "/earth-engine" }] },
  { id: "history", title: "History & cultural context", group: "People & place", description: "Explore dated transportation maps, Census editions and attributed historical research.", facets: ["Historic maps & routes", "People & events", "Archives & accounts"], limitation: "A historical account or current survey overlay does not establish past ownership, identity or exact archaeological locations. Research entries remain distinct from released evidence.", resources: [{ title: "People & events research", href: "/history/people-events" }, { title: "Kansas history · 1909", href: "/history/prentis-1909" }, { title: "Historic map sheets", href: "/?maptab=history&mapui=open" }] },
  { id: "land", title: "Land ownership & purpose", group: "People & place", description: "Organize survey references, lease-case context, land use and soil information.", facets: ["Survey & cadastral reference", "Lease cases", "Land use & cover", "Ownership evidence"], limitation: "Land ownership instruments are not connected to this Explorer. PLSS divisions are survey references; matched BLM lease cases are not exact lease boundaries, deeds or proof of ownership. Unreleased records and private parcel detail stay off the map.", resources: [{ title: "Released knowledge search", href: "/knowledge" }] },
  { id: "people", title: "People & communities", group: "People & place", description: "Explore aggregate population and housing context alongside attributed people-and-event research.", facets: ["Population & housing", "Communities & places", "People & events"], limitation: "Census counts describe areas, not individuals. Historical research does not resolve living-person identity, ancestry, DNA or property ownership. Restricted personal detail remains unavailable.", resources: [{ title: "Government & civic atlas", href: "/civic" }, { title: "People & events research", href: "/history/people-events" }, { title: "Released knowledge search", href: "/knowledge" }] },
  { id: "places", title: "Places & boundaries", group: "People & place", description: "Orient by counties, survey divisions, watersheds and saved investigation places.", facets: ["Counties & communities", "Survey divisions", "Watershed boundaries"], limitation: "Reference geography has its own edition and purpose. County, watershed, survey and ownership boundaries are not interchangeable.", resources: [{ title: "Released place knowledge", href: "/knowledge" }] },
  { id: "science", title: "Science & observations", group: "Research & reference", description: "Browse measurements, remote sensing, calculated context and model products across disciplines.", facets: ["Observations & monitoring", "Remote sensing", "Models & methods"], limitation: "Grouping observations and models does not make them equivalent. Check method, units, time, uncertainty and evidence support before drawing a conclusion.", resources: [{ title: "Event Observatory", href: "/observatory" }, { title: "Source catalogue", href: "/observatory/sources" }] },
  { id: "sky", title: "Sky & solar context", group: "Research & reference", description: "Explore calculated daylight and the map’s astronomical presentation tools.", facets: ["Daylight & twilight", "Sun geometry", "Night-sky presentation"], limitation: "Daylight is calculated geometry, not observed cloud cover. Sky appearance is presentation and does not establish visibility or weather conditions.", resources: [{ title: "Sky appearance", href: "/?maptab=scene&mapui=open" }] },
  { id: "evidence", title: "Evidence & research tools", group: "Research & reference", description: "Organize source inspection, citations, comparison, reports and governance workflows.", facets: ["Sources & citations", "Time & comparison", "Rights & review", "Reports & correction"], limitation: "A tool’s presence or repository maturity label does not prove a live evidence service, approved dataset, release or publication.", resources: [{ title: "Released knowledge search", href: "/knowledge" }, { title: "Source catalogue", href: "/observatory/sources" }] },
] satisfies TopicDefinition[]).map(topic => Object.freeze({ ...topic, facets: Object.freeze(topic.facets), resources: Object.freeze(topic.resources) })));

export const topicDefinition = (id: LayerWorkspace) => TOPIC_STRUCTURE.find(topic => topic.id === id);
export function restoreTopic(value: string | null): LayerWorkspace {
  return TOPIC_STRUCTURE.some(topic => topic.id === value) ? value as TopicId : "all";
}
export const topicSearchText = (ids: readonly LayerWorkspace[]) => ids.map(id => {
  const topic = topicDefinition(id);
  return topic ? topic.title : "";
}).join(" ");
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
  ["all", "All topics"], ...TOPIC_STRUCTURE.map(topic => [topic.id, topic.title] as const),
]);

const weatherIds = ["nws-alerts", "nws-radar", "nws-forecast-wind", "noaa-goes-geocolor", "noaa-lightning-density", "nasa-lightning-climatology"];
const waterIds = ["usgs-streamflow", "noaa-nwps-gauges", "usgs-3dhp-hydrography", "usgs-wbd-watersheds", "noaa-nwm-analysis", "noaa-nwm-short-range"];
const terrainIds = ["usgs-3dep-hillshade", "usgs-3dep-slope"];
const seismicIds = ["usgs-earthquakes", "raspberry-shake-stations"];
const groundwaterIds = ["kgs-aquifer-alluvial", "kgs-aquifer-dakota", "kgs-aquifer-glacial-drift", "kgs-aquifer-high-plains", "kgs-aquifer-ozark", "kgs-aquifer-osage", "kgs-aquifer-flint-hills", "kgs-water-table", "kgs-saturated-thickness", "kgs-depth-to-water", "kgs-monitoring-wells"];
const historicalTransportIds = ["kdot-roads-1918", "kdot-rail-abandoned", "kdot-bridges-historic", "kdot-bridges-old", "kdot-bridges-closed"];

/** Source identity, rather than provider name or a broad domain string, determines membership. */
export function officialSourceTopics(id: string): readonly TopicId[] {
  const topics = new Set<TopicId>();
  if (DISASTER_SOURCE_IDS.includes(id as OfficialContextId)) topics.add("disaster");
  if (LAND_SOURCE_IDS.includes(id as OfficialContextId)) topics.add("land");
  if (TRANSPORT_SOURCE_IDS.includes(id as OfficialContextId)) { topics.add("transport"); topics.add("engineering"); }
  if (weatherIds.includes(id)) topics.add("weather");
  if (waterIds.includes(id)) topics.add("water");
  if (terrainIds.includes(id)) { topics.add("terrain"); topics.add("geology"); topics.add("engineering"); }
  if (id === "usgs-wbd-watersheds" || id === "usgs-3dhp-hydrography") { topics.add("places"); topics.add("ecology"); }
  if (id === "usgs-wbd-watersheds" || id === "usgs-3dhp-hydrography" || id === "fema-flood-zones") topics.add("engineering");
  if (groundwaterIds.includes(id)) { topics.add("groundwater"); topics.add("geology"); topics.add("water"); }
  if (seismicIds.includes(id)) topics.add("geology");
  if (["blm-plss-townships", "blm-plss-sections", "blm-plss-intersected"].includes(id)) { topics.add("places"); topics.add("engineering"); }
  if (id === "census-counties") { topics.add("places"); topics.add("people"); topics.add("history"); }
  if (historicalTransportIds.includes(id) || id === "fema-disaster-declarations" || id === "nasa-lightning-climatology" || id === "blm-mlrs-leases-closed") topics.add("history");
  if (weatherIds.includes(id) || waterIds.includes(id) || terrainIds.includes(id) || seismicIds.includes(id) || groundwaterIds.includes(id) || ["noaa-hms-smoke", "nasa-firms-active-fire", "nasa-gibs-fire-points"].includes(id)) topics.add("science");
  return Array.from(topics);
}

export function specialtyLayerTopics(id: string): readonly TopicId[] {
  if (id === "daylight") return ["terrain", "disaster", "science", "sky"];
  if (id === "soil" || id === "crop") return ["water", "land", "agriculture", "science"];
  if (id === "reviewed-water") return ["water", "science"];
  if (id === "reviewed-weather") return ["weather", "disaster", "water", "science"];
  if (id === "reviewed-soil") return ["agriculture", "water", "land", "science"];
  if (id === "reviewed-storm-events") return ["weather", "disaster", "history", "science"];
  if (id === "reviewed-earthquakes") return ["geology", "disaster", "science"];
  return [];
}

export const SPECIALTY_LAYER_CATALOG = Object.freeze([
  { id: "daylight", title: "Daylight & twilight" }, { id: "soil", title: "Soil moisture" },
  { id: "crop", title: "Soil moisture 1 km hybrid" }, { id: "reviewed-water", title: "Reviewed water stations" },
  { id: "reviewed-weather", title: "Reviewed daily weather" },
]);

export function registryLayerTopics(domain: string): readonly TopicId[] {
  const topics = new Set<TopicId>();
  if (/history|histor|archaeolog/i.test(domain)) topics.add("history");
  if (/people|communit|population/i.test(domain)) topics.add("people");
  if (/hydro|water/i.test(domain)) topics.add("water");
  if (/weather|atmospher|climat/i.test(domain)) topics.add("weather");
  if (/land|soil/i.test(domain)) topics.add("land");
  if (/geolog|subsurface/i.test(domain)) topics.add("geology");
  if (/flora|fauna|habitat|ecolog/i.test(domain)) topics.add("ecology");
  if (/agricultur/i.test(domain)) topics.add("agriculture");
  if (/road|rail|transport/i.test(domain)) topics.add("transport");
  if (/infrastruct|engineer/i.test(domain)) topics.add("engineering");
  if (/terrain|elevation/i.test(domain)) topics.add("terrain");
  if (/hazard|disaster/i.test(domain)) topics.add("disaster");
  if (/place|boundar|locator/i.test(domain) || topics.size === 0) topics.add("places");
  return Array.from(topics);
}

const atlasMembership: Readonly<Record<string, readonly TopicId[]>> = {
  "kansas-overview": ["places", "people", "water"], "county-atlas": ["places", "people", "history"],
  "terrain-landforms": ["terrain", "geology", "engineering", "science"], "living-waters": ["water", "ecology", "science"],
  "smoke-transport": ["disaster", "weather", "science"],
};
export const atlasViewTopics = (id: string): readonly TopicId[] => atlasMembership[id] ?? [];

const featureMembership: Readonly<Record<string, readonly TopicId[]>> = {
  "huc-crosswalk": ["water", "places", "science"], "air-quality": ["weather", "disaster", "science"],
  "environmental-cadence": ["weather", "science"], "ndvi-change": ["ecology", "agriculture", "science"],
  "anomaly-scorecard": ["science", "disaster"], "soil-change": ["agriculture", "land", "science"],
  "streamflow-qc": ["water", "science"], "layer-lineage": ["history"], "story-player": ["history", "people"],
  "consent-card": ["people", "land"], "redaction-preview": ["people", "land"], "reveal-session": ["people", "land"],
  "compare": ["science", "history"], "map-runtime": ["engineering"], "maplibre-runtime": ["engineering"],
};
/** Keep original feature maturity and owning area untouched; subjects are additional facets. */
export const featureTopics = (id: string): readonly TopicId[] => ["evidence", ...(featureMembership[id] ?? [])];
export function functionTopics(id: string): readonly TopicId[] {
  if (["timeline-scrub", "compare-releases", "compare", "story-node", "story", "correction"].includes(id)) return ["evidence", "history", "science"];
  if (["map-navigation", "explore", "feature-click", "legend-view", "diagnostics", "debug-proof-view"].includes(id)) return ["evidence", "engineering", "science"];
  return ["evidence"];
}

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
  return sources.filter(source => (workspace === "all" || officialSourceTopics(source.id).includes(workspace))
    && (!term || `${source.id} ${source.title} ${source.shortTitle} ${source.organization} ${source.domain} ${topicSearchText(officialSourceTopics(source.id))}`.toLowerCase().includes(term)))
    .sort((a, b) => Number(b.defaultVisibility) - Number(a.defaultVisibility));
}

/** The catalog is only a projection of existing owners. Never mount by these results. */
export type LayerBrowseView = "official" | "selected" | "local";

/** Serialize only catalogue navigation; source selection, camera and evidence keys stay untouched. */
export function serializeTopicSelection(params: URLSearchParams, topic: LayerWorkspace, view: LayerBrowseView): void {
  const boundedTopic = restoreTopic(topic);
  if (boundedTopic === "all") params.delete("topic");
  else params.set("topic", boundedTopic);
  if (view === "local") params.set("layerView", "imagery");
  else if (view === "selected") params.set("layerView", "selected");
  else params.delete("layerView");
}

export type LayerCatalogEntry = Readonly<{ id: string; title: string; keywords: string; topics: readonly LayerWorkspace[]; selected: boolean; imagery?: boolean }>;
export function layerEntryMatches(entry: LayerCatalogEntry, view: LayerBrowseView, topic: LayerWorkspace, query: string): boolean {
  const terms = query.trim().toLowerCase().split(/\s+/).filter(Boolean);
  return (view !== "selected" || entry.selected) && (view !== "local" || entry.imagery === true) && (view !== "official" || !entry.imagery)
    && (topic === "all" || entry.topics.includes(topic))
    && terms.every(term => `${entry.title} ${entry.keywords} ${entry.id} ${topicSearchText(entry.topics)}`.toLowerCase().includes(term));
}
export function selectedCatalogCount(entries: readonly LayerCatalogEntry[]): number {
  return new Set(entries.filter(entry => entry.selected).map(entry => entry.id)).size;
}
export function imageryTopics(id: string): readonly LayerWorkspace[] {
  if (id === "ee-3dep") return ["terrain", "geology", "engineering", "science"];
  if (/^ee-(chirps|prism-monthly|prism-daily|terraclimate)$/.test(id)) return ["water", "weather", "disaster", "agriculture", "science"];
  if (id === "ee-cdl") return ["land", "agriculture", "ecology", "science"];
  if (/^ee-(sentinel2|landsat[45789])$/.test(id)) return ["land", "ecology", "science", "history"];
  return [];
}
