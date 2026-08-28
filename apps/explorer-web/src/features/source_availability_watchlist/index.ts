import {
  type SourceAvailabilityWatchlistEntry,
  type SourceAvailabilityWatchlistOutcome,
  type SourceAvailabilityWatchlistReasonCode,
  type SourceAvailabilityWatchlistSummary,
  type WatchlistState,
  parseSourceAvailabilityWatchlistProjection,
} from "../../adapters/SourceAvailabilityWatchlistProjection";

export type SourceAvailabilityWatchlistViewModel = Readonly<{
  visibility: "VISIBLE" | "HIDDEN";
  outcome: SourceAvailabilityWatchlistOutcome;
  code:
    | SourceAvailabilityWatchlistReasonCode
    | "NO_GOVERNED_RESPONSE"
    | "INVALID_PAYLOAD";
  heading: string;
  summaryText: string;
  observedAt: string | null;
  watchlistId: string | null;
  state: WatchlistState | null;
  counts: SourceAvailabilityWatchlistSummary | null;
  entries: readonly SourceAvailabilityWatchlistEntry[];
  ariaLive: "polite" | "assertive";
}>;

export type SourceAvailabilityWatchlistController = Readonly<{
  state: SourceAvailabilityWatchlistViewModel;
  destroy: () => void;
}>;

const EMPTY_ENTRIES: readonly SourceAvailabilityWatchlistEntry[] = Object.freeze([]);

const STATE_COPY: Readonly<Record<WatchlistState, string>> = Object.freeze({
  STABLE:
    "All displayed sources are stable under the supplied health and material-change assessments.",
  REVIEW_REQUIRED:
    "At least one material schema or content change is routed to a separately referenced review candidate.",
  HOLD:
    "At least one source remains held because current availability or materiality is unresolved.",
  ERROR:
    "At least one assessment reports an error. The watchlist creates no fallback authority.",
});

const NEGATIVE_COPY: Readonly<
  Record<
    Exclude<SourceAvailabilityWatchlistReasonCode, "WATCHLIST_AVAILABLE">,
    Readonly<{
      outcome: Exclude<SourceAvailabilityWatchlistOutcome, "ANSWER">;
      heading: string;
      summaryText: string;
      ariaLive: "polite" | "assertive";
    }>
  >
> = Object.freeze({
  WATCHLIST_UNAVAILABLE: Object.freeze({
    outcome: "ABSTAIN",
    heading: "Source watchlist unavailable",
    summaryText: "A complete governed watchlist projection is not available.",
    ariaLive: "polite",
  }),
  POLICY_DENIED: Object.freeze({
    outcome: "DENY",
    heading: "Source watchlist withheld",
    summaryText: "Policy does not permit this watchlist projection to be displayed.",
    ariaLive: "assertive",
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR",
    heading: "Source watchlist unavailable",
    summaryText: "The governed watchlist projection could not be completed.",
    ariaLive: "assertive",
  }),
});

function hidden(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): SourceAvailabilityWatchlistViewModel {
  return Object.freeze({
    visibility: "HIDDEN",
    outcome: "ERROR",
    code,
    heading: "Source watchlist unavailable",
    summaryText: "No watchlist is rendered without a valid governed projection.",
    observedAt: null,
    watchlistId: null,
    state: null,
    counts: null,
    entries: EMPTY_ENTRIES,
    ariaLive: "polite",
  });
}

/** Resolve a strict source-watchlist projection into a read-only view model. */
export function resolveSourceAvailabilityWatchlist(
  input?: unknown,
): SourceAvailabilityWatchlistViewModel {
  if (input === undefined) return hidden("NO_GOVERNED_RESPONSE");
  const parsed = parseSourceAvailabilityWatchlistProjection(input);
  if (!parsed.ok) return hidden("INVALID_PAYLOAD");
  const { payload } = parsed;

  if (payload.outcome !== "ANSWER") {
    const copy = NEGATIVE_COPY[
      payload.reasonCode as Exclude<
        SourceAvailabilityWatchlistReasonCode,
        "WATCHLIST_AVAILABLE"
      >
    ];
    return Object.freeze({
      visibility: "VISIBLE",
      outcome: copy.outcome,
      code: payload.reasonCode,
      heading: copy.heading,
      summaryText: copy.summaryText,
      observedAt: null,
      watchlistId: null,
      state: null,
      counts: null,
      entries: EMPTY_ENTRIES,
      ariaLive: copy.ariaLive,
    });
  }

  return Object.freeze({
    visibility: "VISIBLE",
    outcome: "ANSWER",
    code: "WATCHLIST_AVAILABLE",
    heading: "Source availability watchlist",
    summaryText: `${STATE_COPY[payload.state!]} Display is review routing only; it does not probe sources, create work, or authorize lifecycle, release, or publication actions.`,
    observedAt: payload.observedAt,
    watchlistId: payload.watchlistId,
    state: payload.state,
    counts: payload.summary,
    entries: payload.entries,
    ariaLive: payload.state === "ERROR" ? "assertive" : "polite",
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

/** Mount a text-first, non-interactive source availability watchlist. */
export function mountSourceAvailabilityWatchlist(
  host: HTMLElement,
  input?: unknown,
): SourceAvailabilityWatchlistController {
  const state = resolveSourceAvailabilityWatchlist(input);
  host.replaceChildren();
  if (state.visibility === "HIDDEN") {
    return Object.freeze({ state, destroy: () => host.replaceChildren() });
  }

  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const summary = document.createElement("p");
  const headingId = "kfm-source-availability-watchlist-heading";
  section.dataset.component = "source-availability-watchlist";
  section.dataset.outcome = state.outcome;
  if (state.state !== null) section.dataset.watchlistState = state.state;
  section.setAttribute("role", state.outcome === "ANSWER" ? "region" : "status");
  section.setAttribute("aria-live", state.ariaLive);
  section.setAttribute("aria-labelledby", headingId);
  heading.id = headingId;
  heading.textContent = state.heading;
  summary.textContent = state.summaryText;
  section.append(heading, summary);

  if (
    state.outcome === "ANSWER" &&
    state.counts !== null &&
    state.observedAt !== null &&
    state.watchlistId !== null &&
    state.state !== null
  ) {
    const metadata = document.createElement("dl");
    appendDefinition(document, metadata, "Watchlist state", state.state);
    appendDefinition(document, metadata, "Observed at", state.observedAt);
    appendDefinition(document, metadata, "Watchlist ID", state.watchlistId);
    appendDefinition(
      document,
      metadata,
      "Counts",
      `${state.counts.sourceCount} sources; ${state.counts.stableCount} stable; ${state.counts.reviewCount} review; ${state.counts.holdCount} hold; ${state.counts.errorCount} error`,
    );

    const table = document.createElement("table");
    const caption = document.createElement("caption");
    const head = document.createElement("thead");
    const body = document.createElement("tbody");
    const headerRow = document.createElement("tr");
    caption.textContent = "Source availability and material-change routing";
    for (const label of [
      "Source",
      "Availability",
      "Change",
      "Route",
      "Candidate work",
    ]) {
      const cell = document.createElement("th");
      cell.scope = "col";
      cell.textContent = label;
      headerRow.append(cell);
    }
    head.append(headerRow);

    for (const entry of state.entries) {
      const row = document.createElement("tr");
      row.dataset.sourceId = entry.sourceId;
      row.dataset.route = entry.route;
      const values = [
        entry.sourceId,
        entry.availability,
        `${entry.changeClass} / ${entry.materialKind}`,
        entry.route,
        entry.candidateWorkRef ?? "None",
      ];
      for (const value of values) {
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
