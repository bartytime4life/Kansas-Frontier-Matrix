import type { FeatureCollection } from "geojson";

export const DAILY_FEEDS = [
  { id: "census-counties", title: "County reference", scope: "2020 Census edition; capture date is not its observation date" },
  { id: "usgs-streamflow", title: "River observations", scope: "Latest returned discharge per gauge in the rolling 24-hour window" },
  { id: "usgs-earthquakes", title: "Earthquakes", scope: "Provider events in the rolling window described in the payload" },
  { id: "nws-alerts", title: "Weather alerts", scope: "Alerts active at capture time; alerts between captures may be missed" },
  { id: "noaa-hms-smoke", title: "Smoke analysis", scope: "Satellite-analyzed polygons overlapping the rolling 24-hour window" },
  { id: "nasa-gibs-fire-points", title: "Satellite fire detections", scope: "Provider-dated satellite detections; publication may lag capture day" },
  { id: "nifc-fire-reports", title: "Fire incident reports", scope: "Bounded Kansas working reports discovered in the last 30 days" },
  { id: "raspberry-shake-stations", title: "Seismic station metadata", scope: "Station/channel metadata, not waveform measurements" },
  { id: "fema-disaster-declarations", title: "Disaster declarations", scope: "Bounded recent declaration records on 2020 county reference geometry" },
] as const;
export type DailyFeed = typeof DAILY_FEEDS[number]["id"];
export const ARCHIVE_MAX_PAYLOAD = 16 * 1024 * 1024;
export const ARCHIVE_DEFAULT_BUDGET = 2_000_000_000;
export const ARCHIVE_ATTEMPTS = 4;
export const archiveDay = (value: string) => /^\d{4}-\d{2}-\d{2}$/.test(value) && Number.isFinite(Date.parse(value)) && new Date(value).toISOString().slice(0, 10) === value;
export const archiveFeed = (value: string): value is DailyFeed => DAILY_FEEDS.some(feed => feed.id === value);
export type ArchivePayload = { feed: DailyFeed; state: "ready" | "empty" | "partial"; retrievedAt: string; upstreamUpdatedAt: string | null; sourceDay?: string; featureCount: number; data: FeatureCollection; source: string; limitation: string; truncated: boolean };
export type ArchiveEntry = { id: string; day: string; feed: DailyFeed; attempt: number; status: "running" | "ready" | "empty" | "partial" | "failed"; started_at: string; finished_at: string | null; bytes: number; sha256: string | null; object_key: string | null; feature_count: number | null; source_time: string | null; source_day: string | null; message: string; review: "pending" | "reviewed" | "held"; review_note: string | null };
export type ArchiveCatalog = { day: string; days: { day: string; captures: number }[]; entries: ArchiveEntry[]; storage: { used: number; budget: number; paused: boolean }; feeds: typeof DAILY_FEEDS; earliestDay: string | null; latestDay: string | null };

/** A capture is curated for display, never promoted into governed evidence. */
export function validateArchivePayload(value: unknown, feed: DailyFeed): ArchivePayload {
  const p = value as ArchivePayload;
  if (!p || p.feed !== feed || !["ready", "empty", "partial"].includes(p.state) ||
      !Number.isFinite(Date.parse(p.retrievedAt)) || (p.upstreamUpdatedAt !== null && !Number.isFinite(Date.parse(p.upstreamUpdatedAt))) ||
      typeof p.source !== "string" || !p.source || typeof p.limitation !== "string" || typeof p.truncated !== "boolean" ||
      p.data?.type !== "FeatureCollection" || !Array.isArray(p.data.features) || p.data.features.length > 10000 ||
      p.featureCount !== p.data.features.length || (p.state === "empty" && p.featureCount !== 0) || (p.state === "ready" && !p.featureCount) ||
      (p.sourceDay !== undefined && !archiveDay(p.sourceDay))) throw new Error("INVALID_CAPTURE_PAYLOAD");
  let positions = 0;
  const coordinates = (value: unknown, depth: number): void => {
    if (!Array.isArray(value) || value.length === 0 || depth > 5) throw new Error("INVALID_GEOMETRY");
    if (typeof value[0] === "number") {
      if (value.length < 2 || value.length > 3 || !value.every(v => typeof v === "number" && Number.isFinite(v)) || Math.abs(value[0]) > 180 || Math.abs(value[1]) > 90 || ++positions > 600000) throw new Error("INVALID_GEOMETRY");
    } else value.forEach(item => coordinates(item, depth + 1));
  };
  for (const feature of p.data.features) {
    if (feature?.type !== "Feature" || !feature.geometry || !["Point", "MultiPoint", "LineString", "MultiLineString", "Polygon", "MultiPolygon"].includes(feature.geometry.type) || !feature.properties || typeof feature.properties !== "object" || Array.isArray(feature.properties)) throw new Error("INVALID_FEATURE");
    coordinates((feature.geometry as { coordinates: unknown }).coordinates, 0);
  }
  return p;
}
