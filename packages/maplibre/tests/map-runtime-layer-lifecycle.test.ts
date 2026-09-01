import { describe, expect, it } from "vitest";

import {
  MAP_RUNTIME_LAYER_LIFECYCLE_PROFILE,
  applyMapRuntimeLayerLifecyclePlan,
  createEmptyMapRuntimeLayerLifecycleState,
} from "../src/map-runtime-layer-lifecycle";

describe("renderer-neutral source/layer lifecycle planning", () => {
  it("creates a deeply frozen empty state", () => {
    const state = createEmptyMapRuntimeLayerLifecycleState();

    expect(state).toEqual({
      profile: MAP_RUNTIME_LAYER_LIFECYCLE_PROFILE,
      sources: [],
      layers: [],
    });
    expect(Object.isFrozen(state)).toBe(true);
    expect(Object.isFrozen(state.sources)).toBe(true);
    expect(Object.isFrozen(state.layers)).toBe(true);
  });

  it("applies an ordered source, layer, and visibility plan", () => {
    const result = applyMapRuntimeLayerLifecyclePlan(
      createEmptyMapRuntimeLayerLifecycleState(),
      [
        { op: "ATTACH_SOURCE", sourceId: "source:synthetic-a" },
        {
          op: "ATTACH_LAYER",
          layerId: "layer:synthetic-a",
          sourceId: "source:synthetic-a",
          visibility: "HIDDEN",
        },
        {
          op: "SET_LAYER_VISIBILITY",
          layerId: "layer:synthetic-a",
          visibility: "VISIBLE",
        },
      ],
    );

    expect(result).toEqual({
      profile: MAP_RUNTIME_LAYER_LIFECYCLE_PROFILE,
      sources: ["source:synthetic-a"],
      layers: [
        {
          layerId: "layer:synthetic-a",
          sourceId: "source:synthetic-a",
          visibility: "VISIBLE",
        },
      ],
    });
    expect(Object.isFrozen(result.layers[0])).toBe(true);
  });

  it("canonicalizes independent sources and layers by ID", () => {
    const first = applyMapRuntimeLayerLifecyclePlan(
      createEmptyMapRuntimeLayerLifecycleState(),
      [
        { op: "ATTACH_SOURCE", sourceId: "source:z" },
        { op: "ATTACH_SOURCE", sourceId: "source:a" },
        {
          op: "ATTACH_LAYER",
          layerId: "layer:z",
          sourceId: "source:z",
          visibility: "VISIBLE",
        },
        {
          op: "ATTACH_LAYER",
          layerId: "layer:a",
          sourceId: "source:a",
          visibility: "HIDDEN",
        },
      ],
    );
    const second = applyMapRuntimeLayerLifecyclePlan(
      createEmptyMapRuntimeLayerLifecycleState(),
      [
        { op: "ATTACH_SOURCE", sourceId: "source:a" },
        { op: "ATTACH_SOURCE", sourceId: "source:z" },
        {
          op: "ATTACH_LAYER",
          layerId: "layer:a",
          sourceId: "source:a",
          visibility: "HIDDEN",
        },
        {
          op: "ATTACH_LAYER",
          layerId: "layer:z",
          sourceId: "source:z",
          visibility: "VISIBLE",
        },
      ],
    );

    expect(first).toEqual(second);
  });

  it("rejects a layer before its source is attached", () => {
    expect(() =>
      applyMapRuntimeLayerLifecyclePlan(
        createEmptyMapRuntimeLayerLifecycleState(),
        [
          {
            op: "ATTACH_LAYER",
            layerId: "layer:orphan",
            sourceId: "source:missing",
            visibility: "VISIBLE",
          },
        ],
      ),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));
  });

  it("prevents source removal while a dependent layer remains", () => {
    const state = applyMapRuntimeLayerLifecyclePlan(
      createEmptyMapRuntimeLayerLifecycleState(),
      [
        { op: "ATTACH_SOURCE", sourceId: "source:synthetic" },
        {
          op: "ATTACH_LAYER",
          layerId: "layer:synthetic",
          sourceId: "source:synthetic",
          visibility: "VISIBLE",
        },
      ],
    );

    expect(() =>
      applyMapRuntimeLayerLifecyclePlan(state, [
        { op: "DETACH_SOURCE", sourceId: "source:synthetic" },
      ]),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));

    expect(
      applyMapRuntimeLayerLifecyclePlan(state, [
        { op: "DETACH_LAYER", layerId: "layer:synthetic" },
        { op: "DETACH_SOURCE", sourceId: "source:synthetic" },
      ]),
    ).toEqual(createEmptyMapRuntimeLayerLifecycleState());
  });

  it.each([
    [],
    [{ op: "ATTACH_SOURCE", sourceId: "source:a", extra: true }],
    [{ op: "ATTACH_SOURCE", sourceId: " unsafe " }],
    [{ op: "UNKNOWN", sourceId: "source:a" }],
  ])("rejects malformed plans fail-closed", (plan) => {
    expect(() =>
      applyMapRuntimeLayerLifecyclePlan(
        createEmptyMapRuntimeLayerLifecycleState(),
        plan as never,
      ),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));
  });

  it.each([
    {
      profile: MAP_RUNTIME_LAYER_LIFECYCLE_PROFILE,
      sources: new Array(1),
      layers: [],
    },
    {
      profile: MAP_RUNTIME_LAYER_LIFECYCLE_PROFILE,
      sources: ["source:synthetic"],
      layers: new Array(1),
    },
  ])("rejects sparse lifecycle state arrays", (state) => {
    expect(() =>
      applyMapRuntimeLayerLifecyclePlan(state as never, [
        { op: "ATTACH_SOURCE", sourceId: "source:next" },
      ]),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));
  });

  it("rejects sparse operation arrays", () => {
    expect(() =>
      applyMapRuntimeLayerLifecyclePlan(
        createEmptyMapRuntimeLayerLifecycleState(),
        new Array(1) as never,
      ),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));
  });

  it("does not mutate the prior state when a later operation fails", () => {
    const prior = applyMapRuntimeLayerLifecyclePlan(
      createEmptyMapRuntimeLayerLifecycleState(),
      [{ op: "ATTACH_SOURCE", sourceId: "source:stable" }],
    );

    expect(() =>
      applyMapRuntimeLayerLifecyclePlan(prior, [
        { op: "ATTACH_SOURCE", sourceId: "source:temporary" },
        { op: "ATTACH_SOURCE", sourceId: "source:stable" },
      ]),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));
    expect(prior.sources).toEqual(["source:stable"]);
  });
});
