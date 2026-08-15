export type StoryOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";
export type StoryState =
  | "READY"
  | "PARTIAL"
  | "ABSTAINED"
  | "SUPERSEDED"
  | "BLOCKED"
  | "ERROR";

type TrustState = {
  rights: "CLEARED" | "GENERALIZED" | "WITHHELD" | "UNRESOLVED";
  sensitivity: "PUBLIC" | "GENERALIZED" | "RESTRICTED" | "UNKNOWN";
  policy: "ALLOW" | "ABSTAIN" | "DENY" | "ERROR";
  review: "REVIEWED" | "NOT_APPLICABLE" | "PENDING";
  release: "RELEASED" | "UNRELEASED" | "WITHDRAWN";
  freshness: "CURRENT" | "STALE" | "UNKNOWN";
  correction: "NONE" | "CURRENT" | "CORRECTED" | "SUPERSEDED";
};

type StoryConstituent = {
  node_ref: string;
  order_index: number;
  state: StoryState;
  outcome: StoryOutcome;
  reason_code: string;
  trust_state: TrustState;
};

type StorySupport = {
  evidence_bundle_refs: string[];
  citation_validation_refs: string[];
  policy_decision_refs: string[];
  release_refs: string[];
  review_refs: string[];
  correction_refs: string[];
  rollback_ref?: string;
};

type StoryManifest = {
  profile: "kfm.ui.story-manifest.public-safe.v1";
  id: string;
  version: "1.0.0";
  spec_hash: string;
  story_ref: string;
  title: string;
  accessibility_summary: string;
  state: StoryState;
  outcome: StoryOutcome;
  reason_codes: string[];
  limiting_node_refs: string[];
  constituents: StoryConstituent[];
  trust_state: TrustState;
  support: StorySupport;
  caveats: string[];
  supersession?: {
    replacement_manifest_ref: string;
    public_note: string;
  };
  authoritative: false;
  projection_only: true;
};

export type StoryPlaybackNode = {
  nodeRef: string;
  orderIndex: number;
};

export type StoryPlayerProjection = {
  outcome: StoryOutcome;
  code:
    | "STORY_READY"
    | "STORY_ABSTAINED"
    | "STORY_DENIED"
    | "STORY_ERROR"
    | "NO_GOVERNED_RESPONSE"
    | "INVALID_PAYLOAD";
  title: string | null;
  accessibilitySummary: string;
  storyRef: string | null;
  state: StoryState | null;
  nodes: StoryPlaybackNode[];
  reasonCodes: string[];
  limitingNodeRefs: string[];
  evidenceBundleRefs: string[];
  citationValidationRefs: string[];
  caveats: string[];
  replacementManifestRef: string | null;
  canPlay: boolean;
  mode: "2D";
  authoritative: false;
};

const STATES = new Set<StoryState>([
  "READY",
  "PARTIAL",
  "ABSTAINED",
  "SUPERSEDED",
  "BLOCKED",
  "ERROR",
]);
const OUTCOMES = new Set<StoryOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const RIGHTS = new Set(["CLEARED", "GENERALIZED", "WITHHELD", "UNRESOLVED"]);
const SENSITIVITY = new Set(["PUBLIC", "GENERALIZED", "RESTRICTED", "UNKNOWN"]);
const POLICY = new Set(["ALLOW", "ABSTAIN", "DENY", "ERROR"]);
const REVIEW = new Set(["REVIEWED", "NOT_APPLICABLE", "PENDING"]);
const RELEASE = new Set(["RELEASED", "UNRELEASED", "WITHDRAWN"]);
const FRESHNESS = new Set(["CURRENT", "STALE", "UNKNOWN"]);
const CORRECTION = new Set(["NONE", "CURRENT", "CORRECTED", "SUPERSEDED"]);

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function isStringArray(value: unknown): value is string[] {
  return (
    Array.isArray(value) &&
    value.every((item) => typeof item === "string") &&
    new Set(value).size === value.length
  );
}

function isTrustState(value: unknown): value is TrustState {
  if (!isRecord(value)) return false;
  return (
    RIGHTS.has(String(value.rights)) &&
    SENSITIVITY.has(String(value.sensitivity)) &&
    POLICY.has(String(value.policy)) &&
    REVIEW.has(String(value.review)) &&
    RELEASE.has(String(value.release)) &&
    FRESHNESS.has(String(value.freshness)) &&
    CORRECTION.has(String(value.correction))
  );
}

function isSupport(value: unknown): value is StorySupport {
  if (!isRecord(value)) return false;
  return [
    value.evidence_bundle_refs,
    value.citation_validation_refs,
    value.policy_decision_refs,
    value.release_refs,
    value.review_refs,
    value.correction_refs,
  ].every(isStringArray);
}

function isConstituent(value: unknown): value is StoryConstituent {
  if (!isRecord(value)) return false;
  return (
    typeof value.node_ref === "string" &&
    Number.isInteger(value.order_index) &&
    Number(value.order_index) >= 0 &&
    STATES.has(value.state as StoryState) &&
    OUTCOMES.has(value.outcome as StoryOutcome) &&
    typeof value.reason_code === "string" &&
    isTrustState(value.trust_state)
  );
}

function isStoryManifest(value: unknown): value is StoryManifest {
  if (!isRecord(value)) return false;
  if (
    value.profile !== "kfm.ui.story-manifest.public-safe.v1" ||
    value.version !== "1.0.0" ||
    value.authoritative !== false ||
    value.projection_only !== true ||
    typeof value.id !== "string" ||
    typeof value.spec_hash !== "string" ||
    typeof value.story_ref !== "string" ||
    typeof value.title !== "string" ||
    typeof value.accessibility_summary !== "string" ||
    !STATES.has(value.state as StoryState) ||
    !OUTCOMES.has(value.outcome as StoryOutcome) ||
    !isStringArray(value.reason_codes) ||
    !isStringArray(value.limiting_node_refs) ||
    !isStringArray(value.caveats) ||
    !isTrustState(value.trust_state) ||
    !isSupport(value.support) ||
    !Array.isArray(value.constituents) ||
    value.constituents.length === 0 ||
    !value.constituents.every(isConstituent)
  ) {
    return false;
  }

  const constituents = value.constituents as StoryConstituent[];
  const nodeRefs = constituents.map((item) => item.node_ref);
  const orderIndexes = constituents.map((item) => item.order_index);
  if (
    new Set(nodeRefs).size !== nodeRefs.length ||
    new Set(orderIndexes).size !== orderIndexes.length
  ) {
    return false;
  }

  for (let index = 1; index < orderIndexes.length; index += 1) {
    if (orderIndexes[index - 1] >= orderIndexes[index]) return false;
  }

  if (value.supersession !== undefined) {
    if (
      !isRecord(value.supersession) ||
      typeof value.supersession.replacement_manifest_ref !== "string" ||
      typeof value.supersession.public_note !== "string"
    ) {
      return false;
    }
  }

  return true;
}

function readyTrustIsPublicSafe(manifest: StoryManifest): boolean {
  const trust = manifest.trust_state;
  const support = manifest.support;
  return (
    manifest.state === "READY" &&
    manifest.outcome === "ANSWER" &&
    trust.rights === "CLEARED" &&
    trust.sensitivity === "PUBLIC" &&
    trust.policy === "ALLOW" &&
    trust.review === "REVIEWED" &&
    trust.release === "RELEASED" &&
    trust.freshness === "CURRENT" &&
    trust.correction !== "SUPERSEDED" &&
    support.evidence_bundle_refs.length > 0 &&
    support.citation_validation_refs.length > 0 &&
    support.policy_decision_refs.length > 0 &&
    support.release_refs.length > 0 &&
    support.review_refs.length > 0
  );
}

function emptyProjection(
  outcome: StoryOutcome,
  code: StoryPlayerProjection["code"],
): StoryPlayerProjection {
  return {
    outcome,
    code,
    title: null,
    accessibilitySummary: "Story playback is unavailable.",
    storyRef: null,
    state: null,
    nodes: [],
    reasonCodes: [],
    limitingNodeRefs: [],
    evidenceBundleRefs: [],
    citationValidationRefs: [],
    caveats: [],
    replacementManifestRef: null,
    canPlay: false,
    mode: "2D",
    authoritative: false,
  };
}

/**
 * Consume one already-governed public-safe StoryManifest projection.
 *
 * This function does not resolve refs, fetch data, execute policy, release,
 * publish, render a map, or grant authority. It defensively prevents playback
 * unless the manifest is READY/ANSWER and its declared trust/support posture is
 * fully public-safe under the existing StoryManifest contract.
 */
export function resolveStoryPlayer(
  candidate?: unknown,
): StoryPlayerProjection {
  if (candidate === undefined) {
    return emptyProjection("ABSTAIN", "NO_GOVERNED_RESPONSE");
  }
  if (!isStoryManifest(candidate)) {
    return emptyProjection("ERROR", "INVALID_PAYLOAD");
  }

  const base = {
    title: candidate.title,
    accessibilitySummary: candidate.accessibility_summary,
    storyRef: candidate.story_ref,
    state: candidate.state,
    reasonCodes: [...candidate.reason_codes],
    limitingNodeRefs: [...candidate.limiting_node_refs],
    evidenceBundleRefs: [...candidate.support.evidence_bundle_refs],
    citationValidationRefs: [...candidate.support.citation_validation_refs],
    caveats: [...candidate.caveats],
    replacementManifestRef:
      candidate.supersession?.replacement_manifest_ref ?? null,
    mode: "2D" as const,
    authoritative: false as const,
  };

  if (readyTrustIsPublicSafe(candidate)) {
    return {
      ...base,
      outcome: "ANSWER",
      code: "STORY_READY",
      nodes: candidate.constituents.map((item) => ({
        nodeRef: item.node_ref,
        orderIndex: item.order_index,
      })),
      canPlay: true,
    };
  }

  if (candidate.outcome === "DENY" || candidate.state === "BLOCKED") {
    return {
      ...base,
      outcome: "DENY",
      code: "STORY_DENIED",
      nodes: [],
      canPlay: false,
    };
  }

  if (candidate.outcome === "ERROR" || candidate.state === "ERROR") {
    return {
      ...base,
      outcome: "ERROR",
      code: "STORY_ERROR",
      nodes: [],
      canPlay: false,
    };
  }

  return {
    ...base,
    outcome: "ABSTAIN",
    code: "STORY_ABSTAINED",
    nodes: [],
    canPlay: false,
  };
}
