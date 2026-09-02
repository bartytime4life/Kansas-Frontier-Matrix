import { MAP_FEATURE_SELECTION_PROFILE } from "@kfm/maplibre";

/**
 * Renderer-neutral candidate produced by a crosshair hit test.
 *
 * Candidate identifiers scope a governed evidence request. They are not
 * evidence, source authority, policy, review, release, or publication state.
 */
export const CROSSHAIR_CANDIDATE_PROFILE =
  "kfm.explorer.crosshair-candidate.v1" as const;

export type CrosshairCandidate = Readonly<{
  profile: typeof CROSSHAIR_CANDIDATE_PROFILE;
  candidateId: string;
  layerId: string;
  featureId: string;
  evidenceRefs: readonly string[];
  historyEvidenceRefs?: readonly string[];
  visibility: "PUBLIC_VISIBLE";
  publicSafe: true;
}>;

export type CrosshairMapSelection = Readonly<{
  profile: typeof MAP_FEATURE_SELECTION_PROFILE;
  selection_id: string;
  layer_id: string;
  feature_id: string;
  evidence_refs: readonly string[];
  history_evidence_refs?: readonly string[];
}>;

export type CrosshairSelectionResolution = Readonly<{
  outcome: "ANSWER" | "ABSTAIN" | "ERROR";
  code:
    | "SUPPORTED"
    | "NO_CANDIDATE"
    | "DISAMBIGUATION_REQUIRED"
    | "INVALID_CANDIDATE";
  candidates: readonly CrosshairCandidate[];
  selection: CrosshairMapSelection | null;
}>;

export type CrosshairSelectionControl = Readonly<{
  state: CrosshairSelectionResolution;
  destroy: () => void;
}>;

const REQUIRED_FIELDS = new Set([
  "profile",
  "candidateId",
  "layerId",
  "featureId",
  "evidenceRefs",
  "visibility",
  "publicSafe",
]);
const ALLOWED_FIELDS = new Set([
  ...REQUIRED_FIELDS,
  "historyEvidenceRefs",
]);
const SAFE_ID = /^[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}$/;
const MAX_EVIDENCE_REFS = 16;
const MAX_CANDIDATES = 16;

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasRequiredAllowedFields(value: Record<string, unknown>): boolean {
  const keys = Object.keys(value);
  return (
    keys.every((key) => ALLOWED_FIELDS.has(key)) &&
    [...REQUIRED_FIELDS].every((key) => Object.hasOwn(value, key))
  );
}

function isSafeId(value: unknown): value is string {
  return typeof value === "string" && SAFE_ID.test(value);
}

function parseRefs(value: unknown): readonly string[] | null {
  if (!Array.isArray(value) || value.length > MAX_EVIDENCE_REFS) return null;
  if (!value.every(isSafeId)) return null;
  if (new Set(value).size !== value.length) return null;
  return Object.freeze([...value]);
}

/** Strictly parse one public-safe, visible renderer candidate. */
export function parseCrosshairCandidate(value: unknown): CrosshairCandidate | null {
  if (!isRecord(value) || !hasRequiredAllowedFields(value)) return null;
  if (value.profile !== CROSSHAIR_CANDIDATE_PROFILE) return null;
  if (!isSafeId(value.candidateId)) return null;
  if (!isSafeId(value.layerId)) return null;
  if (!isSafeId(value.featureId)) return null;
  if (value.visibility !== "PUBLIC_VISIBLE" || value.publicSafe !== true) {
    return null;
  }

  const evidenceRefs = parseRefs(value.evidenceRefs);
  if (evidenceRefs === null) return null;
  const historyEvidenceRefs =
    value.historyEvidenceRefs === undefined
      ? undefined
      : parseRefs(value.historyEvidenceRefs);
  if (historyEvidenceRefs === null) return null;
  const allRefs = [...evidenceRefs, ...(historyEvidenceRefs ?? [])];
  if (
    allRefs.length > MAX_EVIDENCE_REFS ||
    new Set(allRefs).size !== allRefs.length
  ) {
    return null;
  }

  return Object.freeze({
    profile: CROSSHAIR_CANDIDATE_PROFILE,
    candidateId: value.candidateId,
    layerId: value.layerId,
    featureId: value.featureId,
    evidenceRefs,
    ...(historyEvidenceRefs === undefined ? {} : { historyEvidenceRefs }),
    visibility: "PUBLIC_VISIBLE",
    publicSafe: true,
  });
}

function toMapSelection(candidate: CrosshairCandidate): CrosshairMapSelection {
  return Object.freeze({
    profile: MAP_FEATURE_SELECTION_PROFILE,
    selection_id: candidate.candidateId,
    layer_id: candidate.layerId,
    feature_id: candidate.featureId,
    evidence_refs: candidate.evidenceRefs,
    ...(candidate.historyEvidenceRefs === undefined
      ? {}
      : { history_evidence_refs: candidate.historyEvidenceRefs }),
  });
}

/**
 * Resolve zero, one, or multiple candidates without silently choosing among
 * overlapping features. A single candidate becomes the existing strict map
 * selection wire shape; multiple candidates require explicit disambiguation.
 */
export function resolveCrosshairSelection(
  input: unknown,
): CrosshairSelectionResolution {
  if (!Array.isArray(input) || input.length > MAX_CANDIDATES) {
    return Object.freeze({
      outcome: "ERROR",
      code: "INVALID_CANDIDATE",
      candidates: Object.freeze([]),
      selection: null,
    });
  }
  if (input.length === 0) {
    return Object.freeze({
      outcome: "ABSTAIN",
      code: "NO_CANDIDATE",
      candidates: Object.freeze([]),
      selection: null,
    });
  }

  const parsed = input.map(parseCrosshairCandidate);
  if (parsed.some((candidate) => candidate === null)) {
    return Object.freeze({
      outcome: "ERROR",
      code: "INVALID_CANDIDATE",
      candidates: Object.freeze([]),
      selection: null,
    });
  }
  const candidates = Object.freeze(parsed as CrosshairCandidate[]);
  if (
    new Set(candidates.map((candidate) => candidate.candidateId)).size !==
    candidates.length
  ) {
    return Object.freeze({
      outcome: "ERROR",
      code: "INVALID_CANDIDATE",
      candidates: Object.freeze([]),
      selection: null,
    });
  }
  if (candidates.length > 1) {
    return Object.freeze({
      outcome: "ABSTAIN",
      code: "DISAMBIGUATION_REQUIRED",
      candidates,
      selection: null,
    });
  }

  return Object.freeze({
    outcome: "ANSWER",
    code: "SUPPORTED",
    candidates,
    selection: toMapSelection(candidates[0]),
  });
}

/**
 * Mount a keyboard-operable crosshair-candidate handoff. The callback receives
 * only the existing strict map-selection shape and remains responsible for the
 * governed evidence request.
 */
export function mountCrosshairSelectionControl(
  host: HTMLElement,
  input: unknown,
  onSelect: (selection: CrosshairMapSelection) => void,
): CrosshairSelectionControl {
  const state = resolveCrosshairSelection(input);
  const document = host.ownerDocument;
  const region = document.createElement("section");
  const heading = document.createElement("h3");
  const status = document.createElement("p");
  const controls = document.createElement("div");
  const listeners = new Map<HTMLButtonElement, () => void>();

  region.dataset.component = "crosshair-selection-control";
  region.dataset.outcome = state.outcome;
  heading.textContent = "Crosshair inspection";
  status.setAttribute("role", "status");
  status.setAttribute("aria-live", "polite");
  status.textContent = `${state.outcome} / ${state.code}`;
  controls.setAttribute("aria-label", "Crosshair candidates");

  const addCandidateButton = (candidate: CrosshairCandidate): void => {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = `Inspect ${candidate.featureId}`;
    const listener = (): void => onSelect(toMapSelection(candidate));
    button.addEventListener("click", listener);
    listeners.set(button, listener);
    controls.append(button);
  };

  if (state.outcome === "ANSWER" && state.selection !== null) {
    addCandidateButton(state.candidates[0]);
  } else if (state.code === "DISAMBIGUATION_REQUIRED") {
    for (const candidate of state.candidates) addCandidateButton(candidate);
  }

  region.replaceChildren(heading, status, controls);
  host.replaceChildren(region);

  return Object.freeze({
    state,
    destroy: () => {
      for (const [button, listener] of listeners) {
        button.removeEventListener("click", listener);
      }
      host.replaceChildren();
    },
  });
}
