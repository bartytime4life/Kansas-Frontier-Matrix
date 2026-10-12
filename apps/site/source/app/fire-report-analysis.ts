import type { Feature, Geometry } from "geojson";

export type FireNeighbor = Readonly<{ name: string; distanceKm: number; eventTime: string | null }>;
export type FireReportContext = Readonly<{
  kind: "nifc-fire-reports" | "nasa-gibs-fire-points";
  title: string;
  featureId: string | null;
  observedAt: string | null;
  retrievedAt: string | null;
  sourceUrl: string;
  feedState: "ready" | "partial" | "empty" | "unavailable";
  comparisonState: "ready" | "partial" | "empty" | "unavailable";
  nearby: readonly FireNeighbor[];
}>;

export const FIRE_REPORT_SOURCES = Object.freeze({
  "nifc-fire-reports": "https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/WFIGS_Incident_Locations_YearToDate/FeatureServer/0",
  "nasa-gibs-fire-points": "https://gibs.earthdata.nasa.gov/vector-metadata/v1.0/FIRMS_VIIRS_Thermal_Anomalies.json",
  inciweb: "https://inciweb.wildfire.gov/",
  news: "https://www.nifc.gov/fire-information",
});

const isoTime = (value: unknown): string | null => typeof value === "string" && Number.isFinite(Date.parse(value)) ? value : null;
const feedState = (value: string): FireReportContext["feedState"] =>
  value === "ready" || value === "partial" || value === "empty" ? value : "unavailable";

/** A bounded report seed, never an assertion that an article matches an incident. */
export function buildFireReportContext(
  kind: FireReportContext["kind"],
  feature: Feature<Geometry> | null | undefined,
  retrievedAt: string | null | undefined,
  state: string,
  comparisonState: string,
  nearby: readonly FireNeighbor[],
): FireReportContext {
  const properties = feature?.properties ?? {};
  const title = typeof properties.name === "string" && properties.name.trim() ? properties.name.trim().slice(0, 120) : "Kansas fire context";
  const featureId = typeof properties.featureId === "string" && properties.featureId.length <= 160 ? properties.featureId : null;
  return {
    kind, title, featureId,
    observedAt: isoTime(kind === "nifc-fire-reports" ? properties.discoveryAt : properties.acquiredAt),
    retrievedAt: isoTime(retrievedAt),
    sourceUrl: FIRE_REPORT_SOURCES[kind],
    feedState: feedState(state), comparisonState: feedState(comparisonState),
    nearby: nearby.filter((item) => Number.isFinite(item.distanceKm) && item.distanceKm >= 0 && item.distanceKm <= 10)
      .slice(0, 3).map((item) => ({ name: item.name.slice(0, 120), distanceKm: item.distanceKm, eventTime: isoTime(item.eventTime) })),
  };
}

export function validFireReportContext(value: unknown): value is FireReportContext {
  if (!value || typeof value !== "object" || Array.isArray(value)) return false;
  const item = value as Partial<FireReportContext>;
  return (item.kind === "nifc-fire-reports" || item.kind === "nasa-gibs-fire-points")
    && item.sourceUrl === FIRE_REPORT_SOURCES[item.kind]
    && typeof item.title === "string" && item.title.length > 0 && item.title.length <= 120
    && (item.featureId === null || typeof item.featureId === "string" && item.featureId.length <= 160)
    && (item.observedAt === null || isoTime(item.observedAt) === item.observedAt)
    && (item.retrievedAt === null || isoTime(item.retrievedAt) === item.retrievedAt)
    && ["ready", "partial", "empty", "unavailable"].includes(String(item.feedState))
    && ["ready", "partial", "empty", "unavailable"].includes(String(item.comparisonState))
    && Array.isArray(item.nearby) && item.nearby.length <= 3
    && item.nearby.every((neighbor) => typeof neighbor.name === "string" && neighbor.name.length <= 120
      && Number.isFinite(neighbor.distanceKm) && neighbor.distanceKm >= 0 && neighbor.distanceKm <= 10
      && (neighbor.eventTime === null || isoTime(neighbor.eventTime) === neighbor.eventTime));
}

const point = (feature: Feature<Geometry> | null | undefined): [number, number] | null => {
  if (feature?.geometry?.type !== "Point") return null;
  const [longitude, latitude] = feature.geometry.coordinates;
  return Number.isFinite(longitude) && Number.isFinite(latitude) ? [longitude, latitude] : null;
};

const distanceKm = (left: [number, number], right: [number, number]) => {
  const rad = Math.PI / 180;
  const deltaLat = (right[1] - left[1]) * rad;
  const deltaLng = (right[0] - left[0]) * rad;
  const a = Math.sin(deltaLat / 2) ** 2 + Math.cos(left[1] * rad) * Math.cos(right[1] * rad) * Math.sin(deltaLng / 2) ** 2;
  return 6371 * 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
};

/** Spatial comparison only. A nearby point cannot establish event identity. */
export const nearbyFireContext = (selected: Feature<Geometry> | null | undefined, candidates: readonly Feature<Geometry>[], timeKey: "acquiredAt" | "discoveryAt", radiusKm = 10): readonly FireNeighbor[] => {
  const origin = point(selected);
  if (!origin) return [];
  return candidates.flatMap((candidate) => {
    const coordinates = point(candidate);
    if (!coordinates) return [];
    const distance = distanceKm(origin, coordinates);
    if (distance > radiusKm) return [];
    const properties = candidate.properties ?? {};
    const time = properties[timeKey];
    return [{
      name: typeof properties.name === "string" ? properties.name.slice(0, 120) : "Unnamed record",
      distanceKm: distance,
      eventTime: typeof time === "string" && Number.isFinite(Date.parse(time)) ? time : null,
    }];
  }).sort((left, right) => left.distanceKm - right.distanceKm).slice(0, 3);
};
