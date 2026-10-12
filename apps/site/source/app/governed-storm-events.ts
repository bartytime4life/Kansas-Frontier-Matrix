/** Reviewed NOAA Storm Events snapshot carrier (ADR-0047). Never acquires or approves source data.
 *  Mirrors packages/release/src/release/core.py (STORM_EVENTS profile: one data year, one evidence bundle per
 *  month part), pipelines/domains/hazards/storm_events_validate.py, storm_events_package.storm_catalog and
 *  release/storm_events_projection.py. Records are historical NWS event reports, never warnings. */
import { canonical, capturedCanonical, capturedObject, codepointOrder, digest, object, parseCapturedObject, parseWaterJson, releaseGate, same, time, verified, without, type CapturedObject, type Entry } from "./governed-water";
import { day } from "./governed-weather";

export const STORM_EVENTS_PACKAGE_LIMIT = 8 * 1024 * 1024;
const NAMES = ["candidate.json", "catalog.json", "evidence.json", "validation.json"] as const;
const DIGEST = /^sha256:[a-f0-9]{64}$/, HASH = /^[a-f0-9]{64}$/;
const FILE_NAME = /^StormEvents_details-ftp_v1\.0_d(\d{4})_c(\d{8})\.csv\.gz$/;
const SOURCE_ID = "noaa-storm-events";
// Must match release.core.MONTH_PART_SIZE and STORM_EVENTS.max_observations.
export const STORM_MONTH_PART_SIZE = 127;
const MAX_OBSERVATIONS = 5000;
const STALE_AFTER_DAYS = 45;
const WITHHELD = ["CASUALTY_UNPARSEABLE", "DAMAGE_UNPARSEABLE", "END_BEFORE_BEGIN"] as const;
export const STORM_FLAGS = ["EPISODE_ID_ABSENT", "EVENT_TYPE_OUTSIDE_DIRECTIVE", "UTC_OFFSET_UNKNOWN", "ZONE_OR_COUNTY_SUPPORT_ONLY"] as const;
// Must match connectors/noaa/src/noaa/storm_events.py DIRECTIVE_EVENT_TYPES (NWS Directive 10-1605).
const DIRECTIVE_EVENT_TYPES = new Set(["Astronomical Low Tide", "Avalanche", "Blizzard", "Coastal Flood", "Cold/Wind Chill",
  "Debris Flow", "Dense Fog", "Dense Smoke", "Drought", "Dust Devil", "Dust Storm", "Excessive Heat", "Extreme Cold/Wind Chill",
  "Flash Flood", "Flood", "Freezing Fog", "Frost/Freeze", "Funnel Cloud", "Hail", "Heat", "Heavy Rain", "Heavy Snow", "High Surf",
  "High Wind", "Hurricane (Typhoon)", "Ice Storm", "Lake-Effect Snow", "Lakeshore Flood", "Lightning", "Marine Dense Fog",
  "Marine Hail", "Marine High Wind", "Marine Strong Wind", "Marine Thunderstorm Wind", "Rip Current", "Seiche", "Sleet",
  "Sneakerwave", "Storm Surge/Tide", "Strong Wind", "Thunderstorm Wind", "Tornado", "Tropical Depression", "Tropical Storm",
  "Tsunami", "Volcanic Ash", "Waterspout", "Wildfire", "Winter Storm", "Winter Weather"]);
type Obj = Record<string, unknown>;
export type StormEvent = { id: string; event_id: number; episode_id: number | null; event_type: string; cz_type: string; cz_fips: number; cz_name: string; cz_timezone: string;
  begin_local: string; end_local: string; begin_utc: string | null; end_utc: string | null; injuries_direct: number; injuries_indirect: number; deaths_direct: number; deaths_indirect: number;
  damage_property_usd: number | null; damage_crops_usd: number | null; damage_property_source: string; damage_crops_source: string; magnitude_source: string; magnitude_type: string;
  tor_f_scale: string; begin_lat: number | null; begin_lon: number | null; end_lat: number | null; end_lon: number | null; has_narrative: boolean; flags: string[];
  source_row_digest: string; page_digest: string; retrieved_at: string; evidence_ref: string; record_digest: string };
type StormCandidate = { candidate_id: string; data_year: number; source_file: string; vintage_created: string; retrieved_at: string; observations: StormEvent[];
  latest_event_date: string | null; withheld_rows: number; withheld_counts: Record<string, number>; freshness_at_capture: string; stale_after_days: number;
  coverage: string; state_fips: number; source_id: string; release_state: string };
export type StormEntry = Omit<Entry, "station_id"> & { month: number; part: number };
export type StormCatalog = { dataset: Obj; entries: Obj[] };
export type StormPackage = { manifest: Obj & { package_id: string; candidate_id: string; start: string; end: string; created_at: string; rollback_target: string | null };
  candidate: StormCandidate; catalog: StormCatalog; evidence: { entries: StormEntry[] }; validation: Obj };
export type StormResponse = { envelope: Obj & { outcome: string; reason_code: string; freshness?: string }; data?: Obj & { observations?: StormEvent[]; entries?: StormEntry[]; months?: number[];
  dataset?: Obj; selection?: { months: number[]; observation_count: number; event_types: Record<string, number>; latest_event_date: string | null } } };
// ADR-0047: the admitted Storm Events license. Must match STORM_EVENTS_SELF_RELEASE_LICENSES in packages/policy-runtime/src/policy_runtime/core.py.
export const STORM_EVENTS_SELF_RELEASE_LICENSES: readonly string[] = ["U.S. Public Domain (NOAA federal records, 17 U.S.C. 105); Storm Events data subject to revision"];
export const STORM_EVENTS_DECISION_PROFILE = "kfm.storm-events-release-decision/v1";
const ATTRIBUTION = "NOAA National Centers for Environmental Information, Storm Events Database. Records are compiled from "
  + "National Weather Service reports and may be revised. Historical event reports, not warnings.";

/** Exact whole nominal USD for an NCEI damage string, as storm_events.parse_damage; null when blank. Throws otherwise. */
export function parseDamage(value: string): number | null {
  if (value === "") return null;
  const match = /^(\d+)(?:\.(\d+))?([KMB]?)$/.exec(value.trim().toUpperCase());
  if (!match) throw new Error("DAMAGE_FORMAT");
  const fraction = match[2] ?? "", zeros = { "": 0, K: 3, M: 6, B: 9 }[match[3] as "" | "K" | "M" | "B"];
  if (fraction.length > zeros && /[1-9]/.test(fraction.slice(zeros))) throw new Error("DAMAGE_FRACTIONAL_DOLLARS");
  const amount = BigInt(match[1] + fraction.slice(0, zeros).padEnd(zeros, "0"));
  if (amount > BigInt(Number.MAX_SAFE_INTEGER)) throw new Error("DAMAGE_RANGE");
  return Number(amount);
}

/** Strict local YYYY-MM-DDTHH:MM, as UTC-epoch milliseconds of the wall clock; impossible times are rejected. */
function localTime(value: unknown): number {
  const match = typeof value === "string" && /^(\d{4}-\d{2}-\d{2})T(\d{2}):(\d{2})$/.exec(value);
  if (!match || Number(match[2]) > 23 || Number(match[3]) > 59) throw new Error("RECORD_TIME_INVALID");
  let date: number;
  try { date = day(match[1]); } catch { throw new Error("RECORD_TIME_INVALID"); }
  return date + Number(match[2]) * 3600000 + Number(match[3]) * 60000;
}

/** UTC minutes for a local time when the NCEI zone token carries an hour offset, as storm_events_validate.expected_utc. */
function expectedUtc(local: string, zone: string): string | null {
  const match = /^[A-Z]{3}-(\d{1,2})$/.exec(zone);
  return match ? new Date(localTime(local) + Number(match[1]) * 3600000).toISOString().slice(0, 16) + "Z" : null;
}

function expectedFlags(r: StormEvent): string[] {
  const flags: string[] = [];
  if (r.episode_id === null) flags.push("EPISODE_ID_ABSENT");
  if (!DIRECTIVE_EVENT_TYPES.has(r.event_type)) flags.push("EVENT_TYPE_OUTSIDE_DIRECTIVE");
  if (r.begin_utc === null) flags.push("UTC_OFFSET_UNKNOWN");
  if (r.begin_lat === null) flags.push("ZONE_OR_COUNTY_SUPPORT_ONLY");
  return flags;
}

const freshness = (vintage: string, retrievedAt: string) => (day(retrievedAt.slice(0, 10)) - day(vintage)) / 86400000 > STALE_AFTER_DAYS ? "STALE" : "CURRENT";

const CANDIDATE_KEYS = ["candidate_id", "capture_id", "coverage", "data_year", "freshness_at_capture", "latest_event_date", "observations", "profile", "release_state",
  "retrieved_at", "review_state", "source_admission", "source_file", "source_id", "stale_after_days", "state_fips", "vintage_created", "withheld_counts", "withheld_rows"];
const RECORD_KEYS = ["begin_lat", "begin_local", "begin_lon", "begin_utc", "cz_fips", "cz_name", "cz_timezone", "cz_type", "damage_crops_source", "damage_crops_usd",
  "damage_property_source", "damage_property_usd", "deaths_direct", "deaths_indirect", "end_lat", "end_local", "end_lon", "end_utc", "episode_id", "event_id", "event_type",
  "evidence_ref", "flags", "has_narrative", "id", "injuries_direct", "injuries_indirect", "magnitude_source", "magnitude_type", "page_digest", "profile", "record_digest",
  "retrieved_at", "source_row_digest", "tor_f_scale"];
const LOCAL = /^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}$/, UTC = /^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}Z$/;
const isTime = (value: unknown) => { try { time(value); return true; } catch { return false; } };
const int = (v: unknown, low: number, high = Number.MAX_SAFE_INTEGER) => Number.isInteger(v) && (v as number) >= low && (v as number) <= high;
const str = (v: unknown, max: number, min = 0) => typeof v === "string" && v.length >= min && v.length <= max;
const coordinate = (v: unknown, limit: number) => v === null || typeof v === "number" && Number.isFinite(v) && Math.abs(v) <= limit;

/** Closed schemas/contracts/v1/domains/hazards/storm_event_record.schema.json, applied first as the Python validator does. */
function recordShapeValid(r: StormEvent & Obj): boolean {
  return same(Object.keys(r).sort(), RECORD_KEYS) && r.profile === "kfm.storm-event-record/v1"
    && typeof r.id === "string" && r.id.startsWith("kfm:storm:") && HASH.test(r.id.slice(10))
    && int(r.event_id, 1) && (r.episode_id === null || int(r.episode_id, 0)) && str(r.event_type, 64, 1)
    && ["C", "Z", "M"].includes(r.cz_type) && int(r.cz_fips, 0, 999) && str(r.cz_name, 128) && str(r.cz_timezone, 16)
    && typeof r.begin_local === "string" && LOCAL.test(r.begin_local) && typeof r.end_local === "string" && LOCAL.test(r.end_local)
    && (r.begin_utc === null || typeof r.begin_utc === "string" && UTC.test(r.begin_utc)) && (r.end_utc === null || typeof r.end_utc === "string" && UTC.test(r.end_utc))
    && ["injuries_direct", "injuries_indirect", "deaths_direct", "deaths_indirect"].every(k => int(r[k], 0, 999999))
    && (r.damage_property_usd === null || int(r.damage_property_usd, 0)) && (r.damage_crops_usd === null || int(r.damage_crops_usd, 0))
    && str(r.damage_property_source, 16) && str(r.damage_crops_source, 16) && str(r.magnitude_source, 16) && str(r.magnitude_type, 8) && str(r.tor_f_scale, 8)
    && coordinate(r.begin_lat, 90) && coordinate(r.begin_lon, 180) && coordinate(r.end_lat, 90) && coordinate(r.end_lon, 180)
    && typeof r.has_narrative === "boolean" && Array.isArray(r.flags) && r.flags.length <= 4 && new Set(r.flags).size === r.flags.length
    && r.flags.every(f => (STORM_FLAGS as readonly string[]).includes(f))
    && typeof r.source_row_digest === "string" && DIGEST.test(r.source_row_digest) && typeof r.page_digest === "string" && DIGEST.test(r.page_digest)
    && isTime(r.retrieved_at) && typeof r.evidence_ref === "string" && r.evidence_ref.startsWith("kfm:evidence:storm:") && HASH.test(r.evidence_ref.slice(19))
    && typeof r.record_digest === "string" && DIGEST.test(r.record_digest);
}

/** (month, part, records) for every month that has records, as SnapshotProfile.month_groups. */
export function stormMonthGroups(observations: StormEvent[]): [number, number, StormEvent[]][] {
  const groups: [number, number, StormEvent[]][] = [];
  for (let month = 1; month <= 12; month++) {
    const records = observations.filter(r => r.begin_local.slice(5, 7) === String(month).padStart(2, "0"));
    for (let first = 0; first < records.length; first += STORM_MONTH_PART_SIZE) groups.push([month, first / STORM_MONTH_PART_SIZE + 1, records.slice(first, first + STORM_MONTH_PART_SIZE)]);
  }
  return groups;
}

const monthRef = (start: string, month: number, part: number, candidateId: string) => `kfm://hazards/storm-events/${start.slice(0, 4)}-${String(month).padStart(2, "0")}/part-${part}/${candidateId.split(":")[1]}`;
const eventTypes = (records: StormEvent[]) => Object.fromEntries([...records.reduce((m, r) => m.set(r.event_type, (m.get(r.event_type) ?? 0) + 1), new Map<string, number>())].sort(([a], [b]) => codepointOrder(a, b)));
const latestDate = (records: StormEvent[]) => records.length ? records.map(r => r.begin_local.slice(0, 10)).sort(codepointOrder).at(-1)! : null;

/** Inner provenance and record rules, as storm_events_validate.validate_candidate. Digests are recomputed
 *  over the captured Python serialization (numbers kept as written). */
async function validateStormCandidate(candidate: StormCandidate & Obj, captured: CapturedObject, validation: Obj, capturedValidation: CapturedObject) {
  if (!same(Object.keys(candidate).sort(), CANDIDATE_KEYS)) throw new Error("CANDIDATE_SHAPE_INVALID");
  if (candidate.profile !== "kfm.storm-events-candidate/v1" || candidate.source_id !== SOURCE_ID || candidate.state_fips !== 20
      || typeof candidate.capture_id !== "string" || !DIGEST.test(candidate.capture_id) || candidate.source_admission !== "PENDING" || candidate.review_state !== "PENDING"
      || candidate.release_state !== "UNRELEASED" || candidate.coverage !== "NOT_ESTABLISHED" || candidate.stale_after_days !== STALE_AFTER_DAYS) throw new Error("CANDIDATE_AUTHORITY_OR_PROFILE_INVALID");
  if (await digest(capturedCanonical(captured, "candidate_id")) !== candidate.candidate_id) throw new Error("CANDIDATE_DIGEST_MISMATCH");
  // The source file names the data year and its creation vintage; both must agree with the candidate.
  const year = candidate.data_year, file = typeof candidate.source_file === "string" ? FILE_NAME.exec(candidate.source_file) : null;
  let created = "";
  try { if (file) { created = `${file[2].slice(0, 4)}-${file[2].slice(4, 6)}-${file[2].slice(6)}`; day(created); } } catch { created = ""; }
  if (!int(year, 1996, 2200) || !file || !created || Number(file[1]) !== year || Number(created.slice(0, 4)) < year
      || candidate.vintage_created !== created || typeof candidate.retrieved_at !== "string" || codepointOrder(candidate.retrieved_at.slice(0, 10), created) < 0) throw new Error("CANDIDATE_SOURCE_FILE_INVALID");
  const counts = candidate.withheld_counts, rows = candidate.withheld_rows;
  if (!counts || typeof counts !== "object" || Array.isArray(counts) || !same(Object.keys(counts).sort(), [...WITHHELD].sort()) || !int(rows, 0)
      || Object.values(counts).some(n => !int(n, 0, rows)) || !(rows <= Object.values(counts).reduce((a, b) => a + b, 0) && Object.values(counts).reduce((a, b) => a + b, 0) <= rows * WITHHELD.length)) throw new Error("WITHHELD_COUNTS_INVALID");
  const records = candidate.observations as (StormEvent & Obj)[], capturedRecords = captured.observations;
  if (!Array.isArray(records) || records.length > MAX_OBSERVATIONS || !Array.isArray(capturedRecords) || capturedRecords.length !== records.length) throw new Error("OBSERVATION_COUNT_INVALID");
  let previous = 0;
  for (let i = 0; i < records.length; i++) {
    const r = records[i];
    if (!recordShapeValid(r)) throw new Error("STORM_EVENT_SCHEMA_INVALID");
    if (await digest(capturedCanonical(capturedObject(capturedRecords[i]), "record_digest")) !== r.record_digest) throw new Error("RECORD_DIGEST_MISMATCH");
    const key = (await digest(canonical([SOURCE_ID, r.event_id]))).slice(7);
    if (r.id !== "kfm:storm:" + key || r.evidence_ref !== "kfm:evidence:storm:" + key) throw new Error("RECORD_IDENTITY_MISMATCH");
    if (r.event_id <= previous) throw new Error("RECORD_ORDER_OR_DUPLICATE");
    previous = r.event_id;
    const begin = localTime(r.begin_local), end = localTime(r.end_local);
    if (new Date(begin).getUTCFullYear() !== year || end < begin || codepointOrder(r.retrieved_at, candidate.retrieved_at) > 0) throw new Error("RECORD_TIME_INVALID");
    let damages: (number | null)[];
    try { damages = [parseDamage(r.damage_property_source), parseDamage(r.damage_crops_source)]; } catch { throw new Error("RECORD_DAMAGE_MISMATCH"); }
    if (!same(damages, [r.damage_property_usd, r.damage_crops_usd])) throw new Error("RECORD_DAMAGE_MISMATCH");
    if (expectedUtc(r.begin_local, r.cz_timezone) !== r.begin_utc || expectedUtc(r.end_local, r.cz_timezone) !== r.end_utc) throw new Error("RECORD_UTC_MISMATCH");
    if ((r.begin_lat === null) !== (r.begin_lon === null) || (r.end_lat === null) !== (r.end_lon === null)) throw new Error("RECORD_COORDINATE_INVALID");
    if (!same(r.flags, expectedFlags(r))) throw new Error("RECORD_FLAGS_MISMATCH");
  }
  if (candidate.latest_event_date !== latestDate(records)) throw new Error("LATEST_EVENT_DATE_MISMATCH");
  if (candidate.freshness_at_capture !== freshness(candidate.vintage_created, candidate.retrieved_at)) throw new Error("FRESHNESS_MISMATCH");
  if (await digest(capturedCanonical(capturedValidation, "receipt_digest")) !== validation.receipt_digest) throw new Error("VALIDATION_RECEIPT_INVALID");
  const expected = { profile: "kfm.storm-events-validation/v1", candidate_id: candidate.candidate_id, outcome: "PASS", observations: records.length,
    withheld: rows, review_required: true, promotion_authorized: false, release_authorized: false, publication_authorized: false };
  if (!same(validation, { ...expected, receipt_digest: await digest(canonical(expected)) })) throw new Error("VALIDATION_RECEIPT_MISMATCH");
}

/** The catalog storm_events_package.storm_catalog builds from a validated candidate; served data never trusts it unchecked. */
function expectedCatalog(candidate: StormCandidate, validation: Obj, start: string) {
  const observations = candidate.observations;
  const dataset = { id: `noaa-storm-events:ks:${candidate.data_year}`, title: `NOAA Storm Events, Kansas, ${candidate.data_year}`,
    source_id: candidate.source_id, state_fips: candidate.state_fips, data_year: candidate.data_year, source_file: candidate.source_file,
    vintage_created: candidate.vintage_created, observation_count: observations.length, withheld_rows: candidate.withheld_rows,
    withheld_counts: candidate.withheld_counts, event_types: eventTypes(observations), latest_event_date: candidate.latest_event_date,
    freshness_at_capture: candidate.freshness_at_capture, coverage: candidate.coverage,
    interval: { start, end: start.slice(0, 4) + "-12-31", basis: "event begin, local time" }, narratives: "excluded", validation_ref: validation.receipt_digest };
  const entries = stormMonthGroups(observations).map(([month, part, records]) => ({ month, part, observation_count: records.length, evidence_ref: monthRef(start, month, part, candidate.candidate_id) }));
  return { profile: "kfm.storm-events-catalog-candidate/v1", candidate_id: candidate.candidate_id, dataset, entries, authoritative: false, release_state: "UNRELEASED" };
}

export async function parseStormEventsPackage(text: string): Promise<StormPackage> {
  if (!text || new TextEncoder().encode(text).length > STORM_EVENTS_PACKAGE_LIMIT) throw new Error("PACKAGE_LIMIT");
  const snapshot = object(parseWaterJson(text));
  if (!same(Object.keys(snapshot).sort(), ["artifacts", "manifest"])) throw new Error("SNAPSHOT_SHAPE_INVALID");
  const manifest = object(snapshot.manifest), artifacts = object(snapshot.artifacts), hashes = object(manifest.artifacts);
  if (!same(Object.keys(manifest).sort(), ["artifacts", "candidate_id", "created_at", "end", "package_id", "profile", "review_requirements", "rollback_target", "source_id", "start"])
      || manifest.profile !== "kfm.storm-events-snapshot/v1" || manifest.source_id !== SOURCE_ID) throw new Error("MANIFEST_PROFILE_INVALID");
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
  const candidate = values["candidate.json"] as StormCandidate & Obj, catalog = values["catalog.json"], evidence = values["evidence.json"] as { entries: StormEntry[] }, validation = values["validation.json"];
  if (candidate.release_state !== "UNRELEASED" || catalog.authoritative !== false || validation.outcome !== "PASS") throw new Error("CARRIER_CANNOT_SELF_APPROVE");
  if (!Number.isInteger(candidate.data_year) || `${String(candidate.data_year).padStart(4, "0")}-01-01` !== start || candidate.retrieved_at !== manifest.created_at) throw new Error("CANDIDATE_IDENTITY_MISMATCH");
  await validateStormCandidate(candidate, parseCapturedObject(artifacts["candidate.json"] as string), validation, parseCapturedObject(artifacts["validation.json"] as string));
  if (!same(catalog, expectedCatalog(candidate, validation, start as string))) throw new Error("CATALOG_MISMATCH");
  // One bundle per (month, part) the records produce, in order (the resolver caps a bundle at 128 members).
  const groups = stormMonthGroups(candidate.observations);
  if (!groups.length || !Array.isArray(evidence.entries) || evidence.entries.length !== groups.length) throw new Error("EVIDENCE_CLOSURE_INVALID");
  for (let i = 0; i < groups.length; i++) {
    const [month, part, records] = groups[i], entry = evidence.entries[i], bundle = entry.bundle;
    if (!Number.isInteger(entry.month) || !Number.isInteger(entry.part) || entry.month !== month || entry.part !== part) throw new Error("SERIES_EVIDENCE_MISMATCH");
    const expectedRef = { ref: monthRef(start as string, month, part, candidate.candidate_id), kind: "dataset", bundle_ref: bundle.bundle_id };
    if (!same(entry.evidence_ref, expectedRef) || !same(bundle.evidence_refs, [expectedRef, ...records.map(r => ({ ref: r.evidence_ref, kind: "record", bundle_ref: bundle.bundle_id }))]) || bundle.evidence_refs.length > 128) throw new Error("MEASUREMENT_EVIDENCE_MISMATCH");
    if (!same(bundle.checksums, { candidate: candidate.candidate_id, validation: validation.receipt_digest }) || !same(bundle.source_records, [...new Set(records.map(r => r.page_digest))].sort(codepointOrder))
        || entry.verification_history.subject_ref !== expectedRef.ref) throw new Error("BUNDLE_CONTENT_BINDING_MISMATCH");
  }
  return { manifest: manifest as StormPackage["manifest"], candidate, catalog: catalog as StormCatalog, evidence, validation };
}

export function stormEventsGate(pkg: StormPackage, decision: Obj | null, now: string): string {
  return releaseGate(pkg, decision, now, STORM_EVENTS_DECISION_PROFILE, STORM_EVENTS_SELF_RELEASE_LICENSES);
}

export async function stormEventsNegative(reason: string, now: string, outcome = "ABSTAIN"): Promise<StormResponse> {
  const envelope = { id: "storm-events:" + reason.toLowerCase(), version: "kfm-storm-events-v1", issued_at: now, outcome, reason_code: reason, evidence_refs: [], policy_state: "withheld", freshness: "unknown", correction_state: "unknown" };
  return { envelope: { ...envelope, spec_hash: await digest(canonical(envelope)) } };
}

export async function projectStormEvents(pkg: StormPackage, decision: Obj | null, view: string, now: string, month: number | null = null): Promise<StormResponse> {
  const reason = stormEventsGate(pkg, decision, now); if (reason !== "ELIGIBLE") return stormEventsNegative(reason, now);
  if (!["bootstrap", "layers", "evidence"].includes(view)) return stormEventsNegative("ROUTE_NOT_FOUND", now);
  const selected = pkg.evidence.entries.filter(e => month === null || e.month === month); if (!selected.length) return stormEventsNegative("EVIDENCE_NOT_FOUND", now);
  for (const entry of selected) if (!await verified(entry as unknown as Entry, now)) return stormEventsNegative("EVIDENCE_UNRESOLVED", now);
  const refs = selected.map(e => e.evidence_ref), months = new Set(selected.map(e => e.month)), candidate = pkg.candidate;
  const observations = candidate.observations.filter(r => months.has(Number(r.begin_local.slice(5, 7))));
  // The age of the NCEI file vintage is the only clock a historical file has.
  const age = (Math.floor(time(now) / 86400000) * 86400000 - day(candidate.vintage_created)) / 86400000;
  const fresh = age <= candidate.stale_after_days ? "current" : "stale-accepted";
  const precision = { spatial: { representation: "county or forecast zone; report points where present", resolution: "NCEI county/zone FIPS; begin and end coordinates in EPSG:4326 when reported",
      accuracy: "Report points, not a path, footprint or area; selection by NCEI STATE_FIPS, not a spatial join", generalization_applied: false },
    temporal: { granularity: "Event begin and end in reported local time; UTC only when the zone token carries an offset", observation_interval: { start: pkg.manifest.start, end: pkg.manifest.end }, freshness_class: fresh },
    attribute: { measures: { damage_property_usd: "nominal event-year USD", damage_crops_usd: "nominal event-year USD" },
      classification_granularity: "NCEI event types as reported; damage, magnitude and F/EF scale kept as source strings; blank damage is unreported, never zero; narratives excluded" },
    evidence_refs: refs, transform_receipt_refs: ["kfm://receipt/validation/" + String(pkg.validation.receipt_digest).split(":")[1]] };
  const envelope = { id: "storm-events:" + view, version: "kfm-storm-events-v1", issued_at: now, outcome: "ANSWER", reason_code: "RELEASED_SNAPSHOT", evidence_refs: refs, policy_state: "approved_snapshot", freshness: fresh, correction_state: "ACTIVE", precision_actually_used: precision };
  const common = { package_id: pkg.manifest.package_id, source_id: SOURCE_ID, coverage: candidate.coverage, data_year: candidate.data_year, source_file: candidate.source_file,
    vintage_created: candidate.vintage_created, retrieved_at: candidate.retrieved_at, reviewed_at: decision!.reviewed_at, released_at: decision!.released_at,
    approval_expires_at: decision!.expires_at, stale_after_days: candidate.stale_after_days, correction_state: "ACTIVE", attribution: ATTRIBUTION, life_safety: "not_for_life_safety" };
  const sortedMonths = [...months].sort((a, b) => a - b);
  const data = view === "bootstrap" ? { ...common, layers: [{ id: "noaa-storm-events-ks", title: "Reviewed NOAA Storm Events, Kansas", evidence_eligible: true }], observation_count: observations.length, months: sortedMonths }
    : view === "layers" ? { ...common, dataset: { ...pkg.catalog.dataset, scope: "data_year" },
        selection: { months: sortedMonths, observation_count: observations.length, event_types: eventTypes(observations), latest_event_date: latestDate(observations) }, observations }
    : { ...common, entries: selected.map(({ month: m, part, evidence_ref, bundle, verification_history }) => ({ month: m, part, evidence_ref, bundle, verification_history })) };
  return { envelope: { ...envelope, spec_hash: await digest(canonical(envelope)) }, data };
}
