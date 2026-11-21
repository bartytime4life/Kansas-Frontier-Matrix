import type { FeatureCollection } from "geojson";
import { accessOverviewPoints, officialClusterSummary } from "./context-clusters";
import { BRIDGE_FEED_IDS, isBridgeFeed } from "./kdot-bridges";

/** The map's current extent in degrees. */
export type ViewBounds = Readonly<{ west: number; south: number; east: number; north: number }>;
/** What a counted layer holds inside the current view, in the words its numbered circles use. */
export type ViewTally = Readonly<{ count: number; total: number; title: string; detail: string; nearest: readonly [number, number] | null; highlights: readonly ViewHighlight[] }>;
/** One record in view worth going to: what the button says, where it is, and the zoom at which it stands apart from its neighbours. */
export type ViewHighlight = Readonly<{ label: string; center: readonly [number, number]; zoom: number }>;

const NOUNS: Readonly<Record<string, string>> = Object.freeze({
  "nps-nrhp-places": "National Register markers", "nps-trail-places": "trail sites", "kdwp-wiha-access": "walk-in hunting tracts",
});
const TRAILS = [["Santa Fe", "santaFe"], ["Oregon", "oregon"], ["California", "california"], ["Pony Express", "ponyExpress"]] as const;
const RESOURCE_TYPES: Readonly<Record<string, string>> = Object.freeze({ building: "buildings", district: "districts", site: "sites", structure: "structures", object: "objects" });
const COMPASS = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest"] as const;
const MILES_PER_DEGREE = 69.05;
/** Past these zooms a bridge or a Register marker is drawn on its own, and a hunting tract fills a useful part of the map. */
const BRIDGE_FOCUS_ZOOM = 14.5, PLACE_FOCUS_ZOOM = 13.5, TRACT_FOCUS_ZOOM = 12;

/** Layers drawn as numbered circles that split as the visitor zooms in. */
export const isCountedLayer = (contextId: string): boolean => isBridgeFeed(contextId) || Object.hasOwn(NOUNS, contextId);
/** Every counted layer, in the order the status bar lists them. */
export const COUNTED_LAYER_IDS: readonly string[] = Object.freeze([...BRIDGE_FEED_IDS, ...Object.keys(NOUNS)]);
/** Short names for the status bar, where several layers share one line. Three of the bridge layers are parts of the local list, so each is named. */
const SHORT_NOUNS: Readonly<Record<string, readonly [one: string, many: string]>> = Object.freeze({
  "kdot-bridges-state": ["state highway bridge", "state highway bridges"], "kdot-bridges-local": ["local bridge", "local bridges"],
  "kdot-bridges-historic": ["historic local bridge", "historic local bridges"], "kdot-bridges-old": ["pre-1950 local bridge", "pre-1950 local bridges"],
  "kdot-bridges-closed": ["closed local bridge", "closed local bridges"], "nps-nrhp-places": ["Register marker", "Register markers"],
  "nps-trail-places": ["trail site", "trail sites"], "kdwp-wiha-access": ["hunting tract", "hunting tracts"],
});
const BRIEF_LIMIT = 3;

const number = (value: unknown): number | null => typeof value === "number" && Number.isFinite(value) ? value : null;
const whole = (value: number) => Math.round(value).toLocaleString("en-US");

/** The records in view that stand out, kept while counting: a layer's oldest and longest bridge, its landmarks, its largest tract. */
type Standouts = { year: number; yearTies: number; yearAt: readonly [number, number] | null; length: number; lengthAt: readonly [number, number] | null;
  landmarks: number; landmarkAt: readonly [number, number] | null; acres: number; acresAt: readonly [number, number] | null };
const noStandouts = (): Standouts => ({ year: 9999, yearTies: 0, yearAt: null, length: 0, lengthAt: null, landmarks: 0, landmarkAt: null, acres: 0, acresAt: null });

function noteStandout(contextId: string, best: Standouts, p: Record<string, unknown>, at: readonly [number, number]) {
  if (isBridgeFeed(contextId)) {
    const built = number(p.built), length = number(p.lengthFt);
    // The same bounds the circles use for a believable recorded year.
    if (built !== null && built >= 1800 && built < 9999) {
      if (built < best.year) { best.year = built; best.yearTies = 1; best.yearAt = at; } else if (built === best.year) best.yearTies++;
    }
    if (length !== null && length > best.length) { best.length = length; best.lengthAt = at; }
  } else if (contextId === "nps-nrhp-places") {
    if (p.landmark === true) { best.landmarks++; best.landmarkAt ??= at; }
  } else if (contextId === "kdwp-wiha-access") {
    const acres = number(p.acres);
    if (acres !== null && acres > best.acres) { best.acres = acres; best.acresAt = at; }
  }
}

/** At most two buttons, in the order the facts are read. A tie is said to be a tie rather than called "the oldest". */
function standoutHighlights(best: Standouts): ViewHighlight[] {
  const highlights: ViewHighlight[] = [];
  if (best.yearAt) highlights.push({ center: best.yearAt, zoom: BRIDGE_FOCUS_ZOOM,
    label: best.yearTies === 1 ? `Show the oldest (${best.year})` : `Show one of ${best.yearTies.toLocaleString("en-US")} from ${best.year}` });
  if (best.lengthAt) highlights.push({ center: best.lengthAt, zoom: BRIDGE_FOCUS_ZOOM, label: `Show the longest (${whole(best.length)} ft)` });
  if (best.landmarkAt) highlights.push({ center: best.landmarkAt, zoom: PLACE_FOCUS_ZOOM,
    label: best.landmarks === 1 ? "Show the National Historic Landmark" : `Show one of ${best.landmarks.toLocaleString("en-US")} National Historic Landmarks` });
  if (best.acresAt) highlights.push({ center: best.acresAt, zoom: TRACT_FOCUS_ZOOM, label: `Show the largest tract (${whole(best.acres)} acres)` });
  return highlights.slice(0, 2);
}

/** Adds one record to the totals a numbered circle keeps for its layer, so a view reads the same way a circle does. */
function addRecord(contextId: string, totals: Record<string, number>, p: Record<string, unknown>) {
  const add = (key: string, by = 1) => { totals[key] = (totals[key] ?? 0) + by; };
  if (isBridgeFeed(contextId)) {
    const built = number(p.built), length = number(p.lengthFt);
    totals.earliest = Math.min(totals.earliest ?? 9999, built ?? 9999);
    totals.longestFt = Math.max(totals.longestFt ?? 0, length ?? 0);
    if (p.statusClass === "closed") add("closed"); else if (p.statusClass === "posted") add("posted");
  } else if (contextId === "nps-nrhp-places") {
    if (p.landmark === true) add("landmarks");
    const key = typeof p.resourceType === "string" ? RESOURCE_TYPES[p.resourceType] : undefined;
    if (key) add(key);
  } else if (contextId === "nps-trail-places") {
    if (p.certified === "NPS-certified trail site") add("certified");
    const trails = typeof p.trails === "string" ? p.trails : "";
    for (const [name, key] of TRAILS) if (trails.includes(name)) add(key);
  } else {
    add("acres", number(p.acres) ?? 0); add("archeryOnly", number(p.archeryOnly) ?? 0);
  }
}

/** Counts a counted layer's records inside the view and describes them. A hunting tract counts where the
 * middle of its outline falls. Returns null for other layers and for a layer with no located records. */
export function viewTally(contextId: string, data: FeatureCollection | null | undefined, bounds: ViewBounds): ViewTally | null {
  if (!isCountedLayer(contextId) || !data || ![bounds.west, bounds.south, bounds.east, bounds.north].every(Number.isFinite)) return null;
  const points = contextId === "kdwp-wiha-access" ? accessOverviewPoints(data) : data;
  const wraps = bounds.west > bounds.east, middleX = wraps ? bounds.west : (bounds.west + bounds.east) / 2, middleY = (bounds.south + bounds.north) / 2;
  const shrink = Math.cos(middleY * Math.PI / 180), totals: Record<string, number> = {}, best = noStandouts();
  let count = 0, total = 0, nearest: readonly [number, number] | null = null, nearestMiles = Infinity;
  for (const feature of points.features) {
    if (feature.geometry?.type !== "Point") continue;
    const [x, y] = feature.geometry.coordinates;
    if (!Number.isFinite(x) || !Number.isFinite(y)) continue;
    total++;
    if (y >= bounds.south && y <= bounds.north && (wraps ? x >= bounds.west || x <= bounds.east : x >= bounds.west && x <= bounds.east)) {
      count++; addRecord(contextId, totals, feature.properties ?? {}); noteStandout(contextId, best, feature.properties ?? {}, [x, y]);
    } else if (count === 0) {
      const miles = Math.hypot((x - middleX) * shrink, y - middleY) * MILES_PER_DEGREE;
      if (miles < nearestMiles) { nearestMiles = miles; nearest = [x, y]; }
    }
  }
  if (total === 0) return null;
  const noun = isBridgeFeed(contextId) ? "bridges" : NOUNS[contextId], all = total.toLocaleString("en-US");
  if (count === 0) {
    const [x, y] = nearest!, bearing = (Math.atan2((x - middleX) * shrink, y - middleY) * 180 / Math.PI + 360) % 360;
    const distance = nearestMiles < 10 ? `about ${Math.max(1, Math.round(nearestMiles))} mi` : `about ${(Math.round(nearestMiles / 5) * 5).toLocaleString("en-US")} mi`;
    return { count, total, highlights: [], title: `No ${noun} in this view`, detail: `The nearest of ${all} is ${distance} ${COMPASS[Math.round(bearing / 45) % 8]} of the middle of the map.`, nearest };
  }
  // The circles' own wording, fed this view's totals; it needs at least two records to speak of a group.
  const facts = count > 1 ? officialClusterSummary(contextId, { cluster: true, point_count: count, ...totals })?.detail : undefined;
  // With one record in view there is nothing to pick out.
  return { count, total, nearest: null, highlights: count > 1 ? standoutHighlights(best) : [],
    title: count === total ? `All ${all} ${noun} are in this view` : `${count.toLocaleString("en-US")} of ${all} ${noun} in this view`,
    detail: facts && facts !== "Select to zoom in" ? facts : "" };
}

/** One short line for the status bar: what each counted layer on the map holds in view. Empty when none is on. */
export function viewTallyBrief(counts: readonly Readonly<{ contextId: string; count: number }>[]): string {
  const known = counts.filter(entry => Object.hasOwn(SHORT_NOUNS, entry.contextId) && Number.isSafeInteger(entry.count) && entry.count >= 0);
  if (!known.length) return "";
  const parts = known.slice(0, BRIEF_LIMIT).map(({ contextId, count }) => {
    const [one, many] = SHORT_NOUNS[contextId];
    return count === 0 ? `no ${many}` : `${count.toLocaleString("en-US")} ${count === 1 ? one : many}`;
  });
  const more = known.length - BRIEF_LIMIT;
  return `In view: ${parts.join(" · ")}${more > 0 ? ` · +${more} more ${more === 1 ? "layer" : "layers"}` : ""}`;
}
