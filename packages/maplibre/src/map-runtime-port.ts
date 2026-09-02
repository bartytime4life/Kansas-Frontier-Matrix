export type MapRuntimeReasonCode =
  | "MAP_RUNTIME_STATE_INVALID"
  | "MAP_RUNTIME_TERRAIN_TRANSITION_FAILED"
  | "MAP_RUNTIME_TERRAIN_TRANSITION_CANCELLED"
  | "MAP_RUNTIME_DISPOSED";

export class MapRuntimePortError extends Error {
  readonly code: MapRuntimeReasonCode;

  constructor(code: MapRuntimeReasonCode, message: string) {
    super(message);
    this.name = "MapRuntimePortError";
    this.code = code;
  }
}
