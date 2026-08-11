import { describe, expect, it } from "vitest";

import invalidExtraField from "../../../fixtures/ui/stac_conformance_inspector_projection/invalid/extra-field.json";
import invalidStateContradiction from "../../../fixtures/ui/stac_conformance_inspector_projection/invalid/state-contradiction.json";
import conformantFixture from "../../../fixtures/ui/stac_conformance_inspector_projection/valid/conformant.json";
import deniedFixture from "../../../fixtures/ui/stac_conformance_inspector_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/stac_conformance_inspector_projection/valid/error.json";
import heldFixture from "../../../fixtures/ui/stac_conformance_inspector_projection/valid/held.json";
import nonConformantFixture from "../../../fixtures/ui/stac_conformance_inspector_projection/valid/non-conformant.json";
import adapterSource from "../src/adapters/StacConformanceInspectorProjection.ts?raw";
import featureSource from "../src/features/stac_conformance_inspector/index.ts?raw";
import { parseStacConformanceInspectorProjection } from "../src/adapters/StacConformanceInspectorProjection";
import { resolveStacConformanceInspector } from "../src/features/stac_conformance_inspector";

describe("Explorer STAC conformance inspector", () => {
  it("shows closed conformance findings without querying a catalog", () => {
    const result = resolveStacConformanceInspector(conformantFixture);

    expect(result).toMatchObject({
      outcome: "AVAILABLE",
      code: "INSPECTION_AVAILABLE",
      inspectionState: "CONFORMANT",
      itemCount: 2,
      profileVersion: "1.0.0-draft.1",
      stacVersion: "1.0.0",
      canQueryCatalog: false,
      canValidateSourceBytes: false,
      canMutateCatalog: false,
      canAdmitSource: false,
      canEvaluatePolicy: false,
      canRelease: false,
      canPublish: false,
      accessibilityLabel: "STAC conformance inspector: available",
    });
    expect(result.conformanceClasses).toHaveLength(2);
    expect(result.identityRules).toHaveLength(4);
    expect(result.mimeTypes).toHaveLength(2);
    expect(result.extensions[0]).toMatchObject({
      extensionId: "kfm://profile/stac/kfm-profile-v1",
      status: "PRESENT_ALL",
      itemCount: 2,
    });
    expect(result.collectionContract).toMatchObject({
      status: "COMPLETE",
      requiredFieldCount: 8,
      presentFieldCount: 8,
    });
  });

  it("preserves a non-conformant result as findings, not authority", () => {
    const result = resolveStacConformanceInspector(nonConformantFixture);

    expect(result).toMatchObject({
      outcome: "AVAILABLE",
      inspectionState: "NON_CONFORMANT",
      ariaLive: "assertive",
      canApprove: false,
      canRelease: false,
      canPublish: false,
    });
    expect(result.conformanceClasses[0]).toMatchObject({
      classId: "KFM_TRUST_EXTENSION_V1",
      status: "FAIL",
      findingCodes: ["KFM_EXTENSION_MISSING"],
    });
    expect(result.collectionContract).toMatchObject({
      status: "INCOMPLETE",
      findingCodes: ["COLLECTION_CONTRACT_INCOMPLETE"],
    });
  });

  it("preserves abstain, deny, and upstream error without STAC detail", () => {
    expect(resolveStacConformanceInspector(heldFixture)).toMatchObject({
      outcome: "ABSTAIN",
      code: "INSPECTION_UNAVAILABLE",
      inspectionId: null,
      conformanceClasses: [],
    });
    expect(resolveStacConformanceInspector(deniedFixture)).toMatchObject({
      outcome: "DENY",
      code: "POLICY_DENIED",
      inspectionId: null,
      conformanceClasses: [],
    });
    expect(resolveStacConformanceInspector(errorFixture)).toMatchObject({
      outcome: "ERROR",
      code: "UPSTREAM_ERROR",
      inspectionId: null,
      conformanceClasses: [],
      ariaLive: "assertive",
    });
  });

  it("rejects unknown fields without reflecting their canary", () => {
    expect(parseStacConformanceInspectorProjection(invalidExtraField)).toEqual({
      ok: false,
      code: "MALFORMED_STAC_CONFORMANCE_INSPECTOR_PROJECTION",
    });
    const result = resolveStacConformanceInspector(invalidExtraField);
    expect(result).toMatchObject({
      outcome: "ERROR",
      code: "INVALID_PAYLOAD",
      inspectionId: null,
      conformanceClasses: [],
    });
    expect(JSON.stringify(result)).not.toContain(
      "STAC_INSPECTOR_INTERNAL_CANARY_6d927e",
    );
  });

  it("fails closed when the declared inspection state contradicts findings", () => {
    expect(
      parseStacConformanceInspectorProjection(invalidStateContradiction),
    ).toEqual({
      ok: false,
      code: "MALFORMED_STAC_CONFORMANCE_INSPECTOR_PROJECTION",
    });
  });

  it("rejects identity, order, completeness, extension, and governance drift", () => {
    const identityDrift = JSON.parse(JSON.stringify(conformantFixture));
    identityDrift.inspection_id =
      "kfm:stac-conformance-inspection:ffffffffffffffffffffffff";

    const reversedClasses = JSON.parse(JSON.stringify(conformantFixture));
    reversedClasses.conformance_classes.reverse();

    const extensionCountDrift = JSON.parse(JSON.stringify(conformantFixture));
    extensionCountDrift.extensions[0].item_count = 1;

    const extensionStateDrift = JSON.parse(JSON.stringify(conformantFixture));
    extensionStateDrift.extensions[0].status = "ABSENT";
    extensionStateDrift.extensions[0].item_count = 0;

    const incompleteCheckSet = JSON.parse(JSON.stringify(conformantFixture));
    incompleteCheckSet.identity_rules.pop();

    const unsafeGovernance = JSON.parse(JSON.stringify(conformantFixture));
    unsafeGovernance.governance.catalog_query_attempted = true;

    for (const candidate of [
      identityDrift,
      reversedClasses,
      extensionCountDrift,
      extensionStateDrift,
      incompleteCheckSet,
      unsafeGovernance,
    ]) {
      expect(parseStacConformanceInspectorProjection(candidate)).toEqual({
        ok: false,
        code: "MALFORMED_STAC_CONFORMANCE_INSPECTOR_PROJECTION",
      });
    }
  });

  it("uses an explicit abstention when no governed projection exists", () => {
    expect(resolveStacConformanceInspector()).toMatchObject({
      outcome: "ABSTAIN",
      code: "NO_GOVERNED_RESPONSE",
      conformanceClasses: [],
      canQueryCatalog: false,
      canMutateCatalog: false,
      canRelease: false,
      canPublish: false,
    });
  });

  it("contains no transport, persistence, direct-store, or mutation seam", () => {
    const source = `${adapterSource}\n${featureSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(|XMLHttpRequest|WebSocket/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(
      /\b(?:queryCatalog|mutateCatalog|admitSource|approve|release|publish)\s*\(/i,
    );
  });
});
