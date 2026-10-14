/** Reviewed USCRN daily soil snapshot carrier (ADR-0046). Never acquires or approves source data.
 *  Mirrors packages/release/src/release/core.py (SOIL profile, one evidence bundle per station and
 *  depth), pipelines/domains/soil/uscrn_daily_validate.py and release/soil_projection.py. */
import { canonical, capturedCanonical, capturedObject, digest, microseconds, object, parseCapturedObject, parseWaterJson, releaseGate, same, time, verified, without, type CapturedObject, type Entry } from "./governed-water";
import { day } from "./governed-weather";

export const SOIL_PACKAGE_LIMIT = 8 * 1024 * 1024;
const NAMES = ["candidate.json", "catalog.json", "evidence.json", "validation.json"] as const;
const DIGEST = /^sha256:[a-f0-9]{64}$/, HASH = /^[a-f0-9]{64}$/;
// Ordered as connectors/noaa/src/noaa/uscrn_daily.py STATIONS.
export const SOIL_STATIONS: readonly string[] = ["53974", "03067"];
const STATION_NAMES: Record<string, string> = { "53974": "Manhattan 6 SSW", "03067": "Oakley 19 SSW" };
export const SOIL_DEPTHS_CM: readonly number[] = [5, 10, 20, 50, 100];
export const SOIL_VARIABLES: readonly string[] = ["SOIL_MOISTURE", "SOIL_TEMP"];
const UNITS: Record<string, string> = { SOIL_MOISTURE: "m3/m3", SOIL_TEMP: "degC" };
const RANGES: Record<string, [number, number]> = { SOIL_MOISTURE: [0, 1], SOIL_TEMP: [-50, 60] };
const SENTINELS: Record<string, string> = { SOIL_MOISTURE: "-99.000", SOIL_TEMP: "-9999.0" };
const TOKENS: Record<string, RegExp> = { SOIL_MOISTURE: /^-?\d{1,2}\.\d{3}$/, SOIL_TEMP: /^-?\d{1,4}\.\d$/ };
const WITHHELD = ["MISSING", "OUT_OF_RANGE"] as const;
// USCRN daily01 days are local standard time; Manhattan and Oakley are both on Central (UTC-6).
// Must match STANDARD_OFFSET_HOURS in packages/release/src/release/soil_projection.py.
export const SOIL_STANDARD_OFFSET_HOURS: Readonly<Record<string, number>> = { "53974": -6, "03067": -6 };
type Obj = Record<string, unknown>;
export type SoilStation = { id: string; name: string; geometry: { type: "Point"; coordinates: [number, number] }; page_digest: string; retrieved_at: string };
export type SoilObservation = { id: string; station_id: string; variable: string; depth_cm: number; observation_date: string; source_token: string; value: number | null;
  unit: string; withheld: string | null; datalogger_version: string; source_role: string; page_digest: string; retrieved_at: string; evidence_ref: string; record_digest: string };
type SoilCandidate = { candidate_id: string; start: string; end: string; retrieved_at: string; coverage: string; stale_after_days: number;
  stations: SoilStation[]; observations: SoilObservation[]; freshness_at_capture: Record<string, string>; release_state: string };
export type SoilEntry = Entry & { series: number };
export type SoilPackage = { manifest: Obj & { package_id: string; candidate_id: string; start: string; end: string; created_at: string; rollback_target: string | null };
  candidate: SoilCandidate; evidence: { entries: SoilEntry[] }; validation: Obj };
export type SoilResponse = { envelope: Obj & { outcome: string; reason_code: string }; data?: Obj & { stations?: SoilStation[]; observations?: SoilObservation[]; entries?: SoilEntry[] } };
// ADR-0046: the admitted USCRN license. Must match SOIL_SELF_RELEASE_LICENSES in packages/policy-runtime/src/policy_runtime/core.py.
export const SOIL_SELF_RELEASE_LICENSES: readonly string[] = ["U.S. Public Domain (NOAA federal station data, 17 U.S.C. 105); USCRN data subject to revision"];
export const SOIL_DECISION_PROFILE = "kfm.soil-release-decision/v1";
const ATTRIBUTION = "NOAA National Centers for Environmental Information, U.S. Climate Reference Network (USCRN) daily01 product; "
  + "Diamond et al. (2013), Bull. Amer. Meteor. Soc. 94, 485-498, doi:10.1175/BAMS-D-12-00170.1. Values may be revised.";

/** (value, withheld) for one daily token, as uscrn_daily_normalize.reading. */
function reading(variable: string, token: string): [number | null, string | null] {
  if (token === SENTINELS[variable]) return [null, "MISSING"];
  const value = Number(token), [low, high] = RANGES[variable];
  if (!Number.isFinite(value) || value < low || value > high) return [null, "OUT_OF_RANGE"];
  return [value, null];
}

const CANDIDATE_KEYS = ["candidate_id", "capture_id", "coverage", "end", "freshness_at_capture", "observations", "profile", "release_state", "retrieved_at", "review_state",
  "source_admission", "source_id", "stale_after_days", "start", "stations", "withheld_counts"];
const OBSERVATION_KEYS = ["datalogger_version", "depth_cm", "evidence_ref", "id", "observation_date", "page_digest", "profile", "record_digest", "retrieved_at",
  "source_role", "source_token", "station_id", "unit", "value", "variable", "withheld"];
const STATION_KEYS = ["geometry", "id", "name", "page_digest", "retrieved_at"];
const isTime = (value: unknown) => { try { time(value); return true; } catch { return false; } };
type SoilRecord = SoilObservation & Obj;

/** Closed schemas/contracts/v1/domains/soil/daily_soil_observation.schema.json, applied first as the Python validator does. */
function observationShapeValid(r: SoilRecord): boolean {
  return same(Object.keys(r).sort(), OBSERVATION_KEYS) && r.profile === "kfm.daily-soil-observation/v1"
    && typeof r.id === "string" && r.id.startsWith("kfm:soil:") && HASH.test(r.id.slice(9))
    && SOIL_STATIONS.includes(r.station_id) && UNITS[r.variable] !== undefined && SOIL_DEPTHS_CM.includes(r.depth_cm)
    && typeof r.observation_date === "string" && /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/.test(r.observation_date)
    && typeof r.source_token === "string" && /^-?[0-9]{1,4}\.[0-9]{1,3}$/.test(r.source_token)
    && (r.value === null || typeof r.value === "number") && (r.unit === "m3/m3" || r.unit === "degC")
    && [null, ...WITHHELD].includes(r.withheld as never)
    && typeof r.datalogger_version === "string" && /^[0-9A-Za-z.-]{1,16}$/.test(r.datalogger_version)
    && r.source_role === "reference_station"
    && typeof r.page_digest === "string" && DIGEST.test(r.page_digest) && isTime(r.retrieved_at)
    && typeof r.evidence_ref === "string" && r.evidence_ref.startsWith("kfm:evidence:soil:") && HASH.test(r.evidence_ref.slice(18))
    && typeof r.record_digest === "string" && DIGEST.test(r.record_digest);
}

/** Python sorts (station_id, observation_date, variable, depth_cm): strings by code point, depth numerically. */
function order(a: SoilObservation, b: SoilObservation): number {
  for (const key of ["station_id", "observation_date", "variable"] as const) if (a[key] !== b[key]) return a[key] < b[key] ? -1 : 1;
  return a.depth_cm - b.depth_cm;
}

/** Inner provenance and record rules, as uscrn_daily_validate.validate_candidate. Digests are recomputed
 *  over the captured Python serialization (numbers kept as written). */
async function validateSoilCandidate(candidate: SoilCandidate & Obj, captured: CapturedObject, validation: Obj, capturedValidation: CapturedObject) {
  if (!same(Object.keys(candidate).sort(), CANDIDATE_KEYS)) throw new Error("CANDIDATE_SHAPE_INVALID");
  if (candidate.profile !== "kfm.uscrn-daily-candidate/v1" || candidate.source_id !== "noaa-uscrn" || typeof candidate.capture_id !== "string" || !DIGEST.test(candidate.capture_id)
      || candidate.source_admission !== "PENDING" || candidate.review_state !== "PENDING" || candidate.release_state !== "UNRELEASED" || candidate.stale_after_days !== 3) throw new Error("CANDIDATE_AUTHORITY_OR_PROFILE_INVALID");
  if (await digest(capturedCanonical(captured, "candidate_id")) !== candidate.candidate_id) throw new Error("CANDIDATE_DIGEST_MISMATCH");
  const start = day(candidate.start), end = day(candidate.end);
  if (end - start !== 29 * 86400000 || typeof candidate.retrieved_at !== "string" || candidate.retrieved_at.slice(0, 10) < candidate.end) throw new Error("CANDIDATE_INTERVAL_INVALID");
  if (!Array.isArray(candidate.stations) || !same(candidate.stations.map(s => object(s).id), SOIL_STATIONS)) throw new Error("STATION_SCOPE_INVALID");
  for (const s of candidate.stations) {
    const xy = Array.isArray(s.geometry?.coordinates) ? s.geometry.coordinates : null;
    if (!same(Object.keys(s).sort(), STATION_KEYS) || !xy || !same(s.geometry, { type: "Point", coordinates: xy }) || xy.length !== 2
        || !xy.every(v => typeof v === "number" && Number.isFinite(v)) || xy[0] < -102.2 || xy[0] > -94.4 || xy[1] < 36.9 || xy[1] > 40.1
        || s.name !== STATION_NAMES[s.id] || typeof s.page_digest !== "string" || !DIGEST.test(s.page_digest)
        || !isTime(s.retrieved_at) || microseconds(s.retrieved_at) > microseconds(candidate.retrieved_at)) throw new Error("STATION_SHAPE_INVALID");
  }
  const records = candidate.observations as SoilRecord[], capturedRecords = captured.observations;
  if (!Array.isArray(records) || records.length > SOIL_STATIONS.length * SOIL_VARIABLES.length * SOIL_DEPTHS_CM.length * 30
      || !Array.isArray(capturedRecords) || capturedRecords.length !== records.length) throw new Error("OBSERVATION_COUNT_INVALID");
  const seen = new Set<string>();
  for (let i = 0; i < records.length; i++) {
    const record = records[i];
    if (!observationShapeValid(record)) throw new Error("SOIL_OBSERVATION_SCHEMA_INVALID");
    if (await digest(capturedCanonical(capturedObject(capturedRecords[i]), "record_digest")) !== record.record_digest) throw new Error("OBSERVATION_DIGEST_MISMATCH");
    const key = canonical([record.station_id, record.variable, record.depth_cm, record.observation_date]);
    const identity = (await digest(key)).slice(7);
    if (record.id !== "kfm:soil:" + identity || record.evidence_ref !== "kfm:evidence:soil:" + identity) throw new Error("OBSERVATION_IDENTITY_MISMATCH");
    const date = day(record.observation_date);
    // Microseconds, not Date.parse milliseconds: .000002Z after .000001Z is later.
    if (date < start || date > end || microseconds(record.retrieved_at) > microseconds(candidate.retrieved_at)) throw new Error("OBSERVATION_DATE_INVALID");
    if (!TOKENS[record.variable].test(record.source_token)) throw new Error("OBSERVATION_TOKEN_INVALID");
    if (record.unit !== UNITS[record.variable]) throw new Error("OBSERVATION_UNIT_MISMATCH");
    if (!same([record.value, record.withheld], reading(record.variable, record.source_token))) throw new Error("OBSERVATION_VALUE_MISMATCH");
    if (seen.has(key)) throw new Error("DUPLICATE_STATION_DAY_VALUE");
    seen.add(key);
  }
  // A source row yields every variable at every depth: a represented station-day must be complete.
  const days = new Map<string, Set<string>>();
  for (const r of records) { const k = r.station_id + "|" + r.observation_date; if (!days.has(k)) days.set(k, new Set()); days.get(k)!.add(r.variable + "|" + r.depth_cm); }
  if ([...days.values()].some(values => values.size !== SOIL_VARIABLES.length * SOIL_DEPTHS_CM.length)) throw new Error("STATION_DAY_INCOMPLETE");
  for (let i = 1; i < records.length; i++) if (order(records[i - 1], records[i]) > 0) throw new Error("OBSERVATION_ORDER_INVALID");
  // Capture-time freshness (latest reported soil moisture), coverage and withheld counts must be what the records say.
  const states = Object.fromEntries(SOIL_STATIONS.map(id => {
    const dates = records.filter(r => r.station_id === id && r.variable === "SOIL_MOISTURE" && r.value !== null).map(r => r.observation_date).sort();
    return [id, !dates.length ? "EMPTY" : (end - day(dates[dates.length - 1])) / 86400000 > 3 ? "STALE" : "RECENT"];
  }));
  const values = new Set(Object.values(states));
  const counts = Object.fromEntries(SOIL_STATIONS.map(id => [id, Object.fromEntries(WITHHELD.map(reason => [reason, records.filter(r => r.station_id === id && r.withheld === reason).length]))]));
  if (!same(candidate.freshness_at_capture, states) || candidate.coverage !== (values.size === 1 && values.has("EMPTY") ? "EMPTY" : values.has("EMPTY") ? "PARTIAL" : "COMPLETE")
      || !same(candidate.withheld_counts, counts)) throw new Error("COVERAGE_OR_FRESHNESS_MISMATCH");
  if (await digest(capturedCanonical(capturedValidation, "receipt_digest")) !== validation.receipt_digest) throw new Error("VALIDATION_RECEIPT_INVALID");
  const expected = { profile: "kfm.uscrn-daily-validation/v1", candidate_id: candidate.candidate_id, outcome: "PASS", observations: records.length,
    withheld: records.filter(r => r.withheld).length, review_required: true, promotion_authorized: false, release_authorized: false, publication_authorized: false };
  if (!same(validation, { ...expected, receipt_digest: await digest(canonical(expected)) })) throw new Error("VALIDATION_RECEIPT_MISMATCH");
}

export async function parseSoilPackage(text: string): Promise<SoilPackage> {
  if (!text || new TextEncoder().encode(text).length > SOIL_PACKAGE_LIMIT) throw new Error("PACKAGE_LIMIT");
  const snapshot = object(parseWaterJson(text));
  if (!same(Object.keys(snapshot).sort(), ["artifacts", "manifest"])) throw new Error("SNAPSHOT_SHAPE_INVALID");
  const manifest = object(snapshot.manifest), artifacts = object(snapshot.artifacts), hashes = object(manifest.artifacts);
  if (!same(Object.keys(manifest).sort(), ["artifacts", "candidate_id", "created_at", "end", "package_id", "profile", "review_requirements", "rollback_target", "source_id", "start"]) || manifest.profile !== "kfm.soil-snapshot/v1" || manifest.source_id !== "noaa-uscrn") throw new Error("MANIFEST_PROFILE_INVALID");
  if (!same(manifest.review_requirements, ["source_admission", "rights", "sensitivity", "policy", "independent_review", "release"]) || manifest.rollback_target !== null && (typeof manifest.rollback_target !== "string" || !DIGEST.test(manifest.rollback_target))) throw new Error("MANIFEST_PROFILE_INVALID");
  if (await digest(canonical(without(manifest, "package_id"))) !== manifest.package_id) throw new Error("PACKAGE_DIGEST_MISMATCH");
  if (day(manifest.end) - day(manifest.start) !== 29 * 86400000) throw new Error("SNAPSHOT_INTERVAL_INVALID");
  time(manifest.created_at);
  if (!same(Object.keys(artifacts).sort(), [...NAMES].sort()) || !same(Object.keys(hashes).sort(), [...NAMES].sort())) throw new Error("ARTIFACT_CLOSURE_INVALID");
  const values: Record<string, Obj> = {};
  for (const name of NAMES) { const raw = artifacts[name]; if (typeof raw !== "string" || await digest(raw) !== hashes[name]) throw new Error("ARTIFACT_DIGEST_MISMATCH"); values[name] = object(parseWaterJson(raw)); if (values[name].candidate_id !== manifest.candidate_id) throw new Error("CANDIDATE_BINDING_MISMATCH"); }
  const candidate = values["candidate.json"] as SoilCandidate & Obj, evidence = values["evidence.json"] as { entries: SoilEntry[] }, validation = values["validation.json"];
  if (candidate.release_state !== "UNRELEASED" || values["catalog.json"].authoritative !== false || validation.outcome !== "PASS") throw new Error("CARRIER_CANNOT_SELF_APPROVE");
  if (candidate.start !== manifest.start || candidate.end !== manifest.end || candidate.retrieved_at !== manifest.created_at) throw new Error("CANDIDATE_IDENTITY_MISMATCH");
  await validateSoilCandidate(candidate, parseCapturedObject(artifacts["candidate.json"] as string), validation, parseCapturedObject(artifacts["validation.json"] as string));
  // One evidence bundle per station and depth (the resolver caps a bundle at 128 members).
  const expectedKeys = SOIL_STATIONS.flatMap(id => SOIL_DEPTHS_CM.map(depth => `${id}|${depth}`)).sort();
  if (!Array.isArray(evidence.entries) || evidence.entries.some(e => !Number.isInteger(e.series))
      || !same(evidence.entries.map(e => `${e.station_id}|${e.series}`).sort(), expectedKeys)) throw new Error("SERIES_EVIDENCE_MISMATCH");
  const hex = String(manifest.candidate_id).split(":")[1];
  for (const entry of evidence.entries) {
    const station = candidate.stations.find(s => s.id === entry.station_id)!;
    const records = candidate.observations.filter(r => r.station_id === station.id && r.depth_cm === entry.series), bundle = entry.bundle;
    const expectedRef = { ref: `kfm://soil/station/${station.id}/depth-${entry.series}cm/${hex}`, kind: "dataset", bundle_ref: bundle.bundle_id };
    if (!same(entry.evidence_ref, expectedRef) || !same(bundle.evidence_refs, [expectedRef, ...records.map(r => ({ ref: r.evidence_ref, kind: "measurement", bundle_ref: bundle.bundle_id }))]) || bundle.evidence_refs.length > 128) throw new Error("MEASUREMENT_EVIDENCE_MISMATCH");
    if (!same(bundle.checksums, { candidate: candidate.candidate_id, validation: validation.receipt_digest }) || !same(bundle.source_records, [...new Set([station.page_digest, ...records.map(r => r.page_digest)])].sort()) || entry.verification_history.subject_ref !== expectedRef.ref) throw new Error("BUNDLE_CONTENT_BINDING_MISMATCH");
  }
  return { manifest: manifest as SoilPackage["manifest"], candidate, evidence, validation };
}

export function soilGate(pkg: SoilPackage, decision: Obj | null, now: string): string {
  return releaseGate(pkg, decision, now, SOIL_DECISION_PROFILE, SOIL_SELF_RELEASE_LICENSES);
}

export async function soilNegative(reason: string, now: string, outcome = "ABSTAIN"): Promise<SoilResponse> {
  const envelope = { id: "soil:" + reason.toLowerCase(), version: "kfm-soil-v1", issued_at: now, outcome, reason_code: reason, evidence_refs: [], policy_state: "withheld", freshness: "unknown", correction_state: "unknown" };
  return { envelope: { ...envelope, spec_hash: await digest(canonical(envelope)) } };
}

export async function projectSoil(pkg: SoilPackage, decision: Obj | null, view: string, now: string, stationId: string | null = null): Promise<SoilResponse> {
  const reason = soilGate(pkg, decision, now); if (reason !== "ELIGIBLE") return soilNegative(reason, now);
  if (!["bootstrap", "layers", "evidence"].includes(view)) return soilNegative("ROUTE_NOT_FOUND", now);
  const selected = pkg.evidence.entries.filter(e => !stationId || e.station_id === stationId); if (!selected.length) return soilNegative("EVIDENCE_NOT_FOUND", now);
  for (const entry of selected) if (!await verified(entry, now)) return soilNegative("EVIDENCE_UNRESOLVED", now);
  const refs = selected.map(e => e.evidence_ref), ids = new Set(selected.map(e => e.station_id)), candidate = pkg.candidate;
  const observations = candidate.observations.filter(r => ids.has(r.station_id));
  // As at capture, a station is current only through a reported soil moisture value, compared with the
  // current day in the station's local standard time, not the UTC date.
  const latest = new Map<string, number>();
  for (const r of observations) if (r.variable === "SOIL_MOISTURE" && r.value !== null) latest.set(r.station_id, Math.max(latest.get(r.station_id) ?? -Infinity, day(r.observation_date)));
  const instant = time(now);
  const ages = [...latest].map(([id, last]) => (Math.floor((instant + SOIL_STANDARD_OFFSET_HOURS[id] * 3600000) / 86400000) * 86400000 - last) / 86400000);
  const freshness = !ages.length ? "unknown" : Math.min(...ages) <= candidate.stale_after_days ? "current" : "stale-accepted";
  const precision = { spatial: { representation: "point", resolution: "USCRN station coordinates, EPSG:4326", accuracy: "NCEI daily01 row coordinates; a station point, not a field, county or region", generalization_applied: false },
    temporal: { granularity: "Station local-standard-time days, not UTC instants", observation_interval: { start: pkg.manifest.start, end: pkg.manifest.end }, freshness_class: freshness },
    attribute: { measures: { SOIL_MOISTURE: "m3/m3", SOIL_TEMP: "degC" }, depths_cm: [...SOIL_DEPTHS_CM], significant_precision: { SOIL_MOISTURE: 3, SOIL_TEMP: 1 },
      classification_granularity: "Daily values as reported; missing and out-of-range values withheld, never zero" },
    evidence_refs: refs, transform_receipt_refs: ["kfm://receipt/validation/" + String(pkg.validation.receipt_digest).split(":")[1]] };
  const envelope = { id: "soil:" + view, version: "kfm-soil-v1", issued_at: now, outcome: "ANSWER", reason_code: "RELEASED_SNAPSHOT", evidence_refs: refs, policy_state: "approved_snapshot", freshness, correction_state: "ACTIVE", precision_actually_used: precision };
  const common = { package_id: pkg.manifest.package_id, source_id: "noaa-uscrn", coverage: candidate.coverage, retrieved_at: candidate.retrieved_at, reviewed_at: decision!.reviewed_at, released_at: decision!.released_at, approval_expires_at: decision!.expires_at, stale_after_days: candidate.stale_after_days, correction_state: "ACTIVE", attribution: ATTRIBUTION };
  const data = view === "bootstrap" ? { ...common, layers: [{ id: "uscrn-daily-soil-pilot", title: "Reviewed NOAA USCRN daily soil moisture and temperature", evidence_eligible: true }], observation_count: observations.length }
    : view === "layers" ? { ...common, stations: candidate.stations.filter(s => ids.has(s.id)), observations, freshness_at_capture: Object.fromEntries(Object.entries(candidate.freshness_at_capture).filter(([k]) => ids.has(k))) }
    : { ...common, entries: selected.map(({ station_id, series, evidence_ref, bundle, verification_history }) => ({ station_id, series, evidence_ref, bundle, verification_history })) };
  return { envelope: { ...envelope, spec_hash: await digest(canonical(envelope)) }, data };
}
