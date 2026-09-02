/**
 * Deterministic plan and result evaluator for a future synthetic point-cloud
 * browser benchmark. It allocates no large arrays, performs no GPU work, and
 * admits no renderer, source, dependency, or production data.
 */
export const SYNTHETIC_POINT_CLOUD_BENCHMARK_PROFILE =
  "kfm.explorer.synthetic-point-cloud-benchmark.v1" as const;

export const SYNTHETIC_POINT_COUNTS = [50_000, 250_000, 1_000_000] as const;
export type SyntheticPointCount = (typeof SYNTHETIC_POINT_COUNTS)[number];

export type SyntheticPointCloudCase = Readonly<{
  id: string;
  seed: number;
  pointCount: SyntheticPointCount;
  nearestNeighbourEdges: boolean;
  publicSafe: true;
  synthetic: true;
}>;

export type SyntheticPointCloudBenchmarkPlan = Readonly<{
  profile: typeof SYNTHETIC_POINT_CLOUD_BENCHMARK_PROFILE;
  version: "1.0.0";
  cases: readonly SyntheticPointCloudCase[];
  measurements: readonly [
    "initialization_ms",
    "p95_frame_ms",
    "main_thread_block_ms",
    "selection_latency_ms",
    "peak_memory_mb",
    "disposed_cleanly",
    "reduced_motion_fallback",
  ];
  authority: "NONE";
}>;

export type SyntheticPoint = Readonly<{
  x: number;
  y: number;
  z: number;
}>;

export type PointCloudBenchmarkMeasurement = Readonly<{
  profile: typeof SYNTHETIC_POINT_CLOUD_BENCHMARK_PROFILE;
  caseId: string;
  pointCount: SyntheticPointCount;
  initializationMs: number;
  p95FrameMs: number;
  mainThreadBlockMs: number;
  selectionLatencyMs: number;
  peakMemoryMb: number;
  disposedCleanly: boolean;
  reducedMotionFallback: boolean;
  synthetic: true;
  publicSafe: true;
}>;

export type PointCloudBenchmarkOutcome = Readonly<{
  outcome: "PASS" | "HOLD" | "DENY" | "ERROR";
  reasons: readonly string[];
  pointCount: SyntheticPointCount | null;
  recommendedCarrier:
    | "POINTS_3D"
    | "DECIMATED_POINTS_3D"
    | "CLUSTERED_2D"
    | null;
}>;

const COUNTS = new Set<number>(SYNTHETIC_POINT_COUNTS);
const MEASUREMENT_FIELDS = new Set([
  "profile",
  "caseId",
  "pointCount",
  "initializationMs",
  "p95FrameMs",
  "mainThreadBlockMs",
  "selectionLatencyMs",
  "peakMemoryMb",
  "disposedCleanly",
  "reducedMotionFallback",
  "synthetic",
  "publicSafe",
]);
const SAFE_ID = /^[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}$/;

const BUDGETS: Readonly<
  Record<
    SyntheticPointCount,
    Readonly<{
      initializationMs: number;
      p95FrameMs: number;
      mainThreadBlockMs: number;
      selectionLatencyMs: number;
      peakMemoryMb: number;
    }>
  >
> = Object.freeze({
  50_000: Object.freeze({
    initializationMs: 750,
    p95FrameMs: 25,
    mainThreadBlockMs: 100,
    selectionLatencyMs: 100,
    peakMemoryMb: 256,
  }),
  250_000: Object.freeze({
    initializationMs: 1_500,
    p95FrameMs: 33,
    mainThreadBlockMs: 150,
    selectionLatencyMs: 150,
    peakMemoryMb: 512,
  }),
  1_000_000: Object.freeze({
    initializationMs: 4_000,
    p95FrameMs: 50,
    mainThreadBlockMs: 250,
    selectionLatencyMs: 250,
    peakMemoryMb: 1_024,
  }),
});

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  fields: ReadonlySet<string>,
): boolean {
  const keys = Object.keys(value);
  return keys.length === fields.size && keys.every((key) => fields.has(key));
}

function finiteNonNegative(value: unknown): value is number {
  return typeof value === "number" && Number.isFinite(value) && value >= 0;
}

function normalizeSeed(value: number): number {
  if (!Number.isSafeInteger(value)) return 1;
  const normalized = Math.abs(value) % 2_147_483_647;
  return normalized === 0 ? 1 : normalized;
}

/** Build the fixed 50k/250k/1m no-network benchmark matrix. */
export function buildSyntheticPointCloudBenchmarkPlan(
  seed = 1,
): SyntheticPointCloudBenchmarkPlan {
  const normalizedSeed = normalizeSeed(seed);
  const cases = SYNTHETIC_POINT_COUNTS.map((pointCount, index) =>
    Object.freeze({
      id: `synthetic-point-cloud-${pointCount}`,
      seed: normalizedSeed + index,
      pointCount,
      nearestNeighbourEdges: pointCount !== 1_000_000,
      publicSafe: true as const,
      synthetic: true as const,
    }),
  );

  return Object.freeze({
    profile: SYNTHETIC_POINT_CLOUD_BENCHMARK_PROFILE,
    version: "1.0.0",
    cases: Object.freeze(cases),
    measurements: Object.freeze([
      "initialization_ms",
      "p95_frame_ms",
      "main_thread_block_ms",
      "selection_latency_ms",
      "peak_memory_mb",
      "disposed_cleanly",
      "reduced_motion_fallback",
    ] as const),
    authority: "NONE",
  });
}

/**
 * Produce one deterministic point without allocating a fixture array. The
 * generator is deliberately synthetic and carries no spatial or evidentiary
 * meaning.
 */
export function sampleSyntheticPoint(seed: number, index: number): SyntheticPoint {
  const normalizedSeed = normalizeSeed(seed);
  const normalizedIndex = Number.isSafeInteger(index) ? Math.max(0, index) : 0;
  let state = (normalizedSeed ^ Math.imul(normalizedIndex + 1, 0x9e3779b1)) >>> 0;

  const next = (): number => {
    state = (state + 0x6d2b79f5) >>> 0;
    let value = state;
    value = Math.imul(value ^ (value >>> 15), value | 1);
    value ^= value + Math.imul(value ^ (value >>> 7), value | 61);
    return ((value ^ (value >>> 14)) >>> 0) / 4_294_967_296;
  };

  return Object.freeze({
    x: next() * 2 - 1,
    y: next() * 2 - 1,
    z: next() * 2 - 1,
  });
}

/** Strictly parse one closed synthetic benchmark measurement. */
export function parsePointCloudBenchmarkMeasurement(
  value: unknown,
): PointCloudBenchmarkMeasurement | null {
  if (!isRecord(value) || !hasExactFields(value, MEASUREMENT_FIELDS)) return null;
  if (value.profile !== SYNTHETIC_POINT_CLOUD_BENCHMARK_PROFILE) return null;
  if (typeof value.caseId !== "string" || !SAFE_ID.test(value.caseId)) return null;
  if (typeof value.pointCount !== "number" || !COUNTS.has(value.pointCount)) return null;
  const pointCount = value.pointCount as SyntheticPointCount;
  if (value.caseId !== `synthetic-point-cloud-${pointCount}`) return null;
  if (!finiteNonNegative(value.initializationMs)) return null;
  if (!finiteNonNegative(value.p95FrameMs)) return null;
  if (!finiteNonNegative(value.mainThreadBlockMs)) return null;
  if (!finiteNonNegative(value.selectionLatencyMs)) return null;
  if (!finiteNonNegative(value.peakMemoryMb)) return null;
  if (typeof value.disposedCleanly !== "boolean") return null;
  if (typeof value.reducedMotionFallback !== "boolean") return null;
  if (value.synthetic !== true || value.publicSafe !== true) return null;

  return Object.freeze({
    profile: SYNTHETIC_POINT_CLOUD_BENCHMARK_PROFILE,
    caseId: value.caseId,
    pointCount,
    initializationMs: value.initializationMs,
    p95FrameMs: value.p95FrameMs,
    mainThreadBlockMs: value.mainThreadBlockMs,
    selectionLatencyMs: value.selectionLatencyMs,
    peakMemoryMb: value.peakMemoryMb,
    disposedCleanly: value.disposedCleanly,
    reducedMotionFallback: value.reducedMotionFallback,
    synthetic: true,
    publicSafe: true,
  });
}

/** Evaluate finite safety and performance outcomes without renderer authority. */
export function evaluatePointCloudBenchmark(
  value: unknown,
): PointCloudBenchmarkOutcome {
  const measurement = parsePointCloudBenchmarkMeasurement(value);
  if (measurement === null) {
    return Object.freeze({
      outcome: "ERROR",
      reasons: Object.freeze(["INVALID_MEASUREMENT"]),
      pointCount: null,
      recommendedCarrier: null,
    });
  }

  const safetyReasons: string[] = [];
  if (!measurement.disposedCleanly) safetyReasons.push("DISPOSAL_NOT_PROVEN");
  if (!measurement.reducedMotionFallback) {
    safetyReasons.push("REDUCED_MOTION_FALLBACK_MISSING");
  }
  if (safetyReasons.length > 0) {
    return Object.freeze({
      outcome: "DENY",
      reasons: Object.freeze(safetyReasons),
      pointCount: measurement.pointCount,
      recommendedCarrier: "CLUSTERED_2D",
    });
  }

  const budget = BUDGETS[measurement.pointCount];
  const reasons: string[] = [];
  if (measurement.initializationMs > budget.initializationMs) {
    reasons.push("INITIALIZATION_BUDGET_EXCEEDED");
  }
  if (measurement.p95FrameMs > budget.p95FrameMs) {
    reasons.push("P95_FRAME_BUDGET_EXCEEDED");
  }
  if (measurement.mainThreadBlockMs > budget.mainThreadBlockMs) {
    reasons.push("MAIN_THREAD_BLOCK_BUDGET_EXCEEDED");
  }
  if (measurement.selectionLatencyMs > budget.selectionLatencyMs) {
    reasons.push("SELECTION_LATENCY_BUDGET_EXCEEDED");
  }
  if (measurement.peakMemoryMb > budget.peakMemoryMb) {
    reasons.push("PEAK_MEMORY_BUDGET_EXCEEDED");
  }

  if (reasons.length === 0) {
    return Object.freeze({
      outcome: "PASS",
      reasons: Object.freeze(["BUDGETS_SATISFIED"]),
      pointCount: measurement.pointCount,
      recommendedCarrier: "POINTS_3D",
    });
  }

  return Object.freeze({
    outcome: "HOLD",
    reasons: Object.freeze(reasons),
    pointCount: measurement.pointCount,
    recommendedCarrier:
      measurement.pointCount === 1_000_000
        ? "CLUSTERED_2D"
        : "DECIMATED_POINTS_3D",
  });
}
