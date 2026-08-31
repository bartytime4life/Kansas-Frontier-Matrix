import {
  MAP_FEATURE_SELECTION_PROFILE,
  MAP_RUNTIME_INLINE_GEOJSON_LAYER_PROFILE,
  freezeMapRuntimeInlineGeoJsonLayer,
  isMapFeatureSelection,
  type MapFeatureSelection,
  type MapRuntimeInlineGeoJsonLayer,
  type MapRuntimeInlineGeoJsonPointFeature,
} from "@kfm/maplibre";

/**
 * Strict adapters and the bounded same-origin transport for the Explorer's
 * public governed slice. Transport returns unknown values; only the parsers in
 * this module can establish browser-safe projections.
 */

export const EVIDENCE_DRAWER_PROJECTION_PROFILE =
  "kfm.explorer.evidence-drawer.public-safe.v1" as const;

export type EvidenceDrawerOutcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";

export type EvidenceDrawerReasonCode =
  | "SUPPORTED"
  | "MISSING_EVIDENCE"
  | "STALE_EVIDENCE"
  | "CITATION_UNRESOLVED"
  | "POLICY_DENIED"
  | "RIGHTS_UNRESOLVED"
  | "SENSITIVE_DETAIL_RESTRICTED"
  | "UPSTREAM_ERROR"
  | "HELD_EVIDENCE"
  | "SUPERSEDED_EVIDENCE"
  | "WITHDRAWN_EVIDENCE"
  | "REVOKED_EVIDENCE";

export type EvidenceDrawerCitation = Readonly<{
  label: string;
  href: string;
}>;

export type EvidenceDrawerTrustState = Readonly<{
  sourceRole: "authoritative" | "official" | "derived" | "context";
  policy: "ALLOW" | "ABSTAIN" | "DENY" | "ERROR";
  review: "REVIEWED" | "PENDING" | "NOT_APPLICABLE";
  release: "RELEASED" | "UNRELEASED" | "WITHDRAWN";
  freshness: "CURRENT" | "STALE" | "UNKNOWN";
  correction: "NONE" | "CURRENT" | "CORRECTED" | "SUPERSEDED";
}>;

export type EvidenceDrawerNegativeState =
  | "HELD"
  | "DENIED"
  | "SUPERSEDED"
  | "REVOKED"
  | "WITHDRAWN";

export type EvidenceDrawerNegativeOutcome = Readonly<{
  evidenceRef: string;
  state: EvidenceDrawerNegativeState;
  reasonCode: Exclude<EvidenceDrawerReasonCode, "SUPPORTED" | "MISSING_EVIDENCE" | "STALE_EVIDENCE" | "CITATION_UNRESOLVED" | "UPSTREAM_ERROR">;
  recordedAt: string;
  visibleInRuntime: true;
  resolvableAsCurrent: false;
}>;

export type EvidenceDrawerCorrection = Readonly<{
  priorEvidenceRef: string;
  activeEvidenceRef: string;
  status: "ACTIVE_CORRECTION";
  recordedAt: string;
}>;

export type EvidenceDrawerHistory = Readonly<{
  negativeOutcomes: readonly EvidenceDrawerNegativeOutcome[];
  corrections: readonly EvidenceDrawerCorrection[];
}>;

export type GovernedEvidenceDrawerProjection = Readonly<{
  profile: typeof EVIDENCE_DRAWER_PROJECTION_PROFILE;
  id: string;
  outcome: EvidenceDrawerOutcome;
  reasonCode: EvidenceDrawerReasonCode;
  title: string;
  summary: string;
  evidenceRefs: readonly string[];
  citations: readonly EvidenceDrawerCitation[];
  limitations: readonly string[];
  trustState: EvidenceDrawerTrustState;
  history: EvidenceDrawerHistory;
}>;

export type GovernedProjectionResult =
  | Readonly<{ ok: true; payload: GovernedEvidenceDrawerProjection }>
  | Readonly<{ ok: false; code: "MALFORMED_GOVERNED_PAYLOAD" }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "id",
  "outcome",
  "reason_code",
  "title",
  "summary",
  "evidence_refs",
  "citations",
  "limitations",
  "trust_state",
  "history",
]);

const CITATION_FIELDS = new Set(["label", "href"]);
const TRUST_STATE_FIELDS = new Set([
  "source_role",
  "policy",
  "review",
  "release",
  "freshness",
  "correction",
]);
const HISTORY_FIELDS = new Set(["negative_outcomes", "corrections"]);
const NEGATIVE_OUTCOME_FIELDS = new Set([
  "evidence_ref",
  "state",
  "reason_code",
  "recorded_at",
  "visible_in_runtime",
  "resolvable_as_current",
]);
const CORRECTION_FIELDS = new Set([
  "prior_evidence_ref",
  "active_evidence_ref",
  "status",
  "recorded_at",
]);

const OUTCOMES = new Set<EvidenceDrawerOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<EvidenceDrawerReasonCode>([
  "SUPPORTED",
  "MISSING_EVIDENCE",
  "STALE_EVIDENCE",
  "CITATION_UNRESOLVED",
  "POLICY_DENIED",
  "RIGHTS_UNRESOLVED",
  "SENSITIVE_DETAIL_RESTRICTED",
  "UPSTREAM_ERROR",
  "HELD_EVIDENCE",
  "SUPERSEDED_EVIDENCE",
  "WITHDRAWN_EVIDENCE",
  "REVOKED_EVIDENCE",
]);
const ABSTAIN_REASON_CODES = new Set<EvidenceDrawerReasonCode>([
  "MISSING_EVIDENCE",
  "STALE_EVIDENCE",
  "CITATION_UNRESOLVED",
  "HELD_EVIDENCE",
  "SUPERSEDED_EVIDENCE",
  "WITHDRAWN_EVIDENCE",
  "REVOKED_EVIDENCE",
]);
const DENY_REASON_CODES = new Set<EvidenceDrawerReasonCode>([
  "POLICY_DENIED",
  "RIGHTS_UNRESOLVED",
  "SENSITIVE_DETAIL_RESTRICTED",
]);
const NEGATIVE_REASON_CODES = new Set([
  "HELD_EVIDENCE",
  "POLICY_DENIED",
  "RIGHTS_UNRESOLVED",
  "SENSITIVE_DETAIL_RESTRICTED",
  "SUPERSEDED_EVIDENCE",
  "WITHDRAWN_EVIDENCE",
  "REVOKED_EVIDENCE",
]);
const NEGATIVE_STATES = new Set<EvidenceDrawerNegativeState>([
  "HELD",
  "DENIED",
  "SUPERSEDED",
  "REVOKED",
  "WITHDRAWN",
]);
const NEGATIVE_STATE_REASONS: Readonly<Record<EvidenceDrawerNegativeState, ReadonlySet<string>>> =
  Object.freeze({
    HELD: new Set(["HELD_EVIDENCE"]),
    DENIED: new Set([
      "POLICY_DENIED",
      "RIGHTS_UNRESOLVED",
      "SENSITIVE_DETAIL_RESTRICTED",
    ]),
    SUPERSEDED: new Set(["SUPERSEDED_EVIDENCE"]),
    REVOKED: new Set(["REVOKED_EVIDENCE"]),
    WITHDRAWN: new Set(["WITHDRAWN_EVIDENCE"]),
  });
const SOURCE_ROLES = new Set([
  "authoritative",
  "official",
  "derived",
  "context",
]);
const POLICY_STATES = new Set(["ALLOW", "ABSTAIN", "DENY", "ERROR"]);
const REVIEW_STATES = new Set(["REVIEWED", "PENDING", "NOT_APPLICABLE"]);
const RELEASE_STATES = new Set(["RELEASED", "UNRELEASED", "WITHDRAWN"]);
const FRESHNESS_STATES = new Set(["CURRENT", "STALE", "UNKNOWN"]);
const CORRECTION_STATES = new Set([
  "NONE",
  "CURRENT",
  "CORRECTED",
  "SUPERSEDED",
]);

const MAX_TITLE_LENGTH = 160;
const MAX_SUMMARY_LENGTH = 500;
const MAX_ITEM_LENGTH = 240;
const MAX_ARRAY_ITEMS = 16;
const SAFE_ID = /^[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}$/;
const CANONICAL_UTC_SECOND = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;

const EMPTY_NEGATIVE_OUTCOMES = Object.freeze([]) as readonly EvidenceDrawerNegativeOutcome[];
const EMPTY_CORRECTIONS = Object.freeze([]) as readonly EvidenceDrawerCorrection[];
const EMPTY_HISTORY: EvidenceDrawerHistory = Object.freeze({
  negativeOutcomes: EMPTY_NEGATIVE_OUTCOMES,
  corrections: EMPTY_CORRECTIONS,
});

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  allowed: ReadonlySet<string>,
): boolean {
  return Object.keys(value).every((field) => allowed.has(field));
}

function isBoundedString(value: unknown, maximum: number): value is string {
  return (
    typeof value === "string" &&
    value.length > 0 &&
    value.length <= maximum &&
    value.trim() === value &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isSafeId(value: unknown): value is string {
  return typeof value === "string" && SAFE_ID.test(value);
}

function isCanonicalUtcSecond(value: unknown): value is string {
  if (typeof value !== "string" || !CANONICAL_UTC_SECOND.test(value)) return false;
  const parsed = Date.parse(value);
  return Number.isFinite(parsed) && new Date(parsed).toISOString() === value.replace("Z", ".000Z");
}

function isStringArray(value: unknown): value is string[] {
  return (
    Array.isArray(value) &&
    value.length <= MAX_ARRAY_ITEMS &&
    value.every((item) => isBoundedString(item, MAX_ITEM_LENGTH))
  );
}

function parseCitation(value: unknown): EvidenceDrawerCitation | null {
  if (!isRecord(value) || !hasExactFields(value, CITATION_FIELDS)) return null;
  if (!isBoundedString(value.label, MAX_TITLE_LENGTH)) return null;
  if (!isBoundedString(value.href, MAX_ITEM_LENGTH)) return null;

  try {
    const href = new URL(value.href);
    if (href.protocol !== "https:" || href.username || href.password) return null;
  } catch {
    return null;
  }

  return Object.freeze({ label: value.label, href: value.href });
}

function parseCitations(value: unknown): readonly EvidenceDrawerCitation[] | null {
  if (!Array.isArray(value) || value.length > MAX_ARRAY_ITEMS) return null;
  const citations = value.map(parseCitation);
  if (citations.some((citation) => citation === null)) return null;
  return Object.freeze(citations as EvidenceDrawerCitation[]);
}

function parseTrustState(value: unknown): EvidenceDrawerTrustState | null {
  if (!isRecord(value) || !hasExactFields(value, TRUST_STATE_FIELDS)) return null;
  if (
    typeof value.source_role !== "string" ||
    !SOURCE_ROLES.has(value.source_role) ||
    typeof value.policy !== "string" ||
    !POLICY_STATES.has(value.policy) ||
    typeof value.review !== "string" ||
    !REVIEW_STATES.has(value.review) ||
    typeof value.release !== "string" ||
    !RELEASE_STATES.has(value.release) ||
    typeof value.freshness !== "string" ||
    !FRESHNESS_STATES.has(value.freshness) ||
    typeof value.correction !== "string" ||
    !CORRECTION_STATES.has(value.correction)
  ) {
    return null;
  }

  return Object.freeze({
    sourceRole: value.source_role as EvidenceDrawerTrustState["sourceRole"],
    policy: value.policy as EvidenceDrawerTrustState["policy"],
    review: value.review as EvidenceDrawerTrustState["review"],
    release: value.release as EvidenceDrawerTrustState["release"],
    freshness: value.freshness as EvidenceDrawerTrustState["freshness"],
    correction: value.correction as EvidenceDrawerTrustState["correction"],
  });
}

function parseNegativeOutcome(value: unknown): EvidenceDrawerNegativeOutcome | null {
  if (!isRecord(value) || !hasExactFields(value, NEGATIVE_OUTCOME_FIELDS)) return null;
  if (!isSafeId(value.evidence_ref)) return null;
  if (typeof value.state !== "string" || !NEGATIVE_STATES.has(value.state as EvidenceDrawerNegativeState)) {
    return null;
  }
  if (typeof value.reason_code !== "string" || !NEGATIVE_REASON_CODES.has(value.reason_code)) {
    return null;
  }
  const state = value.state as EvidenceDrawerNegativeState;
  if (!NEGATIVE_STATE_REASONS[state].has(value.reason_code)) return null;
  if (!isCanonicalUtcSecond(value.recorded_at)) return null;
  if (value.visible_in_runtime !== true || value.resolvable_as_current !== false) return null;

  return Object.freeze({
    evidenceRef: value.evidence_ref,
    state: value.state as EvidenceDrawerNegativeState,
    reasonCode: value.reason_code as EvidenceDrawerNegativeOutcome["reasonCode"],
    recordedAt: value.recorded_at,
    visibleInRuntime: true,
    resolvableAsCurrent: false,
  });
}

function parseCorrection(value: unknown): EvidenceDrawerCorrection | null {
  if (!isRecord(value) || !hasExactFields(value, CORRECTION_FIELDS)) return null;
  if (!isSafeId(value.prior_evidence_ref) || !isSafeId(value.active_evidence_ref)) return null;
  if (value.prior_evidence_ref === value.active_evidence_ref) return null;
  if (value.status !== "ACTIVE_CORRECTION") return null;
  if (!isCanonicalUtcSecond(value.recorded_at)) return null;

  return Object.freeze({
    priorEvidenceRef: value.prior_evidence_ref,
    activeEvidenceRef: value.active_evidence_ref,
    status: "ACTIVE_CORRECTION",
    recordedAt: value.recorded_at,
  });
}

function correctionsContainCycle(corrections: readonly EvidenceDrawerCorrection[]): boolean {
  const edges = new Map<string, string>();
  for (const correction of corrections) {
    if (edges.has(correction.priorEvidenceRef)) return true;
    edges.set(correction.priorEvidenceRef, correction.activeEvidenceRef);
  }
  for (const start of edges.keys()) {
    const seen = new Set<string>();
    let cursor: string | undefined = start;
    while (cursor !== undefined) {
      if (seen.has(cursor)) return true;
      seen.add(cursor);
      cursor = edges.get(cursor);
    }
  }
  return false;
}

function parseHistory(value: unknown): EvidenceDrawerHistory | null {
  if (value === undefined) return EMPTY_HISTORY;
  if (!isRecord(value) || !hasExactFields(value, HISTORY_FIELDS)) return null;
  if (!Array.isArray(value.negative_outcomes) || value.negative_outcomes.length > MAX_ARRAY_ITEMS) {
    return null;
  }
  if (!Array.isArray(value.corrections) || value.corrections.length > MAX_ARRAY_ITEMS) {
    return null;
  }

  const negativeOutcomes = value.negative_outcomes.map(parseNegativeOutcome);
  const corrections = value.corrections.map(parseCorrection);
  if (negativeOutcomes.some((item) => item === null) || corrections.some((item) => item === null)) {
    return null;
  }

  const normalizedNegative = negativeOutcomes as EvidenceDrawerNegativeOutcome[];
  const normalizedCorrections = corrections as EvidenceDrawerCorrection[];
  if (new Set(normalizedNegative.map((item) => item.evidenceRef)).size !== normalizedNegative.length) {
    return null;
  }
  if (correctionsContainCycle(normalizedCorrections)) return null;

  return Object.freeze({
    negativeOutcomes: Object.freeze(normalizedNegative),
    corrections: Object.freeze(normalizedCorrections),
  });
}

function historyCombinationIsValid(
  outcome: EvidenceDrawerOutcome,
  reasonCode: EvidenceDrawerReasonCode,
  evidenceRefs: readonly string[],
  trustState: EvidenceDrawerTrustState,
  history: EvidenceDrawerHistory,
): boolean {
  const currentRefs = new Set(evidenceRefs);
  if (history.negativeOutcomes.some((item) => currentRefs.has(item.evidenceRef))) return false;

  if (outcome === "DENY" || outcome === "ERROR") {
    return history.negativeOutcomes.length === 0 && history.corrections.length === 0;
  }

  if (outcome === "ANSWER") {
    if (trustState.correction === "SUPERSEDED") return false;
    if (history.corrections.length > 0 && trustState.correction !== "CORRECTED") {
      return false;
    }
    if (trustState.correction === "CORRECTED") {
      if (history.corrections.length === 0) return false;
      const priorRefs = new Set(history.corrections.map((item) => item.priorEvidenceRef));
      const supersededRefs = new Set(
        history.negativeOutcomes
          .filter((item) => item.state === "SUPERSEDED")
          .map((item) => item.evidenceRef),
      );
      if (
        priorRefs.size !== supersededRefs.size ||
        [...priorRefs].some((ref) => !supersededRefs.has(ref))
      ) {
        return false;
      }
      if (history.negativeOutcomes.some((item) => item.state !== "SUPERSEDED")) {
        return false;
      }
      const terminalRefs = history.corrections
        .map((item) => item.activeEvidenceRef)
        .filter((ref) => !priorRefs.has(ref));
      if (terminalRefs.length === 0 || terminalRefs.some((ref) => !currentRefs.has(ref))) {
        return false;
      }
    } else if (history.negativeOutcomes.length > 0) {
      return false;
    }
  }

  if (outcome === "ABSTAIN" && reasonCode === "SUPERSEDED_EVIDENCE") {
    return (
      trustState.correction === "SUPERSEDED" &&
      history.negativeOutcomes.some((item) => item.state === "SUPERSEDED")
    );
  }
  if (outcome === "ABSTAIN" && reasonCode === "HELD_EVIDENCE") {
    return history.negativeOutcomes.some((item) => item.state === "HELD");
  }
  if (outcome === "ABSTAIN" && reasonCode === "WITHDRAWN_EVIDENCE") {
    return history.negativeOutcomes.some((item) => item.state === "WITHDRAWN");
  }
  if (outcome === "ABSTAIN" && reasonCode === "REVOKED_EVIDENCE") {
    return history.negativeOutcomes.some((item) => item.state === "REVOKED");
  }

  return true;
}

function outcomeCombinationIsValid(
  outcome: EvidenceDrawerOutcome,
  reasonCode: EvidenceDrawerReasonCode,
  evidenceRefs: readonly string[],
  citations: readonly EvidenceDrawerCitation[],
  trustState: EvidenceDrawerTrustState,
  history: EvidenceDrawerHistory,
): boolean {
  if (outcome === "ANSWER") {
    return (
      reasonCode === "SUPPORTED" &&
      evidenceRefs.length > 0 &&
      citations.length > 0 &&
      trustState.policy === "ALLOW" &&
      trustState.review === "REVIEWED" &&
      trustState.release === "RELEASED" &&
      trustState.freshness === "CURRENT" &&
      historyCombinationIsValid(outcome, reasonCode, evidenceRefs, trustState, history)
    );
  }

  if (outcome === "ABSTAIN") {
    return (
      ABSTAIN_REASON_CODES.has(reasonCode) &&
      trustState.policy === "ABSTAIN" &&
      historyCombinationIsValid(outcome, reasonCode, evidenceRefs, trustState, history)
    );
  }

  if (outcome === "DENY") {
    return (
      DENY_REASON_CODES.has(reasonCode) &&
      evidenceRefs.length === 0 &&
      citations.length === 0 &&
      trustState.policy === "DENY" &&
      historyCombinationIsValid(outcome, reasonCode, evidenceRefs, trustState, history)
    );
  }

  return (
    reasonCode === "UPSTREAM_ERROR" &&
    evidenceRefs.length === 0 &&
    citations.length === 0 &&
    trustState.policy === "ERROR" &&
    historyCombinationIsValid(outcome, reasonCode, evidenceRefs, trustState, history)
  );
}

/** Validate and normalize one bounded public-safe governed projection. */
export function parseEvidenceDrawerProjection(
  value: unknown,
): GovernedProjectionResult {
  const malformed = Object.freeze({
    ok: false as const,
    code: "MALFORMED_GOVERNED_PAYLOAD" as const,
  });

  if (!isRecord(value) || !hasExactFields(value, TOP_LEVEL_FIELDS)) return malformed;
  if (value.profile !== EVIDENCE_DRAWER_PROJECTION_PROFILE) return malformed;
  if (!isSafeId(value.id)) return malformed;
  if (typeof value.outcome !== "string" || !OUTCOMES.has(value.outcome as EvidenceDrawerOutcome)) {
    return malformed;
  }
  if (
    typeof value.reason_code !== "string" ||
    !REASON_CODES.has(value.reason_code as EvidenceDrawerReasonCode)
  ) {
    return malformed;
  }
  if (!isBoundedString(value.title, MAX_TITLE_LENGTH)) return malformed;
  if (!isBoundedString(value.summary, MAX_SUMMARY_LENGTH)) return malformed;
  if (!isStringArray(value.evidence_refs) || !value.evidence_refs.every(isSafeId)) {
    return malformed;
  }
  if (!isStringArray(value.limitations)) return malformed;

  const citations = parseCitations(value.citations);
  const trustState = parseTrustState(value.trust_state);
  const history = parseHistory(value.history);
  if (citations === null || trustState === null || history === null) return malformed;

  const outcome = value.outcome as EvidenceDrawerOutcome;
  const reasonCode = value.reason_code as EvidenceDrawerReasonCode;
  if (
    !outcomeCombinationIsValid(
      outcome,
      reasonCode,
      value.evidence_refs,
      citations,
      trustState,
      history,
    )
  ) {
    return malformed;
  }

  const payload: GovernedEvidenceDrawerProjection = Object.freeze({
    profile: EVIDENCE_DRAWER_PROJECTION_PROFILE,
    id: value.id,
    outcome,
    reasonCode,
    title: value.title,
    summary: value.summary,
    evidenceRefs: Object.freeze([...value.evidence_refs]),
    citations,
    limitations: Object.freeze([...value.limitations]),
    trustState,
    history,
  });

  return Object.freeze({ ok: true, payload });
}

export const GOVERNED_LAYER_SLICE_PROFILE =
  "kfm.governed-api.synthetic-layer-slice.v1" as const;
export const INLINE_GEOJSON_LAYER_PROFILE =
  MAP_RUNTIME_INLINE_GEOJSON_LAYER_PROFILE;

export type GovernedLayerSliceReasonCode =
  | "SUPPORTED"
  | "INVALID_REQUEST"
  | "UPSTREAM_ERROR";

export type InlineGeoJsonPointFeature = MapRuntimeInlineGeoJsonPointFeature;

export type InlineGeoJsonFeatureCollection = Readonly<{
  type: "FeatureCollection";
  features: readonly [InlineGeoJsonPointFeature];
}>;

/** Exact package-owned inline GeoJSON admission bundle. */
export type GovernedInlineGeoJsonLayer = MapRuntimeInlineGeoJsonLayer;

export type GovernedLayerProjection = Readonly<{
  title: string;
  description: string;
  runtimeLayer: GovernedInlineGeoJsonLayer;
}>;

export type GovernedLayerSlice = Readonly<{
  profile: typeof GOVERNED_LAYER_SLICE_PROFILE;
  scope: "slice-local";
  outcome: "ANSWER" | "ERROR";
  reasonCode: GovernedLayerSliceReasonCode;
  layers: readonly GovernedLayerProjection[];
  limitations: readonly [string];
}>;

export type GovernedLayerSliceResult =
  | Readonly<{ ok: true; payload: GovernedLayerSlice }>
  | Readonly<{ ok: false; code: "MALFORMED_GOVERNED_LAYER_PAYLOAD" }>;

const LAYER_SLICE_FIELDS = new Set([
  "profile",
  "scope",
  "outcome",
  "reason_code",
  "layers",
  "limitations",
]);
const LAYER_FIELDS = new Set([
  "source_id",
  "layer_id",
  "kind",
  "title",
  "description",
  "geojson",
  "selection",
]);
const FEATURE_COLLECTION_FIELDS = new Set(["type", "features"]);
const FEATURE_FIELDS = new Set(["type", "id", "geometry", "properties"]);
const POINT_GEOMETRY_FIELDS = new Set(["type", "coordinates"]);
const LAYER_SELECTION_FIELDS = new Set([
  "profile",
  "selection_id",
  "layer_id",
  "feature_id",
  "evidence_refs",
]);
const LAYER_ERROR_REASON_CODES = new Set([
  "INVALID_REQUEST",
  "UPSTREAM_ERROR",
]);
const MAX_MERCATOR_LATITUDE = 85.051129;
const GOVERNED_SYNTHETIC_SOURCE_ID = "source:synthetic-streamflow";
const GOVERNED_SYNTHETIC_LAYER_ID = "layer:synthetic-streamflow";
const GOVERNED_SYNTHETIC_FEATURE_ID = "feature:flow-001";
const GOVERNED_SYNTHETIC_SELECTION_ID = "selection:flow-001";
const GOVERNED_SYNTHETIC_EVIDENCE_REF =
  "kfm:evidence:synthetic:flow-001";
const GOVERNED_SYNTHETIC_COORDINATES = Object.freeze([
  -98.5,
  38.5,
]) as readonly [number, number];
const GOVERNED_SYNTHETIC_LAYER_TITLE =
  "Synthetic streamflow demonstration";
const GOVERNED_SYNTHETIC_LAYER_DESCRIPTION =
  "One generalized, fixture-only Kansas streamflow feature for the bounded governed map slice.";
const GOVERNED_SYNTHETIC_LAYER_LIMITATION =
  "Fixture-only synthetic demonstration; not live data, release authority, or life-safety guidance.";

function hasExactlyFields(
  value: Record<string, unknown>,
  expected: ReadonlySet<string>,
): boolean {
  return (
    Object.keys(value).length === expected.size &&
    Object.keys(value).every((field) => expected.has(field))
  );
}

function parseLayerSelection(value: unknown): MapFeatureSelection | null {
  if (!isRecord(value) || !hasExactlyFields(value, LAYER_SELECTION_FIELDS)) {
    return null;
  }
  if (
    value.profile !== MAP_FEATURE_SELECTION_PROFILE ||
    value.selection_id !== GOVERNED_SYNTHETIC_SELECTION_ID ||
    value.layer_id !== GOVERNED_SYNTHETIC_LAYER_ID ||
    value.feature_id !== GOVERNED_SYNTHETIC_FEATURE_ID ||
    !Array.isArray(value.evidence_refs) ||
    value.evidence_refs.length !== 1 ||
    value.evidence_refs[0] !== GOVERNED_SYNTHETIC_EVIDENCE_REF
  ) {
    return null;
  }

  const selection: MapFeatureSelection = Object.freeze({
    profile: MAP_FEATURE_SELECTION_PROFILE,
    selectionId: value.selection_id,
    layerId: value.layer_id,
    featureId: value.feature_id,
    evidenceRefs: Object.freeze([...value.evidence_refs]),
  });
  return isMapFeatureSelection(selection) ? selection : null;
}

function parsePointFeature(value: unknown): InlineGeoJsonPointFeature | null {
  if (!isRecord(value) || !hasExactlyFields(value, FEATURE_FIELDS)) return null;
  if (
    value.type !== "Feature" ||
    value.id !== GOVERNED_SYNTHETIC_FEATURE_ID ||
    value.properties !== null
  ) {
    return null;
  }
  if (!isRecord(value.geometry) || !hasExactlyFields(value.geometry, POINT_GEOMETRY_FIELDS)) {
    return null;
  }
  if (
    value.geometry.type !== "Point" ||
    !Array.isArray(value.geometry.coordinates) ||
    value.geometry.coordinates.length !== 2
  ) {
    return null;
  }
  const [longitude, latitude] = value.geometry.coordinates;
  if (
    typeof longitude !== "number" ||
    !Number.isFinite(longitude) ||
    longitude < -180 ||
    longitude > 180 ||
    typeof latitude !== "number" ||
    !Number.isFinite(latitude) ||
    latitude < -MAX_MERCATOR_LATITUDE ||
    latitude > MAX_MERCATOR_LATITUDE ||
    longitude !== GOVERNED_SYNTHETIC_COORDINATES[0] ||
    latitude !== GOVERNED_SYNTHETIC_COORDINATES[1]
  ) {
    return null;
  }

  return Object.freeze({
    type: "Feature",
    id: value.id,
    geometry: Object.freeze({
      type: "Point",
      coordinates: Object.freeze([longitude, latitude]) as readonly [number, number],
    }),
    properties: null,
  });
}

function parseLayer(value: unknown): GovernedLayerProjection | null {
  if (!isRecord(value) || !hasExactlyFields(value, LAYER_FIELDS)) return null;
  if (
    value.source_id !== GOVERNED_SYNTHETIC_SOURCE_ID ||
    value.layer_id !== GOVERNED_SYNTHETIC_LAYER_ID ||
    value.kind !== "circle" ||
    value.title !== GOVERNED_SYNTHETIC_LAYER_TITLE ||
    value.description !== GOVERNED_SYNTHETIC_LAYER_DESCRIPTION
  ) {
    return null;
  }
  if (
    !isRecord(value.geojson) ||
    !hasExactlyFields(value.geojson, FEATURE_COLLECTION_FIELDS) ||
    value.geojson.type !== "FeatureCollection" ||
    !Array.isArray(value.geojson.features) ||
    value.geojson.features.length !== 1
  ) {
    return null;
  }

  const feature = parsePointFeature(value.geojson.features[0]);
  const selection = parseLayerSelection(value.selection);
  if (
    feature === null ||
    selection === null ||
    selection.layerId !== value.layer_id ||
    selection.featureId !== feature.id
  ) {
    return null;
  }

  const data: InlineGeoJsonFeatureCollection = Object.freeze({
    type: "FeatureCollection",
    features: Object.freeze([feature]) as readonly [InlineGeoJsonPointFeature],
  });
  const runtimeLayer = freezeMapRuntimeInlineGeoJsonLayer({
    profile: MAP_RUNTIME_INLINE_GEOJSON_LAYER_PROFILE,
    sourceId: value.source_id,
    layerId: value.layer_id,
    kind: "circle",
    data,
    selection,
  });
  return Object.freeze({
    title: value.title,
    description: value.description,
    runtimeLayer,
  });
}

/** Validate and normalize the exact-one public layer slice. */
export function parseGovernedLayerSlice(value: unknown): GovernedLayerSliceResult {
  const malformed = Object.freeze({
    ok: false as const,
    code: "MALFORMED_GOVERNED_LAYER_PAYLOAD" as const,
  });
  if (!isRecord(value) || !hasExactlyFields(value, LAYER_SLICE_FIELDS)) return malformed;
  if (
    value.profile !== GOVERNED_LAYER_SLICE_PROFILE ||
    value.scope !== "slice-local" ||
    !Array.isArray(value.layers) ||
    !Array.isArray(value.limitations) ||
    value.limitations.length !== 1 ||
    value.limitations[0] !== GOVERNED_SYNTHETIC_LAYER_LIMITATION
  ) {
    return malformed;
  }

  let outcome: "ANSWER" | "ERROR";
  let reasonCode: GovernedLayerSliceReasonCode;
  let layers: readonly GovernedLayerProjection[];
  if (value.outcome === "ANSWER" && value.reason_code === "SUPPORTED") {
    if (value.layers.length !== 1) return malformed;
    const layer = parseLayer(value.layers[0]);
    if (layer === null) return malformed;
    outcome = "ANSWER";
    reasonCode = "SUPPORTED";
    layers = Object.freeze([layer]);
  } else if (
    value.outcome === "ERROR" &&
    typeof value.reason_code === "string" &&
    LAYER_ERROR_REASON_CODES.has(value.reason_code) &&
    value.layers.length === 0
  ) {
    outcome = "ERROR";
    reasonCode = value.reason_code as GovernedLayerSliceReasonCode;
    layers = Object.freeze([]);
  } else {
    return malformed;
  }

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: GOVERNED_LAYER_SLICE_PROFILE,
      scope: "slice-local",
      outcome,
      reasonCode,
      layers,
      limitations: Object.freeze([value.limitations[0]]) as readonly [string],
    }),
  });
}

export type GovernedTransport = Readonly<{
  loadLayers: () => Promise<unknown>;
  loadEvidence: (selection: MapFeatureSelection) => Promise<unknown>;
  close: () => void;
}>;

export type GovernedFetch = (
  input: RequestInfo | URL,
  init?: RequestInit,
) => Promise<Response>;

const MAX_GOVERNED_RESPONSE_BYTES = 32 * 1024;
export const DEFAULT_GOVERNED_REQUEST_DEADLINE_MS = 10_000;
const MAX_GOVERNED_REQUEST_DEADLINE_MS = 60_000;

export type GovernedHttpTransportOptions = Readonly<{
  /** Absolute deadline covering response headers and the complete body. */
  requestDeadlineMs?: number;
}>;

function abortReason(signal: AbortSignal): unknown {
  return signal.reason === undefined
    ? new DOMException("Governed request was aborted.", "AbortError")
    : signal.reason;
}

function raceWithAbort<T>(
  operation: Promise<T>,
  signal: AbortSignal,
  onAbort?: () => void,
): Promise<T> {
  return new Promise<T>((resolve, reject) => {
    let settled = false;
    const finish = (callback: () => void): void => {
      if (settled) return;
      settled = true;
      signal.removeEventListener("abort", handleAbort);
      callback();
    };
    const handleAbort = (): void => {
      finish(() => {
        try {
          onAbort?.();
        } catch {
          // Abort still settles even if an injected stream rejects cancellation.
        }
        reject(abortReason(signal));
      });
    };

    signal.addEventListener("abort", handleAbort, { once: true });
    operation.then(
      (value) => finish(() => resolve(value)),
      (error: unknown) => finish(() => reject(error)),
    );
    if (signal.aborted) handleAbort();
  });
}

async function readBoundedJson(
  response: Response,
  signal: AbortSignal,
): Promise<unknown> {
  const contentType = response.headers.get("content-type")?.toLowerCase() ?? "";
  if (!contentType.startsWith("application/json")) {
    throw new Error("Governed response media type is invalid.");
  }
  if (response.body === null) {
    throw new Error("Governed response body is missing.");
  }

  const reader = response.body.getReader();
  const chunks: Uint8Array[] = [];
  let length = 0;
  let cancellationStarted = false;
  const cancelReader = (): void => {
    if (cancellationStarted) return;
    cancellationStarted = true;
    try {
      void reader.cancel().catch(() => undefined);
    } catch {
      // A nonconforming injected stream cannot delay finite rejection.
    }
  };
  try {
    while (true) {
      const next = await raceWithAbort(reader.read(), signal, cancelReader);
      if (next.done) break;
      length += next.value.byteLength;
      if (length > MAX_GOVERNED_RESPONSE_BYTES) {
        throw new Error("Governed response exceeds the browser bound.");
      }
      chunks.push(next.value);
    }
  } catch (error) {
    cancelReader();
    throw error;
  } finally {
    try {
      reader.releaseLock();
    } catch {
      // Cancellation may still be settling on an injected stream.
    }
  }

  const bytes = new Uint8Array(length);
  let offset = 0;
  for (const chunk of chunks) {
    bytes.set(chunk, offset);
    offset += chunk.byteLength;
  }
  const source = new TextDecoder("utf-8", { fatal: true }).decode(bytes);
  return JSON.parse(source) as unknown;
}

/**
 * Create the only browser HTTP seam for this slice. Endpoint paths are fixed,
 * query keys are exact, and each response is deadline- and byte-bounded before
 * its outcome can reach the UI.
 */
export function createGovernedHttpTransport(
  origin: string,
  request: GovernedFetch,
  options: GovernedHttpTransportOptions = {},
): GovernedTransport {
  let sameOrigin: URL;
  try {
    sameOrigin = new URL(origin);
  } catch {
    throw new TypeError("Governed transport origin is invalid.");
  }
  if (
    sameOrigin.origin !== origin ||
    !["http:", "https:"].includes(sameOrigin.protocol) ||
    sameOrigin.username ||
    sameOrigin.password ||
    typeof request !== "function"
  ) {
    throw new TypeError("Governed transport requires an exact HTTP(S) origin.");
  }
  const requestDeadlineMs =
    options.requestDeadlineMs ?? DEFAULT_GOVERNED_REQUEST_DEADLINE_MS;
  if (
    !Number.isSafeInteger(requestDeadlineMs) ||
    requestDeadlineMs < 1 ||
    requestDeadlineMs > MAX_GOVERNED_REQUEST_DEADLINE_MS
  ) {
    throw new TypeError("Governed transport request deadline is invalid.");
  }
  const closeController = new AbortController();
  let closed = false;

  const get = async (url: URL): Promise<unknown> => {
    if (closed) throw new Error("Governed transport is closed.");
    if (url.origin !== sameOrigin.origin) {
      throw new Error("Cross-origin governed request blocked.");
    }
    const requestController = new AbortController();
    const handleClose = (): void => {
      requestController.abort(abortReason(closeController.signal));
    };
    closeController.signal.addEventListener("abort", handleClose, {
      once: true,
    });
    if (closeController.signal.aborted) handleClose();
    const deadline = setTimeout(() => {
      const error = new Error("Governed request deadline exceeded.");
      error.name = "TimeoutError";
      requestController.abort(error);
    }, requestDeadlineMs);

    try {
      const response = await raceWithAbort(
        request(url, {
          method: "GET",
          headers: Object.freeze({ Accept: "application/json" }),
          credentials: "same-origin",
          cache: "no-store",
          redirect: "error",
          signal: requestController.signal,
        }),
        requestController.signal,
      );
      const payload = await readBoundedJson(
        response,
        requestController.signal,
      );
      const outcome = isRecord(payload) ? payload.outcome : undefined;
      if (response.ok) {
        if (outcome === "ERROR") {
          throw new Error("Governed response status and outcome conflict.");
        }
        return payload;
      }
      if (
        (response.status === 400 || response.status === 500) &&
        outcome === "ERROR"
      ) {
        return payload;
      }
      throw new Error("Governed response status and outcome conflict.");
    } finally {
      clearTimeout(deadline);
      closeController.signal.removeEventListener("abort", handleClose);
    }
  };

  return Object.freeze({
    loadLayers: () => get(new URL("/layers", sameOrigin)),
    loadEvidence: (selection: MapFeatureSelection) => {
      if (!isMapFeatureSelection(selection) || selection.evidenceRefs.length !== 1) {
        return Promise.reject(new Error("Governed evidence request scope is invalid."));
      }
      const url = new URL("/evidence", sameOrigin);
      url.searchParams.set("layer_id", selection.layerId);
      url.searchParams.set("feature_id", selection.featureId);
      url.searchParams.set("evidence_ref", selection.evidenceRefs[0]);
      return get(url);
    },
    close: () => {
      if (closed) return;
      closed = true;
      closeController.abort();
    },
  });
}
