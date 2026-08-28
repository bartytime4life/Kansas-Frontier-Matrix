import type { EvidenceState } from "./explorer-data";

export type RuntimeSeamState =
  | "IDLE"
  | "INITIALIZING"
  | "READY"
  | "STALE"
  | "ABSTAINED"
  | "DENIED"
  | "CONFLICT"
  | "DEGRADED"
  | "WITHDRAWN"
  | "ROLLED_BACK"
  | "ERROR"
  | "DISPOSED";

export type RuntimeSeamStep = Readonly<{
  state: RuntimeSeamState;
  reason: string;
  effect: string;
}>;

export const runtimeSeamStepForSelection = (state: EvidenceState | null): RuntimeSeamStep => {
  if (state === null) return Object.freeze({ state: "ABSTAINED", reason: "NO_SELECTION", effect: "No EvidenceRef resolution attempted" });
  if (state === "DENIED_BY_POLICY" || state === "RESTRICTED_ACCESS") return Object.freeze({ state: "DENIED", reason: "PUBLIC_PROJECTION_BLOCKED", effect: "Protected context remains unavailable" });
  if (state === "SOURCE_STALE") return Object.freeze({ state: "STALE", reason: "SELECTION_SUPPORT_STALE", effect: "Selection is inspectable; current claim support is withheld" });
  if (state === "ERROR") return Object.freeze({ state: "ERROR", reason: "EVIDENCE_BINDING_ERROR", effect: "No fallback selection or answer emitted" });
  if (state === "MISSING_EVIDENCE" || state === "GENERALIZED_GEOMETRY" || state === "SUPERSEDED") return Object.freeze({ state: "ABSTAINED", reason: "EVIDENCE_NOT_CLOSED", effect: "Candidate remains visible without a supported claim" });
  return Object.freeze({ state: "READY", reason: "SELECTION_BOUND", effect: "Stable selection and bounded EvidenceRef context available" });
};
