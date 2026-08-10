import { describe, expect, it } from "vitest";

import invalidExtraFieldFixture from "../../../fixtures/ui/view_registry_inspector_projection/invalid/extra-direct-store-field.json";
import invalidHeldEntryFixture from "../../../fixtures/ui/view_registry_inspector_projection/invalid/ready-with-held-entry.json";
import availableFixture from "../../../fixtures/ui/view_registry_inspector_projection/valid/available.json";
import deniedFixture from "../../../fixtures/ui/view_registry_inspector_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/view_registry_inspector_projection/valid/error.json";
import heldFixture from "../../../fixtures/ui/view_registry_inspector_projection/valid/held.json";
import adapterSource from "../src/adapters/ViewRegistryInspectorProjection.ts?raw";
import featureSource from "../src/features/view_registry_inspector/index.ts?raw";
import { parseViewRegistryInspectionProjection } from "../src/adapters/ViewRegistryInspectorProjection";
import { resolveViewRegistryInspector } from "../src/features/view_registry_inspector";

describe("Explorer View Registry inspector", () => {
  it("shows proposed inactive route metadata from a closed projection", () => {
    const result = resolveViewRegistryInspector(availableFixture);

    expect(result).toMatchObject({
      outcome: "AVAILABLE",
      code: "REGISTRY_INSPECTION_READY",
      status: "READY",
      registryId: "kfm:view-registry:aaaaaaaaaaaaaaaaaaaaaaaa",
      evaluatedAt: "2026-08-10T18:00:00Z",
      canBindRoute: false,
      canActivateLayer: false,
      canEvaluatePolicy: false,
      canApprove: false,
      canRelease: false,
      canPublish: false,
      accessibilityLabel: "View Registry inspector: available",
    });
    expect(result.entries).toHaveLength(2);
    expect(result.entries[0]).toMatchObject({
      viewId: "kfm:view:hydrology.streamflow",
      routePath: "/map/hydrology/streamflow",
      deliveryKind: "GOVERNED_API_CONTRACT",
      catalogClosureState: "READY",
      renderer: "MAPLIBRE_2D",
      protocol: "PMTILES",
      activationState: "PROPOSED_INACTIVE",
    });
    expect(result.registryId?.slice("kfm:view-registry:".length)).toBe(
      result.specHash?.slice("sha256:".length, "sha256:".length + 24),
    );
  });

  it("preserves hold, deny, and upstream error without registry detail", () => {
    expect(resolveViewRegistryInspector(heldFixture)).toMatchObject({
      outcome: "ABSTAIN",
      code: "REGISTRY_INSPECTION_HELD",
      status: "HELD",
      registryId: null,
      entries: [],
    });
    expect(resolveViewRegistryInspector(deniedFixture)).toMatchObject({
      outcome: "DENY",
      code: "REGISTRY_INSPECTION_DENIED",
      status: "DENIED",
      registryId: null,
      entries: [],
    });
    expect(resolveViewRegistryInspector(errorFixture)).toMatchObject({
      outcome: "ERROR",
      code: "UPSTREAM_ERROR",
      status: "UPSTREAM_ERROR",
      registryId: null,
      entries: [],
      ariaLive: "assertive",
    });
  });

  it("rejects an unknown source field without reflecting its canary", () => {
    expect(
      parseViewRegistryInspectionProjection(invalidExtraFieldFixture),
    ).toEqual({
      ok: false,
      code: "MALFORMED_VIEW_REGISTRY_INSPECTION_PROJECTION",
    });
    const result = resolveViewRegistryInspector(invalidExtraFieldFixture);
    expect(result).toMatchObject({
      outcome: "ERROR",
      code: "INVALID_PAYLOAD",
      registryId: null,
      specHash: null,
      entries: [],
    });
    expect(JSON.stringify(result)).not.toContain(
      "SENSITIVE_VIEW_REGISTRY_CANARY_7ad3",
    );
  });

  it("fails closed when a ready projection contains a held entry", () => {
    expect(
      parseViewRegistryInspectionProjection(invalidHeldEntryFixture),
    ).toEqual({
      ok: false,
      code: "MALFORMED_VIEW_REGISTRY_INSPECTION_PROJECTION",
    });
  });

  it("rejects identity drift, direct-store references, duplicate routes, and noncanonical arrays", () => {
    const identityDrift = JSON.parse(JSON.stringify(availableFixture));
    identityDrift.registry_id = "kfm:view-registry:bbbbbbbbbbbbbbbbbbbbbbbb";

    const directStore = JSON.parse(JSON.stringify(availableFixture));
    directStore.entries[0].contract_ref =
      "kfm:contract:data/raw/hydrology-streamflow";

    const duplicateRoute = JSON.parse(JSON.stringify(availableFixture));
    duplicateRoute.entries[1].route_path =
      duplicateRoute.entries[0].route_path;

    const reversedEntries = JSON.parse(JSON.stringify(availableFixture));
    reversedEntries.entries.reverse();

    const reversedLayers = JSON.parse(JSON.stringify(availableFixture));
    reversedLayers.entries[0].layer_manifest_refs.reverse();

    for (const candidate of [
      identityDrift,
      directStore,
      duplicateRoute,
      reversedEntries,
      reversedLayers,
    ]) {
      expect(parseViewRegistryInspectionProjection(candidate)).toEqual({
        ok: false,
        code: "MALFORMED_VIEW_REGISTRY_INSPECTION_PROJECTION",
      });
    }
  });

  it("uses an explicit abstention when no governed projection exists", () => {
    expect(resolveViewRegistryInspector()).toMatchObject({
      outcome: "ABSTAIN",
      code: "NO_GOVERNED_RESPONSE",
      entries: [],
      canBindRoute: false,
      canActivateLayer: false,
      canRelease: false,
      canPublish: false,
    });
  });

  it("keeps the adapter and feature free of transport and mutation seams", () => {
    const source = adapterSource + "\n" + featureSource;
    expect(source).not.toMatch(/\bfetch\s*\(|XMLHttpRequest|WebSocket/);
    expect(source).not.toMatch(
      /\b(?:bindRoute|activateLayer|approve|override|publish|release)\s*\(/i,
    );
  });
});
