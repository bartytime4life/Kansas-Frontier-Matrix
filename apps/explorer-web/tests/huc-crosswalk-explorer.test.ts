import { describe, expect, it } from "vitest";

import invalidExtraFieldFixture from "../../../fixtures/ui/huc_crosswalk_projection/invalid/extra-field.json";
import invalidStatusMismatchFixture from "../../../fixtures/ui/huc_crosswalk_projection/invalid/outcome-status-mismatch.json";
import ambiguousFixture from "../../../fixtures/ui/huc_crosswalk_projection/valid/ambiguous.json";
import verifiedFixture from "../../../fixtures/ui/huc_crosswalk_projection/valid/verified-exact.json";
import adapterSource from "../src/adapters/HucCrosswalkProjection.ts?raw";
import featureSource from "../src/features/huc_crosswalk_explorer/index.ts?raw";
import { parseHucCrosswalkProjection } from "../src/adapters/HucCrosswalkProjection";
import { resolveHucCrosswalkExplorer } from "../src/features/huc_crosswalk_explorer";

describe("Explorer HUC crosswalk explorer", () => {
  it("shows a verified digest-bound HUC and station reference projection", () => {
    const result = resolveHucCrosswalkExplorer(verifiedFixture);

    expect(result).toMatchObject({
      outcome: "AVAILABLE",
      code: "CROSSWALK_REFERENCE_READY",
      countyFips: "20177",
      huc12: "102600030101",
      status: "VERIFIED_EXACT",
      evaluatedAt: "2026-08-10T16:00:00Z",
      canFetch: false,
      canChangeCrosswalk: false,
      canRelease: false,
      accessibilityLabel: "HUC crosswalk explorer: available",
    });
    expect(result.stationRefs).toHaveLength(2);
    expect(result.crosswalkRef).toMatch(
      new RegExp(`@${result.crosswalkDigest}$`),
    );
    expect(result.validationReceiptRef).toContain("@sha256:");
  });

  it("preserves ambiguity as abstention without station references", () => {
    expect(resolveHucCrosswalkExplorer(ambiguousFixture)).toMatchObject({
      outcome: "ABSTAIN",
      code: "CROSSWALK_REFERENCE_HELD",
      status: "AMBIGUOUS",
      stationRefs: [],
      canChangeCrosswalk: false,
      canRelease: false,
    });
  });

  it("rejects source detail without reflecting its canary", () => {
    expect(parseHucCrosswalkProjection(invalidExtraFieldFixture)).toEqual({
      ok: false,
      code: "MALFORMED_HUC_CROSSWALK_PROJECTION",
    });
    const result = resolveHucCrosswalkExplorer(invalidExtraFieldFixture);
    expect(result).toMatchObject({
      outcome: "ERROR",
      code: "INVALID_PAYLOAD",
      countyFips: null,
      huc12: null,
      crosswalkRef: null,
      validationReceiptRef: null,
      stationRefs: [],
    });
    expect(JSON.stringify(result)).not.toContain(
      "SENSITIVE_HUC_SOURCE_CANARY_91be",
    );
  });

  it("fails closed when status, outcome, and reason drift apart", () => {
    expect(parseHucCrosswalkProjection(invalidStatusMismatchFixture)).toEqual({
      ok: false,
      code: "MALFORMED_HUC_CROSSWALK_PROJECTION",
    });
  });

  it("rejects mutable, mismatched, duplicate, and unsorted references", () => {
    const candidates = [
      {
        ...verifiedFixture,
        crosswalk_ref: "kfm://manifest/hydrology/huc12-comid/latest",
      },
      {
        ...verifiedFixture,
        crosswalk_digest:
          "sha256:ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
      },
      {
        ...verifiedFixture,
        station_refs: [
          verifiedFixture.station_refs[0],
          verifiedFixture.station_refs[0],
        ],
      },
      {
        ...verifiedFixture,
        station_refs: [...verifiedFixture.station_refs].reverse(),
      },
    ];

    for (const candidate of candidates) {
      expect(parseHucCrosswalkProjection(candidate)).toEqual({
        ok: false,
        code: "MALFORMED_HUC_CROSSWALK_PROJECTION",
      });
    }
  });

  it("uses an explicit abstention when no governed projection exists", () => {
    expect(resolveHucCrosswalkExplorer()).toMatchObject({
      outcome: "ABSTAIN",
      code: "NO_GOVERNED_RESPONSE",
      stationRefs: [],
      canFetch: false,
      canChangeCrosswalk: false,
      canRelease: false,
    });
  });

  it("keeps the adapter and feature free of transport and mutation seams", () => {
    const source = `${adapterSource}\n${featureSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(|XMLHttpRequest|WebSocket/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(
      /\b(?:approve|override|publish|release|sign|verifyCrosswalk)\s*\(/i,
    );
  });
});
