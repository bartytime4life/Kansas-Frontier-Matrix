export const OCI_ARTIFACT_BROWSER_PROFILE =
  "kfm.explorer.oci-artifact-browser.fixture.v1" as const;

export type OciArtifactBrowserOutcome =
  | "ANSWER"
  | "ABSTAIN"
  | "DENY"
  | "ERROR";

export type OciArtifactBrowserReasonCode =
  | "ARTIFACTS_AVAILABLE"
  | "ARTIFACTS_MISSING"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";

export type OciReferrerKind = "SIGNATURE" | "PROVENANCE" | "SBOM";
export type OciReferrerRecordedState = "PRESENT_UNVERIFIED" | "ABSENT";

export type GovernedOciReferrer = Readonly<{
  kind: OciReferrerKind;
  artifactRef: string | null;
  subjectDigest: string;
  recordedState: OciReferrerRecordedState;
}>;

export type GovernedOciArtifact = Readonly<{
  tag: string;
  tagRef: string;
  digest: string;
  artifactRef: string;
  mediaType:
    | "application/vnd.pmtiles"
    | "application/vnd.apache.parquet"
    | "application/vnd.oci.image.manifest.v1+json";
  sizeBytes: number;
  referrers: readonly GovernedOciReferrer[];
}>;

export type GovernedOciArtifactBrowserProjection = Readonly<{
  profile: typeof OCI_ARTIFACT_BROWSER_PROFILE;
  browserId: string;
  outcome: OciArtifactBrowserOutcome;
  reasonCode: OciArtifactBrowserReasonCode;
  registryScope: string | null;
  reviewedAt: string | null;
  artifacts: readonly GovernedOciArtifact[];
  rollbackCandidateRef: string | null;
}>;

export type OciArtifactBrowserProjectionResult =
  | Readonly<{ ok: true; payload: GovernedOciArtifactBrowserProjection }>
  | Readonly<{
      ok: false;
      code: "MALFORMED_OCI_ARTIFACT_BROWSER_PROJECTION";
    }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "browser_id",
  "outcome",
  "reason_code",
  "status",
  "execution_mode",
  "registry_scope",
  "reviewed_at",
  "artifacts",
  "rollback_candidate_ref",
  "governance",
]);
const ARTIFACT_FIELDS = new Set([
  "tag",
  "tag_ref",
  "digest",
  "artifact_ref",
  "media_type",
  "size_bytes",
  "referrers",
]);
const REFERRER_FIELDS = new Set([
  "kind",
  "artifact_ref",
  "subject_digest",
  "recorded_state",
]);
const GOVERNANCE_FIELDS = new Set([
  "registry_contacted",
  "signature_verification_performed",
  "rollback_authorized",
  "release_authorized",
  "publication_authorized",
  "public_use_allowed",
]);

const OUTCOMES = new Set<OciArtifactBrowserOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<OciArtifactBrowserReasonCode>([
  "ARTIFACTS_AVAILABLE",
  "ARTIFACTS_MISSING",
  "POLICY_DENIED",
  "UPSTREAM_ERROR",
]);
const EXPECTED_REASON: Readonly<
  Record<OciArtifactBrowserOutcome, OciArtifactBrowserReasonCode>
> = Object.freeze({
  ANSWER: "ARTIFACTS_AVAILABLE",
  ABSTAIN: "ARTIFACTS_MISSING",
  DENY: "POLICY_DENIED",
  ERROR: "UPSTREAM_ERROR",
});
const MEDIA_TYPES = new Set<GovernedOciArtifact["mediaType"]>([
  "application/vnd.pmtiles",
  "application/vnd.apache.parquet",
  "application/vnd.oci.image.manifest.v1+json",
]);
const REFERRER_KINDS = new Set<OciReferrerKind>([
  "SIGNATURE",
  "PROVENANCE",
  "SBOM",
]);
const RECORDED_STATES = new Set<OciReferrerRecordedState>([
  "PRESENT_UNVERIFIED",
  "ABSENT",
]);
const REFERRER_ORDER: readonly OciReferrerKind[] = Object.freeze([
  "SIGNATURE",
  "PROVENANCE",
  "SBOM",
]);

const MAX_REFERENCE_LENGTH = 512;
const BROWSER_ID =
  /^kfm:oci-artifact-browser:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,460}$/;
const OCI_SCOPE =
  /^oci:\/\/[a-z0-9.-]+(?::[0-9]{1,5})?\/[a-z0-9]+(?:[._/-][a-z0-9]+)*$/;
const OCI_TAG = /^[A-Za-z0-9_][A-Za-z0-9._-]{0,127}$/;
const SHA256 = /^sha256:[0-9a-f]{64}$/;
const UTC_SECOND = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;

function malformed(): OciArtifactBrowserProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_OCI_ARTIFACT_BROWSER_PROJECTION",
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

function isBrowserId(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= MAX_REFERENCE_LENGTH &&
    BROWSER_ID.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isScope(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= MAX_REFERENCE_LENGTH &&
    OCI_SCOPE.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isDigest(value: unknown): value is string {
  return typeof value === "string" && SHA256.test(value);
}

function isDigestPinnedRef(value: unknown): value is string {
  if (typeof value !== "string" || value.length > MAX_REFERENCE_LENGTH) {
    return false;
  }
  const parts = value.split("@");
  return (
    parts.length === 2 &&
    isScope(parts[0]) &&
    isDigest(parts[1]) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isCanonicalUtcSecond(value: unknown): value is string {
  if (typeof value !== "string" || !UTC_SECOND.test(value)) return false;
  const milliseconds = Date.parse(value);
  return (
    Number.isFinite(milliseconds) &&
    new Date(milliseconds).toISOString().replace(".000Z", "Z") === value
  );
}

function parseReferrer(
  value: unknown,
  subjectDigest: string,
): GovernedOciReferrer | null {
  if (!isRecord(value) || !hasExactFields(value, REFERRER_FIELDS)) return null;
  if (
    typeof value.kind !== "string" ||
    !REFERRER_KINDS.has(value.kind as OciReferrerKind) ||
    typeof value.recorded_state !== "string" ||
    !RECORDED_STATES.has(value.recorded_state as OciReferrerRecordedState) ||
    value.subject_digest !== subjectDigest
  ) {
    return null;
  }
  const kind = value.kind as OciReferrerKind;
  const recordedState = value.recorded_state as OciReferrerRecordedState;
  if (
    (recordedState === "PRESENT_UNVERIFIED" &&
      !isDigestPinnedRef(value.artifact_ref)) ||
    (recordedState === "ABSENT" && value.artifact_ref !== null)
  ) {
    return null;
  }
  return Object.freeze({
    kind,
    artifactRef:
      recordedState === "PRESENT_UNVERIFIED"
        ? (value.artifact_ref as string)
        : null,
    subjectDigest,
    recordedState,
  });
}

function parseArtifact(
  value: unknown,
  registryScope: string,
): GovernedOciArtifact | null {
  if (!isRecord(value) || !hasExactFields(value, ARTIFACT_FIELDS)) return null;
  if (
    typeof value.tag !== "string" ||
    !OCI_TAG.test(value.tag) ||
    !isDigest(value.digest) ||
    value.tag_ref !== `${registryScope}:${value.tag}` ||
    value.artifact_ref !== `${registryScope}@${value.digest}` ||
    typeof value.media_type !== "string" ||
    !MEDIA_TYPES.has(value.media_type as GovernedOciArtifact["mediaType"]) ||
    !Number.isSafeInteger(value.size_bytes) ||
    (value.size_bytes as number) < 1 ||
    (value.size_bytes as number) > 10_000_000_000 ||
    !Array.isArray(value.referrers) ||
    value.referrers.length < 1 ||
    value.referrers.length > REFERRER_ORDER.length
  ) {
    return null;
  }

  const referrers: GovernedOciReferrer[] = [];
  for (const candidate of value.referrers) {
    const referrer = parseReferrer(candidate, value.digest);
    if (referrer === null) return null;
    referrers.push(referrer);
  }
  const kinds = referrers.map((referrer) => referrer.kind);
  const expectedKinds = REFERRER_ORDER.filter((kind) => kinds.includes(kind));
  if (
    kinds.length !== new Set(kinds).size ||
    kinds.some((kind, index) => kind !== expectedKinds[index]) ||
    !referrers.some(
      (referrer) =>
        referrer.kind === "SIGNATURE" &&
        referrer.recordedState === "PRESENT_UNVERIFIED",
    )
  ) {
    return null;
  }

  return Object.freeze({
    tag: value.tag,
    tagRef: value.tag_ref as string,
    digest: value.digest,
    artifactRef: value.artifact_ref as string,
    mediaType: value.media_type as GovernedOciArtifact["mediaType"],
    sizeBytes: value.size_bytes as number,
    referrers: Object.freeze(referrers),
  });
}

function governanceIsFalse(value: unknown): boolean {
  return (
    isRecord(value) &&
    hasExactFields(value, GOVERNANCE_FIELDS) &&
    [...GOVERNANCE_FIELDS].every((field) => value[field] === false)
  );
}

/** Parse one exact synthetic, governed OCI artifact review projection. */
export function parseOciArtifactBrowserProjection(
  input: unknown,
): OciArtifactBrowserProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return malformed();
  }
  if (
    input.profile !== OCI_ARTIFACT_BROWSER_PROFILE ||
    input.status !== "PROPOSED_INACTIVE" ||
    input.execution_mode !== "FIXTURE_ONLY" ||
    !isBrowserId(input.browser_id) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as OciArtifactBrowserOutcome) ||
    typeof input.reason_code !== "string" ||
    !REASON_CODES.has(input.reason_code as OciArtifactBrowserReasonCode) ||
    !governanceIsFalse(input.governance)
  ) {
    return malformed();
  }

  const outcome = input.outcome as OciArtifactBrowserOutcome;
  const reasonCode = input.reason_code as OciArtifactBrowserReasonCode;
  if (EXPECTED_REASON[outcome] !== reasonCode || !Array.isArray(input.artifacts)) {
    return malformed();
  }

  if (outcome !== "ANSWER") {
    if (
      input.registry_scope !== null ||
      input.reviewed_at !== null ||
      input.artifacts.length !== 0 ||
      input.rollback_candidate_ref !== null
    ) {
      return malformed();
    }
    return Object.freeze({
      ok: true,
      payload: Object.freeze({
        profile: OCI_ARTIFACT_BROWSER_PROFILE,
        browserId: input.browser_id,
        outcome,
        reasonCode,
        registryScope: null,
        reviewedAt: null,
        artifacts: Object.freeze([]),
        rollbackCandidateRef: null,
      }),
    });
  }

  if (
    !isScope(input.registry_scope) ||
    !isCanonicalUtcSecond(input.reviewed_at) ||
    input.artifacts.length < 1 ||
    input.artifacts.length > 32 ||
    !isDigestPinnedRef(input.rollback_candidate_ref)
  ) {
    return malformed();
  }
  const registryScope = input.registry_scope;
  const artifacts: GovernedOciArtifact[] = [];
  for (const candidate of input.artifacts) {
    const artifact = parseArtifact(candidate, registryScope);
    if (artifact === null) return malformed();
    artifacts.push(artifact);
  }
  const tags = artifacts.map((artifact) => artifact.tag);
  const digests = artifacts.map((artifact) => artifact.digest);
  const refs = artifacts.map((artifact) => artifact.artifactRef);
  if (
    tags.length !== new Set(tags).size ||
    digests.length !== new Set(digests).size ||
    refs.length !== new Set(refs).size ||
    !refs.includes(input.rollback_candidate_ref)
  ) {
    return malformed();
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: OCI_ARTIFACT_BROWSER_PROFILE,
      browserId: input.browser_id,
      outcome,
      reasonCode,
      registryScope,
      reviewedAt: input.reviewed_at,
      artifacts: Object.freeze(artifacts),
      rollbackCandidateRef: input.rollback_candidate_ref,
    }),
  });
}
