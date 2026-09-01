import {
  MapRuntimePortError,
  freezeMapRuntimeCamera,
  type MapRuntimeCamera,
} from "./map-runtime-port";

/**
 * Renderer-neutral discrete camera interaction vocabulary for keyboard,
 * button, switch-control, and other bounded Explorer navigation surfaces.
 */
export const MAP_RUNTIME_CAMERA_INTERACTION_PROFILE =
  "kfm.map-runtime-camera-interaction.v1" as const;

export const MAP_RUNTIME_CAMERA_INTERACTION_COMMANDS = [
  "PAN_NORTH",
  "PAN_SOUTH",
  "PAN_EAST",
  "PAN_WEST",
  "ZOOM_IN",
  "ZOOM_OUT",
  "ROTATE_CLOCKWISE",
  "ROTATE_COUNTERCLOCKWISE",
  "PITCH_UP",
  "PITCH_DOWN",
  "RESET_ORIENTATION",
] as const;

export type MapRuntimeCameraInteractionCommand =
  (typeof MAP_RUNTIME_CAMERA_INTERACTION_COMMANDS)[number];

export type MapRuntimeCameraInteraction = Readonly<{
  profile: typeof MAP_RUNTIME_CAMERA_INTERACTION_PROFILE;
  command: MapRuntimeCameraInteractionCommand;
}>;

const INTERACTION_FIELDS = new Set(["profile", "command"]);
const MAX_MERCATOR_LATITUDE = 85.051129;
const PAN_LONGITUDE_DEGREES_AT_ZOOM_ZERO = 45;
const PAN_LATITUDE_DEGREES_AT_ZOOM_ZERO = 22.5;
const ZOOM_STEP = 1;
const BEARING_STEP_DEGREES = 15;
const PITCH_STEP_DEGREES = 10;

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

function canonicalZero(value: number): number {
  return Object.is(value, -0) ? 0 : value;
}

function clamp(value: number, minimum: number, maximum: number): number {
  return Math.min(maximum, Math.max(minimum, value));
}

function wrapSignedDegrees(value: number): number {
  const wrapped = ((((value + 180) % 360) + 360) % 360) - 180;
  return canonicalZero(wrapped);
}

export function isMapRuntimeCameraInteraction(
  value: unknown,
): value is MapRuntimeCameraInteraction {
  return (
    isRecord(value) &&
    hasExactFields(value, INTERACTION_FIELDS) &&
    value.profile === MAP_RUNTIME_CAMERA_INTERACTION_PROFILE &&
    typeof value.command === "string" &&
    (MAP_RUNTIME_CAMERA_INTERACTION_COMMANDS as readonly string[]).includes(
      value.command,
    )
  );
}

export function applyMapRuntimeCameraInteraction(
  camera: MapRuntimeCamera,
  interaction: MapRuntimeCameraInteraction,
): MapRuntimeCamera {
  const current = freezeMapRuntimeCamera(camera);
  if (!isMapRuntimeCameraInteraction(interaction)) {
    throw new MapRuntimePortError(
      "MAP_RUNTIME_STATE_INVALID",
      "Map runtime camera interaction is invalid.",
    );
  }

  const scale = 2 ** current.zoom;
  const longitudeStep = PAN_LONGITUDE_DEGREES_AT_ZOOM_ZERO / scale;
  const latitudeStep = PAN_LATITUDE_DEGREES_AT_ZOOM_ZERO / scale;

  switch (interaction.command) {
    case "PAN_NORTH":
      return freezeMapRuntimeCamera({
        ...current,
        latitude: canonicalZero(
          clamp(
            current.latitude + latitudeStep,
            -MAX_MERCATOR_LATITUDE,
            MAX_MERCATOR_LATITUDE,
          ),
        ),
      });
    case "PAN_SOUTH":
      return freezeMapRuntimeCamera({
        ...current,
        latitude: canonicalZero(
          clamp(
            current.latitude - latitudeStep,
            -MAX_MERCATOR_LATITUDE,
            MAX_MERCATOR_LATITUDE,
          ),
        ),
      });
    case "PAN_EAST":
      return freezeMapRuntimeCamera({
        ...current,
        longitude: wrapSignedDegrees(current.longitude + longitudeStep),
      });
    case "PAN_WEST":
      return freezeMapRuntimeCamera({
        ...current,
        longitude: wrapSignedDegrees(current.longitude - longitudeStep),
      });
    case "ZOOM_IN":
      return freezeMapRuntimeCamera({
        ...current,
        zoom: canonicalZero(clamp(current.zoom + ZOOM_STEP, 0, 24)),
      });
    case "ZOOM_OUT":
      return freezeMapRuntimeCamera({
        ...current,
        zoom: canonicalZero(clamp(current.zoom - ZOOM_STEP, 0, 24)),
      });
    case "ROTATE_CLOCKWISE":
      return freezeMapRuntimeCamera({
        ...current,
        bearing: wrapSignedDegrees(current.bearing + BEARING_STEP_DEGREES),
      });
    case "ROTATE_COUNTERCLOCKWISE":
      return freezeMapRuntimeCamera({
        ...current,
        bearing: wrapSignedDegrees(current.bearing - BEARING_STEP_DEGREES),
      });
    case "PITCH_UP":
      return freezeMapRuntimeCamera({
        ...current,
        pitch: canonicalZero(clamp(current.pitch + PITCH_STEP_DEGREES, 0, 85)),
      });
    case "PITCH_DOWN":
      return freezeMapRuntimeCamera({
        ...current,
        pitch: canonicalZero(clamp(current.pitch - PITCH_STEP_DEGREES, 0, 85)),
      });
    case "RESET_ORIENTATION":
      return freezeMapRuntimeCamera({
        ...current,
        bearing: 0,
        pitch: 0,
      });
  }
}
