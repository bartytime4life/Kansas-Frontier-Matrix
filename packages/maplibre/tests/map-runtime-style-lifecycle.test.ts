import { describe, expect, it } from "vitest";

import {
  MAP_RUNTIME_STYLE_LAYER_PROFILE,
  MAP_RUNTIME_STYLE_PLAN_PROFILE,
  MAP_RUNTIME_STYLE_PROFILE,
  MAP_RUNTIME_STYLE_SOURCE_PROFILE,
  freezeMapRuntimeStyleState,
  planMapRuntimeStyleLifecycle,
  type MapRuntimeStyleState,
} from "../src/map-runtime-style-lifecycle";

function style(
  sources: readonly [sourceId: string, revision: string][],
  layers: readonly [layerId: string, sourceId: string, revision?: string][],
): MapRuntimeStyleState {
  return {
    profile: MAP_RUNTIME_STYLE_PROFILE,
    sources: sources.map(([sourceId, revision]) => ({
      profile: MAP_RUNTIME_STYLE_SOURCE_PROFILE,
      sourceId,
      revision,
    })),
    layers: layers.map(([layerId, sourceId, revision = "v1"], order) => ({
      profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
      layerId,
      sourceId,
      revision,
      order,
    })),
  };
}

describe("renderer-neutral source and layer lifecycle", () => {
  it("adds canonical sources before bottom-up layers", () => {
    const target = style(
      [
        ["roads", "v1"],
        ["places", "v3"],
      ],
      [
        ["roads-line", "roads"],
        ["places-label", "places"],
      ],
    );

    expect(planMapRuntimeStyleLifecycle(null, target)).toEqual({
      profile: MAP_RUNTIME_STYLE_PLAN_PROFILE,
      current: style([], []),
      target: freezeMapRuntimeStyleState(target),
      actions: [
        {
          effect: "ADD_SOURCE",
          source: {
            profile: MAP_RUNTIME_STYLE_SOURCE_PROFILE,
            sourceId: "places",
            revision: "v3",
          },
        },
        {
          effect: "ADD_SOURCE",
          source: {
            profile: MAP_RUNTIME_STYLE_SOURCE_PROFILE,
            sourceId: "roads",
            revision: "v1",
          },
        },
        {
          effect: "ADD_LAYER",
          layer: {
            profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
            layerId: "roads-line",
            sourceId: "roads",
            revision: "v1",
            order: 0,
          },
        },
        {
          effect: "ADD_LAYER",
          layer: {
            profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
            layerId: "places-label",
            sourceId: "places",
            revision: "v1",
            order: 1,
          },
        },
      ],
    });
  });

  it("removes top-down layers before their sources", () => {
    const current = style(
      [
        ["roads", "v1"],
        ["places", "v3"],
      ],
      [
        ["roads-line", "roads"],
        ["places-label", "places"],
      ],
    );

    expect(planMapRuntimeStyleLifecycle(current, style([], [])).actions).toEqual([
      { effect: "REMOVE_LAYER", layerId: "places-label" },
      { effect: "REMOVE_LAYER", layerId: "roads-line" },
      { effect: "REMOVE_SOURCE", sourceId: "places" },
      { effect: "REMOVE_SOURCE", sourceId: "roads" },
    ]);
  });

  it("rebuilds dependent layers around a source revision change", () => {
    const current = style(
      [["terrain", "2026-08"]],
      [
        ["hillshade", "terrain"],
        ["contours", "terrain"],
      ],
    );
    const target = style(
      [["terrain", "2026-09"]],
      [
        ["hillshade", "terrain"],
        ["contours", "terrain"],
      ],
    );

    expect(planMapRuntimeStyleLifecycle(current, target).actions).toEqual([
      { effect: "REMOVE_LAYER", layerId: "contours" },
      { effect: "REMOVE_LAYER", layerId: "hillshade" },
      { effect: "REMOVE_SOURCE", sourceId: "terrain" },
      {
        effect: "ADD_SOURCE",
        source: {
          profile: MAP_RUNTIME_STYLE_SOURCE_PROFILE,
          sourceId: "terrain",
          revision: "2026-09",
        },
      },
      {
        effect: "ADD_LAYER",
        layer: {
          profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
          layerId: "hillshade",
          sourceId: "terrain",
          revision: "v1",
          order: 0,
        },
      },
      {
        effect: "ADD_LAYER",
        layer: {
          profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
          layerId: "contours",
          sourceId: "terrain",
          revision: "v1",
          order: 1,
        },
      },
    ]);
  });

  it("rebuilds reordered layers without churning their source", () => {
    const current = style(
      [["boundaries", "v1"]],
      [
        ["county-fill", "boundaries"],
        ["county-line", "boundaries"],
      ],
    );
    const target = style(
      [["boundaries", "v1"]],
      [
        ["county-line", "boundaries"],
        ["county-fill", "boundaries"],
      ],
    );

    expect(planMapRuntimeStyleLifecycle(current, target).actions).toEqual([
      { effect: "REMOVE_LAYER", layerId: "county-line" },
      { effect: "REMOVE_LAYER", layerId: "county-fill" },
      {
        effect: "ADD_LAYER",
        layer: {
          profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
          layerId: "county-line",
          sourceId: "boundaries",
          revision: "v1",
          order: 0,
        },
      },
      {
        effect: "ADD_LAYER",
        layer: {
          profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
          layerId: "county-fill",
          sourceId: "boundaries",
          revision: "v1",
          order: 1,
        },
      },
    ]);
  });

  it("rebuilds a changed lower layer and every higher layer", () => {
    const current = style(
      [
        ["lower-source", "v1"],
        ["higher-source", "v1"],
      ],
      [
        ["lower-layer", "lower-source", "paint-v1"],
        ["higher-layer", "higher-source", "paint-v1"],
      ],
    );
    const target = style(
      [
        ["lower-source", "v1"],
        ["higher-source", "v1"],
      ],
      [
        ["lower-layer", "lower-source", "paint-v2"],
        ["higher-layer", "higher-source", "paint-v1"],
      ],
    );

    expect(planMapRuntimeStyleLifecycle(current, target).actions).toEqual([
      { effect: "REMOVE_LAYER", layerId: "higher-layer" },
      { effect: "REMOVE_LAYER", layerId: "lower-layer" },
      {
        effect: "ADD_LAYER",
        layer: {
          profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
          layerId: "lower-layer",
          sourceId: "lower-source",
          revision: "paint-v2",
          order: 0,
        },
      },
      {
        effect: "ADD_LAYER",
        layer: {
          profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
          layerId: "higher-layer",
          sourceId: "higher-source",
          revision: "paint-v1",
          order: 1,
        },
      },
    ]);
  });

  it("is immutable and idempotent for an equivalent canonical state", () => {
    const current = style(
      [
        ["zoning", "v2"],
        ["roads", "v1"],
      ],
      [["roads-line", "roads"]],
    );
    const plan = planMapRuntimeStyleLifecycle(current, current);

    expect(plan.actions).toEqual([]);
    expect(plan.target.sources.map(({ sourceId }) => sourceId)).toEqual([
      "roads",
      "zoning",
    ]);
    expect(Object.isFrozen(plan)).toBe(true);
    expect(Object.isFrozen(plan.actions)).toBe(true);
    expect(Object.isFrozen(plan.target)).toBe(true);
    expect(Object.isFrozen(plan.target.sources[0])).toBe(true);
  });

  it.each([
    {
      ...style([["roads", "v1"]], []),
      extra: true,
    },
    style(
      [
        ["roads", "v1"],
        ["roads", "v2"],
      ],
      [],
    ),
    style([["roads", "v1"]], [["road-line", "missing"]]),
    {
      ...style([["roads", "v1"]], [["road-line", "roads"]]),
      layers: [
        {
          profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
          layerId: "road-line",
          sourceId: "roads",
          revision: "v1",
          order: 1,
        },
      ],
    },
    style([["unsafe/id", "v1"]], []),
    {
      profile: MAP_RUNTIME_STYLE_PROFILE,
      sources: new Array(1),
      layers: [],
    },
    {
      profile: MAP_RUNTIME_STYLE_PROFILE,
      sources: [
        {
          profile: MAP_RUNTIME_STYLE_SOURCE_PROFILE,
          sourceId: "roads",
          revision: "v1",
        },
      ],
      layers: new Array(1),
    },
  ])("fails closed for malformed lifecycle state", (candidate) => {
    expect(() => freezeMapRuntimeStyleState(candidate as never)).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }),
    );
  });
});
