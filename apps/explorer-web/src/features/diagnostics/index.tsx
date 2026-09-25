/** Public-safe renderer status. This projection has no telemetry transport. */
import {
  MAP_RUNTIME_PORT_PROFILE,
  MAP_RUNTIME_STATES,
  MAP_RUNTIME_TRUST_STATE_REASONS,
} from "@kfm/maplibre";

const REASONS = new Set<string>([
  ...Object.values(MAP_RUNTIME_TRUST_STATE_REASONS),
  "MAP_RUNTIME_DISPOSED",
  "MAP_RUNTIME_NOT_READY",
  "MAP_RUNTIME_CONTAINER_INVALID",
  "MAP_RUNTIME_INITIALIZATION_FAILED",
  "MAP_RUNTIME_CAMERA_INVALID",
  "MAP_RUNTIME_SELECTION_INVALID",
  "MAP_RUNTIME_STATE_INVALID",
  "MAP_RUNTIME_TERRAIN_TRANSITION_FAILED",
  "MAP_RUNTIME_TERRAIN_TRANSITION_CANCELLED",
  "MAP_RUNTIME_LISTENER_INVALID",
]);

export function formatRendererDiagnostic(input: unknown): string {
  try {
    if (input === null || typeof input !== "object") {
      return "Renderer ERROR · MAP_RUNTIME_STATE_INVALID";
    }
    const value = input as Record<string, unknown>;
    const { profile, state, reason } = value;
    if (profile !== MAP_RUNTIME_PORT_PROFILE ||
        !MAP_RUNTIME_STATES.some((known) => known === state)) {
      return "Renderer ERROR · MAP_RUNTIME_STATE_INVALID";
    }
    if (reason !== null && (typeof reason !== "string" || !REASONS.has(reason))) {
      return "Renderer ERROR · MAP_RUNTIME_STATE_INVALID";
    }
    if ((state === "READY" || state === "IDLE" || state === "INITIALIZING") &&
        reason !== null) {
      return "Renderer ERROR · MAP_RUNTIME_STATE_INVALID";
    }
    return `Renderer ${state}${reason === null ? "" : ` · ${reason}`}`;
  } catch {
    // A malformed object, including a throwing property accessor, never leaks
    // its contents into public diagnostics.
    return "Renderer ERROR · MAP_RUNTIME_STATE_INVALID";
  }
}
