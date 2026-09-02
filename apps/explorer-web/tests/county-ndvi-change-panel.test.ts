import { describe, expect, it } from "vitest";

import candidateFixture from "../../../fixtures/ui/county_ndvi_change_projection/valid/candidate.json";
import deniedFixture from "../../../fixtures/ui/county_ndvi_change_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/county_ndvi_change_projection/valid/error.json";
import missingFixture from "../../../fixtures/ui/county_ndvi_change_projection/valid/missing.json";
import invalidDeltaFixture from "../../../fixtures/ui/county_ndvi_change_projection/invalid/delta-mismatch.json";
import invalidExtraFixture from "../../../fixtures/ui/county_ndvi_change_projection/invalid/extra-field.json";
import adapterSource from "../src/adapters/CountyNdviChangeProjection.ts?raw";
import featureSource from "../src/features/county_ndvi_change_panel/index.ts?raw";
import { parseCountyNdviChangeProjection } from "../src/adapters/CountyNdviChangeProjection";
import { resolveCountyNdviChangePanel } from "../src/features/county_ndvi_change_panel";

describe("Explorer county NDVI change panel", () => {
  it("shows coherent candidate metrics with the evidence gap visible", () => {
    const result = resolveCountyNdviChangePanel(candidateFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      code: "PANEL_AVAILABLE",
      county: { stateCode: "KS" },
      metrics: {
        deltaNdviMillionths: 150000,
        deltaThresholdMillionths: 120000,
        changedAreaBasisPoints: 1250,
        clusterCount: 3,
        classification: "GAIN_CANDIDATE",
      },
      evidence: { state: "REFERENCED_NOT_RESOLVED" },
    });
    expect(result.message).toContain("does not establish an environmental finding");
  });

  it.each([
    [missingFixture, "ABSTAIN", "PANEL_MISSING"],
    [deniedFixture, "DENY", "POLICY_DENIED"],
    [errorFixture, "ERROR", "UPSTREAM_ERROR"],
  ] as const)("renders a finite negative state without candidate detail", (fixture, outcome, code) => {
    const result = resolveCountyNdviChangePanel(fixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome,
      code,
      county: null,
      windows: null,
      metrics: null,
      evidence: null,
    });
    expect(JSON.stringify(result)).not.toContain("kfm://");
  });

  it.each([invalidExtraFixture, invalidDeltaFixture])(
    "fails closed on extra fields or incoherent arithmetic",
    (fixture) => {
      const result = resolveCountyNdviChangePanel(fixture);
      expect(result).toMatchObject({
        visibility: "HIDDEN",
        code: "INVALID_PAYLOAD",
        county: null,
        metrics: null,
        evidence: null,
      });
      expect(JSON.stringify(result)).not.toContain("NDVI_INTERNAL_CANARY_7c2d91");
    },
  );

  it("rejects mutable references, evidence overclaim, and authority overreach", () => {
    const mutableReference = {
      ...candidateFixture,
      evidence: {
        ...candidateFixture.evidence,
        ndvi_computation_ref: "kfm://ndvi-computation/synthetic/latest",
      },
    };
    const evidenceOverclaim = {
      ...candidateFixture,
      evidence: { ...candidateFixture.evidence, state: "RESOLVED" },
    };
    const authorityOverreach = {
      ...candidateFixture,
      public_use_allowed: true,
    };
    for (const value of [mutableReference, evidenceOverclaim, authorityOverreach]) {
      expect(parseCountyNdviChangeProjection(value)).toEqual({
        ok: false,
        code: "MALFORMED_COUNTY_NDVI_CHANGE_PROJECTION",
      });
    }
  });

  it("renders nothing without a governed projection", () => {
    expect(resolveCountyNdviChangePanel()).toMatchObject({
      visibility: "HIDDEN",
      code: "NO_GOVERNED_RESPONSE",
    });
  });

  it("contains no transport, persistence, lifecycle mutation, or model access", () => {
    const source = `${adapterSource}\n${featureSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
    expect(source).not.toMatch(
      /(?:fetchImagery|calculateNdvi|resolveEvidence|interpretConditions|promoteArtifact|authorizeRelease|publishArtifact)\s*\(/,
    );
  });
});
