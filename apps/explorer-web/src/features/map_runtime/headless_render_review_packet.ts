/**
 * Fixture-only builders for a headless PMTiles render review packet.
 *
 * These pure builders accept one already-completed synthetic browser probe and
 * produce bounded metrics and sidecar JSON. They perform no I/O, source access,
 * MapLibre boot, policy evaluation, release, deployment, or publication.
 */

export const HEADLESS_RENDER_REVIEW_METRICS_PROFILE =
  "kfm.pmtiles.headless-render-review-metrics.v1" as const;
export const HEADLESS_RENDER_REVIEW_SIDECAR_PROFILE =
  "kfm.pmtiles.headless-render-review-sidecar.v1" as const;

export const HEADLESS_RENDER_REVIEW_HOLDS = Object.freeze([
  "PUBLISHED_PMTILES_NOT_LOADED",
  "CRYPTOGRAPHIC_VERIFICATION_UNWIRED",
  "MAPLIBRE_RUNTIME_UNADMITTED",
  "STYLE_HEALTH_NOT_EVALUATED",
  "RELEASE_AUTHORIZATION_NOT_EVALUATED",
] as const);

const MOBILE_RESULT_HOLDS = Object.freeze([
  "CRYPTOGRAPHIC_VERIFICATION_UNWIRED",
  "MAPLIBRE_RUNTIME_UNADMITTED",
  "RELEASE_AUTHORIZATION_NOT_EVALUATED",
] as const);
const SHA256 = /^sha256:[a-f0-9]{64}$/;
const ZERO_HASH = `sha256:${"0".repeat(64)}`;
const INPUT_FIELDS = new Set([
  "archiveName",
  "externalRequestCount",
  "result",
  "render",
  "viewport",
  "browserHeadless",
]);
const RESULT_FIELDS = new Set([
  "outcome",
  "code",
  "authority",
  "holds",
  "maplibreBootState",
  "maplibreBootReason",
  "metrics",
]);
const RESULT_METRIC_FIELDS = new Set([
  "archiveBytes",
  "tileBytes",
  "verifyMs",
  "decodeRenderMs",
]);
const RENDER_FIELDS = new Set([
  "decoded",
  "rendered",
  "width",
  "height",
  "pixelRgba",
]);
const VIEWPORT_FIELDS = new Set([
  "width",
  "height",
  "deviceScaleFactor",
  "hasTouch",
  "isMobile",
]);
const SIDECAR_INPUT_FIELDS = new Set(["screenshotSha256", "metricsSha256"]);

export type HeadlessRenderReviewMetrics = Readonly<{
  profile: typeof HEADLESS_RENDER_REVIEW_METRICS_PROFILE;
  status: "PROPOSED_INACTIVE";
  execution_mode: "SYNTHETIC_FIXTURE_ONLY";
  outcome: "PASS";
  code: "HEADLESS_RENDER_REVIEW_PACKET_PASS";
  source_kind: "SYNTHETIC_FIXTURE";
  viewport: Readonly<{
    width: 390;
    height: 844;
    device_scale_factor: 3;
    has_touch: true;
    is_mobile: true;
  }>;
  browser: Readonly<{ engine: "chromium"; headless: true }>;
  archive: Readonly<{
    name: "mobile-base.pmtiles";
    archive_bytes: 347;
    tile_bytes: 70;
  }>;
  render: Readonly<{
    decoded: true;
    rendered: true;
    width: 1;
    height: 1;
    pixel_rgba: readonly [17, 34, 51, 255];
  }>;
  timing: Readonly<{
    verify_ms: number;
    decode_render_ms: number;
  }>;
  external_request_count: 0;
  maplibre_boot_state: "HOLD";
  style_health: "NOT_EVALUATED";
  publication_state: "NOT_EVALUATED";
  authority: "NONE";
  holds: typeof HEADLESS_RENDER_REVIEW_HOLDS;
}>;

export type HeadlessRenderReviewSidecar = Readonly<{
  profile: typeof HEADLESS_RENDER_REVIEW_SIDECAR_PROFILE;
  status: "PROPOSED_INACTIVE";
  execution_mode: "SYNTHETIC_FIXTURE_ONLY";
  source_kind: "SYNTHETIC_FIXTURE";
  artifacts: readonly [
    Readonly<{
      name: "headless-render.png";
      role: "SCREENSHOT";
      media_type: "image/png";
      sha256: string;
    }>,
    Readonly<{
      name: "metrics.json";
      role: "METRICS";
      media_type: "application/json";
      sha256: string;
    }>,
  ];
  maplibre_boot_state: "HOLD";
  style_health: "NOT_EVALUATED";
  publication_state: "NOT_EVALUATED";
  authority: "NONE";
  holds: typeof HEADLESS_RENDER_REVIEW_HOLDS;
  review_only: true;
}>;

export type HeadlessRenderReviewMetricsResult =
  | Readonly<{ ok: true; metrics: HeadlessRenderReviewMetrics }>
  | Readonly<{
      ok: false;
      code: "HEADLESS_RENDER_REVIEW_OBSERVATION_INVALID";
    }>;

export type HeadlessRenderReviewSidecarResult =
  | Readonly<{ ok: true; sidecar: HeadlessRenderReviewSidecar }>
  | Readonly<{
      ok: false;
      code: "HEADLESS_RENDER_REVIEW_DIGEST_INVALID";
    }>;

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

function exactArray(value: unknown, expected: readonly unknown[]): boolean {
  return (
    Array.isArray(value) &&
    value.length === expected.length &&
    value.every((item, index) => item === expected[index])
  );
}

function boundedTiming(value: unknown): value is number {
  return typeof value === "number" && Number.isFinite(value) && value >= 0 && value <= 2500;
}

function normalizeTiming(value: number): number {
  return Number(value.toFixed(3));
}

function validDigest(value: unknown): value is string {
  return typeof value === "string" && SHA256.test(value) && value !== ZERO_HASH;
}

/** Build deterministic review metrics from one bounded browser observation. */
export function buildHeadlessRenderReviewMetrics(
  input: unknown,
): HeadlessRenderReviewMetricsResult {
  if (!isRecord(input) || !hasExactFields(input, INPUT_FIELDS)) {
    return Object.freeze({
      ok: false,
      code: "HEADLESS_RENDER_REVIEW_OBSERVATION_INVALID",
    });
  }
  const result = input.result;
  const render = input.render;
  const viewport = input.viewport;
  if (
    input.archiveName !== "mobile-base.pmtiles" ||
    input.externalRequestCount !== 0 ||
    input.browserHeadless !== true ||
    !isRecord(result) ||
    !hasExactFields(result, RESULT_FIELDS) ||
    !isRecord(result.metrics) ||
    !hasExactFields(result.metrics, RESULT_METRIC_FIELDS) ||
    result.outcome !== "PASS" ||
    result.code !== "MOBILE_PMTILES_VERIFY_DECODE_RENDER_PASS" ||
    result.authority !== "NONE" ||
    result.maplibreBootState !== "HOLD" ||
    result.maplibreBootReason !== "MAPLIBRE_RUNTIME_UNADMITTED" ||
    !exactArray(result.holds, MOBILE_RESULT_HOLDS) ||
    result.metrics.archiveBytes !== 347 ||
    result.metrics.tileBytes !== 70 ||
    !boundedTiming(result.metrics.verifyMs) ||
    !boundedTiming(result.metrics.decodeRenderMs) ||
    !isRecord(render) ||
    !hasExactFields(render, RENDER_FIELDS) ||
    render.decoded !== true ||
    render.rendered !== true ||
    render.width !== 1 ||
    render.height !== 1 ||
    !exactArray(render.pixelRgba, [17, 34, 51, 255]) ||
    !isRecord(viewport) ||
    !hasExactFields(viewport, VIEWPORT_FIELDS) ||
    viewport.width !== 390 ||
    viewport.height !== 844 ||
    viewport.deviceScaleFactor !== 3 ||
    viewport.hasTouch !== true ||
    viewport.isMobile !== true
  ) {
    return Object.freeze({
      ok: false,
      code: "HEADLESS_RENDER_REVIEW_OBSERVATION_INVALID",
    });
  }

  return Object.freeze({
    ok: true,
    metrics: Object.freeze({
      profile: HEADLESS_RENDER_REVIEW_METRICS_PROFILE,
      status: "PROPOSED_INACTIVE",
      execution_mode: "SYNTHETIC_FIXTURE_ONLY",
      outcome: "PASS",
      code: "HEADLESS_RENDER_REVIEW_PACKET_PASS",
      source_kind: "SYNTHETIC_FIXTURE",
      viewport: Object.freeze({
        width: 390,
        height: 844,
        device_scale_factor: 3,
        has_touch: true,
        is_mobile: true,
      }),
      browser: Object.freeze({ engine: "chromium", headless: true }),
      archive: Object.freeze({
        name: "mobile-base.pmtiles",
        archive_bytes: 347,
        tile_bytes: 70,
      }),
      render: Object.freeze({
        decoded: true,
        rendered: true,
        width: 1,
        height: 1,
        pixel_rgba: Object.freeze([17, 34, 51, 255] as const),
      }),
      timing: Object.freeze({
        verify_ms: normalizeTiming(result.metrics.verifyMs),
        decode_render_ms: normalizeTiming(result.metrics.decodeRenderMs),
      }),
      external_request_count: 0,
      maplibre_boot_state: "HOLD",
      style_health: "NOT_EVALUATED",
      publication_state: "NOT_EVALUATED",
      authority: "NONE",
      holds: HEADLESS_RENDER_REVIEW_HOLDS,
    }),
  });
}

/** Bind screenshot and metrics bytes into a review-only sidecar. */
export function buildHeadlessRenderReviewSidecar(
  input: unknown,
): HeadlessRenderReviewSidecarResult {
  if (
    !isRecord(input) ||
    !hasExactFields(input, SIDECAR_INPUT_FIELDS) ||
    !validDigest(input.screenshotSha256) ||
    !validDigest(input.metricsSha256) ||
    input.screenshotSha256 === input.metricsSha256
  ) {
    return Object.freeze({
      ok: false,
      code: "HEADLESS_RENDER_REVIEW_DIGEST_INVALID",
    });
  }

  const artifacts: HeadlessRenderReviewSidecar["artifacts"] = Object.freeze([
    Object.freeze({
      name: "headless-render.png",
      role: "SCREENSHOT",
      media_type: "image/png",
      sha256: input.screenshotSha256,
    }),
    Object.freeze({
      name: "metrics.json",
      role: "METRICS",
      media_type: "application/json",
      sha256: input.metricsSha256,
    }),
  ]);
  return Object.freeze({
    ok: true,
    sidecar: Object.freeze({
      profile: HEADLESS_RENDER_REVIEW_SIDECAR_PROFILE,
      status: "PROPOSED_INACTIVE",
      execution_mode: "SYNTHETIC_FIXTURE_ONLY",
      source_kind: "SYNTHETIC_FIXTURE",
      artifacts,
      maplibre_boot_state: "HOLD",
      style_health: "NOT_EVALUATED",
      publication_state: "NOT_EVALUATED",
      authority: "NONE",
      holds: HEADLESS_RENDER_REVIEW_HOLDS,
      review_only: true,
    }),
  });
}
