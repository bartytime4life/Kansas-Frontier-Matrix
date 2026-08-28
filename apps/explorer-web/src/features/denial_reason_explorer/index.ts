import {
  type DenialReasonCode,
  parseDenialReasonProjection,
} from "../../adapters/DenialReasonProjection";

export type DenialReasonExplorerOutcome = "ABSTAIN" | "DENY" | "ERROR";
export type DenialReasonExplorerCode =
  | "DENIAL_REASONS_READY"
  | "NO_GOVERNED_RESPONSE"
  | "INVALID_PAYLOAD";

export type DenialReasonCategory =
  | "PROVENANCE"
  | "RESOLUTION"
  | "DISCLOSURE"
  | "INTEGRITY";

export type DenialReasonItem = Readonly<{
  code: DenialReasonCode;
  category: DenialReasonCategory;
  title: string;
  explanation: string;
  nextStep: string;
}>;

export type DenialReasonExplorerViewModel = Readonly<{
  outcome: DenialReasonExplorerOutcome;
  code: DenialReasonExplorerCode;
  title: string;
  message: string;
  reviewId: string | null;
  releaseCandidateRef: string | null;
  policyDecisionRef: string | null;
  evaluatedAt: string | null;
  reasons: readonly DenialReasonItem[];
  canOverride: false;
  accessibilityLabel: string;
  ariaLive: "polite" | "assertive";
}>;

export type DenialReasonExplorerController = Readonly<{
  state: DenialReasonExplorerViewModel;
  destroy: () => void;
}>;

const EMPTY_REASONS = Object.freeze([]) as readonly DenialReasonItem[];

const REASON_CATALOG: Readonly<Record<DenialReasonCode, DenialReasonItem>> =
  Object.freeze({
    MISSING_RECEIPT: Object.freeze({
      code: "MISSING_RECEIPT",
      category: "PROVENANCE",
      title: "Required receipt missing",
      explanation:
        "A required provenance or process receipt is not attached to this candidate.",
      nextStep:
        "Attach the governed receipt reference and rerun the release review.",
    }),
    ZOOM_TOO_FINE: Object.freeze({
      code: "ZOOM_TOO_FINE",
      category: "RESOLUTION",
      title: "Requested zoom is too fine",
      explanation:
        "The candidate exceeds its reviewed spatial-resolution limit.",
      nextStep:
        "Use a coarser reviewed zoom or return the candidate to the governed review path.",
    }),
    LOW_COUNT_CELL: Object.freeze({
      code: "LOW_COUNT_CELL",
      category: "DISCLOSURE",
      title: "Cell count below disclosure threshold",
      explanation:
        "The candidate contains an aggregate cell below its disclosure threshold.",
      nextStep:
        "Apply an approved aggregation or redaction transform and rerun review.",
    }),
    INVALID_ATTESTATION: Object.freeze({
      code: "INVALID_ATTESTATION",
      category: "INTEGRITY",
      title: "Attestation invalid",
      explanation:
        "A required integrity or provenance attestation did not validate.",
      nextStep:
        "Correct or regenerate the attestation through the governed build path.",
    }),
  });

const DISPLAY_ORDER = Object.freeze([
  "MISSING_RECEIPT",
  "INVALID_ATTESTATION",
  "LOW_COUNT_CELL",
  "ZOOM_TOO_FINE",
]) as readonly DenialReasonCode[];

function fixedNegativeView(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): DenialReasonExplorerViewModel {
  const invalid = code === "INVALID_PAYLOAD";
  return Object.freeze({
    outcome: invalid ? "ERROR" : "ABSTAIN",
    code,
    title: "Denial reasons unavailable",
    message: invalid
      ? "The governed denial-reason response is invalid. No review detail is displayed."
      : "No governed denial-reason response is available.",
    reviewId: null,
    releaseCandidateRef: null,
    policyDecisionRef: null,
    evaluatedAt: null,
    reasons: EMPTY_REASONS,
    canOverride: false,
    accessibilityLabel: invalid
      ? "Denial reason explorer: error"
      : "Denial reason explorer: unavailable",
    ariaLive: invalid ? "assertive" : "polite",
  });
}

/** Resolve fixed public-safe reason codes without reflecting payload prose. */
export function resolveDenialReasonExplorer(
  input?: unknown,
): DenialReasonExplorerViewModel {
  if (input === undefined) return fixedNegativeView("NO_GOVERNED_RESPONSE");
  const parsed = parseDenialReasonProjection(input);
  if (!parsed.ok) return fixedNegativeView("INVALID_PAYLOAD");
  const present = new Set(parsed.payload.reasonCodes);
  const reasons = Object.freeze(
    DISPLAY_ORDER.filter((code) => present.has(code)).map(
      (code) => REASON_CATALOG[code],
    ),
  );
  return Object.freeze({
    outcome: "DENY",
    code: "DENIAL_REASONS_READY",
    title: "Release candidate blocked",
    message:
      "Review the public-safe reason codes below. This surface cannot override the decision.",
    reviewId: parsed.payload.reviewId,
    releaseCandidateRef: parsed.payload.releaseCandidateRef,
    policyDecisionRef: parsed.payload.policyDecisionRef,
    evaluatedAt: parsed.payload.evaluatedAt,
    reasons,
    canOverride: false,
    accessibilityLabel: "Denial reason explorer: release candidate blocked",
    ariaLive: "polite",
  });
}

/** Mount a read-only, accessible denial-reason review surface. */
export function mountDenialReasonExplorer(
  host: HTMLElement,
  input?: unknown,
): DenialReasonExplorerController {
  const state = resolveDenialReasonExplorer(input);
  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const outcome = document.createElement("p");
  const message = document.createElement("p");
  const evaluated = document.createElement("p");
  const list = document.createElement("ol");

  section.dataset.component = "denial-reason-explorer";
  section.setAttribute("role", "region");
  section.setAttribute("aria-label", state.accessibilityLabel);
  section.dataset.outcome = state.outcome;
  heading.textContent = state.title;
  outcome.textContent = `${state.outcome} / ${state.code}`;
  outcome.setAttribute("aria-live", state.ariaLive);
  message.textContent = state.message;
  evaluated.textContent =
    state.evaluatedAt === null
      ? "Evaluation time: unavailable"
      : `Evaluation time: ${state.evaluatedAt}`;

  list.replaceChildren(
    ...state.reasons.map((reason) => {
      const item = document.createElement("li");
      const itemHeading = document.createElement("h3");
      const code = document.createElement("code");
      const category = document.createElement("p");
      const explanation = document.createElement("p");
      const nextStep = document.createElement("p");
      item.dataset.reasonCode = reason.code;
      itemHeading.textContent = reason.title;
      code.textContent = reason.code;
      category.textContent = `Category: ${reason.category}`;
      explanation.textContent = reason.explanation;
      nextStep.textContent = `Next step: ${reason.nextStep}`;
      item.replaceChildren(itemHeading, code, category, explanation, nextStep);
      return item;
    }),
  );
  list.hidden = state.reasons.length === 0;
  section.replaceChildren(heading, outcome, message, evaluated, list);
  host.replaceChildren(section);

  return Object.freeze({
    state,
    destroy(): void {
      host.replaceChildren();
    },
  });
}
