import { MapRuntimePortError } from "./map-runtime-port";

export const MAP_RUNTIME_LAYER_LIFECYCLE_PROFILE =
  "kfm.map-runtime-layer-lifecycle.v1" as const;

export const MAP_RUNTIME_LAYER_VISIBILITIES = ["VISIBLE", "HIDDEN"] as const;
export type MapRuntimeLayerVisibility =
  (typeof MAP_RUNTIME_LAYER_VISIBILITIES)[number];

export type MapRuntimeLayerLifecycleEntry = Readonly<{
  layerId: string;
  sourceId: string;
  visibility: MapRuntimeLayerVisibility;
}>;

export type MapRuntimeLayerLifecycleState = Readonly<{
  profile: typeof MAP_RUNTIME_LAYER_LIFECYCLE_PROFILE;
  sources: readonly string[];
  layers: readonly MapRuntimeLayerLifecycleEntry[];
}>;

export type MapRuntimeLayerLifecycleOperation =
  | Readonly<{ op: "ATTACH_SOURCE"; sourceId: string }>
  | Readonly<{
      op: "ATTACH_LAYER";
      layerId: string;
      sourceId: string;
      visibility: MapRuntimeLayerVisibility;
    }>
  | Readonly<{
      op: "SET_LAYER_VISIBILITY";
      layerId: string;
      visibility: MapRuntimeLayerVisibility;
    }>
  | Readonly<{ op: "DETACH_LAYER"; layerId: string }>
  | Readonly<{ op: "DETACH_SOURCE"; sourceId: string }>;

const STATE_FIELDS = new Set(["profile", "sources", "layers"]);
const LAYER_FIELDS = new Set(["layerId", "sourceId", "visibility"]);
const OPERATION_FIELDS = Object.freeze({
  ATTACH_SOURCE: new Set(["op", "sourceId"]),
  ATTACH_LAYER: new Set(["op", "layerId", "sourceId", "visibility"]),
  SET_LAYER_VISIBILITY: new Set(["op", "layerId", "visibility"]),
  DETACH_LAYER: new Set(["op", "layerId"]),
  DETACH_SOURCE: new Set(["op", "sourceId"]),
});
const SAFE_ID = /^[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}$/;
const MAX_SOURCES = 256;
const MAX_LAYERS = 512;
const MAX_OPERATIONS = 1_024;

function invalid(message: string): never {
  throw new MapRuntimePortError("MAP_RUNTIME_STATE_INVALID", message);
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  expected: ReadonlySet<string>,
): boolean {
  const keys = Object.keys(value);
  return keys.length === expected.size && keys.every((key) => expected.has(key));
}

function isSafeId(value: unknown): value is string {
  return typeof value === "string" && SAFE_ID.test(value);
}

function isVisibility(value: unknown): value is MapRuntimeLayerVisibility {
  return (
    typeof value === "string" &&
    (MAP_RUNTIME_LAYER_VISIBILITIES as readonly string[]).includes(value)
  );
}

function compareIds(left: string, right: string): number {
  if (left < right) return -1;
  if (left > right) return 1;
  return 0;
}

function freezeState(
  state: MapRuntimeLayerLifecycleState,
): MapRuntimeLayerLifecycleState {
  if (!isRecord(state) || !hasExactFields(state, STATE_FIELDS)) {
    invalid("Map runtime layer lifecycle state is invalid.");
  }
  if (state.profile !== MAP_RUNTIME_LAYER_LIFECYCLE_PROFILE) {
    invalid("Map runtime layer lifecycle profile is invalid.");
  }
  if (!Array.isArray(state.sources) || state.sources.length > MAX_SOURCES) {
    invalid("Map runtime layer lifecycle sources are invalid.");
  }
  if (!state.sources.every(isSafeId)) {
    invalid("Map runtime layer lifecycle source ID is invalid.");
  }
  const sourceSet = new Set(state.sources);
  if (sourceSet.size !== state.sources.length) {
    invalid("Map runtime layer lifecycle source IDs must be unique.");
  }
  if (!Array.isArray(state.layers) || state.layers.length > MAX_LAYERS) {
    invalid("Map runtime layer lifecycle layers are invalid.");
  }

  const layers = state.layers.map((layer) => {
    if (!isRecord(layer) || !hasExactFields(layer, LAYER_FIELDS)) {
      invalid("Map runtime layer lifecycle entry is invalid.");
    }
    if (!isSafeId(layer.layerId) || !isSafeId(layer.sourceId)) {
      invalid("Map runtime layer lifecycle layer binding is invalid.");
    }
    if (!sourceSet.has(layer.sourceId) || !isVisibility(layer.visibility)) {
      invalid("Map runtime layer lifecycle layer state is invalid.");
    }
    return Object.freeze({
      layerId: layer.layerId,
      sourceId: layer.sourceId,
      visibility: layer.visibility,
    });
  });
  if (new Set(layers.map((layer) => layer.layerId)).size !== layers.length) {
    invalid("Map runtime layer lifecycle layer IDs must be unique.");
  }

  return Object.freeze({
    profile: MAP_RUNTIME_LAYER_LIFECYCLE_PROFILE,
    sources: Object.freeze([...sourceSet].sort(compareIds)),
    layers: Object.freeze(
      [...layers].sort((left, right) => compareIds(left.layerId, right.layerId)),
    ),
  });
}

function validateOperation(
  operation: unknown,
): asserts operation is MapRuntimeLayerLifecycleOperation {
  if (!isRecord(operation) || typeof operation.op !== "string") {
    invalid("Map runtime layer lifecycle operation is invalid.");
  }
  const expected =
    OPERATION_FIELDS[operation.op as keyof typeof OPERATION_FIELDS];
  if (expected === undefined || !hasExactFields(operation, expected)) {
    invalid("Map runtime layer lifecycle operation is invalid.");
  }
  if ("sourceId" in operation && !isSafeId(operation.sourceId)) {
    invalid("Map runtime layer lifecycle source ID is invalid.");
  }
  if ("layerId" in operation && !isSafeId(operation.layerId)) {
    invalid("Map runtime layer lifecycle layer ID is invalid.");
  }
  if ("visibility" in operation && !isVisibility(operation.visibility)) {
    invalid("Map runtime layer lifecycle visibility is invalid.");
  }
}

export function createEmptyMapRuntimeLayerLifecycleState(): MapRuntimeLayerLifecycleState {
  return Object.freeze({
    profile: MAP_RUNTIME_LAYER_LIFECYCLE_PROFILE,
    sources: Object.freeze([]),
    layers: Object.freeze([]),
  });
}

/**
 * Applies a bounded renderer-neutral source/layer lifecycle plan.
 *
 * This pure preflight owns only opaque identifiers, dependency ordering, and
 * visibility state. It neither admits nor activates a source, carries source
 * configuration, touches MapLibre, nor grants evidence/release authority.
 */
export function applyMapRuntimeLayerLifecyclePlan(
  state: MapRuntimeLayerLifecycleState,
  operations: readonly MapRuntimeLayerLifecycleOperation[],
): MapRuntimeLayerLifecycleState {
  const current = freezeState(state);
  if (
    !Array.isArray(operations) ||
    operations.length === 0 ||
    operations.length > MAX_OPERATIONS
  ) {
    invalid("Map runtime layer lifecycle plan is invalid.");
  }

  const sources = new Set(current.sources);
  const layers = new Map(
    current.layers.map((layer) => [layer.layerId, { ...layer }]),
  );

  for (const operation of operations as readonly unknown[]) {
    validateOperation(operation);
    switch (operation.op) {
      case "ATTACH_SOURCE":
        if (sources.has(operation.sourceId) || sources.size >= MAX_SOURCES) {
          invalid("Map runtime layer lifecycle source attachment is invalid.");
        }
        sources.add(operation.sourceId);
        break;
      case "ATTACH_LAYER":
        if (
          !sources.has(operation.sourceId) ||
          layers.has(operation.layerId) ||
          layers.size >= MAX_LAYERS
        ) {
          invalid("Map runtime layer lifecycle layer attachment is invalid.");
        }
        layers.set(operation.layerId, {
          layerId: operation.layerId,
          sourceId: operation.sourceId,
          visibility: operation.visibility,
        });
        break;
      case "SET_LAYER_VISIBILITY": {
        const layer = layers.get(operation.layerId);
        if (layer === undefined) {
          invalid("Map runtime layer lifecycle visibility target is invalid.");
        }
        layers.set(operation.layerId, {
          ...layer,
          visibility: operation.visibility,
        });
        break;
      }
      case "DETACH_LAYER":
        if (!layers.delete(operation.layerId)) {
          invalid("Map runtime layer lifecycle layer removal is invalid.");
        }
        break;
      case "DETACH_SOURCE":
        if (
          !sources.has(operation.sourceId) ||
          [...layers.values()].some(
            (layer) => layer.sourceId === operation.sourceId,
          )
        ) {
          invalid("Map runtime layer lifecycle source removal is invalid.");
        }
        sources.delete(operation.sourceId);
        break;
    }
  }

  return freezeState({
    profile: MAP_RUNTIME_LAYER_LIFECYCLE_PROFILE,
    sources: [...sources],
    layers: [...layers.values()],
  });
}
