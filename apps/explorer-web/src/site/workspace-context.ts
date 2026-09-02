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
