/** NOAA GOES-19 GLM flash centroids, supplied by the independent Atmostorm mirror. */
export const GLM_FLASH_WINDOWS = [5, 15, 30, 60, 180] as const;
export type GlmFlashWindow = typeof GLM_FLASH_WINDOWS[number];
export const GLM_FLASH_LIMIT = 5_000;
export const GLM_FLASH_SOURCE = "https://atmostorm.com/api/v1/lightning";
export const GLM_NOAA_SOURCE = "https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc%3AC01527";

export type GlmFlash = Readonly<{
  id: string;
  longitude: number;
  latitude: number;
  observedAt: string;
  timeMs: number;
  energyFj: number | null;
  areaKm2: number | null;
}>;

export type GlmFlashSnapshot = Readonly<{
  source: "NOAA_GOES19_GLM_VIA_ATMOSTORM" | "NOAA_GOES_GLM_ARCHIVE";
  evidenceRole: "EXTERNAL_CONTEXT_ONLY";
  windowMinutes: GlmFlashWindow;
  requestedAt: string;
  providerGeneratedAt: string;
  oldestFlashAt: string | null;
  latestFlashAt: string | null;
  state: "ready" | "empty" | "partial" | "stale";
  partialReason: string | null;
  providerCount: number;
  nearBorderCount: number;
  flashes: readonly GlmFlash[];
  archive?: { start: string; end: string; files: number; expectedFiles: number; missingFiles: number; omittedQuality: number };
}>;

const object = (value: unknown): value is Record<string, unknown> => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const timestamp = (value: unknown): { raw: string; ms: number } | null => {
  if (typeof value !== "string" || !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?(?:Z|\+00:00)$/.test(value)) return null;
  const ms = Date.parse(value);
  return Number.isFinite(ms) && new Date(ms).toISOString().slice(0, 19) === value.slice(0, 19) ? { raw: value, ms } : null;
};

export function parseGlmFlashSnapshot(raw: unknown, windowMinutes: GlmFlashWindow, requestedAt = new Date().toISOString()): GlmFlashSnapshot {
  if (!GLM_FLASH_WINDOWS.includes(windowMinutes) || !object(raw) || raw.type !== "FeatureCollection" || !Array.isArray(raw.features) || !object(raw.metadata)) throw new Error("GLM response shape is invalid.");
  const metadata = raw.metadata;
  const generated = timestamp(metadata.generated_at);
  const requested = timestamp(requestedAt);
  if (metadata.source !== "goes19_glm" || metadata.window_minutes !== windowMinutes || !Number.isSafeInteger(metadata.count) || metadata.count !== raw.features.length || raw.features.length > GLM_FLASH_LIMIT || !generated || !requested || generated.ms > requested.ms + 60_000) throw new Error("GLM source, window, count or clock is invalid.");

  const flashes: GlmFlash[] = [];
  const ids = new Set<string>();
  let nearBorderCount = 0;
  for (const feature of raw.features) {
    if (!object(feature) || feature.type !== "Feature" || !object(feature.geometry) || feature.geometry.type !== "Point" || !Array.isArray(feature.geometry.coordinates) || feature.geometry.coordinates.length !== 2 || !object(feature.properties)) throw new Error("GLM flash geometry is invalid.");
    const [longitude, latitude] = feature.geometry.coordinates;
    const p = feature.properties;
    const time = timestamp(p.flash_time);
    if (typeof longitude !== "number" || typeof latitude !== "number" || !Number.isFinite(longitude) || !Number.isFinite(latitude) || longitude < -102.2 || longitude > -94.45 || latitude < 36.85 || latitude > 40.12 || !time || time.ms > generated.ms + 60_000 || time.ms < generated.ms - (windowMinutes + 2) * 60_000 || !(typeof p.id === "number" || typeof p.id === "string") || String(p.id).length > 40) throw new Error("GLM flash identity, position or time is invalid.");
    const key = `${p.id}:${time.raw}`;
    if (ids.has(key)) throw new Error("GLM response contains duplicate flashes.");
    ids.add(key);
    const optional = (value: unknown): number | null => value === null || value === undefined ? null : typeof value === "number" && Number.isFinite(value) && value >= 0 ? value : NaN;
    const energyFj = optional(p.energy_fj), areaKm2 = optional(p.area_km2);
    if (Number.isNaN(energyFj) || Number.isNaN(areaKm2)) throw new Error("GLM flash measurements are invalid.");
    // The provider's state shortcut is a Kansas-area box. Do not claim that its
    // edge points have been checked against the exact state boundary.
    if (longitude < -102.052 || longitude > -94.588 || latitude < 36.993 || latitude > 40.004) nearBorderCount++;
    flashes.push({ id: key, longitude, latitude, observedAt: time.raw, timeMs: time.ms, energyFj, areaKm2 });
  }
  flashes.sort((a, b) => a.timeMs - b.timeMs || a.id.localeCompare(b.id));
  const stale = requested.ms - generated.ms > 5 * 60_000;
  const capped = flashes.length === GLM_FLASH_LIMIT;
  return {
    source: "NOAA_GOES19_GLM_VIA_ATMOSTORM", evidenceRole: "EXTERNAL_CONTEXT_ONLY",
    windowMinutes, requestedAt, providerGeneratedAt: generated.raw,
    oldestFlashAt: flashes.at(0)?.observedAt ?? null, latestFlashAt: flashes.at(-1)?.observedAt ?? null,
    state: stale ? "stale" : capped ? "partial" : flashes.length ? "ready" : "empty",
    partialReason: capped ? `Provider limit of ${GLM_FLASH_LIMIT.toLocaleString()} flashes reached; older flashes may be missing.` : null,
    providerCount: flashes.length, nearBorderCount, flashes,
  };
}

export function glmFlashPlaybackBounds(snapshot: GlmFlashSnapshot): { start: number; end: number } {
  if (snapshot.archive) return { start: Date.parse(snapshot.archive.start), end: Date.parse(snapshot.archive.end) };
  const end = Date.parse(snapshot.providerGeneratedAt);
  return { start: end - snapshot.windowMinutes * 60_000, end };
}

/** Disjoint time slices of returned observations; empty slices stay empty. */
export function glmFlashBins(snapshot: GlmFlashSnapshot, minutes: 15 | 30 | 60) {
  const { start, end } = glmFlashPlaybackBounds(snapshot);
  const width = minutes * 60_000;
  const bins = Array.from({ length: Math.ceil((end - start) / width) }, (_, index) => ({
    start: start + index * width, end: Math.min(end, start + (index + 1) * width), count: 0,
  }));
  for (const flash of snapshot.flashes) {
    if (flash.timeMs < start || flash.timeMs > end) continue;
    const index = Math.min(bins.length - 1, Math.floor((flash.timeMs - start) / width));
    bins[index].count++;
  }
  return bins;
}
