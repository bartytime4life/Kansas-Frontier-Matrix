import type { Feature, FeatureCollection, Point } from "geojson";

/** KDOT bridge inventory as map points. Site-only external context: these reads do not
 * acquire or release a KFM dataset, and a recorded value is not a safety determination. */
export type BridgeNetwork = "state" | "local";
export type BridgeFeedId = "kdot-bridges-state" | "kdot-bridges-local" | "kdot-bridges-historic" | "kdot-bridges-old" | "kdot-bridges-closed";
export type BridgeStatusClass = "open" | "posted" | "closed" | "other";
export type KdotBridge = Readonly<{
  id: string; network: BridgeNetwork; longitude: number; latitude: number;
  carries: string | null; crosses: string | null; location: string | null; county: string | null; structureId: string | null;
  built: number | null; rebuilt: number | null; material: string | null; design: string | null;
  lengthFt: number | null; spans: number | null; lanes: number | null; dailyTraffic: number | null; trafficYear: number | null;
  status: string | null; statusClass: BridgeStatusClass; loadPosting: string | null;
  historic: string | null; historicListed: boolean; sufficiency: number | null;
  deck: string | null; superstructure: string | null; substructure: string | null; culvert: string | null;
  inspected: string | null; owner: string | null;
}>;

const STRUCTURES = "https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Structures";
export const BRIDGE_NETWORKS = {
  state: { service: "State_Bridges", pageSize: 1000, maxPages: 10, label: "state highway", idPrefix: "kdot-state-",
    fields: "OBJECTID,STR_NAME,FACILITY,FEATINT,LOCATION,COUNTYNAME,BUILT_DATE,MATERIALMAIN,DESIGNMAIN,STR_LENGTH,LANES_CARRIED,STR_AADT,OPPOSTCL,SUF_RATE,OWNER,UNDER_CONSTRUCTION" },
  local: { service: "Non_State_Bridges", pageSize: 5000, maxPages: 6, label: "local road", idPrefix: "kdot-local-",
    fields: "OBJECTID,STRUCT_NUM,FACILITY,FEATINT,LOCATION,COUNTY,YEARBUILT,YEARRECON,MATERIALMAIN,DESIGNMAIN,LENGTH_ENG,MAINSPANS,LANES,ADTTOTAL,ADTYEAR,OPPOSTCL,POSTING,HISTSIGN,OWNER,SUFF_RATE,DKRATING,SUPRATING,SUBRATING,CULVRATING,INSPDATE" },
} as const;

/** The same record sets the earlier provider-drawn layers used. */
export const BRIDGE_FEEDS: Readonly<Record<BridgeFeedId, Readonly<{ network: BridgeNetwork; label: string; keep: (bridge: KdotBridge) => boolean }>>> = Object.freeze({
  "kdot-bridges-state": { network: "state", label: "state highway structures", keep: () => true },
  "kdot-bridges-local": { network: "local", label: "local road bridges", keep: () => true },
  "kdot-bridges-historic": { network: "local", label: "local road bridges recorded as National Register listed or eligible", keep: bridge => bridge.historicListed },
  "kdot-bridges-old": { network: "local", label: "local road bridges with a recorded build year before 1950", keep: bridge => bridge.built !== null && bridge.built < 1950 },
  "kdot-bridges-closed": { network: "local", label: "local road bridges recorded closed to all traffic", keep: bridge => bridge.statusClass === "closed" },
});
export const BRIDGE_FEED_IDS = Object.freeze(Object.keys(BRIDGE_FEEDS) as BridgeFeedId[]);
export const isBridgeFeed = (value: string): value is BridgeFeedId => Object.hasOwn(BRIDGE_FEEDS, value);

export function bridgeCountUrl(network: BridgeNetwork): string {
  const url = new URL(`${STRUCTURES}/${BRIDGE_NETWORKS[network].service}/MapServer/0/query`);
  url.search = new URLSearchParams({ f: "json", where: "1=1", returnCountOnly: "true" }).toString();
  return url.href;
}
export function bridgePageUrl(network: BridgeNetwork, page: number): string {
  const { service, pageSize, maxPages, fields } = BRIDGE_NETWORKS[network];
  if (!Number.isInteger(page) || page < 0 || page >= maxPages) throw new Error("Invalid bridge page.");
  const url = new URL(`${STRUCTURES}/${service}/MapServer/0/query`);
  url.search = new URLSearchParams({ f: "json", where: "1=1", outFields: fields, returnGeometry: "true", outSR: "4326", geometryPrecision: "5",
    orderByFields: "OBJECTID", resultOffset: String(page * pageSize), resultRecordCount: String(pageSize) }).toString();
  return url.href;
}
export function parseBridgeTotal(raw: unknown): number {
  const count = raw && typeof raw === "object" && !("error" in raw) ? (raw as { count?: unknown }).count : null;
  if (!Number.isSafeInteger(count) || (count as number) < 0) throw new Error("Invalid provider count.");
  return count as number;
}

const inKansas = (longitude: number, latitude: number) => longitude >= -102.06 && longitude <= -94.58 && latitude >= 36.99 && latitude <= 40.01;
const SMALL_WORDS = new Set(["OF", "TO", "AT", "ON", "IN", "THE", "AND", "OVER"]);
/** Provider text is mostly upper case. Words of three or more letters are title-cased;
 * route numbers, directions and abbreviations with digits or punctuation stay as recorded. */
export function tidyBridgeText(value: unknown, limit = 80): string | null {
  if (typeof value !== "string") return null;
  const words = value.replace(/[\u0000-\u001f\u007f<>]/g, " ").trim().split(/\s+/).filter(Boolean);
  if (!words.length) return null;
  const text = words.map((token, index) => {
    // Trailing punctuation ("RIVER," or "TRIB.") stays attached to its word.
    const [, word, tail] = /^([A-Z]+)([.,;:)]*)$/.exec(token) ?? [];
    if (!word) return token;
    if (SMALL_WORDS.has(word)) return (index === 0 ? word[0] + word.slice(1).toLowerCase() : word.toLowerCase()) + tail;
    return (word.length < 3 ? word : word[0] + word.slice(1).toLowerCase()) + tail;
  }).join(" ");
  return text.slice(0, limit);
}
const plain = (value: unknown, limit = 60): string | null => {
  // A leading ">" is a comparison in the provider's posting classes; say it in words before dropping angle brackets.
  const text = typeof value === "string" ? value.replace(/^\s*>\s*/, "More than ").replace(/[\u0000-\u001f\u007f<>]/g, " ").replace(/\s+/g, " ").trim() : "";
  return text && text !== "NA" ? text.slice(0, limit) : null;
};
const whole = (value: unknown, min: number, max: number): number | null => typeof value === "number" && Number.isFinite(value) && Math.round(value) >= min && Math.round(value) <= max ? Math.round(value) : null;
const decimal = (value: unknown, min: number, max: number): number | null => typeof value === "number" && Number.isFinite(value) && value >= min && value <= max ? Math.round(value * 10) / 10 : null;
const rating = (value: unknown): string | null => { const text = plain(value, 40); return text && !/^unknown/i.test(text) ? text : null; };
const statusClass = (status: string | null): BridgeStatusClass => {
  if (!status) return "other";
  if (/^closed/i.test(status)) return "closed";
  if (/^posted for|^weight$/i.test(status)) return "posted";
  return /^open|^new$|^posting recommended$/i.test(status) ? "open" : "other";
};

/** One provider page to validated records. Records without a usable point in Kansas are counted, not guessed. */
export function parseBridgePage(raw: unknown, network: BridgeNetwork, now = new Date()): { bridges: KdotBridge[]; skipped: number; received: number } {
  const body = raw as { error?: unknown; features?: unknown; geometryType?: unknown; spatialReference?: { wkid?: number; latestWkid?: number } } | null;
  if (!body || typeof body !== "object" || body.error || !Array.isArray(body.features) || body.features.length > BRIDGE_NETWORKS[network].pageSize
    || body.geometryType !== "esriGeometryPoint" || (body.spatialReference?.latestWkid ?? body.spatialReference?.wkid) !== 4326) throw new Error("Invalid provider response.");
  const thisYear = now.getUTCFullYear(), bridges: KdotBridge[] = []; let skipped = 0;
  for (const feature of body.features) {
    const item = feature as { attributes?: Record<string, unknown>; geometry?: { x?: unknown; y?: unknown } } | null;
    const a = item?.attributes, x = item?.geometry?.x, y = item?.geometry?.y;
    if (!a || typeof a.OBJECTID !== "number" || !Number.isSafeInteger(a.OBJECTID) || a.OBJECTID < 0 || typeof x !== "number" || typeof y !== "number" || !inKansas(x, y)) { skipped++; continue; }
    const state = network === "state";
    const status = state && a.UNDER_CONSTRUCTION === "Y" && a.OPPOSTCL === "New" ? "New · under construction" : plain(a.OPPOSTCL, 40);
    const historic = state ? null : plain(a.HISTSIGN, 40);
    const inspected = !state && typeof a.INSPDATE === "number" && a.INSPDATE >= Date.UTC(1950, 0, 1) && a.INSPDATE <= now.getTime() ? new Date(a.INSPDATE).toISOString().slice(0, 10) : null;
    bridges.push({
      id: `${BRIDGE_NETWORKS[network].idPrefix}${a.OBJECTID}`, network, longitude: x, latitude: y,
      carries: tidyBridgeText(a.FACILITY), crosses: tidyBridgeText(a.FEATINT), location: tidyBridgeText(a.LOCATION), county: tidyBridgeText(state ? a.COUNTYNAME : a.COUNTY, 40),
      structureId: plain(state ? a.STR_NAME : a.STRUCT_NUM, 24),
      built: whole(state ? a.BUILT_DATE : a.YEARBUILT, 1800, thisYear + 1), rebuilt: state ? null : whole(a.YEARRECON, 1800, thisYear + 1),
      material: plain(a.MATERIALMAIN, 40), design: plain(a.DESIGNMAIN, 40),
      lengthFt: decimal(state ? a.STR_LENGTH : a.LENGTH_ENG, 1, 60_000), spans: state ? null : whole(a.MAINSPANS, 1, 500),
      lanes: whole(state ? a.LANES_CARRIED : a.LANES, 1, 40), dailyTraffic: whole(state ? a.STR_AADT : a.ADTTOTAL, 1, 2_000_000), trafficYear: state ? null : whole(a.ADTYEAR, 1950, thisYear + 1),
      status, statusClass: statusClass(status), loadPosting: state ? null : plain(a.POSTING, 40),
      historic, historicListed: historic === "Br eligible for NRHP" || historic === "Br on Natl Reg Hist Place",
      sufficiency: decimal(state ? a.SUF_RATE : a.SUFF_RATE, 0, 100),
      deck: state ? null : rating(a.DKRATING), superstructure: state ? null : rating(a.SUPRATING), substructure: state ? null : rating(a.SUBRATING), culvert: state ? null : rating(a.CULVRATING),
      inspected, owner: plain(typeof a.OWNER === "string" ? a.OWNER.replace(/^[A-Z]{1,2}\d{0,2}\s+/, "") : a.OWNER, 60),
    });
  }
  return { bridges, skipped, received: body.features.length };
}

/** The slim map record: enough to place, colour, size, label and count a bridge. */
export function bridgeMapFeature(bridge: KdotBridge): Feature<Point> {
  const properties: Record<string, unknown> = { featureId: bridge.id, name: bridge.crosses ?? bridge.carries ?? "Bridge" };
  if (bridge.built !== null) properties.built = bridge.built;
  if (bridge.lengthFt !== null) properties.lengthFt = bridge.lengthFt;
  if (bridge.statusClass === "posted" || bridge.statusClass === "closed") properties.statusClass = bridge.statusClass;
  return { type: "Feature", geometry: { type: "Point", coordinates: [bridge.longitude, bridge.latitude] }, properties };
}
export function bridgeMapCollection(bridges: readonly KdotBridge[]): FeatureCollection<Point> {
  return { type: "FeatureCollection", features: bridges.map(bridgeMapFeature) };
}

export type BridgeHighlights = Readonly<{ longest: KdotBridge | null; busiest: KdotBridge | null; earliestBuilt: number | null; closed: number; posted: number; before1950: number }>;
export function bridgeHighlights(bridges: readonly KdotBridge[]): BridgeHighlights {
  let longest: KdotBridge | null = null, busiest: KdotBridge | null = null, earliestBuilt: number | null = null, closed = 0, posted = 0, before1950 = 0;
  for (const bridge of bridges) {
    if (bridge.lengthFt !== null && (!longest || bridge.lengthFt > longest.lengthFt!)) longest = bridge;
    if (bridge.dailyTraffic !== null && (!busiest || bridge.dailyTraffic > busiest.dailyTraffic!)) busiest = bridge;
    if (bridge.built !== null && (earliestBuilt === null || bridge.built < earliestBuilt)) earliestBuilt = bridge.built;
    if (bridge.built !== null && bridge.built < 1950) before1950++;
    if (bridge.statusClass === "closed") closed++; else if (bridge.statusClass === "posted") posted++;
  }
  return { longest, busiest, earliestBuilt, closed, posted, before1950 };
}
const feet = (value: number) => `${Math.round(value).toLocaleString("en-US")} ft`;
const describe = (bridge: KdotBridge) => [bridge.carries, bridge.crosses].filter(Boolean).join(" at ") || "an unnamed structure";
/** Plain-language facts about one record set, shown with the layer. */
export function bridgeSummary(feed: BridgeFeedId, bridges: readonly KdotBridge[], skipped: number, truncated: boolean): string {
  const h = bridgeHighlights(bridges), parts = [`${bridges.length.toLocaleString("en-US")} ${BRIDGE_FEEDS[feed].label} in KDOT's inventory.`];
  if (h.longest) parts.push(`Longest: ${describe(h.longest)}, ${feet(h.longest.lengthFt!)}${h.longest.county ? ` (${h.longest.county} County)` : ""}.`);
  if (h.busiest) parts.push(`Busiest: ${describe(h.busiest)}, about ${h.busiest.dailyTraffic!.toLocaleString("en-US")} vehicles a day.`);
  if (h.earliestBuilt !== null) parts.push(`Earliest recorded build year: ${h.earliestBuilt}; ${h.before1950.toLocaleString("en-US")} have a recorded year before 1950.`);
  if (feed !== "kdot-bridges-closed") parts.push(`${h.closed.toLocaleString("en-US")} recorded closed and ${h.posted.toLocaleString("en-US")} posted with a restriction.`);
  parts.push(`Numbered circles count the bridges in that area and split as you zoom in until each bridge sits at its recorded point.${skipped ? ` ${skipped} record${skipped === 1 ? "" : "s"} without a usable Kansas location ${skipped === 1 ? "is" : "are"} left out.` : ""}${truncated ? " The provider list was longer than this layer reads, so some bridges are missing." : ""} Recorded years, status and condition come from the provider's inventory and may lag; they are not a live closure feed, a safety determination or navigation advice.`);
  return parts.join(" ");
}

/** The full record for one selected bridge, as short readable values for the details panel. */
export function bridgeDetailProperties(bridge: KdotBridge, peers: BridgeHighlights, now = new Date()): Record<string, string> {
  const out: Record<string, string> = {};
  const put = (key: string, value: string | null | false | undefined) => { if (value) out[key] = value; };
  const age = bridge.built !== null ? now.getUTCFullYear() - bridge.built : null;
  put("name", [bridge.carries, bridge.crosses].filter(Boolean).join(" at ") || null);
  put("carries", bridge.carries); put("crosses", bridge.crosses); put("location", bridge.location); put("county", bridge.county);
  put("builtLabel", bridge.built !== null ? `${bridge.built}${age !== null && age > 0 ? ` · about ${age} year${age === 1 ? "" : "s"} ago` : ""}` : null);
  put("rebuilt", bridge.rebuilt !== null ? String(bridge.rebuilt) : null);
  put("structureType", [bridge.material, bridge.design].filter(Boolean).join(" · ") || null);
  put("lengthLabel", bridge.lengthFt !== null ? `${bridge.lengthFt.toLocaleString("en-US")} ft${bridge.spans ? ` · ${bridge.spans} main span${bridge.spans === 1 ? "" : "s"}` : ""}` : null);
  put("lanesLabel", bridge.lanes !== null ? `${bridge.lanes} lane${bridge.lanes === 1 ? "" : "s"}` : null);
  put("trafficLabel", bridge.dailyTraffic !== null ? `About ${bridge.dailyTraffic.toLocaleString("en-US")} vehicles a day${bridge.trafficYear ? ` (${bridge.trafficYear} count)` : ""}` : null);
  put("status", bridge.status); put("loadPosting", bridge.loadPosting); put("historic", bridge.historic);
  put("condition", [bridge.deck && `Deck ${bridge.deck}`, bridge.superstructure && `Superstructure ${bridge.superstructure}`, bridge.substructure && `Substructure ${bridge.substructure}`, bridge.culvert && `Culvert ${bridge.culvert}`].filter(Boolean).join(" · ") || null);
  put("sufficiencyLabel", bridge.sufficiency !== null ? `${bridge.sufficiency} of 100` : null);
  put("inspected", bridge.inspected); put("owner", bridge.owner); put("structureId", bridge.structureId);
  put("highlight", [peers.longest?.id === bridge.id && `Longest structure in KDOT's ${BRIDGE_NETWORKS[bridge.network].label} inventory`,
    peers.busiest?.id === bridge.id && `Busiest structure in KDOT's ${BRIDGE_NETWORKS[bridge.network].label} inventory`].filter(Boolean).join(" · ") || null);
  put("network", bridge.network === "state" ? "State highway system" : "Local road (county or city)");
  return out;
}

/** Colour by recorded build year; the map key and both circle layers use these stops. */
export const BRIDGE_ERA_STOPS: readonly Readonly<{ from: number; label: string; color: string }>[] = Object.freeze([
  { from: 0, label: "Before 1900", color: "#b3261e" },
  { from: 1900, label: "1900–1929", color: "#e2711d" },
  { from: 1930, label: "1930–1949", color: "#f2b632" },
  { from: 1950, label: "1950–1969", color: "#b5cc4c" },
  { from: 1970, label: "1970–1989", color: "#4fbf9f" },
  { from: 1990, label: "1990–2009", color: "#3d9be0" },
  { from: 2010, label: "2010 and later", color: "#8a7bea" },
]);
export const BRIDGE_UNKNOWN_ERA_COLOR = "#9aa5ad";
export const BRIDGE_CLOSED_COLOR = "#ff4d4d";
export const BRIDGE_POSTED_COLOR = "#ffb020";
/** Zoom past which every bridge is drawn at its own point. */
export const BRIDGE_CLUSTER_MAX_ZOOM = 13;
export const BRIDGE_CLUSTER_RADIUS = 46;

/** What a numbered circle stands for, from the totals MapLibre keeps for the cluster. */
export function bridgeClusterSummary(properties: unknown): { title: string; detail: string } | null {
  const p = properties as Record<string, unknown> | null;
  const count = p && typeof p.point_count === "number" && Number.isFinite(p.point_count) ? p.point_count : null;
  if (!p || !p.cluster || count === null || count < 2) return null;
  const number = (key: string) => typeof p[key] === "number" && Number.isFinite(p[key]) ? p[key] as number : 0;
  const earliest = number("earliest"), longest = number("longestFt"), closed = number("closed"), posted = number("posted");
  const facts = [earliest >= 1800 && earliest < 9999 ? `earliest recorded build year ${earliest}` : null, longest > 0 ? `longest ${Math.round(longest).toLocaleString("en-US")} ft` : null,
    closed > 0 ? `${closed.toLocaleString("en-US")} recorded closed` : null, posted > 0 ? `${posted.toLocaleString("en-US")} posted with a restriction` : null].filter(Boolean);
  return { title: `${count.toLocaleString("en-US")} bridges in this area`, detail: facts.length ? facts.join(" · ") : "Select to zoom in" };
}
