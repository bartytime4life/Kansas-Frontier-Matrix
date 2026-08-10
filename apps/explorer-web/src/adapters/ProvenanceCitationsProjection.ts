/**
 * Strict public-safe projection for the Pass 32 provenance citations panel.
 *
 * This adapter validates bounded display material only. It does not resolve
 * evidence, query a provenance graph, infer rights, execute policy, fetch
 * citations, or authorize release or publication.
 */

export const PROVENANCE_CITATIONS_PROJECTION_PROFILE =
  "kfm.explorer.provenance-citations.public-safe.v1" as const;

export type ProvenanceCitationsOutcome =
  | "ANSWER"
  | "ABSTAIN"
  | "DENY"
  | "ERROR";

export type ProvenanceCitationsReasonCode =
  | "CITATIONS_AVAILABLE"
  | "CITATIONS_MISSING"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR";

export type RepublicationNoteCode =
  | "KFM_DERIVED_REPUBLICATION"
  | "SOURCE_PRESERVED";

export type GovernedProvenanceCitation = Readonly<{
  citationId: string;
  label: string;
  href: string;
  doi: string | null;
  evidenceRef: string;
}>;

export type GovernedProvenanceCitationsProjection = Readonly<{
  profile: typeof PROVENANCE_CITATIONS_PROJECTION_PROFILE;
  panelId: string;
  outcome: ProvenanceCitationsOutcome;
  reasonCode: ProvenanceCitationsReasonCode;
  title: string | null;
  activityRef: string | null;
  citations: readonly GovernedProvenanceCitation[];
  republicationNoteCode: RepublicationNoteCode | null;
  releaseManifestRef: string | null;
}>;

export type ProvenanceCitationsProjectionResult =
  | Readonly<{ ok: true; payload: GovernedProvenanceCitationsProjection }>
  | Readonly<{ ok: false; code: "MALFORMED_PROVENANCE_CITATIONS_PROJECTION" }>;

const TOP_LEVEL_FIELDS = new Set([
  "profile",
  "panel_id",
  "outcome",
  "reason_code",
  "title",
  "activity_ref",
  "citations",
  "republication_note_code",
  "release_manifest_ref",
]);
const CITATION_FIELDS = new Set([
  "citation_id",
  "label",
  "href",
  "doi",
  "evidence_ref",
]);
const OUTCOMES = new Set<ProvenanceCitationsOutcome>([
  "ANSWER",
  "ABSTAIN",
  "DENY",
  "ERROR",
]);
const REASON_CODES = new Set<ProvenanceCitationsReasonCode>([
  "CITATIONS_AVAILABLE",
  "CITATIONS_MISSING",
  "POLICY_DENIED",
  "UPSTREAM_ERROR",
]);
const EXPECTED_REASON: Readonly<
  Record<ProvenanceCitationsOutcome, ProvenanceCitationsReasonCode>
> = Object.freeze({
  ANSWER: "CITATIONS_AVAILABLE",
  ABSTAIN: "CITATIONS_MISSING",
  DENY: "POLICY_DENIED",
  ERROR: "UPSTREAM_ERROR",
});
const REPUBLICATION_CODES = new Set<RepublicationNoteCode>([
  "KFM_DERIVED_REPUBLICATION",
  "SOURCE_PRESERVED",
]);

const PANEL_ID = /^kfm:provenance-citations:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,270}$/;
const CITATION_ID = /^kfm:citation:[A-Za-z0-9][A-Za-z0-9:._~+/-]{2,280}$/;
const KFM_REFERENCE = /^kfm:(?:\/\/)?[A-Za-z0-9][A-Za-z0-9._~:/+-]{2,315}$/;
const RELEASE_REF_PREFIX = ["kfm://release", "/"].join("");
const DOI = /^10\.\d{4,9}\/[a-z0-9][a-z0-9._;()/:+-]{1,220}$/i;
const HOSTNAME = /^(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$/i;
const CONTROL_CHARACTER = /[\u0000-\u0008\u000b\u000c\u000e-\u001f\u007f]/;
const MAX_REFERENCE_LENGTH = 320;
const MAX_CITATIONS = 12;

function malformed(): ProvenanceCitationsProjectionResult {
  return Object.freeze({
    ok: false,
    code: "MALFORMED_PROVENANCE_CITATIONS_PROJECTION",
  });
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  expected: ReadonlySet<string>,
): boolean {
  return (
    Object.keys(value).length === expected.size &&
    Object.keys(value).every((field) => expected.has(field))
  );
}

function isBoundedIdentifier(value: unknown, pattern: RegExp): value is string {
  return (
    typeof value === "string" &&
    value.length <= MAX_REFERENCE_LENGTH &&
    pattern.test(value) &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isSafeLabel(value: unknown): value is string {
  return (
    typeof value === "string" &&
    value.length >= 1 &&
    value.length <= 160 &&
    value === value.trim() &&
    !CONTROL_CHARACTER.test(value)
  );
}

function isPublicHttpsUrl(value: unknown): value is string {
  if (typeof value !== "string" || value.length > 500) return false;
  try {
    const parsed = new URL(value);
    return (
      parsed.protocol === "https:" &&
      parsed.username === "" &&
      parsed.password === "" &&
      parsed.port === "" &&
      parsed.hash === "" &&
      parsed.hostname !== "localhost" &&
      !parsed.hostname.includes(":") &&
      !/^\d{1,3}(?:\.\d{1,3}){3}$/.test(parsed.hostname) &&
      HOSTNAME.test(parsed.hostname) &&
      parsed.href === value
    );
  } catch {
    return false;
  }
}

function parseNullableText(value: unknown): string | null | undefined {
  if (value === null) return null;
  if (isSafeLabel(value)) return value;
  return undefined;
}

function parseNullableReference(value: unknown): string | null | undefined {
  if (value === null) return null;
  if (isBoundedIdentifier(value, KFM_REFERENCE)) return value;
  return undefined;
}

function parseNullableDoi(value: unknown): string | null | undefined {
  if (value === null) return null;
  if (
    typeof value === "string" &&
    value.length <= 255 &&
    value === value.trim() &&
    DOI.test(value)
  ) {
    return value;
  }
  return undefined;
}

function parseCitation(input: unknown): GovernedProvenanceCitation | null {
  if (!isRecord(input) || !hasExactFields(input, CITATION_FIELDS)) return null;
  if (
    !isBoundedIdentifier(input.citation_id, CITATION_ID) ||
    !isSafeLabel(input.label) ||
    !isPublicHttpsUrl(input.href) ||
    !isBoundedIdentifier(input.evidence_ref, KFM_REFERENCE) ||
    !input.evidence_ref.startsWith("kfm://evidence/")
  ) {
    return null;
  }
  const doi = parseNullableDoi(input.doi);
  if (doi === undefined) return null;
  if (doi !== null && input.href !== `https://doi.org/${doi}`) return null;

  return Object.freeze({
    citationId: input.citation_id,
    label: input.label,
    href: input.href,
    doi,
    evidenceRef: input.evidence_ref,
  });
}

function parseCitations(input: unknown): readonly GovernedProvenanceCitation[] | null {
  if (!Array.isArray(input) || input.length > MAX_CITATIONS) return null;
  const parsed: GovernedProvenanceCitation[] = [];
  const ids = new Set<string>();
  for (const candidate of input) {
    const citation = parseCitation(candidate);
    if (citation === null || ids.has(citation.citationId)) return null;
    ids.add(citation.citationId);
    parsed.push(citation);
  }
  return Object.freeze(parsed);
}

/** Parse one exact, bounded provenance-citations projection. */
export function parseProvenanceCitationsProjection(
  input: unknown,
): ProvenanceCitationsProjectionResult {
  if (!isRecord(input) || !hasExactFields(input, TOP_LEVEL_FIELDS)) {
    return malformed();
  }
  if (
    input.profile !== PROVENANCE_CITATIONS_PROJECTION_PROFILE ||
    !isBoundedIdentifier(input.panel_id, PANEL_ID) ||
    typeof input.outcome !== "string" ||
    !OUTCOMES.has(input.outcome as ProvenanceCitationsOutcome) ||
    typeof input.reason_code !== "string" ||
    !REASON_CODES.has(input.reason_code as ProvenanceCitationsReasonCode)
  ) {
    return malformed();
  }

  const outcome = input.outcome as ProvenanceCitationsOutcome;
  const reasonCode = input.reason_code as ProvenanceCitationsReasonCode;
  if (EXPECTED_REASON[outcome] !== reasonCode) return malformed();

  const title = parseNullableText(input.title);
  const activityRef = parseNullableReference(input.activity_ref);
  const citations = parseCitations(input.citations);
  const releaseManifestRef = parseNullableReference(input.release_manifest_ref);
  const republicationNoteCode =
    input.republication_note_code === null
      ? null
      : typeof input.republication_note_code === "string" &&
          REPUBLICATION_CODES.has(
            input.republication_note_code as RepublicationNoteCode,
          )
        ? (input.republication_note_code as RepublicationNoteCode)
        : undefined;
  if (
    title === undefined ||
    activityRef === undefined ||
    citations === null ||
    releaseManifestRef === undefined ||
    republicationNoteCode === undefined
  ) {
    return malformed();
  }

  const positiveIsClosed =
    outcome === "ANSWER" &&
    title !== null &&
    activityRef?.startsWith("kfm://prov/activity/") === true &&
    citations.length >= 1 &&
    republicationNoteCode !== null &&
    releaseManifestRef?.startsWith(RELEASE_REF_PREFIX) === true;
  const negativeIsEmpty =
    outcome !== "ANSWER" &&
    title === null &&
    activityRef === null &&
    citations.length === 0 &&
    republicationNoteCode === null &&
    releaseManifestRef === null;
  if (!positiveIsClosed && !negativeIsEmpty) return malformed();

  return Object.freeze({
    ok: true,
    payload: Object.freeze({
      profile: PROVENANCE_CITATIONS_PROJECTION_PROFILE,
      panelId: input.panel_id,
      outcome,
      reasonCode,
      title,
      activityRef,
      citations,
      republicationNoteCode,
      releaseManifestRef,
    }),
  });
}
