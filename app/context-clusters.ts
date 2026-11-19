import { bridgeClusterSummary, isBridgeFeed } from "./kdot-bridges";
import type { Feature, FeatureCollection, Point, Position } from "geojson";

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

/** Trail sites sit close together along the old roads; ninety-odd markers separate by zoom 10. */
export const TRAIL_PLACE_CLUSTER_MAX_ZOOM = 9;
export const TRAIL_PLACE_CLUSTER_RADIUS = 38;
const TRAIL_NAMES = [["Santa Fe", "santaFe"], ["Oregon", "oregon"], ["California", "california"], ["Pony Express", "ponyExpress"]] as const;
/** Totals MapLibre keeps for each trail-site cluster. A site on a shared corridor counts toward each of its trails. */
export const TRAIL_PLACE_CLUSTER_PROPERTIES: Readonly<Record<string, unknown[]>> = Object.freeze({
  certified: countWhere(["==", ["get", "certified"], "NPS-certified trail site"]),
  ...Object.fromEntries(TRAIL_NAMES.map(([name, key]) => [key, countWhere(["in", name, ["to-string", ["coalesce", ["get", "trails"], ""]]])])),
});

export function trailPlaceClusterSummary(properties: unknown): ClusterSummary | null {
  const cluster = clusterCount(properties);
  if (!cluster) return null;
  const { p, count } = cluster, certified = total(p, "certified");
  const facts = [certified > 0 ? `${certified.toLocaleString("en-US")} NPS-certified` : null,
    ...TRAIL_NAMES.map(([name, key]) => total(p, key) > 0 ? `${name} ${total(p, key).toLocaleString("en-US")}` : null)].filter(Boolean);
  return { title: `${count.toLocaleString("en-US")} trail sites in this area`, detail: facts.length ? facts.join(" · ") : "Select to zoom in" };
}

/** Walk-in hunting tracts are outlines too small to read at statewide scale. Below this zoom a
 * second, display-only source counts them in numbered circles; from it on, the tracts take over. */
export const ACCESS_OVERVIEW_SOURCE_ID = "external-kdwp-wiha-access-overview";
export const ACCESS_OVERVIEW_MAX_ZOOM = 8;
export const ACCESS_OVERVIEW_CLUSTER_RADIUS = 60;
/** Totals MapLibre keeps for each overview circle: recorded acres and archery-only tracts. */
export const ACCESS_OVERVIEW_CLUSTER_PROPERTIES: Readonly<Record<string, unknown[]>> = Object.freeze({
  acres: ["+", ["get", "acres"]], archeryOnly: ["+", ["get", "archeryOnly"]],
});

const overviews = new WeakMap<FeatureCollection, FeatureCollection<Point>>();
/** One point per tract, at the middle of its outline's extent, carrying only what the circles total.
 * The same tract collection always yields the same overview object, so the map is not re-fed on every state change. */
export function accessOverviewPoints(tracts: FeatureCollection): FeatureCollection<Point> {
  const known = overviews.get(tracts);
  if (known) return known;
  const features: Feature<Point>[] = [];
  for (const tract of tracts.features) {
    const geometry = tract.geometry;
    if (!geometry || (geometry.type !== "Polygon" && geometry.type !== "MultiPolygon")) continue;
    let west = Infinity, south = Infinity, east = -Infinity, north = -Infinity;
    const rings: Position[][] = geometry.type === "Polygon" ? geometry.coordinates : geometry.coordinates.flat();
    for (const ring of rings) for (const [x, y] of ring) {
      if (!Number.isFinite(x) || !Number.isFinite(y)) continue;
      if (x < west) west = x; if (x > east) east = x; if (y < south) south = y; if (y > north) north = y;
    }
    if (!Number.isFinite(west) || !Number.isFinite(south)) continue;
    const p = tract.properties ?? {}, acres = typeof p.acres === "number" && Number.isFinite(p.acres) && p.acres > 0 ? p.acres : 0;
    features.push({ type: "Feature", geometry: { type: "Point", coordinates: [(west + east) / 2, (south + north) / 2] },
      properties: { featureId: `${String(p.featureId ?? features.length)}-overview`, acres, archeryOnly: p.archeryOnly === "Archery only" ? 1 : 0 } });
  }
  const overview: FeatureCollection<Point> = { type: "FeatureCollection", features };
  overviews.set(tracts, overview);
  return overview;
}

export function accessOverviewSummary(properties: unknown): ClusterSummary | null {
  const cluster = clusterCount(properties);
  if (!cluster) return null;
  const { p, count } = cluster, acres = Math.round(total(p, "acres")), archery = total(p, "archeryOnly");
  const facts = [acres > 0 ? `${acres.toLocaleString("en-US")} recorded acres` : null, archery > 0 ? `${archery.toLocaleString("en-US")} archery-only` : null].filter(Boolean);
  return { title: `${count.toLocaleString("en-US")} walk-in hunting tracts in this area`, detail: facts.length ? facts.join(" · ") : "Select to zoom in" };
}

/** The summary for a numbered circle on an official source, or null when the feature is a single record. */
export function officialClusterSummary(sourceId: string | undefined, properties: unknown): ClusterSummary | null {
  if (!sourceId) return null;
  if (isBridgeFeed(sourceId)) return bridgeClusterSummary(properties);
  if (sourceId === "nps-nrhp-places") return historicPlaceClusterSummary(properties);
  if (sourceId === "nps-trail-places") return trailPlaceClusterSummary(properties);
  if (sourceId === "kdwp-wiha-access") return accessOverviewSummary(properties);
  return null;
}
