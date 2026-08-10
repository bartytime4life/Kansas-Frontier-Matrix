import { describe, expect, it } from "vitest";

import validFixture from "../../../fixtures/ui/denial_reason_projection/valid/all-source-codes.json";
import invalidExtraFieldFixture from "../../../fixtures/ui/denial_reason_projection/invalid/extra-field.json";
import invalidUnknownReasonFixture from "../../../fixtures/ui/denial_reason_projection/invalid/unknown-reason.json";
import adapterSource from "../src/adapters/DenialReasonProjection.ts?raw";
import featureSource from "../src/features/denial_reason_explorer/index.ts?raw";
import { parseDenialReasonProjection } from "../src/adapters/DenialReasonProjection";
import { resolveDenialReasonExplorer } from "../src/features/denial_reason_explorer";

describe("Explorer denial reason explorer", () => {
  it("maps source-named codes to stable public-safe copy and ordering", () => {
    const result = resolveDenialReasonExplorer(validFixture);

    expect(result).toMatchObject({
      outcome: "DENY",
      code: "DENIAL_REASONS_READY",
      title: "Release candidate blocked",
      evaluatedAt: "2026-08-10T15:00:00Z",
      canOverride: false,
      accessibilityLabel: "Denial reason explorer: release candidate blocked",
    });
    expect(result.reasons.map((reason) => reason.code)).toEqual([
      "MISSING_RECEIPT",
      "INVALID_ATTESTATION",
      "LOW_COUNT_CELL",
      "ZOOM_TOO_FINE",
    ]);
    expect(result.reasons).toEqual([
      expect.objectContaining({
        category: "PROVENANCE",
        title: "Required receipt missing",
      }),
      expect.objectContaining({
        category: "INTEGRITY",
        title: "Attestation invalid",
      }),
      expect.objectContaining({
        category: "DISCLOSURE",
        title: "Cell count below disclosure threshold",
      }),
      expect.objectContaining({
        category: "RESOLUTION",
        title: "Requested zoom is too fine",
      }),
    ]);
  });

  it("rejects free-form detail without reflecting its canary", () => {
    expect(parseDenialReasonProjection(invalidExtraFieldFixture)).toEqual({
      ok: false,
      code: "MALFORMED_DENIAL_REASON_PROJECTION",
    });
    const result = resolveDenialReasonExplorer(invalidExtraFieldFixture);
    expect(result).toMatchObject({
      outcome: "ERROR",
      code: "INVALID_PAYLOAD",
      reviewId: null,
      releaseCandidateRef: null,
      policyDecisionRef: null,
      reasons: [],
      canOverride: false,
    });
    expect(JSON.stringify(result)).not.toContain(
      "SENSITIVE_DENIAL_DETAIL_CANARY_f91c",
    );
  });

  it("fails closed on an unknown reason code", () => {
    expect(parseDenialReasonProjection(invalidUnknownReasonFixture)).toEqual({
      ok: false,
      code: "MALFORMED_DENIAL_REASON_PROJECTION",
    });
    expect(resolveDenialReasonExplorer(invalidUnknownReasonFixture)).toMatchObject({
      outcome: "ERROR",
      code: "INVALID_PAYLOAD",
      reasons: [],
    });
  });

  it("rejects duplicate reasons and mutable candidate references", () => {
    const duplicate = {
      ...validFixture,
      reason_codes: ["MISSING_RECEIPT", "MISSING_RECEIPT"],
    };
    const mutableReference = {
      ...validFixture,
      release_candidate_ref: "kfm://release-candidate/synthetic/latest",
    };

    for (const candidate of [duplicate, mutableReference]) {
      expect(parseDenialReasonProjection(candidate)).toEqual({
        ok: false,
        code: "MALFORMED_DENIAL_REASON_PROJECTION",
      });
    }
  });

  it("uses an explicit abstention when no governed projection exists", () => {
    expect(resolveDenialReasonExplorer()).toMatchObject({
      outcome: "ABSTAIN",
      code: "NO_GOVERNED_RESPONSE",
      reasons: [],
      canOverride: false,
    });
  });

  it("keeps the adapter and feature free of transport and mutation seams", () => {
    const source = `${adapterSource}\n${featureSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(|XMLHttpRequest|WebSocket/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(/\b(?:approve|override|publish|release)\s*\(/i);
  });
});
