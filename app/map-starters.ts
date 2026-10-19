import type { OfficialContextId, OfficialContextSource } from "./live-context";

/** UI recipes over the existing public-context allowlist, never an admission registry. */
export const MAP_STARTERS = [
  { id: "land-water", title: "Land & water", description: "For growers and land stewards: locate rivers, gauge observations and mapped High Plains aquifer extent.",
    ids: ["usgs-3dhp-hydrography", "usgs-streamflow", "kgs-aquifer-high-plains"],
    limitation: "Aquifer extent is not well yield or irrigation advice. Crop, soil and private land records require their own selection and review." },
  { id: "field-science", title: "Field science", description: "Compare river observations, earthquake reports and watershed reference geography.",
    ids: ["usgs-streamflow", "usgs-earthquakes", "usgs-wbd-watersheds"],
    limitation: "Each observation has its own time, units and coverage. A watershed is not a measurement; missing observations remain unknown." },
  { id: "learning-kansas", title: "Learning Kansas", description: "For classrooms and first visits: explore counties, river networks and shaded landforms.",
    ids: ["census-counties", "usgs-3dhp-hydrography", "usgs-3dep-hillshade"],
    limitation: "Population belongs to the Census edition; hillshade is a terrain display, not a survey. Sources may appear only at closer zoom." },
  { id: "historical-landscape", title: "Historical landscape", description: "For historians and archaeological background research: compare the 1918 road map, abandoned rail references and county context.",
    ids: ["kdot-roads-1918", "kdot-rail-abandoned", "census-counties"],
    limitation: "Source editions differ. These references do not locate archaeological sites, establish past ownership or grant access to land." },
  { id: "infrastructure", title: "Infrastructure", description: "For infrastructure professionals: inspect road and state bridge references alongside mapped flood zones.",
    ids: ["kdot-roads", "kdot-bridges-state", "fema-flood-zones"],
    limitation: "Mapped records do not establish structural safety, current road conditions or design suitability. Flood zones are not a live warning." },
  { id: "community-planning", title: "Community planning", description: "For public agencies and communities: orient by county population, roads, watersheds and flood-zone context.",
    ids: ["census-counties", "kdot-roads", "usgs-wbd-watersheds", "fema-flood-zones"],
    limitation: "Reference boundaries have different purposes and dates. Area population does not identify individuals or establish property rights." },
] as const satisfies readonly { id: string; title: string; description: string; ids: readonly OfficialContextId[]; limitation: string }[];

/** Conversation entry points, not source coverage, admission, or release authority. */
export type AtlasMission = Readonly<{
  id: string;
  title: string;
  question: string;
  starterId?: (typeof MAP_STARTERS)[number]["id"];
  kind?: "demo";
}>;
export type AtlasMissionGroup = Readonly<{ id: string; title: string; description: string; missions: readonly AtlasMission[] }>;
export const ATLAS_MISSION_GROUPS: readonly AtlasMissionGroup[] = [
  { id: "work-learning", title: "Work & learning", description: "Starting questions for your work, classroom or research.", missions: [
    { id: "farming", title: "Farming & land stewardship", starterId: "land-water", question: "Find available water, land and aquifer source context for this place. Show the dates and limits relevant to farming." },
    { id: "science", title: "Science & research", starterId: "field-science", question: "Find available observations and reference layers for a scientific investigation of this place. Separate measurements from context." },
    { id: "government", title: "Government officials & workers", starterId: "community-planning", question: "Find available county, roads, watershed and flood-zone context for public-service planning here. Explain gaps and source dates." },
    { id: "education", title: "Education & classrooms", starterId: "learning-kansas", question: "Help me build a classroom investigation of this Kansas place using available sources, their dates and limitations." },
    { id: "business", title: "Business", question: "Find available public sources that could support a business investigation of this place. Explain which questions the indexed records cannot answer." },
  ] },
  { id: "weather-living", title: "Weather, wildlife & resources", description: "Explore the environment while respecting source coverage and sensitive locations.", missions: [
    { id: "weather", title: "Weather & water", question: "Find available weather and water sources for this place. Separate observations, forecasts and historical context, with actual timestamps." },
    { id: "fauna", title: "Fauna & wildlife", question: "Find public-safe wildlife source coverage for this place. Explain gaps and avoid precise sensitive species locations." },
    { id: "flora", title: "Flora & plants", question: "Find public-safe plant and landcover source coverage for this place, with dates, scale and limits." },
    { id: "resources", title: "Natural resources", starterId: "land-water", question: "Find available natural-resource and water context for this place. Explain what the mapped sources support and what remains unknown." },
    { id: "hunting", title: "Hunting & outdoor context", question: "Find available public-safe outdoor and wildlife source context for this place. Do not infer hunting permission, access rights or current regulations from a map." },
  ] },
  { id: "history-heritage", title: "History & heritage", description: "Follow dated evidence without revealing protected places or implying land rights.", missions: [
    { id: "history", title: "History", starterId: "historical-landscape", question: "Find dated historical road, rail and county context for this place. Identify the actual source editions and evidence gaps." },
    { id: "archaeology", title: "Archaeology", starterId: "historical-landscape", question: "Find safe historical landscape context for an archaeological background investigation here. Do not reveal protected sites or infer access permission." },
    { id: "tribal", title: "Tribal lands & context", question: "Find available authoritative, public-safe tribal context for this place. Distinguish historical references from current sovereignty, jurisdiction and access rights; withhold uncertain sensitive details." },
  ] },
  { id: "networks-projects", title: "Networks & public projects", description: "Reference geography for movement, infrastructure and public work.", missions: [
    { id: "roads", title: "Roads & bridges", starterId: "infrastructure", question: "Find available road and bridge reference sources for this place, with dates and limits. Do not infer current safety or road conditions." },
    { id: "rail", title: "Rail", starterId: "historical-landscape", question: "Find available rail source context for this place. Distinguish historical or abandoned references from current operations." },
    { id: "aviation", title: "Air traffic & aviation", question: "Check whether governed aviation or air-traffic sources are indexed for this place. Report actual coverage, timestamps and gaps rather than inventing live traffic." },
    { id: "utilities", title: "Public utilities", question: "Check available public-safe utility context for this place. Do not expose protected infrastructure detail or infer service reliability." },
    { id: "projects", title: "Public projects", question: "Find indexed public-project sources for this place. Separate proposals, approvals and completed work using the dates and authority of each source." },
  ] },
  { id: "culture-economy", title: "Culture, news & economy", description: "Ask what is indexed before relying on current-event or economic claims.", missions: [
    { id: "entertainment", title: "Entertainment & local stories", question: "Find available public sources about cultural activities and local stories for this place. Verify dates and availability before presenting events as current." },
    { id: "news", title: "News & current events", question: "Check which dated news or public updates are indexed for this place. Cite their sources and distinguish publication date from event date." },
    { id: "money", title: "Money & economy", question: "Find available population, income and economic source context for this place. Explain editions, geographic scale and uncertainty without giving personalized financial advice." },
  ] },
  { id: "demonstrations", title: "Demos & guided exploration", description: "Understand an example before treating it as an operational capability.", missions: [
    { id: "demos", title: "Demos", kind: "demo", question: "Which demonstrations and guided exploration workflows are available here? Label synthetic examples, distinguish implemented behavior from proposals, and explain their limits." },
  ] },
];

export function atlasMissionAvailability(mission: AtlasMission): string {
  if (mission.kind === "demo") return "Demo discovery · not operational evidence";
  return mission.starterId ? "Existing context recipe · review source availability" : "No bundled layer set · check search coverage";
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
