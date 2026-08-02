/**
 * Fixture-only governed payload adapter for the Explorer baseline.
 *
 * This module performs no network or lifecycle-store access. It validates one
 * deliberately small browser projection profile so feature code can fail
 * closed while the canonical EvidenceDrawerPayload schema-home decision
 * remains unresolved.
 */

export const EVIDENCE_DRAWER_PROJECTION_PROFILE =
  "kfm.explorer.evidence-drawer.public-safe.v1" as const;

export type EvidenceDrawerOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";

export type EvidenceDrawerReasonCode =
  | "SUPPORTED"
  | "MISSING_EVIDENCE"
  | "STALE_EVIDENCE"
  | "CITATION_UNRESOLVED"
  | "POLICY_DENIED"
  | "RIGHTS_UNRESOLVED"
  | "SENSITIVE_DETAIL_RESTRICTED"
  | "UPSTREAM_ERROR";

export type EvidenceDrawerCitation = Readonly<{
  label: string;
  href: string;
}>;

export type EvidenceDrawerTrustState = Readonly<{
  sourceRole: "authoritative" | "official" | "derived" | "context";
  policy: "ALLOW" | "ABSTAIN" | "DENY" | "ERROR";
  review: "REVIEWED" | "PENDING" | "NOT_APPLICABLE";
  release: "RELEASED" | "UNRELEASED" | "WITHDRAWN";
  freshness: "CURRENT" | "STALE" | "UNKNOWN";
  correction: "NONE" | "CURRENT" | "CORRECTED" | "SUPERSEDED";
}>;

export type GovernedEvidenceDrawerProjection = Readonly<{
  profile: typeof EVIDENCE_DRAWER_PROJECTION_PROFILE;
  id: string;
  outcome: EvidenceDrawerOutcome;
  reasonCode: EvidenceDrawerReasonCode;
  title: string;
  summary: string;
  evidenceRefs: readonly string[];
  citations: readonly EvidenceDrawerCitation[];
  limitations: readonly string[];
  trustState: EvidenceDrawerTrustState;
}>;

export type GovernedProjectionResult =
  | Readonly<{ ok: true; payload: GovernedEvidenceDrawerProjection }>
  | Readonly<{ ok: false; code: "MALFORMED_GOVERNED_PAYLOAD" }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "id",
  "outcome",
  "reason_code",
  "title",
  "summary",
  "evidence_refs",
  "citations",
  "limitations",
  "trust_state",
]);

const CITATION_FIELDS = new Set(["label", "href"]);
const TRUST_STATE_FIELDS = new Set([
  "source_role",
  "policy",
  "review",
  "release",
  "freshness",
  "correction",
]);

const OUTCOMES = new Set<EvidenceDrawerOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<EvidenceDrawerReasonCode>([
  "SUPPORTED",
  "MISSING_EVIDENCE",
  "STALE_EVIDENCE",
  "CITATION_UNRESOLVED",
  "POLICY_DENIED",
  "RIGHTS_UNRESOLVED",
  "SENSITIVE_DETAIL_RESTRICTED",
  "UPSTREAM_ERROR",
]);
const SOURCE_ROLES = new Set([
  "authoritative",
  "official",
  "derived",
  "context",
]);
const POLICY_STATES = new Set(["ALLOW", "ABSTAIN", "DENY", "ERROR"]);
const REVIEW_STATES = new Set(["REVIEWED", "PENDING", "NOT_APPLICABLE"]);
const RELEASE_STATES = new Set(["RELEASED", "UNRELEASED", "WITHDRAWN"]);
const FRESHNESS_STATES = new Set(["CURRENT", "STALE", "UNKNOWN"]);
const CORRECTION_STATES = new Set([
  "NONE",
  "CURRENT",
  "CORRECTED",
  "SUPERSEDED",
]);

const MAX_TITLE_LENGTH = 160;
const MAX_SUMMARY_LENGTH = 500;
const MAX_ITEM_LENGTH = 240;
const MAX_ARRAY_ITEMS = 16;
const SAFE_ID = /^[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  allowed: ReadonlySet<string>,
): boolean {
  return Object.keys(value).every((field) => allowed.has(field));
}

function isBoundedString(value: unknown, maximum: number): value is string {
  return (
    typeof value === "string" &&
    value.length > 0 &&
    value.length <= maximum &&
    value.trim() === value &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isSafeId(value: unknown): value is string {
  return typeof value === "string" && SAFE_ID.test(value);
}

function isStringArray(value: unknown): value is string[] {
  return (
    Array.isArray(value) &&
    value.length <= MAX_ARRAY_ITEMS &&
    value.every((item) => isBoundedString(item, MAX_ITEM_LENGTH))
  );
}

function parseCitation(value: unknown): EvidenceDrawerCitation | null {
  if (!isRecord(value) || !hasExactFields(value, CITATION_FIELDS)) return null;
  if (!isBoundedString(value.label, MAX_TITLE_LENGTH)) return null;
  if (!isBoundedString(value.href, MAX_ITEM_LENGTH)) return null;

  try {
    const href = new URL(value.href);
    if (href.protocol !== "https:" || href.username || href.password) return null;
  } catch {
    return null;
  }

  return Object.freeze({ label: value.label, href: value.href });
}

function parseCitations(value: unknown): readonly EvidenceDrawerCitation[] | null {
  if (!Array.isArray(value) || value.length > MAX_ARRAY_ITEMS) return null;
  const citations = value.map(parseCitation);
  if (citations.some((citation) => citation === null)) return null;
  return Object.freeze(citations as EvidenceDrawerCitation[]);
}

function parseTrustState(value: unknown): EvidenceDrawerTrustState | null {
  if (!isRecord(value) || !hasExactFields(value, TRUST_STATE_FIELDS)) return null;
  if (
    typeof value.source_role !== "string" ||
    !SOURCE_ROLES.has(value.source_role) ||
    typeof value.policy !== "string" ||
    !POLICY_STATES.has(value.policy) ||
    typeof value.review !== "string" ||
    !REVIEW_STATES.has(value.review) ||
    typeof value.release !== "string" ||
    !RELEASE_STATES.has(value.release) ||
    typeof value.freshness !== "string" ||
    !FRESHNESS_STATES.has(value.freshness) ||
    typeof value.correction !== "string" ||
    !CORRECTION_STATES.has(value.correction)
  ) {
    return null;
  }

  return Object.freeze({
    sourceRole: value.source_role as EvidenceDrawerTrustState["sourceRole"],
    policy: value.policy as EvidenceDrawerTrustState["policy"],
    review: value.review as EvidenceDrawerTrustState["review"],
    release: value.release as EvidenceDrawerTrustState["release"],
    freshness: value.freshness as EvidenceDrawerTrustState["freshness"],
    correction: value.correction as EvidenceDrawerTrustState["correction"],
  });
}

function outcomeCombinationIsValid(
  outcome: EvidenceDrawerOutcome,
  reasonCode: EvidenceDrawerReasonCode,
  evidenceRefs: readonly string[],
  citations: readonly EvidenceDrawerCitation[],
  trustState: EvidenceDrawerTrustState,
): boolean {
  if (outcome === "ANSWER") {
    return (
      reasonCode === "SUPPORTED" &&
      evidenceRefs.length > 0 &&
      citations.length > 0 &&
      trustState.policy === "ALLOW" &&
      trustState.review === "REVIEWED" &&
      trustState.release === "RELEASED" &&
      trustState.freshness === "CURRENT"
    );
  }

  if (outcome === "ABSTAIN") {
    return reasonCode !== "SUPPORTED" && trustState.policy === "ABSTAIN";
  }

  if (outcome === "DENY") {
    return (
      reasonCode !== "SUPPORTED" &&
      evidenceRefs.length === 0 &&
      citations.length === 0 &&
      trustState.policy === "DENY"
    );
  }

  return (
    reasonCode === "UPSTREAM_ERROR" &&
    evidenceRefs.length === 0 &&
    citations.length === 0 &&
    trustState.policy === "ERROR"
  );
}

/** Validate and normalize one bounded, fixture-only governed projection. */
export function parseEvidenceDrawerProjection(
  value: unknown,
): GovernedProjectionResult {
  const malformed = Object.freeze({
    ok: false as const,
    code: "MALFORMED_GOVERNED_PAYLOAD" as const,
  });

  if (!isRecord(value) || !hasExactFields(value, TOP_LEVEL_FIELDS)) return malformed;
  if (value.profile !== EVIDENCE_DRAWER_PROJECTION_PROFILE) return malformed;
  if (!isSafeId(value.id)) return malformed;
  if (typeof value.outcome !== "string" || !OUTCOMES.has(value.outcome as EvidenceDrawerOutcome)) {
    return malformed;
  }
  if (
    typeof value.reason_code !== "string" ||
    !REASON_CODES.has(value.reason_code as EvidenceDrawerReasonCode)
  ) {
    return malformed;
  }
  if (!isBoundedString(value.title, MAX_TITLE_LENGTH)) return malformed;
  if (!isBoundedString(value.summary, MAX_SUMMARY_LENGTH)) return malformed;
  if (!isStringArray(value.evidence_refs) || !value.evidence_refs.every(isSafeId)) {
    return malformed;
  }
  if (!isStringArray(value.limitations)) return malformed;

  const citations = parseCitations(value.citations);
  const trustState = parseTrustState(value.trust_state);
  if (citations === null || trustState === null) return malformed;

  const outcome = value.outcome as EvidenceDrawerOutcome;
  const reasonCode = value.reason_code as EvidenceDrawerReasonCode;
  if (
    !outcomeCombinationIsValid(
      outcome,
      reasonCode,
      value.evidence_refs,
      citations,
      trustState,
    )
  ) {
    return malformed;
  }

  const payload: GovernedEvidenceDrawerProjection = Object.freeze({
    profile: EVIDENCE_DRAWER_PROJECTION_PROFILE,
    id: value.id,
    outcome,
    reasonCode,
    title: value.title,
    summary: value.summary,
    evidenceRefs: Object.freeze([...value.evidence_refs]),
    citations,
    limitations: Object.freeze([...value.limitations]),
    trustState,
  });

  return Object.freeze({ ok: true, payload });
}
