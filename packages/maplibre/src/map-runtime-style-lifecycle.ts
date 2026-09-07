import { MapRuntimePortError } from "./map-runtime-port";

export const MAP_RUNTIME_STYLE_PROFILE = "kfm.map-runtime-style.v1" as const;
export const MAP_RUNTIME_STYLE_SOURCE_PROFILE =
  "kfm.map-runtime-style-source.v1" as const;
export const MAP_RUNTIME_STYLE_LAYER_PROFILE =
  "kfm.map-runtime-style-layer.v1" as const;
export const MAP_RUNTIME_STYLE_PLAN_PROFILE =
  "kfm.map-runtime-style-plan.v1" as const;
export const MAP_RUNTIME_STYLE_COORDINATOR_PROFILE =
  "kfm.map-runtime-style-coordinator.v1" as const;

const MAX_STYLE_SOURCES = 256;
const MAX_STYLE_LAYERS = 512;
const SAFE_IDENTIFIER = /^[a-z0-9][a-z0-9._:-]{0,127}$/;

export type MapRuntimeStyleSource = Readonly<{
  profile: typeof MAP_RUNTIME_STYLE_SOURCE_PROFILE;
  sourceId: string;
  revision: string;
}>;

export type MapRuntimeStyleLayer = Readonly<{
  profile: typeof MAP_RUNTIME_STYLE_LAYER_PROFILE;
  layerId: string;
  sourceId: string;
  revision: string;
  order: number;
}>;

export type MapRuntimeStyleState = Readonly<{
  profile: typeof MAP_RUNTIME_STYLE_PROFILE;
  sources: readonly MapRuntimeStyleSource[];
  layers: readonly MapRuntimeStyleLayer[];
}>;

export type MapRuntimeStyleLifecycleAction =
  | Readonly<{ effect: "REMOVE_LAYER"; layerId: string }>
  | Readonly<{ effect: "REMOVE_SOURCE"; sourceId: string }>
  | Readonly<{ effect: "ADD_SOURCE"; source: MapRuntimeStyleSource }>
  | Readonly<{ effect: "ADD_LAYER"; layer: MapRuntimeStyleLayer }>;

export type MapRuntimeStyleLifecyclePlan = Readonly<{
  profile: typeof MAP_RUNTIME_STYLE_PLAN_PROFILE;
  current: MapRuntimeStyleState;
  target: MapRuntimeStyleState;
  actions: readonly MapRuntimeStyleLifecycleAction[];
}>;

export type MapRuntimeStyleLifecycleTicket = Readonly<{
  profile: typeof MAP_RUNTIME_STYLE_COORDINATOR_PROFILE;
  revision: number;
  plan: MapRuntimeStyleLifecyclePlan;
}>;

export type MapRuntimeStyleLifecycleExecutor = (
  plan: MapRuntimeStyleLifecyclePlan,
  signal: AbortSignal,
) => void | Promise<void>;

export type MapRuntimeStyleLifecycleCoordinator = Readonly<{
  getState(): MapRuntimeStyleState;
  requiresReconciliation(): boolean;
  plan(target: MapRuntimeStyleState): MapRuntimeStyleLifecycleTicket;
  commit(ticket: MapRuntimeStyleLifecycleTicket): MapRuntimeStyleState;
  reject(ticket: MapRuntimeStyleLifecycleTicket): MapRuntimeStyleState;
  execute(
    ticket: MapRuntimeStyleLifecycleTicket,
    executor: MapRuntimeStyleLifecycleExecutor,
  ): Promise<MapRuntimeStyleState>;
  cancel(ticket: MapRuntimeStyleLifecycleTicket): MapRuntimeStyleState;
  reconcile(observed: MapRuntimeStyleState): MapRuntimeStyleState;
  dispose(): void;
}>;

/**
 * Validate, clone, canonicalize, and freeze a renderer-neutral style state.
 *
 * Deliberately excluded: URLs, tiles, GeoJSON, credentials, source options,
 * paint/layout expressions, and renderer objects. Those inputs require their
 * own governed admission boundary; this module only owns safe lifecycle order.
 */
export function freezeMapRuntimeStyleState(
  state: MapRuntimeStyleState,
): MapRuntimeStyleState {
  assertExactKeys(state, ["profile", "sources", "layers"], "style state");
  if (state.profile !== MAP_RUNTIME_STYLE_PROFILE) {
    invalid("Map runtime style profile is invalid.");
  }
  if (!Array.isArray(state.sources) || state.sources.length > MAX_STYLE_SOURCES) {
    invalid("Map runtime style sources are invalid.");
  }
  if (!Array.isArray(state.layers) || state.layers.length > MAX_STYLE_LAYERS) {
    invalid("Map runtime style layers are invalid.");
  }

  const sourceIds = new Set<string>();
  const sources = Array.from(state.sources, (source) => {
    assertExactKeys(
      source,
      ["profile", "sourceId", "revision"],
      "style source",
    );
    if (source.profile !== MAP_RUNTIME_STYLE_SOURCE_PROFILE) {
      invalid("Map runtime style source profile is invalid.");
    }
    assertSafeIdentifier(source.sourceId, "sourceId");
    assertSafeIdentifier(source.revision, "revision");
    if (sourceIds.has(source.sourceId)) {
      invalid("Map runtime style source IDs must be unique.");
    }
    sourceIds.add(source.sourceId);
    return Object.freeze({
      profile: MAP_RUNTIME_STYLE_SOURCE_PROFILE,
      sourceId: source.sourceId,
      revision: source.revision,
    });
  });

  const layerIds = new Set<string>();
  const orders = new Set<number>();
  const layers = Array.from(state.layers, (layer) => {
    assertExactKeys(
      layer,
      ["profile", "layerId", "sourceId", "revision", "order"],
      "style layer",
    );
    if (layer.profile !== MAP_RUNTIME_STYLE_LAYER_PROFILE) {
      invalid("Map runtime style layer profile is invalid.");
    }
    assertSafeIdentifier(layer.layerId, "layerId");
    assertSafeIdentifier(layer.sourceId, "sourceId");
    assertSafeIdentifier(layer.revision, "revision");
    if (
      typeof layer.order !== "number" ||
      !Number.isSafeInteger(layer.order) ||
      layer.order < 0
    ) {
      invalid("Map runtime style layer order is invalid.");
    }
    if (layerIds.has(layer.layerId)) {
      invalid("Map runtime style layer IDs must be unique.");
    }
    if (orders.has(layer.order)) {
      invalid("Map runtime style layer orders must be unique.");
    }
    if (!sourceIds.has(layer.sourceId)) {
      invalid("Map runtime style layer references an unknown source.");
    }
    layerIds.add(layer.layerId);
    orders.add(layer.order);
    return Object.freeze({
      profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
      layerId: layer.layerId,
      sourceId: layer.sourceId,
      revision: layer.revision,
      order: layer.order,
    });
  });

  for (let order = 0; order < layers.length; order += 1) {
    if (!orders.has(order)) {
      invalid("Map runtime style layer orders must be contiguous from zero.");
    }
  }

  sources.sort((left, right) =>
    left.sourceId < right.sourceId ? -1 : left.sourceId > right.sourceId ? 1 : 0,
  );
  layers.sort((left, right) => left.order - right.order);

  return Object.freeze({
    profile: MAP_RUNTIME_STYLE_PROFILE,
    sources: Object.freeze(sources),
    layers: Object.freeze(layers),
  });
}

/**
 * Produce dependency-safe renderer operations for an already-admitted style.
 *
 * The plan is deterministic: obsolete layers are removed from the top down,
 * obsolete sources follow, replacement sources are added next, and layers are
 * restored from the bottom up. Equal states yield an empty action list.
 */
export function planMapRuntimeStyleLifecycle(
  current: MapRuntimeStyleState | null,
  target: MapRuntimeStyleState,
): MapRuntimeStyleLifecyclePlan {
  const frozenCurrent = freezeMapRuntimeStyleState(
    current ?? {
      profile: MAP_RUNTIME_STYLE_PROFILE,
      sources: [],
      layers: [],
    },
  );
  const frozenTarget = freezeMapRuntimeStyleState(target);

  const currentSources = new Map(
    frozenCurrent.sources.map((source) => [source.sourceId, source]),
  );
  const targetSources = new Map(
    frozenTarget.sources.map((source) => [source.sourceId, source]),
  );
  const replacedSourceIds = new Set<string>();

  for (const source of frozenCurrent.sources) {
    const next = targetSources.get(source.sourceId);
    if (!next || next.revision !== source.revision) {
      replacedSourceIds.add(source.sourceId);
    }
  }
  for (const source of frozenTarget.sources) {
    const previous = currentSources.get(source.sourceId);
    if (!previous || previous.revision !== source.revision) {
      replacedSourceIds.add(source.sourceId);
    }
  }

  const currentLayers = new Map(
    frozenCurrent.layers.map((layer) => [layer.layerId, layer]),
  );
  const targetLayers = new Map(
    frozenTarget.layers.map((layer) => [layer.layerId, layer]),
  );
  const replaceLayerIds = new Set<string>();

  for (const layer of frozenCurrent.layers) {
    const next = targetLayers.get(layer.layerId);
    if (
      !next ||
      next.sourceId !== layer.sourceId ||
      next.revision !== layer.revision ||
      next.order !== layer.order ||
      replacedSourceIds.has(layer.sourceId)
    ) {
      replaceLayerIds.add(layer.layerId);
    }
  }
  for (const layer of frozenTarget.layers) {
    const previous = currentLayers.get(layer.layerId);
    if (
      !previous ||
      previous.sourceId !== layer.sourceId ||
      previous.revision !== layer.revision ||
      previous.order !== layer.order ||
      replacedSourceIds.has(layer.sourceId)
    ) {
      replaceLayerIds.add(layer.layerId);
    }
  }

  const changedOrders = [
    ...frozenCurrent.layers,
    ...frozenTarget.layers,
  ]
    .filter((layer) => replaceLayerIds.has(layer.layerId))
    .map((layer) => layer.order);
  const firstChangedOrder = Math.min(...changedOrders);
  if (Number.isFinite(firstChangedOrder)) {
    for (const layer of frozenCurrent.layers) {
      if (layer.order >= firstChangedOrder) replaceLayerIds.add(layer.layerId);
    }
    for (const layer of frozenTarget.layers) {
      if (layer.order >= firstChangedOrder) replaceLayerIds.add(layer.layerId);
    }
  }

  const actions: MapRuntimeStyleLifecycleAction[] = [];
  for (const layer of [...frozenCurrent.layers].reverse()) {
    if (replaceLayerIds.has(layer.layerId)) {
      actions.push(
        Object.freeze({ effect: "REMOVE_LAYER", layerId: layer.layerId }),
      );
    }
  }
  for (const source of frozenCurrent.sources) {
    if (replacedSourceIds.has(source.sourceId)) {
      actions.push(
        Object.freeze({ effect: "REMOVE_SOURCE", sourceId: source.sourceId }),
      );
    }
  }
  for (const source of frozenTarget.sources) {
    if (replacedSourceIds.has(source.sourceId)) {
      actions.push(Object.freeze({ effect: "ADD_SOURCE", source }));
    }
  }
  for (const layer of frozenTarget.layers) {
    if (replaceLayerIds.has(layer.layerId)) {
      actions.push(Object.freeze({ effect: "ADD_LAYER", layer }));
    }
  }

  return Object.freeze({
    profile: MAP_RUNTIME_STYLE_PLAN_PROFILE,
    current: frozenCurrent,
    target: frozenTarget,
    actions: Object.freeze(actions),
  });
}

/**
 * Serializes application of lifecycle plans at an injected renderer boundary.
 *
 * A plan becomes confirmed state only after the exact ticket is committed or
 * its executor succeeds. Any started execution that fails or is cancelled may
 * have partially changed the renderer, so planning fails closed until an
 * observed renderer state is explicitly reconciled. This coordinator neither
 * acquires a renderer nor admits source/layer payloads.
 */
export function createMapRuntimeStyleLifecycleCoordinator(
  initial: MapRuntimeStyleState = {
    profile: MAP_RUNTIME_STYLE_PROFILE,
    sources: [],
    layers: [],
  },
): MapRuntimeStyleLifecycleCoordinator {
  let current = freezeMapRuntimeStyleState(initial);
  let pending: MapRuntimeStyleLifecycleTicket | null = null;
  let executing: MapRuntimeStyleLifecycleTicket | null = null;
  let executionController: AbortController | null = null;
  const cancelledTickets = new Set<MapRuntimeStyleLifecycleTicket>();
  let reconciliationRequired = false;
  let nextRevision = 1;
  let disposed = false;

  function requireActive(): void {
    if (disposed) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_DISPOSED",
        "Map runtime style lifecycle coordinator is disposed.",
      );
    }
  }

  function requireReconciled(): void {
    if (reconciliationRequired) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_STYLE_RECONCILIATION_REQUIRED",
        "Map runtime style lifecycle requires renderer reconciliation.",
      );
    }
  }

  function requirePending(
    ticket: MapRuntimeStyleLifecycleTicket,
  ): MapRuntimeStyleLifecycleTicket {
    requireActive();
    if (ticket !== pending) {
      invalid("Map runtime style lifecycle ticket is stale or invalid.");
    }
    return ticket;
  }

  return Object.freeze({
    getState(): MapRuntimeStyleState {
      return current;
    },

    requiresReconciliation(): boolean {
      return reconciliationRequired;
    },

    plan(target: MapRuntimeStyleState): MapRuntimeStyleLifecycleTicket {
      requireActive();
      requireReconciled();
      if (executing !== null) {
        invalid("Map runtime style lifecycle execution is in progress.");
      }
      if (!Number.isSafeInteger(nextRevision)) {
        invalid("Map runtime style lifecycle revision is exhausted.");
      }
      const ticket = Object.freeze({
        profile: MAP_RUNTIME_STYLE_COORDINATOR_PROFILE,
        revision: nextRevision,
        plan: planMapRuntimeStyleLifecycle(current, target),
      });
      nextRevision += 1;
      pending = ticket;
      return ticket;
    },

    commit(ticket: MapRuntimeStyleLifecycleTicket): MapRuntimeStyleState {
      const accepted = requirePending(ticket);
      current = accepted.plan.target;
      pending = null;
      return current;
    },

    reject(ticket: MapRuntimeStyleLifecycleTicket): MapRuntimeStyleState {
      requirePending(ticket);
      pending = null;
      return current;
    },

    async execute(
      ticket: MapRuntimeStyleLifecycleTicket,
      executor: MapRuntimeStyleLifecycleExecutor,
    ): Promise<MapRuntimeStyleState> {
      const accepted = requirePending(ticket);
      if (typeof executor !== "function") {
        invalid("Map runtime style lifecycle executor is invalid.");
      }
      pending = null;
      executing = accepted;
      const controller = new AbortController();
      executionController = controller;

      try {
        await executor(accepted.plan, controller.signal);
      } catch {
        if (disposed) requireActive();
        if (cancelledTickets.delete(accepted)) {
          throw new MapRuntimePortError(
            "MAP_RUNTIME_STYLE_LIFECYCLE_CANCELLED",
            "Map runtime style lifecycle execution was cancelled.",
          );
        }
        if (executing !== accepted || executionController !== controller) {
          invalid("Map runtime style lifecycle execution state is invalid.");
        }
        executing = null;
        executionController = null;
        reconciliationRequired = true;
        throw new MapRuntimePortError(
          "MAP_RUNTIME_STYLE_LIFECYCLE_FAILED",
          "Map runtime style lifecycle execution failed.",
        );
      }

      if (disposed) requireActive();
      if (cancelledTickets.delete(accepted)) {
        throw new MapRuntimePortError(
          "MAP_RUNTIME_STYLE_LIFECYCLE_CANCELLED",
          "Map runtime style lifecycle execution was cancelled.",
        );
      }
      if (executing !== accepted || executionController !== controller) {
        invalid("Map runtime style lifecycle execution state is invalid.");
      }
      current = accepted.plan.target;
      executing = null;
      executionController = null;
      return current;
    },

    cancel(ticket: MapRuntimeStyleLifecycleTicket): MapRuntimeStyleState {
      requireActive();
      if (ticket !== executing || executionController === null) {
        invalid("Map runtime style lifecycle ticket is not executing.");
      }
      const controller = executionController;
      cancelledTickets.add(ticket);
      executing = null;
      executionController = null;
      reconciliationRequired = true;
      controller.abort();
      return current;
    },

    reconcile(observed: MapRuntimeStyleState): MapRuntimeStyleState {
      requireActive();
      if (executing !== null) {
        invalid("Map runtime style lifecycle execution is in progress.");
      }
      current = freezeMapRuntimeStyleState(observed);
      pending = null;
      reconciliationRequired = false;
      return current;
    },

    dispose(): void {
      if (disposed) return;
      disposed = true;
      pending = null;
      executing = null;
      const controller = executionController;
      executionController = null;
      cancelledTickets.clear();
      controller?.abort();
    },
  });
}

function assertSafeIdentifier(
  value: unknown,
  field: string,
): asserts value is string {
  if (typeof value !== "string" || !SAFE_IDENTIFIER.test(value)) {
    invalid(`Map runtime style ${field} is invalid.`);
  }
}

function assertExactKeys(
  value: unknown,
  expectedKeys: readonly string[],
  subject: string,
): asserts value is Record<string, unknown> {
  if (typeof value !== "object" || value === null || Array.isArray(value)) {
    invalid(`Map runtime ${subject} is invalid.`);
  }
  const actualKeys = Object.keys(value).sort();
  const expected = [...expectedKeys].sort();
  if (
    actualKeys.length !== expected.length ||
    actualKeys.some((key, index) => key !== expected[index])
  ) {
    invalid(`Map runtime ${subject} fields are invalid.`);
  }
}

function invalid(message: string): never {
  throw new MapRuntimePortError("MAP_RUNTIME_STATE_INVALID", message);
}
