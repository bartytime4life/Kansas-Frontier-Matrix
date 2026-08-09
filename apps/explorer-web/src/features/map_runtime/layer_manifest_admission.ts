/**
 * Fixture-only LayerManifest runtime admission decision.
 *
 * No registry is mutated and no MapLibre source is created. PASS means only that
 * a closed synthetic release projection would be eligible for a later governed
 * loader. Current legacy, candidate, inactive, stale, withdrawn, superseded,
 * unresolved, policy-denied, or internal-source inputs fail closed.
 */
export const LAYER_MANIFEST_ADMISSION_PROFILE =
  "kfm.layer-manifest-admission-fixture.v1" as const;

export type AdmissionOutcome = "PASS" | "HOLD" | "DENY" | "ERROR";

export type AdmissionCode =
  | "LAYER_MANIFEST_REGISTER_ELIGIBLE"
  | "LAYER_MANIFEST_LEGACY_PROFILE_HELD"
  | "LAYER_MANIFEST_INACTIVE_PROFILE_HELD"
  | "LAYER_MANIFEST_NOT_PUBLISHED"
  | "LAYER_MANIFEST_STALE"
  | "LAYER_MANIFEST_RELEASE_WITHDRAWN"
  | "LAYER_MANIFEST_SUPERSEDED"
  | "LAYER_MANIFEST_EVIDENCE_UNRESOLVED"
  | "LAYER_MANIFEST_POLICY_DENIED"
  | "LAYER_MANIFEST_RELEASE_BINDING_MISMATCH"
  | "LAYER_MANIFEST_SOURCE_CLASS_DENIED"
  | "LAYER_MANIFEST_AUTHORITY_OVERCLAIM"
  | "LAYER_MANIFEST_ADMISSION_INPUT_INVALID";

export type AdmissionResult = Readonly<{
  outcome: AdmissionOutcome;
  code: AdmissionCode;
  authority: "NONE";
  registryMutated: false;
  maplibreSourceCreated: false;
  registrationEligible: boolean;
  holds: readonly string[];
}>;

type JsonRecord = Record<string, unknown>;

const DIGEST = /^sha256:[0-9a-f]{64}$/;
const MANIFEST_ID = /^layer-manifest:[0-9a-f]{24}$/;
const REQUIRED_AUTHORITY_FIELDS = [
  "registry_mutated",
  "release_authorized",
  "publication_authorized",
  "public_use_authorized",
] as const;
const REQUIRED_RELEASE_FIELDS = [
  "release_manifest_ref",
  "release_state",
  "subject_manifest_id",
  "subject_spec_hash",
  "evidence_resolved",
  "policy_allowed",
  "review_approved",
  "promotion_approved",
  "artifact_verified",
  "signature_verified",
  "rollback_ready",
  "correction_state",
] as const;
const REQUIRED_REQUEST_FIELDS = [
  "registry_id",
  "layer_id",
  "source_url_class",
  "requested",
] as const;
const ROOT_FIELDS = new Set([
  "profile",
  "layer_id",
  "manifest_id",
  "manifest_spec_hash",
  "manifest_profile",
  "profile_status",
  "execution_mode",
  "lifecycle_state",
  "trust_state",
  "release_binding",
  "runtime_request",
  "authority",
]);

function record(value: unknown): value is JsonRecord {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function exactKeys(value: JsonRecord, expected: ReadonlySet<string>): boolean {
  const keys = Object.keys(value);
  return keys.length === expected.size && keys.every((key) => expected.has(key));
}

function exactListKeys(value: JsonRecord, expected: readonly string[]): boolean {
  const keys = Object.keys(value);
  return keys.length === expected.length && expected.every((key) => keys.includes(key));
}

function result(
  outcome: AdmissionOutcome,
  code: AdmissionCode,
  registrationEligible = false,
): AdmissionResult {
  return Object.freeze({
    outcome,
    code,
    authority: "NONE",
    registryMutated: false,
    maplibreSourceCreated: false,
    registrationEligible,
    holds: Object.freeze(["RUNTIME_REGISTRATION_NOT_EXECUTED"]),
  });
}

function parse(input: unknown): {
  root: JsonRecord;
  release: JsonRecord;
  request: JsonRecord;
  authority: JsonRecord;
} | null {
  if (!record(input) || !exactKeys(input, ROOT_FIELDS)) return null;
  if (
    input.profile !== LAYER_MANIFEST_ADMISSION_PROFILE ||
    typeof input.layer_id !== "string" ||
    !MANIFEST_ID.test(String(input.manifest_id)) ||
    !DIGEST.test(String(input.manifest_spec_hash)) ||
    !record(input.release_binding) ||
    !record(input.runtime_request) ||
    !record(input.authority) ||
    !exactListKeys(input.release_binding, REQUIRED_RELEASE_FIELDS) ||
    !exactListKeys(input.runtime_request, REQUIRED_REQUEST_FIELDS) ||
    !exactListKeys(input.authority, REQUIRED_AUTHORITY_FIELDS)
  ) {
    return null;
  }
  return {
    root: input,
    release: input.release_binding,
    request: input.runtime_request,
    authority: input.authority,
  };
}

export function evaluateLayerManifestAdmission(input: unknown): AdmissionResult {
  const parsed = parse(input);
  if (parsed === null) {
    return result("ERROR", "LAYER_MANIFEST_ADMISSION_INPUT_INVALID");
  }
  const { root, release, request, authority } = parsed;

  if (Object.values(authority).some((value) => value !== false)) {
    return result("DENY", "LAYER_MANIFEST_AUTHORITY_OVERCLAIM");
  }
  if (request.source_url_class !== "GOVERNED_API") {
    return result("DENY", "LAYER_MANIFEST_SOURCE_CLASS_DENIED");
  }
  if (root.manifest_profile === "LEGACY") {
    return result("HOLD", "LAYER_MANIFEST_LEGACY_PROFILE_HELD");
  }
  if (
    root.profile_status !== "ACTIVE" ||
    root.execution_mode !== "RELEASED_RUNTIME"
  ) {
    return result("HOLD", "LAYER_MANIFEST_INACTIVE_PROFILE_HELD");
  }
  if (release.release_state === "WITHDRAWN" || release.correction_state === "WITHDRAWN") {
    return result("DENY", "LAYER_MANIFEST_RELEASE_WITHDRAWN");
  }
  if (
    release.release_state === "SUPERSEDED" ||
    release.correction_state === "SUPERSEDED"
  ) {
    return result("HOLD", "LAYER_MANIFEST_SUPERSEDED");
  }
  if (root.lifecycle_state !== "PUBLISHED" || release.release_state !== "PUBLISHED") {
    return result("HOLD", "LAYER_MANIFEST_NOT_PUBLISHED");
  }
  if (root.trust_state === "STALE") {
    return result("HOLD", "LAYER_MANIFEST_STALE");
  }
  if (
    release.subject_manifest_id !== root.manifest_id ||
    release.subject_spec_hash !== root.manifest_spec_hash ||
    request.layer_id !== root.layer_id
  ) {
    return result("DENY", "LAYER_MANIFEST_RELEASE_BINDING_MISMATCH");
  }
  if (release.policy_allowed !== true) {
    return result("DENY", "LAYER_MANIFEST_POLICY_DENIED");
  }
  if (release.evidence_resolved !== true) {
    return result("HOLD", "LAYER_MANIFEST_EVIDENCE_UNRESOLVED");
  }
  if (
    release.review_approved !== true ||
    release.promotion_approved !== true ||
    release.artifact_verified !== true ||
    release.signature_verified !== true ||
    release.rollback_ready !== true ||
    request.requested !== true
  ) {
    return result("HOLD", "LAYER_MANIFEST_NOT_PUBLISHED");
  }
  return result("PASS", "LAYER_MANIFEST_REGISTER_ELIGIBLE", true);
}
