/**
 * Renderer-neutral browser map boundary accepted by ADR-0006.
 *
 * These values are KFM-owned and serializable. They intentionally expose no
 * MapLibre classes, events, layers, sources, styles, workers, protocols, or
 * renderer errors. The port has no evidence, policy, review, release, source,
 * lifecycle, correction, deployment, or publication authority.
 */
export const MAP_RUNTIME_PORT_PROFILE = "kfm.map-runtime-port.v1" as const;
export const MAP_FEATURE_SELECTION_PROFILE =
  "kfm.explorer.map-feature-selection.v1" as const;

export const MAP_RUNTIME_STATES = [
  "IDLE",
  "INITIALIZING",
  "READY",
  "STALE",
  "ABSTAINED",
  "DENIED",
  "CONFLICT",
  "DEGRADED",
  "WITHDRAWN",
  "ROLLED_BACK",
  "ERROR",
  "DISPOSED",
] as const;

export type MapRuntimeState = (typeof MAP_RUNTIME_STATES)[number];

export const MAP_RUNTIME_TRUST_STATES = [
  "STALE",
  "ABSTAINED",
  "DENIED",
  "CONFLICT",
  "DEGRADED",
  "WITHDRAWN",
  "ROLLED_BACK",
  "ERROR",
] as const;

export type MapRuntimeTrustState =
  (typeof MAP_RUNTIME_TRUST_STATES)[number];

/**
 * Renderer-neutral reason codes for observed upstream trust/runtime states.
 *
 * These codes report a state already supplied to the runtime. They do not
 * make evidence, policy, review, correction, release, or rollback decisions.
 */
export const MAP_RUNTIME_TRUST_STATE_REASONS = Object.freeze({
  STALE: "MAP_RUNTIME_STALE",
  ABSTAINED: "MAP_RUNTIME_ABSTAINED",
  DENIED: "MAP_RUNTIME_DENIED",
  CONFLICT: "MAP_RUNTIME_CONFLICT",
  DEGRADED: "MAP_RUNTIME_DEGRADED",
  WITHDRAWN: "MAP_RUNTIME_WITHDRAWN",
  ROLLED_BACK: "MAP_RUNTIME_ROLLED_BACK",
  ERROR: "MAP_RUNTIME_ERROR",
} as const satisfies Record<MapRuntimeTrustState, string>);

export type MapRuntimeTrustStateReasonCode =
  (typeof MAP_RUNTIME_TRUST_STATE_REASONS)[MapRuntimeTrustState];

export type MapRuntimeCamera = Readonly<{
  longitude: number;
  latitude: number;
  zoom: number;
  bearing: number;
  pitch: number;
}>;

export type MapFeatureSelection = Readonly<{
  profile: typeof MAP_FEATURE_SELECTION_PROFILE;
  selectionId: string;
  layerId: string;
  featureId: string;
  evidenceRefs: readonly string[];
}>;

export type MapRuntimeReasonCode =
  | MapRuntimeTrustStateReasonCode
  | "MAP_RUNTIME_DISPOSED"
  | "MAP_RUNTIME_NOT_READY"
  | "MAP_RUNTIME_CONTAINER_INVALID"
  | "MAP_RUNTIME_INITIALIZATION_FAILED"
  | "MAP_RUNTIME_CAMERA_INVALID"
  | "MAP_RUNTIME_SELECTION_INVALID"
  | "MAP_RUNTIME_STATE_INVALID"
  | "MAP_RUNTIME_TERRAIN_TRANSITION_FAILED"
  | "MAP_RUNTIME_LISTENER_INVALID";

export type MapRuntimeSnapshot = Readonly<{
  profile: typeof MAP_RUNTIME_PORT_PROFILE;
  state: MapRuntimeState;
  camera: MapRuntimeCamera;
  selection: MapFeatureSelection | null;
  reason: MapRuntimeReasonCode | null;
}>;

export type MapRuntimeSelectionListener = (
  selection: MapFeatureSelection,
) => void;

export type MapRuntimeSnapshotListener = (
  snapshot: MapRuntimeSnapshot,
) => void;

/**
 * Minimal renderer-neutral consumer contract.
 *
 * A future concrete MapLibreAdapter may implement this interface only from the
 * packages/maplibre acquisition seam after separate dependency admission.
 */
export interface MapRuntimePort {
  readonly profile: typeof MAP_RUNTIME_PORT_PROFILE;

  initialize(initialCamera?: MapRuntimeCamera): Promise<MapRuntimeSnapshot>;
  getSnapshot(): MapRuntimeSnapshot;
  setCamera(camera: MapRuntimeCamera): MapRuntimeSnapshot;
  subscribeSnapshot(listener: MapRuntimeSnapshotListener): () => void;
  subscribeSelection(listener: MapRuntimeSelectionListener): () => void;
  dispose(): void;
}

const CAMERA_FIELDS = new Set([
  "longitude",
  "latitude",
  "zoom",
  "bearing",
  "pitch",
]);
const SELECTION_FIELDS = new Set([
  "profile",
  "selectionId",
  "layerId",
  "featureId",
  "evidenceRefs",
]);
const SAFE_ID = /^[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}$/;
const MAX_EVIDENCE_REFS = 16;
const MAX_MERCATOR_LATITUDE = 85.051129;

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

function isSafeId(value: unknown): value is string {
  return typeof value === "string" && SAFE_ID.test(value);
}

export function isMapRuntimeCamera(value: unknown): value is MapRuntimeCamera {
  if (!isRecord(value) || !hasExactFields(value, CAMERA_FIELDS)) return false;
  if (!isFiniteNumber(value.longitude) || value.longitude < -180 || value.longitude > 180) {
    return false;
  }
  if (
    !isFiniteNumber(value.latitude) ||
    value.latitude < -MAX_MERCATOR_LATITUDE ||
    value.latitude > MAX_MERCATOR_LATITUDE
  ) {
    return false;
  }
  if (!isFiniteNumber(value.zoom) || value.zoom < 0 || value.zoom > 24) return false;
  if (!isFiniteNumber(value.bearing) || value.bearing < -180 || value.bearing > 180) {
    return false;
  }
  return isFiniteNumber(value.pitch) && value.pitch >= 0 && value.pitch <= 85;
}

export function isMapFeatureSelection(
  value: unknown,
): value is MapFeatureSelection {
  if (!isRecord(value) || !hasExactFields(value, SELECTION_FIELDS)) return false;
  if (value.profile !== MAP_FEATURE_SELECTION_PROFILE) return false;
  if (!isSafeId(value.selectionId)) return false;
  if (!isSafeId(value.layerId)) return false;
  if (!isSafeId(value.featureId)) return false;
  if (!Array.isArray(value.evidenceRefs) || value.evidenceRefs.length > MAX_EVIDENCE_REFS) {
    return false;
  }
  if (!value.evidenceRefs.every(isSafeId)) return false;
  return new Set(value.evidenceRefs).size === value.evidenceRefs.length;
}

export function isMapRuntimeTrustState(
  value: unknown,
): value is MapRuntimeTrustState {
  return (
    typeof value === "string" &&
    (MAP_RUNTIME_TRUST_STATES as readonly string[]).includes(value)
  );
}

export function reasonForMapRuntimeTrustState(
  state: MapRuntimeTrustState,
): MapRuntimeTrustStateReasonCode {
  if (!isMapRuntimeTrustState(state)) {
    throw new MapRuntimePortError(
      "MAP_RUNTIME_STATE_INVALID",
      "Map runtime trust state is invalid.",
    );
  }
  return MAP_RUNTIME_TRUST_STATE_REASONS[state];
}

export function freezeMapRuntimeCamera(
  camera: MapRuntimeCamera,
): MapRuntimeCamera {
  if (!isMapRuntimeCamera(camera)) {
    throw new MapRuntimePortError(
      "MAP_RUNTIME_CAMERA_INVALID",
      "Map runtime camera is invalid.",
    );
  }
  return Object.freeze({ ...camera });
}

export function freezeMapFeatureSelection(
  selection: MapFeatureSelection,
): MapFeatureSelection {
  if (!isMapFeatureSelection(selection)) {
    throw new MapRuntimePortError(
      "MAP_RUNTIME_SELECTION_INVALID",
      "Map feature selection is invalid.",
    );
  }
  return Object.freeze({
    ...selection,
    evidenceRefs: Object.freeze([...selection.evidenceRefs]),
  });
}

export class MapRuntimePortError extends Error {
  readonly code: MapRuntimeReasonCode;

  constructor(code: MapRuntimeReasonCode, message: string) {
    super(message);
    this.name = "MapRuntimePortError";
    this.code = code;
  }
}
