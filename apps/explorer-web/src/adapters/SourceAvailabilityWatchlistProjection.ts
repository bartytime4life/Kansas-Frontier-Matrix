/**
 * Strict public-safe projection for the Pass 32 source availability watchlist.
 *
 * The adapter accepts a closed, display-only projection. It does not probe a
 * source, read a lifecycle store, resolve assessment references, create or
 * execute candidate work, evaluate policy, or authorize promotion/release.
 */

export const SOURCE_AVAILABILITY_WATCHLIST_PROJECTION_PROFILE =
  "kfm.explorer.source-availability-watchlist.public-safe.v1" as const;

export type SourceAvailabilityWatchlistOutcome =
  | "ANSWER"
  | "ABSTAIN"
  | "DENY"
  | "ERROR";

export type SourceAvailabilityWatchlistReasonCode =
  | "WATCHLIST_AVAILABLE"
  | "WATCHLIST_UNAVAILABLE"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";

export type WatchlistState =
  | "STABLE"
  | "REVIEW_REQUIRED"
  | "HOLD"
  | "ERROR";

export type SourceAvailability =
  | "HEALTHY"
  | "DEGRADED"
  | "STALE"
  | "UNAVAILABLE"
  | "UNKNOWN";

export type MaterialChangeClass =
  | "UNCHANGED"
  | "BYTE_ONLY"
  | "SEMANTIC_NON_MATERIAL"
  | "MATERIAL"
  | "UNDETERMINED"
  | "ERROR";

export type MaterialKind =
  | "NONE"
  | "SCHEMA"
  | "CONTENT"
  | "BOTH"
  | "UNDETERMINED"
  | "ERROR";

export type WatchlistRoute =
  | "NO_ACTION"
  | "REVIEW_CANDIDATE"
  | "HOLD"
  | "ERROR";

export type WatchlistEntryReasonCode =
  | "STABLE_AVAILABILITY"
  | "MATERIAL_SCHEMA_CHANGE"
  | "MATERIAL_CONTENT_CHANGE"
  | "MATERIAL_SCHEMA_AND_CONTENT_CHANGE"
  | "AVAILABILITY_UNRESOLVED"
  | "ASSESSMENT_ERROR";

export type SourceAvailabilityWatchlistEntry = Readonly<{
  sourceId: string;
  sourceRef: string;
  healthAssessmentRef: string;
  materialChangeAssessmentRef: string;
  availability: SourceAvailability;
  changeClass: MaterialChangeClass;
  materialKind: MaterialKind;
  route: WatchlistRoute;
  candidateWorkRef: string | null;
  reasonCodes: readonly WatchlistEntryReasonCode[];
}>;

export type SourceAvailabilityWatchlistSummary = Readonly<{
  sourceCount: number;
  stableCount: number;
  reviewCount: number;
  holdCount: number;
  errorCount: number;
}>;

export type SourceAvailabilityWatchlistGovernance = Readonly<{
  networkAttempted: false;
  sourceActivationAllowed: false;
  candidateExecutionAllowed: false;
  lifecycleWriteAllowed: false;
  authorityCreated: false;
  releaseAuthorized: false;
  publicationAllowed: false;
}>;

export type GovernedSourceAvailabilityWatchlistProjection = Readonly<{
  profile: typeof SOURCE_AVAILABILITY_WATCHLIST_PROJECTION_PROFILE;
  panelId: string;
  outcome: SourceAvailabilityWatchlistOutcome;
  reasonCode: SourceAvailabilityWatchlistReasonCode;
  observedAt: string | null;
  watchlistId: string | null;
  state: WatchlistState | null;
  summary: SourceAvailabilityWatchlistSummary | null;
  entries: readonly SourceAvailabilityWatchlistEntry[];
  governance: SourceAvailabilityWatchlistGovernance;
}>;

export type SourceAvailabilityWatchlistProjectionResult =
  | Readonly<{ ok: true; payload: GovernedSourceAvailabilityWatchlistProjection }>
  | Readonly<{ ok: false; code: "MALFORMED_SOURCE_AVAILABILITY_WATCHLIST_PROJECTION" }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "panel_id",
  "outcome",
  "reason_code",
  "observed_at",
  "watchlist_id",
  "state",
  "summary",
  "entries",
  "governance",
]);
const SUMMARY_FIELDS = new Set([
  "source_count",
  "stable_count",
  "review_count",
  "hold_count",
  "error_count",
]);
const ENTRY_FIELDS = new Set([
  "source_id",
  "source_ref",
  "health_assessment_ref",
  "material_change_assessment_ref",
  "availability",
  "change_class",
  "material_kind",
  "route",
  "candidate_work_ref",
  "reason_codes",
]);
const GOVERNANCE_FIELDS = new Set([
  "network_attempted",
  "source_activation_allowed",
  "candidate_execution_allowed",
  "lifecycle_write_allowed",
  "authority_created",
  "release_authorized",
  "publication_allowed",
]);

const OUTCOMES = new Set<SourceAvailabilityWatchlistOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<SourceAvailabilityWatchlistReasonCode>([
  "WATCHLIST_AVAILABLE",
  "WATCHLIST_UNAVAILABLE",
  "POLICY_DENIED",
  "UPSTREAM_ERROR",
]);
const EXPECTED_REASON: Readonly<
  Record<SourceAvailabilityWatchlistOutcome, SourceAvailabilityWatchlistReasonCode>
> = Object.freeze({
  ANSWER: "WATCHLIST_AVAILABLE",
  ABSTAIN: "WATCHLIST_UNAVAILABLE",
  DENY: "POLICY_DENIED",
  ERROR: "UPSTREAM_ERROR",
});
const STATES = new Set<WatchlistState>([
  "STABLE",
  "REVIEW_REQUIRED",
  "HOLD",
  "ERROR",
]);
const AVAILABILITY = new Set<SourceAvailability>([
  "HEALTHY",
  "DEGRADED",
  "STALE",
  "UNAVAILABLE",
  "UNKNOWN",
]);
const CHANGE_CLASSES = new Set<MaterialChangeClass>([
  "UNCHANGED",
  "BYTE_ONLY",
  "SEMANTIC_NON_MATERIAL",
  "MATERIAL",
  "UNDETERMINED",
  "ERROR",
]);
const MATERIAL_KINDS = new Set<MaterialKind>([
  "NONE",
  "SCHEMA",
  "CONTENT",
  "BOTH",
  "UNDETERMINED",
  "ERROR",
]);
const ROUTES = new Set<WatchlistRoute>([
  "NO_ACTION",
  "REVIEW_CANDIDATE",
  "HOLD",
  "ERROR",
]);
const ENTRY_REASON_CODES = new Set<WatchlistEntryReasonCode>([
  "STABLE_AVAILABILITY",
  "MATERIAL_SCHEMA_CHANGE",
  "MATERIAL_CONTENT_CHANGE",
  "MATERIAL_SCHEMA_AND_CONTENT_CHANGE",
  "AVAILABILITY_UNRESOLVED",
  "ASSESSMENT_ERROR",
]);

const PANEL_ID = /^kfm:source-availability-panel:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,250}$/;
const WATCHLIST_ID = /^kfm:source-availability-watchlist:[a-f0-9]{24}$/;
const SOURCE_ID = /^[a-z0-9][a-z0-9._-]{2,95}$/;
const KFM_REFERENCE = /^kfm:\/\/[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,315}$/;
const CANONICAL_TIMESTAMP = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;
const MAX_ENTRIES = 64;

function malformed(): SourceAvailabilityWatchlistProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_SOURCE_AVAILABILITY_WATCHLIST_PROJECTION",
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

function parseGovernance(input: unknown): SourceAvailabilityWatchlistGovernance | null {
  if (!isRecord(input) || !hasExactFields(input, GOVERNANCE_FIELDS)) return null;
  if (
    input.network_attempted !== false ||
    input.source_activation_allowed !== false ||
    input.candidate_execution_allowed !== false ||
    input.lifecycle_write_allowed !== false ||
    input.authority_created !== false ||
    input.release_authorized !== false ||
    input.publication_allowed !== false
  ) {
    return null;
  }
  return Object.freeze({
    networkAttempted: false,
    sourceActivationAllowed: false,
    candidateExecutionAllowed: false,
    lifecycleWriteAllowed: false,
    authorityCreated: false,
    releaseAuthorized: false,
    publicationAllowed: false,
  });
}

function parseReasonCodes(input: unknown): readonly WatchlistEntryReasonCode[] | null {
  if (!Array.isArray(input) || input.length !== 1) return null;
  const code = input[0];
  if (typeof code !== "string" || !ENTRY_REASON_CODES.has(code as WatchlistEntryReasonCode)) {
    return null;
  }
  return Object.freeze([code as WatchlistEntryReasonCode]);
}

function parseEntry(input: unknown): SourceAvailabilityWatchlistEntry | null {
  if (!isRecord(input) || !hasExactFields(input, ENTRY_FIELDS)) return null;
  if (
    !isIdentifier(input.source_id, SOURCE_ID, 96) ||
    !isIdentifier(input.source_ref, KFM_REFERENCE) ||
    input.source_ref !== `kfm://source/${input.source_id}` ||
    !isIdentifier(input.health_assessment_ref, KFM_REFERENCE) ||
    !input.health_assessment_ref.startsWith("kfm://source-health-assessment/") ||
    !isIdentifier(input.material_change_assessment_ref, KFM_REFERENCE) ||
    !input.material_change_assessment_ref.startsWith("kfm://material-change-assessment/") ||
    typeof input.availability !== "string" ||
    !AVAILABILITY.has(input.availability as SourceAvailability) ||
    typeof input.change_class !== "string" ||
    !CHANGE_CLASSES.has(input.change_class as MaterialChangeClass) ||
    typeof input.material_kind !== "string" ||
    !MATERIAL_KINDS.has(input.material_kind as MaterialKind) ||
    typeof input.route !== "string" ||
    !ROUTES.has(input.route as WatchlistRoute)
  ) {
    return null;
  }

  const reasonCodes = parseReasonCodes(input.reason_codes);
  const candidateWorkRef =
    input.candidate_work_ref === null
      ? null
      : isIdentifier(input.candidate_work_ref, KFM_REFERENCE) &&
          input.candidate_work_ref.startsWith("kfm://candidate-work/")
        ? input.candidate_work_ref
        : undefined;
  if (reasonCodes === null || candidateWorkRef === undefined) return null;

  const availability = input.availability as SourceAvailability;
  const changeClass = input.change_class as MaterialChangeClass;
  const materialKind = input.material_kind as MaterialKind;
  const route = input.route as WatchlistRoute;
  const reason = reasonCodes[0];

  const stable =
    ["UNCHANGED", "BYTE_ONLY", "SEMANTIC_NON_MATERIAL"].includes(changeClass) &&
    materialKind === "NONE" &&
    route === "NO_ACTION" &&
    candidateWorkRef === null &&
    reason === "STABLE_AVAILABILITY" &&
    !["UNAVAILABLE", "UNKNOWN"].includes(availability);
  const material =
    changeClass === "MATERIAL" &&
    ["SCHEMA", "CONTENT", "BOTH"].includes(materialKind) &&
    route === "REVIEW_CANDIDATE" &&
    candidateWorkRef !== null &&
    ((materialKind === "SCHEMA" && reason === "MATERIAL_SCHEMA_CHANGE") ||
      (materialKind === "CONTENT" && reason === "MATERIAL_CONTENT_CHANGE") ||
      (materialKind === "BOTH" &&
        reason === "MATERIAL_SCHEMA_AND_CONTENT_CHANGE")) &&
    !["UNAVAILABLE", "UNKNOWN"].includes(availability);
  const held =
    changeClass === "UNDETERMINED" &&
    materialKind === "UNDETERMINED" &&
    route === "HOLD" &&
    candidateWorkRef === null &&
    reason === "AVAILABILITY_UNRESOLVED";
  const errored =
    changeClass === "ERROR" &&
    materialKind === "ERROR" &&
    route === "ERROR" &&
    candidateWorkRef === null &&
    reason === "ASSESSMENT_ERROR";
  if (!stable && !material && !held && !errored) return null;

  return Object.freeze({
    sourceId: input.source_id,
    sourceRef: input.source_ref,
    healthAssessmentRef: input.health_assessment_ref,
    materialChangeAssessmentRef: input.material_change_assessment_ref,
    availability,
    changeClass,
    materialKind,
    route,
    candidateWorkRef,
    reasonCodes,
  });
}

function parseEntries(input: unknown): readonly SourceAvailabilityWatchlistEntry[] | null {
  if (!Array.isArray(input) || input.length < 1 || input.length > MAX_ENTRIES) return null;
  const entries: SourceAvailabilityWatchlistEntry[] = [];
  const sourceIds = new Set<string>();
  const healthRefs = new Set<string>();
  for (const candidate of input) {
    const entry = parseEntry(candidate);
    if (
      entry === null ||
      sourceIds.has(entry.sourceId) ||
      healthRefs.has(entry.healthAssessmentRef)
    ) {
      return null;
    }
    sourceIds.add(entry.sourceId);
    healthRefs.add(entry.healthAssessmentRef);
    entries.push(entry);
  }
  const sorted = [...entries].sort((left, right) => left.sourceId.localeCompare(right.sourceId));
  if (sorted.some((entry, index) => entry.sourceId !== entries[index]?.sourceId)) return null;
  return Object.freeze(entries);
}

function parseSummary(input: unknown): SourceAvailabilityWatchlistSummary | null {
  if (!isRecord(input) || !hasExactFields(input, SUMMARY_FIELDS)) return null;
  const values = [
    input.source_count,
    input.stable_count,
    input.review_count,
    input.hold_count,
    input.error_count,
  ];
  if (
    values.some(
      (value) =>
        typeof value !== "number" ||
        !Number.isInteger(value) ||
        value < 0 ||
        value > MAX_ENTRIES,
    )
  ) {
    return null;
  }
  return Object.freeze({
    sourceCount: input.source_count as number,
    stableCount: input.stable_count as number,
    reviewCount: input.review_count as number,
    holdCount: input.hold_count as number,
    errorCount: input.error_count as number,
  });
}

function deriveState(entries: readonly SourceAvailabilityWatchlistEntry[]): WatchlistState {
  if (entries.some((entry) => entry.route === "ERROR")) return "ERROR";
  if (entries.some((entry) => entry.route === "HOLD")) return "HOLD";
  if (entries.some((entry) => entry.route === "REVIEW_CANDIDATE")) {
    return "REVIEW_REQUIRED";
  }
  return "STABLE";
}

/** Parse one exact, bounded watchlist projection. */
export function parseSourceAvailabilityWatchlistProjection(
  input: unknown,
): SourceAvailabilityWatchlistProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) return malformed();
  if (
    input.profile !== SOURCE_AVAILABILITY_WATCHLIST_PROJECTION_PROFILE ||
    !isIdentifier(input.panel_id, PANEL_ID) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as SourceAvailabilityWatchlistOutcome) ||
    typeof input.reason_code !== "string" ||
    !REASON_CODES.has(input.reason_code as SourceAvailabilityWatchlistReasonCode)
  ) {
    return malformed();
  }
  const outcome = input.outcome as SourceAvailabilityWatchlistOutcome;
  const reasonCode = input.reason_code as SourceAvailabilityWatchlistReasonCode;
  if (EXPECTED_REASON[outcome] !== reasonCode) return malformed();

  const governance = parseGovernance(input.governance);
  if (governance === null) return malformed();

  if (outcome !== "ANSWER") {
    if (
      input.observed_at !== null ||
      input.watchlist_id !== null ||
      input.state !== null ||
      input.summary !== null ||
      !Array.isArray(input.entries) ||
      input.entries.length !== 0
    ) {
      return malformed();
    }
    return Object.freeze({
      ok: true,
      payload: Object.freeze({
        profile: SOURCE_AVAILABILITY_WATCHLIST_PROJECTION_PROFILE,
        panelId: input.panel_id,
        outcome,
        reasonCode,
        observedAt: null,
        watchlistId: null,
        state: null,
        summary: null,
        entries: Object.freeze([]),
        governance,
      }),
    });
  }

  if (
    !isCanonicalTimestamp(input.observed_at) ||
    !isIdentifier(input.watchlist_id, WATCHLIST_ID) ||
    typeof input.state !== "string" ||
    !STATES.has(input.state as WatchlistState)
  ) {
    return malformed();
  }
  const entries = parseEntries(input.entries);
  const summary = parseSummary(input.summary);
  if (entries === null || summary === null) return malformed();

  const stableCount = entries.filter((entry) => entry.route === "NO_ACTION").length;
  const reviewCount = entries.filter((entry) => entry.route === "REVIEW_CANDIDATE").length;
  const holdCount = entries.filter((entry) => entry.route === "HOLD").length;
  const errorCount = entries.filter((entry) => entry.route === "ERROR").length;
  if (
    summary.sourceCount !== entries.length ||
    summary.stableCount !== stableCount ||
    summary.reviewCount !== reviewCount ||
    summary.holdCount !== holdCount ||
    summary.errorCount !== errorCount ||
    summary.sourceCount !==
      summary.stableCount + summary.reviewCount + summary.holdCount + summary.errorCount ||
    input.state !== deriveState(entries)
  ) {
    return malformed();
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: SOURCE_AVAILABILITY_WATCHLIST_PROJECTION_PROFILE,
      panelId: input.panel_id,
      outcome,
      reasonCode,
      observedAt: input.observed_at,
      watchlistId: input.watchlist_id,
      state: input.state as WatchlistState,
      summary,
      entries,
      governance,
    }),
  });
}
