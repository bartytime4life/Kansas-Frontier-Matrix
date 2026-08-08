import { describe, expect, it, vi } from "vitest";

import answerFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import denyFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/deny-sensitive.json";
import mapRuntimeSource from "../src/features/map_runtime/index.tsx?raw";
import {
  MAP_FEATURE_SELECTION_PROFILE,
  parseMapFeatureSelection,
  resolveMapFeatureEvidence,
} from "../src/features/map_runtime";

const matchingSelection = Object.freeze({
  profile: MAP_FEATURE_SELECTION_PROFILE,
  selection_id: "selection:flow-001",
  layer_id: "layer:synthetic-streamflow",
  feature_id: "feature:flow-001",
  evidence_refs: ["kfm:evidence:synthetic:flow-001"],
});

describe("Explorer map feature to Evidence Drawer bridge", () => {
  it("strictly parses a renderer-neutral selection without retaining caller mutation", () => {
    const input = {
      ...matchingSelection,
      evidence_refs: [...matchingSelection.evidence_refs],
    };
    const parsed = parseMapFeatureSelection(input);
    input.evidence_refs[0] = "kfm:evidence:mutated";

    expect(parsed).toEqual({
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selectionId: "selection:flow-001",
      layerId: "layer:synthetic-streamflow",
      featureId: "feature:flow-001",
      evidenceRefs: ["kfm:evidence:synthetic:flow-001"],
    });
  });

  it("rejects unknown fields, duplicate refs, and unsafe identifiers", () => {
    expect(
      parseMapFeatureSelection({ ...matchingSelection, raw_feature: "not allowed" }),
    ).toBeNull();
    expect(
      parseMapFeatureSelection({
        ...matchingSelection,
        evidence_refs: [
          "kfm:evidence:synthetic:flow-001",
          "kfm:evidence:synthetic:flow-001",
        ],
      }),
    ).toBeNull();
    expect(
      parseMapFeatureSelection({ ...matchingSelection, feature_id: "bad feature id" }),
    ).toBeNull();
  });

  it("resolves a supported click only when returned evidence stays inside selection scope", async () => {
    const resolver = vi.fn(async () => answerFixture);
    const result = await resolveMapFeatureEvidence(matchingSelection, resolver);

    expect(resolver).toHaveBeenCalledTimes(1);
    expect(result).toMatchObject({
      code: "SUPPORTED",
      drawer: {
        outcome: "ANSWER",
        code: "SUPPORTED",
        evidenceRefs: ["kfm:evidence:synthetic:flow-001"],
      },
    });
  });

  it("abstains without calling the resolver when the selected feature has no governed evidence ref", async () => {
    const resolver = vi.fn(async () => answerFixture);
    const result = await resolveMapFeatureEvidence(
      { ...matchingSelection, evidence_refs: [] },
      resolver,
    );

    expect(resolver).not.toHaveBeenCalled();
    expect(result).toMatchObject({
      code: "MISSING_EVIDENCE",
      drawer: {
        outcome: "ABSTAIN",
        code: "MISSING_EVIDENCE",
        evidenceRefs: [],
      },
    });
  });

  it("preserves a governed policy denial without reflecting sensitive canary text", async () => {
    const result = await resolveMapFeatureEvidence(
      matchingSelection,
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

  it("fails closed when the drawer returns evidence outside the clicked selection", async () => {
    const result = await resolveMapFeatureEvidence(
      { ...matchingSelection, evidence_refs: ["kfm:evidence:synthetic:other"] },
      async () => answerFixture,
    );

    expect(result).toMatchObject({
      code: "DRAWER_EVIDENCE_OUTSIDE_SELECTION",
      drawer: {
        outcome: "ERROR",
        code: "UPSTREAM_ERROR",
        evidenceRefs: [],
        citations: [],
      },
    });
  });

  it("uses fixed no-leak error copy when the governed resolver fails", async () => {
    const result = await resolveMapFeatureEvidence(
      matchingSelection,
      async () => {
        throw new Error("PRIVATE_RESOLVER_DIAGNOSTIC_16b49c");
      },
    );

    expect(result).toMatchObject({
      code: "GOVERNED_RESOLVER_ERROR",
      drawer: {
        outcome: "ERROR",
        code: "UPSTREAM_ERROR",
      },
    });
    expect(JSON.stringify(result)).not.toContain(
      "PRIVATE_RESOLVER_DIAGNOSTIC_16b49c",
    );
  });

  it("keeps the feature bridge renderer-neutral, no-network, and outside lifecycle stores", () => {
    expect(mapRuntimeSource).not.toMatch(/\bfetch\s*\(/);
    expect(mapRuntimeSource).not.toMatch(/\bmaplibre(?:-gl)?\b/i);
    expect(mapRuntimeSource).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(mapRuntimeSource).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
  });
});
