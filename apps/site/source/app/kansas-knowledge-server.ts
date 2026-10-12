import { env } from "cloudflare:workers";
import { getRawDb } from "../db";
import { canonicalKnowledge, knowledgeDigest, knowledgeQuery, KNOWLEDGE_PACKAGE_LIMIT, parseKnowledgePackage, publicKnowledgeRecord, validKnowledgeRelease, type KnowledgeRow } from "./kansas-knowledge";

type Statement = { bind(...values: unknown[]): Statement; first<T>(): Promise<T | null>; all<T>(): Promise<{ results: T[] }> };
type Db = { prepare(sql: string): Statement };
type Bucket = { get(key: string): Promise<{ size: number; arrayBuffer(): Promise<ArrayBuffer> } | null> };
type Release = Record<string, unknown> & { release_id: string; package_key: string; package_sha256: string; reviewed_at: string; released_at: string };
const HEADERS = { "Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff", "Vary": "Cookie" };
const COLUMNS = "record_id, release_id, kind, title, summary, location_label, geometry_role, time_start, time_end, source_ref, source_url, evidence_ref, rights_ref, sensitivity_ref, review_ref, correction_state, public_state, assertions_json";

async function envelope(reason: string, now: string, evidenceRefs: string[] = []) {
  const value = {
    id: `kansas-knowledge:${reason.toLowerCase()}`, version: "kfm-kansas-knowledge-v1", issued_at: now,
    outcome: reason === "RELEASED" ? "ANSWER" : reason === "STORAGE_UNAVAILABLE" ? "ERROR" : "ABSTAIN",
    reason_code: reason, evidence_refs: evidenceRefs, policy_state: reason === "RELEASED" ? "released" : "withheld",
    freshness: "historical", correction_state: reason === "RELEASED" ? "active" : "unknown",
  };
  return { ...value, spec_hash: await knowledgeDigest(new TextEncoder().encode(canonicalKnowledge(value))) };
}

function escapeLike(value: string) { return value.replace(/[\\%_]/g, "\\$&"); }

/** Injected stores make negative authorization and tampering behavior testable. */
export async function readKansasKnowledge(request: Request, db: Db, bucket: Bucket, now = new Date().toISOString()): Promise<Response> {
  const correlation = crypto.randomUUID(), start = Date.now();
  let result: { envelope: Awaited<ReturnType<typeof envelope>>; data?: unknown };
  let status = 200;
  try {
    let query;
    try { query = knowledgeQuery(request.url); }
    catch { status = 400; result = { envelope: await envelope("INVALID_QUERY", now) }; return Response.json(result, { status, headers: HEADERS }); }
    const release = await db.prepare("SELECT r.* FROM knowledge_active a JOIN knowledge_releases r ON r.release_id = a.release_id WHERE a.singleton = 1").first<Release>();
    if (!release) result = { envelope: await envelope("NO_APPROVED_KNOWLEDGE", now) };
    else if (!validKnowledgeRelease(release, Date.parse(now))) result = { envelope: await envelope("RELEASE_HELD", now) };
    else {
      const stored = await bucket.get(release.package_key);
      if (!stored || !Number.isSafeInteger(stored.size) || stored.size < 2 || stored.size > KNOWLEDGE_PACKAGE_LIMIT) throw new Error("PACKAGE_UNAVAILABLE");
      const bytes = new Uint8Array(await stored.arrayBuffer());
      if (bytes.length !== stored.size || await knowledgeDigest(bytes) !== release.package_sha256) throw new Error("PACKAGE_DIGEST_MISMATCH");
      const packageRecords = parseKnowledgePackage(bytes, release.release_id);
      const statement = query.kind === "record"
        ? db.prepare(`SELECT ${COLUMNS} FROM knowledge_public WHERE release_id = ? AND public_state = 'PUBLIC_SAFE' AND correction_state = 'ACTIVE' AND record_id = ? LIMIT 1`).bind(release.release_id, query.id)
        : db.prepare(`SELECT ${COLUMNS} FROM knowledge_public WHERE release_id = ? AND public_state = 'PUBLIC_SAFE' AND correction_state = 'ACTIVE' AND (title LIKE ? ESCAPE '\\' OR summary LIKE ? ESCAPE '\\') ORDER BY title, record_id LIMIT 21`).bind(release.release_id, `%${escapeLike(query.term)}%`, `%${escapeLike(query.term)}%`);
      const rows = (await statement.all<KnowledgeRow>()).results;
      const selected = rows.slice(0, query.kind === "record" ? 1 : 20);
      const records = selected.map(row => {
        const record = publicKnowledgeRecord(row), original = packageRecords.get(record.record_id);
        if (!original || canonicalKnowledge(original) !== canonicalKnowledge(record)) throw new Error("PROJECTION_MISMATCH");
        return record;
      });
      if (!records.length) result = { envelope: await envelope("RECORD_NOT_FOUND", now) };
      else result = { envelope: await envelope("RELEASED", now, [...new Set(records.map(record => record.evidence_ref))]),
        data: { release_id: release.release_id, reviewed_at: release.reviewed_at, released_at: release.released_at,
          records, has_more: query.kind === "search" && rows.length > 20 } };
    }
  } catch {
    status = 503;
    result = { envelope: await envelope("STORAGE_UNAVAILABLE", now) };
  }
  console.info(JSON.stringify({ event: "governed_read", component: "site-kansas-knowledge", build: "kfm-kansas-knowledge-v1",
    correlation_id: correlation, outcome: result.envelope.outcome, reason_code: result.envelope.reason_code, duration_ms: Date.now() - start }));
  return Response.json(result, { status, headers: { ...HEADERS, "X-KFM-Correlation-ID": correlation } });
}

export async function kansasKnowledgeRead(request: Request) {
  try {
    const bucket = env.BUCKET as Bucket | undefined;
    if (!bucket) throw new Error("BUCKET_UNAVAILABLE");
    return await readKansasKnowledge(request, getRawDb(), bucket);
  } catch {
    return Response.json({ envelope: await envelope("STORAGE_UNAVAILABLE", new Date().toISOString()) }, { status: 503, headers: HEADERS });
  }
}
