import { describe, expect, it, vi } from "vitest";
import {
  MAP_FEATURE_SELECTION_PROFILE,
  MAP_RUNTIME_PORT_PROFILE,
  MapRuntimePortError,
  createNullMapRuntime,
  isMapFeatureSelection,
  isMapRuntimeCamera,
  type MapFeatureSelection,
} from "@kfm/maplibre";
import {
  MAP_FEATURE_SELECTION_PROFILE as APP_SELECTION_PROFILE,
  parseMapFeatureSelection,
} from "../src/features/map_runtime";

const selection: MapFeatureSelection = Object.freeze({
  profile: MAP_FEATURE_SELECTION_PROFILE,
  selectionId: "selection:synthetic:1",
  layerId: "layer:released:synthetic",
  featureId: "feature:synthetic:1",
  evidenceRefs: Object.freeze(["evidence:synthetic:1"]),
});

describe("MapRuntimePort dependency-free consumer seam", () => {
  it("shares the existing click-selection profile without changing its parser", () => {
    expect(APP_SELECTION_PROFILE).toBe(MAP_FEATURE_SELECTION_PROFILE);
    expect(
      parseMapFeatureSelection({
        profile: MAP_FEATURE_SELECTION_PROFILE,
        selection_id: selection.selectionId,
        layer_id: selection.layerId,
        feature_id: selection.featureId,
        evidence_refs: [...selection.evidenceRefs],
      }),
    ).toEqual(selection);
    expect(isMapFeatureSelection(selection)).toBe(true);
  });

  it("initializes deterministically without a renderer dependency", async () => {
    const runtime = createNullMapRuntime();
    expect(runtime.profile).toBe(MAP_RUNTIME_PORT_PROFILE);
    expect(runtime.getSnapshot().state).toBe("IDLE");

    const ready = await runtime.initialize();
    expect(ready.state).toBe("READY");
    expect(ready.selection).toBeNull();
    expect(Object.isFrozen(ready)).toBe(true);
    expect(Object.isFrozen(ready.camera)).toBe(true);

    expect((await runtime.initialize()).state).toBe("READY");
  });

  it("publishes only validated KFM-owned selections to subscribers", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    const listener = vi.fn();
    const unsubscribe = runtime.subscribeSelection(listener);

    const snapshot = runtime.emitSelection(selection);
    expect(snapshot.selection).toEqual(selection);
    expect(listener).toHaveBeenCalledTimes(1);
    expect(listener).toHaveBeenCalledWith(selection);
    expect(Object.isFrozen(snapshot.selection?.evidenceRefs)).toBe(true);

    unsubscribe();
    runtime.emitSelection({ ...selection, selectionId: "selection:synthetic:2" });
    expect(listener).toHaveBeenCalledTimes(1);
  });

  it("fails closed for invalid camera and selection values", async () => {
    const runtime = createNullMapRuntime();
    expect(isMapRuntimeCamera({ ...runtime.getSnapshot().camera, latitude: 100 })).toBe(false);
    expect(isMapFeatureSelection({ ...selection, evidenceRefs: ["duplicate", "duplicate"] })).toBe(false);

    await runtime.initialize();
    expect(() => runtime.setCamera({ ...runtime.getSnapshot().camera, zoom: 99 })).toThrow(
      MapRuntimePortError,
    );
    expect(() =>
      runtime.emitSelection({
        ...selection,
        evidenceRefs: ["duplicate", "duplicate"],
      }),
    ).toThrow(MapRuntimePortError);
  });

  it("disposes idempotently and prevents later runtime effects", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    runtime.dispose();
    runtime.dispose();

    expect(runtime.getSnapshot()).toMatchObject({
      state: "DISPOSED",
      reason: "MAP_RUNTIME_DISPOSED",
      selection: null,
    });
    expect(() => runtime.setCamera(runtime.getSnapshot().camera)).toThrow(
      MapRuntimePortError,
    );
  });
});
