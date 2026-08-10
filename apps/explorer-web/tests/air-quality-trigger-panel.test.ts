import { describe, expect, it } from "vitest";

import deniedFixture from "../../../fixtures/ui/air_quality_trigger_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/air_quality_trigger_projection/valid/error.json";
import heldFixture from "../../../fixtures/ui/air_quality_trigger_projection/valid/held.json";
import noTriggerFixture from "../../../fixtures/ui/air_quality_trigger_projection/valid/no-trigger.json";
import triggerFixture from "../../../fixtures/ui/air_quality_trigger_projection/valid/proposed-trigger.json";
import invalidExtraFixture from "../../../fixtures/ui/air_quality_trigger_projection/invalid/extra-raw-field.json";
import invalidRelationFixture from "../../../fixtures/ui/air_quality_trigger_projection/invalid/relation-mismatch.json";
import adapterSource from "../src/adapters/AirQualityTriggerProjection.ts?raw";
import featureSource from "../src/features/air_quality_trigger_panel/index.ts?raw";
import { parseAirQualityTriggerProjection } from "../src/adapters/AirQualityTriggerProjection";
import { resolveAirQualityTriggerPanel } from "../src/features/air_quality_trigger_panel";

describe("Explorer air-quality trigger panel", () => {
  it("shows a proposed categorical candidate without creating air or health authority", () => {
    const result = resolveAirQualityTriggerPanel(triggerFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      code: "TRIGGER_CANDIDATE_AVAILABLE",
      heading: "PM2.5 trigger candidate",
      candidate: {
        candidateState: "PROPOSED_TRIGGER_CANDIDATE",
        knowledgeCharacter: "OBSERVED_SENSOR",
        thresholdRelation: "ABOVE_MONITORED_THRESHOLD",
        trailingMedianRelation: "ABOVE_TRAILING_MEDIAN",
        evidenceState: "REFERENCED_NOT_RESOLVED",
      },
    });
    expect(result.candidate?.evidenceRefs).toHaveLength(2);
    expect(result.message).toContain("not an air-quality event");
  });

  it("keeps a no-trigger result distinct from a proposed candidate", () => {
    const result = resolveAirQualityTriggerPanel(noTriggerFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      code: "NO_TRIGGER_CANDIDATE",
      heading: "No PM2.5 trigger candidate",
      candidate: {
        candidateState: "NO_TRIGGER_CANDIDATE",
        thresholdRelation: "AT_OR_BELOW_MONITORED_THRESHOLD",
      },
    });
  });

  it.each([
    [heldFixture, "ABSTAIN", "CONTEXT_HELD"],
    [deniedFixture, "DENY", "POLICY_DENIED"],
    [errorFixture, "ERROR", "UPSTREAM_ERROR"],
  ] as const)("renders a finite negative state without candidate detail", (fixture, outcome, code) => {
    const result = resolveAirQualityTriggerPanel(fixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome,
      code,
      candidate: null,
    });
    expect(JSON.stringify(result)).not.toContain("kfm://");
  });

  it.each([invalidExtraFixture, invalidRelationFixture])(
    "fails closed on raw detail or semantic mismatch",
    (fixture) => {
      const result = resolveAirQualityTriggerPanel(fixture);
      expect(result).toMatchObject({
        visibility: "HIDDEN",
        code: "INVALID_PAYLOAD",
        candidate: null,
      });
      expect(JSON.stringify(result)).not.toContain("PM25_INTERNAL_CANARY_19ea6c");
      expect(JSON.stringify(result)).not.toContain("35.1");
    },
  );

  it("rejects one evidence reference, mutable identity, and authority overreach", () => {
    const oneEvidence = {
      ...triggerFixture,
      candidate: {
        ...triggerFixture.candidate,
        evidence_refs: [triggerFixture.candidate.evidence_refs[0]],
      },
    };
    const mutableIdentity = {
      ...triggerFixture,
      candidate: {
        ...triggerFixture.candidate,
        assessment_ref: "kfm://assessment/pm25-trigger/latest",
      },
    };
    const authorityOverreach = { ...triggerFixture, health_advice_issued: true };
    for (const value of [oneEvidence, mutableIdentity, authorityOverreach]) {
      expect(parseAirQualityTriggerProjection(value)).toEqual({
        ok: false,
        code: "MALFORMED_AIR_QUALITY_TRIGGER_PROJECTION",
      });
    }
  });

  it("renders nothing without a governed projection", () => {
    expect(resolveAirQualityTriggerPanel()).toMatchObject({
      visibility: "HIDDEN",
      code: "NO_GOVERNED_RESPONSE",
    });
  });

  it("contains no transport, persistence, raw metric, lifecycle mutation, or model access", () => {
    const source = `${adapterSource}\n${featureSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(/(?:pm25_value|threshold_value|aqi_value|latitude|longitude)/i);
    expect(source).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
    expect(source).not.toMatch(
      /(?:declareAirQualityEvent|issueHealthAdvice|decideCompliance|mutateDetector|promoteArtifact|authorizeRelease|publishArtifact)\s*\(/,
    );
  });
});
