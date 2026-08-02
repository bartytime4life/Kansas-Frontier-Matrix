import {
  type EvidenceDrawerCitation,
  type EvidenceDrawerOutcome,
  type EvidenceDrawerReasonCode,
  type EvidenceDrawerTrustState,
  parseEvidenceDrawerProjection,
} from "../../adapters/GovernedClient";

export type EvidenceDrawerViewModel = Readonly<{
  outcome: EvidenceDrawerOutcome;
  code: EvidenceDrawerReasonCode | "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD";
  title: string;
  message: string;
  evidenceRefs: readonly string[];
  citations: readonly EvidenceDrawerCitation[];
  limitations: readonly string[];
  trustLabels: readonly string[];
  landmarkRole: "complementary";
  accessibilityLabel: string;
  ariaLive: "polite" | "assertive";
}>;

const EMPTY_STRINGS = Object.freeze([]) as readonly string[];
const EMPTY_CITATIONS = Object.freeze([]) as readonly EvidenceDrawerCitation[];

const SAFE_NEGATIVE_MESSAGES: Readonly<Record<EvidenceDrawerReasonCode, string>> =
  Object.freeze({
    SUPPORTED: "The governed evidence projection is available.",
    MISSING_EVIDENCE: "Required evidence is not available.",
    STALE_EVIDENCE: "Available evidence is stale for this request.",
    CITATION_UNRESOLVED: "One or more required citations could not be resolved.",
    POLICY_DENIED: "Policy does not permit this evidence detail to be shown.",
    RIGHTS_UNRESOLVED: "Source rights are not resolved for this evidence detail.",
    SENSITIVE_DETAIL_RESTRICTED: "Sensitive detail is restricted.",
    UPSTREAM_ERROR: "The governed evidence service could not complete the request.",
  });

function trustLabels(trustState: EvidenceDrawerTrustState): readonly string[] {
  return Object.freeze([
    `Source role: ${trustState.sourceRole}`,
    `Policy: ${trustState.policy}`,
    `Review: ${trustState.review}`,
    `Release: ${trustState.release}`,
    `Freshness: ${trustState.freshness}`,
    `Correction: ${trustState.correction}`,
  ]);
}

function fixedNegativeView(
  outcome: "ABSTAIN" | "DENY" | "ERROR",
  code: EvidenceDrawerReasonCode,
  evidenceRefs: readonly string[],
  labels: readonly string[],
): EvidenceDrawerViewModel {
  const title =
    outcome === "ABSTAIN"
      ? "Evidence not sufficient"
      : outcome === "DENY"
        ? "Evidence restricted"
        : "Evidence unavailable";

  return Object.freeze({
    outcome,
    code,
    title,
    message: SAFE_NEGATIVE_MESSAGES[code],
    evidenceRefs: outcome === "ABSTAIN" ? evidenceRefs : EMPTY_STRINGS,
    citations: EMPTY_CITATIONS,
    limitations: Object.freeze(["No unsupported claim is shown."]),
    trustLabels: labels,
    landmarkRole: "complementary",
    accessibilityLabel: `Evidence Drawer: ${outcome.toLowerCase()}`,
    ariaLive: outcome === "ERROR" ? "assertive" : "polite",
  });
}

/** Resolve a strict governed projection into a finite, no-leak UI state. */
export function resolveEvidenceDrawer(
  input?: unknown,
): EvidenceDrawerViewModel {
  if (input === undefined) {
    return Object.freeze({
      outcome: "ABSTAIN",
      code: "NO_GOVERNED_RESPONSE",
      title: "Evidence not available",
      message: "No governed evidence response is available.",
      evidenceRefs: EMPTY_STRINGS,
      citations: EMPTY_CITATIONS,
      limitations: Object.freeze(["No unsupported claim is shown."]),
      trustLabels: Object.freeze(["Evidence state: unavailable"]),
      landmarkRole: "complementary",
      accessibilityLabel: "Evidence Drawer: no governed response",
      ariaLive: "polite",
    });
  }

  const parsed = parseEvidenceDrawerProjection(input);
  if (!parsed.ok) {
    return Object.freeze({
      outcome: "ERROR",
      code: "INVALID_PAYLOAD",
      title: "Evidence unavailable",
      message: "The governed evidence response is invalid.",
      evidenceRefs: EMPTY_STRINGS,
      citations: EMPTY_CITATIONS,
      limitations: Object.freeze(["No partial or unsupported claim is shown."]),
      trustLabels: Object.freeze(["Evidence state: invalid payload"]),
      landmarkRole: "complementary",
      accessibilityLabel: "Evidence Drawer: invalid governed response",
      ariaLive: "assertive",
    });
  }

  const { payload } = parsed;
  const labels = trustLabels(payload.trustState);
  if (payload.outcome !== "ANSWER") {
    return fixedNegativeView(
      payload.outcome,
      payload.reasonCode,
      payload.evidenceRefs,
      labels,
    );
  }

  return Object.freeze({
    outcome: "ANSWER",
    code: payload.reasonCode,
    title: payload.title,
    message: payload.summary,
    evidenceRefs: payload.evidenceRefs,
    citations: payload.citations,
    limitations: payload.limitations,
    trustLabels: labels,
    landmarkRole: "complementary",
    accessibilityLabel: "Evidence Drawer: supported evidence",
    ariaLive: "polite",
  });
}
