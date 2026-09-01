import { describe, expect, it } from "vitest";
import { MAP_FEATURE_SELECTION_PROFILE } from "@kfm/maplibre";
import mainSource from "../src/main.ts?raw";
import mountSource from "../src/site/mount-explorer-site.ts?raw";
import {
  PUBLIC_WORKSPACE_CONTEXT_PROFILE,
  PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM,
  serializePublicWorkspaceContext,
} from "../src/site/workspace-context";
import {
  resolvePublicMapEvidenceResetFocusCaseId,
  resolvePublicMapCaseManualSelectionTransition,
  resolvePublicMapCaseUrlTransition,
} from "../src/site/workspace-map-deep-link";

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
  it("selects a newly URL-owned case without resetting the fixture", () => {
    expect(resolvePublicMapCaseUrlTransition(missingMapUrl(), null)).toEqual({
      activeDeepLinkMapCaseId: "missing",
      mapCaseIdToSelect: "missing",
      resetOwnedSelection: false,
    });
  });

  it("resets evidence only when a departing URL still owns the fixture", () => {
    const neutralUrl = new URL("https://example.invalid/explorer?lang=en#map");

    expect(resolvePublicMapCaseUrlTransition(neutralUrl, "missing")).toEqual({
      activeDeepLinkMapCaseId: null,
      mapCaseIdToSelect: null,
      resetOwnedSelection: true,
    });
    expect(resolvePublicMapCaseUrlTransition(neutralUrl, null)).toEqual({
      activeDeepLinkMapCaseId: null,
      mapCaseIdToSelect: null,
      resetOwnedSelection: false,
    });
  });

  it("preserves a stable keyboard target when the owned fixture is remounted", () => {
    const caseIds = Object.freeze(["supported", "missing", "restricted"]);

    expect(
      resolvePublicMapEvidenceResetFocusCaseId(false, "missing", caseIds),
    ).toBeNull();
    expect(
      resolvePublicMapEvidenceResetFocusCaseId(true, "missing", caseIds),
    ).toBe("missing");
    expect(
      resolvePublicMapEvidenceResetFocusCaseId(true, null, caseIds),
    ).toBe("supported");
    expect(
      resolvePublicMapEvidenceResetFocusCaseId(true, "retired", caseIds),
    ).toBe("supported");
    expect(
      resolvePublicMapEvidenceResetFocusCaseId(true, null, Object.freeze([])),
    ).toBeNull();
  });

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
    expect(mainSource).toContain("resolvePublicMapCaseUrlTransition");
    expect(mainSource).toContain("site.resetMapEvidenceSelection()");
    expect(mountSource).toContain("resetMapEvidenceSelection");
    expect(mountSource).toContain("mapFixture.destroy()");
    expect(mountSource).toContain("mapFixture = mountMapFixture()");
    expect(mountSource).toContain("focusWasInsideFixture");
    expect(mountSource).toContain("resolvePublicMapEvidenceResetFocusCaseId");
    expect(mountSource).toContain("?.focus()");
    expect(mainSource).not.toContain("selection.evidenceRefs.join");
  });
});
