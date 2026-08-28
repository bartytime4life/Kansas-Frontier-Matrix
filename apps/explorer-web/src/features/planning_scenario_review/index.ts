import {
  type GovernedPlanningScenarioProjection,
  type PlanningScenarioAssumption,
  type PlanningScenarioEquityDimension,
  type PlanningScenarioHorizon,
  type PlanningScenarioInputVariable,
  type PlanningScenarioOutcome,
  type PlanningScenarioReasonCode,
  parsePlanningScenarioProjection,
} from "../../adapters/planning-scenario-projection";

export type PlanningScenarioReviewState = Readonly<{
  visibility: "VISIBLE" | "HIDDEN";
  outcome: PlanningScenarioOutcome;
  code:
    | PlanningScenarioReasonCode
    | "NO_GOVERNED_RESPONSE"
    | "INVALID_PAYLOAD";
  heading: string;
  message: string;
  scenarioStatus: "HELD" | null;
  purpose: string | null;
  geographyLabel: string | null;
  horizon: PlanningScenarioHorizon | null;
  inputVariables: readonly PlanningScenarioInputVariable[];
  assumptions: readonly PlanningScenarioAssumption[];
  equityDimensions: readonly PlanningScenarioEquityDimension[];
  participationRefs: readonly string[];
  evidenceRefs: readonly string[];
  limitations: readonly string[];
  nonAuthorityLabels: readonly string[];
  ariaLive: "polite" | "assertive";
}>;

export type PlanningScenarioReviewController = Readonly<{
  state: PlanningScenarioReviewState;
  destroy: () => void;
}>;

const EMPTY_STRINGS: readonly string[] = Object.freeze([]);
const EMPTY_INPUTS: readonly PlanningScenarioInputVariable[] = Object.freeze([]);
const EMPTY_ASSUMPTIONS: readonly PlanningScenarioAssumption[] = Object.freeze([]);
const EMPTY_EQUITY: readonly PlanningScenarioEquityDimension[] = Object.freeze([]);
const NEGATIVE_COPY: Readonly<
  Record<
    Exclude<PlanningScenarioReasonCode, "SCENARIO_HELD">,
    Readonly<{
      outcome: Exclude<PlanningScenarioOutcome, "ANSWER">;
      heading: string;
      message: string;
      ariaLive: "polite" | "assertive";
    }>
  >
> = Object.freeze({
  SCENARIO_MISSING: Object.freeze({
    outcome: "ABSTAIN",
    heading: "Planning scenario unavailable",
    message: "The governed planning-scenario projection is incomplete.",
    ariaLive: "polite",
  }),
  POLICY_DENIED: Object.freeze({
    outcome: "DENY",
    heading: "Planning scenario withheld",
    message: "Policy does not permit this planning-scenario projection to be displayed.",
    ariaLive: "assertive",
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR",
    heading: "Planning scenario unavailable",
    message: "The governed planning-scenario projection could not be completed.",
    ariaLive: "assertive",
  }),
});

function hidden(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): PlanningScenarioReviewState {
  return Object.freeze({
    visibility: "HIDDEN",
    outcome: "ERROR",
    code,
    heading: "Planning scenario unavailable",
    message: "No scenario is rendered without a valid governed projection.",
    scenarioStatus: null,
    purpose: null,
    geographyLabel: null,
    horizon: null,
    inputVariables: EMPTY_INPUTS,
    assumptions: EMPTY_ASSUMPTIONS,
    equityDimensions: EMPTY_EQUITY,
    participationRefs: EMPTY_STRINGS,
    evidenceRefs: EMPTY_STRINGS,
    limitations: EMPTY_STRINGS,
    nonAuthorityLabels: EMPTY_STRINGS,
    ariaLive: "polite",
  });
}

function negative(
  payload: GovernedPlanningScenarioProjection,
): PlanningScenarioReviewState {
  const copy = NEGATIVE_COPY[
    payload.reasonCode as Exclude<
      PlanningScenarioReasonCode,
      "SCENARIO_HELD"
    >
  ];
  return Object.freeze({
    visibility: "VISIBLE",
    outcome: copy.outcome,
    code: payload.reasonCode,
    heading: copy.heading,
    message: copy.message,
    scenarioStatus: null,
    purpose: null,
    geographyLabel: null,
    horizon: null,
    inputVariables: EMPTY_INPUTS,
    assumptions: EMPTY_ASSUMPTIONS,
    equityDimensions: EMPTY_EQUITY,
    participationRefs: EMPTY_STRINGS,
    evidenceRefs: EMPTY_STRINGS,
    limitations: EMPTY_STRINGS,
    nonAuthorityLabels: EMPTY_STRINGS,
    ariaLive: copy.ariaLive,
  });
}

/** Resolve one governed projection into a read-only planning review state. */
export function resolvePlanningScenarioReview(
  input?: unknown,
): PlanningScenarioReviewState {
  if (input === undefined) return hidden("NO_GOVERNED_RESPONSE");
  const parsed = parsePlanningScenarioProjection(input);
  if (!parsed.ok) return hidden("INVALID_PAYLOAD");
  const { payload } = parsed;
  if (payload.reasonCode !== "SCENARIO_HELD") return negative(payload);

  return Object.freeze({
    visibility: "VISIBLE",
    outcome: "ABSTAIN",
    code: "SCENARIO_HELD",
    heading: payload.title!,
    message:
      "Exploratory fixture for review. It is not a prediction, recommendation, emergency alert, regulatory determination, release, or publication.",
    scenarioStatus: payload.scenarioStatus,
    purpose: payload.purpose,
    geographyLabel: payload.geography!.label,
    horizon: payload.horizon,
    inputVariables: payload.inputVariables,
    assumptions: payload.assumptions,
    equityDimensions: payload.equityDimensions,
    participationRefs: payload.participationRefs,
    evidenceRefs: payload.evidenceRefs,
    limitations: payload.limitations,
    nonAuthorityLabels: payload.nonAuthorityLabels,
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

function appendTextList(
  document: Document,
  parent: HTMLElement,
  headingText: string,
  values: readonly string[],
  ariaLabel: string,
): void {
  const heading = document.createElement("h3");
  const list = document.createElement("ul");
  heading.textContent = headingText;
  list.setAttribute("aria-label", ariaLabel);
  for (const value of values) {
    const item = document.createElement("li");
    item.textContent = value;
    list.append(item);
  }
  parent.append(heading, list);
}

function appendInputTable(
  document: Document,
  parent: HTMLElement,
  inputs: readonly PlanningScenarioInputVariable[],
): void {
  const table = document.createElement("table");
  const caption = document.createElement("caption");
  const head = document.createElement("thead");
  const headerRow = document.createElement("tr");
  const body = document.createElement("tbody");
  caption.textContent = "Scenario inputs and uncertainty";
  for (const label of ["Input", "Uncertainty", "Evidence source"]) {
    const cell = document.createElement("th");
    cell.scope = "col";
    cell.textContent = label;
    headerRow.append(cell);
  }
  head.append(headerRow);
  for (const input of inputs) {
    const row = document.createElement("tr");
    const label = document.createElement("th");
    const uncertainty = document.createElement("td");
    const source = document.createElement("td");
    row.dataset.scenarioInput = input.variableId;
    row.dataset.uncertainty = input.uncertainty;
    label.scope = "row";
    label.textContent = input.label;
    uncertainty.textContent = input.uncertainty;
    source.textContent = input.sourceRef;
    row.append(label, uncertainty, source);
    body.append(row);
  }
  table.append(caption, head, body);
  parent.append(table);
}

function appendAssumptions(
  document: Document,
  parent: HTMLElement,
  assumptions: readonly PlanningScenarioAssumption[],
): void {
  const heading = document.createElement("h3");
  const list = document.createElement("ol");
  heading.textContent = "Assumptions and uncertainty";
  list.setAttribute("aria-label", "Scenario assumptions");
  for (const assumption of assumptions) {
    const item = document.createElement("li");
    const statement = document.createElement("p");
    const uncertainty = document.createElement("p");
    item.dataset.scenarioAssumption = assumption.assumptionId;
    item.dataset.uncertainty = assumption.uncertainty;
    statement.textContent = assumption.statement;
    uncertainty.textContent = `Uncertainty: ${assumption.uncertainty}`;
    item.append(statement, uncertainty);
    list.append(item);
  }
  parent.append(heading, list);
}

function appendEquityDimensions(
  document: Document,
  parent: HTMLElement,
  dimensions: readonly PlanningScenarioEquityDimension[],
): void {
  const heading = document.createElement("h3");
  const list = document.createElement("ul");
  heading.textContent = "Equity questions and limits";
  list.setAttribute("aria-label", "Scenario equity dimensions");
  for (const dimension of dimensions) {
    const item = document.createElement("li");
    const description = document.createElement("p");
    const limitation = document.createElement("p");
    item.dataset.equityDimension = dimension.dimensionId;
    description.textContent = dimension.description;
    limitation.textContent = `Limitation: ${dimension.limitation}`;
    item.append(description, limitation);
    list.append(item);
  }
  parent.append(heading, list);
}

function appendAvailableContent(
  document: Document,
  section: HTMLElement,
  state: PlanningScenarioReviewState,
): void {
  if (
    state.scenarioStatus === null ||
    state.purpose === null ||
    state.geographyLabel === null ||
    state.horizon === null
  ) {
    return;
  }
  const status = document.createElement("p");
  const purpose = document.createElement("p");
  const scope = document.createElement("dl");
  const details = document.createElement("details");
  const detailsSummary = document.createElement("summary");
  status.dataset.scenarioStatus = state.scenarioStatus;
  status.textContent = `Scenario status: ${state.scenarioStatus} — review candidate only`;
  purpose.textContent = state.purpose;
  appendDefinition(document, scope, "Geography", state.geographyLabel);
  appendDefinition(document, scope, "Baseline as of", state.horizon.baselineAsOf);
  appendDefinition(
    document,
    scope,
    "Exploratory horizon",
    `${state.horizon.horizonStart} through ${state.horizon.horizonEnd}`,
  );
  section.append(status, purpose, scope);
  appendInputTable(document, section, state.inputVariables);
  appendAssumptions(document, section, state.assumptions);
  appendEquityDimensions(document, section, state.equityDimensions);

  detailsSummary.textContent = "Inspect participation, evidence, and limitations";
  details.append(detailsSummary);
  appendTextList(
    document,
    details,
    "Participation references",
    state.participationRefs,
    "Scenario participation references",
  );
  appendTextList(
    document,
    details,
    "Evidence references",
    state.evidenceRefs,
    "Scenario evidence references",
  );
  appendTextList(
    document,
    details,
    "Limitations",
    state.limitations,
    "Scenario limitations",
  );
  appendTextList(
    document,
    details,
    "Non-authority labels",
    state.nonAuthorityLabels,
    "Scenario non-authority labels",
  );
  section.append(details);
}

/** Mount a text-first, read-only planning scenario review surface. */
export function mountPlanningScenarioReview(
  host: HTMLElement,
  input?: unknown,
): PlanningScenarioReviewController {
  const state = resolvePlanningScenarioReview(input);
  host.replaceChildren();
  if (state.visibility === "HIDDEN") {
    return Object.freeze({ state, destroy: () => host.replaceChildren() });
  }

  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const outcome = document.createElement("p");
  const message = document.createElement("p");
  const headingId = "kfm-planning-scenario-review-heading";
  section.dataset.component = "planning-scenario-review";
  section.dataset.outcome = state.outcome;
  section.setAttribute(
    "role",
    state.code === "SCENARIO_HELD" ? "region" : "status",
  );
  section.setAttribute("aria-live", state.ariaLive);
  section.setAttribute("aria-labelledby", headingId);
  heading.id = headingId;
  heading.textContent = state.heading;
  outcome.textContent = `${state.outcome} / ${state.code}`;
  outcome.dataset.scenarioOutcome = state.outcome;
  message.textContent = state.message;
  section.append(heading, outcome, message);
  if (state.code === "SCENARIO_HELD") {
    appendAvailableContent(document, section, state);
  }
  host.replaceChildren(section);
  return Object.freeze({
    state,
    destroy: () => host.replaceChildren(),
  });
}
