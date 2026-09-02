import { describe, expect, it, vi } from "vitest";

import {
  MAP_FEATURE_SELECTION_PROFILE,
  createNullMapRuntime,
} from "@kfm/maplibre";
import answerFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import denyFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/deny-sensitive.json";
import adapterSource from "../src/adapters/map-runtime-evidence-adapter.ts?raw";
import {
  mapRuntimeSelectionToEvidenceRequest,
  resolveMapRuntimeSelectionEvidence,
} from "../src/adapters/map-runtime-evidence-adapter";
import { resolveMapFeatureEvidence } from "../src/features/map_runtime";
import {
  SUPPORTED_SYNTHETIC_STREAMFLOW_EVIDENCE_REFS,
  SUPPORTED_SYNTHETIC_STREAMFLOW_HISTORY_EVIDENCE_REFS,
  SUPPORTED_SYNTHETIC_STREAMFLOW_PROJECTION,
} from "../src/site/mount-explorer-site";

const runtimeSelection = Object.freeze({
  profile: MAP_FEATURE_SELECTION_PROFILE,
  selectionId: "selection:flow-001",
  layerId: "layer:synthetic-streamflow",
  featureId: "feature:flow-001",
  evidenceRefs: SUPPORTED_SYNTHETIC_STREAMFLOW_EVIDENCE_REFS,
  historyEvidenceRefs:
    SUPPORTED_SYNTHETIC_STREAMFLOW_HISTORY_EVIDENCE_REFS,
});

describe("MapRuntimePort to Explorer evidence integration", () => {
  it("keeps audit history scoped without presenting it as current support", async () => {
    expect(SUPPORTED_SYNTHETIC_STREAMFLOW_EVIDENCE_REFS).toEqual([
      "kfm:evidence:synthetic:flow-001",
    ]);
    expect(SUPPORTED_SYNTHETIC_STREAMFLOW_HISTORY_EVIDENCE_REFS).toEqual([
      "kfm:evidence:synthetic:flow-000",
    ]);
    expect(SUPPORTED_SYNTHETIC_STREAMFLOW_PROJECTION.evidence_refs).toEqual([
      "kfm:evidence:synthetic:flow-001",
    ]);
    expect(runtimeSelection.evidenceRefs).toBe(
      SUPPORTED_SYNTHETIC_STREAMFLOW_EVIDENCE_REFS,
    );

    const result = await resolveMapFeatureEvidence(
      Object.freeze({
        profile: MAP_FEATURE_SELECTION_PROFILE,
        selection_id: runtimeSelection.selectionId,
        layer_id: runtimeSelection.layerId,
        feature_id: runtimeSelection.featureId,
        evidence_refs: SUPPORTED_SYNTHETIC_STREAMFLOW_EVIDENCE_REFS,
        history_evidence_refs:
          SUPPORTED_SYNTHETIC_STREAMFLOW_HISTORY_EVIDENCE_REFS,
      }),
      async () => SUPPORTED_SYNTHETIC_STREAMFLOW_PROJECTION,
    );

    expect(result).toMatchObject({
      code: "SUPPORTED",
      drawer: {
        outcome: "ANSWER",
        code: "SUPPORTED",
        evidenceRefs: ["kfm:evidence:synthetic:flow-001"],
      },
    });
  });

  it("converts the KFM-owned runtime selection into the strict Explorer bridge shape", () => {
    expect(mapRuntimeSelectionToEvidenceRequest(runtimeSelection)).toEqual({
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:flow-001",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:flow-001",
      evidence_refs: [
        "kfm:evidence:synthetic:flow-001",
      ],
      history_evidence_refs: ["kfm:evidence:synthetic:flow-000"],
    });
  });

  it("resolves a deterministic NullMapRuntime selection through the governed evidence bridge", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    runtime.emitSelection(runtimeSelection);
    const resolver = vi.fn(async () => answerFixture);

    const result = await resolveMapRuntimeSelectionEvidence(
      runtime.getSnapshot().selection,
      resolver,
    );

    expect(resolver).toHaveBeenCalledTimes(1);
    expect(resolver).toHaveBeenCalledWith(runtimeSelection);
    expect(result).toMatchObject({
      code: "SUPPORTED",
      selection: runtimeSelection,
      drawer: {
        outcome: "ANSWER",
        code: "SUPPORTED",
        evidenceRefs: ["kfm:evidence:synthetic:flow-001"],
      },
    });
    runtime.dispose();
  });

  it("fails closed before the resolver when a runtime selection is malformed", async () => {
    const resolver = vi.fn(async () => answerFixture);
    const result = await resolveMapRuntimeSelectionEvidence(
      {
        ...runtimeSelection,
        evidenceRefs: ["unsafe evidence ref"],
      },
      resolver,
    );

    expect(resolver).not.toHaveBeenCalled();
    expect(result).toMatchObject({
      code: "SELECTION_INVALID",
      selection: null,
      drawer: {
        outcome: "ERROR",
        code: "UPSTREAM_ERROR",
        evidenceRefs: [],
      },
    });
  });

  it("preserves governed sensitive-detail denial without reflecting restricted text", async () => {
    const result = await resolveMapRuntimeSelectionEvidence(
      runtimeSelection,
      async () => denyFixture,
    );

    expect(result).toMatchObject({
      code: "SENSITIVE_DETAIL_RESTRICTED",
      drawer: {
        outcome: "DENY",
        code: "SENSITIVE_DETAIL_RESTRICTED",
        evidenceRefs: [],
        citations: [],
      },
    });
    expect(JSON.stringify(result.drawer)).not.toContain(
      "SENSITIVE_DENIAL_CANARY_4d7ec2",
    );
  });

  it("keeps the integration adapter no-network and renderer-neutral", () => {
    expect(adapterSource).not.toMatch(/\bfetch\s*\(/);
    expect(adapterSource).not.toMatch(
      /(?:from\s+|import\s*\()\s*["'](?:maplibre-gl|@maplibre\/[^"']+)["']/i,
    );
    expect(adapterSource).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(adapterSource).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
  });
});
