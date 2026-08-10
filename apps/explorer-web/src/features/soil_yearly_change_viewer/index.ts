import {
  type GovernedSoilYearlyChangeProjection,
  type SoilSnapshotAnchor,
  type SoilYearlyChangeOutcome,
  type SoilYearlyChangeProvenance,
  type SoilYearlyChangeReasonCode,
  type SoilYearlyDiffSummary,
  parseSoilYearlyChangeProjection,
} from "../../adapters/SoilYearlyChangeProjection";

export type SoilYearlyChangeViewerState = Readonly<{
  visibility: "VISIBLE" | "HIDDEN";
  outcome: SoilYearlyChangeOutcome;
  code:
    | SoilYearlyChangeReasonCode
    | "NO_GOVERNED_RESPONSE"
    | "INVALID_PAYLOAD";
  heading: string;
  summary: string;
  previousSnapshot: SoilSnapshotAnchor | null;
  currentSnapshot: SoilSnapshotAnchor | null;
  diff: SoilYearlyDiffSummary | null;
  provenance: SoilYearlyChangeProvenance | null;
  sourceDescriptorRef: string | null;
  ariaLive: "polite" | "assertive";
}>;

export type SoilYearlyChangeViewerController = Readonly<{
  state: SoilYearlyChangeViewerState;
  destroy: () => void;
}>;

const NEGATIVE_COPY: Readonly<
  Record<
    Exclude<SoilYearlyChangeReasonCode, "DIFF_AVAILABLE">,
    Readonly<{
      outcome: Exclude<SoilYearlyChangeOutcome, "ANSWER">;
      heading: string;
      summary: string;
      ariaLive: "polite" | "assertive";
    }>
  >
> = Object.freeze({
  DIFF_MISSING: Object.freeze({
    outcome: "ABSTAIN",
    heading: "SSURGO comparison unavailable",
    summary: "The governed yearly-diff projection is incomplete.",
    ariaLive: "polite",
  }),
  POLICY_DENIED: Object.freeze({
    outcome: "DENY",
    heading: "SSURGO comparison withheld",
    summary: "Policy does not permit this comparison projection to be displayed.",
    ariaLive: "assertive",
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR",
    heading: "SSURGO comparison unavailable",
    summary: "The governed yearly-diff projection could not be completed.",
    ariaLive: "assertive",
  }),
});

function hidden(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): SoilYearlyChangeViewerState {
  return Object.freeze({
    visibility: "HIDDEN",
    outcome: "ERROR",
    code,
    heading: "SSURGO comparison unavailable",
    summary: "No comparison is rendered without a valid governed projection.",
    previousSnapshot: null,
    currentSnapshot: null,
    diff: null,
    provenance: null,
    sourceDescriptorRef: null,
    ariaLive: "polite",
  });
}

/** Resolve a governed projection into a read-only yearly comparison state. */
export function resolveSoilYearlyChangeViewer(
  input?: unknown,
): SoilYearlyChangeViewerState {
  if (input === undefined) return hidden("NO_GOVERNED_RESPONSE");
  const parsed = parseSoilYearlyChangeProjection(input);
  if (!parsed.ok) return hidden("INVALID_PAYLOAD");
  const { payload } = parsed;
  if (payload.outcome !== "ANSWER") {
    const copy = NEGATIVE_COPY[
      payload.reasonCode as Exclude<
        SoilYearlyChangeReasonCode,
        "DIFF_AVAILABLE"
      >
    ];
    return Object.freeze({
      visibility: "VISIBLE",
      outcome: copy.outcome,
      code: payload.reasonCode,
      heading: copy.heading,
      summary: copy.summary,
      previousSnapshot: null,
      currentSnapshot: null,
      diff: null,
      provenance: null,
      sourceDescriptorRef: null,
      ariaLive: copy.ariaLive,
    });
  }

  return Object.freeze({
    visibility: "VISIBLE",
    outcome: "ANSWER",
    code: "DIFF_AVAILABLE",
    heading: "SSURGO yearly change comparison",
    summary:
      "Fixture-only record differences between two year-pinned snapshots. Counts do not establish soil change, materiality, promotion, release, or publication readiness.",
    previousSnapshot: payload.previousSnapshot,
    currentSnapshot: payload.currentSnapshot,
    diff: payload.diff,
    provenance: payload.provenance,
    sourceDescriptorRef: payload.sourceDescriptorRef,
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

function appendSnapshot(
  document: Document,
  host: HTMLElement,
  label: string,
  snapshot: SoilSnapshotAnchor,
): void {
  const section = document.createElement("section");
  const heading = document.createElement("h3");
  const references = document.createElement("dl");
  heading.textContent = `${label} snapshot: ${snapshot.datasetYear}`;
  appendDefinition(document, references, "Artifact", snapshot.artifactRef);
  appendDefinition(document, references, "Artifact digest", snapshot.artifactSha256);
  appendDefinition(document, references, "STAC item", snapshot.stacItemRef);
  appendDefinition(document, references, "PROV entity", snapshot.provEntityRef);
  appendDefinition(
    document,
    references,
    "Snapshot receipt",
    snapshot.snapshotReceiptRef,
  );
  appendDefinition(
    document,
    references,
    "Validation receipt",
    snapshot.validationReceiptRef,
  );
  section.append(heading, references);
  host.append(section);
}

function appendPositiveContent(
  document: Document,
  section: HTMLElement,
  payload: GovernedSoilYearlyChangeProjection,
): void {
  const previous = payload.previousSnapshot;
  const current = payload.currentSnapshot;
  const diff = payload.diff;
  const provenance = payload.provenance;
  if (
    previous === null ||
    current === null ||
    diff === null ||
    provenance === null ||
    payload.sourceDescriptorRef === null
  ) {
    return;
  }

  const years = document.createElement("p");
  const metrics = document.createElement("dl");
  const changedHeading = document.createElement("h3");
  const changed = document.createElement("ul");
  const details = document.createElement("details");
  const detailsSummary = document.createElement("summary");
  const anchors = document.createElement("div");
  const provenanceList = document.createElement("dl");

  years.dataset.yearRange = `${previous.datasetYear}-${current.datasetYear}`;
  years.textContent = `${previous.datasetYear} to ${current.datasetYear}`;
  appendDefinition(document, metrics, "Added records", String(diff.addedRecords));
  appendDefinition(
    document,
    metrics,
    "Removed records",
    String(diff.removedRecords),
  );
  appendDefinition(
    document,
    metrics,
    "Modified records",
    String(diff.modifiedRecords),
  );
  changedHeading.textContent = "Changed properties";
  for (const propertyName of diff.changedPropertyNames) {
    const item = document.createElement("li");
    item.textContent = propertyName;
    changed.append(item);
  }

  detailsSummary.textContent = "Inspect fixture provenance anchors";
  appendDefinition(
    document,
    provenanceList,
    "Source descriptor",
    payload.sourceDescriptorRef,
  );
  appendDefinition(document, provenanceList, "Diff artifact", diff.diffArtifactRef);
  appendDefinition(
    document,
    provenanceList,
    "Diff digest",
    diff.diffArtifactSha256,
  );
  appendDefinition(
    document,
    provenanceList,
    "Fetch activity",
    provenance.fetchActivityRef,
  );
  appendDefinition(
    document,
    provenanceList,
    "Validation activity",
    provenance.validationActivityRef,
  );
  appendDefinition(
    document,
    provenanceList,
    "Diff activity",
    provenance.diffActivityRef,
  );
  anchors.append(provenanceList);
  appendSnapshot(document, anchors, "Previous", previous);
  appendSnapshot(document, anchors, "Current", current);
  details.append(detailsSummary, anchors);
  section.append(years, metrics, changedHeading, changed, details);
}

/** Mount a text-first, non-mutating SSURGO yearly change viewer. */
export function mountSoilYearlyChangeViewer(
  host: HTMLElement,
  input?: unknown,
): SoilYearlyChangeViewerController {
  const state = resolveSoilYearlyChangeViewer(input);
  host.replaceChildren();
  if (state.visibility === "HIDDEN") {
    return Object.freeze({ state, destroy: () => host.replaceChildren() });
  }

  const parsed = parseSoilYearlyChangeProjection(input);
  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const summary = document.createElement("p");
  const headingId = "kfm-soil-yearly-change-heading";
  section.dataset.component = "soil-yearly-change-viewer";
  section.dataset.outcome = state.outcome;
  section.setAttribute("role", state.outcome === "ANSWER" ? "region" : "status");
  section.setAttribute("aria-live", state.ariaLive);
  section.setAttribute("aria-labelledby", headingId);
  heading.id = headingId;
  heading.textContent = state.heading;
  summary.textContent = state.summary;
  section.append(heading, summary);

  if (parsed.ok && parsed.payload.outcome === "ANSWER") {
    appendPositiveContent(document, section, parsed.payload);
  }
  host.replaceChildren(section);
  return Object.freeze({
    state,
    destroy: () => host.replaceChildren(),
  });
}
