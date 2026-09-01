import { describe, expect, it } from "vitest";
import { MAP_FEATURE_SELECTION_PROFILE } from "@kfm/maplibre";
import mainSource from "../src/main.ts?raw";
import navigationCss from "../src/site/site-foundation-a.css?raw";
import navigationSource from "../src/site/workspace-navigation.ts?raw";
import {
  PUBLIC_WORKSPACE_CONTEXT_PROFILE,
  PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM,
  serializePublicWorkspaceContext,
} from "../src/site/workspace-context";
import {
  resolvePublicEvidenceFreeMapCaseId,
  resolvePublicWorkspaceNavigationState,
  resolveSinglePublicKnowledgeDomainId,
  sanitizePublicWorkspaceNavigationUrl,
} from "../src/site/workspace-navigation";

const knowledgeContext = Object.freeze({
  profile: PUBLIC_WORKSPACE_CONTEXT_PROFILE,
  workspaceId: "knowledge",
  domainIds: Object.freeze(["hydrology"]),
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

function contextUrl(context: unknown, hash: string): URL {
  const query = serializePublicWorkspaceContext(context);
  if (query === null) throw new Error("Expected public-safe context to serialize.");
  return new URL(`https://example.invalid/explorer?${query}${hash}`);
}

describe("Explorer public workspace navigation integration", () => {
  it("matches a validated public-safe deep link to the canonical workspace", () => {
    expect(
      resolvePublicWorkspaceNavigationState(contextUrl(knowledgeContext, "#knowledge")),
    ).toEqual({
      workspaceId: "knowledge",
      contextState: "PUBLIC_CONTEXT_MATCHED",
    });
  });

  it("fails closed on mismatched context while preserving ordinary anchor navigation", () => {
    expect(
      resolvePublicWorkspaceNavigationState(contextUrl(knowledgeContext, "#trust")),
    ).toEqual({
      workspaceId: "trust",
      contextState: "ANCHOR_ONLY",
    });
  });

  it("selects exactly one catalog-bounded public Knowledge domain", () => {
    const archaeologyContext = {
      ...knowledgeContext,
      domainIds: ["archaeology"],
    };
    const peopleDnaLandContext = {
      ...knowledgeContext,
      domainIds: ["people_dna_land"],
    };

    expect(
      resolveSinglePublicKnowledgeDomainId(
        contextUrl(archaeologyContext, "#knowledge"),
      ),
    ).toBe("archaeology");
    expect(
      resolveSinglePublicKnowledgeDomainId(
        contextUrl(peopleDnaLandContext, "#knowledge"),
      ),
    ).toBe("people_dna_land");
  });

  it("does not guess a primary domain when a public context names several", () => {
    const multiDomainContext = {
      ...knowledgeContext,
      domainIds: ["archaeology", "people_dna_land"],
    };

    expect(
      resolveSinglePublicKnowledgeDomainId(
        contextUrl(multiDomainContext, "#knowledge"),
      ),
    ).toBeNull();
  });

  it("restores only the existing evidence-free synthetic map abstention case", () => {
    const missingEvidenceContext = {
      ...knowledgeContext,
      workspaceId: "explore",
      domainIds: [],
      layerIds: ["layer:synthetic-streamflow"],
      selection: {
        profile: MAP_FEATURE_SELECTION_PROFILE,
        selectionId: "selection:missing",
        layerId: "layer:synthetic-streamflow",
        featureId: "feature:missing",
        evidenceRefs: [],
      },
    };
    const strippedSupportedContext = {
      ...missingEvidenceContext,
      selection: {
        ...missingEvidenceContext.selection,
        selectionId: "selection:supported",
        featureId: "feature:flow-001",
      },
    };

    expect(
      resolvePublicEvidenceFreeMapCaseId(
        contextUrl(missingEvidenceContext, "#map"),
      ),
    ).toBe("missing");
    expect(
      resolvePublicEvidenceFreeMapCaseId(
        contextUrl(strippedSupportedContext, "#map"),
      ),
    ).toBeNull();
  });

  it("scrubs a rejected context while preserving unrelated public URL state", () => {
    const mismatched = contextUrl(knowledgeContext, "#trust");
    mismatched.searchParams.set("lang", "en");

    const sanitized = sanitizePublicWorkspaceNavigationUrl(mismatched);

    expect(sanitized.searchParams.has(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM)).toBe(
      false,
    );
    expect(sanitized.searchParams.get("lang")).toBe("en");
    expect(sanitized.hash).toBe("#trust");
    expect(resolvePublicWorkspaceNavigationState(sanitized)).toEqual({
      workspaceId: "trust",
      contextState: "ANCHOR_ONLY",
    });
  });

  it("retains a validated public-safe context unchanged", () => {
    const valid = contextUrl(knowledgeContext, "#knowledge");
    valid.searchParams.set("lang", "en");

    const sanitized = sanitizePublicWorkspaceNavigationUrl(valid);

    expect(sanitized.toString()).toBe(valid.toString());
    expect(
      sanitized.searchParams.has(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM),
    ).toBe(true);
  });

  it("does not restore or retain evidence-bearing selections in a shareable URL", () => {
    const unsafeContext = {
      ...knowledgeContext,
      workspaceId: "explore",
      domainIds: [],
      layerIds: ["layer:synthetic-public"],
      selection: {
        profile: MAP_FEATURE_SELECTION_PROFILE,
        selectionId: "selection:synthetic-public",
        layerId: "layer:synthetic-public",
        featureId: "feature:synthetic-public",
        evidenceRefs: ["kfm:evidence:restricted-canary"],
      },
    };
    const params = new URLSearchParams();
    params.set(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM, JSON.stringify(unsafeContext));
    params.set("lang", "en");
    const url = new URL(`https://example.invalid/explorer?${params.toString()}#map`);

    expect(resolvePublicWorkspaceNavigationState(url)).toEqual({
      workspaceId: "explore",
      contextState: "ANCHOR_ONLY",
    });
    expect(resolveSinglePublicKnowledgeDomainId(url)).toBeNull();
    expect(resolvePublicEvidenceFreeMapCaseId(url)).toBeNull();

    const sanitized = sanitizePublicWorkspaceNavigationUrl(url);
    expect(sanitized.searchParams.has(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM)).toBe(
      false,
    );
    expect(sanitized.searchParams.get("lang")).toBe("en");
    expect(sanitized.hash).toBe("#map");
    expect(decodeURIComponent(sanitized.toString())).not.toContain(
      "kfm:evidence:restricted-canary",
    );
  });

  it("keeps URL synchronization bounded to navigation, safe abstention, and public domain state", () => {
    expect(navigationSource).toContain('link.setAttribute("aria-current", "page")');
    expect(navigationSource).toContain('link.removeAttribute("aria-current")');
    expect(navigationSource).toContain(
      "safeUrl.searchParams.delete(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM)",
    );
    expect(navigationSource).toContain(
      "resolveSinglePublicKnowledgeDomainId",
    );
    expect(navigationSource).toContain("resolvePublicEvidenceFreeMapCaseId");
    expect(navigationSource).toContain('selection.selectionId === "selection:missing"');
    expect(navigationSource).toContain("selection.evidenceRefs.length !== 0");
    expect(navigationSource).not.toContain("evidenceRefs.some");
    expect(mainSource).toContain("sanitizePublicWorkspaceNavigationUrl");
    expect(mainSource).toContain("window.history.replaceState");
    expect(mainSource).toContain("syncPublicWorkspaceNavigation");
    expect(mainSource).toContain("resolvePublicEvidenceFreeMapCaseId");
    expect(mainSource).toContain("data-map-evidence-case");
    expect(mainSource).toContain("mapCaseButton.click()");
    expect(mainSource).toContain("resolveSinglePublicKnowledgeDomainId");
    expect(mainSource).toContain(
      'querySelectorAll<HTMLButtonElement>("button[data-domain-id]")',
    );
    expect(mainSource).toContain("domainButton.click()");
    expect(mainSource).toContain('window.addEventListener("hashchange"');
    expect(mainSource).toContain('window.addEventListener("popstate"');
    expect(navigationCss).toContain('.site-nav a[aria-current="page"]');
  });
});
