/**
 * Strict app-local adapter for a public-safe HUC crosswalk reference projection.
 *
 * The browser receives only identifiers, finite status, digest-bound references,
 * and a validation-receipt reference. It never receives source rows, flow values,
 * geometry, counts, credentials, signatures, or release controls.
 */

export const HUC_CROSSWALK_PROJECTION_PROFILE =
  "kfm.explorer.huc-crosswalk.public-safe.v1" as const;

export type HucCrosswalkStatus =
  | "VERIFIED_EXACT"
  | "AMBIGUOUS"
  | "STALE"
  | "UNRESOLVED"
  | "RELEASE_DENIED";

export type HucCrosswalkOutcome = "AVAILABLE" | "ABSTAIN" | "DENY";

export type HucCrosswalkReasonCode =
  | "CROSSWALK_VERIFIED"
  | "CROSSWALK_AMBIGUOUS"
  | "CROSSWALK_STALE"
  | "CROSSWALK_UNRESOLVED"
  | "RELEASE_DENIED";

export type GovernedHucCrosswalkProjection = Readonly<{
  profile: typeof HUC_CROSSWALK_PROJECTION_PROFILE;
  countyFips: string;
  huc12: string;
  outcome: HucCrosswalkOutcome;
  status: HucCrosswalkStatus;
  reasonCode: HucCrosswalkReasonCode;
  sourceHash: string;
  crosswalkRef: string;
  crosswalkDigest: string;
  validationReceiptRef: string;
  stationRefs: readonly string[];
  evaluatedAt: string;
}>;

export type HucCrosswalkProjectionResult =
  | Readonly<{ ok: true; payload: GovernedHucCrosswalkProjection }>
  | Readonly<{ ok: false; code: "MALFORMED_HUC_CROSSWALK_PROJECTION" }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "county_fips",
  "huc12",
  "outcome",
  "status",
  "reason_code",
  "source_hash",
  "crosswalk_ref",
  "crosswalk_digest",
  "validation_receipt_ref",
  "station_refs",
  "evaluated_at",
]);
const STATUS_BINDING = Object.freeze({
  VERIFIED_EXACT: Object.freeze({
    outcome: "AVAILABLE",
    reasonCode: "CROSSWALK_VERIFIED",
  }),
  AMBIGUOUS: Object.freeze({
    outcome: "ABSTAIN",
    reasonCode: "CROSSWALK_AMBIGUOUS",
  }),
  STALE: Object.freeze({
    outcome: "ABSTAIN",
    reasonCode: "CROSSWALK_STALE",
  }),
  UNRESOLVED: Object.freeze({
    outcome: "ABSTAIN",
    reasonCode: "CROSSWALK_UNRESOLVED",
  }),
  RELEASE_DENIED: Object.freeze({
    outcome: "DENY",
    reasonCode: "RELEASE_DENIED",
  }),
}) satisfies Readonly<
  Record<
    HucCrosswalkStatus,
    Readonly<{ outcome: HucCrosswalkOutcome; reasonCode: HucCrosswalkReasonCode }>
  >
>;
const SHA256 = /^sha256:[a-f0-9]{64}$/;
const CROSSWALK_REFERENCE =
  /^kfm:\/\/manifest\/hydrology\/[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,190}@sha256:[a-f0-9]{64}$/;
const VALIDATION_RECEIPT_REFERENCE =
  /^kfm:\/\/receipt\/[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,200}@sha256:[a-f0-9]{64}$/;
const STATION_REFERENCE =
  /^kfm:\/\/station\/[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,180}@sha256:[a-f0-9]{64}$/;
const CANONICAL_UTC_SECOND = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;
const MAX_STATIONS = 8;

function malformed(): HucCrosswalkProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_HUC_CROSSWALK_PROJECTION",
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

function isHash(value: unknown): value is string {
  return typeof value === "string" && SHA256.test(value);
}

function isCrosswalkReference(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= 320 &&
    CROSSWALK_REFERENCE.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isValidationReceiptReference(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length <= 320 &&
    VALIDATION_RECEIPT_REFERENCE.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function parseStationRefs(value: unknown): readonly string[] | null {
  if (
    !Array.isArray(value) ||
    value.length > MAX_STATIONS ||
    !value.every(
      (item) =>
        typeof item === "string" &&
        item.length <= 320 &&
        STATION_REFERENCE.test(item) &&
        !CONTROL_CHARACTER.test(item),
    )
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

/** Parse one closed, digest-bound HUC crosswalk projection. */
export function parseHucCrosswalkProjection(
  input: unknown,
): HucCrosswalkProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return malformed();
  }
  if (
    input.profile !== HUC_CROSSWALK_PROJECTION_PROFILE ||
    typeof input.county_fips !== "string" ||
    !/^\d{5}$/.test(input.county_fips) ||
    typeof input.huc12 !== "string" ||
    !/^\d{12}$/.test(input.huc12) ||
    typeof input.status !== "string" ||
    !Object.hasOwn(STATUS_BINDING, input.status) ||
    !isHash(input.source_hash) ||
    !isCrosswalkReference(input.crosswalk_ref) ||
    !isHash(input.crosswalk_digest) ||
    !input.crosswalk_ref.endsWith(`@${input.crosswalk_digest}`) ||
    !isValidationReceiptReference(input.validation_receipt_ref) ||
    !isCanonicalUtcSecond(input.evaluated_at)
  ) {
    return malformed();
  }
  const status = input.status as HucCrosswalkStatus;
  const binding = STATUS_BINDING[status];
  if (input.outcome !== binding.outcome || input.reason_code !== binding.reasonCode) {
    return malformed();
  }
  const stationRefs = parseStationRefs(input.station_refs);
  if (
    stationRefs === null ||
    (binding.outcome === "AVAILABLE" && stationRefs.length === 0) ||
    (binding.outcome !== "AVAILABLE" && stationRefs.length !== 0)
  ) {
    return malformed();
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: HUC_CROSSWALK_PROJECTION_PROFILE,
      countyFips: input.county_fips,
      huc12: input.huc12,
      outcome: binding.outcome,
      status,
      reasonCode: binding.reasonCode,
      sourceHash: input.source_hash,
      crosswalkRef: input.crosswalk_ref,
      crosswalkDigest: input.crosswalk_digest,
      validationReceiptRef: input.validation_receipt_ref,
      stationRefs,
      evaluatedAt: input.evaluated_at,
    }),
  });
}
