import { describe, expect, it } from "vitest";

import invalidExtra from "../../../fixtures/ui/environmental_anomaly_scorecard_projection/invalid/extra-field.json";
import invalidSummary from "../../../fixtures/ui/environmental_anomaly_scorecard_projection/invalid/summary-mismatch.json";
import completeFixture from "../../../fixtures/ui/environmental_anomaly_scorecard_projection/valid/complete.json";
import deniedFixture from "../../../fixtures/ui/environmental_anomaly_scorecard_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/environmental_anomaly_scorecard_projection/valid/error.json";
import holdFixture from "../../../fixtures/ui/environmental_anomaly_scorecard_projection/valid/hold.json";
import missingFixture from "../../../fixtures/ui/environmental_anomaly_scorecard_projection/valid/missing.json";
import adapterSource from "../src/adapters/EnvironmentalAnomalyScorecardProjection.ts?raw";
import scorecardSource from "../src/features/environmental_anomaly_scorecard/index.ts?raw";
import { resolveEnvironmentalAnomalyScorecard } from "../src/features/environmental_anomaly_scorecard";

describe("Explorer environmental anomaly scorecard", () => {
  it("shows a coherent five-lane complete scorecard", () => {
    const result = resolveEnvironmentalAnomalyScorecard(completeFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      code: "SCORECARD_AVAILABLE",
      county: { stateCode: "KS" },
      assessedAt: "2026-08-10T18:00:00Z",
      summary: {
        laneCount: 5,
        currentCount: 5,
        candidateCount: 1,
        holdCount: 0,
        errorCount: 0,
        overallOutcome: "COMPLETE",
        separateInterpretationGateRequired: true,
      },
    });
    expect(result.lanes.map((lane) => lane.lane)).toEqual([
      "AIR",
      "BIODIVERSITY",
      "HYDROLOGY",
      "SOILS",
      "VEGETATION",
    ]);
    expect(result.lanes[4]).toMatchObject({
      candidateState: "PROPOSED",
      reasonCode: "ANOMALY_CANDIDATE_PROPOSED",
    });
    expect(result.message).toContain("separate interpretation gate");
  });

  it("makes freshness and upstream holds visible without authoring a finding", () => {
    const result = resolveEnvironmentalAnomalyScorecard(holdFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      summary: {
        currentCount: 2,
        candidateCount: 1,
        holdCount: 2,
        errorCount: 1,
        overallOutcome: "HOLD",
      },
    });
    expect(result.lanes[0]).toMatchObject({
      lane: "AIR",
      freshnessState: "STALE",
      candidateState: "HOLD",
      evidenceRef: null,
      candidateRef: null,
    });
    expect(result.lanes[3]).toMatchObject({
      lane: "SOILS",
      freshnessState: "UNKNOWN",
      candidateState: "ERROR",
      evidenceRef: null,
      candidateRef: null,
    });
  });

  it.each([
    [missingFixture, "ABSTAIN", "SCORECARD_MISSING"],
    [deniedFixture, "DENY", "POLICY_DENIED"],
    [errorFixture, "ERROR", "UPSTREAM_ERROR"],
  ] as const)("renders %s without county or evidence detail", (fixture, outcome, code) => {
    const result = resolveEnvironmentalAnomalyScorecard(fixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome,
      code,
      county: null,
      assessedAt: null,
      lanes: [],
      summary: null,
    });
    expect(JSON.stringify(result)).not.toContain("kfm://");
  });

  it.each([invalidExtra, invalidSummary])(
    "fails closed on extra fields or an incoherent rollup",
    (fixture) => {
      const result = resolveEnvironmentalAnomalyScorecard(fixture);
      expect(result).toMatchObject({
        visibility: "HIDDEN",
        code: "INVALID_PAYLOAD",
        county: null,
        lanes: [],
        summary: null,
      });
      expect(JSON.stringify(result)).not.toContain(
        "SCORECARD_INTERNAL_CANARY_4f9c21",
      );
    },
  );

  it("renders nothing without a governed projection", () => {
    expect(resolveEnvironmentalAnomalyScorecard()).toMatchObject({
      visibility: "HIDDEN",
      code: "NO_GOVERNED_RESPONSE",
    });
  });

  it("contains no transport, persistence, lifecycle mutation, or model access", () => {
    const source = `${adapterSource}\n${scorecardSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
    expect(source).not.toMatch(
      /(?:probeSource|authorFreshness|computeAnomaly|interpretConditions|promoteArtifact|authorizeRelease|publishArtifact)\s*\(/,
    );
  });
});
