import {
  parseStreamflowQcDashboardProjection,
  type GovernedStreamflowQcDashboardProjection,
  type StreamflowQcDashboardOutcome,
  type StreamflowQcDashboardStatus,
} from "../../adapters/StreamflowQcDashboardProjection";

export type StreamflowQcDashboardCode =
  | "REGIONAL_CONTEXT_AVAILABLE"
  | "LOCAL_REVIEW_AVAILABLE"
  | "NO_ESCALATION_AVAILABLE"
  | "CONTEXT_HELD"
  | "RELEASE_DENIED"
  | "UPSTREAM_ERROR"
  | "NO_GOVERNED_RESPONSE"
  | "INVALID_PAYLOAD";

export type StreamflowQcDashboardViewModel = Readonly<{
  visibility: "VISIBLE" | "HIDDEN";
  outcome: StreamflowQcDashboardOutcome;
  code: StreamflowQcDashboardCode;
  status: StreamflowQcDashboardStatus | null;
  heading: string;
  message: string;
  assessment: GovernedStreamflowQcDashboardProjection | null;
  canRecalculatePercentile: false;
  canInvalidateSensor: false;
  canDeclareHydrologicEvent: false;
  canMutateDetectorConfiguration: false;
  canEvaluatePolicy: false;
  canApproveReview: false;
  canRelease: false;
  canPublish: false;
  accessibilityLabel: string;
  ariaLive: "polite" | "assertive";
}>;

export type StreamflowQcDashboardController = Readonly<{
  state: StreamflowQcDashboardViewModel;
  destroy: () => void;
}>;

function unavailable(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): StreamflowQcDashboardViewModel {
  const invalid = code === "INVALID_PAYLOAD";
  return Object.freeze({
    visibility: "HIDDEN",
    outcome: invalid ? "ERROR" : "ABSTAIN",
    code,
    status: null,
    heading: "Streamflow QC context unavailable",
    message: invalid
      ? "The governed projection is invalid. No gauge or evidence detail is displayed."
      : "No governed streamflow QC projection is available.",
    assessment: null,
    canRecalculatePercentile: false,
    canInvalidateSensor: false,
    canDeclareHydrologicEvent: false,
    canMutateDetectorConfiguration: false,
    canEvaluatePolicy: false,
    canApproveReview: false,
    canRelease: false,
    canPublish: false,
    accessibilityLabel: invalid
      ? "Streamflow QC dashboard: error"
      : "Streamflow QC dashboard: unavailable",
    ariaLive: invalid ? "assertive" : "polite",
  });
}

function headingFor(outcome: StreamflowQcDashboardOutcome): string {
  if (outcome === "AVAILABLE") return "Streamflow QC context";
  if (outcome === "ABSTAIN") return "Streamflow QC context held";
  if (outcome === "DENY") return "Streamflow QC context withheld";
  return "Streamflow QC context failed";
}

function messageFor(
  outcome: StreamflowQcDashboardOutcome,
  status: StreamflowQcDashboardStatus,
): string {
  if (outcome === "ABSTAIN") {
    return "Required context is incomplete. No gauge or evidence detail is displayed.";
  }
  if (outcome === "DENY") {
    return "The governed projection denies display. This surface cannot override the decision.";
  }
  if (outcome === "ERROR") {
    return "The upstream assessment failed. No gauge or evidence detail is displayed.";
  }
  if (status === "REGIONAL_CONTEXT") {
    return "Declared regional evidence supports low-flow context. This is review context, not a hydrologic event declaration.";
  }
  if (status === "LOCAL_REVIEW") {
    return "The declared context prioritizes local signal review without invalidating the sensor.";
  }
  return "The declared context does not call for a low-flow-driven QC escalation.";
}

/** Resolve one governed packet into an immutable read-only dashboard state. */
export function resolveStreamflowQcDashboard(
  input?: unknown,
): StreamflowQcDashboardViewModel {
  if (input === undefined) return unavailable("NO_GOVERNED_RESPONSE");
  const parsed = parseStreamflowQcDashboardProjection(input);
  if (!parsed.ok) return unavailable("INVALID_PAYLOAD");
  const { payload } = parsed;
  return Object.freeze({
    visibility: "VISIBLE",
    outcome: payload.outcome,
    code: payload.reasonCode,
    status: payload.status,
    heading: headingFor(payload.outcome),
    message: messageFor(payload.outcome, payload.status),
    assessment: payload.outcome === "AVAILABLE" ? payload : null,
    canRecalculatePercentile: false,
    canInvalidateSensor: false,
    canDeclareHydrologicEvent: false,
    canMutateDetectorConfiguration: false,
    canEvaluatePolicy: false,
    canApproveReview: false,
    canRelease: false,
    canPublish: false,
    accessibilityLabel:
      "Streamflow QC dashboard: " + payload.outcome.toLowerCase(),
    ariaLive: payload.outcome === "ERROR" ? "assertive" : "polite",
  });
}

function appendDefinition(
  document: Document,
  list: HTMLDListElement,
  label: string,
  value: string,
): void {
  const term = document.createElement("dt");
  const definition = document.createElement("dd");
  term.textContent = label;
  definition.textContent = value;
  list.append(term, definition);
}

function appendAssessment(
  document: Document,
  section: HTMLElement,
  assessment: GovernedStreamflowQcDashboardProjection,
): void {
  const details = document.createElement("dl");
  appendDefinition(
    document,
    details,
    "Assessment identity",
    assessment.assessmentId ?? "unavailable",
  );
  appendDefinition(
    document,
    details,
    "Gauge reference",
    assessment.gaugeRef ?? "unavailable",
  );
  appendDefinition(
    document,
    details,
    "Flow state",
    assessment.flowState ?? "unavailable",
  );
  appendDefinition(
    document,
    details,
    "Adjacent gauges",
    String(assessment.adjacentGaugeCount),
  );
  appendDefinition(
    document,
    details,
    "Adjacent-gauge context",
    assessment.corroboration ?? "unavailable",
  );
  appendDefinition(
    document,
    details,
    "Drought context",
    assessment.droughtContext ?? "unavailable",
  );
  appendDefinition(
    document,
    details,
    "Ingest state",
    assessment.ingestState ?? "unavailable",
  );
  appendDefinition(
    document,
    details,
    "Unit state",
    assessment.unitState ?? "unavailable",
  );
  appendDefinition(
    document,
    details,
    "Cadence state",
    assessment.cadenceState ?? "unavailable",
  );
  appendDefinition(
    document,
    details,
    "Review priority",
    assessment.priority ?? "unavailable",
  );
  appendDefinition(
    document,
    details,
    "Evaluated at",
    assessment.evaluatedAt,
  );
  section.append(details);

  const evidenceHeading = document.createElement("h3");
  const evidence = document.createElement("ol");
  evidenceHeading.textContent = "Evidence references";
  for (const reference of assessment.evidenceRefs) {
    const item = document.createElement("li");
    item.textContent = reference;
    evidence.append(item);
  }
  section.append(evidenceHeading, evidence);
}

/** Mount an accessible dashboard without controls or network seams. */
export function mountStreamflowQcDashboard(
  host: HTMLElement,
  input?: unknown,
): StreamflowQcDashboardController {
  const state = resolveStreamflowQcDashboard(input);
  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const outcome = document.createElement("p");
  const message = document.createElement("p");

  section.dataset.component = "streamflow-qc-dashboard";
  section.dataset.outcome = state.outcome;
  section.setAttribute("role", "region");
  section.setAttribute("aria-label", state.accessibilityLabel);
  heading.textContent = state.heading;
  outcome.textContent = state.outcome + " / " + state.code;
  outcome.setAttribute("aria-live", state.ariaLive);
  message.textContent = state.message;
  section.append(heading, outcome, message);
  if (state.assessment !== null) {
    appendAssessment(document, section, state.assessment);
  }
  host.replaceChildren(section);

  return Object.freeze({
    state,
    destroy(): void {
      host.replaceChildren();
    },
  });
}
