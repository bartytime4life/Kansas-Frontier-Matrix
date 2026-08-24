import {
  freezeMapFeatureSelection,
  isMapFeatureSelection,
  isMapRuntimeTrustState,
  type MapFeatureSelection,
  type MapRuntimeReasonCode,
  type MapRuntimePort,
  type MapRuntimeTrustState,
} from "@kfm/maplibre";
import {
  EVIDENCE_DRAWER_PROJECTION_PROFILE,
  type EvidenceDrawerOutcome,
  type EvidenceDrawerReasonCode,
} from "../../adapters/GovernedClient";
import {
  resolveMapFeatureEvidence,
  type GovernedMapEvidenceResolver,
  type MapEvidenceResolution,
} from "./index";
import {
  evaluateLayerManifestSelectionAdmission,
  type AdmissionResult,
} from "./layer_manifest_admission";

export type MapRuntimeEvidenceResolution = Readonly<{
  layerAdmission: AdmissionResult | null;
  evidence: MapEvidenceResolution;
}>;

export type MapRuntimeEvidenceInvalidation = Readonly<{
  kind: "RUNTIME_INVALIDATED";
  selectionId: string;
  runtimeState: MapRuntimeTrustState | "DISPOSED";
  runtimeReason: MapRuntimeReasonCode | null;
}>;

export type MapRuntimeEvidenceUpdate =
  | Readonly<{
      kind: "EVIDENCE_RESOLVED";
      resolution: MapRuntimeEvidenceResolution;
    }>
  | MapRuntimeEvidenceInvalidation;

export type RuntimeLayerManifestProjection = (
  selection: MapFeatureSelection,
) => unknown;

export type MapRuntimeEvidenceConsumer = (
  update: MapRuntimeEvidenceUpdate,
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

function admissionDrawerInput(
  selection: MapFeatureSelection,
  admission: AdmissionResult,
): Readonly<Record<string, unknown>> {
  const policyDenial =
    admission.code === "LAYER_MANIFEST_POLICY_DENIED" ||
    admission.code === "LAYER_MANIFEST_SOURCE_CLASS_DENIED" ||
    admission.code === "LAYER_MANIFEST_AUTHORITY_OVERCLAIM";
  const outcome: Exclude<EvidenceDrawerOutcome, "ANSWER"> =
    admission.outcome === "HOLD"
      ? "ABSTAIN"
      : admission.outcome === "DENY" && policyDenial
        ? "DENY"
        : "ERROR";
  const reasonCode: EvidenceDrawerReasonCode =
    outcome === "ABSTAIN"
      ? "MISSING_EVIDENCE"
      : outcome === "DENY"
        ? "POLICY_DENIED"
        : "UPSTREAM_ERROR";

  return Object.freeze({
    profile: EVIDENCE_DRAWER_PROJECTION_PROFILE,
    id: `kfm:drawer:${selection.selectionId}`,
    outcome,
    reason_code: reasonCode,
    title: "Map layer is not admitted",
    summary: `The layer admission gate stopped this request (${admission.code}).`,
    evidence_refs: Object.freeze([]),
    citations: Object.freeze([]),
    limitations: Object.freeze([
      "The selected layer did not pass the closed runtime admission projection.",
      "No governed evidence resolver was called.",
      "No unsupported claim is shown.",
    ]),
    trust_state: Object.freeze({
      source_role: "context",
      policy:
        outcome === "ABSTAIN"
          ? "ABSTAIN"
          : outcome === "DENY"
            ? "DENY"
            : "ERROR",
      review: "NOT_APPLICABLE",
      release: "UNRELEASED",
      freshness: "UNKNOWN",
      correction: "NONE",
    }),
    history: Object.freeze({
      negative_outcomes: Object.freeze([]),
      corrections: Object.freeze([]),
    }),
  });
}

/**
 * Resolve one MapRuntimePort selection without allowing the runtime to bypass
 * the app-owned parser, evidence-subset guard, or finite Evidence Drawer state.
 */
export async function resolveMapRuntimeSelectionEvidence(
  selectionInput: unknown,
  layerManifestInput: unknown,
  resolver: GovernedMapEvidenceResolver,
): Promise<MapRuntimeEvidenceResolution> {
  if (!isMapFeatureSelection(selectionInput)) {
    return Object.freeze({
      layerAdmission: null,
      evidence: await resolveMapFeatureEvidence(selectionInput, resolver),
    });
  }

  const layerAdmission = evaluateLayerManifestSelectionAdmission(
    layerManifestInput,
    selectionInput.layerId,
  );
  const evidence =
    layerAdmission.outcome === "PASS"
      ? await resolveMapFeatureEvidence(
          externalSelection(selectionInput),
          resolver,
        )
      : await resolveMapFeatureEvidence(
          externalSelection(selectionInput),
          async () => admissionDrawerInput(selectionInput, layerAdmission),
        );

  return Object.freeze({ layerAdmission, evidence });
}

/**
 * Bind renderer-neutral runtime selection events to the governed evidence
 * bridge. Newer selections supersede unresolved older requests. A transition
 * away from READY invalidates unresolved evidence so stale, denied, withdrawn,
 * rolled-back, or failed runtime state cannot be followed by a late ANSWER. If
 * an active selection exists, that transition emits a non-claim-bearing
 * invalidation carrying only its selection ID and the exact KFM-owned runtime
 * state/reason. It never synthesizes an evidence, policy, release, correction,
 * or rollback decision. Destroy is idempotent and prevents pending or later
 * results from reaching the consumer.
 *
 * This binding performs no network, renderer, source, evidence-store, policy,
 * lifecycle, model, release, deployment, or publication work. The manifest
 * callback supplies an already available closed projection; it is not a loader
 * or registry. The injected resolver owns transport and remains subject to the
 * existing strict bridge.
 */
export function bindMapRuntimeEvidence(
  runtime: MapRuntimePort,
  layerManifestForSelection: RuntimeLayerManifestProjection,
  resolver: GovernedMapEvidenceResolver,
  consume: MapRuntimeEvidenceConsumer,
): MapRuntimeEvidenceBinding {
  if (typeof layerManifestForSelection !== "function") {
    throw new TypeError("Runtime layer manifest projection must be a function.");
  }
  if (typeof consume !== "function") {
    throw new TypeError("Map runtime evidence consumer must be a function.");
  }

  let active = true;
  let requestVersion = 0;
  let latestSelectionId: string | null = null;

  const unsubscribeSnapshot = runtime.subscribeSnapshot((snapshot) => {
    if (snapshot.state === "READY") return;

    requestVersion += 1;
    const invalidatesVisibleEvidence =
      isMapRuntimeTrustState(snapshot.state) || snapshot.state === "DISPOSED";
    if (!active || !invalidatesVisibleEvidence || latestSelectionId === null) {
      return;
    }

    const selectionId = latestSelectionId;
    latestSelectionId = null;
    consume(
      Object.freeze({
        kind: "RUNTIME_INVALIDATED",
        selectionId,
        runtimeState: snapshot.state,
        runtimeReason: snapshot.reason,
      }),
    );
  });

  const unsubscribeSelection = runtime.subscribeSelection((selection) => {
    const currentRequest = ++requestVersion;
    latestSelectionId = selection.selectionId;
    let layerManifestInput: unknown;
    try {
      layerManifestInput = layerManifestForSelection(selection);
    } catch {
      layerManifestInput = undefined;
    }
    void resolveMapRuntimeSelectionEvidence(
      selection,
      layerManifestInput,
      resolver,
    ).then(
      (resolution) => {
        if (!active || currentRequest !== requestVersion) return;
        consume(Object.freeze({ kind: "EVIDENCE_RESOLVED", resolution }));
      },
    );
  });

  return Object.freeze({
    destroy(): void {
      if (!active) return;
      active = false;
      requestVersion += 1;
      latestSelectionId = null;
      unsubscribeSelection();
      unsubscribeSnapshot();
    },
  });
}
