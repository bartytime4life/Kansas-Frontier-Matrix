import { bridgeClusterSummary, isBridgeFeed } from "./kdot-bridges";

/** Numbered circles on dense point layers: what one circle stands for, by source. */
export type ClusterSummary = Readonly<{ title: string; detail: string }>;

/** National Register markers split apart one zoom level earlier than bridges; there are far fewer of them. */
export const HISTORIC_PLACE_CLUSTER_MAX_ZOOM = 12;
export const HISTORIC_PLACE_CLUSTER_RADIUS = 42;
const HISTORIC_PLACE_TYPES = [["building", "buildings"], ["district", "districts"], ["site", "sites"], ["structure", "structures"], ["object", "objects"]] as const;
const countWhere = (test: unknown[]) => ["+", ["case", test, 1, 0]];
/** Totals MapLibre keeps for each National Register cluster. */
export const HISTORIC_PLACE_CLUSTER_PROPERTIES: Readonly<Record<string, unknown[]>> = Object.freeze({
  landmarks: countWhere(["==", ["get", "landmark"], true]),
  ...Object.fromEntries(HISTORIC_PLACE_TYPES.map(([type, key]) => [key, countWhere(["==", ["get", "resourceType"], type])])),
});

const clusterCount = (properties: unknown): { p: Record<string, unknown>; count: number } | null => {
  const p = properties as Record<string, unknown> | null;
  const count = p && typeof p.point_count === "number" && Number.isFinite(p.point_count) ? p.point_count : 0;
  return p && p.cluster && count >= 2 ? { p, count } : null;
};
const total = (p: Record<string, unknown>, key: string) => typeof p[key] === "number" && Number.isFinite(p[key]) ? p[key] as number : 0;
const plural = (count: number, one: string, many: string) => `${count.toLocaleString("en-US")} ${count === 1 ? one : many}`;

export function historicPlaceClusterSummary(properties: unknown): ClusterSummary | null {
  const cluster = clusterCount(properties);
  if (!cluster) return null;
  const { p, count } = cluster, landmarks = total(p, "landmarks");
  const facts = [landmarks > 0 ? plural(landmarks, "National Historic Landmark", "National Historic Landmarks") : null,
    ...HISTORIC_PLACE_TYPES.map(([type, key]) => total(p, key) > 0 ? plural(total(p, key), type, key) : null)].filter(Boolean);
  // A listing can publish several points, so this counts markers, not listings.
  return { title: `${count.toLocaleString("en-US")} National Register markers in this area`, detail: facts.length ? facts.join(" · ") : "Select to zoom in" };
}

/** The summary for a numbered circle on an official source, or null when the feature is a single record. */
export function officialClusterSummary(sourceId: string | undefined, properties: unknown): ClusterSummary | null {
  if (!sourceId) return null;
  if (isBridgeFeed(sourceId)) return bridgeClusterSummary(properties);
  if (sourceId === "nps-nrhp-places") return historicPlaceClusterSummary(properties);
  return null;
}
