import {
  type GovernedProvenanceCitation,
  type ProvenanceCitationsOutcome,
  type ProvenanceCitationsReasonCode,
  type RepublicationNoteCode,
  parseProvenanceCitationsProjection,
} from "../../adapters/ProvenanceCitationsProjection";

export type ProvenanceCitationsViewModel = Readonly<{
  visibility: "VISIBLE" | "HIDDEN";
  outcome: ProvenanceCitationsOutcome;
  code:
    | ProvenanceCitationsReasonCode
    | "NO_GOVERNED_RESPONSE"
    | "INVALID_PAYLOAD";
  heading: string;
  summary: string;
  citations: readonly GovernedProvenanceCitation[];
  republicationNote: string | null;
  activityRef: string | null;
  releaseManifestRef: string | null;
  ariaLive: "polite" | "assertive";
}>;

export type ProvenanceCitationsController = Readonly<{
  state: ProvenanceCitationsViewModel;
  destroy: () => void;
}>;

const EMPTY_CITATIONS: readonly GovernedProvenanceCitation[] = Object.freeze([]);
const REPUBLICATION_NOTE: Readonly<Record<RepublicationNoteCode, string>> =
  Object.freeze({
    KFM_DERIVED_REPUBLICATION:
      "KFM republishes a derived representation; consult the cited source and provenance activity for source context.",
    SOURCE_PRESERVED:
      "The source citation is preserved as supplied by the governed projection.",
  });

const NEGATIVE_COPY: Readonly<
  Record<
    Exclude<ProvenanceCitationsReasonCode, "CITATIONS_AVAILABLE">,
    Readonly<{
      outcome: Exclude<ProvenanceCitationsOutcome, "ANSWER">;
      heading: string;
      summary: string;
      ariaLive: "polite" | "assertive";
    }>
  >
> = Object.freeze({
  CITATIONS_MISSING: Object.freeze({
    outcome: "ABSTAIN",
    heading: "Citations unavailable",
    summary: "Required public citation material is incomplete.",
    ariaLive: "polite",
  }),
  POLICY_DENIED: Object.freeze({
    outcome: "DENY",
    heading: "Citations withheld",
    summary: "Policy does not permit this citation projection to be displayed.",
    ariaLive: "assertive",
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR",
    heading: "Citations unavailable",
    summary: "The governed citation projection could not be completed.",
    ariaLive: "assertive",
  }),
});

function hidden(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): ProvenanceCitationsViewModel {
  return Object.freeze({
    visibility: "HIDDEN",
    outcome: "ERROR",
    code,
    heading: "Citations unavailable",
    summary: "No citation panel is rendered without a valid governed projection.",
    citations: EMPTY_CITATIONS,
    republicationNote: null,
    activityRef: null,
    releaseManifestRef: null,
    ariaLive: "polite",
  });
}

/** Resolve a governed projection into bounded reader-facing citation state. */
export function resolveProvenanceCitations(
  input?: unknown,
): ProvenanceCitationsViewModel {
  if (input === undefined) return hidden("NO_GOVERNED_RESPONSE");
  const parsed = parseProvenanceCitationsProjection(input);
  if (!parsed.ok) return hidden("INVALID_PAYLOAD");
  const { payload } = parsed;
  if (payload.outcome !== "ANSWER") {
    const copy = NEGATIVE_COPY[
      payload.reasonCode as Exclude<
        ProvenanceCitationsReasonCode,
        "CITATIONS_AVAILABLE"
      >
    ];
    return Object.freeze({
      visibility: "VISIBLE",
      outcome: copy.outcome,
      code: payload.reasonCode,
      heading: copy.heading,
      summary: copy.summary,
      citations: EMPTY_CITATIONS,
      republicationNote: null,
      activityRef: null,
      releaseManifestRef: null,
      ariaLive: copy.ariaLive,
    });
  }

  return Object.freeze({
    visibility: "VISIBLE",
    outcome: "ANSWER",
    code: "CITATIONS_AVAILABLE",
    heading: payload.title ?? "Provenance citations",
    summary:
      "These links identify cited sources. Display does not establish evidence sufficiency, rights, review, release, or publication authority.",
    citations: payload.citations,
    republicationNote:
      payload.republicationNoteCode === null
        ? null
        : REPUBLICATION_NOTE[payload.republicationNoteCode],
    activityRef: payload.activityRef,
    releaseManifestRef: payload.releaseManifestRef,
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

/** Mount a text-first, link-only provenance citations panel. */
export function mountProvenanceCitations(
  host: HTMLElement,
  input?: unknown,
): ProvenanceCitationsController {
  const state = resolveProvenanceCitations(input);
  host.replaceChildren();
  if (state.visibility === "HIDDEN") {
    return Object.freeze({ state, destroy: () => host.replaceChildren() });
  }

  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const summary = document.createElement("p");
  const headingId = "kfm-provenance-citations-heading";
  section.dataset.component = "provenance-citations";
  section.dataset.outcome = state.outcome;
  section.setAttribute("role", state.outcome === "ANSWER" ? "region" : "status");
  section.setAttribute("aria-live", state.ariaLive);
  section.setAttribute("aria-labelledby", headingId);
  heading.id = headingId;
  heading.textContent = state.heading;
  summary.textContent = state.summary;
  section.append(heading, summary);

  if (state.outcome === "ANSWER") {
    const citations = document.createElement("ul");
    for (const citation of state.citations) {
      const item = document.createElement("li");
      const link = document.createElement("a");
      const evidence = document.createElement("p");
      link.dataset.citationId = citation.citationId;
      link.href = citation.href;
      link.textContent = citation.label;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.referrerPolicy = "no-referrer";
      evidence.textContent =
        citation.doi === null
          ? `Evidence reference: ${citation.evidenceRef}`
          : `DOI: ${citation.doi}; evidence reference: ${citation.evidenceRef}`;
      item.append(link, evidence);
      citations.append(item);
    }

    const references = document.createElement("dl");
    if (state.activityRef !== null) {
      appendReference(document, references, "Provenance activity", state.activityRef);
    }
    if (state.releaseManifestRef !== null) {
      appendReference(document, references, "Release manifest", state.releaseManifestRef);
    }
    section.append(citations, references);
    if (state.republicationNote !== null) {
      const note = document.createElement("p");
      note.dataset.republicationNote = "true";
      note.textContent = state.republicationNote;
      section.append(note);
    }
  }

  host.replaceChildren(section);
  return Object.freeze({
    state,
    destroy: () => host.replaceChildren(),
  });
}
