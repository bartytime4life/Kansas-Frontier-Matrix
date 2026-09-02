import { describe, expect, it } from "vitest";

import invalidExtra from "../../../fixtures/ui/layer_lineage_projection/invalid/extra-field.json";
import invalidRollback from "../../../fixtures/ui/layer_lineage_projection/invalid/rollback-digest-mismatch.json";
import availableFixture from "../../../fixtures/ui/layer_lineage_projection/valid/available.json";
import deniedFixture from "../../../fixtures/ui/layer_lineage_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/layer_lineage_projection/valid/error.json";
import missingFixture from "../../../fixtures/ui/layer_lineage_projection/valid/missing.json";
import adapterSource from "../src/adapters/LayerLineageProjection.ts?raw";
import timelineSource from "../src/features/layer_lineage_timeline/index.ts?raw";
import { resolveLayerLineageTimeline } from "../src/features/layer_lineage_timeline";

describe("Explorer rollback and correction lineage timeline", () => {
  it("exposes a chronological correction and rollback chain", () => {
    const result = resolveLayerLineageTimeline(availableFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      code: "LINEAGE_AVAILABLE",
      currentState: "ROLLED_BACK",
      currentReleaseRef: "kfm://release/synthetic/release-003",
    });
    expect(result.entries.map((entry) => entry.eventType)).toEqual([
      "RELEASED",
      "CORRECTED",
      "ROLLED_BACK",
    ]);
    expect(result.entries[1].correctionReceiptRef).toBe(
      "kfm://receipt/correction/synthetic/correction-001",
    );
    expect(result.entries[2]).toMatchObject({
      artifactDigest:
        "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      rollbackTargetRef: "kfm://release/synthetic/release-001",
    });
    expect(result.summary).toContain("cannot correct, withdraw, roll back");
  });

  it.each([
    [missingFixture, "ABSTAIN", "LINEAGE_MISSING"],
    [deniedFixture, "DENY", "POLICY_DENIED"],
    [errorFixture, "ERROR", "UPSTREAM_ERROR"],
  ] as const)("renders fixed %s state without lineage detail", (fixture, outcome, code) => {
    const result = resolveLayerLineageTimeline(fixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome,
      code,
      currentState: null,
      layerRef: null,
      currentReleaseRef: null,
      entries: [],
    });
    expect(JSON.stringify(result)).not.toContain("sha256:");
    expect(JSON.stringify(result)).not.toContain("kfm://");
  });

  it.each([invalidExtra, invalidRollback])(
    "fails closed on extra fields or unresolved rollback digest closure",
    (fixture) => {
      const result = resolveLayerLineageTimeline(fixture);
      expect(result).toMatchObject({
        visibility: "HIDDEN",
        code: "INVALID_PAYLOAD",
        entries: [],
      });
      expect(JSON.stringify(result)).not.toContain("LINEAGE_INTERNAL_CANARY_0b71d8");
    },
  );

  it("renders nothing without a governed response", () => {
    expect(resolveLayerLineageTimeline()).toMatchObject({
      visibility: "HIDDEN",
      code: "NO_GOVERNED_RESPONSE",
    });
  });

  it("contains no transport, persistence, lifecycle mutation, or model access", () => {
    const source = `${adapterSource}\n${timelineSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
    expect(source).not.toMatch(
      /(?:executeRollback|applyCorrection|authorizeRelease|publishArtifact)\s*\(/,
    );
  });
});
