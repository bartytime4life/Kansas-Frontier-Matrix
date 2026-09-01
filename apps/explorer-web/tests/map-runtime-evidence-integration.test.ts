import { describe, expect, it, vi } from "vitest";

import {
  MAP_FEATURE_SELECTION_PROFILE,
  createNullMapRuntime,
} from "@kfm/maplibre";
import answerFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import denyFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/deny-sensitive.json";
import adapterSource from "../src/adapters/MapRuntimeEvidenceAdapter.ts?raw";
import {
  mapRuntimeSelectionToEvidenceRequest,
  resolveMapRuntimeSelectionEvidence,
} from "../src/adapters/MapRuntimeEvidenceAdapter";

const runtimeSelection = Object.freeze({
  profile: MAP_FEATURE_SELECTION_PROFILE,
  selectionId: "selection:flow-001",
  layerId: "layer:synthetic-streamflow",
  featureId: "feature:flow-001",
  evidenceRefs: Object.freeze(["kfm:evidence:synthetic:flow-001"]),
});

describe("MapRuntimePort to Explorer evidence integration", () => {
  it("converts the KFM-owned runtime selection into the strict Explorer bridge shape", () => {
    expect(mapRuntimeSelectionToEvidenceRequest(runtimeSelection)).toEqual({
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:flow-001",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:flow-001",
      evidence_refs: ["kfm:evidence:synthetic:flow-001"],
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
