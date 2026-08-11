/**
 * Strict public-safe projection for the Pass 31 Watcher Registry browser.
 *
 * This adapter accepts a closed display projection. It never reads the
 * control-plane registry, dereferences endpoints, runs a watcher, evaluates
 * policy, writes lifecycle data, or authorizes release or publication.
 */

export const WATCHER_REGISTRY_BROWSER_PROJECTION_PROFILE =
  "kfm.explorer.watcher-registry-browser.public-safe.v1" as const;

export type WatcherRegistryBrowserOutcome =
  | "AVAILABLE"
  | "ABSTAIN"
  | "DENY"
  | "ERROR";

export type WatcherRegistryBrowserReasonCode =
  | "REGISTRY_AVAILABLE"
  | "REGISTRY_UNAVAILABLE"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";

export type WatcherRegistryEntryState =
  | "PLACEHOLDER"
  | "INACTIVE"
  | "SUSPENDED"
  | "RETIRED";

export type WatcherPollMode = "MANUAL_ONLY" | "SCHEDULED" | "EVENT_DRIVEN";

export type WatcherRegistryBrowserEntry = Readonly<{
  watcherId: string;
  canonicalId: string;
  version: string;
  state: WatcherRegistryEntryState;
  specRef: string;
  endpointRef: string | null;
  pollMode: WatcherPollMode;
  policyRef: string | null;
  outputTypes: readonly string[];
  schemaRef: string | null;
  specHash: string;
  signatureRef: string | null;
  reasonCodes: readonly string[];
}>;

export type WatcherRegistryBrowserGovernance = Readonly<{
  networkAttempted: false;
  registryMutationAllowed: false;
  watcherExecutionAllowed: false;
  sourceActivationAllowed: false;
  lifecycleWriteAllowed: false;
  releaseAuthorized: false;
  publicationAllowed: false;
}>;

export type GovernedWatcherRegistryBrowserProjection = Readonly<{
  profile: typeof WATCHER_REGISTRY_BROWSER_PROJECTION_PROFILE;
  outcome: WatcherRegistryBrowserOutcome;
  reasonCode: WatcherRegistryBrowserReasonCode;
  evaluatedAt: string | null;
  registryId: string | null;
  registrySpecHash: string | null;
  registryStatus: "PROPOSED_INACTIVE" | null;
  watchers: readonly WatcherRegistryBrowserEntry[];
  governance: WatcherRegistryBrowserGovernance;
}>;

export type WatcherRegistryBrowserProjectionResult =
  | Readonly<{ ok: true; payload: GovernedWatcherRegistryBrowserProjection }>
  | Readonly<{
      ok: false;
      code: "MALFORMED_WATCHER_REGISTRY_BROWSER_PROJECTION";
    }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "outcome",
  "reason_code",
  "evaluated_at",
  "registry_id",
  "registry_spec_hash",
  "registry_status",
  "watchers",
  "governance",
]);
const ENTRY_FIELDS = new Set([
  "watcher_id",
  "canonical_id",
  "version",
  "state",
  "spec_ref",
  "endpoint_ref",
  "poll_mode",
  "policy_ref",
  "output_types",
  "schema_ref",
  "spec_hash",
  "signature_ref",
  "reason_codes",
]);
const GOVERNANCE_FIELDS = new Set([
  "network_attempted",
  "registry_mutation_allowed",
  "watcher_execution_allowed",
  "source_activation_allowed",
  "lifecycle_write_allowed",
  "release_authorized",
  "publication_allowed",
]);

const OUTCOMES = new Set<WatcherRegistryBrowserOutcome>([
  "AVAILABLE",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const EXPECTED_REASON: Readonly<
  Record<WatcherRegistryBrowserOutcome, WatcherRegistryBrowserReasonCode>
> = Object.freeze({
  AVAILABLE: "REGISTRY_AVAILABLE",
  ABSTAIN: "REGISTRY_UNAVAILABLE",
  DENY: "POLICY_DENIED",
  ERROR: "UPSTREAM_ERROR",
});
const STATES = new Set<WatcherRegistryEntryState>([
  "PLACEHOLDER",
  "INACTIVE",
  "SUSPENDED",
  "RETIRED",
]);
const POLL_MODES = new Set<WatcherPollMode>([
  "MANUAL_ONLY",
  "SCHEDULED",
  "EVENT_DRIVEN",
]);

const WATCHER_ID = /^kfm\.watcher\.[a-z0-9][a-z0-9_.-]{2,126}$/;
const CANONICAL_ID = /^kfm:\/\/watcher\/[a-z0-9][a-z0-9/_-]{2,126}$/;
const KFM_REFERENCE = /^kfm:\/\/[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,315}$/;
const SPEC_REF = /^kfm:\/\/watcher-spec\/[a-z0-9][a-z0-9/_-]{2,180}$/;
const SHA256 = /^sha256:[a-f0-9]{64}$/;
const SEMVER = /^[0-9]+\.[0-9]+\.[0-9]+(?:-[a-z0-9.-]+)?$/;
const UPPER_CODE = /^[A-Z][A-Z0-9_]{2,63}$/;
const CANONICAL_TIMESTAMP = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;
const MAX_WATCHERS = 128;

function malformed(): WatcherRegistryBrowserProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_WATCHER_REGISTRY_BROWSER_PROJECTION",
  });
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

function isString(
  value: unknown,
  pattern: RegExp,
  maxLength = 320,
): value is string {
  return (
    typeof value === "string" &&
    value.length <= maxLength &&
    value === value.trim() &&
    pattern.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isCanonicalTimestamp(value: unknown): value is string {
  if (typeof value !== "string" || !CANONICAL_TIMESTAMP.test(value)) return false;
  const parsed = new Date(value);
  return (
    Number.isFinite(parsed.getTime()) &&
    parsed.toISOString().replace(".000Z", "Z") === value
  );
}

function parseNullableReference(value: unknown): string | null | undefined {
  if (value === null) return null;
  return isString(value, KFM_REFERENCE) ? value : undefined;
}

function parseCanonicalCodes(
  value: unknown,
  minimum: number,
  maximum: number,
): readonly string[] | null {
  if (!Array.isArray(value) || value.length < minimum || value.length > maximum) {
    return null;
  }
  if (!value.every((item) => isString(item, UPPER_CODE, 64))) return null;
  const codes = value as string[];
  if (codes.join("\n") !== [...new Set(codes)].sort().join("\n")) return null;
  return Object.freeze([...codes]);
}

function parseGovernance(input: unknown): WatcherRegistryBrowserGovernance | null {
  if (!isRecord(input) || !hasExactFields(input, GOVERNANCE_FIELDS)) return null;
  if (
    input.network_attempted !== false ||
    input.registry_mutation_allowed !== false ||
    input.watcher_execution_allowed !== false ||
    input.source_activation_allowed !== false ||
    input.lifecycle_write_allowed !== false ||
    input.release_authorized !== false ||
    input.publication_allowed !== false
  ) {
    return null;
  }
  return Object.freeze({
    networkAttempted: false,
    registryMutationAllowed: false,
    watcherExecutionAllowed: false,
    sourceActivationAllowed: false,
    lifecycleWriteAllowed: false,
    releaseAuthorized: false,
    publicationAllowed: false,
  });
}

function parseEntry(input: unknown): WatcherRegistryBrowserEntry | null {
  if (!isRecord(input) || !hasExactFields(input, ENTRY_FIELDS)) return null;
  if (
    !isString(input.watcher_id, WATCHER_ID, 128) ||
    !isString(input.canonical_id, CANONICAL_ID, 160) ||
    !isString(input.version, SEMVER, 64) ||
    typeof input.state !== "string" ||
    !STATES.has(input.state as WatcherRegistryEntryState) ||
    !isString(input.spec_ref, SPEC_REF, 192) ||
    typeof input.poll_mode !== "string" ||
    !POLL_MODES.has(input.poll_mode as WatcherPollMode) ||
    !isString(input.spec_hash, SHA256, 71)
  ) {
    return null;
  }

  const endpointRef = parseNullableReference(input.endpoint_ref);
  const policyRef = parseNullableReference(input.policy_ref);
  const schemaRef = parseNullableReference(input.schema_ref);
  const signatureRef = parseNullableReference(input.signature_ref);
  const outputTypes = parseCanonicalCodes(input.output_types, 0, 16);
  const reasonCodes = parseCanonicalCodes(input.reason_codes, 1, 16);
  if (
    endpointRef === undefined ||
    policyRef === undefined ||
    schemaRef === undefined ||
    signatureRef === undefined ||
    outputTypes === null ||
    reasonCodes === null
  ) {
    return null;
  }

  if (
    input.state === "PLACEHOLDER" &&
    (endpointRef !== null ||
      policyRef !== null ||
      schemaRef !== null ||
      signatureRef !== null ||
      outputTypes.length !== 0 ||
      input.poll_mode !== "MANUAL_ONLY")
  ) {
    return null;
  }
  if (
    (input.state === "SUSPENDED" || input.state === "RETIRED") &&
    input.poll_mode !== "MANUAL_ONLY"
  ) {
    return null;
  }

  return Object.freeze({
    watcherId: input.watcher_id,
    canonicalId: input.canonical_id,
    version: input.version,
    state: input.state as WatcherRegistryEntryState,
    specRef: input.spec_ref,
    endpointRef,
    pollMode: input.poll_mode as WatcherPollMode,
    policyRef,
    outputTypes,
    schemaRef,
    specHash: input.spec_hash,
    signatureRef,
    reasonCodes,
  });
}

/** Parse a closed Watcher Registry browser projection and reject drift. */
export function parseWatcherRegistryBrowserProjection(
  input: unknown,
): WatcherRegistryBrowserProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return malformed();
  }
  if (
    input.profile !== WATCHER_REGISTRY_BROWSER_PROJECTION_PROFILE ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as WatcherRegistryBrowserOutcome)
  ) {
    return malformed();
  }
  const outcome = input.outcome as WatcherRegistryBrowserOutcome;
  if (input.reason_code !== EXPECTED_REASON[outcome]) return malformed();
  const governance = parseGovernance(input.governance);
  if (governance === null || !Array.isArray(input.watchers)) return malformed();

  if (outcome !== "AVAILABLE") {
    if (
      input.evaluated_at !== null ||
      input.registry_id !== null ||
      input.registry_spec_hash !== null ||
      input.registry_status !== null ||
      input.watchers.length !== 0
    ) {
      return malformed();
    }
    return Object.freeze({
      ok: true,
      payload: Object.freeze({
        profile: WATCHER_REGISTRY_BROWSER_PROJECTION_PROFILE,
        outcome,
        reasonCode: EXPECTED_REASON[outcome],
        evaluatedAt: null,
        registryId: null,
        registrySpecHash: null,
        registryStatus: null,
        watchers: Object.freeze([]) as readonly WatcherRegistryBrowserEntry[],
        governance,
      }),
    });
  }

  if (
    !isCanonicalTimestamp(input.evaluated_at) ||
    input.registry_id !== "kfm://control-plane/watcher-registry/v1" ||
    !isString(input.registry_spec_hash, SHA256, 71) ||
    input.registry_status !== "PROPOSED_INACTIVE" ||
    input.watchers.length < 1 ||
    input.watchers.length > MAX_WATCHERS
  ) {
    return malformed();
  }

  const watchers: WatcherRegistryBrowserEntry[] = [];
  for (const item of input.watchers) {
    const parsed = parseEntry(item);
    if (parsed === null) return malformed();
    watchers.push(parsed);
  }
  const watcherIds = watchers.map((item) => item.watcherId);
  const canonicalIds = watchers.map((item) => item.canonicalId);
  if (
    watcherIds.join("\n") !== [...new Set(watcherIds)].sort().join("\n") ||
    canonicalIds.length !== new Set(canonicalIds).size
  ) {
    return malformed();
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: WATCHER_REGISTRY_BROWSER_PROJECTION_PROFILE,
      outcome,
      reasonCode: EXPECTED_REASON[outcome],
      evaluatedAt: input.evaluated_at,
      registryId: input.registry_id,
      registrySpecHash: input.registry_spec_hash,
      registryStatus: "PROPOSED_INACTIVE",
      watchers: Object.freeze(watchers),
      governance,
    }),
  });
}
