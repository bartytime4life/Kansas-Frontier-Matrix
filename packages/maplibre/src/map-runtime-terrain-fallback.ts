import { MapRuntimePortError } from "./map-runtime-port";

export const MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE =
  "kfm.map-runtime-terrain-fallback.v1" as const;

export const MAP_RUNTIME_TERRAIN_MODES = ["FLAT", "TERRAIN"] as const;
export type MapRuntimeTerrainMode =
  (typeof MAP_RUNTIME_TERRAIN_MODES)[number];

export const MAP_RUNTIME_TERRAIN_FALLBACK_REASONS = [
  "TERRAIN_UNSUPPORTED",
  "TERRAIN_SOURCE_UNAVAILABLE",
] as const;
export type MapRuntimeTerrainFallbackReason =
  (typeof MAP_RUNTIME_TERRAIN_FALLBACK_REASONS)[number];

export type MapRuntimeTerrainRequest = Readonly<{
  profile: typeof MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE;
  mode: MapRuntimeTerrainMode;
  exaggeration: number;
  fallback: "FLAT";
}>;

export type MapRuntimeTerrainCapabilities = Readonly<{
  terrainSupported: boolean;
  demSourceReady: boolean;
}>;

export type MapRuntimeTerrainState = Readonly<{
  profile: typeof MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE;
  mode: MapRuntimeTerrainMode;
  exaggeration: number;
  reason: MapRuntimeTerrainFallbackReason | null;
}>;

export const MAP_RUNTIME_TERRAIN_TRANSITION_PROFILE =
  "kfm.map-runtime-terrain-transition.v1" as const;

export const MAP_RUNTIME_TERRAIN_EFFECTS = [
  "NONE",
  "ENABLE_TERRAIN",
  "UPDATE_TERRAIN",
  "DISABLE_TERRAIN",
] as const;
export type MapRuntimeTerrainEffect =
  (typeof MAP_RUNTIME_TERRAIN_EFFECTS)[number];

export type MapRuntimeTerrainTransitionPlan = Readonly<{
  profile: typeof MAP_RUNTIME_TERRAIN_TRANSITION_PROFILE;
  effect: MapRuntimeTerrainEffect;
  target: MapRuntimeTerrainState;
}>;

export const MAP_RUNTIME_TERRAIN_COORDINATOR_PROFILE =
  "kfm.map-runtime-terrain-coordinator.v1" as const;

export type MapRuntimeTerrainTransitionTicket = Readonly<{
  profile: typeof MAP_RUNTIME_TERRAIN_COORDINATOR_PROFILE;
  revision: number;
  plan: MapRuntimeTerrainTransitionPlan;
}>;

export type MapRuntimeTerrainTransitionExecutor = (
  plan: MapRuntimeTerrainTransitionPlan,
  signal: AbortSignal,
) => void | Promise<void>;

export type MapRuntimeTerrainTransitionCoordinator = Readonly<{
  getState(): MapRuntimeTerrainState | null;
  plan(
    request: MapRuntimeTerrainRequest,
    capabilities: MapRuntimeTerrainCapabilities,
  ): MapRuntimeTerrainTransitionTicket;
  commit(ticket: MapRuntimeTerrainTransitionTicket): MapRuntimeTerrainState;
  reject(ticket: MapRuntimeTerrainTransitionTicket): MapRuntimeTerrainState | null;
  execute(
    ticket: MapRuntimeTerrainTransitionTicket,
    executor: MapRuntimeTerrainTransitionExecutor,
  ): Promise<MapRuntimeTerrainState>;
  cancel(ticket: MapRuntimeTerrainTransitionTicket): MapRuntimeTerrainState | null;
  dispose(): void;
}>;

const REQUEST_FIELDS = new Set([
  "profile",
  "mode",
  "exaggeration",
  "fallback",
]);
const CAPABILITY_FIELDS = new Set(["terrainSupported", "demSourceReady"]);
const STATE_FIELDS = new Set(["profile", "mode", "exaggeration", "reason"]);
const MIN_TERRAIN_EXAGGERATION = 0.1;
const MAX_TERRAIN_EXAGGERATION = 5;

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

function isFiniteNumber(value: unknown): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

function isFallbackReason(
  value: unknown,
): value is MapRuntimeTerrainFallbackReason {
  return (
    value === "TERRAIN_UNSUPPORTED" || value === "TERRAIN_SOURCE_UNAVAILABLE"
  );
}

function validateTerrainState(state: unknown): asserts state is MapRuntimeTerrainState {
  if (!isRecord(state) || !hasExactFields(state, STATE_FIELDS)) {
    invalid("Current map runtime terrain state is invalid.");
  }
  if (
    state.profile !== MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE ||
    !isFiniteNumber(state.exaggeration)
  ) {
    invalid("Current map runtime terrain state is invalid.");
  }
  if (state.mode === "FLAT") {
    if (
      state.exaggeration !== 0 ||
      (state.reason !== null && !isFallbackReason(state.reason))
    ) {
      invalid("Current flat map runtime terrain state is invalid.");
    }
    return;
  }
  if (
    state.mode !== "TERRAIN" ||
    state.reason !== null ||
    state.exaggeration < MIN_TERRAIN_EXAGGERATION ||
    state.exaggeration > MAX_TERRAIN_EXAGGERATION
  ) {
    invalid("Current terrain map runtime state is invalid.");
  }
}

function flatState(
  reason: MapRuntimeTerrainFallbackReason | null,
): MapRuntimeTerrainState {
  return Object.freeze({
    profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
    mode: "FLAT",
    exaggeration: 0,
    reason,
  });
}

/**
 * Resolves an already-authorized terrain request against supplied runtime
 * capability facts without acquiring a renderer or source.
 *
 * The resolver owns only finite presentation fallback state. It does not
 * discover, admit, activate, load, or validate a DEM source; evaluate policy;
 * or grant evidence, release, deployment, or publication authority.
 */
export function resolveMapRuntimeTerrainState(
  request: MapRuntimeTerrainRequest,
  capabilities: MapRuntimeTerrainCapabilities,
): MapRuntimeTerrainState {
  if (!isRecord(request) || !hasExactFields(request, REQUEST_FIELDS)) {
    invalid("Map runtime terrain request is invalid.");
  }
  if (
    request.profile !== MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE ||
    request.fallback !== "FLAT" ||
    !isFiniteNumber(request.exaggeration)
  ) {
    invalid("Map runtime terrain request is invalid.");
  }
  if (!isRecord(capabilities) || !hasExactFields(capabilities, CAPABILITY_FIELDS)) {
    invalid("Map runtime terrain capabilities are invalid.");
  }
  if (
    typeof capabilities.terrainSupported !== "boolean" ||
    typeof capabilities.demSourceReady !== "boolean"
  ) {
    invalid("Map runtime terrain capabilities are invalid.");
  }

  if (request.mode === "FLAT") {
    if (request.exaggeration !== 0) {
      invalid("Flat map runtime terrain exaggeration must be zero.");
    }
    return flatState(null);
  }
  if (request.mode !== "TERRAIN") {
    invalid("Map runtime terrain mode is invalid.");
  }
  if (
    request.exaggeration < MIN_TERRAIN_EXAGGERATION ||
    request.exaggeration > MAX_TERRAIN_EXAGGERATION
  ) {
    invalid("Map runtime terrain exaggeration is invalid.");
  }
  if (!capabilities.terrainSupported) {
    return flatState("TERRAIN_UNSUPPORTED");
  }
  if (!capabilities.demSourceReady) {
    return flatState("TERRAIN_SOURCE_UNAVAILABLE");
  }

  return Object.freeze({
    profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
    mode: "TERRAIN",
    exaggeration: request.exaggeration,
    reason: null,
  });
}

/**
 * Plans the renderer effect needed to move from a known governed terrain
 * state to the freshly resolved target. The plan is data only: applying the
 * effect remains the responsibility of an authorized renderer adapter.
 */
export function planMapRuntimeTerrainTransition(
  current: MapRuntimeTerrainState | null,
  request: MapRuntimeTerrainRequest,
  capabilities: MapRuntimeTerrainCapabilities,
): MapRuntimeTerrainTransitionPlan {
  if (current !== null) {
    validateTerrainState(current);
  }

  const target = resolveMapRuntimeTerrainState(request, capabilities);
  let effect: MapRuntimeTerrainEffect = "NONE";

  if (target.mode === "TERRAIN" && current?.mode !== "TERRAIN") {
    effect = "ENABLE_TERRAIN";
  } else if (
    target.mode === "TERRAIN" &&
    current?.mode === "TERRAIN" &&
    target.exaggeration !== current.exaggeration
  ) {
    effect = "UPDATE_TERRAIN";
  } else if (target.mode === "FLAT" && current?.mode === "TERRAIN") {
    effect = "DISABLE_TERRAIN";
  }

  return Object.freeze({
    profile: MAP_RUNTIME_TERRAIN_TRANSITION_PROFILE,
    effect,
    target,
  });
}

/**
 * Coordinates asynchronous renderer application without treating a plan as
 * applied state. A newer plan supersedes the previous pending ticket, and only
 * committing that exact ticket advances the coordinator's current state.
 */
export function createMapRuntimeTerrainTransitionCoordinator(
  initial: MapRuntimeTerrainState | null = null,
): MapRuntimeTerrainTransitionCoordinator {
  if (initial !== null) {
    validateTerrainState(initial);
  }

  let current =
    initial === null ? null : (Object.freeze({ ...initial }) as MapRuntimeTerrainState);
  let pending: MapRuntimeTerrainTransitionTicket | null = null;
  let executing: MapRuntimeTerrainTransitionTicket | null = null;
  let executionController: AbortController | null = null;
  const cancelledTickets = new Set<MapRuntimeTerrainTransitionTicket>();
  let nextRevision = 1;
  let disposed = false;

  function requireActive(): void {
    if (disposed) {
      throw new MapRuntimePortError(
        "MAP_RUNTIME_DISPOSED",
        "Map runtime terrain transition coordinator is disposed.",
      );
    }
  }

  function requirePending(
    ticket: MapRuntimeTerrainTransitionTicket,
  ): MapRuntimeTerrainTransitionTicket {
    requireActive();
    if (ticket !== pending) {
      invalid("Map runtime terrain transition ticket is stale or invalid.");
    }
    return ticket;
  }

  return Object.freeze({
    getState(): MapRuntimeTerrainState | null {
      return current;
    },

    plan(
      request: MapRuntimeTerrainRequest,
      capabilities: MapRuntimeTerrainCapabilities,
    ): MapRuntimeTerrainTransitionTicket {
      requireActive();
      if (executing !== null) {
        invalid("Map runtime terrain transition execution is in progress.");
      }
      if (!Number.isSafeInteger(nextRevision)) {
        invalid("Map runtime terrain transition revision is exhausted.");
      }
      const ticket = Object.freeze({
        profile: MAP_RUNTIME_TERRAIN_COORDINATOR_PROFILE,
        revision: nextRevision,
        plan: planMapRuntimeTerrainTransition(current, request, capabilities),
      });
      nextRevision += 1;
      pending = ticket;
      return ticket;
    },

    commit(ticket: MapRuntimeTerrainTransitionTicket): MapRuntimeTerrainState {
      const accepted = requirePending(ticket);
      current = accepted.plan.target;
      pending = null;
      return current;
    },

    reject(
      ticket: MapRuntimeTerrainTransitionTicket,
    ): MapRuntimeTerrainState | null {
      requirePending(ticket);
      pending = null;
      return current;
    },

    async execute(
      ticket: MapRuntimeTerrainTransitionTicket,
      executor: MapRuntimeTerrainTransitionExecutor,
    ): Promise<MapRuntimeTerrainState> {
      const accepted = requirePending(ticket);
      if (typeof executor !== "function") {
        invalid("Map runtime terrain transition executor is invalid.");
      }
      pending = null;
      executing = accepted;
      const controller = new AbortController();
      executionController = controller;
      try {
        await executor(accepted.plan, controller.signal);
      } catch {
        if (disposed) {
          requireActive();
        }
        if (cancelledTickets.delete(accepted)) {
          throw new MapRuntimePortError(
            "MAP_RUNTIME_TERRAIN_TRANSITION_CANCELLED",
            "Map runtime terrain transition execution was cancelled.",
          );
        }
        if (executing !== accepted || executionController !== controller) {
          invalid("Map runtime terrain transition execution state is invalid.");
        }
        executing = null;
        executionController = null;
        throw new MapRuntimePortError(
          "MAP_RUNTIME_TERRAIN_TRANSITION_FAILED",
          "Map runtime terrain transition execution failed.",
        );
      }
      if (disposed) {
        requireActive();
      }
      if (cancelledTickets.delete(accepted)) {
        throw new MapRuntimePortError(
          "MAP_RUNTIME_TERRAIN_TRANSITION_CANCELLED",
          "Map runtime terrain transition execution was cancelled.",
        );
      }
      if (executing !== accepted || executionController !== controller) {
        invalid("Map runtime terrain transition execution state is invalid.");
      }
      current = accepted.plan.target;
      executing = null;
      executionController = null;
      return current;
    },

    cancel(ticket: MapRuntimeTerrainTransitionTicket): MapRuntimeTerrainState | null {
      requireActive();
      if (ticket !== executing || executionController === null) {
        invalid("Map runtime terrain transition ticket is not executing.");
      }
      const controller = executionController;
      cancelledTickets.add(ticket);
      executing = null;
      executionController = null;
      controller.abort();
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
