/** Reviewed GHCN-Daily weather snapshot carrier (ADR-0045). Never acquires or approves source data.
 *  Mirrors packages/release/src/release/core.py (WEATHER profile) and weather_projection.py. */
import { canonical, capturedCanonical, capturedObject, codepointOrder, digest, object, parseCapturedObject, parseWaterJson, releaseGate, same, time, verified, without, type CapturedObject, type Entry } from "./governed-water";

export const WEATHER_PACKAGE_LIMIT = 8 * 1024 * 1024;
const NAMES = ["candidate.json", "catalog.json", "evidence.json", "validation.json"] as const;
const DIGEST = /^sha256:[a-f0-9]{64}$/;
export const WEATHER_STATIONS: readonly string[] = ["USW00003928", "USW00013985", "USW00013996", "USW00023065"];
const UNITS: Record<string, string> = { PRCP: "mm", TMAX: "degC", TMIN: "degC" };
// GHCN-Daily first-order stations report local standard time days: Central (UTC-6), Goodland Mountain (UTC-7).
// Must match STANDARD_OFFSET_HOURS in packages/release/src/release/weather_projection.py.
export const STANDARD_OFFSET_HOURS: Readonly<Record<string, number>> = { USW00003928: -6, USW00013985: -6, USW00013996: -6, USW00023065: -7 };
type Obj = Record<string, unknown>;
export type WeatherStation = { id: string; name: string; geometry: { type: "Point"; coordinates: [number, number] }; elevation_m: number | null; page_digest: string; retrieved_at: string };
export type WeatherObservation = { id: string; station_id: string; element: string; observation_date: string; raw_value: number; value: number | null; unit: string;
  measurement_flag: string; quality_flag: string; source_flag: string; observation_time: string | null; trace: boolean; withheld: string | null;
  preliminary: boolean; source_role: string; page_digest: string; retrieved_at: string; evidence_ref: string; record_digest: string };
type WeatherCandidate = { candidate_id: string; start: string; end: string; retrieved_at: string; coverage: string; stale_after_days: number;
  stations: WeatherStation[]; observations: WeatherObservation[]; freshness_at_capture: Record<string, string>; release_state: string };
export type WeatherPackage = { manifest: Obj & { package_id: string; candidate_id: string; start: string; end: string; created_at: string; rollback_target: string | null };
  candidate: WeatherCandidate; evidence: { entries: Entry[] }; validation: Obj };
export type WeatherResponse = { envelope: Obj & { outcome: string; reason_code: string }; data?: Obj & { stations?: WeatherStation[]; observations?: WeatherObservation[]; entries?: Entry[] } };
// ADR-0045: the admitted GHCN-Daily license. Must match WEATHER_SELF_RELEASE_LICENSES in packages/policy-runtime/src/policy_runtime/core.py.
export const WEATHER_SELF_RELEASE_LICENSES: readonly string[] = ["U.S. Public Domain (NOAA federal station data, 17 U.S.C. 105); preliminary data subject to revision"];
export const WEATHER_DECISION_PROFILE = "kfm.weather-release-decision/v1";
const ATTRIBUTION = "Menne et al. (2012), Global Historical Climatology Network - Daily (GHCN-Daily), Version 3, NOAA NCEI, doi:10.7289/V5D21VHZ. Values are preliminary and may be revised.";

/** Strict YYYY-MM-DD, as UTC midnight milliseconds; impossible dates are rejected, not normalized. */
export function day(value: unknown): number {
  const match = typeof value === "string" && /^(\d{4})-(\d{2})-(\d{2})$/.exec(value);
  if (!match || Number(match[1]) === 0) throw new Error("DATE_INVALID");
  const instant = Date.UTC(Number(match[1]), Number(match[2]) - 1, Number(match[3]));
  const parsed = new Date(instant);
  if (parsed.getUTCFullYear() !== Number(match[1]) || parsed.getUTCMonth() + 1 !== Number(match[2]) || parsed.getUTCDate() !== Number(match[3])) throw new Error("DATE_INVALID");
  return instant;
}

type WeatherRecord = WeatherObservation & Obj;

/** (value, trace, withheld) for one raw tenths value, as ghcnd_daily_normalize._reading. */
function reading(raw: number, mflag: string, qflag: string): [number | null, boolean, string | null] {
  if (raw === -9999) return [null, false, "MISSING"];
  if (qflag) return [null, false, "QUALITY_FLAG"];
  if (mflag === "T") return [0, true, null];
  if (mflag === "P") return [null, false, "MISSING"];
  return [raw / 10, false, null];
}

const OBSERVATION_KEYS = ["element", "evidence_ref", "id", "measurement_flag", "observation_date", "observation_time", "page_digest", "preliminary", "profile",
  "quality_flag", "raw_value", "record_digest", "retrieved_at", "source_flag", "source_role", "station_id", "trace", "unit", "value", "withheld"];
const STATION_KEYS = ["elevation_m", "geometry", "id", "name", "page_digest", "retrieved_at"];
const FLAG = /^[A-Z0-9]?$/, HASH = /^[a-f0-9]{64}$/;
const isTime = (value: unknown) => { try { time(value); return true; } catch { return false; } };

/** Closed schemas/contracts/v1/domains/atmosphere/daily_weather_observation.schema.json, applied first as the Python validator does. */
function observationShapeValid(r: WeatherRecord): boolean {
  return same(Object.keys(r).sort(), OBSERVATION_KEYS) && r.profile === "kfm.daily-weather-observation/v1"
    && typeof r.id === "string" && r.id.startsWith("kfm:weather:") && HASH.test(r.id.slice(12))
    && WEATHER_STATIONS.includes(r.station_id) && UNITS[r.element] !== undefined
    && typeof r.observation_date === "string" && /^[0-9]{4}-[0-9]{2}-[0-9]{2}$/.test(r.observation_date)
    && Number.isInteger(r.raw_value) && r.raw_value >= -9999 && r.raw_value <= 999999
    && (r.value === null || typeof r.value === "number") && (r.unit === "mm" || r.unit === "degC")
    && [r.measurement_flag, r.quality_flag, r.source_flag].every(flag => typeof flag === "string" && FLAG.test(flag))
    && (r.observation_time === null || typeof r.observation_time === "string" && /^[0-9]{4}$/.test(r.observation_time))
    && typeof r.trace === "boolean" && [null, "MISSING", "QUALITY_FLAG"].includes(r.withheld)
    && r.preliminary === true && r.source_role === "observed_station"
    && typeof r.page_digest === "string" && DIGEST.test(r.page_digest) && isTime(r.retrieved_at)
    && typeof r.evidence_ref === "string" && r.evidence_ref.startsWith("kfm:evidence:weather:") && HASH.test(r.evidence_ref.slice(21))
    && typeof r.record_digest === "string" && DIGEST.test(r.record_digest);
}

/** Inner provenance and record rules, as release/core.py and ghcnd_daily_validate.validate_candidate.
 *  Digests are recomputed over the captured Python serialization (strict canonical text, numbers kept
 *  as written), so 16.0 is hashed as 16.0, not as JavaScript's 16. */
async function validateWeatherIdentities(candidate: WeatherCandidate, captured: CapturedObject, validation: Obj, capturedValidation: CapturedObject) {
  if (await digest(capturedCanonical(captured, "candidate_id")) !== candidate.candidate_id) throw new Error("CANDIDATE_IDENTITY_MISMATCH");
  const records = candidate.observations as WeatherRecord[], capturedRecords = captured.observations;
  if (!Array.isArray(capturedRecords) || capturedRecords.length !== records.length) throw new Error("OBSERVATION_COUNT_INVALID");
  const seen = new Set<string>();
  for (let i = 0; i < records.length; i++) {
    const record = records[i];
    if (!observationShapeValid(record)) throw new Error("WEATHER_OBSERVATION_SCHEMA_INVALID");
    if (await digest(capturedCanonical(capturedObject(capturedRecords[i]), "record_digest")) !== record.record_digest) throw new Error("OBSERVATION_DIGEST_MISMATCH");
    const identity = (await digest(canonical([record.station_id, record.element, record.observation_date]))).slice(7);
    if (record.id !== "kfm:weather:" + identity || record.evidence_ref !== "kfm:evidence:weather:" + identity) throw new Error("OBSERVATION_IDENTITY_MISMATCH");
    if (!Number.isInteger(record.raw_value) || typeof record.measurement_flag !== "string" || typeof record.quality_flag !== "string"
        || !same([record.value, record.trace, record.withheld], reading(record.raw_value, record.measurement_flag, record.quality_flag))) throw new Error("OBSERVATION_VALUE_MISMATCH");
    if (time(record.retrieved_at) > time(candidate.retrieved_at)) throw new Error("OBSERVATION_DATE_INVALID");
    const key = canonical([record.station_id, record.element, record.observation_date]);
    if (seen.has(key)) throw new Error("DUPLICATE_STATION_DAY_ELEMENT");
    seen.add(key);
    // Station ids, dates and elements are fixed-width ASCII, so this orders as Python's tuple sort.
    const previous = records[i - 1];
    if (previous && codepointOrder(canonical([previous.station_id, previous.observation_date, previous.element]), canonical([record.station_id, record.observation_date, record.element])) >= 0) throw new Error("OBSERVATION_ORDER_INVALID");
  }
  // Capture-time freshness, coverage and withheld counts must be what the records say.
  const states = Object.fromEntries(WEATHER_STATIONS.map(id => {
    const dates = records.filter(r => r.station_id === id && r.value !== null).map(r => r.observation_date).sort();
    return [id, !dates.length ? "EMPTY" : (day(candidate.end) - day(dates[dates.length - 1])) / 86400000 > 3 ? "STALE" : "RECENT"];
  }));
  const values = new Set(Object.values(states));
  const counts = Object.fromEntries(WEATHER_STATIONS.map(id => [id, Object.fromEntries(["MISSING", "QUALITY_FLAG"].map(reason => [reason, records.filter(r => r.station_id === id && r.withheld === reason).length]))]));
  if (!same(candidate.freshness_at_capture, states) || (candidate as unknown as Obj).coverage !== (values.size === 1 && values.has("EMPTY") ? "EMPTY" : values.has("EMPTY") ? "PARTIAL" : "COMPLETE")
      || !same((candidate as unknown as Obj).withheld_counts, counts)) throw new Error("COVERAGE_OR_FRESHNESS_MISMATCH");
  if (await digest(capturedCanonical(capturedValidation, "receipt_digest")) !== validation.receipt_digest) throw new Error("VALIDATION_RECEIPT_INVALID");
  const expected = { profile: "kfm.ghcnd-daily-validation/v1", candidate_id: candidate.candidate_id, outcome: "PASS", observations: records.length,
    withheld: records.filter(r => r.withheld).length, review_required: true, promotion_authorized: false, release_authorized: false, publication_authorized: false };
  if (!same(validation, { ...expected, receipt_digest: await digest(canonical(expected)) })) throw new Error("VALIDATION_RECEIPT_MISMATCH");
}

export async function parseWeatherPackage(text: string): Promise<WeatherPackage> {
  if (!text || new TextEncoder().encode(text).length > WEATHER_PACKAGE_LIMIT) throw new Error("PACKAGE_LIMIT");
  const snapshot = object(parseWaterJson(text));
  if (!same(Object.keys(snapshot).sort(), ["artifacts", "manifest"])) throw new Error("SNAPSHOT_SHAPE_INVALID");
  const manifest = object(snapshot.manifest), artifacts = object(snapshot.artifacts), hashes = object(manifest.artifacts);
  if (!same(Object.keys(manifest).sort(), ["artifacts", "candidate_id", "created_at", "end", "package_id", "profile", "review_requirements", "rollback_target", "source_id", "start"]) || manifest.profile !== "kfm.weather-snapshot/v1" || manifest.source_id !== "noaa-ghcnd") throw new Error("MANIFEST_PROFILE_INVALID");
  if (!same(manifest.review_requirements, ["source_admission", "rights", "sensitivity", "policy", "independent_review", "release"]) || manifest.rollback_target !== null && (typeof manifest.rollback_target !== "string" || !DIGEST.test(manifest.rollback_target))) throw new Error("MANIFEST_PROFILE_INVALID");
  if (await digest(canonical(without(manifest, "package_id"))) !== manifest.package_id) throw new Error("PACKAGE_DIGEST_MISMATCH");
  if (day(manifest.end) - day(manifest.start) !== 29 * 86400000) throw new Error("SNAPSHOT_INTERVAL_INVALID");
  time(manifest.created_at);
  if (!same(Object.keys(artifacts).sort(), [...NAMES].sort()) || !same(Object.keys(hashes).sort(), [...NAMES].sort())) throw new Error("ARTIFACT_CLOSURE_INVALID");
  const values: Record<string, Obj> = {};
  for (const name of NAMES) { const raw = artifacts[name]; if (typeof raw !== "string" || await digest(raw) !== hashes[name]) throw new Error("ARTIFACT_DIGEST_MISMATCH"); values[name] = object(parseWaterJson(raw)); if (values[name].candidate_id !== manifest.candidate_id) throw new Error("CANDIDATE_BINDING_MISMATCH"); }
  const candidate = values["candidate.json"] as WeatherCandidate, evidence = values["evidence.json"] as { entries: Entry[] }, validation = values["validation.json"];
  if (candidate.release_state !== "UNRELEASED" || values["catalog.json"].authoritative !== false || validation.outcome !== "PASS") throw new Error("CARRIER_CANNOT_SELF_APPROVE");
  if (candidate.start !== manifest.start || candidate.end !== manifest.end || candidate.retrieved_at !== manifest.created_at || candidate.stale_after_days !== 3) throw new Error("CANDIDATE_IDENTITY_MISMATCH");
  if (!Array.isArray(candidate.stations) || !same(candidate.stations.map(s => s.id).sort(), [...WEATHER_STATIONS].sort()) || !Array.isArray(candidate.observations) || candidate.observations.length > 360 || !Array.isArray(evidence.entries) || evidence.entries.length !== WEATHER_STATIONS.length) throw new Error("STATION_SCOPE_INVALID");
  for (const s of candidate.stations) { if (!same(Object.keys(s).sort(), STATION_KEYS) || !same(Object.keys(object(s.geometry)).sort(), ["coordinates", "type"]) || typeof s.page_digest !== "string" || !DIGEST.test(s.page_digest)
    || !isTime(s.retrieved_at) || time(s.retrieved_at) > time(candidate.retrieved_at) || !Array.isArray(s.geometry.coordinates)
    || s.geometry.coordinates[0] < -102.2 || s.geometry.coordinates[0] > -94.4 || s.geometry.coordinates[1] < 36.9 || s.geometry.coordinates[1] > 40.1
    || typeof s.name !== "string" || !s.name.length || s.name.length > 64 || s.geometry.type !== "Point" || s.geometry.coordinates.length !== 2 || !s.geometry.coordinates.every(Number.isFinite) || Math.abs(s.geometry.coordinates[0]) > 180 || Math.abs(s.geometry.coordinates[1]) > 90) throw new Error("STATION_GEOMETRY_INVALID"); }
  const start = day(candidate.start), end = day(candidate.end);
  for (const r of candidate.observations) {
    if (!WEATHER_STATIONS.includes(r.station_id) || UNITS[r.element] === undefined || r.unit !== UNITS[r.element]
        || r.value !== null && (!Number.isFinite(r.value) || Math.abs(r.value) > 1e4) || r.withheld !== null && r.value !== null
        || day(r.observation_date) < start || day(r.observation_date) > end) throw new Error("OBSERVATION_INVALID");
  }
  await validateWeatherIdentities(candidate, parseCapturedObject(artifacts["candidate.json"] as string), validation, parseCapturedObject(artifacts["validation.json"] as string));
  if (!same(evidence.entries.map(e => e.station_id).sort(), candidate.stations.map(s => s.id).sort())) throw new Error("STATION_EVIDENCE_MISMATCH");
  for (const entry of evidence.entries) {
    const station = candidate.stations.find(s => s.id === entry.station_id)!;
    const records = candidate.observations.filter(r => r.station_id === station.id), bundle = entry.bundle;
    const expectedRef = { ref: `kfm://weather/station/${station.id}/${String(manifest.candidate_id).split(":")[1]}`, kind: "dataset", bundle_ref: bundle.bundle_id };
    if (!same(entry.evidence_ref, expectedRef) || !same(bundle.evidence_refs, [expectedRef, ...records.map(r => ({ ref: r.evidence_ref, kind: "measurement", bundle_ref: bundle.bundle_id }))]) || bundle.evidence_refs.length > 128) throw new Error("MEASUREMENT_EVIDENCE_MISMATCH");
    if (!same(bundle.checksums, { candidate: candidate.candidate_id, validation: validation.receipt_digest }) || !same(bundle.source_records, [...new Set([station.page_digest, ...records.map(r => r.page_digest)])].sort()) || entry.verification_history.subject_ref !== expectedRef.ref) throw new Error("BUNDLE_CONTENT_BINDING_MISMATCH");
  }
  return { manifest: manifest as WeatherPackage["manifest"], candidate, evidence, validation };
}

export function weatherGate(pkg: WeatherPackage, decision: Obj | null, now: string): string {
  return releaseGate(pkg, decision, now, WEATHER_DECISION_PROFILE, WEATHER_SELF_RELEASE_LICENSES);
}

export async function weatherNegative(reason: string, now: string, outcome = "ABSTAIN"): Promise<WeatherResponse> {
  const envelope = { id: "weather:" + reason.toLowerCase(), version: "kfm-weather-v1", issued_at: now, outcome, reason_code: reason, evidence_refs: [], policy_state: "withheld", freshness: "unknown", correction_state: "unknown" };
  return { envelope: { ...envelope, spec_hash: await digest(canonical(envelope)) } };
}

export async function projectWeather(pkg: WeatherPackage, decision: Obj | null, view: string, now: string, stationId: string | null = null): Promise<WeatherResponse> {
  const reason = weatherGate(pkg, decision, now); if (reason !== "ELIGIBLE") return weatherNegative(reason, now);
  if (!["bootstrap", "layers", "evidence"].includes(view)) return weatherNegative("ROUTE_NOT_FOUND", now);
  const selected = pkg.evidence.entries.filter(e => !stationId || e.station_id === stationId); if (!selected.length) return weatherNegative("EVIDENCE_NOT_FOUND", now);
  for (const entry of selected) if (!await verified(entry, now)) return weatherNegative("EVIDENCE_UNRESOLVED", now);
  const refs = selected.map(e => e.evidence_ref), ids = new Set(selected.map(e => e.station_id)), candidate = pkg.candidate;
  const observations = candidate.observations.filter(r => ids.has(r.station_id));
  // A withheld value cannot make a day current. Each station's latest day is compared with the
  // current day in that station's local standard time, not the UTC date.
  const latest = new Map<string, number>();
  for (const r of observations) if (r.value !== null) latest.set(r.station_id, Math.max(latest.get(r.station_id) ?? -Infinity, day(r.observation_date)));
  const instant = time(now);
  const ages = [...latest].map(([id, last]) => (Math.floor((instant + STANDARD_OFFSET_HOURS[id] * 3600000) / 86400000) * 86400000 - last) / 86400000);
  const freshness = !ages.length ? "unknown" : Math.min(...ages) <= candidate.stale_after_days ? "current" : "stale-accepted";
  const precision = { spatial: { representation: "point", resolution: "Provider station coordinates, EPSG:4326", accuracy: "GHCN-Daily station list coordinates; no inferred positional accuracy", generalization_applied: false },
    temporal: { granularity: "Station-local observation days, not UTC instants", observation_interval: { start: pkg.manifest.start, end: pkg.manifest.end }, freshness_class: freshness },
    attribute: { measures: { PRCP: "mm", TMAX: "degC", TMIN: "degC" }, significant_precision: 1, classification_granularity: "Tenths as reported; missing and quality-flagged values withheld, never zero" },
    evidence_refs: refs, transform_receipt_refs: ["kfm://receipt/validation/" + String(pkg.validation.receipt_digest).split(":")[1]] };
  const envelope = { id: "weather:" + view, version: "kfm-weather-v1", issued_at: now, outcome: "ANSWER", reason_code: "RELEASED_SNAPSHOT", evidence_refs: refs, policy_state: "approved_snapshot", freshness, correction_state: "ACTIVE", precision_actually_used: precision };
  const common = { package_id: pkg.manifest.package_id, source_id: "noaa-ghcnd", coverage: candidate.coverage, retrieved_at: candidate.retrieved_at, reviewed_at: decision!.reviewed_at, released_at: decision!.released_at, approval_expires_at: decision!.expires_at, stale_after_days: candidate.stale_after_days, correction_state: "ACTIVE", attribution: ATTRIBUTION };
  const data = view === "bootstrap" ? { ...common, layers: [{ id: "ghcnd-daily-pilot", title: "Reviewed NOAA GHCN-Daily station weather", evidence_eligible: true }], observation_count: observations.length }
    : view === "layers" ? { ...common, stations: candidate.stations.filter(s => ids.has(s.id)), observations, freshness_at_capture: Object.fromEntries(Object.entries(candidate.freshness_at_capture).filter(([k]) => ids.has(k))) }
    : { ...common, entries: selected.map(({ station_id, evidence_ref, bundle, verification_history }) => ({ station_id, evidence_ref, bundle, verification_history })) };
  return { envelope: { ...envelope, spec_hash: await digest(canonical(envelope)) }, data };
}
