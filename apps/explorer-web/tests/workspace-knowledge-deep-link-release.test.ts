import { describe, expect, it } from "vitest";
import {
  resolvePublicKnowledgeDomainManualSelectionTransition,
} from "../src/site/workspace-knowledge-deep-link";
import {
  PUBLIC_WORKSPACE_CONTEXT_PROFILE,
  PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM,
  serializePublicWorkspaceContext,
} from "../src/site/workspace-context";

const knowledgeContext = Object.freeze({
  profile: PUBLIC_WORKSPACE_CONTEXT_PROFILE,
  workspaceId: "knowledge",
  domainIds: Object.freeze(["archaeology"]),
  placeIds: Object.freeze([]),
  layerIds: Object.freeze([]),
  camera: null,
  selection: null,
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

function contextUrl(domainIds: readonly string[]): URL {
  const query = serializePublicWorkspaceContext({
    ...knowledgeContext,
    domainIds,
  });
  if (query === null) throw new Error("Expected public-safe context to serialize.");
  return new URL(`https://example.invalid/explorer?lang=en&${query}#knowledge`);
}

describe("public Knowledge-domain deep-link release", () => {
  it("preserves ownership during programmatic restoration of the same domain", () => {
    expect(
      resolvePublicKnowledgeDomainManualSelectionTransition(
        contextUrl(["archaeology"]),
        "archaeology",
        "archaeology",
      ),
    ).toEqual({
      activeDeepLinkDomainId: "archaeology",
      replacementUrl: null,
      reason: "UNCHANGED",
    });
  });

  it("releases only public context after a different manual domain selection", () => {
    const original = contextUrl(["archaeology"]);
    const transition = resolvePublicKnowledgeDomainManualSelectionTransition(
      original,
      "archaeology",
      "people_dna_land",
    );

    expect(transition.reason).toBe("RELEASED");
    expect(transition.activeDeepLinkDomainId).toBeNull();
    expect(
      transition.replacementUrl?.searchParams.has(
        PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM,
      ),
    ).toBe(false);
    expect(transition.replacementUrl?.searchParams.get("lang")).toBe("en");
    expect(transition.replacementUrl?.hash).toBe("#knowledge");
    expect(decodeURIComponent(transition.replacementUrl?.toString() ?? "")).not.toContain(
      "people_dna_land",
    );
  });

  it("does not rewrite the URL when tracked ownership is stale", () => {
    expect(
      resolvePublicKnowledgeDomainManualSelectionTransition(
        contextUrl(["people_dna_land"]),
        "archaeology",
        "hydrology",
      ),
    ).toEqual({
      activeDeepLinkDomainId: null,
      replacementUrl: null,
      reason: "STALE_OWNER",
    });
  });

  it("leaves ordinary manual selection unchanged without a deep-link owner", () => {
    expect(
      resolvePublicKnowledgeDomainManualSelectionTransition(
        contextUrl(["archaeology"]),
        null,
        "people_dna_land",
      ),
    ).toEqual({
      activeDeepLinkDomainId: null,
      replacementUrl: null,
      reason: "UNCHANGED",
    });
  });
});
