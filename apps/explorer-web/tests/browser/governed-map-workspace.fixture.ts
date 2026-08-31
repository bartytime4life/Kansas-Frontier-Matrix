import {
  createNullMapRuntime,
  type InlineGeoJsonMapRuntimePort,
  type MapRuntimeSnapshot,
} from "@kfm/maplibre";
import { mountGovernedMapWorkspace } from "../../src/site/mount-governed-map-workspace";
import {
  governedAnswerResponse,
  governedLayerResponse,
} from "./governed-map-api-fixtures";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Governed map fixture root is missing.");

let closeCount = 0;
let closeThrows = false;
let neverSettlingDisposeCount = 0;
let primary = createNullMapRuntime();
let controller: ReturnType<typeof mountGovernedMapWorkspace> | null = null;

function createNeverSettlingRuntime(): InlineGeoJsonMapRuntimePort {
  const delegate = createNullMapRuntime();
  return {
    profile: delegate.profile,
    initialize: () => new Promise<MapRuntimeSnapshot>(() => undefined),
    getSnapshot: () => delegate.getSnapshot(),
    setCamera: (camera) => delegate.setCamera(camera),
    subscribeSnapshot: (listener) => delegate.subscribeSnapshot(listener),
    subscribeSelection: (listener) => delegate.subscribeSelection(listener),
    bindInlineGeoJsonLayer: (layer) => delegate.bindInlineGeoJsonLayer(layer),
    removeLayer: (layerId) => delegate.removeLayer(layerId),
    removeSource: (sourceId) => delegate.removeSource(sourceId),
    selectFeature: (layerId, featureId) =>
      delegate.selectFeature(layerId, featureId),
    dispose: () => {
      neverSettlingDisposeCount += 1;
      delegate.dispose();
    },
  };
}

function mount(): void {
  primary = createNullMapRuntime();
  const useNeverSettlingRuntime =
    new URLSearchParams(window.location.search).get("runtime") ===
    "never-settling";
  controller = mountGovernedMapWorkspace(root, {
    createMapRuntime: () =>
      useNeverSettlingRuntime ? createNeverSettlingRuntime() : primary,
    ...(useNeverSettlingRuntime
      ? { runtimeInitializationDeadlineMs: 25 }
      : {}),
    transport: {
      loadLayers: async () => governedLayerResponse,
      loadEvidence: async () => governedAnswerResponse,
      close: () => {
        closeCount += 1;
        if (closeThrows) throw new Error("synthetic transport close failure");
      },
    },
  });
  void controller.start();
}

function destroy(): void {
  controller?.destroy();
  controller = null;
}

mount();

Object.assign(window, {
  __kfmTriggerPostInitializationError: () => primary.emitTrustState("ERROR"),
  __kfmDestroyGovernedWorkspace: destroy,
  __kfmRemountGovernedWorkspace: mount,
  __kfmGovernedTransportCloseCount: () => closeCount,
  __kfmSetGovernedTransportCloseFailure: () => {
    closeThrows = true;
  },
  __kfmNeverSettlingDisposeCount: () => neverSettlingDisposeCount,
});
