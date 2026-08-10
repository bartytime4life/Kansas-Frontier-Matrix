/**
 * Strict fixture-only projection for the Pass 32 SSURGO yearly change viewer.
 *
 * The adapter accepts a pre-governed display projection. It does not fetch
 * NRCS data, compare records, resolve STAC or PROV objects, validate digests,
 * promote artifacts, or authorize release or publication.
 */

export const SOIL_YEARLY_CHANGE_PROJECTION_PROFILE =
  "kfm.explorer.ssurgo-yearly-change.fixture.v1" as const;

export type SoilYearlyChangeOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";
export type SoilYearlyChangeReasonCode =
  | "DIFF_AVAILABLE"
  | "DIFF_MISSING"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";

export type SoilSnapshotAnchor = Readonly<{
  datasetYear: number;
  artifactRef: string;
  artifactSha256: string;
  stacItemRef: string;
  provEntityRef: string;
  snapshotReceiptRef: string;
  validationReceiptRef: string;
}>;

export type SoilYearlyDiffSummary = Readonly<{
  computationProfile: "SSURGO_KEYED_RECORD_DIFF_V1";
  diffArtifactRef: string;
  diffArtifactSha256: string;
  addedRecords: number;
  removedRecords: number;
  modifiedRecords: number;
  changedPropertyNames: readonly string[];
  observedPropertyRelabelled: false;
}>;

export type SoilYearlyChangeProvenance = Readonly<{
  fetchActivityRef: string;
  validationActivityRef: string;
  diffActivityRef: string;
}>;

export type GovernedSoilYearlyChangeProjection = Readonly<{
  profile: typeof SOIL_YEARLY_CHANGE_PROJECTION_PROFILE;
  comparisonId: string;
  outcome: SoilYearlyChangeOutcome;
  reasonCode: SoilYearlyChangeReasonCode;
  status: "PROPOSED_INACTIVE";
  executionMode: "FIXTURE_ONLY";
  sourceFamily: "SSURGO" | null;
  supportType: "AUTHORITATIVE_STATIC_SOIL_SURVEY" | null;
  sourceDescriptorRef: string | null;
  previousSnapshot: SoilSnapshotAnchor | null;
  currentSnapshot: SoilSnapshotAnchor | null;
  diff: SoilYearlyDiffSummary | null;
  provenance: SoilYearlyChangeProvenance | null;
  publicationAuthorized: false;
}>;

export type SoilYearlyChangeProjectionResult =
  | Readonly<{ ok: true; payload: GovernedSoilYearlyChangeProjection }>
  | Readonly<{ ok: false; code: "MALFORMED_SOIL_YEARLY_CHANGE_PROJECTION" }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "comparison_id",
  "outcome",
  "reason_code",
  "status",
  "execution_mode",
  "source_family",
  "support_type",
  "source_descriptor_ref",
  "previous_snapshot",
  "current_snapshot",
  "diff",
  "provenance",
  "publication_authorized",
]);
const SNAPSHOT_FIELDS = new Set([
  "dataset_year",
  "artifact_ref",
  "artifact_sha256",
  "stac_item_ref",
  "prov_entity_ref",
  "snapshot_receipt_ref",
  "validation_receipt_ref",
]);
const DIFF_FIELDS = new Set([
  "computation_profile",
  "diff_artifact_ref",
  "diff_artifact_sha256",
  "added_records",
  "removed_records",
  "modified_records",
  "changed_property_names",
  "observed_property_relabelled",
]);
const PROVENANCE_FIELDS = new Set([
  "fetch_activity_ref",
  "validation_activity_ref",
  "diff_activity_ref",
]);
const OUTCOMES = new Set<SoilYearlyChangeOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<SoilYearlyChangeReasonCode>([
  "DIFF_AVAILABLE",
  "DIFF_MISSING",
  "POLICY_DENIED",
  "UPSTREAM_ERROR",
]);
const EXPECTED_REASON: Readonly<
  Record<SoilYearlyChangeOutcome, SoilYearlyChangeReasonCode>
> = Object.freeze({
  ANSWER: "DIFF_AVAILABLE",
  ABSTAIN: "DIFF_MISSING",
  DENY: "POLICY_DENIED",
  ERROR: "UPSTREAM_ERROR",
});

const COMPARISON_ID =
  /^kfm:ssurgo-yearly-change:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,270}$/;
const OPAQUE_REF = /^[A-Za-z][A-Za-z0-9+.-]*:[^\s]{1,300}$/;
const SHA256 = /^sha256:[a-f0-9]{64}$/;
const PROPERTY_NAME = /^[a-z][a-z0-9_]{1,63}$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;
const MAX_COUNT = 1_000_000;
const MAX_PROPERTIES = 64;

function malformed(): SoilYearlyChangeProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_SOIL_YEARLY_CHANGE_PROJECTION",
  });
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  fields: ReadonlySet<string>,
): boolean {
  return (
    Object.keys(value).length === fields.size &&
    Object.keys(value).every((field) => fields.has(field))
  );
}

function isReference(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= 320 &&
    OPAQUE_REF.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isDigest(value: unknown): value is string {
  return typeof value === "string" && SHA256.test(value);
}

function parseSnapshot(input: unknown): SoilSnapshotAnchor | null {
  if (!isRecord(input) || !hasExactFields(input, SNAPSHOT_FIELDS)) return null;
  if (
    !Number.isInteger(input.dataset_year) ||
    (input.dataset_year as number) < 1900 ||
    (input.dataset_year as number) > 2200 ||
    !isReference(input.artifact_ref) ||
    !isDigest(input.artifact_sha256) ||
    !isReference(input.stac_item_ref) ||
    !input.stac_item_ref.startsWith("stac://") ||
    !isReference(input.prov_entity_ref) ||
    !input.prov_entity_ref.startsWith("kfm://prov/entity/") ||
    !isReference(input.snapshot_receipt_ref) ||
    !input.snapshot_receipt_ref.startsWith("kfm://receipt/source-snapshot/") ||
    !isReference(input.validation_receipt_ref) ||
    !input.validation_receipt_ref.startsWith("kfm://receipt/validation/")
  ) {
    return null;
  }
  return Object.freeze({
    datasetYear: input.dataset_year as number,
    artifactRef: input.artifact_ref,
    artifactSha256: input.artifact_sha256,
    stacItemRef: input.stac_item_ref,
    provEntityRef: input.prov_entity_ref,
    snapshotReceiptRef: input.snapshot_receipt_ref,
    validationReceiptRef: input.validation_receipt_ref,
  });
}

function isBoundedCount(value: unknown): value is number {
  return Number.isInteger(value) && (value as number) >= 0 && (value as number) <= MAX_COUNT;
}

function parseDiff(input: unknown): SoilYearlyDiffSummary | null {
  if (!isRecord(input) || !hasExactFields(input, DIFF_FIELDS)) return null;
  if (
    input.computation_profile !== "SSURGO_KEYED_RECORD_DIFF_V1" ||
    !isReference(input.diff_artifact_ref) ||
    !isDigest(input.diff_artifact_sha256) ||
    !isBoundedCount(input.added_records) ||
    !isBoundedCount(input.removed_records) ||
    !isBoundedCount(input.modified_records) ||
    input.observed_property_relabelled !== false ||
    !Array.isArray(input.changed_property_names) ||
    input.changed_property_names.length > MAX_PROPERTIES ||
    !input.changed_property_names.every(
      (name) => typeof name === "string" && PROPERTY_NAME.test(name),
    )
  ) {
    return null;
  }
  const names = input.changed_property_names as string[];
  if (
    names.join("\u0000") !== [...new Set(names)].sort().join("\u0000") ||
    ((input.modified_records as number) === 0) !== (names.length === 0)
  ) {
    return null;
  }
  return Object.freeze({
    computationProfile: "SSURGO_KEYED_RECORD_DIFF_V1",
    diffArtifactRef: input.diff_artifact_ref,
    diffArtifactSha256: input.diff_artifact_sha256,
    addedRecords: input.added_records,
    removedRecords: input.removed_records,
    modifiedRecords: input.modified_records,
    changedPropertyNames: Object.freeze([...names]),
    observedPropertyRelabelled: false,
  });
}

function parseProvenance(input: unknown): SoilYearlyChangeProvenance | null {
  if (!isRecord(input) || !hasExactFields(input, PROVENANCE_FIELDS)) return null;
  if (
    !isReference(input.fetch_activity_ref) ||
    !input.fetch_activity_ref.startsWith("kfm://prov/activity/fetch/") ||
    !isReference(input.validation_activity_ref) ||
    !input.validation_activity_ref.startsWith("kfm://prov/activity/validation/") ||
    !isReference(input.diff_activity_ref) ||
    !input.diff_activity_ref.startsWith("kfm://prov/activity/diff/")
  ) {
    return null;
  }
  return Object.freeze({
    fetchActivityRef: input.fetch_activity_ref,
    validationActivityRef: input.validation_activity_ref,
    diffActivityRef: input.diff_activity_ref,
  });
}

/** Parse one exact, fixture-only SSURGO change projection. */
export function parseSoilYearlyChangeProjection(
  input: unknown,
): SoilYearlyChangeProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return malformed();
  }
  if (
    input.profile !== SOIL_YEARLY_CHANGE_PROJECTION_PROFILE ||
    typeof input.comparison_id !== "string" ||
    !COMPARISON_ID.test(input.comparison_id) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as SoilYearlyChangeOutcome) ||
    typeof input.reason_code !== "string" ||
    !REASON_CODES.has(input.reason_code as SoilYearlyChangeReasonCode) ||
    input.status !== "PROPOSED_INACTIVE" ||
    input.execution_mode !== "FIXTURE_ONLY" ||
    input.publication_authorized !== false
  ) {
    return malformed();
  }

  const outcome = input.outcome as SoilYearlyChangeOutcome;
  const reasonCode = input.reason_code as SoilYearlyChangeReasonCode;
  if (EXPECTED_REASON[outcome] !== reasonCode) return malformed();

  let previousSnapshot: SoilSnapshotAnchor | null = null;
  let currentSnapshot: SoilSnapshotAnchor | null = null;
  let diff: SoilYearlyDiffSummary | null = null;
  let provenance: SoilYearlyChangeProvenance | null = null;
  if (outcome === "ANSWER") {
    previousSnapshot = parseSnapshot(input.previous_snapshot);
    currentSnapshot = parseSnapshot(input.current_snapshot);
    diff = parseDiff(input.diff);
    provenance = parseProvenance(input.provenance);
    if (
      input.source_family !== "SSURGO" ||
      input.support_type !== "AUTHORITATIVE_STATIC_SOIL_SURVEY" ||
      input.source_descriptor_ref !== "data/registry/sources/soil/nrcs-ssurgo.yaml" ||
      previousSnapshot === null ||
      currentSnapshot === null ||
      currentSnapshot.datasetYear !== previousSnapshot.datasetYear + 1 ||
      previousSnapshot.artifactSha256 === currentSnapshot.artifactSha256 ||
      diff === null ||
      provenance === null
    ) {
      return malformed();
    }
  } else if (
    input.source_family !== null ||
    input.support_type !== null ||
    input.source_descriptor_ref !== null ||
    input.previous_snapshot !== null ||
    input.current_snapshot !== null ||
    input.diff !== null ||
    input.provenance !== null
  ) {
    return malformed();
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: SOIL_YEARLY_CHANGE_PROJECTION_PROFILE,
      comparisonId: input.comparison_id,
      outcome,
      reasonCode,
      status: "PROPOSED_INACTIVE",
      executionMode: "FIXTURE_ONLY",
      sourceFamily: outcome === "ANSWER" ? "SSURGO" : null,
      supportType:
        outcome === "ANSWER" ? "AUTHORITATIVE_STATIC_SOIL_SURVEY" : null,
      sourceDescriptorRef:
        outcome === "ANSWER"
          ? "data/registry/sources/soil/nrcs-ssurgo.yaml"
          : null,
      previousSnapshot,
      currentSnapshot,
      diff,
      provenance,
      publicationAuthorized: false,
    }),
  });
}
