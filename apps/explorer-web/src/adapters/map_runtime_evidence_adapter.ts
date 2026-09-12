import {
  isMapFeatureSelection,
  type MapFeatureSelection,
} from "@kfm/maplibre";

import {
  resolveMapFeatureEvidence,
  type GovernedMapEvidenceResolver,
  type MapEvidenceResolution,
} from "../features/map_runtime";

/**
 * Explorer-owned transport shape for the existing strict map-evidence bridge.
 *
 * MapRuntimePort deliberately exposes KFM-owned camelCase values while the
 * browser bridge accepts the snake_case wire-shaped fixture input it already
 * validates. This adapter is the single bounded conversion between those two
 * established interfaces. It performs no network, renderer, source, evidence,
 * policy, release, lifecycle, or publication work.
 */
export type MapRuntimeEvidenceRequest = Readonly<{
  profile: MapFeatureSelection["profile"];
  selection_id: string;
  layer_id: string;
  feature_id: string;
  evidence_refs: readonly string[];
  history_evidence_refs?: readonly string[];
}>;

/** Convert one validated MapRuntimePort selection into Explorer bridge input. */
export function mapRuntimeSelectionToEvidenceRequest(
  input: unknown,
): MapRuntimeEvidenceRequest | null {
  if (!isMapFeatureSelection(input)) return null;

  const historyEvidenceRefs = input.historyEvidenceRefs;
  return Object.freeze({
    profile: input.profile,
    selection_id: input.selectionId,
    layer_id: input.layerId,
    feature_id: input.featureId,
    evidence_refs: Object.freeze([...input.evidenceRefs]),
    ...(historyEvidenceRefs === undefined
      ? {}
      : {
          history_evidence_refs: Object.freeze([...historyEvidenceRefs]),
        }),
  });
}

/**
 * Resolve a MapRuntimePort selection through the existing governed evidence seam.
 *
 * Invalid or malformed runtime selections fail closed through the bridge's
 * SELECTION_INVALID result without invoking the governed resolver. Valid
 * selections retain the bridge's evidence-subset, denial, and no-leak checks.
 */
export async function resolveMapRuntimeSelectionEvidence(
  input: unknown,
  resolver: GovernedMapEvidenceResolver,
): Promise<MapEvidenceResolution> {
  const request = mapRuntimeSelectionToEvidenceRequest(input);
  return resolveMapFeatureEvidence(request, resolver);
}
