import { describe, expect, it, vi } from "vitest";

import {
  MAP_FEATURE_SELECTION_PROFILE,
  MAP_RUNTIME_INLINE_GEOJSON_LAYER_PROFILE,
  MapRuntimePortError,
  createNullMapRuntime,
  freezeMapRuntimeInlineGeoJsonLayer,
  isMapRuntimeInlineGeoJsonLayer,
  type MapRuntimeInlineGeoJsonLayer,
} from "../src/index";

function inlineLayer(
  evidenceRef = "kfm:evidence:synthetic:flow-001",
): MapRuntimeInlineGeoJsonLayer {
  return {
    profile: MAP_RUNTIME_INLINE_GEOJSON_LAYER_PROFILE,
    sourceId: "source:synthetic-streamflow",
    layerId: "layer:synthetic-streamflow",
    kind: "circle",
    data: {
      type: "FeatureCollection",
      features: [
        {
          type: "Feature",
          id: "feature:flow-001",
          geometry: { type: "Point", coordinates: [-98.5, 38.5] },
          properties: null,
        },
      ],
    },
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selectionId: "selection:flow-001",
      layerId: "layer:synthetic-streamflow",
      featureId: "feature:flow-001",
      evidenceRefs: [evidenceRef],
    },
  };
}

describe("bounded inline GeoJSON map runtime capability", () => {
  it("strictly validates and deeply freezes the exact one-point profile", () => {
    const candidate = inlineLayer();
    expect(isMapRuntimeInlineGeoJsonLayer(candidate)).toBe(true);

    const frozen = freezeMapRuntimeInlineGeoJsonLayer(candidate);
    expect(frozen).toEqual(candidate);
    expect(Object.isFrozen(frozen)).toBe(true);
    expect(Object.isFrozen(frozen.data)).toBe(true);
    expect(Object.isFrozen(frozen.data.features)).toBe(true);
    expect(Object.isFrozen(frozen.data.features[0])).toBe(true);
    expect(Object.isFrozen(frozen.data.features[0].geometry)).toBe(true);
    expect(Object.isFrozen(frozen.data.features[0].geometry.coordinates)).toBe(true);
    expect(Object.isFrozen(frozen.selection.evidenceRefs)).toBe(true);
  });

  it.each([
    ["extra root field", { ...inlineLayer(), extra: true }],
    ["prototype-collision source ID", { ...inlineLayer(), sourceId: "constructor" }],
    ["prototype-collision layer ID", { ...inlineLayer(), layerId: "__proto__" }],
    [
      "more than one feature",
      {
        ...inlineLayer(),
        data: {
          ...inlineLayer().data,
          features: [
            inlineLayer().data.features[0],
            inlineLayer().data.features[0],
          ],
        },
      },
    ],
    [
      "non-point geometry",
      {
        ...inlineLayer(),
        data: {
          type: "FeatureCollection",
          features: [
            {
              ...inlineLayer().data.features[0],
              geometry: { type: "LineString", coordinates: [] },
            },
          ],
        },
      },
    ],
    [
      "non-finite coordinate",
      {
        ...inlineLayer(),
        data: {
          type: "FeatureCollection",
          features: [
            {
              ...inlineLayer().data.features[0],
              geometry: { type: "Point", coordinates: [Number.NaN, 38.5] },
            },
          ],
        },
      },
    ],
    [
      "out-of-range coordinate",
      {
        ...inlineLayer(),
        data: {
          type: "FeatureCollection",
          features: [
            {
              ...inlineLayer().data.features[0],
              geometry: { type: "Point", coordinates: [-98.5, 90] },
            },
          ],
        },
      },
    ],
    [
      "renderer properties",
      {
        ...inlineLayer(),
        data: {
          type: "FeatureCollection",
          features: [
            { ...inlineLayer().data.features[0], properties: { evidence: "forged" } },
          ],
        },
      },
    ],
    [
      "selection feature mismatch",
      {
        ...inlineLayer(),
        selection: { ...inlineLayer().selection, featureId: "feature:other" },
      },
    ],
    [
      "selection layer mismatch",
      {
        ...inlineLayer(),
        selection: { ...inlineLayer().selection, layerId: "layer:other" },
      },
    ],
  ])("rejects %s before binding", (_label, candidate) => {
    expect(isMapRuntimeInlineGeoJsonLayer(candidate)).toBe(false);
    expect(() =>
      freezeMapRuntimeInlineGeoJsonLayer(
        candidate as unknown as MapRuntimeInlineGeoJsonLayer,
      ),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_LAYER_INVALID" }));
  });

  it("gives accessible selection the same stable KFM-owned identity", async () => {
    const runtime = createNullMapRuntime();
    const selectionListener = vi.fn();
    await runtime.initialize();
    runtime.subscribeSelection(selectionListener);
    runtime.subscribeSnapshot((snapshot) => {
      if (snapshot.selection !== null) throw new Error("synthetic snapshot listener");
    });
    runtime.subscribeSelection(() => {
      throw new Error("synthetic selection listener");
    });
    runtime.bindInlineGeoJsonLayer(inlineLayer());

    expect(() =>
      runtime.selectFeature(
        "layer:synthetic-streamflow",
        "feature:flow-001",
      ),
    ).not.toThrow();

    expect(runtime.getSnapshot()).toMatchObject({
      state: "READY",
      reason: null,
      selection: inlineLayer().selection,
    });
    expect(selectionListener).toHaveBeenCalledExactlyOnceWith(
      expect.objectContaining(inlineLayer().selection),
    );
  });

  it("invalidates selection on layer removal, source removal, and replacement", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    runtime.bindInlineGeoJsonLayer(inlineLayer());
    runtime.selectFeature("layer:synthetic-streamflow", "feature:flow-001");

    expect(runtime.removeLayer("layer:synthetic-streamflow")).toMatchObject({
      state: "READY",
      selection: null,
      reason: "MAP_RUNTIME_SELECTION_INVALIDATED",
    });
    expect(() =>
      runtime.selectFeature("layer:synthetic-streamflow", "feature:flow-001"),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_LAYER_NOT_FOUND" }));
    expect(runtime.removeSource("source:synthetic-streamflow")).toMatchObject({
      state: "READY",
      selection: null,
      reason: null,
    });

    runtime.bindInlineGeoJsonLayer(inlineLayer());
    runtime.selectFeature("layer:synthetic-streamflow", "feature:flow-001");
    expect(runtime.removeSource("source:synthetic-streamflow")).toMatchObject({
      selection: null,
      reason: "MAP_RUNTIME_SELECTION_INVALIDATED",
    });

    runtime.bindInlineGeoJsonLayer(inlineLayer());
    runtime.selectFeature("layer:synthetic-streamflow", "feature:flow-001");
    expect(
      runtime.bindInlineGeoJsonLayer(
        inlineLayer("kfm:evidence:synthetic:flow-002"),
      ),
    ).toMatchObject({
      selection: null,
      reason: "MAP_RUNTIME_SELECTION_INVALIDATED",
    });
    expect(
      runtime.selectFeature("layer:synthetic-streamflow", "feature:flow-001")
        .selection?.evidenceRefs,
    ).toEqual(["kfm:evidence:synthetic:flow-002"]);
  });

  it("does not resurrect initialization after an observer disposes then throws", async () => {
    const runtime = createNullMapRuntime();
    runtime.subscribeSnapshot((snapshot) => {
      if (snapshot.state !== "INITIALIZING") return;
      runtime.dispose();
      throw new Error("synthetic initialization observer failure after disposal");
    });

    await expect(runtime.initialize()).rejects.toMatchObject({
      code: "MAP_RUNTIME_DISPOSED",
    });
    expect(runtime.getSnapshot()).toMatchObject({
      state: "DISPOSED",
      selection: null,
      reason: "MAP_RUNTIME_DISPOSED",
    });
  });

  it("returns the post-callback state when bind observers throw and dispose", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    const throwingObserver = vi.fn(() => {
      throw new Error("synthetic bind observer failure");
    });
    const trailingObserver = vi.fn();
    runtime.subscribeSnapshot(throwingObserver);
    runtime.subscribeSnapshot(() => runtime.dispose());
    runtime.subscribeSnapshot(trailingObserver);

    expect(runtime.bindInlineGeoJsonLayer(inlineLayer())).toMatchObject({
      state: "DISPOSED",
      selection: null,
      reason: "MAP_RUNTIME_DISPOSED",
    });
    expect(
      throwingObserver.mock.calls.map(([snapshot]) => snapshot.state),
    ).toEqual(["READY", "DISPOSED"]);
    expect(
      trailingObserver.mock.calls.map(([snapshot]) => snapshot.state),
    ).toEqual(["DISPOSED"]);
  });

  it("returns the post-callback state when removal observers throw and dispose", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    runtime.bindInlineGeoJsonLayer(inlineLayer());
    const throwingObserver = vi.fn(() => {
      throw new Error("synthetic removal observer failure");
    });
    const trailingObserver = vi.fn();
    runtime.subscribeSnapshot(throwingObserver);
    runtime.subscribeSnapshot(() => runtime.dispose());
    runtime.subscribeSnapshot(trailingObserver);

    expect(runtime.removeLayer("layer:synthetic-streamflow")).toMatchObject({
      state: "DISPOSED",
      selection: null,
      reason: "MAP_RUNTIME_DISPOSED",
    });
    expect(
      throwingObserver.mock.calls.map(([snapshot]) => snapshot.state),
    ).toEqual(["READY", "DISPOSED"]);
    expect(
      trailingObserver.mock.calls.map(([snapshot]) => snapshot.state),
    ).toEqual(["DISPOSED"]);
  });

  it("stops selection fanout when a publish observer disposes then throws", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    runtime.bindInlineGeoJsonLayer(inlineLayer());
    const selectionObserver = vi.fn();
    runtime.subscribeSnapshot((snapshot) => {
      if (snapshot.selection === null) return;
      runtime.dispose();
      throw new Error("synthetic publish observer failure after disposal");
    });
    runtime.subscribeSelection(selectionObserver);

    expect(
      runtime.selectFeature("layer:synthetic-streamflow", "feature:flow-001"),
    ).toMatchObject({
      state: "DISPOSED",
      selection: null,
      reason: "MAP_RUNTIME_DISPOSED",
    });
    expect(selectionObserver).not.toHaveBeenCalled();
  });

  it("keeps missing operations finite and disposes all bounded state", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    runtime.bindInlineGeoJsonLayer(inlineLayer());

    expect(() => runtime.removeLayer("layer:other")).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_LAYER_NOT_FOUND" }),
    );
    expect(() => runtime.removeSource("source:other")).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_SOURCE_NOT_FOUND" }),
    );
    expect(() =>
      runtime.selectFeature("layer:synthetic-streamflow", "feature:other"),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_FEATURE_NOT_FOUND" }));

    runtime.subscribeSnapshot((snapshot) => {
      if (snapshot.state === "DISPOSED") {
        throw new Error("synthetic disposal listener failure");
      }
    });
    expect(() => runtime.dispose()).not.toThrow();
    runtime.dispose();
    expect(runtime.getSnapshot()).toMatchObject({
      state: "DISPOSED",
      selection: null,
      reason: "MAP_RUNTIME_DISPOSED",
    });
    expect(() => runtime.bindInlineGeoJsonLayer(inlineLayer())).toThrow(
      MapRuntimePortError,
    );
  });
});
