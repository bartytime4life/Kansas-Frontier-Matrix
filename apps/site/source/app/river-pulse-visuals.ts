import type { StreamflowFrame, StreamflowObservation } from "./streamflow";

export const RIVER_SIGNALS = [
  { id: "rising", label: "Rising", color: "#61edeb" },
  { id: "falling", label: "Falling", color: "#a5b4ff" },
  { id: "steady", label: "Steady", color: "#98dcc3" },
  { id: "unknown", label: "Uncompared", color: "#b3d8e4" },
  { id: "zero", label: "Zero flow", color: "#ffc27c" },
  { id: "missing", label: "No fresh value", color: "#718392" },
] as const;

/** Mutually exclusive groups: measured zero is never counted as a flowing trend. */
export function riverSignalGroups(frame: StreamflowFrame | null) {
  return RIVER_SIGNALS.map(signal => ({ ...signal, stations: (frame?.features ?? []).filter(feature => {
    const p = feature.properties;
    const kind = p.missing || p.value === null || !Number.isFinite(p.value) ? "missing" : p.value === 0 ? "zero"
      : p.trend === "rising" || p.trend === "falling" || p.trend === "steady" ? p.trend : "unknown";
    return signal.id === kind;
  }).map(feature => feature.properties.stationId) }));
}

/** Chooses an actual source sample, including nulls; never fabricates a point in a gap. */
export function nearestRiverSample(observations: readonly StreamflowObservation[], time: number): number {
  if (!observations.length || !Number.isFinite(time)) return -1;
  let low = 0, high = observations.length - 1;
  while (low < high) { const mid = (low + high) >>> 1; if (Date.parse(observations[mid].observedAt) < time) low = mid + 1; else high = mid; }
  return low > 0 && Math.abs(Date.parse(observations[low - 1].observedAt) - time) <= Math.abs(Date.parse(observations[low].observedAt) - time) ? low - 1 : low;
}
