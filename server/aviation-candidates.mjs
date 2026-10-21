/** Private operator import; no route, scheduler, approval or release capability. */
import { createHash } from "node:crypto";
const canonical = value => value === null || typeof value !== "object" ? JSON.stringify(value)
  : Array.isArray(value) ? `[${value.map(canonical).join(",")}]`
    : `{${Object.keys(value).sort().map(k => `${JSON.stringify(k)}:${canonical(value[k])}`).join(",")}}`;

export async function importHeldAirports(connection, candidate) {
  const hash = value => "sha256:" + createHash("sha256").update(canonical(value)).digest("hex");
  if (candidate?.profile !== "kfm.faa-airports-candidate/v1" || candidate.release_state !== "HELD"
      || candidate.rights_state !== "REVIEW_REQUIRED" || candidate.future_at_capture !== false
      || candidate.edition !== "2026-10-01" || !/^[a-f0-9]{64}$/.test(candidate.archive_sha256)
      || !/^sha256:[a-f0-9]{64}$/.test(candidate.candidate_id) || !Array.isArray(candidate.records)
      || candidate.records.length > 10000 || !Array.isArray(candidate.rejects)) throw new Error("CANDIDATE_INVALID");
  const { candidate_id, ...subject } = candidate;
  if (hash(subject) !== candidate_id) throw new Error("CANDIDATE_DIGEST_MISMATCH");
  const ids = new Set();
  for (const r of candidate.records) {
    if (!/^faa:revision:[a-f0-9]{64}$/.test(r.revision_id) || ids.has(r.revision_id) || !/^faa:site:\d{5}\.\d{0,3}:[achgbu]$/.test(r.entity_id)
        || r.edition !== candidate.edition || r.valid_to_exclusive !== "2026-10-29" || ![r.longitude, r.latitude].every(Number.isFinite)
        || r.longitude < -180 || r.longitude > 180 || r.latitude < -90 || r.latitude > 90 || r.elevation_unit !== "ft" || r.vertical_reference !== "MSL"
        || r.horizontal_datum !== "UNVERIFIED_SOURCE_DATUM" || r.bundle?.sensitivity?.level !== "quarantine"
        || r.evidence_ref?.bundle_ref !== r.bundle?.bundle_id || r.bundle.evidence_refs?.[0]?.ref !== r.evidence_ref?.ref
        || r.bundle.checksums?.archive !== "sha256:" + candidate.archive_sha256) throw new Error("CANDIDATE_INVALID");
    if (r.bundle.checksums.record !== hash(r.original) || r.revision_id !== "faa:revision:" + hash([r.entity_id, r.edition, hash(r.original)]).slice(7)) throw new Error("REVISION_DIGEST_MISMATCH");
    const { spec_hash, ...bundle } = r.bundle;
    if (spec_hash?.value !== "sha256:" + createHash("sha256").update(canonical(bundle)).digest("hex")) throw new Error("EVIDENCE_DIGEST_MISMATCH");
    ids.add(r.revision_id);
  }
  await connection.beginTransaction();
  try {
    // Same capture+candidate is immutable. No UPDATE/REPLACE/IGNORE on integrity-bearing rows.
    const [exists] = await connection.execute("SELECT archive_sha256,accepted_rows FROM kfm_faa_captures WHERE candidate_id=? FOR UPDATE", [candidate.candidate_id]);
    if (exists.length) {
      if (exists[0].archive_sha256 !== candidate.archive_sha256 || Number(exists[0].accepted_rows) !== candidate.records.length) throw new Error("CANDIDATE_COLLISION");
      const [stored] = await connection.execute("SELECT record_json FROM kfm_faa_airport_revisions WHERE candidate_id=? ORDER BY revision_id LIMIT 10001", [candidate.candidate_id]);
      const expected = [...candidate.records].sort((a, b) => a.revision_id.localeCompare(b.revision_id));
      if (stored.length !== expected.length || stored.some((r, i) => canonical(typeof r.record_json === "string" ? JSON.parse(r.record_json) : r.record_json) !== canonical(expected[i]))) throw new Error("CANDIDATE_INTEGRITY_FAILED");
      await connection.commit(); return { inserted: 0, release_state: "HELD" };
    }
    await connection.execute("INSERT INTO kfm_faa_captures (candidate_id,archive_sha256,edition,retrieved_at,source_publication_time,parser_version,source_rows,accepted_rows,rejected_rows,rights_state,release_state) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
      [candidate.candidate_id, candidate.archive_sha256, candidate.edition, candidate.retrieved_at, null, candidate.parser_version, candidate.source_rows, candidate.records.length, candidate.rejects.length, "REVIEW_REQUIRED", "HELD"]);
    for (const r of candidate.records) {
      await connection.execute("INSERT INTO kfm_faa_airport_revisions (candidate_id,revision_id,entity_id,edition,valid_to_exclusive,state,county_name,county_state,faa_id,icao_id,name,longitude,latitude,elevation_ft_msl,horizontal_datum,public_candidate,record_json) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        [candidate.candidate_id, r.revision_id, r.entity_id, r.edition, r.valid_to_exclusive, r.state, r.county_name, r.county_state, r.faa_id, r.icao_id, r.name, r.longitude, r.latitude, r.elevation, r.horizontal_datum, r.public_candidate, JSON.stringify(r)]);
    }
    await connection.commit(); return { inserted: candidate.records.length, release_state: "HELD" };
  } catch (error) { await connection.rollback(); throw error; }
}

/** Operator/test-only candidate query; NEVER imported by public routes or AI.
 * Requires an already-scoped transaction. Uses no dynamic identifiers or SQL.
 */
export async function queryHeldAirports(connection, candidateId, county) {
  if (!/^sha256:[a-f0-9]{64}$/.test(candidateId) || !/^[A-Z][A-Z .'-]{0,63}$/.test(county)) throw new Error("INVALID_QUERY");
  const [rows] = await connection.execute(
    "SELECT revision_id,entity_id,edition,faa_id,name,longitude,latitude,elevation_ft_msl FROM kfm_faa_airport_revisions WHERE candidate_id=? AND state='KS' AND county_state='KS' AND county_name=? AND public_candidate=TRUE ORDER BY revision_id LIMIT 201",
    [candidateId, county]);
  return { rows: rows.slice(0, 200), truncated: rows.length > 200, release_state: "HELD" };
}
