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
  nearestNeighborEdges: boolean;
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
  if (!Number.isSafeInteger(value))) return 1;
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
      nearestNeighborEdges: pointCount !== 1_000_000,
      publicSafe: true as const,
      synthetic: true as const,
  }),
  );

  return Object.freeze({
    profile: SYNTHETIC_POINT_CLOUD_BENCHMARK_PROFILE,
    version: "1.0.0",
    cases: Object.freeze(cases),
    measurements: [
      "initialization_ms",
      "p95_frame_ms",
      "main_thread_block_ms",
      "selection_latency_ms",
      "peak_memory_mb",
      "disposed_cleanly",
      "reduced_motion_fallback",
    ] as const,
    authority: "NONE",
  });
}

/**
 * Generate one deterministic normalized sample without materializing the full
 * point set. A future harness may stream samples into an admitted renderer.
 */
export function sampleSyntheticPoint(seed: number, index: number): SyntheticPoint {
  const normalizedSeed = normalizeSeed(seed);
  const safeIndex = Number.isSafeInteger(index) && index >= 0 ? index : 0;
  let state = (normalizedSeed + safeIndex * 48_271) % 2_147_483_647;
  const next = (): number => {
    state = (state * 48_271) % 2_147_483_647;
    return state / 2_147_483_647;
  };
  return Object.freeze({
    x: Number((next() * 2 - 1).toFixed(9)),
    y: Number((next() * 2 - 1).toFixed(9)),
    z: Number((next() * 2 - 1).toFixed(9)),
  });
}

function parseMeasurement(
  value: unknown,
): PointCloudBenchmarkMeasurement | null {
  if (!isRecord(value) || !hasExactFields(value, MEASUREMENT_FIELDS)) {
    return null;
  }
  if (value.profile !== SYNTHETIC_POINT_CLOUD_BENCHMARK_PROFILE) return null;
  if (typeof value.caseId !== "string" || !SAFE_ID.test(value.caseId)) return null;
  if (typeof value.pointCount !== "number" || !COUNTS.has(value.pointCount)) {
    return null;
  }
  if (
    !finiteNonNegative(value.initializationMs) ||
    !finiteNonNegative(value.p95FrameMs) ||
    !finiteNonNegative(value.mainThreadBlockMs) ||
    !finiteNonNegative(value.selectionLatencyMs) ||
   !finiteNonNegative(value.peakMemoryMb)
  ) {
    return null;
  }
  if (
    typeof value.disposedCleanly !== "boolean" ||
    typeof value.reducedMotionFallback !== "boolean" ||
    value.synthetic !== true ||
    value.publicSafe !== true
  ) {
    return null;
  }

  return Object.freeze({
    profile: SYNTHETIC_POINT_CLOUD_BENCHMARK_PROFILE,
    caseId: value.caseId,
    pointCount: value.pointCount as SyntheticPointCount,
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

/** Evaluate benchmark evidence without claiming renderer or production readiness. */
export function evaluatePointCloudBenchmark(
  value: unknown,
): PointCloudBenchmarkOutcome {
  const measurement = parseMeasurement(value);
  if (measurement === null) {
    return Object.freeze({
      outcome: "ERROR",
      reasons: Object.freeze(["INVALID_MEASUREMENT"]),
      pointCount: null,
      recommendedCarrier: null,
    });
  }

  if (!measurement.disposedCleanly || !measurement.reducedMotionFallback) {
    const reasons = Object.freeze([
      ...(measurement.disposedCleanly ? [] : ["DISPOSAL_NOT_PROVEN"]),
      ...(measurement.reducedMotionFallback
        ? []
        : ["REDUCED_MOTION_FALLBACK_MISSING"]),
    ]);
    return Object.freeze({
      outcome: "DENY",
      reasons,
      pointCount: measurement.pointCount,
      recommendedCarrier: "CLUSTERED_2D",
    });
  }

  const budget = BUQMmµ•…ÍÕÉ•µ•¹Ğ¹Á½¥¹Ñ½Õ¹Ñtì(€½¹ÍĞÉ•…Í½¹ÌèÍÑÉ¥¹mt€ômtì(€¥˜€¡µ•…ÍÕÉ•µ•¹Ğ¹¥¹¥Ñ¥…±¥é…Ñ¥½¹5Ì€ø‰Õ‘•Ğ¹¥¹¥Ñ¥…±¥é…Ñ¥½¹5Ì¤ì(€€€É•…Í½¹Ì¹ÁÕÍ  ‰%9%Q%1%iQ%=9}	UQ}aˆ¤ì(€ô(€¥˜€¡µ•…ÍÕÉ•µ•¹Ğ¹ÀäÕÉ…µ•5Ì€ø‰Õ‘•Ğ¹ÀäÕÉ…µ•5Ì¤ì(€€€É•…Í½¹Ì¹ÁÕÍ  ‰I5}Q%5}	UQ}aˆ¤ì(€ô(€¥˜€¡µ•…ÍÕÉ•µ•¹Ğ¹µ…¥¹Q¡É•…‘	±½­5Ì€ø‰Õ‘•Ğ¹µ…¥¹Q¡É•…‘	±½­5Ì¤ì(€€€É•…Í½¹Ì¹ÁÕÍ  ‰5%9}Q!I}	UQ}aˆ¤ì(€ô(€¥˜€¡µ•…ÍÕÉ•µ•¹Ğ¹Í•±•Ñ¥½¹1…Ñ•¹å5Ì€ø‰Õ‘•Ğ¹Í•±•Ñ¥½¹1…Ñ•¹å5Ì¤ì(€€€É•…Í½¹Ì¹ÁÕÍ  ‰M1Q%=9}1Q9e}	UQ}aˆ¤ì(€ô(€¥˜€¡µ•…ÍÕÉ•µ•¹Ğ¹Á•…­5•µ½Éå5ˆ€ø‰Õ‘•Ğ¹Á•…­5•µ½Éå5ˆ¤ì(€€€É•…Í½¹Ì¹ÁÕÍ  ‰55=Ie}	UQ}aˆ¤ì(€ô((€¥˜€¡É•…Í½¹Ì¹±•¹Ñ €ôôô€À¤ì(€€€É•ÑÕÉ¸=‰©•Ğ¹™É••é”¡ì(€€€€€½ÕÑ½µ”è€‰AMLˆ°(€€€€€É•…Í½¹Ìè=‰©•Ğ¹™É••é”¡l‰	UQM}MQ%M%‰t¤°(€€€€€Á½¥¹Ñ½Õ¹Ğèµ•…ÍÕÉ•µ•¹Ğ¹Á½¥¹Ñ½Õ¹Ğ°(€€€€€É•½µµ•¹‘•‘…ÉÉ¥•Èè€‰A=%9QM|Íˆ°(€€€ô¤ì(€ô((€É•ÑÕÉ¸=‰©•Ğ¹™É••é”¡ì(€€€½ÕÑ½µ”è€‰!=1ˆ°(€€€É•…Í½¹Ìè=‰©•Ğ¹™É••é”¡É•…Í½¹Ì¤°(€€€Á½¥¹Ñ½Õ¹Ğèµ•…ÍÕÉ•µ•¹Ğ¹Á½¥¹Ñ½Õ¹Ğ°(€€€É•½µµ•¹‘•‘…ÉÉ¥•Èè(€€€€€µ•…ÍÕÉ•µ•¹Ğ¹Á½¥¹Ñ½Õ¹Ğ€ôôô€Å|ÀÀÁ|ÀÀÀ(€€€€€€€€ü€‰1UMQI|Éˆ(€€€€€€€€è€‰%5Q}A=%9QM|Íˆ°(€ô¤ì)ô(