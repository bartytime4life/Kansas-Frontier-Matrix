import { describe, expect, it } from "vitest";
import { MAP_FEATURE_SELECTION_PROFILE } from "@kfm/maplibre";
import {
  buildTemporalViewStateFromPublicContext,
  PUBLIC_WORKSPACE_CONTEXT_PROFILE,
  PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM,
  parsePublicWorkspaceContext,
  parsePublicWorkspaceContextQuery,
  parsePublicWorkspaceContextUrl,
  serializePublicWorkspaceContext,
  withPublicWorkspaceContext,
  type PublicWorkspaceContext,
} from "../src/site/workspace-context";

const validContext = Object.freeze({
  profile: PUBLIC_WORKSPACE_CONTEXT_PROFILE,
  workspaceId: "explore",
  domainIds: Object.freeze(["hydrology", "soil"]),
  placeIds: Object.freeze(["place:ks:ellsworth"]),
  layerIds: Object.freeze(["layer:synthetic-streamflow"]),
  camera: Object.freeze({
    longitude: -98.58,
    latitude: 38.5,
    zoom: 6,
    bearing: 0,
    pitch: 0,
  }),
  selection: Object.freeze({
    profile: MAP_FEATURE_SELECTION_PROFILE,
    selectionId: "selection:flow-001",
    layerId: "layer:synthetic-streamflow",
    featureId: "feature:flow-001",
    evidenceRefs: Object.freeze(["kfm:evidence:synthetic:flow-001"]),
  }),
  time: Object.freeze({
    validAt: "2026-08-23",
    observedAt: "2026-08-23T16:00:00Z",
    asOf: "2026-08-23T16:30:00-05:00",
    releaseId: "release:fixture:ui-01",
  }),
  compare: Object.freeze({
    mode: "NONE",
    leftContextId: null,
    rightContextId: null,
  }),
  storyNodeId: null,
  publicSafe: true,
});

const urlSafeContext = Object.freeze({
  ...validContext,
  selection: Object.freeze({
    ...validContext.selection,
    evidenceRefs: Object.freeze([]),
  }),
});

describe("Explorer public workspace context", () => {
  it("strictly parses and deeply freezes a public-safe context", () => {
    const parsed = parsePublicWorkspaceContext(validContext);
    expect(parsed).not.toBeNull();
    expect(Object.isFrozen(parsed)).toBe(true);
    expect(Object.isFrozen(parsed?.domainIds)).toBe(true);
    expect(Object.isFrozen(parsed?.camera)).toBe(true);
    expect(Object.isFrozen(parsed?.selection?.evidenceRefs)).toBe(true);
  });

  it("round-trips deterministically through a shareable URL and preserves unrelated parameters", () => {
    const first = serializePublicWorkspaceContext(urlSafeContext);
    const second = serializePublicWorkspaceContext(urlSafeContext);
    expect(first).not.toBeNull();
    expect(first).toBe(second);
    expect(parsePublicWorkspaceContextQuery(first ?? "")).toEqual(
      parsePublicWorkspaceContext(urlSafeContext),
    );

    const url = withPublicWorkspaceContext(
      new URL("https://example.test/explorer?lang=en#top"),
      urlSafeContext,
    );
    expect(url).not.toBeNull();
    expect(url?.searchParams.get("lang")).toBe("en");
    expect(url?.searchParams.has(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM)).toBe(
      true,
    );
    expect(url?.hash).toBe("#map");
    expect(url ? parsePublicWorkspaceContextUrl(url) : null).toEqual(
      parsePublicWorkspaceContext(urlSafeContext),
    );
  });

  it("rejects evidence identifiers at every public URL boundary", () => {
    expect(parsePublicWorkspaceContext(validContext)).not.toBeNull();
    expect(serializePublicWorkspaceContext(validContext)).toBeNull();
    expect(
      withPublicWorkspaceContext(
        new URL("https://example.test/explorer"),
        validContext,
      ),
    ).toBeNull();

    const params = new URLSearchParams();
    params.set(
      PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM,
      JSON.stringify(validContext),
    );
    expect(parsePublicWorkspaceContextQuery(params)).toBeNull();

    const historyOnlyContext = {
      ...urlSafeContext,
      selection: {
        ...urlSafeContext.selection,
        historyEvidenceRefs: ["kfm:evidence:private:history-canary-4a72"],
      },
    };
    expect(parsePublicWorkspaceContext(historyOnlyContext)).not.toBeNull();
    expect(serializePublicWorkspaceContext(historyOnlyContext)).toBeNull();
    expect(
      withPublicWorkspaceContext(
        new URL("https://example.test/explorer"),
        historyOnlyContext,
      ),
    ).toBeNull();

    const historyParams = new URLSearchParams();
    historyParams.set(
      PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM,
      JSON.stringify(historyOnlyContext),
    );
    expect(historyParams.toString()).toContain("history-canary-4a72");
    expect(parsePublicWorkspaceContextQuery(historyParams)).toBeNull();
  });

  it("rejects extra, private, or internally inconsistent fields", () => {
    expect(
      parsePublicWorkspaceContext({ ...validContext, prompt: "private text" }),
    ).toBeNull();
    expect(
      parsePublicWorkspaceContext({ ...validContext, publicSafe: false }),
    ).toBeNull();
    expect(
      parsePublicWorkspaceContext({
        ...validContext,
        domainIds: ["unknown_domain"],
      }),
    ).toBeNull();
    expect(
      parsePublicWorkspaceContext({
        ...validContext,
        camera: { ...validContext.camera, latitude: 90 },
      }),
    ).toBeNull();
    expect(
      parsePublicWorkspaceContext({
        ...validContext,
        layerIds: ["layer:different"],
      }),
    ).toBeNull();
    expect(
      parsePublicWorkspaceContext({
        ...validContext,
        time: { ...validContext.time, validAt: "not-a-time" },
      }),
    ).toBeNull();
  });

  it("rejects malformed, duplicated, oversized, or hash-mismatched deep links", () => {
    expect(
      parsePublicWorkspaceContextQuery(
        `${PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM}=%7Bbroken`,
      ),
    ).toBeNull();

    const encoded = serializePublicWorkspaceContext(urlSafeContext);
    expect(encoded).not.toBeNull();
    const duplicated = new URLSearchParams(encoded ?? "");
    duplicated.append(
      PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM,
      JSON.stringify(urlSafeContext),
    );
    expect(parsePublicWorkspaceContextQuery(duplicated)).toBeNull();

    const oversized = new URLSearchParams();
    oversized.set(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM, "x".repeat(8193));
    expect(parsePublicWorkspaceContextQuery(oversized)).toBeNull();

    const mismatched = withPublicWorkspaceContext(
      new URL("https://example.test/explorer"),
      urlSafeContext,
    );
    expect(mismatched).not.toBeNull();
    if (mismatched) mismatched.hash = "#trust";
    expect(mismatched ? parsePublicWorkspaceContextUrl(mismatched) : null).toBeNull();
  });

  it("requires complete, distinct compare references outside NONE mode", () => {
    expect(
      parsePublicWorkspaceContext({
        ...validContext,
        compare: {
          mode: "SIDE_BY_SIDE",
          leftContextId: "context:left",
          rightContextId: "context:right",
        },
      })?.compare.mode,
    ).toBe("SIDE_BY_SIDE");
    expect(
      parsePublicWorkspaceContext({
        ...validContext,
        compare: {
          mode: "SIDE_BY_SIDE",
          leftContextId: "context:same",
          rightContextId: "context:same",
        },
      }),
    ).toBeNull();
  });
  it("normalizes explicit numeric-offset instants while preserving the raw value", async () => {
    const context = parsePublicWorkspaceContext({
      ...validContext,
      time: {
        ...validContext.time,
        validAt: null,
        observedAt: "2026-08-23T16:00:00-05:00",
      },
    });
    expect(context).not.toBeNull();
    const result = await buildTemporalViewStateFromPublicContext(
      context as PublicWorkspaceContext,
    );
    expect(result).toMatchObject({ status: "SUPPORTED", code: "OK" });
    expect(result.state?.selection.start).toMatchObject({
      raw: "2026-08-23T16:00:00-05:00",
      normalized: "2026-08-23T21:00:00Z",
      source_timezone: "-05:00",
      normalization: { status: "OFFSET_TO_UTC" },
    });
  });

  it("rejects an unparsed context instead of fabricating an uncertain range", async () => {
    const forged = {
      ...validContext,
      time: {
        ...validContext.time,
        validAt: "circa 1880",
        observedAt: null,
      },
    } as unknown as PublicWorkspaceContext;
    await expect(buildTemporalViewStateFromPublicContext(forged)).resolves.toMatchObject({
      status: "ERROR",
      code: "PUBLIC_CONTEXT_INVALID",
      state: null,
    });
  });

});
