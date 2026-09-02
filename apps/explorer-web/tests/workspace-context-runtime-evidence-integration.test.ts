import { describe, expect, it, vi } from "vitest";

import layerAdmissionFixture from "../../../fixtures/runtime/layer_manifest_admission/cases.json";
import {
  MAP_FEATURE_SELECTION_PROFILE,
  type MapFeatureSelection,
} from "@kfm/maplibre";
import { resolveMapRuntimeSelectionEvidence } from "../src/features/map_runtime/runtime-evidence-binding";
import {
  PUBLIC_WORKSPACE_CONTEXT_PROFILE,
  PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM,
  parsePublicWorkspaceContextUrl,
  withPublicWorkspaceContext,
} from "../src/site/workspace-context";
import { sanitizePublicWorkspaceNavigationUrl } from "../src/site/workspace-navigation";

const selection: MapFeatureSelection = Object.freeze({
  profile: MAP_FEATURE_SELECTION_PROFILE,
  selectionId: "selection:synthetic:deep-link-001",
  layerId: "layer:released:synthetic-streamflow",
  featureId: "feature:synthetic:deep-link-001",
  evidenceRefs: Object.freeze([]),
});

function publicContext(currentSelection: MapFeatureSelection = selection): unknown {
  return Object.freeze({
    profile: PUBLIC_WORKSPACE_CONTEXT_PROFILE,
    workspaceId: "explore",
    domainIds: Object.freeze(["hydrology"]),
    placeIds: Object.freeze([]),
    layerIds: Object.freeze([currentSelection.layerId]),
    camera: null,
    selection: currentSelection,
    time: Object.freeze({
      validAt: null,
      observedAt: null,
      asOf: null,
      releaseId: null,
    }),
    compare: Object.freeze({
      mode: "NONE",
      leftContextId: null,
      rightContextId: null,
    }),
    storyNodeId: null,
    publicSafe: true,
  });
}

function admittedLayerManifest(): typeof layerAdmissionFixture.base {
  const value = structuredClone(layerAdmissionFixture.base);
  value.layer_id = selection.layerId;
  value.runtime_request.layer_id = selection.layerId;
  return value;
}

function parsedUrlSelection(): MapFeatureSelection {
  const url = withPublicWorkspaceContext(
    new URL("https://example.invalid/explorer"),
    publicContext(),
  );
  if (url === null) throw new Error("Expected synthetic public context URL.");
  const parsed = parsePublicWorkspaceContextUrl(url);
  if (parsed?.selection === null || parsed?.selection === undefined) {
    throw new Error("Expected public deep-link selection.");
  }
  return parsed.selection;
}

describe("public workspace context to governed runtime evidence integration", () => {
  it("keeps a URL-derived selection inside LayerManifest admission and abstains without evidence", async () => {
    const resolver = vi.fn(async () => {
      throw new Error("Evidence transport must not run for evidence-free URL context.");
    });

    const result = await resolveMapRuntimeSelectionEvidence(
      parsedUrlSelection(),
      admittedLayerManifest(),
      resolver,
    );

    expect(resolver).not.toHaveBeenCalled();
    expect(result).toMatchObject({
      layerAdmission: {
        outcome: "PASS",
        code: "LAYER_MANIFEST_REGISTER_ELIGIBLE",
      },
      evidence: {
        selection,
        code: "MISSING_EVIDENCE",
        drawer: {
          outcome: "ABSTAIN",
          code: "MISSING_EVIDENCE",
        },
      },
    });
  });

  it("denies a URL-derived selection when the admitted manifest belongs to another layer", async () => {
    const resolver = vi.fn(async () => {
      throw new Error("Governed resolver must not run across a layer mismatch.");
    });
    const manifest = admittedLayerManifest();
    manifest.layer_id = "layer:released:other";
    manifest.runtime_request.layer_id = "layer:released:other";

    const result = await resolveMapRuntimeSelectionEvidence(
      parsedUrlSelection(),
      manifest,
      resolver,
    );

    expect(resolver).not.toHaveBeenCalled();
    expect(result).toMatchObject({
      layerAdmission: {
        outcome: "DENY",
        code: "LAYER_MANIFEST_SELECTION_LAYER_MISMATCH",
      },
      evidence: {
        drawer: {
          outcome: "ERROR",
          code: "UPSTREAM_ERROR",
        },
      },
    });
  });

  it("rejects and scrubs an evidence-bearing deep link before runtime evidence resolution", () => {
    const restrictedCanary = "kfm:evidence:restricted-canary";
    const evidenceBearingSelection = Object.freeze({
      ...selection,
      evidenceRefs: Object.freeze([restrictedCanary]),
    });
    const url = new URL("https://example.invalid/explorer#map");
    url.searchParams.set(
      PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM,
      JSON.stringify(publicContext(evidenceBearingSelection)),
    );

    expect(parsePublicWorkspaceContextUrl(url)).toBeNull();

    const sanitized = sanitizePublicWorkspaceNavigationUrl(url);
    expect(
      sanitized.searchParams.has(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM),
    ).toBe(false);
    expect(decodeURIComponent(sanitized.toString())).not.toContain(restrictedCanary);
  });
});
