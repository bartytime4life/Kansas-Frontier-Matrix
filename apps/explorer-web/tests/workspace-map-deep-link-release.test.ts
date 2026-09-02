import { describe, expect, it } from "vitest";
import { MAP_FEATURE_SELECTION_PROFILE } from "@kfm/maplibre";
import mainSource from "../src/main.ts?raw";
import {
  PUBLIC_WORKSPACE_CONTEXT_PROFILE,
  PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM,
  serializePublicWorkspaceContext,
} from "../src/site/workspace-context";
import {
  PUBLIC_MAP_CASE_DEEP_LINK_RETRY_LIMIT,
  resolvePublicMapCaseManualSelectionTransition,
  resolvePublicMapCaseRetryPlan,
  resolvePublicMapCaseUrlConsumerCommit,
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
      activeDeepLinkMapCaseId: null,
      mapCaseIdToSelect: "missing",
      releaseOwnedSelection: false,
    });
  });

  it("commits ownership only after the requested control accepts selection", () => {
    const requested = resolvePublicMapCaseUrlTransition(missingMapUrl(), null);

    expect(resolvePublicMapCaseUrlConsumerCommit(requested, false)).toBeNull();
    expect(
      resolvePublicMapCaseUrlTransition(
        missingMapUrl(),
        resolvePublicMapCaseUrlConsumerCommit(requested, false),
      ),
    ).toEqual(requested);
    expect(resolvePublicMapCaseUrlConsumerCommit(requested, true)).toBe(
      "missing",
    );
    expect(
      resolvePublicMapCaseUrlTransition(
        missingMapUrl(),
        resolvePublicMapCaseUrlConsumerCommit(requested, true),
      ),
    ).toEqual({
      activeDeepLinkMapCaseId: "missing",
      mapCaseIdToSelect: null,
      releaseOwnedSelection: false,
    });
  });

  it("bounds disabled-control retries and resets the budget for a new URL", () => {
    let state = Object.freeze({
      attemptsRemaining: PUBLIC_MAP_CASE_DEEP_LINK_RETRY_LIMIT,
      urlHref: null,
    });
    for (let index = 0; index < PUBLIC_MAP_CASE_DEEP_LINK_RETRY_LIMIT; index += 1) {
      const plan = resolvePublicMapCaseRetryPlan(
        state,
        missingMapUrl().href,
      );
      expect(plan.shouldSchedule).toBe(true);
      state = plan;
    }
    expect(resolvePublicMapCaseRetryPlan(state, missingMapUrl().href)).toEqual({
      attemptsRemaining: 0,
      urlHref: missingMapUrl().href,
      shouldSchedule: false,
    });

    const changedUrl = missingMapUrl();
    changedUrl.searchParams.set("lang", "es");
    expect(resolvePublicMapCaseRetryPlan(state, changedUrl.href)).toEqual({
      attemptsRemaining: PUBLIC_MAP_CASE_DEEP_LINK_RETRY_LIMIT - 1,
      urlHref: changedUrl.href,
      shouldSchedule: true,
    });
  });

  it("releases ownership only when a departing URL still owns the fixture", () => {
    const neutralUrl = new URL("https://example.invalid/explorer?lang=en#map");

    expect(resolvePublicMapCaseUrlTransition(neutralUrl, "missing")).toEqual({
      activeDeepLinkMapCaseId: null,
      mapCaseIdToSelect: null,
      releaseOwnedSelection: true,
    });
    expect(resolvePublicMapCaseUrlTransition(neutralUrl, null)).toEqual({
      activeDeepLinkMapCaseId: null,
      mapCaseIdToSelect: null,
      releaseOwnedSelection: false,
    });
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
    expect(mainSource).toContain("resolvePublicMapCaseUrlConsumerCommit");
    expect(mainSource).toContain("mapCaseButton?.disabled");
    expect(mainSource).toContain("scheduleMapDeepLinkRetry(safeUrl)");
    expect(mainSource).toContain("window.location.href !== retryPlan.urlHref");
    expect(mainSource).toContain("const selectionApplied = mapCaseButton.disabled");
    expect(mainSource).not.toContain("activeDeepLinkMapCaseId = mapTransition.activeDeepLinkMapCaseId");
    expect(mainSource).not.toContain("selection.evidenceRefs.join");
  });
});
