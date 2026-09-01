import { describe, expect, it } from "vitest";
import { MAP_FEATURE_SELECTION_PROFILE } from "@kfm/maplibre";
import mainSource from "../src/main.ts?raw";
import {
  PUBLIC_WORKSPACE_CONTEXT_PROFILE,
  PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM,
  serializePublicWorkspaceContext,
} from "../src/site/workspace-context";
import { resolvePublicMapCaseManualSelectionTransition } from "../src/site/workspace-map-deep-link";

const missingMapContext = Object.freeze({
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

function missingMapUrl(): URL {
  const query = serializePublicWorkspaceContext(missingMapContext);
  if (query === null) throw new Error("Expected synthetic map context to serialize.");
  const url = new URL(`https://example.invalid/explorer?${query}#map`);
  url.searchParams.set("lang", "en");
  return url;
}

describe("Explorer manual map-selection deep-link release", () => {
  it("keeps URL ownership when the restored missing case is selected again", () => {
    const transition = resolvePublicMapCaseManualSelectionTransition(
      missingMapUrl(),
      "missing",
      "missing",
    );

    expect(transition).toEqual({
      activeDeepLinkMapCaseId: "missing",
      replacementUrl: null,
      reason: "UNCHANGED",
    });
  });

  it("releases deep-link ownership instead of serializing a richer manual fixture", () => {
    const transition = resolvePublicMapCaseManualSelectionTransition(
      missingMapUrl(),
      "missing",
      "restricted",
    );

    expect(transition.activeDeepLinkMapCaseId).toBeNull();
    expect(transition.reason).toBe("RELEASED");
    expect(
      transition.replacementUrl?.searchParams.has(
        PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM,
      ),
    ).toBe(false);
    expect(transition.replacementUrl?.searchParams.get("lang")).toBe("en");
    expect(transition.replacementUrl?.hash).toBe("#map");
    expect(decodeURIComponent(transition.replacementUrl?.toString() ?? "")).not.toContain(
      "restricted",
    );
    expect(decodeURIComponent(transition.replacementUrl?.toString() ?? "")).not.toContain(
      "evidence",
    );
  });

  it("drops stale ownership without rewriting an unrelated URL", () => {
    const url = new URL("https://example.invalid/explorer?lang=en#map");
    const transition = resolvePublicMapCaseManualSelectionTransition(
      url,
      "missing",
      "supported",
    );

    expect(transition).toEqual({
      activeDeepLinkMapCaseId: null,
      replacementUrl: null,
      reason: "STALE_OWNER",
    });
    expect(url.toString()).toBe("https://example.invalid/explorer?lang=en#map");
  });

  it("composes the release at the existing synthetic fixture boundary", () => {
    expect(mainSource).toContain(
      "resolvePublicMapCaseManualSelectionTransition",
    );
    expect(mainSource).toContain(
      'button[data-map-evidence-case]',
    );
    expect(mainSource).toContain(
      'root.addEventListener("click", releaseDeepLinkMapOwnershipOnManualSelection)',
    );
    expect(mainSource).toContain(
      "syncPublicWorkspaceNavigation(navigation, transition.replacementUrl)",
    );
    expect(mainSource).not.toContain("selection.evidenceRefs.join");
  });
});
