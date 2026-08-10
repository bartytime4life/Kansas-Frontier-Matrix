import {
  type CountyCadenceLane,
  type CountyCadenceOutcome,
  type CountyCadenceReasonCode,
  type CountyCadenceScope,
  type CountyCadenceStatus,
  type CountyCadenceSummary,
  type CountyCadenceWeek,
  parseCountyEnvironmentalCadenceProjection,
} from "../../adapters/CountyEnvironmentalCadenceProjection";

export type CountyEnvironmentalCadenceCalendarState = Readonly<{
  visibility: "VISIBLE" | "HIDDEN";
  outcome: CountyCadenceOutcome;
  code:
    | CountyCadenceReasonCode
    | "NO_GOVERNED_RESPONSE"
    | "INVALID_PAYLOAD";
  heading: string;
  message: string;
  county: CountyCadenceScope | null;
  week: CountyCadenceWeek | null;
  lanes: readonly CountyCadenceLane[];
  summary: CountyCadenceSummary | null;
  sourceAvailabilityWatchlistRef: string | null;
  ariaLive: "polite" | "assertive";
}>;

export type CountyEnvironmentalCadenceCalendarController = Readonly<{
  state: CountyEnvironmentalCadenceCalendarState;
  destroy: () => void;
}>;

const EMPTY_LANES: readonly CountyCadenceLane[] = Object.freeze([]);
const NEGATIVE_COPY: Readonly<
  Record<
    Exclude<CountyCadenceReasonCode, "CALENDAR_AVAILABLE">,
    Readonly<{
      outcome: Exclude<CountyCadenceOutcome, "ANSWER">;
      heading: string;
      message: string;
      ariaLive: "polite" | "assertive";
    }>
  >
> = Object.freeze({
  CALENDAR_MISSING: Object.freeze({
    outcome: "ABSTAIN",
    heading: "County cadence calendar unavailable",
    message: "The governed weekly cadence projection is incomplete.",
    ariaLive: "polite",
  }),
  POLICY_DENIED: Object.freeze({
    outcome: "DENY",
    heading: "County cadence calendar withheld",
    message: "Policy does not permit this cadence projection to be displayed.",
    ariaLive: "assertive",
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR",
    heading: "County cadence calendar unavailable",
    message: "The governed weekly cadence projection could not be completed.",
    ariaLive: "assertive",
  }),
});

function hidden(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): CountyEnvironmentalCadenceCalendarState {
  return Object.freeze({
    visibility: "HIDDEN",
    outcome: "ERROR",
    code,
    heading: "County cadence calendar unavailable",
    message: "No calendar is rendered without a valid governed projection.",
    county: null,
    week: null,
    lanes: EMPTY_LANES,
    summary: null,
    sourceAvailabilityWatchlistRef: null,
    ariaLive: "polite",
  });
}

function calendarMessage(status: CountyCadenceStatus): string {
  const lead =
    status === "COMPLETE"
      ? "All six synthetic lanes report a healthy recorded check."
      : "One or more synthetic lanes are stale, degraded, unavailable, or missing.";
  return `${lead} This fixture-only calendar does not probe sources, interpret environmental conditions, or authorize public use.`;
}

/** Resolve a governed projection into a read-only weekly calendar state. */
export function resolveCountyEnvironmentalCadenceCalendar(
  input?: unknown,
): CountyEnvironmentalCadenceCalendarState {
  if (input === undefined) return hidden("NO_GOVERNED_RESPONSE");
  const parsed = parseCountyEnvironmentalCadenceProjection(input);
  if (!parsed.ok) return hidden("INVALID_PAYLOAD");
  const { payload } = parsed;
  if (payload.outcome !== "ANSWER") {
    const copy = NEGATIVE_COPY[
      payload.reasonCode as Exclude<
        CountyCadenceReasonCode,
        "CALENDAR_AVAILABLE"
      >
    ];
    return Object.freeze({
      visibility: "VISIBLE",
      outcome: copy.outcome,
      code: payload.reasonCode,
      heading: copy.heading,
      message: copy.message,
      county: null,
      week: null,
      lanes: EMPTY_LANES,
      summary: null,
      sourceAvailabilityWatchlistRef: null,
      ariaLive: copy.ariaLive,
    });
  }

  return Object.freeze({
    visibility: "VISIBLE",
    outcome: "ANSWER",
    code: "CALENDAR_AVAILABLE",
    heading: "County environmental cadence calendar",
    message: calendarMessage(payload.summary!.overallOutcome),
    county: payload.county,
    week: payload.week,
    lanes: payload.lanes,
    summary: payload.summary,
    sourceAvailabilityWatchlistRef: payload.sourceAvailabilityWatchlistRef,
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

function appendCalendarTable(
  document: Document,
  section: HTMLElement,
  lanes: readonly CountyCadenceLane[],
  week: CountyCadenceWeek,
): void {
  const table = document.createElement("table");
  const caption = document.createElement("caption");
  const head = document.createElement("thead");
  const headerRow = document.createElement("tr");
  const body = document.createElement("tbody");
  caption.textContent = `Synthetic weekly checks from ${week.periodStart} through ${week.periodEnd}`;
  for (const heading of ["Lane", "Check", "Health", "Checked at", "Reason"]) {
    const cell = document.createElement("th");
    cell.scope = "col";
    cell.textContent = heading;
    headerRow.append(cell);
  }
  head.append(headerRow);
  for (const lane of lanes) {
    const row = document.createElement("tr");
    row.dataset.cadenceLane = lane.lane;
    row.dataset.health = lane.healthOutcome;
    appendCell(document, row, lane.lane, "th");
    appendCell(document, row, lane.checkResult);
    appendCell(document, row, lane.healthOutcome);
    appendCell(document, row, lane.checkedAt ?? "Not recorded");
    appendCell(document, row, lane.reasonCode);
    body.append(row);
  }
  table.append(caption, head, body);
  section.append(table);
}

function appendPositiveContent(
  document: Document,
  section: HTMLElement,
  state: CountyEnvironmentalCadenceCalendarState,
): void {
  if (
    state.county === null ||
    state.week === null ||
    state.summary === null ||
    state.sourceAvailabilityWatchlistRef === null
  ) {
    return;
  }
  const status = document.createElement("p");
  const metrics = document.createElement("dl");
  const details = document.createElement("details");
  const detailsSummary = document.createElement("summary");
  const references = document.createElement("dl");
  status.dataset.cadenceStatus = state.summary.overallOutcome;
  status.textContent = `Weekly cadence status: ${state.summary.overallOutcome}`;
  appendDefinition(
    document,
    metrics,
    "Recorded lanes",
    String(state.summary.recordedCount),
  );
  appendDefinition(
    document,
    metrics,
    "Hold lanes",
    String(state.summary.holdCount),
  );
  section.append(status, metrics);
  appendCalendarTable(document, section, state.lanes, state.week);

  detailsSummary.textContent = "Inspect fixture scope and source-health references";
  appendDefinition(document, references, "County scope", state.county.scopeRef);
  appendDefinition(document, references, "County geometry", state.county.geometryRef);
  appendDefinition(
    document,
    references,
    "Source availability watchlist",
    state.sourceAvailabilityWatchlistRef,
  );
  appendDefinition(document, references, "Assessed at", state.week.assessedAt);
  for (const lane of state.lanes) {
    appendDefinition(
      document,
      references,
      `${lane.lane} source`,
      lane.sourceDescriptorRef,
    );
    appendDefinition(
      document,
      references,
      `${lane.lane} health assessment`,
      lane.sourceHealthAssessmentRef,
    );
  }
  details.append(detailsSummary, references);
  section.append(details);
}

/** Mount a table-first, non-mutating county cadence calendar. */
export function mountCountyEnvironmentalCadenceCalendar(
  host: HTMLElement,
  input?: unknown,
): CountyEnvironmentalCadenceCalendarController {
  const state = resolveCountyEnvironmentalCadenceCalendar(input);
  host.replaceChildren();
  if (state.visibility === "HIDDEN") {
    return Object.freeze({ state, destroy: () => host.replaceChildren() });
  }

  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const message = document.createElement("p");
  const headingId = "kfm-county-environmental-cadence-heading";
  section.dataset.component = "county-environmental-cadence-calendar";
  section.dataset.outcome = state.outcome;
  section.setAttribute("role", state.outcome === "ANSWER" ? "region" : "status");
  section.setAttribute("aria-live", state.ariaLive);
  section.setAttribute("aria-labelledby", headingId);
  heading.id = headingId;
  heading.textContent = state.heading;
  message.textContent = state.message;
  section.append(heading, message);
  if (state.outcome === "ANSWER") {
    appendPositiveContent(document, section, state);
  }
  host.replaceChildren(section);
  return Object.freeze({
    state,
    destroy: () => host.replaceChildren(),
  });
}
