import {
  MapRuntimePortError,
  freezeMapRuntimeCamera,
  isMapRuntimeCamera,
  type MapRuntimeCamera,
} from "./map-runtime-port";

export const MAP_RUNTIME_CAMERA_STATE_PROFILE =
  "kfm.map-runtime-camera-state.v1" as const;
export const MAX_MAP_RUNTIME_CAMERA_STATE_LENGTH = 160;
const MAP_RUNTIME_CAMERA_STATE_PREFIX = "v1:";

function encodeNumber(value: number): string {
  return Object.is(value, -0) ? "0" : String(value);
}

function invalidNavigationState(): never {
  throw new MapRuntimePortError(
    "MAP_RUNTIME_STATE_INVALID",
    "Map runtime navigation state is invalid.",
  );
}

/**
 * Encode only renderer-neutral camera state into a deterministic URL-safe token.
 *
 * The token deliberately excludes layer, feature, evidence, source, policy, and
 * renderer state. Callers remain responsible for deciding whether an exact
 * camera is safe to expose in a URL or other public surface.
 */
export function encodeMapRuntimeCameraState(camera: MapRuntimeCamera): string {
  const frozen = freezeMapRuntimeCamera(camera);
  return `${MAP_RUNTIME_CAMERA_STATE_PREFIX}${[
    frozen.longitude,
    frozen.latitude,
    frozen.zoom,
    frozen.bearing,
    frozen.pitch,
  ]
    .map(encodeNumber)
    .join(",")}`;
}

/** Decode one canonical camera-state token and fail closed on every other form. */
export function decodeMapRuntimeCameraState(value: unknown): MapRuntimeCamera {
  if (
    typeof value !== "string" ||
    value.length === 0 ||
    value.length > MAX_MAP_RUNTIME_CAMERA_STATE_LENGTH ||
    !value.startsWith(MAP_RUNTIME_CAMERA_STATE_PREFIX)
  ) {
    return invalidNavigationState();
  }

  const fields = value.slice(MAP_RUNTIME_CAMERA_STATE_PREFIX.length).split(",");
  if (fields.length !== 5 || fields.some((field) => field.length === 0)) {
    return invalidNavigationState();
  }

  const candidate = {
    longitude: Number(fields[0]),
    latitude: Number(fields[1]),
    zoom: Number(fields[2]),
    bearing: Number(fields[3]),
    pitch: Number(fields[4]),
  };
  if (!isMapRuntimeCamera(candidate)) return invalidNavigationState();

  const frozen = freezeMapRuntimeCamera(candidate);
  if (encodeMapRuntimeCameraState(frozen) !== value) {
    return invalidNavigationState();
  }
  return frozen;
}

export function isMapRuntimeCameraState(value: unknown): value is string {
  try {
    decodeMapRuntimeCameraState(value);
    return true;
  } catch (error) {
    if (
      error instanceof MapRuntimePortError &&
      error.code === "MAP_RUNTIME_STATE_INVALID"
    ) {
      return false;
    }
    throw error;
  }
}
