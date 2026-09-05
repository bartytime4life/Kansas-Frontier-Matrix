import { deriveTemporalStateId, type TemporalViewState } from "../features/temporal";
import {
  freezeMapFeatureSelection,
  freezeMapRuntimeCamera,
  isMapFeatureSelection,
  isMapRuntimeCamera,
  type MapFeatureSelection,
  type MapRuntimeCamera,
} from "@kfm/maplibre";
import { KNOWLEDGE_DOMAINS } from "./catalog";
import {
  findPublicWorkspace,
  findPublicWorkspaceByHash,
  isPublicWorkspaceId,
  type PublicWorkspaceId,
} from "./workspace-registry";

/** UI-owned public context projection. It is not a semantic or release contract. */
export const PUBLIC_WORKSPACE_CONTEXT_PROFILE =
  "kfm.explorer.public-workspace-context.v1" as const;
export const PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM = "kfm-context" as const;

export const PUBLIC_WORKSPACE_COMPARE_MODES = [
  "NONE",
  "SIDE_BY_SIDE",
  "SWIPE",
  "DIFF",
  "SMALL_MULTIPLES",
] as const;

export type PublicWorkspaceCompareMode =
  (typeof PUBLIC_WORKSPACE_COMPARE_MODES)[number];

export type PublicWorkspaceTimeContext = Readonly<{
  validAt: string | null;
  observedAt: string | null;
  asOf: string | null;
  releaseId: string | null;
}>;

export type PublicWorkspaceCompareContext = Readonly<{
  mode: PublicWorkspaceCompareMode;
  leftContextId: string | null;
  rightContextId: string | null;
}>;

export type PublicWorkspaceContext = Readonly<{
  profile: typeof PUBLIC_WORKSPACE_CONTEXT_PROFILE;
  workspaceId: PublicWorkspaceId;
  domainIds: readonly string[];
  placeIds: readonly string[];
  layerIds: readonly string[];
  camera: MapRuntimeCamera | null;
  selection: MapFeatureSelection | null;
  time: PublicWorkspaceTimeContext;
  compare: PublicWorkspaceCompareContext;
  storyNodeId: string | null;
  publicSafe: true;
}>;

const CONTEXT_FIELDS = new Set([
  "profile",
  "workspaceId",
  "domainIds",
  "placeIds",
  "layerIds",
  "camera",
  "selection",
  "time",
  "compare",
  "storyNodeId",
  "publicSafe",
]);
const TIME_FIELDS = new Set([
  "validAt",
  "observedAt",
  "asOf",
  "releaseId",
]);
const COMPARE_FIELDS = new Set([
  "mode",
  "leftContextId",
  "rightContextId",
]);
const DOMAIN_IDS = new Set(KNOWLEDGE_DOMAINS.map((entry) => entry.id));
const COMPARE_MODES = new Set<string>(PUBLIC_WORKSPACE_COMPARE_MODES);
const SAFE_ID = /^[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}$/;
const ISO_TEMPORAL =
  /^\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?(?:Z|[+-]\d{2}:\d{2}))?$/;
const MAX_CONTEXT_JSON_LENGTH = 8192;
const MAX_DOMAIN_IDS = 13;
const MAX_PLACE_IDS = 16;
const MAX_LAYER_IDS = 32;

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  fields: ReadonlySet<string>,
): boolean {
  const keys = Object.keys(value);
  return keys.length === fields.size && keys.every((key) => fields.has(key));
}

function isSafeId(value: unknown): value is string {
  return typeof value === "string" && SAFE_ID.test(value);
}

function parseIdArray(
  value: unknown,
  maximum: number,
  allowed?: ReadonlySet<string>,
): readonly string[] | null {
  if (!Array.isArray(value) || value.length > maximum) return null;
  if (!value.every(isSafeId)) return null;
  if (new Set(value).size !== value.length) return null;
  if (allowed && !value.every((entry) => allowed.has(entry))) return null;
  return Object.freeze([...value]);
}

function parseTemporal(value: unknown): string | null | undefined {
  if (value === null) return null;
  if (
    typeof value !== "string" ||
    value.length > 64 ||
    !ISO_TEMPORAL.test(value)
  ) {
    return undefined;
  }
  const instant = value.length === 10 ? `${value}T00:00:00Z` : value;
  return Number.isNaN(Date.parse(instant)) ? undefined : value;
}

function parseNullableId(value: unknown): string | null | undefined {
  if (value === null) return null;
  return isSafeId(value) ? value : undefined;
}

function parseTime(value: unknown): PublicWorkspaceTimeContext | null {
  if (!isRecord(value) || !hasExactFields(value, TIME_FIELDS)) return null;
  const validAt = parseTemporal(value.validAt);
  const observedAt = parseTemporal(value.observedAt);
  const asOf = parseTemporal(value.asOf);
  const releaseId = parseNullableId(value.releaseId);
  if (
    validAt === undefined ||
    observedAt === undefined ||
    asOf === undefined ||
    releaseId === undefined
  ) {
    return null;
  }
  return Object.freeze({ validAt, observedAt, asOf, releaseId });
}

function parseCompare(value: unknown): PublicWorkspaceCompareContext | null {
  if (!isRecord(value) || !hasExactFields(value, COMPARE_FIELDS)) return null;
  if (typeof value.mode !== "string" || !COMPARE_MODES.has(value.mode)) {
    return null;
  }
  const leftContextId = parseNullableId(value.leftContextId);
  const rightContextId = parseNullableId(value.rightContextId);
  if (leftContextId === undefined || rightContextId === undefined) return null;

  if (value.mode === "NONE") {
    if (leftContextId !== null || rightContextId !== null) return null;
  } else if (
    leftContextId === null ||
    rightContextId === null ||
    leftContextId === rightContextId
  ) {
    return null;
  }

  return Object.freeze({
    mode: value.mode as PublicWorkspaceCompareMode,
    leftContextId,
    rightContextId,
  });
}

/**
 * Strictly parse the UI-owned context projection. Unknown and extra fields
 * fail closed so private prompts, reviewer notes, restricted coordinates, or
 * other privileged payloads cannot hitchhike here. URL-specific functions
 * apply the additional evidence-reference exclusion below.
 */
export function parsePublicWorkspaceContext(
  value: unknown,
): PublicWorkspaceContext | null {
  if (!isRecord(value) || !hasExactFields(value, CONTEXT_FIELDS)) return null;
  if (value.profile !== PUBLIC_WORKSPACE_CONTEXT_PROFILE) return null;
  if (!isPublicWorkspaceId(value.workspaceId)) return null;
  if (value.publicSafe !== true) return null;

  const domainIds = parseIdArray(value.domainIds, MAX_DOMAIN_IDS, DOMAIN_IDS);
  const placeIds = parseIdArray(value.placeIds, MAX_PLACE_IDS);
  const layerIds = parseIdArray(value.layerIds, MAX_LAYER_IDS);
  if (domainIds === null || placeIds === null || layerIds === null) return null;

  let camera: MapRuntimeCamera | null = null;
  if (value.camera !== null) {
    if (!isMapRuntimeCamera(value.camera)) return null;
    camera = freezeMapRuntimeCamera(value.camera);
  }

  let selection: MapFeatureSelection | null = null;
  if (value.selection !== null) {
    if (!isMapFeatureSelection(value.selection)) return null;
    selection = freezeMapFeatureSelection(value.selection);
    if (!layerIds.includes(selection.layerId)) return null;
  }

  const time = parseTime(value.time);
  const compare = parseCompare(value.compare);
  const storyNodeId = parseNullableId(value.storyNodeId);
  if (time === null || compare === null || storyNodeId === undefined) return null;

  return Object.freeze({
    profile: PUBLIC_WORKSPACE_CONTEXT_PROFILE,
    workspaceId: value.workspaceId,
    domainIds,
    placeIds,
    layerIds,
    camera,
    selection,
    time,
    compare,
    storyNodeId,
    publicSafe: true,
  });
}

/**
 * Evidence references require governed release and access proof that this
 * browser-owned projection cannot establish. Keep them available for bounded
 * in-memory context transfer, but fail closed at every shareable URL boundary.
 */
function isPublicUrlSafeContext(context: PublicWorkspaceContext): boolean {
  return (
    context.selection === null ||
    (context.selection.evidenceRefs.length === 0 &&
      (context.selection.historyEvidenceRefs?.length ?? 0) === 0)
  );
}

/** Serialize one canonical context into the versioned query parameter. */
export function serializePublicWorkspaceContext(
  value: unknown,
): string | null {
  const context = parsePublicWorkspaceContext(value);
  if (!context || !isPublicUrlSafeContext(context)) return null;
  const json = JSON.stringify(context);
  if (json.length > MAX_CONTEXT_JSON_LENGTH) return null;
  const params = new URLSearchParams();
  params.set(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM, json);
  return params.toString();
}

/** Parse only the KFM context parameter; unrelated public URL parameters remain allowed. */
export function parsePublicWorkspaceContextQuery(
  value: string | URLSearchParams,
): PublicWorkspaceContext | null {
  const params =
    typeof value === "string"
      ? new URLSearchParams(value.startsWith("?") ? value.slice(1) : value)
      : value;
  const candidates = params.getAll(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM);
  if (candidates.length !== 1 || candidates[0].length > MAX_CONTEXT_JSON_LENGTH) {
    return null;
  }
  try {
    const context = parsePublicWorkspaceContext(JSON.parse(candidates[0]));
    return context && isPublicUrlSafeContext(context) ? context : null;
  } catch {
    return null;
  }
}

/**
 * Clone a URL, write the canonical public context, and retain the existing
 * section-anchor navigation contract for backward compatibility.
 */
export function withPublicWorkspaceContext(
  baseUrl: URL,
  value: unknown,
): URL | null {
  const context = parsePublicWorkspaceContext(value);
  if (!context || !isPublicUrlSafeContext(context)) return null;
  const workspace = findPublicWorkspace(context.workspaceId);
  if (!workspace) return null;
  const json = JSON.stringify(context);
  if (json.length > MAX_CONTEXT_JSON_LENGTH) return null;

  const next = new URL(baseUrl.toString());
  next.searchParams.set(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM, json);
  next.hash = workspace.href;
  return next;
}

/** Parse a deep link and reject a context whose anchor names another workspace. */
export function parsePublicWorkspaceContextUrl(
  url: URL,
): PublicWorkspaceContext | null {
  const context = parsePublicWorkspaceContextQuery(url.searchParams);
  if (!context) return null;
  const workspace = findPublicWorkspaceByHash(url.hash);
  return workspace?.id === context.workspaceId ? context : null;
}


const ADAPTER_AWARE_INSTANT =
  /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?(?:Z|[+-]\d{2}:\d{2})$/;
const ADAPTER_DATE_ONLY = /^\d{4}-\d{2}-\d{2}$/;
const ADAPTER_MONTH = /^\d{4}-\d{2}$/;
const ADAPTER_YEAR = /^\d{4}$/;
const TEMPORAL_ADAPTER_PROVENANCE =
  "kfm:normalization:adapter:temporal-view-state-v1";

export type PublicWorkspaceTemporalStateResult = Readonly<{
  status: "SUPPORTED" | "UNSUPPORTED" | "ERROR";
  code: string;
  state: TemporalViewState | null;
}>;

function adapterBoundary(raw: string): TemporalViewState["selection"]["start"] {
  if (ADAPTER_AWARE_INSTANT.test(raw)) {
    return {
      profile: "instant",
      raw,
      normalized: raw,
      precision: "second",
      source_timezone: raw.endsWith("Z") ? "UTC" : raw.slice(-6),
      calendar: "GREGORIAN",
      bound_status: "KNOWN",
      normalization: {
        status: "OFFSET_TO_UTC",
        provenance_ref: TEMPORAL_ADAPTER_PROVENANCE,
      },
      uncertainty: null,
    };
  }
  if (ADAPTER_DATE_ONLY.test(raw)) {
    return {
      profile: "date_only",
      raw,
      normalized: null,
      precision: "day",
      source_timezone: null,
      calendar: "GREGORIAN",
      bound_status: "KNOWN",
      normalization: {
        status: "CALENDAR_PRESERVED",
        provenance_ref: TEMPORAL_ADAPTER_PROVENANCE,
      },
      uncertainty: null,
    };
  }
  if (ADAPTER_MONTH.test(raw)) {
    return {
      profile: "month",
      raw,
      normalized: null,
      precision: "month",
      source_timezone: null,
      calendar: "GREGORIAN",
      bound_status: "KNOWN",
      normalization: {
        status: "CALENDAR_PRESERVED",
        provenance_ref: TEMPORAL_ADAPTER_PROVENANCE,
      },
      uncertainty: null,
    };
  }
  if (ADAPTER_YEAR.test(raw)) {
    return {
      profile: "year",
      raw,
      normalized: null,
      precision: "year",
      source_timezone: null,
      calendar: "GREGORIAN",
      bound_status: "KNOWN",
      normalization: {
        status: "CALENDAR_PRESERVED",
        provenance_ref: TEMPORAL_ADAPTER_PROVENANCE,
      },
      uncertainty: null,
    };
  }
  return {
    profile: "uncertain_range",
    raw,
    normalized: null,
    precision: "range",
    source_timezone: null,
    calendar: "EDTF",
    bound_status: "KNOWN",
    normalization: {
      status: "CALENDAR_PRESERVED",
      provenance_ref: TEMPORAL_ADAPTER_PROVENANCE,
    },
    uncertainty: {
      kind: "UNCERTAIN",
      lower_raw: raw,
      upper_raw: raw,
    },
  };
}

/**
 * Compose an existing browser-safe workspace projection into the shared
 * temporal state successor. This is an adapter only: it carries no raw
 * evidence, source URL, privileged option, authority, or release decision.
 */
export async function buildTemporalViewStateFromPublicContext(
  context: PublicWorkspaceContext,
): Promise<PublicWorkspaceTemporalStateResult> {
  const raw = context.time.validAt ?? context.time.observedAt;
  if (raw === null) {
    return {
      status: "UNSUPPORTED",
      code: "NO_TEMPORAL_SELECTION",
      state: null,
    };
  }
  if (context.layerIds.length === 0) {
    return {
      status: "ERROR",
      code: "ACTIVE_LAYER_REQUIRED",
      state: null,
    };
  }
  if (context.compare.mode !== "NONE") {
    return {
      status: "UNSUPPORTED",
      code: "COMPARISON_REQUIRES_TEMPORAL_SIDES",
      state: null,
    };
  }
  if (context.time.asOf !== null && !ADAPTER_AWARE_INSTANT.test(context.time.asOf)) {
    return {
      status: "UNSUPPORTED",
      code: "AS_OF_REQUIRES_ZONED_INSTANT",
      state: null,
    };
  }

  const stateWithoutId = {
    profile: "kfm.temporal.view-state.v1",
    schema_version: "1.0.0",
    state_id: "",
    spatial_scope: {
      scope_type: context.placeIds.length > 0 ? "AOI" : "LAYER_NATIVE",
      aoi_ref: context.placeIds[0] ?? null,
      geometry_ref: null,
      public_safe: true,
    },
    active_layer_ids: [...context.layerIds],
    query: {
      disclosure_profile: "kfm.governance.temporal-query-disclosure.v1",
      query_class: "CURRENT_STATE",
      time_basis: "VALID_TIME",
      interval_semantics: "HALF_OPEN",
      point_event_semantics: "AT_INSTANT",
      master_time: "DECLARED_MASTER",
      controlling_layer_id: null,
    },
    selection: {
      selection_mode: "INSTANT",
      start: adapterBoundary(raw),
      end: null,
      anchor: "START",
      support_ref: context.selection?.selectionId ?? null,
    },
    display: {
      mode: "SNAPSHOT",
      step_rule: "NONE",
      direction: "FORWARD",
      controlling_layer_id: null,
      missing_data_policy: "PAUSE",
      aggregate_semantics: "NONE",
      window_duration: null,
    },
    presentation: {
      speed: 1,
      frame_rate: 30,
      duration_ms: 0,
      loop: false,
      reduced_motion: false,
      camera_easing: "NONE",
    },
    as_of: {
      knowledge_cutoff: context.time.asOf,
      release_ref: context.time.releaseId,
      correction_policy: "CURRENT_POLICY",
    },
    pins: {
      dataset_version_refs: [],
      release_refs: context.time.releaseId ? [context.time.releaseId] : [],
      pin_status: context.time.releaseId ? "PINNED" : "UNPINNED",
    },
    comparison: {
      enabled: false,
      left: null,
      right: null,
      camera_lock: true,
      compatibility: "UNASSESSED",
    },
    representation: {
      color_scale: "STABLE",
      units: "SOURCE_UNITS",
      geometry: "NO_MORPHING",
      accessible_alternative: "TABLE",
    },
  } as unknown as TemporalViewState;

  const state_id = await deriveTemporalStateId(stateWithoutId);
  return {
    status: "SUPPORTED",
    code: "OK",
    state: Object.freeze({ ...stateWithoutId, state_id }),
  };
}
