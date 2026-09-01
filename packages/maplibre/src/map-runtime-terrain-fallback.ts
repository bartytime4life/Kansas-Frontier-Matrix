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
