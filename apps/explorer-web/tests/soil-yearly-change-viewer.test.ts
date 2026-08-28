import { describe, expect, it } from "vitest";

import invalidExtra from "../../../fixtures/ui/soil_yearly_change_projection/invalid/extra-field.json";
import invalidDiff from "../../../fixtures/ui/soil_yearly_change_projection/invalid/incoherent-diff.json";
import availableFixture from "../../../fixtures/ui/soil_yearly_change_projection/valid/available.json";
import deniedFixture from "../../../fixtures/ui/soil_yearly_change_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/soil_yearly_change_projection/valid/error.json";
import missingFixture from "../../../fixtures/ui/soil_yearly_change_projection/valid/missing.json";
import adapterSource from "../src/adapters/SoilYearlyChangeProjection.ts?raw";
import viewerSource from "../src/features/soil_yearly_change_viewer/index.ts?raw";
import { resolveSoilYearlyChangeViewer } from "../src/features/soil_yearly_change_viewer";

describe("Explorer SSURGO yearly change viewer", () => {
  it("shows bounded diff metrics and explicit year-pinned anchors", () => {
    const result = resolveSoilYearlyChangeViewer(availableFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      code: "DIFF_AVAILABLE",
      sourceDescriptorRef: "data/registry/sources/soil/nrcs-ssurgo.yaml",
      previousSnapshot: { datasetYear: 2025 },
      currentSnapshot: { datasetYear: 2026 },
      diff: {
        addedRecords: 1,
        removedRecords: 1,
        modifiedRecords: 1,
        changedPropertyNames: ["representative_slope_pct", "texture_class"],
      },
    });
    expect(result.summary).toContain("do not establish soil change");
  });

  it.each([
    [missingFixture, "ABSTAIN", "DIFF_MISSING"],
    [deniedFixture, "DENY", "POLICY_DENIED"],
    [errorFixture, "ERROR", "UPSTREAM_ERROR"],
  ] as const)("renders %s without fixture anchors", (fixture, outcome, code) => {
    const result = resolveSoilYearlyChangeViewer(fixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome,
      code,
      previousSnapshot: null,
      currentSnapshot: null,
      diff: null,
      provenance: null,
      sourceDescriptorRef: null,
    });
    expect(JSON.stringify(result)).not.toContain("sha256:");
    expect(JSON.stringify(result)).not.toContain("kfm://");
  });

  it.each([invalidExtra, invalidDiff])(
    "fails closed on extra fields or incoherent yearly closure",
    (fixture) => {
      const result = resolveSoilYearlyChangeViewer(fixture);
      expect(result).toMatchObject({
        visibility: "HIDDEN",
        code: "INVALID_PAYLOAD",
        previousSnapshot: null,
        currentSnapshot: null,
        diff: null,
      });
      expect(JSON.stringify(result)).not.toContain("SSURGO_INTERNAL_CANARY_57f22a");
    },
  );

  it("renders nothing without a governed projection", () => {
    expect(resolveSoilYearlyChangeViewer()).toMatchObject({
      visibility: "HIDDEN",
      code: "NO_GOVERNED_RESPONSE",
    });
  });

  it("contains no transport, persistence, lifecycle mutation, or model access", () => {
    const source = `${adapterSource}\n${viewerSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
    expect(source).not.toMatch(
      /(?:activateSource|compareSnapshots|promoteArtifact|authorizeRelease|publishArtifact)\s*\(/,
    );
  });
});
