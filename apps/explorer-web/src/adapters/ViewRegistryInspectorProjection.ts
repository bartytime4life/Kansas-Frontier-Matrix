/**
 * Strict app-local adapter for a public-safe View Registry inspection projection.
 *
 * The browser receives only proposed route metadata, governed references, finite
 * render hints, policy labels, and inactive-state markers. It never receives
 * store endpoints, embedded queries, credentials, source payloads, geometry,
 * activation controls, or release controls.
 */

export const VIEW_REGISTRY_INSPECTOR_PROJECTION_PROFILE =
  "kfm.explorer.view-registry-inspector.public-safe.v1" as const;

export type ViewRegistryInspectionOutcome =
  | "AVAILABLE"
  | "ABSTAIN"
  | "DENY"
  | "ERROR";

export type ViewRegistryInspectionStatus =
  | "READY"
  | "HELD"
  | "DENIED"
  | "UPSTREAM_ERROR";

export type ViewRegistryInspectionReason =
  | "REGISTRY_READY"
  | "REGISTRY_HELD"
  | "REGISTRY_DENIED"
  | "REGISTRY_ERROR";

export type ViewRegistryDeliveryKind =
  | "GOVERNED_API_CONTRACT"
  | "RELEASED_ARTIFACT_CONTRACT";

export type ViewRegistryProtocol = "PMTILES" | "MVT" | "COG" | "NONE";

export type GovernedViewRegistryEntry = Readonly<{
  viewId: string;
  routePath: string;
  deliveryKind: ViewRegistryDeliveryKind;
  contractRef: string;
  catalogClosureState: "READY";
  layerManifestRefs: readonly string[];
  renderer: "MAPLIBRE_2D";
  protocol: ViewRegistryProtocol;
  styleRef: string;
  performanceBudgetRef: string;
  accessPolicyRef: string;
  sensitivityPolicyRef: string;
  evidenceDrawerProfileRef: string;
  releaseManifestRef: string;
  activationState: "PROPOSED_INACTIVE";
}>;

export type GovernedViewRegistryInspectionProjection = Readonly<{
  profile: typeof VIEW_REGISTRY_INSPECTOR_PROJECTION_PROFILE;
  outcome: ViewRegistryInspectionOutcome;
  status: ViewRegistryInspectionStatus;
  reasonCode: ViewRegistryInspectionReason;
  registryId: string | null;
  specHash: string | null;
  entries: readonly GovernedViewRegistryEntry[];
  evaluatedAt: string;
}>;

export type ViewRegistryInspectionProjectionResult =
  | Readonly<{
      ok: true;
      payload: GovernedViewRegistryInspectionProjection;
    }>
  | Readonly<{
      ok: false;
      code: "MALFORMED_VIEW_REGISTRY_INSPECTION_PROJECTION";
    }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "outcome",
  "status",
  "reason_code",
  "registry_id",
  "spec_hash",
  "entries",
  "evaluated_at",
]);

const ENTRY_FIELDS = new Set([
  "view_id",
  "route_path",
  "delivery_kind",
  "contract_ref",
  "catalog_closure_state",
  "layer_manifest_refs",
  "renderer",
  "protocol",
  "style_ref",
  "performance_budget_ref",
  "access_policy_ref",
  "sensitivity_policy_ref",
  "evidence_drawer_profile_ref",
  "release_manifest_ref",
  "activation_state",
]);

const STATUS_BINDING = Object.freeze({
  READY: Object.freeze({
    outcome: "AVAILABLE",
    reasonCode: "REGISTRY_READY",
  }),
  HELD: Object.freeze({
    outcome: "ABSTAIN",
    reasonCode: "REGISTRY_HELD",
  }),
  DENIED: Object.freeze({
    outcome: "DENY",
    reasonCode: "REGISTRY_DENIED",
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR",
    reasonCode: "REGISTRY_ERROR",
  }),
}) satisfies Readonly<
  Record<
    ViewRegistryInspectionStatus,
    Readonly<{
      outcome: ViewRegistryInspectionOutcome;
      reasonCode: ViewRegistryInspectionReason;
    }>
  >
>;

const DELIVERY_KINDS = new Set<ViewRegistryDeliveryKind>([
  "GOVERNED_API_CONTRACT",
  "RELEASED_ARTIFACT_CONTRACT",
]);
const PROTOCOLS = new Set<ViewRegistryProtocol>([
  "PMTILES",
  "MVT",
  "COG",
  "NONE",
]);
const SHA256 = /^sha256:[a-f0-9]{64}$/;
const REGISTRY_ID = /^kfm:view-registry:[a-f0-9]{24}$/;
const VIEW_ID = /^kfm:view:[a-z0-9][a-z0-9._-]{2,96}$/;
const ROUTE_PATH = /^\/[a-z0-9][a-z0-9-]*(?:\/[a-z0-9][a-z0-9-]*)*$/;
const KFM_REFERENCE = /^kfm:[a-z0-9][a-z0-9:._/-]{5,240}$/;
const CANONICAL_UTC_SECOND =
  /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER =
  /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;
const DENIED_REFERENCE_MARKERS = [
  "postgres://",
  "neo4j://",
  "s3://",
  "file://",
  "graph_query",
  "cypher:",
  "select *",
  "match (",
] as const;
const INTERNAL_DATA_STORE_LANES = new Set([
  "raw",
  "work",
  "quarantine",
  "processed",
  "published",
]);
const MAX_ENTRIES = 32;
const MAX_LAYER_REFS = 16;

function malformed(): ViewRegistryInspectionProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_VIEW_REGISTRY_INSPECTION_PROJECTION",
  });
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  allowed: ReadonlySet<string>,
): boolean {
  return (
    Object.keys(value).length === allowed.size &&
    Object.keys(value).every((field) => allowed.has(field))
  );
}

function isCanonicalUtcSecond(value: unknown): value is string {
  if (typeof value !== "string" || !CANONICAL_UTC_SECOND.test(value)) {
    return false;
  }
  const parsed = Date.parse(value);
  return (
    Number.isFinite(parsed) &&
    new Date(parsed).toISOString().replace(".000Z", "Z") === value
  );
}

function hasInternalDataStorePath(value: string): boolean {
  const segments = value.split("/");
  return segments.some((segment, index) => {
    if (index === 0 || !INTERNAL_DATA_STORE_LANES.has(segment)) {
      return false;
    }
    const previous = segments[index - 1];
    return previous === "data" || previous.endsWith(":data");
  });
}

function isSafeReference(value: unknown): value is string {
  if (
    typeof value !== "string" ||
    value.length > 256 ||
    !KFM_REFERENCE.test(value) ||
    CONTROL_CHARACTER.test(value)
  ) {
    return false;
  }
  const lowered = value.toLowerCase();
  return (
    !hasInternalDataStorePath(lowered) &&
    !DENIED_REFERENCE_MARKERS.some((marker) => lowered.includes(marker))
  );
}

function parseLayerRefs(value: unknown): readonly string[] | null {
  if (
    !Array.isArray(value) ||
    value.length < 1 ||
    value.length > MAX_LAYER_REFS ||
    !value.every(isSafeReference)
  ) {
    return null;
  }
  const references = value as string[];
  if (
    new Set(references).size !== references.length ||
    references.some(
      (item, index) => index > 0 && references[index - 1] >= item,
    )
  ) {
    return null;
  }
  return Object.freeze([...references]);
}

function parseEntry(value: unknown): GovernedViewRegistryEntry | null {
  if (!isRecord(value) || !hasExactFields(value, ENTRY_FIELDS)) {
    return null;
  }
  if (
    typeof value.view_id !== "string" ||
    !VIEW_ID.test(value.view_id) ||
    typeof value.route_path !== "string" ||
    !ROUTE_PATH.test(value.route_path) ||
    typeof value.delivery_kind !== "string" ||
    !DELIVERY_KINDS.has(value.delivery_kind as ViewRegistryDeliveryKind) ||
    value.catalog_closure_state !== "READY" ||
    value.renderer !== "MAPLIBRE_2D" ||
    typeof value.protocol !== "string" ||
    !PROTOCOLS.has(value.protocol as ViewRegistryProtocol) ||
    value.activation_state !== "PROPOSED_INACTIVE"
  ) {
    return null;
  }

  const references = [
    value.contract_ref,
    value.style_ref,
    value.performance_budget_ref,
    value.access_policy_ref,
    value.sensitivity_policy_ref,
    value.evidence_drawer_profile_ref,
    value.release_manifest_ref,
  ];
  if (!references.every(isSafeReference)) {
    return null;
  }
  const layerManifestRefs = parseLayerRefs(value.layer_manifest_refs);
  if (layerManifestRefs === null) {
    return null;
  }

  return Object.freeze({
    viewId: value.view_id,
    routePath: value.route_path,
    deliveryKind: value.delivery_kind as ViewRegistryDeliveryKind,
    contractRef: value.contract_ref as string,
    catalogClosureState: "READY",
    layerManifestRefs,
    renderer: "MAPLIBRE_2D",
    protocol: value.protocol as ViewRegistryProtocol,
    styleRef: value.style_ref as string,
    performanceBudgetRef: value.performance_budget_ref as string,
    accessPolicyRef: value.access_policy_ref as string,
    sensitivityPolicyRef: value.sensitivity_policy_ref as string,
    evidenceDrawerProfileRef: value.evidence_drawer_profile_ref as string,
    releaseManifestRef: value.release_manifest_ref as string,
    activationState: "PROPOSED_INACTIVE",
  });
}

function parseEntries(
  value: unknown,
): readonly GovernedViewRegistryEntry[] | null {
  if (!Array.isArray(value) || value.length < 1 || value.length > MAX_ENTRIES) {
    return null;
  }
  const parsed = value.map(parseEntry);
  if (parsed.some((entry) => entry === null)) {
    return null;
  }
  const entries = parsed as GovernedViewRegistryEntry[];
  const viewIds = entries.map((entry) => entry.viewId);
  const routes = entries.map((entry) => entry.routePath);
  if (
    viewIds.some((item, index) => index > 0 && viewIds[index - 1] >= item) ||
    new Set(viewIds).size !== viewIds.length ||
    new Set(routes).size !== routes.length
  ) {
    return null;
  }
  return Object.freeze([...entries]);
}

/**
 * Parse one closed projection emitted after upstream registry validation.
 *
 * A successful parse proves browser-local closure only. It does not resolve a
 * reference, bind a route, activate a layer, evaluate policy, or release a view.
 */
export function parseViewRegistryInspectionProjection(
  input: unknown,
): ViewRegistryInspectionProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return malformed();
  }
  if (
    input.profile !== VIEW_REGISTRY_INSPECTOR_PROJECTION_PROFILE ||
    typeof input.status !== "string" ||
    !Object.hasOwn(STATUS_BINDING, input.status) ||
    !isCanonicalUtcSecond(input.evaluated_at)
  ) {
    return malformed();
  }

  const status = input.status as ViewRegistryInspectionStatus;
  const binding = STATUS_BINDING[status];
  if (
    input.outcome !== binding.outcome ||
    input.reason_code !== binding.reasonCode
  ) {
    return malformed();
  }

  if (binding.outcome !== "AVAILABLE") {
    if (
      input.registry_id !== null ||
      input.spec_hash !== null ||
      !Array.isArray(input.entries) ||
      input.entries.length !== 0
    ) {
      return malformed();
    }
    return Object.freeze({
      ok: true,
      payload: Object.freeze({
        profile: VIEW_REGISTRY_INSPECTOR_PROJECTION_PROFILE,
        outcome: binding.outcome,
        status,
        reasonCode: binding.reasonCode,
        registryId: null,
        specHash: null,
        entries: Object.freeze([]),
        evaluatedAt: input.evaluated_at,
      }),
    });
  }

  if (
    typeof input.registry_id !== "string" ||
    !REGISTRY_ID.test(input.registry_id) ||
    typeof input.spec_hash !== "string" ||
    !SHA256.test(input.spec_hash) ||
    input.registry_id.slice("kfm:view-registry:".length) !==
      input.spec_hash.slice("sha256:".length, "sha256:".length + 24)
  ) {
    return malformed();
  }
  const entries = parseEntries(input.entries);
  if (entries === null) {
    return malformed();
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: VIEW_REGISTRY_INSPECTOR_PROJECTION_PROFILE,
      outcome: binding.outcome,
      status,
      reasonCode: binding.reasonCode,
      registryId: input.registry_id,
      specHash: input.spec_hash,
      entries,
      evaluatedAt: input.evaluated_at,
    }),
  });
}
