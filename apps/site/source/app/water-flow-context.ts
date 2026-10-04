import type { StreamflowFrameProperties, StreamflowObservation } from "./streamflow";
import type { WaterPathAnalysis } from "./water-path-analysis";

export type DownstreamPath = Readonly<{
  id: string;
  coordinates: readonly (readonly [number, number])[];
  hasConnectors?: boolean;
}>;

export type DownstreamGuide = Readonly<{
  format: "kfm-3dhp-direction-v1" | "kfm-3dhp-direction-v2";
  state: "ready" | "empty";
  paths: readonly DownstreamPath[];
  source: string;
  retrievedAt: string;
  evidenceRole: "EXTERNAL_CONTEXT_ONLY";
  limitation: string;
  analysis?: WaterPathAnalysis | null;
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
  if (!["kfm-3dhp-direction-v1", "kfm-3dhp-direction-v2"].includes(String(guide.format))
    || !["ready", "empty"].includes(String(guide.state))
    || !Array.isArray(guide.paths) || guide.paths.length > 20
    || typeof guide.source !== "string" || !guide.source.startsWith("https://3dhp.nationalmap.gov/")
    || typeof guide.retrievedAt !== "string" || !Number.isFinite(Date.parse(guide.retrievedAt))
    || guide.evidenceRole !== "EXTERNAL_CONTEXT_ONLY"
    || typeof guide.limitation !== "string") throw new Error("Downstream guide is invalid.");
  for (const path of guide.paths) {
    if (!path || typeof path.id !== "string" || !/^[A-Za-z0-9]{1,16}$/.test(path.id)
      || !(path.hasConnectors === undefined || typeof path.hasConnectors === "boolean")
      || !Array.isArray(path.coordinates) || path.coordinates.length < 2 || path.coordinates.length > (guide.format === "kfm-3dhp-direction-v2" ? 5000 : 300)
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
  if (guide.format === "kfm-3dhp-direction-v2") {
    if (guide.paths.length > 1 || (guide.state === "ready") !== Boolean(guide.analysis)) throw new Error("Downstream analysis is inconsistent.");
    const a = guide.analysis;
    if (a) {
      const finite = (v: unknown): v is number => typeof v === "number" && Number.isFinite(v);
      if (!finite(a.lengthM) || a.lengthM < 1 || a.lengthM > 40001 || !finite(a.gaugeOffsetM) || a.gaugeOffsetM < 0 || a.gaugeOffsetM > 1200
        || !Number.isInteger(a.segments) || a.segments < 1 || a.segments > 80 || !Number.isInteger(a.connectors) || a.connectors < 0 || a.connectors > a.segments || !(a.name === null || typeof a.name === "string" && a.name.length <= 160)
        || typeof a.stopReason !== "string" || a.stopReason.length > 500 || !a.elevation || !["ready", "partial", "unavailable"].includes(a.elevation.state)
        || !Array.isArray(a.elevation.samples) || a.elevation.samples.length > 25 || typeof a.elevation.notice !== "string"
        || a.elevation.source !== "https://elevation.nationalmap.gov/arcgis/rest/services/3DEPElevation/ImageServer/getSamples"
        || !(a.elevation.retrievedAt === null || typeof a.elevation.retrievedAt === "string" && Number.isFinite(Date.parse(a.elevation.retrievedAt)))
        || !(a.elevation.dropM === null || finite(a.elevation.dropM)) || !(a.elevation.slopePercent === null || finite(a.elevation.slopePercent))) throw new Error("Downstream analysis is invalid.");
      let previousDistance = -1;
      for (const sample of a.elevation.samples) {
        if (!finite(sample.distanceM) || sample.distanceM < previousDistance || sample.distanceM > a.lengthM + 1
          || !Array.isArray(sample.coordinate) || sample.coordinate.length !== 2 || !sample.coordinate.every(finite)
          || sample.coordinate[0] < -102.2 || sample.coordinate[0] > -94.4 || sample.coordinate[1] < 36.8 || sample.coordinate[1] > 40.2
          || !(sample.elevationM === null || finite(sample.elevationM) && sample.elevationM >= -100 && sample.elevationM <= 2000)
          || !(sample.datum === null || typeof sample.datum === "string" && sample.datum.length <= 180)
          || !(sample.resolutionM === null || finite(sample.resolutionM) && sample.resolutionM > 0)) throw new Error("Terrain profile contains an invalid sample.");
        previousDistance = sample.distanceM;
      }
    }
  }
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
