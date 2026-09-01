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
  resolvePublicWorkspaceNavigationState,
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

  it("keeps URL synchronization bounded to navigation state", () => {
    expect(navigationSource).toContain('link.setAttribute("aria-current", "page")');
    expect(navigationSource).toContain('link.removeAttribute("aria-current")');
    expect(navigationSource).toContain(
      "safeUrl.searchParams.delete(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM)",
    );
    expect(navigationSource).not.toContain("evidenceRefs.some");
    expect(mainSource).toContain("sanitizePublicWorkspaceNavigationUrl");
    expect(mainSource).toContain("window.history.replaceState");
    expect(mainSource).toContain("syncPublicWorkspaceNavigation");
    expect(mainSource).toContain('window.addEventListener("hashchange"');
    expect(mainSource).toContain('window.addEventListener("popstate"');
    expect(navigationCss).toContain('.site-nav a[aria-current="page"]');
  });
});
