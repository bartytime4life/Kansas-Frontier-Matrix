import type { StreamflowBundle, StreamflowFrame } from "./streamflow";

export type RiverConnectionState = "idle" | "loading" | "ready" | "partial" | "empty" | "stale" | "error";

/** A selected gauge follows the current frame, not the rendered feature captured at click time. */
export const riverDrawerObservation = (
  stationId: string | null,
  bundle: StreamflowBundle | null,
  frame: StreamflowFrame | null,
  frameTime: string | null,
  connectionState: RiverConnectionState,
) => {
  if (!stationId || !/^USGS-\d{8,15}$/.test(stationId)) return null;
  const station = bundle?.stations.find((item) => item.stationId === stationId) ?? null;
  const sample = frame?.features.find((feature) => feature.properties.stationId === stationId)?.properties ?? null;
  const hasValue = Boolean(sample && !sample.missing && typeof sample.value === "number" && sample.observedAt);
  const status = connectionState === "error" || connectionState === "stale" ? bundle ? "stale" : "error"
    : connectionState === "loading" ? "loading"
      : hasValue ? "observation" : "gap";
  return Object.freeze({
    stationId,
    stationName: station?.name ?? null,
    sourceUrl: `https://waterdata.usgs.gov/monitoring-location/${stationId.slice(5)}/`,
    status,
    connectionState,
    value: hasValue ? sample!.value : null,
    displayValue: hasValue ? sample!.displayValue : null,
    observedAt: hasValue ? sample!.observedAt : null,
    frameTime,
    retrievedAt: bundle?.retrievedAt ?? null,
    approvalStatus: hasValue ? sample!.approvalStatus : null,
    qualifiers: hasValue ? sample!.qualifiers : [],
    trend: hasValue ? sample!.trend : null,
    lastModified: hasValue ? sample!.lastModified : null,
    ageAtFrameMinutes: hasValue ? sample!.ageMinutes : null,
    isPartial: bundle?.state === "partial" || Boolean(bundle?.truncated),
    observationCount: bundle?.observations.filter((item) => item.stationId === stationId).length ?? 0,
  });
};
