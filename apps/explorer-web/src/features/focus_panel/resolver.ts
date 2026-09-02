import type { EvidenceDrawerReasonCode } from "../../adapters/GovernedClient";
import {
  makeNegativeDrawerProjection,
  parseFocusComposedClaimProjection,
  parseFocusComposedClaimRequest,
} from "./parsers";
import type {
  FocusComposedClaimCitation,
  FocusComposedClaimProjection,
  FocusComposedClaimRequest,
  FocusComposedClaimResolution,
  FocusComposedClaimViewModel,
  FocusProjectionReasonCode,
  FocusResolutionCode,
  GovernedFocusComposedClaimResolver,
} from "./types";

const EMPTY_STRINGS = Object.freeze([]) as readonly string[];
const EMPTY_CITATIONS = Object.freeze([]) as readonly FocusComposedClaimCitation[];

type LocalCode = Exclude<FocusResolutionCode, FocusProjectionReasonCode>;

function localView(
  code: LocalCode,
  outcome: "ABSTAIN" | "ERROR",
): FocusComposedClaimViewModel {
  const drawerInput = makeNegativeDrawerProjection(
    `local-${code.toLowerCase()}`,
    outcome,
    (outcome === "ABSTAIN" ? "MISSING_EVIDENCE" : "UPSTREAM_ERROR") as EvidenceDrawerReasonCode,
  );
  return Object.freeze({
    outcome,
    code,
    title: outcome === "ABSTAIN" ? "Focus answer not supported" : "Focus answer unavailable",
    message:
      outcome === "ABSTAIN"
        ? "The composed claim does not have sufficient released evidence support."
        : "The governed Focus service could not complete the request.",
    claimId: null,
    closureId: null,
    closureOutcome: outcome,
    evidenceRefs: EMPTY_STRINGS,
    citations: EMPTY_CITATIONS,
    dependencyLabels: EMPTY_STRINGS,
    limitations: Object.freeze(["No unsupported claim is shown."]),
    aiReceiptLabel: null,
    evidenceDrawerInput: drawerInput,
    accessibilityLabel: `Focus Panel: ${outcome.toLowerCase()}`,
    ariaLive: outcome === "ERROR" ? "assertive" : "polite",
  });
}

function projectionView(
  projection: FocusComposedClaimProjection,
): FocusComposedClaimViewModel {
  const isAnswer = projection.outcome === "ANSWER";
  const dependencyLabels =
    projection.outcome === "DENY" || projection.outcome === "ERROR"
      ? EMPTY_STRINGS
      : Object.freeze([
          ...projection.resolvedRoles.map((role) => `Resolved role: ${role}`),
          ...projection.unavailableRoles.map((role) =>
            projection.outcome === "ANSWER"
              ? `Unavailable optional role: ${role}`
              : `Unresolved role: ${role}`,
          ),
        ]);

  const title = isAnswer
    ? projection.closureOutcome === "QUALIFIED"
      ? "Qualified composed claim"
      : "Supported composed claim"
    : projection.outcome === "ABSTAIN"
      ? "Focus answer not supported"
      : projection.outcome === "DENY"
        ? "Focus answer restricted"
        : "Focus answer unavailable";

  const message = isAnswer
    ? projection.answer ?? ""
    : projection.outcome === "ABSTAIN"
      ? "The composed claim does not have sufficient released evidence support."
      : projection.outcome === "DENY"
        ? "Policy does not permit this composed claim to be shown."
        : "The governed Focus service could not complete the request.";

  return Object.freeze({
    outcome: projection.outcome,
    code: projection.reasonCode,
    title,
    message,
    claimId: projection.claimId,
    closureId: projection.closureId,
    closureOutcome: projection.closureOutcome,
    evidenceRefs: isAnswer ? projection.evidenceRefs : EMPTY_STRINGS,
    citations: isAnswer ? projection.citations : EMPTY_CITATIONS,
    dependencyLabels,
    limitations: projection.limitations,
    aiReceiptLabel:
      projection.aiReceiptRef === null
        ? null
        : `Process receipt: ${projection.aiReceiptRef} (not release proof)`,
    evidenceDrawerInput: projection.evidenceDrawerInput,
    accessibilityLabel:
      isAnswer && projection.closureOutcome === "QUALIFIED"
        ? "Focus Panel: qualified composed claim"
        : isAnswer
          ? "Focus Panel: supported composed claim"
          : `Focus Panel: ${projection.outcome.toLowerCase()}`,
    ariaLive: projection.outcome === "ERROR" ? "assertive" : "polite",
  });
}

function localResolution(
  request: FocusComposedClaimRequest | null,
  code: LocalCode,
  outcome: "ABSTAIN" | "ERROR" = "ERROR",
): FocusComposedClaimResolution {
  return Object.freeze({
    request,
    code,
    projection: null,
    view: localView(code, outcome),
  });
}

/**
 * Resolve one bounded composed claim through an injected governed resolver.
 * The browser performs no transport, model, policy, evidence-store, graph,
 * vector-store, renderer, or lifecycle-store access.
 */
export async function resolveFocusComposedClaim(
  requestInput: unknown,
  resolver: GovernedFocusComposedClaimResolver,
): Promise<FocusComposedClaimResolution> {
  const request = parseFocusComposedClaimRequest(requestInput);
  if (request === null) return localResolution(null, "REQUEST_INVALID");
  if (request.allowedEvidenceRefs.length === 0) {
    return localResolution(request, "MISSING_EVIDENCE_SCOPE", "ABSTAIN");
  }

  let projectionInput: unknown;
  try {
    projectionInput = await resolver(request);
  } catch {
    return localResolution(request, "GOVERNED_RESOLVER_ERROR");
  }

  const projection = parseFocusComposedClaimProjection(projectionInput);
  if (projection === null) return localResolution(request, "PROJECTION_INVALID");
  if (projection.requestId !== request.requestId || projection.claimId !== request.claimId) {
    return localResolution(request, "RESPONSE_SCOPE_MISMATCH");
  }

  const allowedEvidence = new Set(request.allowedEvidenceRefs);
  const projectedEvidence = [
    ...projection.evidenceRefs,
    ...projection.evidenceDrawer.evidenceRefs,
  ];
  if (projectedEvidence.some((evidenceRef) => !allowedEvidence.has(evidenceRef))) {
    return localResolution(request, "EVIDENCE_OUTSIDE_REQUEST");
  }

  return Object.freeze({
    request,
    code: projection.reasonCode,
    projection,
    view: projectionView(projection),
  });
}
