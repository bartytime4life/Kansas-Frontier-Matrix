import { readBoundedJson } from "../../bounded-json";
import { BRIDGE_FEEDS, BRIDGE_NETWORKS, bridgeCountUrl, bridgeDetailProperties, bridgeHighlights, bridgeMapCollection, bridgePageUrl, bridgeSummary,
  parseBridgePage, parseBridgeTotal, type BridgeFeedId, type BridgeHighlights, type BridgeNetwork, type KdotBridge } from "../../kdot-bridges";
import type { OfficialContextPayload } from "../../live-context";

// Fixed statewide inventory reads: no client coordinates, filters or provider URLs.
export const BRIDGE_CACHE_MS = 24 * 60 * 60_000;
const PAGE_BYTES = 6 * 1024 * 1024;
const PAGE_TIMEOUT_MS = 30_000;
const FAILURE_COOLDOWN_MS = 60_000;
const MAX_FAILURE_COOLDOWN_MS = 15 * 60_000;
const cooldownMs = (failures: number) => Math.min(MAX_FAILURE_COOLDOWN_MS, FAILURE_COOLDOWN_MS * 2 ** Math.max(0, failures - 1));
const errorMessage = (waitMs: number) => `KDOT bridge records are unavailable. No bridge locations, status or absence can be inferred. Next provider check in about ${Math.max(1, Math.ceil(waitMs / 60_000))} minute${Math.ceil(waitMs / 60_000) > 1 ? "s" : ""}.`;

type Inventory = { at: number; retrievedAt: string; bridges: KdotBridge[]; byId: Map<string, KdotBridge>; skipped: number; truncated: boolean; highlights: BridgeHighlights; feeds: Map<BridgeFeedId, OfficialContextPayload> };
type Slot = { cached: Inventory | null; inFlight: Promise<Inventory> | null; retryAt: number; failures: number };

/** One shared inventory read per network and process. The two networks load, cache and back off independently. */
export function createBridgeReader(fetcher: typeof fetch = fetch, clock: () => number = Date.now) {
  const slots: Record<BridgeNetwork, Slot> = { state: { cached: null, inFlight: null, retryAt: 0, failures: 0 }, local: { cached: null, inFlight: null, retryAt: 0, failures: 0 } };
  const readJson = async (url: string, maxBytes: number): Promise<unknown> => {
    const controller = new AbortController(), timer = setTimeout(() => controller.abort(), PAGE_TIMEOUT_MS);
    try {
      const response = await fetcher(url, { signal: controller.signal, redirect: "manual", cache: "no-store",
        headers: { Accept: "application/json", "User-Agent": "KansasFrontierMatrix/1.0 (https://kansasfrontiermatrix.com)" } });
      if (!response.ok) { void response.body?.cancel(); throw new Error("upstream status"); }
      return await readBoundedJson(response, maxBytes, controller.signal);
    } finally { clearTimeout(timer); }
  };
  const load = async (network: BridgeNetwork): Promise<Inventory> => {
    const { pageSize, maxPages } = BRIDGE_NETWORKS[network];
    const total = parseBridgeTotal(await readJson(bridgeCountUrl(network), 4096));
    const pages = Math.min(maxPages, Math.ceil(total / pageSize));
    const now = new Date(clock());
    const parsed = await Promise.all(Array.from({ length: pages }, async (_, page) => parseBridgePage(await readJson(bridgePageUrl(network, page), PAGE_BYTES), network, now)));
    const byId = new Map<string, KdotBridge>(); let skipped = 0, received = 0;
    for (const page of parsed) { skipped += page.skipped; received += page.received; for (const bridge of page.bridges) byId.set(bridge.id, bridge); }
    // A page that changed between reads or an inventory beyond the page cap is reported, never hidden.
    const truncated = total > pages * pageSize || received < Math.min(total, pages * pageSize);
    const bridges = [...byId.values()];
    return { at: clock(), retrievedAt: now.toISOString(), bridges, byId, skipped, truncated, highlights: bridgeHighlights(bridges), feeds: new Map() };
  };
  const inventory = async (network: BridgeNetwork): Promise<Inventory> => {
    const slot = slots[network], now = clock();
    if (slot.cached && now >= slot.cached.at && now - slot.cached.at < BRIDGE_CACHE_MS) return slot.cached;
    if (slot.inFlight) return slot.inFlight;
    if (now < slot.retryAt) throw new Error(errorMessage(slot.retryAt - now));
    slot.inFlight = (async () => {
      try {
        const loaded = await load(network);
        slot.cached = loaded; slot.retryAt = 0; slot.failures = 0;
        return loaded;
      } catch {
        slot.cached = null; slot.failures++;
        const wait = cooldownMs(slot.failures); slot.retryAt = clock() + wait;
        throw new Error(errorMessage(wait));
      }
    })();
    try { return await slot.inFlight; } finally { slot.inFlight = null; }
  };
  return {
    /** The slim clustered-map collection for one of the five bridge layers. */
    async feed(feed: BridgeFeedId): Promise<OfficialContextPayload> {
      const { network, keep } = BRIDGE_FEEDS[feed], loaded = await inventory(network);
      let payload = loaded.feeds.get(feed);
      if (!payload) {
        const bridges = loaded.bridges.filter(keep), partial = loaded.skipped > 0 || loaded.truncated;
        payload = { feed, state: partial ? "partial" : bridges.length ? "ready" : "empty", retrievedAt: loaded.retrievedAt, upstreamUpdatedAt: null, featureCount: bridges.length,
          truncated: loaded.truncated, data: bridgeMapCollection(bridges), source: `Kansas Department of Transportation · ${BRIDGE_NETWORKS[network].service.replaceAll("_", " ")} inventory`,
          limitation: bridgeSummary(feed, bridges, loaded.skipped, loaded.truncated) } as OfficialContextPayload;
        loaded.feeds.set(feed, payload);
      }
      return payload;
    },
    /** The full record for one bridge id from the same inventory read; null when the id is not in it. */
    async detail(id: string): Promise<{ retrievedAt: string; properties: Record<string, string> } | null> {
      const network: BridgeNetwork | null = id.startsWith(BRIDGE_NETWORKS.state.idPrefix) ? "state" : id.startsWith(BRIDGE_NETWORKS.local.idPrefix) ? "local" : null;
      if (!network) return null;
      const loaded = await inventory(network), bridge = loaded.byId.get(id);
      return bridge ? { retrievedAt: loaded.retrievedAt, properties: bridgeDetailProperties(bridge, loaded.highlights, new Date(clock())) } : null;
    },
  };
}
export const kdotBridges = createBridgeReader();
export { isBridgeFeed, type BridgeFeedId } from "../../kdot-bridges";
