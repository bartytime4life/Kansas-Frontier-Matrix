import type { StreamflowFrameProperties, StreamflowObservation } from "./streamflow";

export type DownstreamPath = Readonly<{
  id: string;
  coordinates: readonly (readonly [number, number])[];
}>;

export type DownstreamGuide = Readonly<{
  format: "kfm-3dhp-direction-v1";
  state: "ready" | "empty";
  paths: readonly DownstreamPath[];
  source: string;
  retrievedAt: string;
  evidenceRole: "EXTERNAL_CONTEXT_ONLY";
  limitation: string;
}>;

/** Only the provider's explicit downstream channel lines can drive arrows. */
export function boundedDirectionPaths(payload: unknown): DownstreamPath[] {
  if (!payload || typeof payload !== "object") throw new Error("USGS 3DHP response was invalid.");
  const source = payload as { features?: unknown; error?: unknown };
  if (source.error || !Array.isArray(source.features) || source.features.length > 100) throw new Error("USGS 3DHP response was invalid.");
  const paths: DownstreamPath[] = [];
  for (const feature of source.features) {
    if (!feature || typeof feature !== "object") continue;
    const candidate = feature as { properties?: Record<string, unknown>; geometry?: { type?: unknown; coordinates?: unknown } };
    if (candidate.properties?.flowdirection !== 1 || candidate.properties?.featuretype !== 1
      || candidate.geometry?.type !== "LineString" || !Array.isArray(candidate.geometry.coordinates)) continue;
    const id = candidate.properties.id3dhp;
    const coordinates = candidate.geometry.coordinates;
    if (typeof id !== "string" || !/^[A-Za-z0-9]{1,16}$/.test(id) || coordinates.length < 2 || coordinates.length > 300) continue;
    if (!coordinates.every((point) => Array.isArray(point) && point.length === 2
      && point.every((value) => typeof value === "number" && Number.isFinite(value))
      && point[0] >= -102.2 && point[0] <= -94.4 && point[1] >= 36.8 && point[1] <= 40.2)) continue;
    paths.push({ id, coordinates: coordinates as [number, number][] });
    if (paths.length === 20) break;
  }
  return paths;
}

export function parseDownstreamGuide(value: unknown): DownstreamGuide {
  if (!value || typeof value !== "object") throw new Error("Downstream guide is invalid.");
  const guide = value as Partial<DownstreamGuide>;
  if (guide.format !== "kfm-3dhp-direction-v1"
    || !["ready", "empty"].includes(String(guide.state))
    || !Array.isArray(guide.paths) || guide.paths.length > 20
    || typeof guide.source !== "string" || !guide.source.startsWith("https://3dhp.nationalmap.gov/")
    || typeof guide.retrievedAt !== "string" || !Number.isFinite(Date.parse(guide.retrievedAt))
    || guide.evidenceRole !== "EXTERNAL_CONTEXT_ONLY"
    || typeof guide.limitation !== "string") throw new Error("Downstream guide is invalid.");
  for (const path of guide.paths) {
    if (!path || typeof path.id !== "string" || !/^[A-Za-z0-9]{1,16}$/.test(path.id)
      || !Array.isArray(path.coordinates) || path.coordinates.length < 2 || path.coordinates.length > 300
      || !path.coordinates.every((point: unknown) => {
        if (!Array.isArray(point) || point.length !== 2) return false;
        const [longitude, latitude] = point;
        return typeof longitude === "number" && Number.isFinite(longitude)
          && typeof latitude === "number" && Number.isFinite(latitude)
          && longitude >= -102.2 && longitude <= -94.4 && latitude >= 36.8 && latitude <= 40.2;
      })) {
      throw new Error("Downstream guide contains an invalid path.");
    }
  }
  if ((guide.state === "ready") !== (guide.paths.length > 0)) throw new Error("Downstream guide state is inconsistent.");
  return guide as DownstreamGuide;
}

export type WaterReadingCue = Readonly<{
  kind: "missing" | "zero" | "rising" | "falling" | "steady" | "uncompared";
  value: number | null;
  previousValue: number | null;
  change: number | null;
  rangePosition: number | null;
  rangeMinimum: number | null;
  rangeMaximum: number | null;
}>;

/** Relative position is limited to the loaded observations at one station. */
export function waterReadingCue(
  frame: StreamflowFrameProperties | null,
  observations: readonly StreamflowObservation[],
): WaterReadingCue {
  const values = observations.flatMap((observation) => observation.value !== null && Number.isFinite(observation.value) && observation.value >= 0 ? [observation.value] : []);
  const minimum = values.length ? Math.min(...values) : null;
  const maximum = values.length ? Math.max(...values) : null;
  const value = frame && !frame.missing && frame.value !== null && Number.isFinite(frame.value) && frame.value >= 0 ? frame.value : null;
  const previousValue = frame && frame.previousValue !== null && Number.isFinite(frame.previousValue) && frame.previousValue >= 0 ? frame.previousValue : null;
  const change = value !== null && previousValue !== null ? value - previousValue : null;
  const rangePosition = value !== null && minimum !== null && maximum !== null && maximum > minimum
    ? Math.max(0, Math.min(1, (value - minimum) / (maximum - minimum))) : null;
  const kind = value === null ? "missing" : value === 0 ? "zero" : change === null ? "uncompared"
    : change > 0 ? "rising" : change < 0 ? "falling" : "steady";
  return { kind, value, previousValue, change, rangePosition, rangeMinimum: minimum, rangeMaximum: maximum };
}
