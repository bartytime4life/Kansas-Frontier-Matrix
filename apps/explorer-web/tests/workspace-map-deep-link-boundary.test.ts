import { describe, expect, it } from "vitest";
import { MAP_FEATURE_SELECTION_PROFILE } from "@kfm/maplibre";
import {
  PUBLIC_WORKSPACE_CONTEXT_PROFILE,
  parsePublicWorkspaceContextUrl,
  serializePublicWorkspaceContext,
} from "../src/site/workspace-context";
import { resolvePublicEvidenceFreeMapCaseId } from "../src/site/workspace-navigation";

const neutralMapContext = Object.freeze({
  profile: PUBLIC_WORKSPACE_CONTEXT_PROFILE,
  workspaceId: "explore",
  domainIds: Object.freeze([]),
  placeIds: Object.freeze([]),
  layerIds: Object.freeze(["layer:synthetic-streamflow"]),
  camera: null,
  selection: Object.freeze({
    profile: MAP_FEATURE_SELECTION_PROFILE,
    selectionId: "selection:missing",
    layerId: "layer:synthetic-streamflow",
    featureId: "feature:missing",
    evidenceRefs: Object.freeze([]),
  }),
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

function contextUrl(context: unknown): URL {
  const query = serializePublicWorkspaceContext(context);
  if (query === null) throw new Error("Expected public-safe context to serialize.");
  return new URL(`https://example.invalid/explorer?${query}#map`);
}

describe("Explorer evidence-free map deep-link boundary", () => {
  it("restores only the exact domain-neutral synthetic selection", () => {
    const url = contextUrl(neutralMapContext);
    expect(parsePublicWorkspaceContextUrl(url)).not.toBeNull();
    expect(resolvePublicEvidenceFreeMapCaseId(url)).toBe("missing");
  });

  it("does not silently discard unrelated valid public context dimensions", () => {
    const contexts = [
      {
        ...neutralMapContext,
        layerIds: ["layer:synthetic-streamflow", "layer:synthetic-secondary"],
      },
      {
        ...neutralMapContext,
        placeIds: ["place:synthetic-kansas"],
      },
      {
        ...neutralMapContext,
        time: { ...neutralMapContext.time, validAt: "2026-08-01" },
      },
      {
        ...neutralMapContext,
        compare: {
          mode: "SIDE_BY_SIDE",
          leftContextId: "context:left",
          rightContextId: "context:right",
        },
      },
      {
        ...neutralMapContext,
        storyNodeId: "story:synthetic",
      },
    ];

    for (const context of contexts) {
      const url = contextUrl(context);
      expect(parsePublicWorkspaceContextUrl(url)).not.toBeNull();
      expect(resolvePublicEvidenceFreeMapCaseId(url)).toBeNull();
    }
  });

  it("keeps Archaeology and People/DNA/Land domain scope outside the synthetic map fixture", () => {
    for (const domainId of ["archaeology", "people_dna_land"] as const) {
      const url = contextUrl({ ...neutralMapContext, domainIds: [domainId] });
      expect(parsePublicWorkspaceContextUrl(url)).not.toBeNull();
      expect(resolvePublicEvidenceFreeMapCaseId(url)).toBeNull();
    }
  });
});
