/** Reviewed snapshot carrier. This module never acquires or approves source data. */
export const WATER_PACKAGE_LIMIT = 8 * 1024 * 1024;
const NAMES = ["candidate.json", "catalog.json", "evidence.json", "validation.json"] as const;
const DIGEST = /^sha256:[a-f0-9]{64}$/;
type Obj = Record<string, unknown>;
export type WaterStation = { id: string; name: string; geometry: { type: "Point"; coordinates: [number, number] }; page_digest: string; retrieved_at: string; horizontal_accuracy: unknown; original_horizontal_datum: unknown; provider_revision_at: unknown };
export type WaterObservation = { id: string; station_id: string; observed_at: string; provider_revision_at: string; retrieved_at: string; value: number | null; unit: string; provisional: boolean; qualifiers: string[]; evidence_ref: string; page_digest: string };
type WaterCandidate = { candidate_id: string; start: string; end: string; retrieved_at: string; coverage: string; stale_after_seconds: number; stations: WaterStation[]; observations: WaterObservation[]; release_state: string };
type Ref = { ref: string; kind: string; bundle_ref: string };
type Bundle = { bundle_id: string; evidence_refs: Ref[]; rights: { license: string }; sensitivity: { level: string }; spec_hash: { value: string }; checksums: Obj; source_records: string[]; citations: string[] } & Obj;
type History = { subject_ref: string; spec_hash: string; events: ({ event_id: string; event_type: string; state: string; effective_at: string; recorded_at: string; relates_to_event_id?: string } & Obj)[] } & Obj;
export type Entry = { station_id: string; evidence_ref: Ref; bundle: Bundle; verification_history: History };
export type WaterPackage = { manifest: Obj & { package_id: string; candidate_id: string; start: string; end: string; created_at: string; rollback_target: string | null }; candidate: WaterCandidate; evidence: { entries: Entry[] }; validation: Obj };
export type WaterResponse = { envelope: Obj & { outcome: string; reason_code: string }; data?: Obj & { stations?: WaterStation[]; observations?: WaterObservation[]; entries?: Entry[] } };
export function object(value: unknown): Obj { if (!value || typeof value !== "object" || Array.isArray(value)) throw new Error("OBJECT_REQUIRED"); return value as Obj; }
export const without = (value: Obj, key: string) => Object.fromEntries(Object.entries(value).filter(([name]) => name !== key));
export function canonical(value: unknown): string {
  if (value === null || typeof value === "string" || typeof value === "boolean" || typeof value === "number" && Number.isFinite(value)) return JSON.stringify(value);
  if (Array.isArray(value)) return `[${value.map(canonical).join(",")}]`;
  const source = object(value);
  return `{${Object.keys(source).sort().map(key => `${JSON.stringify(key)}:${canonical(source[key])}`).join(",")}}`;
}
export async function digest(text: string): Promise<string> { return "sha256:" + Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(text))), b => b.toString(16).padStart(2, "0")).join(""); }
export function time(value: unknown): number {
  const match = typeof value === "string" && /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})(?:\.\d{1,6})?Z$/.exec(value);
  if (!match || Number(match[1]) === 0) throw new Error("TIME_INVALID");
  const instant = Date.parse(value as string);
  if (!Number.isFinite(instant)) throw new Error("TIME_INVALID");
  // Date.parse normalizes impossible dates such as September 31; release times must not.
  const parsed = new Date(instant);
  if (parsed.getUTCFullYear() !== Number(match[1]) || parsed.getUTCMonth() + 1 !== Number(match[2])
      || parsed.getUTCDate() !== Number(match[3]) || parsed.getUTCHours() !== Number(match[4])
      || parsed.getUTCMinutes() !== Number(match[5]) || parsed.getUTCSeconds() !== Number(match[6])) throw new Error("TIME_INVALID");
  return instant;
}
export function approvalRemainingMs(expiry: unknown, nowMs: number): number {
  try {
    const remaining = time(expiry) - nowMs;
    return Number.isFinite(remaining) && remaining > 0 ? remaining : 0;
  } catch {
    return 0;
  }
}
export function same(a: unknown, b: unknown) { return canonical(a) === canonical(b); }

// Captured JSON uses Python json.dumps, not RFC 8785/JCS. Keep numeric tokens
// losslessly: 1.0, 1e-07 and -0.0 must not become 1, 1e-7 and 0 in an identity.
class CapturedNumber { constructor(readonly token: string) {} }
export type CapturedValue = null | boolean | string | CapturedNumber | CapturedValue[] | { [key: string]: CapturedValue };
export type CapturedObject = { [key: string]: CapturedValue };
export function capturedObject(value: CapturedValue): CapturedObject {
  if (!value || typeof value !== "object" || Array.isArray(value) || value instanceof CapturedNumber) throw new Error("OBJECT_REQUIRED");
  return value;
}
export function codepointOrder(a: string, b: string): number {
  const left = Array.from(a), right = Array.from(b);
  for (let i = 0; i < Math.min(left.length, right.length); i++) {
    const difference = left[i].codePointAt(0)! - right[i].codePointAt(0)!;
    if (difference) return difference;
  }
  return left.length - right.length;
}
export function capturedCanonical(value: CapturedValue, omit?: string): string {
  if (value instanceof CapturedNumber) return value.token;
  if (value === null || typeof value === "string" || typeof value === "boolean") return JSON.stringify(value);
  if (Array.isArray(value)) return `[${value.map(item => capturedCanonical(item)).join(",")}]`;
  return `{${Object.keys(value).filter(key => key !== omit).sort(codepointOrder).map(key => `${JSON.stringify(key)}:${capturedCanonical(value[key])}`).join(",")}}`;
}
function pythonFloatToken(value: number): string {
  if (value === 0) return Object.is(value, -0) ? "-0.0" : "0.0";
  const [mantissa, exponent = "0"] = Math.abs(value).toString().split("e");
  let digits = mantissa.replace(".", ""), magnitude = Number(exponent) + (mantissa.includes(".") ? mantissa.indexOf(".") : mantissa.length) - 1;
  while (digits.startsWith("0")) { digits = digits.slice(1); magnitude--; }
  digits = digits.replace(/0+$/, "");
  const sign = value < 0 ? "-" : "";
  if (magnitude < -4 || magnitude >= 16) return `${sign}${digits[0]}${digits.length > 1 ? "." + digits.slice(1) : ""}e${magnitude < 0 ? "-" : "+"}${String(Math.abs(magnitude)).padStart(2, "0")}`;
  const point = magnitude + 1;
  return sign + (point <= 0 ? "0." + "0".repeat(-point) + digits : point >= digits.length ? digits + "0".repeat(point - digits.length) + ".0" : digits.slice(0, point) + "." + digits.slice(point));
}
export function parseCapturedObject(text: string): CapturedObject {
  // The producer writes compact, sorted artifacts. Only that representation is
  // admitted; numeric aliases are rejected rather than silently recanonicalized.
  // Integer tokens remain exact even when they exceed JavaScript's safe range.
  let cursor = 0;
  const number = /-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?/y;
  function string(): string {
    const start = cursor++;
    while (cursor < text.length && text[cursor] !== '"') { if (text[cursor] === "\\") cursor++; cursor++; }
    if (cursor >= text.length) throw new Error("INVALID_JSON");
    const value = JSON.parse(text.slice(start, ++cursor)) as string;
    for (let i = 0; i < value.length; i++) {
      const unit = value.charCodeAt(i);
      if (unit >= 0xd800 && unit <= 0xdbff) {
        const next = value.charCodeAt(++i);
        if (!(next >= 0xdc00 && next <= 0xdfff)) throw new Error("INVALID_JSON_UNICODE");
      } else if (unit >= 0xdc00 && unit <= 0xdfff) throw new Error("INVALID_JSON_UNICODE");
    }
    return value;
  }
  function read(depth: number): CapturedValue {
    if (depth > 32) throw new Error("JSON_DEPTH_LIMIT");
    const char = text[cursor];
    if (char === " " || char === "\t" || char === "\r" || char === "\n") throw new Error("CAPTURED_JSON_NOT_CANONICAL");
    if (char === '"') return string();
    if (char === "{") {
      cursor++;
      const value: CapturedObject = Object.create(null);
      if (text[cursor] === "}") { cursor++; return value; }
      while (true) {
        if (text[cursor] !== '"') throw new Error("CAPTURED_JSON_NOT_CANONICAL");
        const key = string();
        if (key.length > 256 || Object.hasOwn(value, key)) throw new Error("DUPLICATE_JSON_KEY");
        if (text[cursor++] !== ":") throw new Error("INVALID_JSON");
        value[key] = read(depth + 1);
        const delimiter = text[cursor++];
        if (delimiter === "}") return value;
        if (delimiter !== ",") throw new Error("INVALID_JSON");
      }
    }
    if (char === "[") {
      cursor++;
      const values: CapturedValue[] = [];
      if (text[cursor] === "]") { cursor++; return values; }
      while (true) {
        values.push(read(depth + 1));
        const delimiter = text[cursor++];
        if (delimiter === "]") return values;
        if (delimiter !== ",") throw new Error("INVALID_JSON");
      }
    }
    for (const [token, value] of [["null", null], ["true", true], ["false", false]] as const) {
      if (text.startsWith(token, cursor)) { cursor += token.length; return value; }
    }
    number.lastIndex = cursor;
    const match = number.exec(text);
    if (!match || match[0].length > 128 || !Number.isFinite(Number(match[0]))) throw new Error("INVALID_JSON_NUMBER");
    const token = match[0];
    cursor = number.lastIndex;
    // Integer tokens need no Number conversion. Floats must use the producer's
    // shortest spelling and exponent thresholds, including two-digit exponents.
    if (token === "-0" || /[.eE]/.test(token) && token !== pythonFloatToken(Number(token))) throw new Error("CAPTURED_JSON_NOT_CANONICAL");
    return new CapturedNumber(token);
  }
  const value = capturedObject(read(0));
  if (cursor !== text.length || capturedCanonical(value) !== text) throw new Error("CAPTURED_JSON_NOT_CANONICAL");
  return value;
}
export function microseconds(value: unknown): bigint {
  time(value);
  const stamp = value as string, fraction = /\.(\d{1,6})Z$/.exec(stamp)?.[1] ?? "";
  return BigInt(Date.parse(stamp.slice(0, 19) + "Z")) * 1000n + BigInt(fraction.padEnd(6, "0"));
}
async function validateWaterIdentities(candidate: WaterCandidate, captured: CapturedObject, validation: Obj, capturedValidation: CapturedObject) {
  if (await digest(capturedCanonical(captured, "candidate_id")) !== candidate.candidate_id) throw new Error("CANDIDATE_DIGEST_MISMATCH");
  const revisions = object(candidate).revision_history;
  if (!Array.isArray(revisions) || revisions.length > 4000) throw new Error("OBSERVATION_COUNT_INVALID");
  const history = new Map<string, WaterObservation & Obj>(), start = microseconds(candidate.start), end = microseconds(candidate.end), retrieved = microseconds(candidate.retrieved_at);
  for (const field of ["revision_history", "observations"] as const) {
    const records = field === "revision_history" ? revisions : candidate.observations;
    const capturedRecords = captured[field];
    if (!Array.isArray(capturedRecords) || capturedRecords.length !== records.length) throw new Error("OBSERVATION_COUNT_INVALID");
    for (let i = 0; i < records.length; i++) {
      const record = object(records[i]) as WaterObservation & Obj;
      if (await digest(capturedCanonical(capturedObject(capturedRecords[i]), "record_digest")) !== record.record_digest) throw new Error("OBSERVATION_DIGEST_MISMATCH");
      if (!candidate.stations.some(station => station.id === record.station_id) || typeof record.time_series_id !== "string" || !record.time_series_id.length || record.time_series_id.length > 256
          || record.parameter_code !== "00060" || record.unit !== "ft^3/s" || record.value !== null && (!Number.isFinite(record.value) || Math.abs(record.value) > 1e9)) throw new Error("OBSERVATION_INVALID");
      const identity = (await digest(canonical([record.station_id, record.time_series_id, "00060", record.observed_at]))).slice(7);
      if (record.id !== "kfm:flow:" + identity || record.evidence_ref !== "kfm:evidence:flow:" + identity) throw new Error("OBSERVATION_IDENTITY_MISMATCH");
      const observed = microseconds(record.observed_at), revised = microseconds(record.provider_revision_at), recordRetrieved = microseconds(record.retrieved_at);
      if (!(start <= observed && observed <= end && observed <= revised && revised <= recordRetrieved && recordRetrieved <= retrieved)) throw new Error("OBSERVATION_TIME_MISMATCH");
      if (!["P", "Provisional", "A", "Approved"].includes(record.approval_status as string) || record.provisional !== ["P", "Provisional"].includes(record.approval_status as string)) throw new Error("PROVISIONAL_STATUS_MISMATCH");
      if (field === "revision_history") {
        const key = canonical([record.id, record.provider_revision_at]);
        if (history.has(key)) throw new Error("DUPLICATE_REVISION");
        history.set(key, record);
      }
    }
  }
  const latest = new Map<string, WaterObservation & Obj>();
  const orderedHistory = [...history.values()].sort((a, b) => {
    const left = microseconds(a.provider_revision_at), right = microseconds(b.provider_revision_at);
    return left < right ? -1 : left > right ? 1 : codepointOrder(a.record_digest as string, b.record_digest as string);
  });
  for (const record of orderedHistory) latest.set(record.id, record);
  const observations = [...latest.values()].sort((a, b) => codepointOrder(a.station_id, b.station_id) || codepointOrder(a.observed_at, b.observed_at) || codepointOrder(a.id, b.id));
  if (!same(candidate.observations, observations)) throw new Error("LATEST_REVISION_MISMATCH");
  if (await digest(capturedCanonical(capturedValidation, "receipt_digest")) !== validation.receipt_digest) throw new Error("VALIDATION_RECEIPT_INVALID");
  const expected = { profile: "kfm.water-pilot-validation/v1", candidate_id: candidate.candidate_id, outcome: "PASS", observations: candidate.observations.length,
    review_required: true, promotion_authorized: false, release_authorized: false, publication_authorized: false };
  if (!same(validation, { ...expected, receipt_digest: await digest(canonical(expected)) })) throw new Error("VALIDATION_RECEIPT_MISMATCH");
}
export function parseWaterJson(text: string): unknown {
  // Linear duplicate-key/depth guard, followed by the platform JSON grammar.
  const stack: { keys: Set<string> | null; key: boolean }[] = [];
  for (let i = 0; i < text.length; i++) {
    const char = text[i];
    if (char === '"') {
      const start = i++;
      while (i < text.length && text[i] !== '"') { if (text[i] === "\\") i++; i++; }
      if (i >= text.length) throw new Error("INVALID_JSON");
      const frame = stack.at(-1);
      if (frame?.keys && frame.key) { const key = JSON.parse(text.slice(start, i + 1)) as string; if (key.length > 256 || frame.keys.has(key)) throw new Error("DUPLICATE_JSON_KEY"); frame.keys.add(key); frame.key = false; }
    } else if (char === "{" || char === "[") {
      stack.push({ keys: char === "{" ? new Set() : null, key: char === "{" });
      if (stack.length > 32) throw new Error("JSON_DEPTH_LIMIT");
    } else if (char === "}" || char === "]") stack.pop();
    else if (char === "," && stack.at(-1)?.keys) stack.at(-1)!.key = true;
  }
  return JSON.parse(text) as unknown;
}
export async function parseWaterPackage(text: string): Promise<WaterPackage> {
  if (!text || new TextEncoder().encode(text).length > WATER_PACKAGE_LIMIT) throw new Error("PACKAGE_LIMIT");
  const snapshot = object(parseWaterJson(text));
  if (!same(Object.keys(snapshot).sort(), ["artifacts", "manifest"])) throw new Error("SNAPSHOT_SHAPE_INVALID");
  const manifest = object(snapshot.manifest), artifacts = object(snapshot.artifacts), hashes = object(manifest.artifacts);
  if (!same(Object.keys(manifest).sort(), ["artifacts", "candidate_id", "created_at", "end", "package_id", "profile", "review_requirements", "rollback_target", "source_id", "start"]) || manifest.profile !== "kfm.water-snapshot/v1" || manifest.source_id !== "usgs-nwis") throw new Error("MANIFEST_PROFILE_INVALID");
  if (!same(manifest.review_requirements, ["source_admission", "rights", "sensitivity", "policy", "independent_review", "release"]) || manifest.rollback_target !== null && (typeof manifest.rollback_target !== "string" || !DIGEST.test(manifest.rollback_target))) throw new Error("MANIFEST_PROFILE_INVALID");
  if (await digest(canonical(without(manifest, "package_id"))) !== manifest.package_id) throw new Error("PACKAGE_DIGEST_MISMATCH");
  const interval = time(manifest.end) - time(manifest.start); if (interval <= 0 || interval > 86400000) throw new Error("SNAPSHOT_INTERVAL_INVALID"); time(manifest.created_at);
  if (!same(Object.keys(artifacts).sort(), [...NAMES].sort()) || !same(Object.keys(hashes).sort(), [...NAMES].sort())) throw new Error("ARTIFACT_CLOSURE_INVALID");
  const values: Record<string, Obj> = {};
  for (const name of NAMES) { const raw = artifacts[name]; if (typeof raw !== "string" || await digest(raw) !== hashes[name]) throw new Error("ARTIFACT_DIGEST_MISMATCH"); values[name] = object(parseWaterJson(raw)); if (values[name].candidate_id !== manifest.candidate_id) throw new Error("CANDIDATE_BINDING_MISMATCH"); }
  const candidate = values["candidate.json"] as WaterCandidate, evidence = values["evidence.json"] as { entries: Entry[] }, validation = values["validation.json"];
  if (candidate.release_state !== "UNRELEASED" || values["catalog.json"].authoritative !== false || validation.outcome !== "PASS") throw new Error("CARRIER_CANNOT_SELF_APPROVE");
  if (candidate.start !== manifest.start || candidate.end !== manifest.end || candidate.retrieved_at !== manifest.created_at || candidate.stale_after_seconds !== 7200) throw new Error("CANDIDATE_IDENTITY_MISMATCH");
  if (!Array.isArray(candidate.stations) || !same(candidate.stations.map(s => s.id).sort(), ["USGS-06892518", "USGS-07156900"]) || !Array.isArray(candidate.observations) || candidate.observations.length > 4000 || !Array.isArray(evidence.entries) || evidence.entries.length !== 2) throw new Error("STATION_SCOPE_INVALID");
  await validateWaterIdentities(candidate, parseCapturedObject(artifacts["candidate.json"] as string), validation, parseCapturedObject(artifacts["validation.json"] as string));
  for (const s of candidate.stations) { if (typeof s.name !== "string" || s.name.length > 256 || s.geometry.type !== "Point" || s.geometry.coordinates.length !== 2 || !s.geometry.coordinates.every(Number.isFinite) || Math.abs(s.geometry.coordinates[0]) > 180 || Math.abs(s.geometry.coordinates[1]) > 90) throw new Error("STATION_GEOMETRY_INVALID"); }
  for (const r of candidate.observations) { if (!candidate.stations.some(s => s.id === r.station_id) || r.unit !== "ft^3/s" || r.value !== null && (!Number.isFinite(r.value) || Math.abs(r.value) > 1e9) || time(r.observed_at) < time(candidate.start) || time(r.observed_at) > time(candidate.end)) throw new Error("OBSERVATION_INVALID"); }
  if (!same(evidence.entries.map(e => e.station_id).sort(), candidate.stations.map(s => s.id).sort())) throw new Error("STATION_EVIDENCE_MISMATCH");
  for (const entry of evidence.entries) {
    const station = candidate.stations.find(s => s.id === entry.station_id)!;
    const records = candidate.observations.filter(r => r.station_id === station.id), bundle = entry.bundle;
    const expectedRef = { ref: `kfm://water/station/${station.id}/${String(manifest.candidate_id).split(":")[1]}`, kind: "dataset", bundle_ref: bundle.bundle_id };
    if (!same(entry.evidence_ref, expectedRef) || !same(bundle.evidence_refs, [expectedRef, ...records.map(r => ({ ref: r.evidence_ref, kind: "measurement", bundle_ref: bundle.bundle_id }))]) || bundle.evidence_refs.length > 128) throw new Error("MEASUREMENT_EVIDENCE_MISMATCH");
    if (!same(bundle.checksums, { candidate: candidate.candidate_id, validation: validation.receipt_digest }) || !same(bundle.source_records, [...new Set([station.page_digest, ...records.map(r => r.page_digest)])].sort()) || entry.verification_history.subject_ref !== expectedRef.ref) throw new Error("BUNDLE_CONTENT_BINDING_MISMATCH");
  }
  return { manifest: manifest as WaterPackage["manifest"], candidate, evidence, validation };
}
const REF_KEYS = ["source_admission_ref", "rights_ref", "sensitivity_ref", "policy_ref", "review_ref", "release_ref"];
// ADR-0044: licenses of admitted public sources whose owner may review and release the same package.
// Must match SELF_RELEASE_LICENSES in packages/policy-runtime/src/policy_runtime/core.py.
export const SELF_RELEASE_LICENSES: readonly string[] = ["U.S. Public Domain (USGS-authored data, 17 U.S.C. 105); provisional data subject to revision"];
type GatePackage = { manifest: { package_id: string; created_at: string }; evidence: { entries: { bundle: { rights: { license: string }; sensitivity: { level: string } } }[] } };
const selfReleaseEligible = (pkg: GatePackage, licenses: readonly string[]) => pkg.evidence.entries.length > 0 && pkg.evidence.entries.every(e => e.bundle.sensitivity.level === "public" && licenses.includes(e.bundle.rights.license));
export function waterGate(pkg: WaterPackage, decision: Obj | null, now: string): string {
  return releaseGate(pkg, decision, now, "kfm.water-release-decision/v1", SELF_RELEASE_LICENSES);
}
// The shared gate body; each family names its decision profile and its own self-release license list.
export function releaseGate(pkg: GatePackage, decision: Obj | null, now: string, profile: string, licenses: readonly string[]): string {
  if (!decision) return "REVIEW_REQUIRED";
  if (!same(Object.keys(decision).sort(), ["profile", "package_id", "decision", "reviewed_at", "released_at", "expires_at", "correction_state", "correction_ref", "reviewer", "releaser", ...REF_KEYS].sort())) return "RELEASE_METADATA_INVALID";
  if (decision.profile !== profile || decision.package_id !== pkg.manifest.package_id) return "RELEASE_BINDING_MISMATCH";
  if (decision.correction_state !== "ACTIVE") return "CORRECTION_HOLD";
  if (decision.correction_ref !== null || decision.decision !== "APPROVED") return "RELEASE_NOT_APPROVED";
  if (REF_KEYS.some(k => typeof decision[k] !== "string" || !/^kfm:\/\/[A-Za-z0-9._~:/-]{1,240}$/.test(decision[k] as string))) return "REVIEW_REFERENCE_MISSING";
  if (["reviewer", "releaser"].some(k => typeof decision[k] !== "string" || !(decision[k] as string).length || (decision[k] as string).length > 128)) return "INDEPENDENT_REVIEW_REQUIRED";
  if (decision.reviewer === decision.releaser && !selfReleaseEligible(pkg, licenses)) return "INDEPENDENT_REVIEW_REQUIRED";
  try { if (!(time(pkg.manifest.created_at) <= time(decision.reviewed_at) && time(decision.reviewed_at) <= time(decision.released_at) && time(decision.released_at) <= time(now) && time(now) < time(decision.expires_at))) return "RELEASE_TIME_INVALID"; } catch { return "RELEASE_TIME_INVALID"; }
  if (pkg.evidence.entries.some(e => e.bundle.sensitivity.level !== "public" || e.bundle.rights.license.toLowerCase().includes("review required"))) return "RIGHTS_OR_SENSITIVITY_HOLD";
  return "ELIGIBLE";
}
export async function waterNegative(reason: string, now: string, outcome = "ABSTAIN"): Promise<WaterResponse> {
  const envelope = { id: "water:" + reason.toLowerCase(), version: "kfm-water-v1", issued_at: now, outcome, reason_code: reason, evidence_refs: [], policy_state: "withheld", freshness: "unknown", correction_state: "unknown" };
  return { envelope: { ...envelope, spec_hash: await digest(canonical(envelope)) } };
}
export async function verified(entry: Entry, now: string) {
  const history = entry.verification_history, events = history.events;
  if (await digest(canonical(without(entry.bundle, "spec_hash"))) !== entry.bundle.spec_hash.value || await digest(canonical(without(history, "spec_hash"))) !== history.spec_hash || !Array.isArray(events) || events.length < 1 || events.length > 128) return false;
  let state = "UNKNOWN", previous = "", effective = -Infinity, recorded = -Infinity;
  const transitions: Record<string, string[]> = { UNKNOWN: ["VERIFIED"], ACTIVE: ["CORRECTED", "SUPERSEDED", "REVOKED"], CORRECTED: ["REVERIFIED", "SUPERSEDED", "REVOKED"], REVOKED: ["REVERIFIED"], SUPERSEDED: [] };
  const states: Record<string, string> = { VERIFIED: "ACTIVE", REVERIFIED: "ACTIVE", CORRECTED: "CORRECTED", SUPERSEDED: "SUPERSEDED", REVOKED: "REVOKED" };
  const seen = new Set<string>(); let current = "UNKNOWN";
  for (const event of events) {
    if (seen.has(event.event_id) || !transitions[state]?.includes(event.event_type) || states[event.event_type] !== event.state || previous && event.relates_to_event_id !== previous || time(event.effective_at) > time(event.recorded_at) || time(event.effective_at) < effective || time(event.recorded_at) < recorded) return false;
    seen.add(event.event_id); state = event.state; previous = event.event_id; effective = time(event.effective_at); recorded = time(event.recorded_at);
    if (effective <= time(now) && recorded <= time(now)) current = state;
  }
  return current === "ACTIVE";
}
export async function projectWater(pkg: WaterPackage, decision: Obj | null, view: string, now: string, stationId: string | null = null): Promise<WaterResponse> {
  const reason = waterGate(pkg, decision, now); if (reason !== "ELIGIBLE") return waterNegative(reason, now);
  if (!["bootstrap", "layers", "evidence"].includes(view)) return waterNegative("ROUTE_NOT_FOUND", now);
  const selected = pkg.evidence.entries.filter(e => !stationId || e.station_id === stationId); if (!selected.length) return waterNegative("EVIDENCE_NOT_FOUND", now);
  for (const entry of selected) if (!await verified(entry, now)) return waterNegative("EVIDENCE_UNRESOLVED", now);
  const refs = selected.map(e => e.evidence_ref), ids = new Set(selected.map(e => e.station_id)), candidate = pkg.candidate;
  const observations = candidate.observations.filter(r => ids.has(r.station_id));
  // A timestamp with no discharge value cannot make a measurement current.
  const measured = observations.filter(r => r.value !== null);
  const latest = Math.max(...measured.map(r => time(r.observed_at))), freshness = !measured.length ? "unknown" : time(now) - latest > candidate.stale_after_seconds * 1000 ? "stale-accepted" : "current";
  const precision = { spatial: { representation: "point", resolution: "Provider station coordinates, EPSG:4326", accuracy: "See station horizontal accuracy metadata; no inferred positional accuracy", generalization_applied: false }, temporal: { granularity: "Provider observation instants", observation_interval: { start: pkg.manifest.start, end: pkg.manifest.end }, freshness_class: freshness }, attribute: { measure: "Discharge", unit: "ft^3/s", significant_precision: 0, classification_granularity: "Provider-reported values; no additional significant-figure guarantee" }, evidence_refs: refs, transform_receipt_refs: ["kfm://receipt/validation/" + String(pkg.validation.receipt_digest).split(":")[1]] };
  const envelope = { id: "water:" + view, version: "kfm-water-v1", issued_at: now, outcome: "ANSWER", reason_code: "RELEASED_SNAPSHOT", evidence_refs: refs, policy_state: "approved_snapshot", freshness, correction_state: "ACTIVE", precision_actually_used: precision };
  const common = { package_id: pkg.manifest.package_id, source_id: "usgs-nwis", coverage: candidate.coverage, retrieved_at: candidate.retrieved_at, reviewed_at: decision!.reviewed_at, released_at: decision!.released_at, approval_expires_at: decision!.expires_at, stale_after_seconds: candidate.stale_after_seconds, correction_state: "ACTIVE", attribution: "U.S. Geological Survey. Provisional observations are subject to revision." };
  const data = view === "bootstrap" ? { ...common, layers: [{ id: "usgs-water-pilot", title: "Reviewed USGS discharge snapshot", evidence_eligible: true }], observation_count: observations.length } : view === "layers" ? { ...common, stations: candidate.stations.filter(s => ids.has(s.id)), observations } : { ...common, entries: selected.map(({ station_id, evidence_ref, bundle, verification_history }) => ({ station_id, evidence_ref, bundle, verification_history })) };
  return { envelope: { ...envelope, spec_hash: await digest(canonical(envelope)) }, data };
}
