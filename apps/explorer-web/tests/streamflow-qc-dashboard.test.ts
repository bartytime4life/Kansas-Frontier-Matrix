import { describe, expect, it } from "vitest";

import invalidExtraFieldFixture from "../../../fixtures/ui/streamflow_qc_dashboard_projection/invalid/extra-raw-flow-field.json";
import invalidRegionalFixture from "../../../fixtures/ui/streamflow_qc_dashboard_projection/invalid/regional-with-integrity-concern.json";
import deniedFixture from "../../../fixtures/ui/streamflow_qc_dashboard_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/streamflow_qc_dashboard_projection/valid/error.json";
import heldFixture from "../../../fixtures/ui/streamflow_qc_dashboard_projection/valid/held.json";
import localReviewFixture from "../../../fixtures/ui/streamflow_qc_dashboard_projection/valid/local-review.json";
import noEscalationFixture from "../../../fixtures/ui/streamflow_qc_dashboard_projection/valid/no-escalation.json";
import regionalFixture from "../../../fixtures/ui/streamflow_qc_dashboard_projection/valid/regional-context.json";
import adapterSource from "../src/adapters/StreamflowQcDashboardProjection.ts?raw";
import featureSource from "../src/features/streamflow_qc_dashboard/index.ts?raw";
import { parseStreamflowQcDashboardProjection } from "../src/adapters/StreamflowQcDashboardProjection";
import { resolveStreamflowQcDashboard } from "../src/features/streamflow_qc_dashboard";

describe("Explorer streamflow QC dashboard", () => {
  it("shows regional low-flow context from a closed projection", () => {
    const result = resolveStreamflowQcDashboard(regionalFixture);

    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "AVAILABLE",
      code: "REGIONAL_CONTEXT_AVAILABLE",
      status: "REGIONAL_CONTEXT",
      canRecalculatePercentile: false,
      canInvalidateSensor: false,
      canDeclareHydrologicEvent: false,
      canMutateDetectorConfiguration: false,
      canEvaluatePolicy: false,
      canApproveReview: false,
      canRelease: false,
      canPublish: false,
      accessibilityLabel: "Streamflow QC dashboard: available",
    });
    expect(result.assessment).toMatchObject({
      assessmentId: "kfm:streamflow-qc-context:aaaaaaaaaaaaaaaaaaaaaaaa",
      gaugeRef: "kfm:gauge:synthetic-kansas-001",
      flowState: "LOW_PERCENTILE",
      adjacentGaugeCount: 3,
      corroboration: "CORROBORATES_LOW_FLOW",
      droughtContext: "SUPPORTS_LOW_FLOW",
      ingestState: "CLEAN",
      unitState: "COMPATIBLE",
      cadenceState: "ON_TIME",
      priority: "ROUTINE",
    });
    expect(result.assessment?.evidenceRefs).toHaveLength(3);
  });

  it("preserves local-review and no-escalation meanings", () => {
    expect(resolveStreamflowQcDashboard(localReviewFixture)).toMatchObject({
      outcome: "AVAILABLE",
      code: "LOCAL_REVIEW_AVAILABLE",
      status: "LOCAL_REVIEW",
      assessment: {
        flowState: "LOW_PERCENTILE",
        corroboration: "DOES_NOT_CORROBORATE",
        priority: "ELEVATED",
        sensorInvalidated: false,
      },
    });
    expect(resolveStreamflowQcDashboard(noEscalationFixture)).toMatchObject({
      outcome: "AVAILABLE",
      code: "NO_ESCALATION_AVAILABLE",
      status: "NO_ESCALATION",
      assessment: {
        flowState: "NOT_LOW",
        adjacentGaugeCount: 0,
        priority: "NONE",
      },
    });
  });

  it("preserves hold, deny, and upstream error without gauge detail", () => {
    expect(resolveStreamflowQcDashboard(heldFixture)).toMatchObject({
      outcome: "ABSTAIN",
      code: "CONTEXT_HELD",
      status: "HELD",
      assessment: null,
    });
    expect(resolveStreamflowQcDashboard(deniedFixture)).toMatchObject({
      outcome: "DENY",
      code: "RELEASE_DENIED",
      status: "DENIED",
      assessment: null,
    });
    expect(resolveStreamflowQcDashboard(errorFixture)).toMatchObject({
      outcome: "ERROR",
      code: "UPSTREAM_ERROR",
      status: "UPSTREAM_ERROR",
      assessment: null,
      ariaLive: "assertive",
    });
  });

  it("rejects an unknown raw-value field without reflecting its canary", () => {
    expect(
      parseStreamflowQcDashboardProjection(invalidExtraFieldFixture),
    ).toEqual({
      ok: false,
      code: "MALFORMED_STREAMFLOW_QC_DASHBOARD_PROJECTION",
    });
    const result = resolveStreamflowQcDashboard(invalidExtraFieldFixture);
    expect(result).toMatchObject({
      visibility: "HIDDEN",
      outcome: "ERROR",
      code: "INVALID_PAYLOAD",
      assessment: null,
    });
    expect(JSON.stringify(result)).not.toContain(
      "SENSITIVE_STREAMFLOW_CANARY_8c21",
    );
  });

  it("fails closed when regional context contradicts integrity state", () => {
    expect(
      parseStreamflowQcDashboardProjection(invalidRegionalFixture),
    ).toEqual({
      ok: false,
      code: "MALFORMED_STREAMFLOW_QC_DASHBOARD_PROJECTION",
    });
  });

  it("rejects identity drift, authority drift, unsafe refs, and noncanonical evidence", () => {
    const identityDrift = JSON.parse(JSON.stringify(regionalFixture));
    identityDrift.assessment_id =
      "kfm:streamflow-qc-context:bbbbbbbbbbbbbbbbbbbbbbbb";

    const authorityDrift = JSON.parse(JSON.stringify(regionalFixture));
    authorityDrift.sensor_invalidated = true;

    const unsafeReference = JSON.parse(JSON.stringify(regionalFixture));
    unsafeReference.gauge_ref = "kfm:gauge:data/raw/streamflow";

    const reversedEvidence = JSON.parse(JSON.stringify(regionalFixture));
    reversedEvidence.evidence_refs.reverse();

    for (const candidate of [
      identityDrift,
      authorityDrift,
      unsafeReference,
      reversedEvidence,
    ]) {
      expect(parseStreamflowQcDashboardProjection(candidate)).toEqual({
        ok: false,
        code: "MALFORMED_STREAMFLOW_QC_DASHBOARD_PROJECTION",
      });
    }
  });

  it("uses an explicit abstention when no governed projection exists", () => {
    expect(resolveStreamflowQcDashboard()).toMatchObject({
      visibility: "HIDDEN",
      outcome: "ABSTAIN",
      code: "NO_GOVERNED_RESPONSE",
      assessment: null,
      canInvalidateSensor: false,
      canRelease: false,
      canPublish: false,
    });
  });

  it("keeps the adapter and feature free of transport and mutation seams", () => {
    const source = adapterSource + "\n" + featureSource;
    expect(source).not.toMatch(/\bfetch\s*\(|XMLHttpRequest|WebSocket/);
    expect(source).not.toMatch(
      /\b(?:recalculatePercentile|invalidateSensor|declareHydrologicEvent|mutateDetectorConfiguration|approve|override|publish|release)\s*\(/i,
    );
  });
});
