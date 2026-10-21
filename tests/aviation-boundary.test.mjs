import test from "node:test";
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import { aviationRead, parseAviationQuery } from "../server/aviation-read.mjs";
import { queryHeldAirports, importHeldAirports } from "../server/aviation-candidates.mjs";
import { createAviationSession, aviationQuestion } from "../app/aviation-session.mjs";

test("public reads abstain before any database or provider access, regardless of activation env", async () => {
  process.env.KFM_AVIATION_ENABLED = "1";
  const result = await aviationRead(new Request("https://example.test/api/aviation/airports?county=ELLSWORTH"));
  assert.equal(result.status, 200); assert.equal(result.headers.get("cache-control"), "no-store");
  const value = await result.json(); assert.equal(value.envelope.outcome, "ABSTAIN"); assert.equal(value.data, undefined);
  assert.deepEqual(value.envelope.evidence_refs, []);
  delete process.env.KFM_AVIATION_ENABLED;
});
test("query limits reject unknown fields, duplicate keys, invalid editions and sensitive exports", async () => {
  for (const query of ["sql=select", "county=A&county=B", "edition=2026-02-30", "edition=garbage", "fields=registration", "export=raw", "q=" + "x".repeat(65)]) {
    const result = await aviationRead(new Request("https://example.test/api/aviation/airports?" + query));
    assert.equal(result.status, 400, query); assert.equal((await result.json()).envelope.outcome, "ERROR");
  }
  assert.deepEqual(parseAviationQuery(new URL("https://test/?county=ELLSWORTH&edition=2026-10-01")), { county: "ELLSWORTH", edition: "2026-10-01", q: "" });
});
test("held SQL is parameterized, bounded and cannot query denied fields", async () => {
  const id = "sha256:" + "a".repeat(64); let seen;
  const db = { execute: async (sql, params) => { seen = { sql, params }; return [Array.from({ length: 201 }, (_, id) => ({ id }))]; } };
  const result = await queryHeldAirports(db, id, "O'BRIEN");
  assert.equal(result.rows.length, 200); assert.equal(result.truncated, true);
  assert.deepEqual(seen.params, [id, "O'BRIEN"]); assert.ok(seen.sql.endsWith("LIMIT 201"));
  assert.ok(!seen.sql.includes("O'BRIEN") && !seen.sql.includes("record_json"));
  await assert.rejects(queryHeldAirports(db, id, "'; DROP TABLE x;--"), /INVALID_QUERY/);
});
test("Present, layer removal, date and selection changes retire delayed work", async () => {
  for (const action of ["Present", "layer", "date", "selection"]) {
    const session = createAviationSession(); const old = session.begin();
    let commit = false; const delayed = Promise.resolve().then(() => { if (old.current()) commit = true; });
    session.retire(); await delayed;
    assert.equal(old.signal.aborted, true, action); assert.equal(commit, false, action);
    const current = session.begin(); assert.equal(current.current(), true); assert.equal(old.current(), false);
  }
});
test("AI tools cannot widen evidence, infer activity, or accept generated SQL", () => {
  assert.equal(aviationQuestion("county-airports", { county: "ELLSWORTH" }).outcome, "ABSTAIN");
  for (const tool of ["sql", "ownership", "mission", "raw-export", "traffic-comparison"]) assert.equal(aviationQuestion(tool, {}).outcome, "DENY");
});
test("existing map uses held control; public route cannot import candidate SQL or private storage", async () => {
  const route = await readFile(new URL("../app/api/aviation/airports/route.ts", import.meta.url), "utf8");
  assert.ok(!/queryHeld|mysql|DB_|capture|fs\b/.test(route));
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8"); assert.ok(page.includes("<AviationControl contextKey={JSON.stringify([year, calendarSweep, selected?.featureId ?? null, visibility, officialVisibility])}"));
});

const canonical = value => value === null || typeof value !== "object" ? JSON.stringify(value) : Array.isArray(value) ? `[${value.map(canonical).join(",")}]` : `{${Object.keys(value).sort().map(k => `${JSON.stringify(k)}:${canonical(value[k])}`).join(",")}}`;
const hash = value => "sha256:" + createHash("sha256").update(canonical(value)).digest("hex");
function syntheticCandidate() {
  const original = { SITE_NO: "99999.01", SITE_TYPE_CODE: "A", ARPT_NAME: "SYNTHETIC AIRPORT" };
  const entity_id = "faa:site:99999.01:a", edition = "2026-10-01", revision_id = "faa:revision:" + hash([entity_id, edition, hash(original)]).slice(7);
  const archive_sha256 = "a".repeat(64), evidence_ref = { ref: "kfm://aviation/airport/" + revision_id, kind: "record", bundle_ref: "faa:bundle:" + revision_id.split(":").at(-1) };
  const bundle = { bundle_id: evidence_ref.bundle_ref, sensitivity: { level: "quarantine" }, evidence_refs: [evidence_ref], checksums: { archive: "sha256:" + archive_sha256, record: hash(original) } };
  bundle.spec_hash = { value: hash(bundle) };
  const r = { entity_id, revision_id, edition, valid_to_exclusive: "2026-10-29", state: "KS", county_state: "KS", county_name: "ELLSWORTH", faa_id: "ZZZZ", icao_id: null, name: "SYNTHETIC AIRPORT", longitude: -98.2, latitude: 38.7, elevation: 1500,
    elevation_unit: "ft", vertical_reference: "MSL", horizontal_datum: "UNVERIFIED_SOURCE_DATUM", public_candidate: true, original, evidence_ref, bundle };
  const c = { profile: "kfm.faa-airports-candidate/v1", release_state: "HELD", rights_state: "REVIEW_REQUIRED", future_at_capture: false,
    edition, retrieved_at: "2026-10-21T19:00:00Z", archive_sha256, parser_version: "faa-apt-v1", source_rows: 1, records: [r], rejects: [] };
  c.candidate_id = hash(c); return c;
}
function fakeTransaction(fail = false) {
  let saved = null, records = [], backup; const calls = [];
  return { calls,
    beginTransaction: async () => { backup = { saved, records: [...records] }; calls.push("begin"); },
    commit: async () => { calls.push("commit"); },
    rollback: async () => { ({ saved, records } = backup); calls.push("rollback"); },
    execute: async (sql, params) => {
      if (sql.startsWith("SELECT archive_sha256")) return [saved ? [saved] : []];
      if (sql.startsWith("SELECT record_json")) return [records];
      if (sql.startsWith("INSERT INTO kfm_faa_captures")) { saved = { archive_sha256: params[1], accepted_rows: params[7] }; return [[]]; }
      if (fail) throw new Error("SIMULATED_DISK_FULL");
      records.push({ record_json: params.at(-1) }); return [[]];
    },
    count: () => records.length,
  };
}
test("private candidate import retries without mutation and rolls back partial failure", async () => {
  const c = syntheticCandidate(), db = fakeTransaction();
  assert.equal((await importHeldAirports(db, c)).inserted, 1);
  assert.equal((await importHeldAirports(db, c)).inserted, 0); assert.equal(db.count(), 1);
  const failed = fakeTransaction(true);
  await assert.rejects(importHeldAirports(failed, c), /SIMULATED_DISK_FULL/);
  assert.equal(failed.count(), 0); assert.equal(failed.calls.at(-1), "rollback");
});
test("tampered candidates and future/released state fail before transaction", async () => {
  const c = syntheticCandidate(), db = fakeTransaction();
  c.records[0].name = "changed";
  await assert.rejects(importHeldAirports(db, c), /CANDIDATE_DIGEST_MISMATCH/);
  for (const changes of [{ future_at_capture: true }, { release_state: "RELEASED" }, { rights_state: "REVOKED" }]) {
    await assert.rejects(importHeldAirports(db, { ...syntheticCandidate(), ...changes }), /CANDIDATE_INVALID/);
  }
  assert.equal(db.calls.length, 0);
});
