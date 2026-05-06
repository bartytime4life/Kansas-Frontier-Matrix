// apps/web/src/ecology/evidenceBundle.ts

export const ECOLOGY_EVIDENCE_SCHEMA_VERSION = "v1" as const;
export const ECOLOGY_EVIDENCE_OBJECT_TYPE = "EvidenceBundle" as const;
export const ECOLOGY_DOMAIN = "ecology" as const;

export type EcologyEvidenceBundleRightsStatus =
  | "public"
  | "open"
  | "controlled"
  | "restricted"
  | "unknown";

export type EcologyEvidenceBundleSensitivity =
  | "public"
  | "generalize"
  | "restricted"
  | "review_required";

export type EcologyEvidenceBundleResolutionState =
  | "resolved"
  | "partial"
  | "unresolved"
  | "denied";

export type EcologyEvidenceBundleReviewState =
  | "unreviewed"
  | "review_required"
  | "reviewed"
  | "approved"
  | "rejected";

export type EcologyEvidenceBundleReleaseState =
  | "draft"
  | "candidate"
  | "published"
  | "superseded"
  | "withdrawn";

export type EcologyEvidenceBundleCorrectionState =
  | "none"
  | "corrected"
  | "superseded"
  | "withdrawn";

export type EcologyEvidenceBundleVisibility =
  | "public"
  | "generalized"
  | "review_required"
  | "restricted";

export type EcologyEvidenceBundleFiniteOutcome =
  | "ANSWER"
  | "ABSTAIN"
  | "DENY"
  | "ERROR";

export type EcologyEvidenceBundleArtifact = {
  role?: string;
  uri?: string;
  media_type?: string;
  digest?: string;
  [key: string]: unknown;
};

export type EcologyEvidenceBundle = {
  schema_version: typeof ECOLOGY_EVIDENCE_SCHEMA_VERSION;
  object_type: typeof ECOLOGY_EVIDENCE_OBJECT_TYPE;

  /**
   * May be a local id, a kfm:// ref, or another stable evidence-bundle URI.
   * The fetcher extracts the final safe route id from the caller's bundleRef.
   */
  bundle_id: string;
  bundle_ref?: string;

  domain: typeof ECOLOGY_DOMAIN;

  /**
   * `resolved` is the canonical boolean used by the current ecology slice.
   * `evidence_bundle_resolved` is kept for compatibility with existing KFM
   * payloads and should match `resolved` when present.
   */
  resolved: boolean;
  evidence_bundle_resolved?: boolean;
  resolution_state?: EcologyEvidenceBundleResolutionState;

  policy_label: string;
  rights_status: EcologyEvidenceBundleRightsStatus;
  sensitivity: EcologyEvidenceBundleSensitivity;
  spec_hash: string;

  claim_refs?: string[];
  source_refs?: string[];
  dataset_refs?: string[];
  evidence_refs?: string[];
  object_refs?: string[];
  catalog_refs?: string[];
  release_refs?: string[];
  validation_report_refs?: string[];
  review_record_refs?: string[];
  correction_notice_refs?: string[];
  artifact_digests?: string[];

  artifacts?: EcologyEvidenceBundleArtifact[];
  artifact_count?: number;

  review_state?: EcologyEvidenceBundleReviewState;
  release_state?: EcologyEvidenceBundleReleaseState;
  correction_state?: EcologyEvidenceBundleCorrectionState;

  rights_summary?: string;
  sensitivity_summary?: string;

  generated_at?: string;
  resolved_at?: string;
  expires_at?: string;
  stale?: boolean;

  limitations?: string[];
  notes?: string[];
  warnings?: string[];
};

export type EcologyEvidenceBundleSummary = {
  bundle_id: string;
  resolved: boolean;
  resolution_state: EcologyEvidenceBundleResolutionState;
  policy_label: string;
  rights_status: EcologyEvidenceBundleRightsStatus;
  sensitivity: EcologyEvidenceBundleSensitivity;
  visibility: EcologyEvidenceBundleVisibility;
  spec_hash: string;
  source_count: number;
  dataset_count: number;
  evidence_count: number;
  object_count: number;
  artifact_count: number;
  limitation_count: number;
  warning_count: number;
  stale: boolean;
};

export type EcologyEvidenceDrawerEvidence = {
  bundle_id: string;
  bundle_ref: string;
  resolved: boolean;
  resolution_state: EcologyEvidenceBundleResolutionState;
  visibility: EcologyEvidenceBundleVisibility;
  policy_label: string;
  rights_status: EcologyEvidenceBundleRightsStatus;
  sensitivity: EcologyEvidenceBundleSensitivity;
  spec_hash: string;
  source_refs: string[];
  dataset_refs: string[];
  evidence_refs: string[];
  object_refs: string[];
  catalog_refs: string[];
  release_refs: string[];
  limitations: string[];
  notes: string[];
  warnings: string[];
  artifacts: EcologyEvidenceBundleArtifact[];
};

export type FetchEcologyEvidenceBundleOptions = {
  apiBase?: string;
  signal?: AbortSignal;
  headers?: HeadersInit;
  credentials?: RequestCredentials;
  cache?: RequestCache;

  /**
   * Test hook. Keeps this module easy to fixture-test without mocking global fetch.
   */
  fetcher?: typeof fetch;

  /**
   * Keep true unless the backend intentionally allows aliases that return a
   * different bundle_id from the requested ref.
   */
  validateResponseId?: boolean;

  /**
   * When true, tryFetchEcologyEvidenceBundle returns DENY for bundles whose
   * rights/sensitivity state should not be displayed in an ordinary public UI.
   * fetchEcologyEvidenceBundle itself still returns the validated bundle.
   */
  publicOnly?: boolean;
};

export type EcologyEvidenceBundleFetchResult =
  | {
      outcome: "ANSWER";
      bundle_id: string;
      bundle: EcologyEvidenceBundle;
      visibility: EcologyEvidenceBundleVisibility;
      retrieved_at: string;
    }
  | {
      outcome: "ABSTAIN" | "DENY" | "ERROR";
      bundle_id?: string;
      bundle?: EcologyEvidenceBundle;
      visibility?: EcologyEvidenceBundleVisibility;
      status?: number;
      reason: string;
      error?: EcologyEvidenceBundleError;
      retrieved_at: string;
    };

type EcologyEvidenceBundleErrorOptions = {
  bundleRef?: string;
  bundleId?: string;
  status?: number;
  statusText?: string;
  bodySnippet?: string;
  validationErrors?: string[];
  outcome?: Exclude<EcologyEvidenceBundleFiniteOutcome, "ANSWER">;
  cause?: unknown;
};

export class EcologyEvidenceBundleError extends Error {
  readonly bundleRef?: string;
  readonly bundleId?: string;
  readonly status?: number;
  readonly statusText?: string;
  readonly bodySnippet?: string;
  readonly validationErrors?: string[];
  readonly outcome: Exclude<EcologyEvidenceBundleFiniteOutcome, "ANSWER">;
  readonly cause?: unknown;

  constructor(message: string, options: EcologyEvidenceBundleErrorOptions = {}) {
    super(message);
    this.name = "EcologyEvidenceBundleError";
    this.bundleRef = options.bundleRef;
    this.bundleId = options.bundleId;
    this.status = options.status;
    this.statusText = options.statusText;
    this.bodySnippet = options.bodySnippet;
    this.validationErrors = options.validationErrors;
    this.outcome = options.outcome ?? "ERROR";
    this.cause = options.cause;
  }
}

export class EcologyEvidenceBundleRefError extends EcologyEvidenceBundleError {
  constructor(message: string, options: EcologyEvidenceBundleErrorOptions = {}) {
    super(message, { ...options, outcome: options.outcome ?? "ABSTAIN" });
    this.name = "EcologyEvidenceBundleRefError";
  }
}

export class EcologyEvidenceBundleHttpError extends EcologyEvidenceBundleError {
  constructor(message: string, options: EcologyEvidenceBundleErrorOptions = {}) {
    super(message, options);
    this.name = "EcologyEvidenceBundleHttpError";
  }
}

export class EcologyEvidenceBundleValidationError extends EcologyEvidenceBundleError {
  constructor(message: string, options: EcologyEvidenceBundleErrorOptions = {}) {
    super(message, { ...options, outcome: options.outcome ?? "ABSTAIN" });
    this.name = "EcologyEvidenceBundleValidationError";
  }
}

const SAFE_BUNDLE_ID_RE = /^[A-Za-z0-9][A-Za-z0-9._:-]{0,255}$/;

const RIGHTS_STATUSES = new Set<string>([
  "public",
  "open",
  "controlled",
  "restricted",
  "unknown",
]);

const SENSITIVITY_VALUES = new Set<string>([
  "public",
  "generalize",
  "restricted",
  "review_required",
]);

const RESOLUTION_STATES = new Set<string>([
  "resolved",
  "partial",
  "unresolved",
  "denied",
]);

const REVIEW_STATES = new Set<string>([
  "unreviewed",
  "review_required",
  "reviewed",
  "approved",
  "rejected",
]);

const RELEASE_STATES = new Set<string>([
  "draft",
  "candidate",
  "published",
  "superseded",
  "withdrawn",
]);

const CORRECTION_STATES = new Set<string>([
  "none",
  "corrected",
  "superseded",
  "withdrawn",
]);

const OPTIONAL_STRING_ARRAY_FIELDS: Array<keyof EcologyEvidenceBundle> = [
  "claim_refs",
  "source_refs",
  "dataset_refs",
  "evidence_refs",
  "object_refs",
  "catalog_refs",
  "release_refs",
  "validation_report_refs",
  "review_record_refs",
  "correction_notice_refs",
  "artifact_digests",
  "limitations",
  "notes",
  "warnings",
];

const OPTIONAL_STRING_FIELDS: Array<keyof EcologyEvidenceBundle> = [
  "bundle_ref",
  "rights_summary",
  "sensitivity_summary",
  "generated_at",
  "resolved_at",
  "expires_at",
];

export function extractEcologyEvidenceBundleId(bundleRef: string): string {
  const cleaned = bundleRef.trim();

  if (!cleaned) {
    throw new EcologyEvidenceBundleRefError("Invalid EvidenceBundle ref: empty value", {
      bundleRef,
    });
  }

  if (!cleaned.includes("/") && SAFE_BUNDLE_ID_RE.test(cleaned)) {
    return cleaned;
  }

  let pathOrId = cleaned;

  try {
    const url = new URL(cleaned, "https://kfm.local");
    pathOrId = url.pathname || cleaned;
  } catch {
    pathOrId = cleaned;
  }

  const withoutQuery = pathOrId.split(/[?#]/, 1)[0].replace(/\/+$/, "");
  const rawCandidate = withoutQuery.split("/").filter(Boolean).pop();

  if (!rawCandidate) {
    throw new EcologyEvidenceBundleRefError("Invalid EvidenceBundle ref: missing id", {
      bundleRef,
    });
  }

  let candidate: string;

  try {
    candidate = decodeURIComponent(rawCandidate);
  } catch (cause) {
    throw new EcologyEvidenceBundleRefError(
      "Invalid EvidenceBundle ref: malformed URI encoding",
      { bundleRef, cause },
    );
  }

  if (!SAFE_BUNDLE_ID_RE.test(candidate)) {
    throw new EcologyEvidenceBundleRefError(
      "Invalid EvidenceBundle ref: unsafe id characters",
      { bundleRef, bundleId: candidate },
    );
  }

  return candidate;
}

export function buildEcologyEvidenceBundleUrl(
  bundleId: string,
  apiBase = "/api",
): string {
  const base = apiBase.replace(/\/+$/, "");
  return `${base}/ecology/evidence/${encodeURIComponent(bundleId)}`;
}

export async function fetchEcologyEvidenceBundle(
  bundleRef: string,
  apiBaseOrOptions: string | FetchEcologyEvidenceBundleOptions = "/api",
): Promise<EcologyEvidenceBundle> {
  const options = normalizeFetchOptions(apiBaseOrOptions);
  const bundleId = extractEcologyEvidenceBundleId(bundleRef);
  const url = buildEcologyEvidenceBundleUrl(bundleId, options.apiBase ?? "/api");

  const fetchImpl = options.fetcher ?? globalThis.fetch?.bind(globalThis);

  if (!fetchImpl) {
    throw new EcologyEvidenceBundleError("Fetch API is not available", {
      bundleRef,
      bundleId,
      outcome: "ERROR",
    });
  }

  let response: Response;

  try {
    response = await fetchImpl(url, {
      method: "GET",
      signal: options.signal,
      headers: withDefaultJsonAccept(options.headers),
      credentials: options.credentials,
      cache: options.cache,
    });
  } catch (cause) {
    throw new EcologyEvidenceBundleError("Failed to load EvidenceBundle", {
      bundleRef,
      bundleId,
      outcome: "ERROR",
      cause,
    });
  }

  if (!response.ok) {
    throw await buildHttpError(response, bundleRef, bundleId);
  }

  let payload: unknown;

  try {
    payload = await response.json();
  } catch (cause) {
    throw new EcologyEvidenceBundleValidationError(
      "EvidenceBundle response was not valid JSON",
      { bundleRef, bundleId, cause },
    );
  }

  const bundle = parseEcologyEvidenceBundle(
    unwrapEcologyEvidenceBundlePayload(payload),
    { bundleRef, bundleId },
  );

  if (options.validateResponseId !== false) {
    validateReturnedBundleId(bundle, bundleRef, bundleId);
  }

  return bundle;
}

/**
 * Safe variant for UI state machines. This keeps negative states explicit instead
 * of forcing callers to infer policy/validation/network failures from thrown errors.
 */
export async function tryFetchEcologyEvidenceBundle(
  bundleRef: string,
  apiBaseOrOptions: string | FetchEcologyEvidenceBundleOptions = "/api",
): Promise<EcologyEvidenceBundleFetchResult> {
  const options = normalizeFetchOptions(apiBaseOrOptions);
  const retrieved_at = new Date().toISOString();

  let bundleId: string | undefined;

  try {
    bundleId = extractEcologyEvidenceBundleId(bundleRef);
    const bundle = await fetchEcologyEvidenceBundle(bundleRef, options);
    const visibility = getEcologyEvidenceBundleVisibility(bundle);

    if (bundle.resolution_state === "denied") {
      return {
        outcome: "DENY",
        bundle_id: bundleId,
        bundle,
        visibility,
        reason: "EvidenceBundle resolution was denied by policy.",
        retrieved_at,
      };
    }

    if (!isEcologyEvidenceBundleResolved(bundle)) {
      return {
        outcome: "ABSTAIN",
        bundle_id: bundleId,
        bundle,
        visibility,
        reason: "EvidenceBundle is not fully resolved.",
        retrieved_at,
      };
    }

    if (
      options.publicOnly === true &&
      (visibility === "restricted" || visibility === "review_required")
    ) {
      return {
        outcome: "DENY",
        bundle_id: bundleId,
        bundle,
        visibility,
        reason:
          "EvidenceBundle rights or sensitivity state blocks ordinary public display.",
        retrieved_at,
      };
    }

    return {
      outcome: "ANSWER",
      bundle_id: bundleId,
      bundle,
      visibility,
      retrieved_at,
    };
  } catch (cause) {
    const error = normalizeEcologyEvidenceBundleError(cause, bundleRef, bundleId);

    return {
      outcome: error.outcome,
      bundle_id: error.bundleId ?? bundleId,
      status: error.status,
      reason: error.message,
      error,
      retrieved_at,
    };
  }
}

export function parseEcologyEvidenceBundle(
  value: unknown,
  context: { bundleRef?: string; bundleId?: string } = {},
): EcologyEvidenceBundle {
  const errors = validateEcologyEvidenceBundle(value);

  if (errors.length > 0) {
    throw new EcologyEvidenceBundleValidationError(
      "Invalid Ecology EvidenceBundle payload",
      {
        ...context,
        validationErrors: errors,
      },
    );
  }

  const record = value as EcologyEvidenceBundle;

  return {
    ...record,
    source_refs: record.source_refs ?? [],
    dataset_refs: record.dataset_refs ?? [],
    evidence_refs: record.evidence_refs ?? [],
    object_refs: record.object_refs ?? [],
    catalog_refs: record.catalog_refs ?? [],
    release_refs: record.release_refs ?? [],
    limitations: record.limitations ?? [],
    notes: record.notes ?? [],
    warnings: record.warnings ?? [],
    artifacts: record.artifacts ?? [],
    evidence_bundle_resolved:
      record.evidence_bundle_resolved ?? record.resolved,
    resolution_state:
      record.resolution_state ?? (record.resolved ? "resolved" : "unresolved"),
  };
}

export function validateEcologyEvidenceBundle(value: unknown): string[] {
  const errors: string[] = [];

  if (!isRecord(value)) {
    return ["payload must be an object"];
  }

  requireLiteral(
    value,
    "schema_version",
    ECOLOGY_EVIDENCE_SCHEMA_VERSION,
    errors,
  );
  requireLiteral(value, "object_type", ECOLOGY_EVIDENCE_OBJECT_TYPE, errors);
  requireLiteral(value, "domain", ECOLOGY_DOMAIN, errors);

  requireNonEmptyString(value, "bundle_id", errors);
  requireNonEmptyString(value, "policy_label", errors);
  requireNonEmptyString(value, "spec_hash", errors);

  if (typeof value.resolved !== "boolean") {
    errors.push("resolved must be a boolean");
  }

  if (
    value.evidence_bundle_resolved !== undefined &&
    typeof value.evidence_bundle_resolved !== "boolean"
  ) {
    errors.push("evidence_bundle_resolved must be a boolean when present");
  }

  if (
    typeof value.resolved === "boolean" &&
    typeof value.evidence_bundle_resolved === "boolean" &&
    value.resolved !== value.evidence_bundle_resolved
  ) {
    errors.push("resolved and evidence_bundle_resolved must not disagree");
  }

  requireEnum(value, "rights_status", RIGHTS_STATUSES, errors);
  requireEnum(value, "sensitivity", SENSITIVITY_VALUES, errors);

  optionalEnum(value, "resolution_state", RESOLUTION_STATES, errors);
  optionalEnum(value, "review_state", REVIEW_STATES, errors);
  optionalEnum(value, "release_state", RELEASE_STATES, errors);
  optionalEnum(value, "correction_state", CORRECTION_STATES, errors);

  for (const field of OPTIONAL_STRING_ARRAY_FIELDS) {
    const v = value[field];

    if (v !== undefined && !isStringArray(v)) {
      errors.push(`${String(field)} must be an array of strings when present`);
    }
  }

  for (const field of OPTIONAL_STRING_FIELDS) {
    const v = value[field];

    if (v !== undefined && typeof v !== "string") {
      errors.push(`${String(field)} must be a string when present`);
    }
  }

  if (value.stale !== undefined && typeof value.stale !== "boolean") {
    errors.push("stale must be a boolean when present");
  }

  if (value.artifact_count !== undefined && typeof value.artifact_count !== "number") {
    errors.push("artifact_count must be a number when present");
  }

  if (value.artifacts !== undefined && !Array.isArray(value.artifacts)) {
    errors.push("artifacts must be an array when present");
  }

  return errors;
}

export function isEcologyEvidenceBundleResolved(
  bundle: EcologyEvidenceBundle,
): boolean {
  if (bundle.resolution_state) {
    return bundle.resolution_state === "resolved";
  }

  return bundle.resolved === true && bundle.evidence_bundle_resolved !== false;
}

export function getEcologyEvidenceBundleVisibility(
  bundle: EcologyEvidenceBundle,
): EcologyEvidenceBundleVisibility {
  if (
    bundle.rights_status === "restricted" ||
    bundle.sensitivity === "restricted"
  ) {
    return "restricted";
  }

  if (
    bundle.rights_status === "controlled" ||
    bundle.rights_status === "unknown" ||
    bundle.sensitivity === "review_required"
  ) {
    return "review_required";
  }

  if (bundle.sensitivity === "generalize") {
    return "generalized";
  }

  return "public";
}

export function isPubliclyDisplayableEcologyEvidenceBundle(
  bundle: EcologyEvidenceBundle,
): boolean {
  const visibility = getEcologyEvidenceBundleVisibility(bundle);
  return visibility === "public" || visibility === "generalized";
}

export function summarizeEcologyEvidenceBundle(
  bundle: EcologyEvidenceBundle,
): EcologyEvidenceBundleSummary {
  return {
    bundle_id: bundle.bundle_id,
    resolved: isEcologyEvidenceBundleResolved(bundle),
    resolution_state:
      bundle.resolution_state ?? (bundle.resolved ? "resolved" : "unresolved"),
    policy_label: bundle.policy_label,
    rights_status: bundle.rights_status,
    sensitivity: bundle.sensitivity,
    visibility: getEcologyEvidenceBundleVisibility(bundle),
    spec_hash: bundle.spec_hash,
    source_count: bundle.source_refs?.length ?? 0,
    dataset_count: bundle.dataset_refs?.length ?? 0,
    evidence_count: bundle.evidence_refs?.length ?? 0,
    object_count: bundle.object_refs?.length ?? 0,
    artifact_count: bundle.artifacts?.length ?? bundle.artifact_count ?? 0,
    limitation_count: bundle.limitations?.length ?? 0,
    warning_count: bundle.warnings?.length ?? 0,
    stale: bundle.stale ?? false,
  };
}

export function buildEvidenceDrawerEvidence(
  bundle: EcologyEvidenceBundle,
): EcologyEvidenceDrawerEvidence {
  return {
    bundle_id: bundle.bundle_id,
    bundle_ref: getEcologyEvidenceBundleRef(bundle),
    resolved: isEcologyEvidenceBundleResolved(bundle),
    resolution_state:
      bundle.resolution_state ?? (bundle.resolved ? "resolved" : "unresolved"),
    visibility: getEcologyEvidenceBundleVisibility(bundle),
    policy_label: bundle.policy_label,
    rights_status: bundle.rights_status,
    sensitivity: bundle.sensitivity,
    spec_hash: bundle.spec_hash,
    source_refs: bundle.source_refs ?? [],
    dataset_refs: bundle.dataset_refs ?? [],
    evidence_refs: bundle.evidence_refs ?? [],
    object_refs: bundle.object_refs ?? [],
    catalog_refs: bundle.catalog_refs ?? [],
    release_refs: bundle.release_refs ?? [],
    limitations: bundle.limitations ?? [],
    notes: bundle.notes ?? [],
    warnings: bundle.warnings ?? [],
    artifacts: bundle.artifacts ?? [],
  };
}

export function getEcologyEvidenceBundleRef(
  bundle: EcologyEvidenceBundle,
): string {
  return bundle.bundle_ref ?? bundle.bundle_id;
}

function normalizeFetchOptions(
  apiBaseOrOptions: string | FetchEcologyEvidenceBundleOptions,
): FetchEcologyEvidenceBundleOptions {
  return typeof apiBaseOrOptions === "string"
    ? { apiBase: apiBaseOrOptions }
    : apiBaseOrOptions;
}

function withDefaultJsonAccept(headers?: HeadersInit): Headers {
  const merged = new Headers(headers);

  if (!merged.has("Accept")) {
    merged.set("Accept", "application/json");
  }

  return merged;
}

async function buildHttpError(
  response: Response,
  bundleRef: string,
  bundleId: string,
): Promise<EcologyEvidenceBundleHttpError> {
  const bodySnippet = await readResponseSnippet(response);
  const outcome = classifyHttpOutcome(response.status);

  return new EcologyEvidenceBundleHttpError(
    `Failed to load EvidenceBundle: ${response.status}`,
    {
      bundleRef,
      bundleId,
      status: response.status,
      statusText: response.statusText,
      bodySnippet,
      outcome,
    },
  );
}

async function readResponseSnippet(
  response: Response,
): Promise<string | undefined> {
  try {
    const text = await response.text();
    return text.slice(0, 2_000) || undefined;
  } catch {
    return undefined;
  }
}

function classifyHttpOutcome(
  status: number,
): Exclude<EcologyEvidenceBundleFiniteOutcome, "ANSWER"> {
  if (status === 401 || status === 403 || status === 451) {
    return "DENY";
  }

  if (status === 404 || status === 410 || status === 422) {
    return "ABSTAIN";
  }

  return "ERROR";
}

function unwrapEcologyEvidenceBundlePayload(value: unknown): unknown {
  if (!isRecord(value)) {
    return value;
  }

  if (value.object_type === ECOLOGY_EVIDENCE_OBJECT_TYPE) {
    return value;
  }

  for (const key of ["bundle", "evidence_bundle", "data"] as const) {
    const nested = value[key];

    if (
      isRecord(nested) &&
      nested.object_type === ECOLOGY_EVIDENCE_OBJECT_TYPE
    ) {
      return nested;
    }
  }

  return value;
}

function validateReturnedBundleId(
  bundle: EcologyEvidenceBundle,
  bundleRef: string,
  requestedBundleId: string,
): void {
  const returnedBundleId = extractEcologyEvidenceBundleId(bundle.bundle_id);

  if (returnedBundleId !== requestedBundleId) {
    throw new EcologyEvidenceBundleValidationError(
      "EvidenceBundle response id did not match request id",
      {
        bundleRef,
        bundleId: requestedBundleId,
        validationErrors: [
          `requested ${requestedBundleId}, received ${returnedBundleId}`,
        ],
      },
    );
  }
}

function normalizeEcologyEvidenceBundleError(
  cause: unknown,
  bundleRef: string,
  bundleId?: string,
): EcologyEvidenceBundleError {
  if (cause instanceof EcologyEvidenceBundleError) {
    return cause;
  }

  return new EcologyEvidenceBundleError("Unexpected EvidenceBundle failure", {
    bundleRef,
    bundleId,
    outcome: "ERROR",
    cause,
  });
}

function requireLiteral(
  record: Record<string, unknown>,
  field: string,
  expected: string,
  errors: string[],
): void {
  if (record[field] !== expected) {
    errors.push(`${field} must be ${JSON.stringify(expected)}`);
  }
}

function requireNonEmptyString(
  record: Record<string, unknown>,
  field: string,
  errors: string[],
): void {
  if (!isNonEmptyString(record[field])) {
    errors.push(`${field} must be a non-empty string`);
  }
}

function requireEnum(
  record: Record<string, unknown>,
  field: string,
  allowed: Set<string>,
  errors: string[],
): void {
  const value = record[field];

  if (typeof value !== "string" || !allowed.has(value)) {
    errors.push(`${field} must be one of: ${Array.from(allowed).join(", ")}`);
  }
}

function optionalEnum(
  record: Record<string, unknown>,
  field: string,
  allowed: Set<string>,
  errors: string[],
): void {
  const value = record[field];

  if (value !== undefined && (typeof value !== "string" || !allowed.has(value))) {
    errors.push(`${field} must be one of: ${Array.from(allowed).join(", ")}`);
  }
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function isNonEmptyString(value: unknown): value is string {
  return typeof value === "string" && value.trim().length > 0;
}

function isStringArray(value: unknown): value is string[] {
  return Array.isArray(value) && value.every((item) => typeof item === "string");
}
