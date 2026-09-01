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

const REQUEST_FIELDS = new Set([
  "profile",
  "mode",
  "exaggeration",
  "fallback",
]);
const CAPABILITY_FIELDS = new Set(["terrainSupported", "demSourceReady"]);
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
