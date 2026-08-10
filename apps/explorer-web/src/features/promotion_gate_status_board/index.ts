import {
  type PromotionGateBoardState,
  type PromotionGateComponent,
  type PromotionGateStatusBoardOutcome,
  type PromotionGateStatusBoardReasonCode,
  type PromotionGateStatusSummary,
  parsePromotionGateStatusBoardProjection,
} from "../../adapters/PromotionGateStatusBoardProjection";

export type PromotionGateStatusBoardViewModel = Readonly<{
  visibility: "VISIBLE" | "HIDDEN";
  outcome: PromotionGateStatusBoardOutcome;
  code:
    | PromotionGateStatusBoardReasonCode
    | "NO_GOVERNED_RESPONSE"
    | "INVALID_PAYLOAD";
  heading: string;
  summaryText: string;
  observedAt: string | null;
  candidateRef: string | null;
  boardState: PromotionGateBoardState | null;
  counts: PromotionGateStatusSummary | null;
  components: readonly PromotionGateComponent[];
  ariaLive: "polite" | "assertive";
}>;

export type PromotionGateStatusBoardController = Readonly<{
  state: PromotionGateStatusBoardViewModel;
  destroy: () => void;
}>;

const EMPTY_COMPONENTS: readonly PromotionGateComponent[] = Object.freeze([]);
const BOARD_STATE_COPY: Readonly<Record<PromotionGateBoardState, string>> =
  Object.freeze({
    READY_FOR_REVIEW:
      "All six projected components report PASS. This means ready for human review only, not approved or released.",
    HOLD:
      "At least one projected component is held or not run. The candidate must remain blocked.",
    DENY:
      "At least one projected component reports DENY. No promotion fallback is permitted.",
    ERROR:
      "At least one projected component reports ERROR. The board creates no implicit allow state.",
  });

const NEGATIVE_COPY: Readonly<
  Record<
    Exclude<PromotionGateStatusBoardReasonCode, "BOARD_AVAILABLE">,
    Readonly<{
      outcome: Exclude<PromotionGateStatusBoardOutcome, "ANSWER">;
      heading: string;
      summaryText: string;
      ariaLive: "polite" | "assertive";
    }>
  >
> = Object.freeze({
  BOARD_UNAVAILABLE: Object.freeze({
    outcome: "ABSTAIN",
    heading: "Promotion-gate board unavailable",
    summaryText: "A complete governed status projection is not available.",
    ariaLive: "polite",
  }),
  POLICY_DENIED: Object.freeze({
    outcome: "DENY",
    heading: "Promotion-gate board withheld",
    summaryText: "Policy does not permit this status projection to be displayed.",
    ariaLive: "assertive",
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR",
    heading: "Promotion-gate board unavailable",
    summaryText: "The governed status projection could not be completed.",
    ariaLive: "assertive",
  }),
});

function hidden(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): PromotionGateStatusBoardViewModel {
  return Object.freeze({
    visibility: "HIDDEN",
    outcome: "ERROR",
    code,
    heading: "Promotion-gate board unavailable",
    summaryText: "No status board is rendered without a valid governed projection.",
    observedAt: null,
    candidateRef: null,
    boardState: null,
    counts: null,
    components: EMPTY_COMPONENTS,
    ariaLive: "polite",
  });
}

/** Resolve a closed gate-status projection into a read-only reviewer view. */
export function resolvePromotionGateStatusBoard(
  input?: unknown,
): PromotionGateStatusBoardViewModel {
  if (input === undefined) return hidden("NO_GOVERNED_RESPONSE");
  const parsed = parsePromotionGateStatusBoardProjection(input);
  if (!parsed.ok) return hidden("INVALID_PAYLOAD");
  const { payload } = parsed;

  if (payload.outcome !== "ANSWER") {
    const copy = NEGATIVE_COPY[
      payload.reasonCode as Exclude<
        PromotionGateStatusBoardReasonCode,
        "BOARD_AVAILABLE"
      >
    ];
    return Object.freeze({
      visibility: "VISIBLE",
      outcome: copy.outcome,
      code: payload.reasonCode,
      heading: copy.heading,
      summaryText: copy.summaryText,
      observedAt: null,
      candidateRef: null,
      boardState: null,
      counts: null,
      components: EMPTY_COMPONENTS,
      ariaLive: copy.ariaLive,
    });
  }

  return Object.freeze({
    visibility: "VISIBLE",
    outcome: "ANSWER",
    code: "BOARD_AVAILABLE",
    heading: "Promotion gate status board",
    summaryText: `${BOARD_STATE_COPY[payload.boardState!]} The board does not execute checks, authenticate review, permit promotion, authorize release, or publish anything.`,
    observedAt: payload.observedAt,
    candidateRef: payload.candidateRef,
    boardState: payload.boardState,
    counts: payload.summary,
    components: payload.components,
    ariaLive:
      payload.boardState === "DENY" || payload.boardState === "ERROR"
        ? "assertive"
        : "polite",
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

/** Mount a text-first, non-interactive promotion-gate status board. */
export function mountPromotionGateStatusBoard(
  host: HTMLElement,
  input?: unknown,
): PromotionGateStatusBoardController {
  const state = resolvePromotionGateStatusBoard(input);
  host.replaceChildren();
  if (state.visibility === "HIDDEN") {
    return Object.freeze({ state, destroy: () => host.replaceChildren() });
  }

  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const summary = document.createElement("p");
  const headingId = "kfm-promotion-gate-status-board-heading";
  section.dataset.component = "promotion-gate-status-board";
  section.dataset.outcome = state.outcome;
  if (state.boardState !== null) section.dataset.boardState = state.boardState;
  section.setAttribute("role", state.outcome === "ANSWER" ? "region" : "status");
  section.setAttribute("aria-live", state.ariaLive);
  section.setAttribute("aria-labelledby", headingId);
  heading.id = headingId;
  heading.textContent = state.heading;
  summary.textContent = state.summaryText;
  section.append(heading, summary);

  if (
    state.outcome === "ANSWER" &&
    state.observedAt !== null &&
    state.candidateRef !== null &&
    state.boardState !== null &&
    state.counts !== null
  ) {
    const metadata = document.createElement("dl");
    appendDefinition(document, metadata, "Board state", state.boardState);
    appendDefinition(document, metadata, "Observed at", state.observedAt);
    appendDefinition(document, metadata, "Candidate", state.candidateRef);
    appendDefinition(
      document,
      metadata,
      "Counts",
      `${state.counts.passCount} pass; ${state.counts.holdCount} hold; ${state.counts.denyCount} deny; ${state.counts.errorCount} error; ${state.counts.notRunCount} not run`,
    );

    const table = document.createElement("table");
    const caption = document.createElement("caption");
    const head = document.createElement("thead");
    const body = document.createElement("tbody");
    const headerRow = document.createElement("tr");
    caption.textContent = "Projected promotion-gate component states";
    for (const label of ["Component", "State", "Reason", "Artifact reference"]) {
      const cell = document.createElement("th");
      cell.scope = "col";
      cell.textContent = label;
      headerRow.append(cell);
    }
    head.append(headerRow);

    for (const component of state.components) {
      const row = document.createElement("tr");
      row.dataset.componentKind = component.kind;
      row.dataset.componentState = component.state;
      for (const value of [
        component.kind,
        component.state,
        component.reasonCode,
        component.artifactRef ?? "Not run",
      ]) {
        const cell = document.createElement("td");
        cell.textContent = value;
        row.append(cell);
      }
      body.append(row);
    }
    table.append(caption, head, body);
    section.append(metadata, table);
  }

  host.replaceChildren(section);
  return Object.freeze({ state, destroy: () => host.replaceChildren() });
}
