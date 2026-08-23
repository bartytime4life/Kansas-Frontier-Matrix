import {
  freezeMapFeatureSelection,
  isMapFeatureSelection,
  type MapFeatureSelection,
  type MapRuntimePort,
} from "@kfm/maplibre";
import {
  resolveMapFeatureEvidence,
  type GovernedMapEvidenceResolver,
  type MapEvidenceResolution,
} from "./index";

export type MapRuntimeEvidenceConsumer = (
  resolution: MapEvidenceResolution,
) => void;

export type MapRuntimeEvidenceBinding = Readonly<{
  destroy: () => void;
}>;

/**
 * Translate one validated KFM-owned runtime selection into the strict external
 * selection profile already enforced by the Explorer map-evidence bridge.
 */
function externalSelection(
  selection: MapFeatureSelection,
): Readonly<Record<string, unknown>> {
  const frozen = freezeMapFeatureSelection(selection);
  return Object.freeze({
    profile: frozen.profile,
    selection_id: frozen.selectionId,
    layer_id: frozen.layerId,
    feature_id: frozen.featureId,
    evidence_refs: Object.freeze([...frozen.evidenceRefs]),
  });
}

/**
 * Resolve one MapRuntimePort selection without allowing the runtime to bypass
 * the app-owned parser, evidence-subset guard, or finite Evidence Drawer state.
 */
export async function resolveMapRuntimeSelectionEvidence(
  selectionInput: unknown,
  resolver: GovernedMapEvidenceResolver,
): Promise<MapEvidenceResolution> {
  if (!isMapFeatureSelection(selectionInput)) {
    return resolveMapFeatureEvidence(selectionInput, resolver);
  }

  return resolveMapFeatureEvidence(externalSelection(selectionInput), resolver);
}

/**
 * Bind renderer-neutral runtime selection events to the governed evidence
 * bridge. Newer selections supersede unresolved older requests; destroy is
 * idempotent and prevents pending or later results from reaching the consumer.
 *
 * This binding performs no network, renderer, source, evidence-store, policy,
 * lifecycle, model, release, deployment, or publication work. The injected
 * resolver owns transport and remains subject to the existing strict bridge.
 */
export function bindMapRuntimeEvidence(
  runtime: MapRuntimePort,
  resolver: GovernedMapEvidenceResolver,
  consume: MapRuntimeEvidenceConsumer,
): MapRuntimeEvidenceBinding {
  if (typeof consume !== "function") {
    throw new TypeError("Map runtime evidence consumer must be a function.");
  }

  let active = true;
  let requestVersion = 0;

  const unsubscribe = runtime.subscribeSelection((selection) => {
    const currentRequest = ++requestVersion;
    void resolveMapRuntimeSelectionEvidence(selection, resolver).then(
      (resolution) => {
        if (!active || currentRequest !== requestVersion) return;
        consume(resolution);
      },
    );
  });

  return Object.freeze({
    destroy(): void {
      if (!active) return;
      active = false;
      requestVersion += 1;
      unsubscribe();
    },
  });
}
