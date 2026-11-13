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
  { id: "drought-watch", title: "Drought & water", isNew: true, description: "For growers and water planners: set the seasonal drought outlook beside river observations and the High Plains aquifer extent.",
    ids: ["noaa-cpc-drought-outlook", "usgs-streamflow", "kgs-aquifer-high-plains"],
    limitation: "The drought outlook is a forecast of change, not current drought intensity or a designation. Gauges and aquifer extent are separate products on their own clocks." },
  { id: "fire-season", title: "Fire season", isNew: true, description: "For land managers and burn planners: the SPC fire-weather outlook beside satellite heat detections, interagency fire reports and smoke footprints.",
    ids: ["noaa-spc-fire-weather", "nasa-firms-active-fire", "nifc-fire-reports", "noaa-hms-smoke"],
    limitation: "Fire-weather outlooks are forecasts; heat detections and reports do not confirm the same incident. Check county burn restrictions and red-flag warnings." },
  { id: "heritage-trail", title: "Heritage trail", isNew: true, description: "For history explorers: click National Register places, then follow 1918 roads and historic bridges across Kansas counties.",
    ids: ["nps-nrhp-places", "kdot-roads-1918", "kdot-bridges-historic", "census-counties"],
    limitation: "Listed places are representative public points; sensitive sites are withheld by NPS. Listing does not grant access or confirm a property still stands." },
  { id: "open-lands", title: "Open lands & waters", isNew: true, description: "For naturalists and outdoor planners: read public and protected lands with river networks and watershed boundaries.",
    ids: ["usgs-padus-lands", "usgs-3dhp-hydrography", "usgs-wbd-watersheds"],
    limitation: "PAD-US does not grant access, hunting permission or title, and boundaries can be generalized. Check each managing agency's rules." },
] as const satisfies readonly { id: string; title: string; description: string; ids: readonly OfficialContextId[]; limitation: string; isNew?: boolean }[];

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

/** Recreate the local geology map's public context when no visitor selection exists. */
export const GEOLOGY_OPENING_CONTEXT_IDS = [
  "census-counties", "usgs-streamflow", "usgs-3dhp-hydrography",
  "nasa-gibs-fire-points", "nifc-fire-reports", "kgs-monitoring-wells",
  "usgs-earthquakes", "usgs-3dep-slope",
] as const satisfies readonly OfficialContextId[];

export function openingContextIds(params: URLSearchParams, saved: readonly OfficialContextId[] | null, topic: string): readonly string[] | null {
  return preferredContextIds(params, saved) ?? (topic === "geology" ? GEOLOGY_OPENING_CONTEXT_IDS : null);
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
