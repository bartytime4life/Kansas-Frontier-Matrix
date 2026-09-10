/**
 * Transport-free reconciliation adapter for the saved Sites v15 ACS context.
 *
 * This adapter joins a bounded ACS fixture to an already-owned county reference
 * projection. It does not fetch TIGERweb geometry, admit a source, resolve
 * evidence, or authorize report/export use.
 */

export const ACS_POPULATION_CONTEXT_PROFILE =
  "kfm.explorer.acs-population-context.v1" as const;

export type AcsPopulationContextState =
  | "JOINED" | "MISSING_ACS_ROW" | "UNMATCHED_GEOID" | "DUPLICATE_GEOID"
  | "MALFORMED_ESTIMATE" | "EMPTY_RESPONSE" | "UNAVAILABLE" | "STALE_VINTAGE"
  | "UNEXPECTED_VINTAGE" | "SOURCE_CHECKPOINT_MISMATCH";

export type CountyReference = Readonly<{ geoid: string; name: string }>;

export type AcsPopulationContext = Readonly<{
  profile: typeof ACS_POPULATION_CONTEXT_PROFILE;
  state: AcsPopulationContextState;
  geoid: string | null;
  countyName: string | null;
  population: number | null;
  dataset: "ACS 2024 5-year Data Profiles";
  variable: "DP05_0001E";
  sourceRole: "EXTERNAL_CONTEXT_ONLY";
  knowledgeCharacter: "AGGREGATE_ESTIMATE";
  evidenceRefs: readonly string[];
  reportEligible: false;
  exportEligible: false;
  message: string;
}>;

type Fixture = Readonly<{
  dataset?: unknown; vintage?: unknown; retrieved_at?: unknown; status?: unknown;
  rows?: unknown; sites_source_commit?: unknown; sites_archive_sha256?: unknown;
}>;

const EXPECTED_DATASET = "ACS 2024 5-year Data Profiles" as const;
const EXPECTED_VINTAGE = "2024";
const VARIABLE = "DP05_0001E" as const;
const SITES_SOURCE_COMMIT = "459916cb3622385b2b0d19b83e7fb666966d9ab3";
const SITES_ARCHIVE_SHA256 = "ca1ae92ada5ea03191094224131bc06fcd820e3185db383bd61482d65887ba76";
const GEOID = /^20\d{3}$/;
const NON_NEGATIVE_INTEGER = /^(0|[1-9]\d*)$/;

function result(
  state: AcsPopulationContextState,
  message: string,
  values: Partial<Pick<AcsPopulationContext, "geoid" | "countyName" | "population">> = {},
): AcsPopulationContext {
  return Object.freeze({
    profile: ACS_POPULATION_CONTEXT_PROFILE, state,
    geoid: values.geoid ?? null, countyName: values.countyName ?? null,
    population: values.population ?? null, dataset: EXPECTED_DATASET,
    variable: VARIABLE, sourceRole: "EXTERNAL_CONTEXT_ONLY",
    knowledgeCharacter: "AGGREGATE_ESTIMATE", evidenceRefs: Object.freeze([]),
    reportEligible: false, exportEligible: false, message,
  });
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function validRetrievedAt(value: unknown): boolean {
  return typeof value === "string" && Number.isFinite(Date.parse(value));
}

export function reconcileAcsPopulationContext(
  countyReferences: readonly CountyReference[],
  input: Fixture,
  options: Readonly<{ expectedVintage?: string; stale?: boolean }> = {},
): readonly AcsPopulationContext[] {
  if (input.status === "UNAVAILABLE") {
    return Object.freeze([result("UNAVAILABLE", "ACS context is unavailable; no zero or fallback value was produced.")]);
  }
  if (input.sites_source_commit !== SITES_SOURCE_COMMIT || input.sites_archive_sha256 !== SITES_ARCHIVE_SHA256) {
    return Object.freeze([result("SOURCE_CHECKPOINT_MISMATCH", "The Sites source commit or saved archive digest does not match the reviewed v15 checkpoint.")]);
  }
  if (input.dataset !== EXPECTED_DATASET || input.vintage !== (options.expectedVintage ?? EXPECTED_VINTAGE)) {
    return Object.freeze([result("UNEXPECTED_VINTAGE", "The ACS dataset identity or vintage does not match the pinned context contract.")]);
  }
  if (!validRetrievedAt(input.retrieved_at)) {
    return Object.freeze([result("UNAVAILABLE", "The ACS retrieval timestamp is missing or invalid.")]);
  }
  if (options.stale === true) {
    return Object.freeze([result("STALE_VINTAGE", "The caller marked this pinned ACS context stale; no values were joined.")]);
  }
  if (!Array.isArray(input.rows) || input.rows.length === 0) {
    return Object.freeze([result("EMPTY_RESPONSE", "The bounded ACS response contained no rows; absence is not zero population.")]);
  }

  const references = new Map<string, CountyReference>();
  const duplicateReferences = new Set<string>();
  for (const county of countyReferences) {
    if (!GEOID.test(county.geoid) || county.name.trim().length === 0) continue;
    if (references.has(county.geoid)) duplicateReferences.add(county.geoid);
    references.set(county.geoid, county);
  }

  const seenRows = new Set<string>();
  const output: AcsPopulationContext[] = [];
  for (const rawRow of input.rows) {
    if (!isRecord(rawRow) || typeof rawRow.GEOID !== "string" || !GEOID.test(rawRow.GEOID)) {
      output.push(result("UNMATCHED_GEOID", "An ACS row lacked a valid Kansas county GEOID."));
      continue;
    }
    const geoid = rawRow.GEOID;
    const county = references.get(geoid);
    if (seenRows.has(geoid) || duplicateReferences.has(geoid)) {
      output.push(result("DUPLICATE_GEOID", "Duplicate GEOID identity prevents a deterministic county join.", { geoid, countyName: county?.name }));
      continue;
    }
    seenRows.add(geoid);
    if (county === undefined) {
      output.push(result("UNMATCHED_GEOID", "The ACS GEOID has no matching county in the repository-owned reference projection.", { geoid }));
      continue;
    }
    if (typeof rawRow[VARIABLE] !== "string" || !NON_NEGATIVE_INTEGER.test(rawRow[VARIABLE])) {
      output.push(result("MALFORMED_ESTIMATE", "The ACS population estimate is missing or malformed; no value was inferred.", { geoid, countyName: county.name }));
      continue;
    }
    output.push(result("JOINED", "ACS aggregate population context joined by exact county GEOID.", {
      geoid, countyName: county.name, population: Number(rawRow[VARIABLE]),
    }));
  }

  for (const county of references.values()) {
    if (!seenRows.has(county.geoid) && !duplicateReferences.has(county.geoid)) {
      output.push(result("MISSING_ACS_ROW", "The county reference has no ACS row; absence is not zero population.", {
        geoid: county.geoid, countyName: county.name,
      }));
    }
  }
  return Object.freeze(output);
}
