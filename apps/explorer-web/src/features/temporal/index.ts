/*
 * Renderer-independent TemporalViewState conformance adapter.
 *
 * The Python validator and common JSON Schema remain the repository shape
 * authority. This module mirrors the closed profile for Explorer consumers,
 * preserves raw temporal values, and supplies the runtime generation guard.
 * It has no network, source-admission, evidence, policy, release, or publish
 * side effects.
 */

export const TEMPORAL_VIEW_STATE_PROFILE = "kfm.temporal.view-state.v1" as const;
export const TEMPORAL_VIEW_STATE_SCHEMA_VERSION = "1.0.0" as const;
export const TEMPORAL_QUERY_DISCLOSURE_PROFILE =
  "kfm.governance.temporal-query-disclosure.v1" as const;
export const TEMPORAL_FRAME_CONTEXT_PROFILE =
  "kfm.temporal.frame-context.v1" as const;

export type TemporalBoundaryProfile =
  | "instant"
  | "date_only"
  | "month"
  | "year"
  | "uncertain_range"
  | "geologic_age";
export type TemporalPrecision =
  | "unknown"
  | "second"
  | "minute"
  | "hour"
  | "day"
  | "month"
  | "year"
  | "range"
  | "geologic";
export type TemporalCalendar =
  | "GREGORIAN"
  | "JULIAN"
  | "EDTF"
  | "UNKNOWN"
  | "OTHER";
export type TemporalBoundStatus = "KNOWN" | "UNKNOWN" | "OPEN";
export type TemporalStatus = "SUPPORTED" | "UNSUPPORTED" | "ERROR";

export type TemporalUncertainty = Readonly<{
  kind: "APPROXIMATE" | "UNCERTAIN" | "RANGE";
  lower_raw: string | null;
  upper_raw: string | null;
}>;

export type TemporalBoundaryNormalization = Readonly<{
  status: "NONE" | "OFFSET_TO_UTC" | "CALENDAR_PRESERVED" | "UNSUPPORTED";
  provenance_ref: string | null;
}>;

export type TemporalBoundary = Readonly<{
  profile: TemporalBoundaryProfile;
  raw: string;
  normalized: string | null;
  precision: TemporalPrecision;
  source_timezone: string | null;
  calendar: TemporalCalendar;
  bound_status: TemporalBoundStatus;
  normalization: TemporalBoundaryNormalization;
  uncertainty: TemporalUncertainty | null;
}>;

export type TemporalSelection = Readonly<{
  selection_mode: "INSTANT" | "WINDOW";
  start: TemporalBoundary;
  end: TemporalBoundary | null;
  anchor: "START" | "END" | "CENTER";
  support_ref: string | null;
}>;

export type TemporalQuery = Readonly<{
  disclosure_profile: typeof TEMPORAL_QUERY_DISCLOSURE_PROFILE;
  query_class:
    | "CURRENT_STATE"
    | "PRIOR_STATE"
    | "SEQUENCED"
    | "NONSEQUENCED"
    | "TRACKING_LOG";
  time_basis: "VALID_TIME" | "TRANSACTION_TIME" | "BITEMPORAL" | "RELEASE_TIME";
  interval_semantics: "CLOSED" | "HALF_OPEN" | "OPEN";
  point_event_semantics: "AT_INSTANT" | "CONTAINS_INSTANT" | "UNKNOWN";
  master_time: "DECLARED_MASTER" | "INDEPENDENT_TRACKS";
  controlling_layer_id: string | null;
}>;

export type TemporalDisplay = Readonly<{
  mode:
    | "SNAPSHOT"
    | "MOVING_WINDOW"
    | "ACCUMULATION"
    | "EVENT_STEP"
    | "COMPARISON";
  step_rule: "NONE" | "REGULAR" | "CALENDAR" | "AVAILABLE_EVENT";
  direction: "FORWARD" | "BACKWARD";
  controlling_layer_id: string | null;
  missing_data_policy: "PAUSE" | "WITHHOLD_LAYER" | "PRESENTATION_SKIP";
  aggregate_semantics:
    | "NONE"
    | "EVENT_COUNT"
    | "UNIQUE_ENTITY_COUNT"
    | "INTEGRATED_QUANTITY"
    | "CURRENT_STATE";
  window_duration: string | null;
}>;

export type TemporalPresentation = Readonly<{
  speed: number;
  frame_rate: number;
  duration_ms: number;
  loop: boolean;
  reduced_motion: boolean;
  camera_easing: "NONE" | "LINEAR" | "DECORATIVE";
}>;

export type TemporalAsOf = Readonly<{
  knowledge_cutoff: string | null;
  release_ref: string | null;
  correction_policy: "AS_OF_CUTOFF" | "CURRENT_POLICY";
}>;

export type TemporalPins = Readonly<{
  dataset_version_refs: readonly string[];
  release_refs: readonly string[];
  pin_status: "PINNED" | "UNPINNED";
}>;

export type TemporalComparison = Readonly<{
  enabled: boolean;
  left: TemporalSelection | null;
  right: TemporalSelection | null;
  camera_lock: boolean;
  compatibility: "UNASSESSED" | "COMPATIBLE" | "QUALIFIED" | "INCOMPATIBLE";
}>;

export type TemporalRepresentation = Readonly<{
  color_scale: "STABLE" | "PER_FRAME" | "NOT_APPLICABLE";
  units: "SOURCE_UNITS" | "CONVERTED_WITH_PROVENANCE" | "INCOMPATIBLE";
  geometry: "NO_MORPHING" | "VERSIONED_CROSSWALK" | "STATIC_CONTEXT";
  accessible_alternative: "TABLE" | "TEXT" | "NONE";
}>;

export type TemporalSpatialScope = Readonly<{
  scope_type: "AOI" | "GLOBAL" | "LAYER_NATIVE";
  aoi_ref: string | null;
  geometry_ref: string | null;
  public_safe: true;
}>;

export type TemporalViewState = Readonly<{
  profile: typeof TEMPORAL_VIEW_STATE_PROFILE;
  schema_version: typeof TEMPORAL_VIEW_STATE_SCHEMA_VERSION;
  state_id: string;
  spatial_scope: TemporalSpatialScope;
  active_layer_ids: readonly string[];
  query: TemporalQuery;
  selection: TemporalSelection;
  display: TemporalDisplay;
  presentation: TemporalPresentation;
  as_of: TemporalAsOf;
  pins: TemporalPins;
  comparison: TemporalComparison;
  representation: TemporalRepresentation;
}>;

export type TemporalValidationResult = Readonly<{
  status: TemporalStatus;
  code: string;
  queryId: string | null;
}>;

const REF_PATTERN = /^[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}$/;
const AWARE_INSTANT =
  /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?(?:Z|[+-]\d{2}:\d{2})$/;
const NAIVE_INSTANT =
  /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?$/;
const DATE_ONLY = /^\d{4}-\d{2}-\d{2}$/;
const MONTH = /^\d{4}-\d{2}$/;
const YEAR = /^\d{4}$/;

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactKeys(
  value: Record<string, unknown>,
  keys: readonly string[],
): boolean {
  const expected = new Set(keys);
  const actual = Object.keys(value);
  return actual.length === expected.size && actual.every((key) => expected.has(key));
}

function canonicalize(value: unknown): unknown {
  if (Array.isArray(value)) return value.map(canonicalize);
  if (isRecord(value)) {
    const output: Record<string, unknown> = {};
    for (const key of Object.keys(value).sort()) {
      output[key] = canonicalize(value[key]);
    }
    return output;
  }
  return value;
}

export function canonicalTemporalJson(value: unknown): string {
  return JSON.stringify(canonicalize(value));
}

async function sha256Hex(value: string): Promise<string> {
  const cryptoApi = globalThis.crypto;
  if (!cryptoApi?.subtle) throw new Error("CRYPTO_UNAVAILABLE");
  const digest = await cryptoApi.subtle.digest(
    "SHA-256",
    new TextEncoder().encode(value),
  );
  return Array.from(new Uint8Array(digest))
    .map((byte) => byte.toString(16).padStart(2, "0"))
    .join("");
}

function withoutStateId(state: object): Record<string, unknown> {
  const value = { ...(state as Record<string, unknown>) };
  delete value.state_id;
  return value;
}

export async function deriveTemporalStateId(state: object): Promise<string> {
  const digest = await sha256Hex(canonicalTemporalJson(withoutStateId(state)));
  return "kfm:temporal-view-state:sha256:" + digest;
}

export async function deriveTemporalQueryId(state: object): Promise<string> {
  const value = state as Record<string, unknown>;
  const queryPayload: Record<string, unknown> = {};
  for (const key of [
    "profile",
    "schema_version",
    "query",
    "selection",
    "display",
    "as_of",
    "pins",
    "comparison",
  ]) {
    if (key in value) queryPayload[key] = value[key];
  }
  const digest = await sha256Hex(canonicalTemporalJson(queryPayload));
  return "kfm:temporal-query:sha256:" + digest;
}

export type TemporalBoundaryResult = Readonly<{
  status: TemporalStatus;
  code: string;
  profile: TemporalBoundaryProfile | null;
  raw: string | null;
  normalized: string | null;
}>;

export function normalizeTemporalBoundary(
  value: unknown,
): TemporalBoundaryResult {
  if (!isRecord(value)) {
    return {
      status: "ERROR",
      code: "BOUNDARY_REQUIRED",
      profile: null,
      raw: null,
      normalized: null,
    };
  }
  const profile = value.profile;
  const raw = value.raw;
  const normalized = value.normalized;
  if (
    typeof profile !== "string" ||
    ![
      "instant",
      "date_only",
      "month",
      "year",
      "uncertain_range",
      "geologic_age",
    ].includes(profile)
  ) {
    return {
      status: "ERROR",
      code: "BOUNDARY_PROFILE_INVALID",
      profile: null,
      raw: typeof raw === "string" ? raw : null,
      normalized: null,
    };
  }
  if (typeof raw !== "string" || raw.length === 0) {
    return { status: "ERROR", code: "BOUNDARY_RAW_REQUIRED", profile: profile as TemporalBoundaryProfile, raw: null, normalized: null };
  }
  if (normalized !== null && typeof normalized !== "string") {
    return { status: "ERROR", code: "NORMALIZED_TYPE_INVALID", profile: profile as TemporalBoundaryProfile, raw, normalized: null };
  }

  if (profile === "geologic_age") {
    if (normalized !== null) {
      return { status: "ERROR", code: "NORMALIZED_PRECISION_VIOLATION", profile, raw, normalized: null };
    }
    return { status: "UNSUPPORTED", code: "UNSUPPORTED_PROFILE", profile, raw, normalized: null };
  }

  if (profile === "instant") {
    if (NAIVE_INSTANT.test(raw)) {
      return { status: "UNSUPPORTED", code: "UNKNOWN_TIMEZONE", profile, raw, normalized: null };
    }
    if (!AWARE_INSTANT.test(raw)) {
      return { status: "ERROR", code: "INSTANT_SYNTAX_INVALID", profile, raw, normalized: null };
    }
    if (typeof normalized !== "string" || !AWARE_INSTANT.test(normalized)) {
      return { status: "ERROR", code: "NORMALIZED_INSTANT_INVALID", profile, raw, normalized: null };
    }
    const rawTime = Date.parse(raw);
    const normalizedTime = Date.parse(normalized);
    if (!Number.isFinite(rawTime) || !Number.isFinite(normalizedTime) || rawTime !== normalizedTime) {
      return { status: "ERROR", code: "NORMALIZATION_MISMATCH", profile, raw, normalized };
    }
    return { status: "SUPPORTED", code: "OK", profile, raw, normalized };
  }

  if (normalized !== null) {
    return { status: "ERROR", code: "NORMALIZED_PRECISION_VIOLATION", profile, raw, normalized: null };
  }
  if (
    (profile === "date_only" && !DATE_ONLY.test(raw)) ||
    (profile === "month" && !MONTH.test(raw)) ||
    (profile === "year" && !YEAR.test(raw))
  ) {
    return { status: "ERROR", code: "CALENDAR_SYNTAX_INVALID", profile, raw, normalized: null };
  }
  return { status: "SUPPORTED", code: "CALENDAR_PRESERVED", profile: profile as TemporalBoundaryProfile, raw, normalized: null };
}

function normalizeSelection(
  value: unknown,
): { status: TemporalStatus; code: string; start: TemporalBoundaryResult | null; end: TemporalBoundaryResult | null } {
  if (!isRecord(value)) {
    return { status: "ERROR", code: "SELECTION_REQUIRED", start: null, end: null };
  }
  if (value.selection_mode !== "INSTANT" && value.selection_mode !== "WINDOW") {
    return { status: "ERROR", code: "SELECTION_MODE_INVALID", start: null, end: null };
  }
  if (!["START", "END", "CENTER"].includes(String(value.anchor))) {
    return { status: "ERROR", code: "SELECTION_ANCHOR_INVALID", start: null, end: null };
  }
  if (value.support_ref !== null && (typeof value.support_ref !== "string" || !REF_PATTERN.test(value.support_ref))) {
    return { status: "ERROR", code: "SUPPORT_REF_INVALID", start: null, end: null };
  }
  const start = normalizeTemporalBoundary(value.start);
  const end = value.end === null ? null : normalizeTemporalBoundary(value.end);
  const results = [start, ...(end === null ? [] : [end])];
  const error = results.find((item) => item.status === "ERROR");
  if (error) return { status: "ERROR", code: error.code, start, end };
  const unsupported = results.find((item) => item.status === "UNSUPPORTED");
  if (unsupported) return { status: "UNSUPPORTED", code: unsupported.code, start, end };
  if (end && start.profile !== end.profile) {
    return { status: "ERROR", code: "MIXED_BOUNDARY_PROFILES", start, end };
  }
  if (end && start.normalized && end.normalized && Date.parse(start.normalized) > Date.parse(end.normalized)) {
    return { status: "ERROR", code: "REVERSED_INTERVAL", start, end };
  }
  if (end && start.profile === "date_only" && start.raw > end.raw) {
    return { status: "ERROR", code: "REVERSED_INTERVAL", start, end };
  }
  if (end && start.profile === "month" && start.raw > end.raw) {
    return { status: "ERROR", code: "REVERSED_INTERVAL", start, end };
  }
  if (end && start.profile === "year" && start.raw > end.raw) {
    return { status: "ERROR", code: "REVERSED_INTERVAL", start, end };
  }
  if (end && start.profile === "uncertain_range" && start.raw !== end.raw) {
    return { status: "UNSUPPORTED", code: "UNCERTAIN_ORDERING", start, end };
  }
  return { status: "SUPPORTED", code: "OK", start, end };
}

export async function normalizeTemporalQuery(
  state: object,
): Promise<TemporalValidationResult> {
  const value = state as Record<string, unknown>;
  const queryId = await deriveTemporalQueryId(state);
  const query = value.query;
  const display = value.display;
  const comparison = value.comparison;
  const pins = value.pins;
  const asOf = value.as_of;
  if (!isRecord(query) || !isRecord(display) || !isRecord(comparison) || !isRecord(pins) || !isRecord(asOf)) {
    return { status: "ERROR", code: "QUERY_MEMBER_INVALID", queryId: null };
  }
  if (query.disclosure_profile !== TEMPORAL_QUERY_DISCLOSURE_PROFILE) {
    return { status: "ERROR", code: "DISCLOSURE_PROFILE_INVALID", queryId: null };
  }
  if (![
    "CURRENT_STATE",
    "PRIOR_STATE",
    "SEQUENCED",
    "NONSEQUENCED",
    "TRACKING_LOG",
  ].includes(String(query.query_class))) {
    return { status: "ERROR", code: "QUERY_CLASS_INVALID", queryId: null };
  }
  if (!["VALID_TIME", "TRANSACTION_TIME", "BITEMPORAL", "RELEASE_TIME"].includes(String(query.time_basis))) {
    return { status: "ERROR", code: "TIME_BASIS_INVALID", queryId: null };
  }
  if (!["CLOSED", "HALF_OPEN", "OPEN"].includes(String(query.interval_semantics))) {
    return { status: "ERROR", code: "INTERVAL_SEMANTICS_INVALID", queryId: null };
  }
  if (!["AT_INSTANT", "CONTAINS_INSTANT", "UNKNOWN"].includes(String(query.point_event_semantics))) {
    return { status: "ERROR", code: "POINT_EVENT_SEMANTICS_INVALID", queryId: null };
  }
  if (!["DECLARED_MASTER", "INDEPENDENT_TRACKS"].includes(String(query.master_time))) {
    return { status: "ERROR", code: "MASTER_TIME_INVALID", queryId: null };
  }
  if (query.controlling_layer_id !== null && (typeof query.controlling_layer_id !== "string" || !REF_PATTERN.test(query.controlling_layer_id))) {
    return { status: "ERROR", code: "CONTROLLING_LAYER_INVALID", queryId: null };
  }

  const selectionResult = normalizeSelection(value.selection);
  if (selectionResult.status === "ERROR") {
    return { status: "ERROR", code: selectionResult.code, queryId: null };
  }
  if (selectionResult.status === "UNSUPPORTED") {
    return { status: "UNSUPPORTED", code: selectionResult.code, queryId };
  }

  const mode = display.mode;
  const stepRule = display.step_rule;
  if (!["SNAPSHOT", "MOVING_WINDOW", "ACCUMULATION", "EVENT_STEP", "COMPARISON"].includes(String(mode))) {
    return { status: "ERROR", code: "DISPLAY_MODE_INVALID", queryId: null };
  }
  if (!["NONE", "REGULAR", "CALENDAR", "AVAILABLE_EVENT"].includes(String(stepRule))) {
    return { status: "ERROR", code: "STEP_RULE_INVALID", queryId: null };
  }
  if (!["FORWARD", "BACKWARD"].includes(String(display.direction))) {
    return { status: "ERROR", code: "DIRECTION_INVALID", queryId: null };
  }
  if (!["PAUSE", "WITHHOLD_LAYER", "PRESENTATION_SKIP"].includes(String(display.missing_data_policy))) {
    return { status: "ERROR", code: "MISSING_DATA_POLICY_INVALID", queryId: null };
  }
  if (!["NONE", "EVENT_COUNT", "UNIQUE_ENTITY_COUNT", "INTEGRATED_QUANTITY", "CURRENT_STATE"].includes(String(display.aggregate_semantics))) {
    return { status: "ERROR", code: "AGGREGATE_INVALID", queryId: null };
  }
  if (display.window_duration !== null && (typeof display.window_duration !== "string" || display.window_duration.length === 0)) {
    return { status: "ERROR", code: "WINDOW_DURATION_INVALID", queryId: null };
  }

  if (mode === "SNAPSHOT" && stepRule !== "NONE") {
    return { status: "ERROR", code: "SNAPSHOT_STEP_INVALID", queryId: null };
  }
  if (mode === "MOVING_WINDOW" && (stepRule !== "REGULAR" && stepRule !== "CALENDAR" || value.selection && (value.selection as Record<string, unknown>).selection_mode !== "WINDOW" || display.window_duration === null)) {
    return { status: "ERROR", code: "MOVING_WINDOW_CONFIGURATION_INVALID", queryId: null };
  }
  if (mode === "ACCUMULATION" && display.aggregate_semantics === "NONE") {
    return { status: "ERROR", code: "ACCUMULATION_SEMANTICS_REQUIRED", queryId: null };
  }
  if (mode === "EVENT_STEP" && stepRule !== "AVAILABLE_EVENT") {
    return { status: "ERROR", code: "EVENT_STEP_RULE_REQUIRED", queryId: null };
  }
  if (mode === "COMPARISON") {
    if (comparison.enabled !== true || comparison.left === null || comparison.right === null) {
      return { status: "ERROR", code: "COMPARISON_SIDES_REQUIRED", queryId: null };
    }
    if (comparison.compatibility === "INCOMPATIBLE") {
      return { status: "ERROR", code: "COMPARISON_INCOMPATIBLE", queryId: null };
    }
    const left = normalizeSelection(comparison.left);
    const right = normalizeSelection(comparison.right);
    if (left.status === "ERROR" || right.status === "ERROR") {
      return { status: "ERROR", code: left.status === "ERROR" ? left.code : right.code, queryId: null };
    }
    if (left.status === "UNSUPPORTED" || right.status === "UNSUPPORTED") {
      return { status: "UNSUPPORTED", code: left.status === "UNSUPPORTED" ? left.code : right.code, queryId };
    }
  } else if (comparison.enabled === true) {
    return { status: "ERROR", code: "COMPARISON_MODE_REQUIRED", queryId: null };
  }

  if (pins.pin_status !== "PINNED" && pins.pin_status !== "UNPINNED") {
    return { status: "ERROR", code: "PIN_STATUS_INVALID", queryId: null };
  }
  if (!Array.isArray(pins.dataset_version_refs) || !Array.isArray(pins.release_refs)) {
    return { status: "ERROR", code: "PIN_REFS_INVALID", queryId: null };
  }
  if (pins.pin_status === "PINNED" && pins.dataset_version_refs.length === 0 && pins.release_refs.length === 0) {
    return { status: "ERROR", code: "PIN_REQUIRED_FOR_PINNED", queryId: null };
  }

  if (asOf.knowledge_cutoff !== null) {
    const cutoff = normalizeTemporalBoundary({
      profile: "instant",
      raw: asOf.knowledge_cutoff,
      normalized: asOf.knowledge_cutoff,
    });
    if (cutoff.status !== "SUPPORTED") {
      return {
        status: cutoff.status,
        code: cutoff.code,
        queryId: cutoff.status === "UNSUPPORTED" ? queryId : null,
      };
    }
  }
  return { status: "SUPPORTED", code: "OK", queryId };
}

export async function validateTemporalViewState(
  value: unknown,
): Promise<TemporalValidationResult> {
  if (!isRecord(value)) {
    return { status: "ERROR", code: "ROOT_OBJECT_REQUIRED", queryId: null };
  }
  if (
    !hasExactKeys(value, [
      "profile",
      "schema_version",
      "state_id",
      "spatial_scope",
      "active_layer_ids",
      "query",
      "selection",
      "display",
      "presentation",
      "as_of",
      "pins",
      "comparison",
      "representation",
    ])
  ) {
    return { status: "ERROR", code: "EXTRA_OR_MISSING_PROPERTY", queryId: null };
  }
  if (value.profile !== TEMPORAL_VIEW_STATE_PROFILE || value.schema_version !== TEMPORAL_VIEW_STATE_SCHEMA_VERSION) {
    return { status: "ERROR", code: "PROFILE_VERSION_INVALID", queryId: null };
  }
  if (typeof value.state_id !== "string" || !/^kfm:temporal-view-state:sha256:[a-f0-9]{64}$/.test(value.state_id)) {
    return { status: "ERROR", code: "STATE_ID_INVALID", queryId: null };
  }
  if (!isRecord(value.spatial_scope) || value.spatial_scope.public_safe !== true) {
    return { status: "ERROR", code: "SPATIAL_SCOPE_NOT_PUBLIC_SAFE", queryId: null };
  }
  if (!Array.isArray(value.active_layer_ids) || value.active_layer_ids.length === 0 || value.active_layer_ids.length > 32 || new Set(value.active_layer_ids).size !== value.active_layer_ids.length || !value.active_layer_ids.every((item) => typeof item === "string" && REF_PATTERN.test(item))) {
    return { status: "ERROR", code: "ACTIVE_LAYER_IDS_INVALID", queryId: null };
  }
  const expectedStateId = await deriveTemporalStateId(value);
  if (value.state_id !== expectedStateId) {
    return { status: "ERROR", code: "STATE_ID_MISMATCH", queryId: null };
  }
  return normalizeTemporalQuery(value);
}

export type TemporalFrameAvailability =
  | "AVAILABLE"
  | "WITHHELD"
  | "OUTSIDE_COVERAGE"
  | "UNAVAILABLE"
  | "EXPIRED"
  | "CORRECTED";
export type TemporalReleaseStatus =
  | "RELEASED"
  | "WITHHELD"
  | "REVOKED"
  | "UNRELEASED";

export type TemporalFrameLayer = Readonly<{
  layerId: string;
  actualTime: string | null;
  availability: TemporalFrameAvailability;
  evidenceRefs: readonly string[];
  sourceVersionRef: string | null;
  releaseStatus: TemporalReleaseStatus;
}>;

export type TemporalFrameContext = Readonly<{
  profile: typeof TEMPORAL_FRAME_CONTEXT_PROFILE;
  stateId: string;
  queryId: string;
  selectedSupport: Readonly<Record<string, unknown>>;
  layers: readonly TemporalFrameLayer[];
  datasetVersionRefs: readonly string[];
  releaseRefs: readonly string[];
  policyStatus: string;
  outcome: "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";
}>;

export function validateTemporalFrameContext(
  value: unknown,
): TemporalValidationResult {
  if (!isRecord(value)) {
    return { status: "ERROR", code: "FRAME_REQUIRED", queryId: null };
  }
  if (value.profile !== TEMPORAL_FRAME_CONTEXT_PROFILE) {
    return { status: "ERROR", code: "FRAME_PROFILE_INVALID", queryId: null };
  }
  if (value.outcome !== "ANSWER" && value.outcome !== "ABSTAIN") {
    return { status: "ERROR", code: "FRAME_OUTCOME_BLOCKED", queryId: null };
  }
  if (!Array.isArray(value.layers)) {
    return { status: "ERROR", code: "FRAME_LAYERS_REQUIRED", queryId: null };
  }
  const ids = new Set<string>();
  for (const layer of value.layers) {
    if (!isRecord(layer) || typeof layer.layerId !== "string" || ids.has(layer.layerId)) {
      return { status: "ERROR", code: "DUPLICATE_OR_INVALID_LAYER", queryId: null };
    }
    ids.add(layer.layerId);
    if (layer.availability === "AVAILABLE") {
      if (typeof layer.actualTime !== "string" || layer.actualTime.length === 0 || layer.releaseStatus !== "RELEASED") {
        return { status: "ERROR", code: "AVAILABLE_LAYER_INCOMPLETE", queryId: null };
      }
    } else if (layer.availability === "WITHHELD") {
      if (layer.actualTime !== null || !Array.isArray(layer.evidenceRefs) || layer.evidenceRefs.length !== 0) {
        return { status: "ERROR", code: "WITHHELD_DATA_LEAK", queryId: null };
      }
    } else if (
      layer.availability === "OUTSIDE_COVERAGE" ||
      layer.availability === "UNAVAILABLE" ||
      layer.availability === "EXPIRED" ||
      layer.availability === "CORRECTED"
    ) {
      if (layer.actualTime !== null) {
        return { status: "ERROR", code: "NONAVAILABLE_TIME_LEAK", queryId: null };
      }
    } else {
      return { status: "ERROR", code: "AVAILABILITY_INVALID", queryId: null };
    }
  }
  return { status: "SUPPORTED", code: "OK", queryId: null };
}

export type TemporalRuntimeStatus =
  | "IDLE"
  | "LOADING"
  | "COMMITTED"
  | "ERROR"
  | "UNSUPPORTED";

export type TemporalRuntimeState = Readonly<{
  generation: number;
  status: TemporalRuntimeStatus;
  requestedState: TemporalViewState | null;
  requestedQueryId: string | null;
  committedFrame: TemporalFrameContext | null;
  errorCode: string | null;
}>;

export type TemporalRuntimeEvent =
  | Readonly<{
      type: "REQUEST_FRAME";
      state: TemporalViewState;
      queryId: string;
    }>
  | Readonly<{
      type: "COMMIT_FRAME";
      generation: number;
      frame: TemporalFrameContext;
    }>
  | Readonly<{
      type: "FAIL_FRAME";
      generation: number;
      code: string;
    }>
  | Readonly<{ type: "RESET" }>;

export function createTemporalRuntimeState(): TemporalRuntimeState {
  return {
    generation: 0,
    status: "IDLE",
    requestedState: null,
    requestedQueryId: null,
    committedFrame: null,
    errorCode: null,
  };
}

export function reduceTemporalRuntime(
  runtime: TemporalRuntimeState,
  event: TemporalRuntimeEvent,
): TemporalRuntimeState {
  if (event.type === "RESET") return createTemporalRuntimeState();

  if (event.type === "REQUEST_FRAME") {
    return {
      generation: runtime.generation + 1,
      status: "LOADING",
      requestedState: event.state,
      requestedQueryId: event.queryId,
      committedFrame: runtime.committedFrame,
      errorCode: null,
    };
  }

  if (event.generation !== runtime.generation) return runtime;

  if (event.type === "FAIL_FRAME") {
    return { ...runtime, status: "ERROR", errorCode: event.code };
  }

  if (
    runtime.requestedState === null ||
    runtime.requestedQueryId === null ||
    event.frame.queryId !== runtime.requestedQueryId ||
    event.frame.stateId !== runtime.requestedState.state_id
  ) {
    return runtime;
  }

  const frameResult = validateTemporalFrameContext(event.frame);
  if (frameResult.status !== "SUPPORTED") {
    return { ...runtime, status: "ERROR", errorCode: frameResult.code };
  }
  return {
    ...runtime,
    status: "COMMITTED",
    committedFrame: event.frame,
    errorCode: null,
  };
}
