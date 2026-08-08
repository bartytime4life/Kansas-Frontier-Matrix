import {
  EVIDENCE_DRAWER_PROJECTION_PROFILE,
  type EvidenceDrawerCitation,
  type EvidenceDrawerReasonCode,
} from "../../adapters/GovernedClient";
import { resolveEvidenceDrawer, type EvidenceDrawerViewModel } from "../evidence_drawer";
import {
  FOCUS_COMPOSED_CLAIM_PROJECTION_PROFILE,
  FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
  type FocusClosureOutcome,
  type FocusComposedClaimCitation,
  type FocusComposedClaimProjection,
  type FocusComposedClaimRequest,
  type FocusFreshnessState,
  type FocusOutcome,
  type FocusPolicyState,
  type FocusProjectionReasonCode,
  type FocusReleaseState,
  type FocusReviewState,
} from "./types";

const REQUEST_FIELDS = new Set([
  "profile",
  "request_id",
  "claim_id",
  "question",
  "allowed_evidence_refs",
]);
const PROJECTION_FIELDS = new Set([
  "profile",
  "request_id",
  "claim_id",
  "outcome",
  "reason_code",
  "closure_id",
  "closure_outcome",
  "answer",
  "evidence_refs",
  "citations",
  "resolved_roles",
  "unavailable_roles",
  "limitations",
  "policy",
  "review",
  "release",
  "freshness",
  "ai_receipt_ref",
  "evidence_drawer",
]);
const CITATION_FIELDS = new Set(["evidence_ref", "label", "href"]);
const SAFE_ID = /^[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}$/;
const SAFE_ROLE = /^[A-Z][A-Z0-9_]{0,63}$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;
const MAX_QUESTION_LENGTH = 320;
const MAX_ANSWER_LENGTH = 1600;
const MAX_ITEM_LENGTH = 320;
const MAX_ARRAY_ITEMS = 16;

const OUTCOMES = new Set<FocusOutcome>(["ANSWER", "ABSTAIN", "DENY", "ERROR"]);
const CLOSURE_OUTCOMES = new Set<FocusClosureOutcome>([
  "SUPPORTED",
  "QUALIFIED",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<FocusProjectionReasonCode>([
  "COMPOSED_CLAIM_SUPPORTED",
  "COMPOSED_CLAIM_QUALIFIED",
  "REQUIRED_DEPENDENCY_UNRESOLVED",
  "ALTERNATIVE_GROUP_UNRESOLVED",
  "POLICY_DENIED",
  "UPSTREAM_ERROR",
]);
const POLICY_STATES = new Set<FocusPolicyState>(["ALLOW", "ABSTAIN", "DENY", "ERROR"]);
const REVIEW_STATES = new Set<FocusReviewState>([
  "REVIEWED",
  "PENDING",
  "NOT_APPLICABLE",
]);
const RELEASE_STATES = new Set<FocusReleaseState>([
  "RELEASED",
  "UNRELEASED",
  "WITHDRAWN",
]);
const FRESHNESS_STATES = new Set<FocusFreshnessState>([
  "CURRENT",
  "STALE",
  "UNKNOWN",
]);

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  allowed: ReadonlySet<string>,
): boolean {
  const keys = Object.keys(value);
  return keys.length === allowed.size && keys.every((key) => allowed.has(key));
}

function isSafeId(value: unknown): value is string {
  return typeof value === "string" && SAFE_ID.test(value);
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

function parseUniqueIds(value: unknown): readonly string[] | null {
  if (!Array.isArray(value) || value.length > MAX_ARRAY_ITEMS) return null;
  if (!value.every(isSafeId) || new Set(value).size !== value.length) return null;
  return Object.freeze([...value]);
}

function parseRoles(value: unknown): readonly string[] | null {
  if (!Array.isArray(value) || value.length > MAX_ARRAY_ITEMS) return null;
  if (!value.every((item) => typeof item === "string" && SAFE_ROLE.test(item))) {
    return null;
  }
  if (new Set(value).size !== value.length) return null;
  return Object.freeze([...value]);
}

function parseBoundedStrings(value: unknown): readonly string[] | null {
  if (!Array.isArray(value) || value.length > MAX_ARRAY_ITEMS) return null;
  if (!value.every((item) => isBoundedString(item, MAX_ITEM_LENGTH))) return null;
  if (new Set(value).size !== value.length) return null;
  return Object.freeze([...value]);
}

function parseCitation(value: unknown): FocusComposedClaimCitation | null {
  if (!isRecord(value) || !hasExactFields(value, CITATION_FIELDS)) return null;
  if (!isSafeId(value.evidence_ref)) return null;
  if (!isBoundedString(value.label, 160) || !isBoundedString(value.href, MAX_ITEM_LENGTH)) {
    return null;
  }
  try {
    const href = new URL(value.href);
    if (href.protocol !== "https:" || href.username || href.password) return null;
  } catch {
    return null;
  }
  return Object.freeze({
    evidenceRef: value.evidence_ref,
    label: value.label,
    href: value.href,
  });
}

function parseCitations(value: unknown): readonly FocusComposedClaimCitation[] | null {
  if (!Array.isArray(value) || value.length > MAX_ARRAY_ITEMS) return null;
  const citations = value.map(parseCitation);
  if (citations.some((citation) => citation === null)) return null;
  const normalized = citations as FocusComposedClaimCitation[];
  if (new Set(normalized.map((item) => item.evidenceRef)).size !== normalized.length) {
    return null;
  }
  return Object.freeze(normalized);
}

function sameStringSet(left: readonly string[], right: readonly string[]): boolean {
  return (
    left.length === right.length &&
    left.every((item) => right.includes(item)) &&
    right.every((item) => left.includes(item))
  );
}

function citationsMatchDrawer(
  focusCitations: readonly FocusComposedClaimCitation[],
  drawerCitations: readonly EvidenceDrawerCitation[],
): boolean {
  return (
    focusCitations.length === drawerCitations.length &&
    focusCitations.every(
      (citation, index) =>
        citation.label === drawerCitations[index]?.label &&
        citation.href === drawerCitations[index]?.href,
    )
  );
}

export function parseFocusComposedClaimRequest(
  input: unknown,
): FocusComposedClaimRequest | null {
  if (!isRecord(input) || !hasExactFields(input, REQUEST_FIELDS)) return null;
  if (input.profile !== FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE) return null;
  if (!isSafeId(input.request_id) || !isSafeId(input.claim_id)) return null;
  if (!isBoundedString(input.question, MAX_QUESTION_LENGTH)) return null;
  const allowedEvidenceRefs = parseUniqueIds(input.allowed_evidence_refs);
  if (allowedEvidenceRefs === null) return null;
  return Object.freeze({
    profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
    requestId: input.request_id,
    claimId: input.claim_id,
    question: input.question,
    allowedEvidenceRefs,
  });
}

function projectionCombinationIsValid(
  projection: Omit<FocusComposedClaimProjection, "evidenceDrawerInput" | "evidenceDrawer">,
  drawer: EvidenceDrawerViewModel,
): boolean {
  const citationRefs = projection.citations.map((citation) => citation.evidenceRef);
  if (!sameStringSet(citationRefs, projection.evidenceRefs)) return false;
  if (!sameStringSet(drawer.evidenceRefs, projection.evidenceRefs)) return false;
  if (!citationsMatchDrawer(projection.citations, drawer.citations)) return false;

  if (projection.outcome === "ANSWER") {
    if (
      projection.answer === null ||
      projection.evidenceRefs.length === 0 ||
      projection.citations.length === 0 ||
      projection.resolvedRoles.length === 0 ||
      projection.policy !== "ALLOW" ||
      projection.review !== "REVIEWED" ||
      projection.release !== "RELEASED" ||
      projection.freshness !== "CURRENT" ||
      projection.aiReceiptRef === null ||
      drawer.outcome !== "ANSWER"
    ) {
      return false;
    }
    if (projection.closureOutcome === "SUPPORTED") {
      return (
        projection.reasonCode === "COMPOSED_CLAIM_SUPPORTED" &&
        projection.unavailableRoles.length === 0
      );
    }
    if (projection.closureOutcome === "QUALIFIED") {
      return (
        projection.reasonCode === "COMPOSED_CLAIM_QUALIFIED" &&
        projection.unavailableRoles.length > 0 &&
        projection.limitations.length > 0
      );
    }
    return false;
  }

  if (projection.answer !== null || projection.citations.length !== 0) return false;
  if (projection.outcome === "ABSTAIN") {
    return (
      projection.closureOutcome === "ABSTAIN" &&
      (projection.reasonCode === "REQUIRED_DEPENDENCY_UNRESOLVED" ||
        projection.reasonCode === "ALTERNATIVE_GROUP_UNRESOLVED") &&
      projection.policy === "ABSTAIN" &&
      projection.release !== "RELEASED" &&
      projection.unavailableRoles.length > 0 &&
      drawer.outcome === "ABSTAIN"
    );
  }
  if (projection.outcome === "DENY") {
    return (
      projection.closureOutcome === "DENY" &&
      projection.reasonCode === "POLICY_DENIED" &&
      projection.policy === "DENY" &&
      projection.release !== "RELEASED" &&
      projection.evidenceRefs.length === 0 &&
      projection.resolvedRoles.length === 0 &&
      projection.unavailableRoles.length === 0 &&
      drawer.outcome === "DENY"
    );
  }
  return (
    projection.closureOutcome === "ERROR" &&
    projection.reasonCode === "UPSTREAM_ERROR" &&
    projection.policy === "ERROR" &&
    projection.review === "NOT_APPLICABLE" &&
    projection.release === "UNRELEASED" &&
    projection.freshness === "UNKNOWN" &&
    projection.evidenceRefs.length === 0 &&
    projection.resolvedRoles.length === 0 &&
    projection.unavailableRoles.length === 0 &&
    drawer.outcome === "ERROR"
  );
}

export function makeNegativeDrawerProjection(
  id: string,
  outcome: "ABSTAIN" | "DENY" | "ERROR",
  reasonCode: EvidenceDrawerReasonCode,
): Readonly<Record<string, unknown>> {
  return Object.freeze({
    profile: EVIDENCE_DRAWER_PROJECTION_PROFILE,
    id: `kfm:drawer:focus:${id}`,
    outcome,
    reason_code: reasonCode,
    title:
      outcome === "ABSTAIN"
        ? "Focus evidence not sufficient"
        : outcome === "DENY"
          ? "Focus evidence restricted"
          : "Focus evidence unavailable",
    summary:
      outcome === "ABSTAIN"
        ? "Required evidence is not available for this composed claim."
        : outcome === "DENY"
          ? "Policy does not permit this evidence detail to be shown."
          : "The governed evidence service could not complete the request.",
    evidence_refs: Object.freeze([]),
    citations: Object.freeze([]),
    limitations: Object.freeze(["No unsupported claim is shown."]),
    trust_state: Object.freeze({
      source_role: "context",
      policy: outcome,
      review: "NOT_APPLICABLE",
      release: "UNRELEASED",
      freshness: "UNKNOWN",
      correction: "NONE",
    }),
    history: Object.freeze({
      negative_outcomes: Object.freeze([]),
      corrections: Object.freeze([]),
    }),
  });
}

export function parseFocusComposedClaimProjection(
  input: unknown,
): FocusComposedClaimProjection | null {
  if (!isRecord(input) || !hasExactFields(input, PROJECTION_FIELDS)) return null;
  if (input.profile !== FOCUS_COMPOSED_CLAIM_PROJECTION_PROFILE) return null;
  if (!isSafeId(input.request_id) || !isSafeId(input.claim_id) || !isSafeId(input.closure_id)) {
    return null;
  }
  if (typeof input.outcome !== "string" || !OUTCOMES.has(input.outcome as FocusOutcome)) {
    return null;
  }
  if (
    typeof input.reason_code !== "string" ||
    !REASON_CODES.has(input.reason_code as FocusProjectionReasonCode) ||
    typeof input.closure_outcome !== "string" ||
    !CLOSURE_OUTCOMES.has(input.closure_outcome as FocusClosureOutcome)
  ) {
    return null;
  }
  if (input.answer !== null && !isBoundedString(input.answer, MAX_ANSWER_LENGTH)) return null;

  const evidenceRefs = parseUniqueIds(input.evidence_refs);
  const citations = parseCitations(input.citations);
  const resolvedRoles = parseRoles(input.resolved_roles);
  const unavailableRoles = parseRoles(input.unavailable_roles);
  const limitations = parseBoundedStrings(input.limitations);
  if (
    evidenceRefs === null ||
    citations === null ||
    resolvedRoles === null ||
    unavailableRoles === null ||
    limitations === null ||
    resolvedRoles.some((role) => unavailableRoles.includes(role))
  ) {
    return null;
  }

  if (
    typeof input.policy !== "string" ||
    !POLICY_STATES.has(input.policy as FocusPolicyState) ||
    typeof input.review !== "string" ||
    !REVIEW_STATES.has(input.review as FocusReviewState) ||
    typeof input.release !== "string" ||
    !RELEASE_STATES.has(input.release as FocusReleaseState) ||
    typeof input.freshness !== "string" ||
    !FRESHNESS_STATES.has(input.freshness as FocusFreshnessState) ||
    (input.ai_receipt_ref !== null && !isSafeId(input.ai_receipt_ref))
  ) {
    return null;
  }

  const parsedEvidenceDrawer = resolveEvidenceDrawer(input.evidence_drawer);
  if (
    parsedEvidenceDrawer.code === "INVALID_PAYLOAD" ||
    parsedEvidenceDrawer.code === "NO_GOVERNED_RESPONSE"
  ) {
    return null;
  }

  const normalizedBase = Object.freeze({
    profile: FOCUS_COMPOSED_CLAIM_PROJECTION_PROFILE,
    requestId: input.request_id,
    claimId: input.claim_id,
    outcome: input.outcome as FocusOutcome,
    reasonCode: input.reason_code as FocusProjectionReasonCode,
    closureId: input.closure_id,
    closureOutcome: input.closure_outcome as FocusClosureOutcome,
    answer: input.answer as string | null,
    evidenceRefs,
    citations,
    resolvedRoles,
    unavailableRoles,
    limitations,
    policy: input.policy as FocusPolicyState,
    review: input.review as FocusReviewState,
    release: input.release as FocusReleaseState,
    freshness: input.freshness as FocusFreshnessState,
    aiReceiptRef: input.ai_receipt_ref as string | null,
  });
  if (!projectionCombinationIsValid(normalizedBase, parsedEvidenceDrawer)) return null;

  const evidenceDrawerInput =
    parsedEvidenceDrawer.outcome === "ANSWER"
      ? input.evidence_drawer
      : makeNegativeDrawerProjection(
          input.claim_id,
          parsedEvidenceDrawer.outcome,
          parsedEvidenceDrawer.code as EvidenceDrawerReasonCode,
        );
  const evidenceDrawer =
    parsedEvidenceDrawer.outcome === "ANSWER"
      ? parsedEvidenceDrawer
      : resolveEvidenceDrawer(evidenceDrawerInput);

  return Object.freeze({
    ...normalizedBase,
    evidenceDrawerInput,
    evidenceDrawer,
  });
}
