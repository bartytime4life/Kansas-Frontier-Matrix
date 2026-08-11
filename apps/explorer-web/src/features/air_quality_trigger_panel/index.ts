import {
  type AirQualityPanelOutcome,
  type AirQualityPanelReasonCode,
  type AirQualityTriggerCandidate,
  parseAirQualityTriggerProjection,
} from "../../adapters/AirQualityTriggerProjection";

export type AirQualityTriggerPanelState = Readonly<{
  visibility: "VISIBLE" | "HIDDEN";
  outcome: AirQualityPanelOutcome;
  code: AirQualityPanelReasonCode | "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD";
  heading: string;
  message: string;
  candidate: AirQualityTriggerCandidate | null;
  ariaLive: "polite" | "assertive";
}>;

export type AirQualityTriggerPanelController = Readonly<{
  state: AirQualityTriggerPanelState;
  destroy: () => void;
}>;

const NEGATIVE_COPY = Object.freeze({
  CONTEXT_HELD: Object.freeze({
    outcome: "ABSTAIN" as const,
    heading: "PM2.5 trigger context held",
    message: "The governed categorical context is incomplete or unsuitable.",
    ariaLive: "polite" as const,
  }),
  POLICY_DENIED: Object.freeze({
    outcome: "DENY" as const,
    heading: "PM2.5 trigger panel withheld",
    message: "Policy does not permit this candidate projection to be displayed.",
    ariaLive: "assertive" as const,
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR" as const,
    heading: "PM2.5 trigger panel unavailable",
    message: "The governed categorical assessment could not be completed.",
    ariaLive: "assertive" as const,
  }),
});

function hidden(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): AirQualityTriggerPanelState {
  return Object.freeze({
    visibility: "HIDDEN",
    outcome: "ERROR",
    code,
    heading: "PM2.5 trigger panel unavailable",
    message: "No panel is rendered without a valid governed projection.",
    candidate: null,
    ariaLive: "polite",
  });
}

/** Resolve a governed projection into a read-only categorical panel state. */
export function resolveAirQualityTriggerPanel(
  input?: unknown,
): AirQualityTriggerPanelState {
  if (input === undefined) return hidden("NO_GOVERNED_RESPONSE");
  const parsed = parseAirQualityTriggerProjection(input);
  if (!parsed.ok) return hidden("INVALID_PAYLOAD");
  const { payload } = parsed;
  if (payload.outcome !== "ANSWER") {
    const copy = NEGATIVE_COPY[
      payload.reasonCode as Exclude<
        AirQualityPanelReasonCode,
        "TRIGGER_CANDIDATE_AVAILABLE" | "NO_TRIGGER_CANDIDATE"
      >
    ];
    return Object.freeze({
      visibility: "VISIBLE",
      outcome: copy.outcome,
      code: payload.reasonCode,
      heading: copy.heading,
      message: copy.message,
      candidate: null,
      ariaLive: copy.ariaLive,
    });
  }
  const trigger = payload.reasonCode === "TRIGGER_CANDIDATE_AVAILABLE";
  return Object.freeze({
    visibility: "VISIBLE",
    outcome: "ANSWER",
    code: payload.reasonCode,
    heading: trigger ? "PM2.5 trigger candidate" : "No PM2.5 trigger candidate",
    message: trigger
      ? "A fixture-only candidate has the required categorical relations and evidence references. It is not an air-quality event, regulatory finding, AQI statement, or health advice."
      : "The fixture-only categorical relations do not support a trigger candidate. This is not an air-quality finding or health advice.",
    candidate: payload.candidate,
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

function appendCandidateDetails(
  document: Document,
  section: HTMLElement,
  candidate: AirQualityTriggerCandidate,
): void {
  const status = document.createElement("p");
  const summary = document.createElement("dl");
  const references = document.createElement("details");
  const referencesSummary = document.createElement("summary");
  const referenceList = document.createElement("dl");
  status.dataset.airQualityCandidateState = candidate.candidateState;
  status.textContent = `Candidate state: ${candidate.candidateState}`;
  appendDefinition(document, summary, "Knowledge character", candidate.knowledgeCharacter);
  appendDefinition(document, summary, "Observed at", candidate.observedAt);
  appendDefinition(document, summary, "Threshold relation", candidate.thresholdRelation);
  appendDefinition(
    document,
    summary,
    "Trailing-median relation",
    candidate.trailingMedianRelation,
  );
  appendDefinition(document, summary, "Evidence state", candidate.evidenceState);
  appendDefinition(
    document,
    summary,
    "Evidence reference count",
    String(candidate.evidenceRefs.length),
  );
  section.append(status, summary);

  referencesSummary.textContent = "Inspect fixture-bound references";
  appendDefinition(document, referenceList, "Assessment", candidate.assessmentRef);
  appendDefinition(document, referenceList, "Observation", candidate.observationRef);
  appendDefinition(
    document,
    referenceList,
    "Trailing median",
    candidate.trailingMedianRef,
  );
  candidate.evidenceRefs.forEach((reference, index) =>
    appendDefinition(document, referenceList, `Evidence reference ${index + 1}`, reference),
  );
  references.append(referencesSummary, referenceList);
  section.append(references);
}

/** Mount a non-mutating, categorical air-quality trigger panel. */
export function mountAirQualityTriggerPanel(
  host: HTMLElement,
  input?: unknown,
): AirQualityTriggerPanelController {
  const state = resolveAirQualityTriggerPanel(input);
  host.replaceChildren();
  if (state.visibility === "HIDDEN") {
    return Object.freeze({ state, destroy: () => host.replaceChildren() });
  }
  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const message = document.createElement("p");
  const headingId = "kfm-air-quality-trigger-panel-heading";
  section.dataset.component = "air-quality-trigger-panel";
  section.dataset.outcome = state.outcome;
  section.setAttribute("role", state.outcome === "ANSWER" ? "region" : "status");
  section.setAttribute("aria-live", state.ariaLive);
  section.setAttribute("aria-labelledby", headingId);
  heading.id = headingId;
  heading.textContent = state.heading;
  message.textContent = state.message;
  section.append(heading, message);
  if (state.outcome === "ANSWER" && state.candidate !== null) {
    appendCandidateDetails(document, section, state.candidate);
  }
  host.replaceChildren(section);
  return Object.freeze({ state, destroy: () => host.replaceChildren() });
}
