/**
 * Strict public-safe projection for PMTiles range diagnostics.
 *
 * This adapter displays an already-bounded diagnostic result. It does not make
 * a Range request, read an archive, verify a signature, resolve a sidecar,
 * execute policy, run a renderer, or authorize artifact health or release.
 */

export const PMTILES_RANGE_DIAGNOSTICS_PROJECTION_PROFILE =
  "kfm.explorer.pmtiles-range-diagnostics.public-safe.v1" as const;

export type PmtilesRangeDiagnosticsOutcome =
  | "ANSWER"
  | "ABSTAIN"
  | "DENY"
  | "ERROR";

export type PmtilesRangeDiagnosticsReasonCode =
  | "DIAGNOSTICS_AVAILABLE"
  | "DIAGNOSTICS_UNAVAILABLE"
  | "VERIFICATION_DENIED"
  | "UPSTREAM_ERROR";

export type PmtilesVerificationState = "STRUCTURAL_HOLD";
export type AcceptRangesState = "SUPPORTED" | "MISSING";
export type ContentRangeState = "VALID" | "MISSING";
export type EtagState = "MATCH" | "MISSING";
export type CacheState = "HIT" | "MISS" | "BYPASS" | "UNKNOWN";
export type HeadlessRenderState = "PASS" | "HOLD" | "NOT_RUN";

export type PmtilesHttpDiagnostics = Readonly<{
  acceptRanges: AcceptRangesState;
  contentRange: ContentRangeState;
  etag: EtagState;
  cache: CacheState;
}>;

export type PmtilesSidecarDiagnostics = Readonly<{
  pmidxRef: string;
  pmidxState: "VERIFIED";
  pmsigRef: string;
  pmsigState: "SHAPE_BOUND";
  runReceiptRef: string;
  cryptographicState: "UNVERIFIED";
}>;

export type PmtilesVerifiedRange = Readonly<{
  offset: number;
  length: number;
  leaf: number;
}>;

export type PmtilesHeadlessRender = Readonly<{
  state: HeadlessRenderState;
  receiptRef: string | null;
}>;

export type PmtilesRangeDiagnosticsGovernance = Readonly<{
  networkAttempted: false;
  archiveReadPerformed: false;
  cryptographicVerificationPerformed: false;
  policyEvaluated: false;
  artifactHealthDeclared: false;
  releaseAuthorized: false;
  publicationAllowed: false;
}>;

export type GovernedPmtilesRangeDiagnosticsProjection = Readonly<{
  profile: typeof PMTILES_RANGE_DIAGNOSTICS_PROJECTION_PROFILE;
  panelId: string;
  outcome: PmtilesRangeDiagnosticsOutcome;
  reasonCode: PmtilesRangeDiagnosticsReasonCode;
  observedAt: string | null;
  artifactRef: string | null;
  verificationState: PmtilesVerificationState | null;
  http: PmtilesHttpDiagnostics | null;
  sidecars: PmtilesSidecarDiagnostics | null;
  verifiedRange: PmtilesVerifiedRange | null;
  checks: readonly string[];
  holds: readonly string[];
  headlessRender: PmtilesHeadlessRender | null;
  governance: PmtilesRangeDiagnosticsGovernance;
}>;

export type PmtilesRangeDiagnosticsProjectionResult =
  | Readonly<{ ok: true; payload: GovernedPmtilesRangeDiagnosticsProjection }>
  | Readonly<{ ok: false; code: "MALFORMED_PMTILES_RANGE_DIAGNOSTICS_PROJECTION" }>;

export const REQUIRED_CHECKS = Object.freeze([
  "PMIDX_DECLARED_RANGE_BINDING",
  "CAPTURED_RANGE_EQUALS_CONTAINING_LEAF_SLICE",
  "PMIDX_LEAF_SHA256_AND_MERKLE_ROOT",
  "PMSIG_SUBJECT_SHAPE_BINDING",
] as const);

export const REQUIRED_HOLDS = Object.freeze([
  "CRYPTOGRAPHIC_VERIFICATION_UNWIRED",
  "RANGE_METADATA_NOT_AUTHENTICATED",
  "BAO_OUTBOARD_PROOF_UNADOPTED",
  "FULL_ARCHIVE_DIGEST_NOT_RECOMPUTED",
  "POLICY_EVALUATION_NOT_RUN",
  "RELEASE_AUTHORIZATION_NOT_EVALUATED",
] as const);

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "panel_id",
  "outcome",
  "reason_code",
  "observed_at",
  "artifact_ref",
  "verification_state",
  "http",
  "sidecars",
  "verified_range",
  "checks",
  "holds",
  "headless_render",
  "governance",
]);
const HTTP_FIELDS = new Set([
  "accept_ranges",
  "content_range",
  "etag",
  "cache",
]);
const SIDECAR_FIELDS = new Set([
  "pmidx_ref",
  "pmidx_state",
  "pmsig_ref",
  "pmsig_state",
  "run_receipt_ref",
  "cryptographic_state",
]);
const RANGE_FIELDS = new Set(["offset", "length", "leaf"]);
const HEADLESS_FIELDS = new Set(["state", "receipt_ref"]);
const GOVERNANCE_FIELDS = new Set([
  "network_attempted",
  "archive_read_performed",
  "cryptographic_verification_performed",
  "policy_evaluated",
  "artifact_health_declared",
  "release_authorized",
  "publication_allowed",
]);

const OUTCOMES = new Set<PmtilesRangeDiagnosticsOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASONS = new Set<PmtilesRangeDiagnosticsReasonCode>([
  "DIAGNOSTICS_AVAILABLE",
  "DIAGNOSTICS_UNAVAILABLE",
  "VERIFICATION_DENIED",
  "UPSTREAM_ERROR",
]);
const EXPECTED_REASON: Readonly<
  Record<PmtilesRangeDiagnosticsOutcome, PmtilesRangeDiagnosticsReasonCode>
> = Object.freeze({
  ANSWER: "DIAGNOSTICS_AVAILABLE",
  ABSTAIN: "DIAGNOSTICS_UNAVAILABLE",
  DENY: "VERIFICATION_DENIED",
  ERROR: "UPSTREAM_ERROR",
});
const ACCEPT_RANGES = new Set<AcceptRangesState>(["SUPPORTED", "MISSING"]);
const CONTENT_RANGE = new Set<ContentRangeState>(["VALID", "MISSING"]);
const ETAG = new Set<EtagState>(["MATCH", "MISSING"]);
const CACHE = new Set<CacheState>(["HIT", "MISS", "BYPASS", "UNKNOWN"]);
const HEADLESS = new Set<HeadlessRenderState>(["PASS", "HOLD", "NOT_RUN"]);

const PANEL_ID = /^kfm:pmtiles-range-diagnostics:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,250}$/;
const KFM_REFERENCE = /^kfm:\/\/[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,315}$/;
const CANONICAL_TIMESTAMP = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;
const MAX_SAFE_INTEGER = Number.MAX_SAFE_INTEGER;

function malformed(): PmtilesRangeDiagnosticsProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_PMTILES_RANGE_DIAGNOSTICS_PROJECTION",
  });
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  expected: ReadonlySet<string>,
): boolean {
  return (
    Object.keys(value).length === expected.size &&
    Object.keys(value).every((field) => expected.has(field))
  );
}

function isIdentifier(value: unknown, pattern: RegExp, max = 320): value is string {
  return (
    typeof value === "string" &&
    value.length <= max &&
    value === value.trim() &&
    pattern.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isCanonicalTimestamp(value: unknown): value is string {
  if (typeof value !== "string" || !CANONICAL_TIMESTAMP.test(value)) return false;
  const parsed = new Date(value);
  return (
    Number.isFinite(parsed.getTime()) &&
    parsed.toISOString().replace(".000Z", "Z") === value
  );
}

function isInteger(value: unknown, minimum: number): value is number {
  return (
    typeof value === "number" &&
    Number.isSafeInteger(value) &&
    value >= minimum &&
    value <= MAX_SAFE_INTEGER
  );
}

function exactStringList(input: unknown, expected: readonly string[]): readonly string[] | null {
  if (
    !Array.isArray(input) ||
    input.length !== expected.length ||
    input.some((item, index) => item !== expected[index])
  ) {
    return null;
  }
  return Object.freeze([...expected]);
}

function parseGovernance(input: unknown): PmtilesRangeDiagnosticsGovernance | null {
  if (!isRecord(input) || !hasExactFields(input, GOVERNANCE_FIELDS)) return null;
  if (
    input.network_attempted !== false ||
    input.archive_read_performed !== false ||
    input.cryptographic_verification_performed !== false ||
    input.policy_evaluated !== false ||
    input.artifact_health_declared !== false ||
    input.release_authorized !== false ||
    input.publication_allowed !== false
  ) {
    return null;
  }
  return Object.freeze({
    networkAttempted: false,
    archiveReadPerformed: false,
    cryptographicVerificationPerformed: false,
    policyEvaluated: false,
    artifactHealthDeclared: false,
    releaseAuthorized: false,
    publicationAllowed: false,
  });
}

function parseHttp(input: unknown): PmtilesHttpDiagnostics | null {
  if (!isRecord(input) || !hasExactFields(input, HTTP_FIELDS)) return null;
  if (
    typeof input.accept_ranges !== "string" ||
    !ACCEPT_RANGES.has(input.accept_ranges as AcceptRangesState) ||
    typeof input.content_range !== "string" ||
    !CONTENT_RANGE.has(input.content_range as ContentRangeState) ||
    typeof input.etag !== "string" ||
    !ETAG.has(input.etag as EtagState) ||
    typeof input.cache !== "string" ||
    !CACHE.has(input.cache as CacheState)
  ) {
    return null;
  }
  return Object.freeze({
    acceptRanges: input.accept_ranges as AcceptRangesState,
    contentRange: input.content_range as ContentRangeState,
    etag: input.etag as EtagState,
    cache: input.cache as CacheState,
  });
}

function parseSidecars(input: unknown): PmtilesSidecarDiagnostics | null {
  if (!isRecord(input) || !hasExactFields(input, SIDECAR_FIELDS)) return null;
  if (
    !isIdentifier(input.pmidx_ref, KFM_REFERENCE) ||
    !input.pmidx_ref.startsWith("kfm://pmtiles/pmidx/") ||
    input.pmidx_state !== "VERIFIED" ||
    !isIdentifier(input.pmsig_ref, KFM_REFERENCE) ||
    !input.pmsig_ref.startsWith("kfm://pmtiles/pmsig/") ||
    input.pmsig_state !== "SHAPE_BOUND" ||
    !isIdentifier(input.run_receipt_ref, KFM_REFERENCE) ||
    !input.run_receipt_ref.startsWith("kfm://receipt/run/") ||
    input.cryptographic_state !== "UNVERIFIED"
  ) {
    return null;
  }
  return Object.freeze({
    pmidxRef: input.pmidx_ref,
    pmidxState: "VERIFIED",
    pmsigRef: input.pmsig_ref,
    pmsigState: "SHAPE_BOUND",
    runReceiptRef: input.run_receipt_ref,
    cryptographicState: "UNVERIFIED",
  });
}

function parseRange(input: unknown): PmtilesVerifiedRange | null {
  if (!isRecord(input) || !hasExactFields(input, RANGE_FIELDS)) return null;
  if (
    !isInteger(input.offset, 0) ||
    !isInteger(input.length, 1) ||
    !isInteger(input.leaf, 0) ||
    input.offset + input.length > MAX_SAFE_INTEGER
  ) {
    return null;
  }
  return Object.freeze({
    offset: input.offset,
    length: input.length,
    leaf: input.leaf,
  });
}

function parseHeadless(input: unknown): PmtilesHeadlessRender | null {
  if (!isRecord(input) || !hasExactFields(input, HEADLESS_FIELDS)) return null;
  if (typeof input.state !== "string" || !HEADLESS.has(input.state as HeadlessRenderState)) {
    return null;
  }
  const state = input.state as HeadlessRenderState;
  const receiptRef =
    input.receipt_ref === null
      ? null
      : isIdentifier(input.receipt_ref, KFM_REFERENCE) &&
          input.receipt_ref.startsWith("kfm://receipt/render/")
        ? input.receipt_ref
        : undefined;
  if (receiptRef === undefined) return null;
  if ((state === "NOT_RUN") !== (receiptRef === null)) return null;
  return Object.freeze({ state, receiptRef });
}

/** Parse one exact, bounded PMTiles diagnostic projection. */
export function parsePmtilesRangeDiagnosticsProjection(
  input: unknown,
): PmtilesRangeDiagnosticsProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) return malformed();
  if (
    input.profile !== PMTILES_RANGE_DIAGNOSTICS_PROJECTION_PROFILE ||
    !isIdentifier(input.panel_id, PANEL_ID) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as PmtilesRangeDiagnosticsOutcome) ||
    typeof input.reason_code !== "string" ||
    !REASONS.has(input.reason_code as PmtilesRangeDiagnosticsReasonCode)
  ) {
    return malformed();
  }
  const outcome = input.outcome as PmtilesRangeDiagnosticsOutcome;
  const reasonCode = input.reason_code as PmtilesRangeDiagnosticsReasonCode;
  if (EXPECTED_REASON[outcome] !== reasonCode) return malformed();
  const governance = parseGovernance(input.governance);
  if (governance === null) return malformed();

  if (outcome !== "ANSWER") {
    if (
      input.observed_at !== null ||
      input.artifact_ref !== null ||
      input.verification_state !== null ||
      input.http !== null ||
      input.sidecars !== null ||
      input.verified_range !== null ||
      !Array.isArray(input.checks) ||
      input.checks.length !== 0 ||
      !Array.isArray(input.holds) ||
      input.holds.length !== 0 ||
      input.headless_render !== null
    ) {
      return malformed();
    }
    return Object.freeze({
      ok: true,
      payload: Object.freeze({
        profile: PMTILES_RANGE_DIAGNOSTICS_PROJECTION_PROFILE,
        panelId: input.panel_id,
        outcome,
        reasonCode,
        observedAt: null,
        artifactRef: null,
        verificationState: null,
        http: null,
        sidecars: null,
        verifiedRange: null,
        checks: Object.freeze([]),
        holds: Object.freeze([]),
        headlessRender: null,
        governance,
      }),
    });
  }

  if (
    !isCanonicalTimestamp(input.observed_at) ||
    !isIdentifier(input.artifact_ref, KFM_REFERENCE) ||
    !input.artifact_ref.startsWith("kfm://artifact/pmtiles/") ||
    input.verification_state !== "STRUCTURAL_HOLD"
  ) {
    return malformed();
  }
  const http = parseHttp(input.http);
  const sidecars = parseSidecars(input.sidecars);
  const verifiedRange = parseRange(input.verified_range);
  const checks = exactStringList(input.checks, REQUIRED_CHECKS);
  const holds = exactStringList(input.holds, REQUIRED_HOLDS);
  const headlessRender = parseHeadless(input.headless_render);
  if (
    http === null ||
    sidecars === null ||
    verifiedRange === null ||
    checks === null ||
    holds === null ||
    headlessRender === null
  ) {
    return malformed();
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: PMTILES_RANGE_DIAGNOSTICS_PROJECTION_PROFILE,
      panelId: input.panel_id,
      outcome,
      reasonCode,
      observedAt: input.observed_at,
      artifactRef: input.artifact_ref,
      verificationState: "STRUCTURAL_HOLD",
      http,
      sidecars,
      verifiedRange,
      checks,
      holds,
      headlessRender,
      governance,
    }),
  });
}
