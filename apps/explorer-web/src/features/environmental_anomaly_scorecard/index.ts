import {
  type EnvironmentalScorecardLane,
  type EnvironmentalScorecardOutcome,
  type EnvironmentalScorecardReasonCode,
  type EnvironmentalScorecardScope,
  type EnvironmentalScorecardSummary,
  parseEnvironmentalAnomalyScorecardProjection,
} from "../../adapters/EnvironmentalAnomalyScorecardProjection";

export type EnvironmentalAnomalyScorecardState = Readonly<{
  visibility: "VISIBLE" | "HIDDEN";
  outcome: EnvironmentalScorecardOutcome;
  code:
    | EnvironmentalScorecardReasonCode
    | "NO_GOVERNED_RESPONSE"
    | "INVALID_PAYLOAD";
  heading: string;
  message: string;
  county: EnvironmentalScorecardScope | null;
  assessedAt: string | null;
  lanes: readonly EnvironmentalScorecardLane[];
  summary: EnvironmentalScorecardSummary | null;
  ariaLive: "polite" | "assertive";
}>;

export type EnvironmentalAnomalyScorecardController = Readonly<{
  state: EnvironmentalAnomalyScorecardState;
  destroy: () => void;
}>;

const EMPTY_LANES: readonly EnvironmentalScorecardLane[] = Object.freeze([]);
const NEGATIVE_COPY: Readonly<
  Record<
    Exclude<EnvironmentalScorecardReasonCode, "SCORECARD_AVAILABLE">,
    Readonly<{
      outcome: Exclude<EnvironmentalScorecardOutcome, "ANSWER">;
      heading: string;
      message: string;
      ariaLive: "polite" | "assertive";
    }>
  >
> = Object.freeze({
  SCORECARD_MISSING: Object.freeze({
    outcome: "ABSTAIN",
    heading: "Environmental anomaly scorecard unavailable",
    message: "The governed county scorecard projection is incomplete.",
    ariaLive: "polite",
  }),
  POLICY_DENIED: Object.freeze({
    outcome: "DENY",
    heading: "Environmental anomaly scorecard withheld",
    message: "Policy does not permit this scorecard projection to be displayed.",
    ariaLive: "assertive",
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR",
    heading: "Environmental anomaly scorecard unavailable",
    message: "The governed county scorecard projection could not be completed.",
    ariaLive: "assertive",
  }),
});

function hidden(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): EnvironmentalAnomalyScorecardState {
  return Object.freeze({
    visibility: "HIDDEN",
    outcome: "ERROR",
    code,
    heading: "Environmental anomaly scorecard unavailable",
    message: "No scorecard is rendered without a valid governed projection.",
    county: null,
    assessedAt: null,
    lanes: EMPTY_LANES,
    summary: null,
    ariaLive: "polite",
  });
}

function availableMessage(summary: EnvironmentalScorecardSummary): string {
  const lead =
    summary.overallOutcome === "COMPLETE"
      ? "All five synthetic domain lanes have current freshness evidence."
      : "One or more synthetic domain lanes retain a freshness or upstream hold.";
  return `${lead} Candidate states are proposals only and require a separate interpretation gate.`;
}

/** Resolve a governed projection into a read-only scorecard state. */
export function resolveEnvironmentalAnomalyScorecard(
  input?: unknown,
): EnvironmentalAnomalyScorecardState {
  if (input === undefined) return hidden("NO_GOVERNED_RESPONSE");
  const parsed = parseEnvironmentalAnomalyScorecardProjection(input);
  if (!parsed.ok) return hidden("INVALID_PAYLOAD");
  const { payload } = parsed;
  if (payload.outcome !== "ANSWER") {
    const copy = NEGATIVE_COPY[
      payload.reasonCode as Exclude<
        EnvironmentalScorecardReasonCode,
        "SCORECARD_AVAILABLE"
      >
    ];
    return Object.freeze({
      visibility: "VISIBLE",
      outcome: copy.outcome,
      code: payload.reasonCode,
      heading: copy.heading,
      message: copy.message,
      county: null,
      assessedAt: null,
      lanes: EMPTY_LANES,
      summary: null,
      ariaLive: copy.ariaLive,
    });
  }

  return Object.freeze({
    visibility: "VISIBLE",
    outcome: "ANSWER",
    code: "SCORECARD_AVAILABLE",
    heading: "County environmental anomaly scorecard",
    message: availableMessage(payload.summary!),
    county: payload.county,
    assessedAt: payload.assessedAt,
    lanes: payload.lanes,
    summary: payload.summary,
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

function appendCell(
  document: Document,
  row: HTMLTableRowElement,
  value: string,
  cellType: "th" | "td" = "td",
): void {
  const cell = document.createElement(cellType);
  cell.textContent = value;
  if (cellType === "th") cell.scope = "row";
  row.append(cell);
}

function appendScorecardTable(
  document: Document,
  section: HTMLElement,
  lanes: readonly EnvironmentalScorecardLane[],
): void {
  const table = document.createElement("table");
  const caption = document.createElement("caption");
  const head = document.createElement("thead");
  const headerRow = document.createElement("tr");
  const body = document.createElement("tbody");
  caption.textContent = "Synthetic domain freshness and anomaly-candidate states";
  for (const heading of ["Domain", "Freshness", "Candidate", "Reason"]) {
    const cell = document.createElement("th");
    cell.scope = "col";
    cell.textContent = heading;
    headerRow.append(cell);
  }
  head.append(headerRow);
  for (const lane of lanes) {
    const row = document.createElement("tr");
    row.dataset.scorecardLane = lane.lane;
    row.dataset.freshness = lane.freshnessState;
    row.dataset.candidateState = lane.candidateState;
    appendCell(document, row, lane.lane, "th");
    appendCell(document, row, lane.freshnessState);
    appendCell(document, row, lane.candidateState);
    appendCell(document, row, lane.reasonCode);
    body.append(row);
  }
  table.append(caption, head, body);
  section.append(table);
}

function appendPositiveContent(
  document: Document,
  section: HTMLElement,
  state: EnvironmentalAnomalyScorecardState,
): void {
  if (
    state.county === null ||
    state.assessedAt === null ||
    state.summary === null
  ) {
    return;
  }
  const status = document.createElement("p");
  const metrics = document.createElement("dl");
  const details = document.createElement("details");
  const detailsSummary = document.createElement("summary");
  const references = document.createElement("dl");
  status.dataset.scorecardStatus = state.summary.overallOutcome;
  status.textContent = `Scorecard status: ${state.summary.overallOutcome}`;
  appendDefinition(document, metrics, "Current lanes", String(state.summary.currentCount));
  appendDefinition(
    document,
    metrics,
    "Proposed candidates",
    String(state.summary.candidateCount),
  );
  appendDefinition(document, metrics, "Hold lanes", String(state.summary.holdCount));
  appendDefinition(document, metrics, "Error lanes", String(state.summary.errorCount));
  section.append(status, metrics);
  appendScorecardTable(document, section, state.lanes);

  detailsSummary.textContent = "Inspect fixture scope and governed references";
  appendDefinition(document, references, "County scope", state.county.scopeRef);
  appendDefinition(document, references, "County geometry", state.county.geometryRef);
  appendDefinition(document, references, "Assessed at", state.assessedAt);
  for (const lane of state.lanes) {
    appendDefinition(
      document,
      references,
      `${lane.lane} health assessment`,
      lane.sourceHealthAssessmentRef,
    );
    if (lane.evidenceRef !== null) {
      appendDefinition(document, references, `${lane.lane} evidence`, lane.evidenceRef);
    }
    if (lane.candidateRef !== null) {
      appendDefinition(
        document,
        references,
        `${lane.lane} proposed candidate`,
        lane.candidateRef,
      );
    }
  }
  details.append(detailsSummary, references);
  section.append(details);
}

/** Mount a table-first, non-mutating environmental anomaly scorecard. */
export function mountEnvironmentalAnomalyScorecard(
  host: HTMLElement,
  input?: unknown,
): EnvironmentalAnomalyScorecardController {
  const state = resolveEnvironmentalAnomalyScorecard(input);
  host.replaceChildren();
  if (state.visibility === "HIDDEN") {
    return Object.freeze({ state, destroy: () => host.replaceChildren() });
  }

  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const message = document.createElement("p");
  const headingId = "kfm-environmental-anomaly-scorecard-heading";
  section.dataset.component = "environmental-anomaly-scorecard";
  section.dataset.outcome = state.outcome;
  section.setAttribute("role", state.outcome === "ANSWER" ? "region" : "status");
  section.setAttribute("aria-live", state.ariaLive);
  section.setAttribute("aria-labelledby", headingId);
  heading.id = headingId;
  heading.textContent = state.heading;
  message.textContent = state.message;
  section.append(heading, message);
  if (state.outcome === "ANSWER") appendPositiveContent(document, section, state);
  host.replaceChildren(section);
  return Object.freeze({
    state,
    destroy: () => host.replaceChildren(),
  });
}
