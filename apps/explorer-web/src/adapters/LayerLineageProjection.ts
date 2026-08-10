/**
 * Strict public-safe projection for the Pass 32 rollback/correction timeline.
 *
 * This adapter validates a bounded read model only. It does not resolve
 * manifests or receipts, execute rollback/correction, mutate lifecycle state,
 * authorize release, or publish artifacts.
 */

export const LAYER_LINEAGE_PROJECTION_PROFILE =
  "kfm.explorer.layer-lineage.public-safe.v1" as const;

export type LayerLineageOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";
export type LayerLineageReasonCode =
  | "LINEAGE_AVAILABLE"
  | "LINEAGE_MISSING"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";
export type LayerLineageEventType =
  | "RELEASED"
  | "CORRECTED"
  | "ROLLED_BACK"
  | "WITHDRAWN";

export type GovernedLayerLineageEntry = Readonly<{
  sequence: number;
  eventType: LayerLineageEventType;
  occurredAt: string;
  artifactDigest: string;
  releaseRef: string;
  correctionReceiptRef: string | null;
  rollbackTargetRef: string | null;
  supersedesDigest: string | null;
}>;

export type GovernedLayerLineageProjection = Readonly<{
  profile: typeof LAYER_LINEAGE_PROJECTION_PROFILE;
  timelineId: string;
  outcome: LayerLineageOutcome;
  reasonCode: LayerLineageReasonCode;
  layerRef: string | null;
  currentReleaseRef: string | null;
  currentState: LayerLineageEventType | null;
  entries: readonly GovernedLayerLineageEntry[];
}>;

export type LayerLineageProjectionResult =
  | Readonly<{ ok: true; payload: GovernedLayerLineageProjection }>
  | Readonly<{ ok: false; code: "MALFORMED_LAYER_LINEAGE_PROJECTION" }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "timeline_id",
  "outcome",
  "reason_code",
  "layer_ref",
  "current_release_ref",
  "current_state",
  "entries",
]);
const ENTRY_FIELDS = new Set([
  "sequence",
  "event_type",
  "occurred_at",
  "artifact_digest",
  "release_ref",
  "correction_receipt_ref",
  "rollback_target_ref",
  "supersedes_digest",
]);
const OUTCOMES = new Set<LayerLineageOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<LayerLineageReasonCode>([
  "LINEAGE_AVAILABLE",
  "LINEAGE_MISSING",
  "POLICY_DENIED",
  "UPSTREAM_ERROR",
]);
const EVENT_TYPES = new Set<LayerLineageEventType>([
  "RELEASED",
  "CORRECTED",
  "ROLLED_BACK",
  "WITHDRAWN",
]);
const EXPECTED_REASON: Readonly<Record<LayerLineageOutcome, LayerLineageReasonCode>> =
  Object.freeze({
    ANSWER: "LINEAGE_AVAILABLE",
    ABSTAIN: "LINEAGE_MISSING",
    DENY: "POLICY_DENIED",
    ERROR: "UPSTREAM_ERROR",
  });

const TIMELINE_ID = /^kfm:layer-lineage:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,280}$/;
const KFM_REFERENCE = /^kfm:(?:\/\/)?[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,315}$/;
const RELEASE_REF_PREFIX = ["kfm://release", "/"].join("");
const SHA256_DIGEST = /^sha256:[0-9a-f]{64}$/;
const UTC_SECOND = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;
const MAX_REFERENCE_LENGTH = 320;
const MAX_ENTRIES = 16;

function malformed(): LayerLineageProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_LAYER_LINEAGE_PROJECTION",
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

function isBoundedIdentifier(value: unknown, pattern: RegExp): value is string {
  return (
    typeof value === "string" &&
    value.length <= MAX_REFERENCE_LENGTH &&
    pattern.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isReferenceFamily(value: unknown, prefix: string): value is string {
  return isBoundedIdentifier(value, KFM_REFERENCE) && value.startsWith(prefix);
}

function parseNullableReference(value: unknown): string | null | undefined {
  if (value === null) return null;
  if (isBoundedIdentifier(value, KFM_REFERENCE)) return value;
  return undefined;
}

function parseNullableDigest(value: unknown): string | null | undefined {
  if (value === null) return null;
  if (typeof value === "string" && SHA256_DIGEST.test(value)) return value;
  return undefined;
}

function isCanonicalUtcSecond(value: unknown): value is string {
  if (typeof value !== "string" || !UTC_SECOND.test(value)) return false;
  const milliseconds = Date.parse(value);
  return (
    Number.isFinite(milliseconds) &&
    new Date(milliseconds).toISOString().replace(".000Z", "Z") === value
  );
}

function parseEntry(input: unknown): GovernedLayerLineageEntry | null {
  if (!isRecord(input) || !hasExactFields(input, ENTRY_FIELDS)) return null;
  if (
    !Number.isSafeInteger(input.sequence) ||
    (input.sequence as number) < 1 ||
    typeof input.event_type !== "string" ||
    !EVENT_TYPES.has(input.event_type as LayerLineageEventType) ||
    !isCanonicalUtcSecond(input.occurred_at) ||
    typeof input.artifact_digest !== "string" ||
    !SHA256_DIGEST.test(input.artifact_digest) ||
    !isReferenceFamily(input.release_ref, RELEASE_REF_PREFIX)
  ) {
    return null;
  }
  const correctionReceiptRef = parseNullableReference(
    input.correction_receipt_ref,
  );
  const rollbackTargetRef = parseNullableReference(input.rollback_target_ref);
  const supersedesDigest = parseNullableDigest(input.supersedes_digest);
  if (
    correctionReceiptRef === undefined ||
    rollbackTargetRef === undefined ||
    supersedesDigest === undefined ||
    (correctionReceiptRef !== null &&
      !correctionReceiptRef.startsWith("kfm://receipt/correction/")) ||
    (rollbackTargetRef !== null &&
      !rollbackTargetRef.startsWith(RELEASE_REF_PREFIX))
  ) {
    return null;
  }

  return Object.freeze({
    sequence: input.sequence as number,
    eventType: input.event_type as LayerLineageEventType,
    occurredAt: input.occurred_at,
    artifactDigest: input.artifact_digest,
    releaseRef: input.release_ref,
    correctionReceiptRef,
    rollbackTargetRef,
    supersedesDigest,
  });
}

function laterEntryIsConsistent(
  entry: GovernedLayerLineageEntry,
  previous: GovernedLayerLineageEntry,
  earlierByRelease: ReadonlyMap<string, GovernedLayerLineageEntry>,
): boolean {
  if (entry.eventType === "RELEASED") return false;
  if (entry.supersedesDigest !== previous.artifactDigest) return false;

  if (entry.eventType === "CORRECTED") {
    return (
      entry.correctionReceiptRef !== null &&
      entry.rollbackTargetRef === null &&
      entry.artifactDigest !== previous.artifactDigest
    );
  }

  if (entry.eventType === "ROLLED_BACK") {
    if (
      entry.correctionReceiptRef !== null ||
      entry.rollbackTargetRef === null ||
      entry.artifactDigest === previous.artifactDigest
    ) {
      return false;
    }
    const target = earlierByRelease.get(entry.rollbackTargetRef);
    return target !== undefined && target.artifactDigest === entry.artifactDigest;
  }

  if (
    entry.artifactDigest !== previous.artifactDigest ||
    (entry.correctionReceiptRef === null && entry.rollbackTargetRef === null)
  ) {
    return false;
  }
  return (
    entry.rollbackTargetRef === null ||
    earlierByRelease.has(entry.rollbackTargetRef)
  );
}

function parseEntries(input: unknown): readonly GovernedLayerLineageEntry[] | null {
  if (!Array.isArray(input) || input.length > MAX_ENTRIES) return null;
  const parsed: GovernedLayerLineageEntry[] = [];
  const releaseRefs = new Set<string>();
  const correctionRefs = new Set<string>();
  const earlierByRelease = new Map<string, GovernedLayerLineageEntry>();
  let previousMilliseconds = Number.NEGATIVE_INFINITY;

  for (let index = 0; index < input.length; index += 1) {
    const entry = parseEntry(input[index]);
    if (entry === null || entry.sequence !== index + 1) return null;
    const milliseconds = Date.parse(entry.occurredAt);
    if (milliseconds <= previousMilliseconds || releaseRefs.has(entry.releaseRef)) {
      return null;
    }
    if (
      entry.correctionReceiptRef !== null &&
      correctionRefs.has(entry.correctionReceiptRef)
    ) {
      return null;
    }

    if (index === 0) {
      if (
        entry.eventType !== "RELEASED" ||
        entry.correctionReceiptRef !== null ||
        entry.rollbackTargetRef !== null ||
        entry.supersedesDigest !== null
      ) {
        return null;
      }
    } else if (
      !laterEntryIsConsistent(entry, parsed[index - 1], earlierByRelease)
    ) {
      return null;
    }

    releaseRefs.add(entry.releaseRef);
    if (entry.correctionReceiptRef !== null) {
      correctionRefs.add(entry.correctionReceiptRef);
    }
    earlierByRelease.set(entry.releaseRef, entry);
    parsed.push(entry);
    previousMilliseconds = milliseconds;
  }
  return Object.freeze(parsed);
}

/** Parse one exact, chronological, public-safe layer lineage projection. */
export function parseLayerLineageProjection(
  input: unknown,
): LayerLineageProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return malformed();
  }
  if (
    input.profile !== LAYER_LINEAGE_PROJECTION_PROFILE ||
    !isBoundedIdentifier(input.timeline_id, TIMELINE_ID) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as LayerLineageOutcome) ||
    typeof input.reason_code !== "string" ||
    !REASON_CODES.has(input.reason_code as LayerLineageReasonCode)
  ) {
    return malformed();
  }

  const outcome = input.outcome as LayerLineageOutcome;
  const reasonCode = input.reason_code as LayerLineageReasonCode;
  if (EXPECTED_REASON[outcome] !== reasonCode) return malformed();

  const layerRef = parseNullableReference(input.layer_ref);
  const currentReleaseRef = parseNullableReference(input.current_release_ref);
  const currentState =
    input.current_state === null
      ? null
      : typeof input.current_state === "string" &&
          EVENT_TYPES.has(input.current_state as LayerLineageEventType)
        ? (input.current_state as LayerLineageEventType)
        : undefined;
  const entries = parseEntries(input.entries);
  if (
    layerRef === undefined ||
    currentReleaseRef === undefined ||
    currentState === undefined ||
    entries === null
  ) {
    return malformed();
  }

  const last = entries.at(-1);
  const positiveIsClosed =
    outcome === "ANSWER" &&
    layerRef?.startsWith("kfm://layer/") === true &&
    currentReleaseRef?.startsWith(RELEASE_REF_PREFIX) === true &&
    currentState !== null &&
    entries.length >= 1 &&
    last?.releaseRef === currentReleaseRef &&
    last.eventType === currentState;
  const negativeIsEmpty =
    outcome !== "ANSWER" &&
    layerRef === null &&
    currentReleaseRef === null &&
    currentState === null &&
    entries.length === 0;
  if (!positiveIsClosed && !negativeIsEmpty) return malformed();

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: LAYER_LINEAGE_PROJECTION_PROFILE,
      timelineId: input.timeline_id,
      outcome,
      reasonCode,
      layerRef,
      currentReleaseRef,
      currentState,
      entries,
    }),
  });
}
