import { describe, expect, it } from "vitest";
import { FEATURE_CATALOG } from "../src/site/catalog";
import {
  PUBLIC_WORKSPACES,
  findPublicWorkspace,
  findPublicWorkspaceByHash,
} from "../src/site/workspace-registry";

describe("Explorer public workspace registry", () => {
  it("preserves the existing public anchor navigation in a code-owned registry", () => {
    expect(PUBLIC_WORKSPACES.map((entry) => entry.id)).toEqual([
      "explore",
      "knowledge",
      "features",
      "trust",
    ]);
    expect(PUBLIC_WORKSPACES.map((entry) => entry.href)).toEqual([
      "#map",
      "#knowledge",
      "#features",
      "#trust",
    ]);
    expect(new Set(PUBLIC_WORKSPACES.map((entry) => entry.sectionId)).size).toBe(
      PUBLIC_WORKSPACES.length,
    );
  });

  it("registers only public, non-privileged descriptors", () => {
    expect(
      PUBLIC_WORKSPACES.every(
        (entry) => entry.publicSafe === true && entry.privileged === false,
      ),
    ).toBe(true);
  });

  it("resolves every registered feature to the current Explorer catalog", () => {
    const catalogIds = new Set(FEATURE_CATALOG.map((entry) => entry.id));
    expect(
      PUBLIC_WORKSPACES.every((workspace) =>
        workspace.featureIds.every((featureId) => catalogIds.has(featureId)),
      ),
    ).toBe(true);
    expect(findPublicWorkspace("features")?.featureIds).toHaveLength(
      FEATURE_CATALOG.length,
    );
  });

  it("resolves workspace IDs and compatibility hashes without inventing routes", () => {
    expect(findPublicWorkspace("explore")?.sectionId).toBe("map");
    expect(findPublicWorkspace("review")).toBeNull();
    expect(findPublicWorkspaceByHash("#knowledge")?.id).toBe("knowledge");
    expect(findPublicWorkspaceByHash("%6d%61%70")?.id).toBe("explore");
    expect(findPublicWorkspaceByHash("#admin")).toBeNull();
    expect(findPublicWorkspaceByHash("%E0%A4%A")).toBeNull();
  });
});
