import type { LayerRecord } from "./explorer-data";

export type TemporalSweepMode = "snapshot" | "moving-window" | "event-stepping" | "accumulation" | "comparison";
export type TemporalStepRule = "available-events" | "regular-calendar";
export type TemporalPlaybackDirection = "forward" | "reverse";
export type TemporalLoopMode = "stop" | "loop";

export type TemporalSweepQuery = Readonly<{
  mode: TemporalSweepMode;
  frame: number;
  rangeStart: number;
  rangeEnd: number;
  windowStart: number;
}>;

export type TemporalFrameRecord = Readonly<{
  id: string;
  featureId: string;
  title: string;
  layerId: string;
  layerTitle: string;
  domain: string;
  year: number;
  axis: "declared-feature-year" | "untimed-reference";
  layerTemporalMode: "exact" | "through" | "untimed";
  sourceTime: string;
  releaseTime: string;
  releaseState: string;
}>;

export type TemporalDomainPair = Readonly<{
  id: string;
  leftDomain: string;
  rightDomain: string;
  leftRecordCount: number;
  rightRecordCount: number;
}>;

export type TemporalFrameSummary = Readonly<{
  frame: number;
  windowStart: number;
  timedRecordCount: number;
  activeDomainCount: number;
  entered: readonly TemporalFrameRecord[];
  exited: readonly TemporalFrameRecord[];
  persisted: readonly TemporalFrameRecord[];
  domainCounts: Readonly<Record<string, number>>;
  domainPairs: readonly TemporalDomainPair[];
}>;

const orderedRange = (left: number, right: number) => ({
  start: Math.min(left, right),
  end: Math.max(left, right),
});

const uniqueSorted = (values: readonly number[]) => [...new Set(values)].sort((left, right) => left - right);

export const temporalEventYears = (layers: readonly LayerRecord[]) => uniqueSorted(
  layers
    .filter((layer) => Boolean(layer.temporal))
    .flatMap((layer) => layer.data.features.map((feature) => feature.properties.year)),
);

export const buildTemporalSequence = (
  layers: readonly LayerRecord[],
  atlasSteps: readonly number[],
  rangeStart: number,
  rangeEnd: number,
  rule: TemporalStepRule,
) => {
  const range = orderedRange(rangeStart, rangeEnd);
  const boundedAtlasSteps = uniqueSorted(atlasSteps).filter((step) => step >= range.start && step <= range.end);
  if (boundedAtlasSteps.length === 0 && rule === "regular-calendar") return Object.freeze(uniqueSorted([range.start, range.end]));
  if (rule === "regular-calendar") return Object.freeze(boundedAtlasSteps);

  const eventSteps = temporalEventYears(layers).filter((step) => step >= range.start && step <= range.end);
  return Object.freeze(uniqueSorted([range.start, ...eventSteps, range.end]));
};

export const buildTemporalQuery = (
  mode: TemporalSweepMode,
  frame: number,
  rangeStart: number,
  rangeEnd: number,
  sequence: readonly number[],
  windowFrames = 3,
): TemporalSweepQuery => {
  const requestedRange = orderedRange(rangeStart, rangeEnd);
  const safeFrame = Number.isFinite(frame) ? frame : requestedRange.end;
  const range = {
    start: Math.min(requestedRange.start, safeFrame),
    end: Math.max(requestedRange.end, safeFrame),
  };
  const safeWindowFrames = Math.max(1, Math.min(8, Math.round(windowFrames)));
  const frameIndex = Math.max(0, sequence.reduce((nearestIndex, step, index) => (
    step <= safeFrame ? index : nearestIndex
  ), -1));
  const windowStart = safeFrame < (sequence[0] ?? safeFrame)
    ? safeFrame
    : sequence[Math.max(0, frameIndex - safeWindowFrames + 1)] ?? safeFrame;
  return Object.freeze({ mode, frame: safeFrame, rangeStart: range.start, rangeEnd: range.end, windowStart });
};

export const isFeatureAvailableForTemporalQuery = (
  layer: Pick<LayerRecord, "temporal">,
  featureYear: number,
  query: TemporalSweepQuery,
) => {
  if (!layer.temporal) return true;
  if (query.mode === "moving-window") {
    if (layer.temporal.mode === "through") return featureYear <= query.frame;
    return featureYear >= query.windowStart && featureYear <= query.frame;
  }
  if (query.mode === "accumulation") {
    return featureYear >= query.rangeStart && featureYear <= query.frame;
  }
  if (layer.temporal.mode === "exact") return featureYear === query.frame;
  return featureYear <= query.frame;
};

export const temporalRecordsForQuery = (
  layers: readonly LayerRecord[],
  query: TemporalSweepQuery,
  timedOnly = false,
): readonly TemporalFrameRecord[] => Object.freeze(layers.flatMap((layer) => {
  if (timedOnly && !layer.temporal) return [];
  return layer.data.features
    .filter((feature) => isFeatureAvailableForTemporalQuery(layer, feature.properties.year, query))
    .map((feature) => Object.freeze({
      id: `${layer.id}:${feature.properties.fid}`,
      featureId: feature.properties.fid,
      title: feature.properties.title,
      layerId: layer.id,
      layerTitle: layer.title,
      domain: layer.domain,
      year: feature.properties.year,
      axis: layer.temporal ? "declared-feature-year" as const : "untimed-reference" as const,
      layerTemporalMode: layer.temporal?.mode ?? "untimed",
      sourceTime: layer.sourceTime,
      releaseTime: layer.releaseTime,
      releaseState: layer.releaseState,
    }));
}));

const domainPairsFor = (domainCounts: Readonly<Record<string, number>>) => {
  const domains = Object.keys(domainCounts).sort();
  const pairs: TemporalDomainPair[] = [];
  for (let left = 0; left < domains.length; left += 1) {
    for (let right = left + 1; right < domains.length; right += 1) {
      const leftDomain = domains[left];
      const rightDomain = domains[right];
      pairs.push(Object.freeze({
        id: `${leftDomain}::${rightDomain}`,
        leftDomain,
        rightDomain,
        leftRecordCount: domainCounts[leftDomain],
        rightRecordCount: domainCounts[rightDomain],
      }));
    }
  }
  return Object.freeze(pairs.sort((left, right) => (
    Math.min(right.leftRecordCount, right.rightRecordCount) - Math.min(left.leftRecordCount, left.rightRecordCount)
    || left.id.localeCompare(right.id)
  )));
};

export const buildTemporalFrameSummary = (
  layers: readonly LayerRecord[],
  query: TemporalSweepQuery,
  previousQuery?: TemporalSweepQuery | null,
): TemporalFrameSummary => {
  const current = temporalRecordsForQuery(layers, query, true);
  const previous = previousQuery ? temporalRecordsForQuery(layers, previousQuery, true) : Object.freeze([]);
  const currentIds = new Set(current.map((record) => record.id));
  const previousIds = new Set(previous.map((record) => record.id));
  const domainCounts = Object.freeze(current.reduce<Record<string, number>>((counts, record) => {
    counts[record.domain] = (counts[record.domain] ?? 0) + 1;
    return counts;
  }, {}));

  return Object.freeze({
    frame: query.frame,
    windowStart: query.windowStart,
    timedRecordCount: current.length,
    activeDomainCount: Object.keys(domainCounts).length,
    entered: Object.freeze(current.filter((record) => !previousIds.has(record.id))),
    exited: Object.freeze(previous.filter((record) => !currentIds.has(record.id))),
    persisted: Object.freeze(current.filter((record) => previousIds.has(record.id))),
    domainCounts,
    domainPairs: domainPairsFor(domainCounts),
  });
};

export const nextTemporalFrame = (
  sequence: readonly number[],
  current: number,
  direction: TemporalPlaybackDirection,
  loopMode: TemporalLoopMode,
): number | null => {
  if (sequence.length === 0) return null;
  const fallbackIndex = direction === "forward" ? 0 : sequence.length - 1;
  const currentIndex = sequence.indexOf(current);
  if (currentIndex < 0) {
    const adjacent = direction === "forward"
      ? sequence.find((step) => step > current)
      : [...sequence].reverse().find((step) => step < current);
    if (adjacent !== undefined) return adjacent;
    return loopMode === "loop" ? sequence[fallbackIndex] : null;
  }
  const nextIndex = currentIndex + (direction === "forward" ? 1 : -1);
  if (nextIndex >= 0 && nextIndex < sequence.length) return sequence[nextIndex];
  if (loopMode === "loop") return sequence[direction === "forward" ? 0 : sequence.length - 1];
  return null;
};

export const nearestTemporalFrame = (sequence: readonly number[], frame: number) => {
  if (sequence.length === 0) return frame;
  return sequence.reduce((nearest, candidate) => (
    Math.abs(candidate - frame) < Math.abs(nearest - frame) ? candidate : nearest
  ), sequence[0]);
};
