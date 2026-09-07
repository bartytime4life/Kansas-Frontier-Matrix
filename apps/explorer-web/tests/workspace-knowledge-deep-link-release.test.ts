import { describe, expect, it } from "vitest";
import mainSource from "../src/main.ts?raw";
import {
  PUBLIC_KNOWLEDGE_DOMAIN_DEEP_LINK_RETRY_LIMIT,
  hasSinglePublicKnowledgeDomainConsumer,
  isPublicKnowledgeDomainOwnedConsumerCurrent,
  isPublicKnowledgeDomainRetryGenerationCurrent,
  resolvePublicKnowledgeDomainRetryPlan,
  resolvePublicKnowledgeDomainManualSelectionTransition,
  resolvePublicKnowledgeDomainUrlConsumerCommit,
  resolveSinglePublicKnowledgeDomainControlId,
} from "../src/site/workspace-knowledge-deep-link";
import { resolvePublicKnowledgeDomainSelectionTransition } from "../src/site/workspace-navigation";
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
  it("fails closed when mounted or selected Knowledge controls are ambiguous", () => {
    expect(
      hasSinglePublicKnowledgeDomainConsumer(
        ["hydrology", "archaeology"],
        "archaeology",
      ),
    ).toBe(true);
    expect(
      hasSinglePublicKnowledgeDomainConsumer([], "archaeology"),
    ).toBe(false);
    expect(
      hasSinglePublicKnowledgeDomainConsumer(
        ["archaeology", "archaeology"],
        "archaeology",
      ),
    ).toBe(false);

    expect(
      resolveSinglePublicKnowledgeDomainControlId(["archaeology"]),
    ).toBe("archaeology");
    expect(resolveSinglePublicKnowledgeDomainControlId([])).toBeNull();
    expect(
      resolveSinglePublicKnowledgeDomainControlId([
        "archaeology",
        "archaeology",
      ]),
    ).toBeNull();
    expect(
      resolveSinglePublicKnowledgeDomainControlId([undefined]),
    ).toBeNull();
  });

  it("bounds unavailable-control retries and resets the budget for a new URL", () => {
    let state = Object.freeze({
      attemptsRemaining: PUBLIC_KNOWLEDGE_DOMAIN_DEEP_LINK_RETRY_LIMIT,
      urlHref: null,
    });
    for (
      let index = 0;
      index < PUBLIC_KNOWLEDGE_DOMAIN_DEEP_LINK_RETRY_LIMIT;
      index += 1
    ) {
      const plan = resolvePublicKnowledgeDomainRetryPlan(
        state,
        contextUrl(["archaeology"]).href,
      );
      expect(plan.shouldSchedule).toBe(true);
      state = plan;
    }
    expect(
      resolvePublicKnowledgeDomainRetryPlan(
        state,
        contextUrl(["archaeology"]).href,
      ),
    ).toEqual({
      attemptsRemaining: 0,
      urlHref: contextUrl(["archaeology"]).href,
      shouldSchedule: false,
    });

    expect(
      resolvePublicKnowledgeDomainRetryPlan(
        state,
        contextUrl(["people_dna_land"]).href,
      ),
    ).toEqual({
      attemptsRemaining: PUBLIC_KNOWLEDGE_DOMAIN_DEEP_LINK_RETRY_LIMIT - 1,
      urlHref: contextUrl(["people_dna_land"]).href,
      shouldSchedule: true,
    });
  });

  it("rejects a stale retry callback after cancellation or replacement", () => {
    expect(isPublicKnowledgeDomainRetryGenerationCurrent(4, 4)).toBe(true);
    expect(isPublicKnowledgeDomainRetryGenerationCurrent(5, 4)).toBe(false);
    expect(isPublicKnowledgeDomainRetryGenerationCurrent(6, 4)).toBe(false);
  });

  it("invalidates ownership when a Knowledge control is remounted", () => {
    const acceptedControl = Object.freeze({ domainId: "archaeology" });
    const remountedControl = Object.freeze({ domainId: "archaeology" });

    expect(
      isPublicKnowledgeDomainOwnedConsumerCurrent(
        acceptedControl,
        acceptedControl,
      ),
    ).toBe(true);
    expect(
      isPublicKnowledgeDomainOwnedConsumerCurrent(
        acceptedControl,
        remountedControl,
      ),
    ).toBe(false);
    expect(
      isPublicKnowledgeDomainOwnedConsumerCurrent(acceptedControl, undefined),
    ).toBe(false);
    expect(
      isPublicKnowledgeDomainOwnedConsumerCurrent(null, remountedControl),
    ).toBe(false);
  });

  it("clears a replaced owner before resolving context-removal cleanup", () => {
    const acceptedControl = Object.freeze({ domainId: "archaeology" });
    const remountedControl = Object.freeze({ domainId: "archaeology" });
    const currentOwner = isPublicKnowledgeDomainOwnedConsumerCurrent(
      acceptedControl,
      remountedControl,
    )
      ? "archaeology"
      : null;

    expect(
      resolvePublicKnowledgeDomainSelectionTransition(
        new URL("https://example.invalid/explorer?lang=en#knowledge"),
        currentOwner,
        "archaeology",
      ),
    ).toEqual({
      activeDeepLinkDomainId: null,
      domainIdToSelect: null,
    });
  });

  it("commits URL ownership after the existing control applies the domain", () => {
    const transition = resolvePublicKnowledgeDomainSelectionTransition(
      contextUrl(["archaeology"]),
      null,
      "hydrology",
    );

    expect(transition.domainIdToSelect).toBe("archaeology");
    expect(
      resolvePublicKnowledgeDomainUrlConsumerCommit(
        transition,
        "archaeology",
        true,
        true,
        true,
      ),
    ).toBe("archaeology");
  });

  it("keeps an unapplied domain consumer unowned and retryable", () => {
    const transition = resolvePublicKnowledgeDomainSelectionTransition(
      contextUrl(["people_dna_land"]),
      null,
      "hydrology",
    );

    expect(transition.domainIdToSelect).toBe("people_dna_land");
    expect(
      resolvePublicKnowledgeDomainUrlConsumerCommit(
        transition,
        "hydrology",
        true,
        true,
        true,
      ),
    ).toBeNull();
    expect(
      resolvePublicKnowledgeDomainUrlConsumerCommit(
        transition,
        null,
        true,
        true,
        true,
      ),
    ).toBeNull();
  });

  it("preserves established ownership when no new selection is required", () => {
    const transition = resolvePublicKnowledgeDomainSelectionTransition(
      contextUrl(["archaeology"]),
      "archaeology",
      "archaeology",
    );

    expect(transition.domainIdToSelect).toBeNull();
    expect(
      resolvePublicKnowledgeDomainUrlConsumerCommit(
        transition,
        "archaeology",
        true,
        true,
        true,
      ),
    ).toBe("archaeology");
  });

  it("releases established ownership when final visible selection changes", () => {
    const transition = resolvePublicKnowledgeDomainSelectionTransition(
      contextUrl(["archaeology"]),
      "archaeology",
      "archaeology",
    );

    expect(transition.domainIdToSelect).toBeNull();
    expect(
      resolvePublicKnowledgeDomainUrlConsumerCommit(
        transition,
        null,
        true,
        true,
        true,
      ),
    ).toBeNull();
    expect(
      resolvePublicKnowledgeDomainUrlConsumerCommit(
        transition,
        "hydrology",
        true,
        true,
        true,
      ),
    ).toBeNull();
  });

  it("keeps an already-selected but disabled domain consumer unowned", () => {
    const transition = resolvePublicKnowledgeDomainSelectionTransition(
      contextUrl(["people_dna_land"]),
      null,
      "people_dna_land",
    );

    expect(transition.domainIdToSelect).toBeNull();
    expect(
      resolvePublicKnowledgeDomainUrlConsumerCommit(
        transition,
        "people_dna_land",
        false,
        true,
        true,
      ),
    ).toBeNull();
    expect(
      resolvePublicKnowledgeDomainUrlConsumerCommit(
        transition,
        "people_dna_land",
        true,
        true,
        true,
      ),
    ).toBe("people_dna_land");
  });

  it("releases established ownership for a replacement Knowledge control", () => {
    const transition = resolvePublicKnowledgeDomainSelectionTransition(
      contextUrl(["archaeology"]),
      "archaeology",
      "archaeology",
    );

    expect(
      resolvePublicKnowledgeDomainUrlConsumerCommit(
        transition,
        "archaeology",
        true,
        false,
        true,
      ),
    ).toBeNull();
  });

  it("rejects ownership when selection rewrites the requested URL", () => {
    const transition = resolvePublicKnowledgeDomainSelectionTransition(
      contextUrl(["archaeology"]),
      null,
      "hydrology",
    );

    expect(
      resolvePublicKnowledgeDomainUrlConsumerCommit(
        transition,
        "archaeology",
        true,
        true,
        false,
      ),
    ).toBeNull();
  });

  it("preserves ownership during programmatic restoration of the same domain", () => {
    expect(
      resolvePublicKnowledgeDomainManualSelectionTransition(
        contextUrl(["archaeology"]),
        "archaeology",
        "archaeology",
        true,
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
      true,
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
        false,
      ),
    ).toEqual({
      activeDeepLinkDomainId: null,
      replacementUrl: null,
      reason: "STALE_OWNER",
    });
  });

  it("releases an uncommitted URL request after a different manual domain applies", () => {
    const transition = resolvePublicKnowledgeDomainManualSelectionTransition(
      contextUrl(["archaeology"]),
      null,
      "people_dna_land",
      true,
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

  it("leaves ordinary manual selection unchanged without a URL request", () => {
    expect(
      resolvePublicKnowledgeDomainManualSelectionTransition(
        new URL("https://example.invalid/explorer?lang=en#knowledge"),
        null,
        "people_dna_land",
        true,
      ),
    ).toEqual({
      activeDeepLinkDomainId: null,
      replacementUrl: null,
      reason: "UNCHANGED",
    });
  });

  it("keeps an uncommitted URL request when a manual domain does not apply", () => {
    expect(
      resolvePublicKnowledgeDomainManualSelectionTransition(
        contextUrl(["archaeology"]),
        null,
        "people_dna_land",
        false,
      ),
    ).toEqual({
      activeDeepLinkDomainId: null,
      replacementUrl: null,
      reason: "UNCHANGED",
    });
  });

  it("retains URL ownership when a different manual control does not apply", () => {
    expect(
      resolvePublicKnowledgeDomainManualSelectionTransition(
        contextUrl(["archaeology"]),
        "archaeology",
        "people_dna_land",
        false,
      ),
    ).toEqual({
      activeDeepLinkDomainId: "archaeology",
      replacementUrl: null,
      reason: "UNCHANGED",
    });
  });

  it("composes ownership at the existing enabled domain-control boundary", () => {
    expect(mainSource).toContain(
      "resolvePublicKnowledgeDomainUrlConsumerCommit",
    );
    expect(mainSource).toContain("!domainButton.disabled");
    expect(mainSource).toContain(
      "requestedDomainId !== null && !consumerReady",
    );
    expect(mainSource).not.toContain(
      "requestedDomainId === null || consumerReady,",
    );
    expect(mainSource).toContain(
      "isPublicKnowledgeDomainOwnedConsumerCurrent(\n      activeDeepLinkKnowledgeDomainConsumer,",
    );
    expect(mainSource).toContain(
      "activeDeepLinkKnowledgeDomainConsumer =\n    activeDeepLinkKnowledgeDomainId !== null",
    );
    const ownershipValidationIndex = mainSource.indexOf(
      "const mountedOwnedConsumer =",
    );
    const domainTransitionIndex = mainSource.indexOf(
      "const domainTransition = resolvePublicKnowledgeDomainSelectionTransition(",
    );
    expect(ownershipValidationIndex).toBeGreaterThan(-1);
    expect(domainTransitionIndex).toBeGreaterThan(ownershipValidationIndex);
    expect(mainSource).toContain(
      '!button.disabled && button.getAttribute("aria-pressed") === "true"',
    );
    expect(mainSource).toContain("domainButton.click()");
    expect(mainSource).toContain(
      "scheduleKnowledgeDomainDeepLinkRetry(safeUrl)",
    );
    expect(mainSource).toContain(
      "cancelPendingKnowledgeDomainDeepLinkRetry()",
    );
    expect(mainSource).toContain(
      "window.location.href !== retryPlan.urlHref",
    );
    const knowledgeRetryScheduleIndex = mainSource.indexOf(
      "const scheduleKnowledgeDomainDeepLinkRetry",
    );
    const staleGenerationGuardIndex = mainSource.indexOf(
      "isPublicKnowledgeDomainRetryGenerationCurrent(",
      knowledgeRetryScheduleIndex,
    );
    const knowledgeRetryClearIndex = mainSource.indexOf(
      "pendingKnowledgeDomainDeepLinkRetry = null",
      staleGenerationGuardIndex,
    );
    expect(staleGenerationGuardIndex).toBeGreaterThan(
      knowledgeRetryScheduleIndex,
    );
    expect(knowledgeRetryClearIndex).toBeGreaterThan(staleGenerationGuardIndex);
    const clickIndex = mainSource.indexOf("domainButton.click()");
    const finalReadinessIndex = mainSource.indexOf(
      "const consumerReadyAfterSelection =",
      clickIndex,
    );
    const finalConsumerQueryIndex = mainSource.indexOf(
      "const mountedDomainConsumersAfterSelection =",
      clickIndex,
    );
    const ownershipCommitIndex = mainSource.indexOf(
      "resolvePublicKnowledgeDomainUrlConsumerCommit(",
      clickIndex,
    );
    expect(finalConsumerQueryIndex).toBeGreaterThan(clickIndex);
    expect(finalReadinessIndex).toBeGreaterThan(clickIndex);
    expect(finalReadinessIndex).toBeGreaterThan(finalConsumerQueryIndex);
    expect(ownershipCommitIndex).toBeGreaterThan(finalReadinessIndex);
    expect(mainSource).toContain(
      "requestedDomainId === null || consumerReadyAfterSelection",
    );
    expect(mainSource).toContain(
      "isPublicKnowledgeDomainOwnedConsumerCurrent(\n      domainButton ?? null,\n      mountedConsumerAfterSelection,",
    );
    expect(mainSource).toContain(
      "activeDeepLinkKnowledgeDomainId !== null &&\n    mountedConsumerAfterSelection !== undefined",
    );
    expect(mainSource).toContain(
      "const requestUrlCurrent = currentUrlAfterSelection.href === safeUrl.href",
    );
    expect(mainSource).toContain(
      "requestUrlCurrent ? safeUrl : currentUrlAfterSelection",
    );
    expect(mainSource).toContain(
      'button[data-domain-id][aria-pressed="true"]',
    );
    expect(mainSource).toContain(
      "hasSinglePublicKnowledgeDomainConsumer(",
    );
    expect(mainSource).toContain(
      "resolveSinglePublicKnowledgeDomainControlId(",
    );
    expect(mainSource).not.toContain("domainIds.join");
  });
});
