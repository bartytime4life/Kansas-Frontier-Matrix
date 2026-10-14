/** Reviewed USGS ComCat earthquake snapshot carrier (ADR-0049). Never acquires or approves source data.
 *  Mirrors packages/release/src/release/core.py (EARTHQUAKES profile: one data year, one evidence bundle per UTC
 *  origin month part), pipelines/domains/hazards/earthquake_validate.py, earthquake_package.earthquake_catalog and
 *  release/earthquake_projection.py. Records are catalog solutions, never shaking estimates or alerts. */
import { canonical, capturedCanonical, capturedObject, codepointOrder, digest, object, parseCapturedObject, parseWaterJson, pythonFloatToken, releaseGate, same, time, verified, without, type CapturedObject, type CapturedValue, type Entry } from "./governed-water";
import { day } from "./governed-weather";

export const EARTHQUAKE_PACKAGE_LIMIT = 8 * 1024 * 1024;
const NAMES = ["candidate.json", "catalog.json", "evidence.json", "validation.json"] as const;
const DIGEST = /^sha256:[a-f0-9]{64}$/, HASH = /^[a-f0-9]{64}$/;
const SOURCE_ID = "usgs-earthquakes";
// Must match connectors/usgs/src/usgs/earthquake.py KANSAS_CONTEXT and earthquake_normalize.KANSAS_RECTANGLE.
const BOUNDS = [-102.1, 36.9, -94.5, 40.1];
const KANSAS_RECTANGLE = [-102.0517, 37.0, -94.5884, 40.0];
// Must match release.core.MONTH_PART_SIZE, EARTHQUAKES.max_observations and earthquake_projection.STALE_AFTER_DAYS.
export const EARTHQUAKE_MONTH_PART_SIZE = 127;
const MAX_OBSERVATIONS = 6000;
const STALE_AFTER_DAYS = 30;
const FIRST_YEAR = 1973;
const WITHHELD = ["STATUS_DELETED"] as const;
export const EARTHQUAKE_FLAGS = ["MAGNITUDE_ABSENT", "DEPTH_ABSENT", "REVIEW_AUTOMATIC", "REVIEW_STATUS_UNKNOWN", "CONTEXT_MARGIN"] as const;
type Obj = Record<string, unknown>;
export type Earthquake = { id: string; event_id: string; aliases: string[]; origin_utc: string; updated_utc: string | null; longitude: number; latitude: number;
  depth_km: number | null; magnitude: number | null; magnitude_type: string | null; review_status: string | null; net: string | null; place: string | null;
  flags: string[]; feature_sha256: string; page_digest: string; retrieved_at: string; evidence_ref: string; record_digest: string };
type MonthSummary = { month: number; query_status: number; events: number };
type EarthquakeCandidate = { candidate_id: string; data_year: number; bounds: number[]; retrieved_at: string; months: MonthSummary[]; observations: Earthquake[];
  latest_event_date: string | null; withheld_counts: Record<string, number>; year_state: string; coverage: string; source_id: string; release_state: string };
export type EarthquakeEntry = Omit<Entry, "station_id"> & { month: number; part: number };
export type EarthquakeCatalog = { dataset: Obj; entries: Obj[] };
export type EarthquakePackage = { manifest: Obj & { package_id: string; candidate_id: string; start: string; end: string; created_at: string; rollback_target: string | null };
  candidate: EarthquakeCandidate; catalog: EarthquakeCatalog; evidence: { entries: EarthquakeEntry[] }; validation: Obj };
export type EarthquakeSelection = { months: number[]; observation_count: number; review_status: Record<string, number>; context_margin_count: number;
  magnitude_range: [number, number] | null; latest_event_date: string | null };
export type EarthquakeResponse = { envelope: Obj & { outcome: string; reason_code: string; freshness?: string }; data?: Obj & { observations?: Earthquake[]; entries?: EarthquakeEntry[];
  months?: number[]; dataset?: Obj; selection?: EarthquakeSelection } };
// ADR-0049: the admitted ComCat license. Must match EARTHQUAKE_SELF_RELEASE_LICENSES in packages/policy-runtime/src/policy_runtime/core.py.
export const EARTHQUAKE_SELF_RELEASE_LICENSES: readonly string[] = ["U.S. Public Domain (USGS works, 17 U.S.C. 105); ComCat solutions subject to revision"];
export const EARTHQUAKE_DECISION_PROFILE = "kfm.earthquake-release-decision/v1";
const ATTRIBUTION = "U.S. Geological Survey, Earthquake Hazards Program, ANSS Comprehensive Earthquake Catalog (ComCat). "
  + "Solutions may be revised. Catalog solutions, not shaking estimates or alerts.";

const IDENTIFIER = /^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$/;
const ORIGIN = /^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}Z$/;
// The UTC instant form the capture writes (earthquake_normalize.UTC_INSTANT).
const UTC_INSTANT = /^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,6})?Z$/;
// JSON Schema date-time: any RFC 3339 offset; the UTC-only rule is checked after the schema, as in Python.
const DATE_TIME = /^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$/i;
const isInstant = (value: unknown) => { try { time(value); return true; } catch { return false; } };
const int = (v: unknown, low: number, high = Number.MAX_SAFE_INTEGER) => Number.isInteger(v) && (v as number) >= low && (v as number) <= high;
const optionalText = (v: unknown, max: number) => v === null || typeof v === "string" && v.length >= 1 && v.length <= max;
const inRange = (v: unknown, low: number, high: number) => typeof v === "number" && Number.isFinite(v) && v >= low && v <= high;
const optionalRange = (v: unknown, low: number, high: number) => v === null || inRange(v, low, high);

/** Closed schemas/contracts/v1/domains/hazards/earthquake_record.schema.json, applied first as the Python validator does. */
const RECORD_KEYS = ["aliases", "depth_km", "event_id", "evidence_ref", "feature_sha256", "flags", "id", "latitude", "longitude", "magnitude", "magnitude_type",
  "net", "origin_utc", "page_digest", "place", "profile", "record_digest", "retrieved_at", "review_status", "updated_utc"];
function recordShapeValid(r: Earthquake & Obj): boolean {
  return same(Object.keys(r).sort(), RECORD_KEYS) && r.profile === "kfm.earthquake-record/v1"
    && typeof r.id === "string" && r.id.startsWith("kfm:quake:") && HASH.test(r.id.slice(10))
    && typeof r.event_id === "string" && IDENTIFIER.test(r.event_id)
    && Array.isArray(r.aliases) && r.aliases.length >= 1 && r.aliases.length <= 128 && new Set(r.aliases).size === r.aliases.length
    && r.aliases.every(a => typeof a === "string" && IDENTIFIER.test(a))
    && typeof r.origin_utc === "string" && ORIGIN.test(r.origin_utc) && (r.updated_utc === null || typeof r.updated_utc === "string" && ORIGIN.test(r.updated_utc))
    && inRange(r.longitude, -102.1, -94.5) && inRange(r.latitude, 36.9, 40.1) && optionalRange(r.depth_km, -10, 1000) && optionalRange(r.magnitude, -2, 10)
    && optionalText(r.magnitude_type, 16) && optionalText(r.review_status, 16) && optionalText(r.net, 16) && optionalText(r.place, 256)
    && Array.isArray(r.flags) && r.flags.length <= 5 && new Set(r.flags).size === r.flags.length && r.flags.every(f => (EARTHQUAKE_FLAGS as readonly string[]).includes(f))
    && typeof r.feature_sha256 === "string" && DIGEST.test(r.feature_sha256) && typeof r.page_digest === "string" && DIGEST.test(r.page_digest)
    && typeof r.retrieved_at === "string" && DATE_TIME.test(r.retrieved_at)
    && typeof r.evidence_ref === "string" && r.evidence_ref.startsWith("kfm:evidence:quake:") && HASH.test(r.evidence_ref.slice(19))
    && typeof r.record_digest === "string" && DIGEST.test(r.record_digest);
}

/** earthquake_normalize.number: the source value at 4 decimal places, written as an integer when whole. Judged on the
 *  captured token, so 5.0 for 5 and over-precise values are refused exactly as the Python type check refuses them. */
function canonicalNumber(token: CapturedValue | undefined): boolean {
  const text = capturedCanonical(token ?? null);
  if (text === "null") return true;
  const value = Number(text);
  if (!Number.isFinite(value) || Number(value.toFixed(4)) !== value) return false;
  return text === (Number.isInteger(value) ? String(value) : pythonFloatToken(value));
}

function expectedFlags(r: Earthquake): string[] {
  const flags: string[] = [];
  if (r.magnitude === null) flags.push("MAGNITUDE_ABSENT");
  if (r.depth_km === null) flags.push("DEPTH_ABSENT");
  if (r.review_status === "automatic") flags.push("REVIEW_AUTOMATIC");
  else if (r.review_status !== "reviewed") flags.push("REVIEW_STATUS_UNKNOWN");
  const [west, south, east, north] = KANSAS_RECTANGLE;
  if (!(west <= r.longitude && r.longitude <= east && south <= r.latitude && r.latitude <= north)) flags.push("CONTEXT_MARGIN");
  return flags;
}

/** (month, part, records) for every UTC origin month that has records, as SnapshotProfile.month_groups. */
export function earthquakeMonthGroups(observations: Earthquake[]): [number, number, Earthquake[]][] {
  const groups: [number, number, Earthquake[]][] = [];
  for (let month = 1; month <= 12; month++) {
    const records = observations.filter(r => r.origin_utc.slice(5, 7) === String(month).padStart(2, "0"));
    for (let first = 0; first < records.length; first += EARTHQUAKE_MONTH_PART_SIZE) groups.push([month, first / EARTHQUAKE_MONTH_PART_SIZE + 1, records.slice(first, first + EARTHQUAKE_MONTH_PART_SIZE)]);
  }
  return groups;
}

const monthRef = (start: string, month: number, part: number, candidateId: string) => `kfm://hazards/earthquakes/${start.slice(0, 4)}-${String(month).padStart(2, "0")}/part-${part}/${candidateId.split(":")[1]}`;
const latestDate = (records: Earthquake[]) => records.length ? records.map(r => r.origin_utc.slice(0, 10)).sort(codepointOrder).at(-1)! : null;
const reviewStatus = (records: Earthquake[]) => Object.fromEntries([...records.reduce((m, r) => m.set(r.review_status ?? "unknown", (m.get(r.review_status ?? "unknown") ?? 0) + 1), new Map<string, number>())].sort(([a], [b]) => codepointOrder(a, b)));
const marginCount = (records: Earthquake[]) => records.filter(r => r.flags.includes("CONTEXT_MARGIN")).length;
function magnitudeRange(records: Earthquake[]): [number, number] | null {
  const values = records.map(r => r.magnitude).filter((m): m is number => m !== null);
  return values.length ? [Math.min(...values), Math.max(...values)] : null;
}
export function earthquakeSelection(months: number[], records: Earthquake[]): EarthquakeSelection {
  return { months, observation_count: records.length, review_status: reviewStatus(records), context_margin_count: marginCount(records),
    magnitude_range: magnitudeRange(records), latest_event_date: latestDate(records) };
}

const CANDIDATE_KEYS = ["bounds", "candidate_id", "capture_id", "coverage", "data_year", "latest_event_date", "months", "observations", "profile", "release_state",
  "retrieved_at", "review_state", "source_admission", "source_id", "withheld_counts", "year_state"];

/** Inner provenance and record rules, as earthquake_validate.validate_candidate. Digests are recomputed over the captured
 *  Python serialization (numbers kept as written). */
async function validateEarthquakeCandidate(candidate: EarthquakeCandidate & Obj, captured: CapturedObject, validation: Obj, capturedValidation: CapturedObject) {
  if (!same(Object.keys(candidate).sort(), CANDIDATE_KEYS)) throw new Error("CANDIDATE_SHAPE_INVALID");
  if (candidate.profile !== "kfm.earthquake-candidate/v1" || candidate.source_id !== SOURCE_ID || !same(candidate.bounds, BOUNDS)
      || typeof candidate.capture_id !== "string" || !DIGEST.test(candidate.capture_id) || candidate.source_admission !== "PENDING" || candidate.review_state !== "PENDING"
      || candidate.release_state !== "UNRELEASED" || candidate.coverage !== "NOT_ESTABLISHED") throw new Error("CANDIDATE_AUTHORITY_OR_PROFILE_INVALID");
  if (await digest(capturedCanonical(captured, "candidate_id")) !== candidate.candidate_id) throw new Error("CANDIDATE_DIGEST_MISMATCH");
  // A UTC instant, never a date or a zone-free time, so year_state and record ordering compare instants.
  const year = candidate.data_year, retrieved = candidate.retrieved_at;
  if (!int(year, FIRST_YEAR, 2200) || typeof retrieved !== "string" || !UTC_INSTANT.test(retrieved) || !isInstant(retrieved)
      || Number(retrieved.slice(0, 4)) < year || candidate.year_state !== (Number(retrieved.slice(0, 4)) > year ? "CLOSED" : "OPEN")) throw new Error("CANDIDATE_TIME_INVALID");
  const counts = candidate.withheld_counts;
  if (!counts || typeof counts !== "object" || Array.isArray(counts) || !same(Object.keys(counts).sort(), [...WITHHELD]) || Object.values(counts).some(n => !int(n, 0))) throw new Error("WITHHELD_COUNTS_INVALID");
  const records = candidate.observations as (Earthquake & Obj)[], capturedRecords = captured.observations;
  if (!Array.isArray(records) || records.length > MAX_OBSERVATIONS || !Array.isArray(capturedRecords) || capturedRecords.length !== records.length) throw new Error("OBSERVATION_COUNT_INVALID");
  const aliases = new Set<string>(), perMonth = new Array(12).fill(0) as number[];
  let previous: Earthquake | null = null;
  for (let i = 0; i < records.length; i++) {
    const r = records[i], capturedRecord = capturedObject(capturedRecords[i]);
    if (!recordShapeValid(r)) throw new Error("EARTHQUAKE_SCHEMA_INVALID");
    if (await digest(capturedCanonical(capturedRecord, "record_digest")) !== r.record_digest) throw new Error("RECORD_DIGEST_MISMATCH");
    const key = (await digest(canonical([SOURCE_ID, r.event_id]))).slice(7);
    if (r.id !== "kfm:quake:" + key || r.evidence_ref !== "kfm:evidence:quake:" + key) throw new Error("RECORD_IDENTITY_MISMATCH");
    // The preferred id leads its aliases, and no alias names two records.
    if (r.aliases[0] !== r.event_id || r.aliases.some(a => aliases.has(a))) throw new Error("RECORD_ORDER_OR_DUPLICATE");
    r.aliases.forEach(a => aliases.add(a));
    if (previous && (codepointOrder(r.origin_utc, previous.origin_utc) || codepointOrder(r.event_id, previous.event_id)) <= 0) throw new Error("RECORD_ORDER_OR_DUPLICATE");
    previous = r;
    if (!isInstant(r.origin_utc) || r.updated_utc !== null && !isInstant(r.updated_utc)) throw new Error("RECORD_TIME_INVALID");
    const origin = new Date(time(r.origin_utc));
    if (origin.getUTCFullYear() !== year || !UTC_INSTANT.test(r.retrieved_at) || codepointOrder(r.retrieved_at, retrieved) > 0) throw new Error("RECORD_TIME_INVALID");
    perMonth[origin.getUTCMonth()]++;
    if (!["longitude", "latitude", "depth_km", "magnitude"].every(field => canonicalNumber(capturedRecord[field]))) throw new Error("RECORD_NUMBER_NOT_CANONICAL");
    if (r.review_status === "deleted") throw new Error("RECORD_STATUS_WITHHELD");
    if (!same(r.flags, expectedFlags(r))) throw new Error("RECORD_FLAGS_MISMATCH");
  }
  const months = candidate.months;
  if (!Array.isArray(months) || months.length !== 12 || months.some((m, i) => !m || typeof m !== "object" || Array.isArray(m)
      || !same(Object.keys(m).sort(), ["events", "month", "query_status"]) || m.month !== i + 1 || ![200, 204].includes(m.query_status)
      || m.events !== perMonth[i] || m.query_status === 204 && m.events !== 0)) throw new Error("MONTH_SUMMARY_MISMATCH");
  if (candidate.latest_event_date !== latestDate(records)) throw new Error("LATEST_EVENT_DATE_MISMATCH");
  if (await digest(capturedCanonical(capturedValidation, "receipt_digest")) !== validation.receipt_digest) throw new Error("VALIDATION_RECEIPT_INVALID");
  const expected = { profile: "kfm.earthquake-validation/v1", candidate_id: candidate.candidate_id, outcome: "PASS", observations: records.length,
    withheld: Object.values(counts).reduce((a, b) => a + b, 0), review_required: true, promotion_authorized: false, release_authorized: false, publication_authorized: false };
  if (!same(validation, { ...expected, receipt_digest: await digest(canonical(expected)) })) throw new Error("VALIDATION_RECEIPT_MISMATCH");
}

/** The catalog earthquake_package.earthquake_catalog builds from a validated candidate; served data never trusts it unchecked. */
function expectedCatalog(candidate: EarthquakeCandidate, validation: Obj, start: string) {
  const observations = candidate.observations;
  const dataset = { id: `usgs-earthquakes:ks-envelope:${candidate.data_year}`, title: `USGS ComCat earthquakes, Kansas context envelope, ${candidate.data_year}`,
    source_id: candidate.source_id, bounds: candidate.bounds, data_year: candidate.data_year, observation_count: observations.length,
    withheld_counts: candidate.withheld_counts, context_margin_count: marginCount(observations), review_status: reviewStatus(observations),
    magnitude_range: magnitudeRange(observations), latest_event_date: candidate.latest_event_date, year_state: candidate.year_state, coverage: candidate.coverage,
    interval: { start, end: start.slice(0, 4) + "-12-31", basis: "origin time, UTC" }, validation_ref: validation.receipt_digest };
  const entries = earthquakeMonthGroups(observations).map(([month, part, records]) => ({ month, part, observation_count: records.length, evidence_ref: monthRef(start, month, part, candidate.candidate_id) }));
  return { profile: "kfm.earthquake-catalog-candidate/v1", candidate_id: candidate.candidate_id, dataset, entries, authoritative: false, release_state: "UNRELEASED" };
}

export async function parseEarthquakePackage(text: string): Promise<EarthquakePackage> {
  if (!text || new TextEncoder().encode(text).length > EARTHQUAKE_PACKAGE_LIMIT) throw new Error("PACKAGE_LIMIT");
  const snapshot = object(parseWaterJson(text));
  if (!same(Object.keys(snapshot).sort(), ["artifacts", "manifest"])) throw new Error("SNAPSHOT_SHAPE_INVALID");
  const manifest = object(snapshot.manifest), artifacts = object(snapshot.artifacts), hashes = object(manifest.artifacts);
  if (!same(Object.keys(manifest).sort(), ["artifacts", "candidate_id", "created_at", "end", "package_id", "profile", "review_requirements", "rollback_target", "source_id", "start"])
      || manifest.profile !== "kfm.earthquake-snapshot/v1" || manifest.source_id !== SOURCE_ID) throw new Error("MANIFEST_PROFILE_INVALID");
  if (!same(manifest.review_requirements, ["source_admission", "rights", "sensitivity", "policy", "independent_review", "release"]) || manifest.rollback_target !== null && (typeof manifest.rollback_target !== "string" || !DIGEST.test(manifest.rollback_target))) throw new Error("MANIFEST_PROFILE_INVALID");
  if (await digest(canonical(without(manifest, "package_id"))) !== manifest.package_id) throw new Error("PACKAGE_DIGEST_MISMATCH");
  // One calendar data year, as release.core._calendar_year_interval.
  const start = manifest.start, end = manifest.end;
  let interval = false;
  try { interval = typeof start === "string" && typeof end === "string" && day(start) <= day(end) && start.slice(4) === "-01-01" && end.slice(4) === "-12-31" && start.slice(0, 4) === end.slice(0, 4); } catch { interval = false; }
  if (!interval) throw new Error("SNAPSHOT_INTERVAL_INVALID");
  time(manifest.created_at);
  if (!same(Object.keys(artifacts).sort(), [...NAMES].sort()) || !same(Object.keys(hashes).sort(), [...NAMES].sort())) throw new Error("ARTIFACT_CLOSURE_INVALID");
  const values: Record<string, Obj> = {};
  for (const name of NAMES) { const raw = artifacts[name]; if (typeof raw !== "string" || await digest(raw) !== hashes[name]) throw new Error("ARTIFACT_DIGEST_MISMATCH"); values[name] = object(parseWaterJson(raw)); if (values[name].candidate_id !== manifest.candidate_id) throw new Error("CANDIDATE_BINDING_MISMATCH"); }
  const candidate = values["candidate.json"] as EarthquakeCandidate & Obj, catalog = values["catalog.json"], evidence = values["evidence.json"] as { entries: EarthquakeEntry[] }, validation = values["validation.json"];
  if (candidate.release_state !== "UNRELEASED" || catalog.authoritative !== false || validation.outcome !== "PASS") throw new Error("CARRIER_CANNOT_SELF_APPROVE");
  if (!Number.isInteger(candidate.data_year) || `${String(candidate.data_year).padStart(4, "0")}-01-01` !== start || candidate.retrieved_at !== manifest.created_at) throw new Error("CANDIDATE_IDENTITY_MISMATCH");
  await validateEarthquakeCandidate(candidate, parseCapturedObject(artifacts["candidate.json"] as string), validation, parseCapturedObject(artifacts["validation.json"] as string));
  if (!same(catalog, expectedCatalog(candidate, validation, start as string))) throw new Error("CATALOG_MISMATCH");
  // One bundle per (month, part) the records produce, in order (the resolver caps a bundle at 128 members).
  const groups = earthquakeMonthGroups(candidate.observations);
  if (!groups.length || !Array.isArray(evidence.entries) || evidence.entries.length !== groups.length) throw new Error("EVIDENCE_CLOSURE_INVALID");
  for (let i = 0; i < groups.length; i++) {
    const [month, part, records] = groups[i], entry = evidence.entries[i], bundle = entry.bundle;
    if (!Number.isInteger(entry.month) || !Number.isInteger(entry.part) || entry.month !== month || entry.part !== part) throw new Error("SERIES_EVIDENCE_MISMATCH");
    const expectedRef = { ref: monthRef(start as string, month, part, candidate.candidate_id), kind: "dataset", bundle_ref: bundle.bundle_id };
    if (!same(entry.evidence_ref, expectedRef) || !same(bundle.evidence_refs, [expectedRef, ...records.map(r => ({ ref: r.evidence_ref, kind: "record", bundle_ref: bundle.bundle_id }))]) || bundle.evidence_refs.length > 128) throw new Error("MEASUREMENT_EVIDENCE_MISMATCH");
    if (!same(bundle.checksums, { candidate: candidate.candidate_id, validation: validation.receipt_digest }) || !same(bundle.source_records, [...new Set(records.map(r => r.page_digest))].sort(codepointOrder))
        || entry.verification_history.subject_ref !== expectedRef.ref) throw new Error("BUNDLE_CONTENT_BINDING_MISMATCH");
  }
  return { manifest: manifest as EarthquakePackage["manifest"], candidate, catalog: catalog as EarthquakeCatalog, evidence, validation };
}

export function earthquakesGate(pkg: EarthquakePackage, decision: Obj | null, now: string): string {
  return releaseGate(pkg, decision, now, EARTHQUAKE_DECISION_PROFILE, EARTHQUAKE_SELF_RELEASE_LICENSES);
}

export async function earthquakesNegative(reason: string, now: string, outcome = "ABSTAIN"): Promise<EarthquakeResponse> {
  const envelope = { id: "earthquakes:" + reason.toLowerCase(), version: "kfm-earthquakes-v1", issued_at: now, outcome, reason_code: reason, evidence_refs: [], policy_state: "withheld", freshness: "unknown", correction_state: "unknown" };
  return { envelope: { ...envelope, spec_hash: await digest(canonical(envelope)) } };
}

export async function projectEarthquakes(pkg: EarthquakePackage, decision: Obj | null, view: string, now: string, month: number | null = null): Promise<EarthquakeResponse> {
  const reason = earthquakesGate(pkg, decision, now); if (reason !== "ELIGIBLE") return earthquakesNegative(reason, now);
  if (!["bootstrap", "layers", "evidence"].includes(view)) return earthquakesNegative("ROUTE_NOT_FOUND", now);
  const selected = pkg.evidence.entries.filter(e => month === null || e.month === month); if (!selected.length) return earthquakesNegative("EVIDENCE_NOT_FOUND", now);
  for (const entry of selected) if (!await verified(entry as unknown as Entry, now)) return earthquakesNegative("EVIDENCE_UNRESOLVED", now);
  const refs = selected.map(e => e.evidence_ref), months = new Set(selected.map(e => e.month)), candidate = pkg.candidate;
  const observations = candidate.observations.filter(r => months.has(Number(r.origin_utc.slice(5, 7))));
  // The age of the capture: ComCat revises solutions after retrieval.
  const fresh = time(now) - time(candidate.retrieved_at) > STALE_AFTER_DAYS * 86400000 ? "stale-accepted" : "current";
  const precision = { spatial: { representation: "epicenter points in the Kansas context envelope", resolution: "EPSG:4326 longitude and latitude rounded to 4 decimal places",
      accuracy: "Catalog epicenter estimates with kilometre-scale uncertainty; the envelope (-102.1 to -94.5, 36.9 to 40.1) is not the state boundary", generalization_applied: false },
    temporal: { granularity: "Origin time in UTC to the millisecond", observation_interval: { start: pkg.manifest.start, end: pkg.manifest.end }, freshness_class: fresh },
    attribute: { measures: { magnitude: "catalog magnitude of the stated magnitude_type", depth_km: "hypocentral depth in kilometres" },
      classification_granularity: "Magnitude types (ml, md, mb_lg, mww, ...) are not interchangeable; automatic solutions are flagged; deleted solutions are withheld" },
    evidence_refs: refs, transform_receipt_refs: ["kfm://receipt/validation/" + String(pkg.validation.receipt_digest).split(":")[1]] };
  const envelope = { id: "earthquakes:" + view, version: "kfm-earthquakes-v1", issued_at: now, outcome: "ANSWER", reason_code: "RELEASED_SNAPSHOT", evidence_refs: refs, policy_state: "approved_snapshot", freshness: fresh, correction_state: "ACTIVE", precision_actually_used: precision };
  const common = { package_id: pkg.manifest.package_id, source_id: SOURCE_ID, coverage: candidate.coverage, data_year: candidate.data_year, year_state: candidate.year_state,
    bounds: candidate.bounds, retrieved_at: candidate.retrieved_at, reviewed_at: decision!.reviewed_at, released_at: decision!.released_at,
    approval_expires_at: decision!.expires_at, stale_after_days: STALE_AFTER_DAYS, correction_state: "ACTIVE", attribution: ATTRIBUTION, life_safety: "not_for_life_safety" };
  const sortedMonths = [...months].sort((a, b) => a - b);
  const data = view === "bootstrap" ? { ...common, layers: [{ id: "usgs-earthquakes-ks", title: "Reviewed USGS earthquakes, Kansas context envelope", evidence_eligible: true }], observation_count: observations.length, months: sortedMonths }
    : view === "layers" ? { ...common, dataset: { ...pkg.catalog.dataset, scope: "data_year" }, selection: earthquakeSelection(sortedMonths, observations), observations }
    : { ...common, entries: selected.map(({ month: m, part, evidence_ref, bundle, verification_history }) => ({ month: m, part, evidence_ref, bundle, verification_history })) };
  return { envelope: { ...envelope, spec_hash: await digest(canonical(envelope)) }, data };
}
