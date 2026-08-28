import { describe, expect, it } from "vitest";

import manifest from "../../../fixtures/domains/water_planning/planning_scenario_manifest/valid/valid_1.json";
import invalidExtra from "../../../fixtures/ui/planning_scenario_projection/invalid/extra-field.json";
import invalidReference from "../../../fixtures/ui/planning_scenario_projection/invalid/reference-mismatch.json";
import availableFixture from "../../../fixtures/ui/planning_scenario_projection/valid/available.json";
import deniedFixture from "../../../fixtures/ui/planning_scenario_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/planning_scenario_projection/valid/error.json";
import missingFixture from "../../../fixtures/ui/planning_scenario_projection/valid/missing.json";
import adapterSource from "../src/adapters/planning-scenario-projection.ts?raw";
import featureSource from "../src/features/planning_scenario_review/index.ts?raw";
import { resolvePlanningScenarioReview } from "../src/features/planning_scenario_review";

describe("Explorer planning scenario review", () => {
  it("shows a bounded held scenario with explicit uncertainty and non-authority labels", () => {
    const result = resolvePlanningScenarioReview(availableFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ABSTAIN",
      code: "SCENARIO_HELD",
      heading: "Synthetic Kansas drought-planning exploration",
      scenarioStatus: "HELD",
      geographyLabel: "Kansas (synthetic generalized fixture)",
      horizon: {
        baselineAsOf: "2026-01-01",
        horizonStart: "2030-01-01",
        horizonEnd: "2040-12-31",
      },
    });
    expect(result.inputVariables).toHaveLength(3);
    expect(result.assumptions).toHaveLength(3);
    expect(result.equityDimensions).toHaveLength(2);
    expect(result.nonAuthorityLabels).toEqual([
      "NOT_A_PREDICTION",
      "NOT_EMERGENCY_ALERTING",
      "NOT_REGULATORY_DETERMINATION",
    ]);
    expect(result.message).toContain("not a prediction");
    expect(result.message).toContain("recommendation");
  });

  it("keeps the UI projection aligned with the validated domain manifest", () => {
    const result = resolvePlanningScenarioReview(availableFixture);
    expect(availableFixture.outcome).toBe(manifest.public_summary.outcome);
    expect(result.heading).toBe(manifest.title);
    expect(result.purpose).toBe(manifest.purpose);
    expect(result.horizon).toEqual({
      baselineAsOf: manifest.time_horizon.baseline_as_of,
      horizonStart: manifest.time_horizon.horizon_start,
      horizonEnd: manifest.time_horizon.horizon_end,
    });
    expect(result.inputVariables).toEqual(
      manifest.input_variables.map((input) => ({
        variableId: input.variable_id,
        label: input.label,
        sourceRef: input.source_ref,
        uncertainty: input.uncertainty,
      })),
    );
    expect(result.assumptions).toEqual(
      manifest.assumptions.map((assumption) => ({
        assumptionId: assumption.assumption_id,
        statement: assumption.statement,
        evidenceRefs: assumption.evidence_refs,
        uncertainty: assumption.uncertainty,
      })),
    );
    expect(result.equityDimensions).toEqual(
      manifest.equity_dimensions.map((dimension) => ({
        dimensionId: dimension.dimension_id,
        description: dimension.description,
        evidenceRefs: dimension.evidence_refs,
        limitation: dimension.limitation,
      })),
    );
    expect(result.participationRefs).toEqual(manifest.participation_refs);
    expect(result.evidenceRefs).toEqual(manifest.evidence_refs);
    expect(result.limitations).toEqual(manifest.public_summary.limitations);
    expect(result.nonAuthorityLabels).toEqual(
      manifest.public_summary.non_authority_labels,
    );
  });

  it.each([
    [missingFixture, "ABSTAIN", "SCENARIO_MISSING"],
    [deniedFixture, "DENY", "POLICY_DENIED"],
    [errorFixture, "ERROR", "UPSTREAM_ERROR"],
  ] as const)("renders %s without scenario or reference detail", (fixture, outcome, code) => {
    const result = resolvePlanningScenarioReview(fixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome,
      code,
      scenarioStatus: null,
      purpose: null,
      geographyLabel: null,
      horizon: null,
      inputVariables: [],
      assumptions: [],
      equityDimensions: [],
      participationRefs: [],
      evidenceRefs: [],
      limitations: [],
      nonAuthorityLabels: [],
    });
    expect(JSON.stringify(result)).not.toContain("fixture:");
  });

  it.each([invalidExtra, invalidReference])(
    "fails closed on unexpected fields or undeclared evidence references",
    (fixture) => {
      const result = resolvePlanningScenarioReview(fixture);
      expect(result).toMatchObject({
        visibility: "HIDDEN",
        code: "INVALID_PAYLOAD",
        scenarioStatus: null,
        inputVariables: [],
        assumptions: [],
        equityDimensions: [],
        evidenceRefs: [],
      });
      expect(JSON.stringify(result)).not.toContain(
        "PLANNING_SCENARIO_INTERNAL_CANARY_6ad4b2",
      );
    },
  );

  it("renders nothing without a governed projection", () => {
    expect(resolvePlanningScenarioReview()).toMatchObject({
      visibility: "HIDDEN",
      code: "NO_GOVERNED_RESPONSE",
    });
  });

  it("contains no transport, persistence, scenario computation, policy, or release action", () => {
    const source = `${adapterSource}\n${featureSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
    expect(source).not.toMatch(
      /(?:computeScenario|aggregatePreferences|evaluatePolicy|recommendAction|authorizeRelease|publishArtifact)\s*\(/,
    );
  });
});
