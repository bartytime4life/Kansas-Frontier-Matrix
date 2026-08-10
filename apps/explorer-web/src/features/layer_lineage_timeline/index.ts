import {
  type GovernedLayerLineageEntry,
  type LayerLineageEventType,
  type LayerLineageOutcome,
  type LayerLineageReasonCode,
  parseLayerLineageProjection,
} from "../../adapters/LayerLineageProjection";

export type LayerLineageTimelineViewModel = Readonly<{
  visibility: "VISIBLE" | "HIDDEN";
  outcome: LayerLineageOutcome;
  code:
    | LayerLineageReasonCode
    | "NO_GOVERNED_RESPONSE"
    | "INVALID_PAYLOAD";
  heading: string;
  summary: string;
  currentState: LayerLineageEventType | null;
  layerRef: string | null;
  currentReleaseRef: string | null;
  entries: readonly GovernedLayerLineageEntry[];
  ariaLive: "polite" | "assertive";
}>;

export type LayerLineageTimelineController = Readonly<{
  state: LayerLineageTimelineViewModel;
  destroy: () => void;
}>;

const EMPTY_ENTRIES: readonly GovernedLayerLineageEntry[] = Object.freeze([]);
const EVENT_LABEL: Readonly<Record<LayerLineageEventType, string>> =
  Object.freeze({
    RELEASED: "Release established",
    CORRECTED: "Correction published",
    ROLLED_BACK: "Rollback applied",
    WITHDRAWN: "Release withdrawn",
  });
const NEGATIVE_COPY: Readonly<
  Record<
    Exclude<LayerLineageReasonCode, "LINEAGE_AVAILABLE">,
    Readonly<{
      outcome: Exclude<LayerLineageOutcome, "ANSWER">;
      heading: string;
      summary: string;
      ariaLive: "polite" | "assertive";
    }>
  >
> = Object.freeze({
  LINEAGE_MISSING: Object.freeze({
    outcome: "ABSTAIN",
    heading: "Release lineage unavailable",
    summary: "Required public correction and rollback lineage is incomplete.",
    ariaLive: "polite",
  }),
  POLICY_DENIED: Object.freeze({
    outcome: "DENY",
    heading: "Release lineage withheld",
    summary: "Policy does not permit this lineage projection to be displayed.",
    ariaLive: "assertive",
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR",
    heading: "Release lineage unavailable",
    summary: "The governed lineage projection could not be completed.",
    ariaLive: "assertive",
  }),
});

function hidden(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): LayerLineageTimelineViewModel {
  return Object.freeze({
    visibility: "HIDDEN",
    outcome: "ERROR",
    code,
    heading: "Release lineage unavailable",
    summary: "No timeline is rendered without a valid governed projection.",
    currentState: null,
    layerRef: null,
    currentReleaseRef: null,
    entries: EMPTY_ENTRIES,
    ariaLive: "polite",
  });
}

/** Resolve a governed projection into a read-only timeline view model. */
export function resolveLayerLineageTimeline(
  input?: unknown,
): LayerLineageTimelineViewModel {
  if (input === undefined) return hidden("NO_GOVERNED_RESPONSE");
  const parsed = parseLayerLineageProjection(input);
  if (!parsed.ok) return hidden("INVALID_PAYLOAD");
  const { payload } = parsed;
  if (payload.outcome !== "ANSWER") {
    const copy = NEGATIVE_COPY[
      payload.reasonCode as Exclude<LayerLineageReasonCode, "LINEAGE_AVAILABLE">
    ];
    return Object.freeze({
      visibility: "VISIBLE",
      outcome: copy.outcome,
      code: payload.reasonCode,
      heading: copy.heading,
      summary: copy.summary,
      currentState: null,
      layerRef: null,
      currentReleaseRef: null,
      entries: EMPTY_ENTRIES,
      ariaLive: copy.ariaLive,
    });
  }

  return Object.freeze({
    visibility: "VISIBLE",
    outcome: "ANSWER",
    code: "LINEAGE_AVAILABLE",
    heading: "Rollback and correction lineage",
    summary:
      "Read-only lineage. This surface cannot correct, withdraw, roll back, release, or publish artifacts.",
    currentState: payload.currentState,
    layerRef: payload.layerRef,
    currentReleaseRef: payload.currentReleaseRef,
    entries: payload.entries,
    ariaLive: "polite",
  });
}

function appendReference(
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

/** Mount a chronological, read-only rollback/correction timeline. */
export function mountLayerLineageTimeline(
  host: HTMLElement,
  input?: unknown,
): LayerLineageTimelineController {
  const state = resolveLayerLineageTimeline(input);
  host.replaceChildren();
  if (state.visibility === "HIDDEN") {
    return Object.freeze({ state, destroy: () => host.replaceChildren() });
  }

  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const summary = document.createElement("p");
  const headingId = "kfm-layer-lineage-heading";
  section.dataset.component = "layer-lineage-timeline";
  section.dataset.outcome = state.outcome;
  section.setAttribute("role", state.outcome === "ANSWER" ? "region" : "status");
  section.setAttribute("aria-live", state.ariaLive);
  section.setAttribute("aria-labelledby", headingId);
  heading.id = headingId;
  heading.textContent = state.heading;
  summary.textContent = state.summary;
  section.append(heading, summary);

  if (state.outcome === "ANSWER" && state.currentState !== null) {
    const current = document.createElement("p");
    const timeline = document.createElement("ol");
    current.dataset.currentReleaseState = state.currentState;
    current.textContent = `Current release state: ${state.currentState}`;
    for (const entry of state.entries) {
      const item = document.createElement("li");
      const eventHeading = document.createElement("h3");
      const occurredAt = document.createElement("time");
      const references = document.createElement("dl");
      item.dataset.lineageSequence = String(entry.sequence);
      item.dataset.lineageEvent = entry.eventType;
      eventHeading.textContent = EVENT_LABEL[entry.eventType];
      occurredAt.dateTime = entry.occurredAt;
      occurredAt.textContent = entry.occurredAt;
      appendReference(document, references, "Artifact digest", entry.artifactDigest);
      appendReference(document, references, "Release", entry.releaseRef);
      if (entry.supersedesDigest !== null) {
        appendReference(
          document,
          references,
          "Supersedes artifact",
          entry.supersedesDigest,
        );
      }
      if (entry.correctionReceiptRef !== null) {
        appendReference(
          document,
          references,
          "Correction receipt",
          entry.correctionReceiptRef,
        );
      }
      if (entry.rollbackTargetRef !== null) {
        appendReference(
          document,
          references,
          "Rollback target",
          entry.rollbackTargetRef,
        );
      }
      item.append(eventHeading, occurredAt, references);
      timeline.append(item);
    }
    section.append(current, timeline);
  }

  host.replaceChildren(section);
  return Object.freeze({
    state,
    destroy: () => host.replaceChildren(),
  });
}
