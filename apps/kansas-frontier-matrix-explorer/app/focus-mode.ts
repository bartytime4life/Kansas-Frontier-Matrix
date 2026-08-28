import type { EvidenceState, ReleaseState, TemporalDefinition } from "./explorer-data";

export type FocusOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";
export type FocusResult = { outcome: FocusOutcome; title: string; body: string; code: string };
export type FocusStage = "outcome" | "checks" | "actions";
export type FocusIntentId = "explain" | "why" | "lineage" | "time";
export type FocusGateState = "PASS" | "NOTICE" | "HOLD" | "BLOCK" | "ERROR";
export type FocusGate = Readonly<{
  id: "context" | "time" | "evidence" | "rights" | "release" | "correction";
  label: string;
  state: FocusGateState;
  detail: string;
}>;
export type FocusActionKind = "SET_TIME" | "CENTER_SELECTION" | "OPEN_EVIDENCE" | "OPEN_METADATA" | "OPEN_LINEAGE" | "OPEN_SOURCES";
export type FocusActionProposal = Readonly<{
  id: string;
  kind: FocusActionKind;
  title: string;
  summary: string;
  before: string;
  after: string;
  impact: string;
  targetYear?: number;
}>;

export const FOCUS_INTENTS: readonly Readonly<{ id: FocusIntentId; label: string; shortLabel: string }>[] = Object.freeze([
  Object.freeze({ id: "explain", label: "Explain current context", shortLabel: "Explain" }),
  Object.freeze({ id: "why", label: "Why this outcome?", shortLabel: "Why" }),
  Object.freeze({ id: "lineage", label: "Trace the evidence", shortLabel: "Lineage" }),
  Object.freeze({ id: "time", label: "Compare active and source time", shortLabel: "Time" }),
]);

export const isFeatureTimeMismatch = (
  temporal: TemporalDefinition | undefined,
  featureYear: number,
  activeYear: number,
) => {
  if (!temporal) return false;
  if (temporal.mode === "exact") return featureYear !== activeYear;
  return featureYear > activeYear;
};

export const focusResultForState = (state: EvidenceState, timeMismatch = false): FocusResult => {
  // Controlling faults and policy boundaries take precedence over temporal support.
  if (state === "ERROR") {
    return { outcome: "ERROR", code: "ADAPTER_UNAVAILABLE", title: "Demonstration adapter failed safely", body: "An operational fault produced a finite error. No model output or fallback claim was generated." };
  }
  if (state === "DENIED_BY_POLICY" || state === "RESTRICTED_ACCESS") {
    return { outcome: "DENY", code: "PUBLIC_DISCLOSURE_BLOCKED", title: "Protected detail remains withheld", body: "Policy, rights, or sensitivity prevents this public client from resolving the requested detail." };
  }
  if (timeMismatch) {
    return { outcome: "ABSTAIN", code: "TIME_SCOPE_MISMATCH", title: "Active time is outside the selected support", body: "The selected fixture does not support an interpretation for the active Explorer year." };
  }
  if (state === "ANSWER" || state === "CORRECTED") {
    return { outcome: "ANSWER", code: "CITATIONS_VALID", title: "Bounded interpretation supported", body: "The selected site-local fixture has a matching demonstration evidence reference for its declared place and time scope." };
  }
  const abstainCodes: Partial<Record<EvidenceState, string>> = {
    MISSING_EVIDENCE: "SUPPORT_INSUFFICIENT",
    SOURCE_STALE: "SOURCE_STALE",
    GENERALIZED_GEOMETRY: "GEOMETRY_IS_NOT_EVIDENCE",
    SUPERSEDED: "SUPPORT_SUPERSEDED",
  };
  return { outcome: "ABSTAIN", code: abstainCodes[state] ?? "SUPPORT_INSUFFICIENT", title: "The Explorer declines to infer", body: "Available context does not support a broader claim, forecast, or precise interpretation." };
};

export const buildFocusGateTrace = ({
  state,
  timeMismatch,
  temporal,
  featureYear,
  activeYear,
  releaseState,
  correctionState,
}: {
  state: EvidenceState;
  timeMismatch: boolean;
  temporal?: TemporalDefinition;
  featureYear: number;
  activeYear: number;
  releaseState: ReleaseState;
  correctionState: string;
}): readonly FocusGate[] => {
  const evidenceGate: FocusGate = state === "ERROR"
    ? { id: "evidence", label: "Evidence resolution", state: "ERROR", detail: "The local adapter faulted; no fallback support was substituted." }
    : state === "DENIED_BY_POLICY" || state === "RESTRICTED_ACCESS"
      ? { id: "evidence", label: "Evidence resolution", state: "BLOCK", detail: "A controlling policy or access boundary prevents public resolution." }
      : state === "ANSWER"
        ? { id: "evidence", label: "Evidence resolution", state: "PASS", detail: "A matching site-local demonstration EvidenceRef is present." }
        : state === "CORRECTED"
          ? { id: "evidence", label: "Evidence resolution", state: "NOTICE", detail: "Support resolves, with a visible correction posture retained." }
          : { id: "evidence", label: "Evidence resolution", state: "HOLD", detail: "Support is missing, stale, generalized, or superseded; the resolver abstains." };

  const rightsGate: FocusGate = state === "DENIED_BY_POLICY" || state === "RESTRICTED_ACCESS"
    ? { id: "rights", label: "Rights and policy", state: "BLOCK", detail: "The public-safe projection cannot disclose the protected detail." }
    : state === "GENERALIZED_GEOMETRY"
      ? { id: "rights", label: "Rights and policy", state: "NOTICE", detail: "Generalized geometry may orient the view, but it cannot carry a precise claim." }
      : { id: "rights", label: "Rights and policy", state: "PASS", detail: "No additional site-fixture disclosure block controls this finite result." };

  return Object.freeze([
    Object.freeze({ id: "context", label: "Context identity", state: "PASS", detail: "Stable feature and layer identifiers are bound to this local session." }),
    Object.freeze(timeMismatch
      ? { id: "time", label: "Temporal closure", state: "HOLD", detail: `Source year ${featureYear} does not close against active year ${activeYear} under ${temporal?.mode ?? "untimed"} semantics.` }
      : { id: "time", label: "Temporal closure", state: "PASS", detail: temporal ? `Source year ${featureYear} closes against active year ${activeYear} under ${temporal.mode} semantics.` : "This layer is untimed; the Explorer year does not filter its support." }),
    Object.freeze(evidenceGate),
    Object.freeze(rightsGate),
    Object.freeze(releaseState === "RELEASED"
      ? { id: "release", label: "Release posture", state: "PASS", detail: "The fixture declares RELEASED posture; source authority still remains explicit." }
      : { id: "release", label: "Release posture", state: "NOTICE", detail: `${releaseState} is a visible site posture, not proof of production publication.` }),
    Object.freeze(correctionState !== "NONE" || state === "CORRECTED" || state === "SUPERSEDED"
      ? { id: "correction", label: "Correction posture", state: "NOTICE", detail: `Correction state ${correctionState} remains visible and cannot be silently collapsed.` }
      : { id: "correction", label: "Correction posture", state: "PASS", detail: "No correction marker is attached to this fixture." }),
  ]);
};

export const focusIntentNarrative = ({
  intent,
  result,
  state,
  timeMismatch,
  activeYear,
  featureYear,
  citation,
}: {
  intent: FocusIntentId;
  result: FocusResult;
  state: EvidenceState;
  timeMismatch: boolean;
  activeYear: number;
  featureYear: number;
  citation: string;
}) => {
  if (intent === "why") return `${state}${timeMismatch ? " plus a temporal mismatch" : ""} resolves to ${result.outcome} / ${result.code}. This diagnostic explanation cannot override the outcome.`;
  if (intent === "lineage") return `The bounded trace ends at ${citation}. Map pixels identify a candidate; the application registry and EvidenceRef carry the inspectable support posture.`;
  if (intent === "time") return timeMismatch
    ? `Active year ${activeYear} and selected source year ${featureYear} diverge. The selection remains inspectable, but its normal map halo is hidden and Focus Mode abstains unless a controlling DENY or ERROR takes precedence.`
    : `Active year ${activeYear} is compatible with selected source year ${featureYear} under the layer's declared temporal semantics.`;
  return result.body;
};

export const buildFocusActionProposals = ({
  state,
  timeMismatch,
  activeYear,
  featureYear,
  currentCenter,
  focusCenter,
}: {
  state: EvidenceState;
  timeMismatch: boolean;
  activeYear: number;
  featureYear: number;
  currentCenter: [number, number];
  focusCenter: [number, number];
}): readonly FocusActionProposal[] => {
  const proposals: FocusActionProposal[] = [];
  const controllingBoundary = state === "DENIED_BY_POLICY" || state === "RESTRICTED_ACCESS" || state === "ERROR";

  if (timeMismatch && !controllingBoundary) {
    proposals.push({
      id: `set-time-${featureYear}`,
      kind: "SET_TIME",
      title: `Use source year ${featureYear}`,
      summary: "Align the active timeline with the selected fixture's declared year.",
      before: `Active time ${activeYear}`,
      after: `Active time ${featureYear}`,
      impact: "View state only · manifest, release, policy, and evidence remain unchanged",
      targetYear: featureYear,
    });
  }

  proposals.push({
    id: "center-selection",
    kind: "CENTER_SELECTION",
    title: "Center the selected context",
    summary: "Reframe the public-safe map camera around the selected fixture.",
    before: `Camera ${currentCenter[1].toFixed(2)}, ${currentCenter[0].toFixed(2)}`,
    after: `Camera ${focusCenter[1].toFixed(2)}, ${focusCenter[0].toFixed(2)}`,
    impact: "Camera only · no evidence, policy, review, release, or publication effect",
  });

  if (state === "DENIED_BY_POLICY" || state === "RESTRICTED_ACCESS" || state === "GENERALIZED_GEOMETRY") {
    proposals.push({
      id: "inspect-boundary",
      kind: "OPEN_METADATA",
      title: "Inspect the public boundary",
      summary: "Review rights, generalization, and registry metadata without attempting a bypass.",
      before: "Focus action review",
      after: "Metadata tab",
      impact: "Review navigation only · protected detail stays withheld",
    });
  } else if (state === "MISSING_EVIDENCE" || state === "SOURCE_STALE" || state === "SUPERSEDED" || state === "CORRECTED" || state === "ERROR") {
    proposals.push({
      id: "inspect-lineage",
      kind: "OPEN_LINEAGE",
      title: "Inspect evidence lineage",
      summary: "Trace the selected fixture, EvidenceRef, and visible correction or failure posture.",
      before: "Focus action review",
      after: "Lineage tab",
      impact: "Review navigation only · no support is invented or admitted",
    });
  } else {
    proposals.push({
      id: "inspect-evidence",
      kind: "OPEN_EVIDENCE",
      title: "Inspect bounded evidence",
      summary: "Open the evidence facts and limitations behind this finite result.",
      before: "Focus action review",
      after: "Evidence tab",
      impact: "Review navigation only · finite outcome remains immutable",
    });
  }

  if (state === "MISSING_EVIDENCE" || state === "SOURCE_STALE" || state === "SUPERSEDED") {
    proposals.push({
      id: "open-source-observatory",
      kind: "OPEN_SOURCES",
      title: "Open source observatory",
      summary: "Review discovery candidates and gaps without treating discovery as admission.",
      before: "Focus action review",
      after: "Repository briefing · Sources",
      impact: "Discovery only · no source admission, activation, release, or publication",
    });
  }

  return Object.freeze(proposals.map((proposal) => Object.freeze(proposal)));
};
