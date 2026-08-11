import {
  type CountyNdviEvidence,
  type CountyNdviMetrics,
  type CountyNdviPanelOutcome,
  type CountyNdviPanelReasonCode,
  type CountyNdviScope,
  type CountyNdviWindows,
  parseCountyNdviChangeProjection,
} from "../../adapters/CountyNdviChangeProjection";

export type CountyNdviChangePanelState = Readonly<{
  visibility: "VISIBLE" | "HIDDEN";
  outcome: CountyNdviPanelOutcome;
  code: CountyNdviPanelReasonCode | "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD";
  heading: string;
  message: string;
  county: CountyNdviScope | null;
  windows: CountyNdviWindows | null;
  metrics: CountyNdviMetrics | null;
  evidence: CountyNdviEvidence | null;
  ariaLive: "polite" | "assertive";
}>;

export type CountyNdviChangePanelController = Readonly<{
  state: CountyNdviChangePanelState;
  destroy: () => void;
}>;

const NEGATIVE_COPY = Object.freeze({
  PANEL_MISSING: Object.freeze({
    outcome: "ABSTAIN" as const,
    heading: "County NDVI panel unavailable",
    message: "The governed fixture projection is incomplete.",
    ariaLive: "polite" as const,
  }),
  POLICY_DENIED: Object.freeze({
    outcome: "DENY" as const,
    heading: "County NDVI panel withheld",
    message: "Policy does not permit this candidate projection to be displayed.",
    ariaLive: "assertive" as const,
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR" as const,
    heading: "County NDVI panel unavailable",
    message: "The governed fixture projection could not be completed.",
    ariaLive: "assertive" as const,
  }),
});

function hidden(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): CountyNdviChangePanelState {
  return Object.freeze({
    visibility: "HIDDEN",
    outcome: "ERROR",
    code,
    heading: "County NDVI panel unavailable",
    message: "No panel is rendered without a valid governed projection.",
    county: null,
    windows: null,
    metrics: null,
    evidence: null,
    ariaLive: "polite",
  });
}

/** Resolve a governed projection into a read-only candidate panel state. */
export function resolveCountyNdviChangePanel(
  input?: unknown,
): CountyNdviChangePanelState {
  if (input === undefined) return hidden("NO_GOVERNED_RESPONSE");
  const parsed = parseCountyNdviChangeProjection(input);
  if (!parsed.ok) return hidden("INVALID_PAYLOAD");
  const { payload } = parsed;
  if (payload.outcome !== "ANSWER") {
    const copy = NEGATIVE_COPY[
      payload.reasonCode as Exclude<CountyNdviPanelReasonCode, "PANEL_AVAILABLE">
    ];
    return Object.freeze({
      visibility: "VISIBLE",
      outcome: copy.outcome,
      code: payload.reasonCode,
      heading: copy.heading,
      message: copy.message,
      county: null,
      windows: null,
      metrics: null,
      evidence: null,
      ariaLive: copy.ariaLive,
    });
  }
  return Object.freeze({
    visibility: "VISIBLE",
    outcome: "ANSWER",
    code: "PANEL_AVAILABLE",
    heading: "County NDVI change candidate",
    message:
      "Synthetic fixture metrics are shown for review. Evidence is referenced but unresolved, so this panel does not establish an environmental finding or authorize public use.",
    county: payload.county,
    windows: payload.windows,
    metrics: payload.metrics,
    evidence: payload.evidence,
    ariaLive: "polite",
  });
}

function appendDefinition(
  document: Document,
  list: HTMLDListElement,
  term: string,
  value: string,
): void {
  const dt = document.createElement("dt");
  const dd = document.createElement("dd");
  dt.textContent = term;
  dd.textContent = value;
  list.append(dt, dd);
}

function formatMillionths(value: number): string {
  return (value / 1_000_000).toFixed(6);
}

function formatBasisPoints(value: number): string {
  return `${(value / 100).toFixed(2)}%`;
}

function appendCandidateDetails(
  document: Document,
  section: HTMLElement,
  state: CountyNdviChangePanelState,
): void {
  if (
    state.county === null ||
    state.windows === null ||
    state.metrics === null ||
    state.evidence === null
  ) {
    return;
  }
  const status = document.createElement("p");
  const metrics = document.createElement("dl");
  const evidenceDetails = document.createElement("details");
  const evidenceSummary = document.createElement("summary");
  const references = document.createElement("dl");
  status.dataset.ndviClassification = state.metrics.classification;
  status.textContent = `Classification: ${state.metrics.classification}`;
  appendDefinition(document, metrics, "County scope", state.county.scopeRef);
  appendDefinition(
    document,
    metrics,
    "Baseline window",
    `${state.windows.baselineStart} to ${state.windows.baselineEnd}`,
  );
  appendDefinition(
    document,
    metrics,
    "Recent window",
    `${state.windows.recentStart} to ${state.windows.recentEnd}`,
  );
  appendDefinition(
    document,
    metrics,
    "Baseline median NDVI",
    formatMillionths(state.metrics.baselineMedianMillionths),
  );
  appendDefinition(
    document,
    metrics,
    "Recent median NDVI",
    formatMillionths(state.metrics.recentMedianMillionths),
  );
  appendDefinition(
    document,
    metrics,
    "NDVI delta",
    formatMillionths(state.metrics.deltaNdviMillionths),
  );
  appendDefinition(
    document,
    metrics,
    "Candidate delta threshold",
    formatMillionths(state.metrics.deltaThresholdMillionths),
  );
  appendDefinition(
    document,
    metrics,
    "Changed area",
    formatBasisPoints(state.metrics.changedAreaBasisPoints),
  );
  appendDefinition(
    document,
    metrics,
    "Cluster count",
    String(state.metrics.clusterCount),
  );
  appendDefinition(document, metrics, "Evidence state", state.evidence.state);
  section.append(status, metrics);

  evidenceSummary.textContent = "Inspect fixture-bound references";
  appendDefinition(
    document,
    references,
    "NDVI computation",
    state.evidence.ndviComputationRef,
  );
  appendDefinition(
    document,
    references,
    "Connectivity assessment",
    state.evidence.connectivityAssessmentRef,
  );
  evidenceDetails.append(evidenceSummary, references);
  section.append(evidenceDetails);
}

/** Mount a non-mutating county NDVI candidate panel. */
export function mountCountyNdviChangePanel(
  host: HTMLElement,
  input?: unknown,
): CountyNdviChangePanelController {
  const state = resolveCountyNdviChangePanel(input);
  host.replaceChildren();
  if (state.visibility === "HIDDEN") {
    return Object.freeze({ state, destroy: () => host.replaceChildren() });
  }
  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const message = document.createElement("p");
  const headingId = "kfm-county-ndvi-change-panel-heading";
  section.dataset.component = "county-ndvi-change-panel";
  section.dataset.outcome = state.outcome;
  section.setAttribute("role", state.outcome === "ANSWER" ? "region" : "status");
  section.setAttribute("aria-live", state.ariaLive);
  section.setAttribute("aria-labelledby", headingId);
  heading.id = headingId;
  heading.textContent = state.heading;
  message.textContent = state.message;
  section.append(heading, message);
  if (state.outcome === "ANSWER") appendCandidateDetails(document, section, state);
  host.replaceChildren(section);
  return Object.freeze({
    state,
    destroy: () => host.replaceChildren(),
  });
}
