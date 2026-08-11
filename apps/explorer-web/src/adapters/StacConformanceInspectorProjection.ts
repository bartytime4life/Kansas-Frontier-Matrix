/**
 * Strict public-safe projection for the Pass 31 STAC conformance inspector.
 *
 * The adapter consumes precomputed, closed validation summaries. It does not
 * query a STAC API, read a catalog, resolve references, validate source bytes,
 * mutate a collection, or authorize evidence, policy, release, or publication.
 */

export const STAC_CONFORMANCE_INSPECTOR_PROJECTION_PROFILE =
  "kfm.explorer.stac-conformance-inspector.public-safe.v1" as const;

export type StacConformanceInspectorOutcome =
  | "AVAILABLE"
  | "ABSTAIN"
  | "DENY"
  | "ERROR";

export type StacConformanceInspectorReasonCode =
  | "INSPECTION_AVAILABLE"
  | "INSPECTION_UNAVAILABLE"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";

export type StacInspectionState =
  | "CONFORMANT"
  | "NON_CONFORMANT"
  | "INCOMPLETE";

export type CheckStatus = "PASS" | "FAIL" | "NOT_EVALUATED";

export type StacConformanceClass = Readonly<{
  classId: "KFM_TRUST_EXTENSION_V1" | "STAC_1_0_0_ITEM";
  status: CheckStatus;
  checkedCount: number;
  findingCodes: readonly string[];
}>;

export type StacExtensionUse = Readonly<{
  extensionId: "kfm://profile/stac/kfm-profile-v1";
  status: "PRESENT_ALL" | "PRESENT_PARTIAL" | "ABSENT";
  itemCount: number;
}>;

export type StacIdentityRule = Readonly<{
  ruleId:
    | "COLLECTION_LINK_PRESENT"
    | "DATETIME_OR_INTERVAL_PRESENT"
    | "ITEM_ID_PATTERN"
    | "ITEM_ID_UNIQUE";
  status: CheckStatus;
  checkedCount: number;
  findingCodes: readonly string[];
}>;

export type StacMimeTypeCheck = Readonly<{
  mediaType: string;
  assetCount: number;
  status: CheckStatus;
  findingCodes: readonly string[];
}>;

export type StacCollectionContract = Readonly<{
  collectionRef: string;
  status: "COMPLETE" | "INCOMPLETE" | "NOT_EVALUATED";
  requiredFieldCount: number;
  presentFieldCount: number;
  findingCodes: readonly string[];
}>;

export type StacConformanceInspectorGovernance = Readonly<{
  networkAttempted: false;
  catalogQueryAttempted: false;
  catalogMutationAllowed: false;
  sourceAdmissionAllowed: false;
  evidenceAuthorityCreated: false;
  policyEvaluated: false;
  releaseAuthorized: false;
  publicationAllowed: false;
}>;

export type GovernedStacConformanceInspectorProjection = Readonly<{
  profile: typeof STAC_CONFORMANCE_INSPECTOR_PROJECTION_PROFILE;
  outcome: StacConformanceInspectorOutcome;
  reasonCode: StacConformanceInspectorReasonCode;
  evaluatedAt: string | null;
  inspectionId: string | null;
  specHash: string | null;
  profileVersion: "1.0.0-draft.1" | null;
  stacVersion: "1.0.0" | null;
  inspectionState: StacInspectionState | null;
  itemCount: number | null;
  conformanceClasses: readonly StacConformanceClass[];
  extensions: readonly StacExtensionUse[];
  identityRules: readonly StacIdentityRule[];
  mimeTypes: readonly StacMimeTypeCheck[];
  collectionContract: StacCollectionContract | null;
  governance: StacConformanceInspectorGovernance;
}>;

export type StacConformanceInspectorProjectionResult =
  | Readonly<{ ok: true; payload: GovernedStacConformanceInspectorProjection }>
  | Readonly<{
      ok: false;
      code: "MALFORMED_STAC_CONFORMANCE_INSPECTOR_PROJECTION";
    }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "outcome",
  "reason_code",
  "evaluated_at",
  "inspection_id",
  "spec_hash",
  "profile_version",
  "stac_version",
  "inspection_state",
  "item_count",
  "conformance_classes",
  "extensions",
  "identity_rules",
  "mime_types",
  "collection_contract",
  "governance",
]);
const CHECK_FIELDS = new Set([
  "class_id",
  "status",
  "checked_count",
  "finding_codes",
]);
const EXTENSION_FIELDS = new Set([
  "extension_id",
  "status",
  "item_count",
]);
const RULE_FIELDS = new Set([
  "rule_id",
  "status",
  "checked_count",
  "finding_codes",
]);
const MIME_FIELDS = new Set([
  "media_type",
  "asset_count",
  "status",
  "finding_codes",
]);
const COLLECTION_FIELDS = new Set([
  "collection_ref",
  "status",
  "required_field_count",
  "present_field_count",
  "finding_codes",
]);
const GOVERNANCE_FIELDS = new Set([
  "network_attempted",
  "catalog_query_attempted",
  "catalog_mutation_allowed",
  "source_admission_allowed",
  "evidence_authority_created",
  "policy_evaluated",
  "release_authorized",
  "publication_allowed",
]);

const OUTCOMES = new Set<StacConformanceInspectorOutcome>([
  "AVAILABLE",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const EXPECTED_REASON: Readonly<
  Record<StacConformanceInspectorOutcome, StacConformanceInspectorReasonCode>
> = Object.freeze({
  AVAILABLE: "INSPECTION_AVAILABLE",
  ABSTAIN: "INSPECTION_UNAVAILABLE",
  DENY: "POLICY_DENIED",
  ERROR: "UPSTREAM_ERROR",
});
const CHECK_STATUSES = new Set<CheckStatus>([
  "PASS",
  "FAIL",
  "NOT_EVALUATED",
]);
const CLASS_IDS = new Set([
  "KFM_TRUST_EXTENSION_V1",
  "STAC_1_0_0_ITEM",
]);
const RULE_IDS = new Set([
  "COLLECTION_LINK_PRESENT",
  "DATETIME_OR_INTERVAL_PRESENT",
  "ITEM_ID_PATTERN",
  "ITEM_ID_UNIQUE",
]);

const INSPECTION_ID = /^kfm:stac-conformance-inspection:[a-f0-9]{24}$/;
const SHA256 = /^sha256:[a-f0-9]{64}$/;
const COLLECTION_REF = /^kfm:\/\/catalog\/stac\/collection\/[a-z0-9][a-z0-9._/-]{2,190}$/;
const MEDIA_TYPE = /^[a-z0-9][a-z0-9!#$&^_.+-]{0,63}\/[a-z0-9][a-z0-9!#$&^_.+-]{0,95}$/;
const UPPER_CODE = /^[A-Z][A-Z0-9_]{2,63}$/;
const CANONICAL_TIMESTAMP = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;

function malformed(): StacConformanceInspectorProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_STAC_CONFORMANCE_INSPECTOR_PROJECTION",
  });
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  expected: ReadonlySet<string>,
): boolean {
  const keys = Object.keys(value);
  return keys.length === expected.size && keys.every((key) => expected.has(key));
}

function isString(
  value: unknown,
  pattern: RegExp,
  maxLength = 320,
): value is string {
  return (
    typeof value === "string" &&
    value.length <= maxLength &&
    value === value.trim() &&
    pattern.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isCount(value: unknown, maximum: number): value is number {
  return Number.isInteger(value) && (value as number) >= 0 && (value as number) <= maximum;
}

function isCanonicalTimestamp(value: unknown): value is string {
  if (typeof value !== "string" || !CANONICAL_TIMESTAMP.test(value)) return false;
  const parsed = new Date(value);
  return (
    Number.isFinite(parsed.getTime()) &&
    parsed.toISOString().replace(".000Z", "Z") === value
  );
}

function parseFindingCodes(value: unknown, status: CheckStatus): readonly string[] | null {
  if (!Array.isArray(value) || value.length > 16) return null;
  if (!value.every((item) => isString(item, UPPER_CODE, 64))) return null;
  const codes = value as string[];
  if (codes.join("\n") !== [...new Set(codes)].sort().join("\n")) return null;
  if (status === "PASS" && codes.length !== 0) return null;
  if (status !== "PASS" && codes.length === 0) return null;
  return Object.freeze([...codes]);
}

function parseGovernance(input: unknown): StacConformanceInspectorGovernance | null {
  if (!isRecord(input) || !hasExactFields(input, GOVERNANCE_FIELDS)) return null;
  if (
    input.network_attempted !== false ||
    input.catalog_query_attempted !== false ||
    input.catalog_mutation_allowed !== false ||
    input.source_admission_allowed !== false ||
    input.evidence_authority_created !== false ||
    input.policy_evaluated !== false ||
    input.release_authorized !== false ||
    input.publication_allowed !== false
  ) {
    return null;
  }
  return Object.freeze({
    networkAttempted: false,
    catalogQueryAttempted: false,
    catalogMutationAllowed: false,
    sourceAdmissionAllowed: false,
    evidenceAuthorityCreated: false,
    policyEvaluated: false,
    releaseAuthorized: false,
    publicationAllowed: false,
  });
}

function parseClass(input: unknown, itemCount: number): StacConformanceClass | null {
  if (!isRecord(input) || !hasExactFields(input, CHECK_FIELDS)) return null;
  if (
    typeof input.class_id !== "string" ||
    !CLASS_IDS.has(input.class_id) ||
    typeof input.status !== "string" ||
    !CHECK_STATUSES.has(input.status as CheckStatus) ||
    !isCount(input.checked_count, itemCount) ||
    input.checked_count !== itemCount
  ) {
    return null;
  }
  const status = input.status as CheckStatus;
  const findingCodes = parseFindingCodes(input.finding_codes, status);
  if (findingCodes === null) return null;
  return Object.freeze({
    classId: input.class_id as StacConformanceClass["classId"],
    status,
    checkedCount: input.checked_count,
    findingCodes,
  });
}

function parseExtension(input: unknown, itemCount: number): StacExtensionUse | null {
  if (!isRecord(input) || !hasExactFields(input, EXTENSION_FIELDS)) return null;
  if (
    input.extension_id !== "kfm://profile/stac/kfm-profile-v1" ||
    !["PRESENT_ALL", "PRESENT_PARTIAL", "ABSENT"].includes(String(input.status)) ||
    !isCount(input.item_count, itemCount)
  ) {
    return null;
  }
  if (
    (input.status === "PRESENT_ALL" && input.item_count !== itemCount) ||
    (input.status === "PRESENT_PARTIAL" &&
      (input.item_count === 0 || input.item_count === itemCount)) ||
    (input.status === "ABSENT" && input.item_count !== 0)
  ) {
    return null;
  }
  return Object.freeze({
    extensionId: "kfm://profile/stac/kfm-profile-v1",
    status: input.status as StacExtensionUse["status"],
    itemCount: input.item_count,
  });
}

function parseRule(input: unknown, itemCount: number): StacIdentityRule | null {
  if (!isRecord(input) || !hasExactFields(input, RULE_FIELDS)) return null;
  if (
    typeof input.rule_id !== "string" ||
    !RULE_IDS.has(input.rule_id) ||
    typeof input.status !== "string" ||
    !CHECK_STATUSES.has(input.status as CheckStatus) ||
    !isCount(input.checked_count, itemCount) ||
    input.checked_count !== itemCount
  ) {
    return null;
  }
  const status = input.status as CheckStatus;
  const findingCodes = parseFindingCodes(input.finding_codes, status);
  if (findingCodes === null) return null;
  return Object.freeze({
    ruleId: input.rule_id as StacIdentityRule["ruleId"],
    status,
    checkedCount: input.checked_count,
    findingCodes,
  });
}

function parseMime(input: unknown): StacMimeTypeCheck | null {
  if (!isRecord(input) || !hasExactFields(input, MIME_FIELDS)) return null;
  if (
    !isString(input.media_type, MEDIA_TYPE, 160) ||
    !isCount(input.asset_count, 10000) ||
    typeof input.status !== "string" ||
    !CHECK_STATUSES.has(input.status as CheckStatus)
  ) {
    return null;
  }
  const status = input.status as CheckStatus;
  const findingCodes = parseFindingCodes(input.finding_codes, status);
  if (findingCodes === null) return null;
  return Object.freeze({
    mediaType: input.media_type,
    assetCount: input.asset_count,
    status,
    findingCodes,
  });
}

function parseCollection(input: unknown): StacCollectionContract | null {
  if (!isRecord(input) || !hasExactFields(input, COLLECTION_FIELDS)) return null;
  if (
    !isString(input.collection_ref, COLLECTION_REF, 224) ||
    !["COMPLETE", "INCOMPLETE", "NOT_EVALUATED"].includes(String(input.status)) ||
    !isCount(input.required_field_count, 128) ||
    input.required_field_count < 1 ||
    !isCount(input.present_field_count, input.required_field_count)
  ) {
    return null;
  }
  const status = input.status as StacCollectionContract["status"];
  const findingStatus: CheckStatus = status === "COMPLETE" ? "PASS" : status === "INCOMPLETE" ? "FAIL" : "NOT_EVALUATED";
  const findingCodes = parseFindingCodes(input.finding_codes, findingStatus);
  if (
    findingCodes === null ||
    (status === "COMPLETE" && input.present_field_count !== input.required_field_count) ||
    (status === "INCOMPLETE" && input.present_field_count >= input.required_field_count)
  ) {
    return null;
  }
  return Object.freeze({
    collectionRef: input.collection_ref,
    status,
    requiredFieldCount: input.required_field_count,
    presentFieldCount: input.present_field_count,
    findingCodes,
  });
}

function expectedState(
  classes: readonly StacConformanceClass[],
  extensions: readonly StacExtensionUse[],
  rules: readonly StacIdentityRule[],
  mimeTypes: readonly StacMimeTypeCheck[],
  collection: StacCollectionContract,
): StacInspectionState {
  const statuses = [
    ...classes.map((item) => item.status),
    ...rules.map((item) => item.status),
    ...mimeTypes.map((item) => item.status),
  ];
  if (
    statuses.includes("FAIL") ||
    extensions.some((item) => item.status !== "PRESENT_ALL") ||
    collection.status === "INCOMPLETE"
  ) {
    return "NON_CONFORMANT";
  }
  if (
    classes.length !== CLASS_IDS.size ||
    rules.length !== RULE_IDS.size ||
    statuses.includes("NOT_EVALUATED") ||
    collection.status === "NOT_EVALUATED"
  ) {
    return "INCOMPLETE";
  }
  return "CONFORMANT";
}

function isCanonicalOrder<T>(items: readonly T[], key: (item: T) => string): boolean {
  const values = items.map(key);
  return values.join("\n") === [...new Set(values)].sort().join("\n");
}

/** Parse a closed STAC conformance summary and reject semantic drift. */
export function parseStacConformanceInspectorProjection(
  input: unknown,
): StacConformanceInspectorProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) return malformed();
  if (
    input.profile !== STAC_CONFORMANCE_INSPECTOR_PROJECTION_PROFILE ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as StacConformanceInspectorOutcome)
  ) {
    return malformed();
  }
  const outcome = input.outcome as StacConformanceInspectorOutcome;
  if (input.reason_code !== EXPECTED_REASON[outcome]) return malformed();
  const governance = parseGovernance(input.governance);
  if (
    governance === null ||
    !Array.isArray(input.conformance_classes) ||
    !Array.isArray(input.extensions) ||
    !Array.isArray(input.identity_rules) ||
    !Array.isArray(input.mime_types)
  ) {
    return malformed();
  }

  if (outcome !== "AVAILABLE") {
    if (
      input.evaluated_at !== null ||
      input.inspection_id !== null ||
      input.spec_hash !== null ||
      input.profile_version !== null ||
      input.stac_version !== null ||
      input.inspection_state !== null ||
      input.item_count !== null ||
      input.conformance_classes.length !== 0 ||
      input.extensions.length !== 0 ||
      input.identity_rules.length !== 0 ||
      input.mime_types.length !== 0 ||
      input.collection_contract !== null
    ) {
      return malformed();
    }
    return Object.freeze({
      ok: true,
      payload: Object.freeze({
        profile: STAC_CONFORMANCE_INSPECTOR_PROJECTION_PROFILE,
        outcome,
        reasonCode: EXPECTED_REASON[outcome],
        evaluatedAt: null,
        inspectionId: null,
        specHash: null,
        profileVersion: null,
        stacVersion: null,
        inspectionState: null,
        itemCount: null,
        conformanceClasses: Object.freeze([]) as readonly StacConformanceClass[],
        extensions: Object.freeze([]) as readonly StacExtensionUse[],
        identityRules: Object.freeze([]) as readonly StacIdentityRule[],
        mimeTypes: Object.freeze([]) as readonly StacMimeTypeCheck[],
        collectionContract: null,
        governance,
      }),
    });
  }

  if (
    !isCanonicalTimestamp(input.evaluated_at) ||
    !isString(input.inspection_id, INSPECTION_ID, 64) ||
    !isString(input.spec_hash, SHA256, 71) ||
    input.inspection_id.slice("kfm:stac-conformance-inspection:".length) !==
      input.spec_hash.slice("sha256:".length, "sha256:".length + 24) ||
    input.profile_version !== "1.0.0-draft.1" ||
    input.stac_version !== "1.0.0" ||
    !["CONFORMANT", "NON_CONFORMANT", "INCOMPLETE"].includes(String(input.inspection_state)) ||
    !isCount(input.item_count, 1000) ||
    input.item_count < 1 ||
    input.conformance_classes.length < 1 ||
    input.conformance_classes.length > 2 ||
    input.extensions.length !== 1 ||
    input.identity_rules.length < 1 ||
    input.identity_rules.length > 4 ||
    input.mime_types.length < 1 ||
    input.mime_types.length > 32
  ) {
    return malformed();
  }

  const itemCount = input.item_count as number;
  const classes = input.conformance_classes.map((item) => parseClass(item, itemCount));
  const extensions = input.extensions.map((item) =>
    parseExtension(item, itemCount),
  );
  const rules = input.identity_rules.map((item) => parseRule(item, itemCount));
  const mimeTypes = input.mime_types.map((item) => parseMime(item));
  const collection = parseCollection(input.collection_contract);
  if (
    classes.some((item) => item === null) ||
    extensions.some((item) => item === null) ||
    rules.some((item) => item === null) ||
    mimeTypes.some((item) => item === null) ||
    collection === null
  ) {
    return malformed();
  }

  const parsedClasses = classes as StacConformanceClass[];
  const parsedExtensions = extensions as StacExtensionUse[];
  const parsedRules = rules as StacIdentityRule[];
  const parsedMimeTypes = mimeTypes as StacMimeTypeCheck[];
  if (
    !isCanonicalOrder(parsedClasses, (item) => item.classId) ||
    !isCanonicalOrder(parsedRules, (item) => item.ruleId) ||
    !isCanonicalOrder(parsedMimeTypes, (item) => item.mediaType) ||
    input.inspection_state !==
      expectedState(
        parsedClasses,
        parsedExtensions,
        parsedRules,
        parsedMimeTypes,
        collection,
      )
  ) {
    return malformed();
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: STAC_CONFORMANCE_INSPECTOR_PROJECTION_PROFILE,
      outcome,
      reasonCode: EXPECTED_REASON[outcome],
      evaluatedAt: input.evaluated_at,
      inspectionId: input.inspection_id,
      specHash: input.spec_hash,
      profileVersion: "1.0.0-draft.1",
      stacVersion: "1.0.0",
      inspectionState: input.inspection_state as StacInspectionState,
      itemCount,
      conformanceClasses: Object.freeze(parsedClasses),
      extensions: Object.freeze(parsedExtensions),
      identityRules: Object.freeze(parsedRules),
      mimeTypes: Object.freeze(parsedMimeTypes),
      collectionContract: collection,
      governance,
    }),
  });
}
