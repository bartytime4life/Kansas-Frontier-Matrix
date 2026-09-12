import { readFileSync } from "node:fs";

import { describe, expect, it } from "vitest";

import {
  PHASE_4_LIVING_WATERS_PRODUCT_SELECTION,
  PHASE_4_LIVING_WATERS_PRODUCT_SELECTION_ID,
  type Phase4LivingWatersProductSelection,
  projectPhase4LivingWatersProductSelection,
} from "../src/features/living_atlas";

describe("Phase 4 Living Waters product selection", () => {
  it("projects the human-selected nomination without retrieving an observation", () => {
    const frame = projectPhase4LivingWatersProductSelection(
      PHASE_4_LIVING_WATERS_PRODUCT_SELECTION,
    );

    expect(frame).toMatchObject({
      selectionId: PHASE_4_LIVING_WATERS_PRODUCT_SELECTION_ID,
      selectionState: "HUMAN_SELECTED_REVIEW_PENDING",
      product: {
        publisher: "USGS",
        product: "continuous-values",
        parameterCode: "00060",
        parameterName: "discharge",
        statisticName: "instantaneous",
        unitCode: "ft3/s",
      },
      gauge: {
        agency: "USGS",
        siteNumber: "07146500",
        displayName: "Arkansas River at Arkansas City, KS",
        state: "KS",
      },
      observation: { state: "NOT_RETRIEVED", value: null, observedAt: null },
      trust: {
        evidenceState: "REFERENCED_NOT_RESOLVED",
        sourceAdmitted: false,
        sourceActivated: false,
        sourcePayloadRetrieved: false,
        policyEvaluated: false,
        released: false,
        deployed: false,
        published: false,
        floodWarningAuthority: false,
      },
      render: {
        representation: "REVIEW_RECORD_ONLY",
        visible: false,
        rendererBound: false,
      },
    });
    expect(frame.sourceReferences).toEqual([
      "https://api.waterdata.usgs.gov/ogcapi/v0/collections/continuous",
      "https://waterdata.usgs.gov/monitoring-location/USGS-07146500/",
    ]);
    expect(Object.isFrozen(frame)).toBe(true);
    expect(Object.isFrozen(frame.sourceReferences)).toBe(true);
  });

  it("rejects a selection that crosses the no-activation boundary", () => {
    const unsafeSelection: Phase4LivingWatersProductSelection = {
      ...PHASE_4_LIVING_WATERS_PRODUCT_SELECTION,
      governance: {
        ...PHASE_4_LIVING_WATERS_PRODUCT_SELECTION.governance,
        sourceActivated: true,
      },
    };

    expect(() => projectPhase4LivingWatersProductSelection(unsafeSelection)).toThrow(
      "LIVING_WATERS_PRODUCT_SELECTION_GOVERNANCE_BOUNDARY_VIOLATION",
    );
  });

  it("rejects a different gauge or product semantics instead of silently retargeting", () => {
    const retargetedSelection: Phase4LivingWatersProductSelection = {
      ...PHASE_4_LIVING_WATERS_PRODUCT_SELECTION,
      gauge: {
        ...PHASE_4_LIVING_WATERS_PRODUCT_SELECTION.gauge,
        siteNumber: "06877600",
      },
    };

    expect(() => projectPhase4LivingWatersProductSelection(retargetedSelection)).toThrow(
      "LIVING_WATERS_PRODUCT_SELECTION_SEMANTICS_MISMATCH",
    );
  });

  it("contains no direct browser-network primitive", () => {
    const source = readFileSync(
      new URL(
        "../src/features/living_atlas/living-waters-product-selection.ts",
        import.meta.url,
      ),
      "utf8",
    );

    expect(source).not.toMatch(/\bfetch\s*\(|\bXMLHttpRequest\b|\bWebSocket\b/);
  });
});
