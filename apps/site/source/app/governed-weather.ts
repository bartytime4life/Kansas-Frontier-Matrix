/** Reviewed GHCN-Daily weather snapshot carrier (ADR-0045). Never acquires or approves source data.
 *  Mirrors packages/release/src/release/core.py (WEATHER profile) and weather_projection.py. */
import { canonical, digest, object, parseWaterJson, releaseGate, same, time, verified, without, type Entry } from "./governed-water";

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

/** Digest of a canonical JSON object's text with one top-level member removed. Artifact text is the
 *  Python canonical serialization (sorted keys, no whitespace; its digest is checked first), so this
 *  reproduces digest_bytes(canonical_bytes({k: v ... if k != key})) without re-serializing numbers,
 *  which JavaScript would print differently (25.0 becomes 25). Non-canonical text fails closed. */
export async function digestWithout(text: string, key: string): Promise<string> {
  if (text.length < 2 || text[0] !== "{" || text[text.length - 1] !== "}") throw new Error("CANONICAL_OBJECT_REQUIRED");
  const members: [number, number][] = [];
  let depth = 0, inString = false, escaped = false, start = 1;
  for (let i = 1; i < text.length - 1; i++) {
    const c = text[i];
    if (inString) { if (escaped) escaped = false; else if (c === "\\") escaped = true; else if (c === '"') inString = false; continue; }
    if (c === '"') inString = true;
    else if (c === "{" || c === "[") depth++;
    else if (c === "}" || c === "]") depth--;
    else if (c === "," && depth === 0) { members.push([start, i]); start = i + 1; }
  }
  members.push([start, text.length - 1]);
  const name = JSON.stringify(key) + ":", kept = members.filter(([from]) => !text.startsWith(name, from));
  if (depth !== 0 || inString || kept.length !== members.length - 1) throw new Error("CANONICAL_MEMBER_INVALID");
  return digest("{" + kept.map(([from, to]) => text.slice(from, to)).join(",") + "}");
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
  // Inner provenance, as release/core.py validate_snapshot: the candidate id and validation receipt
  // digest must describe the artifacts they label, not only match each other.
  if (await digestWithout(artifacts["candidate.json"] as string, "candidate_id") !== manifest.candidate_id) throw new Error("CANDIDATE_IDENTITY_MISMATCH");
  if (await digestWithout(artifacts["validation.json"] as string, "receipt_digest") !== validation.receipt_digest) throw new Error("VALIDATION_RECEIPT_INVALID");
  if (candidate.start !== manifest.start || candidate.end !== manifest.end || candidate.retrieved_at !== manifest.created_at || candidate.stale_after_days !== 3) throw new Error("CANDIDATE_IDENTITY_MISMATCH");
  if (!Array.isArray(candidate.stations) || !same(candidate.stations.map(s => s.id).sort(), [...WEATHER_STATIONS].sort()) || !Array.isArray(candidate.observations) || candidate.observations.length > 360 || !Array.isArray(evidence.entries) || evidence.entries.length !== WEATHER_STATIONS.length) throw new Error("STATION_SCOPE_INVALID");
  for (const s of candidate.stations) { if (typeof s.name !== "string" || s.name.length > 64 || s.geometry.type !== "Point" || s.geometry.coordinates.length !== 2 || !s.geometry.coordinates.every(Number.isFinite) || Math.abs(s.geometry.coordinates[0]) > 180 || Math.abs(s.geometry.coordinates[1]) > 90) throw new Error("STATION_GEOMETRY_INVALID"); }
  const start = day(candidate.start), end = day(candidate.end);
  for (const r of candidate.observations) {
    if (!WEATHER_STATIONS.includes(r.station_id) || UNITS[r.element] === undefined || r.unit !== UNITS[r.element]
        || r.value !== null && (!Number.isFinite(r.value) || Math.abs(r.value) > 1e4) || r.withheld !== null && r.value !== null
        || day(r.observation_date) < start || day(r.observation_date) > end) throw new Error("OBSERVATION_INVALID");
  }
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
